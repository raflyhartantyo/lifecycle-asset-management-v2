# SO_Respondents_Confirm — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Get_items | Get_items | OpenApiConnection | shared_sharepointonline | GetItems | Initialize_variable_-_Table_Approvers | $filter, dataset, table |
| /properties/definition/actions/Select_-_Approver_Data_Initial | Select_-_Approver_Data_Initial | Select | - | - | Parse_JSON_-Approver_Data |  |
| /properties/definition/actions/Parse_JSON_-Approver_Data | Parse_JSON_-Approver_Data | ParseJson | - | - | Get_file_content |  |
| /properties/definition/actions/Initialize_variable_-_varApproverIndex | Initialize_variable_-_varApproverIndex | InitializeVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Initialize_variable_-_varFinalOutcome | Initialize_variable_-_varFinalOutcome | InitializeVariable | - | - | Initialize_variable_-_varApproverIndex |  |
| /properties/definition/actions/Initialize_variable_-_varStopDoUntil | Initialize_variable_-_varStopDoUntil | InitializeVariable | - | - | Initialize_variable_-_varFinalOutcome |  |
| /properties/definition/actions/Initialize_variable_-_Approver_Data | Initialize_variable_-_Approver_Data | InitializeVariable | - | - | Initialize_variable_-_varStopDoUntil |  |
| /properties/definition/actions/Initialize_variable_-_Temp_Approver_Data | Initialize_variable_-_Temp_Approver_Data | InitializeVariable | - | - | Initialize_variable_-_Approver_Data |  |
| /properties/definition/actions/Initialize_variable_-_Table_Approvers | Initialize_variable_-_Table_Approvers | InitializeVariable | - | - | Initialize_variable_-_Temp_Approver_Data |  |
| /properties/definition/actions/Apply_to_each | Apply_to_each | Foreach | - | - | Filter_array |  |
| /properties/definition/actions/Apply_to_each/actions/Condition | Condition | If | - | - | (scope entry) |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Append_to_array_variable | Append_to_array_variable | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Apply_to_each/actions/Condition/actions/Update_item_1 | Update_item_1 | OpenApiConnection | shared_sharepointonline | PatchItem | Append_to_array_variable | dataset, id, item/Current_Approver, table |
| /properties/definition/actions/Apply_to_each/actions/Condition/else/actions/Append_to_array_variable_1 | Append_to_array_variable_1 | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1 | Condition_1 | If | - | - | Update_item |  |
| /properties/definition/actions/Condition_1/actions/Select_-_Available_Assets | Select_-_Available_Assets | Select | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1/actions/Create_CSV_table_-_Available_Assets | Create_CSV_table_-_Available_Assets | Table | - | - | Select_-_Available_Assets |  |
| /properties/definition/actions/Condition_1/actions/Filter_array_-_Confirmed_True | Filter_array_-_Confirmed_True | Query | - | - | Create_CSV_table_-_Available_Assets |  |
| /properties/definition/actions/Condition_1/actions/Filter_array_-_Confirmed_False | Filter_array_-_Confirmed_False | Query | - | - | Filter_array_-_Confirmed_True |  |
| /properties/definition/actions/Condition_1/actions/Compose_-_Table_Confirmed | Compose_-_Table_Confirmed | Compose | - | - | Filter_array_-_Confirmed_False |  |
| /properties/definition/actions/Condition_1/actions/Add_attachment | Add_attachment | OpenApiConnection | shared_sharepointonline | CreateAttachment | Compose_-_Table_Confirmed | body, dataset, displayName, itemId, table |
| /properties/definition/actions/Condition_1/actions/Do_until | Do_until | Until | - | - | Set_variable_-_Reset_Temp_Approver_Data |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Set_variable__-_Approver_Table | Set_variable__-_Approver_Table | SetVariable | - | - | Select_-_Approver_Data_Updated |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Apply_to_each_-_Approver_Table | Apply_to_each_-_Approver_Table | Foreach | - | - | Set_variable__-_Approver_Table |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Apply_to_each_-_Approver_Table/actions/Append_to_string_variable | Append_to_string_variable | AppendToStringVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Increment_variable_-_Order_Approver | Increment_variable_-_Order_Approver | IncrementVariable | - | - | Apply_to_each_-_Approver_Table |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Filter_array_-_Approver_Order | Filter_array_-_Approver_Order | Query | - | - | Increment_variable_-_Order_Approver |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Parse_JSON_-_Approver_Data_Updated | Parse_JSON_-_Approver_Data_Updated | ParseJson | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Select_-_Approver_Data_Updated | Select_-_Approver_Data_Updated | Select | - | - | Parse_JSON_-_Approver_Data_Updated |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Sent_Approval | Condition_-_Sent_Approval | If | - | - | Filter_array_-_Approver_Order |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Sent_Approval/actions/Update_item_-_Current_Approver | Update_item_-_Current_Approver | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Current_Approver, item/Status, table |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Sent_Approval/actions/Create_an_approval | Create_an_approval | OpenApiConnection | shared_approvals | CreateAnApproval | Update_item_-_Current_Approver | ApprovalCreationInput/assignedTo, ApprovalCreationInput/attachments, ApprovalCreationInput/details, ApprovalCreationInput/enableNotifications, ApprovalCreationInput/enableReassignment, ApprovalCreationInput/requestor, ApprovalCreationInput/title, approvalType |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Sent_Approval/actions/Send_an_email_(V2) | Send_an_email_(V2) | OpenApiConnection | shared_office365 | SendEmailV2 | Create_an_approval |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Sent_Approval/actions/Wait_for_an_approval | Wait_for_an_approval | OpenApiConnectionWebhook | shared_approvals | WaitForAnApproval | Send_an_email_(V2) | approvalName |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Apply_to_each_-_Update_Approver_Data | Apply_to_each_-_Update_Approver_Data | Foreach | - | - | Condition_-_Sent_Approval |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Apply_to_each_-_Update_Approver_Data/actions/Condition_-_Update_Approver_Data | Condition_-_Update_Approver_Data | If | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Apply_to_each_-_Update_Approver_Data/actions/Condition_-_Update_Approver_Data/actions/Append_to_array_variable_-_Current_Approver | Append_to_array_variable_-_Current_Approver | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Apply_to_each_-_Update_Approver_Data/actions/Condition_-_Update_Approver_Data/else/actions/Append_to_array_variable_-_Not_Current_Approver | Append_to_array_variable_-_Not_Current_Approver | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Set_variable_-_Updated_Approver_Data | Set_variable_-_Updated_Approver_Data | SetVariable | - | - | Apply_to_each_-_Update_Approver_Data |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Filter_array_-_All_Approved | Filter_array_-_All_Approved | Query | - | - | Set_variable_-_Updated_Approver_Data |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Q_Last_Approve | Condition_-_Q_Last_Approve | If | - | - | Filter_array_-_All_Approved |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Q_Last_Approve/actions/Update_item_-_All_Approve | Update_item_-_All_Approve | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Approval_Status, item/Status, table |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Q_Last_Approve/else/actions/Set_variable_-_Reset_Temp_Approver_Data_2 | Set_variable_-_Reset_Temp_Approver_Data_2 | SetVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Current_Approver_Accept_Reject | Condition_-_Current_Approver_Accept_Reject | If | - | - | Condition_-_Q_Last_Approve |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Current_Approver_Accept_Reject/actions/Update_item_-_Accept | Update_item_-_Accept | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Approval_Data, table |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Current_Approver_Accept_Reject/else/actions/Condition_2 | Condition_2 | If | - | - | Compose |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Current_Approver_Accept_Reject/else/actions/Condition_2/actions/Update_item_-_Reject | Update_item_-_Reject | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Approval_Data, item/Approval_Status, table |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Current_Approver_Accept_Reject/else/actions/Condition_2/actions/Set_variable_-_Max_Approver_Index | Set_variable_-_Max_Approver_Index | SetVariable | - | - | Update_item_-_Reject |  |
| /properties/definition/actions/Condition_1/actions/Do_until/actions/Condition_-_Current_Approver_Accept_Reject/else/actions/Compose | Compose | Compose | - | - | (scope entry) |  |
| /properties/definition/actions/Condition_1/actions/Set_variable_-_Reset_Temp_Approver_Data | Set_variable_-_Reset_Temp_Approver_Data | SetVariable | - | - | Add_attachment |  |
| /properties/definition/actions/Filter_array | Filter_array | Query | - | - | Select_-_Approver_Data_Initial |  |
| /properties/definition/actions/Filter_array_1 | Filter_array_1 | Query | - | - | Apply_to_each |  |
| /properties/definition/actions/Update_item | Update_item | OpenApiConnection | shared_sharepointonline | PatchItem | Set_variable | dataset, id, item/Approval_Data, table |
| /properties/definition/actions/Set_variable | Set_variable | SetVariable | - | - | Filter_array_1 |  |
| /properties/definition/actions/Get_file_content | Get_file_content | OpenApiConnection | shared_sharepointonline | GetFileContent | Get_items | dataset, id, inferContentType |
