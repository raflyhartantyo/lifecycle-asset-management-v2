# 3_HomePageMasterData

Reference baseline; target V2 replacement is pending.

Source: `../screens/3_HomePageMasterData.pa.yaml`.

Data references: none found by static formula scan.
Flow calls: none found by static formula scan.
Navigation destinations: 2_HomePage, ALM - Master Asset Type, ALM - Master Category, ALM - Master Employee, ALM - Master Function, ALM - Master Location, ALM - Master Organization, ALM-Asset Master.

## Implementation

1. Follow the app-level `../IMPLEMENTATION.md` prerequisites and preserve existing control names while recreating this reference.
2. Inspect the destination Studio-generated YAML shape before pasting. A full Screens: export wrapper is not assumed to be a paste-ready control snippet. Use supported screen/control copy-and-paste where compatible, or apply the supplied property formulas to the matching screen/control. Capture any rejected YAML and schema error before requesting an adapted delivery.
3. Resolve listed data sources and flow bindings before validating formulas; references through aliases and dynamic expressions need designer inspection too.
4. Run App Checker; navigate to/from this screen and exercise its visible actions with test records. Compare persisted state and audit/history where relevant.
5. For ALM-DisposeRequest, finish as reference-only; V2 retains ALM - Dispose for direct disposal. Baseline review does not authorize disabling a live production screen.

## Formula evidence

| Location in original YAML | Observed functions | Data sources | Flow calls |
|---|---|---|---|
| L150 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/1/Ctr_HPMD_2/Children/0/Ctr_HPMD_2_1/Children/0/ImgCtr_HPMD_2_1/Children/0/Icon_AssetMaster_HPMD_2/Properties/OnSelect | Navigate |  |  |
| L179 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/1/Ctr_HPMD_2/Children/0/Ctr_HPMD_2_1/Children/1/TtlCtr_HPMD_2_1/Children/0/Txt_TitleAssetMaster_HPMD_2/Properties/OnSelect | Navigate |  |  |
| L261 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/1/Ctr_HPMD_2/Children/1/Ctr_HPMD_2_2/Children/0/ImgCtr_HPMD_2_2/Children/0/Icon_MasterAssetType_HPMD_2/Properties/OnSelect | Navigate |  |  |
| L290 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/1/Ctr_HPMD_2/Children/1/Ctr_HPMD_2_2/Children/1/TtlCtr_HPMD_2_2/Children/0/Txt_TitleMasterAssetType_HPMD_2/Properties/OnSelect | Navigate |  |  |
| L371 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/1/Ctr_HPMD_2/Children/2/Ctr_HPMD_2_3/Children/0/ImgCtr_HPMD_2_3/Children/0/Icon_MasterCategory_HPMD_2/Properties/OnSelect | Navigate |  |  |
| L400 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/1/Ctr_HPMD_2/Children/2/Ctr_HPMD_2_3/Children/1/TtlCtr_HPMD_2_3/Children/0/Txt_TitleMasterCategeory_HPMD_2/Properties/OnSelect | Navigate |  |  |
| L483 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/1/Ctr_HPMD_2/Children/3/Ctr_HPMD_2_4/Children/0/ImgCtr_HPMD_2_4/Children/0/Icon_MasterEmployee_HPMD_2/Properties/OnSelect | Navigate |  |  |
| L512 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/1/Ctr_HPMD_2/Children/3/Ctr_HPMD_2_4/Children/1/TtlCtr_HPMD_2_4/Children/0/Txt_TitleMasterEmployee_HPMD_2/Properties/OnSelect | Navigate |  |  |
| L596 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/2/Ctr_HPMD_3/Children/0/Ctr_HPMD_3_1/Children/0/ImgCtr_HPMD_3_1/Children/0/Icon_MasterFunction_HPMD_3/Properties/OnSelect | Navigate |  |  |
| L625 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/2/Ctr_HPMD_3/Children/0/Ctr_HPMD_3_1/Children/1/TtlCtr_HPMD_3_1/Children/0/Txt_TitleMasterFunction_HPMD_3/Properties/OnSelect | Navigate |  |  |
| L686 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/2/Ctr_HPMD_3/Children/1/Ctr_HPMD_3_2/Children/0/ImgCtr_HPMD_3_2/Children/0/Icon_MasterOrganization_HPMD_3/Properties/OnSelect | Navigate |  |  |
| L715 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/2/Ctr_HPMD_3/Children/1/Ctr_HPMD_3_2/Children/1/TtlCtr_HPMD_3_2/Children/0/Txt_TitleMasterOrganization_HPMD_3/Properties/OnSelect | Navigate |  |  |
| L776 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/2/Ctr_HPMD_3/Children/2/Ctr_HPMD_3_3/Children/0/ImgCtr_HPMD_3_3/Children/0/Icon_MasterLocation_HPMD_3/Properties/OnSelect | Navigate |  |  |
| L805 /Screens/3_HomePageMasterData/Children/0/Ctr_HPMD/Children/2/Ctr_HPMD_3/Children/2/Ctr_HPMD_3_3/Children/1/TtlCtr_HPMD_3_3/Children/0/Txt_TitleMasterLocation_HPMD_3/Properties/OnSelect | Navigate |  |  |
| L825 /Screens/3_HomePageMasterData/Children/1/Icon_Home_HPMD/Properties/OnSelect | Navigate |  |  |
