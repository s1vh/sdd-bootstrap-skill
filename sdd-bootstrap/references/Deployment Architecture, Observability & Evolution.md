# Research 08 — Deployment Architecture, Observability & Evolution


> **Reviewed and enriched candidate — 12 November 2026 (v0.2).** Independently revised from the 11 November Drive draft. This is an advanced knowledge reference for the SDD Bootstrap Skill, **not** a deployment plan approved for any real project, a tested infrastructure configuration, or proof of operational readiness. Source links and proposed heuristics are identified below. This Drive edition has been editorially aligned with the accepted methodology conventions; historical source drafts remain distinguishable through Drive revision history.


## Executive synthesis and evidence discipline


Deployment architecture is the mapping of application capabilities, data, dependencies, identities and trust boundaries onto execution and distribution environments. It is a consequential architecture view, not a cloud-provider shopping list. A specification-driven bootstrap should describe *where the proposed system could run, how it would be released, how its failure would be detected and recovered from, who would operate it, and what decisions remain unapproved*. It should not create paid resources, obtain credentials, deploy code, announce successful checks, or invent operational targets.


The recommended approach is **risk-proportionate operational design**. A solo static portfolio can be implementation-ready with a hosting hypothesis, domain/DNS dependencies, a publishing procedure, a privacy check and a recovery path. A multi-user educational platform may additionally need identity and tenant isolation, personal-data controls, release and migration plans, cost ownership and incident response. A privacy-sensitive API may need stronger supply-chain, vendor, data-transfer and resilience controls. An offline-capable client may need version-compatible synchronization and signed device releases rather than a traditional web deployment pipeline. These differences are design consequences, not different levels of professionalism.


**Evidence classes used throughout:**


| Label | Meaning |
|---|---|
| Established | Primary standard, authoritative specification or official tool documentation supports the statement. |
| Context-dependent practice | A commonly useful engineering pattern, with applicability contingent on workload and organization. |
| Proposed SDD heuristic | A v0.1 methodology suggestion requiring pilot evaluation. |
| Illustrative | A fictional example, not a measured threshold, selected vendor, stakeholder approval or executed result. |
| Volatile | Pricing, free-tier terms, provider features, runtime versions, legal interpretations or quotas requiring a fresh check at decision time. |


The report is grounded in published guidance from ISO/IEC/IEEE 42010, NIST SSDF and CSF, Google SRE, OpenTelemetry, SLSA, OWASP, HHS, W3C, FinOps and official provider documentation [S01–S25]. The source list is selective rather than a claim that every recommendation has empirical proof. Standards define vocabulary and controls; they do not decide a particular project's cloud, SLO or topology. Research conclusions and the v0.1 rules below are proposals to test, not universal mandates. The accepted [`PROJECT_CONVENTIONS.md`](PROJECT_CONVENTIONS.md) is the authoritative methodology contract for generated-project paths, baseline Git history, human approval and handoff. Its approved D01–D10 rules prevail over conflicting research examples; project-specific exceptions still require appropriate human authorization.


### Bootstrap boundary and status vocabulary


| State | What it permits us to say | What it does **not** imply |
|---|---|---|
| Proposed | Candidate topology, service, control or template exists | Approved choice |
| Reviewed | Responsible participants assessed the proposal | Tested implementation |
| Approved for implementation | Decision owner accepted scope and trade-offs | Resources provisioned |
| Configured | Actual environment settings were applied with evidence | Correctness or security |
| Exercised | A check was run with recorded inputs and result | All failure modes covered |
| Production-ready | Authorized evidence meets agreed release/operational criteria | Permanent future reliability |


A bootstrap normally ends at **approved-for-implementation**, with some artifacts still proposed or blocked. A future implementer can then execute the work and attach actual build, deployment, recovery and monitoring evidence. Never infer a passing check from a YAML file or an operational guarantee from a provider's marketing page. This boundary complements Research 02 (requirements/traceability), 03 (architecture), 04 (security/privacy), 05 (repository governance), 06 (verification) and 07 (domain/data/API contracts).


## 1. Deployment architecture as a decision system


ISO/IEC/IEEE 42010 distinguishes an architecture from its description and encourages views that address stakeholders' concerns [S01]. A deployment view should therefore be chosen for its explanatory power. It may show execution nodes, networks, storage, external systems, credentials as *types*, administrative access, trust boundaries, data residency, failure domains and release channels. It must not publish secret values or pretend that conceptual nodes are already running.


| Distinction | Meaning | Example |
|---|---|---|
| Application architecture | Internal boundaries and interactions | UI, domain module, API adapter |
| Deployment architecture | Execution placement and connectivity | CDN, app process, managed DB |
| Distribution architecture | How software reaches clients | Static publish, app store, OTA |
| Environment architecture | Isolation and configuration per stage | Local, preview, staging, production |
| Delivery architecture | How artifacts are built, approved and promoted | CI, registry, deployment gate |
| Operational architecture | How behavior is observed, protected and recovered | SLI, alerts, runbook, backup |
| Architecture description | Documented model and rationale | Diagram + ADR + dependency inventory |


A bootstrap should elicit *drivers* before generating a diagram: public/private access; location of persistent state; sensitivity and jurisdiction; traffic pattern; offline needs; latency; recovery expectations; operator availability; funding; integrations; distribution constraints; and reversibility. If a driver is unknown, record its owner, consequence and decision deadline rather than filling it with a confident guess.


### The minimum meaningful deployment view


~~~mermaid
flowchart LR
    User[Visitor / client] -->|TLS| Edge[Public delivery boundary]
    Edge --> App[Proposed application runtime]
    App -->|restricted identity| Data[(Private persistent store)]
    App -->|scoped credentials| Vendor[External provider]
    Ops[Authorized operator] -.->|controlled access| App
    CI[Future build and promotion] -.->|approved artifact| Edge
~~~


**Interpretation:** This is a *generic illustration*, not a required three-tier architecture. A static site can remove App and Data. An embedded application may have no Edge. A service may combine Edge and App. Every edge in a project-specific diagram should eventually identify protocol, data class, trust boundary, failure implication and whether the connection is confirmed or hypothetical.


### Decision protocol


1. Identify veto constraints (regulatory location, platform support, offline operation, contractual obligations, staffing, cost ceiling).
2. Describe at least two viable alternatives for a consequential choice, unless one is eliminated by a verified hard constraint.
3. Compare operations, security, cost, data portability, recoverability, delivery speed and exit path.
4. Identify uncertainties that can be resolved cheaply by a time-boxed spike.
5. Ask the accountable human to approve, reject or defer the decision.
6. Record the rationale, evidence date, reversibility and re-evaluation trigger in an ADR.
7. Trace the approved decision to requirements, deployment view, backlog and planned verification.


**Proposed heuristic:** Operational significance increases with the consequence of failure, cost of reversal, sensitivity of data, external dependency and scarcity of operator capacity. This is a triage aid, not a numerical risk standard.


## 2. Deployment and distribution options


Deployment models overlap. A managed container platform can be serverless in its billing/execution model; Kubernetes may run on premises or in a managed cloud; an edge function is still a function runtime. “Container”, “serverless”, “cloud”, “PaaS” and “microservices” answer different questions. Evaluate *responsibility boundaries*, not labels.


| Candidate | Typical strengths | Common hidden costs / limits | Good initial fit |
|---|---|---|---|
| Static hosting + CDN | Low application operations; globally cacheable files | DNS, content publishing, cache invalidation, optional forms/analytics | Public content, static portfolio |
| Managed web/PaaS | Provider manages much of runtime and platform | Pricing tiers, quotas, sleep behavior, regional coverage, platform-specific configuration | Small web apps, simple APIs |
| Managed containers | Portable image packaging; flexible runtime | Registry, networking, startup behavior, image patching, secrets, observability | APIs/workers with container needs |
| Functions/edge runtime | Event-based scale and low idle compute for suitable workloads | Runtime/time limits, request economics, provider APIs, concurrency, cold start variability | Webhooks, scheduled jobs, edge logic |
| VM / on-prem host | Control and compatibility | OS maintenance, patching, backup, capacity and access management | Legacy, special runtime, local constraints |
| Kubernetes | Rich scheduling and platform ecosystem | Cluster expertise, policies, upgrades, multi-component failure modes | Existing platform teams, complex orchestration |
| Hybrid / edge / device | Locality, offline or hardware control | Fleet management, sync, update safety, device security | Embedded, intermittently connected workloads |
| Store / package distribution | Native platform reach and signing channels | Review policies, signing identities, backward compatibility, rollout lag | Mobile, desktop, games |


