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

Source: `https://github.com/normlanguage/Norm-Std-Skill.git`; revision: `54b5fad246a81197da3d38dc97b6533d05b7c1ed`.

<!-- component:norm-std -->
# Norm Standard Library Skill

Norm source revision: 741a0e1fdbfbc93c5b006d3971cb68fa4a55a1c6

Generated declarations and signatures follow below. Source indexes:

- [std.application.providers](https://github.com/normlanguage/Norm/blob/741a0e1fdbfbc93c5b006d3971cb68fa4a55a1c6/norm/stdlib/std/application/application.norm)
- [std.logging.logInfo](https://github.com/normlanguage/Norm/blob/741a0e1fdbfbc93c5b006d3971cb68fa4a55a1c6/norm/stdlib/std/logging/log.norm)
- [std.filesystem.readText](https://github.com/normlanguage/Norm/blob/741a0e1fdbfbc93c5b006d3971cb68fa4a55a1c6/norm/stdlib/std/filesystem/files.norm)
- [std.process.runProcess](https://github.com/normlanguage/Norm/blob/741a0e1fdbfbc93c5b006d3971cb68fa4a55a1c6/norm/stdlib/std/process/process.norm)

# std Skill

Use this skill to work with Norm module `std` version 1. Use only declarations listed below.

## `std.annotation`

Source: `annotation/protocols.norm`

Defines annotation targets, retention policies, interceptors, and structured documentation metadata.

### `AnnotationTarget`

Marks an interface as an annotation policy rather than an ordinary application interface.

```norm
interface AnnotationTarget
```

### `PackageTarget`

Allows an annotation to target a package declaration.

```norm
interface PackageTarget extends AnnotationTarget
```

### `TypeTarget`

Allows an annotation to target a class, value, interface, enum, or annotation declaration.

```norm
interface TypeTarget extends AnnotationTarget
```

### `ManagedImplementation`

Marks types whose implementation is supplied by a managed runtime.

```norm
interface ManagedImplementation extends TypeTarget
```

### `FieldTarget`

Allows an annotation to target a stored field declaration.

```norm
interface FieldTarget extends AnnotationTarget
```

### `ManagedField`

Marks fields whose storage is supplied by a managed runtime.

```norm
interface ManagedField extends FieldTarget
```

### `FieldInterceptor`

Intercepts writes to fields whose declared value type is T.

```norm
interface FieldInterceptor<T> extends FieldTarget
```

Type parameters:

- `T`

#### `before`

Transforms or validates a field value before it is stored.

```norm
T before(FieldContext context, T value)
```

Parameters:

- `context`: `FieldContext`
Identifies the field declaration receiving the value.

- `value`: `T`
The value proposed for storage.


Returns: `T`

#### `after`

Observes completion after a field write has entered the interceptor.

```norm
Void after(FieldContext context, FunctionCompletion completion)
```

Parameters:

- `context`: `FieldContext`
Identifies the field declaration that received the value.

- `completion`: `FunctionCompletion`
Describes whether the intercepted write completed successfully.


Returns: `Void`

### `ConstructorTarget`

Allows an annotation to target an explicit constructor declaration.

```norm
interface ConstructorTarget extends AnnotationTarget
```

### `FunctionTarget`

Allows an annotation to target a function, method, extension, or interface requirement.

```norm
interface FunctionTarget extends AnnotationTarget
```

### `FunctionInterceptor`

Intercepts concrete function and method invocations.

```norm
interface FunctionInterceptor extends FunctionTarget
```

#### `before`

Runs before entering an intercepted function invocation.

```norm
Void before(FunctionContext context)
```

Parameters:

- `context`: `FunctionContext`
Identifies the intercepted function declaration.


Returns: `Void`

#### `around`

Controls whether and when the intercepted invocation proceeds.

```norm
R around<R>(FunctionInvocation<R> invocation)
```

Type parameters:

- `R`

Parameters:

- `invocation`: `FunctionInvocation<R>`
Provides the single-use continuation for the intercepted invocation.


Returns: `R`

#### `after`

Observes completion after an invocation has entered the interceptor.

```norm
Void after(FunctionContext context, FunctionCompletion completion)
```

Parameters:

- `context`: `FunctionContext`
Identifies the intercepted function declaration.

- `completion`: `FunctionCompletion`
Describes whether the intercepted invocation completed successfully.


Returns: `Void`

### `ParameterTarget`

Allows an annotation to target a callable parameter declaration.

```norm
interface ParameterTarget extends AnnotationTarget
```

### `ParameterInterceptor`

Intercepts arguments bound to parameters whose declared value type is T.

```norm
interface ParameterInterceptor<T> extends ParameterTarget
```

Type parameters:

- `T`

#### `before`

Transforms or validates an argument before parameter binding.

```norm
T before(ParameterContext context, T value)
```

Parameters:

- `context`: `ParameterContext`
Identifies the parameter declaration receiving the argument.

- `value`: `T`
The argument proposed for parameter binding.


Returns: `T`

#### `after`

Observes completion after a parameter binding has entered the interceptor.

```norm
Void after(ParameterContext context, FunctionCompletion completion)
```

Parameters:

- `context`: `ParameterContext`
Identifies the intercepted parameter declaration.

- `completion`: `FunctionCompletion`
Describes whether the containing invocation completed successfully.


Returns: `Void`

### `LocalTarget`

Allows an annotation to target a local variable declaration.

```norm
interface LocalTarget extends AnnotationTarget
```

### `AnnotationRetention`

Marks an interface as an annotation retention policy.

```norm
interface AnnotationRetention
```

### `SourceRetention`

Retains annotation behavior during compilation without storing general metadata.

```norm
interface SourceRetention extends AnnotationRetention
```

### `BinaryRetention`

Stores annotation metadata in compiled Core artifacts without runtime reflection access.

```norm
interface BinaryRetention extends AnnotationRetention
```

### `RuntimeRetention`

Stores annotation metadata in Core artifacts and exposes it through runtime reflection.

```norm
interface RuntimeRetention extends AnnotationRetention
```

### `RepeatableAnnotation`

Allows multiple applications of the same annotation on one declaration.

```norm
interface RepeatableAnnotation
```

### `InheritedAnnotation`

Makes type annotation lookup include annotations inherited from parent classes.

```norm
interface InheritedAnnotation
```

### `Document`

Attaches structured prose and declaration relationships directly to a code declaration.

```norm
annotation Document implements PackageTarget, TypeTarget, FieldTarget, ConstructorTarget, FunctionTarget, ParameterTarget, LocalTarget, BinaryRetention
```

#### `description`

The canonical prose description of the annotated declaration.

```norm
String description
```

Type: `String`

#### `types`

Related type declarations in presentation order, or null when none are specified.

```norm
List<Class<?>>? types
```

Type: `List<Class<?>>?`

#### `functions`

Related function declarations in presentation order, or null when none are specified.

```norm
List<Function<?>>? functions
```

Type: `List<Function<?>>?`

#### `fields`

Related field declarations in presentation order, or null when none are specified.

```norm
List<Field<?, ?>>? fields
```

Type: `List<Field<?, ?>>?`

### `IdentityField`

Marks fields that participate in managed identity.

```norm
interface IdentityField extends FieldTarget
```

## `std.application`

Source: `application/application.norm`

Defines the standard application lifecycle contract.

### `Application`

Runs an application and owns its lifetime until completion or cancellation.

```norm
interface Application
```

#### `run`

Starts the application and blocks until its lifetime ends.

```norm
Void run()
```

Returns: `Void`

### `applicationPackage`

Returns the package used to expose this application to host frameworks.

```norm
String applicationPackage()
```

Returns: `String`

### `applicationDirectory`

Returns the deployed executable directory, or the entry source directory during source execution.

```norm
Path applicationDirectory()
```

Returns: `Path`

### `arguments`

Returns this invocation's application arguments with their original boundaries.

```norm
List<String> arguments()
```

Returns: `List<String>`

### `environmentVariable`

Reads a variable from this execution's environment; missing variables return null.

```norm
String? environmentVariable(String name)
```

Parameters:

- `name`: `String`
The environment variable name.


Returns: `String?`

### `workingDirectory`

Returns the current execution's working directory, independently of the application directory.

```norm
Path workingDirectory()
```

Returns: `Path`

### `setExitCode`

Sets the application completion code; execution continues and the host exits after cleanup.

```norm
Void setExitCode(Integer code)
```

Parameters:

- `code`: `Integer`
The portable completion code in 0..255.


Returns: `Void`

### `Provider`

Creates one discovered application service implementation.

```norm
interface Provider<T>
```

Type parameters:

- `T`

#### `name`

Returns the qualified name of the implementation.

```norm
String name()
```

Returns: `String`

#### `create`

Creates a new instance of the implementation.

```norm
T create()
```

Returns: `T`

### `providers`

Returns the public implementations of an application service interface.

```norm
List<Provider<T>> providers<T>()
```

Type parameters:

- `T`

Returns: `List<Provider<T>>`

## `std.build`

Source: `build/builders.norm`

Defines typed result builders for block expressions.

### `BuildWith`

Selects the result builder for an annotated block parameter.

```norm
annotation BuildWith implements ParameterTarget, BinaryRetention
```

#### `value`

The result builder type.

```norm
Class<?> value
```

Type: `Class<?>`

### `ResultBuilder`

Accumulates block elements into a typed result.

```norm
interface ResultBuilder<Element, Result>
```

Type parameters:

- `Element`
- `Result`

#### `add`

Adds an element to the result.

```norm
Void add(Element value)
```

Parameters:

- `value`: `Element`
The element to add.


Returns: `Void`

#### `finish`

Returns the completed result.

```norm
Result finish()
```

Returns: `Result`

## `std.cli`

Source: `cli/arguments.norm`

Parses explicit command-line options while preserving argument boundaries.

### `OptionKind`

Selects a flag or an option that consumes one value.

```norm
enum OptionKind
```

#### `Flag`

```norm
Flag
```

#### `Value`

```norm
Value
```

### `CliFailure`

Identifies invalid definitions and command-line input problems.

```norm
enum CliFailure
```

#### `InvalidDefinition`

```norm
InvalidDefinition
```

#### `UnknownOption`

```norm
UnknownOption
```

#### `MissingValue`

```norm
MissingValue
```

#### `DuplicateOption`

```norm
DuplicateOption
```

#### `UnexpectedValue`

```norm
UnexpectedValue
```

### `CliException`

Reports a command-line problem with its option and stable code.

```norm
class CliException extends Exception
```

#### `code`

The stable machine-readable problem code.

```norm
String code
```

Type: `String`

#### `reason`

The command-line failure category.

```norm
CliFailure reason
```

Type: `CliFailure`

#### `option`

The offending option name.

```norm
String option
```

Type: `String`

#### `CliException`

Creates a command-line input failure.

```norm
CliException(CliFailure reason, String option)
```

Parameters:

- `reason`: `CliFailure`
The failure category.

- `option`: `String`
The offending option.


### `Option`

Declares one unique long option, its help text and value requirement.

```norm
value Option
```

#### `name`

The command or option name; option names exclude leading dashes.

```norm
String name
```

Type: `String`

#### `description`

The description displayed in generated help.

```norm
String description
```

Type: `String`

#### `kind`

Whether the option consumes a value.

```norm
OptionKind kind
```

Type: `OptionKind`

### `Arguments`

Contains parsed options and the unchanged positional argument sequence.

```norm
value Arguments
```

#### `options`

Parsed option values; flags have an empty value.

```norm
Map<String, String> options
```

Type: `Map<String, String>`

#### `positionals`

Positional arguments in their original order.

```norm
List<String> positionals
```

Type: `List<String>`

#### `has`

Reports whether an option was explicitly supplied.

```norm
Boolean has(String name)
```

Parameters:

- `name`: `String`
The option name.


Returns: `Boolean`

#### `value`

Returns a supplied option value or null when absent.

```norm
String? value(String name)
```

Parameters:

- `name`: `String`
The option name.


Returns: `String?`

### `CommandLine`

Owns validated option definitions, parsing and derived help text.

```norm
class CommandLine
```

#### `name`

The command or option name; option names exclude leading dashes.

```norm
String name
```

Type: `String`

#### `description`

The description displayed in generated help.

```norm
String description
```

Type: `String`

#### `CommandLine`

Validates and stores a command definition.

```norm
CommandLine(String name, String description, List<Option> options)
```

Parameters:

- `name`: `String`
The command name.

- `description`: `String`
The command description.

- `options`: `List<Option>`
Unique long option definitions.


#### `parse`

Parses options, honoring -- and optionally stopping at the first positional argument.

```norm
Arguments parse(List<String> arguments, Boolean stopAtPositional)
```

Parameters:

- `arguments`: `List<String>`
The unmodified application argument array.

- `stopAtPositional`: `Boolean`
Whether the first positional argument ends option parsing.


Returns: `Arguments`

#### `help`

Builds usage text from this command and its option definitions.

```norm
String help()
```

Returns: `String`

## `std.collections`

Source: `collections/mutable.norm`

### `mutableMap`

Creates an insertion-ordered Java map with shared identity.

```norm
JavaMap<K, V> mutableMap<K, V>()
```

Type parameters:

- `K`
- `V`

Returns: `JavaMap<K, V>`

## `std.collections`

Source: `collections/sequences.norm`

Provides reusable operations for List and Array sequences.

### `listContains`

Reports whether a list contains a value equal to the target.

```norm
Boolean listContains<T>(List<T> values, T target)
```

Type parameters:

- `T`

Parameters:

- `values`: `List<T>`
The list to search.

- `target`: `T`
The value to find.


Returns: `Boolean`

Related tests:

- `std.test.collections.collections::collectionsTest()` — collectionsTest
  tests/test/collections/collections/case.api.json
- `std.test.integration.edge_cases::edgeCasesTest()` — edgeCasesTest
  tests/test/integration/edge_cases/case.api.json

### `listCount`

Counts values in a list that are equal to the target.

```norm
Integer listCount<T>(List<T> values, T target)
```

Type parameters:

- `T`

Parameters:

- `values`: `List<T>`
The list to search.

- `target`: `T`
The value to count.


Returns: `Integer`

Related tests:

- `std.test.collections.collections::collectionsTest()` — collectionsTest
  tests/test/collections/collections/case.api.json
- `std.test.integration.edge_cases::edgeCasesTest()` — edgeCasesTest
  tests/test/integration/edge_cases/case.api.json

### `toList`

Copies an array into a mutable list while preserving order.

```norm
List<T> toList<T>(Array<T> values)
```

Type parameters:

- `T`

Parameters:

- `values`: `Array<T>`
The array whose values are copied.


Returns: `List<T>`

### `toList`

Copies a Java list into an independent mutable list, preserving order and nullable elements.

```norm
List<T?> toList<T>(JavaList<T> values)
```

Type parameters:

- `T`

Parameters:

- `values`: `JavaList<T>`
The Java list whose values are copied.


Returns: `List<T?>`

### `sort`

Returns the integer list values in ascending numeric order.

```norm
List<Integer> sort(List<Integer> values)
```

Parameters:

- `values`: `List<Integer>`
The integer list to sort.


Returns: `List<Integer>`

### `sort`

Returns the integer array values in ascending numeric order.

```norm
Array<Integer> sort(Array<Integer> values)
```

Parameters:

- `values`: `Array<Integer>`
The integer array to sort.


Returns: `Array<Integer>`

### `sort`

Returns the code point list values in ascending scalar-value order.

```norm
List<CodePoint> sort(List<CodePoint> values)
```

Parameters:

- `values`: `List<CodePoint>`
The code point list to sort.


Returns: `List<CodePoint>`

### `sort`

Returns the code point array values in ascending scalar-value order.

```norm
Array<CodePoint> sort(Array<CodePoint> values)
```

Parameters:

- `values`: `Array<CodePoint>`
The code point array to sort.


Returns: `Array<CodePoint>`

### `sort`

Returns the string list values in ascending code point order.

```norm
List<String> sort(List<String> values)
```

Parameters:

- `values`: `List<String>`
The string list to sort.


Returns: `List<String>`

### `sort`

Returns the string array values in ascending code point order.

```norm
Array<String> sort(Array<String> values)
```

Parameters:

- `values`: `Array<String>`
The string array to sort.


Returns: `Array<String>`

## `std.concurrent`

Source: `concurrent/completion.norm`

### `completion`

Creates an owned task source completed by external events.

```norm
Completion<T> completion<T>()
```

Type parameters:

- `T`

Returns: `Completion<T>`

### `Completion`

Completes typed tasks once with a result or failure; closing cancels pending tasks.

```norm
class Completion<T> implements Resource
```

Type parameters:

- `T`

#### `task`

Returns a task sharing this source; cancelling the task cancels the source.

```norm
Task<T> task()
```

Returns: `Task<T>`

#### `succeed`

Completes this source successfully and reports whether it was still pending.

```norm
Boolean succeed(T value)
```

Parameters:

- `value`: `T`
The successful result.


Returns: `Boolean`

#### `fail`

Fails this source and reports whether it was still pending.

```norm
Boolean fail(Exception error)
```

Parameters:

- `error`: `Exception`
The failure delivered to task consumers.


Returns: `Boolean`

#### `close`

Cancels this source if pending and releases its resource ownership.

```norm
Void close()
```

Returns: `Void`

## `std.concurrent`

Source: `concurrent/delay.norm`

### `delay`

Suspends the current task for a nonnegative duration, responding to cancellation.

```norm
Void delay(Duration duration)
```

Parameters:

- `duration`: `Duration`
The duration to wait; zero returns immediately.


Returns: `Void`

## `std.concurrent`

Source: `concurrent/java.norm`

### `completionFuture`

Projects task completion into a Java future without a result; cancellation propagates in both directions and failure retains its cause.

```norm
CompletableFuture<JavaVoid> completionFuture<T>(Task<T> task)
```

Type parameters:

- `T`

Parameters:

- `task`: `Task<T>`
The task whose completion is projected to the Java future.


Returns: `CompletableFuture<JavaVoid>`

### `fromCompletionStage`

Adapts Java completion without blocking, preserving nullable results and failure causes; task cancellation cancels the Java future and the current resource owner owns the task.

```norm
Task<T?> fromCompletionStage<T>(CompletionStage<T> stage, TaskExecutor? executor)
```

Type parameters:

- `T`

Parameters:

- `stage`: `CompletionStage<T>`
The Java completion to adapt.

- `executor`: `TaskExecutor?`
Optional scheduler for task callbacks and unhandled failures.


Returns: `Task<T?>`

## `std.concurrent`

Source: `concurrent/lifecycle.norm`

### `awaitCancellation`

Waits until the current execution is cancelled or interrupted.

```norm
Void awaitCancellation()
```

Returns: `Void`

## `std.concurrent`

Source: `concurrent/publishers.norm`

### `Publisher`

Represents a backpressured sequence published asynchronously.

```norm
interface Publisher<T>
```

Type parameters:

- `T`

## `std.concurrent`

Source: `concurrent/tasks.norm`

Provides typed tasks with deterministic waiting, cancellation, and resource ownership.

### `TaskScope`

Owns tasks started within the current execution scope.

```norm
interface TaskScope
```

#### `start`

Starts typed work using this scope.

```norm
Task<T> start<T>(Function<T()> work)
```

Type parameters:

- `T`

Parameters:

- `work`: `Function<T()>`
The computation to start.


Returns: `Task<T>`

### `async`

Starts work in the current task scope, preserving its scheduling and resource ownership.

```norm
Task<T> async<T>(Function<T()> work)
```

Type parameters:

- `T`

Parameters:

- `work`: `Function<T()>`
The computation to run.


Returns: `Task<T>`

### `async`

Starts work without a result in the current task scope.

```norm
Task<Unit> async(Function<Void()> work)
```

Parameters:

- `work`: `Function<Void()>`
The action to run.


Returns: `Task<Unit>`

### `startTask`

Starts typed work on a virtual thread and returns its owned task immediately.

```norm
Task<T> startTask<T>(Function<T()> work, TaskExecutor? executor)
```

Type parameters:

- `T`

Parameters:

- `work`: `Function<T()>`
The computation to run.

- `executor`: `TaskExecutor?`
Optional scheduler for task callbacks and unhandled failures.


Returns: `Task<T>`

### `startTask`

Starts work without a result on a virtual thread.

```norm
Task<Unit> startTask(Function<Void()> work, TaskExecutor? executor)
```

Parameters:

- `work`: `Function<Void()>`
The action to run.

- `executor`: `TaskExecutor?`
Optional scheduler for task callbacks and unhandled failures.


Returns: `Task<Unit>`

### `TaskExecutor`

Schedules task callbacks and handles unhandled failures.

```norm
interface TaskExecutor
```

#### `dispatch`

Schedules an action for execution.

```norm
Void dispatch(Function<Void()> action)
```

Parameters:

- `action`: `Function<Void()>`
The action to schedule.


Returns: `Void`

#### `report`

Handles an unobserved task failure.

```norm
Void report(Exception error)
```

Parameters:

- `error`: `Exception`
The unhandled failure.


Returns: `Void`

### `Task`

Represents a typed operation whose result may become available later.

```norm
class Task<T> implements Resource
```

Type parameters:

- `T`

#### `termination`

Returns a task that completes when termination finishes, or null if no wait is needed.

```norm
Task<Unit>? termination()
```

Returns: `Task<Unit>?`

#### `then`

Transforms a successful result in a continuation task.

```norm
Task<R> then<R>(R completed(T result))
```

Type parameters:

- `R`

Parameters:

- `completed`: `Function<R(T)>`
The transformation applied to the result.


Returns: `Task<R>`

#### `then`

Runs an action after successful completion.

```norm
Task<Unit> then(Void completed(T result))
```

Parameters:

- `completed`: `Function<Void(T)>`
The action applied to the result.


Returns: `Task<Unit>`

#### `error`

Recovers a failed task with a replacement result.

```norm
Task<T> error(T failed(Exception failure))
```

Parameters:

- `failed`: `Function<T(Exception)>`
The recovery function.


Returns: `Task<T>`

#### `error`

Observes task failure in a continuation.

```norm
Task<Unit> error(Void failed(Exception failure))
```

Parameters:

- `failed`: `Function<Void(Exception)>`
The failure handler.


Returns: `Task<Unit>`

#### `await`

Waits for completion and returns the task result.

```norm
T await()
```

Returns: `T`

#### `cancel`

Requests cancellation and reports whether the task was cancelled.

```norm
Boolean cancel()
```

Returns: `Boolean`

#### `completed`

Reports whether the task has completed, failed, or been cancelled.

```norm
Boolean completed()
```

Returns: `Boolean`

#### `close`

Releases task ownership and cancels unfinished work.

```norm
Void close()
```

Returns: `Void`

## `std.configuration`

Source: `configuration/configuration.norm`

Maps typed Norm values to flat framework configuration properties.

### `ConfigurationKey`

Uses a field as the property-path segment for elements in a named configuration collection.

```norm
annotation ConfigurationKey implements FieldTarget, RuntimeRetention
```

Related tests:

- `std.test.configuration.properties::propertiesTest()` — propertiesTest
  tests/test/configuration/properties/case.api.json

### `ConfigurationValue`

Uses a field as the scalar representation of its enclosing configuration value.

```norm
annotation ConfigurationValue implements FieldTarget, RuntimeRetention
```

Related tests:

- `std.test.configuration.properties::propertiesTest()` — propertiesTest
  tests/test/configuration/properties/case.api.json

### `configurationProperties`

Flattens a serializable typed value into insertion-ordered host configuration properties.

```norm
JavaMap<String, Any> configurationProperties<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The serializable configuration value to flatten.


Returns: `JavaMap<String, Any>`

Related tests:

- `std.test.configuration.properties::propertiesTest()` — propertiesTest
  tests/test/configuration/properties/case.api.json

## `std.context`

Source: `context/context.norm`

Provides typed context values scoped to an execution.

### `currentContext`

Returns the current value for a context type, or null when absent.

```norm
T? currentContext<T>()
```

Type parameters:

- `T`

Returns: `T?`

### `withContext`

Runs a computation with a context value and restores the previous context afterward.

```norm
R withContext<T, R>(T value, Function<R()> action)
```

Type parameters:

- `T`
- `R`

Parameters:

- `value`: `T`
The scoped context value.

- `action`: `Function<R()>`
The computation to run.


Returns: `R`

### `withContext`

Runs an action with a context value and restores the previous context afterward.

```norm
Void withContext<T>(T value, Function<Void()> action)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The scoped context value.

- `action`: `Function<Void()>`
The action to run.


Returns: `Void`

## `std.core`

Source: `core/exception.norm`

Provides the root exception type and foundational protocols and result values.

### `Exception`

Represents a recoverable failure with a human-readable message.

```norm
class Exception
```

#### `message`

The human-readable explanation of the failure.

```norm
String message
```

Type: `String`

#### `Exception`

Creates an exception with the supplied failure message.

```norm
Exception(String message)
```

Parameters:

- `message`: `String`
The human-readable explanation of the failure.


## `std.core`

Source: `core/protocols.norm`

### `Iterator`

Traverses a sequence of values of type T.

```norm
interface Iterator<T>
```

Type parameters:

- `T`

Related tests:

- `std.test.io.output_lines::outputLinesTest()` — outputLinesTest
  tests/test/io/output_lines/case.api.json

#### `hasNext`

Reports whether another value can be read from the iterator.

```norm
Boolean hasNext()
```

Returns: `Boolean`

#### `next`

Returns the next value and advances the iterator.

```norm
T next()
```

Returns: `T`

### `Iterable`

Produces an iterator over values of type T.

```norm
interface Iterable<T>
```

Type parameters:

- `T`

Related tests:

- `std.test.io.output_lines::outputLinesTest()` — outputLinesTest
  tests/test/io/output_lines/case.api.json

#### `iterator`

Creates an iterator positioned before the first value.

```norm
Iterator<T> iterator()
```

Returns: `Iterator<T>`

#### `map`

Transforms every value in iteration order and returns the collected results.

```norm
List<R> map<R>(R transform(T value))
```

Type parameters:

- `R`

Parameters:

- `transform`: `Function<R(T)>`
The transformation applied once to each source value.


Returns: `List<R>`

### `Sized`

Exposes the number of values held by an object.

```norm
interface Sized
```

Related tests:

- `std.test.core.protocols::protocolsTest()` — protocolsTest
  tests/test/core/protocols/case.api.json

#### `size`

Returns the number of contained values.

```norm
Integer size()
```

Returns: `Integer`

### `Comparable`

Defines a total ordering comparison against values of type T.

```norm
interface Comparable<T>
```

Type parameters:

- `T`

Related tests:

- `std.test.core.protocols::protocolsTest()` — protocolsTest
  tests/test/core/protocols/case.api.json

#### `compareTo`

Returns a negative, zero, or positive integer when this value is less than, equal to, or greater than the other value.

```norm
Integer compareTo(T other)
```

Parameters:

- `other`: `T`
The value to compare against.


Returns: `Integer`

### `Equatable`

Defines semantic equality against values of type T.

```norm
interface Equatable<T>
```

Type parameters:

- `T`

#### `equals`

Reports whether this value is semantically equal to the other value.

```norm
Boolean equals(T other)
```

Parameters:

- `other`: `T`
The value to compare for equality.


Returns: `Boolean`

### `Hashable`

Produces a stable integer hash compatible with semantic equality.

```norm
interface Hashable
```

#### `hash`

Returns the hash value of this object.

```norm
Integer hash()
```

Returns: `Integer`

### `Stringable`

Provides a human-readable string representation.

```norm
interface Stringable
```

#### `toString`

Returns the string representation of this object.

```norm
String toString()
```

Returns: `String`

## `std.core`

Source: `core/result.norm`

### `Result`

Represents either a successful value of type T or an error value of type E, with an optional message.

```norm
enum Result<T, E = String>
```

Type parameters:

- `T`
- `E` = `String`

Related tests:

- `std.test.core.result::resultTest()` — resultTest
  tests/test/core/result/case.api.json

#### `Ok`

```norm
Ok(T value, String msg)
```

Parameters:

- `value`: `T`
- `msg`: `String`

#### `Err`

```norm
Err(E error, String msg)
```

Parameters:

- `error`: `E`
- `msg`: `String`

## `std.core`

Source: `core/unit.norm`

### `Unit`

Represents a single meaningful value when no additional data is required.

```norm
enum Unit
```

Related tests:

- `std.test.core.result::resultTest()` — resultTest
  tests/test/core/result/case.api.json

#### `Value`

```norm
Value
```

## `std.filesystem`

Source: `filesystem/files.norm`

Provides typed filesystem paths, readers, writers, synchronization, and bounded text reads.

### `Path`

Represents a filesystem path string interpreted by the host platform.

```norm
value Path
```

Related tests:

- `std.test.filesystem.file_read_text::fileReadTextTest()` — fileReadTextTest
  tests/test/filesystem/file_read_text/case.api.json

#### `value`

The path text passed to the host filesystem.

```norm
String value
```

Type: `String`

### `FileOperation`

Identifies filesystem operations that can fail.

```norm
enum FileOperation
```

#### `OpenRead`

```norm
OpenRead
```

#### `OpenWrite`

```norm
OpenWrite
```

#### `Read`

```norm
Read
```

#### `Write`

```norm
Write
```

#### `Flush`

```norm
Flush
```

#### `Sync`

```norm
Sync
```

#### `Close`

```norm
Close
```

### `FileFailure`

Classifies filesystem lookup, permission, existence, path, closure, and I/O failures.

```norm
enum FileFailure
```

#### `NotFound`

```norm
NotFound
```

#### `PermissionDenied`

```norm
PermissionDenied
```

#### `AlreadyExists`

```norm
AlreadyExists
```

#### `InvalidPath`

```norm
InvalidPath
```

#### `Closed`

```norm
Closed
```

#### `Io`

```norm
Io
```

### `FileWriteMode`

Selects creation, replacement, or append behavior when opening a file for writing.

```norm
enum FileWriteMode
```

#### `CreateNew`

```norm
CreateNew
```

#### `Replace`

```norm
Replace
```

#### `Append`

```norm
Append
```

### `FileSyncMode`

Selects data-only or data-and-metadata durability for filesystem synchronization.

```norm
enum FileSyncMode
```

#### `Data`

```norm
Data
```

#### `DataAndMetadata`

```norm
DataAndMetadata
```

### `FileException`

Reports a typed filesystem failure for a specific operation and path.

```norm
class FileException extends IOException
```

#### `operation`

The filesystem operation that failed.

```norm
FileOperation operation
```

Type: `FileOperation`

#### `reason`

The filesystem failure category.

```norm
FileFailure reason
```

Type: `FileFailure`

#### `path`

The path associated with the failure.

```norm
Path path
```

Type: `Path`

#### `FileException`

Creates a typed filesystem failure.

```norm
FileException(String code, String message, FileOperation operation, FileFailure reason, Path path)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `operation`: `FileOperation`
The filesystem operation that failed.

- `reason`: `FileFailure`
The filesystem failure category.

- `path`: `Path`
The path associated with the failure.


### `FileReader`

Reads byte chunks from an open file and owns its file handle.

```norm
interface FileReader extends ByteReader, Resource
```

### `FileWriter`

Writes bytes to an open file, supports flushing and synchronization, and owns its file handle.

```norm
interface FileWriter extends ByteWriter, Flushable, Resource
```

#### `sync`

Synchronizes written file content according to the selected durability mode.

```norm
Void sync(FileSyncMode mode)
```

Parameters:

- `mode`: `FileSyncMode`
The durability mode requested from the host filesystem.


Returns: `Void`

### `openRead`

Opens a file for sequential byte reads.

```norm
FileReader openRead(Path path)
```

Parameters:

- `path`: `Path`
The path of the file to open.


Returns: `FileReader`

### `openWrite`

Opens a file for byte writes using the selected creation behavior.

```norm
FileWriter openWrite(Path path, FileWriteMode mode)
```

Parameters:

- `path`: `Path`
The path of the file to open.

- `mode`: `FileWriteMode`
The creation, replacement, or append behavior.


Returns: `FileWriter`

### `readText`

Reads, bounds, decodes, and closes a text file in one operation.

```norm
String readText(Path path, TextEncoding encoding, Integer maximumBytes)
```

Parameters:

- `path`: `Path`
The path of the text file to read.

- `encoding`: `TextEncoding`
The encoding used to decode the file bytes.

- `maximumBytes`: `Integer`
The maximum number of file bytes accepted.


Returns: `String`

Related tests:

- `std.test.filesystem.file_read_text::fileReadTextTest()` — fileReadTextTest
  tests/test/filesystem/file_read_text/case.api.json

### `writeTextAtomic`

Creates parent directories and atomically replaces a text file after writing and syncing a sibling temporary file; unsupported atomic moves fail without replacing the target.

```norm
Void writeTextAtomic(Path path, String text, TextEncoding encoding)
```

Parameters:

- `path`: `Path`
The destination file path.

- `text`: `String`
The complete text to publish.

- `encoding`: `TextEncoding`
The encoding used for the file bytes.


Returns: `Void`

## `std.http`

Source: `http/client.norm`

Provides typed HTTP requests, responses, clients, headers, status values, and transport failures.

### `Uri`

Stores an absolute or relative URI string accepted by the HTTP transport.

```norm
value Uri
```

Related tests:

- `std.test.http.json_request::jsonRequestTest()` — jsonRequestTest
  tests/test/http/json_request/case.api.json

#### `value`

The URI text passed to the transport.

```norm
String value
```

Type: `String`

### `HttpMethod`

Selects an HTTP request method: GET, HEAD, POST, PUT, PATCH, DELETE, or OPTIONS.

```norm
enum HttpMethod
```

#### `Get`

```norm
Get
```

#### `Head`

```norm
Head
```

#### `Post`

```norm
Post
```

#### `Put`

```norm
Put
```

#### `Patch`

```norm
Patch
```

#### `Delete`

```norm
Delete
```

#### `Options`

```norm
Options
```

### `HttpHeader`

Represents one HTTP header name and value pair.

```norm
value HttpHeader
```

#### `name`

The case-insensitive HTTP header name.

```norm
String name
```

Type: `String`

#### `value`

The HTTP header value.

```norm
String value
```

Type: `String`

### `HeaderMap`

Preserves an ordered collection of HTTP headers, including repeated names.

```norm
value HeaderMap
```

#### `values`

The headers in transport order.

```norm
Array<HttpHeader> values
```

Type: `Array<HttpHeader>`

#### `HeaderMap`

Constructs headers from ordered typed entries.

```norm
HeaderMap(Array<HttpHeader> values)
```

Parameters:

- `values`: `Array<HttpHeader>`
The ordered header entries.


#### `HeaderMap`

Constructs headers from field lines or alternating names and values.

```norm
HeaderMap(Array<String> entries)
```

Parameters:

- `entries`: `Array<String>`
The ordered field lines or alternating names and values.


#### `HeaderMap`

Constructs a single header.

```norm
HeaderMap(String k1, String v1)
```

Parameters:

- `k1`: `String`
The header name.

- `v1`: `String`
The header value.


#### `HeaderMap`

Constructs two ordered headers.

```norm
HeaderMap(String k1, String v1, String k2, String v2)
```

Parameters:

- `k1`: `String`
The first header name.

- `v1`: `String`
The first header value.

- `k2`: `String`
The second header name.

- `v2`: `String`
The second header value.


### `Status`

Represents a numeric HTTP response status code.

```norm
value Status
```

#### `code`

The three-digit HTTP status code.

```norm
Integer code
```

Type: `Integer`

### `HttpRequest`

Describes an HTTP request before it is sent by a client.

```norm
value HttpRequest
```

Related tests:

- `std.test.http.json_request::jsonRequestTest()` — jsonRequestTest
  tests/test/http/json_request/case.api.json

#### `method`

The HTTP request method.

```norm
HttpMethod method
```

Type: `HttpMethod`

#### `uri`

The request target URI.

```norm
Uri uri
```

Type: `Uri`

#### `headers`

The ordered request headers.

```norm
HeaderMap headers
```

Type: `HeaderMap`

#### `body`

The optional request body bytes.

```norm
Bytes? body
```

Type: `Bytes?`

### `HttpOperation`

Identifies whether an HTTP failure occurred while sending, reading, or closing.

```norm
enum HttpOperation
```

#### `Send`

```norm
Send
```

#### `Read`

```norm
Read
```

#### `Close`

```norm
Close
```

### `HttpFailure`

Classifies HTTP request, connection, timeout, cancellation, TLS, protocol, closure, and I/O failures.

```norm
enum HttpFailure
```

#### `InvalidRequest`

```norm
InvalidRequest
```

#### `Connect`

```norm
Connect
```

#### `Timeout`

```norm
Timeout
```

#### `Cancelled`

```norm
Cancelled
```

#### `Tls`

```norm
Tls
```

#### `Protocol`

```norm
Protocol
```

#### `Closed`

```norm
Closed
```

#### `Io`

```norm
Io
```

### `HttpException`

Reports a typed HTTP transport failure for a specific operation and URI.

```norm
class HttpException extends IOException
```

#### `operation`

The HTTP operation that failed.

```norm
HttpOperation operation
```

Type: `HttpOperation`

#### `reason`

The transport failure category.

```norm
HttpFailure reason
```

Type: `HttpFailure`

#### `uri`

The request URI associated with the failure.

```norm
Uri uri
```

Type: `Uri`

#### `HttpException`

Creates a typed HTTP transport failure.

```norm
HttpException(String code, String message, HttpOperation operation, HttpFailure reason, Uri uri)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `operation`: `HttpOperation`
The HTTP operation that failed.

- `reason`: `HttpFailure`
The transport failure category.

- `uri`: `Uri`
The request URI associated with the failure.


### `HttpResponse`

Streams an HTTP response body and exposes its status and headers.

```norm
interface HttpResponse extends ByteReader, Resource
```

#### `status`

Returns the response status code.

```norm
Status status()
```

Returns: `Status`

#### `headers`

Returns the response headers in transport order.

```norm
HeaderMap headers()
```

Returns: `HeaderMap`

### `HttpClient`

Sends HTTP requests with an explicit timeout.

```norm
interface HttpClient
```

#### `send`

Sends one request and returns a streaming response.

```norm
HttpResponse send(HttpRequest request, Duration timeout)
```

Parameters:

- `request`: `HttpRequest`
The request to send.

- `timeout`: `Duration`
The positive timeout for the complete send operation.


Returns: `HttpResponse`

### `systemHttpClient`

Returns the process-wide HTTP client backed by the host transport.

```norm
HttpClient systemHttpClient()
```

Returns: `HttpClient`

### `request`

Creates an HTTP request from explicit method, URI, headers, and optional body values.

```norm
HttpRequest request(HttpMethod method, Uri uri, HeaderMap headers, Bytes? body)
```

Parameters:

- `method`: `HttpMethod`
The HTTP request method.

- `uri`: `Uri`
The request target URI.

- `headers`: `HeaderMap`
The ordered request headers.

- `body`: `Bytes?`
The optional request body bytes.


Returns: `HttpRequest`

### `get`

Creates a GET request with no headers or body.

```norm
HttpRequest get(Uri uri)
```

Parameters:

- `uri`: `Uri`
The request target URI.


Returns: `HttpRequest`

## `std.http`

Source: `http/json.norm`

### `jsonBody`

Encodes a value as UTF-8 JSON request-body bytes.

```norm
Bytes jsonBody<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The value to encode as JSON.


Returns: `Bytes`

Related tests:

- `std.test.http.json_request::jsonRequestTest()` — jsonRequestTest
  tests/test/http/json_request/case.api.json

### `jsonRequest`

Creates an HTTP request with a JSON body and a canonical application/json content type.

```norm
HttpRequest jsonRequest<T>(HttpMethod method, Uri uri, HeaderMap headers, T body)
```

Type parameters:

- `T`

Parameters:

- `method`: `HttpMethod`
The HTTP request method.

- `uri`: `Uri`
The request target URI.

- `headers`: `HeaderMap`
The request headers to preserve and normalize.

- `body`: `T`
The value to encode as the JSON request body.


Returns: `HttpRequest`

### `postJson`

Creates a POST request with a JSON body and no additional headers.

```norm
HttpRequest postJson<T>(Uri uri, T body)
```

Type parameters:

- `T`

Parameters:

- `uri`: `Uri`
The request target URI.

- `body`: `T`
The value to encode as the JSON request body.


Returns: `HttpRequest`

Related tests:

- `std.test.http.json_request::jsonRequestTest()` — jsonRequestTest
  tests/test/http/json_request/case.api.json

### `decodeJson`

Decodes UTF-8 JSON response-body bytes into a value of type T.

```norm
T decodeJson<T>(Bytes body)
```

Type parameters:

- `T`

Parameters:

- `body`: `Bytes`
The JSON response-body bytes to decode.


Returns: `T`

Related tests:

- `std.test.http.json_request::jsonRequestTest()` — jsonRequestTest
  tests/test/http/json_request/case.api.json

## `std.io`

Source: `io/bytes.norm`

Provides immutable bytes, streaming I/O protocols, text codecs, resources, and typed I/O failures.

### `ByteOperation`

Identifies byte operations that can fail.

```norm
enum ByteOperation
```

#### `Create`

```norm
Create
```

### `ByteFailure`

Classifies failures caused by byte values outside the unsigned 0 through 255 range.

```norm
enum ByteFailure
```

#### `OutOfRange`

```norm
OutOfRange
```

### `ByteException`

Reports an invalid byte value together with its operation and array position.

```norm
class ByteException extends IOException
```

#### `operation`

The byte operation that failed.

```norm
ByteOperation operation
```

Type: `ByteOperation`

#### `reason`

The byte failure category.

```norm
ByteFailure reason
```

Type: `ByteFailure`

#### `index`

The array index containing the invalid value.

```norm
Integer index
```

Type: `Integer`

#### `value`

The invalid integer supplied as a byte.

```norm
Integer value
```

Type: `Integer`

#### `ByteException`

Creates a typed byte construction failure.

```norm
ByteException(String code, String message, ByteOperation operation, ByteFailure reason, Integer index, Integer value)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `operation`: `ByteOperation`
The byte operation that failed.

- `reason`: `ByteFailure`
The byte failure category.

- `index`: `Integer`
The array index containing the invalid value.

- `value`: `Integer`
The invalid integer supplied as a byte.


### `Bytes`

Provides immutable random access to an ordered sequence of unsigned bytes.

```norm
interface Bytes
```

Related tests:

- `std.test.io.bytes::bytesTest()` — bytesTest
  tests/test/io/bytes/case.api.json

#### `size`

Returns the number of bytes in the sequence.

```norm
Integer size()
```

Returns: `Integer`

#### `at`

Returns the unsigned byte value at a zero-based index.

```norm
Integer at(Integer index)
```

Parameters:

- `index`: `Integer`
The zero-based byte index.


Returns: `Integer`

#### `slice`

Returns an immutable byte slice for the requested range.

```norm
Bytes slice(Integer start, Integer length)
```

Parameters:

- `start`: `Integer`
The zero-based first byte in the slice.

- `length`: `Integer`
The number of bytes in the slice.


Returns: `Bytes`

#### `toArray`

Copies the bytes into an integer array in sequence order.

```norm
Array<Integer> toArray()
```

Returns: `Array<Integer>`

### `BytesValue`

Provides the standard runtime-backed implementation of immutable Bytes values.

```norm
value BytesValue implements Bytes
```

#### `size`

Returns the number of bytes in this sequence.

```norm
Integer size()
```

Returns: `Integer`

#### `at`

Returns the unsigned byte value at a zero-based index.

```norm
Integer at(Integer index)
```

Parameters:

- `index`: `Integer`
The zero-based byte index.


Returns: `Integer`

#### `slice`

Returns an immutable byte slice for the requested range.

```norm
Bytes slice(Integer start, Integer length)
```

Parameters:

- `start`: `Integer`
The zero-based first byte in the slice.

- `length`: `Integer`
The number of bytes in the slice.


Returns: `Bytes`

#### `toArray`

Copies the bytes into an integer array in sequence order.

```norm
Array<Integer> toArray()
```

Returns: `Array<Integer>`

### `bytes`

Validates unsigned byte integers and creates an immutable byte sequence.

```norm
Bytes bytes(Array<Integer> values)
```

Parameters:

- `values`: `Array<Integer>`
The integers to validate and copy in sequence order.


Returns: `Bytes`

Related tests:

- `std.test.io.bytes::bytesTest()` — bytesTest
  tests/test/io/bytes/case.api.json

## `std.io`

Source: `io/console.norm`

### `standardInput`

Returns the borrowed standard input byte stream; the host owns its lifetime.

```norm
ByteReader standardInput()
```

Returns: `ByteReader`

### `print`

Writes and flushes standard output without adding a newline.

```norm
Void print(String text)
```

Parameters:

- `text`: `String`
The text to write.


Returns: `Void`

### `printError`

Writes and flushes standard error without adding a newline.

```norm
Void printError(String text)
```

Parameters:

- `text`: `String`
The diagnostic text to write.


Returns: `Void`

## `std.io`

Source: `io/output.norm`

### `printLines`

Prints each stringable value on its own output line in iteration order.

```norm
Void printLines<T extends Stringable>(Iterable<T> values)
```

Type parameters:

- `T` extends `Stringable`

Parameters:

- `values`: `Iterable<T>`
The values whose string representations are printed.


Returns: `Void`

Related tests:

- `std.test.io.output_lines::outputLinesTest()` — outputLinesTest
  tests/test/io/output_lines/case.api.json

## `std.io`

Source: `io/ownership.norm`

### `ResourceOwner`

Tracks resources and executes actions under their owning scope.

```norm
interface ResourceOwner
```

#### `own`

Registers a resource with this owner.

```norm
Void own(Resource resource)
```

Parameters:

- `resource`: `Resource`
The resource to register.


Returns: `Void`

#### `release`

Removes a resource from this owner.

```norm
Void release(Resource resource)
```

Parameters:

- `resource`: `Resource`
The resource to remove.


Returns: `Void`

#### `execute`

Runs an action within the owning scope.

```norm
Void execute(Function<Void()> action)
```

Parameters:

- `action`: `Function<Void()>`
The action to execute.


Returns: `Void`

### `ownResource`

Transfers a host resource into an explicit owner once.

```norm
Void ownResource(ResourceOwner owner, Resource resource)
```

Parameters:

- `owner`: `ResourceOwner`
The owner receiving the resource.

- `resource`: `Resource`
The host resource to transfer.


Returns: `Void`

### `ownResource`

Transfers a Java resource through its canonical lifetime record.

```norm
Void ownResource(ResourceOwner owner, AutoCloseable resource)
```

Parameters:

- `owner`: `ResourceOwner`
The owner receiving the resource.

- `resource`: `AutoCloseable`
The Java resource to transfer.


Returns: `Void`

### `ownResourceInContext`

Registers owned host resources with the current owner while preserving the input type.

```norm
T ownResourceInContext<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The value whose owned host resource joins the current scope.


Returns: `T`

### `closeHostResource`

Closes an owned host resource through its canonical lifetime record.

```norm
Void closeHostResource(Resource resource)
```

Parameters:

- `resource`: `Resource`
The owned host resource to close.


Returns: `Void`

## `std.io`

Source: `io/streams.norm`

### `ReadChunk`

Represents either a non-empty chunk of bytes or the end of a readable stream.

```norm
enum ReadChunk
```

Related tests:

- `std.test.io.bytes::bytesTest()` — bytesTest
  tests/test/io/bytes/case.api.json

#### `Data`

```norm
Data(Bytes bytes)
```

Parameters:

- `bytes`: `Bytes`

#### `Eof`

```norm
Eof
```

### `StreamOperation`

Identifies complete-stream read and write operations.

```norm
enum StreamOperation
```

#### `ReadAll`

```norm
ReadAll
```

#### `WriteAll`

```norm
WriteAll
```

### `StreamFailure`

Classifies stream limit, stalled progress, and invalid progress failures.

```norm
enum StreamFailure
```

#### `LimitExceeded`

```norm
LimitExceeded
```

#### `NoProgress`

```norm
NoProgress
```

#### `InvalidProgress`

```norm
InvalidProgress
```

### `StreamException`

Reports a complete-stream operation that violated its progress or size contract.

```norm
class StreamException extends IOException
```

#### `operation`

The complete-stream operation that failed.

```norm
StreamOperation operation
```

Type: `StreamOperation`

#### `reason`

The stream failure category.

```norm
StreamFailure reason
```

Type: `StreamFailure`

#### `StreamException`

Creates a typed complete-stream failure.

```norm
StreamException(String code, String message, StreamOperation operation, StreamFailure reason)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `operation`: `StreamOperation`
The complete-stream operation that failed.

- `reason`: `StreamFailure`
The stream failure category.


### `ByteReader`

Reads bounded byte chunks from a resource.

```norm
interface ByteReader
```

#### `read`

Reads at most the requested number of bytes or reports end of stream.

```norm
ReadChunk read(Integer maximumBytes)
```

Parameters:

- `maximumBytes`: `Integer`
The maximum number of bytes requested from this read.


Returns: `ReadChunk`

### `ByteWriter`

Writes bytes and reports how many values were accepted.

```norm
interface ByteWriter
```

#### `write`

Writes a prefix of the supplied bytes and returns the accepted byte count.

```norm
Integer write(Bytes content)
```

Parameters:

- `content`: `Bytes`
The bytes offered to the writer.


Returns: `Integer`

### `Flushable`

Flushes buffered output to its next destination.

```norm
interface Flushable
```

#### `flush`

Flushes all currently buffered output.

```norm
Void flush()
```

Returns: `Void`

### `Resource`

Owns an external resource that requires deterministic closure.

```norm
interface Resource
```

Related tests:

- `std.test.io.bytes::bytesTest()` — bytesTest
  tests/test/io/bytes/case.api.json
- `std.test.io.resource_use::resourceUseTest()` — resourceUseTest
  tests/test/io/resource_use/case.api.json

#### `close`

Closes the resource and releases its external ownership.

```norm
Void close()
```

Returns: `Void`

### `InputStream`

Adapts a hosted byte input stream to Norm byte I/O and resource ownership.

```norm
class InputStream implements ByteReader, Resource
```

#### `read`

Reads at most the requested number of bytes or reports end of stream.

```norm
ReadChunk read(Integer maximumBytes)
```

Parameters:

- `maximumBytes`: `Integer`
The maximum number of bytes requested from this read.


Returns: `ReadChunk`

#### `close`

Closes the input stream and releases its external ownership.

```norm
Void close()
```

Returns: `Void`

### `OutputStream`

Adapts a hosted byte output stream to Norm byte I/O and resource ownership.

```norm
class OutputStream implements ByteWriter, Flushable, Resource
```

#### `write`

Writes the supplied bytes and returns the accepted byte count.

```norm
Integer write(Bytes content)
```

Parameters:

- `content`: `Bytes`
The bytes offered to the output stream.


Returns: `Integer`

#### `flush`

Flushes buffered bytes to the next destination.

```norm
Void flush()
```

Returns: `Void`

#### `close`

Closes the output stream and releases its external ownership.

```norm
Void close()
```

Returns: `Void`

### `readAll`

Reads a complete byte stream without exceeding an explicit size limit.

```norm
Bytes readAll(ByteReader reader, Integer maximumBytes)
```

Parameters:

- `reader`: `ByteReader`
The reader supplying byte chunks.

- `maximumBytes`: `Integer`
The maximum total number of bytes allowed in the result.


Returns: `Bytes`

### `writeAll`

Writes all bytes while enforcing forward progress from the writer.

```norm
Void writeAll(ByteWriter writer, Bytes content)
```

Parameters:

- `writer`: `ByteWriter`
The writer receiving the bytes.

- `content`: `Bytes`
The complete byte sequence to write.


Returns: `Void`

### `use`

Runs a body and closes its resource when the body completes or fails.

```norm
T use<T>(Resource resource, T body())
```

Type parameters:

- `T`

Parameters:

- `resource`: `Resource`
The resource closed after the body exits.

- `body`: `Function<T()>`
The operation performed while the resource is open.


Returns: `T`

Related tests:

- `std.test.io.resource_use::resourceUseTest()` — resourceUseTest
  tests/test/io/resource_use/case.api.json

## `std.io`

Source: `io/system.norm`

### `TextEncoding`

Selects the text encoding used to convert between strings and bytes.

```norm
enum TextEncoding
```

Related tests:

- `std.test.filesystem.file_read_text::fileReadTextTest()` — fileReadTextTest
  tests/test/filesystem/file_read_text/case.api.json

#### `Utf8`

```norm
Utf8
```

### `TextOperation`

Identifies text encoding and decoding operations.

```norm
enum TextOperation
```

#### `Encode`

```norm
Encode
```

#### `Decode`

```norm
Decode
```

### `TextFailure`

Classifies text input that is invalid for the selected encoding operation.

```norm
enum TextFailure
```

#### `InvalidInput`

```norm
InvalidInput
```

### `IOException`

Provides the common typed base for standard-library I/O failures.

```norm
class IOException extends SystemException
```

#### `IOException`

Creates an I/O failure with a stable code and readable explanation.

```norm
IOException(String code, String message)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.


### `TextException`

Reports invalid text or bytes for a selected encoding operation.

```norm
class TextException extends IOException
```

#### `operation`

The text conversion operation that failed.

```norm
TextOperation operation
```

Type: `TextOperation`

#### `reason`

The text conversion failure category.

```norm
TextFailure reason
```

Type: `TextFailure`

#### `TextException`

Creates a typed text conversion failure.

```norm
TextException(String code, String message, TextOperation operation, TextFailure reason)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `operation`: `TextOperation`
The text conversion operation that failed.

- `reason`: `TextFailure`
The text conversion failure category.


### `encodeText`

Encodes valid Unicode text using the selected byte encoding.

```norm
Bytes encodeText(String text, TextEncoding encoding)
```

Parameters:

- `text`: `String`
The Unicode text to encode.

- `encoding`: `TextEncoding`
The byte encoding to apply.


Returns: `Bytes`

### `decodeText`

Decodes bytes into valid Unicode text using the selected encoding.

```norm
String decodeText(Bytes content, TextEncoding encoding)
```

Parameters:

- `content`: `Bytes`
The encoded bytes to decode.

- `encoding`: `TextEncoding`
The byte encoding to apply.


Returns: `String`

## `std.json`

Source: `json/json.norm`

Provides typed JSON serialization and a format-neutral JSON value tree.

### `JsonValue`

Represents a JSON object, array, string, number, Boolean, or null value.

```norm
enum JsonValue
```

Related tests:

- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json

#### `Object`

```norm
Object(Map<String, JsonValue> fields)
```

Parameters:

- `fields`: `Map<String, JsonValue>`

#### `Array`

```norm
Array(List<JsonValue> values)
```

Parameters:

- `values`: `List<JsonValue>`

#### `String`

```norm
String(String value)
```

Parameters:

- `value`: `String`

#### `Number`

```norm
Number(String value)
```

Parameters:

- `value`: `String`

#### `Boolean`

```norm
Boolean(Boolean value)
```

Parameters:

- `value`: `Boolean`

#### `Null`

```norm
Null
```

### `jsonSchema`

Derives a JSON Schema from the shared serialization shape of a type.

```norm
JsonValue jsonSchema(Class<?> type)
```

Parameters:

- `type`: `Class<?>`
The serialized type.


Returns: `JsonValue`

### `functionSchema`

Derives an argument schema and verifies the serializable result of a function.

```norm
JsonValue functionSchema(Function<?> operation)
```

Parameters:

- `operation`: `Function<?>`
A top-level function or bound method.


Returns: `JsonValue`

### `invokeJson`

Validates and decodes named JSON arguments, invokes a function, and serializes its result.

```norm
String invokeJson(Function<?> operation, String arguments)
```

Parameters:

- `operation`: `Function<?>`
A top-level function or bound method.

- `arguments`: `String`
A JSON object containing named arguments.


Returns: `String`

### `JsonException`

Reports a JSON parsing, encoding, decoding, or mapping failure with source location data.

```norm
class JsonException extends Exception
```

Related tests:

- `std.test.json.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/json/failure_matrix/case.api.json
- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json

#### `code`

The stable machine-readable failure code.

```norm
String code
```

Type: `String`

#### `path`

The structural path at which the failure occurred.

```norm
String path
```

Type: `String`

#### `offset`

The zero-based source offset associated with the failure.

```norm
Integer offset
```

Type: `Integer`

#### `line`

The one-based source line associated with the failure.

```norm
Integer line
```

Type: `Integer`

#### `column`

The one-based source column associated with the failure.

```norm
Integer column
```

Type: `Integer`

#### `JsonException`

Creates a JSON failure with structural and textual location details.

```norm
JsonException(String code, String message, String path, Integer offset, Integer line, Integer column)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `path`: `String`
The structural path at which the failure occurred.

- `offset`: `Integer`
The zero-based source offset associated with the failure.

- `line`: `Integer`
The one-based source line associated with the failure.

- `column`: `Integer`
The one-based source column associated with the failure.


### `JsonMapper`

Creates JSON readers and writers for requested value types.

```norm
value JsonMapper implements DataMapper
```

Related tests:

- `std.test.serialization.mapper::mapperTest()` — mapperTest
  tests/test/serialization/mapper/case.api.json

#### `reader`

Creates a JSON reader for values of type T.

```norm
DataReader<T> reader<T>()
```

Type parameters:

- `T`

Returns: `DataReader<T>`

#### `writer`

Creates a JSON writer for values of type T.

```norm
DataWriter<T> writer<T>()
```

Type parameters:

- `T`

Returns: `DataWriter<T>`

### `JsonReader`

Decodes JSON text and bytes into values of type T.

```norm
value JsonReader<T> implements DataReader<T>
```

Type parameters:

- `T`

#### `readString`

Decodes JSON text into a value of type T.

```norm
T readString(String source)
```

Parameters:

- `source`: `String`
The JSON text to decode.


Returns: `T`

#### `readBytes`

Decodes UTF-8 JSON bytes into a value of type T.

```norm
T readBytes(Bytes source)
```

Parameters:

- `source`: `Bytes`
The UTF-8 JSON bytes to decode.


Returns: `T`

### `JsonWriter`

Encodes values of type T as JSON text and UTF-8 bytes.

```norm
value JsonWriter<T> implements DataWriter<T>
```

Type parameters:

- `T`

#### `writeString`

Encodes a value as JSON text.

```norm
String writeString(T value)
```

Parameters:

- `value`: `T`
The value to encode.


Returns: `String`

#### `writeBytes`

Encodes a value as UTF-8 JSON bytes.

```norm
Bytes writeBytes(T value)
```

Parameters:

- `value`: `T`
The value to encode.


Returns: `Bytes`

### `toJson`

Encodes a value as JSON text.

```norm
extension String toJson<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The value to encode.


Returns: `String`

Related tests:

- `std.test.json.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/json/failure_matrix/case.api.json
- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json
- `std.test.serialization.recursive::recursiveTest()` — recursiveTest
  tests/test/serialization/recursive/case.api.json

### `fromJson`

Decodes JSON text into a value of type T.

```norm
extension T fromJson<T>(String value)
```

Type parameters:

- `T`

Parameters:

- `value`: `String`
The JSON text to decode.


Returns: `T`

Related tests:

- `std.test.json.construction::constructionTest()` — constructionTest
  tests/test/json/construction/case.api.json
- `std.test.json.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/json/failure_matrix/case.api.json
- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json
- `std.test.serialization.recursive::recursiveTest()` — recursiveTest
  tests/test/serialization/recursive/case.api.json

### `toJsonBytes`

Encodes a value as UTF-8 JSON bytes.

```norm
extension Bytes toJsonBytes<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The value to encode.


Returns: `Bytes`

### `fromJsonBytes`

Decodes UTF-8 JSON bytes into a value of type T.

```norm
extension T fromJsonBytes<T>(Bytes value)
```

Type parameters:

- `T`

Parameters:

- `value`: `Bytes`
The UTF-8 JSON bytes to decode.


Returns: `T`

### `parseJson`

Parses JSON text into a JsonValue tree without mapping it to an application type.

```norm
JsonValue parseJson(String value)
```

Parameters:

- `value`: `String`
The JSON text to parse.


Returns: `JsonValue`

Related tests:

- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json

### `writeJson`

Writes a JsonValue tree as JSON text.

```norm
String writeJson(JsonValue value)
```

Parameters:

- `value`: `JsonValue`
The JSON value tree to write.


Returns: `String`

Related tests:

- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json

### `toJsonValue`

Converts a typed value into a JsonValue tree.

```norm
JsonValue toJsonValue<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The typed value to convert.


Returns: `JsonValue`

### `fromJsonValue`

Maps a JsonValue tree into a value of type T.

```norm
T fromJsonValue<T>(JsonValue value)
```

Type parameters:

- `T`

Parameters:

- `value`: `JsonValue`
The JSON value tree to map.


Returns: `T`

Related tests:

- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json

## `std.logging`

Source: `logging/file.norm`

### `FileLogOutputer`

Persists JSON Lines in size-limited files with per-run isolation.

```norm
class FileLogOutputer implements LogOutputer
```

#### `open`

Opens the destination directory and applies its retention settings.

```norm
Void open(Map<String, String> configuration)
```

Parameters:

- `configuration`: `Map<String, String>`
Directory, segmentBytes, retainDays and totalBytes options.


Returns: `Void`

#### `output`

Appends one JSON record to the current segment.

```norm
Void output(LogEvent event)
```

Parameters:

- `event`: `LogEvent`
The event to persist.


Returns: `Void`

#### `flush`

Flushes pending file output.

```norm
Void flush()
```

Returns: `Void`

#### `close`

Closes the active segment and releases the run lock.

```norm
Void close()
```

Returns: `Void`

## `std.logging`

Source: `logging/log.norm`

### `logLevelName`

Returns the stable output label for a log level.

```norm
String logLevelName(LogLevel level)
```

Parameters:

- `level`: `LogLevel`
The event severity.


Returns: `String`

### `ConsoleLogOutputer`

Writes timestamped application log events to standard error.

```norm
class ConsoleLogOutputer implements LogOutputer
```

#### `open`

Initializes console output.

```norm
Void open(Map<String, String> configuration)
```

Parameters:

- `configuration`: `Map<String, String>`
Console output options.


Returns: `Void`

#### `output`

Writes an event to standard error.

```norm
Void output(LogEvent event)
```

Parameters:

- `event`: `LogEvent`
The event to write.


Returns: `Void`

#### `flush`

Completes pending console writes.

```norm
Void flush()
```

Returns: `Void`

#### `close`

Releases the output without closing the host stream.

```norm
Void close()
```

Returns: `Void`

### `logDebug`

Emits an application debug event.

```norm
Void logDebug(String message)
```

Parameters:

- `message`: `String`
The message to record.


Returns: `Void`

### `logInfo`

Emits an application info event.

```norm
Void logInfo(String message)
```

Parameters:

- `message`: `String`
The message to record.


Returns: `Void`

### `logWarn`

Emits an application warn event.

```norm
Void logWarn(String message)
```

Parameters:

- `message`: `String`
The message to record.


Returns: `Void`

### `logError`

Emits an application error event.

```norm
Void logError(String message)
```

Parameters:

- `message`: `String`
The message to record.


Returns: `Void`

## `std.logging`

Source: `logging/output.norm`

Defines application log events and output destinations.

### `LogLevel`

Identifies the severity of a log event.

```norm
enum LogLevel
```

Related tests:

- `std.test.logging.outputer::acceptsLibraryOutput()` — acceptsLibraryOutput
  tests/test/logging/outputer/case.api.json

#### `Debug`

```norm
Debug
```

#### `Info`

```norm
Info
```

#### `Warn`

```norm
Warn
```

#### `Error`

```norm
Error
```

### `LogEvent`

Carries a timestamped message from its originating package.

```norm
value LogEvent
```

Related tests:

- `std.test.logging.outputer::acceptsLibraryOutput()` — acceptsLibraryOutput
  tests/test/logging/outputer/case.api.json

#### `time`

The time the caller emitted the event.

```norm
Instant time
```

Type: `Instant`

#### `level`

The severity assigned by the caller.

```norm
LogLevel level
```

Type: `LogLevel`

#### `source`

The qualified package name of the caller.

```norm
String source
```

Type: `String`

#### `message`

The message supplied by the caller.

```norm
String message
```

Type: `String`

### `LogOutputer`

Consumes application logs for one configured destination.

```norm
interface LogOutputer extends Flushable, Resource
```

Related tests:

- `std.test.logging.outputer::acceptsLibraryOutput()` — acceptsLibraryOutput
  tests/test/logging/outputer/case.api.json

#### `open`

Initializes the destination with its instance configuration.

```norm
Void open(Map<String, String> configuration)
```

Parameters:

- `configuration`: `Map<String, String>`
Options for this destination.


Returns: `Void`

#### `output`

Receives one matching event.

```norm
Void output(LogEvent event)
```

Parameters:

- `event`: `LogEvent`
The event to deliver.


Returns: `Void`

## `std.math`

Source: `math/integer.norm`

Provides integer comparison, magnitude, range, and sign operations.

### `min`

Returns the smaller of two integers.

```norm
Integer min(Integer left, Integer right)
```

Parameters:

- `left`: `Integer`
The first integer.

- `right`: `Integer`
The second integer.


Returns: `Integer`

Related tests:

- `std.test.integration.edge_cases::edgeCasesTest()` — edgeCasesTest
  tests/test/integration/edge_cases/case.api.json
- `std.test.math.min_max::minMaxTest()` — minMaxTest
  tests/test/math/min_max/case.api.json

### `max`

Returns the larger of two integers.

```norm
Integer max(Integer left, Integer right)
```

Parameters:

- `left`: `Integer`
The first integer.

- `right`: `Integer`
The second integer.


Returns: `Integer`

Related tests:

- `std.test.integration.edge_cases::edgeCasesTest()` — edgeCasesTest
  tests/test/integration/edge_cases/case.api.json
- `std.test.math.min_max::minMaxTest()` — minMaxTest
  tests/test/math/min_max/case.api.json

### `abs`

Returns the absolute magnitude of an integer.

```norm
Integer abs(Integer value)
```

Parameters:

- `value`: `Integer`
The integer whose magnitude is returned.


Returns: `Integer`

Related tests:

- `std.test.integration.edge_cases::edgeCasesTest()` — edgeCasesTest
  tests/test/integration/edge_cases/case.api.json
- `std.test.math.abs::absTest()` — absTest
  tests/test/math/abs/case.api.json

### `clamp`

Constrains an integer to an inclusive interval.

```norm
Integer clamp(Integer value, Integer minimum, Integer maximum)
```

Parameters:

- `value`: `Integer`
The integer to constrain.

- `minimum`: `Integer`
The inclusive lower bound.

- `maximum`: `Integer`
The inclusive upper bound.


Returns: `Integer`

Related tests:

- `std.test.integration.edge_cases::edgeCasesTest()` — edgeCasesTest
  tests/test/integration/edge_cases/case.api.json
- `std.test.math.clamp::clampTest()` — clampTest
  tests/test/math/clamp/case.api.json

### `sign`

Returns -1, 0, or 1 according to an integer's sign.

```norm
Integer sign(Integer value)
```

Parameters:

- `value`: `Integer`
The integer whose sign is inspected.


Returns: `Integer`

Related tests:

- `std.test.math.sign::signTest()` — signTest
  tests/test/math/sign/case.api.json

## `std.observation`

Source: `observation/fields.norm`

Provides subscriptions to field reads and changes.

### `onChange`

Subscribes to changes of a field until the returned resource is closed.

```norm
extension Resource onChange<T>(FieldHandle<T> field, Void changed(T oldValue, T newValue))
```

Type parameters:

- `T`

Parameters:

- `field`: `FieldHandle<T>`
The field to observe.

- `changed`: `Function<Void(T, T)>`
The callback receiving previous and current values.


Returns: `Resource`

### `observeFields`

Observes field access on a target until the returned resource is closed.

```norm
Resource observeFields<T>(T target, Void read(Integer field), Void changed(Integer field))
```

Type parameters:

- `T`

Parameters:

- `target`: `T`
The instance to observe.

- `read`: `Function<Void(Integer)>`
Receives the identity of a read field.

- `changed`: `Function<Void(Integer)>`
Receives the identity of a changed field.


Returns: `Resource`

## `std.process`

Source: `process/process.norm`

Runs external processes with explicit arguments, bounded output and cancellation.

### `ProcessOutcome`

Distinguishes normal exit, deadline expiry and cancellation.

```norm
enum ProcessOutcome
```

#### `Exited`

```norm
Exited
```

#### `TimedOut`

```norm
TimedOut
```

#### `Cancelled`

```norm
Cancelled
```

### `ProcessFailure`

Classifies invalid requests, start failures and process I/O failures.

```norm
enum ProcessFailure
```

#### `InvalidRequest`

```norm
InvalidRequest
```

#### `StartFailed`

```norm
StartFailed
```

#### `Io`

```norm
Io
```

### `ProcessException`

Reports process execution failures with an executable and typed reason.

```norm
class ProcessException extends IOException
```

#### `reason`

The process failure category.

```norm
ProcessFailure reason
```

Type: `ProcessFailure`

#### `executable`

The executable name or path.

```norm
String executable
```

Type: `String`

#### `ProcessException`

Creates a typed process failure.

```norm
ProcessException(ProcessFailure reason, String executable, String message)
```

Parameters:

- `reason`: `ProcessFailure`
The failure category.

- `executable`: `String`
The executable.

- `message`: `String`
The explanation.


### `ProcessResult`

Reports actual process completion and separately bounded output streams.

```norm
value ProcessResult
```

#### `outcome`

How execution completed.

```norm
ProcessOutcome outcome
```

Type: `ProcessOutcome`

#### `exitCode`

The observed exit code, or null when no exit was observed.

```norm
Integer? exitCode
```

Type: `Integer?`

#### `stdout`

Captured standard output bytes.

```norm
Bytes stdout
```

Type: `Bytes`

#### `stderr`

Captured standard error bytes.

```norm
Bytes stderr
```

Type: `Bytes`

#### `stdoutTruncated`

Whether standard output exceeded its capture budget.

```norm
Boolean stdoutTruncated
```

Type: `Boolean`

#### `stderrTruncated`

Whether standard error exceeded its capture budget.

```norm
Boolean stderrTruncated
```

Type: `Boolean`

### `runProcess`

Runs without a shell, drains both output streams and returns nonzero exits as results.

```norm
ProcessResult runProcess(String executable, List<String> arguments, Path directory, Map<String, String> environment, Bytes input, Duration timeout, Integer maximumOutputBytes)
```

Parameters:

- `executable`: `String`
The executable name or path.

- `arguments`: `List<String>`
Arguments with preserved boundaries.

- `directory`: `Path`
The child working directory.

- `environment`: `Map<String, String>`
Overrides applied to the inherited host environment.

- `input`: `Bytes`
Bytes written before closing child standard input.

- `timeout`: `Duration`
The total execution and stream-drain budget.

- `maximumOutputBytes`: `Integer`
The maximum captured bytes per output stream; excess is drained and marked.


Returns: `ProcessResult`

## `std.runtime`

Source: `runtime/events.norm`

### `RuntimeUpdateEvent`

Reports one runtime update transition and the declarations changed by that publication.

```norm
value RuntimeUpdateEvent
```

#### `sequence`

Monotonic event sequence assigned by the runtime.

```norm
Long sequence
```

Type: `Long`

#### `kind`

The update transition kind.

```norm
String kind
```

Type: `String`

#### `revision`

The published revision associated with the transition.

```norm
Long revision
```

Type: `Long`

#### `pendingLocations`

Active locations that still need to adopt the published revision.

```norm
List<String> pendingLocations
```

Type: `List<String>`

#### `changes`

Stable summaries of declarations changed by the publication.

```norm
List<String> changes
```

Type: `List<String>`

### `UpdateSubscription`

Consumes runtime update events in publication order.

```norm
class UpdateSubscription implements Resource
```

#### `close`

Stops this subscription.

```norm
Void close()
```

Returns: `Void`

## `std.runtime`

Source: `runtime/migration.norm`

Provides explicit converters for retained runtime state.

### `StateMigration`

Declares the converter used when this type adopts an incompatible retained-state schema.

```norm
annotation StateMigration implements TypeTarget, RuntimeRetention
```

#### `convert`

Converts one retained instance synchronously through its migration state. Failed conversion preserves its previous Norm state; external I/O is not rolled back. Same-thread host reentry is allowed, while cross-thread guest callbacks are rejected during conversion.

```norm
Function<Void(MigrationState)> convert
```

Type: `Function<Void(MigrationState)>`

### `MigrationState`

Provides the previous schema and staged candidate representation during a converter invocation. Operations are invalid after that invocation returns.

```norm
class MigrationState
```

#### `type`

Returns a snapshot of the previous reified type and its schema.

```norm
Class<?> type()
```

Returns: `Class<?>`

#### `variant`

Returns the previous enum variant name, or null for a stored-field instance.

```norm
String? variant()
```

Returns: `String?`

#### `read`

Reads a previous enum payload after validating that its declared type is assignable to T.

```norm
T read<T>(Integer index)
```

Type parameters:

- `T`

Parameters:

- `index`: `Integer`
The zero-based payload index to read.


Returns: `T`

#### `replace`

Stages a complete candidate representation of the same logical nominal type. Identity instances retain their existing shell.

```norm
Void replace<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The complete candidate value to stage.


Returns: `Void`

#### `contains`

Reports whether the previous schema declares this field. Ambiguous inherited names fail.

```norm
Boolean contains(String field)
```

Parameters:

- `field`: `String`
The field name to look up in the previous schema.


Returns: `Boolean`

#### `read`

Reads a previous field snapshot after validating that its declared type is assignable to T.

```norm
T read<T>(String field)
```

Type parameters:

- `T`

Parameters:

- `field`: `String`
The field name to read from the previous schema.


Returns: `T`

#### `write`

Stages a value using a target field descriptor whose declared type matches T.

```norm
Void write<T>(Field<?, T> field, T value)
```

Type parameters:

- `T`

Parameters:

- `field`: `Field<?, T>`
The target field descriptor receiving the staged value.

- `value`: `T`
The value to stage in the target field.


Returns: `Void`

#### `transfer`

Copies a previous field to a target field after validating their instance-specific declared types. Consuming a renamed source field requires remove.

```norm
Void transfer(String source, String target)
```

Parameters:

- `source`: `String`
The previous field name to copy.

- `target`: `String`
The target field name receiving the copied value.


Returns: `Void`

#### `remove`

Explicitly consumes a previous field removed from the target schema. Retained compatible fields cannot be removed.

```norm
Void remove(String field)
```

Parameters:

- `field`: `String`
The previous field name to consume.


Returns: `Void`

## `std.runtime`

Source: `runtime/updates.norm`

### `Runtime`

Provides the current source execution's runtime update capability.

```norm
class Runtime
```

#### `status`

Reports live source execution state.

```norm
RuntimeStatus status()
```

Returns: `RuntimeStatus`

#### `latestUpdate`

Returns the most recent automatic or requested compilation result, or null before any update completes.

```norm
UpdateResult? latestUpdate()
```

Returns: `UpdateResult?`

#### `beginUpdate`

Starts a publication batch for related source and dependency edits.

```norm
UpdateBatch beginUpdate()
```

Returns: `UpdateBatch`

#### `publishUpdate`

Requests compilation of current sources and waits only for publication, never for running activations to finish adopting it.

```norm
UpdateResult publishUpdate()
```

Returns: `UpdateResult`

#### `previewUpdate`

Compiles current sources and returns all before and after changes without publishing them.

```norm
UpdatePreview previewUpdate()
```

Returns: `UpdatePreview`

#### `onUpdate`

Subscribes a callback to runtime update transitions.

```norm
UpdateSubscription onUpdate(Void callback(RuntimeUpdateEvent event))
```

Parameters:

- `callback`: `Function<Void(RuntimeUpdateEvent)>`
The callback receiving each runtime update transition.


Returns: `UpdateSubscription`

### `UpdateOutcome`

Distinguishes successful publication, unchanged sources, invalid code and host compilation failure.

```norm
enum UpdateOutcome
```

#### `Published`

```norm
Published
```

#### `Unchanged`

```norm
Unchanged
```

#### `Rejected`

```norm
Rejected
```

#### `Failed`

```norm
Failed
```

### `PreviewOutcome`

Distinguishes a reviewable preview from unchanged sources, invalid code and host compilation failure.

```norm
enum PreviewOutcome
```

#### `Previewed`

```norm
Previewed
```

#### `Unchanged`

```norm
Unchanged
```

#### `Rejected`

```norm
Rejected
```

#### `Failed`

```norm
Failed
```

### `RuntimeDiagnostic`

Reports a compiler diagnostic without parsing formatted output.

```norm
value RuntimeDiagnostic
```

#### `code`

The stable diagnostic code.

```norm
String code
```

Type: `String`

#### `severity`

The diagnostic severity.

```norm
String severity
```

Type: `String`

#### `message`

The human-readable diagnostic message.

```norm
String message
```

Type: `String`

#### `source`

The source URI or display name containing the diagnostic.

```norm
String source
```

Type: `String`

#### `startOffset`

The inclusive diagnostic start offset in the source.

```norm
Integer startOffset
```

Type: `Integer`

#### `endOffset`

The exclusive diagnostic end offset in the source.

```norm
Integer endOffset
```

Type: `Integer`

### `RuntimeStatus`

Reports the latest published revision and active locations awaiting adoption.

```norm
value RuntimeStatus
```

#### `publishedRevision`

The most recent revision published by the runtime.

```norm
Long publishedRevision
```

Type: `Long`

#### `activeRevision`

The revision currently active at the observing location.

```norm
Long activeRevision
```

Type: `Long`

#### `pendingLocations`

Active locations that still need to adopt the published revision.

```norm
List<String> pendingLocations
```

Type: `List<String>`

### `RuntimeChange`

Describes one declaration changed by a source publication. Before and after contain the stable semantic shape of the declaration.

```norm
value RuntimeChange
```

#### `kind`

The change kind, such as added, removed, or modified.

```norm
String kind
```

Type: `String`

#### `declarationKind`

The changed declaration category.

```norm
String declarationKind
```

Type: `String`

#### `identity`

The stable identity of the changed declaration.

```norm
String identity
```

Type: `String`

#### `before`

The declaration shape before publication, when present.

```norm
String? before
```

Type: `String?`

#### `after`

The declaration shape after publication, when present.

```norm
String? after
```

Type: `String?`

#### `source`

The source URI or display name containing the declaration.

```norm
String source
```

Type: `String`

#### `startOffset`

The inclusive declaration start offset in the source.

```norm
Integer startOffset
```

Type: `Integer`

#### `endOffset`

The exclusive declaration end offset in the source.

```norm
Integer endOffset
```

Type: `Integer`

### `UpdateResult`

Reports publication independently from adoption by existing activations. Pending locations can remain after successful publication.

```norm
value UpdateResult
```

#### `outcome`

The publication outcome.

```norm
UpdateOutcome outcome
```

Type: `UpdateOutcome`

#### `revision`

The published revision, when one exists.

```norm
Long revision
```

Type: `Long`

#### `pendingLocations`

Active locations that still need to adopt the published revision.

```norm
List<String> pendingLocations
```

Type: `List<String>`

#### `diagnostics`

Compiler diagnostics produced while preparing the publication.

```norm
List<RuntimeDiagnostic> diagnostics
```

Type: `List<RuntimeDiagnostic>`

#### `changes`

Declarations changed by the publication.

```norm
List<RuntimeChange> changes
```

Type: `List<RuntimeChange>`

#### `failure`

The host failure message, when publication failed.

```norm
String? failure
```

Type: `String?`

### `UpdatePreview`

Reports the complete before and after declaration changes without publishing them.

```norm
value UpdatePreview
```

#### `outcome`

The preview outcome.

```norm
PreviewOutcome outcome
```

Type: `PreviewOutcome`

#### `revision`

The candidate revision represented by this preview.

```norm
Long revision
```

Type: `Long`

#### `pendingLocations`

Active locations that still need to adopt the candidate revision.

```norm
List<String> pendingLocations
```

Type: `List<String>`

#### `diagnostics`

Compiler diagnostics produced while preparing the preview.

```norm
List<RuntimeDiagnostic> diagnostics
```

Type: `List<RuntimeDiagnostic>`

#### `changes`

All declarations changed by the candidate publication.

```norm
List<RuntimeChange> changes
```

Type: `List<RuntimeChange>`

#### `failure`

The host failure message, when preview failed.

```norm
String? failure
```

Type: `String?`

### `UpdateBatch`

Suppresses automatic publication until commit or close. Closing without commit releases suppression; it does not undo filesystem writes.

```norm
class UpdateBatch implements Resource
```

#### `preview`

Compiles the complete source tree and returns all before and after changes without publishing them. The preview remains valid until the batch sources change or the batch closes.

```norm
UpdatePreview preview()
```

Returns: `UpdatePreview`

#### `commit`

Publishes the complete source tree when it changes. Unchanged sources preserve their previous outcome. Waits for compilation, while existing activations may still be pending.

```norm
UpdateResult commit()
```

Returns: `UpdateResult`

#### `close`

Releases publication suppression. Closing an already completed batch has no effect.

```norm
Void close()
```

Returns: `Void`

## `std.serialization`

Source: `serialization/core.norm`

Defines serialization metadata and format-independent reader, writer, and mapper protocols.

### `Serializable`

Marks a type as eligible for structural serialization.

```norm
annotation Serializable implements TypeTarget, RuntimeRetention
```

Related tests:

- `std.test.configuration.properties::propertiesTest()` — propertiesTest
  tests/test/configuration/properties/case.api.json
- `std.test.http.json_request::jsonRequestTest()` — jsonRequestTest
  tests/test/http/json_request/case.api.json
- `std.test.json.construction::constructionTest()` — constructionTest
  tests/test/json/construction/case.api.json
- `std.test.json.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/json/failure_matrix/case.api.json
- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json
- `std.test.serialization.mapper::mapperTest()` — mapperTest
  tests/test/serialization/mapper/case.api.json
- `std.test.serialization.recursive::recursiveTest()` — recursiveTest
  tests/test/serialization/recursive/case.api.json
- `std.test.xml.construction::constructionTest()` — constructionTest
  tests/test/xml/construction/case.api.json
- `std.test.xml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/xml/failure_matrix/case.api.json
- `std.test.xml.round_trip::roundTripTest()` — roundTripTest
  tests/test/xml/round_trip/case.api.json
- `std.test.xml.structures::structuresTest()` — structuresTest
  tests/test/xml/structures/case.api.json
- `std.test.yaml.construction::constructionTest()` — constructionTest
  tests/test/yaml/construction/case.api.json
- `std.test.yaml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/yaml/failure_matrix/case.api.json
- `std.test.yaml.output::outputTest()` — outputTest
  tests/test/yaml/output/case.api.json
- `std.test.yaml.round_trip::roundTripTest()` — roundTripTest
  tests/test/yaml/round_trip/case.api.json
- `std.test.yaml.structures::structuresTest()` — structuresTest
  tests/test/yaml/structures/case.api.json

### `SerialName`

Overrides the serialized name of a type or field.

```norm
annotation SerialName implements TypeTarget, FieldTarget, RuntimeRetention
```

Related tests:

- `std.test.configuration.properties::propertiesTest()` — propertiesTest
  tests/test/configuration/properties/case.api.json
- `std.test.http.json_request::jsonRequestTest()` — jsonRequestTest
  tests/test/http/json_request/case.api.json
- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json
- `std.test.xml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/xml/failure_matrix/case.api.json
- `std.test.xml.round_trip::roundTripTest()` — roundTripTest
  tests/test/xml/round_trip/case.api.json
- `std.test.xml.structures::structuresTest()` — structuresTest
  tests/test/xml/structures/case.api.json
- `std.test.yaml.round_trip::roundTripTest()` — roundTripTest
  tests/test/yaml/round_trip/case.api.json

#### `name`

The external name used by serializers and deserializers.

```norm
String name
```

Type: `String`

### `SerialIgnore`

Excludes a field from structural serialization and deserialization.

```norm
annotation SerialIgnore implements FieldTarget, RuntimeRetention
```

Related tests:

- `std.test.json.round_trip::roundTripTest()` — roundTripTest
  tests/test/json/round_trip/case.api.json
- `std.test.xml.round_trip::roundTripTest()` — roundTripTest
  tests/test/xml/round_trip/case.api.json
- `std.test.yaml.round_trip::roundTripTest()` — roundTripTest
  tests/test/yaml/round_trip/case.api.json

### `DataMapper`

Creates typed readers and writers for one serialization format.

```norm
interface DataMapper
```

Related tests:

- `std.test.serialization.mapper::mapperTest()` — mapperTest
  tests/test/serialization/mapper/case.api.json

#### `reader`

Creates a reader that decodes values of type T.

```norm
DataReader<T> reader<T>()
```

Type parameters:

- `T`

Returns: `DataReader<T>`

#### `writer`

Creates a writer that encodes values of type T.

```norm
DataWriter<T> writer<T>()
```

Type parameters:

- `T`

Returns: `DataWriter<T>`

### `DataReader`

Decodes values of type T from text or bytes.

```norm
interface DataReader<T>
```

Type parameters:

- `T`

Related tests:

- `std.test.serialization.mapper::mapperTest()` — mapperTest
  tests/test/serialization/mapper/case.api.json

#### `readString`

Decodes a value from its textual representation.

```norm
T readString(String source)
```

Parameters:

- `source`: `String`
The serialized text to decode.


Returns: `T`

#### `readBytes`

Decodes a value from its binary representation.

```norm
T readBytes(Bytes source)
```

Parameters:

- `source`: `Bytes`
The serialized bytes to decode.


Returns: `T`

### `DataWriter`

Encodes values of type T as text or bytes.

```norm
interface DataWriter<T>
```

Type parameters:

- `T`

Related tests:

- `std.test.serialization.mapper::mapperTest()` — mapperTest
  tests/test/serialization/mapper/case.api.json

#### `writeString`

Encodes a value as text.

```norm
String writeString(T value)
```

Parameters:

- `value`: `T`
The value to encode.


Returns: `String`

#### `writeBytes`

Encodes a value as bytes.

```norm
Bytes writeBytes(T value)
```

Parameters:

- `value`: `T`
The value to encode.


Returns: `Bytes`

## `std.system`

Source: `system/exceptions.norm`

Provides structured failures reported by host-system capabilities.

### `SystemException`

Represents a host-system failure with a stable machine-readable code.

```norm
class SystemException extends Exception
```

#### `code`

The stable machine-readable failure code.

```norm
String code
```

Type: `String`

#### `SystemException`

Creates a host-system failure with a code and readable explanation.

```norm
SystemException(String code, String message)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.


## `std.system`

Source: `system/runtime.norm`

### `System`

Provides system capabilities for the current execution.

```norm
class System
```

#### `runtime`

Returns the current execution's runtime update capability.

```norm
Runtime runtime()
```

Returns: `Runtime`

### `currentSystem`

Returns the system capabilities of the current execution.

```norm
System currentSystem()
```

Returns: `System`

## `std.testing`

Source: `testing/output.norm`

Provides assertions and expected-output helpers for Norm tests.

### `expectedOutputLines`

Registers each supplied string as the next expected output line.

```norm
Void expectedOutputLines(Iterable<String> lines)
```

Parameters:

- `lines`: `Iterable<String>`
The expected lines in output order.


Returns: `Void`

## `std.testing`

Source: `testing/predicates.norm`

### `equal`

Reports whether an actual value equals the expected value.

```norm
Boolean equal<T>(T actual, T expected)
```

Type parameters:

- `T`

Parameters:

- `actual`: `T`
The value produced by the test subject.

- `expected`: `T`
The value required by the test.


Returns: `Boolean`

Related tests:

- `std.test.testing.testing_predicates::testingPredicatesTest()` — testingPredicatesTest
  tests/test/testing/testing_predicates/case.api.json

### `notEqual`

Reports whether an actual value differs from the expected value.

```norm
Boolean notEqual<T>(T actual, T expected)
```

Type parameters:

- `T`

Parameters:

- `actual`: `T`
The value produced by the test subject.

- `expected`: `T`
The value that must not match.


Returns: `Boolean`

Related tests:

- `std.test.testing.testing_predicates::testingPredicatesTest()` — testingPredicatesTest
  tests/test/testing/testing_predicates/case.api.json

### `isTrue`

Returns the supplied Boolean for a positive truth assertion.

```norm
Boolean isTrue(Boolean actual)
```

Parameters:

- `actual`: `Boolean`
The Boolean value under test.


Returns: `Boolean`

Related tests:

- `std.test.testing.testing_predicates::testingPredicatesTest()` — testingPredicatesTest
  tests/test/testing/testing_predicates/case.api.json

### `isFalse`

Reports whether the supplied Boolean is false.

```norm
Boolean isFalse(Boolean actual)
```

Parameters:

- `actual`: `Boolean`
The Boolean value under test.


Returns: `Boolean`

Related tests:

- `std.test.testing.testing_predicates::testingPredicatesTest()` — testingPredicatesTest
  tests/test/testing/testing_predicates/case.api.json

## `std.testing`

Source: `testing/tests.norm`

### `Test`

Marks an independently executable, zero-argument Void test function and its tested declarations.

```norm
annotation Test implements FunctionTarget, BinaryRetention
```

#### `types`

Types whose behavior this test verifies.

```norm
List<Class<?>>? types
```

Type: `List<Class<?>>?`

#### `functions`

Functions whose behavior this test verifies.

```norm
List<Function<?>>? functions
```

Type: `List<Function<?>>?`

#### `fields`

Fields whose behavior this test verifies.

```norm
List<Field<?, ?>>? fields
```

Type: `List<Field<?, ?>>?`

## `std.text`

Source: `text/builders.norm`

Provides text construction and Unicode normalization operations.

### `repeat`

Concatenates a string with itself the requested number of times.

```norm
String repeat(String value, Integer count)
```

Parameters:

- `value`: `String`
The string to repeat.

- `count`: `Integer`
The number of repetitions.


Returns: `String`

Related tests:

- `std.test.integration.edge_cases::edgeCasesTest()` — edgeCasesTest
  tests/test/integration/edge_cases/case.api.json
- `std.test.text.text::textTest()` — textTest
  tests/test/text/text/case.api.json

### `join`

Joins strings in list order with a separator between adjacent values.

```norm
String join(List<String> values, String separator)
```

Parameters:

- `values`: `List<String>`
The strings to join.

- `separator`: `String`
The string inserted between adjacent values.


Returns: `String`

Related tests:

- `std.test.integration.edge_cases::edgeCasesTest()` — edgeCasesTest
  tests/test/integration/edge_cases/case.api.json
- `std.test.text.text::textTest()` — textTest
  tests/test/text/text/case.api.json

### `fromCodePoints`

Builds a string from Unicode code points in array order.

```norm
String fromCodePoints(Array<CodePoint> values)
```

Parameters:

- `values`: `Array<CodePoint>`
The Unicode code points to append.


Returns: `String`

## `std.text`

Source: `text/normalization.norm`

### `Normalization`

Selects NFC, NFD, NFKC, or NFKD Unicode normalization.

```norm
enum Normalization
```

#### `Nfc`

```norm
Nfc
```

#### `Nfd`

```norm
Nfd
```

#### `Nfkc`

```norm
Nfkc
```

#### `Nfkd`

```norm
Nfkd
```

### `normalize`

Returns a string normalized to the selected Unicode form.

```norm
String normalize(String value, Normalization form)
```

Parameters:

- `value`: `String`
The string to normalize.

- `form`: `Normalization`
The normalization form to produce.


Returns: `String`

### `isNormalized`

Reports whether a string already has the selected Unicode normalization form.

```norm
Boolean isNormalized(String value, Normalization form)
```

Parameters:

- `value`: `String`
The string to inspect.

- `form`: `Normalization`
The normalization form to test.


Returns: `Boolean`

## `std.time`

Source: `time/core.norm`

Provides normalized durations, instants, clocks, and typed time failures.

### `TimeOperation`

Identifies clock access and temporal value construction operations.

```norm
enum TimeOperation
```

#### `Now`

```norm
Now
```

#### `CreateDuration`

```norm
CreateDuration
```

#### `CreateInstant`

```norm
CreateInstant
```

### `TimeFailure`

Classifies unavailable clocks and invalid duration or instant components.

```norm
enum TimeFailure
```

#### `ClockUnavailable`

```norm
ClockUnavailable
```

#### `InvalidDuration`

```norm
InvalidDuration
```

#### `InvalidInstant`

```norm
InvalidInstant
```

### `TimeException`

Reports a typed clock or temporal value construction failure.

```norm
class TimeException extends SystemException
```

#### `operation`

The time operation that failed.

```norm
TimeOperation operation
```

Type: `TimeOperation`

#### `reason`

The time failure category.

```norm
TimeFailure reason
```

Type: `TimeFailure`

#### `TimeException`

Creates a typed time failure.

```norm
TimeException(String code, String message, TimeOperation operation, TimeFailure reason)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `operation`: `TimeOperation`
The time operation that failed.

- `reason`: `TimeFailure`
The time failure category.


### `Duration`

Represents a normalized signed duration using seconds and a non-negative nanosecond fraction.

```norm
value Duration
```

Related tests:

- `std.test.time.foundation::foundationTest()` — foundationTest
  tests/test/time/foundation/case.api.json

#### `seconds`

Returns the whole signed seconds component.

```norm
Long seconds()
```

Returns: `Long`

#### `nanoseconds`

Returns the nanosecond fraction in the range 0 through 999999999.

```norm
Integer nanoseconds()
```

Returns: `Integer`

### `Instant`

Represents an instant on the Unix time line using an epoch second and nanosecond fraction.

```norm
interface Instant
```

Related tests:

- `std.test.time.foundation::foundationTest()` — foundationTest
  tests/test/time/foundation/case.api.json

#### `epochSecond`

Returns the whole seconds since the Unix epoch.

```norm
Long epochSecond()
```

Returns: `Long`

#### `nanosecond`

Returns the nanosecond fraction in the range 0 through 999999999.

```norm
Integer nanosecond()
```

Returns: `Integer`

### `duration`

Creates a normalized duration from a seconds component and nanosecond fraction.

```norm
Duration duration(Long seconds, Integer nanoseconds)
```

Parameters:

- `seconds`: `Long`
The whole signed seconds component.

- `nanoseconds`: `Integer`
The nanosecond fraction from 0 through 999999999.


Returns: `Duration`

Related tests:

- `std.test.time.foundation::foundationTest()` — foundationTest
  tests/test/time/foundation/case.api.json

### `instant`

Creates an instant from a Unix epoch second and nanosecond fraction.

```norm
Instant instant(Long epochSecond, Integer nanosecond)
```

Parameters:

- `epochSecond`: `Long`
The whole seconds since the Unix epoch.

- `nanosecond`: `Integer`
The nanosecond fraction from 0 through 999999999.


Returns: `Instant`

### `Clock`

Supplies the current instant from a time source.

```norm
interface Clock
```

Related tests:

- `std.test.time.foundation::foundationTest()` — foundationTest
  tests/test/time/foundation/case.api.json

#### `now`

Returns the current instant from this clock.

```norm
Instant now()
```

Returns: `Instant`

### `systemClock`

Returns a clock backed by the host system time source.

```norm
Clock systemClock()
```

Returns: `Clock`

Related tests:

- `std.test.time.foundation::foundationTest()` — foundationTest
  tests/test/time/foundation/case.api.json

## `std.validation`

Source: `validation/constraints.norm`

Provides typed parameter and field constraints with structured violation metadata.

### `ConstraintLocation`

Identifies whether a constraint is evaluating a parameter or a field.

```norm
enum ConstraintLocation
```

Related tests:

- `std.test.validation.field_constraints::fieldConstraintsTest()` — fieldConstraintsTest
  tests/test/validation/field_constraints/case.api.json
- `std.test.validation.violation_metadata::violationMetadataTest()` — violationMetadataTest
  tests/test/validation/violation_metadata/case.api.json

#### `Parameter`

```norm
Parameter
```

#### `Field`

```norm
Field
```

### `ConstraintContext`

Carries the declaration references available while evaluating a constraint.

```norm
value ConstraintContext
```

#### `location`

The kind of declaration receiving the constrained value.

```norm
ConstraintLocation location
```

Type: `ConstraintLocation`

#### `functionReference`

The containing function for a parameter constraint, otherwise null.

```norm
Function<?>? functionReference
```

Type: `Function<?>?`

#### `parameterReference`

The constrained parameter declaration, otherwise null.

```norm
Parameter<?>? parameterReference
```

Type: `Parameter<?>?`

#### `fieldReference`

The constrained field declaration, otherwise null.

```norm
Field<?, ?>? fieldReference
```

Type: `Field<?, ?>?`

### `ConstraintViolation`

Reports a value that failed a parameter or field constraint.

```norm
class ConstraintViolation extends Exception
```

Related tests:

- `std.test.json.construction::constructionTest()` — constructionTest
  tests/test/json/construction/case.api.json
- `std.test.validation.builtin_constraints::builtinConstraintsTest()` — builtinConstraintsTest
  tests/test/validation/builtin_constraints/case.api.json
- `std.test.validation.custom_constraint::customConstraintTest()` — customConstraintTest
  tests/test/validation/custom_constraint/case.api.json
- `std.test.validation.field_constraints::fieldConstraintsTest()` — fieldConstraintsTest
  tests/test/validation/field_constraints/case.api.json
- `std.test.validation.parameter_constraints::parameterConstraintsTest()` — parameterConstraintsTest
  tests/test/validation/parameter_constraints/case.api.json
- `std.test.validation.unicode_sizes::unicodeSizesTest()` — unicodeSizesTest
  tests/test/validation/unicode_sizes/case.api.json
- `std.test.validation.violation_metadata::violationMetadataTest()` — violationMetadataTest
  tests/test/validation/violation_metadata/case.api.json
- `std.test.xml.construction::constructionTest()` — constructionTest
  tests/test/xml/construction/case.api.json
- `std.test.yaml.construction::constructionTest()` — constructionTest
  tests/test/yaml/construction/case.api.json

#### `location`

The kind of declaration that rejected the value.

```norm
ConstraintLocation location
```

Type: `ConstraintLocation`

#### `functionReference`

The containing function for a parameter violation, otherwise null.

```norm
Function<?>? functionReference
```

Type: `Function<?>?`

#### `parameterReference`

The parameter that rejected the value, otherwise null.

```norm
Parameter<?>? parameterReference
```

Type: `Parameter<?>?`

#### `fieldReference`

The field that rejected the value, otherwise null.

```norm
Field<?, ?>? fieldReference
```

Type: `Field<?, ?>?`

#### `code`

The stable machine-readable constraint code.

```norm
String code
```

Type: `String`

#### `ConstraintViolation`

Creates a violation tied to its constrained declaration.

```norm
ConstraintViolation(ConstraintLocation location, Function<?>? functionReference, Parameter<?>? parameterReference, Field<?, ?>? fieldReference, String code, String message)
```

Parameters:

- `location`: `ConstraintLocation`
The kind of declaration that rejected the value.

- `functionReference`: `Function<?>?`
The containing function for a parameter violation, otherwise null.

- `parameterReference`: `Parameter<?>?`
The parameter that rejected the value, otherwise null.

- `fieldReference`: `Field<?, ?>?`
The field that rejected the value, otherwise null.

- `code`: `String`
The stable machine-readable constraint code.

- `message`: `String`
The human-readable constraint message.


### `ConstraintDefinitionException`

Reports an invalid constraint configuration before value validation can proceed.

```norm
class ConstraintDefinitionException extends Exception
```

Related tests:

- `std.test.validation.invalid_configuration::invalidConfigurationTest()` — invalidConfigurationTest
  tests/test/validation/invalid_configuration/case.api.json

#### `code`

The stable machine-readable constraint code.

```norm
String code
```

Type: `String`

#### `ConstraintDefinitionException`

Creates a failure for an invalid constraint definition.

```norm
ConstraintDefinitionException(String code, String message)
```

Parameters:

- `code`: `String`
The stable machine-readable constraint code.

- `message`: `String`
The human-readable configuration failure explanation.


### `Constraint`

Defines a reusable typed constraint for parameter binding and field writes.

```norm
interface Constraint<T> extends ParameterInterceptor<T>, FieldInterceptor<T>, SourceRetention
```

Type parameters:

- `T`

Related tests:

- `std.test.validation.custom_constraint::customConstraintTest()` — customConstraintTest
  tests/test/validation/custom_constraint/case.api.json

#### `isValid`

Reports whether a value satisfies this constraint.

```norm
Boolean isValid(T value)
```

Parameters:

- `value`: `T`
The value to validate.


Returns: `Boolean`

#### `code`

Returns the stable machine-readable code for this constraint.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the human-readable violation message for this constraint.

```norm
String message()
```

Returns: `String`

#### `validate`

Returns a valid value unchanged or throws a declaration-aware violation.

```norm
T validate(ConstraintContext context, T value)
```

Parameters:

- `context`: `ConstraintContext`
The declaration context for the validation.

- `value`: `T`
The value to validate.


Returns: `T`

#### `before`

Validates an argument before it is bound to a constrained parameter.

```norm
T before(ParameterContext context, T value)
```

Parameters:

- `context`: `ParameterContext`
Identifies the constrained parameter declaration.

- `value`: `T`
The argument to validate.


Returns: `T`

#### `before`

Validates a value before it is stored in a constrained field.

```norm
T before(FieldContext context, T value)
```

Parameters:

- `context`: `FieldContext`
Identifies the constrained field declaration.

- `value`: `T`
The value to validate.


Returns: `T`

### `AssertTrue`

Requires a Boolean value to be true.

```norm
annotation AssertTrue implements Constraint<Boolean>
```

Related tests:

- `std.test.validation.parameter_constraints::parameterConstraintsTest()` — parameterConstraintsTest
  tests/test/validation/parameter_constraints/case.api.json

#### `isValid`

Reports whether the Boolean value is true.

```norm
Boolean isValid(Boolean value)
```

Parameters:

- `value`: `Boolean`
The Boolean value to validate.


Returns: `Boolean`

#### `code`

Returns the assert_true violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a false value.

```norm
String message()
```

Returns: `String`

### `AssertFalse`

Requires a Boolean value to be false.

```norm
annotation AssertFalse implements Constraint<Boolean>
```

Related tests:

- `std.test.validation.builtin_constraints::builtinConstraintsTest()` — builtinConstraintsTest
  tests/test/validation/builtin_constraints/case.api.json

#### `isValid`

Reports whether the Boolean value is false.

```norm
Boolean isValid(Boolean value)
```

Parameters:

- `value`: `Boolean`
The Boolean value to validate.


Returns: `Boolean`

#### `code`

Returns the assert_false violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a true value.

```norm
String message()
```

Returns: `String`

### `Min`

Requires an integer to be greater than or equal to a configured minimum.

```norm
annotation Min implements Constraint<Integer>
```

Related tests:

- `std.test.json.construction::constructionTest()` — constructionTest
  tests/test/json/construction/case.api.json
- `std.test.validation.parameter_constraints::parameterConstraintsTest()` — parameterConstraintsTest
  tests/test/validation/parameter_constraints/case.api.json
- `std.test.xml.construction::constructionTest()` — constructionTest
  tests/test/xml/construction/case.api.json
- `std.test.yaml.construction::constructionTest()` — constructionTest
  tests/test/yaml/construction/case.api.json

#### `minimum`

The inclusive lower bound.

```norm
Integer minimum
```

Type: `Integer`

#### `Min`

Creates an inclusive minimum constraint.

```norm
Min(Integer value)
```

Parameters:

- `value`: `Integer`
The inclusive lower bound.


#### `isValid`

Reports whether an integer is at least the configured minimum.

```norm
Boolean isValid(Integer value)
```

Parameters:

- `value`: `Integer`
The integer to validate.


Returns: `Boolean`

#### `code`

Returns the min violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for an integer below the minimum.

```norm
String message()
```

Returns: `String`

### `Max`

Requires an integer to be less than or equal to a configured maximum.

```norm
annotation Max implements Constraint<Integer>
```

Related tests:

- `std.test.validation.field_constraints::fieldConstraintsTest()` — fieldConstraintsTest
  tests/test/validation/field_constraints/case.api.json
- `std.test.validation.parameter_constraints::parameterConstraintsTest()` — parameterConstraintsTest
  tests/test/validation/parameter_constraints/case.api.json

#### `maximum`

The inclusive upper bound.

```norm
Integer maximum
```

Type: `Integer`

#### `Max`

Creates an inclusive maximum constraint.

```norm
Max(Integer value)
```

Parameters:

- `value`: `Integer`
The inclusive upper bound.


#### `isValid`

Reports whether an integer is at most the configured maximum.

```norm
Boolean isValid(Integer value)
```

Parameters:

- `value`: `Integer`
The integer to validate.


Returns: `Boolean`

#### `code`

Returns the max violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for an integer above the maximum.

```norm
String message()
```

Returns: `String`

### `Negative`

Requires an integer to be less than zero.

```norm
annotation Negative implements Constraint<Integer>
```

Related tests:

- `std.test.validation.violation_metadata::violationMetadataTest()` — violationMetadataTest
  tests/test/validation/violation_metadata/case.api.json

#### `isValid`

Reports whether an integer is negative.

```norm
Boolean isValid(Integer value)
```

Parameters:

- `value`: `Integer`
The integer to validate.


Returns: `Boolean`

#### `code`

Returns the negative violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a non-negative integer.

```norm
String message()
```

Returns: `String`

### `NegativeOrZero`

Requires an integer to be less than or equal to zero.

```norm
annotation NegativeOrZero implements Constraint<Integer>
```

Related tests:

- `std.test.validation.builtin_constraints::builtinConstraintsTest()` — builtinConstraintsTest
  tests/test/validation/builtin_constraints/case.api.json

#### `isValid`

Reports whether an integer is negative or zero.

```norm
Boolean isValid(Integer value)
```

Parameters:

- `value`: `Integer`
The integer to validate.


Returns: `Boolean`

#### `code`

Returns the negative_or_zero violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a positive integer.

```norm
String message()
```

Returns: `String`

### `Positive`

Requires an integer to be greater than zero.

```norm
annotation Positive implements Constraint<Integer>
```

Related tests:

- `std.test.validation.builtin_constraints::builtinConstraintsTest()` — builtinConstraintsTest
  tests/test/validation/builtin_constraints/case.api.json
- `std.test.validation.parameter_constraints::parameterConstraintsTest()` — parameterConstraintsTest
  tests/test/validation/parameter_constraints/case.api.json

#### `isValid`

Reports whether an integer is positive.

```norm
Boolean isValid(Integer value)
```

Parameters:

- `value`: `Integer`
The integer to validate.


Returns: `Boolean`

#### `code`

Returns the positive violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a non-positive integer.

```norm
String message()
```

Returns: `String`

### `PositiveOrZero`

Requires an integer to be greater than or equal to zero.

```norm
annotation PositiveOrZero implements Constraint<Integer>
```

Related tests:

- `std.test.validation.field_constraints::fieldConstraintsTest()` — fieldConstraintsTest
  tests/test/validation/field_constraints/case.api.json

#### `isValid`

Reports whether an integer is positive or zero.

```norm
Boolean isValid(Integer value)
```

Parameters:

- `value`: `Integer`
The integer to validate.


Returns: `Boolean`

#### `code`

Returns the positive_or_zero violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a negative integer.

```norm
String message()
```

Returns: `String`

### `NotEmpty`

Requires a string to contain at least one code point.

```norm
annotation NotEmpty implements Constraint<String>
```

Related tests:

- `std.test.validation.field_constraints::fieldConstraintsTest()` — fieldConstraintsTest
  tests/test/validation/field_constraints/case.api.json

#### `isValid`

Reports whether a string is non-empty.

```norm
Boolean isValid(String value)
```

Parameters:

- `value`: `String`
The string to validate.


Returns: `Boolean`

#### `code`

Returns the not_empty violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for an empty string.

```norm
String message()
```

Returns: `String`

### `NotBlank`

Requires a string to contain at least one non-whitespace code point.

```norm
annotation NotBlank implements Constraint<String>
```

Related tests:

- `std.test.validation.parameter_constraints::parameterConstraintsTest()` — parameterConstraintsTest
  tests/test/validation/parameter_constraints/case.api.json

#### `isValid`

Reports whether a string contains a non-whitespace code point.

```norm
Boolean isValid(String value)
```

Parameters:

- `value`: `String`
The string to validate.


Returns: `Boolean`

#### `code`

Returns the not_blank violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a blank string.

```norm
String message()
```

Returns: `String`

### `CodePointSize`

Requires a string's Unicode code point count to fall within an inclusive interval.

```norm
annotation CodePointSize implements Constraint<String>
```

Related tests:

- `std.test.validation.invalid_configuration::invalidConfigurationTest()` — invalidConfigurationTest
  tests/test/validation/invalid_configuration/case.api.json
- `std.test.validation.unicode_sizes::unicodeSizesTest()` — unicodeSizesTest
  tests/test/validation/unicode_sizes/case.api.json

#### `minimum`

The inclusive minimum code point count.

```norm
Integer minimum
```

Type: `Integer`

#### `maximum`

The inclusive maximum code point count.

```norm
Integer maximum
```

Type: `Integer`

#### `CodePointSize`

Creates an inclusive Unicode code point count constraint.

```norm
CodePointSize(Integer minimum, Integer maximum)
```

Parameters:

- `minimum`: `Integer`
The non-negative inclusive minimum code point count.

- `maximum`: `Integer`
The inclusive maximum code point count, not less than minimum.


#### `isValid`

Reports whether a string's code point count is inside the configured interval.

```norm
Boolean isValid(String value)
```

Parameters:

- `value`: `String`
The string to validate.


Returns: `Boolean`

#### `code`

Returns the code_point_size violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a code point count outside the interval.

```norm
String message()
```

Returns: `String`

### `GraphemeSize`

Requires a string's grapheme cluster count to fall within an inclusive interval.

```norm
annotation GraphemeSize implements Constraint<String>
```

Related tests:

- `std.test.validation.invalid_configuration::invalidConfigurationTest()` — invalidConfigurationTest
  tests/test/validation/invalid_configuration/case.api.json
- `std.test.validation.unicode_sizes::unicodeSizesTest()` — unicodeSizesTest
  tests/test/validation/unicode_sizes/case.api.json

#### `minimum`

The inclusive minimum grapheme cluster count.

```norm
Integer minimum
```

Type: `Integer`

#### `maximum`

The inclusive maximum grapheme cluster count.

```norm
Integer maximum
```

Type: `Integer`

#### `GraphemeSize`

Creates an inclusive grapheme cluster count constraint.

```norm
GraphemeSize(Integer minimum, Integer maximum)
```

Parameters:

- `minimum`: `Integer`
The non-negative inclusive minimum grapheme cluster count.

- `maximum`: `Integer`
The inclusive maximum grapheme cluster count, not less than minimum.


#### `isValid`

Reports whether a string's grapheme count is inside the configured interval.

```norm
Boolean isValid(String value)
```

Parameters:

- `value`: `String`
The string to validate.


Returns: `Boolean`

#### `code`

Returns the grapheme_size violation code.

```norm
String code()
```

Returns: `String`

#### `message`

Returns the violation message for a grapheme count outside the interval.

```norm
String message()
```

Returns: `String`

## `std.websocket`

Source: `websocket/client.norm`

Provides resource-owned WebSocket client connections and typed message events.

### `WebSocketOperation`

Identifies the WebSocket operation that failed.

```norm
enum WebSocketOperation
```

#### `Connect`

```norm
Connect
```

#### `Send`

```norm
Send
```

#### `Receive`

```norm
Receive
```

#### `Close`

```norm
Close
```

### `WebSocketFailure`

Classifies WebSocket connection, protocol, cancellation, and capacity failures.

```norm
enum WebSocketFailure
```

#### `InvalidRequest`

```norm
InvalidRequest
```

#### `Connect`

```norm
Connect
```

#### `Tls`

```norm
Tls
```

#### `Handshake`

```norm
Handshake
```

#### `Protocol`

```norm
Protocol
```

#### `Timeout`

```norm
Timeout
```

#### `Cancelled`

```norm
Cancelled
```

#### `Closed`

```norm
Closed
```

#### `Busy`

```norm
Busy
```

#### `MessageTooLarge`

```norm
MessageTooLarge
```

#### `Io`

```norm
Io
```

### `WebSocketException`

Reports a typed WebSocket failure with a stable code and endpoint.

```norm
class WebSocketException extends IOException
```

#### `operation`

The failed operation.

```norm
WebSocketOperation operation
```

Type: `WebSocketOperation`

#### `reason`

The failure category.

```norm
WebSocketFailure reason
```

Type: `WebSocketFailure`

#### `uri`

The connection endpoint.

```norm
Uri uri
```

Type: `Uri`

#### `WebSocketException`

Creates a WebSocket failure.

```norm
WebSocketException(String code, String message, WebSocketOperation operation, WebSocketFailure reason, Uri uri)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The failure description.

- `operation`: `WebSocketOperation`
The failed operation.

- `reason`: `WebSocketFailure`
The failure category.

- `uri`: `Uri`
The connection endpoint.


### `WebSocketEvent`

A complete data message, Pong reply, or peer close notification. Ping is answered by the transport.

```norm
enum WebSocketEvent
```

#### `Text`

```norm
Text(String text)
```

Parameters:

- `text`: `String`

#### `Binary`

```norm
Binary(Bytes data)
```

Parameters:

- `data`: `Bytes`

#### `Pong`

```norm
Pong(Bytes data)
```

Parameters:

- `data`: `Bytes`

#### `Closed`

```norm
Closed(Integer code, String reason)
```

Parameters:

- `code`: `Integer`
- `reason`: `String`

### `WebSocket`

A single WebSocket connection. Operations may run in existing Tasks; only one receive may be active.

```norm
interface WebSocket extends Resource
```

#### `subprotocol`

Returns the negotiated subprotocol, or an empty string.

```norm
String subprotocol()
```

Returns: `String`

#### `sendText`

Sends one complete text message within the timeout. In-flight send timeout or cancellation releases the connection.

```norm
Void sendText(String text, Duration timeout)
```

Parameters:

- `text`: `String`
The complete text message.

- `timeout`: `Duration`
The positive operation timeout, including send queue wait.


Returns: `Void`

#### `sendBinary`

Sends one complete binary message within the timeout.

```norm
Void sendBinary(Bytes data, Duration timeout)
```

Parameters:

- `data`: `Bytes`
The complete binary message.

- `timeout`: `Duration`
The positive operation timeout, including send queue wait.


Returns: `Void`

#### `ping`

Sends at most 125 bytes as a Ping. A reply is delivered as a Pong event.

```norm
Void ping(Bytes data, Duration timeout)
```

Parameters:

- `data`: `Bytes`
The Ping payload, at most 125 bytes.

- `timeout`: `Duration`
The positive send timeout; it does not wait for Pong.


Returns: `Void`

#### `receive`

Receives one complete event. Timeout or cancellation leaves queued data available for the next receive.

```norm
WebSocketEvent receive(Duration timeout)
```

Parameters:

- `timeout`: `Duration`
The positive wait timeout for one event.


Returns: `WebSocketEvent`

#### `finish`

Sends Close, discards remaining data, waits for peer Close within the timeout, and releases the connection.

```norm
Void finish(Integer code, String reason, Duration timeout)
```

Parameters:

- `code`: `Integer`
The protocol close status code.

- `reason`: `String`
The close reason, at most 123 UTF-8 bytes.

- `timeout`: `Duration`
The positive total timeout for the close handshake.


Returns: `Void`

### `connectWebSocket`

Connects to a WS or WSS endpoint. Bounds each complete incoming and outgoing message; defaults to 1 MiB. Does not reconnect automatically.

```norm
WebSocket connectWebSocket(Uri uri, Duration timeout, HeaderMap headers, Array<String> subprotocols, Integer maximumMessageBytes)
```

Parameters:

- `uri`: `Uri`
The absolute WS or WSS endpoint.

- `timeout`: `Duration`
The positive opening handshake timeout.

- `headers`: `HeaderMap`
Additional handshake headers; protocol-owned headers are managed by the transport.

- `subprotocols`: `Array<String>`
Offered subprotocols in preference order.

- `maximumMessageBytes`: `Integer`
The positive maximum complete data message size in bytes, using UTF-8 for text.


Returns: `WebSocket`

## `std.xml`

Source: `xml/xml.norm`

Provides typed XML serialization and XML-specific field metadata.

### `XmlAttribute`

Serializes the annotated field as an XML attribute instead of an element.

```norm
annotation XmlAttribute implements FieldTarget, RuntimeRetention
```

Related tests:

- `std.test.xml.round_trip::roundTripTest()` — roundTripTest
  tests/test/xml/round_trip/case.api.json

### `XmlException`

Reports an XML encoding, decoding, or mapping failure with source location data.

```norm
class XmlException extends Exception
```

Related tests:

- `std.test.xml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/xml/failure_matrix/case.api.json

#### `code`

The stable machine-readable failure code.

```norm
String code
```

Type: `String`

#### `path`

The structural path at which the failure occurred.

```norm
String path
```

Type: `String`

#### `offset`

The zero-based source offset associated with the failure.

```norm
Integer offset
```

Type: `Integer`

#### `line`

The one-based source line associated with the failure.

```norm
Integer line
```

Type: `Integer`

#### `column`

The one-based source column associated with the failure.

```norm
Integer column
```

Type: `Integer`

#### `XmlException`

Creates an XML failure with structural and textual location details.

```norm
XmlException(String code, String message, String path, Integer offset, Integer line, Integer column)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `path`: `String`
The structural path at which the failure occurred.

- `offset`: `Integer`
The zero-based source offset associated with the failure.

- `line`: `Integer`
The one-based source line associated with the failure.

- `column`: `Integer`
The one-based source column associated with the failure.


### `XmlMapper`

Creates XML readers and writers for requested value types.

```norm
value XmlMapper implements DataMapper
```

Related tests:

- `std.test.serialization.mapper::mapperTest()` — mapperTest
  tests/test/serialization/mapper/case.api.json

#### `reader`

Creates an XML reader for values of type T.

```norm
DataReader<T> reader<T>()
```

Type parameters:

- `T`

Returns: `DataReader<T>`

#### `writer`

Creates an XML writer for values of type T.

```norm
DataWriter<T> writer<T>()
```

Type parameters:

- `T`

Returns: `DataWriter<T>`

### `XmlReader`

Decodes XML text and bytes into values of type T.

```norm
value XmlReader<T> implements DataReader<T>
```

Type parameters:

- `T`

#### `readString`

Decodes XML text into a value of type T.

```norm
T readString(String source)
```

Parameters:

- `source`: `String`
The XML text to decode.


Returns: `T`

#### `readBytes`

Decodes UTF-8 XML bytes into a value of type T.

```norm
T readBytes(Bytes source)
```

Parameters:

- `source`: `Bytes`
The UTF-8 XML bytes to decode.


Returns: `T`

### `XmlWriter`

Encodes values of type T as XML text and UTF-8 bytes.

```norm
value XmlWriter<T> implements DataWriter<T>
```

Type parameters:

- `T`

#### `writeString`

Encodes a value as XML text.

```norm
String writeString(T value)
```

Parameters:

- `value`: `T`
The value to encode.


Returns: `String`

#### `writeBytes`

Encodes a value as UTF-8 XML bytes.

```norm
Bytes writeBytes(T value)
```

Parameters:

- `value`: `T`
The value to encode.


Returns: `Bytes`

### `toXml`

Encodes a value as XML text.

```norm
extension String toXml<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The value to encode.


Returns: `String`

Related tests:

- `std.test.xml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/xml/failure_matrix/case.api.json
- `std.test.xml.round_trip::roundTripTest()` — roundTripTest
  tests/test/xml/round_trip/case.api.json
- `std.test.xml.structures::structuresTest()` — structuresTest
  tests/test/xml/structures/case.api.json

### `fromXml`

Decodes XML text into a value of type T.

```norm
extension T fromXml<T>(String value)
```

Type parameters:

- `T`

Parameters:

- `value`: `String`
The XML text to decode.


Returns: `T`

Related tests:

- `std.test.xml.construction::constructionTest()` — constructionTest
  tests/test/xml/construction/case.api.json
- `std.test.xml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/xml/failure_matrix/case.api.json
- `std.test.xml.round_trip::roundTripTest()` — roundTripTest
  tests/test/xml/round_trip/case.api.json
- `std.test.xml.structures::structuresTest()` — structuresTest
  tests/test/xml/structures/case.api.json

### `toXmlBytes`

Encodes a value as UTF-8 XML bytes.

```norm
extension Bytes toXmlBytes<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The value to encode.


Returns: `Bytes`

### `fromXmlBytes`

Decodes UTF-8 XML bytes into a value of type T.

```norm
extension T fromXmlBytes<T>(Bytes value)
```

Type parameters:

- `T`

Parameters:

- `value`: `Bytes`
The UTF-8 XML bytes to decode.


Returns: `T`

## `std.yaml`

Source: `yaml/yaml.norm`

Provides typed YAML serialization for text and UTF-8 byte representations.

### `YamlException`

Reports a YAML encoding, decoding, or mapping failure with source location data.

```norm
class YamlException extends Exception
```

Related tests:

- `std.test.yaml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/yaml/failure_matrix/case.api.json
- `std.test.yaml.round_trip::roundTripTest()` — roundTripTest
  tests/test/yaml/round_trip/case.api.json

#### `code`

The stable machine-readable failure code.

```norm
String code
```

Type: `String`

#### `path`

The structural path at which the failure occurred.

```norm
String path
```

Type: `String`

#### `offset`

The zero-based source offset associated with the failure.

```norm
Integer offset
```

Type: `Integer`

#### `line`

The one-based source line associated with the failure.

```norm
Integer line
```

Type: `Integer`

#### `column`

The one-based source column associated with the failure.

```norm
Integer column
```

Type: `Integer`

#### `YamlException`

Creates a YAML failure with structural and textual location details.

```norm
YamlException(String code, String message, String path, Integer offset, Integer line, Integer column)
```

Parameters:

- `code`: `String`
The stable machine-readable failure code.

- `message`: `String`
The human-readable failure explanation.

- `path`: `String`
The structural path at which the failure occurred.

- `offset`: `Integer`
The zero-based source offset associated with the failure.

- `line`: `Integer`
The one-based source line associated with the failure.

- `column`: `Integer`
The one-based source column associated with the failure.


### `YamlMapper`

Creates YAML readers and writers for requested value types.

```norm
value YamlMapper implements DataMapper
```

Related tests:

- `std.test.serialization.mapper::mapperTest()` — mapperTest
  tests/test/serialization/mapper/case.api.json

#### `reader`

Creates a YAML reader for values of type T.

```norm
DataReader<T> reader<T>()
```

Type parameters:

- `T`

Returns: `DataReader<T>`

#### `writer`

Creates a YAML writer for values of type T.

```norm
DataWriter<T> writer<T>()
```

Type parameters:

- `T`

Returns: `DataWriter<T>`

### `YamlReader`

Decodes YAML text and bytes into values of type T.

```norm
value YamlReader<T> implements DataReader<T>
```

Type parameters:

- `T`

#### `readString`

Decodes YAML text into a value of type T.

```norm
T readString(String source)
```

Parameters:

- `source`: `String`
The YAML text to decode.


Returns: `T`

#### `readBytes`

Decodes UTF-8 YAML bytes into a value of type T.

```norm
T readBytes(Bytes source)
```

Parameters:

- `source`: `Bytes`
The UTF-8 YAML bytes to decode.


Returns: `T`

### `YamlWriter`

Encodes values of type T as YAML text and UTF-8 bytes.

```norm
value YamlWriter<T> implements DataWriter<T>
```

Type parameters:

- `T`

#### `writeString`

Encodes a value as YAML text.

```norm
String writeString(T value)
```

Parameters:

- `value`: `T`
The value to encode.


Returns: `String`

#### `writeBytes`

Encodes a value as UTF-8 YAML bytes.

```norm
Bytes writeBytes(T value)
```

Parameters:

- `value`: `T`
The value to encode.


Returns: `Bytes`

### `toYaml`

Encodes a value as YAML text.

```norm
extension String toYaml<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The value to encode.


Returns: `String`

Related tests:

- `std.test.yaml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/yaml/failure_matrix/case.api.json
- `std.test.yaml.output::outputTest()` — outputTest
  tests/test/yaml/output/case.api.json
- `std.test.yaml.round_trip::roundTripTest()` — roundTripTest
  tests/test/yaml/round_trip/case.api.json
- `std.test.yaml.structures::structuresTest()` — structuresTest
  tests/test/yaml/structures/case.api.json

### `fromYaml`

Decodes YAML text into a value of type T.

```norm
extension T fromYaml<T>(String value)
```

Type parameters:

- `T`

Parameters:

- `value`: `String`
The YAML text to decode.


Returns: `T`

Related tests:

- `std.test.yaml.construction::constructionTest()` — constructionTest
  tests/test/yaml/construction/case.api.json
- `std.test.yaml.failure_matrix::failureMatrixTest()` — failureMatrixTest
  tests/test/yaml/failure_matrix/case.api.json
- `std.test.yaml.round_trip::roundTripTest()` — roundTripTest
  tests/test/yaml/round_trip/case.api.json
- `std.test.yaml.structures::structuresTest()` — structuresTest
  tests/test/yaml/structures/case.api.json

### `toYamlBytes`

Encodes a value as UTF-8 YAML bytes.

```norm
extension Bytes toYamlBytes<T>(T value)
```

Type parameters:

- `T`

Parameters:

- `value`: `T`
The value to encode.


Returns: `Bytes`

### `fromYamlBytes`

Decodes UTF-8 YAML bytes into a value of type T.

```norm
extension T fromYamlBytes<T>(Bytes value)
```

Type parameters:

- `T`

Parameters:

- `value`: `Bytes`
The UTF-8 YAML bytes to decode.


Returns: `T`
<!-- end-component:norm-std -->


## Component: package-standards

Source: `https://github.com/normlanguage/package-standards.git`; revision: `01f419ab14f65793644f1c700feec5768aeda68e`.

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

Source: `https://github.com/normlanguage/registry.git`; revision: `90b4d247fa4f5f2b620924d2cbc0553e89843700`.

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
