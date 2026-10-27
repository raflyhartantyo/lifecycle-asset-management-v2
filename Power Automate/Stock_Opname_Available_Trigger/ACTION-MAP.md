# Stock_Opname_Available_Trigger — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/GUID_Initialize | GUID_Initialize | InitializeVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Get_items_-_All_Assets | Get_items_-_All_Assets | OpenApiConnection | shared_sharepointonline | GetItems | Initialize_variable_-_Approver_Data | $filter, dataset, table |
| /properties/definition/actions/Select_-_Columns | Select_-_Columns | Select | - | - | Get_file_content |  |
| /properties/definition/actions/Create_Result_List | Create_Result_List | OpenApiConnection | shared_sharepointonline | PostItem | Set_variable_-_Approver_Data | dataset, item/Approval_Data, item/Approval_Status, item/Available_Assets, item/Current_Approver, item/SO_Type, item/Status, item/Title, table |
| /properties/definition/actions/Compose_-_JSON | Compose_-_JSON | Compose | - | - | Select_-_Columns |  |
| /properties/definition/actions/Initialize_variable_-_Approver_Data | Initialize_variable_-_Approver_Data | InitializeVariable | - | - | GUID_Initialize |  |
| /properties/definition/actions/Set_variable_-_Approver_Data | Set_variable_-_Approver_Data | SetVariable | - | - | Compose_-_JSON |  |
| /properties/definition/actions/Parse_JSON | Parse_JSON | ParseJson | - | - | Create_Result_List |  |
| /properties/definition/actions/Select_-_Approver_Data | Select_-_Approver_Data | Select | - | - | Parse_JSON |  |
| /properties/definition/actions/Filter_array | Filter_array | Query | - | - | Select_-_Approver_Data |  |
| /properties/definition/actions/Apply_to_each | Apply_to_each | Foreach | - | - | Filter_array |  |
| /properties/definition/actions/Apply_to_each/actions/Send_an_email_(V2) | Send_an_email_(V2) | OpenApiConnection | shared_office365 | SendEmailV2 | (scope entry) |  |
| /properties/definition/actions/Get_file_content | Get_file_content | OpenApiConnection | shared_sharepointonline | GetFileContent | Get_items_-_All_Assets | dataset, id, inferContentType |
