# Actionable Bootstrap & Development Roadmap  


> **Editorial review — 12 November 2026.** Distinguished the proposed bootstrap-specific handoff contract from general agile practice; aligned the examples with the accepted PROJECT_CONVENTIONS.md v0.1 (D01–D10); corrected misleading Git, licensing, toolchain and first-agent examples; and clarified that “implementation-ready” is not “implemented,” “tested,” or “production-ready.” Review anchors appear below. The accepted methodology conventions govern generated handoffs; this research report does not independently override them.


**Research Date:** November 11, 2026  
**Scope and Non-Goals:** This report addresses how to produce a minimal, *actionable* project bootstrap for a Spec-Driven Development (SDD) workflow and how to translate validated requirements into a prioritized, evidence-backed development roadmap.  It assumes the SDD skill has distilled user intent into requirements, clarifications, and design decisions.  We focus on the *handoff* package (ZIP/repo) and planning artifacts, **not** on implementing or deploying any code. For generated projects, the accepted *PROJECT_CONVENTIONS.md v0.1* (D01–D10) provides the default, adaptable operating contract. Project-specific exceptions require documented human authorization; optional directories and files remain conditional.  


**Executive Summary:** An effective bootstrap delivers a clear “Start Here” experience: a structured repository with documentation (README, PRD, architecture outline), a backlog of tasks, and no surprise code. It must explicitly **declare what is absent** (no executable) and what to do first.  Each near-term implementation item should have sufficient context and testable acceptance criteria to start safely; INVEST is a useful story-writing heuristic, not a universal Definition of Ready or gate for every spike, research task or creative project.  For product work where useful, the initial development roadmap can be organized into vertical slices and milestones: e.g. a first “walking skeleton” vertical slice spanning UI, logic, and data, followed by additional slices.  Techniques like **tracer bullets** (quick end-to-end prototypes), **user-story mapping**, and **impact mapping** guide feature prioritization and sequence.  Roadmap tasks are classified (implementation, research spike, decision/ADR, acceptance test, etc.) and ordered by dependencies, risk, and value.  A rubric drives when to produce a full spec (with acceptance criteria) versus leaving a backlog item or spike: high-priority, low-uncertainty items get concrete specs; high-uncertainty or architectural questions become spikes or ADRs.  We must provide clear traceability: assign stable IDs (e.g. `REQ-001`, `SPEC-002`, `TASK-010`) and link requirements→specs→tasks→tests so nothing is orphaned.  


For the **first agent session**, provide a bounded approved task with its specification, acceptance criteria, dependencies and authority boundaries. One task per session and a dedicated branch can be useful defaults, but are **workflow choices**, not universal requirements; parallelism is safe only when write scopes and integration ownership are clear. Concurrency (multiple agents) is managed by clear task boundaries and separate branches.  Deployment-specific prerequisites (toolchains, accounts, secrets, licenses) are *declared* but not embedded: we list them in README/prerequisites and interview questions. The scaffold includes only useful files and placeholders; empty `src/`/`tests/` directories and a placeholder `LICENSE` are not mandatory and can be misleading. The user is explicitly told this is a scaffold (e.g. in README) so they are not surprised by “no executable.”  


We define lightweight **acceptance gates** for the bootstrap: consistency across PRD/architecture/backlog, at least one genuinely unblocked **implementation** task, no unresolved showstopper assumptions, and a reproducible structure (test archive extraction, check metadata).  Automated checks can verify file presence, linkable IDs, and clean markdown; human review must verify feasibility, scope-boundedness, and clarity of next steps.  


Finally, we outline an MVP for the skill itself (interview prompt templates, minimal QA checklists, roadmap generation heuristics) versus future enhancements (more automation, analytics). We propose pilot evaluation metrics (e.g. time-to-first-task, backlog clarity) and fault-injection tests (e.g. missing secrets, ambiguous spec) to validate the approach.  Recommendations synthesize established agile/requirements-engineering guidance with proposed SDD Bootstrap v0.1 heuristics; the package design is not itself an empirically validated industry standard. 


---


## 1. Actionable Bootstrap Deliverables  


**Proposed bootstrap contract, not an industry-wide rule:** For this Skill, the intended handoff is a **planning/scaffold package**, not a newly implemented application. Include only project-relevant documents and directories. The project conventions are an **accepted methodology baseline**, not a mandate to create empty directories. An existing repository may already contain code that the bootstrap must accurately inventory rather than erase. The README or a dedicated **Getting Started** section must state that a new bootstrap contains no newly implemented runnable product, or accurately distinguish pre-existing code when working in an existing repository, and guide the user's first steps. This follows general best practices (e.g. READMEs describing prerequisites and quick-start steps) and ensures transparency. For example, a recommended README could begin:


> *“**Bootstrap Summary:** This repository contains project definitions and plans. No new executable application has been implemented by this bootstrap. Read through the documentation to understand the requirements and planned tasks, then pick the first task described below to implement.”*


