---
source: appendix_us_stage_a.tex
source_type: latex
status: partial_reconstruction
latex_label: app:us_stage_a
bib: references.bib
---

# Appendix — US Estimation of Capacity Utilization via MPF

label: app:us_stage_a


## Recovered core result

The Johansen reduced-rank regression on the state vector  
$X_t = (y_t, k_t, \omega_t, \omega_t k_t)'$ with $K = 2$ lags over 1929–2024 identifies a single dominant cointegrating relation.

$$
y_t = 8.924\, k_t + 222.161\, \omega_t - 12.851\, \omega_t k_t - 138.254
$$

label: eq:mpf_us

From this, the distribution-conditioned transformation elasticity is:

$$
\hat{\theta}(\omega_t) = 8.924 - 12.851\,\omega_t
$$

label: eq:theta_us

At the sample mean $\bar{\omega} = 0.623$, the estimated elasticity is `0.918`, interpreted as an over-accumulation regime where the productive-capacity frontier grows slower than the capital stock.

The Harrodian knife-edge is:

$$
\omega_H = \frac{8.924 - 1}{12.851} = 0.617
$$

label: eq:omega_H_us

The crisis boundary is reported as `\omega^* = 0.694`.

## Figure placeholders

![Figure placeholder](#)

label: fig:theta_omega_scatter

<!-- FLAG: figure_placeholder | label=fig:theta_omega_scatter | source=figures/r1_theta_omega_scatter_full.pdf -->

Caption: The Mechanization Possibility Frontier: `\hat{\theta}(\omega_t)`, US Non-Financial Corporate Sector, 1929–2024.

![Figure placeholder](#)

label: fig:mu_us

<!-- FLAG: figure_placeholder | label=fig:mu_us | source=figures/r1_mu_capacity_utilization.pdf -->

Caption: Capacity utilization `\hat{\mu}_t`, US Non-Financial Corporate Sector, 1929–2024.

## Recovered interpretation block

The loading vector under `r = 1` is described as showing that output does not error-correct to the MPF, while capital and the wage share do adjust significantly. The appendix also states that `\hat{\mu}_t` is constructed by pinning the frontier at `\hat{\mu}(1948) = 0.80` and accumulating forward and backward via the unbalanced growth closure.

<!-- FLAG: partial_appendix_sections_missing | missing=rank_tables,alpha_table,mu_construction,restrictions,regime -->