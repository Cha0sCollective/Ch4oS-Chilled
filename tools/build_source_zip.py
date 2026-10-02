"""Export an allowlisted packwiz profile without third-party binaries or source."""

from pathlib import Path
import tomllib
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    pack = tomllib.loads((ROOT / "pack.toml").read_text(encoding="utf-8"))
    index = tomllib.loads((ROOT / "index.toml").read_text(encoding="utf-8"))
    listed = {item["file"] for item in index["files"]}
    expected = {"options.txt", "config/iris.properties",
                "shaderpacks/Bliss_v2.1.2_(Chocapic13_Shaders_edit).zip.txt",
                "shaderpacks/DERCODE [1.7].zip.txt",
                "resourcepacks/patrix-32x.pw.toml",
                "shaderpacks/bliss-shader.pw.toml", "shaderpacks/dercode.pw.toml"}
    expected.update(f"mods/{path.name}" for path in (ROOT / "mods").glob("*.pw.toml"))
    if listed != expected or len(listed) != 14:
        raise ValueError(f"Unexpected packwiz index files: {listed ^ expected}")
    allowed = listed | {".gitattributes", ".gitignore", ".packwizignore", "README.md",
                       "pack.toml", "index.toml", "docs/visual-defaults.md",
                       "docs/bliss-license.md", "docs/dercode-notice.txt", "docs/patrix-credits.txt", "docs/patrix-128x.md", "tools/build_source_zip.py",
                       "tools/build_prism_zip.py", "launcher/instance.cfg",
                       "launcher/mmc-pack.json", "launcher/minecraft/packwiz-start.ps1"}
    output = ROOT.parent / "dist" / f"Ch4oS-Chilled-{pack['version']}-public-source.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for name in sorted(allowed):
            path = ROOT / name
            if path.suffix.lower() in (".zip", ".jar", ".mrpack"):
                raise ValueError(f"Third-party binary in source export: {name}")
            archive.write(path, name)
    with ZipFile(output) as check:
        if set(check.namelist()) != allowed:
            raise ValueError("Source-only ZIP contents changed")
    print(f"Created {output} ({output.stat().st_size:,} bytes; {len(allowed)} source files)")


if __name__ == "__main__":
    main()