We should include:  
- **Overview/Scope:** A short project description or PRD summary outlining goals and scope (what is in/out of scope).  
- **Start Here Checklist:** A “hand-off summary” or README section explicitly titled “Start Here” or “Bootstrap Readiness” that lists the contents of the zip and first actions. (See *Sample “Bootstrap Readiness Summary”* below.)  
- **Prerequisites:** A list of required tools or accounts (e.g. programming language versions, cloud accounts, payment of services, licenses needed). These belong in the interview or README, not embedded in code.  
- **Project Conventions:** Link the accepted v0.1 contract (D01–D10). For a new repository, the default baseline is an initialized Git repository with `main` and `dev` plus a truthful initial commit. The user selects ZIP or, if available and explicitly authorized, direct publication to a personal GitHub account. Record the actual author/committer identity, optional agent co-author policy, and any authorized project exception.  
- **Directory Structure:** Create only files and directories justified by actual project artifacts, e.g. `docs/PRD.md` and `docs/BACKLOG.md`; do not add empty placeholder directories. A short, **useful** `AGENTS.md` pointing to real authoritative sources and authority limits, not an empty TODO placeholder. Do not insert a placeholder `LICENSE` that could be mistaken for a valid license grant; instead record **licensing unresolved / publication blocked pending decision** where necessary.  
- **No Secret Artifacts:** Explicitly state that no secret keys or credentials are included. If configuration files need secrets, leave placeholders and refer user to follow instructions to populate them.  


**Candidate contents (risk-proportionate):** `README.md` with start-here/status, authoritative requirement/specification links, prioritized `BACKLOG.md`, a compact `AGENTS.md` when coding agents are expected, explicit open decisions, and planned verification. Architecture details, ADRs, `CONTRIBUTING.md`, licensing files, `.agents/`, `src/`, and test directories are conditional on actual need; the applicable `PROJECT_CONVENTIONS.md` contract is included. A new implementation-ready bootstrap has a verified initial Git baseline with `main`/`dev` unless an approved exception applies: ZIP mode includes `.git/`, while authorized personal-GitHub mode verifies the remote history. Select the delivery channel and obtain only missing truthful identity metadata; never fabricate a human commit identity or claim an unperformed publication.  


**Not generated by this bootstrap:** no new runnable product, application binary, working server, APK, validated build, or deployed environment. If bootstrapping an **existing** repository, pre-existing files may remain and must be inventoried separately; existing code is not evidence that new specifications were implemented. The README must state exactly what the delivered ZIP includes and excludes.  


**First Actions Made Obvious:** The README should clearly say where to begin. For example:  


- **Getting Started:** A checklist enumerating exactly what files to read (e.g. “1. Review `docs/PRD.md` for requirements.  2. Review `docs/ARCHITECTURE.md` for proposed design, if present.  3. Open `docs/BACKLOG.md` to see the task list (use a board only if the project actually has one). 4. Select the first approved, unblocked task from `docs/BACKLOG.md` and read its acceptance criteria.  5. Begin implementation of TASK-001.”)  
- **Unimplemented Notice:** A statement like “All features are proposed. No code has been written yet. Implementation tasks are marked TODO.”  


By following these guidelines (consistent with SDD principles) the bootstrap is “actionable”: the user knows *exactly* what to do first, sees the project structure, and understands that code must be written, not found.  


> **Sample Bootstrap Readiness Summary (illustrative):**  
> ```markdown
> **Bootstrap Readiness Summary (Draft - illustrative)**  
> - Git baseline: `not yet verified` until an actual initial commit and `main`/`dev` are checked. ZIP: verify `.git/` after extraction; personal-GitHub delivery: verify the authorized remote. An approved exception must be recorded.  
> - `README.md` includes project description, prerequisites, and “Getting Started” steps.  
> - `docs/PRD.md`: High-level requirements and scope (with version “Proposed”).  
> - `docs/ARCHITECTURE.md`: Proposed high-level design (marked Draft).  
> - `docs/BACKLOG.md`: List of features/user stories split into tasks (each with status TODO/Review).  
> - `docs/decisions/`: include only if actual decisions/ADRs warrant it; no empty directory required.  
> - **No newly implemented executable code included.** At least one specific, approved-scope **implementation task** is feasible, sufficiently specified and unblocked. A research spike may precede it but cannot alone satisfy this gate.  
> - **Prerequisites:** runtime/toolchain version `TBD`; account/billing owner `TBD`; deployment target `TBD`. No real secrets included; no resources provisioned.  
> ```  


## 2. Implementation Roadmap Planning  


**Findings:** Effective roadmaps in agile/SDD emphasize delivering end-to-end functionality in increments. A *walking skeleton* is defined as a minimal, end-to-end implementation that exercises all layers of the architecture. A *tracer bullet* is similarly a thin vertical slice built early to validate direction. Both contrast with purely horizontal slices (e.g. “build all UI first, then all business logic”), which can delay user value. Vertical slicing delivers usable features sooner. 


User-story mapping is recommended to visualize priority and sequence. For example, TasksBoard explains that a story map arranges features by the user journey (horizontal axis) and importance (vertical axis), making clear the “walking skeleton” (top row) and subsequent release slices. Impact mapping (goals→impacts→deliverables) is another collaborative planning method to ensure features align with business outcomes.


**Comparative Strategies:** We compared techniques:


- **Walking Skeleton (Cockburn)**: Build a tiny end-to-end feature that connects all main components. Pros: establishes continuous integration, reveals infra issues early. Cons: low user functionality initially.
- **Tracer Bullet (Pragmatic Programmer)**: Create minimal runnable slices through the system to verify assumptions. Pros: quick feedback, low cost for validation. Cons: might not look like final UI.
- **Vertical Slice / Thin MVP Slice**: Split features so each slice is complete (UI→backend→DB). Pros: delivers user value per increment, easier to test. Cons: needs some base architecture in place.
- **Horizontal Layering**: Build one layer across all features (e.g. UI forms first). Cons: yields no end-user feature until later, delaying validation.
- **Story Mapping**: Visual planning by user journey (as above). Identifies core flows and release cuts.
- **Impact Mapping**: Links features to user behaviors and business goals. Helps prioritize tasks that make an impact.
- **Risk-First Prototyping / Spikes**: Do quick experiments on highest-risk areas (e.g. third-party API integration) to reduce uncertainty before core dev. 
- **Progressive Elaboration**: Plan in broad strokes, refine details as more is known (an agile rule). 
- **Dependency DAG/PERT**: Graph dependencies for critical path analysis (less commonly done manually in small teams but useful for planning).


**Evidence vs. Recommendations:** Many of these are practiced in industry. For example, INVEST is a story-quality heuristic, not a formal prohibition on infrastructure or layer-focused work. Vertical slices often improve feedback, while a horizontal enabling task may still be justified by dependencies or risk. The DevOps community championed walking skeleton to avoid late integration issues. Our recommendation (MVP architecture) is to combine these: start with one high-level use case as a walking skeleton/tracer bullet, then iteratively add vertical slices. Use story-mapping workshops with stakeholders to validate release boundaries (consistent with Jeff Patton’s agile guidance). 


**Proposed Approach:** 


1. **Vertical Slicing & Skeleton:** Identify the minimal “core flow” that proves the architecture. For example, if building a web service, the first slice could be “User login with dashboard”. This satisfies at least one small end-to-end feature. Create tasks across UI, API, and data for this flow. Mark this as Milestone 1 (Walking Skeleton).  
2. **Sequencing by Dependency and Value:** List all high-priority features. For each, do vertical decomposition. Order them so that dependencies are satisfied and value is delivered early. For instance, data schema tasks before features that need them.  
3. **Milestones / Releases:** Group tasks into milestones or “release slices” (e.g. MVP, Beta, etc.). Story mapping can help define these releases by highlighting which features fit in the first cut vs. later.  
4. **Tracers & Spikes:** For any high-risk unknown (e.g. untested library or external service), allocate time as a “spike” to experiment. Implement a quick tracer bullet slice for it (e.g. a dummy call to the API) to inform later dev.  
5. **Progressive Elaboration:** Keep major features on the backlog initially as epics. As work proceeds, break epics into specific stories/tasks in story/burndown form, refining acceptance details on the go.  
6. **Tools:** Use a backlog/roadmap chart (even a simple Kanban board) to visualize tasks and status. With traceability in mind, label tasks with IDs and link to requirements.  


The roadmap should clearly label *“Do Now”, “Do Later”, “Deferred”* priorities. High-risk or foundational tasks (architecture, infrastructure setup) go first, then core features (value-add), leaving polish/edge-cases for last.  Tasks are classified: implementation, research spike (uncertainty), decision/ADR tasks, test/verification tasks, deployment-prep tasks. Label each with an estimated or “critical path” order.  


> **Sample Roadmap (YAML, illustrative):**  
> ```yaml
> roadmap:
>   - milestone: "M1: Core Architecture"
>     tasks:
>       - id: TASK-001
>         name: "Set up database schema"  
>         depends_on: []  
>       - id: TASK-002
>         name: "Implement user authentication (login)"  
>         depends_on: [TASK-001]  
>       - id: TASK-003
>         name: "REST API framework skeleton (health check endpoint)"  
>         depends_on: []  
>   - milestone: "M2: Core Features"
>     tasks:
>       - id: TASK-004
>         name: "Build user profile page"  
>         depends_on: [TASK-002, TASK-003]  
>       - id: TASK-005
>         name: "Add settings/preferences UI"  
>         depends_on: [TASK-004]  
>   - milestone: "M3: Beta Release"
>     tasks:
>       - id: TASK-006
>         name: "Integrate payment API (spike)"  
>         depends_on: [TASK-003]  
>       - id: TASK-007
>         name: "Implement checkout flow"  
>         depends_on: [TASK-006]  
> ```
> *This roadmap shows vertical slices: M1 is the initial skeleton, M2 adds more user-facing features, M3 covers payment. Dependencies ensure a critical path. (IDs are illustrative.)*  


## 3. Specs, Backlog Items, Spikes, ADRs  


**Verified Insights:** In agile/Scrum parlance, a **Definition of Ready (DoR)** helps decide if a backlog item is actionable. It typically requires that a story/task is independent, well-defined, and *testable*. The agile INVEST checklist explicitly includes *Testable* as a criterion – meaning acceptance criteria are specified. If an item lacks these (e.g. missing details, unclear success conditions), it should not be pulled into development as-is. Instead, it becomes a refinement task or a “spike.”  


**Proposed Decision Rubric:** Based on priority, risk, and clarity, we classify outputs as:  


