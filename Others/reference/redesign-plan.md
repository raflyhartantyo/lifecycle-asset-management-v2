# Lifecycle Asset Management V2: package and scoping plan

## Context

The LAM redesign (Context.txt section 12) is accepted. Two things are now needed:
1. Package the current LAM app and handover into the project folder `ANTZ'26\Revamp LAM`, under the project name **Lifecycle Asset Management V2**.
2. Scope the design by **entity and function**, so other functions can use the same app. Today only entity is a filter.

The target folder `C:\Users\<user>\OneDrive - Zurich APAC\ANTZ'26\Revamp LAM` exists and is empty.

## Data check (read-only)

- Organizations: ORG-01 (Zurich Asuransi Indonesia), ORG-02 (Zurich General Takaful Indonesia).
- Functions: FNC-01 (IT) and FNC-02 (CRESS), both under ORG-01. Each function belongs to exactly one organization.
- Assets: all 2,179 assets are ORG-01 + FNC-01 (IT). FNC-02 (CRESS) has no assets yet.
- Asset types: all 26 types belong to FNC-01.

So the structure is **Organization → Function → assets**. A function is a child of an entity. It is not a separate axis.

## Part A: Packaging into `ANTZ'26\Revamp LAM`

Layout (from the earlier packaging advice, with the project name):

```
Revamp LAM/
  README.md                       (project name, read order, how to import)
  docs/
    Context.txt                   (handover, sections 1 to 12)
    Zurich Brand Guidelines.md
    redesign-plan.md              (copy of the redesign plan)
  app/src/*.pa.yaml               (one per screen, plus App.pa.yaml)
  flows/
    solution.zip                  (export from Power Automate, for import)
    <flow display name>/definition.json
    index.md                      (display name to GUID map)
  data/
    schema/<list>.md              (columns, types, required, indexes)
    samples/<list>.csv            (anonymized, 5 to 10 rows per list)
  tools/
    check_yaml.py                 (YAML parse and control-reference check)
```

Rules:
- The original `.msapp` (8.44 MB) is **not** copied. The YAML under `app/src/` is the editable source. The `.msapp` stays in the old folder as a restore point.
- Connection files (`connectionsMap.json`, `apisMap.json`) are not copied. They are environment-specific.
- The CSV exports under `Databases/` are **not** copied as-is. They contain personal data (names, emails, phone numbers). Only anonymized samples are copied.
- Remove the Power BI report ID and tenant ID from the copy.
- Flow folders are renamed from GUIDs to display names. `index.md` keeps the GUID mapping.

## Part B: Scoping by entity and function

**Data model**
- Add `Function_ID` to every operational list, next to `Entity` (`Organization_ID`). Every row carries both.
- Functions list gets `Organization_ID` as its parent. A function can exist under one entity only.
- Asset types, categories, locations, and stock opname requests carry the same pair.

**Filter behaviour**
- The app opens on an entity picker. The home screen then shows a function picker with only that entity's functions. The function is set once per session.
- Both values are stored once: `gblEntity` and `gblFunction`. Every query filters on both.
- A user's role is scoped to an (entity, function) pair. The `Roles` list gets a `Function_ID` column next to `Entity`, so a user can be a requester in IT and have no access in CRESS.

**Adding a new function**
- Add one row in `Functions` with its `Organization_ID`. The app shows it in the picker. No screen changes.
- Asset types for the function are added in `AssetTypes`. Stock opname and reconciliation work the same way.

**Current gap**
- FNC-02 (CRESS) has no asset types, so it will appear in the picker but be empty. This is expected until its types are added.

## Migration order

1. Add `Function_ID` and `Organization_ID` to every list. Backfill existing rows: all current assets get `ORG-01` and `FNC-01`.
2. Extend `Roles` with `Function_ID`. Backfill from `Acces_Matrix` with `FNC-01`.
3. Add the function picker next to the entity picker, and filter every query on both values.
4. Replace the hardcoded function and organization IDs with lookups.
5. Test with two functions (IT and CRESS) to confirm the filters isolate them.

## Verification

- Every row in every operational list has an `Entity` and a `Function`, and each pair matches `Functions` (a function's `Organization_ID` must equal the row's entity).
- Row counts after backfill match the source exports (2,179 assets, all ORG-01 and FNC-01).
- With `gblFunction` set to CRESS, no IT asset appears, and the reverse.
- A user with a role only in IT cannot see or submit CRESS data.
- `tools/check_yaml.py` parses every `.pa.yaml` in `app/src/` and reports unresolved control names.
- The package folder contains no real names, no `@zurich` addresses, and no tenant or report IDs.

## Decisions (answered)

1. **Function picker:** set once per session, on the home screen, after the entity picker. It is not shown on every screen.
2. **Multiple functions per user:** allowed. One row per (email, entity, function) in `Roles`.
3. **CRESS (FNC-02):** create it empty. It is listed in `Functions` with no asset types yet.
4. **Project name:** "Lifecycle Asset Management V2" appears in the app (title and header) and in the folder and README.
