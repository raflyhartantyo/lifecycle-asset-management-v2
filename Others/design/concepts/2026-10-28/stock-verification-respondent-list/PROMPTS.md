# Image-generation instructions

Tool: built-in image generation. Date: 2026-10-28. Style reference: prior per-asset movement workspace. Instructions describe proposals, not extra approved requirements.

## Shared direction

Create one high-fidelity desktop Power Apps UI screenshot for Lifecycle Asset Management V2 using the supplied movement screen as a visual-style reference only. Landscape1500x1050; calm Zurich style: navy #23366F text, ZurichBlue #2167AE actions, #ECEEEF background, whitecards, thinDove #DDE4E3 outlines, #E4E9EC topbar. Arial-like16–18pxtext,32pxtitles,24pxspacing, roundedcards/pillbuttons, no inventedlogos, noheavyshadows, noemoji, nofloor/roomfields. The PERSON shown is a TASK-ONLY RESPONDENT, not a global asset administrator: headeravatar Employee A, simple leftsidebar ONLY My Tasks selected and My History. All data sample. User has many assets and explicitly wants movement-like LIST verification. One deliberate tap on a row's state marks Correct; a second tap on that same state opens a separate correction screen. This means two ordinary successive activations, NOT a timed double-click gesture. UI must clearly explain this. Correct and Needs correction are RESPONSE STATES, not final manager verification. Per-assigned-item response data only; masterdata never changes fromrespondentinput. No Approve/Rejectbuttons. No AddAssets becauseassignmentlist fixed; noAccessMatrix edit, no asset registration, no broadsearch. Tinyfooter "PROPOSED RESPONSE WORKSPACE · SAMPLE DATA". Onlyshowassignedrecords, notglobalregister.

## 01-assigned-asset-list

Title "Check your assigned assets". Subtitle "October verification · Entity A / IT · Due 30 Oct 2026".
Nearheading clearguidance "Tap once: Correct. Tap again: enter corrections." Also smallplaintext "Changes are saved to your verification response, not the asset register."
One dominantwhitecard "Assigned assets · 125" with3inlineprogresscounts "94 Marked correct" "6 Need correction" "25 Not checked". These sum125. Do NOT label94verified.
Filterrow within samecard: labeled Search assignedassets input; Response dropdown "All responses". Table columns Accounting code | Asset | Registered building | Registered custodian | Condition | Your response.
Five rows:
ACCT-000245 / Business laptop / Building A / Employee A / Good / readablebutton "Correct" withsmallhelper "Tap again to correct".
ACCT-000246 / Office monitor / Building A / Employee B / Good / button "Correct".
ACCT-000247 / Shared printer / Building A / Employee C / Good / outlinedorange-softbutton "Needs correction" withsmallhelper "Details pending" and link "Enter corrections".
ACCT-000248 / Meeting display / Building B / Employee D / Good / neutralbutton "Not checked" withhelper "Tap to mark correct".
ACCT-000249 / Office projector / Building A / Employee A / Broken / button "Needs correction" withsmallhelper "Corrections entered" andlink "Edit".
Response buttons use navy text and restrainedblue/Dove/palecaution backgrounds, notlotsfilledprimaries; mainprimaryactiononly "Review responses" atbottomright. Rowsatleast64pxhigh forfastclick.
Tablefooter "Showing 1–5 of 125" andPrevious/Next, noSelectAllcorrectshortcutbecauseunapproved. Abovefooter plainnote "Not checked and incomplete corrections are highlighted for follow-up." Do not autoconfirmthem.
Bottomleft secondarylink BacktoMyTasks. No perassetquestionnaire forcorrectrows, no openingassetdetail, no AddAssets or movement destinationcontrols. One efficientlistresponse screen.

## 02-correct-assigned-response

Title "Correct this asset's response". Subtitle "Shared printer · ACCT-000247 · October verification". Toplink "Back to assigned assets". Strongblueoutlinedinfostrip "Verification response only — the master asset record will not change."
Single dominantwhitecard headed "Record what you observed". Show a cleartable with3columns Field | Registered value (read-only) | Your observed value (editable).
Row Asset presence / "Listed for this cycle" / dropdown "Present" (optionsNotfoundUnabletocheckunopened).
Row Building / "Building A" / dropdown "Building B".
Row Custodian / "Employee C" / directoryselection "Employee D".
Row Condition / "Good" / dropdown "Broken". OnlyallowedconditionGoodBrokenReadytoAuction, unopened.
The identityAccountingcode/assetname/cycle/sourceentityfunction is NEVEReditable. Correctedbuilding/custodian/conditionareonlyperassignedresponseobservations; noPatchmaster or transferapprovals. Do not add fields for price or arbitrary masteredits.
Belowtable optional fullwidth fieldlabel "Additional observation (optional)" withtext "Printer is now used by Employee D in Building B." No mandatoryremarksfield.
A compactchange-summaryline "3 differences recorded: building, custodian and condition." PresencePresentnotcountedasdifference.
Smallnote "Saving returns you to the assigned list with this asset marked Needs correction."
Footer secondary "Cancel" and oneprimary "Save response corrections". DO NOT saySaveassetUpdateassetApplytomasterConfirmtransfer. Bottomhelper "Asset Manager reviews discrepancies separately." No outgoingBOapprovals on this responseform.
Keepunambiguousoldvsobservedvisualcomparison, bigreadablecontrols, one straightforwardverticalreadingpath. The actiononlysavesassignmentresponse; itdoesnotmarkcycleclosedorverified.

## Targeted correction

On the correction screen, replace the Asset presence helper with “Can you locate this asset?”; preserve the rest of the image. This avoids confusing physical presence with the Available lifecycle status.
