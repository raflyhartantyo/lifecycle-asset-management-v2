# Shared location model

Status: confirmed scope D049; granularity and physical contract pending. No company resources created or changed.

## Confirmed

One shared location reference can be used by assets from different entities and functions. Most locations represent shared buildings. Do not assign an exclusive organization/function parent to a location, or create duplicate building records merely because several entities occupy it.

Asset entity/function scope and location are independent relationships. Shared physical location does not broaden read/write/export/report permissions, approve a scope transfer, or merge inventories belonging to different scopes. A location-only asset move that leaves scope and Business Owner unchanged follows the already agreed BAU movement rules and automatic history; it does not trigger dual-owner approval solely because the building is shared.

## Proposed implementation

Maintain stable shared location identifiers; assets reference a location without changing its owning entity/function. Inventory availability and balances retain their own authorized scope even where storage locations are shared. Final inventory balance/location identity is a separate data contract.

Record a location change's prior/new reference in history. Preserve referenced locations through deactivation rather than destructive ordinary removal. Shared location metadata must contain only approved common reference details, not another entity's asset register or access grants. The shared catalogue's maintainer permissions remain to be designed; Global User's entity maintenance scope does not implicitly authorize changing shared references for all entities.

Granularity is the next design choice: a flat building catalogue, or building/floor/room detail. Do not create an assumed hierarchy or extra mandatory fields until confirmed. Address, location codes, aliases, uniqueness, active-state behavior, required operational detail and any location-PIC model remain open. Physical list names, lookups and application field contracts will follow that decision.
