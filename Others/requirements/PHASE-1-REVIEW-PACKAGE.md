# Phase 1 — consolidated review package

Status: twelve planned interview rounds complete; decisions D001–D041 recorded. Ready for owner review. This is not a runtime-tested app, deployment package, environment authorization grant or claim that every architecture dependency is resolved.

## Product and release scope

A total Zurich-branded LAM redesign for individually tracked assets, quantity inventory, stock verification, accounting reconciliation, reporting and audits. First production replacement covers all retained capabilities, built/tested incrementally and piloted in ORG-01/IT before further onboarding. Direct disposal remains; separate disposal-request/approval is retired.

## Confirmed operating model

- Ordinary roles use explicit organization/function grants; Global User maintains one entity across functions; Super User maintains all entities/functions and grants privileged roles.
- Asset Operator registers/moves assets. Asset Manager additionally runs stock/reconciliation/disposal. Inventory Operator handles quantities/transfers. Business Owner owns asset accountability and relevant reporting/reminders/assigned sign-off. Respondent is task participation with assigned historical read/export access.
- Viewers/respondents export assigned data; other exports follow module/ownership/entity/application scope. Only open assigned responses are editable; audited reopening/reassignment preserves history.
- Asset entity/function/Business Owner changes require both owner capacities to approve. One explicit decision can cover both capacities for the same person; rejection leaves assets unchanged. BAU transactions need no remarks/reason; automatic history remains.
- Quantity inventory transfers deliberately omit dual Business Owner approval while retaining authorization, quantity and movement history controls.
- Bulk imports preview rows and create confirmed valid new assets only; report invalid/duplicate rows without overwriting existing records. Disposal supports sale/non-sale outcomes with date and applicable sale fields.
- Stock verification derives scope from the permission source/session, filters Available/In Use and uses configurable default due dates. Respondents supply evidence, managers review discrepancies and owners sign off. Acknowledged unresolved exceptions stay visibly unverified after closure.
- Reconciliation previews ledger comparisons/provenance, routes Accounting/Governance sign-off and requires explicit authorized Asset Manager application of corrections. Existing action/transfer rules still apply.
- Desktop/laptop primary, responsive tablet and mobile-friendly responses/approvals/progress; Zurich branding and accessibility govern design.
- The project owner performs human UAT alone. Main developer supplies cases, setup and fixes; company Claude assists implementation/setup. No separate business-representative testers are assumed.

## Review documents

- [Decision register](../decisions/DECISIONS.md): authority for confirmed choices.
- [Requirements detail](PHASE-1-REQUIREMENTS.md) and [business process maps](BUSINESS-PROCESSES.md).
- [Permission matrix](PERMISSION-MATRIX.md) and [role working draft](ROLE-PERMISSIONS-DRAFT.md).
- [Acceptance criteria](ACCEPTANCE-CRITERIA.md) and [individual testing kit](../testing/README.md).
- [Prioritized backlog](IMPLEMENTATION-BACKLOG.md) and [assumptions/dependencies](ASSUMPTIONS-AND-DEPENDENCIES.md).

## What review establishes

Review confirms the captured business requirements and any corrections. Required unknown company facts remain tracked; numerical performance, exact schemas/approval routing/field visibility and promotion ownership are not invented. Begin Phase 2 architecture/data/authorization design using the confirmed decisions and resolve evidence-dependent choices through the company inventory. New consequential business conflicts get targeted follow-up; routine field-by-field interview rounds are complete.

## Next practical action

Prepare the individual UAT setup and return the read-only company inventory. The next development deliverable is architecture/data/authorization design and a foundation implementation plan, not an immediate production redesign deployment.
