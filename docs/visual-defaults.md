# Visual defaults and source downloads

Ch4oS-Chilled 0.2.0 replaces the four Chill packs with **LB Photo Realism Reload! 128x**, and the Derivative compatibility fork with the original **Bliss 2.1.2** release. The five existing rendering mods and Minecraft/NeoForge versions remain pinned.

## Exact upstream files

| Component | Release | Installed file | Source |
| --- | --- | --- | --- |
| LB Photo Realism Reload! by 1LotS | 6.3-1.21.3, listed for Minecraft 1.21.1–1.21.3 | `LBPR Reload! v.6.3 for mc1.21.3.zip` | [Modrinth release](https://modrinth.com/resourcepack/lb-photo-realism-reload/version/vGVLaEbp) |
| Bliss by X0nk, based on Chocapic13's shaders | 2.1.2 | `Bliss_v2.1.2_(Chocapic13_Shaders_edit).zip` | [Modrinth release](https://modrinth.com/shader/bliss-shader/version/kC2Y8q1P) |

Packwiz downloads both original ZIPs from their pinned Modrinth URLs and verifies their SHA-512 hashes. Neither ZIP is modified, renamed, unpacked, or included in this repository. No local resource-pack builder or shader patch step is needed.

LB's downloaded `pack.mcmeta` declares format 42 (Minecraft 1.21.3), despite the release listing support for 1.21.1. The default `incompatibleResourcePacks` entry acknowledges this metadata mismatch so Minecraft retains the selected pack. Its resource-pack menu can still show the newer-version label; we do not rewrite the creator archive to suppress it. Visual compatibility still needs a client check.

The LB ZIP has no separate license/terms file. No redistribution grant is inferred from that absence. The pack profile uses the creator's Modrinth download. Bliss includes `LICENSE.md` with Chocapic13's sharing rules; the download retains that license and original title. See the [exact bundled Bliss license](bliss-license.md). No third-party asset or shader source is copied into our public distribution.

## Starting preset

The sidecar `shaderpacks/Bliss_v2.1.2_(Chocapic13_Shaders_edit).zip.txt` contains normal Iris options for a 1440p display, RTX 4070-class GPU and modern CPU. Shader source is untouched.

- 2048 shadow map, 128-block shadow distance.
- Volumetric clouds at the upstream 0.5 quality and 8 volumetric-light samples.
- TAA enabled at native resolution; TAA upscaling disabled.
- LabPBR material reflections remain at Bliss's upstream off defaults: LB does not supply block normal/specular maps. Bliss's normal water reflections remain enabled.
- Bloom strength 0.75. Motion blur, depth of field, parallax, high-quality SSGI, voxel floodfill lighting and translucent entity separation off.
- Bliss's own sky remains selected. Other weather, color and atmosphere settings use upstream defaults.
- Game defaults: Fancy graphics, 16 render chunks and 10 simulation chunks.

Set **Java 21** and **8 GiB maximum heap** in the launcher on a 32 GiB system. Launcher memory is not controlled by packwiz. These are starting settings, not an FPS guarantee.

## Validation scope

Release checks verify the packwiz index and download hashes, installed filenames, supported shader option names/values, resource/shader defaults and source-only export contents. On October 1, 2026, a fresh Java 21 / packwiz-installer 0.5.14 client installation completed all 10 of 10 files successfully; the installed downloads and defaults were verified against the profile. The Windows Prism import ZIP's exact startup script was also run from a newly extracted folder with spaces in its path under Windows PowerShell 5.1, starting with no installer JARs: it downloaded the official bootstrap, ran the live GitHub packwiz profile, and installed all 10 files with matching hashes and defaults. The archive contains the `instance.cfg` and `mmc-pack.json` manifests recognized by Prism's import format; GUI import itself was not automated. The current build has not yet passed an in-game visual or shader compilation check; earlier Chill/Derivative client results do not validate LB/Bliss. MVT is not rerun for this visual-only change, as requested.
