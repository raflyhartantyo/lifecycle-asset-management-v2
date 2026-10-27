# Accounting_ReconsiliationV3 — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Create_file | Create_file | OpenApiConnection | shared_sharepointonline | CreateFile | (scope entry) | body, dataset, folderPath, name |
| /properties/definition/actions/GUID_Initialize | GUID_Initialize | InitializeVariable | - | - | Create_file |  |
| /properties/definition/actions/Create_Result_List | Create_Result_List | OpenApiConnection | shared_sharepointonline | PostItem | GUID_Initialize | dataset, item/Status, item/Title, table |
| /properties/definition/actions/Initialize_varSPRows | Initialize_varSPRows | InitializeVariable | - | - | Respond_to_a_Power_App_or_flow |  |
| /properties/definition/actions/Initialize_varSPMap | Initialize_varSPMap | InitializeVariable | - | - | Initialize_varSPRows |  |
| /properties/definition/actions/Initialize_varSPCodesRemaining | Initialize_varSPCodesRemaining | InitializeVariable | - | - | Initialize_varSPMap |  |
| /properties/definition/actions/Initialize_varExcelRows | Initialize_varExcelRows | InitializeVariable | - | - | Initialize_varSPCodesRemaining |  |
| /properties/definition/actions/Initialize_varExcelRowsFiltered | Initialize_varExcelRowsFiltered | InitializeVariable | - | - | Initialize_varExcelRows |  |
| /properties/definition/actions/Initialize_arrMaxDate | Initialize_arrMaxDate | InitializeVariable | - | - | Initialize_varExcelRowsFiltered |  |
| /properties/definition/actions/Initialize_varNotFoundLatest | Initialize_varNotFoundLatest | InitializeVariable | - | - | Initialize_arrMaxDate |  |
| /properties/definition/actions/Initialize_varFoundCodes | Initialize_varFoundCodes | InitializeVariable | - | - | Initialize_varNotFoundLatest |  |
| /properties/definition/actions/Initialize_varExpandedRows | Initialize_varExpandedRows | InitializeVariable | - | - | Initialize_varFoundCodes |  |
| /properties/definition/actions/Try | Try | Scope | - | - | Initialize_GroupedResultSP |  |
| /properties/definition/actions/Try/actions/Get_items | Get_items | OpenApiConnection | shared_sharepointonline | GetItems | (scope entry) | dataset, table |
| /properties/definition/actions/Try/actions/Set_varSPRows | Set_varSPRows | SetVariable | - | - | Get_items |  |
| /properties/definition/actions/Try/actions/Select_varSPMap | Select_varSPMap | Select | - | - | Set_varSPRows |  |
| /properties/definition/actions/Try/actions/Set_varSPMap | Set_varSPMap | SetVariable | - | - | Select_varSPMap |  |
| /properties/definition/actions/Try/actions/Select_varSPCodesRemaining | Select_varSPCodesRemaining | Select | - | - | Set_varSPMap |  |
| /properties/definition/actions/Try/actions/Get_tables | Get_tables | OpenApiConnection | shared_excelonlinebusiness | GetTables | Set_varSPCodesRemaining | drive, file, source |
| /properties/definition/actions/Try/actions/List_rows_present_in_a_table | List_rows_present_in_a_table | OpenApiConnection | shared_excelonlinebusiness | GetItems | Get_tables | drive, file, source, table |
| /properties/definition/actions/Try/actions/Set_varExcelRows | Set_varExcelRows | SetVariable | - | - | List_rows_present_in_a_table |  |
| /properties/definition/actions/Try/actions/Filter_array | Filter_array | Query | - | - | Set_varExcelRows |  |
| /properties/definition/actions/Try/actions/Set_varExcelRowsFiltered | Set_varExcelRowsFiltered | SetVariable | - | - | Filter_array |  |
| /properties/definition/actions/Try/actions/arrQtyLE1 | arrQtyLE1 | Query | - | - | arrQtyGT1 |  |
| /properties/definition/actions/Try/actions/Apply_to_each | Apply_to_each | Foreach | - | - | arrQtyLE1 |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/compRange | compRange | Compose | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/Set_variable | Set_variable | SetVariable | - | - | Compose_3 |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/Compose_3 | Compose_3 | Compose | - | - | selExpandedRowsForThisAsset |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/selExpandedRowsForThisAsset | selExpandedRowsForThisAsset | Select | - | - | compRange |  |
| /properties/definition/actions/Try/actions/arrQtyGT1 | arrQtyGT1 | Query | - | - | Set_varExcelRowsFiltered |  |
| /properties/definition/actions/Try/actions/Compose_4 | Compose_4 | Compose | - | - | Apply_to_each |  |
| /properties/definition/actions/Try/actions/Set_variable_1 | Set_variable_1 | SetVariable | - | - | Compose_4 |  |
| /properties/definition/actions/Try/actions/Select | Select | Select | - | - | Set_variable_1 |  |
| /properties/definition/actions/Try/actions/Set_arrMaxDate | Set_arrMaxDate | SetVariable | - | - | Select |  |
| /properties/definition/actions/Try/actions/Compose | Compose | Compose | - | - | Set_arrMaxDate |  |
| /properties/definition/actions/Try/actions/Compose_1 | Compose_1 | Compose | - | - | Compose |  |
| /properties/definition/actions/Try/actions/varMaxMonth | varMaxMonth | Compose | - | - | Compose_1 |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching | Apply_to_each_-_Matching | Foreach | - | - | varMaxMonth |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/CurAssetCode | CurAssetCode | Compose | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/CurBookVal | CurBookVal | Compose | - | - | CurAssetCodeConcat |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/CurMonth | CurMonth | Compose | - | - | CurBookVal |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1 | Condition_1 | If | - | - | Filter_array_2 |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/actions/Append_ALL_to_varFoundCodes | Append_ALL_to_varFoundCodes | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/actions/Append_to_[AssetCode]_1 | Append_to_[AssetCode]_1 | AppendToArrayVariable | - | - | Append_ALL_to_varFoundCodes |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/actions/Append_to_[AssetCodeConcat] | Append_to_[AssetCodeConcat] | AppendToArrayVariable | - | - | Append_to_[AssetCode]_1 |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/else/actions/Condition_2 | Condition_2 | If | - | - | Append_to_VarNotFoundCodes |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/else/actions/Condition_2/actions/Append_to_array_variable | Append_to_array_variable | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/else/actions/Append_to_VarNotFoundCodes | Append_to_VarNotFoundCodes | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/CurAssetCodeConcat | CurAssetCodeConcat | Compose | - | - | CurAssetCode |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Filter_array_1 | Filter_array_1 | Query | - | - | CurMonth |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Filter_array_2 | Filter_array_2 | Query | - | - | Filter_array_1 |  |
| /properties/definition/actions/Try/actions/Set_varSPCodesRemaining | Set_varSPCodesRemaining | SetVariable | - | - | Select_varSPCodesRemaining |  |
| /properties/definition/actions/Try/actions/SPCodesRemainingCode | SPCodesRemainingCode | Select | - | - | Apply_to_each_-_Matching |  |
| /properties/definition/actions/Try/actions/Filter_array_SPCodesRemaining | Filter_array_SPCodesRemaining | Query | - | - | SPCodesRemainingCode |  |
| /properties/definition/actions/Try/actions/Check_varNotFoundLatest | Check_varNotFoundLatest | Compose | - | - | Check_varFoundCodes |  |
| /properties/definition/actions/Try/actions/Check_varFoundCodes | Check_varFoundCodes | Compose | - | - | Check_VarNotFoundCodes |  |
| /properties/definition/actions/Try/actions/Check_VarNotFoundCodes | Check_VarNotFoundCodes | Compose | - | - | Filter_array_SPCodesRemaining |  |
| /properties/definition/actions/Try/actions/Check_Differences | Check_Differences | Compose | - | - | Check_varNotFoundLatest |  |
| /properties/definition/actions/Try/actions/Select_ClassAcquis_Acc | Select_ClassAcquis_Acc | Select | - | - | Check_Differences |  |
| /properties/definition/actions/Try/actions/Select_Distinct_Class_Acc | Select_Distinct_Class_Acc | Select | - | - | Select_ClassAcquis_Acc |  |
| /properties/definition/actions/Try/actions/Compose_Dedupe_Class_Acc | Compose_Dedupe_Class_Acc | Compose | - | - | Select_Distinct_Class_Acc |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc | Apply_to_each_Group_Acc | Foreach | - | - | Compose_Dedupe_Class_Acc |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc/actions/Filter_array_Group_Acc | Filter_array_Group_Acc | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc/actions/Sum_Acquisition_Group_Acc | Sum_Acquisition_Group_Acc | Compose | - | - | GroupAccAcq |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc/actions/Append_to_array_variable_Group_Acc | Append_to_array_variable_Group_Acc | AppendToArrayVariable | - | - | Increment_variable_-_Qty_Acc |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc/actions/Sum_Qty_Group_Acc_ | Sum_Qty_Group_Acc_ | Compose | - | - | GroupAccQty |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc/actions/GroupAccAcq | GroupAccAcq | Select | - | - | Filter_array_Group_Acc |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc/actions/GroupAccQty | GroupAccQty | Select | - | - | Increment_variable_-_Acquisition_Acc |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc/actions/Increment_variable_-_Acquisition_Acc | Increment_variable_-_Acquisition_Acc | IncrementVariable | - | - | Sum_Acquisition_Group_Acc |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_Acc/actions/Increment_variable_-_Qty_Acc | Increment_variable_-_Qty_Acc | IncrementVariable | - | - | Sum_Qty_Group_Acc_ |  |
| /properties/definition/actions/Try/actions/Select_ClassAcquis_SP | Select_ClassAcquis_SP | Select | - | - | Append_to_array_variable_Group_Acc_Total |  |
| /properties/definition/actions/Try/actions/Select_Distinct_Class_SP | Select_Distinct_Class_SP | Select | - | - | Select_ClassAcquis_SP |  |
| /properties/definition/actions/Try/actions/Compose_Dedupe_Class_SP | Compose_Dedupe_Class_SP | Compose | - | - | Select_Distinct_Class_SP |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_SP | Apply_to_each_Group_SP | Foreach | - | - | Compose_Dedupe_Class_SP |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_SP/actions/Filter_array_Group_SP | Filter_array_Group_SP | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_SP/actions/Sum_Acquisition_Group_SP | Sum_Acquisition_Group_SP | Compose | - | - | GroupSPAcq |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_SP/actions/Sum_Qty_Group_SP | Sum_Qty_Group_SP | Compose | - | - | Increment_variable_-_Acquisition_SP |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_SP/actions/GroupSPAcq | GroupSPAcq | Select | - | - | Filter_array_Group_SP |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_SP/actions/Append_to_array_variable_Group_SP | Append_to_array_variable_Group_SP | AppendToArrayVariable | - | - | Increment_variable_-_Qty_SP |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_SP/actions/Increment_variable_-_Acquisition_SP | Increment_variable_-_Acquisition_SP | IncrementVariable | - | - | Sum_Acquisition_Group_SP |  |
| /properties/definition/actions/Try/actions/Apply_to_each_Group_SP/actions/Increment_variable_-_Qty_SP | Increment_variable_-_Qty_SP | IncrementVariable | - | - | Sum_Qty_Group_SP |  |
| /properties/definition/actions/Try/actions/Append_to_array_variable_Group_Acc_Total | Append_to_array_variable_Group_Acc_Total | AppendToArrayVariable | - | - | Apply_to_each_Group_Acc |  |
| /properties/definition/actions/Try/actions/Append_to_array_variable_Group_Acc_Total_1 | Append_to_array_variable_Group_Acc_Total_1 | AppendToArrayVariable | - | - | Apply_to_each_Group_SP |  |
| /properties/definition/actions/Try/actions/Get_items_-_Disposed_Assets | Get_items_-_Disposed_Assets | OpenApiConnection | shared_sharepointonline | GetItems | Append_to_array_variable_Group_Acc_Total_1 | dataset, table |
| /properties/definition/actions/Try/actions/Filter_array__-_Disposed_Assets | Filter_array__-_Disposed_Assets | Query | - | - | Get_items_-_Disposed_Assets |  |
| /properties/definition/actions/Try/actions/Select_-_Disposed_Assets | Select_-_Disposed_Assets | Select | - | - | Filter_array__-_Disposed_Assets |  |
| /properties/definition/actions/Try/actions/Update_item | Update_item | OpenApiConnection | shared_sharepointonline | PatchItem | Compose_String_-_Disposed_Assets | dataset, id, item/Acc_IT, item/Differences, item/Disposed_IT_Assets, item/Gov_IT, item/IT_Asset, item/NewAssetLatestMonth, item/Non_IT_Asset, item/Status, table |
| /properties/definition/actions/Try/actions/Compose_String_-_Disposed_Assets | Compose_String_-_Disposed_Assets | Compose | - | - | Select_-_Disposed_Assets |  |
| /properties/definition/actions/Catch | Catch | Scope | - | - | Try |  |
| /properties/definition/actions/Catch/actions/Error_Catching | Error_Catching | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Catch/actions/Terminate | Terminate | Terminate | - | - | Update_error |  |
| /properties/definition/actions/Catch/actions/Update_error | Update_error | OpenApiConnection | shared_sharepointonline | PatchItem | Error_Catching | dataset, id, item/ErrorDetails, item/Result, table |
| /properties/definition/actions/Initialize_VarNotFoundCodes | Initialize_VarNotFoundCodes | InitializeVariable | - | - | Initialize_varExpandedRows |  |
| /properties/definition/actions/Initialize_varNotFoundCodesPure | Initialize_varNotFoundCodesPure | InitializeVariable | - | - | Initialize_VarNotFoundCodes |  |
| /properties/definition/actions/Initialize_GroupedResultAcc | Initialize_GroupedResultAcc | InitializeVariable | - | - | Initialize_varNotFoundCodesPure |  |
| /properties/definition/actions/Initialize_GroupedResultSP | Initialize_GroupedResultSP | InitializeVariable | - | - | Initialize_TotalGroupedResultSPVal |  |
| /properties/definition/actions/Respond_to_a_Power_App_or_flow | Respond_to_a_Power_App_or_flow | Response | - | - | Create_Result_List |  |
| /properties/definition/actions/Initialize_TotalGroupedResultAccQty | Initialize_TotalGroupedResultAccQty | InitializeVariable | - | - | Initialize_GroupedResultAcc |  |
| /properties/definition/actions/Initialize_TotalGroupedResultAccVal | Initialize_TotalGroupedResultAccVal | InitializeVariable | - | - | Initialize_TotalGroupedResultAccQty |  |
| /properties/definition/actions/Initialize_TotalGroupedResultSPQty | Initialize_TotalGroupedResultSPQty | InitializeVariable | - | - | Initialize_TotalGroupedResultAccVal |  |
| /properties/definition/actions/Initialize_TotalGroupedResultSPVal | Initialize_TotalGroupedResultSPVal | InitializeVariable | - | - | Initialize_TotalGroupedResultSPQty |  |
