# Proposed operation interface resources

Status: design contract version `0.1-design`; no handlers, callable endpoints or Power Automate flows have been created. The catalogue's logical operations are not a physical flow count. No access/connector questionnaire is required.

- [OPERATION-CATALOG.json](OPERATION-CATALOG.json): app operation names, modes, relevant data/connector responsibilities and deferred feature policies; system-only entries are separate.
- [request.schema.json](request.schema.json): JSON Schema for named request envelopes, typed payloads and explicit set/clear field intents.
- [response.schema.json](response.schema.json): common response shape, safe errors and accepted-background reference requirement.
- [EXAMPLES.json](EXAMPLES.json): synthetic request/response examples. Structurally valid examples can still be denied or fail business validation; none has been executed.

Read [flow semantics](../FLOW-OPERATION-CONTRACTS.md) and [app component interfaces](../APP-COMPONENT-CONTRACTS.md) before implementing these shapes. They define identity, authority, draft/preview, idempotency, concurrency and outcome boundaries that JSON Schema cannot prove.

Payloads with field edits use operation-specific field allow-lists and types at the handler. The schema's fieldKey/value shape is not permission to edit arbitrary columns. Query filter/status strings are likewise validated against the operation's supported vocabulary. Page size 1–200 is a proposed protocol bound, not an established runtime capacity or performance target.

Buyer uses a text alias in the wire draft while the final buyer model is deferred. Decimal strings define transport without choosing precision or allowed financial ranges. Lifecycle/review/approval states inside response data are illustrative projections; exact response data schemas and platform action output mapping follow the feature delivery. Mixed-mode disposal and other open batch policies are not settled by accepting a JSON shape.

The common response schema validates the envelope; it intentionally does not prove operation-specific `data` contents. Each feature delivery must provide the concrete authorized response projection/schema, negative domain cases and platform bindings before its handler is considered complete. If a Power Apps flow adapter uses text JSON or action-specific parameters, the adapter must map and validate this contract explicitly; no paste-ready trigger format is assumed.

## Local contract checks

Python 3 and the `jsonschema` package are required for:

```bash
python3 Others/tools/validate_interface_contracts.py
```

Run from the GitHub delivery root. The checker validates catalogue/schema consistency, model references, examples and selected malformed/forged envelope shapes. It does not authenticate users, invoke flows, prove row permissions, execute business handlers or mark UAT cases passed. All company runtime tests remain NOT RUN.
