# Generation prompts

Date: 2026-10-28. Tool: built-in image generation. Style reference: per-asset movement workspace previously shown in the conversation. Instructions below describe proposed illustrative visuals, not additional approved business rules.

## Shared direction

Generate ONE high-fidelity desktop screen for Lifecycle Asset Management V2. Supplied image is a style reference only. Same calm Zurich palette/navy text #23366F, ZurichBlue #2167AE primary actions, #ECEEEF background, #FFFFFF cards, #DDE4E3 fine borders and #E4E9EC topbar. Arial-like16–18px readablebody,32px headings, spacious24px gaps,16pxroundedcards and pillbuttons. No heavyshadow, no inventedlogo, no emoji, no deviceframe, no collage. Landscape around1500x1050. Headerappname, GlobalUseravatar. White220px sidebar: Home, Assets selected, Inventory, My Tasks, Stock Verification, Reconciliation, Reports, Administration. Headercontext Entity A / IT. Use ONE strong dominant content area with clear start and nextaction. All data are illustrative. No AssetTag example numbers because format is deferred; identify assets using Accounting Asset Code. No floor/roomfields. Tinyfooter "DESIGN CONCEPT · SAMPLE DATA". No embedded approvaldecisionbuttons and no disposalapprovalworkflow.

## 01-disposal-workspace

Screen is the DISPOSAL WORKSPACE, title "Enter disposal details", subtitle "Set the details for each asset, then review before disposing." Stepper "1 Select assets" done, "2 Disposal details" active navy, "3 Review & confirm" pending. Top link "Back to selection". Main singlewhitecard "Disposal list · 3 assets". Small helper "Sale requires buyer and selling price. All disposals require a date." In samecard at top a compact shareddetailsstrip headed "Apply shared details" with input "Disposal date"28Oct2026 and input "Buyer"BuyerA; secondaryoutlinedbutton "Apply to 2 selected". Helper "Fills selected rows only; you can still edit each asset." There must be NO sharedsellingpriceinput and no batchtotalprice.
Below, clear editabletable columns Select | Asset | Mode | Disposal date | Buyer | Selling price (IDR).
Row1checked Business laptop ACCT-000245 / dropdownSale / date28Oct2026 / buyerinputBuyerA / amount2.500.000.
Row2checked Office monitor ACCT-000246 / Sale / 28Oct2026 / BuyerA / 750.000.
Row3unchecked Shared printer ACCT-000247 / Sale / 28Oct2026 / BuyerB / 1.200.000.
All shown rows areSale; this illustrates perasset fields without deciding mixedmodepolicy. Modecontrol couldchooseNon-sale but don'topen dropdown. Eachperassetinput legible not tiny packedtable. Bottomsimple line "Selling price is recorded separately for each asset." No totalprice, taxformula, BookValuecalculation, mandatoryreason, approvalstep or 'Awaitingapproval'.
Footer ofmaincard onleft "Nothing is disposed until final confirmation." SecondaryBack and ONE primary "Review disposal". Do not showcompleteddisposalstatus. Secondary link "Add more assets" nearcardheader. No extra scatteredsummarycards or detachedsidepanel. Layout fits3rows and shortcutcomfortably.

## 02-asset-details-history

Screen is ASSET DETAILS & HISTORY, heading "Business laptop" with Accounting code "ACCT-000245" directlybelow. Toplink "Back to Assets". Quietpilllabels "Available" and "Good". Topright primary "Move asset" and secondaryoutline "Dispose" with spacebetween. These are optionaloneassetentrypoints; bulkselectionpathremains available.
Belowheader, ONE compact horizontal reference-summarystrip: "Asset Type: Laptop · Komputer (KO)" ; "Building: Shared Building A" ; "Custodian: Not assigned". Do not showAssetTag number. No editfinancialamount controls.
Horizontal tabs Overview, Financials, History SELECTED blueunderline, Documents. Main dominantfullwidth whitecard "Asset history". Shorthelper "Follow changes and decisions recorded for this asset." Filter "Event type"dropdownAll events, secondarytextlink "Export history".
Show ONE readable chronological event list, latestfirst, with datesalignedleft, titlebold, changecomparison and actorsecondary. Five events:
"28 Oct 2026" / "Returned to stock" / "Status: In Use → Available" and "Custodian: Employee A → Not assigned" / "Recorded by Operator A".
"15 Oct 2026" / "Business Owner change applied" / "Employee D → Employee E" / "Approved through Microsoft Approvals · View request" (blue link), "Applied by Manager A".
"14 Oct 2026" / "Business Owner change approved" / "Both owner capacities approved" / link "View approval history". Clearly approvalevent separatefrom appliedevent.
"02 Sep 2026" / "Assigned to employee" / "Status: Available → In Use · Custodian: Employee A" / "Recorded by Operator A".
"01 Sep 2026" / "Asset registered" / "Initial Status: Available · Condition: Good" / "Recorded by Operator A".
Use verticalsubtleline smallnavycircles or cleanrowdividers, no inventedlogography, not hugecolorfuleventcards. Keep eventslegible avoidoverlap. Bottomtinyinfo "Movements, decisions and application outcomes remain separate history events." No fakebuttonApprove, no disposaldoneeventforactiveasset, no financialformula assumed, no floor/room. Clearchronologicalreadingpath, no scatteredwidgetdashboard.