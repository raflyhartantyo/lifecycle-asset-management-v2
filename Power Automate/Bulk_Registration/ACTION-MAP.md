# Bulk_Registration — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Create_file | Create_file | OpenApiConnection | shared_sharepointonline | CreateFile | Initialize_variable | body, dataset, folderPath, name |
| /properties/definition/actions/Get_tables | Get_tables | OpenApiConnection | shared_excelonlinebusiness | GetTables | Create_file | drive, file, source |
| /properties/definition/actions/List_rows_present_in_a_table | List_rows_present_in_a_table | OpenApiConnection | shared_excelonlinebusiness | GetItems | Get_tables | drive, file, source, table |
| /properties/definition/actions/Respond_to_a_Power_App_or_flow | Respond_to_a_Power_App_or_flow | Response | - | - | List_rows_present_in_a_table |  |
| /properties/definition/actions/Initialize_variable | Initialize_variable | InitializeVariable | - | - | (scope entry) |  |
