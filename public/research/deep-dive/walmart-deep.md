# Walmart refrigeration: deeper evidence and unresolved net impact

Research cutoff: 12 September 2026. The live app has not been edited. Machine-readable evidence, suggested record updates and diagnostic calculations are in `walmart-deep.json`.

The reported **4.08 million tonnes CO2e** FY2026 onsite refrigerant baseline is correctly copied. A measured company-wide preventable amount still cannot be calculated: current gas mix, asset-level leakage, conversion eligibility, energy changes and the replacement counterfactual are missing. Keep the existing 25/50/100% coverage cases only as explicit sensitivities. Neither the company’s installation count nor its selected-project stock reduction supplies a defensible replacement for those assumptions.

## What the latest company evidence establishes

[Walmart FY2026 ESG report, printed p.31](https://corporate.walmart.com/content/dam/corporate/documents/esgreport/2026/FY2026-Walmart-ESG-Report.pdf) reports:

- Onsite refrigerant emissions of 4.08 MtCO2e and a 20.7% year-over-year decline. The decline is achieved inventory change, not an experiment identifying the contribution of replacement versus maintenance.
- 619 U.S. facilities using ultra-low-GWP systems **partly or fully** at December 31, 2025. Different facility types, fluids and degrees of conversion are included. There is no matching emissions denominator.
- Approximately 80% less **installed legacy refrigerant footprint** in some projects. The phrase does not define whether it is mass or GWP-weighted stock precisely; it is not annual leakage avoided or an average across Walmart.
- Transcritical CO2 refrigeration in all new Walmart stores and Sam’s Clubs; CO2 adoption for new remote condensing units.
- Existing capital funding for replacements as equipment reaches end of life, plus more than 600 in-house technicians.

The [FY2025 report](https://corporate.walmart.com/content/dam/corporate/documents/esgreport/2025/FY2025-Walmart-ESG-Report.pdf), Onsite Refrigerants section, reported 408 U.S. partial/full facilities for 2024. The difference is 211 reported facilities, not proof of 211 full-store conversions. Dividing either count by retail-store count would mix facility boundaries and still would not produce emissions-weighted coverage. No asset-by-asset conversion schedule was found in the reviewed disclosures.

## A useful historical gas-mix improvement, with limits

[Walmart’s 2024 CDP response](https://corporate.walmart.com/content/dam/corporate/documents/esgreport/2025/2024-Walmart-CDP-Response.pdf?cid=esgreport) identifies R-404A system leakage as the main reason refrigerant emissions increased in CY2023 (printed p.151, question 7.10.1). The gas-family breakdown reports 4,432,447 tCO2e of HFCs and 106,468 tCO2e of HCFCs, using AR5 GWPs (pp.154–155, question 7.15.1). This confirms relevant legacy chemistry, but is historical, covers broader Scope 1, and provides neither current blend shares nor emitted kilograms by refrigerant. It cannot recalibrate FY2026 eligibility. The response’s quantified investment example is lighting, not refrigeration (pp.207–208); its figures must not be borrowed for refrigeration payback.

A more defensible site-level calculation is:

`direct avoided tCO2e = (baseline emitted kg × baseline GWP − project emitted kg × project GWP) / 1000`

Cooling service must be equivalent. Emitted mass must be measured or modeled explicitly; it need not stay constant when system charge, pressures and maintenance change. Net operational savings then add baseline-minus-project electricity and fuel emissions. Installation losses, refrigerant recovery and equipment manufacture need separate treatment. Do not double count complete leak-prevention savings and complete refrigerant-replacement savings for the same system.

The [EPA’s 2011 leak-prevention guidance, p.2](https://www.epa.gov/sites/production/files/documents/leakpreventionrepairguidelines.pdf) gives R-404A GWP 3,922 under that table’s convention. Thus **one verified kilogram/year of avoided R-404A leakage equals 3.922 tCO2e/year** under that convention. This is a useful physical unit, not a current Walmart aggregate; GWP vintages must be aligned before comparison with inventories. The same guidance describes sub-5% store leakage as achievable with technology and practices. Walmart’s numerical leakage baseline is not disclosed in the reviewed latest report, so subtracting 5% from a generic 20–25% industry baseline would be unjustified.

## The external supermarket case has an unresolved conversion discrepancy

The [DOE/Navigant Hannaford study](https://www.energy.gov/sites/prod/files/2015/02/f19/Hannaford%20Study%20Report%201-22-2015_CLEAN.pdf) is a comparison of two external stores, not Walmart. Table V.2, printed p.20, gives direct impacts of 191 versus 0.1 tCO2e and net totals of 1,179 versus 1,003. The direct arithmetic is 99.9476%; the reported whole-store difference is approximately 15%. Equipment and piping/case premiums were about 40% and 10–15% respectively on different component denominators (p.6), not current Walmart bids. Few existing components are reusable in conversion (p.1); deployment economics depend on replacement timing. Maintenance was near the chain average, with additional pilot monitoring (p.18).

**The net result is source-reported, not independently validated.** The saved page image confirms these exact propane rows:

| Table V.2 row | Bradford conventional | Turner transcritical CO2 |
|---|---:|---:|
| Propane Usage — Site (MMBtu) | 766 | 1,543 |
| Propane Usage — Source (MT CO2 Eq.) | 13.18 | 26.56 |

Those pairs imply approximately **17.2 kgCO2e/MMBtu**. [EPA’s 2024 emission-factor table, p.1](https://www.epa.gov/system/files/documents/2024-02/ghg-emission-factors-hub-2024.pdf), gives **61.46 kgCO2/MMBtu for propane gas** and **62.87 for liquid propane**. This discrepancy is much larger than rounding. The image says MMBtu, not therm or cubic metres. The preceding text describes whole-store utility bills; no allocation multiplier is documented. The source-energy graph on p.19 does not explain a different unit in the table’s explicitly site-labelled row. We cannot establish whether the source error is the input unit, conversion, table transcription or another undocumented treatment without original bills/calculator inputs.

A diagnostic recalculation retaining the study’s rounded electricity/refrigerant emissions but using its printed propane MMBtu gives roughly **141–142 tonnes difference, or 11.6–11.7%**. This excludes combustion methane/N2O and upstream effects. It is **not a replacement validated estimate**, and is not transferable to Walmart. The table is labelled September 2013–July 2014 while the leak discussion describes a year-long measurement; do not silently annualize. The audit and original screenshot are preserved locally.

## Climate and financing implications

[ORNL’s 2018 research](https://www.ornl.gov/publication/integrated-supermarket-refrigeration-very-high-ambient-temperature) models alternatives across hot-climate cities. An ammonia/CO2 cascade outperformed the studied all-CO2 configuration by up to 12.23% in efficiency and 11.20% in total emissions under extreme warmth; all-CO2 performed better in cold/mild conditions. These are analytical comparisons between specific configurations, not measured Walmart savings. They establish why climate, architecture and heat recovery matter, rather than furnishing another universal percentage.

[Current EPA GreenChill certification criteria](https://www.epa.gov/greenchill/about-store-certification) assess refrigerant GWP, charge relative to cooling load, and emissions relative to load. This is a useful design for the missing asset dataset. Voluntary certification criteria are not a statutory conversion deadline.

Potential repayment sources are avoided refrigerant purchases, maintenance, energy and spoilage costs, measured net of added costs. Social damage valuation is not company cash flow. No defensible current Walmart refrigeration capex, payback or unmet finance volume was found in this bounded source review. Already funded replacement and new-store CO2 adoption belong in the baseline. Additional fund impact requires evidence that funding advances named assets or removes a documented capacity bottleneck, with credit only for the resulting incremental emissions difference before the baseline catches up.

## Recommended app treatment

Preserve the reported baseline. Label the 99.95% number as an external equal-mass direct sensitivity, with measured eligible share and net/additional fund impact left unknown. Add deployment, historical gas-family evidence, installation constraints and the unresolved net-study audit. Do not replace the current reduction factor with 80%, the source’s 15%, the diagnostic 11.6–11.7%, or an installation-count percentage. These quantify different boundaries.

Source images and the downloaded CDP/EPA originals are in `walmart-sources/`. The original Walmart and DOE full reports remain in the pilot’s `sources/` directory. Eight primary sources support this expansion; exact locators and short excerpts are indexed in the JSON.
