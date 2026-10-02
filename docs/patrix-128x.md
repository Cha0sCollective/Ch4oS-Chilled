# Switching to Patrix 128x

Ch4oS-Chilled installs the official **Patrix 1.21 32x basic** pack through packwiz. Higher resolutions are a player-installed option; obtain them directly from [Patrix's creator](https://www.patreon.com/patrix).

1. Get the **Minecraft 1.21 / 1.21.1** version of the **128x basic** pack. Its material maps work with the included Bliss preset.
2. In Minecraft, open **Options → Resource Packs → Open Pack Folder**, and copy the original ZIP there without extracting or renaming it.
3. Disable the selected **Patrix 32x basic** pack and enable **Patrix 128x basic**. Use only one basic resolution at a time. Keep basic at the bottom of your selected Patrix packs, just above the default/mod resources.
4. If you use matching optional Patrix packs, put them above basic. The resolution-independent models pack can go above basic too. The modpack only installs basic; optional packs are your own downloads.
5. Leave **Bliss 2.1.2** selected. POM, material AO, porosity, LabPBR emission/SSS, water and puddles are already configured. Bliss does not need a separate 32x/128x texture-resolution setting for this preset. Do not apply an upstream shader quality preset unless you intend to replace these settings.

The 32x ZIP remains managed by packwiz and can stay installed while disabled. Future pack defaults updates may restore the 32x selection; if that happens, select 128x again. Never replace or rename the managed 32x ZIP with a 128x archive: packwiz verifies its exact download hash.

Use Java 21 and the existing 8 GiB memory limit as a starting point. Higher-resolution Patrix uses more graphics memory and may require shorter view distance. The 1440p / RTX 4070 shader preset is a starting point, not a measured FPS guarantee.

Our distribution contains download references and settings. It does not include or host any Patrix archive, including 128x.