- **Concrete Spec (with AC):** For high-priority features or changes whose requirements and design are relatively well-understood, we produce a formal spec (in `docs/specs/` or inline in backlog) with clear acceptance tests. Each acceptance criterion should be unambiguous and testable. This spec is treated as ready for implementation.  
- **Backlog Item:** A user story or task on the backlog without full details yet. It is marked *TODO* or *Pending*. We list any known info, but note that acceptance criteria are incomplete. For example, “User can log in” might be a backlog item whose spec is in `docs/specs/`. If a backlog item is high priority but still has open questions, it must be clarified (see Questions below). Until clarified, it remains as a _backlog placeholder_, not a developer “start now” card.  
- **Spike/Research Task:** If an item has high uncertainty (new technology, ambiguous requirement) or depends on external factors, we explicitly create a spike story. This is time-boxed research/experiment work, not full implementation. For example, “Spike: Evaluate cloud DB options.” Spikes have a goal (answer a question) rather than a feature AC.  
- **ADR/Decision Task:** If a design or tech choice needs formal decision (e.g. database type, architecture variant), we create an Architecture Decision Record (ADR) or a decision ticket. This is distinct from implementation. For example, “ADR: Choose payment provider – Stripe vs PayPal.” An ADR has its own context and acceptance (e.g. “decision logged by team”).  
- **Questions/Assumptions:** Any open questions arising during analysis (e.g. “What user roles are needed?”) are logged (in backlog or docs) as items requiring answers from stakeholders. They may become backlog tasks if they trigger spec changes.  


In practice, we say: **If a task meets DoR/INVEST (small, independent, with AC), make it an implementable task.** Otherwise, if it is important but missing details, *do not* mark it “In Progress”; leave it as backlog/To-Do and note what’s missing.  


For example, Atlassian’s DoR emphasizes testability. So if a story has no clear acceptance criteria, we treat it as “Not Ready” – either write those criteria first (spec) or spawn a sub-task to define them. Only after AC are defined does that item become “Ready for Dev.”  


> **Example:** Suppose a feature “Integrate Payment API” is needed (high priority). Initially we might only know it involves an external service, but not which one. We create a *Backlog Item* (TODO) with description and list open questions. We also create a *Spike* story “Explore Payment Providers” as the first step. Only after the spike yields a decision (say, select Stripe) do we write a detailed spec (with API endpoints, error handling AC) and then split it into implementation tasks.  


This rubric ensures the skill *does not rush into code* without clarity, and it prevents vague backlog items from being accepted prematurely.  


## 4. Traceability and Identification  


**Best Practices:** Traceability means every requirement, design decision, implementation task, and test is linked. A typical approach (used in industries and ALM tools) is a **traceability matrix**: list requirements and show which tasks/tests fulfill them. In our context, we keep everything in plain markdown/ADRs, but we must maintain this linkage manually.  


Recommendations:  
- **Stable IDs:** Assign low-overhead IDs for each element. For example:  
  - Requirements or user stories: `REQ-###` or `STORY-###`.  
  - Spec documents: `SPEC-###`.  
  - Tasks/backlog items: `TASK-###` or `TICKET-###`.  
  - ADRs/Decisions: `ADR-###`.  
  - Test cases or verification scripts: `TEST-###`.  
  - Milestones/releases: `M#`.  
- **Cross-Referencing:** In each spec or task description, mention related IDs. For instance, a spec might say “Satisfies REQ-001.” A task item would refer to its spec or user story ID. This mimics Atlassian’s advice to “Connect each requirement to tasks, stories, or test cases”.  
- **Status Semantics:** Clearly mark status of each ID: Proposed, Draft, In-Progress, Done. For example, prefix an ID with `(Proposed)` or add a column “Status.” Distinguish things created by the bootstrap (proposed) from those verified/implemented. Avoid claiming anything is complete that hasn’t been tested or accepted by the user.  
- **Traceability Map:** Include a minimal traceability table (in docs/) that shows “REQ→SPEC→TASK→TEST”. For example, it might list REQ-001 (“User login works”) traced to SPEC-001 (“Login Spec”), to TASK-005 (“Implement login flow”), to TEST-003 (“Login test script”). Update it as items are added.  


> **Sample Traceability Map (illustrative):**  
> ```markdown
> | ID       | Type          | Description                 | Links (Related IDs)     | Status     |
> |----------|---------------|-----------------------------|-------------------------|------------|
> | REQ-001  | Requirement   | User can log in securely    | SPEC-001, TEST-001      | Proposed   |
> | SPEC-001 | Spec          | Login feature (draft)       | REQ-001, TASK-001       | Draft      |
> | TASK-001 | Implementation Task | Build login API endpoint | SPEC-001, REQ-001       | To Do      |
> | TEST-001 | Verification  | Automated login tests       | SPEC-001, REQ-001       | Pending    |
> ```  
> *In this table, each ID links to artifacts of different types. For example, TASK-001 depends on SPEC-001 and REQ-001. (Columns are illustrative and not project rules.)*  


By keeping IDs and links simple (text, no special tooling), we avoid overhead while enabling the team to trace feature coverage. This also supports the SDD principle of end-to-end traceability from requirements to code.  


## 5. First Sprint / First Agent Session Package  


**Background:** The first development session should be laser-focused. Based on agile/agentic practice, an agent or team member should begin with a clearly bounded task and no hidden assumptions; one task per session is a useful option, not a mandatory rule. The `AGENTS.md` file (or equivalent) is used to instruct agents (e.g. Codex, Kiro) about the workflow.  


**Content for Agent:** The initial prompt to an AI agent should include:  
- Context from AGENTS.md (brief system instructions, e.g. “You are a coding agent using spec-driven development.”).  
- The specific first backlog item ID and its content (title, description, acceptance criteria).  
- Any relevant excerpts (e.g. a small part of the spec or PRD that clarifies the task). Don’t dump everything at once—only the pieces needed for this task.  
- Instructions on what to produce: usually “draft a plan” first, then “implement code” in a new branch once the plan is approved.  
- Clarify boundaries: e.g. “Do not modify other parts of the project; focus on this task only.”


