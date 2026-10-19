#!/usr/bin/env python3
"""Build and validate the single runtime Skill from pinned components."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def git_revision(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()

def read_manifest() -> dict:
    return json.loads((ROOT / "skill-manifest.json").read_text(encoding="utf-8"))

def component_path(component: dict) -> Path:
    if component.get("source", "remote") == "local":
        return ROOT / component["path"]
    return ROOT / "components" / component["name"] / component["path"]

def collect(manifest: dict) -> tuple[str, list[dict]]:
    sections = []
    evidence = []
    for component in manifest["components"]:
        path = component_path(component)
        if not path.is_file():
            if component.get("required", True):
                raise RuntimeError(f"required Skill component is missing: {component['name']} ({path})")
            continue
        if component.get("source", "remote") != "local":
            repo = path.parents[0]
            actual = git_revision(repo)
            expected = component["revision"]
            if expected.startswith("TODO_") or actual != expected:
                raise RuntimeError(f"{component['name']} is at {actual}, expected pinned revision {expected}")
        text = path.read_text(encoding="utf-8").strip()
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        evidence.append({"name": component["name"], "revision": component.get("revision", "working-tree"), "sha256": digest})
        sections.append(f"\n<!-- component:{component['name']} -->\n{text}\n<!-- end-component:{component['name']} -->\n")
    return "\n".join(sections), evidence

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / "SKILL.md")
    args = parser.parse_args()
    manifest = read_manifest()
    body, evidence = collect(manifest)
    output = "---\nname: norm-skill\ndescription: Norm language, CLI, standard-library, package, and registry guidance for Norm projects.\n---\n\n# Norm\n\nThis file is generated from the pinned components in `skill-manifest.json`.\n" + body
    if args.check:
        current = args.output.read_text(encoding="utf-8") if args.output.exists() else ""
        if current != output:
            raise SystemExit(f"{args.output} is stale; run aggregate_skill.py")
    else:
        args.output.write_text(output, encoding="utf-8", newline="\n")
        (ROOT / "skill-lock.json").write_text(json.dumps({"formatVersion": 1, "components": evidence}, indent=2) + "\n", encoding="utf-8", newline="\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
