# Deployment-Aware Architecture  

> **Editorial review — 12 November 2026.** Reviewed deployment guidance for misleading platform absolutes, unqualified cost/compliance claims and evidence-state inflation. Updated the security/configuration and shared-responsibility discussion, and attached primary reference links. A deployment model or configuration in this report remains **proposed**, never provisioned, tested or approved by this research.
*Research Date: 12 November 2026*  

**Evidence taxonomy:** **Established** = supported by an identified primary standard/specification or official platform documentation; **context-dependent practice** = architectural pattern whose trade-offs vary; **proposed SDD heuristic** = unvalidated recommendation for this Skill; **illustrative** = fictional example; **volatile** = pricing, quotas, features or regulatory interpretation requiring current verification. The original draft lacked inline source URLs and used some overgeneralizations; the reference anchors and corrections below make those limits explicit.

## Executive Summary  
A **deployment-aware architecture** is one that explicitly anticipates *how* and *where* a system will run (cloud vs on-prem, infrastructure layout, trust zones, data flows, etc.) during the design phase, without actually performing any deployment. In practice this means capturing deployment constraints, explicit unknowns and proposed choices in architecture documentation and backlog tasks – e.g. noting target environments, infrastructure nodes, security zones, and operational requirements – but **not** provisioning resources or running the system yet. Standards like arc42 and the C4 model include a “Deployment View” for exactly this purpose: to map software containers/components onto hardware, network, and environments. 

Our research finds that the SDD Skill must ensure that deployment decisions (hosting model, distribution method, data residency, CI/CD strategy, etc.) are *considered and documented*, while any execution (e.g. creating cloud resources, publishing to app stores) is explicitly out of scope. For example, AWS emphasizes defining “trust boundaries” before writing policies, and The Twelve-Factor App advocates environment variables for per-deployment configuration, including credentials; this is **one application design convention**, not the only valid secret-management mechanism. Scoped secret managers and platform identity remain relevant. The skill should elicit these requirements (via interview questions) and produce architecture artifacts (Diagrams, ADRs, backlog) reflecting them. This report outlines a comparative analysis of deployment models, a prioritized interview & decision framework, minimal templates (profile/ADRs/backlog), and MVP delivery recommendations. All recommendations are backed by up-to-date sources. 

## Scope and Non-Goals  
- **In Scope:** Identifying and documenting deployment-relevant requirements and decisions: target platforms (web, mobile, desktop, embedded), hosting preferences (cloud, on-prem, edge, offline), environments (dev/test/prod), distribution channels (CDN, app stores, package registries), data location and privacy rules, availability & performance targets, CI/CD approach, and security/service accounts. Producing architectural descriptions (e.g. a Deployment section in ARCHITECTURE.md), ADRs for major choices, and an implementation/backlog plan that includes deployment-preparation tasks (infrastructure as code templates, config templates, etc.), but with dummy placeholders. 

- **Out of Scope:** Executing any deployment or related actions. The skill will *not* create accounts, provision servers, obtain certificates, upload apps, or run any code. It will not assume a particular cloud or force vendor lock-in. It will not generate actual pipelines or secrets; instead it flags what would be needed. The output ZIP is documentation-centric (specs, ADRs, .env.example, backlog), and we will *explicitly* note that no runnable artifact or live deployment is included (per earlier bootstrap findings).  

## Verified Principles and Best Practices  
We first summarize facts and standards that inform a deployment-aware architecture.

- **Architecture Views:** Modern architecture frameworks include deployment documentation. For example, the arc42 template allocates a “Deployment View” section to describe “the technical infrastructure (geographical locations, environments, computers, networks, etc.) and the mapping of software building blocks to that infrastructure”. Likewise, Simon Brown’s C4 model explicitly has a *Deployment Diagram* for each environment (dev, test, prod) showing how containers/components are deployed onto servers, VMs, containers, or cloud services. These guides underscore the need to capture nodes (load balancers, DNS, firewalls), environment differences, and software-hardware mappings in the architecture docs.

- **Deployment vs. Release Cycle:** The software delivery pipeline conceptually breaks into phases (code → build → package → distribute → deploy → run/operate). In our context, we stop at “package/distribute” planning. The skill should plan *how* the build artifact will be packaged (e.g. container image, JAR, mobile bundle) and *where* it will go (artifact repo, container registry, app store), but not perform those steps. For example, Google Cloud notes that any link in the supply chain can be a vulnerability, so we document provenance best practices (e.g. SBOMs, SLSA checks) without actually signing artifacts. In short, **build/package/distribute** steps are included as design tasks; **provision/deploy/operate/observe/decommission** steps are logged as to-do items or plans but not executed.

