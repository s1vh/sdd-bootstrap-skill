# Spec-Driven Development in the Agentic Era

**State of the art as of 4 November 2026**  
**Purpose:** a tool-agnostic reference for understanding, evaluating, and eventually designing Spec-Driven Development workflows for human–AI software engineering.

## Scope, terminology, and executive synthesis

Spec-Driven Development, or **SDD**, is best understood in late 2026 not as a single standardized methodology but as an emerging family of software-development practices in which explicit specifications become first-class operational artifacts for both humans and AI coding agents. GitHub Spec Kit, Kiro, OpenSpec, BMAD, Tessl, Augment and a growing number of smaller projects use overlapping terminology while implementing materially different workflows. The academic literature itself describes the vocabulary as unsettled, and current research explicitly warns that the field has not yet reached academic–industrial consensus. citeturn492537view6turn492537view5turn228400search18

The common denominator is a reversal of the increasingly popular prompt-first or “vibe coding” pattern. Instead of giving an agent an informal request and evaluating whatever implementation emerges, SDD externalizes intent before or during implementation into inspectable artifacts: requirements, constraints, acceptance criteria, architectural decisions, implementation plans, tasks, tests, policies and evidence of verification. GitHub describes this as moving from code as the primary source of truth toward intent as the source of truth; Kiro formalizes feature work as requirements, design and tasks; OpenSpec organizes changes around proposal, specification, design and task artifacts. citeturn628524search3turn492537view8turn287894search2

A crucial distinction is that **“executable specification” has at least two meanings in this literature**. In classical software engineering, an executable specification is directly machine-evaluable, as in Cucumber/Gherkin scenarios, API contracts, formal assertions or property-based tests. In contemporary agentic SDD, a Markdown specification may instead be “executable” in the looser sense that an AI agent can interpret it and generate or modify software from it. Those two kinds of executability should not be conflated: the latter remains probabilistic unless the generated result is checked by deterministic tests, static analysis, formal methods or other validators. citeturn860486search2turn860486search26turn860486search52turn287894search7

A useful conceptual taxonomy proposed in 2026 distinguishes **spec-first**, **spec-anchored** and **spec-as-source** development. In spec-first development, a specification precedes implementation but may later become secondary to the code. In spec-anchored development, specifications remain durable reference artifacts against which the evolving system is checked. In spec-as-source development, maintained specifications are intended to be authoritative enough that substantial portions of implementation can be regenerated or derived from them. This taxonomy is useful, but it is a research proposal rather than an industry standard. citeturn132300academia3

The strongest defensible conclusion today is therefore narrower than some vendor rhetoric: **SDD is a promising way of making intent, constraints and evaluation criteria explicit for agents, but there is not yet strong causal evidence that merely adding specification artifacts reduces defects or rework.** The first peer-reviewed large-scale empirical test found no defect or rework benefit from the kinds of specification artifacts available in its open-source dataset; importantly, that study explicitly notes that it did *not* observe committed outputs from Spec Kit, Kiro or comparable SDD tools, so it cannot be treated as a direct evaluation of those systems. citeturn899470search0

At the same time, several newer results support important components of the SDD hypothesis. Experiments with ambiguous requirements show that ambiguity degrades LLM code-generation performance; repository-level studies show that richer specification quality correlates with some healthier engineering outcomes, although causality is not established; and the new SpecMine corpus demonstrates that specification-centric workflows are already visible at substantial scale in public repositories. citeturn530671view6turn530671view0turn530671view3

The resulting working definition used throughout this reference is:

> **Spec-Driven Development is a software-engineering discipline in which explicit, versionable representations of intent, constraints, design decisions, work decomposition and verification criteria are maintained as operational inputs to human and AI implementation, with feedback loops that reconcile specifications, implementation and evidence over time.**

This definition intentionally does **not** require a particular vendor, model, agent, file layout, command syntax, programming language or degree of automation. That separation is essential for an agnostic implementation because the current tools differ far more in orchestration and persistence than they do in their fundamental need for explicit intent. citeturn287894search34turn970210search20turn970210search26


## Intellectual foundations and what is genuinely new

Modern SDD is new mainly in its **execution model**, not in the idea that software should be driven by explicit requirements and contracts. Requirements engineering has spent decades addressing elicitation, analysis, specification, validation, traceability and change management. ISO/IEC/IEEE 29148:2018 remains the principal international requirements-engineering standard and provides lifecycle guidance for requirements-related activities in systems and software engineering. citeturn860486search1turn860486search15

The problem SDD addresses is therefore not “software engineering never had specifications.” The novelty is that generative models can now consume natural-language and semi-structured specifications as **active execution context**: they can elaborate them, derive plans and tests, perform implementation work, compare code against them and iterate. The 2026 literature frames this as a shift from specifications being primarily communication or verification documents toward specifications acting as a contract substrate through which teams constrain and coordinate autonomous agents. citeturn530671view7

Several older disciplines contribute directly to SDD:

