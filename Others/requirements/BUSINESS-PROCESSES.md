# Business process requirements — working draft

Status: asset lifecycle discovery, owner proposals pending. Confirmed role/scope requirements are in PERMISSION-MATRIX.md and ../decisions/DECISIONS.md. No new app/flow behavior is implemented by this document.

## Process coverage

1. Individually tracked asset registration (single and spreadsheet input), movement and direct disposal.
2. Quantity inventory registration and transfer.
3. Available/in-use stock verification, response, confirmation and relevant approvals.
4. Accounting reconciliation, discrepancy handling and relevant approvals.
5. Reporting, export, reminders and progress monitoring.

Separate disposal request/approval remains retired. Reopening/reassignment/history rules already confirmed are reused by relevant processes; their workflow-specific consequences still require design.

## Asset lifecycle: evidence already available

- Master_Asset supplies Asset_ID, organization/function, Accounting_Asset_Code, asset/business owner references, condition/status, location/type/category, dates, values and serial/device attributes.
- Asset_Movement_History references Asset_ID and stores movement-related state; audit records are separate. These are schema names, not proof of uniqueness, field types or complete historical integrity.
- Current implementation contains individual registration, a bulk parsing flow, movement form handling and direct disposal archive/audit/history/active-record removal. Static findings are documented in ../architecture/IMPLEMENTATION-FINDINGS.md.
- Preserve traceability of existing asset identities across migration and subsequent changes. Validate current identity quality rather than silently rewriting historical references. Whether accounting codes or serials may be duplicated is a business/data-contract question; neither is assumed to be the system key.

## Round 7 proposals — awaiting owner response

| ID | Decision | Proposed behavior | Details deferred until the decision is settled |
|---|---|---|---|
| P7-01 | Bulk-registration error handling | Validate all rows first, show row-level errors and allow the operator to confirm importing only valid rows; invalid rows remain unimported with a downloadable error report | Mandatory fields, duplicate rules, import identifiers, retry/concurrency behavior and partial-write recovery |
| P7-02 | Transfers across functions/entities | Support explicit transfers with source/destination authorization, traceable scope changes and retained asset history | Whether transfer is immediate or requires acceptance/approval; accounting-code/ownership consequences; history/report visibility after transfer |
| P7-03 | Movement reason | Ownership, location and status changes require a recorded reason, retained with actor/time and old/new values | Reason categories, mandatory-field changes by asset type, correction versus movement distinction |

## Asset registration acceptance criteria still to define

Required fields by asset type, accounting-code uniqueness scope, serial-number applicability, initial statuses, owner/location defaults, record validation, duplicate handling and bulk confirmation/error behavior. Existing YAML provides evidence for review but does not automatically approve every current rule as the V2 requirement.

## Remaining process work

Resolve selected asset proposals, then define direct-disposal fields and confirmation, quantity inventory transfer rules, stock-verification participants/statuses/deadlines, reconciliation matching/discrepancies/approvals and reporting scope. Keep company-side facts separate from owner business decisions. Define retention and operational acceptance targets from company requirements rather than assumptions.
