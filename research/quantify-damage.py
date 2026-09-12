"""Explicit climate-damage proxy and technology scenarios; not causal attribution."""
import csv
import json
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NS = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
SOURCE = 'https://capitalscoalition.org/wp-content/uploads/2026/07/Global-Value-Factors-Database-V4-2026-External.xlsx'
with zipfile.ZipFile(ROOT / 'sources/global-value-factors-v4.xlsx') as z:
    ghg = ET.fromstring(z.read('xl/worksheets/sheet3.xml'))
    factor = float(ghg.find('.//m:c[@r="H15"]/m:v', NS).text)
assert factor == 255.12

COMPANIES = [
    ('Microsoft', 'microsoft', 170887, 'FY25 July2024–June2025', 'MSFT-01', 'scope1'),
    ('Walmart', 'walmart', 8160000, 'FY2026 February2025–January2026', 'WMT01', 'scope1'),
    ('ExxonMobil', 'exxon', 90000000, '2025; operated basis', 'operated_ghg', 'scope1'),
    ('JPMorgan Chase', 'jpmorgan', 100024, '2024', 'JPM01', 'scope1'),
    ('Nucor', 'nucor', 6600000, '2025; company-wide', 'N01', 'scope1'),
]
rows = []
for name, slug, expected, period, obs_id, key in COMPANIES:
    baseline = json.loads((ROOT / f'{slug}-footprint.json').read_text())
    observation = next(o for o in baseline['observations'] if o['id'] == obs_id)
    value = observation.get('value', observation.get('values'))[key]
    if 'million' in observation['unit']:
        value *= 1e6
    assert value == expected, (name, value, expected)
    rows.append({
        'company': name, 'reporting_period': period,
        'scope1_tco2e': value, 'factor_usd2024_per_tco2e': factor,
        'modeled_damage_usd2024': value * factor,
        'meaning': 'Fixed-factor modeled lifetime societal climate damage associated with one reported-year direct inventory; not observed annual losses or company liability.',
        'exclusions': 'Purchased electricity, suppliers, sold products, financed emissions, water, pollution, nature and social impacts.',
        'source_url': observation['source_url'],
        'source_observation': f'{slug}-footprint.json:{obs_id}',
        'valuation_source': SOURCE,
    })

factor_metadata = {
    'value': factor, 'unit': '2024 USD/tCO2e', 'source_url': SOURCE,
    'source_cell': 'GHGs!H15', 'database': 'Global Value Factors Database V4',
    'sheet_update': 'June18,2026', 'price_year': 2024,
    'application': 'One common published factor applied to different company reporting years for a screening comparison. No emission-year escalation assumed; not claimed as complete methodology compliance.',
    'scenario_use': 'Applying the same factor to net scenario emissions differences is an analytical extension; the GHG inventory methodology itself does not validate avoided-emission claims.',
    'uncertainty': 'Damage-model, ethical discounting, GWP and inventory uncertainty remain. No statistical interval inferred from database decimal precision.',
}

(ROOT / 'climate-damage-baselines.json').write_text(json.dumps({'factor': factor_metadata, 'companies': rows}, indent=2) + '\n')
with (ROOT / 'climate-damage-baselines.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

extra = [
    dict(case='Walmart onsite refrigerants', type='Source damage proxy, not avoidable harm',
         baseline_tco2e=4080000, damage_usd2024=4080000*factor),
    dict(case='Nucor current-to-target product comparison', type='Company target scenario, not proven available-tech gap',
         baseline_kgco2e_per_t_product=1051, target_kgco2e_per_t_product=975,
         gap_percent=(1051-975)/1051*100, damage_difference_usd2024_per_t_product=(1051-975)/1000*factor,
         normalized_annual_output_t_product=1000000,
         normalized_damage_difference_usd2024=1000000*(1051-975)/1000*factor),
]
(ROOT / 'damage-context-calculations.json').write_text(json.dumps(extra, indent=2) + '\n')
print(json.dumps({'factor':factor,'baseline_companies':len(rows),'results':[(r['company'],r['modeled_damage_usd2024']) for r in rows]},indent=2))