**Reject universal rankings.** “Kubernetes is most scalable” ignores workload, people, failure domains and cost. “Serverless has no operations” ignores configuration, identity, observability and vendor dependencies. “Containers eliminate lock-in” ignores managed databases, ingress, IAM, billing, storage and proprietary APIs. Static sites may use third-party form services, but that introduces its own data-processing and availability boundary.


A portable design may prefer open protocols and exportable data, but abstraction has cost. A managed database may be the correct choice when operations capacity is scarce. The ADR should record a credible *exit strategy* (export format, migration feasibility, contract termination, domain/DNS ownership), not promise zero lock-in.


**Volatile pricing correction:** Heroku ended free dynos and free Heroku Postgres/Key-Value Store plans in November 2022 [S18]. AWS free-tier terms differ for accounts created before versus after 15 July 2025 [S19]. Neither “free forever” nor a fixed cloud price belongs in a static reference report. Recheck the chosen provider's official price calculator, billing conditions, region and limits at decision time.


### Deployment-option comparison record


~~~yaml
decision_id: ADR-DEP-001
status: proposed
question: "Where should the first deployable run?"
hard_constraints:
  - "No real credentials or cloud resources in bootstrap"
alternatives:
  - name: static_host
    viable_if: "No server-side protected workflow is required"
  - name: managed_app
    viable_if: "Dynamic backend is required and provider constraints fit"
  - name: self_managed_vm
    viable_if: "Team accepts OS and runtime operations"
unknowns:
  - id: Q-DEP-01
    question: "Is a protected server-side workflow required in v1?"
    owner: product_owner
    gate_before: final_topology
decision_owner: human_product_owner_and_technical_lead
approved: false
~~~


## 3. Environment design, configuration and trust


There is **no universal requirement for three environments**. Local development plus production may be enough for a static portfolio; ephemeral preview environments may replace a permanent staging environment; high-risk services may need isolated integration, pre-production and recovery environments. The governing question is what must be validated without exposing production users, secrets or data.


| Environment profile | Purpose | Data policy | Deployment authority | When warranted |
|---|---|---|---|---|
| Local | Rapid iteration and unit checks | Synthetic/local | Developer | Almost always |
| Preview / ephemeral | Review a branch or PR | Synthetic; isolated | CI with constrained permissions | UI and collaborative review |
| Integration | Test real boundaries | Test fixtures and non-production credentials | CI/authorized testers | External systems and data flows |
| Staging / pre-prod | Rehearse release, migrations and recovery | Synthetic or legally approved de-identified data | Restricted deployer | Risk or complexity justifies fidelity |
| Production | Serve real users | Approved operational data | Authorized release process | After readiness gates |
| Recovery sandbox | Restore rehearsal and incident simulation | Controlled snapshots or synthetic replicas | Explicit owner approval | Durable/sensitive data |


**Isolation is not merely naming.** Assess accounts/projects, networks, IAM roles, key material, data stores, domains, billing boundaries and log destinations. Do not copy production data into staging by default. Synthetic test data is preferable; de-identification is a substantive process, not a synonym for deleting names.


A configuration contract should specify the **name and purpose** of each setting, whether it is secret, its source and environment scope, who provisions it, how it rotates, and how to detect absence without printing its value. Client-side variables are public even when named “SECRET”; mobile application packages cannot securely conceal a long-lived provider credential. Prefer short-lived, audience-scoped tokens and server-side handling where appropriate.


~~~yaml
# docs/operations/environments.yaml — illustrative schema, not deployed config
environments:
  local:
    purpose: development
    data_class: synthetic
    secret_source: local_uncommitted
  production:
    purpose: real_users
    data_class: to_be_classified
    secret_source: approved_secret_manager
    deployment_approval: human_release_owner
    provisioned: false
open_questions:
  - id: Q-ENV-002
    question: "Is an independent staging environment justified?"
    owner: technical_lead
    gate_before: release_design_approval
~~~


Separate **configuration drift** (actual settings diverge), **architecture drift** (running topology diverges from decisions) and **specification drift** (decisions no longer satisfy requirements). Infrastructure as Code can reduce some drift, but not detect every manual change, provider default or semantic mismatch.


## 4. Build, release, promotion and rollback


A build turns reviewed source and declared dependencies into an artifact. A release identifies an approved artifact and its change set. Deployment places it into an environment. **Release approval, deployment success and user-visible feature enablement are separate events.** Continuous integration, delivery and deployment are not synonyms; choose the automation level according to the team's authority model.


~~~mermaid
flowchart LR
    Spec[Approved requirement / ADR] --> Change[Reviewed change]
    Change --> CI[CI checks and artifact build]
    CI --> Evidence[Recorded result + artifact identity]
    Evidence --> Gate{Human / policy release gate}
    Gate -->|approved| Promote[Promote same artifact]
    Promote --> Verify[Post-deploy checks]
    Verify --> Monitor[Observe user impact]
    Monitor -->|regression| Mitigate[Rollback / forward fix / disable feature]
    Gate -->|not approved| Hold[Hold release]
~~~


The **same artifact** should ordinarily be promoted across environments where feasible, with environment-specific configuration supplied separately. Rebuilding from mutable dependencies at every promotion weakens traceability. Artifact identity may use an immutable digest, signed attestation and commit reference when risk warrants. A version tag alone is not a security guarantee.


### Risk-based release strategies


| Strategy | Strength | Risk / prerequisite | Appropriate when |
|---|---|---|---|
| Atomic static publish | Simple replacement | CDN cache and DNS behavior | Small static sites |
| Rolling | Low extra capacity | Mixed versions must coexist | Ordinary stateless services |
| Blue/green | Fast traffic switch | Double capacity; DB/schema compatibility | Reversible traffic routing |
| Canary / progressive | Observe subset before broad rollout | Routing, sufficient traffic and signals | Significant user-impact risk |
| Feature flag | Separate deployment from activation | Flag lifecycle, state/authorization consistency | Incremental rollout |
| Store/phased mobile rollout | Platform-managed distribution | Installed clients persist; no instant rollback | Mobile/desktop releases |
| OTA staged rollout | Fleet risk containment | Signing, power loss, hardware compatibility | Embedded/IoT |


**Rollback is not “deploy the previous image” when persistent data has changed.** Schema changes, external side effects, queued events and irreversible migrations may require *forward recovery*, compatibility windows or compensating actions. An expand–migrate–contract approach can permit old and new code to coexist during data evolution. Record what can be rolled back, what cannot, and who authorizes recovery.


A proposed release plan should include: artifact provenance; environment prerequisites; credentials/permissions (types only); deployment and smoke-test sequence; change window if relevant; expected user impact; monitoring signals; rollback/forward-fix decision rule; communication owner; and evidence capture. A successful build is not a successful deployment; a successful deployment is not proof of business acceptance.


### Supply-chain assurance without ritual


Pin runtime versions and dependencies where useful; use lockfiles where the ecosystem supports them; isolate privileged CI from untrusted contributions; minimize token permissions; pin third-party CI actions to immutable revisions when feasible; review dependencies and generated scripts. GitHub's secure-use guidance documents risks from privileged workflows, compromised runners and untrusted PR content [S10]. NIST SSDF supplies lifecycle-oriented secure development practices [S05].


SBOMs (SPDX/CycloneDX), signatures (e.g. Sigstore), provenance and SLSA are **conditional controls**, not a mandatory bundle for every bootstrap. SLSA 1.2 describes graded build/source provenance and trust properties [S07]. A signature establishes a relationship to a signing identity under a verification policy; it does not prove an artifact is safe, correct or free of vulnerabilities. A checksum of a Markdown file verifies bytes, not operational readiness.


