import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timezone
from urllib.parse import urljoin, urlparse

# =========================
# CONFIG
# =========================
BASE_URL = "https://alvarovalenzuela.substack.com"
ARCHIVE_URL = f"{BASE_URL}/archive"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# =========================
# HELPERS
# =========================
def clean_text(text):
    return re.sub(r"\s+", " ", text or "").strip()

def slug_from_url(url):
    path = urlparse(url).path.strip("/")
    return path.split("/")[-1] if path else ""

def is_valid_post_url(url):
    if not url.startswith(BASE_URL):
        return False

    path = urlparse(url).path.strip("/")

    if not path:
        return False

    if "/" in path:
        return False

    banned = {
        "archive", "about", "subscribe", "podcast",
        "publish", "account"
    }

    if path in banned:
        return False

    return True

def fetch(url):
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r

# =========================
# STEP 1 — ARCHIVE PARSING
# =========================
def extract_archive_entries():
    print("Fetching archive page...")

    html = fetch(ARCHIVE_URL).text
    soup = BeautifulSoup(html, "lxml")

    entries = []
    seen = set()

    for a in soup.find_all("a", href=True):
        full_url = urljoin(BASE_URL, a["href"])

        if not is_valid_post_url(full_url):
            continue

        if full_url in seen:
            continue
        seen.add(full_url)

        title = clean_text(a.get_text(" ", strip=True))
        slug = slug_from_url(full_url)

        if not title or not slug:
            continue

        entries.append({
            "post_title": title,
            "post_url": full_url,
            "slug": slug
        })

    print(f"Archive candidates found: {len(entries)}")
    return entries

# =========================
# STEP 2 — POST PARSING
# =========================
def parse_post(url):
    html = fetch(url).text
    soup = BeautifulSoup(html, "lxml")

    # Title
    h1 = soup.find("h1")
    post_title = clean_text(h1.get_text(" ", strip=True)) if h1 else None

    # Subtitle (best-effort)
    subtitle = None
    for tag in ["h2", "h3", "p"]:
        el = soup.find(tag)
        if el:
            txt = clean_text(el.get_text(" ", strip=True))
            if txt and txt != post_title:
                subtitle = txt
                break

    # Author
    author = None
    meta_author = soup.find("meta", attrs={"name": "author"})
    if meta_author and meta_author.get("content"):
        author = clean_text(meta_author["content"])

    # Date
    publish_date = None
    time_el = soup.find("time")
    if time_el:
        publish_date = time_el.get("datetime") or clean_text(time_el.get_text(" ", strip=True))

    # Content extraction
    content_node = (
        soup.find("article")
        or soup.find("div", class_=re.compile("body|markup", re.I))
        or soup.find("section")
    )

    if content_node:
        content_html = str(content_node)
        content_text = clean_text(content_node.get_text(" ", strip=True))
    else:
        content_html = None
        content_text = clean_text(soup.get_text(" ", strip=True))

    excerpt = content_text[:240] if content_text else None

    is_paywalled = (
        "subscribe to continue reading" in html.lower()
        or "paid subscribers" in html.lower()
    )

    # Date normalization
    year = None
    month = None
    if publish_date:
        try:
            dt = pd.to_datetime(publish_date, utc=True)
            publish_date = dt.isoformat()
            year = dt.year
            month = dt.month
        except:
            pass

    return {
        "source": "substack",
        "item_type": "essay",
        "publication_title": "Crónica de la crisis política chilena (2011-2023)",
        "author": author or "Álvaro Valenzuela",
        "post_title": post_title,
        "post_subtitle": subtitle,
        "post_url": url,
        "slug": slug_from_url(url),
        "publish_date": publish_date,
        "year": year,
        "month": month,
        "excerpt": excerpt,
        "content_text": content_text,
        "word_count": len(content_text.split()) if content_text else None,
        "is_paywalled": is_paywalled,
        "retrieved_at": datetime.now(timezone.utc).isoformat()
    }

# =========================
# STEP 3 — BUILD LEDGER
# =========================
def build_ledger():
    entries = extract_archive_entries()

    rows = []
    seen = set()

    for i, entry in enumerate(entries, start=1):
        url = entry["post_url"]

        if url in seen:
            continue
        seen.add(url)

        print(f"[{i}/{len(entries)}] Processing: {url}")

        try:
            row = parse_post(url)
            rows.append(row)
            time.sleep(1.2)

        except Exception as e:
            print(f"ERROR at {url}: {e}")

    df = pd.DataFrame(rows)
    df = df.drop_duplicates(subset=["post_url"])

    return df

# =========================
# STEP 4 — EXPORT
# =========================
def export(df):
    df.to_csv("alvaro_substack_ledger.csv", index=False, encoding="utf-8-sig")
    df.to_json("alvaro_substack_ledger.json", orient="records", force_ascii=False, indent=2)

    print("\nSaved:")
    print("- alvaro_substack_ledger.csv")
    print("- alvaro_substack_ledger.json")

# =========================
# MAIN
# =========================
if __name__ == "__main__":
    df = build_ledger()

    print(f"\nTotal posts: {len(df)}")

    if not df.empty:
        print("\nPreview:")
        print(df[[
            "post_title",
            "post_url",
            "publish_date",
            "word_count"
        ]].head(10).to_string(index=False))

    export(df)