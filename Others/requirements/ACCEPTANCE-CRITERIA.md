# Acceptance criteria — consolidated review draft

Status: confirmed business acceptance requirements translated into scenarios; company runtime evidence and certain technical facts remain pending. These are acceptance targets, not completed tests or a deployment claim. Company UAT evidence is still required.

## Traceable functional and authorization checks

| ID | Scenario / pass evidence | Source |
|---|---|---|
| AC-01 | All retained capabilities pass representative end-to-end tests; separate disposal-request/approval is absent from target UI/processes. | D001/D005 |
| AC-02 | Ordinary users access only authorized pairs; Global User stays within its entity; Super User operates across authorized application administration. Test backend calls as well as UI. | D002/D007/D013 |
| AC-03 | Only Super User grants/revokes Global User/Super User; Global User administers ordinary roles within its entity. | D017 |
| AC-04 | Respondents read/export assigned current/historical data and edit only their open responses; unrelated records remain inaccessible. | D010/D012/D019 |
| AC-05 | Every export obeys the role's row/field scope; Viewer exports assigned data without business-data edit rights. | D018/D019 |
| AC-06 | Business Owner sees relevant request progress even when another person initiates it; Business Owner/Asset Manager can send standard relevant reminders without altering responses/status. | D014/D016/D020 |
| AC-07 | Reopening/reassignment requires authorized scope, reasons and audit; preserve previous answers and former-assignee historical visibility. | D021/D022 |
| AC-08 | Routine archive/retire/cancel/disposal retains history. Historical/audit permanent deletion is separately controlled under company retention requirements. | D023 |
| AC-09 | Bulk validation previews every row; import attempts only confirmed valid new rows, reports invalid/duplicate rows and never silently overwrites existing assets. | D024/D030 |
| AC-10 | Asset scope/Business Owner changes wait for both required capacities to approve; same person gives one explicit decision recorded in both capacities; rejection leaves the asset unchanged. | D025/D027–D029 |
| AC-11 | BAU asset transactions save without mandatory remarks/reason and retain automatic actor/time/old-new history. | D026 |
| AC-12 | Sale/non-sale disposal records its date and applicable sale details, without fake buyer/price requirements for non-sale retirement. | D031 |
| AC-13 | Inventory transfers retain scope/quantity/history checks without creating asset-style dual Business Owner approval tasks. | D018/D032 |
| AC-14 | Stock scope derives from access/session, Available/In Use filters assets, and configured default due date is used. Respondent discrepancies become evidence for review. | D033/D034 |
| AC-15 | Business Owners sign off stock results; acknowledged exceptions can remain after closure, but missing/unresolved assets are never counted verified. | D035 |
| AC-16 | Reconciliation comparison preserves provenance and does not mutate the register. Configured Accounting/Governance sign-off precedes explicit authorized Asset Manager correction application. Preserve applicable action/transfer rules and correction outcomes. | D036–D038 |

## Brand and accessibility requirements from baseline

Use the supplied Zurich guidelines as the design acceptance reference: palette/type/logo/icons/components, visible focus, keyboard operation, labels, required contrast, 200% zoom and reduced motion. Verify primary workflows in the supported company environment; valid YAML alone is insufficient. Document missing approved brand assets as dependencies.

## Confirmed device, release and testing requirements

D039 confirms desktop/laptop primary, responsive tablet and mobile-friendly assigned responses/approvals/progress. D040 confirms retained-workflow UAT, authorization/history/export and Zurich/accessibility checks, no unresolved critical/high defects, and developer-provided concrete test cases. D041 assigns human UAT execution to the project owner alone. Separate business-representative testers are not required by this plan.

Use ../testing/README.md, TEST-CASES.csv, SOLO-UAT-RUNBOOK.md and result templates. Multiple personas are exercised sequentially by the same operator using company-approved identities/access. Cases needing a missing identity/environment capability remain BLOCKED, not passed by simulation. Fixed launch date and post-launch support ownership remain unspecified.

## Performance and operational evidence

Capture representative company data volumes, devices, network conditions, concurrency and normal/long-running operation timings using COMPANY-ENVIRONMENT-INVENTORY.md. Propose numerical performance targets with explicit measurement conditions during architecture review; no unmeasured latency/SLA claim or invented committed threshold is made here. Long-running work needs honest status/progress and recovery; draft UX behavior follows the supplied brand guidelines.

## Required test result format

For each criterion: selected release/commit, target environment/version, test role/scope, anonymized input fixture, expected/actual result, PASS/FAIL/NOT RUN, evidence/run ID, defect severity, and cleanup/rollback outcome. Use the company handover result template. Unknown company dependencies stay explicit and cannot be marked passed by assumption.