| Foundation | Core idea inherited by SDD | What SDD changes |
|---|---|---|
| Requirements engineering | Elicit, analyze, document, validate and manage requirements | Requirements become direct context for generative agents, not only input to humans. citeturn860486search1 |
| Design by Contract | State obligations, preconditions, postconditions and invariants explicitly | Contracts can guide generation as well as runtime/static verification. citeturn860486search9turn860486search12 |
| Behaviour-Driven Development | Express expected behavior collaboratively through examples and executable scenarios | Agents can derive or implement scenarios from broader natural-language intent. citeturn860486search2turn860486search58 |
| Test-Driven Development | Verification criteria shape implementation rather than merely inspect it afterward | Agents can generate and execute tests within iterative autonomous loops. |
| API/contract-first development | Define machine-readable interfaces before implementations | Agents can generate clients, servers, tests and documentation from the same contract. OpenAPI is a language-agnostic interface description for HTTP APIs. citeturn860486search39turn860486search52 |
| Formal methods | Replace ambiguity with mechanically checkable properties | Modern SDD often uses lightweight natural language first, selectively escalating high-risk properties to formal or executable constraints. citeturn547616search8 |
| Agile requirements | Refine intent incrementally rather than freeze a monolithic requirements document | Specifications can evolve continuously alongside implementation, provided drift is controlled. citeturn970210search23 |

One especially relevant bridge between traditional requirements engineering and AI-era SDD is **EARS — Easy Approach to Requirements Syntax**. EARS was introduced to impose lightweight structure on natural-language requirements without requiring a full formal language; its original study targeted common problems such as ambiguity, vagueness and excessive complexity. Kiro now uses EARS-style structured requirements in its specification workflow, illustrating how an older requirements technique has been repurposed for generative agents. citeturn547616search5turn970210search2

BDD provides another important precedent. Cucumber treats plain-text Gherkin scenarios as executable specifications stored alongside the source code. That model already embodies several ideas central to SDD: a human-readable specification, version control, shared vocabulary, linkage to automated execution and a feedback loop between stated behavior and implementation. Modern agentic SDD extends this idea beyond behavioral scenarios to encompass architectural decisions, implementation planning, task decomposition and project-level rules. citeturn860486search2turn860486search26

Design by Contract contributes the principle that a specification becomes more valuable when obligations are stated in forms that can actually be checked. Eiffel’s contract model treats assertions as simultaneous aids to specification, design, documentation and verification. Contemporary agentic workflows increasingly rediscover the same principle through acceptance criteria, property-based tests, schema validation, static checks and policy gates. citeturn860486search12turn287894search7

The genuinely new element is therefore **the agentic loop**. A specification is no longer consumed only by developers who then manually translate it into code. An AI system may participate in elicitation, clarification, design, decomposition, implementation, testing, review and maintenance. That creates a new problem: specifications must now communicate effectively not only with other engineers but with probabilistic systems that may silently fill gaps. The 2026 Orchid study found that requirement ambiguity consistently degraded code-generation performance across evaluated models and frequently produced divergent implementations of the same ambiguous requirement. citeturn530671view6

This makes clarification a first-class engineering activity rather than conversational nicety. An agent that recognizes uncertainty and asks a bounded question is generally more useful than one that invents a plausible answer, because the latter turns an unknown requirement into an undocumented design decision. This principle appears explicitly in Spec Kit’s clarification phase and in Kiro’s requirement analysis, both of which attempt to surface ambiguity before implementation. citeturn628524search2turn287894search19


## The emerging SDD lifecycle and artifact model

Although current systems use different names and ordering, a common lifecycle can be reconstructed from Spec Kit, Kiro, OpenSpec and the research literature. The central pattern is not a rigid waterfall. It is a sequence of **progressive constraint and feedback**:

**intent → requirements → clarification → design → decomposition → implementation → verification → reconciliation → evolution**

Spec Kit currently exposes this most explicitly. Its production-oriented path is constitution → specify → clarify → plan → checklist → tasks → analyze → implement → converge. `analyze` performs read-only cross-artifact consistency checking, while `converge` compares implementation against the specification, plan and tasks and can create further work when gaps remain. citeturn628524search2turn970210search4

Kiro uses a more compact core of `requirements.md`, `design.md` and `tasks.md`, with requirements-first and design-first variants and a Quick Spec path for work that does not warrant explicit approval gates. It also supports requirement analysis and property-based correctness testing, making verification more directly connected to stated requirements. citeturn492537view8turn287894search4turn287894search10turn287894search29

OpenSpec uses a change-centric model: a **proposal** explains why a change is needed; one or more **specifications** describe changed behavior; a **design** describes how it will be built; and **tasks** describe the implementation work. Its default schema permits specifications and design to be developed in parallel after the proposal, with tasks depending on both. OpenSpec subsequently supports applying and archiving changes, making the evolution of specifications an explicit part of the workflow rather than a disposable planning phase. citeturn287894search2turn287894search8

Across those systems, a tool-independent artifact model can be stated more usefully than any particular directory tree:

| Artifact class | Question answered | Typical content |
|---|---|---|
| **Project principles / normative context** | “What rules always apply here?” | Quality principles, architecture constraints, security policy, testing expectations, technology rules, style and organizational conventions. Spec Kit calls this a constitution; Kiro uses steering files; OpenSpec injects project context and rules through configuration. citeturn970210search7turn970210search1turn970210search24 |
| **Problem / proposal** | “Why should this change exist?” | Problem statement, stakeholders, expected outcome, scope and non-goals. OpenSpec gives this a dedicated proposal artifact. citeturn287894search2 |
| **Behavioral specification** | “What must the system do?” | User journeys, requirements, scenarios, invariants, edge cases, constraints and acceptance criteria. citeturn628524search2turn492537view8 |
| **Clarifications / decisions** | “What ambiguity was resolved, and how?” | Explicit answers, assumptions rejected or accepted, decision records and unresolved questions. Spec Kit folds clarification back into the feature specification. citeturn628524search2 |
| **Technical design / plan** | “How will this requirement be realized?” | Architecture, interfaces, data model, dependencies, trade-offs, migration concerns and testing strategy. citeturn287894search4turn287894search2 |
| **Task decomposition** | “What executable work remains?” | Dependency-aware tasks, implementation boundaries, expected outcomes and associated verification. citeturn492537view8turn287894search2 |
| **Executable checks** | “How will correctness be demonstrated?” | Unit tests, integration tests, acceptance scenarios, property-based tests, schemas, linters, policy checks and static analyses. citeturn287894search7turn860486search2 |
| **Evidence / convergence record** | “What demonstrates that implementation satisfies intent?” | Test results, validation output, requirement-to-code/test traceability, unresolved deviations and reviewer decisions. Spec Kit’s convergence and the evidence-backed models discussed in current research fit this role. citeturn970210search23turn530671view7 |

