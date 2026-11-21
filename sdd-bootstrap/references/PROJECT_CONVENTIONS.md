# Project Conventions

> **Methodology:** SDD Bootstrap Skill — experimental v0.2 candidate  
> **Status:** Experimental pilot revision — 21 November 2026. It builds on the accepted 12 November 2026 v0.1 baseline; it is **not** an approved stable release until reviewed and promoted to `main`. Each generated project still needs authorized project-specific decisions.  
> **Purpose:** Durable, provider-agnostic default operating contract for humans and AI agents collaborating on a generated project repository.  
> **Decision basis:** Inherited v0.1 D01–D10 plus pilot-driven candidate refinements D11–D14 (21 November 2026). The refinements encode observed Portfoling feedback but are not evidence of successful regression or cross-provider testing.  
> **Licensing boundary:** The SDD Bootstrap Skill is intended for distribution under the MIT License; each generated project's code, documentation and assets have independent licensing decisions.

## 1. Project profile and authority

Complete this profile before treating the generated project as ready for implementation. Use **undecided** rather than inventing answers.

| Field | Project-specific value |
| --- | --- |
| Project name and purpose | `TBD` |
| Project type | `TBD` (web app / game / gamified system / mobile / other) |
| Current scope and non-goals | See the generated project's `docs/PRD.md` (created during bootstrap; not part of the Skill reference library) |
| Maintainer / human decision authority | `TBD` |
| Language of public README | `TBD` (default: English) |
| Language of GDD, if any | `TBD` (default: English) |
| Stack and toolchain | `TBD` |
| Deployment targets and production branches | `TBD` (none unless justified) |
| Code / asset / documentation licensing | Human-approved project licensing; see root `LICENSE.md` when an actual license is selected. Unresolved rights must be documented, never assumed. |
| Repository handoff channel | **Project-files ZIP without `.git/` by default**; optional initialized Git ZIP or authorized remote repository publication; see §4 |
| Git baseline author/committer | `Not applicable` unless Git initialization is requested; then use verified/provided values and request missing fields, never invent them; see §4 |
| AI agent self-attribution in Git commits | `allowed` by default — optional for each real contributor; never infer model/platform, use truthful name/role/agent ID and valid attribution policy; see §4 |
| Initial pilot / current phase and essential journeys | `TBD` or `Not applicable` — record actual success conditions and critical paths in PRD; see §5/§9 |
| Hard cost/billing constraints | `TBD` — distinguish zero expected costs, hard zero-charge exposure, no card, and commercial use eligibility |
| Future launch preferences | `TBD` / `Not applicable` — weigh provider continuity and migration effort without overruling current-phase feasibility |
| Bootstrap convention revision | `0.2-experimental` |

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

The following are **available conventions, not mandatory empty directories**. This experimental bootstrap creates only the files needed for an implementation-ready handoff, plus **justified, non-executed** technical templates (D02). Technical configuration, CI and integration examples require a real project reason and MUST NOT masquerade as working application code, successful tests or deployed infrastructure. An explicitly approved project-specific layout exception is recorded under §1; required tool-specific directories may use their actual locations. Future contributors SHOULD use these paths when adding the corresponding concern unless a documented decision or tool constraint requires another location.

```text
/
├── .git/                    # OPTIONAL: absent in default bootstrap; created only when authorized
├── .gitignore               # ALWAYS included; stack-aware exclusions of .secrets/, secrets/, caches, credentials
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
└── .secrets/              # Local only; ignored by Git; not shipped in ZIP (also protect /secrets/)
```

**Same-change rule:** adding, moving, renaming, or removing a directory, a documentation authority, a build target, or an operational workflow MUST update these conventions and all affected indices/instructions in the **same change**. A change is not complete while the documented structure differs from the repository. Tool-required directories (such as Unity, Visual Studio, CI, or agent-specific adapters) are legitimate when explicitly registered.

## 4. Optional Git initialization, authentic provenance, and development-branch lifecycle

### 4.1 Git delivery and first-initialization safety (D01, D02, D10, D11)