- **Platform Patterns & Trade-offs:** The choice of deployment model drives architecture trade-offs. Key comparisons (with supporting sources) include:

  | Model                       | Data/State            | Security / Isolation                                      | Portability & Ops                                         | Cost & Performance                                    | Example Fit              |
  |-----------------------------|-----------------------|----------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------|--------------------------|
  | **Static Website (SSG)**    | Essentially no dynamic state; all pages pre-generated. | Very low attack surface (no server-side code); content served from CDN. | Highly portable – can host on any HTTP server or CDN; trivial ops (just upload files, no runtimes). | Very low hosting cost (often free for storage/CDN); extremely fast response due to caching.  | Personal blogs, docs, portfolios. |
  | **SSR/Hybrid Web App**      | Server renders dynamic pages or data; may use cache for static content. | Requires a running server; attack surface includes server and DB. SSL termination needed at server/load-balancer.  | Less portable – needs a compute host or PaaS capable of running app (e.g. Node.js, etc.).  | Higher cost (always-on compute); slower initial load than static (but better UX/SEO). | Content sites needing SEO or per-user views (e.g. Next.js). |
  | **Backend/API Services**    | Stateful (DB) and stateless components; session or token-based auth. | Can use API gateways, mTLS, VPCs. Container/VM/PaaS each have different hardening needs. | Fairly portable if packaged (e.g. container), but chosen stack can tie to infra (DB engine, OS). | Cost depends on hosting: small VPS or PaaS for low load, horizontal scaling for high load. | Microservices, data APIs. |
  | **Platform as a Service**   | E.g. PaaS host (Heroku, App Engine); managed DB. | Provider handles OS/patching; user sets config/roles. Shared responsibility applies. | Abstracts away infra details – only app code and config matters. Portability is limited by proprietary PaaS (unless similar offerings exist). | Predictable: pay for reserved dynos/instances or flat fees. Less operational burden (CI/CD often built-in). | Web apps, small teams wanting ease (e.g. proof-of-concept app). |
  | **Containers (Docker/K8s)** | Image contains runtime and app; external state in managed services. | Good isolation (namespaces, cgroups), but you must patch base images and host OS. Security of container runtime and images is your responsibility. | Highly portable across hosts; can emulate prod environment locally. Requires orchestration (orchestration may lock to K8s/ECS). | Moderate ops overhead (managing cluster, updates). Can be cost-effective at scale. | Modern microservices, polyglot stacks, lift-and-shift monoliths. |
  | **Serverless / FaaS**       | Stateless functions, state in external storage. | Provider abstracts servers – reduced OS burden. Focus shifts to code security and IAM roles. Careful with least-privilege roles to avoid escalations. | Tied to provider runtime (e.g. Lambda, Cloud Functions); code is portable but tooling differs. Cold-start latency to consider. | Usage-based pricing is common, but requests, duration, storage, networking, minimums and related services can all cost money; verify the chosen provider’s current terms. Reduced server administration, but nontrivial identity, observability, quotas, failure handling, and cost management. | Event-driven tasks, asynchronous processing, spiky APIs. |
  | **Virtual Machines (VM/VPS)** | Entire OS per instance; full state control. | Strong isolation (hypervisor level), OS security patches needed, firewall management.  | Less portable (images tied to hypervisor); lengthy startup time. OS + middleware to manage. | Higher baseline cost (instance running continuously) but fully controlled. Good for legacy apps. | Traditional monoliths, lift-and-shift migrations. |
  | **Managed Databases**       | E.g. Cloud SQL, DynamoDB. Provider handles storage nodes and replication. | Responsibility varies by product and service tier: managed patching or backups may exist, but restore testing, access policy, key responsibilities and actual HA guarantees require verification. | Generally highly available; tied to specific engine (lock-in) but minimal ops. | Pricing and total ownership cost vary by workload, availability level, egress, backup and staff effort; no universal cost ranking. | SaaS products, any app requiring reliable DB with minimal ops. |
  | **Self-Managed DB (Self-hosted)** | DB on your VM/cluster. | You manage everything: install, patch, backups, HA. High risk if neglected. | Portable (engine choice) but you shoulder complexity. Complete control. | Lower raw infra cost at scale, but hidden ops cost (maintenance/on-call). | Complex requirements (custom engines, extreme scale) or cost-sensitive at scale. |
  | **On-Premises / Private**  | Entire infrastructure owned by organization. | Full control of network and hardware. May help meet particular network/data-locality constraints, but physical hosting does not itself establish regulatory compliance. | Low portability (must deal with data center hardware). Scaling up requires buying gear. | High upfront capex but can be cheaper long-term for steady workload. Maintenance overhead and risk of underutilization. | Regulated enterprises, legacy systems, education labs without cloud access. |
  | **Edge / IoT**             | Processing near data source (edge servers, gateways). | Data may stay local depending on data flows, telemetry, backups and external integrations; locality alone does not prove privacy compliance. May use localized firewalls/WAFs at edge nodes. | Highly distributed; often tied to specific network or 5G infrastructure. | Very low latency and reduced backbone cost, but requires many devices/machines. | Real-time analytics, IoT (factories, CDN edge for static caching). |
  | **Mobile Apps (iOS/Android)** | Code + local storage on device; state often synced to cloud. | Store distribution commonly requires signing and platform review; enterprise/sideload channels differ. Device encryption and data protection depend on OS, configuration and implementation. | Portability by target OS; separate development for each platform (iOS vs Android). | App stores take revenue cut; developers handle updates/signing. | Consumer or enterprise apps needing offline UI. |
  | **Desktop Apps**           | Installed on user’s machine (Windows, Mac, Linux); may access cloud. | Often signed executables (e.g. Apple notarization, Windows code signing). Local file/network permissions. | Portability requires separate builds per OS; use installers or package managers. | Single purchase or free; update delivery (auto-updater) adds ops. | Productivity tools, games (PC), offline-capable apps. |
  | **CLI/Library Distribution** | Language-specific (PyPI, npm) or OS packages. No runtime server. | Registry transport security does not establish package safety; verify publisher, provenance, dependencies, signing and release controls as appropriate. Developer must avoid secrets in code. | Very portable in principle (works anywhere with the runtime). | Low hosting cost (just a registry); DevOps needed only for releases. | Internal tools, developer libraries, cross-platform utilities. |
  
  *Table: Deployment models, trade-offs, and example scenarios (sources in text).*