| Assurance layer | Bootstrap can define | Later execution must prove |
|---|---|---|
| Dependency repeatability | Toolchain/version policy, lockfile approach | Clean build resolves as expected |
| CI security | Least-privilege workflow design, untrusted-PR boundary | Actual permissions and logs |
| Artifact integrity | Registry, digest, signing/provenance plan | Artifact and verified attestation |
| Vulnerability management | Scan and exception policy | Scan results, triage and remediation |
| Release controls | Gate owner and criteria | Actual approval and promotion evidence |
| Recovery | Rollback/restore procedure | Rehearsal or incident evidence |


Do not write “SLSA-compliant”, “SBOM generated”, “signed release” or “CI passed” unless corresponding evidence exists.


## 5. Infrastructure as Code, GitOps and provisioning authority


IaC is a way to describe and manage resources; it is not intrinsically required for every project and is not equivalent to reproducible deployment. Tool selection depends on target infrastructure, team skills, state security, provider coverage, testing needs and portability.


| Approach | Strength | Principal caution |
|---|---|---|
| Provider-managed configuration / documented UI | Low initial overhead | Manual drift, weak repeatability |
| Terraform / OpenTofu | Declarative desired state across many providers | Provider/plugin versions, state security, plan/apply authority |
| Pulumi | Infrastructure in general-purpose languages | Program complexity, state/backend governance |
| CloudFormation / cloud-specific IaC | Native service integration | Provider-specific semantics and migration cost |
| Ansible | Host configuration and procedural automation | Inventory, idempotence and secret handling |
| Kubernetes manifests / Helm | Cluster workload configuration | Requires an actual cluster/platform and operational expertise |
| GitOps controller | Reconciliation from reviewed desired state | Controller permissions, secrets, drift policy and failure modes |


Terraform and OpenTofu are related but distinct projects with licensing, governance and compatibility considerations; they should not be treated as one identical product [S16]. Kubernetes manifests are not a substitute for defining network, storage, identity and cluster lifecycle. GitOps is not “all Git commits deploy automatically”; it requires explicit reconciliation, authority and audit controls.


**IaC state may contain sensitive information**, including provider-returned secrets or resource metadata. State storage needs access control, encryption, locking where supported and recovery policy. Plans may expose sensitive values; do not paste them into general-purpose agent context. Generated infrastructure code should default to *non-applying*, secret-free templates and include explicit cost and destruction warnings.


### Bootstrap IaC gate


~~~yaml
infrastructure_change:
  status: proposed
  target: undecided
  resources_created: false
  network_access_executed: false
  estimated_cost: unknown
  credentials_included: false
  required_before_apply:
    - human_approval_of_provider_and_region
    - billing_owner_and_budget_guardrail
    - state_backend_security_review
    - least_privilege_identity_review
    - preview_or_plan_review
    - backup_and_deletion_policy
~~~


An agent may draft and statically inspect templates in an approved local workspace. Running `plan` may access remote APIs and reveal infrastructure details; running `apply` or `destroy` changes external state. Neither should be silently treated as a harmless documentation step. All externally consequential operations require explicit authorization.


## 6. Security, privacy, jurisdiction and operational risk


Security architecture begins with the trust boundaries and the data lifecycle. Record: what data exists; who controls it; who can access it; where it is stored, backed up and observed; which vendors receive it; how access is revoked; how it is deleted; and which incident duties apply. NIST CSF 2.0 organizes cybersecurity outcomes across Govern, Identify, Protect, Detect, Respond and Recover [S06]; NIST SSDF addresses secure-development practices [S05]. Neither prescribes a specific deployment platform.


Key controls to *consider, not automatically assert as implemented*:


- Identity: authentication protocol, token audience/lifetime, service identities, least privilege, privileged administrator MFA, emergency access.
- Network: intended public endpoints, egress rules, segmentation, TLS termination, certificate renewal, SSRF risk.
- Application: authorization at every protected resource boundary; input validation; safe uploads; dependency and container security; appropriate OWASP ASVS/API Security requirements [S09].
- Secrets: provision through approved stores; no secrets in repository, screenshots, prompts, logs, client binaries or exported ZIPs; defined rotation/revocation process.
- Data: classification, encryption/key ownership, backup protection, retention/deletion, consent and access controls.
- Delivery: protected CI identities, human review of destructive changes, signed or provenance-backed artifacts when justified.
- Incident: severity, escalation, evidence retention, notification decision authority, containment and recovery roles.


**OAuth 2.0 is an authorization framework; OpenID Connect is an identity layer; JWT is a token format.** They are not interchangeable security prescriptions. A static public portfolio may need none of them. “Use JWT” is not a requirement or an architecture by itself.


**Jurisdiction is conditional.** GDPR applicability depends on actual processing and territorial scope, not merely the presence of an EU IP address; data residency requirements may be contractual, regulatory or self-imposed. “EU database” does not by itself settle backups, support access, telemetry, third-party processors or international transfers. Record a data-flow inventory and request qualified legal/privacy review where warranted [S11]. For educational projects, do not assume students are minors or automatically require parental consent: age, jurisdiction, service context and applicable rules must be established.


**HIPAA correction:** there is no generic “HIPAA-certified cloud” shortcut. Where HIPAA applies, HHS guidance addresses the covered-entity/business-associate relationship, including a compliant business associate agreement with a cloud provider handling ePHI, plus applicable safeguards and responsibilities [S12]. Likewise, PCI DSS applicability depends on payment-data handling and contractual obligations, not simply being a financial application.


### Security/privacy decision ledger


| Trigger | Required discovery | Possible outcome |
|---|---|---|
| Students, minors or educational records | Age ranges, roles, institutions, jurisdiction, consent and retention | Privacy/legal review before account design |
| Sensitive health/finance data | Classification, applicable regulation, vendor contracts, threat model | Stronger hosting, key and audit requirements |
| Public file uploads | Content type, size, malware/abuse risk, moderation, access rules | Isolated storage, scanning or explicit rejection |
| External APIs | Credential scope, data transfer, rate limits, outage behavior | Integration contract and vendor exit plan |
| Multiple tenants/cohorts | Data isolation model, role transitions, admin boundaries | Negative authorization tests and tenant-aware telemetry |
| Offline devices | Device loss, local encryption, update signing, revocation | Device lifecycle and compatibility plan |


**Human gate:** Regulatory interpretations, retention periods, security exceptions and material risk acceptance require accountable participants; AI-generated checklists are not legal opinions or proof of compliance.


## 7. Reliability, recovery and failure economics


Reliability should be expressed through *user-relevant outcomes*, not infrastructure adjectives. A service can have healthy CPU and still fail users; a statically hosted site can be reachable while its contact form is broken. Google SRE guidance treats service-level indicators (SLIs) as measurements, objectives (SLOs) as targets for those measurements, and service-level agreements (SLAs) as contractual commitments with consequences [S02].


### Deriving rather than inventing SLOs


A candidate SLI needs a numerator, denominator or measurement distribution, eligible population, time window, source and exclusion policy. Examples:


~~~yaml
sli_id: SLI-PUBLISH-001
user_journey: "Student publishes an approved portfolio"
indicator: successful_publish_operations / eligible_publish_attempts
measurement_window: TBD
data_source: planned_application_event
exclusions: needs_stakeholder_review
slo:
  target: TBD
  approved_by: null
status: proposed_not_measured
~~~


A percentile is a statistic of a latency distribution, not a universal SLO. “99% of requests under 300 ms p95” mixes two incompatible formulations unless carefully defined. Better candidates are “at least X% of eligible requests complete within Y ms over Z days” *or* “the measured p95 latency is below Y ms over Z days”, with X/Y/Z approved from user needs, baselines and economics. Do not insert 99.9%, 500 ms or other attractive numbers as project facts.


An **error budget** derives from an approved SLO and its measurement window. SRE guidance describes multi-window burn-rate alerting to identify consequential consumption of that budget, and explicitly warns that low-traffic services need different handling [S03]. Do not page a volunteer for every transient error or use CPU-only alerts as a substitute for user impact.


### Recovery is a design obligation


| Term | Correct interpretation | Bootstrap question |
|---|---|---|
| RPO | Maximum acceptable data loss measured in time | How much recent data may be lost? |
| RTO | Target time to restore service after disruption | How long can users tolerate outage? |
| Backup frequency | How often copies are created | Does it plausibly support the RPO? |
| Restore test | Evidence that a backup can be used | Who will rehearse it, when and where? |
| HA / replication | Techniques for reducing outage | What failure modes remain shared? |
| Disaster recovery | Response to major disruption | What people, credentials, data and dependencies are needed? |