1. **Default:** deliver a verified **project-files ZIP with no `.git/` directory**. The user MAY explicitly request an initialized local Git ZIP or authenticated remote publication instead. There is **no incomplete-bootstrap penalty** for choosing the default. Do not silently create a repository, an initial commit, or remote branches.
2. **Always** include a suitable `.gitignore` in the generated project, even when Git is not initialized. Protect `/.secrets/`, `/secrets/`, `.env` credentials and other sensitive paths; include only justified stack-specific exclusions (for example Unity's generated `Library/` and `Temp/`), preserving intended deliverables and approved packaged builds. `.gitignore` is NOT an access control or proof of secrecy; see §6.
3. **Optional Git mode:** with explicit user approval, initialize a truthful repository and baseline commit, then `main` (or recorded project primary) and `dev` in the agreed topology. For ZIP mode, include and verify the initialized `.git/` archive and real author/committer metadata. For GitHub mode, verify actual account, ownership, visibility, permissions, initial commit and branches. Authorization for Git initialization is **not** authorization for remote publication. Never fabricate author metadata to avoid asking the user.
4. **Remote publication:** offer creation in an authenticated user's selected personal GitHub account only if a capable connector is actually available, and obtain explicit approval of account, repository name, and visibility **before** mutation. Organization publication is not the v0.1 default. Unsupported/declined remote mode falls back to the no-Git project-files ZIP or an explicitly requested initialized ZIP.
5. **First-Git transition guard:** when an agent first observes Git after a handoff documented as not initialized, compare the existing `.gitignore` against the bootstrap's intended protection. Check that sensitive and stack-specific paths are still ignored (e.g. using `git check-ignore -v` and `git status --ignored`), and that no excluded sensitive files were accidentally added/tracked. Reconcile before the initial commit if possible; if an exposure already exists, report the incident separately rather than assuming an ignore-file fix erases Git history. Record that check once in `UPDATES.md` or the normal handoff. Repeat only after material ignore changes or a discovered concern. If reliable before-state cannot be established, do a targeted current-state check without claiming a verified transition.
6. **Future branch contract exists before Git:** generated `docs/PROJECT_CONVENTIONS.md` and the root `AGENTS.md` routing instructions MUST explain how a future agent creates the initial commit and `dev` then task branches. Never claim branches exist when they have only been documented. A newly initialized empty repository has an unborn branch until the first commit; it cannot provide normal branch ancestry before that baseline.

### 4.2 Accurate human/agent authorship and coauthor trailers (D10, D12)

7. **Separate roles:** repository owner, human accountable decision-maker, authenticated pusher, Git author, Git committer, and message co-author are **distinct**. A push from the human's account alone does not prove that the human is the recorded commit author. Use truthful metadata, and ask only for identity information required for the chosen operation.
8. **Agent identity:** any material contributor MAY self-identify as a co-author unless project policy or a specific instruction prohibits it. This is **allowed but not required**. Assign a **stable and unique project-agent identity** (personal name, role, opaque ID or a distinguishable combination). Two different agents MUST NOT use an indistinguishable full identity; model version changes by themselves neither prove nor disprove continuity. A recoverable agent profile/registry is optional, based on actual project coordination complexity, not mandatory for small projects.
9. **No inherited technical identity:** a new or rehydrated agent MUST NOT infer its **current model, revision, serial/build number, platform or account** from previous commits, earlier agents, style, vendor family, branch names, or probabilities. Exact model may appear as `(Model)` and independently confirmed execution host as `@ Platform` (include a space after `@`), each ONLY when reliably provided or declared by the user. Unknown fields are **omitted**. If a missing detail materially affects provenance, ask the user; otherwise do not interrupt. Distinguish user-declared metadata from independent attestation.
10. **Email decision:** (a) use an agent-controlled, genuinely operable mailbox when legitimately available and authorized; (b) a mailbox accessible through a connector is not an agent-owned mailbox and must not be reused as an agent's Git identity without appropriate permission—**the human owner's email requires the owner's explicit request**; (c) a verified platform/bot attribution email may be used only when it truthfully corresponds to that platform's real participation, not merely a provider family/model (e.g. do not misrepresent non-Codex GPT work as Codex); (d) otherwise a clearly **non-deliverable reserved placeholder** (e.g. `agent-017@agents.invalid`) may be used for **textual** co-author trailers. Placeholder mail is neither a contact channel nor guaranteed GitHub account linkage. A generic `noreply` address is not proof of an associated account. Prefer project-agent rather than generic platform attribution.
11. **Commit message structure:** readable subject and body summarize actual changes and, as applicable, source branch and real tip SHA, requirement/backlog IDs, meaningful verification. After **one blank line**, write one `Co-authored-by: Agent Name [(known exact model)] [@ known platform] <address>` trailer per **material contributor to that particular commit**, on consecutive lines, ordered by significance of contribution rather than chronology. Use canonical `Co-authored-by:` spelling for GitHub compatibility. No copied unrelated coauthors, guessed versions or duplicate identities. An illustrative valid trailer: `Co-authored-by: agent-017 <agent-017@agents.invalid>`.
12. **Handoff:** context may rehydrate assigned project work but not prove identical hidden runtime or previous model identity. Keep project-agent identity separate from per-session model/platform evidence. Preserve actual commit provenance in existing `UPDATES.md` and optional handoffs; create a separate agent register only when the scale or cross-session needs justify it.

### 4.3 Autonomous topic→`dev` integration; human-owned `main` releases (D03, D13)

13. **Branches:** `dev` is granular development integration, **not** a guaranteed regression-free/release-ready state. `main` (or the documented stable primary branch) is a **human-approved stable build/release reference**. Topic branches start from current `dev` for bounded, approved tasks; names SHOULD include known spec/backlog IDs (e.g. `feat/REQ-017-title`, `fix/TASK-042-title`), or use a readable description when no ID exists. Never invent an ID merely to name a branch.
14. **Autonomous ordinary local work:** the project-approved operating contract and assigned task scope delegate topic branch creation, commits, relevant cheap checks, **completed no-squash topic→`dev` merge commits**, and safe subsequent local cleanup to agents **without per-merge human confirmation**. Prefer `git merge --no-ff` to retain original commits, SHAs, authorship, coauthor trailers, and explicit merge parentage. Integration messages identify the original branch name, actual source tip commit, task/spec IDs and material integration contributors. Credit earlier source-commit contributors on their original commits; do not blindly duplicate their trailers on the merge commit.
15. **Hold and clean up branches:** keep a branch open while incomplete, awaiting a material decision, required check, or exceptional dependency. After integration, inspect the merged tree and ancestry (e.g., `git merge-base --is-ancestor source-tip dev`), record relevant checks, then delete the **fully merged local** source branch with safe operations (`git branch -d`), not unconditional force deletion. Preserve original history reachable from `dev`; a deleted branch name can remain discoverable in the merge body and `UPDATES.md`. Protected, unique/unmerged, shared-worktree, still-needed PR or historical branches require an exception and must not be blindly removed. **Remote push/delete is separate authority** and requires actual permission/authorization and post-publication verification.
16. **`main` release gate:** the human ordinarily performs `dev`→`main` manually. Agents may propose promotion and explain the steps, but MUST NOT promote without **specific authorization** to do so. A request to deploy can authorize a **scoped release workflow** only after validating that intent and destination; it does not grant a silent blanket permission for other releases, targets or spending. Never deploy from `dev` or a topic branch: deploy only from approved stable `main` or a justified, authorized `prod*` release path. Routine agent access to `dev` does not authorize `main`, publication, spending or deployment.
17. **History rewrite and special refs:** rebasing/history rewriting requires a **specific human authorization**, especially for shared or published work. No force rewrite, destructive cleanup, deletion of unique commits, or historical tag/branch replacement is implicit in normal topic integration. Urgent changes outside `dev` need an explicit reconciliation plan. Optional `prod*` branches are allowed where genuinely different deployment trees or operational contracts require them; multiple build targets alone do not justify redundant branches.

## 5. Verification and release policy

**General principle:** verification is based on affected requirements, risk, and reproducible evidence—not on rerunning every suite after every commit. Incomplete work SHOULD NOT be subjected to costly acceptance batteries; unchanged, still-applicable evidence MAY be reused, with its commit, scope, dependencies, environment, and invalidation conditions recorded. A passed test never substitutes for missing human acceptance. This proportionality does **not** waive the explicit gameplay-test and release-promotion approval gates below (D03).

### 5.1 Normal application work

Before normal topic→`dev` integration, agents SHOULD **autonomously** perform the smallest relevant inexpensive checks (for example type checking, linting, focused unit/contract tests, or quick applicable build checks). The human does not need to approve each cheap check or routine within-scope merge. Do **not** launch expensive, comprehensive, long-duration, resource-intensive, or gameplay-oriented suites as a routine feature gate. If indispensable costly verification is needed before safe integration, **retain the topic branch** and seek authorization; if it is only needed later for release, defer with a clear risk/evidence note. `dev` is integration-oriented, not a promise of zero regression. At an authorized `main` release/deployment checkpoint, run **critical relevant release checks** without requiring redundant per-check consent, subject to separately gated campaigns and sensitive external operations. Test execution does not by itself authorize `dev`→`main`, paid services or deployment.

### 5.2 Games and gamified systems — mandatory gameplay exception

**Gameplay tests MUST run ONLY on an identified, coherent, stable checkpoint of `dev`, and ONLY after explicit authorization from the human-in-the-loop for that test campaign.** A rare candidate that cannot merge safely without a costly gameplay assessment is **blocked**, not silently exempt; a specifically approved exceptional candidate-test protocol would require a separate explicit methodology/project decision. This applies to human playtesting campaigns and costly automated gameplay-oriented test suites (for example full-run simulations, extensive physics traversal campaigns, balancing, playability, or game-feel evaluations).

- **DO NOT** launch such gameplay tests after each feature or on unfinished topic branches, even when a feature appears locally complete.
- Several completed features MAY accumulate in `dev` before the human authorizes a combined gameplay campaign. First establish a reproducible stable `dev` commit and document the intended scope.
- Normal narrow non-gameplay checks of isolated components, static analysis, and builds MAY be run at the appropriate feature gate. If uncertain whether a proposed suite constitutes gameplay testing, treat it as gameplay testing and request authorization.
- Automated checks MUST NOT be described as proving subjective playability or human acceptance. Human testers, including professional testers where available, provide independent gameplay assessment.
- **If the human requests `dev` → `main` without the gameplay campaign**, the agent MUST **warn before merging** that gameplay behavior has not been fully validated and that release regressions may remain. The agent MUST offer the option to run testing first, but MAY proceed once the human explicitly accepts the risk and authorizes that promotion. Human-performed manual tests MAY be recorded as such; do not imply that skipped automated gameplay tests passed.
- Any accepted exception MUST be recorded in `/docs/verification/` or `/docs/UPDATES.md`: source commit, evidence actually available, omitted gameplay checks, stated risks, human decision, and release identifier. Urgency does not silently convert a waiver into verification.

### 5.3 Evidence and reconciliation

Use statuses with distinct meanings: `implemented`, `automated-verified`, `human-reviewed`, `accepted`, `deferred`, and `waived-with-risk`. Records SHOULD link requirements to code changes, checks, and observed outcomes. When implementation, tests, and specifications disagree, investigate which layer is wrong; do not silently rewrite the intended product to make a check pass.

## 6. Secrets and data access

- Secrets and sensitive local credentials belong in `/.secrets/` or `/secrets/` (or an explicitly approved external secret manager), with environment-specific configuration as necessary. `/.secrets/`, `/secrets/`, `.env` credentials, and similar sensitive artifacts MUST be excluded by `.gitignore` and from distributable ZIPs.
- **`AGENTS.md` MUST expressly tell agents not to open, index, inspect, transmit, or copy `/.secrets/` or `/secrets/` without an explicit, authorized, narrowly scoped human request.** `.gitignore` is not an access-control mechanism; use tool permissions and sandbox restrictions when supported.
- The human-in-the-loop controls the real secrets and the decision to grant access. Checked-in examples MUST contain placeholders rather than live credentials.
- If secrets are encountered unintentionally, stop the sensitive operation, avoid echoing the values, notify the authorized human, and follow the project's containment/rotation procedure. Do not invent self-erasure or other destructive responses.
- MCP and agent tools SHOULD follow least privilege. An entry in the MCP inventory does not automatically grant permission or require loading the server into a session. Explicit approval for a proposed provider or contract (D07) authorizes **documentation of the integration**, not installation, connection, live invocation, account creation or transmission of real data.
- **Public research (D06):** The Skill MAY consult relevant **public** technical documentation and official sources by default when its current environment provides lawful, authorized access. It SHOULD prioritize source authority and record source/version/review dates for material volatile claims. It MUST NOT transmit confidential project data, credentials, or other nonpublic information to a search service, MCP server or external provider without separate authorization. Connected private sources remain subject to their actual permissions and user intent; a missing tool or network connection is recorded as unverified, not faked. No continuous background monitoring is implied.

## 7. Agent context, handoffs, and selective loading

- `AGENTS.md` MUST be small enough to function as a **router**, not an encyclopedia. At session start load only mandatory safety/authority rules and the files necessary for the assigned task; expand on demand.
- `/docs/` contains enduring, shared project knowledge. `/.agents/context/` holds **small recoverable summaries** of agent-specific responsibilities, non-obvious findings, relevant references, and unresolved questions; `/.agents/handoffs/` records pause/completion and resumption instructions. Neither directory should duplicate PRD, architecture, source code, or full chat logs.
- A resumable handoff SHOULD include: task/role ID, date, status, related requirements/decisions, source/integration commit IDs, changed areas, checks and limitations, open questions, next action, and what would invalidate its conclusions.
- Provider-native sessions MAY be resumed where supported, but interoperability MUST rely on provider-neutral persistent artifacts. A reconstructed session is a **continuation of documented work**, not a guaranteed revival of the identical model instance or hidden state. Never inherit a previous agent's model/platform identity from these records; preserve a unique project-agent identity and omit unverified runtime details. Use a separate agent register only when actual project scale or coordination warrants it.
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
- **Pilot-feasibility-first planning (D14):** For consequential infrastructure decisions, distinguish current pilot goals, **hard vetoes** (including exact billing exposure, credit-card requirement and eligible terms), preferences and later commercial objectives. Identify the critical end-to-end path before selecting the exact provider/plan, check CPU/runtime limits, quotas, auth compatibility, total stack cost and failure behavior, then weigh reversibility and future migration. If compatibility cannot be supported by reliable evidence, plan a **bounded, authorized feasibility spike** before large dependent work; a cheap static deployment or successful build is not proof that Google sign-in or another critical path works. A non-viable option MUST NOT win a preference score. If none meets hard constraints, disclose the conflict, propose options and request an owner decision. Keep the output proportional; usually a concise PRD constraint, ADR/architecture note and prioritized backlog item suffice.
- **Deployment-aware but non-deploying (D02–D04):** The bootstrap SHOULD capture target distribution/execution environments, data boundaries, operational ownership, prerequisite accounts/costs, recovery and release questions to the depth needed for the **first unblocked implementation task**. Exact providers, numbers of environments, CI/IaC templates, budgets and runtime services are project-specific decisions, not universal mandates. Human sign-off is necessary for spending and production release. No undocumented deployment or readiness claim is permitted.
- **Roadmap and handoff (D04):** Distinguish proposed decisions, approved decisions, tasks, planned verification, executed verification and human acceptance. One specific, feasible, adequately specified and **unblocked implementation task** must be identifiable in the initial handoff; a spike or pure research task may precede it but does not, by itself, satisfy the implementation-readiness gate. Do not force one agent per chat, one task per conversation, or a particular CI implementation unless this project's authority rules justify it; focused branches remain governed by §4.
- Project conventions themselves are revisable: propose a reasoned change, record its decision authority and impact, and update dependent documents. Their purpose is **reliable collaboration without suppressing engineering judgment**.

## 10. Bootstrap acceptance checklist

The delivered **project-files ZIP (or other authorized handoff)** may be labelled **implementation-ready** only when all applicable conditions below are met (D04). A draft may be saved earlier, but MUST be clearly marked **incomplete / not implementation-ready**, not presented as a completed bootstrap:

- [ ] Project profile and unresolved decisions are explicit; no invented approvals.
- [ ] PRD has sufficient agreed scope and falsifiable acceptance criteria for the intended starting phase.
- [ ] **Default project-files ZIP:** contains working documentation and `.gitignore` **without `.git/`** and declares that Git branches are conventions to apply later. **Optional initialized Git ZIP:** real author identity, baseline commit and actual branches are verified after extraction. **Optional GitHub:** explicit publication consent and actual remote repository/branch state are verified. No special exception or fabricated author identity is required just because Git has not been initialized.
- [ ] The stack-specific `.gitignore` excludes `/.secrets/`, `/secrets/`, environment credentials and disposable outputs without silently excluding deliverables. First-Git transition verification is documented for the next authorized agent, not falsely claimed already done.
- [ ] Root entrypoints link to these conventions, and documentation paths are internally consistent.
- [ ] Optional files/directories and non-executed templates reflect actual needs instead of a blanket scaffold, and do not imply finished application code.
- [ ] Cheap autonomous topic→`dev` checks, retained history, safe branch deletion, human-owned `main` release, **no deployments from `dev`/topics**, and (when relevant) gameplay-test authorization rules are discoverable.
- [ ] Agent context boundaries, handoff conventions, and permitted tools are explicit.
- [ ] Scripts are traceable, actual project licenses are approved or explicitly unresolved, and deployment claims are not fabricated.
- [ ] **At least one implementation task is genuinely unblocked**, sufficiently specified, feasible, and linked to approved scope and verifiable acceptance criteria; significant provider-tier unknowns are **explicit prerequisites**, not falsely passed feasibility evidence. A research spike alone is insufficient.
- [ ] Material uncertainties have owners and gates, and no unresolved issue invalidates the starter task; no unapproved external action, secret disclosure, or paid commitment occurred. If GitHub delivery was chosen, repository visibility and destination were explicitly authorized and the actual result was verified.

## 11. Methodology decisions and validation status

The **inherited v0.1 methodology principles** D01–D10 were accepted on 12 November 2026. This document also proposes experimental D11–D14 adjustments from Portfoling feedback on 21 November 2026. They remain **candidate methodology** pending pilot tests and promotion; they do not pre-authorize remote writes, payments, deployment or choices within generated projects.

| ID | Inherited principle or experimental refinement | Application |
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
| D10 | **Inherited principles:** offer authorized Git/repository delivery and allow (never require) truthful optional AI self-attribution; **delivery default amended experimentally by D11** | §1–§4 and §10; truthful attribution, owner controls |
| D11 | **Experimental:** default to project files without `.git/`, with stack-aware `.gitignore` and one-time validation when Git first appears | §3, §4.1, §6, §10 |
| D12 | **Experimental:** distinct persistent agent and current runtime identities; precise optional coauthor trailers without fabricated model/platform/email | §4.2, §7 |
| D13 | **Experimental:** autonomous local non-squash topic→`dev` merges and safe cleanup, human-controlled `main` promotion, no `dev` deployments | §4.3, §5 |
| D14 | **Experimental:** critical-path feasibility under current-phase hard constraints before provider optimization; future horizon and migration considered proportionately | §1, §5, §9, §10 |

**Validation distinction:** D01–D10 are inherited approved principles; D11–D14 are **experimental candidates**, not evidence that the Skill works across providers or project classes. Pilot outcomes, defects, changes and lessons SHOULD later be tracked separately without retrospectively inventing acceptance or execution evidence. The original research reports are evidence and design inputs, not automatic normative rules.

*This document is a default collaboration contract, not a substitute for project-specific engineering judgment, authorized human decisions, or independent verification.*
