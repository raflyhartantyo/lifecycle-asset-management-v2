# Export Data — implementation

Release: `baseline-001`. Status: reference source; no redesigned flow is delivered here.

## Flow-specific scope

Reference baseline. Preserve the current contract and behavior until a specific V2 delivery replaces it.

Observed Canvas callers: ALM - StockOpname - Available, ALM-Asset Master.

Connectors observed: shared_sharepointonline.
Nested actions: 9. Trigger: Request / PowerAppV2. No recurrence schedule is defined.

## Trigger contract

| Internal input key | Display title | Type | Required | Nested file fields |
|---|---|---|---|---|
| text | Text | string | yes |  |

`TRIGGER-CONTRACT.json` is authoritative for full schema details, input order and required properties. The baseline does not implement the future entity/function contract merely because documentation calls for it.

## Implement in the target environment

1. Read `../../Others/handover/START-HERE.md` and select a development copy of this flow. Record its target identifier and prior version.
2. Obtain a genuine exported flow package or solution from the company environment if available. `definition.json` is a reference definition, not a standalone importable ZIP. For manual recreation, create a Power Apps (V2) triggered flow and reproduce `TRIGGER-CONTRACT.json` exactly.
3. Resolve every applicable `CONFIGURATION.json` binding using company environment values. Inspect all connection references, recipients, hardcoded links/identifiers, document libraries, SharePoint lists/columns, workbook table names and placeholder strings in the source. Listed bindings are a starting inventory; expressions may contain additional literals. Keep deployment values in the company environment or approved configuration storage.
4. Recreate the action tree from `definition.json` using `ACTION-MAP.md`: preserve nesting, branch conditions, expressions, Parse JSON schemas, response outputs, retries, concurrency and each `runAfter` status. Configure matching connector actions in the designer. Record unsupported actions precisely rather than substituting behavior.
5. Save and run the flow checker. Bind a development Canvas App to the new flow, verify the generated `.Run(...)` parameter signature and compare it with each observed caller before changing callers.
6. Execute `VALIDATION.md` with nonproduction data and test recipients. Capture evidence in the handover results template. Reference-only/placeholder flows can complete as reviewed-and-not-enabled.
7. After the target implementation is validated, export a real company-generated package/solution and record its version in the delivery result. Production promotion is a separate release task.

## Rollback

Keep the previous flow and app binding available. Disable the development replacement and reconnect the previous binding if validation fails. Revert test-created list records/files using captured IDs; flow rollback does not automatically undo data, messages or approvals already created.

## Documentation

[Microsoft flow package import/export](https://learn.microsoft.com/en-us/power-automate/export-import-flow-non-solution).
