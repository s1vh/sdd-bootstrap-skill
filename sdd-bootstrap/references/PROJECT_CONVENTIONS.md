# Project Conventions

> **Methodology:** SDD Bootstrap Skill — v0.1  
> **Status:** Accepted methodology baseline — 12 November 2026. Each generated project's profile, decisions and exceptions still require appropriate authorization.  
> **Purpose:** Durable, provider-agnostic default operating contract for humans and AI agents collaborating on a generated project repository.  
> **Decision basis:** D01–D09, approved by the methodology's human project initiator on 12 November 2026, plus D10 on delivery options and optional agent self-attribution across the project lifecycle (clarified on 12 November 2026). This is a methodology baseline, not evidence of successful pilot testing.  
> **Licensing boundary:** The SDD Bootstrap Skill is intended for distribution under the MIT License; each generated project's code, documentation and assets have independent licensing decisions.

## 1. Project profile and authority

Complete this profile before treating the generated project as ready for implementation. Use **undecided** rather than inventing answers.

| Field | Project-specific value |
| --- | --- |
| Project name and purpose | `TBD` |
| Project type | `TBD` (web app / game / gamified system / mobile / other) |
| Current scope and non-goals | See [`PRD.md`](PRD.md) |
| Maintainer / human decision authority | `TBD` |
| Language of public README | `TBD` (default: English) |
| Language of GDD, if any | `TBD` (default: English) |
| Stack and toolchain | `TBD` |
| Deployment targets and production branches | `TBD` (none unless justified) |
| Code / asset / documentation licensing | Human-approved project licensing; see root `LICENSE.md` when an actual license is selected. Unresolved rights must be documented, never assumed. |
| Repository handoff channel | `TBD` — downloadable Git ZIP, or direct publication to the user’s personal GitHub account where a suitable authorized connector is available; see §4 |
| Git baseline author/committer | `TBD` — record the actual authenticated or explicitly provided identity; acquire missing name/email only when required for the selected handoff method; see §4 |
| AI agent self-attribution in Git commits | `allowed` by default — optional for each contributing agent, throughout the project; project owner may disable/change it, and explicit per-task/per-commit directions take precedence; see §4 |
| Bootstrap convention revision | `0.1` |

**Normative terms:** **MUST** is obligatory; **MUST NOT** is prohibited; **SHOULD** is the recommended default, with a documented reason for deviation; **MAY** is optional. These rules define the **default contract (D01)**, not an inflexible universal project profile. An authorized human MAY approve a project-specific deviation from an operational convention, with its rationale, scope, impacts and affected artifacts recorded (usually in an ADR or project decision record). Deviations MUST NOT silently remove confidentiality, truthful provenance, least privilege, consent/authorization boundaries, or other applicable legal and safety obligations. When a project/tool constraint conflicts with a convention, document the conflict and seek the responsible human's approval rather than inventing consensus. Humans and agents MAY question, challenge or propose changing these rules; neither an unapproved proposal nor an AI recommendation is an accepted decision.

**Risk-proportionate authority (D03):** Routine, reversible, low-impact drafting and implementation-detail recommendations MAY be delegated within an approved scope. Architecture-locking choices, material specification changes, security/privacy exceptions, distribution/licensing commitments, budget commitments, and irreversible operations require review by the appropriate human authority. Specific approvals elsewhere in this contract (for example, release promotion, gameplay campaigns, secret access or external effects) remain mandatory.

## 2. Sources of truth and document responsibilities

