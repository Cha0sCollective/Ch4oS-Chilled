# Visual defaults and source downloads

Ch4oS-Chilled **0.3.0** replaces LB with the original **Patrix 1.21 32x basic** archive and configures **Bliss 2.1.2** for its LabPBR materials. Minecraft/NeoForge and the five original rendering mods stay pinned. Entity Texture Features and Entity Model Features are added for the custom mob features included in Patrix. DERCODE stays available with its separate existing preset.

## Exact upstream files

| Component | Release | Installed file | Source |
| --- | --- | --- | --- |
| Patrix by patrix1221 | 1.21/1.21.1, file 5866765 | `Patrix_1.21_32x_basic.zip` | [CurseForge release](https://www.curseforge.com/minecraft/texture-packs/patrix-32x/files/5866765) |
| Bliss by X0nk | 2.1.2 | `Bliss_v2.1.2_(Chocapic13_Shaders_edit).zip` | [Modrinth release](https://modrinth.com/shader/bliss-shader/version/kC2Y8q1P) |
| DERCODE | 1.7, file 7680105 | `DERCODE [1.7].zip` | [CurseForge release](https://www.curseforge.com/minecraft/shaders/dercode/files/7680105) |

Packwiz verifies pinned SHA-512 hashes for these original downloads. No resource/shader ZIP is changed or bundled in our repository or exports. Patrix declares resource pack format 34, matching Minecraft 1.21/1.21.1, so no incompatibility acknowledgement is needed. Its archive includes 956 block normal maps, 935 block specular maps, 7,754 connected-texture normal maps, 78 custom entity models and 16 random-entity rule files.

The downloaded Patrix archive includes `CREDITS.txt`, copied byte-for-byte to [patrix-credits.txt](patrix-credits.txt), but no separate license/terms file. We infer no asset redistribution grant and use the original creator-hosted download. Bliss and DERCODE keep the licenses/notices bundled in their original archives; see [Bliss license](bliss-license.md) and [DERCODE notice](dercode-notice.txt). Higher-resolution Patrix is a player-supplied option; follow the [128x swap guide](patrix-128x.md).

## Bliss Patrix preset

The `Bliss_v2.1.2_(Chocapic13_Shaders_edit).zip.txt` sidecar supplies normal Iris options for 1440p, an RTX 4070-class GPU and a modern CPU. Shader source is untouched.

- POM on: adaptive step length, depth 0.25, 40 maximum iterations and 25-block maximum distance. The normal maps supply height data; no separate texture-resolution setting is needed to swap 32x for 128x.
- Material ambient occlusion and porosity on. `EMISSIVE_TYPE=2` and `SSS_TYPE=2` use LabPBR emission/subsurface maps with hardcoded fallback for unmapped modded materials. Mob SSS is enabled.
- The tested ground/puddle settings stay: specular, sky, scenery reflections and Detailed Roughness on; fixed ground SSR quality 100 with dynamic reduction off; puddles at size 1.0. Solid-block sun/moon highlight multiplier remains zero.
- Water settings stay: specular, scenery and sky/fog reflections, sun/moon highlights and refraction on; water SSR quality 100, dirt amount 0.08, wave strength 1.0 and wave speed 0.8; vanilla-like water off.
- 2048 shadows out to 128 blocks, cloud quality 0.5, 8 volumetric-light samples, native TAA, bloom 0.75. Motion blur, depth of field, high-quality SSGI, LPV and translucent entity separation stay off.
- Game defaults: Fancy graphics, 16 render chunks, 10 simulation chunks; Patrix 32x basic selected. Use Java 21 and 8 GiB maximum heap as a starting point. This is not a measured FPS guarantee.

Patrix material maps change how reflections and wet surfaces look even with identical shader options. The earlier LB screenshot tests do not validate the new Patrix appearance; client testing is still needed.

## DERCODE alternative

The DERCODE 1.7 ZIP and sidecar are unchanged. That alternative retains Derivative water style 0, rain ripples, native TAA, 2048 shadows and reduced extra bloom, but normal/specular material maps and terrain parallax remain disabled. Bliss is the configured Patrix default. DERCODE has a known bright-ground-reflection issue during rain. Distant Horizons is not installed; future compatibility needs testing with the chosen Iris/DH versions.

## Historical validation through 0.2.5


Release checks verify the packwiz index and download hashes, installed filenames, supported shader option names/values, resource/shader defaults and source-only export contents. On October 1, 2026, a fresh Java 21 / packwiz-installer 0.5.14 client installation completed all 10 of 10 files successfully; the installed downloads and defaults were verified against the profile. The Windows Prism import ZIP's exact startup script was also run from a newly extracted folder with spaces in its path under Windows PowerShell 5.1, starting with no installer JARs: it downloaded the official bootstrap, ran the live GitHub packwiz profile, and installed all 10 files with matching hashes and defaults. The archive contains the `instance.cfg` and `mmc-pack.json` manifests recognized by Prism's import format; GUI import itself was not automated. At the 0.2.0 release checks, the build had not yet passed an in-game visual or shader compilation check; earlier Chill/Derivative client results do not validate LB/Bliss. MVT is not rerun for this visual-only change, as requested.

For version 0.2.1, a clean packwiz-installer 0.5.14 client installation from the refreshed local profile completed all 12 of 12 files successfully. All eight downloaded archives/JARs matched their pinned hashes; all four settings files matched the profile byte for byte. The DERCODE sidecar contains 53 option names with values checked against declarations in the original ZIP. The source ZIP and optional launcher export were checked for bundled third-party binaries; the latter has eight download references, including the original CurseForge DERCODE URL. Bliss selection and its existing sidecar are unchanged. At the 0.2.1 release checks, in-game DERCODE compilation, rainy water appearance and future DH integration had not yet been tested.

For version 0.2.2, the user confirmed that Bliss puddles appear in the running client and requested these settings as the default. DERCODE testing showed bright rectangular ground reflections during rain, which persisted with forced ground reflections disabled; DERCODE remains available as an alternative. The Bliss change uses supported Iris options only, with the original shader ZIP untouched. It does not add Derivative's rain-ripple behavior. No performance benchmark or Distant Horizons test was performed.

Version 0.2.2 release checks passed for both matching 12-file packwiz profiles, supported Bliss option names/values, original visual download hashes and bundled notices. The Prism import ZIP, source ZIP and optional launcher export were rebuilt and checked; the export has eight download references and the archives contain no third-party JARs or asset ZIPs. MVT was not rerun for this settings change, as requested.

Version 0.2.3 applies the requested water settings: SSR quality 100 (previously 30), dirt amount 0.08 (previously 0.14) and wave speed 0.8 (previously 1.0). The other requested water toggles and wave strength are now explicit in the sidecar and retain their upstream values. Puddle settings and the DERCODE profile are unchanged. Supported shader options, profile hashes and rebuilt export contents were checked; the new water appearance and performance still need client testing. MVT was not rerun.

Version 0.2.4 promotes the combined grass-reflection fix after the user confirmed it in the running client: solid-block sky reflections off and solid-block sun/moon highlights at strength zero. Puddle scenery reflections, water SSR quality 100, water sun/moon and sky/fog reflections, refraction, dirt amount 0.08, wave strength 1.0 and wave speed 0.8 remain enabled or unchanged as applicable. The DERCODE profile and original shader ZIPs are unchanged. Release checks verified both packwiz profiles, supported option values, upstream visual archive hashes and rebuilt export contents. MVT was not rerun for this settings change.

Version 0.2.5 restores sky reflections to make puddles visible while retaining the disabled solid-block sun/moon highlights. Turning off Detailed Roughness alone did not resolve the reported glitter, and disabling ground scenery reflections looked worse. The user reported that the glitter was gone or much reduced with ground scenery reflections restored, ground SSR quality fixed at 100 and dynamic SSR quality disabled. Re-enabling Detailed Roughness with that fixed sampling then looked better with the glitter controlled, according to the user; the final defaults keep Detailed Roughness on. All requested water options and the DERCODE profile are unchanged. Supported option values, both profile hashes and rebuilt export contents were verified; original shader ZIPs remain unmodified. No FPS benchmark or MVT run was performed.


## Version 0.3.0 validation

The pinned Patrix archive matched the SHA-1 reported by CurseForge and our SHA-512 download hash, passed ZIP integrity checks and declared pack format 34. Its bundled credits and material/model assets were inspected. Every supplied Bliss option name/value was checked against the exact original shader release. The resource/shader archives remain unmodified. A clean Java 21 / packwiz-installer 0.5.14 client install completed all 14 of 14 files successfully. All ten downloaded JARs/ZIPs matched the pinned hashes and all four installed settings files matched the profile byte-for-byte. Both development/public profiles match, and all 42 Bliss option names and values are supported by the exact upstream ZIP. EMF requires ETF 7.2.0 or newer, satisfied by the pinned ETF 7.2.4. Rebuilt exports were checked for expected manifests, defaults and ten official download references, with no bundled third-party JARs or asset ZIPs. No new in-game Patrix result or performance benchmark is claimed. MVT is not rerun for these visual changes.
