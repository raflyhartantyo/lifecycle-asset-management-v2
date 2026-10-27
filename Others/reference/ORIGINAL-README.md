# Lifecycle Asset Management V2

Redesign package for the Lifecycle Asset Management (LAM) PowerApps. Start here.

## Read order
1. `docs/Context.txt`: handover (databases, screens, relationships, flows, access, known bugs, redesign direction).
2. `docs/Zurich Brand Guidelines.md`: the brand rules to apply.
3. `docs/redesign-plan.md`: the approved plan for the redesign, including the entity and function scoping.
4. `flows/index.md`: flow names and their original GUIDs.
5. `data/schema/`: list definitions to create in SharePoint.

## What is in this package
- `app/src/`: one YAML file per screen, plus `App.pa.yaml`. This is the editable source of the current app.
- `flows/`: one folder per Power Automate flow, named by display name, with `definition.json`.
- `data/`: list schemas and anonymized sample rows. No real data.
- `tools/`: `check_yaml.py` checks YAML syntax and control references.

## Not in this package (on purpose)
- The original `.msapp` file. The YAML in `app/src/` replaces it. Keep the `.msapp` only as a restore point.
- Connection and API map files. These are environment-specific and must be recreated on import.
- Raw CSV exports. They contain personal data. Only anonymized samples are provided.

## Importing the app
Paste each YAML file into Power Apps Studio using the Source Code schema (the only format it accepts). Check that no control shows an error before saving.

## Importing the flows
Import the flows in the target environment, then recreate the connections. Each flow takes an `Entity` input (see the redesign plan).