- **Insights:** Static/SSG sites can have a small hosting surface, but third-party scripts, forms, build pipelines, DNS and content handling still require security review; server-side functions may exist behind external services. SSR/hybrid models improve UX/SEO at the cost of requiring servers. Containerized apps give portability and control, but shift patching/updates onto you, whereas serverless reduces some host maintenance but leaves identity, data, configuration, dependencies, runtime limits, observability, cost and supplier risk. PaaS is a middle ground with managed environments but less flexible than raw containers. On-prem offers full data control but sacrifices elasticity and adds hardware overhead. Edge computing dramatically reduces latency and can improve compliance by keeping data local, but at complexity of many distributed nodes. Mobile/desktop packaging introduces unique distribution and signing requirements (app stores, package managers, OS policies). 

- **Quality Attributes:** Deployment choices drive key ISO/IEC 25010 quality attributes. For example, **performance** and latency needs (fast user response) may push toward CDN/edge or global cloud regions. **Availability/Reliability** needs (SLA, RTO/RPO) push toward multi-region/multi-AZ architectures and managed HA services. **Portability/Maintainability** favor containers or serverless functions with minimal infra assumptions. **Security** demands drive trust boundaries: e.g. run untrusted code in isolated VMs/containers, encrypt data in transit and at rest, and minimize secret exposure (12-Factor config). Zero-trust guidance informs identity and authorization decisions across trust boundaries, but jurisdiction and data-residency constraints are separate legal/contractual questions requiring their own evidence.  

- **Data and Compliance:** Deployment impacts data flow and compliance. Regulated data may create jurisdiction-, role-, contract- and processing-specific obligations. **GDPR does not universally require EU-only hosting, and HIPAA does not universally mandate customer-managed keys or one geographic region.** Record the legal/contractual basis and seek qualified review instead of inferring a single infrastructure control. Multi-tenant SaaS requires strong tenant isolation (AWS recommends building tenant ID into tokens and IAM policies). Off-line or air-gapped scenarios (education labs, remote sites) eliminate reliance on external networks and require bundling all software and documentation with the deliverable. 

- **CI/CD and Supply Chain:** While the skill won’t run CI, architecture must specify CI/CD approach. Best practice (12-Factor) is to use environment variables or secure vaults for config/secrets; the repo should include a secret-free `.env.example`. The architecture should record risk-proportionate supply-chain plans (dependency inventories, pinning, SBOM/provenance/signing where justified); the bootstrap must not claim such artifacts have been generated or verified. For example, Google’s security team recommends documenting the build process to create authenticated provenance of artifacts (SLSA). All static analysis, dependency scanning, and artifact signing are planned but not executed by the skill.

- **Trust/Authority Boundaries:** Consistent with AWS shared-responsibility, we must delineate what the cloud (or any platform) secures vs. what the application secures. E.g. in IaaS the team owns the OS/config; in serverless the provider owns much of the stack. The skill should capture these boundaries in architecture diagrams/ADRs: e.g. noting that “Amazon manages RDS OS patching” versus “we must configure DB user roles and KMS keys”. During discovery, the skill must identify who (human) owns each realm: who has the keys to the AWS account? Who is responsible for network ACLs vs app logic? These role delineations are crucial for secure deployment planning.

