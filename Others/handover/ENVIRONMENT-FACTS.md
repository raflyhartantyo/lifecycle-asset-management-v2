# V2 environment facts

Source: project owner's chat observations, 2026-10-27, with hosting update 2026-10-30 (D073) and response 005 configuration progress reviewed 2026-10-30. Other observations retain their original date unless updated. These are user-reported facts, not independent tenant inspection. Supersedes the assumption that the old implementation is deployed as V2; original baseline files remain reference only.

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
| V2 lists | Response 005 reports all five reference lists created in SITE-F; four reported configured; D074 confirms the omitted AssetTypes.OrganizationRef is correct for shared types. Specific AssetTypes lookup/index/retention settings remain unconfirmed. Categories has three fixed seed rows; other lists reported empty except AssetTypes zero-row state not separately confirmed |
| Site permission | Response 005 reports LAM-list inheritance separated, Owners/IT Asset Management access retained, Members/Visitors removed from those lists only, host-site groups unchanged. Effective custom permission rights and backend isolation not tested |
| Site readiness | Reference-list setup partially complete by report; no app/flow connection changes or operational-list setup reported |
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

Reference configuration progress: [response 005](../prompts/responses/005-shared-site-foundation-response.md) and [review](../prompts/responses/005-shared-site-foundation-review.md). Retention 50 is reported for Organizations/Functions/Buildings; exact Categories/AssetTypes retention remains unrecorded. These are report-based observations; Codex has not inspected company systems or the screenshots referenced by Claude.

D074 owner clarification (2026-10-30): Asset Types shared across entities; Global Users and Super Users maintain the shared catalogue. This resolves the scope discrepancy in response 005, without proving remaining settings or runtime cases.