This layered view resolves a recurrent source of confusion: **requirements, design and tasks are not interchangeable prompts**. Requirements define observable obligations and outcomes. Design chooses how to satisfy them. Tasks turn that design into an execution order. Mixing all three together may give an agent useful context, but it also makes it difficult to determine whether a later change modifies the desired behavior or only its implementation. GitHub’s methodology deliberately separates the “what and why” specification stage from technical planning for precisely this reason. citeturn628524search2turn628524search3

The same separation matters for project-wide rules. GitHub’s constitution is read as live project guidance during later phases; Kiro steering files provide persistent repository knowledge and conventions across sessions; OpenSpec separates project context and rules from individual change artifacts. These are three implementations of the same deeper idea: **ephemeral feature intent should not be forced to carry durable organizational policy**. citeturn970210search15turn970210search1turn970210search25

A robust SDD model also needs **bidirectional traceability**. Forward traceability asks which design elements, tasks, code and tests realize a requirement. Backward traceability asks which requirement or decision justifies a particular implementation. This is old requirements-engineering territory, but it becomes especially important when agents can generate large changes faster than humans can manually reconstruct their rationale. SpecMine’s dataset already records millions of typed links between specification files, code, sibling documents, pull requests, issues and branches, showing that these relationships are empirically observable in modern repositories. citeturn530671view3

A practical invariant follows:

**No important requirement should be accepted merely because an agent reports that it has been implemented.**

Verification evidence should come from something independent of that assertion whenever feasible: tests, schemas, type checking, static analysis, formal properties, security scanners, build output, benchmarks or human review. The recent SWE-CC benchmark reinforces why this distinction matters: agents can produce functionally correct patches while still violating repository policies, with the evaluated systems violating a substantial fraction of applicable contribution rules. Functional success is therefore not synonymous with merge readiness. citeturn547616academia10

The lifecycle must also remain iterative. A failed test can mean defective code, a defective test, an incomplete design or an incorrect requirement. Kiro’s property-based testing workflow explicitly acknowledges this: failures can lead to implementation changes, test changes or requirement refinement. Mature SDD therefore treats the specification/code relationship as a **closed feedback system**, not a one-way compiler pipeline. citeturn287894search7


## Current tool landscape and interoperability lessons

The SDD ecosystem has expanded extremely quickly. SpecMine identified hundreds of thousands of specification files across tens of thousands of public repositories and attributed artifacts to 17 named SDD tools; among developer-adopted tools in its census, Kiro, Spec Kit and OpenSpec were particularly prominent. These figures demonstrate adoption of specification-shaped workflows, not proof of their effectiveness. citeturn530671view3

**GitHub Spec Kit** is currently the most explicit methodology toolkit among the major open-source options. It began around SDD but has evolved into a more general process harness supporting SDD, bug fixing, idea assessment, extensions, presets, workflows and bundles. Its current SDD process provides constitution, specification, clarification, planning, requirements-quality checklists, tasks, cross-artifact analysis, implementation and convergence. It supports multiple coding-agent integrations rather than requiring GitHub Copilot specifically. citeturn628524search0turn970210search20

Spec Kit is particularly interesting architecturally because the methodology is increasingly decomposed from the tool. Presets can override process templates, extensions can add domain-specific commands and quality gates, and workflows and bundles compose reusable process components. This makes Spec Kit closer to a **process runtime** than a single fixed SDD recipe. citeturn287894search15turn628524search0

It also exposes one of the unresolved questions in SDD: persistence. Spec Kit explicitly states that it does not mandate one universal policy for how `spec.md`, `plan.md` and `tasks.md` should evolve after delivery. Its documentation describes alternative persistence models and asks teams to establish their own convention. This is a significant design signal: specification lifecycle semantics are not an implementation detail but a policy decision. citeturn287894search41turn970210search23

**Kiro** integrates SDD more tightly into an agentic development environment. Its core specification consists of requirements, technical design and tasks; it supports feature and bug-fix specifications, requirements-first and design-first paths, quick specifications, requirement analysis and parallel task execution. Its task runner builds a dependency graph and can execute independent work concurrently. citeturn492537view8

Kiro is especially notable for connecting requirements with **property-based testing**. It can derive properties from requirements and turn them into generated tests intended to exercise many input combinations. This moves closer to genuinely executable specification than a Markdown-only workflow, although generated properties still require human scrutiny because an incorrectly inferred property can faithfully test the wrong requirement. citeturn287894search7turn287894search24

Kiro’s steering mechanism separates persistent codebase knowledge from individual specifications. Markdown files under `.kiro/steering/` can contain architecture decisions, coding standards, testing expectations and other project conventions, and Kiro also recognizes `AGENTS.md`. This separation between **persistent operating context** and **change-specific intent** is highly transferable to tool-agnostic SDD. citeturn970210search1turn970210search3

