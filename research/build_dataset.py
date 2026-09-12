"""Combine the reviewed research records without discarding their boundaries."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COMPANIES = ['microsoft', 'walmart', 'exxon', 'jpmorgan', 'nucor']


def numeric_leaves(value, prefix=''):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from numeric_leaves(child, f'{prefix}.{key}' if prefix else key)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from numeric_leaves(child, f'{prefix}[{index}]')
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        yield prefix, value


def text_value(value):
    return json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else value


bundle = {'purpose': 'Evidence for conditional sustainability-gap estimates; not company scores.',
          'cutoff': '2026-09-12', 'companies': {}}
rows = []
for company in COMPANIES:
    baseline = json.loads((ROOT / f'{company}-footprint.json').read_text())
    solutions = json.loads((ROOT / f'{company}-solutions.json').read_text())
    assert baseline.get('observations'), f'No observations: {company}'
    assert solutions.get('interventions'), f'No interventions: {company}'
    bundle['companies'][company] = {'baseline': baseline, 'solutions': solutions}
    for observation in baseline['observations']:
        values = observation.get('value', observation.get('values'))
        for field, value in numeric_leaves(values):
            rows.append({
                'company': company,
                'observation_id': observation.get('id', ''),
                'metric': observation.get('metric', observation.get('title', observation.get('name', ''))),
                'component': field,
                'value': value,
                'unit': text_value(observation.get('unit', observation.get('units', ''))),
                'period': text_value(observation.get('period', baseline.get('baseline_period', ''))),
                'boundary': text_value(observation.get('boundary', observation.get('portfolio_boundary', ''))),
                'geography': text_value(observation.get('geography', observation.get('geographic_coverage', ''))),
                'source_url': text_value(observation.get('source_url', observation.get('source', ''))),
                'source_locator': text_value(observation.get('source_table', observation.get('source_locator', observation.get('locator', observation.get('page_or_table', ''))))),
                'evidence_status': text_value(observation.get('reported_vs_modeled', observation.get('status', ''))),
                'assurance': text_value(observation.get('assurance', '')),
                'caveat': text_value(observation.get('caveat', observation.get('caveats', observation.get('notes', '')))),
                'full_record_file': f'{company}-footprint.json',
            })

(ROOT / 'research-bundle.json').write_text(json.dumps(bundle, ensure_ascii=False, indent=2) + '\n')
with (ROOT / 'baseline-observations.csv').open('w', newline='') as output:
    writer = csv.DictWriter(output, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

summary = {
    'companies': len(bundle['companies']),
    'observation_groups': sum(len(x['baseline']['observations']) for x in bundle['companies'].values()),
    'numeric_baseline_rows': len(rows),
    'intervention_records': sum(len(x['solutions']['interventions']) for x in bundle['companies'].values()),
    'note': 'Mixed-unit groups retain full component labels. Consult original JSON before calculations. Rows are not additive.',
}
(ROOT / 'dataset-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