- `/docs/PROJECT_CONVENTIONS.md` defines **how this repository is organized and operated**, not what the product should do.
- `/docs/PRD.md` defines **product intent, the current phase's scope, functional and non-functional requirements, constraints, and acceptance criteria**.
- `/docs/GDD.md`, when present, defines **game design and gameplay intent**. It may describe a broader game than the current PRD phase. An implementation mismatch does not authorize rewriting the GDD.
- `/docs/ARCHITECTURE.md`, scoped design documents, and `/docs/decisions/` define **technical design, alternatives, and architectural decisions**.
- `/docs/specs/` contains **feature/change specifications** when the project requires finer-grained specifications.
- `/docs/BACKLOG.md` tracks **identified, deferred, and in-progress work**; its entries do not authorize implementation by themselves.
- `/docs/UPDATES.md` records **implemented work and evidence**, retaining requirement IDs, source/integration commits, verification and outstanding risks. An update is not automatically a public release; use `CHANGELOG.md` separately if necessary.
- `/docs/TEST_PLAN.md`, when present, defines **verification strategy**, while `/docs/verification/` stores concise records of what was actually verified.
- `/docs/MCP.md`, **only when justified by a genuine requirement**, inventories proposed or selected MCP servers and capabilities, including source/config links, evidence date, protocol/transport compatibility, risk, access requirements, approval state and account/role ownership. Registry discovery is not approval, and an inventory entry is not an instruction to install or connect. Documentation/configuration may live in `/docs/mcp/`; executable local MCP implementations, if later approved for development, belong under `/scripts/` or another documented executable-code location. A project may legitimately have **no MCP integration**.
- Root `README.md` is the **short public cover**: purpose, high-level structure, prominent links, and concise local use/deployment instructions; detailed procedures belong in `/docs/`.
- Root `CONTRIBUTING.md` is the **human-and-agent collaboration entrypoint**; it links to `AGENTS.md` and these conventions, gives branch/PR procedures, and welcomes contributions where appropriate.
- Root `AGENTS.md` is the **compact first-read router for coding agents**, carrying minimum safety/authority rules and links to task-relevant sources. It MUST NOT require unconditional reading of all project documentation.
- Root `LICENSE.md`, **when an actual project license has been approved**, documents applicable licensing boundaries. If selection is pending, record it explicitly in the PRD/decision ledger and do not create a misleading pseudo-license. The assisting model MAY recommend a license with reasons and alternatives, but the project's authorized human chooses. Third-party code, assets, audio, and legacy material MUST retain their own applicable terms; absence of a confirmed license MUST NOT be misrepresented as permission to reuse. The SDD Bootstrap Skill's intended MIT license does **not** automatically apply to any generated project.

When sources conflict or appear stale, the contributor MUST identify the conflict, distinguish accepted decisions from hypotheses, and consult the appropriate decision authority before consequential changes. Historical records MUST remain identifiable as historical.

## 3. Repository layout and growth

The following are **available conventions, not mandatory empty directories**. The v0.1 bootstrap creates only the files needed for an implementation-ready handoff, plus **justified, non-executed** technical templates (D02). Technical configuration, CI and integration examples require a real project reason and MUST NOT masquerade as working application code, successful tests or deployed infrastructure. An explicitly approved project-specific layout exception is recorded under §1; required tool-specific directories may use their actual locations. Future contributors SHOULD use these paths when adding the corresponding concern unless a documented decision or tool constraint requires another location.

```text
/
├── .git/                    # Local Git history in ZIP mode; Git history lives in the remote repository for GitHub mode
├── .gitignore               # Stack-aware exclusions, including .secrets/
├── .gitattributes
├── .editorconfig
├── README.md
├── CONTRIBUTING.md
├── LICENSE.md               # When an actual project license is approved
├── AGENTS.md
├── docs/
│   ├── PROJECT_CONVENTIONS.md
│   ├── PRD.md
│   ├── BACKLOG.md
│   ├── UPDATES.md
│   ├── ARCHITECTURE.md    # If applicable
│   ├── TEST_PLAN.md       # If applicable
│   ├── GDD.md             # If applicable
│   ├── MCP.md             # If applicable
│   ├── specs/             # Feature/change contracts, if applicable
│   ├── decisions/         # ADRs, if applicable
│   ├── verification/      # Evidence records, if applicable
│   └── mcp/               # MCP inventory attachments, if applicable
├── .agents/
│   ├── roles/             # Role/task guidance, if needed
│   ├── context/           # Compact, recoverable agent context
│   └── handoffs/          # Completed/paused-task handoffs
├── src/                   # Application source, only when implementation begins
├── tests/                 # Tests/fixtures when actually needed
├── scripts/               # Auxiliary executable code, if later needed
├── builds/                # Selected packaged deliverables, if relevant
└── .secrets/              # Local only; ignored by Git; not shipped in ZIP
```

