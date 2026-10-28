# List-first respondent verification

Status: list/correction direction confirmed D067; screen details and storage contracts proposed. No company app/list/flow changed; runtime tests NOT RUN.

## Main interaction

Open assigned task → Search/check assigned list → tap once Correct → tap again when incorrect → enter observations on the correction screen → save assigned response → return to list → review/submit responses.

The second activation is proposed as a second deliberate tap/click on the same clearly labeled state control, not a timed double-click or hidden gesture. Provide visible state labels and keyboard/touch activation. The exact UI affordance remains subject to review. The main path for matching assets is one activation, without opening individual details.

## Meaning and proposed state transitions

| Current response | Activation/result |
| --- | --- |
| Not checked | Mark Correct as a respondent assertion |
| Correct | Mark Needs correction, open the correction screen |
| Needs correction | Open/edit that assigned asset's corrections |

Propose an explicit Undo/reset affordance for accidental checks rather than an undocumented third-click cycle. Pending/saved/error feedback must reflect actual persistence. Proposed cancel behavior leaves a flagged item Needs correction / details pending rather than silently treating it as Correct. Exact undo/cancel/submission policies still need review.

Correct means the respondent affirms the asset's observed presence and applicable displayed comparison data. It does not mean Condition=Good: an observed Broken asset may match the registered condition. Correct does not automatically grant final verified status, resolve manager exceptions or close the cycle. Confirm the final comparison-field set and completeness rules before implementation.

## Assignment-only data boundary

Store original assigned/cycle context and actual observations separately (logical model; physical fields pending). Render corrected observations in the assigned response copy while retaining old/original values for review. The sample correction screen compares building, custodian and condition, with presence for not-found/uncheckable cases. These controls/wording illustrate the proposal; the exact editable field set is not newly approved merely by the image.

Asset identity, source register reference, cycle ID, assignment ID, respondent identity and authorization scope are not editable by the respondent. Validate the authenticated caller's current assignment and open-response state on every read/write; an arbitrary client-supplied asset/assignment ID must not authorize access. Limit list search, pagination, correction entry, history and exports to the user's assigned visibility. Former/replaced participants retain the agreed read-only history; reopening/reassignment uses the existing audited process.

No respondent action updates master assets, their Business Owner/scope, inventory or authoritative financial data. No transfer/disposal is created implicitly from an observation. Asset Manager review and subsequent authorized operations retain their separate rules. Directory/reference pickers may supply approved observation values without granting broader register access.

## Correction entry

Compare original values with editable observed values and clearly label Save response corrections. Retain data on failure and mark incomplete entries visibly. Not-found or unable-to-check evidence must remain expressible without inventing a custodian/building/condition that was not observed. Keep unresolved and unanswered assets visibly unverified under existing review rules. No new mandatory BAU reason or mandatory photo requirement is introduced; optional observation notes are proposed.

## Persistence and volume requirements

Assignments can contain many rows; use bounded source-filtered queries/pagination and complete authorized counts. Do not rely on a truncated local asset collection. Keep response state across searches/pages according to the approved persistence contract, and show save/pending/error feedback.

Order per-row activations safely: a delayed first Correct write must not overwrite a later Needs correction action or its observations. Use revision/concurrency and retry/idempotency controls in the delivered implementation. Whether edits auto-save, require a save action or remain a local draft until submission is not yet selected. No false saved/verified count may be shown while a write failed.

Review/submission is a separate stage. Final rules for incomplete/Not checked rows, partial responses and editing after submission remain to be specified while preserving open-step versus closed-history requirements. The sample Review responses button does not declare that all 125 rows are ready to submit.

## Visuals and tests

[Two-screen concept](../design/concepts/2026-10-28/stock-verification-respondent-list/README.md) supersedes the earlier questionnaire-first storyboard. Respondent navigation is restricted to assigned work/history. Desktop/tablet list layout must adapt for mobile; no timed double-click requirement is introduced.

Tests to deliver: one-tap match; second-tap correction; keyboard/touch; cancel/undo; pending/failed/out-of-order writes; saved correction return; unobserved fields; no master mutation; assignment-ID tampering; revoked/reassigned/closed tasks; scoped history/export; pagination and complete counts; manager review distinct from respondent assertion. All NOT RUN.
