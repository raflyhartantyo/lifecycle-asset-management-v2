# Transfer prompts

D072: general access/capability questionnaires are deferred. No observation report is required to continue design. Use [the solution/connector architecture](../architecture/SOLUTION-AND-CONNECTOR-ARCHITECTURE.md) as the dependency reference; the owner handles setup when implementing each feature. Prompts are optional aids for concrete implementation work, and status is not a runtime test result.

| ID | Status | When to use | Prompt |
| --- | --- | --- | --- |
| 005 | **IN PROGRESS — REVIEWED PARTIAL** | Five lists created by report; D074 resolves shared Asset Types/no OrganizationRef; targeted lookup/index, row-count and retention settings remain | [Shared-site foundation setup](PENDING-005-shared-site-foundation.md) |
| 004 | **PENDING — OPTIONAL** | When choosing to implement the delivered reference-list/browser resources; no action requested now | [Reference catalogue implementation Q&A](PENDING-004-reference-catalogues.md) |
| 003 | **DEFERRED** | Optional reference only; no response requested under D072 | [Access capability check](PENDING-003-access-capability-check.md) |
| 002 | **PENDING** | Optional: create two dedicated empty LAM lists on the existing Function site SITE-F (D073) | [SharePoint foundation](PENDING-002-sharepoint-foundation.md) |
| 001 | **DEFERRED** | Optional historical reference; no new report requested under D072 | [Company environment inventory](PENDING-001-environment-inventory.md) |

Mark an executed prompt complete only after its returned output has been reviewed by the user/main developer. DEFERRED means no action or response is currently requested. Historical filenames may still include PENDING; the status in this index and the file takes precedence.

## Creating future prompts

Use [TEMPLATE.md](TEMPLATE.md) for every new company Claude prompt. Include the response instructions inside the copyable prompt and replace the response path with that prompt's ID and topic.

To return output manually: open this folder on GitHub, choose **Add file → Create new file**, enter `responses/<ID>-<topic>-response.md`, paste Claude's Markdown report, and commit. Send the file link to the main developer for review. A photo sent in chat is also accepted when text transfer is difficult.

## Operating model

The user implements and inspects company systems. Claude provides Q&A using supplied materials and has no direct company-system visibility. Every future prompt must carry this context and manual evidence-collection steps from the template.

Response 001 received; [review and corrections](responses/001-environment-inventory-review.md). Further general inventory collection is DEFERRED under D072; existing observations remain available as reference.

## Visual flow proposals

D066: accompany proposed user flows with a mockup/storyboard/flowchart and concise explanation. The main developer supplies image concepts; text-only Claude Q&A may reference those images or provide a Mermaid flowchart. Link the relevant visual in task-specific prompts so company transfer includes its context. A generated visual is a proposal until reviewed.

Response 005 received and [reviewed](responses/005-shared-site-foundation-review.md). Configuration is partially complete; no runtime/security cases have run. Preserve the [original response](responses/005-shared-site-foundation-response.md); resume only the specific open items rather than repeating completed setup.
