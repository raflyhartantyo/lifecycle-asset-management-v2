# Create the V2 organization/function foundation

Prerequisite: SITE-A creation is complete and the owner confirms the user can create/configure dedicated V2 lists. Keep this step to empty list/column setup. Leave the blank app unchanged.

## 1. Create LAM2_Organizations

1. In SITE-A, open Settings → Site contents → New → List → Blank list. Use the exact name LAM2_Organizations. If it already exists, inspect it and report differences rather than replacing it.
2. Open List settings. Keep the built-in Title column's name as Title; use it for the human-readable organization name. Make it required, single-line text, maximum 255 characters, non-unique.
3. Add Organization_ID as Single line of text, required, maximum 50 characters, enforce unique values Yes, no default. Create with that exact name. This stable code identifies an entity; do not reuse it for another entity. For future data, use uppercase codes without surrounding whitespace.
4. Add IsActive as Yes/No with default Yes. Leave all other optional user columns absent.
5. Keep SharePoint's built-in ID, Created, Modified, Created By and Modified By fields; do not manually create equivalents. ID is the numeric site-local list item identifier, distinct from Organization_ID.
6. In Versioning settings, enable creation of a version on each edit. Keep content approval disabled for this foundation setup. Record the version retention limit selected/mandated by company policy; an unspecified limit is UNKNOWN, not a reason to invent a retention policy.
7. Record the resulting internal names, unique/index settings and list settings. SharePoint creates an index for a unique supported column; verify Organization_ID appears under Indexed columns.

## 2. Create LAM2_Functions

1. Create another blank list named LAM2_Functions in the same SITE-A. Keep Title for the human-readable function name, required, single-line text, maximum 255 characters, non-unique. Names may repeat between entities.
2. Add Function_ID as required Single line of text, maximum 50 characters, enforce unique values Yes, no default. Codes must be globally unique across this list, including where function names repeat. Use an entity-prefixed stable code when actual data is loaded later.
3. Through List settings → Create column, create OrganizationRef as a Lookup to LAM2_Organizations, displaying Organization_ID. Require one value, allow multiple values No, enforce unique values No. Multiple functions must be allowed to share an organization.
4. Enable relationship behavior on OrganizationRef and select Restrict delete. This prevents deleting an organization referenced by a function. If this setting is unavailable or rejected, stop that configuration step and report it; do not substitute Cascade delete. Verify lookup target and relationship settings.
5. Add IsActive as Yes/No, default Yes. Enable edit versioning as above. Keep the built-in ID and audit metadata.
6. Verify Function_ID's unique/index settings. Confirm OrganizationRef is a single-valued lookup; its stored reference is the organization's numeric SharePoint ID, while its displayed value is Organization_ID. Do not fill it with an unrelated text code or create another Organization_ID text column here.

## 3. Check the empty foundation

Report PASS/FAIL/NOT RUN for each, supported by settings screenshots or transcribed settings:

| Check | Expected result |
| --- | --- |
| FND-01 Lists | Both exact names exist in SITE-A; zero business rows |
| FND-02 Organization columns | Title required; Organization_ID required/text/50/unique; IsActive defaults Yes |
| FND-03 Function columns | Title required; Function_ID required/text/50/unique; IsActive defaults Yes |
| FND-04 Relationship | OrganizationRef required/single lookup to Organizations.Organization_ID; non-unique; Restrict delete |
| FND-05 Versioning | Enabled on both lists; retention setting recorded |
| FND-06 Permissions | Actual maintainers/readers/groups and inheritance recorded by aliases; ability to manage permissions verified on SITE-A |
| FND-07 Scope | No production rows, flows, app connections, or baseline changes introduced |

This checks configuration only. Duplicate rejection, parent deletion protection, role authorization and runtime behavior are NOT RUN until a later synthetic-data test instruction. Do not interpret list creation as UAT completion.

Return the report via prompt 002. Actual entity/function names and codes will be entered in a later master-data step; no placeholder company names are assumed.

## Recovery

If a new empty list has a wrong setting, record the discrepancy and correct the setting where possible. Before removing/recreating an incorrectly configured empty list, confirm it has no rows, consumers or dependencies and preserve its settings/evidence. Once records or consumers exist, use a reviewed corrective change; do not casually recreate it. OrganizationRef depends on LAM2_Organizations, so resolve/remove that dependency first if an approved empty-list recreation is necessary.

## Microsoft references

- [Create a list](https://support.microsoft.com/en-us/sharepoint/lists/data-and-lists/create-a-list)
- [List settings](https://support.microsoft.com/en-us/sharepoint/lists/data-and-lists/edit-list-settings)
- [Lookup relationships and unique columns](https://support.microsoft.com/en-us/sharepoint/lists/data-and-lists/create-list-relationships-by-using-lookup-columns)
- [Versioning](https://support.microsoft.com/en-us/sharepoint/lists/documents-and-library/how-versioning-works-in-lists-and-libraries)

These support SharePoint capabilities; names, lengths and setup sequence above are project design choices. Record the actual internal names from column settings rather than assuming creation preserved them.