Nightly backups do not prove a 24-hour RPO under every failure; replication does not replace backups and can propagate deletion/corruption. A one-hour RPO is not implied by “multi-AZ”. Recovery targets must be approved in light of data value, operational capacity and cost. A static site's source repository may enable reconstruction, but only if its assets, domain configuration, build inputs, access rights and independent copies survive the incident.


**Failure-oriented questions:** What happens if the identity provider is down? DNS is misconfigured? A database migration partially completes? A queue redelivers an event? A cloud account is locked? A maintainer is unavailable? A mobile device remains offline for months? A third-party vendor changes its API? Which failures require manual intervention, and which may safely retry?


Retries require bounded attempts, deadlines, backoff/jitter, idempotency and an understanding of partial side effects. Circuit breakers, queues and caching can improve resilience but also create stale-data, consistency and recovery complexity. Design them for observed risks rather than inserting them automatically.


### Operational runbook structure


~~~markdown
# RUNBOOK-001 — Public service unavailable
Status: PROPOSED / NOT REHEARSED
Service owner: TBD
Trigger: User-impact SLI or verified synthetic check
Severity / escalation: TBD


1. Confirm the user-visible symptom and affected scope.
2. Identify recent releases, dependency outages and configuration changes.
3. Check approved dashboards/logs without exposing personal data.
4. Determine whether rollback is safe for current schema and side effects.
5. Obtain the required incident or production-change authorization.
6. Apply the least destructive approved mitigation.
7. Verify recovery using the agreed user journey, not just process health.
8. Communicate status; preserve evidence; schedule follow-up.


Do not restart, fail over, delete data or restore a snapshot merely because
a generic runbook says so. These actions can worsen an incident.
~~~


A runbook is not “tested” until a qualified operator can follow it in a controlled rehearsal or incident. Document what to do when no 24/7 on-call team exists; an unrealistic support promise is an operational defect.


## 8. Observability as an answer to operational questions


Observability is the ability to infer relevant internal behavior from available signals. **Metrics, logs and traces are useful signal families, not a mandatory three-product shopping list.** OpenTelemetry supports traces, metrics and logs and documents additional context mechanisms; support and maturity can vary by language and component [S04]. A static site may need a synthetic check, host status and error reports, while a distributed API may justify tracing and queue instrumentation.


Design observability *backward from questions*:


| Operational question | Candidate signal | Owner/action | Privacy/cost consideration |
|---|---|---|---|
| Can a visitor open the portfolio? | External synthetic page check | Site maintainer investigates hosting/DNS | Avoid unnecessary visitor tracking |
| Can a student publish? | Eligible attempt/success counters | Product/operations triage | Aggregate; no project title or student ID in metric labels |
| Are cohorts isolated? | Authorization-denial patterns + audit events | Security owner investigates | Restricted access; avoid exposing identities in dashboards |
| Are vendor events stuck? | Oldest queue item age, retry count, dead-letter count | Integration operator checks provider and replay | Do not log payloads containing sensitive data |
| Are offline edits at risk? | Local unsynced count, age and sync outcome | Client team investigates compatibility | Consent, data minimization and bounded offline storage |
| Did a release regress? | Error/latency delta by release version | Release owner mitigates | Control metric cardinality and sampling |


### Instrumentation contract


An event or metric should specify name, meaning, unit, dimensions, collection method, retention, access control and redaction policy. **High-cardinality identifiers** (student email, portfolio ID, request ID) should not be metric labels; where necessary, correlate specific events through restricted logs or traces. Structured logs have stable fields and semantics, not merely JSON serialization [S04]. W3C Trace Context defines propagation mechanisms, but tracing baggage and custom headers can leak sensitive data across trust boundaries if misused [S13].


~~~yaml
# docs/operations/observability.yaml — plan, not a deployed configuration
service: portfolio_api
signals:
  - id: OBS-001
    question: "Are approved publish requests succeeding?"
    kind: metric
    name: publish_attempts_total
    labels: [result, release_version]  # bounded cardinality
    prohibited_labels: [student_email, portfolio_title, access_token]
    status: planned
  - id: OBS-002
    question: "Why did a request fail?"
    kind: structured_log
    allowed_fields: [timestamp, service, severity, route_template, status, trace_id]
    prohibited_fields: [authorization_header, password, request_body]
    status: planned
alerts:
  - id: ALERT-001
    condition: TBD_after_baseline_and_SLO_approval
    notification_owner: TBD
    escalation: TBD
    status: not_configured
telemetry:
  retention_days: TBD
  collection_region: TBD
  data_controller_review: required_if_personal_data
~~~


Sampling and retention are trade-offs: tracing every request may be expensive or intrusive, while sampling too aggressively can obscure rare incidents. Define who can view telemetry, how long it persists, whether it crosses regions, and how it is deleted. Product analytics and operational observability have different purposes and may need different consent or legal bases. A “privacy-safe” label is not evidence of compliance.


**Alert design:** Alert on actionable user impact where possible; identify an owner and a response; avoid arbitrary “CPU > 80% for 2 minutes” pages. For low-traffic systems, synthetic checks or longer windows may provide a more meaningful signal than request-rate error budgets. A dashboard without a responder is not an operational control.


## 9. Cost, ownership and sustainable operations


Operational cost includes more than compute: database, storage, backup, egress, logs/traces, DNS, certificates, email, queues, third-party APIs, build minutes, support, staff time, incident response, account administration and exit/migration. Managed services can lower human operations while increasing usage-based spending; self-hosting can reduce some invoices while raising maintenance and security burden.


FinOps distinguishes estimation, forecasting, budgeting and unit economics; forecasts should be revisited against actuals rather than presented as certain predictions [S14, S15]. A bootstrap can model cost drivers but should not claim current prices without a dated official quote.


~~~text
Illustrative monthly cost model (no prices asserted):
C_total =
  C_fixed_hosting
+ requests × cost_per_request
+ stored_GB_month × storage_rate
+ transferred_GB × egress_rate
+ retained_telemetry_GB × telemetry_rate
+ backups_and_recovery
+ third_party_licenses
+ operator_hours × loaded_hourly_cost


For scenario analysis, calculate low/base/high demand ranges,
including failure and growth cases. Record unknown prices as unknown.
~~~


**Budget guardrails:** Name a billing owner, approved spending ceiling or alert threshold, cancellation/cleanup policy, account and domain ownership, and a review date. An alert is not a hard cap: cloud budgets often notify after spending is incurred. Never activate a paid resource or trial that may auto-renew without explicit authorization.


A useful unit metric might be cost per successfully published portfolio or per accepted API event, but only if the denominator is meaningful and collection respects privacy. Unit economics should connect spending to product value, not encourage reducing quality by hiding failures.


### Operational ownership matrix


| Responsibility | Minimum accountable party | Can an AI agent decide it? |
|---|---|---|
| Domain, DNS and service account custody | Named human/organization | No |
| Release approval | Authorized release owner | No |
| Incident severity and communications | Assigned operator | Propose, not authorize |
| Security/privacy exceptions | Qualified accountable reviewer | No |
| Budget and supplier contracts | Billing/procurement owner | No |
| Backup restore and access review | Operational owner | Plan, not claim execution |
| Telemetry/retention policy | Product + privacy/ops owners | Propose |
| Technical debt and upgrade planning | Maintainer/team | Assist |


For volunteer teams, “24/7 support” is often an unjustified promise. Choose less operationally demanding designs, transparent service expectations and clear escalation rather than assuming constant availability of people.


## 10. Evolution, change and exit strategy


Evolution should be driven by **observed triggers and consequential changes**, not an arbitrary six-month rewrite or an assumption that a growing monolith must become microservices. Relevant triggers include:


- Measured capacity/latency or cost pressure.
- A new tenant, trust or regulatory boundary.
- A third-party API or contract change.
- A platform end-of-life date or security advisory.
- A new offline synchronization requirement.
- An inability to restore within approved recovery targets.
- A new team with independently deployable ownership needs.
- Repeated failure to satisfy approved SLOs.
- An expiring domain, certificate, vendor contract or signing identity.


