# Accounting reconciliation — proposed detailed flow

Status: visual/interaction proposal extending D036–D038, D042 and D046. No new owner decision is inferred from sample fields or button states. No company resources changed or runtime tests run.

## Existing confirmed requirements

Retain ledger period/file/run provenance; compare matches, records missing on either side, value/quantity differences and disposed-asset exceptions. Accounting and Governance sign-off comes from configured assignments through Microsoft Approvals. After sign-off, an authorized Asset Manager explicitly previews/applies eligible corrections with history. Registration, direct-disposal and owner/scope-transfer rules still apply. IDR is fixed; register Book Value uses the deferred formula and scheduled monthly flow rather than automatic ledger overwrite.

## Proposed visual sequence

1. Upload within the authorized entity/function context, choose accounting period and inspect column mapping.
2. Validate/compare, review findings and record a proposed resolution plan. Show current/proposed values before requesting configured sign-offs.
3. Collect Accounting/Governance decisions in Microsoft Approvals; no competing LAM approval controls. Parallel/sequential routing and same-person capacity rules for this workflow remain to be specified.
4. Show the approved, versioned plan and current register state. An authorized Asset Manager explicitly selects/applies eligible changes; follow-up actions stay distinct. Successful approval does not mean correction application succeeded or every finding is resolved.

[Three-screen visual proposal](../design/concepts/2026-10-28/reconciliation-flow/README.md).

## Source and matching contract — still pending

The screenshot's Excel filename, AssetCode / NetBookValue / Quantity source columns and mapping controls are illustrative. Supported formats, required columns, ledger periods/snapshots, semantic field definitions and normalization need confirmation from Accounting and the final formula contract. Company-wide unique Accounting Asset Code is the proposed matching anchor; final canonicalization, leading-zero/case treatment and invalid/duplicate input policy remain open. Do not silently merge duplicate ledger codes or treat unmatched rows as permission to create/dispose records.

Select/filter only authorized scope server-side and validate uploaded row provenance. Do not expose other entities' data through comparisons, error previews or exports. Report out-of-scope inputs through the agreed safe error contract. Snapshot source/register evidence and record the compared version/period, including the relevant monthly Book Value calculation version/state. Complete paging/index/delegation behavior must cover the expected approximately 5,000-asset workload and growing history; a preview is not proof that all rows were compared.

## Review plan and sign-off semantics

Preserve row findings, selected proposed dispositions, evidence and the exact plan version considered by approvers. A finding can be investigated, routed to an existing operation or proposed for an eligible correction; the full state/disposition set is not yet approved. The examples show follow-up alongside proposed corrections. Whether every finding must be resolved before sign-off, or a reviewed plan may explicitly retain follow-ups, remains a business-policy gate. The Request sign-offs button illustrates placement, not an approved readiness/exception policy.

Final counts must distinguish assets, ledger rows and findings; categories may overlap depending on the matching contract. Illustrative totals must not become the production aggregation specification. Exact quantity/grouping and disposal-history matches need explicit definition.

Collect approval IDs, assigned/responder identities, decision/time and reviewed snapshot version. Changed input, record versions or plan scope require the agreed invalidation/reapproval handling; old sign-offs must not authorize unseen changes. Rejection, timeout, cancellation and retry paths remain visible and preserve history.

## Correction application and Book Value boundary

Asset name is an illustrative correction-field example in the screenshots, not a confirmed editable-field allow-list. No physical mutation API should accept it until field eligibility, authority and validations are finalized. Likewise no financial correction rule or Book Value override is approved by the concept.

Book Value differences must be investigated against the formula/period/ledger facts. Do not silently copy the ledger amount into the register or invent a zero/purchase-cost initial value. Resolve any authorized exception/manual override/recalculation policy together with D046's monthly formula contract before financial implementation.

Missing register items route to authorized create-only registration; disposed-asset discrepancies route to review of the retained disposal evidence. Do not auto-create records, reactivate disposed assets or bypass dual-owner transfer approvals. If a proposed correction needs an existing registration/disposal/transfer operation, keep that operation's own prerequisites and outcomes linked to the reconciliation run.

Before applying a selected eligible correction, revalidate authority, current state/version, approved plan and inputs. Use durable per-operation identities and auditable prior/new outcomes so retries or uncertain writes do not duplicate or silently lose changes. There is no inferred cross-row atomic transaction. Show approved/not-yet-applied/applied/failed/conflicted/follow-up concepts separately; final physical states are still to be defined.

## Remaining design gates

Ledger template and actual mapping; matching/grouping, duplicate/invalid policy; calculation period alignment; eligible fields; unresolved-follow-up sign-off policy; configured approvers/order/substitution; input/plan reapproval; partial application/recovery; summary/row export and evidence retention; authority/backend isolation; query/index/pagination and operational connections. Financial formula, precision, initial value and override policies remain deferred.

## Planned implementation checks

File/period provenance; valid/invalid/duplicate and out-of-scope rows; all finding classes; counts beyond connector pages; no write on upload/compare; allowed sign-off eligibility; rejected/stale/late approval; explicit authorized apply only; no automatic Book Value overwrite; unchanged registration/disposal/transfer controls; concurrent monthly calculation/edit; duplicate retry/uncertain write; complete per-row history and partial recovery. All NOT RUN.
