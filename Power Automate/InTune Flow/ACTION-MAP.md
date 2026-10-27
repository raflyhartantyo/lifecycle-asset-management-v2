# InTune Flow — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Try | Try | Scope | - | - | Respond_to_a_Power_App_or_flow |  |
| /properties/definition/actions/Try/actions/Get_tables | Get_tables | OpenApiConnection | shared_excelonlinebusiness | GetTables | (scope entry) | drive, file, source |
| /properties/definition/actions/Try/actions/List_rows_present_in_a_table | List_rows_present_in_a_table | OpenApiConnection | shared_excelonlinebusiness | GetItems | Get_tables | drive, file, source, table |
| /properties/definition/actions/Try/actions/Get_items | Get_items | OpenApiConnection | shared_sharepointonline | GetItems | List_rows_present_in_a_table | $filter, dataset, table |
| /properties/definition/actions/Try/actions/Apply_to_each | Apply_to_each | Foreach | - | - | Get_items |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/Filter_InTune_By_Serial | Filter_InTune_By_Serial | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/Condition | Condition | If | - | - | Filter_InTune_By_Serial |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/Condition/actions/Update_item | Update_item | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Accounting_Asset_Code, item/Arrival_Date, item/Asset_Condition, item/Asset_Name, item/Asset_Status, item/Asset_Type_ID, item/Category_ID, item/Function_ID, item/HostName, item/Location_ID, item/MYID_Asset_Owner, item/MYID_Business_Owner, item/Organization_ID, item/SODate, item/SO_Method, item/Title, item/Update_Type, item/Updated_Date, table |
| /properties/definition/actions/Catch | Catch | Scope | - | - | Try |  |
| /properties/definition/actions/Catch/actions/Error_Catching | Error_Catching | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Catch/actions/Terminate | Terminate | Terminate | - | - | Error_Catching |  |
| /properties/definition/actions/Create_file | Create_file | OpenApiConnection | shared_sharepointonline | CreateFile | (scope entry) | body, dataset, folderPath, name |
| /properties/definition/actions/varInTuneRows | varInTuneRows | InitializeVariable | - | - | Create_file |  |
| /properties/definition/actions/varMatchedSerial | varMatchedSerial | InitializeVariable | - | - | varInTuneRows |  |
| /properties/definition/actions/varMatchedDeviceName | varMatchedDeviceName | InitializeVariable | - | - | varMatchedSerial |  |
| /properties/definition/actions/varToday | varToday | InitializeVariable | - | - | varMatchedDeviceName |  |
| /properties/definition/actions/Respond_to_a_Power_App_or_flow | Respond_to_a_Power_App_or_flow | Response | - | - | varToday |  |