**OpenSpec** takes a deliberately lightweight, change-oriented approach. Its default `spec-driven` schema expresses proposal → specifications/design → tasks → apply, and project configuration supplies context and rules. Unlike systems with a hard-coded artifact structure, OpenSpec also allows workflow schemas to be forked or replaced, so organizations can change artifact names, dependencies and generation guidance. citeturn492537view7turn970210search26

That configurability is important for agnostic methodology design. OpenSpec treats the workflow schema as data: the workflow can be customized without assuming that every project necessarily needs the same three Markdown documents or the same command vocabulary. Its supported-tool documentation likewise maps the same workflow instructions into the invocation conventions of many different coding agents. citeturn287894search31turn287894search34

**BMAD** is broader than SDD proper. It positions itself as an AI-driven agile SDLC framework incorporating product, architecture, UX, development and testing roles, with the principle that planning rigor should vary with the work rather than applying one heavyweight process everywhere. It is therefore best viewed as an adjacent orchestration methodology from which SDD can borrow adaptive process ideas rather than as a canonical definition of SDD. citeturn228400search4turn228400search6

**Tessl** illustrates how quickly this ecosystem can change. Its earlier public positioning emphasized a more radical spec-as-source model; by 2026 its platform emphasizes reusable agent skills and evaluations, while an SDD methodology remains available as an installable skill package that creates `.spec.md` artifacts and links specifications to tests. This is a useful caution against baking current vendor architecture into a supposedly general methodology. citeturn228400search5turn228400search0

The most stable interoperability lesson is therefore that **artifact semantics should be independent of agent invocation syntax**. Whether an environment invokes a workflow as `/speckit-plan`, `$something`, a Skill, an MCP tool, an IDE action or a CLI command should be treated as an adapter concern. The enduring semantics are “create or revise design,” “clarify requirements,” “validate consistency,” “implement selected tasks,” and so forth. Current Spec Kit and OpenSpec documentation already has to translate common workflow concepts into different agent syntaxes, confirming the need for this abstraction. citeturn287894search28turn287894search34

Likewise, file names are conventions rather than ontology. `requirements.md`, `spec.md`, `proposal.md`, `design.md`, `plan.md` and `tasks.md` are useful human interfaces, but an interoperable system should reason about artifact **roles**, relationships and lifecycle states rather than assuming one product’s directory layout.

A future-proof SDD standard would therefore benefit from a distinction among at least four layers:

| Layer | Stable concern | Variable implementation |
|---|---|---|
| **Semantics** | Intent, requirement, constraint, decision, design, task, evidence | Markdown, YAML, database records, issue trackers |
| **Lifecycle** | Draft, clarify, approve, implement, verify, supersede | Slash commands, IDE UI, CI workflow, autonomous orchestration |
| **Validation** | Completeness, consistency, traceability, correctness, policy compliance | LLM review, schemas, tests, static tools, formal verification |
| **Execution adapter** | Give the right context and operation to an agent | Codex, Claude Code, Copilot, Kiro, OpenCode, Gemini CLI, future agents |

This layered decomposition is a synthesis rather than an existing formal standard, but it follows directly from the architectural variability of current systems. citeturn970210search20turn970210search26turn970210search1


## Writing specifications that agents can actually use

Traditional requirements quality matters more, not less, when the consumer is an AI agent. A human engineer may recognize that a stakeholder’s statement is vague and seek clarification based on domain knowledge. An agent may instead generate a plausible interpretation and proceed. The Orchid benchmark’s finding that ambiguous requirements reduce code-generation performance provides direct empirical support for treating ambiguity management as a core part of SDD. citeturn530671view6

The most substantial 2026 attempt to characterize high-quality SDD artifacts is the **EPIC framework**. Researchers derived it from ISO/IEC/IEEE 29148, artifacts from 114 open-source SDD repositories, grey literature and practitioner feedback. EPIC organizes 40 practices into ten quality dimensions under four broad categories: **Expressive, Precise, Interpretable and Compartmentalized**. citeturn530671view1

The framework’s deeper significance is not the acronym but the shift from asking “Do we have a spec?” to asking **“Is the spec fit to constrain an agent?”** A long specification can still be poor if obligations are implicit, terminology changes between sections, acceptance conditions are unverifiable, constraints are buried in prose or implementation tasks cannot be traced back to requirements. EPIC’s authors explicitly frame specification quality as a distinct engineering concern that templates alone do not solve. citeturn132300academia0

Several principles emerge consistently across the research and current tools.

**Requirements should state observable outcomes rather than prematurely encode implementation.** Spec Kit explicitly separates what/why from technical planning. This makes alternative implementations possible and makes it clearer when a disagreement concerns product intent rather than engineering strategy. citeturn628524search2

**Normative language should be deliberate.** “Must,” “should,” “may,” “prefer” and “consider” should not be treated as stylistic synonyms when agents are expected to infer obligation strength. EPIC’s research specifically reports practitioners paying attention to modal wording because agents may treat apparently small linguistic differences as different levels of obligation. citeturn132300academia0

**Acceptance criteria should be falsifiable.** “The application should be fast” gives neither an agent nor a reviewer a reliable stopping condition. “For dataset X under environment Y, operation Z completes within N milliseconds at percentile P” can be turned into a benchmark. The same principle applies to accessibility, security, reliability and resource limits.

**Examples and properties should complement one another.** Examples make intent concrete; properties describe behavior across classes of inputs. Kiro’s property-testing work explicitly attempts to derive general properties from requirements because a handful of passing example tests does not establish that the implementation respects the intended invariant. citeturn287894search7

**Edge cases belong in the specification when they affect intent.** If unspecified edge behavior matters, allowing the agent to invent it converts product decisions into implementation accidents. Clarification stages exist largely to catch this class of omission. citeturn628524search2turn287894search19

