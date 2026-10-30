# PENDING-002 — Create empty SharePoint foundation lists

Status: **PENDING**

Optional implementation aid for the selected existing Function site SITE-F (D073); no new dedicated site is required. This is manual setup; no operational data or app connections yet.

## Prompt to copy

You are my Q&A guide. You have no direct visibility into Power Platform, SharePoint, company configuration or identities. I perform all changes and checks. Use the document excerpts and screenshots I supply; request missing relevant excerpts and mark unconfirmed facts UNKNOWN. Repository access is not assumed.

Guide me through Others/sharepoint/v2/CREATION-GUIDE.md and its FOUNDATION-COLUMNS.csv, one list at a time. Create only the two empty reference lists LAM2_Organizations and LAM2_Functions inside the existing Function site SITE-F. Apply Others/sharepoint/v2/SHARED-FUNCTION-SITE-SETUP.md to the new LAM lists only: isolate inheritance while empty, review copied broad access, retain approved maintainers/readers and preserve existing host content/site membership. Explain required permissions at the relevant step; do not turn this into a general capability questionnaire. Use the revised D044 settings: editable business columns are optional in SharePoint, while the later application enforces business-requiredness. FOUNDATION-COLUMNS.csv separates SharePointRequired from BusinessRequired. Keep unique constraints and the lookup relationship; do not make SharePoint fields mandatory. Keep both lists empty until application validation/master-data entry is delivered. For every step, explain where I click, what I enter, what I should see and what evidence to return. The existing app is blank; leave app connections and baseline resources unchanged. Record discrepancies instead of inventing missing configuration.

Finish when checks FND-01 through FND-07 have PASS/FAIL/NOT RUN with supporting user observations, missing settings, blockers and the version retention setting. Configuration inspection is not a runtime or authorization test pass. Keep operational testing and data loading for a later instruction.

Return your report as one Markdown document that I can paste into Others/prompts/responses/002-sharepoint-foundation-response.md on GitHub. Include what I completed, evidence, missing/unknown items and blockers. Use aliases for sites/groups/identities; omit credentials, secrets and confidential records. Provide the Markdown text and destination path for me to paste; you do not need repository write access.

## Tracking

Keep PENDING until the user/main developer reviews the returned report.