**Example Agent Prompt:**  


```text
Task: TASK-001 - "Implement user authentication (email/password login)"
Description: Implement the login API endpoint and UI form as per SPEC-001.
Acceptance Criteria: [List acceptance criteria from SPEC-001 here.]
Instructions: 
1. Outline an implementation plan (approach, libraries, endpoints to use). 
2. After approval, generate code for the API endpoint and login form, including tests. 
Use a new Git branch named `feat/auth`. Wait for review at each step.
```  


In this way, the agent’s “job” is clearly scoped. Backlog.md’s recommended workflow is similar: *“Work on a single task per agent session, one PR per task”*. Reviewers check the applicable plan, code, verification evidence and required approvals before marking the task done; one PR per task is a tool-specific workflow option.  


**Multi-Agent Coordination:** If multiple agents or team members work concurrently, we must prevent conflicts. Best practice is one active feature branch per task/story. The `AGENTS.md` or team process should ensure: *an agent only works on TASK-n as named, and other agents see it as “in progress”*. Merging only happens after review. In *Backlog.md* flow, tasks are independent so agents don’t overlap. The roadmap should clearly split responsibilities (e.g. “Frontend” vs “Backend” tasks). 


**Branch/Handoff Conventions:** The approved default is a focused topic branch from `dev` (e.g. `feat/TASK-001` or `fix/TASK-002`), with actual project exceptions documented. A completed change or paused session leaves a traceable handoff, commit or review reference as applicable; a PR is not required after every conversation. Integrate to `dev` only after the required checks and authorization; promotion to `main` requires explicit human approval. Task status reflects actual work and evidence, not merely a commit. 


**First-Sprint Package:** A new bootstrap contains a verified baseline Git commit and at least one approved-scope, unblocked implementation task (for example `TASK-001`) with traceable acceptance criteria. In ZIP mode, `.git/` accompanies that baseline; in authorized personal-GitHub mode, the same history is verified remotely. The first agent session picks up the task. Include a concise, useful `AGENTS.md` when needed; never leave an empty or misleading instruction placeholder. Avoid giving the agent the entire codebase context (especially if large); rather, sequentially expand context as tasks are completed.  


> **Illustrative First Agent Prompt (in AGENTS.md or conversation):**  
> ```text
> Agent, please begin with *TASK-001: Implement user authentication*. The details and acceptance criteria are in the backlog. Outline how you would implement login (data model, endpoints, UI). Then pause for approval before coding.
> ```  


## 6. Prerequisites, Environment and Accounts  


**Separating Concerns:** Some project-specific setup (toolchains, accounts, environment) must be handled, but we decide what belongs to the bootstrap vs what to get from the user. Typically, *developers must obtain these, not the skill*.  


**In Interview:** During the initial requirements interview or clarification phase, the skill should ask about:  
- **Target platforms:** Web, mobile, desktop, embedded? This affects dependencies.  
- **Technology preferences:** Language (Java, Python, JS), frameworks (React, Django), and any mandated tech.  
- **Required accounts/services:** Cloud providers (AWS, Azure, Firebase), databases (MongoDB Atlas, etc.), third-party APIs (e.g. payment gateway accounts, OAuth providers), container registries. If free tiers are needed or credentials created, inform the user.  
- **Licensing needs:** If certain libraries require payment or licenses (e.g. a mobile dev kit, game engine), the user must know.  
- **Infrastructure:** CI/CD services (GitHub Actions, Jenkins), mobile build setups (Android keystore, iOS certs), where the app will run (on-prem vs cloud).  
- **Test data and secrets:** Should ask if any sample/test data or keys exist or need provisioning.


These details are captured as part of the project plan or a “Prerequisites” section in the README. For example, a standard README would have a section **Prerequisites** listing things like “Install Node.js v18, Python 3.10, AWS credentials with IAM user having DynamoDB access,” etc. Good README templates even call out environment assumptions. 


**In Bootstrap Deliverable:** We **do not include secrets or accounts** in the ZIP. Instead:  
- In the README or `docs/SETUP.md`, list what tools to install and which accounts the user must create before running code. For each, note if there is a free tier or trial. E.g. “Create a free-tier MongoDB Atlas account, and store the URI in an environment variable MONGODB_URI.”  
- If the project will eventually be deployed, note the target (e.g. “This will eventually be deployed to Heroku/Azure” under Architecture).
- Provide placeholder files (e.g. `config.example.json`) with instructions to rename and fill in secrets.


By asking these in interview and documenting them, we avoid surprises later. The user is aware up front of any external requirements; the bootstrap code can then assume their presence.  


## 7. Repository Scaffold Content  


**What to Include:** The scaffold should show enough structure to guide development, without implementing features. Include:  
- **Directories and files:** Create `src/`, `app/`, `tests/` or other technical paths only when a justified artifact needs them. Do not add empty directories or dummy code merely to make a future layout visible; describe the planned layout in architecture documentation instead.  
- **Configuration templates:** Include a stack-specific manifest, Dockerfile or build template only if its purpose and target are justified for the first development step. Mark non-executed templates explicitly; do not create misleading empty dependency manifests or pretend a template is a verified build.  
- **CI template (optional):** Include a workflow only when there is a real, bounded check to define. Never add a no-op CI workflow that might be mistaken for validated delivery automation.  
- **License and contributing:** Add root `LICENSE.md` only after the project owner approves actual applicable license terms. Otherwise record unresolved licensing and any publication block without a pseudo-license. `CONTRIBUTING.md` is conditional on collaboration needs.  
- **Mockups/Designs:** If UX wireframes or mockups were mentioned in requirements, it is acceptable to include reference images or diagram placeholders in `docs/` (especially if they guide development). These are documentation-only, not code.  
- **Executable Boilerplate:** Generally **do not** include a working “Hello World” app unless the user explicitly expects it. We want to avoid overstepping the spec: it’s a bootstrap, not a full implementation. If a *minimal* “app skeleton” contradicts user instructions, skip it. Instead, use the backlog tasks to prompt the agent to create those files.  


