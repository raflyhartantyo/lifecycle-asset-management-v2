# Lifecycle Asset Management V2

Reference implementation and versioned implementation handovers for the company LAM redesign. The main developer/designer supplies complete files; company Claude helps apply them and returns validation evidence.

## Start

1. Read [baseline-001](Others/releases/baseline-001/RELEASE.md) and [confirmed decisions](Others/decisions/DECISIONS.md).
2. Follow the [implementation order](Others/releases/IMPLEMENTATION-ORDER.md).
3. Give company Claude [START-HERE](Others/handover/START-HERE.md), then the selected app/flow handover.
4. Return the completed [implementation result](Others/handover/IMPLEMENTATION-RESULT-TEMPLATE.md) for the next delivery.

## Three main folders

- [Power Apps](Power%20Apps/README.md): one app folder, original screen/App-object YAML, per-screen guides, app implementation, validation and rollback.
- [Power Automate](Power%20Automate/README.md): one folder per flow, exact source definition, trigger contract, configuration worksheet, action map and implementation handover.
- [Others](Others/README.md): architecture, SharePoint, confirmed decisions, reference documents and release records.

[Interactive knowledge map](Others/architecture/knowledge-map/README.md) preserves the handover analysis with repository-relative source paths.

## Release status

`baseline-001` preserves the supplied current implementation; redesigned V2 functionality is pending. V2 retains direct disposal and retires only the separate disposal-request/approval process. Target scope is Organization → Function → assets, with roles per email/entity/function.

## Local verification

Python 3.10+ and PyYAML are needed for the existing YAML validator:

```bash
python3 Others/tools/validate_delivery.py
python3 Others/tools/check_yaml.py "Power Apps/Lifecycle Asset Management V2/screens"
```

Local checks establish source integrity and syntax. Company-side Studio and flow validation are separate.

## Platform guidance

[Microsoft Code View](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/code-view) supports Studio-generated control YAML; App-object properties use formula bars. A full exported YAML file is not assumed to be a paste-ready control snippet.

[Microsoft flow package guidance](https://learn.microsoft.com/en-us/power-automate/export-import-flow-non-solution) describes genuine ZIP packages. Supplied definition.json files are references for recreation and are not standalone import packages.
