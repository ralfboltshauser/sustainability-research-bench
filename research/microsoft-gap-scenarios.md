# Microsoft: a quantified available-technology gap

**Supported conditional result: 15% less climate impact for equivalent source-matched compute service, worth $38,268 in modeled avoided climate damage per 1,000 baseline lifecycle tonnes.** This is a normalized engineering opportunity, **not Microsoft's total gap**, an observed dollar loss, or fund revenue.

| Measure | Present air-cooled practice | Source-model cold plates | Available-technology difference |
|---|---:|---:|---:|
| Lifecycle GHG, per 1,000 baseline tCO2e | 1,000 t | 850 t | **150 t avoided; 15%** |
| Modeled climate damage, 2024 USD | $255,120 | $216,852 | **$38,268 avoided** |
| Lifecycle blue water, separately per 1,000 baseline m³ | 1,000 m³ | 690 m³ | **310 m³ avoided; 31%** |
| Nonrenewable primary energy, separately per 1,000 baseline MJ | 1,000 MJ | 850 MJ | **150 MJ avoided; 15%** |

The three physical denominators are separate normalizations, not an assertion that a cohort emitting 1,000 tonnes consumes 1,000 m³ or 1,000 MJ. Residual-impact scores, with each baseline set to 100, are **85 for climate, 69 for water, and 85 for primary energy**. These compare designs, not companies. They are not added into a composite score.

## Source and calculation

The [original Microsoft/WSP Nature study](https://www.nature.com/articles/s41586-025-08832-3), Table 4, printed p336, reports these cold-plate reductions against its air-cooled case using the 2021 US average grid. Its functional unit is annualized virtual-core service. Table 3 includes 20% overclocking, 28% more virtual cores and 3% lower PUE; the model assumes a 15-year datacenter and six-year servers. The [archived article](https://d-nb.info/137120098X/34) provides Figure 4 as normalized percentages. Its later one-kilogram-per-core example is explicitly illustrative; it cannot supply an observed absolute baseline.

The supplied Global Value Factors Database version 4 was independently checked: **GHGs worksheet H15 = 255.12**, with G15 specifying dollars per tCO2e. Its version note specifies a **2024 USD price year**. The workbook is archived at `sources/global-value-factors-v4.xlsx`.

Calculation: **1,000 × 15% = 150 tCO2e; 150 × $255.12 = $38,268**. This applies one selected damage valuation to the physical gap. It does not establish the precise realized harm from those emissions. Water remains a separate physical score because the life-cycle inventory's locations and matching water-damage factors are unavailable.

## Why this is feasible technology but not yet a fleet estimate

[Vertiv announced commercially available direct-to-chip equipment in June 2025](https://www.vertiv.com/en-emea/about/news-and-events/news-releases/vertiv-expands-liquid-cooling-portfolio-with-scalable-solutions-for-ai-and-hpc-applications/), including retrofit configurations. That supports technology availability. It does not establish that every Microsoft rack can adopt the model assumptions, preserve service/SLA, or complete conversion by 2031.

The normalized case adopts the alternative design within a precisely bounded comparison. A company-level 2031 calculation requires the **baseline lifecycle emissions G of the actual eligible cohort converted by then**, along with equivalent delivered service and engineering validation. Only then would the conditional gap be **0.15 × G tonnes**, valued at **$38.268 × G**. G is currently missing; it is not an arbitrary share of Microsoft's total emissions. Do not apply the water percentage to company on-site water consumption, or treat primary-energy savings as billed-electricity savings.

No cumulative five-year number is reported: this source is a lifecycle annualized service comparison, and deployment timing and emissions profiles are missing. Do not combine this case with a separate zero-evaporation design saving; that heat-rejection choice can raise electricity use.

## Pitch-ready statement

> Microsoft’s own peer-reviewed engineering study identifies a 15% climate-impact reduction for matched air-cooled compute service using available cold-plate technology. That is 150 tonnes—and $38,268 in modeled avoided climate damage—for each 1,000 baseline lifecycle tonnes. Its modeled water reduction is 31%. The next diligence step is identifying the unconverted, technically eligible fleet so this credible unit opportunity can become a defensible company-scale estimate.

The investor-additional gap is a further subset: installed and committed work must be excluded, and new capital must cause extra or earlier conversion. Repayment must come from contracted cashflows or measured cost savings. The modeled damage dollars do not repay principal.
