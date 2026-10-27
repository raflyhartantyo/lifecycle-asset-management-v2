# Transfer prompts

Copy the linked prompt into company Claude when indicated. Status tracks handover completion, not application test results.

| ID | Status | When to use | Prompt |
| --- | --- | --- | --- |
| 002 | **PENDING** | Once SITE-A is complete: create two empty foundation lists | [SharePoint foundation](PENDING-002-sharepoint-foundation.md) |
| 001 | **PENDING** | Now: read-only preparation | [Company environment inventory](PENDING-001-environment-inventory.md) |

Mark a prompt complete only after its returned output has been reviewed by the user/main developer.

## Creating future prompts

Use [TEMPLATE.md](TEMPLATE.md) for every new company Claude prompt. Include the response instructions inside the copyable prompt and replace the response path with that prompt's ID and topic.

To return output manually: open this folder on GitHub, choose **Add file → Create new file**, enter `responses/<ID>-<topic>-response.md`, paste Claude's Markdown report, and commit. Send the file link to the main developer for review. A photo sent in chat is also accepted when text transfer is difficult.

## Operating model

The user implements and inspects company systems. Claude provides Q&A using supplied materials and has no direct company-system visibility. Every future prompt must carry this context and manual evidence-collection steps from the template.

Response 001 received; [review and corrections](responses/001-environment-inventory-review.md). Inventory remains PENDING until company evidence is supplied.
