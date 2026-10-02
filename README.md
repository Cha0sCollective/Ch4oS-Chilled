# Ch4oS-Chilled

Minecraft **1.21.1**, **NeoForge 21.1.252**, **Patrix 32x**, **Bliss 2.1.2** and optional **DERCODE 1.7**. Pack version **0.3.0**.

Packwiz downloads seven mod JARs and the original shader/resource archives from pinned creator-hosted URLs. This repository and its exports contain download metadata and our settings. No third-party binaries, shader source edits or asset preparation steps are bundled.

## Install

For **Prism on Windows**, choose **Add Instance → Import from ZIP** and select `Ch4oS-Chilled-0.3.0-Prism-packwiz.zip`. Launch the instance. Our pre-launch script downloads the official packwiz bootstrap, verifies its SHA-256, and runs the live GitHub profile. The first launch installs the seven mods, Patrix 32x basic, Bliss and DERCODE; later launches check for updates.

Use **64-bit Java 21** and **8 GiB maximum memory** on a 32 GiB system. Patrix 32x and Bliss are selected automatically. Bliss enables POM, material AO, porosity, LabPBR emission/SSS and the tested water/puddle settings. See [visual defaults and validation scope](docs/visual-defaults.md).

Players who obtain **Patrix 128x** from its creator can [swap resolutions using this guide](docs/patrix-128x.md). Only 32x basic is installed by the pack. Optional Patrix packs are player downloads.

The `public-source.zip` is for editing this packwiz profile and **cannot be imported into a launcher**. The optional `.mrpack` is a separate launcher export with direct CurseForge and Modrinth download references; it is not a Modrinth-hosting submission. Prism users should use the packwiz ZIP.

Alternatively, create a Minecraft 1.21.1 / NeoForge 21.1.252 instance and run the official [packwiz-installer bootstrap](https://github.com/packwiz/packwiz-installer-bootstrap/releases) in its game directory with Java 21:

```text
"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/Cha0sCollective/Ch4oS-Chilled/main/pack.toml
```

See the [packwiz installer guide](https://packwiz.infra.link/tutorials/installing/packwiz-installer/) for other MultiMC-compatible launchers. Back up controls and video settings before manually replacing `options.txt`. Existing installations can retain old unmanaged resource ZIPs, but the new default selects Patrix only.

## Included foundation

| Component | Version |
| --- | --- |
| Iris Shaders | 1.8.12 |
| Sodium | 0.6.13 |
| Continuity | 3.0.0+1.21.neoforge |
| Sinytra Connector | 2.0.0-beta.17 |
| Forgified Fabric API | 0.116.15+2.3.5 |
| Entity Texture Features | 7.2.4, NeoForge 1.21 build |
| Entity Model Features | 3.3.9, NeoForge 1.21 build |
| Patrix 32x basic | Minecraft 1.21/1.21.1, CurseForge file 5866765 |
| Bliss Shaders | 2.1.2 |
| DERCODE, alternative shader | 1.7 |

Continuity supports Patrix's connected textures. ETF and EMF support its included custom mob textures, models and animations. Bliss is the configured Patrix shader. DERCODE keeps its independent earlier preset and has known bright ground reflections during rain; its material mapping remains disabled. Distant Horizons is not installed and remains untested.

## Sources and terms

- [Patrix 32x basic by patrix1221, exact release](https://www.curseforge.com/minecraft/texture-packs/patrix-32x/files/5866765). Its archive retains [these bundled credits](docs/patrix-credits.txt). The downloaded archive has no separate redistribution license; no asset redistribution grant is inferred. Packwiz directs the original creator-hosted download.
- [Bliss 2.1.2 by X0nk](https://modrinth.com/shader/bliss-shader/version/kC2Y8q1P), based on Chocapic13's shaders, retains its [bundled license](docs/bliss-license.md).
- [DERCODE 1.7, exact release](https://www.curseforge.com/minecraft/shaders/dercode/files/7680105) retains its bundled [README and terms](docs/dercode-notice.txt).
- The seven mod metadata files direct pinned official Modrinth downloads. Those JARs are not in this repository or its exports.

## Build

```powershell
packwiz refresh
packwiz --cache ../.cache/packwiz modrinth export --restrictDomains=false --output ../dist/Ch4oS-Chilled-0.3.0.mrpack
python tools/build_source_zip.py
python tools/build_prism_zip.py
```

The Prism ZIP runs packwiz at launch. The source ZIP contains the editable profile. The optional `.mrpack` contains official download references and our defaults. MVT is not rerun for these visual changes, as requested.
