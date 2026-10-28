# Delivery and implementation order

Use the [implementation blueprint](../architecture/IMPLEMENTATION-BLUEPRINT.md), [logical screen map](../architecture/SCREEN-IMPLEMENTATION-MAP.md) and [slice/evidence gates](../architecture/BUILD-SEQUENCE-AND-GATES.md) for the concrete target breakdown. Accepted working UX extends through D071; operational data and backend contracts remain prerequisites.

1. **baseline-001 (this delivery):** archive/source fidelity, company-side comparison, dependency inventory and per-unit review. No redesigned feature is implemented by this release.
2. **Data/authorization design:** finalize list/internal-column contracts, Organization→Function hierarchy, role tuples and backend isolation. Resolve remaining owner decisions before committing affected implementations.
3. **Application foundation:** Zurich design system, reusable components, identity, once-per-session entity/function selection and shared data/error conventions.
4. **Master data and asset register:** implement scoped reference lists, employee/classification relationships, asset browsing and registration; validate two functions.
5. **Asset and quantity transactions:** movement, direct disposal, inventory registration/transfer and consistent audit/history. Exclude separate disposal-request/approval.
6. **Flows and app integration:** deliver entity/function-aware import/reconciliation/stock-taking/export contracts in coordination with their callers. Retain the deferred-formula monthly Book Value calculation (D046/BL-14), with its own specification/tests before activation. Reconciliation explicitly applies eligible corrections before final Accounting/Governance sign-offs on actual results (D070). Keep both current reconciliation variants as reference until their replacements pass validation. Shared approval flows require branch-level review.
7. **Reporting and end-to-end acceptance:** build D071 scoped progress/detail, exports and eligible standard respondent reminders, connections/refresh and complete positive/negative scenarios, rollback and company-side export packages. Scope checks, durable audit/recovery and basic progress accompany each producing slice; this final stage completes integration rather than postponing these controls.

Future features will ship complete affected files, per-app/per-flow guides, exact changes, dependencies and validation/rollback. Each release identifies the company commit being replaced and the operator's required feedback. Rebuild the knowledge map after structural changes; the original graph is historical baseline analysis.
