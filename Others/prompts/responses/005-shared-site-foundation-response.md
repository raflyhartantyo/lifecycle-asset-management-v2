# 005: Shared-site foundation response (progress report)

## Status summary

**Overall: PARTIAL. Four of five lists complete. LAM2_AssetTypes NOT PASSED.**

| List | Status | Open item |
|---|---|---|
| LAM2_Organizations | PASS (configuration) | None |
| LAM2_Functions | PASS (configuration) | None |
| LAM2_Categories | PASS (configuration) | None |
| LAM2_AssetTypes | NOT PASSED | OrganizationRef not created |
| LAM2_Buildings | PASS (configuration) | None |

## Scope and evidence basis

- Site: SITE-F, the existing Function site. No dedicated LAM site was created.
- Method: manual configuration in SharePoint by the operator, checked against the contract (`CREATION-GUIDE.md`, `FOUNDATION-COLUMNS.csv`, `reference-foundation-002/COLUMNS.csv`).
- Evidence type: most checks are **user-reported**. Screenshots were supplied for LAM2_Functions indexed columns, OrganizationRef relationship settings, and LAM2_Categories seed rows.
- Configuration inspection is **not** a runtime or security test. No test case was executed.
- No Power Apps, flow, or accounting mapping was changed. The blank app was not modified.
- Site-level permissions in SITE-F were not changed.

## Completed steps and settings

### LAM2_Organizations
- Created as a blank list, no rows at creation.
- Title: optional, 255 characters, not unique.
- Organization_ID: optional, single line, 50 characters, unique, indexed.
- IsActive: Yes/No, default Yes.
- Versioning: on. Retention 50, aligned with company policy.
- Permissions: inheritance stopped. Owners (Full Control) and IT Asset Management (Contribute from PowerApps) retained. Members and Visitors removed from this list only, with site owner agreement. Site-level groups confirmed intact.
- Rows: 0.

### LAM2_Functions
- Created as a blank list, no rows at creation.
- Title: optional, 255 characters, not unique.
- Function_ID: optional, single line, 50 characters, unique, indexed.
- OrganizationRef: lookup to LAM2_Organizations, showing Organization_ID. Single value. Enforce unique values No. Enforce relationship behavior on. Restrict delete. Confirmed by screenshot.
- Additional index on OrganizationRef, not in the contract. Harmless; left in place.
- IsActive: Yes/No, default Yes.
- Versioning: on. Retention 50, aligned with company policy.
- Permissions: configured as for LAM2_Organizations.
- Rows: 0.

### LAM2_Categories
- Created as a blank list.
- Title: optional, 255 characters, not unique.
- CategoryCode: optional, single line, 2 characters, unique, indexed.
- Versioning: on. Retention aligned with company policy.
- Permissions: configured as for LAM2_Organizations.
- Seed rows: three rows, confirmed by screenshot: KO / Komputer, NK / Non-Komputer, PL / Perangkat Lunak. No other rows.

### LAM2_AssetTypes: NOT PASSED
- Created as a blank list.
- Title: optional, 255 characters, not unique. PASS (user-reported).
- AssetTypeKey: optional, single line, 36 characters, unique. PASS (user-reported).
- CategoryRef: lookup to LAM2_Categories. Reported as set up. Index state to confirm.
- IsActive: Yes/No, default Yes. PASS (user-reported).
- Versioning: on. PASS (user-reported).
- Permissions: configured. PASS (user-reported).
- **OrganizationRef: not created.** The operator chose not to add it. The contract requires it to link each asset type to its entity. This is a deliberate gap, recorded as not passed.
- Rows: 0 (not separately confirmed).

### LAM2_Buildings
- Created as a blank list, no rows.
- Title: optional, 255 characters, not unique.
- BuildingKey: optional, single line, 36 characters, unique, indexed.
- IsActive: Yes/No, default Yes.
- No Organization, Function, floor or room column.
- Versioning: on. Retention 50, aligned with company policy.
- Permissions: configured as for LAM2_Organizations.
- Rows: 0.

## PASS / FAIL / NOT RUN

| Check | Result | Evidence |
|---|---|---|
| FND-01 Lists exist with exact names, zero rows | PASS | User-reported; Organizations and Functions empty |
| FND-02 Organization columns | PASS | User-reported |
| FND-03 Function columns | PASS | User-reported, indexed screenshot |
| FND-04 OrganizationRef relationship | PASS | Screenshot: lookup target, Restrict delete, enforced, multiple values off |
| FND-05 Versioning, retention recorded | PASS | User-reported, retention 50 aligned |
| FND-06 Permissions (LAM lists only) | PASS | User-reported; site-level groups confirmed intact |
| FND-07 Scope, no production rows or flows | PASS | User-reported |
| CAT-01 to CAT-06 | PASS | User-reported; screenshot for seed rows |
| CAT-07 Seed rows exactly KO, NK, PL | PASS | Screenshot |
| TYP-04 OrganizationRef on AssetTypes | **NOT PASSED** | Not created by operator decision |
| TYP-05 CategoryRef index | UNKNOWN | Index state not confirmed |
| BLD-01 to BLD-08 | PASS | User-reported |
| Duplicate rejection, parent-delete protection, role authorization, runtime behaviour | NOT RUN | Requires the synthetic-data test instruction |

## Unresolved items and exact next steps

1. **LAM2_AssetTypes, OrganizationRef.** Decision needed: create it per the contract (recommended), or record a contract change. Until then, the list stays NOT PASSED. Steps: List settings → Create column → Lookup to LAM2_Organizations, showing Organization_ID, Restrict delete, enforce relationship on, multiple values off.
2. **LAM2_AssetTypes, CategoryRef index.** Confirm it appears under Indexed columns.
3. **LAM2_AssetTypes, row count.** Confirm zero rows.
4. **Retention for LAM2_Categories and LAM2_AssetTypes.** Not recorded in this session. Confirm each matches company policy.
5. **Permission screenshots** for the lists other than LAM2_Organizations and LAM2_Functions, if Codex needs screenshot evidence.

## Not done

- No asset, inventory, or operational list was created.
- No flow, Power Apps change, or accounting mapping was made.
- No duplicate, authorization, or runtime test was run.
- No site, group, or site-level permission was changed.
- No credentials, tenant IDs, or personal records were recorded.

## Configuration changes made in this session

Only in SITE-F, on the five LAM2 lists listed above: list creation, column creation, versioning settings, indexes, list-level permissions (LAM2 lists only), and three category rows. No other site content was changed.