**Same-change rule:** adding, moving, renaming, or removing a directory, a documentation authority, a build target, or an operational workflow MUST update these conventions and all affected indices/instructions in the **same change**. A change is not complete while the documented structure differs from the repository. Tool-required directories (such as Unity, Visual Studio, CI, or agent-specific adapters) are legitimate when explicitly registered.

## 4. Git initialization, delivery channel, and branches

1. **User-selected delivery channel (D10):** At bootstrap handoff, **offer a downloadable ZIP** containing the initialized Git repository. When the runtime exposes an authorized, working GitHub connector capable of creating a repository in the **authenticated user's personal account**, additionally offer **direct creation/publication to that personal GitHub account**. The user chooses the channel; if multiple usable personal GitHub accounts are connected, let the user select the account. **Organization repositories are out of scope for the initial v0.1 publishing flow**; users may transfer/reconfigure ownership later through GitHub's own processes. Do not infer that a GitHub connector's mere presence guarantees permissions, a verified identity, or actual publication. If remote creation is unsupported, unavailable, or declined, retain the ZIP path. An explicit, informed user action MUST authorize repository creation/publication, target account, name and public/private visibility **before** any remote mutation. In the absence of authorization, do not create or push any remote repository. No organization access should be requested merely to bootstrap a new personal project.
2. **Baseline Git history in either channel (D01, D02, D10):** The initial project baseline MUST be committed in an initialized Git repository with a suitable `.gitignore`, `main` and `dev` based on that baseline (`dev` as the initial development branch), unless an authorized, documented project exception applies. **ZIP mode:** deliver and verify the initialized local repository, including `.git/`, baseline commit and branches after extraction. **GitHub mode:** create/verify the repository and baseline history/branches under the selected personal account; a downloadable ZIP or local `.git/` archive is optional rather than required. Record the actual repository URL and initial commit when available; never claim publication without tool confirmation. The GitHub publication is a bootstrap **delivery action**, not application deployment or approval to release unimplemented product features.
3. **Initial-commit author identity and ZIP fallback (D10):** In **direct GitHub mode**, use the authenticated user's GitHub account as the repository owner and the identity that the actual connector/API can truthfully attribute to the initial commit; do not request the user's Git name/email merely because a local ZIP would need it. If the tool requires author metadata not exposed by the connection, request **only the missing details** instead of inventing them; don't silently change the owner or impersonate the user. In **ZIP mode**, obtain the real initial-commit author name and email from the eligible connected identity if available and appropriate; otherwise ask the user for whichever identity fields are missing before creating that commit. When multiple eligible identities are available, ask which one to use; explicit user preferences override defaults. A login name alone is not proof of a valid commit email. Never fabricate another human's name, email or consent. Separate repository ownership, Git commit author/committer fields, and co-author attribution; they are not interchangeable.
4. **Project-wide optional AI self-attribution (D10):** At bootstrap, offer the human project owner a configurable convention: **AI agents are permitted to identify themselves as co-authors of commits they materially contribute to**, or **AI agents must not self-identify as commit co-authors**. The default, absent a contrary user request, is **permitted**, not **required**. This policy applies to **the initial bootstrap commit and all subsequent implementation, testing, DevOps, deployment-preparation and maintenance commits**. Each contributing agent independently MAY choose whether to self-attribute, using an honest self-chosen name/alias and suitable co-author metadata; it MUST NOT claim to be a different human/agent, a verified account, or an endorsed vendor identity without evidence. When supported, a valid `Co-authored-by: Agent Name <agent-email>` trailer MAY be used; if no truthful, technically valid co-author identity is available, use optional plain-text provenance or a task handoff instead. This does **not** authorize inventing the user's author/committer identity, nor does permission to self-attribute authorize adding an agent that did not contribute. **Precedence:** an explicit authorized direction for the particular task/commit overrides the current project convention; otherwise follow the current project convention; otherwise use the default `allowed`. The human project owner MAY change the convention later using normal documented project change control. Changes apply prospectively unless the owner explicitly authorizes a history change; existing commit history is not silently rewritten. See item 10 for later contributors.
5. Existing repositories MAY use another primary branch name (for example, `master`); record the **actual** name and do not rename it implicitly. Publishing an existing project or rewriting its history requires its own explicit authorization.
6. `dev` is the active integration branch and SHOULD remain coherent and buildable. Normal changes start on focused branches from up-to-date `dev`.
7. Recommended provider-neutral prefixes: `feat/`, `fix/`, `docs/`, `refactor/`, `test/`, `chore/`. Provider-specific names such as `codex/feature/` MAY be retained when valuable for provenance; they are not required by this methodology.
8. Every topic branch MUST have a bounded task, approved scope, and appropriate acceptance criteria. Finishing or pushing a topic branch does **not** authorize integration or release by itself.
9. **Default integration:** after suitable non-gameplay checks and required approval, squash-merge into `dev` **and preserve the source branch/reference**. The integration message MUST identify the source branch, exact source commit, relevant requirement/task IDs, and material human/agent contributions. Source branches SHOULD become read-only historical references after integration; subsequent changes start from current `dev`, not the stale branch. A normal merge is allowed when preserving ancestry directly is more useful.
10. **Attribution across agents and commits:** The optional self-attribution policy in item 4 follows the **contributing agent and the specific commit**, not the identity of the bootstrap agent. A DevOps agent, implementation agent, test agent or other collaborator MAY independently add its **own** truthful co-author trailer when permitted by the effective project policy and any more specific human instruction; no agent is required to add one merely because self-attribution is allowed. Agents MUST NOT add unrelated agents as co-authors, impersonate a human/agent, or falsely claim verified GitHub accounts or model versions. Handoffs and task records MAY document contributors independently of Git co-author trailers, subject to project authorization and privacy rules. The project-wide convention and any relevant per-commit override SHOULD be discoverable from this file and the task or decision record.
11. `main` (or its recorded equivalent) denotes the human-approved stable/release state. **Promotion from `dev` requires explicit human authorization.** Tests passing do not imply release approval.
12. Production branches (`prod`, `prod-firebase`, `prod-android`, etc.) are **optional** and justified only by genuinely different deployment trees or operational contracts. Ordinary multi-target builds SHOULD share the same validated source commit and use target-specific pipelines instead. Production-only configuration differences and drift controls MUST be documented.
13. Frozen historical milestones SHOULD use annotated tags or protected releases. If a historical branch is required, it MUST be marked documentary and never routinely updated. No automatic deletion, force rewrite, or destructive cleanup of historical references is allowed without human approval.
14. An urgent change applied outside `dev` MUST have an explicit reconciliation/backport plan. No agent MAY silently perform a push, merge, publication, or deployment that the project's authority rules reserve for a human decision.