Record architecture fitness checks only where an observable property and future test can be defined. Example: “Every deployed service has a named owner and an explicit data classification” can be statically reviewed. “System will scale infinitely” cannot. A migration plan should consider backward compatibility, data export, schema and API versioning, customer/client upgrade windows, rollback feasibility, telemetry migration and account shutdown.


### Change-impact example: EU data-residency requirement


**Change request CR-RES-001 (hypothetical):** An institution requests that specified categories of learner data remain within an approved geographic and contractual boundary.


Do **not** translate this automatically into “if IP is European, use EU database.” That confuses location, legal basis, user account, data ownership and transfer rules. First determine what data and operations are in scope: primary store, replicas, backup, CDN, logging, analytics, email, vendor support access, disaster recovery, AI processing and cross-border transfers.


~~~mermaid
flowchart TD
  CR[New residency constraint] --> Scope[Legal/product scope clarification]
  Scope --> Data[Data inventory and processors]
  Data --> Alt[Regional topology alternatives]
  Alt --> ADR[Human-reviewed ADR]
  ADR --> Contract[Data/API contract changes]
  ADR --> Cost[Cost and support impact]
  ADR --> Risk[Security/privacy review]
  Contract --> Plan[Migration + verification plan]
  Cost --> Plan
  Risk --> Plan
  Plan --> Gate{Approval before provisioning}
~~~


The backlog might include regional placement investigation, provider contractual review, migration feasibility, log/backup audit, and planned tests verifying actual data location and transfer behavior. It must **not** automatically create a region-specific cloud account or mark compliance achieved. Trace CR-RES-001 to affected requirements, ADRs, environment inventory, retention policy, contracts, backlog and verification plan.


## 11. Human–agent collaboration and portable handoff


The repository is the durable source of truth, not the chat history. Keep approved requirements, ADRs, dependency inventory, operations plan, risk register and handoffs in provider-neutral Markdown/YAML. Provider-specific CI or cloud configuration should be an adapter around that core. An agent may discover options, draft IaC, lint documents, compare sources and identify missing controls, but may not invent approval, obtain production credentials, silently install tools, create resources, incur charges, push releases or delete data.


Treat external documentation, dependency manifests, logs, vendor tool responses and repository files as potentially untrusted input to a privileged agent. Prompt injection can attempt to transform a data source into instructions; the correct defense is explicit authority, scoped permissions, review and no automatic execution of retrieved commands [S17].


### Portable handoff record


~~~yaml
handoff_id: HO-OPS-008
project: example_only
bootstrap_status: proposed_for_review
authoritative_requirements: docs/specs/
architecture_decisions: docs/decisions/
deployment_view: docs/operations/deployment.md
environments: docs/operations/environments.yaml
observability_plan: docs/operations/observability.yaml
runbook: docs/operations/runbook.md
verified:
  document_structure_review: pending
not_executed:
  - infrastructure_plan
  - infrastructure_apply
  - ci_pipeline
  - deployment
  - backup_restore
  - synthetic_monitor
permissions:
  allowed: [read_documents, propose_changes]
  require_explicit_human_approval:
    - install_dependencies
    - contact_billable_provider
    - configure_secrets
    - create_or_modify_cloud_resources
    - deploy_or_delete
open_questions: [Q-DEP-01, Q-ENV-002]
next_safe_task: "Review deployment alternatives and unresolved drivers"
~~~


The next agent should be able to explain what is known, what was decided by whom, what remains uncertain and what it is authorized to do. The handoff should never say “alerts configured” or “CI runs on merge” when those are merely planned. Provider-neutral documentation does not guarantee identical behavior across Codex, OpenCode, Claude, Copilot or other agents; adapter behavior and permissions need to be checked in the target environment.


## 12. Worked case A — Solo static portfolio


**Scenario, not an approved project:** One creator publishes public pages and project descriptions. A contact channel is optional; there is no known need for accounts or persistent application data.


**Discovery:** Who owns the domain and content? Are forms needed? Must third-party analytics be avoided? What accessibility and language expectations apply? Is the site static-only? Is the host account owned by the creator or an institution? Which assets are licensed for publication?


**Minimal viable topology:**


~~~mermaid
flowchart LR
    Visitor[Browser] -->|HTTPS| CDN[Static hosting / CDN]
    Creator[Creator] -->|reviewed publish| Repo[Source repository]
    Repo -.->|future build/publish| CDN
    Visitor -.->|only if approved| Contact[External form/email service]
~~~


**ADR-PORT-DEP-001 — Proposed, not accepted.** Candidate: static hosting without application server or database. Alternatives: managed web application and self-managed VM. Rationale: lower operational surface when no dynamic protected behavior is required. Consequences: optional contact service creates a new data processor and failure boundary; domain and content backup remain necessary. Revisit if authenticated publishing, user-generated content or server-side workflows become approved requirements.


| Requirement / risk | Planned check | Owner / gate |
|---|---|---|
| Public pages load | Browser smoke + broken-link check | Creator before publication |
| Accessibility | Keyboard/semantic checks against agreed WCAG scope | Creator/reviewer |
| Content privacy | Manual check for secrets, unpublished client material and metadata | Creator |
| Contact form, if used | End-to-end delivery and anti-abuse review | Creator + provider |
| Recovery | Rebuild from independent source copy; domain/DNS recovery checklist | Creator |


**Implementation backlog:** confirm hosting choice and account ownership; record DNS/domain requirements; create publication instructions; define content backup; add lightweight link/accessibility checks; optionally assess a form service and its data policy. No Kubernetes, container registry, distributed tracing, dedicated staging environment or elaborate on-call rotation by default.


**Acceptance examples:** “Given the approved published artifact, when a visitor opens each primary navigation path, the expected public page is accessible.” “Given an authorized publisher, when a bad release is detected, the previous static artifact can be restored using the documented procedure.” Both remain *planned*, not passed.


**Operational risks:** expired domain, broken external links, provider lockout, unauthorized publication, accidental disclosure in assets, form-service failure. A CDN's marketing SLA does not establish a measured SLO for this specific site.


## 13. Worked case B — Hackadō educational portfolio platform


**Scenario, not an approved architecture:** A bootcamp evolves toward a platform where learners publish portfolios, mentors review assigned work and administrators manage cohorts or organizations. Some users might be minors; multi-institution tenancy and scale are not yet confirmed. Do not assume a specific identity provider, cloud, database or legal regime.


**Key unknowns:** age and jurisdiction; public versus private portfolio content; institutional tenancy; mentor delegation; file upload rules; moderation; content ownership; identity federation; deletion/retention; support capacity; expected concurrent activity; budget owner; and whether the first milestone is only a static showcase.


**Candidate initial topology (only if a protected multi-user backend is approved):**


~~~mermaid
flowchart LR
  Student[Student / mentor browser] --> Edge[HTTPS delivery]
  Edge --> App[Single deployable app / modular monolith]
  App --> DB[(Managed relational data)]
  App --> Blob[(Private object storage)]
  App --> IdP[Identity authority]
  Operator[Authorized operator] -.-> App
  App -.-> Obs[Restricted telemetry]
~~~


**ADR-HACK-DEP-001 — Proposed.** Candidate: one managed deployable application with a relational store and isolated file storage. Alternatives: static-only first milestone; serverless composition; multiple independently deployed services. Rationale: reduce operational burden while retaining domain boundaries. Explicitly *defer* Kubernetes, multi-region and microservice decomposition until a requirement or evidence justifies them. Do not treat managed PostgreSQL, Node.js, AWS or any other vendor as already selected.


**Security/privacy drivers:** cohort/tenant authorization; protected uploads; public/private content transitions; account and content deletion; vendor access; accessibility; moderation; auditability where warranted. If minors are involved, qualified legal review must establish applicable consent and safeguarding requirements. Administrative MFA may be an appropriate candidate control; its actual scope and mechanism require approval.


