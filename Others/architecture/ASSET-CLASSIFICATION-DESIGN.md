# Asset classification

Status: confirmed business direction D047/D048; physical reference-list contracts and implementation to follow. No lists, app formulas or runtime tests were created by this document.

## Confirmed hierarchy

Category ← Asset Type ← Asset. Each Asset Type has a foreign-key lookup to its Category. The three categories are fixed by Accounting:

| Category | Supplied abbreviation |
| --- | --- |
| Komputer | KO |
| Non-Komputer | NK |
| Perangkat Lunak | PL |

Accounting mappings/codes remain deferred. The category's accounting mapping is distinct from an asset's company-wide unique Accounting Asset Code. No automatic mapping from KO/NK/PL to the latter is assumed.

PL describes internal software enhancements budgeted and documented as assets. It uses the same registration fields and common asset lifecycle. No licence seats, subscriptions, expiry tracking or alternative registration form are added by implication. The owner has not yet supplied the operational Asset Type catalogue; prior examples are illustrative only.

## Proposed implementation behavior

- Use a single-valued SharePoint lookup on Asset Type to the Category reference row, with application validation requiring a valid parent. Keep editable business columns optional in SharePoint per D044. Actual internal names, lookup display field and list names will be specified in the provisioning contract.
- In registration, either choose Category first and filter Asset Types to that category, or derive/display Category from the selected type. Choose the interaction during screen design. Avoid independently editable inconsistent category/type selections.
- If Category is changed in the form, clear an incompatible type and require a new compatible selection before saving. Mutation/import paths should validate the same relationship. This is an engineering recommendation, not a new business role permission.
- Treat the three categories as a centrally controlled reference set, not a freely editable operational taxonomy. Do not grant ordinary type maintainers permission to add accounting categories merely because they can maintain types. Final authorized maintainer roles remain open.
- Preserve historical classification evidence. Restrict deletion of referenced category/type rows and define a reviewed deactivation/reclassification path; do not cascade-delete assets. Reclassification of a type already used by assets needs an explicit design because it could change the inferred accounting category of existing records.
- Global versus entity-specific Asset Type availability, type uniqueness, exact names and type/category reclassification rules remain open. Do not infer them from the category being a shared accounting concept.

## Next data-model dependency

Location scope and operational Asset Type catalogue remain to be defined. Shared registration fields for PL do not authorize silent removal of already agreed mandatory fields; field representation and any actual exceptions need explicit confirmation if they arise.
