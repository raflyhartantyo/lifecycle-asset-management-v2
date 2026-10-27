# App validation

Local syntax/control-reference validation passed for the original 30 YAML files and 2,354 controls. It does not validate target connector schemas, Power Fx types, delegation, permissions or runtime behavior.

In the company development environment:

1. App Checker has no unresolved controls, data sources, flow bindings, formula or media errors; record warnings separately.
2. Startup resolves the intended signed-in user and expected permitted menus. Exercise each reachable screen and return navigation.
3. Test one asset registration, movement, direct disposal, quantity registration and inventory transfer; verify active/history/audit records and clean up test data.
4. Exercise available/in-use stock request/response paths, dedicated reconciliation and export/refresh using test recipients and data.
5. Inspect the known static concerns in `../../Others/architecture/IMPLEMENTATION-FINDINGS.md`: SubmitForm/LastSubmit sequencing, sequential disposal writes and Remarks audit/persistence.
6. Record whether source formulas/flows are reachable in this copy; static references alone do not prove enabled features.
7. Keep baseline results distinct from future V2 acceptance. V2 acceptance requires per-session entity/function scope, per-tuple roles and backend isolation, and absence of the separate disposal-request process. This release does not implement those changes.

Return the implementation-result template with PASS/FAIL/NOT RUN per scenario, exact control/formula errors, version IDs and rollback outcome.
