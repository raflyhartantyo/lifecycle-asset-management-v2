# Power Automate

15 individually packaged baseline flows. Each folder contains its original definition, trigger contract, configuration worksheet, complete action map, implementation guide, Claude prompt and validation steps. These are reference definitions, not import-ready solution packages.

| Flow | Scope / note | Observed app callers | Actions | Connectors |
|---|---|---|---|---|
| Accounting Reconciliation - Approval Request | Accounting reconciliation approvals remain in V2 scope. D001 retires only the separate disposal-request/approval process; disposal-related branches inside reconciliation require separate review rather than deleting this flow wholesale. | ALM - StockOpname - Available, ALM - StockOpname - In Use, ALM-AccReconcile | 68 | shared_approvals, shared_office365, shared_sharepointonline |
| Accounting_ReconsiliationV2 | Legacy reference: both stock-opname screens still contain V2 calls. Reachability and deployment activation remain unverified. Keep this baseline; use V3 for the future dedicated reconciliation feature only after its contract is tested. | ALM - StockOpname - Available, ALM - StockOpname - In Use | 60 | shared_excelonlinebusiness, shared_sharepointonline |
| Accounting_ReconsiliationV3 | Dedicated ALM-AccReconcile screen references V3. Preserve grouped accounting comparisons and response schema when redesigning. | ALM-AccReconcile | 101 | shared_excelonlinebusiness, shared_sharepointonline |
| Bulk_Registration | Reference baseline. Preserve the current contract and behavior until a specific V2 delivery replaces it. | ALM-Registration | 5 | shared_excelonlinebusiness, shared_sharepointonline |
| Data Refresh ALM | ALM-Dashboard contains DataRefreshALM.Run(). Set the target Power BI workspace and dataset; this flow triggers a refresh, not a guarantee that it has finished. | ALM-Dashboard | 1 | shared_powerbi |
| Export Data | Reference baseline. Preserve the current contract and behavior until a specific V2 delivery replaces it. | ALM - StockOpname - Available, ALM-Asset Master | 9 | shared_sharepointonline |
| Flow Networking Device | Placeholder: the supplied definition only initializes Temp=true. This release provides no networking reconciliation implementation. Keep disabled in the target until an implemented replacement is delivered. | ALM - StockOpname - Available, ALM - StockOpname - In Use | 1 | None |
| InTune Flow | Reference baseline. Preserve the current contract and behavior until a specific V2 delivery replaces it. | ALM - StockOpname - Available, ALM - StockOpname - In Use | 17 | shared_excelonlinebusiness, shared_sharepointonline |
| PowerAppV2 -_ Respond to a Power App or flow | Test/helper reference: returns a fixed Testing array. Keep disabled in the target; this release supplies no production business behavior for it. | No static match | 2 | None |
| Return Master Asset | Reference baseline. Preserve the current contract and behavior until a specific V2 delivery replaces it. | No static match | 3 | shared_sharepointonline |
| SO_Respondent_Save | Reference baseline. Preserve the current contract and behavior until a specific V2 delivery replaces it. | ALM - StockOpname - Available | 17 | shared_sharepointonline, shared_teams |
| SO_Respondents_Confirm | Available-stock confirmation/approval remains in V2 scope. D001 does not retire stock-opname approvals. | ALM - StockOpname - Available | 55 | shared_approvals, shared_office365, shared_sharepointonline |
| Stock_Opname_Available_Trigger | Reference baseline. Preserve the current contract and behavior until a specific V2 delivery replaces it. | ALM - StockOpname - Available | 13 | shared_office365, shared_sharepointonline |
| Stock_Opname_In_Use_Match | Reference baseline. Preserve the current contract and behavior until a specific V2 delivery replaces it. | ALM - StockOpname - In Use | 27 | shared_excelonlinebusiness, shared_sharepointonline, shared_teams |
| Stock_Opname_In_Use_Trigger | Review embedded campaign dates and recipient placeholders before testing; dates in a message are not a recurrence trigger. | ALM - StockOpname - In Use | 24 | shared_office365, shared_sharepointonline |

## Target V2 operation interfaces

[Flow/operation contracts](../Others/architecture/FLOW-OPERATION-CONTRACTS.md) and [request/output resources](../Others/architecture/interfaces/README.md) define proposed logical operations, input/output responsibilities, result handling and connector dependencies. They are architecture documents, not new deployed flows or import packages. Logical operation count does not prescribe physical flow count. Existing per-flow baseline sources above remain intact; feature deliveries will provide concrete affected flow resources and manual guidance.

The first [reference-foundation-002 slice](../Others/releases/reference-foundation-002/RELEASE.md) uses direct read-only SharePoint reference queries and supplies no additional flow. Operational/maintenance writers will have their own concrete per-flow resources; no placeholder flow folder is created for this slice.
