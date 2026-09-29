"""Build local visual assets from the exact creator downloads; never redistribute Chill files."""

import argparse
from copy import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

PACK = Path(__file__).resolve().parents[1]
CHILL_SHA256 = "c3666301b3a72bcf3e2410adf95167a10822b361c8e0507e16b0a95da340a507"
DERIVATIVE_SHA1 = "45342cbb6baf37da5f92b6d9bd23001eba6e180b"
SHADER = "Derivative-25.1.0-Chilled-[DC Fork]-Iris-1.8-r3.zip"
COMPONENTS = {
    "Basicpackage": "Chill-Mod-1.3-Free-128x-Base.zip",
    "Equipmentpack": "Chill-Mod-1.3-Free-128x-Equipment.zip",
    "OtherBlockOverlays": "Chill-Mod-1.3-Free-128x-Block-Overlays.zip",
    "Plantpackage": "Chill-Mod-1.3-Free-128x-Plants.zip",
}
SUPPORTED = {"min_inclusive": 4, "max_inclusive": 34}


def digest(path: Path, algorithm: str) -> str:
    result = hashlib.new(algorithm)
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def build_chill(source: Path, destination: Path) -> dict[str, int]:
    if digest(source, "sha256") != CHILL_SHA256:
        raise ValueError("Chill download does not match the pinned 1.3 Free archive")
    destination.mkdir(parents=True, exist_ok=True)
    count = {name: 0 for name in COMPONENTS}
    with ZipFile(source) as original:
        for part, output_name in COMPONENTS.items():
            matches = [item for item in original.infolist()
                       if not item.is_dir() and len(item.filename.split("/")) >= 3
                       and part in item.filename.split("/")[1]]
            if not matches:
                raise ValueError(f"Missing Chill component {part}")
            target = destination / output_name
            temporary = target.with_suffix(".zip.tmp")
            with ZipFile(temporary, "w") as output:
                for item in matches:
                    pieces = item.filename.split("/", 2)
                    relative = pieces[2]
                    if not relative or any(piece in ("", ".", "..") for piece in relative.rstrip("/").split("/")):
                        continue
                    data = original.read(item)
                    if relative == "pack.mcmeta":
                        metadata = json.loads(data.decode("utf-8-sig"), strict=False)
                        if metadata["pack"]["pack_format"] != 4:
                            raise ValueError(f"Unexpected Chill metadata in {part}")
                        metadata["pack"]["supported_formats"] = SUPPORTED
                        data = (json.dumps(metadata, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
                    entry = copy(item)
                    entry.filename = relative
                    output.writestr(entry, data)
                    count[part] += 1
            with ZipFile(temporary) as check:
                if "pack.mcmeta" not in check.namelist() or not any(name.startswith("assets/") for name in check.namelist()):
                    raise ValueError(f"Incomplete Chill component {part}")
                if json.loads(check.read("pack.mcmeta"))["pack"]["supported_formats"] != SUPPORTED:
                    raise ValueError(f"Compatibility metadata missing from {part}")
            temporary.replace(target)
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--instance", type=Path, required=True, help="Minecraft instance game directory")
    parser.add_argument("--chill-archive", type=Path, required=True, help="Official chillmod1.3128x.zip download")
    args = parser.parse_args()
    instance = args.instance.resolve()
    chill = args.chill_archive.resolve()
    derivative = instance / "source-downloads/Derivative [25.1.0].zip"
    if not derivative.is_file():
        raise FileNotFoundError(f"Run packwiz-installer first; missing {derivative}")
    if digest(derivative, "sha1") != DERIVATIVE_SHA1:
        raise ValueError("Derivative download does not match the pinned creator release")
    counts = build_chill(chill, instance / "resourcepacks")
    shader_path = instance / "shaderpacks" / SHADER
    subprocess.run([sys.executable, str(PACK / "tools/build_derivative_compat.py"),
                    "--source", str(derivative), "--output", str(shader_path),
                    "--report", str(instance / "source-downloads/derivative-patch-report.json")], check=True)
    import shutil
    shutil.copyfile(PACK / "shaderpacks" / (SHADER + ".txt"), shader_path.with_name(SHADER + ".txt"))
    print("Prepared four Chill resource packs and the Derivative compatibility fork.")
    print("Chill entries:", counts)


if __name__ == "__main__":
    main()