**Git and Versioning (accepted D01/D10 default):** A new implementation-ready handoff has an initialized repository, truthful baseline commit, suitable `.gitignore`, and `main` plus initial integration branch `dev`, unless an authorized, documented exception applies. Offer a downloadable ZIP with `.git/` and verify its history after extraction; if an authorized connector supports the user's personal GitHub account, also offer direct publication with explicit approval of account, repository and visibility. In that mode, verify the remote commit/branches. Request missing author/committer details only when necessary; agent self-attribution is permitted by default but optional, and never substitutes for the real initial-commit identity. A bootstrap baseline is not a production release.  


> *When a runnable boilerplate conflicts with expectations:* If the user specifically asked *not* to produce any runnable code, then providing even a minimal “index.html” might confuse them. In that case, stick to documentation-only scaffolding. The key is to reflect user wishes: **if in doubt, err on the side of offering a plan rather than code.**  


## 8. Acceptance Gates for the Bootstrap  


Before delivering the bootstrap to the user, run through an internal checklist (some automated, some human). Key items:  


- **Consistency Checks:** Verify that the PRD, architecture, specs, and backlog align. For example, every backlog item should trace to at least one requirement, and each requirement should appear in specs or ADRs. Ensure no two specs contradict (scope not overlapping). Spell-check and link-check the documentation (URLs, cross-IDs).  
- **Feasibility / Sanity:** Is at least one implementation task genuinely unblocked, sufficiently specified and tied to approved scope and verifiable acceptance criteria? A time-boxed clarification/decision spike may precede implementation but does **not** satisfy the v0.1 implementation-readiness gate by itself. If all implementation tasks are blocked, label the package incomplete rather than ready.  
- **Dependency Readiness:** Flag any missing prerequisites needed before work begins (e.g. needed API keys, data models). These should be noted as interview action items or high-priority tickets, not hidden.  
- **Unresolved Assumptions:** Check for any remaining assumptions in the docs. If an assumption can be resolved now, do it. Otherwise, document it explicitly as an assumption in the spec or backlog (so it’s visible).  
- **Reproducible Setup:** Test unzipping and basic scripts. For example, if there is a build or lint config, run it (even if it does nothing) to catch syntax issues. Ensure file permissions allow execution if needed.  
- **No Secrets Leaked:** Confirm no API keys, passwords, or sensitive URLs are present. If secret placeholders exist, verify they’re clearly labeled.  
- **Git Integrity:** For a new repository, verify the actual baseline commit and default `main`/`dev` (or an authorized, documented exception). ZIP mode verifies `.git/` and branches after extraction; personal-GitHub mode verifies the actual remote repository, history, account and visibility. Existing repositories retain their recorded primary branch name unless a separate authorized change occurs.  
- **Explicit Ownership/Approval:** Each document (esp. specs and ADRs) should have an author or “owner” listed (even if just placeholder “(Name TBD)”). A reference to a human reviewer or stakeholder approval is ideal on key docs.  
- **First Task Clarity:** The very first backlog item must have clear instructions. As a test, imagine handing the ZIP to a new developer: Can they open the first issue and understand it? If ambiguous, refine it now.  
- **Handoff Clarity:** Include a brief handoff note (in the README or an email template): “Review the above artifacts. Your first task is [TASK-001]. See `docs/BACKLOG.md`.”  


**Automated vs. Manual Checks:** 
- *Automatable:* file presence (README, BACKLOG, etc.), ID format regexes, markdown link validation, no broken relative links, no large binary files, archive extraction test, `.gitignore` entries. Tools like markdown lint and link checkers can be run.  
- *Manual:* content consistency (the “sanity” checks above), business logic feasibility, and uncovered scope. These require human domain knowledge.  


This gate ensures that the bootstrap passes basic quality standards (like a Definition of Done for the bootstrap itself). It parallels the “gap analysis” proposed by Gavrylenko, where we explicitly check if “the value is clear, scope is bounded, requirements traceable, assumptions visible”. Unresolved gaps are recorded in the **open-issues/backlog or decision queue**; `docs/UPDATES.md`, if adopted, records only actions actually performed and their evidence.  


## 9. MVP Design and Future Iterations  


**MVP Features (v0.1):** For the skill itself to output this bootstrap, the minimum viable implementation should include:  
- **Template Artifacts:** Markdown templates for README (with placeholders), spec template, backlog format, ADR stub.  
- **Interview Prompt Flows:** A guided set of questions/prompts to elicit stack choices and prerequisites. (This could be as simple as an initial conversation script.)  
- **Roadmap Generation Heuristic:** A basic algorithm or ruleset that orders features by dependencies and value. Even a simple list sorted by priority is a start.  
- **Linter/Checklist:** A built-in checklist (from section 8) to validate the generated docs (e.g. Python or YAML list of questions to confirm).  
- **Examples and Guidance:** In-code comments or hidden instructions illustrating how to fill in missing pieces.  


