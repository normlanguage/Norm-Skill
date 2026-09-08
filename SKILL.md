---
name: norm-skill
description: Write, modify, refactor, and test Norm language applications using the Norm CLI, authoritative language rules, and existing library catalogs. Use for .norm source and Norm modules.
---

# Norm

Use the installed toolchain and the project's existing declarations to guide implementation. Read only the reference sections relevant to the task; follow their links when more detail is needed.

## CLI

Start with `norm --version` and `norm -h`. Read `norm <command> -h` for arguments, defaults and examples; for name refactoring use `norm refactor name -h`. Obtain CLI syntax from help rather than constructing input JSON or relying on remembered flags.

Use query to discover existing declarations and inspect the source, references, dependencies or associated tests needed for the change. Copy qualified names or overload selectors from results; resolve ambiguity before editing. Refactoring previews describe captured inputs and proposed edits: inspect the reported validation scope and whether files were written.

After editing, use check and the relevant tests. Read their help for machine output and test selection. Compilation, executed tests and native builds establish different facts; report the verification actually performed.

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
