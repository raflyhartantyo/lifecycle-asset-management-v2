# Stock_Opname_In_Use_Trigger — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Get_items | Get_items | OpenApiConnection | shared_sharepointonline | GetItems | (scope entry) | $filter, dataset, table |
| /properties/definition/actions/Parse_JSON | Parse_JSON | ParseJson | - | - | Compose |  |
| /properties/definition/actions/Compose | Compose | Compose | - | - | Get_file_content |  |
| /properties/definition/actions/Select_Employees | Select_Employees | Select | - | - | Parse_JSON |  |
| /properties/definition/actions/Select_-_PIC | Select_-_PIC | Select | - | - | Select_Employees |  |
| /properties/definition/actions/Select_-_Receiver | Select_-_Receiver | Select | - | - | Select_-_PIC |  |
| /properties/definition/actions/Compose_Unique_Employee | Compose_Unique_Employee | Compose | - | - | Select_-_Receiver |  |
| /properties/definition/actions/Apply_to_each | Apply_to_each | Foreach | - | - | Initialize_HTML_String |  |
| /properties/definition/actions/Apply_to_each/actions/Compose_Check_Email | Compose_Check_Email | Compose | - | - | Compose_3 |  |
| /properties/definition/actions/Apply_to_each/actions/Set_variable_1 | Set_variable_1 | SetVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Apply_to_each/actions/Condition | Condition | If | - | - | Compose_Check_Email |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Filter_Array_-_DelegateAssets | Filter_Array_-_DelegateAssets | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Select_Delegates | Select_Delegates | Select | - | - | Filter_Array_-_DelegateAssets |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Compose_UniqueDelegates | Compose_UniqueDelegates | Compose | - | - | Select_Delegates |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Apply_to_each_DelegateAssets | Apply_to_each_DelegateAssets | Foreach | - | - | Compose_UniqueDelegates |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Apply_to_each_DelegateAssets/actions/Append_to_string_variable | Append_to_string_variable | AppendToStringVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Compose_DelegateSection | Compose_DelegateSection | Compose | - | - | Apply_to_each_DelegateAssets |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Send_an_email_(V2) | Send_an_email_(V2) | OpenApiConnection | shared_office365 | SendEmailV2 | Compose_DelegateSection |  |
| /properties/definition/actions/Apply_to_each/actions/Filter_array_1 | Filter_array_1 | Query | - | - | Set_variable_1 |  |
| /properties/definition/actions/Apply_to_each/actions/Compose_3 | Compose_3 | Compose | - | - | Filter_array_1 |  |
| /properties/definition/actions/Initialize_HTML_String | Initialize_HTML_String | InitializeVariable | - | - | Filter_array |  |
| /properties/definition/actions/Filter_array | Filter_array | Query | - | - | Compose_Unique_Employee |  |
| /properties/definition/actions/Update_item | Update_item | OpenApiConnection | shared_sharepointonline | PatchItem | Apply_to_each | dataset, id, item/Status, table |
| /properties/definition/actions/Get_file_content | Get_file_content | OpenApiConnection | shared_sharepointonline | GetFileContent | Get_items | dataset, id, inferContentType |
