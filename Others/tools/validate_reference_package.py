"""Validate manual reference resources only; not a Power Fx compiler/runtime test."""
import csv
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[2]
app = root / 'Power Apps/Lifecycle Asset Management V2/target-v2/reference-catalogues'
data = root / 'Others/sharepoint/v2/reference-foundation-002'
manifest = json.loads((app / 'MANIFEST.json').read_text())
controls = manifest['controls']
names = {c['name'] for c in controls}
assert len(names) == len(controls)
assert all(c['parent'] in names or c['parent'] == 'App' for c in controls)
with (app / 'CONTROL-PROPERTIES.csv').open(newline='') as f:
    properties = list(csv.DictReader(f))
assert len({(p['Control'], p['Property']) for p in properties}) == len(properties)
files = set()
for prop in properties:
    assert prop['Control'] in names
    assert bool(prop['Formula']) != bool(prop['FormulaFile']), prop
    if prop['FormulaFile']:
        assert (app / prop['FormulaFile']).is_file()
        files.add(prop['FormulaFile'])
for prop in manifest['appProperties']:
    assert prop['mergeNotReplace'] and (app / prop['formulaFile']).is_file()
    files.add(prop['formulaFile'])
assert files == {str(p.relative_to(app)) for p in (app / 'formulas').glob('*.powerfx')}
formula_text = '\n'.join((app / p).read_text() for p in files)
inline_text = '\n'.join(p['Formula'] for p in properties)
assert not re.search(r'\b(Patch|Collect|ClearCollect|Remove|RemoveIf|UpdateIf|SubmitForm)\s*\(', formula_text + inline_text)
assert not re.search(r'\.Run\s*\(', formula_text + inline_text)
assert 'OrganizationItemId: 0' in formula_text and 'IsResolved: false' in formula_text
assert 'First(LAM2_Organizations)' not in formula_text
assert all(alias in formula_text for alias in manifest['sourceAliases'])
assert not manifest['powerFxCompiled'] and manifest['runtimeTests'] == 'NOT RUN'
with (data / 'COLUMNS.csv').open(newline='') as f:
    columns = list(csv.DictReader(f))
assert len(columns) == 9
assert all(None not in c and all(v is not None for v in c.values()) for c in columns)
assert len({(c['List'], c['InternalName']) for c in columns}) == len(columns)
assert all(c['SharePointRequired'] in ('No', 'N/A') for c in columns)
lookup = {c['InternalName']: c for c in columns if c['Type'] == 'Lookup'}
assert 'OrganizationRef' not in lookup
assert 'OrganizationRef.Id' not in (app / 'formulas/galLAMRefAssetTypes.Items.powerfx').read_text()
assert lookup['CategoryRef']['LookupList'] == 'LAM2_Categories'
assert all(c['AllowMultiple'] == 'No' and c['Unique'] == 'No' and c['DeleteBehavior'] == 'Restrict delete' for c in lookup.values())
assert not any(c['InternalName'] in ('OrganizationRef', 'FunctionRef', 'Floor', 'Room') for c in columns if c['List'] == 'LAM2_Buildings')
with (data / 'CATEGORY-SEED.csv').open(newline='') as f:
    seed = list(csv.DictReader(f))
assert [(x['CategoryCode'], x['Title']) for x in seed] == [('KO', 'Komputer'), ('NK', 'Non-Komputer'), ('PL', 'Perangkat Lunak')]
with (app / 'TEST-CASES.csv').open(newline='') as f:
    tests = list(csv.DictReader(f))
assert len(tests) == len({t['Case_ID'] for t in tests}) == 20
assert all(t['Status'] == 'NOT RUN' for t in tests)
print(f'PASS: {len(columns)} reference columns, 3 fixed Category rows, {len(controls)} controls, '
      f'{len(files)} read-only formula files and 20 NOT RUN feature cases. '
      'Source checks only; no Power Fx compilation or company runtime execution.')
