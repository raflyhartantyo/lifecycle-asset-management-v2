# Asset classification

Status: confirmed business direction D047/D048/D055; physical reference-list contracts and implementation to follow. No lists, app formulas or runtime tests were created by this document.

## Confirmed hierarchy

Category ← Asset Type ← Asset. Each Asset Type has a foreign-key lookup to its Category and belongs to one entity (D055). Maintain distinct Asset Type catalogues per entity. An identical display label in two entities represents separate type records, not one globally shared type. Validate the type's entity against the asset's entity at registration and other mutations. The three categories are fixed by Accounting:

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
- Asset Type catalogues are entity-specific, confirmed D055. Global User maintains its entity's catalogue and Super User maintains across entities (D056); other roles select existing types. Type uniqueness within an entity, exact names, availability across that entity's functions and type/category reclassification rules remain open. Do not infer them from the category being a shared accounting concept. Cross-entity asset transfers need explicit destination type mapping/reselection consistent with the final category/accounting rules; do not apply a source-entity type record to the destination merely because names match.

## Next data-model dependency

Location scope is globally shared, building-only under D049/D050. Operational type names and destination-type handling for entity transfers remain to be defined. Catalogue-maintainer roles are confirmed by D056. Shared registration fields for PL do not authorize silent removal of already agreed mandatory fields; field representation and any actual exceptions need explicit confirmation if they arise.

## Asset Type maintenance — confirmed D056

Global User can maintain types for its assigned entity; Super User can maintain across entities. Other roles can select existing types but do not gain catalogue maintenance through those roles alone. Validate actor authority and the type's entity at every maintenance mutation. Do not permit a user to change a type's entity to escape scope restrictions. Maintenance UI and backend contracts will implement this rule later; no runtime authority has been configured by this document.
