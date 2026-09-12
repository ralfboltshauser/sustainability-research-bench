# Independent bounded QA: Walmart and ExxonMobil

Review date: September 12, 2026. Reviewed the available Walmart footprint Markdown/JSON and solutions Markdown/JSON, and ExxonMobil footprint Markdown/JSON and solutions Markdown. ExxonMobil solutions JSON was not available at the initial file check; no work was delayed for it. This is a targeted source/arithmetic review, not independent verification of company measurements or a literature survey.

## Outcome

No decision-changing numerical transcription or arithmetic errors were found in the requested source pools and denominators. One boundary omission should be corrected in the **Walmart solutions** files: the CY2025 food mass is labeled global Walmart without saying **India excluded**. The footprint file already states this correctly. No other researcher's file was edited.

## Walmart checks

Primary source: [FY2026 ESG Report](https://corporate.walmart.com/content/dam/corporate/documents/esgreport/2026/FY2026-Walmart-ESG-Report.pdf), preserved as `sources/walmart-2026-esg.pdf` and `.txt`.

| Check | Independent result | Verdict |
|---|---|---|
| Onsite refrigerants, p31 | 4.08 million tonnes CO2e | Matches footprint and solutions. Direct onsite refrigerants only; transport/mobile refrigerants are in a separate 2.28 Mt source. |
| Scope 1, p31 | 4.08 + 2.28 + 1.80 = 8.16 MtCO2e | Correct. |
| Scope 2 market-based, p31 | 6.23 electricity + 0.01 steam = 6.24 MtCO2e | Correct. |
| Operational total, pp30–31 | 8.16 + 6.24 = 14.40 MtCO2e | Correct denominator for onsite-refrigerant operational share, not a full value-chain footprint. |
| Refrigerant shares | Rounded amounts imply 28.333% of operational total and 50.000% of Scope 1; source reports 28.4% and 50.1% | Differences compatible with underlying unrounded figures. Preserve source percentages as reported, label ratios calculated from rounded numbers separately. |
| Prior progress, p31 | 619 US facilities fully **or partly** use ultra-low-GWP systems; reference date December 31, 2025 | Correctly not treated as completed global conversion share. Source explicitly says capital plan funds replacements; additionality caveat is necessary. |
| CY2025 food disposal, p137 | 1,420 million lb × 0.45359237 kg/lb ÷ 1,000 = 644,101.1654 metric tonnes | Conversion correct. Sensible presentation is approximately 644,000 tonnes; source mass is rounded, not accurate to fractions of a tonne. |
| All six listed food pathways, p137 | 878 + 225 + 669 + 247 + 54.2 + 1,420 = 3,493.2 million lb | Correct sum, but not automatically FLW-standard waste. Donation/feed and diversion must retain distinct treatment. |
| Food boundary, p137 footnote89 | India excluded from global food loss/waste reporting | Correct in footprint; omission in solutions Markdown/JSON should be repaired. CY2025 is separately labeled in table despite overall report heading FY2026. |

The normalized lighting arithmetic is correct: 100 MWh × 44% or 63% = 44 or 63 MWh, and × 1,000 kWh/MWh × historical $0.056/kWh gives $2,464 or $3,528. This check validates arithmetic only; this review did not retrieve the historical external DOE source. Similarly, 3,922 kgCO2e/kg divided by 1,000 is 3.922 tonnes CO2e/kg; external GWP-table provenance was not re-audited here. No remaining eligible fixture stock or 2031 adoption volume is established.

### Requested correction

In `walmart-solutions.json`, intervention `food_waste`, first evidence geography: change “global Walmart” to “global operational Walmart food reporting, excluding India”. Add the same exclusion to the food-baseline sentence in `walmart-solutions.md`. Do not change the numerical amount. This is a scope correction, not evidence that Indian activity is zero.

## ExxonMobil checks

Primary source: [2026 Advancing Climate Solutions report](https://corporate.exxonmobil.com/-/media/global/files/advancing-climate-solutions/2026/2026-advancing-climate-solutions-report.pdf), preserved as `sources/exxon-2026-acs.pdf` and `.txt`. The methane chart was independently inspected in `sources/exxon-methane.png` as well as extracted source text.

### Methane source pools: p39

Reported total approximately 142,000 tonnes CH4/year; upstream approximately 96%. The implied upstream base is **136,320 tonnes CH4/year**. Multiplying by each published rounded share yields:

| Upstream source | Reported share | Arithmetic tonnes CH4/year |
|---|---:|---:|
| Pneumatic devices | 10% | 13,632 |
| Fugitives | 27% | 36,806.4 |
| Engines | 19% | 25,900.8 |
| Flares | 15% | 20,448 |
| Tanks/storage | 5% | 6,816 |
| Vents | 17% | 23,174.4 |
| Other | 8% | 10,905.6 |

Shares sum **101%** and raw source pools sum **137,683.2 tonnes**, exceeding the upstream base by **1,363.2 tonnes**. Both research files correctly flag rounding and do not silently normalize. These are approximate source envelopes, not separately measured equipment pools, certified upper bounds or addable abatement estimates. The source's approximate inputs do not justify decimal precision in external presentation.

The solutions' displayed approximately 13,600 / 36,800 / 6,800 / 20,400 tonnes match sensible rounding. Its conditional tank calculation is correct: 6,816 × 95% = **6,475.2 tonnes CH4/year**, approximately 6,475. The 95% factor must apply to an eligible untreated source cohort, not all company methane; the solutions explicitly preserve this limitation.

### Corporate accounting and product boundaries: pp64–67

| Check | Independent result | Verdict |
|---|---|---|
| Operated Scope 1 + market Scope 2 | Published total 97 MtCO2e; component rows 90 and 8 | 90 + 8 = 98 reflects independently rounded rows; p67 explicitly allows rounding. Preserve reported 97, do not silently replace with 98. |
| Operated sector rows | 36 upstream + 39 downstream + 22 chemical = 97 | Correct. |
| Equity Scope 1 + market Scope 2 | 104 + 7 = 111 MtCO2e | Correct, alternative ownership allocation, not additive to 97 operated. |
| Equity sector rows | 46 + 40 + 25 = 111 | Correct. |
| Product-use Category 11 | 170 natural gas + 530 crude production = 700 MtCO2e | Correct extraction/production-based view. Refined-throughput 630 and petroleum-sales 720 are alternatives, explicitly not summed in source. Other 14 Scope 3 categories and nonfuel products omitted. |
| Routine upstream flaring | 4 million standard cubic feet/day × 365 = 1.46 billion standard cubic feet/year | Correct fixed-flow envelope. 150 million scf/day is broader total hydrocarbon flaring. No justified allocation of 5 Mt flaring GHG by ratio 4/150. |
| Energy | 1.4 billion GJ ÷ 3.6 million GJ/TWh = 388.889 TWh-equivalent | Correct conversion; not electricity consumption. |

The 700 Mt production-use quantity must remain separate from the operated inventory unless an explicit ownership/lifecycle bridge is established. It is not eliminated by fixing upstream leaks while maintaining the same fuel service. The files preserve this distinction.

The historical VRU economic arithmetic is also correct from the quoted inputs: 0.95 × 50 Mcf/day × 365 = 17,337.5 Mcf/year; × $3/Mcf = $52,012.50; less $7,200 O&M gives $44,812.50; $41,125 divided by that annual amount = **0.9177 years** simple recovery. This review did not re-retrieve the external EPA cost report; historical-price, omitted-cost and simple-versus-discounted-payback caveats remain mandatory.

## Review limits

Both baseline JSON files and Walmart solutions JSON parse successfully. No assurance is inferred from this transcription/arithmetic check. Source uncertainty, realistic adoption, additionality, costs, and local damages remain unresolved. This review did not independently re-check external technology literature, financial assumptions, S&P membership, or every secondary observation. No overall harm score or additive carbon/water valuation is supported.

## Coordinator resolution

The India exclusion was added to the Walmart solutions Markdown and the food-waste JSON evidence geography after this review. No numerical values were changed.
