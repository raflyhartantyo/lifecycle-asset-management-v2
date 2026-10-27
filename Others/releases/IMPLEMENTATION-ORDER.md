# Delivery and implementation order

1. **baseline-001 (this delivery):** archive/source fidelity, company-side comparison, dependency inventory and per-unit review. No redesigned feature is implemented by this release.
2. **Data/authorization design:** finalize list/internal-column contracts, Organization→Function hierarchy, role tuples and backend isolation. Resolve remaining owner decisions before committing affected implementations.
3. **Application foundation:** Zurich design system, reusable components, identity, once-per-session entity/function selection and shared data/error conventions.
4. **Master data and asset register:** implement scoped reference lists, employee/classification relationships, asset browsing and registration; validate two functions.
5. **Asset and quantity transactions:** movement, direct disposal, inventory registration/transfer and consistent audit/history. Exclude separate disposal-request/approval.
6. **Flows and app integration:** deliver entity/function-aware import/reconciliation/stock-taking/export contracts in coordination with their callers. Keep both current reconciliation variants as reference until their replacements pass validation. Shared approval flows require branch-level review.
7. **Reporting and end-to-end acceptance:** connections, refresh, role/tuple isolation, complete positive/negative scenarios, rollback and company-side export packages.

Future features will ship complete affected files, per-app/per-flow guides, exact changes, dependencies and validation/rollback. Each release identifies the company commit being replaced and the operator's required feedback. Rebuild the knowledge map after structural changes; the original graph is historical baseline analysis.
