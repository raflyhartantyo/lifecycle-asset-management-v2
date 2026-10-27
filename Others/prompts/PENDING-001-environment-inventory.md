# PENDING-001 — Company environment inventory

Status: **PENDING**

Use now for read-only preparation. Copy the prompt below into company Claude with access to the repository documents.

## Prompt to copy

You are helping prepare the Lifecycle Asset Management project for implementation and individual testing. Read these repository files first:

- `Others/handover/COMPANY-ENVIRONMENT-INVENTORY.md`
- `Others/testing/SETUP-CHECKLIST.md`

Collect the read-only company environment inventory and identify available approved test identities and setup dependencies. Follow the inventory document's fields and the checklist's prerequisites.

Report each item as AVAILABLE, MISSING, or UNKNOWN, with the evidence or source used. Separate observed facts from assumptions. Identify approved identities suitable for the required permission scopes and distinct Business Owner approval paths; the same human tester may use those identities sequentially. Do not treat a UI role switch or an administrator account as proof of restricted access.

If you cannot inspect an item, mark it UNKNOWN and provide the precise read-only steps the human should take to confirm it. Do not invent environment details or claim checks were performed without evidence.

Do not modify or provision resources, create accounts or fixtures, execute app/flow/business tests, or send notifications. Do not include credentials, secrets, or raw personal/business records in the report; use aliases for test identities.

Return:

1. The completed inventory report, with availability and evidence for each item.
2. Missing or unknown prerequisites and who needs to resolve each one, if known.
3. A preparation readiness summary, explicitly identifying testing that remains blocked.

Return your completed report as one Markdown document that I can paste into `Others/prompts/responses/001-environment-inventory-response.md` on GitHub. Use aliases for identities and omit credentials, secrets, and confidential business records. If repository write access is already authorized and available, commit only the response file and return its link; otherwise provide the Markdown text and destination path for me to paste.

Stop after reporting. Fixture creation and test execution require a later implementation/testing instruction.

## Tracking

This prompt remains PENDING until the returned report is reviewed by the user/main developer. Publishing this file does not mean the inventory or any testing has been performed.
