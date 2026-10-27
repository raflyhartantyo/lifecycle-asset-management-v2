# SO_Respondent_Save — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Check_Responses | Check_Responses | Compose | - | - | Initialize_variable |  |
| /properties/definition/actions/Get_items_Sharepoint | Get_items_Sharepoint | OpenApiConnection | shared_sharepointonline | GetItems | Select_Responses | $filter, dataset, table |
| /properties/definition/actions/Parse_JSON_Responses | Parse_JSON_Responses | ParseJson | - | - | Check_Responses |  |
| /properties/definition/actions/Select_Responses | Select_Responses | Select | - | - | Parse_JSON_Responses |  |
| /properties/definition/actions/Check_Sharepoint | Check_Sharepoint | Compose | - | - | Get_items_Sharepoint |  |
| /properties/definition/actions/Parse_JSON_Sharepoint | Parse_JSON_Sharepoint | ParseJson | - | - | Check_Sharepoint |  |
| /properties/definition/actions/Select_Sharepoint | Select_Sharepoint | Select | - | - | Parse_JSON_Sharepoint |  |
| /properties/definition/actions/Initialize_variable | Initialize_variable | InitializeVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Apply_to_each | Apply_to_each | Foreach | - | - | Filter_array_-_Updated_Yes |  |
| /properties/definition/actions/Apply_to_each/actions/Filter_array_1 | Filter_array_1 | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Apply_to_each/actions/Condition | Condition | If | - | - | Filter_array_1 |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Append_to_array_variable_1 | Append_to_array_variable_1 | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/else/actions/Append_to_array_variable | Append_to_array_variable | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Filter_array_-_Updated_Yes | Filter_array_-_Updated_Yes | Query | - | - | Select_Sharepoint |  |
| /properties/definition/actions/Compose_1 | Compose_1 | Compose | - | - | Apply_to_each |  |
| /properties/definition/actions/Update_item | Update_item | OpenApiConnection | shared_sharepointonline | PatchItem | Compose_1 | dataset, id, item/Available_Assets, table |
| /properties/definition/actions/Post_message_in_a_chat_or_channel | Post_message_in_a_chat_or_channel | OpenApiConnection | shared_teams | PostMessageToConversation | Update_item | body/messageBody, body/recipient, location, poster |