**Non-goals are requirements too.** They constrain scope and can prevent an agent from “helpfully” redesigning neighboring systems. Explicitly describing what a change must *not* do is particularly important when agents have broad repository access.

**Architecture decisions should retain rationale, not merely outcome.** “Use PostgreSQL” is less durable than a decision that records the forces, alternatives and reason PostgreSQL was selected. Without rationale, a later agent cannot distinguish a deliberate constraint from an arbitrary historical choice.

**Tasks should be independently verifiable units of progress.** Current Kiro and OpenSpec task models encourage discrete tasks with explicit outcomes, and Spec Kit orders work according to dependencies. A checkbox that says “implement backend” is not useful decomposition merely because it appears in `tasks.md`. citeturn492537view8turn492537view7

**Every transformation should preserve provenance.** If requirement R leads to design decision D, tasks T1/T2 and tests V1/V2, those relationships should remain discoverable. Traceability does not necessarily require heavyweight identifiers everywhere, but the information must survive beyond the original chat session.

The specification should also contain **uncertainty explicitly**. Known fact, decision, assumption, hypothesis, question and preference are different epistemic categories. Collapsing them into confident prose encourages agents to treat assumptions as requirements. A mature SDD workflow should allow an agent to say, in effect, “this cannot be determined from the current contract,” and escalate the ambiguity.

This is where the methodology should preserve agent judgment rather than eliminate it. The objective is not to reduce the agent to a deterministic macro processor. It is to give the agent enough stable context to identify when judgment is appropriate, enough authority to propose alternatives, and enough procedural discipline to distinguish a proposal from an approved decision. That human–agent pattern closely resembles the “consultation” mode identified in the 2026 socio-technical SDD literature: an agent suspends work when a bounded decision requires human input rather than silently manufacturing an answer. citeturn530671view7


## Collaboration, multi-agent work, memory, and governance

Agentic software engineering changes the coordination problem. With one human and one assistant in one short session, much context can remain implicit in conversation. With multiple agents, multiple humans, long-running projects and context-window resets, conversational history becomes an unreliable coordination substrate. The emerging SDD literature consequently treats persistent specifications as a form of shared organizational memory. citeturn530671view7

That shift explains why plain, version-controlled artifacts remain attractive even as models improve. A decision written only in one agent’s context disappears from the working state when another agent starts with a different context; a decision encoded in a repository artifact can be inspected by humans, consumed by different models and reviewed through normal version-control mechanisms. The point is not that Markdown is intrinsically superior to databases or issue trackers, but that **important project state must exist outside a particular model session**. citeturn970210search1turn970210search16

Current research on human–agent teamwork identifies recurring interaction patterns including briefing, consultation, evidence-based review, encoding recurring norms and orchestration of multiple agents. That model moves the human role toward defining intent, making bounded decisions, curating norms and evaluating evidence rather than manually authoring every implementation detail. The paper presenting this model explicitly cautions that its framework is conceptual and that the evidence base remains immature. citeturn530671view7

For collaborative SDD, **decision ownership** therefore matters. An agent may discover a conflict; that does not imply it should have authority to resolve every conflict. A security invariant, product trade-off, irreversible migration or regulatory interpretation may require a particular human or team role. Conversely, requiring human approval for every trivial naming choice would destroy the economic advantage of delegation. The workflow needs configurable autonomy boundaries rather than a single “AI can decide / AI cannot decide” switch.

A useful governance distinction is:

| Decision class | Typical handling |
|---|---|
| Explicitly specified and mechanically verifiable | Agent may execute autonomously and return evidence. |
| Reversible local implementation choice within established constraints | Agent may choose and record rationale. |
| Ambiguous product behavior | Agent should surface alternatives and request clarification. |
| Cross-cutting architecture change | Agent may analyze and propose; approval should follow project governance. |
| Security, compliance, destructive migration or other high-impact decision | Deterministic checks and explicit accountable review should normally be required. |

This table is a methodological synthesis, not a universal risk standard. Its purpose is to distinguish **delegation authority** from raw technical capability.

Multi-agent work also benefits from **task isolation and explicit interfaces**. If two agents modify tightly coupled parts of the system without shared constraints, parallelism can amplify inconsistency rather than throughput. Kiro therefore constructs task dependency graphs before parallel execution, while the emerging academic literature treats orchestration as a distinct human–agent competence. citeturn492537view8turn530671view7

Parallel implementation can also be used intentionally as **N-version exploration**: multiple agents independently solve the same constrained problem, after which their outputs are compared against a common specification and evaluation suite. This is different from ordinary parallel task decomposition because redundancy is deliberate. Current practitioner and research discussions increasingly treat comparative generation as useful when architecture or implementation strategy is uncertain, although the additional cost means it is not sensible for every task. citeturn228400search9turn530671view7

Review must evolve accordingly. A human reviewing thousands of lines of agent-generated code line by line can become the throughput bottleneck. The proposed alternative in current agentic-SE research is an **evidence-backed acceptance package**: implementation plus test results, requirement mappings, policy checks, rationale and known deviations. This does not eliminate code review; it changes where attention is directed. The approach remains a proposed socio-technical pattern rather than a proven universal productivity improvement. citeturn530671view7

Governance also requires a distinction between **agent-generated evidence and independent evidence**. If the same model writes a requirement, implements it, writes an easy test and announces success, the apparent chain of verification may contain no genuinely independent check. SDD becomes stronger when at least some gates are deterministic or independently produced: compiler/type checker, static analyzer, property tester, externally defined contract suite, security scanner or separate reviewer.

