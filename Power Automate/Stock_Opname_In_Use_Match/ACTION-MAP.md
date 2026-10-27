# Stock_Opname_In_Use_Match — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Respond_to_a_Power_App_or_flow | Respond_to_a_Power_App_or_flow | Response | - | - | Create_Result_List |  |
| /properties/definition/actions/Create_new_folder | Create_new_folder | OpenApiConnection | shared_sharepointonline | CreateNewFolder | (scope entry) | dataset, parameters/path, table |
| /properties/definition/actions/Create_file_CMDB | Create_file_CMDB | OpenApiConnection | shared_sharepointonline | CreateFile | Create_new_folder | body, dataset, folderPath, name |
| /properties/definition/actions/Create_Result_List | Create_Result_List | OpenApiConnection | shared_sharepointonline | PostItem | GUID | dataset, item/Active, item/Request_Date, item/Requested_By, item/Title, table |
| /properties/definition/actions/Try | Try | Scope | - | - | Init_VarOutput |  |
| /properties/definition/actions/Try/actions/Parse_JSON_-_Unfiltered | Parse_JSON_-_Unfiltered | ParseJson | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Filter_out_ATP-023 | Filter_out_ATP-023 | Query | - | - | Parse_JSON_-_Unfiltered |  |
| /properties/definition/actions/Try/actions/List_rows_present_in_a_table_CMDB | List_rows_present_in_a_table_CMDB | OpenApiConnection | shared_excelonlinebusiness | GetItems | Get_tables_CMDB_Data | drive, file, source, table |
| /properties/definition/actions/Try/actions/Get_tables_CMDB_Data | Get_tables_CMDB_Data | OpenApiConnection | shared_excelonlinebusiness | GetTables | Filter_out_ATP-023 | drive, file, source |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Item_Matching | Apply_to_each_-_Item_Matching | Foreach | - | - | List_rows_present_in_a_table_CMDB |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Item_Matching/actions/Condition_-_Notebook | Condition_-_Notebook | If | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Item_Matching/actions/Condition_-_Notebook/actions/Filter_array_-_Hostname_Match | Filter_array_-_Hostname_Match | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Item_Matching/actions/Condition_-_Notebook/actions/Condition_Found_CMDB | Condition_Found_CMDB | If | - | - | Filter_array_-_Hostname_Match |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Item_Matching/actions/Condition_-_Notebook/actions/Condition_Found_CMDB/actions/Append_to_array_variable_-_Matched_Notebook | Append_to_array_variable_-_Matched_Notebook | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Item_Matching/actions/Condition_-_Notebook/actions/Condition_Found_CMDB/else/actions/Append_to_array_variable_-_Mismatched_Notebook | Append_to_array_variable_-_Mismatched_Notebook | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Item_Matching/actions/Condition_-_Notebook/else/actions/Append_to_array_variable_-_Non_Automated | Append_to_array_variable_-_Non_Automated | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Update_item | Update_item | OpenApiConnection | shared_sharepointonline | PatchItem | Compose | dataset, id, item/Asset_Details, item/Status, table |
| /properties/definition/actions/Try/actions/Compose | Compose | Compose | - | - | Apply_to_each_-_Item_Matching |  |
| /properties/definition/actions/Try/actions/Post_message_-_Done_Notification | Post_message_-_Done_Notification | OpenApiConnection | shared_teams | PostMessageToConversation | Update_item | body/messageBody, body/recipient, location, poster |
| /properties/definition/actions/Catch | Catch | Scope | - | - | Try |  |
| /properties/definition/actions/Catch/actions/Error_Catching | Error_Catching | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Catch/actions/Terminate | Terminate | Terminate | - | - | Update_error |  |
| /properties/definition/actions/Catch/actions/Update_error | Update_error | OpenApiConnection | shared_sharepointonline | PatchItem | Error_Catching | dataset, id, item/ErrorDetails, item/Result, table |
| /properties/definition/actions/Init_VarToday | Init_VarToday | InitializeVariable | - | - | Respond_to_a_Power_App_or_flow |  |
| /properties/definition/actions/Init_VarOutput | Init_VarOutput | InitializeVariable | - | - | Init_VarToday |  |
| /properties/definition/actions/GUID | GUID | Compose | - | - | Create_file_Networking_Data |  |
| /properties/definition/actions/Create_file_Networking_Data | Create_file_Networking_Data | OpenApiConnection | shared_sharepointonline | CreateFile | Create_file_CMDB | body, dataset, folderPath, name |