| Failure or change | Operational question | Planned evidence |
|---|---|---|
| Mentor reads another cohort | Can tenant boundaries be bypassed? | Negative authorization tests and security review |
| Upload is malicious/oversized | Can unsafe content reach users or exhaust storage? | File-validation and isolation tests |
| Identity provider unavailable | Can users be informed safely? | Dependency-failure exercise |
| Data accidentally deleted | Can records be restored within approved loss window? | Restore rehearsal |
| Publishing release regresses | Can deployment be mitigated without corrupting data? | Migration/rollback rehearsal |
| Student asks for deletion | Which stores, backups, logs and processors are affected? | Data-lifecycle verification |


**Candidate SLIs (no targets assigned):** successful publish attempts; authorized mentor review completion; denied cross-cohort access events; file-processing failures; critical journey latency. Per-role telemetry should use bounded categories rather than student identifiers as metric labels. An initial volunteer-operated service may deliberately have modest support expectations.


**Backlog:** decide v1 boundary; classify data; obtain identity/tenancy decisions; create threat model; define upload controls; choose provider and region only after budget/privacy review; write migration and recovery plans; design CI/release gates; plan accessibility and authorization verification; establish ownership and support.


**Acceptance:** A learner can publish according to approved visibility rules; an unassigned mentor cannot retrieve protected learner data; authorized deletion propagates through the agreed data lifecycle. These are requirements and future checks, not observed facts.


**Revisit triggers:** a new institution requiring stronger isolation; measured capacity issue; evidence of operational bottleneck; a new residency constraint; independent team ownership. Growth alone does not prove microservices are necessary.


## 14. Worked case C — Privacy-sensitive API integration service


**Scenario:** A backend receives authorized events or requests, processes sensitive data, calls external vendors and exposes a limited API. Applicability of health, financial or payment regulations remains to be established.


**Key unknowns:** data classification, jurisdictions, vendor terms, request volume, downstream outage behavior, idempotency semantics, retention, audit requirements, support model, RPO/RTO and contractual SLAs.


~~~mermaid
flowchart LR
  Client[Authorized client] -->|TLS| Gateway[API boundary]
  Gateway --> Service[Service runtime]
  Service --> DB[(Restricted persistent store)]
  Service --> Queue[(Optional durable queue)]
  Queue --> Worker[Optional worker]
  Worker --> Vendor[Third-party API]
  Service --> Vendor
  Service -.-> Telemetry[Redacted operational signals]
~~~


The queue/worker are conditional: they become useful when delivery semantics, rate limits or durable retries demand asynchronous work. The diagram does not require Kubernetes, Redis or a particular cloud.


**ADR-API-DEP-001 — Proposed.** Candidate: managed service runtime plus encrypted, access-controlled storage, with an optional durable queue. Alternatives: functions, managed containers, VMs, Kubernetes. Select according to isolation, supported protocols, operations, data residency, throughput and economics. **Do not declare managed Kubernetes chosen solely because the data is sensitive.** A simpler managed platform may meet the same controls with lower operational risk.


**Critical invariants:** no unapproved data disclosure; idempotent or explicitly reconciled external side effects; bounded retry and rate-limit handling; authenticated service-to-service access; recoverable event processing; deletion and retention consistent with contracts. The API contract should identify errors, timeouts, duplicate delivery and version compatibility.


| Risk | Planned mitigation | Future verification |
|---|---|---|
| Vendor timeout after side effect | Idempotency key and reconciliation strategy | Fault-injection integration test |
| Provider API changes | Contract version monitoring and adapter boundary | Contract tests |
| Sensitive data in logs | Redaction and allowlisted telemetry schema | Log inspection |
| Secret leakage | Scoped identities and secret-manager policy | Access/config review |
| Regional transfer violation | Processor/backup/telemetry inventory | Legal and data-flow audit |
| Vendor outage | Bounded queue/retry or degraded response | Recovery exercise |


**Candidate SLIs:** successful eligible requests, age of oldest unprocessed event, duplicate-side-effect count, vendor error classification. **SLOs remain unapproved** until stakeholder impact, baseline and cost are understood. No claim of HIPAA compliance, PCI compliance or provider certification is made.


**Backlog:** determine legal/data scope; vendor contracts and credential model; idempotency contract; storage/retention; deployment options; threat model; synthetic fixtures; release and migration strategy; audit/event logging; cost forecast; disaster recovery. High-risk controls should be review gates before real processing, not silently left to “later”.


**Acceptance:** Duplicate delivery produces no additional unauthorized side effect; vendor unavailability does not cause unbounded retries; sensitive request bodies do not appear in routine logs; recovery meets an *approved* RPO/RTO. None are tested at bootstrap.


## 15. Worked case D — Offline-first client, mobile or embedded


**Scenario:** A mobile/desktop application or connected device continues to function while disconnected and synchronizes when connectivity returns. Mobile app stores, desktop packages and firmware OTA have different trust and release mechanisms; they must not be collapsed into a single “deploy to cloud” pattern.


**Key unknowns:** platform and hardware, local data sensitivity, conflict semantics, identity while offline, maximum offline duration, update/signing process, storage limits, battery/power-loss behavior, device ownership and recovery from lost devices.


~~~mermaid
flowchart LR
  subgraph Device
    App[Local application] --> Local[(Local durable state)]
    App --> Outbox[Pending operations]
  end
  Outbox -.->|when connected| Sync[Versioned sync boundary]
  Sync --> Server[(Server-side state, if required)]
  Release[Signed update channel] -.->|phased rollout| App
~~~


**ADR-OFF-DEP-001 — Proposed.** Candidate: local-first data authority for disconnected edits with an explicit sync protocol if shared state is required. Alternatives: read-only offline cache; manual export/import; periodic API sync; peer-to-peer sync. Select based on collaboration, consistency and device constraints. “Last write wins” is a consequential conflict policy, not a harmless default.


**Release model:** signed mobile/desktop packages or firmware images where platform requires; staged distribution; rollback/anti-rollback rules appropriate to the threat model; compatibility window for older clients; safe handling of interrupted updates. For firmware, power-loss and hardware-specific recovery may be safety-relevant. A cloud rollback cannot instantly remove a faulty client binary already installed on devices.


| Risk | Planned evidence |
|---|---|
| Edit lost during offline period | Local persistence tests and device restart scenarios |
| Duplicate or reordered sync | Idempotency/state-machine tests |
| Conflicting edits | Approved merge policy and adversarial examples |
| Older client meets new server | Compatibility contract tests |
| Interrupted upgrade | Recovery/rollback or safe-failure rehearsal |
| Lost/stolen device | Local encryption, token revocation and data-handling review |
| Telemetry while offline | Local retention, consent, delayed upload and privacy review |


**Backlog:** classify on-device data; choose conflict semantics; define sync protocol/versioning; identify signing custody; plan device/store accounts and costs; establish update/recovery policy; design tests for offline duration and migration; select minimal privacy-preserving telemetry. No assumption that a sync backend is needed if the product is entirely local.


**Acceptance:** An edit persists across restart while disconnected; re-sending a committed operation does not duplicate effects; a supported old client either syncs compatibly or receives a safe, intelligible upgrade requirement. Future tests must supply execution evidence.


### Cross-case comparison


| Concern | Static portfolio | Hackadō platform | Sensitive API | Offline client |
|---|---|---|---|---|
| Main distribution | Static publish | Managed web release | Service artifact | Signed client/device update |
| Most important boundary | Public content/form vendor | Identity, cohorts, uploads | Data/vendor credentials | Local state/sync/signing |
| Observability minimum | Synthetic availability + broken links | Publish journey + auth failures | Queue/vendor/idempotency | Sync failures + client health |
| Recovery focus | Restore source/DNS/publish | Data restore + migration | Replay/reconciliation + backups | Local recovery + version compatibility |
| Typical escalation | Form/privacy processing | Multi-tenant security | Regulatory/vendor outage | OTA safety, offline consistency |
| Default to avoid | Kubernetes | Premature microservices | Automatic K8s choice | Assuming instant rollback |


## 16. Reusable, conditional artifact contracts


The goal is not to create a mandatory operations bureaucracy. Generate the smallest set of artifacts that makes the first approved implementation task safe and transferable. A simple static site may need a single operations section in `README.md`; a complex service may justify separate documents. **Implementation-ready** also requires at least one approved-scope, sufficiently specified and genuinely unblocked implementation task plus the verified user-selected Git handoff; a research spike alone is insufficient.


