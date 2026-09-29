"""Build a minimal Iris 1.8 compatibility copy of the pinned creator release."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source", type=Path, default=ROOT / ".cache/derivative/Derivative [25.1.0].zip")
parser.add_argument("--output", type=Path, default=ROOT / "shaderpacks/Derivative-25.1.0-Chilled-[DC Fork]-Iris-1.8-r3.zip")
parser.add_argument("--report", type=Path, default=ROOT / "docs/derivative-compat-patch.json")
args = parser.parse_args()
SOURCE = args.source
OUTPUT = args.output
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
assert hashlib.sha1(SOURCE.read_bytes()).hexdigest() == "45342cbb6baf37da5f92b6d9bd23001eba6e180b"
changes = []
with zipfile.ZipFile(SOURCE) as original, zipfile.ZipFile(OUTPUT, "w") as output:
    # No pass consumes this extra rain attachment. Removing it avoids allocating
    # target 31, which Iris 1.8.12 rejects, while keeping the visible rain output.
    rain_path = "shaders/world0/gbuffers_weather.fsh"
    consumers = [n for n in original.namelist() if n.endswith((".glsl", ".inc", ".frag", ".vert", ".fsh", ".vsh", ".properties"))
                 and n != rain_path and re.search(rb"\bcolortex31\b", original.read(n))]
    assert not consumers, consumers
    for entry in original.infolist():
        before = original.read(entry)
        after = before
        if entry.filename == rain_path:
            text = before.decode("utf-8")
            text, declarations = re.subn(r"^layout\(location = 1\) out vec4 colortex31Out;\r?\n", "", text, flags=re.M)
            text, directives = re.subn(r"/\* RENDERTARGETS: 0,31 \*/", "/* DRAWBUFFERS:0 */", text)
            text, writes = re.subn(r"^\s*colortex31Out = vec4\(rainColor, albedoAlpha > 0\.1 \? 1\.0 : 0\.0\);\r?\n", "\n", text, flags=re.M)
            assert (declarations, directives, writes) == (1, 1, 1)
            after = text.encode("utf-8")
        elif entry.filename == "shaders/block.properties":
            # The upstream file closes an already-closed conditional here.
            lines = before.decode("utf-8").splitlines(keepends=True)
            assert lines[330].strip() == "#endif"
            del lines[330]
            after = "".join(lines).encode("utf-8")
        elif entry.filename == "shaders/item.properties":
            # Java Properties reads ISO-8859-1; these UTF-8 prose comments break
            # Iris's C preprocessor. Keep all mapping values and ASCII comments.
            lines = before.decode("utf-8").splitlines(keepends=True)
            after = "".join(line for line in lines if not (
                line.lstrip().startswith("#") and not line.isascii())).encode("utf-8")
        elif entry.filename == "shaders/lib/util/voxelMap.glsl":
            # The LOD image is declared only for voxel reflections, but the
            # original writes it even when REFLECTION_MODE=0 (screen-space).
            text = before.decode("utf-8")
            text, count = re.subn(r"^(\s*)imageStore\(voxellodimg, ivec3\(voxelPos\) / 4, uvec4\(1u, 0u, 0u, 0u\)\);",
                                 r"\1#if REFLECTION_MODE >= 1\n\1imageStore(voxellodimg, ivec3(voxelPos) / 4, uvec4(1u, 0u, 0u, 0u));\n\1#endif", text, flags=re.M)
            assert count == 1
            after = text.encode("utf-8")
        elif entry.filename == "shaders/program/Post/Grade.glsl":
            # Upstream adds a second weather-only bloom composite on top of
            # ordinary bloom. It uses a colortex0 blue-channel mask and ignores
            # BLOOM_AMOUNT, creating bright edge flashes while the camera turns.
            # Preserve ordinary bloom in both styles, but omit this extra boost.
            donor = (b"    #if !defined IS_NETHER\r\n"
                     b"        if (isEyeInWater == 0 && wetness > 1e-2) {\r\n"
                     b"            float rain = texelFetch(colortex0, texel, 0).b * 0.35;\r\n"
                     b"            color = color * (1.0 - rain) + bloomData * rain * 1.25;\r\n"
                     b"        }\r\n"
                     b"    #endif\r\n")
            standard = (b"    #if !defined IS_NETHER\r\n"
                        b"        if (isEyeInWater == 0 && wetness > 1e-2) {\r\n"
                        b"            float rain = texelFetch(colortex0, texel, 0).b * 0.35;\r\n"
                        b"            fogBloom *= 1.0 + weatherSnowySmooth * 2.0;\r\n"
                        b"            color = color * (1.0 - rain) + fogBloom * fma(clamp(exposure, 0.6, 2.0), 0.15, 0.3) * rain;\r\n"
                        b"        }\r\n"
                        b"    #endif\r\n")
            assert before.count(donor) == 1 and before.count(standard) == 1
            after = before.replace(donor, b"    // Extra weather bloom omitted in the Chilled compatibility fork.\r\n")
            after = after.replace(standard, b"    // Extra weather bloom omitted in the Chilled compatibility fork.\r\n")
        elif entry.filename in ("shaders/lib/Atmosphere/Fogs.glsl", "shaders/program/Deferred0.glsl", "shaders/program/Deferred1.glsl"):
            lines = before.decode("utf-8").splitlines(keepends=True)
            stack = []
            unmatched = []
            for i, line in enumerate(lines):
                if re.match(r"^\s*#\s*(if|ifdef|ifndef)\b", line):
                    stack.append(i)
                elif re.match(r"^\s*#\s*endif\b", line):
                    if stack:
                        stack.pop()
                    else:
                        unmatched.append(i)
            assert len(unmatched) == 1 and not stack
            del lines[unmatched[0]]
            after = "".join(lines).encode("utf-8")
        output.writestr(entry, after)
        if after != before:
            changes.append({"file": entry.filename, "original_sha256": hashlib.sha256(before).hexdigest(),
                            "patched_sha256": hashlib.sha256(after).hexdigest()})
    output.writestr("CHILLED-COMPAT.txt", """Derivative [DC Fork] - Ch4oS-Chilled Iris 1.8 compatibility

Original DC authors: _DureXXX, M1zore, Skeeder461, Frs0n, and _Sone4ka.
Original project: https://www.curseforge.com/minecraft/shaders/derivative-main
Official DC Team Discord: https://discord.gg/UavqfqAwzv

Based on the creator's Derivative [25.1.0].zip, CurseForge file 8529690.
The original License.txt is retained. The main shader settings menu is unchanged.
This compatibility fork removes an unused unsupported rain render attachment,
fixes unmatched preprocessor directives and item-property comment encoding,
guards a voxel LOD image write consistently with its declaration, and removes
the separate weather-only bloom boost that caused edge flashes. Ordinary bloom
remains available through shader settings.
It is a community compatibility fork, not an official creator release.
""")
assert len(changes) == 8
report = {"source_sha1": hashlib.sha1(SOURCE.read_bytes()).hexdigest(), "output": str(OUTPUT),
          "output_sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(), "changes": changes,
          "unchanged_entries": len(zipfile.ZipFile(SOURCE).infolist()) - len(changes)}
with zipfile.ZipFile(SOURCE) as original, zipfile.ZipFile(OUTPUT) as patched:
    assert original.read("License.txt") == patched.read("License.txt")
    assert original.read("shaders/shaders.properties") == patched.read("shaders/shaders.properties")
if args.report:
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report))
