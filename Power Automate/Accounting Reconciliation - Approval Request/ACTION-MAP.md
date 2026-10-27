# Accounting Reconciliation - Approval Request — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Get_items | Get_items | OpenApiConnection | shared_sharepointonline | GetItems | Initialize_variable_-_Table_Approvers | $filter, dataset, table |
| /properties/definition/actions/Parse_JSON_Table_Accounting | Parse_JSON_Table_Accounting | ParseJson | - | - | Create_IT_Asset_CSV |  |
| /properties/definition/actions/Parse_JSON_Table_IT_Governance | Parse_JSON_Table_IT_Governance | ParseJson | - | - | Create_Markdown_Table_Accounting_-_3 |  |
| /properties/definition/actions/Select_IT_Asset_CSV | Select_IT_Asset_CSV | Select | - | - | Create_Non-IT_Asset_CSV |  |
| /properties/definition/actions/Create_IT_Asset_CSV | Create_IT_Asset_CSV | Table | - | - | Select_IT_Asset_CSV |  |
| /properties/definition/actions/Add_attachment_-_Asset_IT | Add_attachment_-_Asset_IT | OpenApiConnection | shared_sharepointonline | CreateAttachment | Update_item | body, dataset, displayName, itemId, table |
| /properties/definition/actions/Select_Non-IT_Asset_CSV | Select_Non-IT_Asset_CSV | Select | - | - | Create_Disposed_IT_Asset_CSV |  |
| /properties/definition/actions/Create_Non-IT_Asset_CSV | Create_Non-IT_Asset_CSV | Table | - | - | Select_Non-IT_Asset_CSV |  |
| /properties/definition/actions/Create_Markdown_Table_Accounting_-_1 | Create_Markdown_Table_Accounting_-_1 | Select | - | - | Parse_JSON_Table_Accounting |  |
| /properties/definition/actions/Create_Markdown_Table_Accounting_-_3 | Create_Markdown_Table_Accounting_-_3 | Compose | - | - | Create_Markdown_Table_Accounting_-_2 |  |
| /properties/definition/actions/Create_Markdown_Table_Accounting_-_2 | Create_Markdown_Table_Accounting_-_2 | Select | - | - | Create_Markdown_Table_Accounting_-_1 |  |
| /properties/definition/actions/Create_Markdown_Table_Governance_-_1 | Create_Markdown_Table_Governance_-_1 | Select | - | - | Parse_JSON_Table_IT_Governance |  |
| /properties/definition/actions/Create_Markdown_Table_Governance_-_2 | Create_Markdown_Table_Governance_-_2 | Select | - | - | Create_Markdown_Table_Governance_-_1 |  |
| /properties/definition/actions/Create_Markdown_Table_Governance_-_3 | Create_Markdown_Table_Governance_-_3 | Compose | - | - | Create_Markdown_Table_Governance_-_2 |  |
| /properties/definition/actions/Initialize_variable_-_varApproverIndex | Initialize_variable_-_varApproverIndex | InitializeVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Initialize_variable_-_varFinalOutcome | Initialize_variable_-_varFinalOutcome | InitializeVariable | - | - | Initialize_variable_-_varApproverIndex |  |
| /properties/definition/actions/Initialize_variable_-_varStopDoUntil | Initialize_variable_-_varStopDoUntil | InitializeVariable | - | - | Initialize_variable_-_varFinalOutcome |  |
| /properties/definition/actions/Do_until | Do_until | Until | - | - | Condition_3 |  |
| /properties/definition/actions/Do_until/actions/Increment_variable | Increment_variable | IncrementVariable | - | - | Apply_to_each_-_Approver_Table |  |
| /properties/definition/actions/Do_until/actions/Filter_array | Filter_array | Query | - | - | Increment_variable |  |
| /properties/definition/actions/Do_until/actions/Parse_JSON_-_Approver_Data | Parse_JSON_-_Approver_Data | ParseJson | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Select_-_Approver_Data | Select_-_Approver_Data | Select | - | - | Parse_JSON_-_Approver_Data |  |
| /properties/definition/actions/Do_until/actions/Apply_to_each | Apply_to_each | Foreach | - | - | Condition_3_1 |  |
| /properties/definition/actions/Do_until/actions/Apply_to_each/actions/Condition | Condition | If | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Apply_to_each/actions/Condition/actions/Condition_3_1_1 | Condition_3_1_1 | If | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Apply_to_each/actions/Condition/actions/Condition_3_1_1/actions/Append_to_array_variable | Append_to_array_variable | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Apply_to_each/actions/Condition/actions/Condition_3_1_1/else/actions/Append_to_array_variable_2 | Append_to_array_variable_2 | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Apply_to_each/actions/Condition/else/actions/Append_to_array_variable_1 | Append_to_array_variable_1 | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Update_item_1_1 | Update_item_1_1 | OpenApiConnection | shared_sharepointonline | PatchItem | Filter_array | dataset, id, item/Current_Approver, table |
| /properties/definition/actions/Do_until/actions/Condition_2 | Condition_2 | If | - | - | Filter_array_1 |  |
| /properties/definition/actions/Do_until/actions/Condition_2/actions/Update_item_1_3 | Update_item_1_3 | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Approval_Status, table |
| /properties/definition/actions/Do_until/actions/Condition_2/else/actions/Set_variable_1 | Set_variable_1 | SetVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Set_variable | Set_variable | SetVariable | - | - | Apply_to_each |  |
| /properties/definition/actions/Do_until/actions/Filter_array_1 | Filter_array_1 | Query | - | - | Set_variable |  |
| /properties/definition/actions/Do_until/actions/Apply_to_each_-_Approver_Table | Apply_to_each_-_Approver_Table | Foreach | - | - | Set_variable__-_Approver_Table |  |
| /properties/definition/actions/Do_until/actions/Apply_to_each_-_Approver_Table/actions/Append_to_string_variable | Append_to_string_variable | AppendToStringVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Set_variable__-_Approver_Table | Set_variable__-_Approver_Table | SetVariable | - | - | Select_-_Approver_Data |  |
| /properties/definition/actions/Do_until/actions/Condition_3_1 | Condition_3_1 | If | - | - | Update_item_1_1 |  |
| /properties/definition/actions/Do_until/actions/Condition_3_1/actions/Create_an_approval_-_Dispose | Create_an_approval_-_Dispose | OpenApiConnection | shared_approvals | CreateAnApproval | (scope entry) | ApprovalCreationInput/assignedTo, ApprovalCreationInput/attachments, ApprovalCreationInput/details, ApprovalCreationInput/enableNotifications, ApprovalCreationInput/enableReassignment, ApprovalCreationInput/title, approvalType |
| /properties/definition/actions/Do_until/actions/Condition_3_1/actions/Send_an_email_(V2) | Send_an_email_(V2) | OpenApiConnection | shared_office365 | SendEmailV2 | Create_an_approval_-_Dispose |  |
| /properties/definition/actions/Do_until/actions/Condition_3_1/actions/Wait_for_an_approval | Wait_for_an_approval | OpenApiConnectionWebhook | shared_approvals | WaitForAnApproval | Send_an_email_(V2) | approvalName |
| /properties/definition/actions/Do_until/actions/Condition_3_1/else/actions/Create_an_approval_-_No_Dispose | Create_an_approval_-_No_Dispose | OpenApiConnection | shared_approvals | CreateAnApproval | (scope entry) | ApprovalCreationInput/assignedTo, ApprovalCreationInput/attachments, ApprovalCreationInput/details, ApprovalCreationInput/enableNotifications, ApprovalCreationInput/enableReassignment, ApprovalCreationInput/title, approvalType |
| /properties/definition/actions/Do_until/actions/Condition_3_1/else/actions/Send_an_email_(V2)_-_No_Dispose | Send_an_email_(V2)_-_No_Dispose | OpenApiConnection | shared_office365 | SendEmailV2 | Create_an_approval_-_No_Dispose |  |
| /properties/definition/actions/Do_until/actions/Condition_3_1/else/actions/Wait_for_an_approval_-_No_Dispose | Wait_for_an_approval_-_No_Dispose | OpenApiConnectionWebhook | shared_approvals | WaitForAnApproval | Send_an_email_(V2)_-_No_Dispose | approvalName |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1 | Condition_3_1_1_1 | If | - | - | Condition_2 |  |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1/actions/Condition_1 | Condition_1 | If | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1/actions/Condition_1/actions/Update_item_1 | Update_item_1 | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Approval_Data, table |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1/actions/Condition_1/else/actions/Update_item_1_2 | Update_item_1_2 | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Approval_Data, item/Approval_Status, table |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1/actions/Condition_1/else/actions/Set_variable_2 | Set_variable_2 | SetVariable | - | - | Update_item_1_2 |  |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1/else/actions/Condition_1_1 | Condition_1_1 | If | - | - | (scope entry) |  |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1/else/actions/Condition_1_1/actions/Update_item_2 | Update_item_2 | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Approval_Data, table |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1/else/actions/Condition_1_1/else/actions/Update_item_1_4 | Update_item_1_4 | OpenApiConnection | shared_sharepointonline | PatchItem | (scope entry) | dataset, id, item/Approval_Data, item/Approval_Status, table |
| /properties/definition/actions/Do_until/actions/Condition_3_1_1_1/else/actions/Condition_1_1/else/actions/Set_variable_3 | Set_variable_3 | SetVariable | - | - | Update_item_1_4 |  |
| /properties/definition/actions/Update_item | Update_item | OpenApiConnection | shared_sharepointonline | PatchItem | Set_variable_-_Approver_Data_Initialize | dataset, id, item/Approval_Data, item/Approval_Status, table |
| /properties/definition/actions/Initialize_variable_-_Approver_Data | Initialize_variable_-_Approver_Data | InitializeVariable | - | - | Initialize_variable_-_varStopDoUntil |  |
| /properties/definition/actions/Set_variable_-_Approver_Data_Initialize | Set_variable_-_Approver_Data_Initialize | SetVariable | - | - | Create_Markdown_Table_New_Asset_-_3 |  |
| /properties/definition/actions/Initialize_variable_-_Temp_Approver_Data | Initialize_variable_-_Temp_Approver_Data | InitializeVariable | - | - | Initialize_variable_-_Approver_Data |  |
| /properties/definition/actions/Initialize_variable_-_Table_Approvers | Initialize_variable_-_Table_Approvers | InitializeVariable | - | - | Initialize_variable_-_Temp_Approver_Data |  |
| /properties/definition/actions/Select_Disposed_IT_Asset_CSV | Select_Disposed_IT_Asset_CSV | Select | - | - | Get_items |  |
| /properties/definition/actions/Create_Disposed_IT_Asset_CSV | Create_Disposed_IT_Asset_CSV | Table | - | - | Select_Disposed_IT_Asset_CSV |  |
| /properties/definition/actions/Condition_3 | Condition_3 | If | - | - | Get_file_content |  |
| /properties/definition/actions/Condition_3/actions/Add_attachment_-_Disposed_IT_Asset | Add_attachment_-_Disposed_IT_Asset | OpenApiConnection | shared_sharepointonline | CreateAttachment | (scope entry) | body, dataset, displayName, itemId, table |
| /properties/definition/actions/Add_attachment_-_Non_Asset_IT | Add_attachment_-_Non_Asset_IT | OpenApiConnection | shared_sharepointonline | CreateAttachment | Add_attachment_-_Asset_IT | body, dataset, displayName, itemId, table |
| /properties/definition/actions/Filter_array_New_Asset_Markdown | Filter_array_New_Asset_Markdown | Query | - | - | Create_Markdown_Table_Governance_-_3 |  |
| /properties/definition/actions/Create_Markdown_Table_New_Asset_-_2 | Create_Markdown_Table_New_Asset_-_2 | Select | - | - | Create_Markdown_Table_New_Asset |  |
| /properties/definition/actions/Create_Markdown_Table_New_Asset_-_3 | Create_Markdown_Table_New_Asset_-_3 | Compose | - | - | Create_Markdown_Table_New_Asset_-_2 |  |
| /properties/definition/actions/Create_Markdown_Table_New_Asset | Create_Markdown_Table_New_Asset | Select | - | - | Filter_array_New_Asset_Markdown |  |
| /properties/definition/actions/Get_file_content | Get_file_content | OpenApiConnection | shared_sharepointonline | GetFileContent | Add_attachment_-_Non_Asset_IT | dataset, id, inferContentType |
