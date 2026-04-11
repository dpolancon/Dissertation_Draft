---
source: appendix_theta_identification.tex
source_type: latex
status: shell_reconstruction
latex_label: app:us_formal_id
bib: references.bib
---
---
source: appendix_theta_identification.tex
source_type: latex
status: reconstructed_from_current_tex
latex_label: app:us_formal_id
bib: references.bib
---

# Appendix — Identification Details

label: app:us_formal_id

## A.1 Admissibility Conditions

The positivity of the optimal mechanization rate $\hat{q}^* > 0$
requires $\lambda_1 > 1 - \omega$: the MPF slope must exceed the
profit share for mechanization to be profitable. Since
$\lambda_1 = 2\beta_1 - 1$, this translates to $\beta_1 > 1 -
\omega/2$, which binds at $\omega \to 0$ as $\beta_1 > 1$.

Progressive technical change ($g' > 0$ everywhere in the feasible
domain) is automatically satisfied at the optimum for all
$\omega \in (0,1)$. The vertex of the quadratic frontier lies at
$\hat{q}_{\text{max}} = -\lambda_1 / (2\lambda_2)$, with maximum
productivity growth:

$$
\hat{a}_{\text{max}} = \frac{\lambda_1^2}{-4\lambda_2}
$$

label: eq:amax

This is the ceiling on productivity growth — a pure function of
the MPF parameters, independent of distribution. The transformation
elasticity is bounded accordingly:

$$
1 - \omega < \theta(\omega) < \lambda_1,
\qquad
\theta_{\text{max}} = \frac{\lambda_1}{2}
$$

label: eq:theta_bounds

## A.2 Short-Run Exclusion on the Interaction Term

The interaction $\omega_t k_t$ is a constructed variable carrying
long-run identification content. Its first difference
$\Delta(\omega_t k_t) = \omega_t \Delta k_t + k_t \Delta \omega_t
+ \Delta \omega_t \Delta k_t$ conflates short-run distributional
fluctuations with capital-stock movements. These short-run dynamics
are not independently meaningful for the identification of $\theta$.

All short-run coefficients on $\Delta(\omega_t k_t)$ are therefore
restricted to zero in the VECM. The interaction enters exclusively
through the error correction term $\beta' X_{t-1}$. The VECM takes
the form:

$$
\Delta X_t = \alpha \beta' X_{t-1}
+ \sum_{i=1}^{p-1} \Gamma_i^{*} \Delta X_{t-i}
+ \varepsilon_t
$$

label: eq:vecm_restricted

where $\Gamma_i^{*}$ denotes the short-run coefficient matrices with
the columns corresponding to $\Delta(\omega_t k_t)$ set to zero.

## A.3 Restriction Test Implementation

The state vector is
$X_t = (y_t,\; k_t,\; \omega_t,\; \omega_t k_t,\; \mathbf{1})'$
with restricted constant absorbed into the cointegrating space.
The cointegrating rank is determined by the trace and
maximum-eigenvalue statistics of the Johansen procedure
[@Johansen1991].

<!-- FLAG: latex_crosswalk | original=\citep{Johansen1991} -->

For each cointegrating vector $\beta_i$ admitted by the rank test,
restrictions R1 ($\beta_2 = -1/2$) and R3 ($\beta_\omega = 0$) are
tested jointly using the Johansen LR test for linear restrictions on
$\beta$ [@Johansen1991].

<!-- FLAG: latex_crosswalk | original=\citep{Johansen1991} -->

The unrestricted cointegrating vector,
normalized on $y$, is:

$$
\beta = (1,\; -\beta_1,\; -\beta_\omega,\; -\beta_2,\; -c)'
$$

Under R1 and R3, the restricted vector is:

$$
\beta = (1,\; -\beta_1,\; 0,\; \tfrac{1}{2},\; -c)'
$$

with two free parameters ($\beta_1$, $c$). The restriction matrix
$H$ that maps the free parameters into the full cointegrating space
is:

$$
H = \begin{pmatrix}
0 & 0 \\
1 & 0 \\
0 & 0 \\
0 & 0 \\
0 & 1
\end{pmatrix}
$$

label: eq:H_matrix

with fixed values imposed on the remaining slots: $y$ normalized to
1, $\omega$ restricted to 0, and $\omega k$ restricted to $1/2$. The
LR statistic is distributed $\chi^2$ with degrees of freedom equal
to the number of restrictions imposed (here, 2 per cointegrating
vector tested). R2 ($\beta_1 > 1$) is verified post-estimation on
the point estimate and its confidence interval.