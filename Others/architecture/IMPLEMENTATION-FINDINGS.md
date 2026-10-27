# Implemented behavior in the handover snapshot

All 30 `.pa.yaml` files were parsed through their last scalar using PyYAML's composition API (the Power Fx bare `=` scalar has a YAML `value` tag, so ordinary safe_load is unsuitable). All 15 flow definitions were parsed as complete JSON trees. The reusable `map_power_platform.py` reads these sources without executing formulas, calling connectors, or changing app files. `implementation-inventory.json` indexes relevant formulas and all 403 nested actions, with physical YAML lines and flow JSON pointers. The graph fragment includes coverage counts for all 45 source files.

## App and access

`app/src/App.pa.yaml:L11` starts at `1_LandingPage`. Its Start button looks up the signed-in email in `Master_Employee`, uses the employee MyID against `Acces_Matrix.Title`, and branches by Asset_Management / Inventories_Management into the asset home page, inventory page, or combined selector (`1_LandingPage.pa.yaml:L61–89`). More menu permissions are formula-driven. These are observed UI gates; this export does not establish list-level authorization or deployment access.

Registration (`ALM-Registration.pa.yaml:L1353`) checks mandatory asset code/name/type/price/date, requires serial numbers for ATP-012/ATP-013, and looks for existing accounting codes. It creates Master_Asset rows and AuditLog rows with correlation IDs and per-field old/new changes. Bulk upload calls Bulk_Registration to parse spreadsheet rows. The formula audits a Remarks value but the shown new-asset Patch omits Remarks: field intent and actual persistence differ.

Movement (`ALM - Movement.pa.yaml:L1966`) calls SubmitForm, immediately tests LastSubmit, builds changed-field audit text, writes AuditLog, and copies the original buffer into Asset_Movement_History. This sequencing may rely on a stale LastSubmit because SubmitForm completes asynchronously; this is a static concern, not a runtime-confirmed failure. History preserves the pre-edit buffer while current state comes from form submission.

Disposal (`ALM - Dispose.pa.yaml:L1253` onward) archives selected assets to the app data source `'Inactive Assets'`, creates a Dispose audit entry and movement-history snapshot for the active asset, then removes it from Master_Asset. Multi-list writes are sequential rather than an atomic transaction. The distinct disposal-request screen (`ALM-DisposeRequest.pa.yaml:L2385`) creates a `'Disposal Request'` row with a GUID, serialized approvers/assets, pending count/status. No matching schema file for that named list appears among the 18 supplied schemas; its complete approval implementation cannot be asserted from this package.

Inventories are a parallel quantity-based branch. `Registration_Inventories.pa.yaml:L857` writes Master_Inventories, Inventories_Movement_History, and AuditLog. `Inventaris_Transfer.pa.yaml:L915–947` writes transfer history, creates child inventory entries, returns quantities to scope/stock, and updates current inventory. Asset and inventory histories are distinct.

## Reconciliation and stock opname

The dedicated `ALM-AccReconcile` screen calls Accounting_ReconsiliationV3; the two stock-opname screens still contain Accounting_ReconsiliationV2 calls. Both versions are present and app-referenced in the snapshot, so treating V3 as the sole active reconciliation flow would be wrong. Their actions create uploaded Excel files, retrieve rows, compare with SharePoint records, and persist temporary results. Accounting Reconciliation - Approval Request contains create/wait approval operations, attachments, updates and email operations. Actual environment activation and successful execution are not verified by a file export.

Available stock opname uses Temp_Stock_Opname, SO_Respondent_Save and SO_Respondents_Confirm. The save flow joins updated responses to existing Available_Assets by Accounting_Asset_Code, preserves unchanged entries, patches the stored array, then posts a Teams message. The confirm flow contains approval creation/wait, attachments, status updates and email operations. The start flow reads available assets, creates a request, and sends notification email.

In-use stock opname additionally uses Stock_Opname_InUse and Stock_Opname_In_Use_Match. Match ingests spreadsheet data, builds intermediate files/results and updates records. The notification flow groups receiver/PIC responsibilities, excludes Response_Type = Automated, sends tutorial attachments and updates status to Waiting for User Approval. Its email embeds a 2026 campaign timeline; this is literal message content, not a scheduling trigger.

All **15/15 flows have a manual Request/PowerAppV2 trigger**. There are no recurrence triggers in the supplied definitions. Names such as Trigger and dates in email bodies do not establish automation schedules.

`Flow Networking Device` has only Initialize_variable (Temp = true). It is a placeholder in this export; no networking reconciliation logic is implemented there. `PowerAppV2 -_ Respond to a Power App or flow` initializes a fixed Testing array and returns it, suggesting a demonstration/test helper rather than live reconciliation. InTune Flow has Excel/file/read/update actions. Export Data writes a file and creates a sharing link; Data Refresh ALM calls the Power BI RefreshDataset operation.

## Evidence and limits

Screen→flow bindings using display names with punctuation/spacing differences are represented by explicit app reference nodes plus INFERRED 0.95 alias bridges, because connection-binding metadata is absent. `Inactive Assets`→Inactive_Assets and `Employee Master`→Master_Employee are inferred display-name aliases. Every screen/data reference, navigation, trigger, action, connector use and runAfter dependency carries a concrete source location. Multiple relationships between the same endpoint pair retain an evidence list to avoid silent edge collapse.

Flow SharePoint tables are GUID references without an authoritative list-name binding export. They are kept distinct from named schema nodes; guessed GUID-to-list joins are not asserted as facts. Excel tables are distinguished from SharePoint lists. The parser recognizes direct named Power Fx references and direct .Run calls; it does not prove delegation completeness, runtime permissions, dynamic data-source resolution, or service health. Formula matching strips comments and double-quoted string literals but remains lexical, rather than a full Power Fx parser. Graph calls represent formula dependencies, not proof a runtime branch was taken.

Generated inventories exclude raw authentication material, recipient addresses, email bodies, connection IDs and sample personal records. Token fields are zero because this deterministic pass consumes no external LLM API; host-agent analysis token counts are unavailable and zero is not a claim about total session usage.


This analysis was produced against the original handover paths; resolve `app/src/` to the Power Apps app screens folder, `flows/` to Power Automate and `data/schema/` to Others/sharepoint/schema in this repository.
