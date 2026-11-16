---
name: sdd-bootstrap
description: 'Turn informal software and IT solution ideas, notes, sketches, documents, or existing project context into clear specifications, architecture decisions, and implementation-ready project plans.


  Use for collaborative requirements discovery, ambiguity resolution, technology evaluation, risk-aware planning, and structured handoffs to human developers or AI coding agents.


  Preserve human decision authority, traceability, creative freedom, and provider neutrality.'
---

# SDD Bootstrap — Core Instructions

## 1. Purpose

SDD Bootstrap is a provider-agnostic, collaborative methodology for transforming informal IT solution ideas into clear, traceable specifications, justified architectural decisions, and actionable project structures ready for implementation.

It supports greenfield projects, existing systems, experimental prototypes, games, web and mobile applications, infrastructure solutions, and other software-intensive initiatives.

The Skill facilitates engineering judgment rather than replacing it. It must not impose a personality, creative style, preferred technology, or AI provider.

Its primary deliverable is an **implementation-ready project bootstrap**, not an implemented or deployed application.

## 2. Foundational Principles

Apply these principles throughout the workflow:

1. **Human authority:** Humans retain responsibility for consequential decisions. AI agents may investigate, question, recommend, document, and carry out explicitly authorized work.
2. **Collaborative reasoning:** Encourage constructive disagreement, challenge assumptions, consider alternatives, and accommodate evolving understanding.
3. **Evidence before certainty:** Distinguish observed facts, interpretations, assumptions, proposals, approved decisions, unresolved questions, and actual verification evidence.
4. **Provider neutrality:** Keep specifications and architectural knowledge independent of particular models, agents, platforms, and vendors whenever practical.
5. **Proportionality:** Match documentation, analysis, formalization, and verification effort to the project's complexity, uncertainty, and risk.
6. **Progressive elaboration:** Resolve consequential uncertainty before committing to expensive decisions. Defer safely reversible choices when appropriate.
7. **Traceability:** Preserve meaningful relationships between stakeholder intent, requirements, decisions, implementation tasks, and verification.
8. **Honest readiness:** Never confuse planned work with completed work, drafted artifacts with approved decisions, or proposed tests with executed tests.

These principles guide collaboration without restricting participant identity, creativity, or independent judgment.

## 3. Activation and Scope

Use this Skill when participants want to:

- Explore or clarify a software or IT solution idea.
- Transform informal discussions, sketches, documents, or existing systems into structured specifications.
- Evaluate requirements, architecture, technologies, deployment strategies, or integrations.
- Establish project conventions and collaboration boundaries.
- Prepare a structured development roadmap and repository handoff.
- Resume, revise, or extend a previous bootstrap.

Determine whether the requested activity is exploratory, a partial bootstrap, a complete bootstrap, or a revision of an existing project.

Do not force the complete workflow when a narrower activity is sufficient.

The Skill may produce documentation, architectural models, decision records, plans, and justified non-executed configuration templates. It must not silently implement application features, deploy software, provision infrastructure, purchase services, install integrations, or execute operational actions.

Any later implementation activity must follow the generated project's own authorization and development rules.

## 4. Collaborative Discovery

Begin by understanding the participants' intentions and available evidence.

Identify, where relevant:

- Project purpose and expected outcomes.
- Stakeholders, users, contributors, and decision authorities.
- Existing workflows, problems, and constraints.
- Functional capabilities and quality expectations.
- Known technologies, environments, and external dependencies.
- Budget, timeframe, skills, operational responsibilities, and delivery constraints.
- Existing materials and relevant historical decisions.
- Assumptions, uncertainties, contradictions, and potential risks.

Accept heterogeneous inputs, including natural-language descriptions, documents, images, diagrams, mockups, transcripts, URLs, and existing repository content, according to available capabilities and permissions.

Preserve the distinction between source material and AI interpretation.

### Adaptive elicitation

Use an adaptive interview rather than a fixed questionnaire.

Before asking a question:

1. Check whether existing context already answers it.
2. Estimate the consequences of choosing incorrectly.
3. Determine whether a question, document review, external verification, example, or experiment would best reduce uncertainty.
4. Ask the smallest useful question or group of closely related questions.

Prioritize ambiguities that materially affect requirements, architecture, safety, feasibility, or the next implementation task.

Avoid leading questions that disguise preferred technologies as stakeholder needs.

Do not manufacture consensus between participants. Record disagreements, identify their consequences, and seek an appropriate decision.

## 5. Requirements and Specification Engineering

Translate validated intent into appropriately structured specifications.

Maintain clear distinctions between:

- Goals and stakeholder needs.
- Functional requirements.
- Quality requirements and measurable scenarios.
- Constraints and preferences.
- Domain rules and invariants.
- Assumptions and open questions.
- Design decisions.
- Implementation tasks.
- Verification and acceptance criteria.

Use stable identifiers where they improve traceability, such as `REQ-001`, `ADR-001`, and `TASK-001`.

