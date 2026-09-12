# Quantified damage and current-technology gaps

**Research update:** the [expanded eight-company audit](expansion/RESEARCH-UPDATE.md) is the latest synthesis. It adds three company cases, 92 app evidence records, source-specific caveats and deeper Walmart, ExxonMobil and Microsoft reviews. The company-scale cases below remain conditional sensitivities.

The useful claim is a modeled gap between present environmental burdens and the burdens of an explicitly defined alternative using available technology. Public data can support calculations under stated assumptions before every deployment detail is known. Those calculations must remain visibly conditional; a chosen adoption share is not discovered evidence that the corresponding harm is unnecessary.

## Three numbers for each problem

1. **Damage magnitude:** the physical burden and, where a model supports it, estimated societal damage.
2. **Technology gap:** the reduction relative to that burden for a specific available alternative delivering equivalent service.
3. **Deployable extent:** the share of affected activity that can actually adopt the alternative within the stated period. Unknown extent is represented by explicit sensitivities, not hidden in the score.

For a selected activity: **avoidable burden = baseline burden × eligible-and-converted share × reduction on converted activity − additional burdens caused elsewhere.** Its gap percentage uses the same baseline boundary. This activity score does not become a whole-company score merely because it is attached to a company name.

## Climate damage valuation

The current public [Global Value Factors Database V4](https://capitalscoalition.org/wp-content/uploads/2026/07/Global-Value-Factors-Database-V4-2026-External.xlsx), linked by the [Impact Value Standards Board](https://capitalscoalition.org/impact-value-standards-board-ivsb/), provides **$255.12 per tonne CO2e**, expressed in **2024 US dollars**. It was extracted from the GHGs worksheet, cell H15; worksheet update June 18, 2026. The original workbook is preserved locally.

Here that same factor is used for a screening comparison across reporting years. This is a fixed-factor proxy, not an emission-year-specific valuation, confidence interval, company liability, or financial investment return. The result represents modeled future societal damages associated with one reporting year's emissions; it is not damage observed entirely during that year. Monetary valuation depends on scientific and normative assumptions, including discounting and use of CO2 equivalence. It is not an objective price of all planetary harm.

Applying the factor to an intervention's emissions difference is our analytical extension. The [IFVI GHG methodology](https://ifvi.org/methodology/environmental-topic-methodology/greenhouse-gas-ghg-emissions-topic-methodology/) supports inventory valuation but explicitly does not itself establish avoided-emissions claims. Such claims need the separate physical counterfactual.

## Direct climate damage across the five companies

The following deliberately uses **Scope 1 only**, so it has a named common accounting scope. It excludes purchased electricity, suppliers, products, financing, water, pollution and nature. Consequently this is a direct-climate-damage comparison, not a fair all-sustainability ranking: it misses much of the impact associated with a bank or technology business. Organizational control boundaries and reporting periods also differ.

| Company | Reported direct emissions | Modeled damage associated with that reporting year's direct emissions |
|---|---:|---:|
| ExxonMobil, 2025 operated assets | 90.0 million tCO₂e | **$22.96 billion** |
| Walmart, FY2026 | 8.16 million tCO₂e | **$2.08 billion** |
| Nucor, 2025 company boundary | 6.60 million tCO₂e | **$1.68 billion** |
| Microsoft, FY25 | 170,887 tCO₂e | **$43.6 million** |
| JPMorgan Chase, 2024 | 100,024 tCO₂e | **$25.5 million** |

Original inventory sources and boundaries: [ExxonMobil](https://corporate.exxonmobil.com/publications/metrics-and-data), [Walmart p. 31](https://corporate.walmart.com/content/dam/corporate/documents/esgreport/2026/FY2026-Walmart-ESG-Report.pdf), [Nucor p. 37](https://indd.adobe.com/view/publication/cc4a577c-36f1-4ae0-a823-7e9f3f547ca5/4a1d/publication-web-resources/pdf/2025_Sustainability_Report.pdf), [Microsoft Table 1A](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf), [JPMorgan operational inventory](https://www.jpmorganchase.com/content/dam/jpmorganchase/documents/2024-operational-ghg-emissions-and-electric-power-use.pdf). Reproducible inputs, calculations and metadata: [climate-damage-baselines.csv](climate-damage-baselines.csv), [JSON](climate-damage-baselines.json).

## Walmart: a material refrigeration gap

Walmart's onsite refrigerant emissions are **4.08 million tCO₂e** in FY2026, approximately **$1.04 billion** in modeled climate damage. A [DOE/Navigant paired-supermarket study](https://www.energy.gov/sites/prod/files/2015/02/f19/Hannaford%20Study%20Report%201-22-2015_CLEAN.pdf), printed pp. 19–20, compared similar refrigeration loads. At the same reported leaked mass, HFC equipment produced 191 tonnes CO2e versus 0.1 tonnes for CO2 equipment: approximately **99.95% less direct refrigerant climate impact**. The source reports about 15% lower whole-store operational emissions. The later audit found an unresolved propane unit/conversion discrepancy, so this figure is not treated as a validated net reduction factor; see [the deeper Walmart audit](expansion/walmart-deep.md). Additional energy and other effects matter. This is an observed comparison with limitations, not a randomized causal test or a universal fleet factor.

**Conditional transfer to Walmart:** assume systems responsible for a specified share of its refrigerant emissions are suitable for conversion and achieve comparable direct performance by 2031. The share refers to emissions, not store count.

| Assumed eligible and converted emissions share | Direct reduction after conversion | Share of operational Scope 1 + market-based Scope 2 inventory | Modeled direct damage avoided from one year's reduced emissions |
|---|---:|---:|---:|
| **If 25%** | **1.02 million tCO₂e/year** | **7.08%** | **$260 million** |
| **If 50%** | **2.04 million tCO₂e/year** | **14.16%** | **$520 million** |
| **If 100%** | **4.08 million tCO₂e/year** | **28.32%** | **$1.04 billion** |

These are sensitivity cases, not a forecast range. The 100% case is an all-source substitution benchmark with unproven universal applicability. Gas mix, actual leakage, equipment age, climate, replacement timing and labor capacity determine feasible coverage. Net lifecycle savings require subtracting additional electricity, fuel and embodied emissions. Existing conversions are already in the baseline. There is no established positive lower bound for the *new fund's* effect.

**Usable pitch:** “Walmart reports a billion-dollar-scale modeled climate burden from refrigerant leaks. Existing refrigeration technology demonstrates that most direct impact can be removed in suitable equipment. If systems responsible for half that source can be converted with comparable performance, the direct opportunity is about 2 million tonnes annually, before energy and lifecycle effects.”

Detailed evidence: [refrigeration scenarios](walmart-gap-scenarios.md).

## ExxonMobil: capture methane, count the resulting CO2

The reported methane inventory and source shares imply approximately **6,800 tonnes CH4/year** from upstream tanks/storage. This is an approximate source pool, not an inventory of untreated eligible tanks. EPA's [vapor-recovery method](https://www.epa.gov/natural-gas-star-program/vapor-recovery-units) uses 95% capture for suitable sources. [IPCC AR6 Table 7.15](https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter07.pdf) gives fossil methane GWP100 of 29.8.

For methane recovered and completely burned, the calculation subtracts 2.75tonnes CO2 for each tonne CH4 burned. It does not assume recovered gas displaces other production. Added recovery/compression power, downstream leakage, other hydrocarbons and equipment impacts remain unquantified.

| Assumed eligible untreated source share | Reduction after recovered methane combustion, before other lifecycle effects | Modeled climate damage avoided from one year's reduction |
|---|---:|---:|
| **If 25%** | **43,800 tCO₂e/year** | **$11.2 million** |
| **If 50%** | **87,600 tCO₂e/year** | **$22.3 million** |
| **If 100%** | **175,000 tCO₂e/year** | **$44.7 million** |

The 95% equipment methane-control factor becomes about 86.2% of the treated source's GWP100 burden after this combustion adjustment, before other lifecycle effects. This illustrates why the relevant technology gap is a modeled physical difference, not a marketing efficiency percentage. None of these scenarios establishes the actual untreated share or additional funding need. Details: [methane scenarios](exxon-gap-scenarios.md).

## Microsoft and Nucor: quantify the supported process, not an invented fleet total

For a cooling cohort that matches the original study's functional unit and design assumptions, Microsoft-related research supports a **15% lifecycle climate reduction** and a separate **31% lifecycle blue-water reduction**. Per 1,000 tonnes of matching baseline lifecycle emissions, that is 150 tonnes avoided, or **$38,268** in modeled climate damage. The company's total footprint and onsite water consumption are not valid scaling denominators for that study. [Cooling calculation and original-study references](microsoft-gap-scenarios.md)

At Nucor Seattle, supplier-reported furnace controls demonstrated **5% lower furnace electricity use**. If repeated at genuinely comparable unoptimized equipment, that is 50 MWh saved per 1,000 MWh of qualifying baseline electricity. Seattle's own installation already happened; it is not remaining gap. No unsupported enterprise conversion rate or electricity-damage factor is supplied. [Original Tenova case](https://tenova.com/newsroom/press-releases/tenovas-nextgenr-i-eafr-and-water-detection-technologies-significantly)

Nucor also has a **7.23% current-to-target hot-rolled product intensity gap**. Reaching that target corresponds to approximately **$19.39 less modeled climate damage per tonne of matching product**, or **$19.39 million per normalized 1 million-tonne annual output block**. This remains a target scenario, not independently established available-technology potential; it must be labeled separately. [Nucor report pp. 38,41](https://indd.adobe.com/view/publication/cc4a577c-36f1-4ae0-a823-7e9f3f547ca5/4a1d/publication-web-resources/pdf/2025_Sustainability_Report.pdf)

For JPMorgan, no bank-wide technology-gap percentage is established. A useful next score would concern named borrower assets and the physical improvements financing could enable. Treating reduced portfolio exposure as prevented planetary damage would be false. The existing pilot contains quantified historical project examples, explicitly not identified JPMorgan borrowers.

## Water and other damage

Multiple scores are appropriate when they preserve meaningful units and boundaries. Microsoft's FY25 consumption is 8.17 million cubic metres, with 3.926 million in high/extremely high baseline water-stress areas. This is **48.1% of reported consumption exposed to high baseline stress**, not 48.1% avoidable water damage. Source: [Microsoft Table 8](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf).

The current valuation database does provide water-impact factors, but applying national or basin factors to these regional/global totals would invent the missing location distribution. No monetary water, biodiversity, or pollution damage score is assigned in this update. Missing scores are unavailable, not zero. Climate valuation must not be relabeled as total sustainability damage.

## The key message

**“The gap is the environmental cost of continuing with today's practices when a lower-impact technology can deliver the same service.”**

The evidence supports specific process comparisons and conditional company-scale scenarios. It does not prove that every modeled tonne is currently unnecessary or that all obstacles are technological. A defensible demonstration shows the source, the alternative, the quantified difference, the coverage assumption and the remaining constraints together. This lets the pitch be concrete without inventing certainty.

The dollar values in this report describe modeled societal damage associated with emissions, never cash available to repay the billion-dollar fund. Investment selection still needs deployment costs, repayable cashflows and evidence that the funding changes the outcome.
