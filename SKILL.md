---
name: norm-skill
description: Norm language, CLI, standard-library, package, and registry guidance for Norm projects.
---

# Norm

This file is generated from the pinned components in `skill-manifest.json`.

## Component: language-cli

Source: `Norm-Skill local source`; revision: `self`.

<!-- component:language-cli -->
# Norm

Use the installed toolchain and the project's existing declarations to guide implementation. Read only the reference sections relevant to the task; follow their links when more detail is needed.

## CLI

Start with `norm --version` and `norm -h`. Read `norm <command> -h` for arguments, defaults and examples; for name refactoring use `norm refactor name -h`. Obtain CLI syntax from help rather than constructing input JSON or relying on remembered flags.

Use query to discover existing declarations and inspect the source, references, dependencies or associated tests needed for the change. Copy qualified names or overload selectors from results; resolve ambiguity before editing. Refactoring previews describe captured inputs and proposed edits: inspect the reported validation scope and whether files were written.

After editing, use check and the relevant tests. Read their help for machine output and test selection. Compilation, executed tests and native builds establish different facts; report the verification actually performed.

## Live runtime

Running source applications expose live update capability through the system runtime. This is an application capability, not an Agent constructor option and not an Agent library type. Acquire it explicitly when the application needs to inspect or publish source changes:

```norm
import std.system.currentSystem

var runtime = currentSystem().runtime()
```

Use `runtime.previewUpdate()` before publication when the caller needs to review the complete before/after declaration changes. Use `runtime.beginUpdate()` for a related group of source or dependency edits, call `preview()` when review is required, and call `commit()` to publish the batch. `runtime.publishUpdate()` is the direct publication form. A rejected or failed result leaves the running revision active and carries structured diagnostics; do not treat a file write as a successful runtime update.

Use `runtime.onUpdate` when the application needs transition notifications. The callback receives `RuntimeUpdateEvent` values such as `Requested`, `Published`, `Rejected`, `Failed`, `AdoptionPending`, and `Adopted`; close the returned subscription when the listener is no longer needed. Inspect `changes` for the declarations changed by a publication and use `before` and `after` from the preview or result for reviewable details.

