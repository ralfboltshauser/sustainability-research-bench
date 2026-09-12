# UPS: quantify delivery electrification without inventing an eligible fleet

Research cutoff: 12 September 2026. Suggested app record: [ups.json](ups.json).

**Strongest defensible technology comparison: approximately 46% lower operating climate emissions per mile in an independent historical electric-delivery study, conditional on its duty cycle and electricity assumptions. This is not a UPS-wide preventable percentage.** Per 1,000 tonnes of matching baseline operating emissions, the difference is 463.54 tonnes, valued at approximately **$118,257 in 2024 dollars** using the pilot’s fixed $255.12/tCO₂e factor. Manufacture and disposal are outside this comparison.

## Latest company inventory

[UPS 2025 GRI](https://about.ups.com/content/dam/upsstories/images/our-impact/reporting/2025-ups-gri.pdf), Appendix B, printed p. 38 (PDF page 38), reports **14.898 million tonnes Scope 1**, 0.540 million Scope 2 market-based, and 10.333 million Scope 3 for calendar 2025. Operational control defines consolidation. Ground vehicle fuel contributes 3.608 million direct tonnes, including 1.624 million diesel tonnes; airline fuel contributes 10.905 million (printed p. 52). These source pools include activity beyond eligible urban delivery. Biomass CO₂ is separate from Scope 1; its methane and nitrous oxide remain included.

The main inventory gives 14.898 million Scope 1 while the segment-total table on printed p. 39 gives 14.897 million. We retain the main inventory and disclose the unresolved 1,000-tonne difference; the fuel table reconciles to the main figure. At the common pilot factor, direct climate damage associated with that reporting year is **$3.801 billion**, a modeled societal burden rather than a financial liability or annual realized loss.

## Reproducible original study

[NREL, *Field Evaluation of Medium-Duty Plug-in Electric Delivery Trucks* (December 2016)](https://docs.nlr.gov/docs/fy17osti/66382.pdf), printed pp. 20–21, supplies the comparison. The original PDF and full text are archived in [sources/ups](sources/ups). This is Frito-Lay’s Federal Way, Washington, delivery operation, not UPS. The Class 6 Smith Newton EVs had 80-kWh batteries; diesel comparators included model years 2001–2012. Their similar routes involved delivery and shelf stocking, typically less than 40 miles daily and approximately 1.5 hours driving. It is an observed fleet comparison, not a randomized experiment, and payload-equivalence at every trip is not established.

The study combines observed energy use with emission factors:

| Item | Source value | Locator |
|---|---:|---|
| Diesel well-to-wheels benchmark | 1,414.93 gCO₂e/mile | printed p. 20 |
| EV, historical local electricity | 759.06 gCO₂e/mile | printed p. 20 |
| EV, historical national electricity | 958.51 gCO₂e/mile | printed pp. 20–21 |
| Local generation intensity before grid losses | 450.58 gCO₂e/kWh | printed p. 20 |
| Electricity intensity delivered to depot | 485.54 gCO₂e/kWh | printed p. 20 |

The local case reflects Puget Sound Energy’s 2014 electricity and a 7.2% transmission/distribution loss assumption. Charging losses are also included. Using the printed per-mile values:

- Local case: `(1,414.93 − 759.06) / 1,414.93 = 46.3535%`.
- National-electricity case: `(1,414.93 − 958.51) / 1,414.93 = 32.2574%`.
- Per 100,000 genuinely matching miles: 65.587 tonnes difference in the local case, or 45.642 tonnes in the national case.

These are historical grid comparisons, not a confidence interval or 2026 electricity forecast. The EV side is electricity generation and use; the diesel side is described as GREET well-to-wheels. Neither establishes a complete vehicle lifecycle. Battery mining/production, vehicle production, replacement batteries, disposal and premature scrappage require a separate project lifecycle assessment. Do not call the EV zero-carbon simply because it has no exhaust. Recalculate electricity supply with actual charging location and timing, and distinguish inventory-average factors from marginal project consequences.

The source’s annual savings statement uses “tons” and does not transparently match a metric-tonne calculation from its rounded distance and per-mile figures. We deliberately use the explicitly unit-labelled per-mile values, not that annual headline.

## Available technology and existing adoption

[UPS’s June 2024 deployment announcement](https://about.ups.com/gb/en/our-stories/innovation-driven/new-ups-electric-vehicles-hit-the-streets-of-europe.html) reports more than 100 electric vans deployed in Paris, identifies IVECO eDaily, and advertises up to 142 miles range. This verifies operating deployment, not universal route suitability or a measured reduction factor for that model. Its broader planned rollout is not counted as completed.

The [UPS 2025 overview](https://about.ups.com/ca/en/our-impact/ups-sustainability-and-community-impact-report/delivering-for-our-planet.html) reports more than 580 battery EVs deployed and more than 1,400 electric/hybrid electric vehicles. It also attributes **10–14 fewer miles per driver per day** to its routing platform. These are already-achieved measures. Neither the historical routing savings nor the already-deployed EVs can be presented as the remaining gap financed by a new fund. The company’s categories and prior plans do not provide a clean eligible-unconverted denominator.

## Deployment and investment decision

Before financing, obtain route-level vehicle types, payloads, stops, mileage and energy; identify vehicles still using diesel and otherwise due for replacement; verify seasonal range and battery reserve; check depot parking, grid interconnection, transformer capacity, tariffs and charging schedule; quote vehicles, chargers, civil works, maintenance and downtime. Demonstrate equivalent delivered service and identify commitments already funded. Avoid stacking routing and electrification savings against the same original mileage: optimize mileage first, then electrify the residual work.

NREL printed p. 19 gives a historical **$86,791 incremental vehicle cost**, with a **$60,000 New York voucher** example. These do not establish current UPS prices, eligibility, payback or financing need. No current project cost, operating savings or guaranteed recovery of principal is assigned. Societal damage avoided is not money that can service debt. Project cashflow would need verified diesel/maintenance savings net of electricity, demand charges, installation, replacement and finance costs.

## Index membership and verification limits

[S&P’s own Quality FCF High Dividend index page](https://www.spglobal.com/spdji/en/indices/dividends-factors/sp-500-quality-fcf-high-dividend-index/) states its universe comprises S&P 500 companies. Provider-indexed content lists UPS among constituents with an August 31, 2026 date. This supports membership through an index-provider subset, but the opened live page did not expose its dynamic constituent rows. It is not an archived complete parent-index roster.

Company report text and tables were accessed through the web PDF reader. A direct local download returned HTTP 403; extracted facts and locators are preserved in the JSON and the source note. The NREL original report downloaded successfully and its actual technical passages were inspected locally. The older study was retained because it exposes calculation inputs; it is a historical process benchmark, not a claim to represent the newest truck’s performance.
