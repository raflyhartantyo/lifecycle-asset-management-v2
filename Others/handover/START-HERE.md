# Company Claude: start here

Release `baseline-001` packages the supplied reference implementation. Start by reading the root README, `../decisions/DECISIONS.md` and `../releases/baseline-001/RELEASE.md`.

For an app task, read the selected app's IMPLEMENTATION.md, SCREEN-INDEX.md and the current screen's guide. For a flow task, read that flow's IMPLEMENTATION.md, TRIGGER-CONTRACT.json, CONFIGURATION.json and ACTION-MAP.md. Load other files only when the selected task depends on them.

## Work sequence

1. Identify the exact repository commit/release, target development environment, selected app/flow and requested operation.
2. Compare target state and source before changes; record existing versions/bindings for rollback. List missing environment metadata with exact affected files/actions.
3. Implement the selected unit following its guide. Preserve input/output contracts, names and approval/data behavior unless the release explicitly changes them. Follow the company operator's authorization and available tools.
4. Run its validation steps. A file supplied, a formula pasted and a successful runtime test are distinct outcomes; record each accurately.
5. Return IMPLEMENTATION-RESULT-TEMPLATE.md with precise errors/evidence. When implementation diverges from delivered behavior, send the discrepancy back to the main developer for a replacement delivery.

Complete when the selected unit's checks are reported as PASS/FAIL/NOT RUN with evidence, remaining dependencies and rollback status. A blocked unit may be reported while independent units continue. Keep credentials and live company records in approved company systems.