| Artifact | Minimum content | Generate when |
|---|---|---|
| `docs/operations/deployment.md` | Deployment view, trust boundaries, dependency inventory, open decisions | Any nontrivial runtime/distribution choice |
| `docs/operations/environments.yaml` | Environment purpose, data class, isolation, credential source | Multiple environments or secrets |
| `docs/operations/release.md` | Build artifact, promotion, approval, rollback/forward fix | Deployable app or distributed client |
| `docs/operations/observability.yaml` | Questions, candidate signals, privacy, owner, unapproved targets | Operated service or monitored client |
| `docs/operations/recovery.md` | Failure modes, RPO/RTO questions, backup/restore ownership | Durable data or critical availability |
| `docs/operations/runbook.md` | Symptoms, diagnosis, safe actions, escalation | Human operator must respond to incidents |
| `docs/operations/costs.md` | Demand assumptions, pricing sources, budget owner, exit costs | Any paid/usage-based dependency |
| `docs/decisions/ADR-*.md` | Alternatives, rationale, trade-offs, owner, revisit trigger | Consequential deployment choice |
| `docs/verification/operations-plan.md` | Planned checks, environments, evidence expectations | Verification spans release/operations |
| `AGENTS.md` | Compact first-read authority, safety and handoff router | Agent-assisted repository |
| `docs/PROJECT_CONVENTIONS.md` | Governing repository contract and documented project exceptions | Every generated project |
| `docs/BACKLOG.md` | Implementation tasks and blocked questions with trace links | Every implementation handoff |


**Minimum deployment decision template:**


~~~markdown
# ADR-DEP-NNN — Deployment substrate


Status: PROPOSED
Decision owner:
Date / evidence as of:
Requirements and quality scenarios:
Hard constraints:
Assumptions and confidence:
Alternatives (including do-less / defer):
Comparison: cost, security, operability, portability, recovery
Decision / explicit deferral:
Consequences and reversibility:
Data residency and supplier dependencies:
Verification planned:
Open questions and gates:
Revisit triggers:
Primary sources:
~~~


**Minimal deployment view contract:**


~~~yaml
deployment_view:
  status: proposed
  approved_by: null
  execution_units: []
  public_endpoints: []
  private_data_stores: []
  external_processors: []
  trust_boundaries: []
  data_classes: []
  network_protocols: []
  secret_names_only: []
  failure_domains: []
  environment_variants: []
  cost_owner: TBD
  evidence:
    infrastructure_provisioned: false
    deployment_executed: false
    recovery_rehearsed: false
~~~


**Operational acceptance matrix:**


| ID | Planned verification | Prerequisite | Status at bootstrap | Evidence after execution |
|---|---|---|---|---|
| OPS-01 | Rebuild artifact from clean source | Approved toolchain | planned | Build log, digest, revision |
| OPS-02 | Deploy to isolated target | Credentials, approved target | blocked | Deployment record |
| OPS-03 | Run user-journey smoke check | Running environment | blocked | Test result and URL |
| OPS-04 | Exercise rollback or forward recovery | Safe migration fixture | planned | Recovery rehearsal |
| OPS-05 | Restore a controlled backup | Backup source and isolated target | planned | Restore report |
| OPS-06 | Verify alert reaches an owner | Monitor and escalation policy | planned | Alert test |
| OPS-07 | Review telemetry for sensitive data | Instrumented service | planned | Privacy inspection |
| OPS-08 | Compare actual spend with forecast | Billing data and owner | planned | Cost variance record |


A `planned` entry must never be relabeled `passed` merely because an agent produced the test case. A `blocked` entry is not a failure if the prerequisite intentionally lies beyond bootstrap scope.


### Traceability and change propagation


~~~mermaid
flowchart LR
  Need[Stakeholder need / constraint] --> Req[Requirement or quality scenario]
  Req --> ADR[Deployment ADR]
  ADR --> View[Topology and environment view]
  ADR --> Task[Backlog item]
  Req --> Check[Planned operational verification]
  Task --> Future[Future implementation / CI]
  Future --> Evidence[Execution evidence]
  Evidence --> Review[Human release/operations decision]
  Change[Change request] --> Req
  Change --> ADR
  Change --> Check
~~~


Use stable identifiers and typed relations. A deployment diagram alone cannot reveal whether a new data-retention rule affects backups, logs, third-party services and the restore procedure; trace links and human impact review are required.


## 17. Pilot design: test the methodology, not its rhetoric


A v0.1 pilot should test whether deployment/operations questions improve implementation handoff **without imposing disproportionate documentation or infrastructure**. It should not claim to establish causality from a handful of projects.


**Contrasting cases:** (A) solo static portfolio; (B) Hackadō-like multi-user platform; (C) privacy-sensitive API integration; (D) offline-first client or embedded project. If only two pilots are feasible initially, select cases with sharply different operational risk. Each should begin from comparable informal intent and record what was known before the bootstrap.


**Measures and observations:**


| Measure | Operational definition | Failure signal |
|---|---|---|
| Time to implementation-ready handoff | Elapsed effort to approved spec + first task | More time without reduced uncertainty |
| Unresolved high-impact questions | Count and severity, with owner and gate | Important issues hidden or silently assumed |
| Handoff reconstruction | New human/agent explains topology, permissions and next task | Requires prior chat or invented facts |
| Unnecessary artifact burden | Files/steps unused during actual development | Static portfolio gets enterprise ops stack |
| Reversibility | Can a reviewer explain exit/rollback implications? | Cloud choice recorded without migration path |
| Verification honesty | Planned/executed/passed statuses match evidence | Generated CI mistaken for green CI |
| Cost reasoning | Estimates with dated assumptions; later variance | “Free forever” or missing billable dependency |
| Privacy/security coverage | Relevant trust/data questions surfaced | Student/vendor/telemetry exposure omitted |
| Change-impact completeness | Participants trace a simulated change | Data residency change ignores logs/backups |
| Cross-agent portability | Handoff reproduced in at least two agent tools | Instructions depend on one provider |


**Pilot procedure:** capture the same initial brief; run the bootstrap with explicit timebox; have an independent reviewer attempt the handoff; record clarification count and unresolved risks; perform a *paper* incident or change exercise without deploying production; only later, with authorization, compare the planned controls to actual implementation evidence. Record counterexamples and negative feedback as prominently as successes.


**Falsification criteria:** If the Skill forces staging, Kubernetes, SLO percentages or IaC for a trivial site; invents stakeholder approvals; creates external resources without authorization; misses a sensitive data transfer; or claims checks passed without execution, that pilot is a methodology failure. If an independent agent cannot find the authoritative deployment decision or safe next task, the handoff is incomplete.


A conventional/ad-hoc comparator can be useful but must be matched for project complexity and team experience. Small samples, learning effects and differing implementations limit any causal conclusion. Pilot results should drive revision of question triggers and artifact thresholds, not broad claims that SDD automatically reduces defects.


## 18. Implications for SDD Bootstrap Skill v0.1


The Skill should implement **adaptive deployment discovery**, not a fixed questionnaire or infrastructure generator. The following are proposed rules to test:


1. **Discover runtime shape first.** Ask whether the product is public static content, an operated backend, a distributed client, an embedded device or a hybrid. Do not assume a server.
2. **Elicit consequential constraints.** Data sensitivity, jurisdictions, user roles, offline behavior, budget ownership, service criticality, external dependencies and available operators should determine depth.
3. **Separate fact, hypothesis and decision.** Every topology, SLO, region, vendor, credential and legal obligation must carry provenance, confidence and approval status.
4. **Offer genuine alternatives.** Compare a do-less option with heavier architectures; use explicit veto constraints; avoid “Kubernetes by default” and “microservices as growth plan.”
5. **Create conditional artifacts.** A simple README section can suffice; generate separate operations, recovery and observability files only when they reduce material uncertainty.
6. **Keep operational values unknown until authorized.** No invented 99.9% uptime, 500 ms latency, 1-hour RPO, mandatory 3 environments or arbitrary retention periods.
7. **Design for reversibility.** Record rollback limits, data migration and supplier exit strategy; distinguish software rollback from data recovery.
8. **Treat privacy and telemetry together.** Logs, traces, backups, analytics and vendor support access are data flows, not invisible infrastructure.
9. **Prefer portable knowledge over portable illusion.** Neutral Markdown/ADRs and standards-based contracts support transfer; provider-specific runtime behavior still needs verification. Follow the accepted initial `main` + `dev` Git baseline, use focused topic branches from `dev`, and add `prod*` branches only for justified distinct deployment trees; publication to personal GitHub requires explicit user choice and authorization.
10. **Gate consequential actions.** No resource creation, billing, deployment, secret acquisition, production access, destructive operation or release publication without explicit human approval.
11. **Report evidence states accurately.** Bootstrap can plan and review checks; it cannot assert live monitoring, successful restore, security certification or deployment success.
12. **Hand off a safe first task.** Provide an approved scope, open questions, dependencies, planned verification, permissions and stop conditions.
13. **Revalidate volatile facts.** Pricing, quotas, versions, cloud availability, regulations and provider terms require dated official-source checks at the moment of commitment.
14. **Learn from failures.** Pilot contrasting project types; measure artifact burden, risk discovery, handoff fidelity and false confidence; revise the Skill accordingly.


