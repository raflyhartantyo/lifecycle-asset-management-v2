# Generation instruction

Tool: built-in image generation. Date: 2026-10-28. Style reference: the prior My Tasks concept. This instruction describes a proposal, not additional approved business requirements.

Create ONE clear high-fidelity UI storyboard illustrating a proposed stock-verification respondent flow for Lifecycle Asset Management V2. Three MOBILE SCREEN MOCKUPS arranged left to right on one landscape design board around1900x1200. Screen mockups are clean rectangles, no shiny hardware/deviceframes, no perspective. Three equally sized columns with generous gutters and a short arrow between each column. Each should be large enough for readable16–18pxUItext. Heading at top outside screens "Stock verification · Respondent flow", small subtitle "Open task → Check assigned assets → Review & submit". Caption below each screen "1. Open your assigned task", "2. Check each asset", "3. Review and submit". Everything is a PROPOSAL with sample data.

Use the supplied image only as Zurich style reference: navy #23366F main text, ZurichBlue #2167AE oneprimaryaction per screen, offwhite #ECEEEF background, white cards, thin Dove #DDE4E3 outlines, topbar #E4E9EC, rounded16pxcards,8pxinputs, pillbuttons. Arial-like legibletext, strong headinghierarchy,24pxfieldspacing, calmwhite/offwhite dominant. Do not invent Zurich logo or LAM logo, no emojis, no purple, no heavyshadows, no busycharts. Avoid tiny pale labels; navy text with real field labels. Mobiletapbuttons large.

SCREEN 1 — task list:
Topbar "My Tasks". Tabs "Open" selected and "History". Small scope line "Assigned work only".
One dominant taskcard title "October verification". Subtext "Entity A / IT". Show "3 assets assigned to you", "Due 30 Oct 2026". Small progress text "0 of 3 responses entered". Oneprimary "Open task". Below one quieter historyrow "September verification" with "Submitted · View history" as read-only textlink. No entireassetregister, no Adminnavigation, no role switcher, no Approve/Rejectbutton. Bottomhelper "Previous assignments remain read-only."

SCREEN 2 — respondent asset evidence:
Topbar backarrow "October verification". Progress "Asset 1 of 3" with simplethinprogressline.
Small card "Business laptop", accountingcode "ACCT-000245", registeredcontext "Building A · Employee A". These are read-only context.
Question "Can you locate this asset?" compact 3choicegroup "Present" SELECTED, "Not found", "Unable to check".
Fieldlabel "Observed condition" dropdown "Good". Other permittedconditionvalues are Broken, Ready to Auction but don'topen dropdown or addauctionflag.
Question "Building matches register?" Yes SELECTED, No.
Question "Custodian matches register?" Yes, No SELECTED.
Small conditional field "Observed custodian / discrepancy" value "Used by Employee B"; mark "Optional detail" so no unapprovedmandatoryreason.
Oneprimarybottom "Next asset". Small secondarytext "Back to asset list". No masterupdate or officialapprovecontrols. Thisscreen records evidence, not permanentcustodianchange.

SCREEN 3 — review:
Topbar backarrow "Review responses".
Heading "3 responses ready".
Short vertically ordered reviewlist:
"Business laptop" / "Present · Good" / "Custodian mismatch reported" / link "Edit".
"Office monitor" / "Present · Good" / "No discrepancy reported" / link "Edit".
"Shared printer" / "Not found" / "Flagged for review" / link "Edit". Do not show Good/Brokencondition for unobservedprinter.
Summary "2 present · 1 not found". Oneclearinformationalbox "Not-found assets remain unverified. Your responses go to the Asset Manager for review." Do not falsely label allverifiedorcompleted.
ONEprimarybottom "Submit responses", secondary Back.
Tiny note "Submitting does not change the asset register." No finishcycle, noownerapproval or applymasterbuttons. No upload/requiredphoto policy inventing. Successfulsubmission is not depicted yet.

Acrossboard capture the guided path and clear distinction between submitting evidence and changing masterrecords. Keep all text accurate and nonclipped. Tinybottomcaption "PROPOSED MOBILE EXPERIENCE · SAMPLE DATA". This is the immediate visual accompanying a flow proposal, not final implemented UI.
