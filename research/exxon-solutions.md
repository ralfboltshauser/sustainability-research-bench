# ExxonMobil: commercially available interventions and a fundable pilot

Research cutoff: 12 September 2026. This is an operational improvement assessment at fixed 2025 activity, not a forecast of ExxonMobil production or a claim that reducing operational emissions solves product combustion. Public information supports source envelopes and a conditional equipment scenario; it does **not** establish a defensible company-wide feasible reduction by 2031 or a repayable billion-dollar allocation.

## Baseline and boundaries

ExxonMobil reports approximately 142,000 tonnes CH4 in 2025, with 96% upstream. The source chart allocates upstream methane to pneumatics 10%, fugitives 27%, engines 19%, flares 15%, tanks/storage 5%, vents 17%, and other 8%. Rounded shares total 101%; do not normalize them silently. These are company estimates, not independently measured source totals. [Company methane chapter, source chart and footnote 8](https://corporate.exxonmobil.com/Publications/Advancing-Climate-Solutions/driving-reductions-in-methane-emissions). The chart was independently inspected visually and saved as `exxon-methane-sources.png`.

| Source | Approximate 2025 operated upstream source pool, t CH4/year | Calculation |
|---|---:|---|
| Pneumatic devices | 13,600 | 142,000 × 0.96 × 0.10 |
| Fugitive leaks | 36,800 | 142,000 × 0.96 × 0.27 |
| Tanks/storage | 6,800 | 142,000 × 0.96 × 0.05 |
| Flares | 20,400 | 142,000 × 0.96 × 0.15 |

These pools identify where to investigate; they are **not** a 2031 abatement estimate. Eligibility, existing controls, replacement timing, new leaks, and implementation already planned all matter.

Company operated emissions are 97 MtCO2e combined Scope 1 and market-based Scope 2 in 2025. Routine upstream flaring is 4 million standard cubic feet/day, versus 150 million for total hydrocarbon flaring. The extraction-based use-of-products estimate is 700 MtCO2e; alternative refinery and sales boundaries must not be added to it. [Metrics table, flaring rows and Scope 3 section](https://corporate.exxonmobil.com/publications/metrics-and-data). The footprint companion report contains full accounting details.

## Four interventions

### 1. Replace remaining gas-driven pneumatic controllers

Use electric controllers, mechanical controls where functional requirements allow, or instrument air with dependable power and backup. EPA's engineering assessment specifies 100% elimination of the **controller's direct natural-gas emissions**, not lifecycle emissions. Electricity, compressed-air leaks, maintenance and backup equipment remain. [EPA technical proposal, printed page 355](https://www.epa.gov/system/files/documents/2021-11/san-8510-ong-climate-review-proposal-frn-2021-11_1.pdf).

Heritage Permian devices are already eliminated; Pioneer replacement is planned by 2030, with more than 6,000 replaced during 2025. Monitoring is also already being expanded. These facts preclude presenting basic deployment there as automatically additional. [Company methane chapter](https://corporate.exxonmobil.com/Publications/Advancing-Climate-Solutions/driving-reductions-in-methane-emissions).

The approximately 13,600 t CH4/year source pool is a ceiling, not wholly eligible US equipment. For a surveyed device cohort, direct annual reduction equals measured baseline venting minus verified post-installation venting. Current equipment quotes, remaining device inventory, controller duty cycles and site electricity are absent. No contemporary corporate cost or payback is claimed. Gas retained for sale can repay equipment only if the borrower actually owns that gas and can deliver it economically.

### 2. Capture remaining low-pressure tank vapors

Install or repair vapor recovery units (VRUs), sealed collection piping and pressure controls at eligible tank batteries. EPA permits a 95% reduction factor against **pre-VRU emissions of the specific controlled source**, reflecting approximately 95% operating availability. This applies to appropriate low-pressure storage/vent sources with reliable power and a gas outlet; it is not 95% of all company venting. [EPA VRU page, Description / Applicability / Methane Emissions Reductions](https://www.epa.gov/natural-gas-star-program/vapor-recovery-units).

ExxonMobil identifies VRU retrofits on existing tanks and pressurized closed vessels in new builds. Therefore this is deployed technology within its operations, but remaining eligible units are undisclosed. [Company methane chapter](https://corporate.exxonmobil.com/Publications/Advancing-Climate-Solutions/driving-reductions-in-methane-emissions).

Conditional source envelope: if all reported tank/storage emissions were uncontrolled, suitable for VRUs, and sustainably captured, 0.95 × 6,816 = 6,475 t CH4/year. **This is an engineering ceiling, not a feasible adoption case**: existing VRU downtime, pressure-relief events, already controlled tanks and scheduled retrofits invalidate blanket application. The deployable amount must instead be 0.95 times the measured eligible untreated cohort, with post-installation validation.

**Computable equipment scenario, explicitly historical rather than a current quote:** EPA's Exhibit 6 gives a 100 Mcf/day unit at half-capacity average feed, $41,125 installed cost and $7,200 annual O&M, with gas valued at $3/Mcf. The source's annual recovery formula is 0.95 × 50 × 365 = 17,337.5 Mcf. This yields $52,012.50 gross/year and $44,812.50/year before financing, tax and omitted connection costs; simple principal recovery is 0.918 years. Exhibit 6 rounds gross value to $52,015 and reports a different discounted-payback result; do not conflate that with this transparent simple-payback calculation. These are old nominal US costs, not inflation-adjusted 2026 economics. [EPA historical VRU report, Exhibits 5–6, printed pp. 7–8](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1004FDH.TXT).

A current pilot must replace every price with a vendor quote and contractual netback, meter actual recoverable gas, include connection/power costs and avoid treating gas volume as pure methane mass. At measured recovery Q and netback P, available annual repayment is Q×P minus power, maintenance, transport, verification and other cash costs. This is a usable underwriting equation, not a financing promise.

### 3. Find and repair persistent and recurrent leaks

Use ground optical gas imaging/quantification plus aerial or continuous screening, fast repair and remeasurement. Detection alone saves no methane. A published randomized study of roughly 200 Canadian sites found about 50% fewer leaks in treatment sites relative to controls, but control-site emissions also fell about 36%. Leak-count improvement cannot be substituted for a methane-mass reduction factor. [Wang et al., 2024, original research abstract](https://pubs.acs.org/doi/abs/10.1021/acs.est.3c09147).

A separate Alberta field study reports total emissions falling 44%, with fugitives falling 22% and vents 47% across follow-up surveys; its mixed sources and uncontrolled changes make 44% unsuitable for multiplication by Exxon's total methane baseline. [Ravikumar et al., original authors' institutional record](https://eao.stanford.edu/publications/journal-articles/repeated-leak-detection-and-repair-surveys-reduce-methane-emissions).

The 36,800 t CH4/year company fugitive pool is the relevant starting envelope. The 2031 increment depends on the uncovered sites, current inspection/repair performance, leak persistence and recurrence. Measure time-integrated reductions against a matched maintenance counterfactual. Avoid assuming continuous monitoring benefits that the company already plans to obtain. Repairs that retain gas have a possible cash stream, but survey costs recur and many sites will have little economically recoverable leakage.

### 4. Recover remaining routine flared gas and improve necessary flare reliability

Gas gathering/compression, reinjection where appropriate, and a verified useful gas outlet can displace routine flaring. Necessary safety flares need reliable ignition and combustion control. Improving destruction converts methane to CO2, so it reduces methane but does not eliminate greenhouse emissions. A US three-basin study measured effective destruction of 91.1% (95% interval 90.2–91.8%), including unlit flares. This is evidence to **measure Exxon flares**, not an Exxon performance assumption. [Plant et al., original study abstract](https://pubmed.ncbi.nlm.nih.gov/36173866/).

**Bounded company volume scenario:** hold disclosed 2025 routine upstream flare flow fixed. Implementing the existing zero-routine-flaring commitment would divert at most 4 million scf/day × 365 = **1.46 billion scf/year** from this baseline by 2031. This is an observed-baseline volume envelope attached to a stated commitment, not a promise all gas can be sold. [Company flaring metric and footnote 9](https://corporate.exxonmobil.com/publications/metrics-and-data). No fabricated uptake fraction is used. The feasible volume is lower if gathering, reinjection or permitting fails; grant additionality can be zero if the company would complete the work anyway.

Do not multiply total flaring CO2e by the routine/total gas-volume ratio: composition and destruction efficiency differ. Likewise, the upstream flare methane pool includes non-routine and safety sources; it cannot all be attributed to the routine volume. Composition, flare-specific flow and methane-slip measurements are required to calculate climate benefit. Gas burned by a customer largely moves combustion from Scope 1 to Scope 3; a full lifecycle comparison must include that combustion and gathering energy/leakage. A flare-ignition improvement alone has no captured-gas sales revenue.

## Electrification and efficiency: technically credible, unquantified residual

Electric motors and low-emission power can reduce compressor/engine combustion and methane slip. ExxonMobil lists Permian electrification and contracts enabling 4 GW of renewable capacity, while the integrated Permian net-zero plan is now 2035. [Company operating plans, unconventional operations](https://corporate.exxonmobil.com/publications/advancing-climate-solutions/positioned-for-growth-in-a-lower-emission-future). Contracted generation capacity is not metered energy supplied to a particular engine. Without engine fuel/shaft work, electric motor efficiency, remaining conversion inventory and hourly power emissions, a corporate reduction factor would be invented. Use actual avoided fuel emissions minus electricity and equipment lifecycle emissions; do not claim zero physical emissions merely from certificates. This opportunity is retained for diligence, rather than added as an unsupported fifth quantified intervention.

## 2031 rollout and principal-recovery test

First reconcile source measurements and select an equipment cohort whose work is absent from funded company plans. Then obtain firm quotes, gas ownership/offtake terms, permits and outage dates; install commercial equipment, independently verify persistence and finance further cohorts only from demonstrated results. No assumed fraction of corporate equipment is inserted into this sequence. The company-wide 2031 feasible total remains **not established**, and the fund-attributable reduction remains **not established**, until those inputs exist.

For a principal-only fund, a capped equipment loan or lease repaid from incremental metered gas net receipts could work for selected VRUs, pneumatic replacements and leak repairs. Repayment stops when principal and explicitly agreed administration costs are recovered; philanthropic objectives do not eliminate default or commodity-price risk. Avoided climate damage is not revenue, and no carbon-credit revenue or methane penalty saving is included. Jurisdictional compliance obligations require site-specific review before assessing additionality. Financing a financially strong operator's already economic or committed work may simply replace its own capital.

IEA's current 2026 assessment identifies existing technologies and profitable methane opportunities globally, but also highlights ownership and contractual barriers. Its sector abatement share is **not** multiplied by Exxon's inventory. [IEA key findings](https://www.iea.org/reports/global-methane-tracker-2026/key-findings), [financing barriers](https://www.iea.org/reports/global-methane-tracker-2026/strategies-to-speed-action).

Maintain one source-event ledger across all measures: a tank repair found by LDAR and then routed to a VRU is one abatement, not two. Separately report methane mass, combustion CO2, electricity, VOC/air-quality effects and financial receipts. None of these interventions establishes reductions in freshwater use, spills, waste, biodiversity damage or sold-product demand. Those need separate evidence. Fixed output also excludes an assumed societal transition to different energy services; such substitution is a separate counterfactual.

### Missing inputs that determine the answer

- Asset-level 2025 measured emissions, source classification and uncertainty; continued fixed-output operational relevance through 2031.
- Remaining device/tank/flare inventory, control coverage, equipment life and existing funded/mandatory replacement schedule.
- Source-specific methane fraction, gas standard conditions/heating value and measurement of event duration and recurrence.
- Current installed bids, electricity/connection and maintenance costs, gas ownership, binding netback/offtake, taxes and credit terms.
- Site feasibility, grid/interconnection, permits, emergency-service constraints, partner approvals and contractor availability.
- A credible without-fund counterfactual and verified timing difference, to distinguish accelerated reductions from substituted finance.
