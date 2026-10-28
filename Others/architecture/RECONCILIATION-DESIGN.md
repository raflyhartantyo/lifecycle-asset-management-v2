# Accounting reconciliation — proposed detailed flow

Status: D070 confirms application before final sign-off, updating D038’s original order. Remaining interaction details extend D036–D038, D042 and D046 as proposals; sample fields/button states are not additional owner decisions. No company resources changed or runtime tests run.

## Existing confirmed requirements

Retain ledger period/file/run provenance; compare matches, records missing on either side, value/quantity differences and disposed-asset exceptions. Accounting and Governance sign-off comes from configured assignments through Microsoft Approvals. Under D070, an authorized Asset Manager explicitly previews/applies eligible corrections with history before final Accounting/Governance sign-off on the actual applied results. Registration, direct-disposal and owner/scope-transfer rules still apply. IDR is fixed; register Book Value uses the deferred formula and scheduled monthly flow rather than automatic ledger overwrite.

## Proposed visual sequence

1. Upload within the authorized entity/function context, choose accounting period and inspect column mapping.
2. Validate/compare, review findings and record a versioned resolution plan with current/proposed values.
3. An authorized Asset Manager explicitly previews/selects/applies eligible corrections after revalidating authority, versions and transaction-specific prerequisites. Retain actual applied/failed/conflicted results and follow-ups; no write occurs merely from upload/comparison.
4. Request configured Accounting/Governance final decisions through Microsoft Approvals on a versioned snapshot of actual results and evidence. An applied run awaiting sign-off is not finally certified. Order between Accounting and Governance and same-person capacity rules remain open.

[Revised two-screen apply-first sequence](../design/concepts/2026-10-28/reconciliation-apply-first/README.md). Earlier approval-first images are historical and superseded for ordering.

```mermaid
flowchart LR
    A[Upload] --> B[Compare and review]
    B --> C[Preview and explicitly apply eligible corrections]
    C --> D[Record actual results and evidence]
    D --> E[Accounting and Governance final sign-off]
```

Existing Business Owner approvals still precede their specific owner/scope transfer transactions. Final reconciliation sign-off is a separate certification after application.

## Source and matching contract — still pending

The screenshot's Excel filename, AssetCode / NetBookValue / Quantity source columns and mapping controls are illustrative. Supported formats, required columns, ledger periods/snapshots, semantic field definitions and normalization need confirmation from Accounting and the final formula contract. Company-wide unique Accounting Asset Code is the proposed matching anchor; final canonicalization, leading-zero/case treatment and invalid/duplicate input policy remain open. Do not silently merge duplicate ledger codes or treat unmatched rows as permission to create/dispose records.

Select/filter only authorized scope server-side and validate uploaded row provenance. Do not expose other entities' data through comparisons, error previews or exports. Report out-of-scope inputs through the agreed safe error contract. Snapshot source/register evidence and record the compared version/period, including the relevant monthly Book Value calculation version/state. Complete paging/index/delegation behavior must cover the expected approximately 5,000-asset workload and growing history; a preview is not proof that all rows were compared.

## Review plan and sign-off semantics

Preserve row findings, selected proposed dispositions, evidence and the reviewed plan version and actual application-result snapshot considered by final approvers. A finding can be investigated, routed to an existing operation or proposed for an eligible correction; the full state/disposition set is not yet approved. The examples show follow-up alongside proposed corrections. Whether every finding must be resolved before sign-off, or a reviewed plan may explicitly retain follow-ups, remains a business-policy gate. The Request sign-offs button illustrates placement, not an approved readiness/exception policy.

Final counts must distinguish assets, ledger rows and findings; categories may overlap depending on the matching contract. Illustrative totals must not become the production aggregation specification. Exact quantity/grouping and disposal-history matches need explicit definition.

Collect approval IDs, assigned/responder identities, decision/time and reviewed snapshot version. Final sign-offs must identify the actual result snapshot and underlying evidence. Changed results/input/record versions require defined invalidation/resubmission handling; old sign-offs cannot certify unseen changes. Rejection, timeout, cancellation and retry paths remain visible and preserve history. Rejection does not imply an automatic rollback: final rejection/rework/rollback policy remains open. Do not infer readiness from the illustrative button states when failures or follow-ups remain.

## Correction application and Book Value boundary

Asset name is an illustrative correction-field example in the screenshots, not a confirmed editable-field allow-list. No physical mutation API should accept it until field eligibility, authority and validations are finalized. Likewise no financial correction rule or Book Value override is approved by the concept.

Book Value differences must be investigated against the formula/period/ledger facts. Do not silently copy the ledger amount into the register or invent a zero/purchase-cost initial value. Resolve any authorized exception/manual override/recalculation policy together with D046's monthly formula contract before financial implementation.

Missing register items route to authorized create-only registration; disposed-asset discrepancies route to review of the retained disposal evidence. Do not auto-create records, reactivate disposed assets or bypass dual-owner transfer approvals. If a proposed correction needs an existing registration/disposal/transfer operation, keep that operation's own prerequisites and outcomes linked to the reconciliation run.

Before applying a selected eligible correction, revalidate authority, current state/version, reviewed plan and inputs, including any required transfer approvals. Use durable per-operation identities and auditable prior/new outcomes so retries or uncertain writes do not duplicate or silently lose changes. There is no inferred cross-row atomic transaction. Show reviewed/not-yet-applied/applied/failed/conflicted/follow-up outcomes separately from final-sign-off pending/approved/rejected; final physical states are still to be defined.

## Remaining design gates

Ledger template and actual mapping; matching/grouping, duplicate/invalid policy; calculation period alignment; eligible fields; unresolved-follow-up sign-off policy; configured approvers/order/substitution; result-snapshot invalidation/resubmission; final rejection/rework/rollback; partial application/recovery; summary/row export and evidence retention; authority/backend isolation; query/index/pagination and operational connections. Financial formula, precision, initial value and override policies remain deferred.

## Planned implementation checks

File/period provenance; valid/invalid/duplicate and out-of-scope rows; all finding classes; counts beyond connector pages; no write on upload/compare; allowed sign-off eligibility; explicit authorized apply before final sign-off; final review of actual applied/failed results; rejected/stale/late sign-off; no automatic Book Value overwrite; unchanged registration/disposal/transfer controls; concurrent monthly calculation/edit; duplicate retry/uncertain write; complete per-row history and partial recovery. All NOT RUN.
