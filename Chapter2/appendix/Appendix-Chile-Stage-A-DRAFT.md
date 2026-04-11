---
source: appendix_chile_stage_a.tex
source_type: latex
status: draft
latex_label: app:chile_stage_a
bib: references.bib
---
---


# Appendix B — Chilean Stage A: Peripheral Structural Identification

label: app:chile_stage_a

<!-- FLAG: appendix_note_link | label=app:chile_stage_a | target=[[Appendix-Chile-Stage-A-DRAFT]] -->
<!-- FLAG: draft_source | file=appendix_chile_stage_a.tex | reason=template_or_unresolved_content -->
<!-- FLAG: parse_issues | file=appendix_chile_stage_a.tex | reason=template_placeholders_and_incomplete_tables -->
<!-- FLAG: unresolved_appendix_body | source=appendix_chile_stage_a.tex | reason=template_status_and_incomplete_body -->

This appendix reports the econometric detail underlying the Chilean capacity utilization estimates presented in [[Chapter-2-Profit-Rate-Investment#Chile]]. The identification mirrors the US procedure ([[Appendix-US-Stage-A]]) with two structural modifications: the capital stock is decomposed into machinery and equipment ($K^{ME}$) and non-residential infrastructure ($K^{NR}$), and the balance-of-payments constraint enters through the machinery share $\phi_t = K_t^{ME}/K_t^{CL}$ as a fifth state variable.

<!-- FLAG: local_crosswalk | original=Section~\ref{sec:results_chile} -->
<!-- FLAG: latex_crosswalk | original=Appendix~\ref{app:us_stage_a} -->

## State Vector and Data

label: app:cl:data

The Chilean state vector is:

$$
X_t^{CL} = \left(y_t,\; k_t^{NR},\; \omega_t,\;
\omega_t \cdot k_t^{ME},\; \phi_t\right)'
$$

label: eq:cl:sa:state_vector

with a restricted constant (`ecdet="const"`, Case 3), where
$y_t = \ln(\text{GDP}^{CL}_{real})$,
$k_t^{NR} = \ln(K^{NR,CL}_{real})$,
$\omega_t = EC^{CL}_{NF}/GVA^{CL}_{NF}$ is the non-financial
corporate wage share, and $\phi_t = K_t^{ME}/K_t^{CL}$ is the
machinery share of the non-residential capital stock.[^1]

[^1]: The distributional variable is the wage share $\omega_t$, consistent with the 2026-04-05 specification lock. The interaction $\omega_t k_t^{ME}$ — not $\omega_t k_t^{NR}$ — follows from the cost-minimization result that distribution conditions technique choice through the machinery component ([[Chapter-2-Profit-Rate-Investment#The BoP Penalty and the Effective Profit Share]]). <!-- FLAG: local_crosswalk | original=Section~\ref{subsec:chile_bop_penalty} -->

## Integration Order

label: app:cl:integration

A critical stage-gate is the integration order of $\phi_t$. If
$\phi_t \sim I(0)$, it enters the short-run dynamics only and cannot
serve as a cointegrating variable; in that case, the state vector
reduces to four dimensions.

### Unit Root Tests — Chilean Variables

label: tab:cl:sa:unit_root

| Variable | ADF stat | ADF $p$ | KPSS stat | KPSS $p$ | Order |
| --- | ---: | ---: | ---: | ---: | --- |
| $y_t$ |  |  |  |  |  |
| $k_t^{NR}$ |  |  |  |  |  |
| $\omega_t$ |  |  |  |  |  |
| $\omega_t k_t^{ME}$ |  |  |  |  |  |
| $\phi_t$ |  |  |  |  |  |

*Notes:* Sample: [insert sample period]. ADF specification: [insert lag/deterministic terms]. KPSS bandwidth: [insert method].

## Rank Determination

label: app:cl:rank

The Johansen trace test is conducted on the system above using lag order $K = [\text{insert lag}]$ and long-run normalization. The working expectation is $r = 3$: two cointegrating relations associated with the capacity frontier and the balance-of-payments equilibrium, plus one additional distributional or compositional relation.

### Johansen Trace Test — Chilean System

label: tab:cl:sa:trace

| $H_0$ | Eigenvalue | Trace statistic | 5% critical value |
| --- | ---: | ---: | ---: |
| $r \leq 0$ |  |  |  |
| $r \leq 1$ |  |  |  |
| $r \leq 2$ |  |  |  |
| $r \leq 3$ |  |  |  |
| $r \leq 4$ |  |  |  |

*Notes:* Sample: [insert sample period]. The test is implemented with $K = [\text{insert lag}]$ lags, `spec="longrun"`, and `ecdet="const"`.

## Cointegrating Vector 1: Capacity Frontier

label: app:cl:cv1

The $y$-normalized first cointegrating vector, $\hat{\beta}_1^{CL}$, is:

$$
y_t
= c_1 + \tilde{\theta}_0\, k_t^{NR}
+ \theta_3\, \phi_t
+ \theta_2\, (\omega_t \phi_t)
$$

label: eq:cl:sa:cv1

where $\theta_3$ captures the machinery-composition productivity premium and $\theta_2 < 0$ captures the distribution--composition interaction.

### CV1 Structural Parameters (Chilean Capacity Frontier)

label: tab:cl:sa:cv1_params

| Parameter | Structural role | Estimate |
| --- | --- | ---: |
| $\tilde{\theta}_0$ | Infrastructure base elasticity |  |
| $\theta_3$ | Machinery-composition productivity premium |  |
| $\theta_2$ | Distribution--composition interaction |  |
| $c_1$ | Constant |  |

*Notes:* Estimated via Johansen MLE on the state vector above. The theoretically expected signs are $\theta_3 > 0$ and $\theta_2 < 0$.

The distribution-conditioned, composition-dependent transformation elasticity is:

$$
\hat{\theta}^{CL}(\omega_t,\phi_t)
= \tilde{\theta}_0 + \theta_3\,\phi_t
+ \theta_2\,\omega_t\,\phi_t
$$

label: eq:cl:sa:theta

This is the empirical counterpart of the main text object below.[^2]

<!-- FLAG: latex_crosswalk | original=\eqref{eq:cl:theta} -->

[^2]: The theoretical object $\theta^{CL}(\omega,\phi,\lambda)$ includes the shadow cost of foreign exchange. In the linear VECM, $\lambda$ is absorbed into the cointegrating coefficients. The threshold extension below recovers $\hat{\lambda}$ from regime-differential loadings. <!-- FLAG: local_crosswalk | original=Section~\ref{app:cl:threshold} -->

## Cointegrating Vector 2: BoP Equilibrium

label: app:cl:cv2

The second cointegrating vector identifies the long-run BoP equilibrium:

$$
\ln m_t = \zeta_0
+ \zeta_1\, \ln nrs_{Y,t}
+ \zeta_3\, k_t^{ME}
+ \zeta_2\, \omega_t
$$

label: eq:cl:sa:cv2

### CV2 Structural Parameters (BoP Equilibrium)

label: tab:cl:sa:cv2_params

| Parameter | Channel | Estimate | Expected sign |
| --- | --- | ---: | --- |
| $\zeta_1$ | Palma--Marcel (NRS relief) |  | $> 0$ |
| $\zeta_3$ | Tavares (ME structural imports) |  | $> 0$ |
| $\zeta_2$ | Distribution |  | ambiguous |
| $\zeta_0$ | Constant |  | --- |

*Notes:* Trap intensity ratio $\zeta_3/\zeta_1 = \text{}$. If $> 1$, machinery accumulation outpaces the NRS relief valve.

## Error Correction Loading

label: app:cl:alpha

### Loading Matrix $\hat{\alpha}^{CL}$ — Linear VECM

label: tab:cl:sa:alpha

| Equation | $\hat{\alpha}_{\cdot,1}$ | SE | $t$ | $\hat{\alpha}_{\cdot,2}$ | SE | $t$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| $\Delta y_t$ |  |  |  |  |  |  |
| $\Delta k_t^{NR}$ |  |  |  |  |  |  |
| $\Delta \omega_t$ |  |  |  |  |  |  |
| $\Delta(\omega_t k_t^{ME})$ |  |  |  |  |  |  |
| $\Delta \phi_t$ |  |  |  |  |  |  |

*Notes:* Johansen MLE, $r = \text{}$. Key diagnostic: $\hat{\alpha}_{\phi,2}$ (BoP disequilibrium adjusts machinery composition) and $\hat{\alpha}_{y,1} \approx 0$ (output does not error-correct to the capacity frontier — demand-determined, as in the US).

## ECT Stationarity

label: app:cl:ect_stationarity

### ADF Tests on Chilean ECTs

label: tab:cl:sa:ect_adf

|  | ADF statistic | $p$-value |
| --- | ---: | ---: |
| $ECT_{1,t}$ (capacity frontier) |  |  |
| $ECT_{2,t}$ (BoP equilibrium) |  |  |

*Notes:* $ECT_{2,t} \sim I(0)$ is a precondition for the threshold VECM extension: the Hansen--Seo procedure requires a stationary threshold variable.

## Regime Partition

label: app:cl:regime

Setting $\hat{\theta}^{CL}(\omega, \phi) = 1$ in the equation above:

$$
\omega_H^{CL}(\phi)
= \frac{\tilde{\theta}_0 + \theta_3\,\phi - 1}{\theta_2\,\phi}
$$

label: eq:cl:sa:omega_H

Unlike the center, the Harrodian knife-edge is *composition-dependent*: the wage share at which $\hat{\theta} = 1$ shifts with $\phi_t$. As $\phi$ rises (more ME), the knife-edge moves — the regime classification is jointly determined by distribution and composition.

### Regime Partition of $\hat{\theta}^{CL}(\omega_t, \phi_t)$

label: tab:cl:sa:regime_summary

| Object | Value |
| --- | ---: |
| $\hat{\theta}^{CL}$ at $(\bar{\omega}, \bar{\phi})$ |  |
| $\hat{\theta}^{CL}$ range |  |
| $\omega_H^{CL}$ at $\bar{\phi}$ |  |
| % sample under-accumulation ($\hat{\theta} > 1$) |  |
| % sample over-accumulation ($\hat{\theta} < 1$) |  |

*Notes:* $\hat{\theta}^{CL}(\omega_t, \phi_t)$ from the equation above.

## Capacity Utilization: Construction

label: app:cl:mu_construction

The capacity utilization rate $\hat{\mu}_t^{CL}$ is constructed by the same growth closure as the US ([[Appendix-US-Stage-A#Structural Closure]]). The frontier is pinned at:

<!-- FLAG: latex_crosswalk | original=Appendix~\ref{app:sa:mu_structural} -->

$$
\hat{\mu}^{CL}(t_0) = \mu_0
$$

label: eq:cl:sa:mu_pin

The growth rate of productive capacity is:

$$
g(Y_t^{p,CL}) = \hat{\theta}^{CL}(\omega_t, \phi_t)
\cdot g(K_t^{NR,CL})
$$

label: eq:cl:sa:frontier_growth

and $Y_t^{p,CL}$ is accumulated forward and backward from the pin year:

$$
\hat{\mu}_t^{CL} = \frac{Y_t^{CL}}{Y_t^{p,CL}}
$$

label: eq:cl:sa:mu_def

### $\hat{\theta}^{CL}$ and $\hat{\mu}^{CL}$ Period Averages

label: tab:cl:sa:mu_periods

| Period | Years | $n$ | $\bar{\theta}^{CL}$ | $\bar{\mu}^{CL}$ |
| --- | --- | ---: | ---: | ---: |
| ISI |  |  |  |  |
| UP | 1970--1973 | 4 |  |  |
| Regime transition | 1973--1978 | 6 |  |  |

*Notes:* $\hat{\theta}^{CL}(\omega_t, \phi_t)$ from the equation above; $\hat{\mu}_t^{CL}$ from the utilization definition above with pin-year condition above.

## Pin-Year Sensitivity

label: app:cl:pin_sensitivity

### Pin-Year Sensitivity of $\hat{\mu}^{CL}$

label: tab:cl:sa:mu_pin_sensitivity

| Pin year | $\mu_0$ | $\bar{\mu}^{CL}$ (ISI) | $\bar{\mu}^{CL}$ (UP) |
| --- | ---: | ---: | ---: |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

*Notes:* Level shifts uniformly but cyclical profile and regime timing are invariant to pin choice.

## Threshold VECM: BoP Regime Switch

label: app:cl:threshold

The threshold VECM extends the linear system by allowing the loading matrix $\alpha$ to switch across two regimes defined by the lagged BoP disequilibrium:

$$
R_t = \mathbf{1}\!\left[ECT_{2,t-1} > \hat{\gamma}\right]
$$

label: eq:cl_sa_regime_indicator

The Hansen--Seo (2002) procedure jointly estimates the threshold $\hat{\gamma}$ and the regime-specific loadings. The key diagnostic is the loading on $ECT_2$ in the $k^{ME}$ equation:

### Threshold VECM Regime-Specific Loadings ($ECT_2$, $k^{ME}$ equation)

label: tab:cl:sa:tvecm_loadings

| Regime | $\hat{\alpha}_{k^{ME},\,ECT_2}$ | SE | Interpretation |
| --- | ---: | ---: | --- |
| 1 (BoP slack) |  |  | ME unconstrained |
| 2 (BoP binding) |  |  | Leash activates ($< 0$ expected) |

*Notes:* Regime-specific loading matrices (iii); recovered $\hat{\lambda}$ from the recovery equation below.

The recovered shadow cost:

$$
\hat{\lambda} = \frac{-2|\lambda_2|\;
\hat{\alpha}^{(2)}_{k^{ME},\,ECT_2}
\cdot \text{SD}(ECT_2)}{\xi\,\hat{\phi}}
$$

label: eq:cl_sa_lambda_recovered

The recovered $\hat{\lambda}$ carries bootstrap confidence intervals. Compare to Kaldor (1959) implicit shadow cost; the import content $\xi \approx 0.92$--$0.94$ provides a scaling check for plausibility.

## Cross-Country Comparison Objects

label: app:cl:cross_country

Four diagnostics produce the restriction menu for Chapter 3:

1. $\Delta r$: profit rate gap $\hat{r}^{US} - \hat{r}^{CL}$
2. $\Delta\hat{\theta}$: transformation elasticity gap $\hat{\theta}^{US}(\omega_t) - \hat{\theta}^{CL}(\omega_t, \phi_t)$, evaluated at respective sample means
3. IICS sign stability: does the sign of the loading on $ECT_1$ in the $\omega$ equation hold across both countries?
4. Block exogeneity: Granger causality from $\hat{u}_t^{US}$ to $\Delta X_t^{CL}$