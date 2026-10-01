# Ch4oS-Chilled

Minecraft **1.21.1**, **NeoForge 21.1.252**, **LB Photo Realism Reload! 128x**, **Bliss 2.1.2** and **DERCODE 1.7**. Pack version **0.2.2**.

Packwiz downloads all five mod JARs, the original LB resource-pack ZIP and the exact Bliss release from pinned Modrinth URLs, plus the original DERCODE 1.7 ZIP from CurseForge. This repository contains download metadata and our settings. There are no bundled third-party binaries, shader source edits or local asset preparation steps.

## Install

For **Prism on Windows**, choose **Add Instance → Import from ZIP** and select `Ch4oS-Chilled-0.2.2-Prism-packwiz.zip` directly. Launch the imported instance. Our pre-launch script downloads the official packwiz bootstrap, verifies its SHA-256, and runs packwiz against the live GitHub profile. Packwiz downloads the five mods, LB, Bliss and DERCODE, and checks for updates on later launches. No third-party binaries are bundled in the ZIP.

The `public-source.zip` is a source archive for editing the pack; **it cannot be imported into a launcher**. The optional `.mrpack` is a separate launcher export with direct download references, including CurseForge. It is not a Modrinth-hosting submission; Prism users should use the packwiz ZIP.

Set the instance to use **64-bit Java 21** and **8 GiB maximum memory** on a 32 GiB system. A fresh instance selects LB and enables Bliss with built-in rain puddles and reflections enabled in the balanced 1440p / RTX 4070 starting settings. DERCODE has a separate balanced preset: select `DERCODE [1.7].zip` in **Video Settings → Shader Packs** to load its Derivative water and rain ripples. Iris keeps settings separately for each shader. Do not apply an upstream quality preset afterward unless you want to replace our settings. See [visual defaults, provenance and validation scope](docs/visual-defaults.md).

Alternatively, use the live packwiz profile:

1. Create a Minecraft 1.21.1 / NeoForge 21.1.252 instance. Find its game directory, containing `mods`, `config` and `resourcepacks`.
2. Download the official [packwiz-installer bootstrap JAR](https://github.com/packwiz/packwiz-installer-bootstrap/releases) into that game directory.
3. Set this Prism pre-launch command, or run it from the game directory with Java 21:

   ```text
   "$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/Cha0sCollective/Ch4oS-Chilled/main/pack.toml
   ```

   See the [packwiz installer guide](https://packwiz.infra.link/tutorials/installing/packwiz-installer/) for other MultiMC-compatible launchers.
4. Launch Minecraft. No manual Chill download or Python preparation step is needed.

For an existing Chill/Derivative instance, import the Prism ZIP as a separate instance for client testing. When using packwiz to update an existing instance, locally prepared Chill/Derivative ZIPs from older versions may remain on disk, but the new defaults select only LB and Bliss. Back up existing controls and video settings before replacing `options.txt`.

## Included foundation

| Component | Version |
| --- | --- |
| Iris Shaders | 1.8.12 |
| Sodium | 0.6.13 |
| Continuity | 3.0.0+1.21.neoforge |
| Sinytra Connector | 2.0.0-beta.17 |
| Forgified Fabric API | 0.116.15+2.3.5 |
| LB Photo Realism Reload! | 6.3-1.21.3 (supports 1.21.1) |
| Bliss Shaders | 2.1.2 |
| DERCODE (alternative shader) | 1.7 |

LB's archive declares a newer resource-pack format even though the release explicitly lists 1.21.1 support. The defaults acknowledge this mismatch without changing the ZIP; the menu may still label it as made for a newer version. The user confirmed Bliss rain puddles in client testing. DERCODE testing showed bright rectangular ground reflections during rain; it remains an optional shader. DERCODE includes DH terrain/water programs for the Overworld and Nether; Distant Horizons is not installed yet and its compatibility remains untested.

## Sources and terms

- [LB Photo Realism Reload! by 1LotS, exact release](https://modrinth.com/resourcepack/lb-photo-realism-reload/version/vGVLaEbp). The downloaded archive contains no separate license file. This profile directs the creator-hosted download and does not redistribute its assets.
- [Bliss 2.1.2 by X0nk](https://modrinth.com/shader/bliss-shader/version/kC2Y8q1P), based on Chocapic13's shaders. The original ZIP includes [these license rules](docs/bliss-license.md), which remain unchanged in the download.
- [DERCODE 1.7 by the DERCODE team, exact release](https://www.curseforge.com/minecraft/shaders/dercode/files/7680105). The pinned original download retains its bundled [README and terms](docs/dercode-notice.txt). Our preset changes only normal Iris options; there is no shader fork or patch.
- The mod metadata points to the creators' pinned Modrinth downloads. Those JARs are not in this repository or our exports.

## Build

```powershell
packwiz refresh
packwiz --cache ../.cache/packwiz modrinth export --restrictDomains=false --output ../dist/Ch4oS-Chilled-0.2.2.mrpack
python tools/build_source_zip.py
python tools/build_prism_zip.py
```

The Prism ZIP is directly importable and runs packwiz at launch. The source ZIP contains this packwiz profile for development. The optional `.mrpack` contains official download references and our defaults. MVT was not rerun for these visual changes at the user's request.
