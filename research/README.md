# Sustainability gap: five-company research pilot

**Quantification update:** [Damage values and current-technology scenarios](avoidable-damage-scorecard.md) now add monetary climate-damage estimates and explicit conditional reduction cases. The original pilot findings below remain the baseline evidence review.

Ten parallel researchers completed paired footprint and intervention investigations for Microsoft, Walmart, ExxonMobil, JPMorgan Chase and Nucor. The dataset contains 59 observation groups, 372 numeric baseline rows and 18 intervention records. The records include component quantities, historical values, percentages and alternative accounting views; they are not 372 independent measurements and must not be added together.

**Result:** public evidence supports quantitative company profiles and selected intervention calculations. It does not yet support a comparable, complete sustainability gap score for all five companies. The main missing inputs are the remaining eligible assets, matching physical activity volumes, feasible deployment schedules and current costs. That is a specific data constraint, not evidence of zero opportunity.

Research cutoff is September 12, 2026. Reporting periods differ and remain explicit. Membership was corroborated centrally against [iShares' S&P 500 tracker holdings dated September 10](https://www.ishares.com/us/products/239726/ishares-core-s-p-500-etf/latest-holdings.csv); the preserved evidence is in [membership-evidence.json](membership-evidence.json). Tracker holdings are corroboration rather than a licensed index constituent feed.

## Results by company

| Company | Quantified evidence | Most useful opportunity direction | What cannot yet be claimed |
|---|---|---|---|
| Microsoft | FY25 standard GHG inventory: 21.121 million tCO2e; electricity: 37.026 TWh; water consumption: 8.170 million m3 | Site-specific cooling and efficiency, qualified construction/material changes, additional physical clean electricity | A cooling-study percentage applied to the whole fleet; capital-goods savings without a material breakdown |
| Walmart | FY2026 Scope 1 + market Scope 2:  14.4 million tCO2e; onsite refrigerants: 4.08 million; CY2025 food disposal about 644,000 tonnes, excluding India | Refrigerant management, appropriate equipment replacement, food prevention and targeted fleet changes | That all refrigerant emissions or disposed food are preventable; a global conversion rate from partly converted US facilities |
| ExxonMobil | 2025 operated Scope 1 + market Scope 2: 97 million tCO2e; approximately 142,000 tonnes CH4; tank/storage methane source pool approximately 6,800 tonnes | Verified remaining vapor recovery, pneumatic controls and leak-repair cohorts | All source-pool emissions are eligible; source controls eliminate sold-product combustion; funded commitments need new capital |
| JPMorgan Chase | 2024 operational Scope 1 + location Scope 2: 873,876 tCO2e; market-based alternative106,830 | Finance named borrower equipment projects with verified resource savings and repayable contracts | Portfolio attribution changes represent real-world reductions, or generic project exemplars are identified bank borrowers |
| Nucor | 2025 hot-rolled steel intensity 1,051 kgCO2e/t versus2030 target 975; enterprise electricity 18.398 TWh | Remaining furnace improvements, qualified scrap/iron substitution and appropriate electricity projects | The target is a proven technical frontier; hot-rolled factors apply to all cast steel; existing capture contracts are new fund impact |

Sources: [Microsoft factsheet, Tables 1A, 5, 8](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf); [Walmart report, pp. 30–31 and 137](https://corporate.walmart.com/content/dam/corporate/documents/esgreport/2026/FY2026-Walmart-ESG-Report.pdf); [ExxonMobil metrics](https://corporate.exxonmobil.com/publications/metrics-and-data) and [methane chapter](https://corporate.exxonmobil.com/Publications/Advancing-Climate-Solutions/driving-reductions-in-methane-emissions); [JPMorgan operational inventory](https://www.jpmorganchase.com/content/dam/jpmorganchase/documents/2024-operational-ghg-emissions-and-electric-power-use.pdf); [Nucor report, pp. 38, 44](https://indd.adobe.com/view/publication/cc4a577c-36f1-4ae0-a823-7e9f3f547ca5/4a1d/publication-web-resources/pdf/2025_Sustainability_Report.pdf).

These rows intentionally preserve different boundaries; they are not a best-to-worst league table. ExxonMobil's product-use inventory, for example, is separate from its operational inventory. JPMorgan's borrower inventories can overlap the other companies. Water volume is not a direct measure of local damage.

## Calculations available now

**Walmart: identify a material source, then quantify a repair.** Its rounded figures imply onsite refrigerants represent 28.33% of operational emissions and 50% of direct emissions. These are footprint shares, not gap scores. For a verified kilogram of R-404A leakage prevented, the [EPA reference factor](https://www.epa.gov/hfcs/technology-transitions-gwp-reference-table) gives 3.922 tCO2e of direct avoided emissions. Actual gas species, leakage logs and equipment changes are needed for a Walmart-wide estimate. Electricity, servicing and end-of-life effects remain separate.

**ExxonMobil: calculate the relevant source pool before applying a technology factor.** The approximate tank/storage pool is 142,000×96%×5%=6,816 tCH4/year. [EPA's vapor-recovery method](https://www.epa.gov/natural-gas-star-program/vapor-recovery-units) supplies 95% direct control for suitable sources. Applying it to the entire pool gives approximately 6,475 tCH4/year, but that is only a conditional engineering envelope: all-source eligibility and absence of existing controls are unsupported. A valid project calculation instead applies the factor to a measured, eligible untreated cohort and accounts separately for power and recovered-gas combustion. Source shares are rounded and sum 101%; these are not exact physical ceilings.

**Nucor: distinguish current target gap from the original roadmap.** The latest difference is 1,051−975=76 kgCO2e per tonne of hot-rolled steel, or 7.23%. For an explicitly normalized 1 million-tonne annual output block, that corresponds to 76,000 tCO2e/year if the target is achieved at matching product mix and boundary. The block is not a measured eligible company volume. The original 2023 roadmap's 116 kg/t is not all remaining. A target gap is neither a validated available-technology gap nor investor additionality. [Nucor report, pp. 38, 41](https://indd.adobe.com/view/publication/cc4a577c-36f1-4ae0-a823-7e9f3f547ca5/4a1d/publication-web-resources/pdf/2025_Sustainability_Report.pdf)

**Microsoft: retain a useful engineering factor without inventing fleet scale.** The cooling research supplies conditional lifecycle factors, but its configurations differ in computing capacity as well as cooling. Selected site electricity and water data do not establish compatible rack counts or equivalent computing service. The [intervention report](microsoft-solutions.md) records those applicability conditions. A headline study reduction is not a fleet reduction, and zero evaporation is not zero lifecycle water use.

**JPMorgan route: demonstrate how capital could return using a clearly separate project exemplar.** A [DOE-hosted historical GM cooling project](https://betterbuildingssolutioncenter.energy.gov/showcase-projects/general-motors-chilled-water-system-optimization-project) reports about $2 million cost, 8,600 MWh annual electricity savings and $760,000 annual bill savings. Those numbers imply 2.63 years simple cost/gross-savings payback before incremental costs and without incentives. A five-year principal-only schedule would require $400,000/year, leaving $360,000/year of the reported gross saving for other costs. These are historical nominal figures, not a current quote, net repayment forecast or verified JPMorgan borrower. This example supports the financing mechanism, not a bank-wide opportunity estimate.

All arithmetic is reproduced in [calculated-examples.csv](calculated-examples.csv), with formulas, result units, evidence status and limitations. No full-company score or cross-company abatement total was computed.

## What the pilot changes about the scoring design

The original gap-percentage idea requires a defensible feasible alternative over the same complete boundary as the baseline. This pilot shows that a formula alone does not supply that alternative. Corporate targets, historic demonstrations and technology factors are different types of evidence and cannot be substituted for one another.

For the first product, use four explicit result types:

- **Reported footprint:** a sourced quantity with its scope, year and assurance status.
- **Quantified intervention scenario:** a matched physical calculation, with adoption assumptions and unresolved inputs exposed.
- **Reported target gap:** a separately labeled comparison to a company target, such as Nucor's 7.23%.
- **Insufficient evidence:** a missing material input prevents the desired estimate.

Only the second type can eventually support the proposed technology-gap numerator, and only after enough interventions and harms are covered. Funding additionality requires a further counterfactual: what happens without this capital, including already planned work. Do not multiply the score by an evidence-confidence weight; that would make low disclosure look like low harm.

A required hackathon ranking can be demonstrated on a transparently specified comparable subset or scenario. A claim of a complete, fair all-five environmental ranking would exceed the evidence collected. If the final submission requires that exact claim, more data or a narrower score definition is necessary.

## Investment directions supported for further diligence

The repeated pattern is deployment of existing equipment and practices: refrigeration maintenance and replacement, gas recovery, furnace controls, and industrial cooling or pumping efficiency. Some projects can have utility, consumables or recovered-product cashflows. Those are plausible repayment sources; modeled environmental damage is not.

This supports investigating startups that identify eligible assets, verify performance, simplify installation or aggregate finance. It does not yet establish which startup has the best economics or that financing is always the binding constraint. Large companies may already have the capital and approved deployment plans. The exact fund contribution could instead involve their smaller suppliers, where evidence must be collected separately.

Before any billion-dollar allocation, obtain a named eligible project pipeline, contemporary bids, service-normalized baselines, implementation schedules, proof of a real capital or deployment constraint, and enforceable repayment terms. Returning principal in expectation is different from guaranteeing it. No current allocation, expected portfolio return or repayment probability has been justified by this pilot.

## Pitch-ready wording

“We tested our approach on five very different S&P 500 companies. Our researchers traced environmental quantities back to original disclosures, linked activities to available solutions, and made the missing inputs visible.

For example, refrigeration is a material part of Walmart's operational footprint. Nucor's latest hot-rolled steel data lets us calculate a gap to its stated target. Neither number alone proves a fundable opportunity. Our system connects that evidence to the equipment, deployment and financial questions needed to establish one.

The goal is a sustainability gap score that can explain every claimed improvement—and a map of projects where capital could help close those gaps and return through real cashflows.”

This wording describes a completed research pilot and a proposed system. It does not claim an implemented autonomous 500-company platform, proven global optimality, or a unique scoring category that has been exhaustively checked against competitors.

## Research package

- [Combined JSON dataset](research-bundle.json): all five footprint and intervention records, with original source metadata.
- [Baseline CSV](baseline-observations.csv): numeric observations for spreadsheet inspection. Mixed-unit groups preserve component names; original JSON remains authoritative for interpretation.
- [Calculation CSV](calculated-examples.csv) and [JSON](calculated-examples.json): 14 reproducible, labeled calculations.
- [Calculation rules](calculation-rules.md): boundaries, evidence classes and aggregation policy.
- [Independent QA](cross-company-qa.md): targeted Walmart and ExxonMobil source/arithmetic review; the identified India-exclusion omission was corrected.

| Company | Footprint research | Intervention research |
|---|---|---|
| Microsoft | [Report](microsoft-footprint.md) · [Data](microsoft-footprint.json) | [Report](microsoft-solutions.md) · [Data](microsoft-solutions.json) |
| Walmart | [Report](walmart-footprint.md) · [Data](walmart-footprint.json) | [Report](walmart-solutions.md) · [Data](walmart-solutions.json) |
| ExxonMobil | [Report](exxon-footprint.md) · [Data](exxon-footprint.json) | [Report](exxon-solutions.md) · [Data](exxon-solutions.json) |
| JPMorgan Chase | [Report](jpmorgan-footprint.md) · [Data](jpmorgan-footprint.json) | [Report](jpmorgan-solutions.md) · [Data](jpmorgan-solutions.json) |
| Nucor | [Report](nucor-footprint.md) · [Data](nucor-footprint.json) | [Report](nucor-solutions.md) · [Data](nucor-solutions.json) |

Original source files are retained where downloadable. The review checks transcription, arithmetic and accounting boundaries; it is not independent environmental assurance, facility engineering diligence or a verification of every future project outcome.
