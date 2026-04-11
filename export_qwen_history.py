"""
Export Qwen history and memory to local repository.

This script pulls:
1. Chat history from all projects
2. Settings and configuration
3. Debug logs (latest only, to minimize size)
4. OAuth metadata (without sensitive tokens)

Output structure:
qwen-export/
├── metadata.json          # Export summary and stats
├── config/
│   ├── settings.json      # Qwen settings
│   └── installation_id    # Installation ID
├── chats/
│   ├── {session-id}.json  # Chat conversations (one per session)
│   └── chat-index.json    # Index of all chats
├── debug/
│   └── {session-id}.json  # Debug logs (compact format)
└── projects/
    └── project-index.json # List of all projects

Run: python export_qwen_history.py
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

# Configuration
QWEN_DIR = Path.home() / ".qwen"
EXPORT_DIR = Path("qwen-export")
MAX_DEBUG_LOGS = 10  # Only export most recent debug logs per session


def clean_oauth_creds(data):
    """Remove sensitive token data from OAuth credentials."""
    cleaned = data.copy()
    if "access_token" in cleaned:
        cleaned["access_token"] = "[REDACTED]"
    if "refresh_token" in cleaned:
        cleaned["refresh_token"] = "[REDACTED]"
    return cleaned


def compact_jsonl_to_list(jsonl_file):
    """Convert JSONL file to list of compact JSON objects."""
    entries = []
    with open(jsonl_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entry = json.loads(line)
                    entries.append(entry)
                except json.JSONDecodeError:
                    continue
    return entries


def extract_chat_summary(chat_entries):
    """Create a compact summary of chat entries."""
    summary = []
    for entry in chat_entries:
        compact_entry = {
            "uuid": entry.get("uuid"),
            "timestamp": entry.get("timestamp"),
            "type": entry.get("type"),
        }
        
        # Include message content for user/assistant messages
        if "message" in entry and entry["type"] in ["user", "assistant"]:
            compact_entry["message"] = entry["message"]
        
        # Include tool calls and results
        if "toolCallResult" in entry:
            compact_entry["toolCallResult"] = {
                "callId": entry["toolCallResult"].get("callId"),
                "status": entry["toolCallResult"].get("status"),
            }
        
        # Include usage metadata for assistant messages
        if "usageMetadata" in entry:
            compact_entry["usageMetadata"] = entry["usageMetadata"]
        
        # Include model info
        if "model" in entry:
            compact_entry["model"] = entry["model"]
        
        summary.append(compact_entry)
    
    return summary


def export_metadata(stats):
    """Export metadata about the export process."""
    metadata = {
        "export_date": datetime.now().isoformat(),
        "source_directory": str(QWEN_DIR),
        "statistics": stats,
    }
    return metadata


def main():
    """Main export function."""
    print(f"Exporting Qwen history from: {QWEN_DIR}")
    
    # Create export directory
    if EXPORT_DIR.exists():
        print(f"Warning: {EXPORT_DIR} already exists. Overwriting...")
        shutil.rmtree(EXPORT_DIR)
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    
    stats = {
        "projects_exported": 0,
        "chats_exported": 0,
        "debug_logs_exported": 0,
        "total_files": 0,
        "total_size_bytes": 0,
    }
    
    # 1. Export configuration
    print("\n[1/5] Exporting configuration...")
    config_dir = EXPORT_DIR / "config"
    config_dir.mkdir(exist_ok=True)
    
    # Settings
    settings_file = QWEN_DIR / "settings.json"
    if settings_file.exists():
        with open(settings_file, "r", encoding="utf-8") as f:
            settings = json.load(f)
        with open(config_dir / "settings.json", "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=2)
        stats["total_files"] += 1
        stats["total_size_bytes"] += (config_dir / "settings.json").stat().st_size
    
    # Installation ID
    install_id_file = QWEN_DIR / "installation_id"
    if install_id_file.exists():
        shutil.copy2(install_id_file, config_dir / "installation_id")
        stats["total_files"] += 1
        stats["total_size_bytes"] += (config_dir / "installation_id").stat().st_size
    
    # OAuth credentials (redacted)
    oauth_file = QWEN_DIR / "oauth_creds.json"
    if oauth_file.exists():
        with open(oauth_file, "r", encoding="utf-8") as f:
            oauth_data = json.load(f)
        cleaned_oauth = clean_oauth_creds(oauth_data)
        with open(config_dir / "oauth_creds_redacted.json", "w", encoding="utf-8") as f:
            json.dump(cleaned_oauth, f, indent=2)
        stats["total_files"] += 1
        stats["total_size_bytes"] += (config_dir / "oauth_creds_redacted.json").stat().st_size
    
    # 2. Export projects and chats
    print("[2/5] Exporting projects and chats...")
    projects_dir = QWEN_DIR / "projects"
    project_index = {"projects": [], "export_date": datetime.now().isoformat()}
    
    if projects_dir.exists():
        for project_folder in projects_dir.iterdir():
            if not project_folder.is_dir():
                continue
            
            project_name = project_folder.name
            project_info = {
                "name": project_name,
                "path": str(project_folder),
                "chats": [],
            }
            
            # Export chats for this project
            chats_folder = project_folder / "chats"
            if chats_folder.exists():
                project_chats_dir = EXPORT_DIR / "chats" / project_name
                project_chats_dir.mkdir(parents=True, exist_ok=True)
                
                for chat_file in chats_folder.iterdir():
                    if chat_file.suffix == ".jsonl":
                        chat_entries = compact_jsonl_to_list(chat_file)
                        chat_summary = extract_chat_summary(chat_entries)
                        
                        # Save compact chat data
                        output_file = project_chats_dir / chat_file.with_suffix(".json").name
                        with open(output_file, "w", encoding="utf-8") as f:
                            json.dump(chat_summary, f, indent=2, ensure_ascii=False)
                        
                        stats["chats_exported"] += 1
                        stats["total_files"] += 1
                        stats["total_size_bytes"] += output_file.stat().st_size
                        
                        # Add to project index
                        session_id = chat_file.stem
                        project_info["chats"].append({
                            "session_id": session_id,
                            "file": str(output_file),
                            "messages": len(chat_summary),
                            "export_date": datetime.now().isoformat(),
                        })
            
            project_index["projects"].append(project_info)
            stats["projects_exported"] += 1
    
    # Save project index
    with open(EXPORT_DIR / "chats" / "chat-index.json", "w", encoding="utf-8") as f:
        json.dump(project_index, f, indent=2, ensure_ascii=False)
    stats["total_files"] += 1
    stats["total_size_bytes"] += (EXPORT_DIR / "chats" / "chat-index.json").stat().st_size
    
    # 3. Export debug logs (compact format)
    print("[3/5] Exporting debug logs...")
    debug_dir = QWEN_DIR / "debug"
    debug_export_dir = EXPORT_DIR / "debug"
    debug_export_dir.mkdir(exist_ok=True)
    
    if debug_dir.exists():
        # Get all debug log files (excluding 'latest' symlink)
        log_files = [f for f in debug_dir.iterdir() 
                     if f.is_file() and f.name != "latest" and f.suffix == ".txt"]
        
        # Sort by modification time (newest first) and limit
        log_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        
        for log_file in log_files[:MAX_DEBUG_LOGS]:
            # Read and compact the log
            with open(log_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            # Save as JSON array of lines for better structure
            compact_log = {
                "session_id": log_file.stem,
                "log_lines": len(lines),
                "content": [line.strip() for line in lines if line.strip()],
                "export_date": datetime.now().isoformat(),
            }
            
            output_file = debug_export_dir / log_file.with_suffix(".json").name
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(compact_log, f, indent=2, ensure_ascii=False)
            
            stats["debug_logs_exported"] += 1
            stats["total_files"] += 1
            stats["total_size_bytes"] += output_file.stat().st_size
    
    # 4. Export output language rule
    print("[4/5] Exporting custom rules...")
    output_lang_file = QWEN_DIR / "output-language.md"
    if output_lang_file.exists():
        shutil.copy2(output_lang_file, EXPORT_DIR / "output-language.md")
        stats["total_files"] += 1
        stats["total_size_bytes"] += (EXPORT_DIR / "output-language.md").stat().st_size
    
    # 5. Create metadata
    print("[5/5] Creating metadata...")
    metadata = export_metadata(stats)
    metadata_file = EXPORT_DIR / "metadata.json"
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print("\n" + "=" * 60)
    print("EXPORT COMPLETE")
    print("=" * 60)
    print(f"Export directory: {EXPORT_DIR.absolute()}")
    print(f"Projects exported: {stats['projects_exported']}")
    print(f"Chats exported: {stats['chats_exported']}")
    print(f"Debug logs exported: {stats['debug_logs_exported']}")
    print(f"Total files: {stats['total_files']}")
    print(f"Total size: {stats['total_size_bytes'] / 1024:.2f} KB")
    print("=" * 60)
    print("\nTo view the exported data:")
    print(f"  - Chat index: {EXPORT_DIR / 'chats' / 'chat-index.json'}")
    print(f"  - Metadata: {EXPORT_DIR / 'metadata.json'}")
    print(f"  - Settings: {EXPORT_DIR / 'config' / 'settings.json'}")


if __name__ == "__main__":
    main()
