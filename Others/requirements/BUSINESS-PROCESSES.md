# Business process requirements — working draft

Status: registration/transfer/reason policies partly confirmed; further process decisions remain open. Confirmed role/scope requirements are in PERMISSION-MATRIX.md and ../decisions/DECISIONS.md. No new app/flow behavior is implemented by this document.

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

## Round 7 — confirmed asset process rules

| Decision | Confirmed behavior | Remaining design detail |
|---|---|---|
| D024 — bulk registration | Validate every row, preview results and let the operator confirm importing only valid rows. Keep invalid rows unimported with a downloadable error report. | Required fields, duplicate matching, import identifiers, row outcomes and safe retries after partial failure |
| D025 — cross-function/entity transfers | Both outgoing and receiving Business Owners approve; preserve asset identity/history and validate source/destination authority. Apply the transfer only after both approvals. | Same-person handling, route order, rejection/resubmission, field locking/versioning and accounting consequences |
| D026 — routine transactions | No mandatory remarks/reason for BAU asset transactions; actor/time/old-new values are captured automatically. | Field-specific validation and automated event formats; reasons remain required for reopening/reassignment exceptions |

## Round 8 — proposed transfer policies, not approved

| ID | Decision | Recommendation |
|---|---|---|
| P8-01 | Same person is both Business Owners | One explicit approval may satisfy both capacities; record both source and destination capacities, rather than silently auto-approving. No blanket self-approval ban applies (D009). |
| P8-02 | Either Business Owner rejects | End the transfer request as rejected and leave the asset unchanged. Permit a corrected new request with prior history retained. |
| P8-03 | Change Business Owner without changing entity/function | Require outgoing/receiving Business Owner approval too. Changes to location, asset custodian or status that change none of entity/function/Business Owner remain BAU with ordinary permissions. |

## Requirement-level acceptance examples for confirmed rules

- A spreadsheet containing valid and invalid rows is fully validated before confirmation. Only explicitly confirmed valid rows are attempted; invalid rows appear in an error report and never silently become assets.
- A cross-function/entity transfer is not applied with only one required approval or before both eligible Business Owners approve. Unauthorized requests cannot bypass this through a direct flow call.
- Successful transfer preserves the asset identity and source/destination history. Request approval is not reported as completed asset movement if applying the change fails.
- BAU asset changes save without entering remarks/reason. Automated change history still records actor/time/old-new values. Reopening/reassignment without the required exceptional reason remains rejected.

## Asset registration acceptance criteria still to define

Required fields by asset type, accounting-code uniqueness scope, serial-number applicability, initial statuses, owner/location defaults, record validation, duplicate handling and bulk confirmation/error behavior. Existing YAML provides evidence for review but does not automatically approve every current rule as the V2 requirement.

## Remaining process work

Resolve transfer policy and registration validation details, then define direct-disposal fields and confirmation, quantity inventory transfer rules, stock-verification participants/statuses/deadlines, reconciliation matching/discrepancies/approvals and reporting scope. Keep company-side facts separate from owner business decisions. Define retention and operational acceptance targets from company requirements rather than assumptions.
