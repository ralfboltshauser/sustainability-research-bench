"""Reproduce pilot arithmetic; no calculation is a full-company gap score."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
results = []


def record(company, metric, formula, result, unit, status, limits, source):
    results.append(dict(company=company, metric=metric, formula=formula, result=result,
                        unit=unit, status=status, limits=limits, source=source))


record('Walmart', 'Onsite refrigerant share of rounded operational inventory',
       '4.08 / 14.4 * 100', 4.08 / 14.4 * 100, '%', 'Derived footprint share; not avoidable share',
       'Scope1 plus market-based Scope2 only. Source reports28.4% using unrounded inputs.', 'walmart-footprint.json WMT01/WMT02')
record('Walmart', 'Direct impact per kg R-404A leakage prevented', '3922 / 1000', 3922 / 1000,
       'tCO2e per kg leakage prevented', 'Unit-level conditional factor',
       'EPA reference GWP basis; actual gas mix, leakage avoided, energy and recovery effects required.',
       'https://www.epa.gov/hfcs/technology-transitions-gwp-reference-table')
record('Walmart', 'Food disposal mass conversion', '1420e6 * 0.45359237 / 1000',
       1420e6 * 0.45359237 / 1000, 'metric tonnes', 'Derived reported disposal pool',
       'CY2025 excludes India. Not all edible, preventable, landfilled, or methane-generating.', 'walmart-footprint.json food disposition')
record('Microsoft', 'Water balance', '13266 - 5096', 13266 - 5096, 'ML',
       'Reported balance arithmetic', 'FY25 consumption; not savings or monetized local harm.', 'microsoft-footprint.json Table8')
record('Microsoft', 'Scope1 plus market Scope2 plus Scope3', '170887 + 2707428 + 18243000',
       170887 + 2707428 + 18243000, 'tCO2e', 'Inventory reconciliation',
       'Rounds to reported21,121,000. Different from management-adjusted inventory.', 'microsoft-footprint.json Table1A')
record('ExxonMobil', 'Approximate upstream tank/storage methane pool', '142000 * 0.96 * 0.05',
       142000 * 0.96 * 0.05, 'tCH4/year', 'Company source-pool estimate',
       'Rounded source shares total101%. Not measured eligible untreated tanks or feasible abatement.', 'exxon-footprint.json methane sources')
record('ExxonMobil', 'VRU sensitivity if entire estimated tank pool were eligible and untreated',
       '142000 * 0.96 * 0.05 * 0.95', 142000 * 0.96 * 0.05 * 0.95, 'tCH4/year',
       'Conditional engineering envelope; not achievable forecast',
       'Full eligibility unsupported; direct methane only; combustion, power and existing controls excluded.',
       'exxon-footprint.json; https://www.epa.gov/natural-gas-star-program/vapor-recovery-units')
record('ExxonMobil', 'Routine flaring annual volume', '4e6 * 365', 4e6 * 365, 'standard cubic feet/year',
       'Annualized reported volume', 'Existing commitment; no inferred sales, net carbon benefit or fund additionality.', 'exxon-footprint.json flaring')
record('Nucor', 'Current hot-rolled product intensity target gap', '1051 - 975', 1051 - 975,
       'kgCO2e/t hot-rolled steel', 'Current-to-target difference; not validated technical frontier',
       '2025 actual vs2030 goal; same GSCC boundary. Already committed work included.', 'nucor-footprint.json N03')
record('Nucor', 'Current hot-rolled product target gap percentage', '(1051 - 975) / 1051 * 100',
       (1051 - 975) / 1051 * 100, '%', 'Target-gap percentage; not company sustainability score',
       'Cannot apply to23Mt cast steel. Feasible remaining deployment and investor effect unverified.', 'nucor-footprint.json N03')
record('Nucor', 'Current-target normalized annual product difference', '(1051 - 975) * 1e6 / 1000',
       (1051 - 975) * 1e6 / 1000, 'tCO2e/year per1Mt/year matched hot-rolled output',
       'Analyst-normalized scenario', '1Mt is normalization, not eligible corporate output. No cumulative5-year claim.', 'nucor-footprint.json N03')
record('JPMorgan route / GM exemplar', 'Historical cooling project simple gross-savings payback',
       '2000000 / 760000', 2000000 / 760000, 'years', 'Historical illustrative economics',
       'GM case not established JPMorgan borrower; excludes incentives, incremental costs, defaults and current quotes.',
       'https://betterbuildingssolutioncenter.energy.gov/showcase-projects/general-motors-chilled-water-system-optimization-project')
record('JPMorgan route / GM exemplar', 'Five-year gross savings before additional costs',
       '760000 * 5', 760000 * 5, 'historical nominal USD', 'Conditional illustration',
       'Assumes five full operating years and unchanged savings; not collectible net cash forecast.', 'jpmorgan-solutions.json GM cooling case')
record('JPMorgan route / GM exemplar', 'Annual principal-only payment on historical cost over5years',
       '2000000 / 5', 2000000 / 5, 'USD/year', 'Arithmetic repayment requirement',
       'No guarantee of recovery; credit, operating, administration and performance costs still required.', 'jpmorgan-solutions.json GM cooling case')

assert abs(results[2]['result'] - 644101.1654) < 1e-6
assert sum([35,26,25,15,15]) == 1091 - 975
assert 1051 - 975 < 1091 - 975
(ROOT / 'calculated-examples.json').write_text(json.dumps(results, indent=2) + '\n')
with (ROOT / 'calculated-examples.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(results[0]))
    w.writeheader()
    w.writerows(results)
print(f'Wrote {len(results)} labeled calculations; no company scores or portfolio sums.')