Repository policies are a particularly important example. SWE-CC found that coding agents could satisfy functional tests while violating contribution policies governing style, testing and development process. The implication is that a complete SDD contract must include not only feature behavior but also the rules under which the repository considers a change acceptable. citeturn547616academia10

Project-level rule files provide one mechanism for encoding those norms. Spec Kit has its constitution; Kiro has steering; OpenSpec supplies project context and per-artifact rules. The deeper pattern is **norm accumulation**: when reviewers repeatedly correct the same agent behavior, that correction should eventually become durable project knowledge rather than being retyped in every conversation. citeturn970210search15turn970210search1turn970210search24

This principle is especially relevant to reusable skills. A skill should not attempt to encode a fixed “personality” or force every agent into identical reasoning. It should encode reusable capabilities, invariants, decision protocols and artifact semantics while preserving room for models and humans to disagree, propose alternatives and improve the process. In an SDD context, **consistency should constrain commitments, not imagination**.


## Evidence, failure modes, and unresolved research questions

SDD currently has a much stronger **conceptual and tooling story** than an empirical one. The 2026 literature repeatedly acknowledges that the practice is young, terminology varies, tool behavior changes quickly and many claims still originate in vendor or practitioner material rather than controlled studies. citeturn530671view7

The strongest counterweight to uncritical enthusiasm is Brenn Hill’s peer-reviewed ESEM 2026 study. It analyzed 88,052 pull requests across 119 open-source repositories and tested five hypotheses derived from SDD claims. After controls including propensity-score matching, it found no evidence that the observed specification artifacts reduced defects or rework, and specification quality did not predict either outcome in that dataset. The authors explicitly state, however, that the artifacts were predominantly issue/ticket references rather than committed output from modern SDD tools; **the study therefore falsifies a simplistic “having a spec automatically improves quality” claim, not the entire agentic SDD methodology.** citeturn899470search0

EPIC supplies a different, more encouraging observational signal. Among the repositories studied, those in the top specification-quality band spent 11.8% of scanned commits on bug fixes versus 20.4% in the bottom band, and they also showed lower median complexity and more contributors. The authors explicitly treat these associations as hypothesis-generating rather than causal evidence, and their limitations section acknowledges that relevant quality dimensions or practices may still have been missed. citeturn530671view0turn530671view2

SpecMine contributes evidence of **practice**, not effectiveness. Its broad census contains 470,795 specification files across 73,030 repositories associated with 17 named tools, plus a separate Kiro corpus. In the subset of spec-touching pull requests it examined, 81.2% also modified code in the same PR. That provides a valuable empirical foundation for studying SDD evolution, but the corpus itself does not establish that those workflows outperform alternatives. citeturn530671view3

Research into requirements ambiguity supplies one of the most actionable results. The Orchid benchmark contains 1,304 programming tasks with lexical, syntactic, semantic and vague requirements and reports that ambiguity consistently hurts LLM code generation. This supports clarification and structured requirement quality independently of any specific SDD product. citeturn547616search7turn530671view6

The 2025 IEEE requirements-engineering interview study adds an important qualification to the idea that “requirements can simply be fed to an LLM.” Practitioners reported that ordinary high-level requirements were often too abstract to serve directly as coding prompts; they decomposed them into programming tasks and enriched them with architectural and design decisions first. That observation closely matches the multi-artifact pipelines now implemented by Spec Kit, Kiro and OpenSpec. citeturn547616search6

Several failure modes consequently deserve to be treated as first-class SDD problems.

| Failure mode | Why it happens | Mitigation direction |
|---|---|---|
| **Specification theater** | Documents exist but are too vague to constrain implementation | Quality review of the spec itself; measurable criteria; ambiguity detection. citeturn530671view6turn530671view1 |
| **Spec drift** | Code changes after the spec, or the spec changes without downstream reconciliation | Explicit persistence policy, convergence checks and bidirectional traceability. citeturn970210search23 |
| **Over-specification** | Planning cost exceeds the value for exploratory or disposable work | Scale rigor to uncertainty, risk and expected lifetime; current research explicitly rejects SDD as a universal prescription. citeturn530671view7 |
| **Premature design commitment** | Implementation detail leaks into requirements before alternatives are understood | Preserve a semantic distinction between behavioral specification and technical design. citeturn628524search2 |
| **Self-validating agent loops** | The same model creates requirement, implementation and weak validation | Introduce deterministic or independent verification evidence. |
| **Context overload** | Large specifications bury relevant constraints and consume model context | Compartmentalize artifacts, use scoped context and maintain explicit relationships. EPIC treats compartmentalization as a quality dimension. citeturn530671view1 |
| **Hidden assumption propagation** | An agent resolves ambiguity silently and later artifacts treat the choice as fact | Record assumptions and require consultation for consequential ambiguity. citeturn530671view6turn530671view7 |
| **Policy blindness** | Functional tests pass while repository/security/process constraints are violated | Treat governance rules as part of the contract and validate them separately. citeturn547616academia10 |
| **Vendor lock-in** | Workflow semantics are encoded in proprietary command syntax or directories | Separate artifact semantics and lifecycle from adapters and UI conventions. citeturn287894search34turn970210search26 |
| **Stale norms** | Persistent rule files accumulate obsolete guidance | Version, review and periodically prune normative context just like source code. |

Another unresolved issue is the **cost of specification**. Specifications consume human attention, tokens and review time. For high-risk, long-lived or multi-person systems, this investment can plausibly amortize across implementation, maintenance and onboarding. For a throwaway prototype whose requirements are deliberately being discovered through experimentation, extensive up-front formalization can be counterproductive. Current academic SDD work explicitly argues that rigor should depend on uncertainty, stability and expected lifetime. citeturn530671view7

