# Skill aggregation

`skill-manifest.json` is the source of the aggregate component revisions. Each remote component is checked out as a Git submodule under `components/`; the generator refuses to build when a required component is absent or its checkout does not match the pinned revision.

Run `python scripts/aggregate_skill.py` to generate `SKILL.md` and `skill-lock.json`. Run `python scripts/aggregate_skill.py --check` in CI to ensure the committed aggregate is reproducible.