## Deployment Interview Questionnaire  
To elicit deployment requirements without overwhelming the user, questions are organized by priority. Critical topics have a “must-know” tag; others are optional based on project context.

- **Stakeholder & Product Context (Must):**  
  - *Target users/region:* Where will users be located? (e.g. EU-only, global)  
  - *Distribution channel:* How is the product delivered? (Web app, mobile app store, embedded device, etc.)  
  - *Deployment ownership:* Are there existing cloud or data center accounts/credits? Who controls them?  
  - *Deployment Model Preference:* Any constraint (e.g. “we have an Azure account” or “no cloud allowed”)?  

- **Hosting & Environments (Must):**  
  - *Hosting environment:* Cloud, on-prem, hybrid, edge, or offline? Specific providers or restrictions?  
  - *Deployment environments:* Will there be dev/staging/production? (Environment parity vs cost tradeoff)  
  - *Domain/DNS:* Are domains purchased or need to be? Who manages DNS and TLS certificates?  
  - *Scaling:* Expected load/scale? Need auto-scaling? Vertical or horizontal scaling?  

- **Data & Compliance (High):**  
  - *Data classification:* Any sensitive or regulated data? (PII, health, education, etc.)  
  - *Data residency:* Must data reside in particular geographic locations? (GDPR, local laws)  
  - *Multi-tenancy:* Single organization vs multi-tenant (customer A vs B)? Tenant isolation model?  
  - *Retention & backups:* Required retention period, backup frequency, encryption at rest?  

- **Reliability & Performance (High):**  
  - *Availability targets:* Uptime/SLA expectations? RTO/RPO goals?  
  - *Latency:* Response time requirements (e.g. “real-time” vs “few seconds acceptable”).  
  - *Caching/CDN:* Need CDN or edge caching? Offline support?  

- **Security Model (High):**  
  - *Authentication:* SSO, third-party IDP, custom auth? On-prem AD? OAuth?  
  - *Secrets:* Where will secrets (API keys, DB passwords) be stored or obtained? Vault service? (Do *not* ask for actual values).  
  - *Access control:* Least-privilege policies? Roles for different environments (e.g. separate AWS IAM roles for dev vs prod).  
  - *Incident response:* Are there existing runbooks or contacts for security incidents?  

- **CI/CD & Operations (Medium):**  
  - *CI/CD pipeline:* Preferred tooling (GitHub Actions, GitLab, Jenkins, none)? Manual vs automated deploy?  
  - *Observability:* Metrics, logging, tracing – any requirements for tools or retention?  
  - *Rollback strategy:* Ability to roll back releases (versioned artifacts, database migrations).  
  - *Provisioning:* Will infra be IaC (Terraform/ARM) or manual scripted? Known IaC tools or policies?  

- **Budget & Procurement (Medium):**  
  - *Cost limits:* Any fixed budget or billing constraints? Are costs borne by client or by user?  
  - *Accounts/credits:* Who will pay for hosting, domains, certificates?  
  - *Vendor exit:* Is there a plan if switching providers or terminating service?  

- **Team/Skills (Low):**  
  - *Expertise:* Does the team have devops/cloud skills, or is it all new?  
  - *Existing infrastructure:* E.g. corporate VPN, firewalls, container registries already set up?  

Each question should be asked as neutral options (“Cloud or on-prem?”, “Multi-tenant or single-tenant?”) rather than assuming cloud-first. The skill must refrain from requesting any credentials. For example, it can ask *if* an AWS account exists and who owns it, but never solicit actual access keys. Any deferrable question (“Do you have a hosting account? If not, we’ll note it as a prerequisite”) should be marked as backlog. Critical questions (like data sensitivity or legal constraints) should be highlighted so the user knows they must answer or acknowledge them.  

## Deployment Decision Rubric  
Decisions are evaluated as *must-decide*, *defer*, or *out-of-scope* based on impact:  

- **Must-Decide (during bootstrap):** Topology (cloud vs on-prem vs edge), tenancy model (single vs multi), high-level stack (e.g. container vs serverless), compliance regions, CI/CD approach. These affect architecture and backlog. For each such decision, generate an ADR.  
- **Defer (to implementation):** Low-level config (exact instance type, provider-specific networking rules), fine-tuning (performance vs cost trade-off), or specific service offerings unless they drive architecture (e.g. choosing AWS RDS vs Azure SQL might be deferred until a provider is chosen).  
- **Out-of-Scope:** Actually obtaining credentials or provisioning. **Do not** spin up servers, buy domains, or write deploy scripts. Also do not fabricate numeric targets like “99.9% availability” – rather record that the user should specify them in development.  

For example, choosing to store secrets in AWS Secrets Manager vs HashiCorp Vault can be noted as an option but the skill should not create any vault instance – that’s deferred. Similarly, actual database migration scripts are noted as backlog tasks, not built now.  

