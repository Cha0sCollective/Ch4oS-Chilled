"""Build a directly importable Windows Prism instance that installs with packwiz."""

import json
from pathlib import Path
import shutil
import tomllib
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    pack = tomllib.loads((ROOT / 'pack.toml').read_text(encoding='utf-8'))
    version = pack['version']
    cfg = (ROOT / 'launcher/instance.cfg').read_text(encoding='utf-8')
    components = json.loads((ROOT / 'launcher/mmc-pack.json').read_text(encoding='utf-8'))
    versions = {item['uid']: item['version'] for item in components['components']}
    if versions != {'net.minecraft': pack['versions']['minecraft'],
                    'net.neoforged': pack['versions']['neoforge']}:
        raise ValueError('Prism and packwiz versions differ')
    if f'name=Ch4oS-Chilled {version}' not in cfg or 'PreLaunchCommand=' not in cfg:
        raise ValueError('Prism name or pre-launch configuration is missing')
    output = ROOT.parent / 'dist' / f'Ch4oS-Chilled-{version}-Prism-packwiz.zip'
    output.parent.mkdir(parents=True, exist_ok=True)
    files = {'instance.cfg': 'launcher/instance.cfg',
             'mmc-pack.json': 'launcher/mmc-pack.json',
             'minecraft/packwiz-start.ps1': 'launcher/minecraft/packwiz-start.ps1'}
    instructions = f'''Ch4oS-Chilled {version} - Windows Prism / packwiz installer

In Prism, choose Add Instance > Import from ZIP, then select this ZIP directly.
You do not need to extract it or import a .mrpack.

Minecraft 1.21.1 / NeoForge 21.1.252 / Java 21 / maximum memory 8 GiB.
The first launch downloads the official packwiz installer, then packwiz installs
the five mods, LB Photo Realism Reload 128x and original Bliss 2.1.2.
Allow the first download to finish. Later launches check the live GitHub profile
for updates. Internet access is required.

This ZIP contains only our instance configuration and startup script.
Third-party installers, mods and visual packs are fetched from official URLs.
LB and Bliss are selected automatically after packwiz finishes.

Profile: https://raw.githubusercontent.com/Cha0sCollective/Ch4oS-Chilled/main/pack.toml
'''
    with ZipFile(output, 'w', compression=ZIP_DEFLATED) as archive:
        for target, source in files.items():
            archive.write(ROOT / source, target)
        archive.writestr('INSTALL.txt', instructions)
    with ZipFile(output) as archive:
        if set(archive.namelist()) != set(files) | {'INSTALL.txt'}:
            raise ValueError('Unexpected Prism ZIP contents')
        if archive.testzip() is not None:
            raise ValueError('Invalid Prism ZIP')
    # Keep the earlier client-test download name usable as a direct Prism import.
    shutil.copyfile(output, output.with_name(f'Ch4oS-Chilled-{version}-client-test.zip'))
    print(f'Created {output} ({output.stat().st_size:,} bytes; no bundled third-party files)')


if __name__ == '__main__':
    main()
