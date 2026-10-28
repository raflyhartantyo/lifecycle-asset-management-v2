#!/usr/bin/env python3
"""Validate design schemas/examples only; never execute LAM operations."""
from copy import deepcopy
import json
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    raise SystemExit('Requires Python package jsonschema; no runtime checks were performed.')

root = Path(__file__).resolve().parents[2]
folder = root / 'Others/architecture/interfaces'
def read(name):
    return json.loads((folder / name).read_text())

catalog = read('OPERATION-CATALOG.json')
request = read('request.schema.json')
response = read('response.schema.json')
Draft202012Validator.check_schema(request)
Draft202012Validator.check_schema(response)
validators = {
    'request': Draft202012Validator(request, format_checker=FormatChecker()),
    'response': Draft202012Validator(response, format_checker=FormatChecker()),
}
operations = catalog['operations']
names = [op['operation'] for op in operations]
assert len(names) == len(set(names)), 'Duplicate operation name'
assert set(names) == set(request['properties']['operation']['enum'])
assert set(names) == set(response['properties']['operation']['enum'])
system_names = {op['operation'] for op in catalog['systemOnlyOperations']}
assert not system_names.intersection(names)
model = json.loads((root / 'Others/sharepoint/v2/OPERATIONAL-DATA-CONTRACT.json').read_text())
model_names = {entity['name'] for entity in model['entities']}
for op in operations:
    assert op['payloadDefinition'] in request['$defs'], op['operation']
    assert set(op['modelEntities']).issubset(model_names), op['operation']
    assert op['requiresSubmissionKey'] == (op['mode'] in ('prepare', 'command'))

examples = read('EXAMPLES.json')['examples']
for example in examples:
    validators[example['kind']].validate(example['document'])

def request_for(operation):
    return deepcopy(next(e['document'] for e in examples if e['kind'] == 'request' and e['document']['operation'] == operation))

negative = []
def reject(name, kind, document):
    assert not validators[kind].is_valid(document), name
    negative.append(name)

for field in ('actorEmail', 'actorPrincipalKey', 'role'):
    doc = request_for('Assets.Query')
    doc[field] = 'FORGED'
    reject('unknown caller authority field: ' + field, 'request', doc)
doc = request_for('Movement.Preview'); del doc['submissionKey']
reject('durable preview missing submission identity', 'request', doc)
doc = request_for('Movement.Preview'); del doc['payload']['items'][0]['changes'][0]['value']
reject('set without value', 'request', doc)
doc = request_for('Movement.Preview'); doc['payload']['items'][1]['changes'][0]['value'] = 'SILENT-CLEAR-VALUE'
reject('clear with conflicting value', 'request', doc)
doc = request_for('Disposal.Preview'); del doc['payload']['items'][0]['sellingPrice']
reject('sale without per-asset price', 'request', doc)
doc = request_for('Disposal.Preview'); doc['payload']['items'][0]['mode'] = 'NonSale'
reject('non-sale payload carries stale sale fields', 'request', doc)
doc = request_for('StockResponse.Save'); doc['payload']['assetMasterChanges'] = {'BuildingRef': 'FORGED'}
reject('response payload contains master write instruction', 'request', doc)
doc = request_for('StockResponse.Save'); doc['payload']['responseKind'] = 'Correct'
reject('correct assertion with correction values', 'request', doc)
doc = request_for('StockResponse.Save'); doc['payload']['observations'] = []
reject('correction assertion without observations', 'request', doc)
doc = request_for('Reconciliation.Apply'); del doc['payload']['previewVersion']
reject('apply without reviewed preview version', 'request', doc)
doc = request_for('Reconciliation.Apply'); doc['payload']['itemKeys'] *= 2
reject('duplicate reviewed selection keys', 'request', doc)
doc = request_for('Assets.Query'); doc['operation'] = 'ApprovalDecision.Process'
reject('system callback through app dispatch', 'request', doc)
doc = request_for('Assets.Query'); doc['payload']['page']['pageSize'] = 0
reject('invalid page bound', 'request', doc)
doc = deepcopy(next(e['document'] for e in examples if e['kind'] == 'response' and e['document']['result'] == 'accepted'))
del doc['operationRef']
reject('accepted response without durable reference', 'response', doc)

by_name = {op['operation']: op for op in operations}
for name in ('Disposal.Preview', 'Disposal.Commit', 'Inventory.Preview', 'Inventory.Commit'):
    assert 'StandardApprovals' not in by_name[name]['connectorResponsibilities']
assert 'ReconciliationSignoff.Prepare' in by_name
print(f'PASS: {len(operations)} logical app interfaces, {len(system_names)} separate system entries, '
      f'{len(examples)} valid examples, {len(negative)} rejected malformed envelope shapes; '
      'schema/model references consistent. Design validation only; no handler, flow, security or UAT runtime executed.')
