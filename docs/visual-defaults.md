# Visual defaults and source downloads

Ch4oS-Chilled 0.2.0 replaces the four Chill packs with **LB Photo Realism Reload! 128x**, and the Derivative compatibility fork with the original **Bliss 2.1.2** release. Version 0.2.1 adds the original **DERCODE 1.7** as an alternative with its own Iris settings file; Bliss stays selected by default. Version 0.2.2 enables the client-tested Bliss rain puddles and reflections by default. The five existing rendering mods and Minecraft/NeoForge versions remain pinned.

## Exact upstream files

| Component | Release | Installed file | Source |
| --- | --- | --- | --- |
| LB Photo Realism Reload! by 1LotS | 6.3-1.21.3, listed for Minecraft 1.21.1–1.21.3 | `LBPR Reload! v.6.3 for mc1.21.3.zip` | [Modrinth release](https://modrinth.com/resourcepack/lb-photo-realism-reload/version/vGVLaEbp) |
| Bliss by X0nk, based on Chocapic13's shaders | 2.1.2 | `Bliss_v2.1.2_(Chocapic13_Shaders_edit).zip` | [Modrinth release](https://modrinth.com/shader/bliss-shader/version/kC2Y8q1P) |
| DERCODE by DureXXX and the DERCODE team | 1.7, CurseForge file 7680105 | `DERCODE [1.7].zip` | [CurseForge release](https://www.curseforge.com/minecraft/shaders/dercode/files/7680105) |

Packwiz downloads LB and Bliss from pinned Modrinth URLs and DERCODE from its pinned CurseForge CDN URL and verifies their SHA-512 hashes. None of these ZIPs is modified, renamed, unpacked, or included in this repository. No local resource-pack builder or shader patch step is needed.

LB's downloaded `pack.mcmeta` declares format 42 (Minecraft 1.21.3), despite the release listing support for 1.21.1. The default `incompatibleResourcePacks` entry acknowledges this metadata mismatch so Minecraft retains the selected pack. Its resource-pack menu can still show the newer-version label; we do not rewrite the creator archive to suppress it. The newer-version label remains visible independently of the shader settings.

The LB ZIP has no separate license/terms file. No redistribution grant is inferred from that absence. The pack profile uses the creator's Modrinth download. Bliss includes `LICENSE.md` with Chocapic13's sharing rules; the download retains that license and original title. See the [exact bundled Bliss license](bliss-license.md). DERCODE retains the original `README.txt` in its download; [this exact notice](dercode-notice.txt) is also included for reference. Its terms are taken from the downloaded archive. We distribute download metadata and our own settings, with no shader source changes. No third-party asset or shader source is copied into our public distribution.

## Starting preset

The sidecar `shaderpacks/Bliss_v2.1.2_(Chocapic13_Shaders_edit).zip.txt` contains normal Iris options for a 1440p display, RTX 4070-class GPU and modern CPU. Shader source is untouched.

- 2048 shadow map, 128-block shadow distance.
- Volumetric clouds at the upstream 0.5 quality and 8 volumetric-light samples.
- TAA enabled at native resolution; TAA upscaling disabled.
- Built-in rain puddles enabled at size 1.0, with specular, screen-space, sky and rough reflections enabled; reflection quality 20.0. These generated puddles do not require block normal/specular maps from LB. Bliss's normal water reflections remain enabled.
- Water reflections, screen-space reflections, sun/moon and sky/fog reflections, and refraction enabled. Water SSR quality (`SSR_STEPS`) 100; dirt amount 0.08, wave strength 1.0 and wave speed 0.8; vanilla-like water disabled. Water SSR quality is separate from the ground/puddle reflection quality of 20.0.
- Bloom strength 0.75. Motion blur, depth of field, parallax, high-quality SSGI, voxel floodfill lighting and translucent entity separation off.
- Bliss's own sky remains selected. Other weather, color and atmosphere settings use upstream defaults.
- Game defaults: Fancy graphics, 16 render chunks and 10 simulation chunks.

Set **Java 21** and **8 GiB maximum heap** in the launcher on a 32 GiB system. Launcher memory is not controlled by packwiz. These are starting settings, not an FPS guarantee.

## DERCODE starting preset

`shaderpacks/DERCODE [1.7].zip.txt` stores independent normal Iris options for the same 1440p / RTX 4070 system. Select **DERCODE [1.7].zip** in Iris's Shader Packs menu to apply them. Switching back to Bliss uses its independent puddle settings file. This appears as a custom combination in the upstream preset selector; no custom preset is inserted into the shader source. DERCODE's release warns about its preset system, so the values are supplied explicitly rather than relying on a named preset.

- Original Derivative **Water Style 0**, upstream wave height 1.2 and speed 1.0, water parallax, caustics, rain ripples and wet surfaces enabled.
- Native render scale 1.0 (instead of the archive's 2.0), TAA, 2048 shadows out to 128 blocks, 12 shadow-filter samples, 16 reflection steps and 4 refinement steps, 16-sample SSAO; GI off.
- Derivative atmosphere/tonemapper, 24 cloud samples and 20 fog samples. Cloud shadows off.
- Regular bloom amount 0.6; added CoD/fog bloom contributions reduced to zero. Chromatic aberration, dirty lens, vignette, motion blur, depth of field and elytra blur off.
- Block normal/specular maps and block parallax off for LB; water reflections remain enabled.

The original ZIP contains DH terrain/water programs for the Overworld and Nether, including a DH-specific branch in the water-wave code. DH is not installed by this change; future compatibility needs testing with the chosen DH/Iris versions, including the End. No DH integration code is removed or changed. These are starting settings, not measured performance results or confirmation that the shader compiles in-game.

## Validation scope

Release checks verify the packwiz index and download hashes, installed filenames, supported shader option names/values, resource/shader defaults and source-only export contents. On October 1, 2026, a fresh Java 21 / packwiz-installer 0.5.14 client installation completed all 10 of 10 files successfully; the installed downloads and defaults were verified against the profile. The Windows Prism import ZIP's exact startup script was also run from a newly extracted folder with spaces in its path under Windows PowerShell 5.1, starting with no installer JARs: it downloaded the official bootstrap, ran the live GitHub packwiz profile, and installed all 10 files with matching hashes and defaults. The archive contains the `instance.cfg` and `mmc-pack.json` manifests recognized by Prism's import format; GUI import itself was not automated. At the 0.2.0 release checks, the build had not yet passed an in-game visual or shader compilation check; earlier Chill/Derivative client results do not validate LB/Bliss. MVT is not rerun for this visual-only change, as requested.

For version 0.2.1, a clean packwiz-installer 0.5.14 client installation from the refreshed local profile completed all 12 of 12 files successfully. All eight downloaded archives/JARs matched their pinned hashes; all four settings files matched the profile byte for byte. The DERCODE sidecar contains 53 option names with values checked against declarations in the original ZIP. The source ZIP and optional launcher export were checked for bundled third-party binaries; the latter has eight download references, including the original CurseForge DERCODE URL. Bliss selection and its existing sidecar are unchanged. At the 0.2.1 release checks, in-game DERCODE compilation, rainy water appearance and future DH integration had not yet been tested.

For version 0.2.2, the user confirmed that Bliss puddles appear in the running client and requested these settings as the default. DERCODE testing showed bright rectangular ground reflections during rain, which persisted with forced ground reflections disabled; DERCODE remains available as an alternative. The Bliss change uses supported Iris options only, with the original shader ZIP untouched. It does not add Derivative's rain-ripple behavior. No performance benchmark or Distant Horizons test was performed.

Version 0.2.2 release checks passed for both matching 12-file packwiz profiles, supported Bliss option names/values, original visual download hashes and bundled notices. The Prism import ZIP, source ZIP and optional launcher export were rebuilt and checked; the export has eight download references and the archives contain no third-party JARs or asset ZIPs. MVT was not rerun for this settings change, as requested.

Version 0.2.3 applies the requested water settings: SSR quality 100 (previously 30), dirt amount 0.08 (previously 0.14) and wave speed 0.8 (previously 1.0). The other requested water toggles and wave strength are now explicit in the sidecar and retain their upstream values. Puddle settings and the DERCODE profile are unchanged. Supported shader options, profile hashes and rebuilt export contents were checked; the new water appearance and performance still need client testing. MVT was not rerun.