## Delivery Models and Topologies  
We classify deployment topologies as a key architecture driver. The *system context view* should outline all external endpoints and services (users, browsers, devices, 3rd-party APIs, etc.). A *C4 container view* or *component view* shows the runtime containers/applications. A *deployment view* (arc42 Sec.7) shows physical/logical nodes, e.g. load balancers, VMs, PaaS services, networks, and the mapping of containers onto them. Trust zones (public Internet, DMZ, corporate intranet) should be demarcated. Arrows represent data flows (encrypted channels, etc.).  

Key considerations (to capture in ARCHITECTURE.md and ADRs) include: ingress (firewall or API gateway at front door), egress (outbound internet calls), service boundaries, and where identity is verified (e.g. frontend vs backend). Persistent storage (RDBMS, object store) and its failure domains should appear (e.g. “SQL DB is multi-AZ with daily backups”). Observability endpoints (metrics/log collectors) and their access controls should be noted. For each environment (Dev/Test/Prod), note differences (Prod might require a hardened subnet, while Dev might use a local DB). If offline or air-gapped, the context diagram would exclude external services entirely.  

High-impact decisions should be captured as ADRs. For example: **ADR-001:** “Hosting Model”. It would document the context (“needs to serve 1M global users with <200ms latency” or “must run in EU data centers for GDPR compliance”), the decision (“we will use AWS ECS with ALB”), alternatives considered (serverless Lambdas, on-prem cluster, etc.), and reasoning (e.g. Lambda was ruled out due to cold-start concerns for  high-throughput API). Where vendor claims or features are volatile, the ADR should include the as-of date and footnote any research (e.g. provider price quotes or SLA docs) that influenced the choice.  

## Dev/Test/Prod, Config and Secrets  
Environment parity is a trade-off (development cost vs production fidelity). Best practice is one pipeline that can deploy to multiple environments with just config changes. The Skill should recommend separating config/secrets from code (12‑Factor style). For example, include a `.env.example` listing all required secrets (DB URL, API keys) but with empty values. In ARCHITECTURE.md or an ops section, note how each secret will be provided (e.g. AWS SSM, Kubernetes Secrets) and who will provision them (a named owner).  

Even an MVP should flag essential config management: use environment variables or a secure config store, do not hardcode credentials, and pin or at least record versions of runtime components to avoid drift. Supply-chain integrity (SLSA) steps like generating SBOMs, signing images, and using immutable version tags should be in backlog tasks. For example: “Task: Implement SLSA Level 1 build (scripted builds with provenance).”  

Rollback and migrations: The architecture should outline a strategy (e.g. blue/green deploy, DB migration scripts with rollback plan). The Skill outputs a **fallback plan** entry in ADRs or backlog (e.g. “If deployment fails, revert to previous container image; backups will be restored from snapshots”).

## Data Locality & Compliance Implications  
Deployment choices heavily affect data security and compliance. This research avoids legal advice, but certain design implications are clear. For sensitive data (e.g. student records at Hackadō), prefer encrypting data in transit and at rest, and consider using customer-managed keys. Multi-tenant designs should embed tenant IDs in storage keys or partitions, or use separate databases per tenant if strict isolation is needed. Logs and telemetry must also honor privacy (e.g. not logging PII). If geographic restrictions apply, the stack should support configurable data stores per region and blocking cross-border replication. The architecture doc should mention these controls (encryption at DB, limited VPC endpoints, private networking). 

## Deployment-Related Backlog Tasks  
Even without executing deployment, the roadmap should list concrete tasks for later implementation. For example:
- **Setup/Procure:** “Create [CloudProvider] account; configure billing/roles.” (Priority: high) – dependencies: none.  
- **Infrastructure as Code:** “Draft Terraform templates for networking (VPC, subnets, security groups).” (blocker: cloud account).  
- **CI/CD Pipeline:** “Configure pipeline skeleton (e.g. GitHub Actions) to build and test code; deploy to staging on merge.”  
- **Secrets Management:** “Choose secret store (e.g. AWS Secrets Manager) and create placeholder entries (dev vs prod).”  
- **DNS & Certs:** “Purchase domain and set up DNS records; issue TLS certificate (using Let’s Encrypt or managed CA).”  
- **Database:** “Define database schema migration plan; include rollback script.”  
- **Monitoring:** “Integrate logging/metrics (e.g. CloudWatch, Prometheus); define alert thresholds.”  

Each task should trace back to specific requirements or risks: e.g. “CI/CD task” supports requirement [CI/CD needed] and mitigates [manual deploy risk]. Tasks should be ordered (e.g. “account creation” precedes “Terraform”). This makes the roadmap actionable and transparent.  

## Example Artifacts (Illustrative)  

