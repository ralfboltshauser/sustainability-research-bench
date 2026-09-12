# Project context and continuation guide

This repository is an evidence-led sustainability research prototype called **the gap.** It asks how much environmental harm could be prevented through specific available technologies, then connects those opportunities to possible investments. It currently demonstrates eight company cases. **It does not establish a defensible whole-company preventable-damage ranking, an automated S&P 500 research system, or an underwritten investment portfolio.**

This is the main handoff for a person or AI agent continuing the work. It records the original intent, decisions, completed work, known limitations, and the path to a rigorous system. The research snapshot is September 12, 2026; statements about deployments, assurance and technology availability need rechecking in later work.

- [Live application](https://preventable-gap-app.vercel.app)
- [Repository README and setup](README.md)
- [Latest research synthesis](research/expansion/RESEARCH-UPDATE.md)
- [Dataset used by the application](app/data.json)
- [Agent entry point](AGENTS.md)

## 1. Original goal

The hackathon asked for a data-driven sustainability score for S&P 500 companies. Its bonus challenge asked how to invest one billion dollars for maximum impact. The capital could go into companies, startups, equipment, projects or other investments; it was not restricted to public stocks. The financial objective was to recover principal, without needing to generate a profit.

The concern was that another opaque or slightly different ESG score would add little value. Existing scores and underlying data can be difficult to access, and a score of current corporate performance does not directly answer where new funding can cause improvement.

The chosen question became:

> What environmental burden is associated with this company, what available alternative could reduce it while delivering comparable service, and what would enable that change?

The ambition is eventually to aggregate these opportunities across companies into shared problem areas worth financing. A startup addressing the same bottleneck at many companies could matter more than buying shares in whichever company has the best sustainability rating.

## 2. How the approach evolved

| Stage | Decision | Reason |
|---|---|---|
| Generic sustainability ranking | Move toward a decision-specific improvement gap | A current-footprint ranking does not establish what an investment changes. |
| “Unnecessary damage” pitch | Use “potentially preventable harm” in the analytical product | Technology availability alone does not prove applicability, reasonable deployment timing or absence of constraints. |
| One universal score | Separate absolute reduction, relative improvement and evidence | Large opportunities and large percentages answer different questions. Evidence uncertainty should not disappear inside a blended score. |
| Whole-company estimates | Begin with bounded activities and normalized process comparisons | Public reports often omit the asset-level denominators needed to scale an intervention. |
| Five-company pilot | Research Microsoft, Walmart, ExxonMobil, JPMorgan Chase and Nucor | Deliberately different business models expose accounting and comparability problems. |
| Quantified damage | Add an explicit climate valuation model | Monetary screening can communicate magnitude, but must not pretend to measure all environmental harm or investment returns. |
| App prototype | Show sources, formulas, assumptions and missing evidence in the interface | The score needs to be inspectable, not merely visually convincing. |
| Deeper audit and expansion | Add UPS, Delta and Duke; revisit the strongest original cases | More scrutiny uncovered consequential denominator, deployment and source-quality limitations. |

Parallel research agents performed company-footprint and intervention investigations, followed by deeper reviews and reconciliation. Their outputs were checked against original reports and studies, with arithmetic reproduced and findings assembled into the app dataset. This describes how the pilot was produced; **there is no deployed agent fleet or autonomous research backend in the application.**

## 3. What the proposed scores mean

### Three different quantities

1. **Baseline burden:** a reported or calculated physical quantity within a defined boundary, such as direct greenhouse-gas emissions or water consumed.
2. **Potentially preventable amount:** the modeled difference produced by an explicitly defined alternative and deployment case.
3. **Improvement gap:** that difference divided by the baseline of the same assessed activity.

A simplified screening calculation is:

```text
Potentially preventable burden
  = activity baseline
  × eligible-and-converted activity share
  × reduction on converted activity
  − additional burdens caused elsewhere

Improvement gap (%)
  = potentially preventable burden / same activity baseline × 100
```

These expressions are only valid with compatible units, periods and boundaries. A reduction in refrigerant leakage is not automatically a reduction in the company’s entire footprint. Water withdrawal is not water consumption. Fuel-use emissions, operating lifecycle emissions and full equipment lifecycle emissions are different boundaries.

The current app uses several incomplete-boundary calculations. Their limitations are stated beside them; they must not be described as fully net savings merely because the calculation includes one adjustment.

### Technical potential is not funding impact

The opportunity from changing an asset and the improvement caused by new funding are separate questions. A stronger project calculation compares time-dependent outcomes **with and without the proposed financing**. The without-funding case must include existing installations, funded replacements, credible commitments and expected operational changes.

If financing only accelerates a planned replacement, credit the extra improvement during the acceleration period, rather than claiming every subsequent year forever. Deployment by 2031 in this pilot is a stated scenario horizon, not a forecast. The 0%, 25%, 50% and 100% controls are sensitivities, not probabilities or a confidence interval.

### Why there is no composite score

Absolute preventable impact helps prioritize scale. A percentage helps describe an activity’s relative gap. Evidence and coverage say how much is known. Combining these into a single grade would hide assumptions and could reward poor disclosure if unknown harm were treated as zero.

Climate, water, air pollution and nature should initially retain their own units and methods. Monetary aggregation requires defensible impact pathways, location-specific factors where relevant, explicit valuation choices and double-counting controls. Do not add a percentage for electricity use to one for climate damage.

### Climate damage dollars

The pilot applies a fixed **$255.12 per tonne CO₂e in 2024 US dollars**, taken from the Global Value Factors Database V4, as a screening valuation. The [calculation notes](research/avoidable-damage-scorecard.md) identify the workbook and assumptions.

This models future societal climate damage associated with emissions. It is not damage observed entirely in the inventory year, company liability, a project cash saving, or the value of all environmental harm. GWP equivalence is not exact gas-specific damage equivalence. Applying this factor to a physical intervention difference is an analytical extension, not independent validation of an avoided-emissions claim.

The billion-dollar mandate therefore needs a separate cashflow model. Avoided societal damage cannot repay a loan. Startup equity, grants and equipment loans also have different principal-recovery properties; none should be presented as guaranteeing capital recovery.

## 4. What has actually been completed

The checked-in app dataset currently contains **eight companies, 92 evidence records and 40 distinct URLs in the company source lists**. These are record and coverage counts, not independent observations, quality grades or statistical confidence measures.

| Company | Implemented opportunity | Interpretation that must survive future edits |
|---|---|---|
| Walmart | Refrigerant substitution sensitivity using a reported 4.08 MtCO₂e source | At 50% assumed coverage, about 2.04 Mt/year is a gross direct sensitivity. Eligibility and net lifecycle savings are unknown. |
| ExxonMobil | Tank methane recovery sensitivity | At 50% assumed untreated eligibility, about 87,600 tCO₂e/year remains after recovered-gas combustion, before other lifecycle effects. The untreated cohort is undisclosed. |
| Microsoft | Matched cold-plate cooling comparison; deeper water evidence | The 15% climate result is process-specific. The separate 31% lifecycle water result cannot be applied to corporate onsite water. |
| Nucor | Furnace-control replication benchmark | The 5% electricity improvement was already achieved at Seattle. Remaining comparable unoptimized assets are not identified. |
| JPMorgan Chase | Borrower-project financing research gap | No bank-wide physical preventable percentage is established. Selling exposures does not itself reduce physical emissions. |
| UPS | Historical external delivery-fleet electrification comparison | The approximately 46.4% operating reduction uses Frito-Lay study conditions, not measured UPS performance; vehicle manufacture is excluded. |
| Delta Air Lines | Gate power and cooling lifecycle comparison | The 63% displayed case is the low study case, not a guaranteed floor. It starts from partly electrified gates, not a wholly fossil baseline. |
| Duke Energy | Pipeline-maintenance gas recovery comparison | The approximately 45.4% displayed case assumes 50% recovery and counts combustion of recovered methane; compressor and other effects remain unquantified. |

See the [expanded research synthesis](research/expansion/RESEARCH-UPDATE.md) and individual dossiers for original citations, exact figures and source boundaries. The app’s separate direct-climate-burden view uses Scope 1 inventories as context. It omits purchased electricity, suppliers, product use and financing, and does not fairly rank all business models by total sustainability.

### Important corrections from deeper investigation

- **Walmart:** 619 facilities with partial or full ultra-low-GWP systems is not a full-conversion count or an emissions share. The old paired-store study has an unresolved propane unit/conversion discrepancy; its reported whole-store result is not a validated Walmart net factor. [Audit](research/expansion/walmart-deep.md)
- **ExxonMobil:** a tank-source pool is not an inventory of untreated eligible tanks. Monitoring and recognition of a reporting pathway do not establish complete measured verification. Historical recovery-unit costs are not current Exxon quotes. [Audit](research/expansion/exxon-deep.md)
- **Microsoft:** an achieved WUE improvement differs from absolute saved water. The projected design withdrawal-avoidance figure is not measured consumption savings. Deployment and electricity tradeoffs need site-specific treatment. [Audit](research/expansion/microsoft-deep.md)
- **Delta:** the emissions comparison uses partly electrified operations, while the cited payback calculation uses a 100%-APU baseline. These cannot be combined as if they describe one identical project. Detailed original-author methods resolved this distinction. [Dossier](research/expansion/delta.md)

These corrections are part of the product’s value. Future work should strengthen or revise claims when evidence changes, rather than preserve a dramatic headline at the expense of its denominator.

### Software and publication

The Next.js prototype includes an opportunity table, company search, direct Scope 1 context, eight detail routes, scenario controls, methodology, an investment-thesis view, evidence ledgers, additional environmental metrics, financing-evidence panels and downloadable research reports. It was deployed with the Vercel CLI and published in this public GitHub repository.

Production build and browser checks covered all eight routes, evidence rendering, scenario interactions including zero, report downloads, navigation and mobile overflow. Those checks establish application behavior; they do not validate the scientific claims. The committed `smoke.cjs` is an earlier production-URL smoke script and does not reproduce the full expanded validation. A complete portable regression suite remains work to do.

## 5. Repository map and current sources of truth

| Location | Role |
|---|---|
| [AGENTS.md](AGENTS.md) | Agent entry point and essential continuation rules. |
| [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) | This handoff: intent, decisions, status and roadmap. |
| [app/data.json](app/data.json) | The dataset the live app renders. Check here for actual displayed values. |
| [app/ui.js](app/ui.js) | Client interface, scenario calculations and presentation. |
| [app/globals.css](app/globals.css) | Visual design and responsive layout. |
| [app/company/[slug]/page.js](app/company/%5Bslug%5D/page.js) | Company route wrapper. |
| [research/expansion/RESEARCH-UPDATE.md](research/expansion/RESEARCH-UPDATE.md) | Latest research synthesis, including corrections to early interpretations. |
| [research/expansion](research/expansion) | Three added-company dossiers and three deeper audits, with structured data. |
| [research](research) | Original pilot observations, calculations and historical scripts. |
| [public/research](public/research) | Downloadable copies and the packaged research archive. |
| [screenshots](screenshots) | Desktop/mobile examples; not evidence for environmental claims. |

The app dataset is the source of truth for what the app displays, **not an authority above original evidence**. When a report, archived calculation and app record disagree, investigate the original source, record the discrepancy, and reconcile the affected outputs. Later audited interpretations supersede earlier provisional interpretations where explicitly documented.

There are duplicated research representations. Some archived scripts contain absolute paths from the original workspace and expect source files not included in the repository. Do not run them blindly or claim a clean clone can reproduce all research automatically. The app itself runs from the checked-in dataset without API keys. See [README.md](README.md) for setup.

GitHub publication and Vercel deployment were separate CLI operations. Automatic deployment from repository pushes has not been established. A documentation commit does not require redeploying the app.

## 6. What is needed to do this properly

### Priority 1 — Finish one complete asset-level case

The highest-value next milestone is one independently reviewed project with sufficient data to estimate net impact and repayment. More company rows alone do not solve the missing denominator problem.

For a refrigerant project, for example, obtain the actual asset and refrigerant mix, charge, measured leakage, cooling load, climate, equipment age, current energy use, replacement design, planned replacement date, lifecycle energy changes, installation quote and operational constraints. Confirm which benefits are extra or earlier than the without-funding case.

**Completion criterion:** another reviewer can reproduce a physical reduction and its range, explain all omitted effects, identify the eligible asset, and evaluate a cashflow and repayment schedule from source evidence. The result need not be positive; rejecting an inapplicable or uneconomic case is valid progress.

### Priority 2 — Make research and calculations reproducible

Create one portable, versioned data flow from evidence to calculations to interface. Preserve raw numeric values separately from formatted labels, plus units, reporting boundaries, periods, gas/GWP conventions, functional units, source locators, retrieval dates, source versions and review status.

Separate reported facts, analyst assumptions, derived quantities, targets, achieved measures and projected measures in a controlled schema. Record why an applicability judgment was made. Mark unavailable inputs explicitly; do not backfill them with an agent’s plausible guess.

Replace absolute workspace paths, document how to obtain permitted source artifacts, preserve checksums or versions where useful, and generate the app dataset, reports and downloads from the same inputs. Respect publisher access and redistribution terms.

**Completion criterion:** a clean checkout plus documented source acquisition reproduces the supported calculations and generated outputs, with tests for units, formulas, missing inputs and scenario boundaries. Review a small adjudicated reference set before scaling extraction.

### Priority 3 — Establish comparability and coverage

For each company, define material activities and a coverage denominator before assigning any company-level gap. Separate technical suitability, operational feasibility, deployment timing, economics and financing additionality. Missing material activities remain unassessed; a partial study must not appear to cover the whole firm.

Use comparable service units within activities—for example, equivalent delivered cooling or the same transport duty—rather than assuming a universal revenue-normalized score solves sector differences. Preserve reporting and ownership boundaries. Resolve overlap among interventions, and deduplicate physical emissions shared across customers, suppliers and financed exposures.

**Completion criterion:** a company-level figure can be traced to compatible, non-overlapping activity estimates with stated coverage. Rank only estimates that actually support comparison; keep incomplete cases outside that ranking.

### Priority 4 — Validate net environmental effects

Use the appropriate intervention boundary: equipment manufacture, electricity and fuel changes, upstream effects, use, leakage, retirement and disposal where material. Account for displacement or rebound only when justified. Model deployment over time rather than multiplying a full annual saving by every year of a horizon.

For water, retain consumption versus withdrawal, basin, season and competing use. For air pollution, emissions mass alone is not health damage; location, dispersion and exposure matter. Nature impacts need suitable spatial and ecological context. Use consistent, explicitly chosen valuation assumptions and sensitivity analysis if monetization is attempted.

**Completion criterion:** qualified review identifies a justified boundary and uncertainty treatment for each claimed impact, with material omissions visible. A scenario range must not be mislabeled a statistical confidence interval.

### Priority 5 — Underwrite the billion-dollar strategy

Group supported interventions into investment opportunities only after deduplication. Gather installed costs, maintenance, energy and material prices, savings ownership, contracts, payment timing, useful life, execution capacity and default risk. Assess whether funding enables additional adoption or merely replaces money the company already intended to spend.

Evaluate physical impact, financial recovery and concentration risk separately. Portfolio principal recovery depends on real repayments and losses; large avoided externalities do not offset a missing payment. No current app figure establishes how to allocate the full billion dollars.

**Completion criterion:** a proposed allocation has project-level evidence, a net-impact model, a cashflow model and explicit downside cases. It is reviewable as an investment proposal rather than just a list of technologies.

### Priority 6 — Scale agents after the schema and review process work

A future workflow can assign bounded roles: inventory extraction, technology evidence, applicability review, calculation validation and synthesis. All roles should emit the same structured evidence records. An independent reviewer should challenge denominators, source transfer, achieved-versus-remaining claims and unsupported extrapolation.

Start with a few fully reviewed cases. Measure extraction errors, unsupported claims, boundary errors, review effort, cost and update latency. Then broaden to sectors and eventually the full constituent universe, with a dated index-membership source and an update policy for restated reports.

Keep software simple: a reproducible ingestion/calculation pipeline and a reviewed dataset are more useful now than an elaborate autonomous orchestration framework. Do not mistake adding a live agent-status panel for building a reliable research system.

## 7. Recommended next working session

1. Read this handoff, the expanded synthesis, and one selected company dossier.
2. Choose one asset-level intervention and identify the exact missing inputs that prevent a net estimate.
3. Improve the portable evidence schema and source-to-output traceability for that case.
4. Obtain or explicitly fail to obtain the missing evidence; record both outcomes.
5. Have the case independently reviewed, update all affected app/report representations, and run relevant behavior checks.
6. Only then use the result to expand comparable coverage or construct an investment proposal.

The story remains: **identify the gap, show the evidence, and determine what would actually close it.** The unfinished work is proving applicability, coverage, net impact and financial additionality—not finding a more persuasive name for an unsupported score.