## 5. Verification and release policy

**General principle:** verification is based on affected requirements, risk, and reproducible evidence—not on rerunning every suite after every commit. Incomplete work SHOULD NOT be subjected to costly acceptance batteries; unchanged, still-applicable evidence MAY be reused, with its commit, scope, dependencies, environment, and invalidation conditions recorded. A passed test never substitutes for missing human acceptance. This proportionality does **not** waive the explicit gameplay-test and release-promotion approval gates below (D03).

### 5.1 Normal application work

Before a feature/fix enters `dev`, contributors SHOULD perform the relevant inexpensive checks (for example type checking, linting, focused unit/contract tests, and an applicable build). Before production publication, validate the integrated release and target-specific configuration according to the test plan. Security- or data-critical changes may require additional independent checks.

### 5.2 Games and gamified systems — mandatory gameplay exception

**Gameplay tests MUST run ONLY on an identified, coherent, stable checkpoint of `dev`, and ONLY after explicit authorization from the human-in-the-loop for that test campaign.** This applies to human playtesting campaigns and costly automated gameplay-oriented test suites (for example full-run simulations, extensive physics traversal campaigns, balancing, playability, or game-feel evaluations).

- **DO NOT** launch such gameplay tests after each feature or on unfinished topic branches, even when a feature appears locally complete.
- Several completed features MAY accumulate in `dev` before the human authorizes a combined gameplay campaign. First establish a reproducible stable `dev` commit and document the intended scope.
- Normal narrow non-gameplay checks of isolated components, static analysis, and builds MAY be run at the appropriate feature gate. If uncertain whether a proposed suite constitutes gameplay testing, treat it as gameplay testing and request authorization.
- Automated checks MUST NOT be described as proving subjective playability or human acceptance. Human testers, including professional testers where available, provide independent gameplay assessment.
- **If the human requests `dev` → `main` without the gameplay campaign**, the agent MUST **warn before merging** that gameplay behavior has not been fully validated and that release regressions may remain. The agent MUST offer the option to run testing first, but MAY proceed once the human explicitly accepts the risk and authorizes that promotion. Human-performed manual tests MAY be recorded as such; do not imply that skipped automated gameplay tests passed.
- Any accepted exception MUST be recorded in `/docs/verification/` or `/docs/UPDATES.md`: source commit, evidence actually available, omitted gameplay checks, stated risks, human decision, and release identifier. Urgency does not silently convert a waiver into verification.

