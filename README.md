# Ch4oS-Chilled

Minecraft **1.21.1**, **NeoForge 21.1.252**, Chill Mod **1.3 Free**, and the Derivative **[DC Fork]** compatibility shader. This is the public, source-only packwiz profile for the client-tested 0.1.5 visual setup. Set the Minecraft launcher to Java 21 and about 8 GiB maximum memory on a 32 GiB computer.

The five mod JARs download from their pinned Modrinth releases through packwiz. Packwiz also fetches the original Derivative 25.1.0 release from CurseForge into `source-downloads/`. The local preparation script applies our Iris 1.8 fixes, retains Derivative's bundled `License.txt` and original main shader settings menu, and writes the selected shader to `shaderpacks/`.

**Chill Mod is not in this repository or its download ZIP.** The creator's [free download](https://theartofblocks.com/en/worlds/chill-mod-free-version) is a Google Drive archive containing four nested resource-pack folders. Download it from that page yourself, then run the local preparation step. The script verifies SHA-256 `c3666301b3a72bcf3e2410adf95167a10822b361c8e0507e16b0a95da340a507`, creates four Minecraft-ready ZIPs in your instance, and adds Minecraft 1.21.1 compatibility metadata. It never uploads the files.

## Install

1. Create a new Minecraft 1.21.1 / NeoForge 21.1.252 instance in Prism or another launcher. Find that instance's **game directory** (the folder containing `mods`, `config`, and `resourcepacks`).
2. Use [packwiz-installer](https://packwiz.infra.link/tutorials/installing/packwiz-installer/) with this repository's raw `pack.toml` URL to install the pinned mods, original Derivative download, and our client defaults into that game directory. For a local copy of this folder, its `file:///.../pack.toml` URL also works. Do this before starting Minecraft.
3. Download `chillmod1.3128x.zip` from the creator's [Chill Mod 1.3 Free page](https://theartofblocks.com/en/worlds/chill-mod-free-version). Keep the creator archive intact.
4. With Python 3.10 or newer installed, run:

   ```powershell
   python tools/prepare_visuals.py --instance "C:\path\to\instance\.minecraft" --chill-archive "C:\path\to\chillmod1.3128x.zip"
   ```

   Run this command from a local clone or extracted copy of this source-only repository. The script requires only the Python standard library.
5. Launch Minecraft. The resource-pack menu should show **Equipment**, **Block Overlays**, **Plants**, then **Base** from top to bottom. Iris should select `Derivative-25.1.0-Chilled-[DC Fork]-Iris-1.8-r3.zip` with the balanced 1440p starting preset.

If packwiz-installer has not fetched Derivative yet, the preparation script stops with the missing file path. If either creator download has changed, it stops on the hash check rather than applying the tested compatibility edits to an unknown release.

## Source and terms

- Chill Mod 1.3 Free: [The Art Of Blocks official download](https://theartofblocks.com/en/worlds/chill-mod-free-version). The archive contains no separate license file; this repository carries no Chill assets.
- Derivative 25.1.0: [original release](https://www.curseforge.com/minecraft/shaders/derivative-main/files/8529690). Its bundled [DERCODE 2.5 license](docs/derivative-license.txt) permits credited forks and redistribution subject to its conditions. The locally built fork keeps that license, preserves the main settings menu, and carries `[DC Fork]` in its name. Original DC authors: _DureXXX, M1zore, Skeeder461, Frs0n, and _Sone4ka_. [Original DC project](https://www.curseforge.com/minecraft/shaders/derivative-main) · [DC Team Discord](https://discord.gg/UavqfqAwzv).
- The mod metadata points to the creators' pinned Modrinth downloads. Those files are not in this repository.

The tested 0.1.5 setup kept ordinary bloom and removed the shader's additional wet-weather bloom that produced white edge flashes while turning. The user confirmed that this revision removed the flash. No MVT rerun was requested for these visual changes.
