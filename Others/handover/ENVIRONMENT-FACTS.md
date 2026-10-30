# V2 environment facts

Source: project owner's chat observations, 2026-10-27, with hosting update 2026-10-30 (D073). Other observations retain their original date unless updated. These are user-reported facts, not independent tenant inspection. Supersedes the assumption that the old implementation is deployed as V2; original baseline files remain reference only.

| Item | Current observation |
| --- | --- |
| Target environment | ENV-A |
| Other visible environment | ENV-B; purpose unknown |
| App | Lifecycle Asset Management V2 |
| App state | Blank; Screen1 only; no data sources |
| User can edit app | Yes |
| Used for daily operations | No; new build from scratch |
| Separate dev/test environment | No |
| SharePoint target | SITE-F: existing Function site will host dedicated LAM resources; SITE-A dedicated-site plan is unavailable (2026-10-30) |
| V2 lists | Last reported not created; current creation/migration state not supplied. Dedicated LAM2_ resources are planned inside SITE-F |
| Site permission | SITE-F rights not supplied. Earlier Member/list-creation/permission-management observations applied to the previous site plan and are not proof of SITE-F rights |
| Site readiness | Existing host selected; actual LAM list/library setup and connection bindings not reported |
| Permanent asset count | Owner clarified: up to 2,500 per entity; approximately 5,000 overall |
| Inventory types | Approximately 15; total stock quantity not supplied |
| Users | Approximately 10 initially, scalable to 30 |
| Concurrent users | Approximately 3–5 |
| Entities | 3 |
| Functions | Approximately 2–3 per entity (6–9 total) |

## Outstanding facts

Actual SITE-F list/library permissions and bindings, Power Automate access/connections, approved connector/licensing limits, backend authorization implementation, identity availability, production promotion/rollback arrangement, approved brand media and Power BI configuration remain unconfirmed. ENV-B is not assumed to be a test environment. Low record counts do not establish security or runtime acceptance.

The owner implements and tests. Claude provides Q&A from supplied evidence; Codex prepares design/resources/tests. No runtime checks or company changes were made to produce this record.

Current setup guidance: [shared Function site](../sharepoint/v2/SHARED-FUNCTION-SITE-SETUP.md). Existing host content/site membership is preserved; LAM Entity/Function scope remains independent of the hosting Function. D072 keeps company setup with the owner during implementation, without a general observation-report prerequisite.
