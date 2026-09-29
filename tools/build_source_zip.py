"""Make a source-only distribution; fail if a third-party binary could be included."""

from pathlib import Path
import tomllib
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT.parent / "dist" / "Ch4oS-Chilled-0.1.5-public-source.zip"
ALLOW = {
    ".gitattributes", ".gitignore", ".packwizignore", "README.md",
    "pack.toml", "index.toml", "options.txt", "config/iris.properties",
    "docs/derivative-license.txt", "shaderpacks/Derivative-25.1.0-Chilled-[DC Fork]-Iris-1.8-r3.zip.txt",
    "source-downloads/derivative.pw.toml", "tools/build_derivative_compat.py",
    "tools/prepare_visuals.py", "tools/build_source_zip.py",
}
ALLOW.update(f"mods/{path.name}" for path in (ROOT / "mods").glob("*.pw.toml"))


def main() -> None:
    index = tomllib.loads((ROOT / "index.toml").read_text(encoding="utf-8"))
    listed = {item["file"] for item in index["files"]}
    expected = {"options.txt", "config/iris.properties",
                "shaderpacks/Derivative-25.1.0-Chilled-[DC Fork]-Iris-1.8-r3.zip.txt",
                "source-downloads/derivative.pw.toml"}
    expected.update(f"mods/{path.name}" for path in (ROOT / "mods").glob("*.pw.toml"))
    if listed != expected:
        raise ValueError(f"Unexpected packwiz index files: {listed ^ expected}")
    if len(listed) != 9:
        raise ValueError("Expected five mod downloads, one shader source, and three first-party files")
    for name in ALLOW:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(name)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(OUTPUT, "w", compression=ZIP_DEFLATED) as archive:
        for name in sorted(ALLOW):
            archive.write(ROOT / name, name)
    with ZipFile(OUTPUT) as check:
        if set(check.namelist()) != ALLOW:
            raise ValueError("Source-only ZIP contents changed")
    print(f"Created {OUTPUT} ({OUTPUT.stat().st_size:,} bytes; {len(ALLOW)} source files)")


if __name__ == "__main__":
    main()