### 5.3 Evidence and reconciliation

Use statuses with distinct meanings: `implemented`, `automated-verified`, `human-reviewed`, `accepted`, `deferred`, and `waived-with-risk`. Records SHOULD link requirements to code changes, checks, and observed outcomes. When implementation, tests, and specifications disagree, investigate which layer is wrong; do not silently rewrite the intended product to make a check pass.

## 6. Secrets and data access

- Secrets and sensitive local credentials belong in `/.secrets/` (or an explicitly approved external secret manager), with environment-specific configuration as necessary. `/.secrets/`, `.env` credentials, and similar sensitive artifacts MUST be excluded by `.gitignore` and from distributable ZIPs.
- **`AGENTS.md` MUST expressly tell agents not to open, index, inspect, transmit, or copy `/.secrets/` without an explicit, authorized, narrowly scoped human request.** `.gitignore` is not an access-control mechanism; use tool permissions and sandbox restrictions when supported.
- The human-in-the-loop controls the real secrets and the decision to grant access. Checked-in examples MUST contain placeholders rather than live credentials.
- If secrets are encountered unintentionally, stop the sensitive operation, avoid echoing the values, notify the authorized human, and follow the project's containment/rotation procedure. Do not invent self-erasure or other destructive responses.
- MCP and agent tools SHOULD follow least privilege. An entry in the MCP inventory does not automatically grant permission or require loading the server into a session. Explicit approval for a proposed provider or contract (D07) authorizes **documentation of the integration**, not installation, connection, live invocation, account creation or transmission of real data.
- **Public research (D06):** The Skill MAY consult relevant **public** technical documentation and official sources by default when its current environment provides lawful, authorized access. It SHOULD prioritize source authority and record source/version/review dates for material volatile claims. It MUST NOT transmit confidential project data, credentials, or other nonpublic information to a search service, MCP server or external provider without separate authorization. Connected private sources remain subject to their actual permissions and user intent; a missing tool or network connection is recorded as unverified, not faked. No continuous background monitoring is implied.

## 7. Agent context, handoffs, and selective loading

- `AGENTS.md` MUST be small enough to function as a **router**, not an encyclopedia. At session start load only mandatory safety/authority rules and the files necessary for the assigned task; expand on demand.
- `/docs/` contains enduring, shared project knowledge. `/.agents/context/` holds **small recoverable summaries** of agent-specific responsibilities, non-obvious findings, relevant references, and unresolved questions; `/.agents/handoffs/` records pause/completion and resumption instructions. Neither directory should duplicate PRD, architecture, source code, or full chat logs.
- A resumable handoff SHOULD include: task/role ID, date, status, related requirements/decisions, source/integration commit IDs, changed areas, checks and limitations, open questions, next action, and what would invalidate its conclusions.
- Provider-native sessions MAY be resumed where supported, but interoperability MUST rely on provider-neutral persistent artifacts. A reconstructed session is a **continuation of documented work**, not a guaranteed revival of the identical model instance or hidden state.
- Context records MUST avoid secrets and sensitive user data and MUST distinguish historical observations from current instructions. Stale context is archived or marked superseded rather than presented as authoritative.
- Agents MUST NOT load every MCP, historical handoff, or project document by default. Context selection is based on task relevance, dependencies, authority, and permissions.
- **Knowledge freshness (D05):** Source checks SHOULD be triggered by material risk, newly discovered changes, and upcoming high-impact decisions rather than a fixed global calendar. Source claims SHOULD record source, date, version/status and uncertainty when relevant. Newer does not necessarily mean compatible, safer or approved; changes are **proposed for review**, not automatically applied. Unsupported, unverifiable or offline claims MUST be labelled accordingly. Local docs and targeted on-demand checks are the v0.1 baseline; a vector database, RAG infrastructure or continuous surveillance is not required.
- **Provider portability:** Preserve capability intent and decisions in provider-neutral artifacts. Any client-specific adapter, prompt or MCP configuration is optional and MUST be justified by the selected target environment. Agents MAY challenge assumptions constructively; this contract does not impose personality, identity or creative style.

