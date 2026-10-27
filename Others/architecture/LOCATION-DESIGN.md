# Shared location model

Status: confirmed shared scope D049 and building-only granularity D050; physical contract pending. No company resources created or changed.

## Confirmed

One shared location reference can be used by assets from different entities and functions. Location is recorded at building level only. Based on the owner's operational experience, floor/room documentation is too burdensome; omit floor and room fields entirely, including optional ones. Do not assign an exclusive organization/function parent to a location, or create duplicate building records merely because several entities occupy it.

Asset entity/function scope and location are independent relationships. Shared physical location does not broaden read/write/export/report permissions, approve a scope transfer, or merge inventories belonging to different scopes. A location-only asset move that leaves scope and Business Owner unchanged follows the already agreed BAU movement rules and automatic history; it does not trigger dual-owner approval solely because the building is shared.

## Proposed implementation

Maintain stable shared location identifiers; assets reference a location without changing its owning entity/function. Inventory availability and balances retain their own authorized scope even where storage locations are shared. Final inventory balance/location identity is a separate data contract.

Record a location change's prior/new reference in history. Preserve referenced locations through deactivation rather than destructive ordinary removal. Shared location metadata must contain only approved common reference details, not another entity's asset register or access grants. The shared catalogue's maintainer permissions remain to be designed; Global User's entity maintenance scope does not implicitly authorize changing shared references for all entities.

Use a flat building catalogue. Registration and movement select the building directly; there is no floor/room drill-down or subordinate location hierarchy. Address, location codes, aliases, uniqueness, active-state behavior and any location-PIC model remain open. Physical list names, lookups and application field contracts will follow separately. Do not reintroduce finer granularity without a new explicit owner decision.
