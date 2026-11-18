# Claim-to-source map

**Review date** 2026-11-18. **Research snapshot** 2026-11-04.

Line numbers refer to the untouched report in [the input snapshot](https://github.com/s1vh/sdd-bootstrap-skill/blob/90957acec028f39350a5e3f0a2e60c29fcc8ecec/sdd-bootstrap/references/Spec-Driven%20Development%20in%20the%20Agentic%20Era.md). Rows preserve the handoff’s CIT-### handles.

Claim support and pointer provenance are assessed independently. All selected links are independently located replacement or supplemental evidence. A named primary work can be identified from the prose and its findings while the original session identifier remains unresolved. No historical pointer was resolved through original session metadata.

- **High** means the scoped statement or correction is directly checkable in a primary source or official documentation.
- **Moderate** means the conclusion depends on synthesis, a conceptual model, access limitations or living documentation. The reason column describes the relevant limit.
- **claim_supported_by_replacement** means public evidence supports the core claim at its stated scope.
- **claim_qualified** means the original claim needed narrower scope, corrected attribution or more precise wording.
- **partially_supported** means evidence supports only part of the original attribution. See the [unresolved items ledger](UNRESOLVED_ITEMS.md).

## Original citation groups

| Group | Input → revised line | Claim | Evidence | Accessed | Status / confidence | Evidence and editorial treatment |
|---|---|---|---|---|---|---|
| CIT-001 | 8 → 13 | Different workflow families and unsettled vocabulary | [TEAMWORK](#teamwork), [PISKALA](#piskala), [SK-INDEX](#sk-index), [KI-SPECS](#ki-specs), [OS-CONCEPTS](#os-concepts), [BMAD](#bmad), [TESSL-CORE](#tessl-core), [AUGMENT](#augment) | 2026-11-18 | claim_qualified / Moderate | Díaz et al. describe a lack of shared vocabulary in their review. Vendor examples demonstrate workflow differences, with BMad identified as adjacent and living docs dated to this review. |
| CIT-002 | 10 → 15 | Explicit intent and differences in core artifacts | [SK-LAUNCH](#sk-launch), [SK-FLOW](#sk-flow), [KI-SPECS](#ki-specs), [OS-CONCEPTS](#os-concepts) | 2026-11-18 | claim_supported_by_replacement / Moderate | GitHub supplies the intent framing. Kiro documents requirements/design/tasks and OpenSpec documents change artifacts. The prompt-first contrast is the report’s framing. |
| CIT-003 | 12 → 17 | Two meanings of executable specification | [GHERKIN](#gherkin), [OPENAPI](#openapi), [EIFFEL](#eiffel), [KI-TEST](#ki-test), [NONDET](#nondet) | 2026-11-18 | claim_qualified / High | Cucumber needs matching executable steps and OpenAPI needs consuming tooling. Testable properties and assertions supply checks. Non-determinism research supports the narrower generation caveat. |
| CIT-004 | 14 → 19 | Spec-first, spec-anchored and spec-as-source | [TAXONOMY](#taxonomy), [PISKALA](#piskala) | 2026-11-18 | claim_qualified / High | Böckeler published the taxonomy in 2025. Piskala discusses it in 2026. This corrects the implied date of origin. |
| CIT-005 | 16 → 21 | Defects and rework in Hill’s study | [HILL](#hill) | 2026-11-18 | claim_qualified / High | Verified the named proceedings paper and its explicit exclusion of committed SDD-tool output. Dropped priority and avoided extending a null result beyond the sample. |
| CIT-006 | 18 → 23 | Ambiguity, specification quality and corpus scale | [ORCHID](#orchid), [EPIC](#epic), [SPECMINE](#specmine) | 2026-11-18 | claim_supported_by_replacement / High | Orchid is task-level evidence. EPIC associations are observational. SpecMine measures the presence of artifacts, with a corpus caveat retained. |
| CIT-007 | 24 → 29 | Tool-independent working definition | [SK-INDEX](#sk-index), [OS-TOOLS](#os-tools), [OS-CONFIG](#os-config) | 2026-11-18 | claim_supported_by_replacement / Moderate | Repository documents show workflow and adapter variability. Independence is a chosen definition of the report. |
| CIT-008 | 29 → 34 | Lifecycle requirements engineering | [ISO29148](#iso29148), [NASA-RE](#nasa-re) | 2026-11-18 | claim_qualified / High | ISO’s public abstract verifies scope. NASA gives publicly readable requirements-management activities. Removed the unverified ranking of standards. |
| CIT-009 | 31 → 36 | Natural-language specs as shared contract context | [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Conceptual argument in §§4–6, with no demonstrated universal change in practice inferred. |
| CIT-010 | 37 → 42 | Lifecycle requirements and agent input | [ISO29148](#iso29148), [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / High | Standard establishes scope. Spec Kit documents an agent workflow driven by requirements. |
| CIT-011 | 38 → 43 | Design by Contract as an antecedent | [EIFFEL](#eiffel), [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Eiffel defines the obligations. The application to agent generation is an analogy proposed in the report. |
| CIT-012 | 39 → 44 | BDD examples and executable scenarios | [GHERKIN](#gherkin), [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Gherkin examples map to step definitions. Teamwork discusses executable specs for coding agents. |
| CIT-013 | 41 → 46 | Language-agnostic HTTP contracts and generation | [OPENAPI](#openapi), [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / High | OpenAPI introduction lists generation, testing and documentation uses. Agent consumption is a practical application. |
| CIT-014 | 42 → 47 | Mechanically checkable properties and selective use of formalism | [TLC](#tlc), [TEAMWORK](#teamwork) | 2026-11-18 | claim_qualified / Moderate | TLC verifies modeled properties within stated bounds. Selective escalation is an editorial suggestion, with no ecosystem-frequency claim. |
| CIT-015 | 43 → 48 | Incremental change and persistence | [AGILE](#agile), [SK-PERSIST](#sk-persist) | 2026-11-18 | claim_supported_by_replacement / High | Primary Agile principles support changing requirements. Spec Kit documents maintenance and drift trade-offs. |
| CIT-016 | 45 → 50 | EARS and adoption in Kiro | [EARS](#ears), [KI-QUICK](#ki-quick) | 2026-11-18 | claim_supported_by_replacement / High | The original publication addresses ambiguity, complexity and vagueness. Quick Spec explicitly describes EARS acceptance criteria. |
| CIT-017 | 47 → 52 | Versionable behavioral scenarios and expanded agent workflow | [GHERKIN](#gherkin), [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / Moderate | Gherkin supports plain-text runnable scenarios. The Spec Kit workflow illustrates design, planning and task stages. Versioning is a project practice. |
| CIT-018 | 49 → 54 | Explicit obligations and checkable properties | [EIFFEL](#eiffel), [KI-TEST](#ki-test) | 2026-11-18 | claim_supported_by_replacement / Moderate | Primary documentation illustrates both mechanisms. Wider applicability is synthesis. |
| CIT-019 | 51 → 56 | Ambiguity and divergent function-level generations | [ORCHID](#orchid) | 2026-11-18 | claim_supported_by_replacement / High | Public v3 abstract describes both effects across its evaluated models. Scope made explicit in the report. |
| CIT-020 | 53 → 58 | Requirements clarification and issue detection | [SK-FLOW](#sk-flow), [KI-ANALYZE](#ki-analyze) | 2026-11-18 | claim_supported_by_replacement / Moderate | Spec Kit documents its optional clarify gate. Kiro documents a requirements analysis action. The human–agent comparison is guidance. |
| CIT-021 | 62 → 67 | Spec Kit command sequence and convergence | [SK-FLOW](#sk-flow) | 2026-11-18 | claim_qualified / High | Pinned workflow documents the order and optional checks. Analyze is read-only. Converge may append remaining work to tasks.md. |
| CIT-022 | 64 → 69 | Kiro spec variants and verification | [KI-SPECS](#ki-specs), [KI-QUICK](#ki-quick), [KI-ANALYZE](#ki-analyze), [KI-TEST](#ki-test) | 2026-11-18 | claim_supported_by_replacement / High | Quick Spec skips inter-phase gates. Analysis and property testing are separate documented features. |
| CIT-023 | 66 → 71 | OpenSpec artifact graph and archive | [OS-SCHEMA](#os-schema), [OS-CONCEPTS](#os-concepts) | 2026-11-18 | claim_supported_by_replacement / High | Schema establishes parallelizable specs/design after proposal and tasks depending on both. Concepts documents archival workflow. |
| CIT-024 | 72 → 77 | Durable rules via constitution, steering and configuration | [SK-FLOW](#sk-flow), [KI-STEER](#ki-steer), [OS-CONFIG](#os-config) | 2026-11-18 | claim_supported_by_replacement / High | Pinned or official docs document each tool’s mechanism. Artifact-class generalization is synthesis. |
| CIT-025 | 73 → 78 | Dedicated proposal artifact | [OS-CONCEPTS](#os-concepts) | 2026-11-18 | claim_supported_by_replacement / High | Concepts describes motivation, scope and approach in proposal.md. |
| CIT-026 | 74 → 79 | Behavioral specifications | [SK-FLOW](#sk-flow), [KI-SPECS](#ki-specs) | 2026-11-18 | claim_supported_by_replacement / High | Documents user stories, requirements, acceptance criteria and constraints. |
| CIT-027 | 75 → 80 | Clarification answers in the spec | [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / High | Clarify section documents integrating resolved ambiguities into the feature spec. |
| CIT-028 | 76 → 81 | Design and technical plan | [KI-SPECS](#ki-specs), [OS-SCHEMA](#os-schema) | 2026-11-18 | claim_supported_by_replacement / High | Both document design artifacts with implementation choices. The table’s list gives examples. |
| CIT-029 | 77 → 82 | Task decomposition | [KI-SPECS](#ki-specs), [OS-SCHEMA](#os-schema) | 2026-11-18 | claim_supported_by_replacement / High | Kiro describes dependency-aware execution and OpenSpec supplies tracked tasks and verification guidance. |
| CIT-030 | 78 → 83 | Executable checks as an artifact class | [KI-TEST](#ki-test), [GHERKIN](#gherkin) | 2026-11-18 | claim_supported_by_replacement / High | Sources directly illustrate property tests and acceptance scenarios. Other entries in the table are possible checks. |
| CIT-031 | 79 → 84 | Convergence and acceptance evidence | [SK-FLOW](#sk-flow), [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Spec Kit documents assessing implementation against artifacts. Teamwork §5.9 proposes a broader evidence package. |
| CIT-032 | 81 → 86 | Specifying intent before technical planning | [SK-LAUNCH](#sk-launch), [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / High | Spec Kit distinguishes what/why from planning a technical implementation. General separation is synthesis. |
| CIT-033 | 83 → 88 | Project-wide guidance versus feature artifacts | [SK-FLOW](#sk-flow), [KI-STEER](#ki-steer), [OS-CONFIG](#os-config) | 2026-11-18 | claim_supported_by_replacement / Moderate | Each documents an applicable mechanism. The common rule is the report’s interpretation. |
| CIT-034 | 85 → 90 | Bidirectional traceability and typed references | [NASA-RE](#nasa-re), [SPECMINE](#specmine) | 2026-11-18 | claim_supported_by_replacement / High | NASA §6.2 supplies the established concept. SpecMine v1 Table I and Appendix A enumerate 2,421,323 typed references and their entities. |
| CIT-035 | 91 → 96 | Functional patches can violate repository policy | [SWE-CC](#swe-cc) | 2026-11-18 | claim_supported_by_replacement / High | SWE-CC preprint abstract reports violations among successful patches in evaluated configurations. Independent evidence is a recommendation. |
| CIT-036 | 93 → 98 | Failure handling can revise the requirement | [KI-TEST](#ki-test) | 2026-11-18 | claim_supported_by_replacement / High | Kiro’s correctness workflow includes revising implementation, test or requirement following a property failure. |
| CIT-037 | 98 → 103 | Corpus counts and prominent developer tools | [SPECMINE](#specmine) | 2026-11-18 | claim_qualified / High | v1 Table I and developer-tool discussion support the counts and examples. Filename-search limitations block an adoption-rate inference. |
| CIT-038 | 100 → 105 | Spec Kit processes, components and integrations | [SK-INDEX](#sk-index), [SK-FLOW](#sk-flow) | 2026-11-18 | claim_qualified / High | Pinned documentation supports workflow and features. Removed unsupported ranking of methodology toolkits. |
| CIT-039 | 102 → 107 | Spec Kit process customization | [SK-INDEX](#sk-index) | 2026-11-18 | claim_supported_by_replacement / Moderate | Documentation overview describes extensions, presets, workflows and bundles. Process runtime is an analogy. |
| CIT-040 | 104 → 109 | Post-delivery specification persistence | [SK-PERSIST](#sk-persist) | 2026-11-18 | claim_supported_by_replacement / High | Pinned how-to sets out team-owned alternatives. It explicitly leaves the choice open. |
| CIT-041 | 106 → 111 | Kiro feature/bug workflows and independent task execution | [KI-SPECS](#ki-specs) | 2026-11-18 | claim_supported_by_replacement / High | Specs documentation describes variants and task dependency graph with concurrent execution waves. |
| CIT-042 | 108 → 113 | Requirements-derived property tests | [KI-TEST](#ki-test) | 2026-11-18 | claim_supported_by_replacement / High | Official documentation describes extraction and generated cases, and explicitly flags weak or incorrect properties. |
| CIT-043 | 110 → 115 | Steering files and AGENTS.md | [KI-STEER](#ki-steer) | 2026-11-18 | claim_supported_by_replacement / High | Official docs describe directory, persistent context and AGENTS.md support. Transferability is a design judgment. |
| CIT-044 | 112 → 117 | OpenSpec schema customizability | [OS-SCHEMA](#os-schema), [OS-CONFIG](#os-config) | 2026-11-18 | claim_supported_by_replacement / High | Schema records dependencies and apply. Customization docs cover project config, schema forking and replacements. |
| CIT-045 | 114 → 119 | Workflow schemas and adapter syntax | [OS-CONFIG](#os-config), [OS-TOOLS](#os-tools) | 2026-11-18 | claim_supported_by_replacement / High | Pinned sources document custom roles and agent-specific command and skill locations. |
| CIT-046 | 116 → 121 | BMad’s broader adaptive process | [BMAD](#bmad) | 2026-11-18 | claim_supported_by_replacement / Moderate | Official role/stage description supports varied entry points and roles. Positioning as adjacent is editorial synthesis. |
| CIT-047 | 118 → 123 | Tessl’s launch positioning and later documentation | [TESSL-LAUNCH](#tessl-launch), [TESSL-CORE](#tessl-core), [TESSL-SDD](#tessl-sdd) | 2026-11-18 | claim_qualified / Moderate | Original announcement and public docs show the two emphases. Registry v2.0.1 links specs and tests. Exact transition date and version availability on 4 Nov remain unverified. |
| CIT-048 | 120 → 125 | Agent-dependent invocation syntax | [SK-FLOW](#sk-flow), [OS-TOOLS](#os-tools) | 2026-11-18 | claim_supported_by_replacement / High | Pinned docs show slash, skill or other conventions. The recommended abstraction is synthesis. |
| CIT-049 | 133 → 138 | Separate workflow layers | [SK-INDEX](#sk-index), [OS-CONFIG](#os-config), [KI-STEER](#ki-steer) | 2026-11-18 | claim_supported_by_replacement / Moderate | Tools provide concrete examples of varying mechanisms. Four-layer structure is the report’s proposed model. |
| CIT-050 | 138 → 143 | Ambiguity decreases code generation performance | [ORCHID](#orchid) | 2026-11-18 | claim_supported_by_replacement / High | v3 reports the effect in benchmark tasks. It supports investigating ambiguity management. |
| CIT-051 | 140 → 145 | EPIC derivation and categories | [EPIC](#epic) | 2026-11-18 | claim_qualified / High | Methods and results confirm the 114 repositories and 40 practices across 10 dimensions. Removed unverified ranking among 2026 studies. |
| CIT-052 | 142 → 147 | Specification quality beyond templates | [EPIC](#epic) | 2026-11-18 | claim_supported_by_replacement / High | Paper distinguishes template coverage from quality and describes terminology, traceability and verifiability practices. |
| CIT-053 | 146 → 151 | Observable outcomes before technical choices | [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / High | Specify covers user-visible intent. Technical context belongs in Plan. |
| CIT-054 | 148 → 153 | Deliberate normative language | [EPIC](#epic), [BCP14](#bcp14) | 2026-11-18 | claim_qualified / High | EPIC reports practitioner agreement with intentional wording. BCP 14 supplies an explicit convention. Removed unsupported causal claim about differences between modal verbs. |
| CIT-055 | 152 → 157 | Examples versus properties | [KI-TEST](#ki-test) | 2026-11-18 | claim_supported_by_replacement / High | Correctness documentation describes randomized cases and explicitly limits what passing tests show. |
| CIT-056 | 154 → 159 | Clarification can surface edge cases | [SK-FLOW](#sk-flow), [KI-ANALYZE](#ki-analyze) | 2026-11-18 | claim_supported_by_replacement / Moderate | Both document detecting ambiguity and missing cases. Product ownership conclusion is synthesis. |
| CIT-057 | 160 → 165 | Verifiable tasks and dependency ordering | [KI-SPECS](#ki-specs), [OS-SCHEMA](#os-schema), [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / High | OpenSpec schema calls for verification per task. Spec Kit and Kiro describe dependency-aware tasks. |
| CIT-058 | 166 → 171 | Bounded consultation | [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | §§5.8 and 6.1 describe consultation as asking for a decision when intent is insufficient. This is a proposed pattern. |
| CIT-059 | 171 → 176 | Persistent specifications as shared memory | [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | §5.4 proposes persistent shared knowledge across sessions and agents. |
| CIT-060 | 173 → 178 | Project state outside an individual session | [KI-STEER](#ki-steer), [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Kiro documents persistent steering; teamwork argues for versioned shared knowledge. Markdown exclusivity is not inferred. |
| CIT-061 | 175 → 180 | Five human–agent interaction patterns | [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | §6 names briefing, consultation, review, norm encoding and orchestration. Limits of the conceptual framework are retained. |
| CIT-062 | 191 → 196 | Task isolation and parallel agent work | [KI-SPECS](#ki-specs), [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Kiro documents dependency waves. Teamwork discusses decomposition, working-tree isolation and orchestration. |
| CIT-063 | 193 → 198 | N-version exploration compared with task decomposition | [TEAMWORK](#teamwork) | 2026-11-18 | claim_qualified / Moderate | §5.6 directly proposes multiple implementations and shared checking. Avoided asserting an adoption trend or measured comparative benefit. |
| CIT-064 | 195 → 200 | Evidence-backed acceptance package | [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | §5.9 provides requirements, tests, checks, traceability and rationale as a proposed review package. |
| CIT-065 | 199 → 204 | Functional success and contribution policy | [SWE-CC](#swe-cc) | 2026-11-18 | claim_supported_by_replacement / High | SWE-CC reports failures across codes and process obligations. Applying the distinction to a contract is synthesis. |
| CIT-066 | 201 → 206 | Project rule files and durable norms | [SK-FLOW](#sk-flow), [KI-STEER](#ki-steer), [OS-CONFIG](#os-config) | 2026-11-18 | claim_supported_by_replacement / Moderate | The three tool mechanisms are firsthand examples. Recording repeated feedback is guidance. |
| CIT-067 | 208 → 213 | Limited mature empirical evidence | [TEAMWORK](#teamwork), [HILL](#hill) | 2026-11-18 | claim_qualified / Moderate | Teamwork states its own evidence limits and Hill distinguishes tool claims from what was tested. Avoided characterizing the entire literature as inventoried. |
| CIT-068 | 210 → 215 | Hill’s final proceedings data and scope | [HILL](#hill) | 2026-11-18 | claim_qualified / High | Final proceedings replace the earlier differently sized draft as evidence for the reported sample. The null result is observational with controls and does not establish no effect. |
| CIT-069 | 212 → 217 | EPIC bug-fix rate, complexity and contributors | [EPIC](#epic) | 2026-11-18 | claim_supported_by_replacement / High | RQ2 directly reports 11.8% versus 20.4%, complexity normalized by KLOC and contributor comparisons. Observational limits and mixed outcomes remain visible. |
| CIT-070 | 214 → 219 | SpecMine census sizes and 81.2% code co-change | [SPECMINE](#specmine) | 2026-11-18 | claim_supported_by_replacement / High | v1 Table I gives both censuses and 5,992 spec-touching PRs. Co-change is a subsample observation and a heuristic for implementation. |
| CIT-071 | 216 → 221 | 1,304 ambiguity benchmark tasks and four types | [ORCHID](#orchid) | 2026-11-18 | claim_supported_by_replacement / High | v3 and the conference abstract verify the total, taxonomy and benchmark finding. |
| CIT-072 | 218 → 223 | 2025 interview study on requirements as prompts | [ULLRICH](#ullrich) | 2026-11-18 | claim_supported_by_replacement / High | Publisher metadata and author preprint support 18 interviews at 14 companies and the reported transformation into enriched tasks. |
| CIT-073 | 224 → 229 | Specification quality and ambiguity review | [ORCHID](#orchid), [EPIC](#epic) | 2026-11-18 | claim_supported_by_replacement / Moderate | Benchmark and framework motivate review. Specification theater is a descriptive label used by this report. |
| CIT-074 | 225 → 230 | Persistence and convergence as approaches to drift | [SK-PERSIST](#sk-persist), [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / Moderate | Docs set out maintenance models, read-only analysis and append-only convergence. Reconciliation is still team-owned. |
| CIT-075 | 226 → 231 | Over-specification and scaling rigor | [TEAMWORK](#teamwork), [SPECMINE-PRACTICE](#specmine-practice) | 2026-11-18 | claim_supported_by_replacement / Moderate | Conceptual account plus interviews support conditional use and planning costs. This does not quantify benefit. |
| CIT-076 | 227 → 232 | Product intent distinct from architecture choices | [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / High | The workflow explicitly stages these tasks separately. |
| CIT-077 | 229 → 234 | Compartmentalized spec artifacts | [EPIC](#epic) | 2026-11-18 | claim_supported_by_replacement / Moderate | Compartmentalized is an EPIC category. Context-overload mitigation remains a design recommendation. |
| CIT-078 | 230 → 235 | Assumptions and consultation | [ORCHID](#orchid), [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Orchid shows benchmark ambiguity effects. Teamwork proposes escalation and recording. No causal benefit is inferred for this table mitigation. |
| CIT-079 | 231 → 236 | Policy blindness separate from functional correctness | [SWE-CC](#swe-cc) | 2026-11-18 | claim_supported_by_replacement / High | The benchmark measures policy compliance independently of unit-test success. |
| CIT-080 | 232 → 237 | Adapters can reduce coupling to agent syntax | [OS-TOOLS](#os-tools), [OS-CONFIG](#os-config), [SK-INDEX](#sk-index) | 2026-11-18 | claim_supported_by_replacement / Moderate | Primary docs show configurable artifacts and differing invocations. Lock-in mitigation is an editorial inference. |
| CIT-081 | 235 → 240 | Cost and proportional rigor | [TEAMWORK](#teamwork), [SPECMINE-PRACTICE](#specmine-practice) | 2026-11-18 | claim_supported_by_replacement / Moderate | Conceptual argument and practitioner reports support conditional adoption and planning/review effort. No verified amortization estimate. |
| CIT-082 | 239 → 244 | Open causal and return-on-investment questions | [HILL](#hill), [ROSA](#rosa), [TEST-GEN](#test-gen) | 2026-11-18 | claim_qualified / Moderate | Hill is observational, Rosa proposes a study design, and Tufano measures one test-generation intervention. None establishes net value for complete general workflows. |
| CIT-083 | 241 → 246 | Project context and discoverable repository facts | [OS-CONFIG](#os-config) | 2026-11-18 | partially_supported / Moderate | OpenSpec documents context injection. Treating easily discoverable details as unnecessary repetition is presented as a practice suggestion. |
| CIT-084 | 250 → 255 | Discovery before commitment | [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Discussion supports using rigor according to the work. The resulting bootstrap principle is an editorial design hypothesis. |
| CIT-085 | 252 → 257 | Separate project and feature artifact roles | [SK-FLOW](#sk-flow), [KI-SPECS](#ki-specs), [OS-CONCEPTS](#os-concepts) | 2026-11-18 | claim_supported_by_replacement / Moderate | Primary docs supply multiple concrete examples. The generalization is a design hypothesis. |
| CIT-086 | 256 → 261 | Making ambiguity visible | [ORCHID](#orchid), [EPIC](#epic) | 2026-11-18 | claim_qualified / Moderate | Cites a measured problem and a proposed response. Removes an unsubstantiated ranking of how strongly the principle has been validated. |
| CIT-087 | 270 → 275 | Evolving specs and archiving changes | [SK-PERSIST](#sk-persist), [OS-CONCEPTS](#os-concepts) | 2026-11-18 | claim_supported_by_replacement / High | Persistence models and OpenSpec archival workflow are explicitly documented. |
| CIT-088 | 272 → 277 | Inspectable, cross-session project memory | [KI-STEER](#ki-steer), [SK-FLOW](#sk-flow), [OS-CONFIG](#os-config) | 2026-11-18 | claim_supported_by_replacement / Moderate | Tool mechanisms for steering, constitution and config are documented. Cross-tool memory strategy is the report’s proposed practice. |
| CIT-089 | 274 → 279 | Semantic workflow versus execution syntax | [OS-TOOLS](#os-tools), [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / Moderate | Pinned documentation shows the same operations delivered through different conventions. |
| CIT-090 | 278 → 283 | Rigor proportional to risk and information value | [TEAMWORK](#teamwork), [SPECMINE-PRACTICE](#specmine-practice) | 2026-11-18 | claim_supported_by_replacement / Moderate | Conceptual and qualitative research supports selective use. Examples are illustrations, with no claim of equivalence across regulated fields. |
| CIT-091 | 280 → 285 | Workflow evolvability and different vendor emphases | [SK-INDEX](#sk-index), [OS-CONFIG](#os-config), [TESSL-LAUNCH](#tessl-launch), [TESSL-CORE](#tessl-core) | 2026-11-18 | claim_qualified / Moderate | Spec Kit and OpenSpec show customization. Tessl sources support differing emphases without dating a product migration or its speed. |
| CIT-092 | 326 → 331 | Verification feedback can lead to change | [KI-TEST](#ki-test), [SK-FLOW](#sk-flow) | 2026-11-18 | claim_supported_by_replacement / High | Correctness documents multiple remediation paths. Spec Kit converge assesses implementation and appends remaining tasks. |
| CIT-093 | 328 → 333 | Feature work inherits durable context | [SK-FLOW](#sk-flow), [KI-STEER](#ki-steer), [OS-CONFIG](#os-config) | 2026-11-18 | claim_supported_by_replacement / Moderate | Official docs support guidance crossing feature boundaries. Placement in the abstract architecture is a synthesis. |
| CIT-094 | 341 → 346 | Engineering standards and established practices | [ISO29148](#iso29148), [ISO25010](#iso25010), [EARS](#ears), [GHERKIN](#gherkin), [EIFFEL](#eiffel), [OPENAPI](#openapi) | 2026-11-18 | claim_supported_by_replacement / High | Public standards catalogue records verify scope. Primary docs and the original EARS publication record supply the other statements. |
| CIT-095 | 343 → 348 | Primary tooling documentation | [SK-FLOW](#sk-flow), [SK-PERSIST](#sk-persist), [KI-SPECS](#ki-specs), [KI-STEER](#ki-steer), [KI-TEST](#ki-test), [OS-SCHEMA](#os-schema), [OS-CONFIG](#os-config) | 2026-11-18 | claim_supported_by_replacement / High | Authoritative for described behavior in reviewed versions. No effectiveness claim is inferred. |
| CIT-096 | 345 → 350 | Peer-reviewed findings about observed artifacts | [HILL](#hill) | 2026-11-18 | claim_supported_by_replacement / Moderate | ESEM proceedings support the limited negative finding. The revised sentence avoids inferring maturity from a count of all published work. |
| CIT-097 | 347 → 352 | Provisional evidence and Orchid’s conference status | [EPIC](#epic), [SPECMINE](#specmine), [ORCHID](#orchid), [TEAMWORK](#teamwork), [SWE-CC](#swe-cc) | 2026-11-18 | claim_qualified / High | EPIC, SpecMine, SWE-CC and Teamwork are described at the cited preprint stage. Orchid is separately identified by its ASE proceedings DOI and public author version. |
| CIT-098 | 349 → 354 | Industry examples of parallel work, context and customization | [AUGMENT](#augment), [TESSL-CORE](#tessl-core), [SK-INDEX](#sk-index) | 2026-11-18 | claim_supported_by_replacement / Moderate | Vendor documentation identifies deployed or documented patterns. Parallel task work is distinguished from comparative generation. |
| CIT-099 | 351 → 356 | Snapshot conclusion and limited effectiveness evidence | [SPECMINE](#specmine), [EPIC](#epic), [ORCHID](#orchid), [HILL](#hill), [TEAMWORK](#teamwork) | 2026-11-18 | claim_qualified / Moderate | Substantial corpus presence and targeted findings are kept. Artifact coverage does not establish adoption prevalence or generalized improvement. |
| CIT-100 | 353 → 358 | Durable intent, uncertainty, constraints and evidence | [ISO29148](#iso29148), [KI-STEER](#ki-steer), [SK-PERSIST](#sk-persist), [TEAMWORK](#teamwork) | 2026-11-18 | claim_supported_by_replacement / Moderate | Sources explain foundations and mechanisms. The closing interpretation is a research synthesis. |

## Supplemental evidence for uncited statements

| Input line | Evidence | Treatment |
|---|---|---|
| 40 | [TDD](#tdd), [KI-TEST](#ki-test) | Publisher material anchors the test-first foundation. Kiro illustrates the optional agent workflow. |
| 58 | [SK-FLOW](#sk-flow), [KI-SPECS](#ki-specs), [OS-CONCEPTS](#os-concepts) | Grounded the synthesized lifecycle in three workflows. |
| 150 | [EPIC](#epic) | Connected the existing illustrative acceptance criterion to EPIC verifiability. |
| 237 | [SPECMINE-PRACTICE](#specmine-practice) | Grounded the implementation detail and durability trade-off in reported practice. |

## Evidence catalogue

Access date for every entry below is **2026-11-18**.

### ISO29148

**ISO/IEC/IEEE 29148:2018 — Requirements engineering**. 2018 edition, public ISO catalogue entry. Overview and lifecycle scope. Full normative text can require purchase. [Public source](https://www.iso.org/standard/72089.html)

### ISO25010

**ISO/IEC 25010:2023 — Product quality model**. 2023 edition, public ISO catalogue entry. Product-quality model scope. Full normative text can require purchase. [Public source](https://www.iso.org/standard/78176.html)

### NASA-RE

**NASA Systems Engineering Handbook, §6.2 Requirements Management**. Public handbook, §6.2. Change management and bidirectional traceability among requirements, design and tests. [Public source](https://www.nasa.gov/reference/6-2-requirements-management/)

### EARS

**Mavin et al., Easy Approach to Requirements Syntax (EARS)**. IEEE RE 2009, DOI 10.1109/RE.2009.9, public institutional abstract. Syntax rules for recurring natural-language requirements problems. [Public source](https://research.manchester.ac.uk/en/publications/easy-approach-to-requirements-syntax-ears/)

### GHERKIN

**Cucumber, Gherkin Reference**. Public project documentation. Examples, Given/When/Then and matching steps to executable step definitions. [Public source](https://cucumber.io/docs/gherkin/reference/)

### EIFFEL

**Eiffel, Design by Contract and Assertions**. Public language documentation. Preconditions, postconditions and invariants as obligations and assertions. [Public source](https://www.eiffel.org/doc/eiffel/Design_by_Contract_and_Assertions)

### OPENAPI

**OpenAPI Initiative, OpenAPI Specification v3.1.1**. Released version 3.1.1. Introduction and use of a language-agnostic HTTP API description by documentation, generation and testing tools. [Public source](https://spec.openapis.org/oas/v3.1.1.html)

### TLC

**TLA+ project wiki, TLC model checker**. Public project documentation. Checking a formal model against stated properties within the model’s bounds. [Public source](https://docs.tlapl.us/using:tlc:start)

### TDD

**Beck, Test Driven Development: By Example**. 2002, public publisher description and contents. Test-first sequence and refactoring. Full book is commercially distributed. [Public source](https://www.informit.com/store/test-driven-development-by-example-9780321146533)

### AGILE

**Principles behind the Agile Manifesto**. 2001, public primary statement. Welcoming changing requirements and iterative delivery. [Public source](https://agilemanifesto.org/principles.html)

### BCP14

**IETF, RFC 2119 and RFC 8174 (BCP 14)**. 2017 clarification of RFC 2119, public RFC record. Capitalized normative terms under the BCP 14 convention. The report’s prose recommendation is broader than that convention. [Public source](https://www.rfc-editor.org/info/rfc8174/)

### NONDET

**Ouyang et al., An Empirical Study of the Non-Determinism of ChatGPT in Code Generation**. ACM TOSEM, DOI 10.1145/3697010, public accepted manuscript. Variation across repeated code-generation requests in three benchmark datasets. [Public source](https://discovery.ucl.ac.uk/id/eprint/10198256/)

### TAXONOMY

**Böckeler, Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl**. 2025-10-15, practitioner field report. SDD Levels section defines spec-first, spec-anchored and spec-as-source. [Public source](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)

### PISKALA

**Piskala, Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants**. 2026-01-30 arXiv preprint. Reuses the three levels and discusses tool and domain examples. A conceptual account. [Public source](https://arxiv.org/abs/2602.00180)

### HILL

**Hill, Specification Artifacts in Open-Source Pull Request Workflows Do Not Reduce Defects**. 2026-10-05 ESEM proceedings, DOI 10.4230/LIPIcs.ESEM.2026.84. Abstract and paper results. The published analysis uses 88,052 PRs from 119 repositories and separates issue and ticket artifacts from tool outputs. [Public source](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84)

### EPIC

**Claudino et al., The EPIC Framework for Spec-Driven Development**. 2026-10-06 arXiv preprint. Methods §3, framework and evaluation §4, and limitations. Observational repository comparisons and practitioner feedback. [Public source](https://arxiv.org/abs/2610.07534)

### SPECMINE

**Agarwal and Vasilescu, SPECMINE: A Large-Scale Corpus of Spec-Driven Development Artifacts**. 2026-08-25 arXiv v1. Table I, traceability index and Appendices A–B. This version describes the original corpus and PR subsample. [Public source](https://arxiv.org/pdf/2608.25202v1)

### SPECMINE-PRACTICE

**Agarwal et al., Spec-Driven Development as Prescribed and as Practiced**. 2026-10-15 arXiv v4. Practitioner reports and sampled repository practice. Distinct version of the submission, used for qualitative findings. [Public source](https://arxiv.org/abs/2608.25202v4)

### ORCHID

**Yang et al., Clarity Is Not Assumed: Understanding LLM-Based Code Generation under Ambiguous Requirements**. 2026-09-27 arXiv v3, conference DOI 10.1145/3832783.3834403. 1,304 function-level tasks, four ambiguity types and measured performance and divergence. Scope is the evaluated tasks and models. [Public source](https://arxiv.org/abs/2604.21505v3)

### TEAMWORK

**Diaz et al., Spec-Driven Development for Agentic Software Engineering: Harnessing Human–Agent Teamwork**. 2026-08-31 arXiv v1. §§4–6 and §8. Conceptual synthesis including persistence, consultation, evidence review, and N-version generation. [Public source](https://arxiv.org/html/2609.00252v1)

### SWE-CC

**Truong et al., Correct Code, Broken Contributions? SWE-CC**. 2026-10-05 arXiv preprint 2610.06193, linked author replication package. Paper abstract and author results describe 500 tasks and policy violations among functionally correct patches across evaluated models and scaffolds. [Public source](https://github.com/dangtruong01/swe-cc-arxiv)

### ULLRICH

**Ullrich et al., From Requirements to Code: Understanding Developer Practices in LLM-Assisted Software Engineering**. 2025 IEEE RE, DOI 10.1109/RE63999.2025.00032, public author preprint. Interview study of 18 practitioners at 14 companies and the reported task decomposition and enrichment. [Public source](https://arxiv.org/abs/2507.07548v1)

### ROSA

**Rosa et al., Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**. 2026-01-07 preprint, SANER 2026 Registered Report. Study design for a scoped human-in-the-loop workflow. Evidence of a research question and design. [Public source](https://arxiv.org/abs/2601.03878)

### TEST-GEN

**Tufano et al., Grounding AI Agents in Contracts: An Empirical Evaluation of Spec-Driven Test Generation**. SpecOps 2026, public institutional abstract. Controlled comparison of a scoped test-generation technique using production bugs from Google. [Public source](https://research.google/pubs/grounding-ai-agents-in-contracts-an-empirical-evaluation-of-spec-driven-test-generation/)

### SK-FLOW

**GitHub Spec Kit, Agentic SDD**. Repository snapshot, 2026-11-03. Workflow order, optional quality gates, constitution, clarification, consistency analysis, implementation and convergence. [Public source](https://github.com/github/spec-kit/blob/a227e38315cd38172b04f2fb8f06ce8b69b38331/docs/reference/agentic-sdd.md)

### SK-PERSIST

**GitHub Spec Kit, How to choose a specification persistence model**. Repository snapshot, 2026-11-03. Post-delivery alternatives, team ownership and convergence limits. [Public source](https://github.com/github/spec-kit/blob/a227e38315cd38172b04f2fb8f06ce8b69b38331/docs/how-to/spec-persistence.md)

### SK-INDEX

**GitHub Spec Kit, documentation overview**. Repository snapshot, 2026-11-04. History and configurable processes, integrations, extensions, presets, workflows and bundles. [Public source](https://github.com/github/spec-kit/blob/ec9a6f3b94c0aa856f77e550785a1ddde1993de1/docs/index.md)

### SK-LAUNCH

**GitHub, Spec-driven development with AI: Get started with a new open source toolkit**. 2025-09-02 launch article. GitHub’s framing of intent and specifications as sources of truth for agentic implementation. [Public source](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)

### KI-SPECS

**Kiro, Specs**. Public living documentation, IDE workflow. Feature and bug-fix specs, requirements-first/design-first paths, and dependency-aware parallel task execution. [Public source](https://kiro.dev/docs/specs/)

### KI-QUICK

**Kiro, Quick Spec**. Documentation page dated 2026-08-04. Up-front questions, EARS notation and three generated files without inter-phase approval gates. [Public source](https://kiro.dev/docs/specs/quick-spec/)

### KI-ANALYZE

**Kiro, Analyze Requirements**. Public living documentation. Analysis of requirements for issues such as ambiguity and missing detail. [Public source](https://kiro.dev/docs/specs/analyze-requirements/)

### KI-TEST

**Kiro, Correctness**. Documentation page dated 2026-08-04. Properties derived from requirements, optional tests and triage of implementation, test or requirement failures. [Public source](https://kiro.dev/docs/specs/correctness/)

### KI-STEER

**Kiro, Steering**. Public living documentation. Repository steering files, persistent conventions and AGENTS.md as agent context. [Public source](https://kiro.dev/docs/steering/)

### OS-SCHEMA

**OpenSpec, built-in spec-driven schema**. Repository snapshot, 2026-10-30. Executable artifact dependency graph and task completion checks. [Public source](https://github.com/Fission-AI/OpenSpec/blob/dc37609827c8c3aba49e49347745f47aaa65cb1b/schemas/spec-driven/schema.yaml)

### OS-CONCEPTS

**OpenSpec, Concepts**. Repository snapshot, 2026-10-14. Change workspaces, specification deltas, artifact roles and archive. Use the schema file for exact dependency edges. [Public source](https://github.com/Fission-AI/OpenSpec/blob/e0a2f00f95731af7cf22a30c2c4a8b7ff910b509/docs/concepts.md)

### OS-CONFIG

**OpenSpec, Customization**. Repository snapshot, 2026-10-30. Project context, per-artifact rules and custom or forked schemas. [Public source](https://github.com/Fission-AI/OpenSpec/blob/625834c8fe8b94b4ebc3ae6550e67cd7039fcde8/docs/customization.md)

### OS-TOOLS

**OpenSpec, Supported Tools**. Repository snapshot, 2026-09-22. Skills and command adapters with agent-specific locations and invocation conventions. [Public source](https://github.com/Fission-AI/OpenSpec/blob/fe429a13dc875bf48588ce8239cd57c8d8905955/docs/supported-tools.md)

### BMAD

**BMad Method, How BMad Works**. Public living documentation. Role-based workflow and task-dependent selection of stages. [Public source](https://docs.bmad-method.org/start/how-bmad-works/)

### TESSL-LAUNCH

**Tessl, Tessl launches spec-driven development tools for reliable AI coding agents**. 2025-09-23 vendor launch announcement. Original framework and registry positioning, including code generation from specifications. [Public source](https://tessl.io/blog/tessl-launches-spec-driven-framework-and-registry)

### TESSL-CORE

**Tessl, Core concepts**. Public living documentation. Skills as units of agent context and skill evaluations. [Public source](https://docs.tessl.io/introduction-to-tessl/core-concepts)

### TESSL-SDD

**Tessl Labs, Spec-Driven Development registry package**. Registry version 2.0.1. Spec-writing workflow and test links in .spec.md, with package version pinned and historical availability of this exact version unverified. [Public source](https://tessl.io/registry/tessl-labs/spec-driven-development/2.0.1/files/docs/index.md)

### AUGMENT

**Augment Code, Intent: A workspace for agent orchestration**. Published 2026-02-10, updated 2026-06-18. Vendor example of spec-based coordination and parallel work, separate from N-version evaluation. [Public source](https://www.augmentcode.com/blog/intent-a-workspace-for-agent-orchestration)

## Historical pointer index

All entries have status **unresolved — historical pointer provenance**. This index records each pointer’s original group placements only. The claim table above identifies public evidence at the claim level.

| Opaque identifier | Mentions | Groups |
|---|---|---|
| turn132300academia0 | 2 | CIT-052 (line 142), CIT-054 (line 148) |
| turn132300academia3 | 1 | CIT-004 (line 14) |
| turn228400academia62 | 1 | CIT-082 (line 239) |
| turn228400search0 | 1 | CIT-047 (line 118) |
| turn228400search18 | 1 | CIT-001 (line 8) |
| turn228400search4 | 1 | CIT-046 (line 116) |
| turn228400search5 | 3 | CIT-047 (line 118), CIT-091 (line 280), CIT-098 (line 349) |
| turn228400search6 | 1 | CIT-046 (line 116) |
| turn228400search9 | 2 | CIT-063 (line 193), CIT-098 (line 349) |
| turn287894search0 | 1 | CIT-095 (line 343) |
| turn287894search10 | 1 | CIT-022 (line 64) |
| turn287894search15 | 1 | CIT-039 (line 102) |
| turn287894search19 | 2 | CIT-020 (line 53), CIT-056 (line 154) |
| turn287894search2 | 5 | CIT-002 (line 10), CIT-023 (line 66), CIT-025 (line 73), CIT-028 (line 76), CIT-029 (line 77) |
| turn287894search24 | 1 | CIT-042 (line 108) |
| turn287894search28 | 1 | CIT-048 (line 120) |
| turn287894search29 | 1 | CIT-022 (line 64) |
| turn287894search31 | 1 | CIT-045 (line 114) |
| turn287894search34 | 5 | CIT-007 (line 24), CIT-045 (line 114), CIT-048 (line 120), CIT-080 (line 232), CIT-089 (line 274) |
| turn287894search4 | 2 | CIT-022 (line 64), CIT-028 (line 76) |
| turn287894search41 | 1 | CIT-040 (line 104) |
| turn287894search7 | 8 | CIT-003 (line 12), CIT-018 (line 49), CIT-030 (line 78), CIT-036 (line 93), CIT-042 (line 108), CIT-055 (line 152), CIT-092 (line 326), CIT-095 (line 343) |
| turn287894search8 | 2 | CIT-023 (line 66), CIT-087 (line 270) |
| turn492537view5 | 1 | CIT-001 (line 8) |
| turn492537view6 | 1 | CIT-001 (line 8) |
| turn492537view7 | 4 | CIT-044 (line 112), CIT-057 (line 160), CIT-085 (line 252), CIT-095 (line 343) |
| turn492537view8 | 9 | CIT-002 (line 10), CIT-022 (line 64), CIT-026 (line 74), CIT-029 (line 77), CIT-041 (line 106), CIT-057 (line 160), CIT-062 (line 191), CIT-085 (line 252), CIT-095 (line 343) |
| turn530671view0 | 2 | CIT-006 (line 18), CIT-069 (line 212) |
| turn530671view1 | 5 | CIT-051 (line 140), CIT-073 (line 224), CIT-077 (line 229), CIT-097 (line 347), CIT-099 (line 351) |
| turn530671view2 | 1 | CIT-069 (line 212) |
| turn530671view3 | 6 | CIT-006 (line 18), CIT-034 (line 85), CIT-037 (line 98), CIT-070 (line 214), CIT-097 (line 347), CIT-099 (line 351) |
| turn530671view6 | 8 | CIT-006 (line 18), CIT-019 (line 51), CIT-050 (line 138), CIT-071 (line 216), CIT-073 (line 224), CIT-078 (line 230), CIT-086 (line 256), CIT-097 (line 347) |
| turn530671view7 | 17 | CIT-009 (line 31), CIT-031 (line 79), CIT-058 (line 166), CIT-059 (line 171), CIT-061 (line 175), CIT-062 (line 191), CIT-063 (line 193), CIT-064 (line 195), CIT-067 (line 208), CIT-075 (line 226), CIT-078 (line 230), CIT-081 (line 235), CIT-084 (line 250), CIT-090 (line 278), CIT-097 (line 347), CIT-099 (line 351), CIT-100 (line 353) |
| turn547616academia10 | 3 | CIT-035 (line 91), CIT-065 (line 199), CIT-079 (line 231) |
| turn547616search5 | 2 | CIT-016 (line 45), CIT-094 (line 341) |
| turn547616search6 | 1 | CIT-072 (line 218) |
| turn547616search7 | 1 | CIT-071 (line 216) |
| turn547616search8 | 1 | CIT-014 (line 42) |
| turn628524search0 | 4 | CIT-038 (line 100), CIT-039 (line 102), CIT-091 (line 280), CIT-098 (line 349) |
| turn628524search2 | 10 | CIT-020 (line 53), CIT-021 (line 62), CIT-026 (line 74), CIT-027 (line 75), CIT-032 (line 81), CIT-053 (line 146), CIT-056 (line 154), CIT-076 (line 227), CIT-085 (line 252), CIT-092 (line 326) |
| turn628524search3 | 2 | CIT-002 (line 10), CIT-032 (line 81) |
| turn860486search0 | 1 | CIT-094 (line 341) |
| turn860486search1 | 4 | CIT-008 (line 29), CIT-010 (line 37), CIT-094 (line 341), CIT-100 (line 353) |
| turn860486search12 | 2 | CIT-011 (line 38), CIT-018 (line 49) |
| turn860486search15 | 1 | CIT-008 (line 29) |
| turn860486search2 | 5 | CIT-003 (line 12), CIT-012 (line 39), CIT-017 (line 47), CIT-030 (line 78), CIT-094 (line 341) |
| turn860486search26 | 2 | CIT-003 (line 12), CIT-017 (line 47) |
| turn860486search39 | 2 | CIT-013 (line 41), CIT-094 (line 341) |
| turn860486search52 | 2 | CIT-003 (line 12), CIT-013 (line 41) |
| turn860486search58 | 1 | CIT-012 (line 39) |
| turn860486search9 | 2 | CIT-011 (line 38), CIT-094 (line 341) |
| turn899470search0 | 5 | CIT-005 (line 16), CIT-068 (line 210), CIT-082 (line 239), CIT-096 (line 345), CIT-099 (line 351) |
| turn970210search1 | 10 | CIT-024 (line 72), CIT-033 (line 83), CIT-043 (line 110), CIT-049 (line 133), CIT-060 (line 173), CIT-066 (line 201), CIT-088 (line 272), CIT-093 (line 328), CIT-095 (line 343), CIT-100 (line 353) |
| turn970210search15 | 4 | CIT-033 (line 83), CIT-066 (line 201), CIT-088 (line 272), CIT-093 (line 328) |
| turn970210search16 | 1 | CIT-060 (line 173) |
| turn970210search2 | 1 | CIT-016 (line 45) |
| turn970210search20 | 4 | CIT-007 (line 24), CIT-038 (line 100), CIT-049 (line 133), CIT-089 (line 274) |
| turn970210search23 | 6 | CIT-015 (line 43), CIT-031 (line 79), CIT-040 (line 104), CIT-074 (line 225), CIT-087 (line 270), CIT-100 (line 353) |
| turn970210search24 | 4 | CIT-024 (line 72), CIT-066 (line 201), CIT-088 (line 272), CIT-095 (line 343) |
| turn970210search25 | 2 | CIT-033 (line 83), CIT-093 (line 328) |
| turn970210search26 | 5 | CIT-007 (line 24), CIT-044 (line 112), CIT-049 (line 133), CIT-080 (line 232), CIT-091 (line 280) |
| turn970210search3 | 1 | CIT-043 (line 110) |
| turn970210search30 | 1 | CIT-083 (line 241) |
| turn970210search4 | 2 | CIT-021 (line 62), CIT-095 (line 343) |
| turn970210search7 | 1 | CIT-024 (line 72) |