Keep runtime wiring in the application layer. The basic Agent entry point should pass its instruction, `skills`, and `tools`; an application that lets an Agent request publication can expose a normal tool which calls the application-owned `Runtime`. Do not add `toolProvider`, `beginToolScope`, or `contextProvider` just to obtain runtime access. Read the [Runtime update design](https://github.com/normlanguage/Norm/blob/main/docs/zh/design/runtime-update-tool-261018.md), [`std.system`](https://github.com/normlanguage/Norm/tree/main/norm/stdlib/std/system), and [`std.runtime`](https://github.com/normlanguage/Norm/tree/main/norm/stdlib/std/runtime) for the authoritative declarations.

## Language rules

For a first Norm task, read the [Language Tour](https://normlanguage.github.io/Norm/learn/). Resolve exact syntax and semantics through the [Language Reference](https://normlanguage.github.io/Norm/spec/language-spec). Do not infer Norm behavior from Java or another familiar language.

Choose the reference that owns the question:

- Data modeling, identity, copying and aliases: [value, class and ref semantics](https://normlanguage.github.io/Norm/spec/value-identity-semantics).
- Parameters, argument labels and calls: [functions](https://normlanguage.github.io/Norm/learn/functions).
- Optional values and inference: [nullability and inference](https://normlanguage.github.io/Norm/learn/nullability-inference).
- Failure modeling and exceptions: [error handling](https://normlanguage.github.io/Norm/learn/errors).
- Source organization and dependencies: [packages and modules](https://normlanguage.github.io/Norm/learn/packages-modules) and [package manager](https://normlanguage.github.io/Norm/ecosystem/package-manager).

Check [Status](https://normlanguage.github.io/Norm/status) and [version contracts](https://normlanguage.github.io/Norm/versions/) when capability availability matters. Main-branch documentation may describe unreleased changes. In a Norm compiler checkout, prefer the matching local docs and executable examples; otherwise follow documentation for the installed version.

## Libraries and examples

- Discover standard APIs through the [standard library catalog](https://normlanguage.github.io/Norm/stdlib/overview) and [generated API browser](https://normlanguage.github.io/Norm/stdlib/api).
- Discover external modules through the [registry](https://github.com/normlanguage/registry); its [registry contract](https://normlanguage.github.io/Norm/ecosystem/registry) explains ownership and lookup. Follow each entry to its owning repository for actual APIs and versions.
- For a project's own public API, consult [API documentation export](https://normlanguage.github.io/Norm/tooling/api-documentation) and `norm docs -h`; query loaded declarations for precise signatures.
- Use the [executable example and test index](https://github.com/normlanguage/Norm/blob/main/norm/tests/README.md) to locate working patterns. The [testing API](https://normlanguage.github.io/Norm/stdlib/testing-api) owns test declarations and association rules.
- For packaging or Java-backed modules, read [application builds](https://normlanguage.github.io/Norm/tooling/application-build) or [Java adapters](https://normlanguage.github.io/Norm/design/java-library-adapters) as the task requires.

Keep API lists, language rules and command definitions in these owning sources. Extend application code using verified declarations rather than inventing APIs from names.
<!-- end-component:language-cli -->


## Component: norm-std

Source: `https://github.com/normlanguage/Norm-Std-Skill.git`; revision: `53124bf6c680c49ad007274e2b193fc0233f29c9`.

<!-- component:norm-std -->
# Norm Standard Library Skill

This skill describes the public `std` module shipped with Norm. It is generated from the Norm standard-library sources and their `@Document` annotations.

- Norm source revision: `291eb53b8b6afa3668522d5f6774f3f34f960cc7`
- Standard library module: `std` version `1`
- Source: https://github.com/normlanguage/Norm/tree/codex/skill-distribution/norm/stdlib/std
- API export command: `norm docs norm/stdlib/std --output build/std-api --skill SKILL.md --strict`

## Usage

Use the exact imports and signatures from the API documentation generated with this skill. Do not invent declarations. The `std` module is exported by package and source file, including `std.io`, `std.filesystem`, `std.process`, `std.application`, `std.cli`, `std.http`, `std.json`, `std.collections`, `std.text`, `std.time`, `std.validation`, `std.serialization`, `std.websocket`, and `std.yaml`.

## Capability index

### Application and CLI

- `std.application.arguments()` returns the application argument sequence.
- `std.application.environmentVariable(name:)` reads one environment variable.
- `std.application.applicationDirectory()` and `workingDirectory()` return application paths.
- `std.cli.CommandLine` declares options, parses arguments, and produces help text.

### Console and streams

- `std.io.print(text:)` writes standard output.
- `std.io.printError(text:)` writes standard error.
- `std.io.standardInput()` returns a `ByteReader`.
- `ByteReader.read(maximumBytes:)` returns `ReadChunk.Data` or `ReadChunk.Eof`.
- Input is a byte stream. A line-oriented caller must buffer chunks, decode UTF-8, and handle both LF and CRLF. `readAll` waits for EOF and is not an interactive line reader.

### Filesystem

- `std.filesystem.Path` represents a filesystem path.
- `std.filesystem.readText(path:, encoding:, maximumBytes:)` reads bounded text.
- `std.filesystem.writeTextAtomic(path:, text:, encoding:)` writes text atomically.
- `std.filesystem.openRead(path:)` and `openWrite(path:, mode:)` expose stream ownership.
- Directory enumeration is not part of the current `std.filesystem` surface. Do not call `std.filesystem.listDirectory` unless it is present in the installed API export.

### Processes

- `std.process.runProcess(executable:, arguments:, directory:, environment:, input:, timeout:, maximumOutputBytes:)` runs one executable with structured argument boundaries.
- The result exposes stdout, stderr, outcome, exit code, and truncation information.
- `std.process.run` is not a standard-library declaration.

### Data and protocols

Use the `std.json`, `std.yaml`, `std.xml`, `std.http`, and `std.websocket` packages only through their generated declarations and documented resource lifecycle. Prefer typed values and bounded operations.

## Source of truth

The Norm source files and `@Document` annotations are authoritative. This file is a generated distribution artifact. Regenerate it when the pinned Norm revision changes; do not hand-edit API signatures.
<!-- end-component:norm-std -->


## Component: package-standards

Source: `https://github.com/normlanguage/package-standards.git`; revision: `b8009530ecc3b5622c4c082d53cf5d06bd516f9b`.

<!-- component:package-standards -->
# Package Standards Skill

Use this skill when creating, reviewing, publishing, or consuming a Norm library repository.

## Source of truth

- `module.norm` is the only source for module name, version, dependencies, exports, and binding fingerprints.
- Public API facts come from Norm declarations and their `@Document` metadata. Do not duplicate API signatures in README or registry data.
- The standard is defined by [`docs/standard.zh-CN.md`](docs/standard.zh-CN.md). This file is an agent-oriented index of that standard.

## Repository contract

A publishable library repository owns one public Module. The repository name and Module name use the same lowercase dot-separated identity. `exports` contains only maintained public API. Internal bindings remain behind module visibility.

Required entry points:

- `README.md` and `README.zh-CN.md` for discovery and a verified quick start.
- `LICENSE` for the repository license.
- The module's single `module.norm` declaration.
- A runnable `samples/` consumer using the released package.
- Tests and build entry points that work from a clean checkout.

Do not publish aliases, implementation-only modules, duplicate type definitions, generated caches, credentials, or samples inside the runtime artifact.

## Skill publication

Every publishable library exposes a root `SKILL.md` at the repository root. It is generated from declarations, `@Document`, and verified samples through the repository's canonical generator. The generated file must be checked in and reproducible; CI must fail when regeneration changes it.

A library Skill should state:

- module name, supported Norm version, and immutable release URL;
- public packages, types, functions, fields, errors, and resource lifecycles;
- the smallest verified examples and their required dependencies;
- unsupported or unavailable capabilities when agents might otherwise guess them;
- links back to source/API documentation.

The Skill describes the library; it does not replace API declarations, `module.norm`, README, or Registry ownership data.

## Release and consumption

Release versions are positive integers. Version `N` is tag `vN`; tags and artifacts are immutable. A release must contain the package artifact, SHA-256 sidecar, license contract, and a consumer check from an empty cache. Dependencies resolve through the package manager and must not rely on sibling checkouts, absolute paths, or hidden caches.

Before publishing, verify the public API, module declaration, tests, samples, README commands, generated Skill, artifact checksum, license, and clean-cache consumer installation. Use the shared workflows from [`normlanguage/registry`](https://github.com/normlanguage/registry) instead of copying packaging logic.

## Agent workflow

When an API is missing, inspect the library source and generated documentation first. Add a dependency only through `module.norm`, then implement and verify a public tool or sample against the published contract. Never invent an import or function name from another language.
<!-- end-component:package-standards -->


## Component: registry

Source: `https://github.com/normlanguage/registry.git`; revision: `ab7dced7a37109af9bd1221d83b3f5720103a11c`.

<!-- component:registry -->
# Registry Skill

Use this skill when registering Norm modules, validating ownership, or consuming immutable package releases.

## Registry contract

`registry.json` is the single source for Module-to-GitHub ownership. Its schema is [`registry.schema.json`](registry.schema.json). Each entry has exactly `name`, `owner`, and `repository`.

The Registry does not copy module versions, dependencies, API signatures, Skill text, or release metadata. Those facts remain in the package repository and its `module.norm` declaration.

## Lookup and Skill URL

For a registered entry `{name, owner, repository}`, the canonical repository is:

```text
https://github.com/{owner}/{repository}
```

A released library Skill is discovered at the immutable tag URL:

```text
https://raw.githubusercontent.com/{owner}/{repository}/v{version}/SKILL.md
```

The `main` URL may be used for development inspection. Agents should use a version tag for reproducible work and must not infer a Skill URL for an unregistered module.

## Registering a module

1. Confirm the repository is public, maintained, and follows the Package Standards Skill.
2. Confirm its `module.norm` name matches the proposed registry name and its repository identity follows the package naming rules.
3. Add one ownership entry to `registry.json`.
4. Run the schema and duplicate/name validation used by the repository CI.
5. Open a pull request containing only the ownership change and supporting evidence.

Existing owners publish new versions in their package repositories. A registry change does not publish or overwrite an artifact.

## Releases and installation

Package repositories publish immutable `v<version>` tags and `<artifact>-<version>.nar` plus its SHA-256 sidecar. Use the shared workflows and actions in `.github/` for package, checksum, license, and consumer verification. Pass one explicit `norm-version` or immutable `norm-source-ref`; do not silently select a moving compiler revision.

A package consumer resolves the registry entry, downloads the immutable artifact, verifies the sidecar and module identity, and installs through the Norm package manager. A missing registry entry, mismatched module identity, changed tag, checksum failure, or missing license is a release error.

## Agent workflow

Use the Registry to discover ownership and the package repository to read API and Skill content. Never treat Registry data as an API catalog. When adding a dependency, record it in the consumer's `module.norm` and use the package manager; do not create a local dependency directory or copy generated Skill content into the consumer.
<!-- end-component:registry -->
