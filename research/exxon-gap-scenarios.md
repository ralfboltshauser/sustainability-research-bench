# ExxonMobil tank vapor recovery: conditional climate-gap scenarios

As of 12 September 2026. These calculations quantify a climate-burden sensitivity, **not measured damages, a verified feasible 2031 program, or a fund-attributable result**.

The approximate reported tank/storage methane pool is 6,816 tonnes/year: 142,000 tonnes company methane × 96% upstream × 5% tanks/storage. This translates to about **203,117 tonnes CO2e100/year of reported baseline climate burden** with the factor below. Rounded source inputs limit precision. [ExxonMobil methane chapter and source chart, footnote8](https://corporate.exxonmobil.com/Publications/Advancing-Climate-Solutions/driving-reductions-in-methane-emissions).

EPA describes a 95% annual source methane reduction for appropriately designed and operated vapor recovery systems. Use that factor only on an eligible untreated source cohort, with adequate vapor flow, power and an outlet—not on already controlled emissions by default. [EPA VRU guidance, Description / Applicability / Methane Emissions Reductions](https://www.epa.gov/natural-gas-star-program/vapor-recovery-units).

## Explicit conversion and sensitivity

IPCC AR6 WGI Table7.15 gives fossil methane a 100-year global warming potential of **29.8 ±11**; the central value is used here. The official PDF was downloaded and its table checked at PDF page95, printed page1017 after the web viewer returned an access error. GWP is an integrated climate metric, not a monetary damage estimate or a temperature prediction. [IPCC AR6 WGI Chapter7, Table7.15](https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter07.pdf).

For eligible share s, avoided methane M = 6,816 × s ×0.95 tonnes/year. Gross climate benefit = M×29.8. If all captured methane is fully combusted, new CO2 = M×44/16 = M×2.75, from carbon conservation in CH4 +2O2 → CO2 +2H2O. Net benefit before other lifecycle emissions = M×(29.8−2.75) = M×27.05.

The higher fossil-methane GWP already incorporates CO2 from atmospheric methane oxidation. It is appropriate for fugitive/process methane; do not add baseline oxidation CO2 a second time. Subtracting project combustion accounts for that new, immediate release once. [IPCC AR6 WGIII AnnexII, Table11 and accompanying explanation](https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Annex-II.pdf).

**The following eligible shares are analyst sensitivities, not adoption forecasts or confidence intervals.**

| Eligible share of reported tank pool | Avoided CH4, t/year | Gross benefit, tCO2e100/year | New combustion CO2, t/year | Net before other lifecycle, tCO2e100/year | Net / operated total, contextual |
|---|---:|---:|---:|---:|---:|
| 25% | 1,618.8 | 48,240 | 4,452 | 43,789 | 0.045% |
| 50% | 3,237.6 | 96,480 | 8,903 | 87,577 | 0.090% |
| 100% | 6,475.2 | 192,961 | 17,807 | 175,154 | 0.181% |

Displayed tonnes are rounded; exact arithmetic is preserved in the companion JSON. Source uncertainty is much larger than arithmetic rounding. The 100% row is a conditional engineering ceiling, not a realistic default.

## What the comparison does and does not show

The contextual denominator is Exxon's reported **97 million tonnes CO2e of operated Scope1 plus market-based Scope2 in2025**, with IPCC2021 cited in its methodology. The net cases represent roughly **0.045%, 0.090%, and 0.181%** of that scale. Gross ratios are approximately **0.050%, 0.099%, and 0.199%**. These are approximate scale comparisons rather than fully harmonized inventory reductions: the numerator explicitly uses AR6 fossil methane GWP100, the full denominator's species factors have not been rebuilt, and the net numerator includes customer combustion outside the denominator's operational boundary. [ExxonMobil Metrics and Data, operated table and footnote2](https://corporate.exxonmobil.com/publications/metrics-and-data).

There is **no justified positive lower bound for additional feasible abatement from these public data**. Zero remains possible for the fund if remaining sources are already controlled, unsuitable, scheduled for treatment without funding, or cannot be brought forward. Exxon already identifies tank VRU retrofits. The disclosed source pool does not identify untreated locations or committed work, and applying95% to residual emissions from a failing existing VRU may be wrong. [Company methane chapter](https://corporate.exxonmobil.com/Publications/Advancing-Climate-Solutions/driving-reductions-in-methane-emissions).

No displacement of other gas or fuel is assumed. The net result excludes electricity, compression, transport leakage, construction, other recovered hydrocarbons, and associated air pollutants. It is therefore **not a complete lifecycle result**. Recovering tank methane also does not eliminate emissions from the company's sold oil and gas. Annual results describe a steady operating year after deployment; multiplying them across five years would require an explicit commissioning and persistence schedule.

A defensible pitch line is: **If an audit finds that one-quarter to one-half of Exxon's reported tank methane remains suitable for additional vapor recovery, existing technology could avoid approximately44,000–88,000 tonnes CO2-equivalent per operating year even after the recovered methane is burned, before equipment energy and other lifecycle effects. The eligible share and additionality must still be verified.**

To turn this into a funded project, measure eligible source emissions, inspect existing controls, reconcile funded and mandatory schedules, price power and capture infrastructure, establish gas ownership/disposition, and compare implementation timing with the without-fund case. Monetization must use a stated damage model separately; neither CO2e nor avoided damage constitutes repayment revenue.