### Suggested minimal decision sequence


~~~text
Informal idea
  → classify distribution/runtime form
  → identify data, trust, jurisdiction and operations drivers
  → record unknowns with owners and gates
  → compare deployment alternatives proportionately
  → human approve / investigate / defer
  → document deployment view + conditional operational artifacts
  → derive release, recovery, observability and cost questions
  → plan verification and assign authority
  → produce implementation-ready handoff
  → STOP: no real deployment or claim of operational evidence
~~~


**Final assessment:** The original report's scope and four case-study categories are valuable, but its unsupported numerical targets, blanket infrastructure recommendations, nonexistent free-plan examples, hypothetical “approved” ADRs and uncited assertions should not be adopted as Skill policy. This revised research reference replaces those with risk-based decisions, source-linked knowledge, explicit uncertainty, realistic human authority and honest readiness states. It is a **reviewed research input**, not an independently approved methodology policy or a production-readiness claim; the accepted Project Conventions govern actual bootstrap decisions.


## 19. Annotated primary sources and maintenance watchlist


The links below are primary specifications, standards, official guidance or vendor documentation. They support concepts and correct specific claims; they do **not** prove the project-specific choices in illustrative cases. Accessed or reviewed for this edition in November 2026 where indicated. Recheck volatile items when the Skill is used.


- **[S01] ISO/IEC/IEEE 42010:2022**, architecture description, stakeholders, views and concerns. https://www.iso.org/standard/74393.html
- **[S02] Google SRE Workbook**, implementing service-level objectives and separating user indicators from targets. https://sre.google/workbook/implementing-slos/
- **[S03] Google SRE Workbook**, alerting on SLOs, error-budget burn rates and low-traffic caveats. https://sre.google/workbook/alerting-on-slos/
- **[S04] OpenTelemetry**, official signals and logging concepts; metrics/logs/traces are signal families, not a mandatory tooling stack. https://opentelemetry.io/docs/concepts/signals/ and https://opentelemetry.io/docs/concepts/signals/logs/
- **[S05] NIST SP 800-218**, Secure Software Development Framework 1.1 (published final); risk-oriented secure-development baseline. https://csrc.nist.gov/pubs/sp/800/218/final
- **[S06] NIST Cybersecurity Framework 2.0**, Govern, Identify, Protect, Detect, Respond, Recover. https://www.nist.gov/cyberframework
- **[S07] SLSA 1.2**, approved Build and Source tracks and provenance levels; distinguish current release from future drafts. https://slsa.dev/spec/v1.2/
- **[S08] Sigstore**, signing and artifact-verification ecosystem; apply only when a suitable trust/verification model is defined. https://docs.sigstore.dev/
- **[S09] OWASP ASVS and API Security**, structured verification requirements and API-specific risk categories. https://asvs.owasp.org/ and https://owasp.org/API-Security/editions/2023/en/0x00-header/
- **[S10] GitHub Actions**, official secure-use guidance on token permissions, action pinning and untrusted code. https://docs.github.com/en/actions/reference/security/secure-use
- **[S11] EU GDPR**, Regulation (EU) 2016/679; application and transfer questions require contextual interpretation. https://eur-lex.europa.eu/eli/reg/2016/679/oj
- **[S12] US HHS**, guidance on HIPAA and cloud computing, including cloud-provider business associate agreements. https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html
- **[S13] W3C Trace Context**, standardized distributed-trace propagation; review information exposure across trust boundaries. https://www.w3.org/TR/trace-context/
- **[S14] FinOps Foundation**, forecasting capability, assumptions and variance review. https://www.finops.org/framework/capabilities/forecasting/
- **[S15] FinOps Foundation**, unit economics and linking technology cost to value. https://www.finops.org/framework/capabilities/unit-economics/
- **[S16] Terraform and OpenTofu official docs**, IaC language/state concepts and separate project governance. https://developer.hashicorp.com/terraform/language and https://opentofu.org/docs/
- **[S17] OWASP GenAI Security Project**, LLM prompt-injection and tool-use risks; apply scoped permissions and human gates. https://genai.owasp.org/llm-top-10/
- **[S18] Heroku Help**, removal of free dynos and free data plans in November 2022; corrects an obsolete claim in the source draft. https://help.heroku.com/RSBRUH58/removal-of-heroku-free-product-plans-faq
- **[S19] AWS EC2 official guide**, free-tier differences for accounts created before/after 15 July 2025; provider terms are volatile. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-free-tier-usage.html
- **[S20] Kubernetes documentation**, liveness, readiness and startup probes; relevant only when that platform is chosen. https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/
- **[S21] W3C WCAG 2.2**, accessibility criteria for web systems. https://www.w3.org/TR/WCAG22/
- **[S22] W3C Service Workers**, browser mechanisms relevant to offline-capable web applications. https://www.w3.org/TR/service-workers/
- **[S23] Android Developers**, application signing and release-key management. https://developer.android.com/studio/publish/app-signing
- **[S24] Reproducible Builds**, precise definition of reproducible build artifacts. https://reproducible-builds.org/docs/definition/
- **[S25] OpenSSF**, concise secure software development and dependency-handling guidance. https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software


### Evidence limits and freshness checks


This review cross-checked selected high-impact factual claims against official sources, but did **not** execute infrastructure code, audit every vendor feature, validate all links by HTTP status, or provide a legal opinion. The bibliography intentionally excludes the original draft's unlinked analogy and blank embedded base64 “microservice topology” image, which did not substantiate the caption. Verify current product prices, plans, licensing, runtime compatibility, standards revisions, security advisories, provider regions, local legal requirements and organizational policies before a real decision.


### Editorial change log from the Drive draft


| Original issue | Treatment in this revision |
|---|---|
| No accessible bibliographic URLs despite claiming authoritative sourcing | Added annotated official sources with in-text identifiers |
| Uninformative embedded base64 diagram and duplicate caption | Replaced with readable Mermaid deployment views |
| “At least three environments” as a general rule | Replaced with conditional environment profiles |
| Mandatory SBOM/signing/SLSA and IaC even for small projects | Replaced with risk-based assurance tiers and conditional artifacts |
| Heroku free dynos and outdated AWS free-tier statements | Corrected with official vendor guidance |
| “HIPAA-certified cloud services” | Replaced with HHS guidance on applicability, BAAs and safeguards |
| OAuth, OIDC and JWT treated as interchangeable | Distinguished framework, identity layer and token format |
| “Three pillars required” and fixed CPU/latency alerts | Replaced with question-driven, privacy-aware observability |
| Arbitrary SLO, RPO, RTO, retention, multi-AZ and canary values | Recast as unknowns requiring evidence and approval |
| Fictional ADRs marked “Approved” | Changed to explicitly hypothetical/proposed decisions |
| Kubernetes as default for privacy-sensitive API | Replaced with alternatives and operator/cost analysis |
| EU residency inferred from IP address | Replaced with data-flow, processor and legal-scope analysis |
| Generic “restart service” as first response | Replaced with diagnosis, safety and authorization gates |
| Agent handoff claiming CI/alerts already configured | Replaced with truthful planned/executed evidence states |
| Deployment-readiness ambiguity | Clarified implementation-ready versus operational/production-ready |