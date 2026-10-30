# Review of response 005 — shared-site foundation

Reviewed response commit `13fbebdb9b73c849d03d9577f81a82c221f256ba` on 2026-10-30, with the owner's subsequent D074 clarification.

Status: **IN PROGRESS — reported setup largely complete; targeted settings remain unconfirmed**. All five lists are reported created. The omission of AssetTypes.OrganizationRef is now correct under the revised shared-catalogue contract. No runtime/security acceptance is claimed.

## Evidence boundary

The [submitted report](005-shared-site-foundation-response.md) is the evidence available to Codex. It says screenshots were used for Functions lookup/index settings and Category seeds, but the images are not attached to this response. Codex has not independently inspected those screenshots or company systems. Other settings remain user-reported. The original report is preserved unchanged.

## Owner clarification resolves the model discrepancy

D074 confirms:
- Asset Types are shared across all entities and retain their Category lookup.
- Both Global Users and Super Users can maintain this shared catalogue.
- LAM2_AssetTypes has no OrganizationRef or FunctionRef.
- This catalogue-specific Global User permission does not expand operational asset/inventory or grant-administration scope.
- Entity transfers retain the same shared Asset Type unless a separate authorized classification change is reviewed; existing owner approvals, identity/accounting-code preservation and Category consistency remain.

The report's original “NOT PASSED because OrganizationRef is missing” finding applied to the previous contract and is superseded by D074. **Do not add that column.** Schema, logical model, permissions, guidance, gallery query and feature cases are updated together.

## Current configuration assessment

| Resource | Review result | Remaining detail |
| --- | --- | --- |
| LAM2_Organizations | Reported configuration consistent with foundation contract | Runtime uniqueness/authorization not tested |
| LAM2_Functions | Reported configuration consistent | Extra OrganizationRef index does not conflict; retain the required OrganizationRef on Functions |
| LAM2_Categories | Three reported fixed code/label rows match KO/NK/PL | Exact numeric version-retention setting not recorded |
| LAM2_AssetTypes | Missing OrganizationRef is correct under D074; other core settings reported configured | CategoryRef full settings/index, AssetTypeKey index, row count and numeric retention not fully evidenced |
| LAM2_Buildings | Reported configuration consistent with shared building-only contract | Runtime/source access behavior not tested |

Organizations, Functions and Buildings report retention 50 aligned with company policy. Do not assume that value was applied to Categories/AssetTypes without recording their actual settings.

## Resume only these specific checks

1. In AssetTypes, confirm CategoryRef is Lookup → LAM2_Categories.CategoryCode; Required No; single-valued; non-unique; Restrict delete; indexed.
2. Confirm AssetTypeKey's unique/index state and the actual AssetTypes row count.
3. Record the exact numeric version-retention settings for Categories and AssetTypes.

No list recreation, general capability questionnaire or new screenshot package is requested. The owner can supply concise actual settings. No AssetTypes.OrganizationRef is required; Functions.OrganizationRef remains required by its separate parent relationship.

## Reader and transfer resource changes

The [revised Asset Type gallery formula](../../../Power%20Apps/Lifecycle%20Asset%20Management%20V2/target-v2/reference-catalogues/formulas/galLAMRefAssetTypes.Items.powerfx) selects active shared types, without OrganizationRef.Id. The screen still uses its context adapter for normal app/session presentation; that adapter does not turn shared types into owned operational records.

Cross-entity transfer no longer needs a receiving-entity type mapping solely because scope changes. Do not broaden asset/report visibility or bypass required owner decisions. Reclassification/deactivation safeguards remain part of the later maintenance writer.

## Permission implementation note

The label “Contribute from PowerApps” does not establish app-only write enforcement. Standard Contribute includes list-item read/add/update/delete, while a custom level depends on its included permissions. [Microsoft permission levels](https://learn.microsoft.com/en-us/sharepoint/understanding-permission-levels). The actual custom level and backend/role isolation remain untested; preserve that distinction for the relevant implementation slice. No site-wide permission change or renewed survey is requested.

## Test/status handling

No UAT case has run. CAT/TYP/BLD labels in Claude's report are session-specific checks, not automatic PASS results for REF2 or the 78-case target/baseline kit. Keep 005 IN PROGRESS until the targeted remaining settings are recorded. Source/schema checks do not compile the app or prove company runtime/security behavior.