- **Interview Extract (Q&A):** A sample snippet might look like:  
  ```markdown
  - **Q:** Who will own the cloud/infrastructure accounts?  
    **A:** Alice (DevOps lead) owns the AWS org; no current accounts, needs creation.  
  - **Q:** Will the app handle user login?  
    **A:** Yes, use Google OAuth (no admin password needed on our side).  
  - **Q:** Is any data classified as sensitive?  
    **A:** Yes, student grades are PII; must stay in EU.  
  - **Q:** Are we allowed to auto-scale?  
    **A:** Yes, budget allows up to moderate cloud usage.  
  ```
  This shows how questions and answers are recorded (owners, needs, constraints), without capturing secrets.

- **Deployment Profile (YAML):** A neutral spec outline for the project’s target environment, e.g.:  
  ```yaml
  deployment_profile:
    product_type: web_api
    target_platforms: [web, mobile_web]
    hosting:
      preference: "cloud (AWS)"
      mandatory_residency: ["EU"]
      environments: ["development", "staging", "production"]
    compute: 
      type: "containerized microservices"
    state: 
      database: "PostgreSQL RDS (multi-AZ, backups)"
      cache: "managed Redis"
    scaling: 
      auto_scaling: true
      min_instances: 1
      max_instances: 5
    security:
      trust_boundary: "Cloud VPC"
      tls_termination: "Load balancer"
      secrets_store: "AWS Secrets Manager"
  ```
  This abstractly captures the intentions without binding to exact values.

- **Architecture Section (Deployment Context):** In *ARCHITECTURE.md*, one might include:  
  ```markdown
  ## Deployment Context

  The **hypothetical** system is proposed as a web service; AWS in an approved EU region is **one candidate**, not a project decision. A load balancer (ALB) will terminate HTTPS; traffic passes to containerized app servers (Docker on ECS) in private subnets. Static assets are hosted on S3 + CloudFront (CDN). The database is Amazon RDS (PostgreSQL) in Multi-AZ for high availability; no direct public access. 

  For this **fictional** scenario, three environments are under consideration within a **single approved data region** (specific region and account isolation TBD pending data-location review). Dev will use smaller instance types; staging/production use larger for SLA. Users authenticate via a third-party OAuth (Google), so no user passwords stored.  

  Future considerations (v0.2+): We may add a disaster-recovery region replication, and a private on-prem instance if required by clients.
  ```
  (This would be accompanied by a C4 container diagram and a Deployment diagram as ASCII or image.)

- **ADR Example (Markdown):**  
  ```markdown
  # ADR-003: Hosting/Compute Model  
  **Date:** 2026-11-12 (proposed)  
  **Context:** Must serve a public web API with low latency in EU, scaling to ~1000 QPS. The team has limited Kubernetes experience.  
  **Decision:** Use AWS ECS Fargate (managed containers) for the backend services, with an Application Load Balancer. User authentication is via OAuth (we do not manage identity infra).  
  **Alternatives:** 
  - *AWS Lambda (Serverless):* Automatic scaling but risk of cold-start delays and statelessness. Rejected because the workload is moderately consistent and team prefers containers for local testing.
  - *Kubernetes (EKS):* Full control but higher ops complexity for a small team. 
  **Consequences:** Fargate abstracts server maintenance (no EC2 to patch). We pay per running container task. This proposed choice retains customer responsibility for application/configuration security, dependencies, identity, data, monitoring and incident response; exact boundaries depend on service. It also means AWS handles OS and orchestrator layers (shared-responsibility shift).  
  ```
  
- **Secrets/Accounts Table:**  
  ```markdown
  | Resource            | Owner  | Purpose                      | Status           |
  |---------------------|--------|------------------------------|------------------|
  | Cloud account administrator | `TBD human owner` | Billing and IAM governance | **Not created; authorization pending** |
  | Domain (`example.com` placeholder) | `TBD` | Public address | Ownership unverified |
  | TLS certificate     | `TBD`  | HTTPS transport              | Issuance method undecided |
  | DB Admin Password   | N/A    | (will use AWS IAM auth)      | *Not stored here*|
  | OAuth Client Secret | N/A    | External (Google OAuth)      | *Not in repo*    |
  ```
  (Note: sensitive values are blank; we indicate storage/ownership only.)

- **Backlog (Markdown with tasks):**  
  ```markdown
  - [ ] **Create AWS account** (owner: Alice; priority: high; depends: none)  
  - [ ] **Configure DNS** for example.com (owner: Bob; priority: high; depends: domain ownership)  
  - [ ] **Setup VPC and Subnets** (IaC via Terraform; owner: DevOps; depends: AWS account)  
  - [ ] **Initialize Docker images** and push to container registry (owner: Team; priority: medium)  
  - [ ] **Draft CI workflow**: lint, build, test, deploy to dev cluster (owner: DevOps; priority: medium)  
  - [ ] **Configure AWS Secrets Manager** entries for DB credentials (owner: Security; depends: AWS account)  
  - [ ] **Design rollback plan** and include in runbook (owner: Team; priority: medium)  
  - [ ] **Enable monitoring** (CloudWatch alarms, ELK) (owner: Ops; depends: prod deployment)  
  ```
  
