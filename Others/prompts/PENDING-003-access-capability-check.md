# 003 — Read-only access implementation capability check

Status: **DEFERRED** — D072: optional reference only. No report is required to continue architecture; the owner handles access/connector setup at the relevant implementation stage. The historical filename is retained to preserve links.

Use when: the owner is ready to collect company capability observations. SITE-A need not be finished; unavailable items remain UNKNOWN. This is a read-only check, not permission to create lists, prototype flows, change sharing or provision services.

## Prompt to copy

You are a Q&A assistant with no direct visibility into Power Platform, SharePoint, Power BI, company identities or company configuration. The user performs every check. Use only the supplied files, screenshots and observations; GitHub access is not assumed. When a referenced file is unavailable, ask the user to paste the relevant section. Mark facts UNKNOWN until evidence is supplied; distinguish user-reported observations from runtime proof.

Help me gather the facts needed to choose LAM V2's backend access mechanism. Codex supplies designs/resources/tests; I implement and test. Do not present app filters, hidden buttons, an app-passed email or an elevated connection as proof of authorization.

References, when supplied:

- `Others/architecture/ACCESS-AND-AUTHORIZATION-CONTRACT.md`
- `Others/architecture/BACKEND-ACCESS-FEASIBILITY.md`
- `Others/sharepoint/v2/ACCESS-GRANT-COLUMNS-DRAFT.csv` — draft; do not create these lists
- `Others/handover/ENVIRONMENT-FACTS.md`

Known observations: ENV-A contains the new blank Lifecycle Asset Management V2 app, Screen1 only and no connected data. ENV-B exists but its purpose is unknown. SITE-A is a dedicated site being created; no V2 lists are confirmed created. I reported Member access, New → List and permission-management availability. No separate test environment is confirmed. These are observations, not independently verified capabilities.

Guide me in small batches of numbered read-only steps. For each step give the screen/location, expected evidence and what to record if unavailable. Do not ask for credentials, tokens, actual tenant IDs, named employee records or confidential asset data. Use aliases such as SERVICE-A and TEST-USER-A.

Collect the following without making changes:

1. SITE-A readiness and visible site/list permission inheritance or broad Members/Visitors access, if a completed site and relevant existing nonconfidential list can be inspected. Record the alias-level membership/permission pattern; do not change it. If SITE-A is unfinished, leave this UNKNOWN and continue independent checks.
2. Whether I can open Power Automate in ENV-A and inspect an already-authorized instant flow's sharing/Run only users and connection-source options without changing them. Record observed labels/settings using connection aliases. Do not create or run a flow, share it, save changes or trigger an approval.
3. Whether company administrators have already confirmed an approved flow/service connection identity, who maintains it, whether end users may be prevented from broad direct master-list access, and which connectors/connection-sharing patterns are permitted. Existing written confirmation can be summarized; otherwise mark UNKNOWN. Do not claim approval from the presence of a connector button. Do not send administrator messages on my behalf.
4. Whether a documented, company-approved mechanism exists to prove the authenticated caller in the chosen read/write path. Do not prescribe an undocumented trigger header or rely on an app-submitted email/object ID. A service connection's own profile is not the invoking user's identity. Record the mechanism/source if already confirmed, or UNKNOWN; do not build a workaround during this check.
5. Whether approved separate synthetic test identities and a genuinely isolated scratch setup are available. Record aliases and access only; ENV-B's existence is not proof of readiness. Do not add users or fixtures.
6. Any already-confirmed connector/licensing/data-policy limitations affecting the candidate mechanisms. Record the company source/date or UNKNOWN; do not infer entitlement or spend money from visible UI options.

The design proposes controlled authenticated reads/writes over protected SharePoint as a candidate; it is not an approved or implemented architecture. Native SharePoint permissions are an alternative requiring complete row/field/history/transfer and scope-growth validation. Never recommend broad site/list Edit or Read plus app filtering as compliance with the accepted access contract. Do not assume an application Super User is a SharePoint/tenant administrator or an assigned workflow approver.

If a step needs company authority I do not have, stop that step and record the missing capability while continuing independent read-only steps. Return findings, unknowns and the specific decision each affects; do not mark the backend design ready from observations alone.

If explaining the flow, include this conceptual visual or an equivalent Mermaid flowchart:

```mermaid
flowchart LR
    A[Authenticated caller] --> B[Trusted identity and current access evaluation]
    B --> C[Authorized row and field subset]
    C --> D[Validated read or controlled mutation]
    D --> E[Attributable result and evidence]
```

Return one Markdown report with: source repository commit if known; observation table with Evidence/UNKNOWN for each item; checks not performed; candidate mechanism and remaining proof; blockers; and confirmation that no configuration changed. Do not label observation-only items as runtime PASS. All security/runtime cases remain NOT RUN unless separately executed under an authorized test plan.

Return the completed report as one Markdown document I can paste into `Others/prompts/responses/003-access-capability-response.md` on GitHub. Include supporting evidence, missing/unknown items and blockers. Use aliases and omit credentials, secrets and confidential business records. Provide the exact destination path and Markdown text for me to paste; do not assume repository access. I will send Codex the resulting GitHub file link for review.

## Tracking

Keep DEFERRED under D072; no report is requested to advance the design. Retain as optional reference if the owner later wants it. This prompt does not authorize an implementation or permission change. No company checks have been performed by its publication.
