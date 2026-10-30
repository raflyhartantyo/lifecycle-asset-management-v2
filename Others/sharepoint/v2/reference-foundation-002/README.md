# Reference foundation 002 — physical list contract

Status: manual implementation resources prepared; configuration and runtime NOT RUN. This extends the existing Organization/Function foundation with three dedicated V2 reference lists. It is not an instruction to perform setup now; implement when ready under D072.

| List | Purpose | Exact fields |
| --- | --- | --- |
| LAM2_Categories | Accounting's fixed KO/NK/PL catalogue | Title, CategoryCode |
| LAM2_AssetTypes | Shared types linked to Category (D074) | Title, AssetTypeKey, CategoryRef, IsActive |
| LAM2_Buildings | Shared building-only locations | Title, BuildingKey, IsActive |

[COLUMNS.csv](COLUMNS.csv) defines exact physical names/settings. [CATEGORY-SEED.csv](CATEGORY-SEED.csv) contains only the three confirmed category rows, not accounting account mappings. The CSV files are specifications/seed references, not a provisioning package. No Asset Type or Building catalogue has been invented.

## Logical-to-physical mapping

- Logical CategoryKey maps to CategoryCode, which is stable and unique for the three fixed categories. No duplicate surrogate text column is needed. SharePoint's numeric ID remains the site-local lookup identity.
- AssetTypeKey and BuildingKey are proposed immutable GUID-text identities, maximum 36 characters. Actual rows will receive keys through a later authorized maintenance delivery; no labels or key rows are seeded here.
- Asset Types have no OrganizationRef under D074. CategoryRef stores the Category's numeric ID and displays CategoryCode. The display code is not the stored numeric lookup ID.
- Shared Buildings have no Organization/Function foreign key and no floor or room columns. Asset Types are shared across entities and retain only their Category parent. Type/Building labels are not made unique because those name policies remain deferred.

The existing [foundation columns](../FOUNDATION-COLUMNS.csv) are unchanged. Other operational entities retain their logical design contracts; this package does not provision Assets, access grants or workflows.

## Manual setup when implementing

1. Use dedicated LAM2_ lists inside SITE-F, the existing Function site under D073. Follow [the shared-site layout/permissions](../SHARED-FUNCTION-SITE-SETUP.md) while the new lists are empty; change only LAM-resource permissions, not host-site content/membership. Existing LAM2_Organizations and LAM2_Functions follow their existing guide; do not recreate them. If any target list already exists, compare settings and preserve data/consumers rather than replacing it.
2. Create LAM2_Categories. Keep built-in Title as single-line text, optional, maximum 255 and non-unique. Add CategoryCode with the exact ASCII internal name, single-line text, optional, maximum 2 and unique. Verify its index.
3. Create LAM2_AssetTypes. Keep Title optional/text/255/non-unique. Add AssetTypeKey optional/text/36/unique. Add CategoryRef as an optional single lookup to LAM2_Categories.CategoryCode, non-unique, with Restrict delete and an index. Do not add OrganizationRef or FunctionRef to Asset Types (D074). Add IsActive as Yes/No, default Yes.
4. Create LAM2_Buildings. Keep Title optional/text/255/non-unique. Add BuildingKey optional/text/36/unique, then IsActive Yes/No default Yes. Do not add an entity, function, floor or room field.
5. Preserve built-in ID/Created/Modified/author metadata. Enable edit versioning on each list, with retention under the company policy. Record the actual internal names/settings. Do not substitute Cascade delete or change optional business fields to Required to work around a setup discrepancy.
6. After the new lists' LAM-specific permissions are configured, populate only the confirmed Category rows by the controlled initial setup process, using the seed CSV as a reference. If a code exists, compare it instead of adding another row. Do not overwrite a conflicting existing label silently. No placeholder accounting mapping is supplied.
7. Leave Asset Types and Buildings empty until their real authorized catalogue population or approved synthetic test setup. The later forms enforce required labels/keys/parents; optional SharePoint storage is not permission to accept incomplete business data.
8. Configure the chosen reference-read permissions when binding the app. The delivered reader needs read access, not write/manage-list rights. These common catalogue permissions are separate from future Assets/inventory/task data. A client entity filter is not a security boundary if direct-list access must also be restricted.

The physical setup is reviewable without an access questionnaire. The owner handles company configuration at the implementation stage. Missing platform settings are implementation discrepancies to resolve, not a reason to change the accepted model silently.

## App integration

Use the [manual reference-browser package](../../../../Power%20Apps/Lifecycle%20Asset%20Management%20V2/target-v2/reference-catalogues/README.md) for exact control/property/formula resources. It reads the three reference lists directly under the configured connector/source permissions and makes no business writes. No Power Automate flow is needed for this read-only slice; reference maintenance and operational writers are later feature deliveries.

The screen expects a resolved current Organization numeric item ID from the eventual session/context adapter. The maker can bind an approved synthetic context during isolated UAT, without shipping a hardcoded entity or treating a display flag as authorization. This dependency is documented, not a request for a capability report.

## Validation and rollback

Run the package's [feature checks](../../../../Power%20Apps/Lifecycle%20Asset%20Management%20V2/target-v2/reference-catalogues/TEST-CASES.csv) when implemented. Check exact optional/unique/lookup settings, three fixed categories, shared-type Category integrity, shared Buildings, read-only behavior, context filtering, source permission denial and honest refresh failure. No test has run in company systems.

For empty, unused lists, correct settings in place where possible. Before any recreation, confirm no rows/consumers/references and retain settings evidence. Once dependent rows/app bindings exist, use a corrective migration rather than deleting/recreating. Restoring an app version does not undo SharePoint data/schema changes. Never remove existing business rows or referenced history as cleanup for this package.

## Platform references

[SharePoint lookup relationships and unique columns](https://support.microsoft.com/en-us/sharepoint/lists/data-and-lists/create-list-relationships-by-using-lookup-columns) support the relationships; list names, key strategy and lengths are project choices. [SharePoint app connection/data mappings](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/connections/connection-sharepoint-online) explain the connector representation. Actual configuration and behavior must be checked during implementation.