- **Handoff Summary:**  
  ```markdown
  # Handoff Summary  
  No infrastructure has been deployed in this bootstrap phase. The ZIP contains architecture docs, ADRs, and a prioritized backlog outlining all deployment-related tasks.  Next steps (in development phase) include: provisioning accounts (AWS, DNS), implementing CI/CD pipelines, setting up Kubernetes/ECS environments, and configuring data migrations. Once implemented, staging and production deployments will follow the documented plan.
  ```

- **Verification/Acceptance Checklist:**  
  ```markdown
  - [ ] **Architecture includes deployment view:** Deployment topology and trust zones are documented in ARCHITECTURE.md.  
  - [ ] **ADRs for major deployment choices:** e.g. compute model, database hosting, multi-tenancy.  
  - [ ] **Interview records captured:** Key answers (environments, accounts, security requirements) are recorded.  
  - [ ] **Secrets absent in repo:** `.env.example` present; no real secret values committed.  
  - [ ] **Backlog contains deployment tasks:** All critical infrastructure tasks appear with owners and dependencies.  
  - [ ] **No deployment actions performed:** Confirm the skill did not call any cloud API or require credentials.  
  ```

## MVP v0.1 Recommendations & v0.2+ Deferrals  
For a minimal v0.1 Skill, focus on the most common web/service use-cases with lean features:

- **Core v0.1:**  
  - Include a **Deployment** section in ARCHITECTURE.md (consolidating infra context).  
  - A basic interview tree covering cloud/on-prem, environment count, basic security (dev/prod isolation, top-level data class).  
  - Generate ADR stubs for “Hosting model” and “Data management”.  
  - A template `.env.example` and secrets table without values.  
  - Actionable tasks for account setup, DNS, container image prep.  
  - A single environment model (dev vs prod) – multi-region or advanced DR deferrable.  
  - Skip embedded/mobile/disconnected specifics unless the product explicitly requires it.  

- **Deferred to v0.2+:**  
  - Native integration of edge/CDN or IoT topology questions.  
  - Detailed multi-region or hybrid-cloud planning (e.g. AWS+Azure).  
  - Vendor-specific manifest templates (skip actual Terraform/Azure ARM examples unless user chooses it).  
  - Automated cost estimation (just note “check pricing” without computing actual costs).  
  - Sophisticated threat modeling beyond trust zones.  

**Pilot Evaluation Matrix (Example):** In pilot tests, the Skill should be evaluated on scenarios such as:
- *Static portfolio site:* Confirm it suggests a basic web host/CDN, notes “no dynamic backend” and minimal tasks.  
- *API with private data:* Check it flags TLS, data-at-rest encryption, and deployment of a DB with restricted access.  
- *Education platform (Hackadō-like):* Verify it addresses multi-user isolation, student data privacy, and recommends staging/production dev cycles.  
- *Mobile app requiring signing:* See if it asks about app stores and code signing (e.g. recommending Fastlane or store enrollments).  
- *Desktop/offline app:* Ensure it covers standalone packaging (e.g. creating an installer) and no reliance on cloud.  
- *Non-profit with no cloud account:* The Skill should offer local VM/hosting alternatives and not insist on cloud.  
- *On-prem regulated environment:* It should emphasize physical security, network segmentation, and compliance gates.  
- *Unknown jurisdiction:* It should point out uncertainties (e.g. data may cross borders) and flag it as risk to clarify later.  
- *Sudden vendor switch:* Ensure ADRs consider portability (e.g. using Docker images to ease switching).  
- *No deployment preference:* The Skill should recommend a default (e.g. portable containers on a common cloud) while allowing the user to override.  
- *Budget shock:* If user mentions cost limits, see if the Skill downshifts to simpler options (static hosting, serverless) and flags manual scaling.  
- *Security incident readiness:* Test if it adds backlog tasks for incident management (e.g. include S3 public-bucket check, patch cycles).  

Metrics for success include: completeness of documented decisions, correctness (no forbidden actions), and user confidence (does the user feel guided to “where to start”).

