# V2 environment facts

Source: project owner's chat observations, 2026-10-27. These are user-reported facts, not independent tenant inspection. Supersedes the assumption that the old implementation is deployed as V2; original baseline files remain reference only.

| Item | Current observation |
| --- | --- |
| Target environment | ENV-A |
| Other visible environment | ENV-B; purpose unknown |
| App | Lifecycle Asset Management V2 |
| App state | Blank; Screen1 only; no data sources |
| User can edit app | Yes |
| Used for daily operations | No; new build from scratch |
| Separate dev/test environment | No |
| SharePoint target | SITE-A, dedicated LAM site being created |
| V2 lists | Not created; will be dedicated to V2 |
| Site permission | Member; user reports New → List and ability to manage list permissions |
| Site readiness | In progress; capabilities must be confirmed on the completed target site |
| Permanent asset count | Owner clarified: up to 2,500 per entity; approximately 5,000 overall |
| Inventory types | Approximately 15; total stock quantity not supplied |
| Users | Approximately 10 initially, scalable to 30 |
| Concurrent users | Approximately 3–5 |
| Entities | 3 |
| Functions | Approximately 2–3 per entity (6–9 total) |

## Outstanding facts

Actual site readiness/permissions, Power Automate access/connections, approved connector/licensing limits, backend authorization implementation, identity availability, production promotion/rollback arrangement, approved brand media and Power BI configuration remain unconfirmed. ENV-B is not assumed to be a test environment. Low record counts do not establish security or runtime acceptance.

The owner implements and tests. Claude provides Q&A from supplied evidence; Codex prepares design/resources/tests. No runtime checks or company changes were made to produce this record.