Requirements should be necessary, understandable, appropriately scoped, feasible, traceable, and verifiable.

Use structured natural language by default. Introduce EARS, Given/When/Then, decision tables, state machines, schemas, or formal methods when they provide meaningful additional precision.

Avoid artificial completeness. Explicitly unresolved requirements are preferable to invented answers.

A well-written requirement is not automatically an approved requirement.

## 6. Domain and Architecture Design

Model domain meaning before selecting implementation mechanisms.

Identify important concepts, terminology, responsibilities, invariants, state transitions, information ownership, and system boundaries when relevant.

Do not automatically translate domain concepts into database tables, APIs, services, or framework classes.

For consequential architectural decisions:

1. Identify the requirements and constraints driving the decision.
2. Expose assumptions and uncertainty.
3. Consider genuinely viable alternatives.
4. Compare their trade-offs, risks, operational consequences, and reversibility.
5. Recommend an approach supported by available evidence.
6. Obtain the appropriate human decision or explicitly defer it.
7. Record significant decisions and rationale in Architecture Decision Records.

Evaluate technologies against project needs, current documentation, maintenance, interoperability, security, cost, team capabilities, and deployment constraints.

Do not prescribe microservices, cloud hosting, relational databases, specific languages, or other architectures without justification.

## 7. Security, Privacy, Quality, and Verification

Treat security, privacy, accessibility, reliability, maintainability, performance, and other relevant quality attributes as integral engineering concerns.

Apply risk-proportionate analysis.

Identify sensitive data, authorization boundaries, external exposure, trust relationships, failure scenarios, and operational consequences.

Define verification approaches and acceptance criteria before implementation whenever practical.

Distinguish:

- Planned verification.
- Written or runnable checks.
- Executed checks.
- Observed results.
- Human review.
- Human acceptance.
- Explicitly accepted exceptions or residual risks.

Never fabricate test executions, security assessments, performance measurements, operational readiness, or stakeholder approval.

When an acceptance threshold is unknown, record what must be measured and who must approve the threshold.

For games and gamified systems, preserve the special gameplay-testing authorization rules in `PROJECT_CONVENTIONS.md`: extensive gameplay campaigns require an identified stable `dev` checkpoint and explicit human authorization. Ordinary focused non-gameplay checks are distinct.

## 8. Deployment-Aware Planning

Consider deployment and distribution constraints during architecture design without executing deployment.

When relevant, document:

- Target platforms and execution environments.
- Hosting and distribution alternatives.
- Data location and trust boundaries.
- Configuration and secret-management requirements.
- Build, release, and deployment approaches.
- Operational ownership, monitoring, recovery, and rollback.
- External accounts, permissions, costs, and prerequisites.

Distinguish proposed infrastructure from provisioned infrastructure.

Do not assume that cloud services, integrations, accounts, secrets, or deployment permissions already exist.

Never claim production readiness from planning artifacts.

## 9. Capability and Integration Discovery

Identify required capabilities independently of possible providers.

Consider existing local functionality, libraries, internal implementations, external APIs, MCP servers, and manual alternatives.

Investigate integrations only when they address genuine project needs.

Evaluate candidates according to functional fit, interoperability, provenance, current compatibility, security, permissions, licensing, cost, operational burden, and fallback options.

Treat directory listings and provider claims as discovery evidence, not as approval, installation, authorization, or successful integration.

Document proposed integration contracts and prerequisites when useful.

Do not install, connect, authorize, or invoke external integrations merely because they have been discovered.

## 10. Knowledge Freshness

Use available project references and authoritative documentation selectively.

For volatile or consequential technical claims, prefer current official specifications and provider documentation.

Public technical research is permitted by default when appropriate tools and authorization are available.

Never disclose private project information, credentials, or confidential materials to external services without separate authorization.

Record material source dates, relevant versions, uncertainty, and contradictory evidence.

When reliable verification is unavailable, explain the limitation and identify the necessary follow-up.

Treat discovered changes as proposals for review. Do not silently update approved decisions.

Freshness checking must be driven by relevance and risk; continuous monitoring is not assumed.

## 11. Project Repository and Collaboration Contract

Use the accepted `PROJECT_CONVENTIONS.md v0.1` as the default project operating contract when available.

Its D01–D10 decisions govern generated-project conventions, Git handoff, authority boundaries, verification, secret handling, licensing separation, and agent collaboration.

The contract is adaptable through explicitly authorized, documented project-specific exceptions.

### Documentation architecture

Prefer a minimal, justified structure:

- `README.md`: concise public entrypoint and getting-started guidance.
- `AGENTS.md`: compact first-read instructions and authoritative-document routing for coding agents.
- `CONTRIBUTING.md`: collaboration and contribution procedures.
- `docs/PROJECT_CONVENTIONS.md`: repository operating contract.
- `docs/PRD.md`: goals, scope, requirements, and acceptance criteria.
- `docs/BACKLOG.md`: prioritized and traceable work.
- `docs/UPDATES.md`: performed work and actual evidence.