## Risks, Limitations, Open Issues  
- **Scope Creep:** There is tension between guiding the user and taking over decisions. We must not “overwrite” human choices. For example, the Skill should *suggest* CI/CD steps but not assume the user will use GitHub or AWS specifically – humans may have corporate policies.  
- **Incomplete Info:** The Skill relies on user answers. If key data (e.g. target scale or compliance needs) is unknown, it should note assumptions as risks (“Assuming low traffic” or “Compliance jurisdiction and data obligations: UNKNOWN; review before binding deployment choices”).  
- **Provider Volatility:** Cloud offerings and prices change rapidly. The skill should cite current info with date, and possibly warn “as of Nov 2026” if using any specific numbers.  
- **Security/Injection:** The assistant itself must guard against prompt injections. It should not accept or produce real secrets. Any code example must sanitize placeholders.  
- **Trust in AI:** Users may overestimate automation. We must clearly say “this is a plan; human review needed”.  
- **Complexity for Tiny Projects:** The interview must avoid overwhelming very small teams. Risk of “analysis paralysis” is mitigated by marking some questions as optional and suggesting simple defaults (e.g. “choose the least complex topology that satisfies confirmed residency, resilience, and legal constraints”).  
- **Next Steps:** Collaboratively decide on open policies: e.g. “Should the skill insist on picking a provider now, or leave it TBD?” (We lean to force a decision if it affects architecture, otherwise record it as open). Likewise for CI vs manual. These governance choices should be configurable.  

## Conclusion  
Deployment-aware design ensures that when implementation begins, the groundwork for hosting, security, and operation is laid. By treating deployment planning as a first-class architecting activity (and codifying it in documentation and backlog), the SDD Skill bridges informal ideas and actual releases. Our findings and templates above provide a source-backed blueprint for incorporating deployment considerations into the bootstrap process, while respecting the constraints (no actual deployment, no secret handling) and priming the project for a smooth handoff to engineers.  

**Sources:** Industry documentation (arc42, C4), tech blogs and wikis on deployment models, and official guidance (AWS shared responsibility, 12-Factor config, Google Cloud security and SLSA). All links accessed Nov 2026, to ensure current validity. Further citations to vendor docs (AWS, Azure, etc.), standards (ISO/IEEE), OWASP, and regulatory sources should be consulted during implementation.

## Editorial Reference Anchors and Corrections (12 November 2026)

Primary and official resources supporting the corrected principles:

- [ISO/IEC/IEEE 42010:2022 — architecture descriptions](https://www.iso.org/standard/74393.html), [C4 model — deployment diagram](https://c4model.com/diagrams/deployment), [arc42 — deployment view](https://docs.arc42.org/section-7/): architecture views explain allocations, boundaries and consequences; they do not themselves provision resources.
- [The Twelve-Factor App — Config](https://12factor.net/config): environment-based configuration is a proposed application convention, not proof that all systems must use this mechanism exclusively.
- [NIST SSDF, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final), [GitHub — Security for GitHub Actions](https://docs.github.com/en/actions/how-tos/secure-your-work), [SLSA build provenance specifications](https://slsa.dev/spec/): risk-based software delivery and supply-chain controls; the report does not claim that any check passed.
- [Google SRE — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [OpenTelemetry documentation](https://opentelemetry.io/docs/): stakeholder-derived SLOs and planned instrumentation, not automatically applicable numerical guarantees.
- [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng): assess actual roles, data flows, transfers, purpose and retention; avoid inferring a blanket EU-region requirement or declaring compliance from a topology diagram.
- [AWS — Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/): provider-versus-customer responsibilities depend on selected services, configurations and contracts.
- [Google Play — target API requirements](https://developer.android.com/google/play/requirements/target-sdk) and [Apple — App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/): distribution obligations are platform-specific and volatile; an offline APK, enterprise installation or store release is not interchangeable.

### Proportional deployment interview — correction

Ask initially: **(1)** Who uses it and where? **(2)** Is it delivered via browser, package/store, device or internal system? **(3)** What data is stored and where may it flow? **(4)** Is it offline or publicly accessible? **(5)** Who owns accounts, costs, permissions and future secrets? **(6)** What happens when it is unavailable or data must be recovered? Branch to tenancy, legal review, RTO/RPO/SLO calibration, environments, signing, CI/CD or incident response only where the problem warrants it. Do **not** ask for credential values, invent numerical targets or choose a cloud provider automatically.

### Handoff gate — proposed, not executed

```yaml
deployment_intent:
  channel: undecided
  hosting_or_distribution_target: undecided
  accounts_and_billing_owner: undecided
  secrets_values_present: false
  infrastructure_provisioned: false
  build_executed: false
  tests_executed: false
  deployment_performed: false
  release_approved: false
  blockers:
    - "Document architecture-affecting target constraints before committing to a runtime."
  next_recheck: "Before implementation of a provider-bound deployment task."
```

**Human decisions still open:** acceptable unresolved target at bootstrap exit; minimum environment count; whether IaC/CI templates are useful; budget authorization threshold; privacy/legal review trigger; and who approves a production release. Do not silently convert these proposals into universal skill policy.
