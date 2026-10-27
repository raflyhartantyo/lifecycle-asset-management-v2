# Company Claude task — read-only environment inventory

Purpose: supply facts needed for Phase 1 requirements and Phase 2 architecture. Work within the operator's company authorization and tools. This task makes no app/list/flow/configuration changes and executes no business workflows. If your tools cannot inspect a fact, give the operator precise read-only steps and mark it UNKNOWN until evidence is returned.

Read Others/requirements/PHASE-1-REQUIREMENTS.md, Others/requirements/PERMISSION-MATRIX.md and Others/decisions/DECISIONS.md from the selected repository commit. Report the commit and inspection date. Compare with the actual company development/production setup; baseline source is not proof of current deployment.

## Collect facts

1. **Environments and deployment:** available development/test/production environments, environment type, Dataverse provisioned status, current solution membership, permitted deployment/export methods and maker access. Record confirmed license/connector restrictions and whether these require administrator verification; avoid inferring entitlements from visible buttons alone.
2. **App and flows:** current display names, versions/last-modified dates, enabled/disabled status, accessible app checker findings and source/export availability. Record whether both reconciliation variants and the reference helper/placeholder flows are reachable/used. Inspect definitions/run history metadata only; do not trigger execution.
3. **SharePoint metadata:** list display/internal names, column internal/display names, types, required/choice/lookup/index/unique settings and approximate record counts. Resolve Master_Asset2 binding and ordinary data-source display aliases where evidence permits. Use metadata, not raw employee/asset row exports.
4. **Existing authorization:** describe group/role-based access to app, lists, flows and reports; identify whether users can bypass client filtering through direct list access. Report role/group labels or anonymized identifiers, not names, emails or membership lists. New proposed roles have not been implemented.
5. **Scale and usage evidence:** known user/concurrency counts, devices/browsers, asset/inventory counts and retention requirements. Separate measured facts, owner estimates and unknowns.
6. **Brand/media/reporting dependencies:** availability of approved Zurich logo/icon/font assets; missing app media/components; Power BI workspace/report/dataset bindings and permissions. Keep secrets and environment-specific configuration values in company-approved storage; reference them by alias.

## Return format

| Topic | Observed fact / value | Evidence source and date | VERIFIED / ESTIMATE / UNKNOWN | Constraint or follow-up |
|---|---|---|---|---|

Include a missing-dependencies list and differences from baseline. Return metadata and summaries only; omit credentials, tokens, raw personal records and live business payloads. Any fact blocked by access remains UNKNOWN. Complete when all six topics have evidence or explicit unknowns; the main developer will translate the findings into design choices.
