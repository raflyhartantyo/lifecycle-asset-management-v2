# Accounting_ReconsiliationV2 — action map

Every nested action is indexed. Use each JSON pointer in `definition.json` for exact expressions, conditions, schemas, settings and payloads. `runAfter` is local to its enclosing scope; preserve success/failure/timeout/skipped statuses from the source. Table order is an inventory, not execution order.

| JSON pointer | Action | Type | Connector | Operation | runAfter actions | Parameter fields |
|---|---|---|---|---|---|---|
| /properties/definition/actions/Create_file | Create_file | OpenApiConnection | shared_sharepointonline | CreateFile | (scope entry) | body, dataset, folderPath, name |
| /properties/definition/actions/Respond_to_a_Power_App_or_flow_1 | Respond_to_a_Power_App_or_flow_1 | Response | - | - | Create_item_1 |  |
| /properties/definition/actions/Create_item_1 | Create_item_1 | OpenApiConnection | shared_sharepointonline | PostItem | Initialize_variable | dataset, item/Status, item/Title, table |
| /properties/definition/actions/Initialize_variable | Initialize_variable | InitializeVariable | - | - | Create_file |  |
| /properties/definition/actions/Try | Try | Scope | - | - | Initialize_varExpandedRows |  |
| /properties/definition/actions/Try/actions/Get_items | Get_items | OpenApiConnection | shared_sharepointonline | GetItems | (scope entry) | dataset, table |
| /properties/definition/actions/Try/actions/Set_varSPRows | Set_varSPRows | SetVariable | - | - | Get_items |  |
| /properties/definition/actions/Try/actions/Select_varSPMap | Select_varSPMap | Select | - | - | Set_varSPRows |  |
| /properties/definition/actions/Try/actions/Set_varSPMap | Set_varSPMap | SetVariable | - | - | Select_varSPMap |  |
| /properties/definition/actions/Try/actions/Select_varSPCodesRemaining | Select_varSPCodesRemaining | Select | - | - | Set_varSPMap |  |
| /properties/definition/actions/Try/actions/Set_varSPCodesRemaining | Set_varSPCodesRemaining | SetVariable | - | - | Select_varSPCodesRemaining |  |
| /properties/definition/actions/Try/actions/Get_tables | Get_tables | OpenApiConnection | shared_excelonlinebusiness | GetTables | Set_varSPCodesRemaining | drive, file, source |
| /properties/definition/actions/Try/actions/List_rows_present_in_a_table | List_rows_present_in_a_table | OpenApiConnection | shared_excelonlinebusiness | GetItems | Get_tables | drive, file, source, table |
| /properties/definition/actions/Try/actions/Set_varExcelRows | Set_varExcelRows | SetVariable | - | - | List_rows_present_in_a_table |  |
| /properties/definition/actions/Try/actions/Filter_array | Filter_array | Query | - | - | Set_varExcelRows |  |
| /properties/definition/actions/Try/actions/Set_varExcelRowsFiltered | Set_varExcelRowsFiltered | SetVariable | - | - | Filter_array |  |
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
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/actions/Append_to_[AssetCode] | Append_to_[AssetCode] | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/actions/Append_to_[AssetCodeConcat] | Append_to_[AssetCodeConcat] | AppendToArrayVariable | - | - | Append_to_[AssetCode] |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/else/actions/Condition_2 | Condition_2 | If | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Condition_1/else/actions/Condition_2/actions/Append_to_array_variable | Append_to_array_variable | AppendToArrayVariable | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/CurAssetCodeConcat | CurAssetCodeConcat | Compose | - | - | CurAssetCode |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Filter_array_1 | Filter_array_1 | Query | - | - | CurMonth |  |
| /properties/definition/actions/Try/actions/Apply_to_each_-_Matching/actions/Filter_array_2 | Filter_array_2 | Query | - | - | Filter_array_1 |  |
| /properties/definition/actions/Try/actions/Select_1 | Select_1 | Select | - | - | Apply_to_each_-_Matching |  |
| /properties/definition/actions/Try/actions/Compose_2 | Compose_2 | Compose | - | - | Select_1 |  |
| /properties/definition/actions/Try/actions/Filter_array_SPCodesRemaining | Filter_array_SPCodesRemaining | Query | - | - | Compose_2 |  |
| /properties/definition/actions/Try/actions/Compose_5 | Compose_5 | Compose | - | - | Filter_array_SPCodesRemaining |  |
| /properties/definition/actions/Try/actions/Update_item | Update_item | OpenApiConnection | shared_sharepointonline | PatchItem | Compose_5 | dataset, id, item/Differences, item/NewAssetLatestMonth, item/Status, table |
| /properties/definition/actions/Try/actions/arrQtyGT1 | arrQtyGT1 | Query | - | - | Set_varExcelRowsFiltered |  |
| /properties/definition/actions/Try/actions/arrQtyLE1 | arrQtyLE1 | Query | - | - | arrQtyGT1 |  |
| /properties/definition/actions/Try/actions/Apply_to_each | Apply_to_each | Foreach | - | - | arrQtyLE1 |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/compRange | compRange | Compose | - | - | (scope entry) |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/selExpandedRowsForThisAsset | selExpandedRowsForThisAsset | Select | - | - | compRange |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/Set_variable | Set_variable | SetVariable | - | - | Compose_3 |  |
| /properties/definition/actions/Try/actions/Apply_to_each/actions/Compose_3 | Compose_3 | Compose | - | - | selExpandedRowsForThisAsset |  |
| /properties/definition/actions/Try/actions/Set_variable_1 | Set_variable_1 | SetVariable | - | - | Compose_4 |  |
| /properties/definition/actions/Try/actions/Compose_4 | Compose_4 | Compose | - | - | Apply_to_each |  |
| /properties/definition/actions/Initialize_varSPRows | Initialize_varSPRows | InitializeVariable | - | - | Respond_to_a_Power_App_or_flow_1 |  |
| /properties/definition/actions/Initialize_varSPMap | Initialize_varSPMap | InitializeVariable | - | - | Initialize_varSPRows |  |
| /properties/definition/actions/Initialize_varSPCodesRemaining | Initialize_varSPCodesRemaining | InitializeVariable | - | - | Initialize_varSPMap |  |
| /properties/definition/actions/Initialize_varExcelRows | Initialize_varExcelRows | InitializeVariable | - | - | Initialize_varSPCodesRemaining |  |
| /properties/definition/actions/Initialize_varExcelRowsFiltered | Initialize_varExcelRowsFiltered | InitializeVariable | - | - | Initialize_varExcelRows |  |
| /properties/definition/actions/Initialize_arrMaxDate | Initialize_arrMaxDate | InitializeVariable | - | - | Initialize_varExcelRowsFiltered |  |
| /properties/definition/actions/Initialize_varNotFoundLatest | Initialize_varNotFoundLatest | InitializeVariable | - | - | Initialize_arrMaxDate |  |
| /properties/definition/actions/Initialize_varFoundCodes | Initialize_varFoundCodes | InitializeVariable | - | - | Initialize_varNotFoundLatest |  |
| /properties/definition/actions/Catch | Catch | Scope | - | - | Try |  |
| /properties/definition/actions/Catch/actions/Error_Catching | Error_Catching | Query | - | - | (scope entry) |  |
| /properties/definition/actions/Catch/actions/Terminate | Terminate | Terminate | - | - | Update_error |  |
| /properties/definition/actions/Catch/actions/Update_error | Update_error | OpenApiConnection | shared_sharepointonline | PatchItem | Error_Catching | dataset, id, item/ErrorDetails, item/Result, item/Status, table |
| /properties/definition/actions/Initialize_varExpandedRows | Initialize_varExpandedRows | InitializeVariable | - | - | Initialize_varFoundCodes |  |