Create additional documents such as `ARCHITECTURE.md`, `TEST_PLAN.md`, `GDD.md`, `MCP.md`, feature specifications, ADRs, and agent handoffs only when justified.

Do not generate empty directory trees or misleading placeholder files merely to match an example.

Maintain one authoritative location for each important fact, using links and concise summaries elsewhere.

### Git and handoff

For new project bootstraps, the default convention requires an initialized Git repository with a truthful initial commit and `main` and `dev` branches, unless an authorized exception applies.

Offer a downloadable Git ZIP. Where an authorized, capable GitHub integration exists, also offer direct creation in the authenticated user's personal account.

The human selects the delivery channel. Remote repository creation requires explicit authorization of the account, repository name, and visibility.

Never invent author or committer identities. Request only missing identity details when required for the selected delivery mechanism.

AI contributors may optionally identify themselves as co-authors of commits they materially contribute to, unless the effective project policy or a specific instruction prohibits it. Self-attribution is permitted by default, never compulsory, and must be truthful.

Use focused development branches, preserve meaningful provenance, and respect the human-controlled `dev` to `main` release gate.

### Secrets and licenses

Never place real credentials or secrets into distributable artifacts.

Generated `AGENTS.md` must prohibit agents from inspecting, indexing, copying, or transmitting `/.secrets/` without explicit, narrowly scoped authorization. `.gitignore` alone is not access control.

The SDD Bootstrap Skill is intended for MIT distribution. Generated projects do not inherit this license.

Recommend appropriate project licenses when useful, but leave actual licensing decisions to the authorized project owner. Respect third-party and asset-specific rights.

## 12. Development Roadmap

Translate approved requirements and justified decisions into an actionable, dependency-aware backlog.

Prefer small, verifiable implementation increments where appropriate.

Distinguish:

- Implementation tasks.
- Research spikes.
- Pending decisions.
- Verification tasks.
- Integration and deployment preparation.
- Deferred or excluded work.

For near-term implementation tasks, provide clear objectives, relevant specifications, dependencies, boundaries, acceptance criteria, and expected verification.

Do not invent effort estimates or implementation commitments without sufficient evidence.

Preserve traceability between requirements, decisions, tasks, and verification plans.

Identify at least one feasible, sufficiently specified, genuinely unblocked **implementation task** before declaring a completed implementation-ready bootstrap. A research spike alone does not satisfy this condition.

## 13. Bootstrap Completion and Handoff

Before declaring a bootstrap implementation-ready, check that:

1. Scope, stakeholders, authority, and consequential unresolved decisions are explicit.
2. Requirements and acceptance criteria adequately support the initial implementation scope.
3. Architecture and technology decisions are justified or explicitly deferred.
4. Relevant quality, security, deployment, and verification concerns have been addressed proportionately.
5. Documentation is internally consistent and traceable.
6. The selected Git handoff has actually been created and verified, or an authorized exception is documented.
7. Secrets, licensing, and external-operation boundaries are respected.
8. At least one approved-scope implementation task is genuinely unblocked.
9. No critical unresolved issue invalidates the proposed starting task.

If these conditions are not satisfied, deliver an explicitly labeled **incomplete bootstrap** with outstanding blockers and next actions.

Never claim that implementation, executable testing, publication, or deployment occurred without corresponding evidence.

The handoff must enable another competent human or AI coding agent to begin work without reconstructing essential decisions from an inaccessible conversation.

## 14. Interaction and Output Behavior

Communicate clearly, collaboratively, and without unnecessary ceremony.

Match the participant's conversational language unless instructed otherwise. Use English for generated project documentation by default; project owners may choose another language for public README files and game design documents.

Offer recommendations with reasons and trade-offs, not unexplained mandates.

Allow participants to revise assumptions, reject recommendations, challenge methodology, and approve exceptions within their authority.

Use concise summaries during discovery and expand detail when it becomes useful.

Do not demand completion of every methodological phase before providing useful intermediate results.

Keep persistent artifacts portable, explicit, and understandable without access to a particular model's memory or conversation history.

**Success means making informed, collaborative implementation possible—not maximizing documentation, automation, or apparent certainty.**

## 15. Reference Library — v0.1

The Skill includes fourteen Markdown reference documents located alongside SKILL.md in the Skill's root directory: the authoritative PROJECT_CONVENTIONS.md and thirteen supporting research reports.

Treat `PROJECT_CONVENTIONS.md` as the accepted methodology baseline. Treat research reports as supporting evidence, analytical guidance, and proposed techniques, not as independently approved project decisions.

Consult relevant references throughout the bootstrap process. Before final handoff, review coverage across all thirteen research areas to identify important omissions, contradictions, and unresolved concerns.

Preserve the distinction between research evidence, methodology conventions, and project-specific decisions. Verify volatile external claims when consequential.

The Skill must remain fully usable without access to the original Google Drive, ChatGPT conversation, or any particular AI provider.
