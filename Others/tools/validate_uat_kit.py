"""Validate the UAT kit's structure, traceability, fixtures and result templates."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEST = ROOT / 'Others/testing'
def rows(path):
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        result = list(reader)
        assert all(None not in row for row in result), ('Malformed CSV', path)
        return result
cases = rows(TEST / 'TEST-CASES.csv')
ids = [r['Case_ID'] for r in cases]
assert len(ids) == len(set(ids)) == 78
assert sum(r['Requirement_Basis'].startswith('TARGET') for r in cases) == 63
assert sum(r['Requirement_Basis'].startswith('BASELINE') for r in cases) == 15
required = ('Case_ID','Suite','Unit','Requirement_Basis','Priority','Persona','Preconditions_and_Fixtures','Steps','Expected_Result','Evidence','Cleanup','Decisions','Acceptance_IDs')
for row in cases:
    assert all(row.get(k, '').strip() for k in required), ('Incomplete case', row['Case_ID'])
    assert row['Priority'] in {'Critical','High','Medium','Low'}
decisions = (ROOT / 'Others/decisions/DECISIONS.md').read_text()
acceptance = (ROOT / 'Others/requirements/ACCEPTANCE-CRITERIA.md').read_text()
for row in cases:
    for d in re.findall(r'D\d{3}', row['Decisions']):
        assert re.search(r'^## '+d+r'\b', decisions, re.M), (row['Case_ID'], d)
    for ac in re.findall(r'AC-\d{2}', row['Acceptance_IDs']):
        assert ac in acceptance, (row['Case_ID'], ac)
results = rows(TEST / 'RESULT-LOG.csv')
assert {r['Case_ID'] for r in results} == set(ids)
assert len(results) == 78 and all(r['Status'] == 'NOT RUN' for r in results)
assert not rows(TEST / 'DEFECT-LOG.csv')
scopes = rows(TEST / 'fixtures/SCOPES.csv')
valid_scopes = {(r['Entity_Key'],r['Function_Key']) for r in scopes}
assert len(valid_scopes) == 3
assets = rows(TEST / 'fixtures/ASSETS.csv')
assert len(assets) == 7 and len({r['Asset_ID'] for r in assets}) == 7
assert all((r['Entity_Key'],r['Function_Key']) in valid_scopes for r in assets)
primary = [r for r in assets if r['Function_Key'] == 'UAT-FNC-A1']
assert sum(r['Asset_Status']=='Available' for r in primary) == 3
assert sum(r['Asset_Status']=='In Use' for r in primary) == 2
inventory = rows(TEST / 'fixtures/INVENTORY.csv')
assert sum(int(r['Quantity']) for r in inventory) == 10
assert len(rows(TEST / 'fixtures/INACTIVE-ASSETS.csv')) == 1
assert len(rows(TEST / 'fixtures/IMPORT-SCENARIOS.csv')) == 4
assert len(rows(TEST / 'fixtures/RECONCILIATION-SCENARIOS.csv')) == 4
assert len(rows(TEST / 'PERSONA-BINDINGS.csv')) == 13
flow_dirs = [p for p in (ROOT / 'Power Automate').iterdir() if p.is_dir()]
assert len(flow_dirs) == 15
for p in flow_dirs:
    assert (p / 'TEST-PLAN.md').is_file()
    unit_cases = [c for c in cases if c['Unit'] == p.name and c['Case_ID'].startswith('FLOW-')]
    assert len(unit_cases) == 1 and unit_cases[0]['Case_ID'] in (p / 'TEST-PLAN.md').read_text()
assert (ROOT / 'Power Apps/Lifecycle Asset Management V2/TEST-PLAN.md').is_file()
print('PASS: 78 unique complete cases (63 target + 15 baseline); valid decision/acceptance references; 78 NOT RUN result rows; 15 flow plans + app plan; synthetic fixture counts/scopes consistent. No runtime test outcomes are claimed.')
