# Lifecycle Asset Management: working understanding

The supplied handover describes a SharePoint-backed Canvas App for individually tracked assets and quantity-based inventory. Power Automate handles spreadsheet ingestion, matching, stock-taking requests/responses/approvals, exports and Power BI refresh. This is an offline source snapshot plus an approved redesign direction; it is not a connected or deployable environment by itself.

## What the current system does

- **Access and navigation:** starts at `1_LandingPage`; resolves the signed-in user's email against Master_Employee and then the MyID against Acces_Matrix. Menus and operations use formula-level access checks. This does not demonstrate SharePoint data-layer isolation.
- **Asset lifecycle:** register assets in Master_Asset, move/update ownership and location, retain Asset_Movement_History and AuditLog, and dispose into the separate inactive register before removing the active record.
- **Quantity inventory:** Master_Inventories and Inventories_Movement_History form a separate registration/transfer branch. Actual YAML contains history writes, despite the handover's statement that writers were absent.
- **Stock opname:** physical stock verification is split into Available and In Use workflows. Requests hold serialized asset and approver payloads; flows handle notifications, response updates, approvals and confirmations.
- **Accounting reconciliation:** uploads ledger spreadsheets and compares them against the asset register, preserving temporary results and routing approvals. The dedicated screen references V3; both stock-opname screens still contain V2 calls. A formula reference does not prove that a control is reachable or its flow enabled.
- **Reporting:** the dashboard has an explicit `DataRefreshALM.Run()` button handler (ALM-Dashboard.pa.yaml:96); its flow invokes Power BI dataset refresh. This resolves the contradictory document claim that no screen calls it.

## Approved V2 direction

The hierarchy is **Organization → Function → assets**. Every function belongs to one organization. The later redesign-plan refines earlier entity-only guidance: a session selects an entity and then one of its functions, stored in `gblEntity` and `gblFunction`. Operational reads and submissions must respect both IDs. Roles have one row per `(email, entity, function)`, and users may belong to several functions.

Historical full-export counts are 2,179 assets and 26 asset types, all under ORG-01 / IT FNC-01. CRESS FNC-02 also belongs to ORG-01 and intentionally starts empty. The archive contains only anonymized subsets: 96 rows across 18 CSVs. These are different measures and must not be conflated.

The redesign aims to consolidate task-based screens, remove hardcoded IDs and repeated logic, canonicalize statuses, parameterize workflows and follow Zurich branding/accessibility requirements. The current source is a reference for business rules, not proof that V2 scoping or its new Roles model is implemented.

## Verified coverage and integrity

All **87 archive files** were inventoried: 30 Canvas YAML files, 15 flow JSON definitions, one Python validator, 23 documentation/schema files and 18 CSV samples. All documents were read completely; all YAML and flow JSON parsed completely; CSV headers exactly matched their schema files. The supplied validator passed 30 files and 2,354 controls. A graph diagnostic checks endpoints, self-loops and consolidated endpoint pairs.

`graph.html` is the interactive map; `graph.json` holds evidence and confidence; `GRAPH_REPORT.md` lists communities and hubs. Detail is retained in `implementation-inventory.json`, `implementation-notes.md`, `data-model-notes.md` and `handover-docs-notes.md`.

## Scope decisions and remaining questions

1. **Disposal scope — confirmed 2026-10-27:** retain direct asset disposal; retire only the separate disposal-request/approval process. This resolves the contradictory handover wording. See `Others/decisions/DECISIONS.md`, decision D001. The implementation snapshot has not been changed.
2. **Authorization architecture:** the required IT/CRESS isolation is clear, but its enforcement below Canvas UI filters is unspecified. This is a design decision, not evidence of an existing backend control.
3. **Provisioning contracts:** SharePoint schema types are blank; internal names, indexes, required fields, choices and lookup rules remain unspecified. Entity versus Organization_ID terminology needs a single physical contract.
4. **Bindings and import:** no original msapp, connector/API binding maps or import-ready flow solution zip is supplied. GUID-addressed SharePoint tables cannot be reliably joined to named list schemas from this package alone.
5. **Legacy variants:** Master_Asset2 duplicates the supplied Master_Asset schema/sample. Networking Device is a placeholder flow. A response helper returns a static Testing array. Do not assume these are live production features.
6. **Behavior to verify later:** movement's immediate LastSubmit usage may race asynchronous SubmitForm; sequential disposal writes are not atomic; registration audits Remarks while the shown creation Patch omits it. These are static observations, not reproduced runtime failures.

No application or flow source was modified, no flow was executed, and no live production behavior was tested. Token usage of delegated semantic analysis was unavailable; placeholder zero counters are not actual zero usage.


This analysis was produced against the original handover paths; resolve `app/src/` to the Power Apps app screens folder, `flows/` to Power Automate and `data/schema/` to Others/sharepoint/schema in this repository.