**Out-of-Scope for MVP (v0.1):**  
- Automated CI integration or actual project creation scripts.  
- Complex AI logic beyond scripted prompts (e.g. no trained model needed; just prompt engineering).  
- Paid services or external integrations beyond what the user provides.  
- Overly complex backlog analysis (e.g. no full dependency DAG solver).  


**Future (v0.2+):**  
- Improved AI plans (let agent propose priorities), plugin to tools like Backlog.md for live editing.  
- Customizable templates (support different tech stacks).  
- Empirical feedback loop (learning from pilot metrics).  
- Support for partial code scaffolding if user desires.  


## 10. Pilot Evaluation and Testing  


To validate the bootstrap approach, we propose pilot projects across diverse domains (web app, mobile app, game, desktop, legacy port) with measurable outcomes. Metrics could include:  


- **Time to First Implementable Task:** Measure how long (in hours) after delivery before a developer can start coding on the first task. (Lower is better.)  
- **Number of Clarification Questions:** How many unanswered questions or discoveries arise *after* handoff? (We aim to minimize surprises, so fewer is better.)  
- **Coverage of Requirements:** Fraction of requirements/specs that have corresponding backlog tasks (and vice versa). Ideally near 100%.  
- **Task Executability:** Percentage of tasks that can be executed by an agent or developer without further spec.  
- **Rework/Waste:** Number of tasks or code pieces that had to be re-done because of missing information.  
- **User Confusion/Feedback:** Subjective survey of the developer or team: did the documentation feel complete and clear?  
- **Decision Authority:** Check that no technical tasks were executed that should have required human approval (i.e. the bootstrap did not assume decision autonomy).  


We also define **Failure Injection Tests** to simulate common issues:  
- *Missing Secrets:* Remove a required API key or credential and see if the roadmap or first task flags this immediately.  
- *Ambiguous Requirement:* Provide a vague user story (e.g. “fast login feature”) and see if the skill either asks questions or marks it for refinement.  
- *Conflicting Docs:* Introduce a contradiction (e.g. two PRD items with same ID) and check if it’s detected.  
- *Unmet Dependencies:* Omit mentioning a needed library or service; see if the first task is accidentally unblocked or flagged.  
- *Old Stack:* Set a tech version to end-of-life; test if any “validation” step suggests updating.  
- *Concurrent Changes:* Simulate two agents modifying the same spec; ensure the system would warn of conflict (likely requiring human merge).  
- *Failed Build:* If a CI template is proposed, statically review its configuration; **execution and failure-injection in a real CI environment belong to a later authorized phase**.  


For each pilot, collect data against these metrics to refine the process.  


## 11. Supporting Research and Standards  


This report’s recommendations draw on established sources (all retrievals as of Nov 2026). Key references include agile best practices and SDD guidance:


- **Agile Backlog and Stories:** The INVEST criteria (Agile Alliance) and Definition of Ready (Atlassian) underpin how we decide if work items are actionable. They emphasize *independence, value, estimability, size,* and *testability* for stories. Our rubric aligns with these: tasks lacking clear acceptance (“Testable”) stay in refinement.  
- **Story Mapping:** Jeff Patton’s User Story Mapping technique (explained by TasksBoard) shows how to create a backlog that preserves user journey context. We use this to define the “backbone” activities, walking skeleton, and release cuts.  
- **Vertical/Horizontal Slicing:** Agile educators note that vertical slices (feature-based) deliver end-to-end value, whereas horizontal layers create risk. We recommend vertical slicing and walking skeletons (as defined by Cockburn).  
- **Walking Skeleton & Tracer Bullet:** The DevOps community (StackExchange) describes walking skeleton as a minimal, shippable skeleton linking main components. The “tracer bullets” concept from *The Pragmatic Programmer* (summarized in 2026 blog) advocates building small running slices early. Both support our evidence-first, risk-driven approach.  
- **Definition of Done:** While not exactly the same as our bootstrap, agile guidance on DoD is relevant. For the bootstrap itself, our “acceptance gates” mirror a DoD for the artifact set – ensuring everything needed for the next phase is in place. Atlassian’s DoD emphasizes quality checks and collaboration.  
- **Requirement Standards:** SDD is consistent with ISO/IEC/IEEE 29148’s requirements engineering rules (document, trace, verify). The medium article by Gavrylenko et al. explicitly advises that a “good output” has clear goals, bounded scope, defined users, separate functional vs. quality requirements, exposed assumptions, acceptance criteria, and stable identifiers for traceability – all of which we incorporate above.  
- **Tools and Frameworks:** We considered existing SDD tools (GitHub Spec Kit, OpenSpec, Kiro, Backlog.md). The Backlog.md project (MrLesk) provides a concrete AI-centric process: it explicitly recommends one task per agent and linking plans to tasks. Our agent-session design borrows from this. We also note community resources like ImpactMapping.org for mapping goals to features.  


By distinguishing *facts* (from these sources) from *recommendations* (our design decisions), we ensure our plan is grounded and evidence-backed.


## 12. Risks, Limitations, and Open Decisions  


