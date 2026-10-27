# Scale and query requirements for operational V2 design

Owner clarification, 2026-10-27: up to 2,500 assets in one entity, approximately 5,000 overall across three entities. The earlier 100-asset planning interpretation is superseded. Approximately 15 inventory item types, 10 users growing to 30, and 3–5 simultaneous users remain the estimates. Total inventory stock quantity is unconfirmed.

## Implications

SharePoint remains a candidate backend; this estimate is not by itself a reason to change platforms or proof that the design will perform. A 5,000-item list view threshold concerns query operations, not a maximum storage capacity. Nondelegable Power Apps queries process only an initial record window (500 by default, configurable to at most 2,000); an entity with 2,500 assets already exceeds that window. Indexing and delegation are separate requirements. History, assignments and verification evidence can exceed 5,000 rows even when the register does not.

## Design requirements before operational provisioning

1. Specify stable scalar scope identifiers and indexes on operational lists before loading data. For large-list access paths, plan indexed text/number partition/filter keys; an indexed lookup alone does not avoid SharePoint's list view threshold. The small organization/function reference relationship in foundation 001 can remain a lookup.
2. Define the exact supported Power Fx predicates/sorts and connector delegation behavior for browse, search and filters. Filter at the source by authorized scope. Fetching a full register into a collection and filtering locally is not an acceptable primary browse/search design.
3. Use selective indexed queries for scope and growing workflow/history data; define additional time/run/task partitions where necessary. Confirm actual SharePoint query plans/behavior in company tests; indexes alone are not a guarantee. UI filtering is not an authorization boundary.
4. Specify bounded server queries/pagination for cross-scope administration, reports and exports. Global/Super access must not rely on collecting a truncated whole list. Distinguish full-result export from currently displayed gallery rows. Aggregations/counts require complete-result semantics.
5. Provide Power Automate pagination/continuation and completeness checks where actions return more than a default page. Imports/exports, reconciliation and stock-cycle selection must report expected/processed/failed counts and explicit partial failure rather than silently succeeding with truncated data.
6. Define optimistic concurrency/retry behavior for asset edits and inventory quantity transfers. The 3–5 user estimate does not remove simultaneous-update risks. Durable audit/idempotency/recovery must accompany the first working mutation.
7. Select physical partitioning and backend authorization together. No per-entity list duplication or row-permission implementation is assumed approved by this note. Licensing, service identity/caller authentication, privileged role changes and direct-list bypass are still architecture dependencies.

## Additional company-side acceptance scenarios to deliver with implementation

- Load approved synthetic data reaching 5,000 assets overall and 2,500 in one entity. Verify search/filter/sort/browse can find known records beyond both the first 500 and first 2,000 source rows. A function distribution must not be assumed to divide assets evenly.
- Exercise filters with a deliberately low nondelegation row limit in a development copy to expose local-query dependence. Compare results with independently established expected IDs/counts; a lack of a warning alone is insufficient evidence.
- Verify Global User and Super User scope-wide browse/export/report counts against expected records across multiple pages. Repeat with restrictive identities to prove no scope leakage.
- Exercise history/evidence lists above 5,000 records and a synthetic register growth case above 5,000 total, with indexed views and operational queries. Test duplicate/missing boundary records across page transitions and retries.
- Run stock-cycle population, import validation, reconciliation and export with inputs/results beyond a connector's default page. Verify complete counts and safe partial failure/resume behavior.
- Exercise simultaneous edits and inventory deductions from two sessions, proving no lost update, negative stock or duplicate history.

These are requirements for forthcoming executable/manual test steps, not results. All runtime/performance checks remain NOT RUN. Company infrastructure and response times have not been measured; record timings during tests before agreeing a performance target.

## Sources

- [Microsoft: Power Apps delegation](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview)
- [Microsoft: SharePoint list view threshold](https://support.microsoft.com/en-us/sharepoint/lists/data-and-lists/list-view-threshold-for-large-lists-and-libraries)
- [Microsoft: indexes and lookup-column limitation](https://support.microsoft.com/en-us/sharepoint/data-and-lists/add-an-index-to-a-list-or-library-column)

The platform facts above come from Microsoft documentation. Proposed design requirements and validation scenarios are project engineering choices; capacity acceptance still requires company-side evidence.