## 8. Reproducible scripts and build artifacts

- Auxiliary code intended to be **executed even once** (local servers, PDF/document processing, migrations, conversions, diagnostics, administration helpers, etc.) MUST be created under `/scripts/` or a clearly documented tool-mandated executable location, committed when appropriate, and made traceable. Application source stays under `/src/` and test source under `/tests/`.
- Scripts SHOULD describe purpose, usage, inputs/outputs, dependencies, side effects, and safe execution conditions. Avoid unreviewed destructive defaults; record any necessary exception.
- The bootstrap MAY create **non-secret, non-executed** placeholders or examples for justified future work (for example `.env.example`, CI policy sketch or proposed API/MCP contract). It MUST NOT silently implement features, run the application, provision infrastructure, purchase services, install/connect MCP servers, or perform deployment. A placeholder or config template is not operational evidence (D02, D07).
- Ephemeral generated outputs MAY be ignored. Select packaged release artifacts MAY live under `/builds/` when redistribution or inspection requires them; otherwise prefer build pipelines and versioned release artifacts. Override stack template ignore rules deliberately when tracked builds are intended.

## 9. Change control, licensing, and completion

- The default documentation language is **English**. `README.md` and, for games, `GDD.md` MAY use a human-selected language. Translation must not silently change normative meaning.
- **Skill vs. project licensing (D08):** The SDD Bootstrap Skill itself is intended for release under the MIT License (subject to rights in its own materials). Generated repositories do **not** inherit that license. License selection for each project is an explicit decision by its authorized human owner; the assisting model SHOULD offer reasoned alternatives tailored to the project's characteristics, constraints and third-party materials. The project MAY use different licenses for software, original art, third-party media, and legacy work. Unresolved licensing MUST be stated rather than assigned automatically. No placeholder `LICENSE.md` may claim permissions that have not been granted. **AI self-attribution is optional project workflow metadata, not an MIT-license condition or a requirement to use, modify or fork the Skill.**
- Any material specification/architecture change MUST update the relevant controlling document, decision record, task status, and verification expectations. Structural changes MUST also update this file in the same change.
- Before declaring a task complete, check: scope/authorization; required non-gameplay validation; documentation consistency; provenance/attribution; secret exclusion; known risks; and whether human acceptance is still pending.
- **Deployment-aware but non-deploying (D02–D04):** The bootstrap SHOULD capture target distribution/execution environments, data boundaries, operational ownership, prerequisite accounts/costs, recovery and release questions to the depth needed for the **first unblocked implementation task**. Exact providers, numbers of environments, CI/IaC templates, budgets and runtime services are project-specific decisions, not v0.1 universals. Human sign-off is necessary for spending and production release. No undocumented deployment or readiness claim is permitted.
- **Roadmap and handoff (D04):** Distinguish proposed decisions, approved decisions, tasks, planned verification, executed verification and human acceptance. One specific, feasible, adequately specified and **unblocked implementation task** must be identifiable in the initial handoff; a spike or pure research task may precede it but does not, by itself, satisfy the implementation-readiness gate. Do not force one agent per chat, one task per conversation, or a particular CI implementation unless this project's authority rules justify it; focused branches remain governed by §4.
- Project conventions themselves are revisable: propose a reasoned change, record its decision authority and impact, and update dependent documents. Their purpose is **reliable collaboration without suppressing engineering judgment**.