A second unresolved issue is **how much implementation detail belongs in a durable spec**. Agents often perform better with more concrete technical context, but embedding implementation detail into the same artifact that defines product intent accelerates decay when architecture changes. The likely answer is not “never include implementation detail” but “place it in the artifact whose lifecycle matches it.”

A third open question is **causal evaluation**. Future studies need to compare complete SDD workflows against realistic alternatives using the same tasks, developers, agents and repositories while accounting for planning time, implementation speed, defects, review effort, maintainability, security and long-term drift. The field currently lacks enough such studies to support strong quantitative ROI claims. citeturn899470search0turn228400academia62

A fourth concerns **agent adaptation**. As models improve, some forms of painstaking context may become unnecessary while other governance needs remain. The more durable SDD investments are therefore likely to be those encoding facts that cannot be inferred reliably from the repository itself: stakeholder intent, non-obvious constraints, organizational policies, rejected alternatives, risk decisions and acceptance criteria. OpenSpec’s current configuration guidance makes a similar distinction by advising teams to keep durable project facts in project context while avoiding information an agent can simply discover from the code. citeturn970210search30

Finally, SDD itself should be treated as **a governance discipline, not a guarantee of correctness**. A precise specification can still specify the wrong product. A complete implementation can still instantiate a bad architecture. A passing test suite can still omit important behavior. An AI agent can still misunderstand a good specification. SDD improves the inspectability and controllability of these failures; it does not abolish software engineering judgment.


## A tool-agnostic reference model for future work

The research supports a compact set of principles that are sufficiently independent of today’s products to serve as a reference when a general SDD skill is eventually designed. They should be regarded as research-derived design hypotheses rather than a finished specification for that skill.

**Intent precedes implementation, but discovery may precede intent.** SDD should not force premature certainty. When the problem itself is unclear, exploration belongs before or alongside specification. Once a commitment is made, however, it should be externalized so subsequent agents are not required to rediscover it. This reconciles structured engineering with exploratory work. citeturn530671view7

**Specification is plural.** There is no single magical `SPEC.md`. Product intent, behavioral requirements, architecture, policies, implementation tasks and verification evidence have different semantics and different lifetimes. Current leading tools already separate several of these concerns. citeturn628524search2turn492537view8turn492537view7

**Artifact roles are more important than filenames.** An agnostic methodology should be able to map `spec.md`, `requirements.md`, an issue, a structured YAML object or an external requirements system into the same conceptual role where appropriate.

**Every consequential ambiguity should become visible.** The workflow should prefer explicit questions, recorded assumptions or bounded alternative proposals over silent invention. The empirical evidence on ambiguous requirements makes this one of the strongest research-backed principles available to SDD today. citeturn530671view6

**The agent should retain engineering judgment.** A specification is a contract about outcomes and constraints, not necessarily a script for every implementation decision. Agents should be permitted to discover better approaches, flag contradictions and challenge weak assumptions, while distinguishing proposals from approved commitments.

**Constraints and preferences should not be conflated.** “Must use PostgreSQL because an external platform requires it” and “we usually prefer PostgreSQL” should not produce the same behavior. Normative strength and rationale should survive into downstream artifacts.

**Verification criteria should be created before implementation whenever practical.** This does not imply that every project must follow strict TDD. It means the system should know what evidence will count as success before declaring success.

**Validation should be heterogeneous.** LLM review is useful for semantic completeness and consistency; deterministic tools are better for properties they can actually decide. The methodology should combine them rather than ask one model to simulate every kind of verifier.

**Traceability should be proportional, not ceremonial.** A tiny feature may need only recognizable requirement-to-test relationships. A regulated or safety-critical change may require stable identifiers and auditable trace matrices. The goal is reconstructability, not bureaucracy.

**Specifications and implementation should be allowed to disagree temporarily, but never silently.** During development there will naturally be periods where one leads the other. The workflow needs an explicit reconciliation step so the divergence ends in either a changed implementation, an amended specification or a documented deviation.

**Change is a first-class operation.** SDD is incomplete if it only explains greenfield generation. The harder problem is how a specification evolves after deployment and how that change propagates through design, tasks, tests and code. Spec Kit’s explicit persistence models and OpenSpec’s change/archive workflow demonstrate that this is now recognized as a central problem. citeturn970210search23turn287894search8

**Project memory should live outside the conversational session.** Durable decisions, norms and requirements should be stored in inspectable project artifacts so humans and different agents can recover them without relying on a particular model’s conversational continuity. Kiro steering, Spec Kit constitutions and OpenSpec configuration are three concrete implementations of this principle. citeturn970210search1turn970210search15turn970210search24

**Workflow semantics should be independent of execution environment.** “Clarify this specification” is a capability. `/speckit-clarify` is one interface to that capability. An agnostic system should be able to express the former and adapt it to Codex, OpenCode, Copilot, Claude Code, Kiro or future agents without redefining the methodology. citeturn287894search34turn970210search20

**Human and agent authority should be explicit.** Some choices may be delegated freely, some require consultation and some require approval. Autonomy should be a property of the decision and risk context, not of the agent’s brand name.

**Process rigor should scale with risk and information value.** The methodology should not make a weekend prototype produce the same artifact set as a financial ledger or medical system. Current research explicitly recommends treating SDD as a contextual governance discipline rather than a universal heavyweight prescription. citeturn530671view7

