# baseline-001 — reference implementation and handover

Prepared 2026-10-27. Status: reference baseline for company-side review; not deployed.

Contains one app (29 screen YAML files plus App object), 15 flow definitions, 18 list schemas, 18 sample CSVs, original handover/brand/redesign documents, confirmed decisions and implementation resources. All 87 files from the original archive plus the later confirmed-decisions document are mapped byte-for-byte in SOURCE-MANIFEST.json.

Validation: JSON parsing, YAML syntax/control checks, file counts, source SHA-256 fidelity, per-flow action coverage, local Markdown links and repository layout. Runtime Power Fx, connections, permissions, flows, media completeness and imports require company-side validation.

No redesigned V2 app or flow is included. Separate disposal-request/approval is retained only as baseline evidence and retired from target scope. Direct disposal and other stock/reconciliation approvals remain.

Missing artifacts: original msapp, connector/API binding maps, reusable component exports/media binaries and genuine Power Automate import packages/solution ZIPs. Plain definitions are not represented as import-ready packages.

Rollback: this release itself changes no company environment. For any company-side reconstruction, keep previous app/flow versions and bindings, use development data, and follow the unit-level rollback instructions.