## 10. Bootstrap acceptance checklist

The generated ZIP may be labelled **implementation-ready** only when all applicable conditions below are met (D04). A draft may be saved earlier, but MUST be clearly marked **incomplete / not implementation-ready**, not presented as a completed bootstrap:

- [ ] Project profile and unresolved decisions are explicit; no invented approvals.
- [ ] PRD has sufficient agreed scope and falsifiable acceptance criteria for the intended starting phase.
- [ ] The user selected a handoff channel and its account/destination where applicable; **ZIP:** `.git/`, baseline commit, primary branch and `dev` are verified after archive extraction. **GitHub:** the authorized personal repository, initial commit and expected branches are verified remotely. Authorized exceptions are documented; baseline author identity and the project-wide **optional** agent self-attribution convention follow §4.
- [ ] The stack-specific `.gitignore` excludes secrets and disposable outputs without silently excluding deliverables.
- [ ] Root entrypoints link to these conventions, and documentation paths are internally consistent.
- [ ] Optional files/directories and non-executed templates reflect actual needs instead of a blanket scaffold, and do not imply finished application code.
- [ ] Game/gamification gameplay-test authorization and stable-`dev` rules are present when relevant.
- [ ] Agent context boundaries, handoff conventions, and permitted tools are explicit.
- [ ] Scripts are traceable, actual project licenses are approved or explicitly unresolved, and deployment claims are not fabricated.
- [ ] **At least one implementation task is genuinely unblocked**, sufficiently specified, feasible, and linked to approved scope and verifiable acceptance criteria. A research spike alone is insufficient.
- [ ] Material uncertainties have owners and gates, and no unresolved issue invalidates the starter task; no unapproved external action, secret disclosure, or paid commitment occurred. If GitHub delivery was chosen, repository visibility and destination were explicitly authorized and the actual result was verified.

## 11. Methodology decisions and validation status

The following **methodology-level** decisions were accepted by the project initiator on **12 November 2026**. **D10** records the subsequently approved clarification of bootstrap handoff and **optional agent self-attribution for any contributed commit**, with project-level and per-commit controls. They do not pre-approve specific repository creation, publishing actions, account permissions, or choices within an individual generated project.

| ID | Accepted v0.1 policy | Application |
|---|---|---|
| D01 | Default but adaptable conventions contract | §1, §3, §4; justified project exceptions need human approval and traceability |
| D02 | Justified technical templates only | §3 and §8; no speculative code scaffold or automatic deployment |
| D03 | Risk- and impact-proportionate human approval | §1, §5, §6, §9; explicit sensitive-operation gates remain |
| D04 | Do not complete bootstrap without an unblocked implementation task | §9 and §10; research-ready alone is not implementation-ready |
| D05 | Freshness checks driven by risk, events and upcoming decisions | §7; no universal fixed interval or automatic updating |
| D06 | Relevant public research allowed by default | §6; never expose private information without authorization |
| D07 | Integration/MCP templates when justified and authorized | §2, §6, §8; no automatic installations or connections |
| D08 | MIT License for the Skill; project license chosen by owner | §2 and §9; recommendations allowed, no license inheritance |
| D09 | Select pilot projects after building initial v0.1 | Evaluate across different project types; none pre-selected by this contract |
| D10 | Offer ZIP or authorized personal-GitHub bootstrap delivery; default to **allowing (never requiring)** each contributing AI agent to self-attribute on **any commit**; support project-wide opt-out/revision and explicit per-commit overrides | §1, §3, §4, §10; truthful authorship, no automatic remote publication or forced organization setup |

**Validation distinction:** These are **approved methodology decisions**, not proof that the Skill works across providers or project classes. Pilot outcomes, defects, changes and lessons SHOULD later be tracked separately without retrospectively inventing acceptance or execution evidence. The original research reports are evidence and design inputs, not automatic normative rules.

*This document is a default collaboration contract, not a substitute for project-specific engineering judgment, authorized human decisions, or independent verification.*