**The process itself should remain evolvable.** GitHub’s move from a fixed SDD toolkit toward customizable extensions, presets and workflows, OpenSpec’s schema system and the rapid repositioning of products such as Tessl all indicate that freezing today’s workflow would age badly. citeturn628524search0turn970210search26turn228400search5

This leads to a useful abstract architecture:

```text
                         ┌──────────────────────────┐
                         │ Durable project context  │
                         │ principles · norms · ADRs│
                         └────────────┬─────────────┘
                                      │
                                      ▼
┌──────────┐    ┌────────────┐    ┌──────────────┐
│ Problem  │───▶│ Behavioral │───▶│ Clarification│
│ / intent │    │    spec    │    │ & decisions  │
└──────────┘    └─────┬──────┘    └──────┬───────┘
                      │                   │
                      └─────────┬─────────┘
                                ▼
                        ┌───────────────┐
                        │ Design / plan │
                        └───────┬───────┘
                                ▼
                        ┌───────────────┐
                        │    Tasks      │
                        └───────┬───────┘
                                ▼
                        ┌───────────────┐
                        │Implementation │
                        └───────┬───────┘
                                ▼
                    ┌───────────────────────┐
                    │ Independent evidence  │
                    │ tests · analysis · CI │
                    └───────────┬───────────┘
                                ▼
                        ┌───────────────┐
                        │  Reconcile /  │
                        │   converge    │
                        └───────┬───────┘
                                │
                  change intent │
                       ┌────────┴────────┐
                       ▼                 ▼
                 revise spec       accept result
```

The important characteristic of this model is the return path. A failing verification step does not mechanically imply “change the code.” It can reveal a code defect, a flawed design, a missing requirement, an incorrect test or a newly discovered constraint. The specification-driven loop must be able to repair the appropriate layer rather than optimize blindly for green checks. Kiro’s correctness workflow and Spec Kit’s convergence model both embody parts of this idea. citeturn287894search7turn628524search2

The model also places **durable project context above the feature lifecycle rather than inside it**. This reflects the common architecture visible in constitutions, steering files and project configuration: feature work inherits organizational rules instead of duplicating them. citeturn970210search15turn970210search1turn970210search25

The resulting philosophy can be summarized in one sentence:

**Specify what must remain true, expose what is uncertain, preserve why decisions were made, let capable agents exercise judgment inside those boundaries, and require evidence before considering the resulting implementation complete.**

That formulation is deliberately compatible with different models, different agent harnesses and different degrees of autonomy. It captures what is presently most defensible about Spec-Driven Development without mistaking any vendor’s current command set for the methodology itself.


## Source map and research status

The evidence base behind this reference falls into several distinct reliability classes, and they should not be treated interchangeably.

**Standards and mature engineering foundations** provide the strongest stable base. ISO/IEC/IEEE 29148:2018 covers requirements engineering; ISO/IEC 25010:2023 provides a contemporary software-product quality model; EARS provides a lightweight structured requirements notation; Cucumber documents executable BDD specifications; Eiffel documents Design by Contract; and OpenAPI provides a standardized, language-agnostic machine-readable API description. citeturn860486search1turn860486search0turn547616search5turn860486search2turn860486search9turn860486search39

**Primary tool documentation** is the best source for what current SDD products actually do, but not for proving their claimed benefits. The most relevant current sources are GitHub Spec Kit’s methodology and agentic-SDD documentation, Kiro’s specifications/steering/correctness documentation, and OpenSpec’s default schema and configuration documentation. citeturn287894search0turn970210search4turn492537view8turn970210search1turn287894search7turn492537view7turn970210search24

**Peer-reviewed empirical evidence directly about SDD remains sparse.** Hill’s ESEM 2026 study is currently important because it challenges simple causal claims about specification artifacts while simultaneously acknowledging that modern SDD-tool output was absent from the sampled repositories. citeturn899470search0

**Recent preprints provide valuable but provisional evidence.** EPIC develops a specification-quality framework from repositories and practitioner feedback; SpecMine establishes a large corpus for studying real SDD artifacts; the Orchid work measures the effect of requirement ambiguity on LLM generation; and recent agentic-SDD research develops socio-technical models of human–agent collaboration while explicitly acknowledging the immaturity of the evidence base. These findings are highly relevant but should not be reported as settled scientific consensus. citeturn530671view1turn530671view3turn530671view6turn530671view7

**Industry and project material is useful for identifying emerging patterns** such as parallel implementation, skills, persistent agent context and customizable workflows, but those sources have obvious incentives and should be treated as design evidence rather than neutral validation. citeturn228400search9turn228400search5turn628524search0

As of **4 November 2026**, the most defensible overall assessment is that Spec-Driven Development has moved beyond a niche label into a substantial and rapidly evolving family of agentic software-engineering practices, but its methodology is still consolidating and its empirical evidence lags behind its tooling. SpecMine demonstrates substantial real-world artifact adoption; EPIC and ambiguity research are beginning to establish measurable properties of good specifications; established requirements, contract and executable-specification disciplines provide a mature intellectual foundation; yet there is still insufficient evidence to claim that any current SDD workflow universally improves quality, productivity or maintainability. citeturn530671view3turn530671view1turn899470search0turn530671view7

The most promising interpretation of SDD is therefore not **“write more documentation before coding.”** It is **“make intent, uncertainty, constraints, decisions and evidence durable enough that humans and increasingly autonomous software agents can reason about the same system without depending on invisible context.”** That is the part of the paradigm most strongly supported by both its historical foundations and the architecture of the current ecosystem. citeturn860486search1turn970210search1turn970210search23turn530671view7