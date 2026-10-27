# Data model understanding

Read all 20 assigned Markdown files to their final line and parsed all 18 CSV samples with `csv.DictReader`. Samples contain 96 data rows in total. Every header set exactly matches its paired schema, with no missing/extra headers or malformed row widths. Samples are subsets, not the full historical counts printed in the schemas. No personal row values are reproduced here.

`Master_Asset` contains identity, accounting code, owner identifiers, organization/function/location/type/category identifiers, lifecycle dates, purchase/book values, and stock-opname fields. `Asset_Movement_History` and `Inactive_Assets` contain asset identifiers, suggesting history/disposal links; these schema-level joins are inferred because no foreign keys or cardinalities are declared. `Master_Inventories` uses quantity and Parent_ID instead of the richer asset record, with a matching movement history structure. `Stock_Opname_InUse`, `Temp_Stock_Opname`, and `Temp_Acc_Reconcile` hold GUID/status/approval and payload-style fields; payload formats are unspecified. `AuditLog` identifies a target list and item alongside change metadata. `Acces_Matrix` contains permission-like columns but does not define role assignments or enforcement.

`Master_Organization`, `Master_Function`, `Master_Location`, `Master_Category`, `Master_Asset_Type`, and `Master_Employee` are reference lists. Identifier names suggest asset joins; inferred connections are explicitly marked in the graph, not presented as declared relationships.

All schema Type/Sample type cells are blank. These files are inventories of column names, not complete SharePoint provisioning definitions: storage types, required constraints, choice sets, lookups, indexes, and uniqueness must be specified. All 18 schemas repeat the directive to add Entity (Organization_ID) and Function_ID to operational lists. None contains an actual Entity column; Function_ID exists in six schemas (including Master_Asset2). Organization_ID exists in five. Whether Entity is a new physical column or the app's name for Organization_ID remains unresolved.

README distinguishes editable Source Code schema YAML from an import-ready msapp: the original msapp and connection/API maps are intentionally absent. Flow connections, requester address, Power BI IDs, and tenant IDs need target-environment values. README says every flow takes Entity; this is an intended contract to verify against actual definitions, not something this schema pass can establish.

## CSV fidelity

| List | Sample rows | Columns | Header fidelity |
|---|---:|---:|---|
| Acces_Matrix | 8 | 10 | Exact |
| Asset_Movement_History | 8 | 13 | Exact |
| AuditLog | 8 | 8 | Exact |
| Inactive_Assets | 2 | 13 | Exact |
| Inventories_Movement_History | 8 | 10 | Exact |
| Master_Asset | 8 | 34 | Exact |
| Master_Asset2 | 8 | 34 | Exact |
| Master_Asset_Type | 8 | 5 | Exact |
| Master_Category | 4 | 5 | Exact |
| Master_Employee | 8 | 20 | Exact |
| Master_Function | 2 | 4 | Exact |
| Master_Inventories | 5 | 10 | Exact |
| Master_Location | 8 | 6 | Exact |
| Master_Organization | 2 | 3 | Exact |
| Stock_Opname_InUse | 1 | 8 | Exact |
| Temp_Acc_Reconcile | 5 | 15 | Exact |
| Temp_Inventory_Asset | 0 | 3 | Exact |
| Temp_Stock_Opname | 3 | 8 | Exact |

## Questions requiring source or owner clarification

1. Is Master_Asset2 a real second SharePoint list, an alternate connector binding, or a duplicate handover artifact? It duplicates Master_Asset's 34 columns and source-export description.
2. Does Entity mean the existing Organization_ID column, or must an additional Entity column be provisioned? Which lists are operational, and should global reference lists such as organization/category be scoped too?
3. What are the SharePoint column types, internal names, required fields, choices, lookup/cardinality rules, unique keys, and indexes? These cannot be reconstructed reliably from the blank type cells.
4. What does Parent_ID identify in Master_Inventories and Inventories_Movement_History? Is it a parent record, source transaction, or grouping identifier?
5. What is the supported format for payload-like Asset_Details, Approval_Data, Changes, Differences, and Available_Assets fields? The schema names alone do not establish serialization or versioning.
6. Which access-matrix row key maps to employees/roles, and where is authorization enforced? Permission-like column names alone are insufficient.
7. Is the Update_Date versus Updated_Date difference between inventory and inventory history intentional?
8. Are sample rows anonymized consistently across lists so candidate-key joins can be tested? Header fidelity does not demonstrate referential integrity or production completeness.

Token accounting: agent tool did not expose usage counters; JSON zeros are placeholders, not measured zero token consumption.


This analysis was produced against the original handover paths; resolve `app/src/` to the Power Apps app screens folder, `flows/` to Power Automate and `data/schema/` to Others/sharepoint/schema in this repository.