- **Bootstrap’s Sufficiency:** There is a risk the bootstrap misses something subtle the user expected. Mitigate by human review of relevant artifacts. Additional branches, CI configuration and project-specific exceptions are contextual choices; the new-repository Git baseline and `main`/`dev` are accepted v0.1 defaults unless an exception is authorized.  
- **.git in ZIP / personal GitHub:** D10 already resolves the default delivery options and baseline history: ZIP includes `.git/`; direct publication to the user's personal GitHub account is offered only when an authorized connector can do it. The selected channel, destination, visibility and any missing truthful author/committer metadata are project-specific decisions. Never invent a human identity or silently publish. AI co-author self-attribution is allowed by default but optional, subject to the owner's policy and explicit task overrides.  
- **LICENSE File:** The accepted conventions require a project-specific, human-approved license before writing an actual `LICENSE.md`; the Skill's intended MIT license does not transfer automatically to generated repositories. Record unresolved rights and block distribution where necessary. Do not create a misleading placeholder grant.  
- **Task vs. Feature Definitions:** The exact granularity of tasks (“thin slices” vs “stories”) varies by team. We assume small tasks (one per agent session), but this should be confirmed with the user’s process.  
- **AI/Agent Limitations:** The plan assumes agents can handle tasks given clear prompts. In practice, prompt engineering and model capabilities (e.g. Codex vs. others) might require iteration. The skill should warn that generated plans/code need human review.  
- **Domain Complexity:** Some domains (e.g. safety-critical systems) might need extra verification steps not covered here. If such constraints exist, they should be input during interview and the roadmap augmented (e.g. adding formal verification spikes).  
- **Project Conventions Flexibility:** PROJECT_CONVENTIONS.md v0.1 (D01–D10) is the accepted, adaptable methodology baseline. An existing repository's actual branch names are preserved; a new repository defaults to `main`/`dev`. Any project-specific deviation requires an authorized, recorded decision with rationale and impact, rather than silently treating every convention as undecided.  


**Next Steps:** Finalize any open questions from this research (e.g. syncing with actual user/process), then implement the MVP as outlined. Pilot the workflow on sample projects, refine based on feedback, and update templates and heuristics accordingly.


**Sources:** Agile/backlog practices (INVEST, DoR, DoD), SDD tooling (Spec Kit, Backlog.md), walker/tracer definitions, story mapping, impact mapping, and requirements quality guidance. All cited excerpts and concepts are current as of late 2026.


## Editorial Verification Notes and Primary References (12 November 2026)


The original report provided no standalone bibliographic links. The following are source anchors for the relevant methods, not proof that the proposed SDD skill has been tested:


- [OpenAI — Iterating Development Workflows with Codex](https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex): `AGENTS.md` is optional, useful as a scoped repository instruction file, and should not become a context dump.
- [OpenCode — Instructions](https://opencode.ai/docs/instructions/): repository instruction loading and runtime behavior are tool-specific and should be rechecked when generating adapters.
- [GitHub — GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) and [GitLab — Branching Strategies](https://docs.gitlab.com/user/project/repository/branches/strategies/): branching strategies vary in general practice; this Skill nevertheless adopts `main`/`dev` as its accepted new-repository default, with authorized, documented exceptions.
- [Git — Git Book](https://git-scm.com/book/en/v2): commits include author/committer identity metadata; generated histories must not impersonate humans.
- [NASA — How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) and [ISO/IEC/IEEE 29148:2018 — catalog record](https://www.iso.org/standard/72089.html): rationale for traceable, testable obligations and explicit source/authority, not prescribed Markdown filenames.
- [Jeff Patton — User Story Mapping](https://jpattonassociates.com/user-story-mapping/): practitioner guidance for user-journey slicing; not a guarantee that every first slice must span UI, API and database.
- [GitHub Spec Kit](https://github.com/github/spec-kit) and [OpenSpec](https://github.com/Fission-AI/OpenSpec): examples of current SDD workflow families with different artifact structures.
- [SPDX License List](https://spdx.org/licenses/): a license is an explicit grant under known terms; a stub does not grant unselected rights.


### Illustrative implementation handoff record — methodology baseline approved; project-specific evidence pending


```yaml
handoff_status: draft_not_implementation_ready  # change only after actual gates pass
methodology_baseline: PROJECT_CONVENTIONS_v0.1_D01-D10
delivery_channel: undecided  # git_zip | authorized_personal_github
git_baseline_verified: false
main_and_dev_verified: false
initial_commit_identity_verified: false
agent_coauthor_policy: allowed  # optional, never required; owner may override
new_application_code_generated: false
executable_verified: false
tests_executed: false
deployment_performed: false
package_contents_verified: false
first_unblocked_implementation_task:
  task_id: TBD
  requirement_refs: []
  acceptance_criteria_verified: false
  dependencies_unblocked: false
  status: pending_human_scope_review
preceding_spikes: []  # do not substitute for an implementation task
human_decisions:
  - handoff_channel_and_destination
  - actual_git_author_identity_if_required
  - project_licensing_or_distribution_rights
  - deployment_and_secrets_owners_where_applicable
```


**Correction of the first-session rule:** avoid hard-coding one task per chat, one branch per agent, mandatory authentication, or a CI command absent from the actual repository. The accepted Git baseline is required for a new implementation-ready handoff unless an authorized exception applies. The handoff should state *which* next action is permitted and how its result will later be verified.


**Evidence hierarchy:** method references support why a workflow might be useful; a successful pilot would require actual measurements (clarification burden, first-task feasibility, trace integrity, human review, time and token cost). None of those outcomes are claimed here.