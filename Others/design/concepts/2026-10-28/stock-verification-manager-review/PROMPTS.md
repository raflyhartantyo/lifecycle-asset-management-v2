# Generation instructions

Tool: built-in image generation. Date: 2026-10-28. Style reference: prior assignment-response correction concept. These instructions describe proposed illustrative interfaces, not extra approved workflow policies.

## Shared direction

Create ONE readable high-fidelity desktop Power Apps screenshot for Lifecycle Asset Management V2, using the supplied image ONLY as Zurich visual-style reference. Landscape1500x1050. Navy #23366F text, ZurichBlue #2167AE singleprimary action, whitecards, #ECEEEF background, #DDE4E3 borders, #E4E9EC topbar. Arial-like16–18pxbody/32pxtitles,24pxgaps,16pxroundedcards and pillbuttons. No inventedlogo, noemoji, noheavyeffects, nofloor/room. Topbar role Asset Manager, avatar AM. Leftnav Home, Assets, My Tasks, Stock Verification SELECTED, Reconciliation, Reports. Scope Entity A / IT. Conceptualsampledata, noactualcompanyrecords. Mainheading thensteptracker thenone clearlyordered workarea, notscatteredsmallwidgets. Respondent observations are evidence only. Review/owner signoff MUST NOT silently write corrections to the asset register. No embedded MicrosoftApprove/Rejectbuttons; no new disposalapprovals. Tinyfooter "PROPOSED REVIEW FLOW · SAMPLE DATA".

## 01-manager-review

Title "Review verification results". Subtitle "October cycle · Review discrepancies before owner sign-off." Three-stage tracker "1 Collect responses" done, "2 Manager review" active navy, "3 Owner sign-off" pending. Compact countsinline "50 Assets" "43 Reviewed" "7 Need review".
One dominantwhitecard "Discrepancies to review". Topfilter "Review status: Needs review". Table columns Asset | Reported issue | Respondent | Review status. Three rows Shared printer ACCT-000247 / Building, custodian and condition differ / Employee A / Needs review SELECTED; Office projector ACCT-000249 / Not found / Employee B / Needs review; Meeting display ACCT-000248 / Custodian differs / Employee C / Needs review.
Belowtable, attacheddetailsection forselected "Shared printer · Compare evidence" with Field | Assigned register snapshot | Respondent observation:
Building / Building A / Building B
Custodian / Employee C / Employee D
Condition / Good / Broken.
Plain attribution "Response submitted by Employee A".
Reviewfield label "Review outcome" dropdown "Unresolved — follow-up required". Thisisaproposedreviewclassification, notapproval. No mandatoryreasonfield.
Smallinfo "Recording this review does not update master data." Secondarylink "Prepare a separate register correction" (opensauthorizedmovementworkflowlater,notapplybutton).
Footer secondary "Back to cycle" and ONE primary "Save review". Footerhelper "An unresolved exception stays unverified." No auto-markverifiedwhensavingthis unresolvedoutcome. No cyclecompletionbutton or Requestsignoffyet.

## 02-owner-signoff

Title "Prepare Business Owner sign-off". Subtitle "October cycle · Confirm the reviewed results and exceptions." Three-stage tracker "1 Collect responses" done, "2 Manager review" done, "3 Owner sign-off" currentnavy. A simplefullwidthsummarystrip "50 Assets" "43 Verified" "7 Unresolved · remain unverified". Small "All responses reviewed" line. These are a laterstateofsamplecycle, notclaimingwrongassetverified.
Main dominantwhitecard "Sign-off requests by Business Owner". Helper "Each owner receives only their relevant asset results and exceptions." Table columns Business Owner | Assets | Verified | Unresolved | Delivery.
Employee D /30/26/4/ Microsoft Approvals
Employee E /20/17/3/ Microsoft Approvals.
Belowtable an expandable row "Review 7 unresolved exceptions" with a chevron. Smallinstruction "Unresolved assets must remain visible in the sign-off summary." Do not hide unresolved behindcompleted100% badge. A checkedproposedreviewcheckbox "I have reviewed the results and unresolved exceptions." No mandatoryfree-textreason.
Oneprimaryfooterbutton "Request sign-offs", secondary Back. Smalltext "Owners make their decisions in Microsoft Approvals." Do not renderApproveReject inLAM. No fakealreadyapprovedlabels.
Bottomquietinfo "Requesting sign-off does not update the asset register or close the cycle." Anotherplainnote "Cycle closure follows required owner decisions and acknowledged exceptions." No automaticmark7asverified. Show noawaitingresponseorunreviewedcountbecauseallreviewdone. Restrainedwhite/navyblue notbrightcolors. Entirepagefitsviewport.