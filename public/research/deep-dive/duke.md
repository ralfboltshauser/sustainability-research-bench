# Duke Energy: verified inventory, conditional methane-recovery process

Research cutoff: 12 September 2026. Completed bounded primary-source review; app not edited.

**Strongest defensible result:** suitable pipeline maintenance recovery has an EPA benchmark of **50–90% recovered gas**. After charging complete combustion of recovered fossil methane, that corresponds to **454–817 tonnes CO₂e per 1,000 tonnes of qualifying baseline methane CO₂e**, before compressor and other lifecycle effects. This is a normalized candidate intervention, **not a measured Duke remaining gap**. No Duke annual deployable extent was established.

## Latest inventory

Duke's July 2026 [2025 Sustainability Metrics Center](https://s201.q4cdn.com/583395453/files/doc_downloads/2026/2025-Sustainability-Metrics-Center.pdf), p. 4, reports nine Scope 1 components in thousands of metric tonnes CO₂e. Their sum is **80,703,000 tCO₂e**: 79,000 + 150 + 224 + 393 + 162 + 164 + 524 + 82 + 4, multiplied by 1,000. This is a derived total from rounded inputs, not exact underlying emissions. Use approximately **80.7 million tonnes** in prose. Footnote 10, p. 8, uses ownership share of generating assets under Duke operational control at calendar-year end. Gas methane uses Subpart W and NGSI, with revised reporting provisions from 2025 (footnote 11).

At the pilot's fixed $255.12/tCO₂e factor, the direct inventory proxy is **$20.589 billion** modeled societal damage. It excludes other scopes and nonclimate harm and is not corporate liability or cashflow.

The [EEI/AGA template](https://s201.q4cdn.com/583395453/files/doc_downloads/esg-key-documents/2026/EEI_AGA_ESG_Template_Quantitative-2025_Final.pdf) is titled 2025 but its actual current data year is **2024**. Do not substitute it for 2025 inventory. Its gas page names Duke Energy Ohio and Piedmont Natural Gas. It has no remaining unprotected-steel/cast-iron mains; generic replacement of those pipes is therefore not a defensible outstanding Duke opportunity.

## Counterfactual and physical calculation

The service is safe scheduled maintenance of a pipeline segment while meeting required gas delivery and outage timing. Baseline is methane actually vented from a qualifying event without recovery. Alternative is in-line and/or portable compression that transfers gas to a connected operating pipeline before final depressurization. Already recovered gas and flared gas do not belong in this baseline.

[EPA's pipeline blowdown description](https://www.epa.gov/natural-gas-star-program/pipeline-blowdowns) confirms the source applies in distribution and transmission. [EPA pump-down lessons](https://19january2017snapshot.epa.gov/sites/production/files/2016-06/documents/ll_pipeline.pdf), pp. 1–3 and 7, supplies the 50–90% benchmark and identifies pressure, connections, compressor availability and planned-maintenance constraints. [EPA's TransCanada case](https://19january2017snapshot.epa.gov/sites/production/files/2016-06/documents/ngspartnerup_fall09.pdf), p. 1, independently underscores that only a subset of events is practical and economical. Recovery must not extend outages or compromise safety beyond the accepted service definition.

Use [IPCC AR6 WGIII Annex II, Table 11](https://www.ipcc.ch/report/ar6/wg3/downloads/report/IPCC_AR6_WGIII_Annex-II.pdf): fossil fugitive methane GWP100 = 29.8. Complete combustion yields 44/16 = 2.75 tonnes CO₂ per tonne methane. With recovery fraction r:

`avoided tCO₂e = baseline methane tCO₂e × r × (29.8 − 2.75) / 29.8`.

| Recovery assumption within EPA benchmark | Reduction before other lifecycle effects | Modeled damage proxy per normalized block |
|---|---:|---:|
| 50% | 453.859 tCO₂e | $115,789 |
| 90% | 816.946 tCO₂e | $208,419 |

These are conditional performance cases, not a statistical uncertainty interval or guaranteed lower bound. The app JSON defaults to the 50% case and retains the upper case in its formula. The normalized block uses AR6 methane equivalence; Duke's reported CO₂e cannot silently be treated as the same GWP basis.

Net lifecycle savings remain unknown: measure compressor fuel/electricity, any incremental methane leakage, mobilization and equipment burdens, other gas constituents and downstream leakage. No displaced gas production credit is assumed. Charging all recovered-gas combustion is a cautious boundary choice; delivering fixed customer gas service could displace other supply, but that counterfactual has not been established.

## Extent and financing

Duke's reported gas methane category is **393,000 tCO₂e** for 2025, but includes sources other than untreated eligible blowdowns. It is contextual inventory, never a valid scaling baseline for this technology. Needed: event-level vented mass, pressures, connections, current recovery/flaring practice, planned dates, service requirements and equipment availability. Company-scale reduction is unavailable, not zero.

EPA's historical Southern Natural Gas example, p. 7, reports 32,550 Mcf recovered in 1998, cost $68,100 on a 2006 basis, $7/Mcf valuation and $159,900 net savings. It illustrates a possible retained-product repayment mechanism; it is not a current equipment quote, Duke project, or assured fund return. Project economics need contemporary bids, gas ownership, tariff treatment, annual utilization and contracts. Additional financing must cause extra or earlier recovery beyond existing commitments.

## Other evidence and rejected shortcuts

[Historical Duke gas-transmission presentation hosted by EPA](https://www.epa.gov/sites/default/files/2017-06/documents/segura_2005aiw.pdf) confirms this is long-established technology. Its old corporate name does **not** establish applicability to today's Duke asset boundary, so none of its historical savings is counted as remaining opportunity.

[Duke's 2020 strategy release](https://news.duke-energy.com/releases/duke-energy-unveils-sweeping-clean-energy-and-emissions-reduction-plan-at-inaugural-esg-day) already announced removal of cast iron and bare steel. This supports excluding that tempting generic intervention.

Coal-to-solar emission intensities alone do not preserve firm power, hourly energy, grid constraints or reliability. A defensible coal retirement alternative needs asset-specific dispatch/replacement modeling with methane supply-chain impacts and capacity accreditation. No such net company-scale number was established here; corporate targets are not a technology frontier.

[S&P's 2016 index announcement](https://press.spglobal.com/2016-03-11-Danaher-Duke-Energy-and-NextEra-Energy-Set-to-Join-the-S-P-100) explicitly identifies Duke as an S&P 500 constituent. This verifies historical membership only; a dated September 2026 provider constituent file was not obtained.

## Audit artifacts and failures

Original inventory, EEI/AGA and EPA technology PDFs plus extracted text are archived under `sources/duke/`. Exact locators above identify important source passages; `duke.json` carries structured evidence records. The company Impact Report link failed to load; the directly linked Metrics Center succeeded. The IPCC WGI chapter was blocked; the official WGIII annex provided the needed factor. No evidence was inferred from either failed retrieval.
