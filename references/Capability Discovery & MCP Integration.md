# Capability Discovery & MCP Integration  


> **Editorial review — 12 November 2026.** Corrected the major protocol-era error (legacy `initialize` versus modern `server/discover`), removed gRPC as an assumed core transport, separated MCP authorization from URL-mode elicitation, corrected inappropriate trust/permission claims, and removed fictitious test approvals, provider choices and numerical scores. Sources are linked directly, with a planning-only/no-install/no-execute boundary. The illustrative inventory and ownership ledger below must not be read as an actual selection, approval, verified installation or credential state.
*Date: 2026-11-12*  


## Executive Summary  
This report examines how an SDD (Spec-Driven Development) bootstrap skill can find and evaluate external “capabilities” (tools, APIs, services, etc.) to satisfy project requirements, focusing on the Model Context Protocol (MCP) ecosystem.  We define *capability discovery* as the process of matching a validated requirement with available functions or data (tools, resources, prompts, or services) provided by the ecosystem, then planning how to integrate them (or not) into the design.  We survey the current MCP standard (v2026-07-28) and its primitives (tools, resources, prompts, elicitation); review official registries and community directories (MCP Registry, mcpservers.org, mcp.directory, vendor lists); and analyze security, trust and governance issues (drawing on OWASP GenAI guidance).  We propose a vendor-neutral workflow for capability discovery and selection (steps and decision criteria), a taxonomy/schema for cataloging capabilities versus actual tools, decision matrices (build vs. buy vs. integrate), and sample artifact templates (capability inventory, scorecard, integration contract, vetting checklist, ledger, ADRs, backlog entries, verification plan).  Throughout, we highlight worst-case threats (malicious servers, supply-chain attacks, injection) and human-in-the-loop controls.  This report connects to earlier research on knowledge validation, bootstrap planning, and architecture by ensuring discovered capabilities have current documentation, are included in the spec and design, and fit within planned trust boundaries.  


## Scope, Non-Goals, and Methodology  
We focus on discovering *external* capabilities (APIs, data sources, agents, MCP servers, libraries, etc.) relevant to project requirements, deciding if/how to include them in a platform-agnostic design, without actually implementing or deploying them.  The target is a minimal v0.1 MVP bootstrap workflow: identify candidate capabilities, vet them, record decisions and evidence, and produce explicit integration tasks and contracts.  Non-goals include running MCP servers, installing libraries, or executing code. We build on earlier work (#1 knowledge freshness, #2 roadmap, #3 architecture) by treating those reports as context: for example, we assume requirements have been distilled into specifications and initial architectural sketches, and now we map those to capabilities.  


Our methodology is evidence-based: we surveyed official MCP specification sources (the modelcontextprotocol.io site and GitHub, including the released v2026-07-28 spec and SEPs) and third-party documentation (e.g. Anthropic blogs, Google Cloud introductions) to summarize protocol fundamentals. We inventoried MCP ecosystem sources: official *MCP Registry* documentation, community directories (mcpservers.org, mcp.directory), vendor lists, and open-source MCP servers. We reviewed security guidelines (OWASP GenAI top risks, OAuth standards, NIST where available) to build a threat model. We then derived a capability taxonomy, selection rules, and workflow by combining these sources with software integration best practices (e.g. build vs. buy analysis). The original draft lacked standalone citations for many claims; this editorial revision adds verifiable official anchors, downgrades unsupported comparisons to hypotheses, and labels templates as hypothetical. Independent provider testing has not been performed.  


## MCP Fundamentals and Discovery Primitives


The [Model Context Protocol](https://modelcontextprotocol.io/specification/2026-07-28) is an open protocol for exposing contextual data and operations to AI applications. Its core primitives are **tools** (`tools/list`, `tools/call`), **resources** (`resources/list`, `resources/read`) and **prompts** (`prompts/list`, `prompts/get`). A tool definition describes a possible operation; merely listing it is **not permission** to invoke it. Execution permissions, user consent, the provider's actual authorization policy and side-effect controls are separate concerns. [Official architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture).


### MCP protocol eras — significant correction


As of 12 November 2026, the published `2026-07-28` revision is materially different from older revisions. **The legacy protocol through `2025-11-25` uses `initialize` / `notifications/initialized` and session-level version/capability negotiation. The modern `2026-07-28` core removes that initialization handshake and protocol-level sessions; requests carry the required version/client metadata, and `server/discover` provides optional pre-request discovery to clients.** Servers claiming to implement the modern revision must support `server/discover`, but it is incorrect to assert that every MCP server in the ecosystem supports it or that every client must call it on each connection. Older servers may support only the legacy handshake. Official references: [MCP 2026-07-28 release](https://blog.modelcontextprotocol.io/posts/2026-07-28/), [protocol versions in the official TypeScript SDK](https://ts.sdk.modelcontextprotocol.io/v2/protocol-versions), and [official Go SDK discovery guidance](https://go.sdk.modelcontextprotocol.io/protocol/).


The modern discovery response may carry version, feature and cache metadata. Tools/resources/prompts lists can be queried **only after an authorized runtime connection**, not merely because a directory says a server exists. Modern cache hints and change notifications are optional/context-specific, and a cached listing may become stale. **Publication in a registry, modern capability discovery, a working connection, authorization, successful tool calls and production-safe behavior are six different evidence states.** Compatibility is determined by actual host/client/SDK support, not by the latest protocol revision alone.


### Transport, authentication and advanced features


The core transport patterns to evaluate are **stdio** for local subprocesses and **Streamable HTTP** for remote MCP, with protocol-version-specific behavior. **gRPC is not a core MCP transport simply because a custom gateway might use it internally.** Encryption and network authentication must be designed for the chosen transport and execution boundary; TLS/HTTPS is needed for appropriate remote communications and cannot be inferred from a server listing. [MCP transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports).


MCP authorization is not universally required for every local tool or server. **Remote protected-resource integrations may use OAuth**, with the actual client/provider/authorization-server configuration and least-privilege scopes reviewed against current guidance such as [OAuth Security BCP RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) and [issuer identification RFC 9207](https://www.rfc-editor.org/rfc/rfc9207.html). The *URL-mode elicitation* feature is a separate process for sending a user to a third-party authorization or data-entry page; **it is not the same as authorizing a client to access an MCP server**. The skill may document the approval/account owner but must not request or persist tokens, passwords, refresh tokens or live secrets in repository text. [MCP elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation).


Modern MCP also provides multi-round-trip interaction mechanisms and an extensions framework; features such as **sampling** have lifecycle and compatibility caveats (sampling was marked deprecated in the `2026-07-28` specification). No bootstrap should assume that a planned client implements every optional feature. [Sampling status](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling).


### MCP Registry and ecosystem — discovery is not endorsement


The [official MCP Registry](https://modelcontextprotocol.io/registry/about) and its [API documentation](https://registry.modelcontextprotocol.io/docs) provide metadata and publisher-discovery mechanisms, **not a complete security audit, continuous uptime guarantee or automatic authorization**. Publisher-domain or repository identity checks are narrower than establishing that code is safe. Third-party directories such as [mcpservers.org](https://mcpservers.org/) and [mcp.directory](https://mcp.directory/) are leads for further investigation; their labels, popularity counts or sponsored entries do not establish provenance, active maintenance, compatibility or trust. A service may be listed without being installed, configured, available to the target host, or acceptable under the project's data policy.


For each candidate, verify its actual maintainer and source, license, distribution artifact, dependency provenance, change history, permissions, side effects, cost model, service region and supported **client + protocol version + transport** against official provider/repository evidence. Prefer no integration when a local library, manual step or existing trusted runtime capability sufficiently meets the requirement. **During this research/bootstrap, do not connect to, install or invoke candidate servers.**


## Capability Taxonomy and Terminology  
To avoid confusion, we distinguish several concepts:


- **Requirement vs. Capability vs. Implementation:** A *requirement* is a need derived from project goals (e.g. “convert Word to PDF”). A *capability* is a description of a needed function or data, separate from any specific provider or tool (e.g. “access to a document conversion API”). An *implementation* or *tool* is a concrete way to fulfill it (e.g. “LibreOffice command-line”, or “Zamzar conversion API”). In our process, we first record the requirement and then discover what capabilities exist: native (built-in libraries), MCP servers, cloud services, or manual processes.


- **Tool vs. Resource vs. Prompt (MCP terms):** Tools and resources are MCP primitives, as defined earlier. A *tool* is essentially a function that can be invoked (via MCP tools/call). A *resource* is contextual data (via resources/read). A *prompt* is a template to feed the LLM (via prompts/get).  For our taxonomy, we also speak of *connectors* or *adapters*: for example, an “HTTP-connector” MCP server might wrap any REST API as an MCP tool, but the underlying capability is really “REST API call”.  We may list these MCP primitives as **candidate interfaces** in an inventory, without implying that a protocol-exposed operation satisfies a product requirement, is installed, or has been permitted.


- **Provider vs. Protocol:** A *provider* is an entity offering the capability – e.g. Google, Microsoft, or a specific OSS project. The *protocol* (like MCP or REST) is how the agent talks to it. For instance, Google’s Calendar could be accessed via a REST API, via an OpenAI plugin protocol, or via an MCP server that wraps the REST API. The capability is “Manage Calendar”, the provider is Google, and the protocol option might be MCP or direct API. We choose MCP or direct integration (or none) as part of selection rules.


- **Local Skills vs. Network Services:** A “local skill” is code running within the agent’s environment (or on-prem) – e.g. a Python library or shell command. A “network service” is remote (MCP server or HTTP API). Local solutions can reduce network exposure but are **not automatically trusted**: downloaded packages, filesystem/shell permissions, telemetry and supply-chain compromise can still create serious risks. They may require packaging into the project (e.g. bundling an SDK). Conversely, a cloud MCP server offers quick features but introduces trust and cost considerations.


Using this taxonomy, capability *discovery* means: For each requirement or high-level function, enumerate all plausible capability types (build in-house, library, MCP server, third-party API, manual process, etc.), then for each candidate gather metadata (provider, protocol, auth needed, security posture, etc.), score and rank them, and decide one.


## Capability Discovery Workflow  
We propose a structured workflow integrating human and automated steps. Key phases: 


1. **Start from Validated Needs:** Use the confirmed requirements/specifications (from earlier elicitation). For each functional requirement, derive one or more *capability statements* (“We need a service to *send emails*,” “We need *OCR* on PDF attachments,” etc.). 


2. **Inventory Native/Local Options:** Check if the needed function can be met by built-in code or libraries. For example, sending email might be done by an SMTP library (native/API); OCR might use Tesseract locally. Local libraries can reduce some external dependencies but are not intrinsically lower-risk; licensing, maintenance, sandbox permissions and provenance still require evaluation. Record these as potential approaches (build vs. buy decision to come later).


3. **Identify Missing Capabilities:** For unmet needs, consider MCP or external. Ask “is this best handled by a network service?” If so, proceed. Otherwise, mark as “manual” (e.g. admin does it). 


4. **Search Official Docs/Registries:** For each needed capability, search official docs and MCP resources. Start with [official MCP documentation](https://modelcontextprotocol.io/), the [official Registry](https://modelcontextprotocol.io/registry/about), and the named provider’s official documentation; community directories are discovery hints only. The MCP Registry (if matured) or directories can suggest MCP servers. For example, to integrate email, one might check if Gmail or SMTP has an MCP server on mcp.directory. 


5. **Vet Candidate Servers/Services:** For each candidate (MCP server or API), gather metadata:
   - Provider name and domain (who maintains it, e.g. “Acme Corp”).
   - Endpoint/installation link (GitHub URL, Docker image, URL).
   - Documented features and, **later when explicitly authorized**, actual capabilities verified through a compatible legacy `initialize` or modern `server/discover` process plus primitive listing; do not contact a server merely to fill the bootstrap inventory.
   - Compatibility: MCP spec version it supports (e.g. “2026-07-28”), transport (stdio vs HTTP), hosting (self-hostable or remote).
   - Security posture: open-source or closed; any known audits or warnings. E.g., OWASP examples warn about insecure npm MCP packages.
   - Cost/licensing: Open or paid; usage limits; data usage policy.
   - Operational needs: Required credentials or accounts; how to provide secrets (via env var, Google IAM, etc.); how to test it.
   - Trust and maintenance: last updated date; maintainer contacts; incidents (some OWASP WP cited real incidents like malicious “postmark-mcp” packages). 


6. **Assess Alignment and Risk:** Score each candidate on fit vs. requirement, using factors like coverage, security, compliance, cost, and closeness to spec. For example, an unofficial MCP that scrapes a website might work functionally but has high risk. We should have a small decision matrix (see below) weighing:
   - **Functionality:** Does it fully meet the requirement?
   - **Maturity/Trust:** Official vs. community vs. unknown.
   - **Security/Privacy:** Data handling, encryption, isolation.
   - **Maintainability:** Versioning, active support.
   - **Cost/License:** Free vs. paid, usage limits.
   - **Integration Effort:** How much work to plug in (dependencies, etc.).
   - **Fallbacks:** Can we do without it if needed?


7. **Decision (Human in Loop):** For each requirement, present the options to the stakeholders. Capture an ADR (Architectural Decision Record) if needed (e.g. “Evaluate a direct SMS API versus a managed messaging provider; approval pending until requirements, pricing, permissions and contract are verified”). Explicitly defer any uncertain cases to further research or human follow-up. If a capability is not needed (trivial or out-of-scope), document “No Integration – do manually or drop.” No silent assumptions: every integration must be consciously chosen or rejected by a human reviewer.


8. **Record and Plan Integration:** For each approved capability, produce:
   - A *backlog item* (or Spike if needed) describing exactly what to implement (e.g. “Integrate SendGrid for email: verify using SendGrid API key, implement `sendEmail()` method, write unit tests”). Include acceptance criteria (e.g. “Email arrives and contains correct content”). 
   - An *integration contract* or specification: a stub/interface definition (see below).
   - If MCP is chosen, note how to configure the client (which MCP client to use, environment needed).
   - Document any hidden work (e.g. “Set up AWS account and parameter store for secrets”).
   - Update an ADR or NOTES with justification and references.
   - Add to a *verification plan* (protocol conformance tests, security tests, etc.).


9. **Out-of-Loop vs On-Demand Checks:** We plan discovery at bootstrap time (initial planning phase). For example, checking an MCP registry or contacting providers happens now. Once development starts, some checks can be repeated by the dev agents (e.g., fetching the latest OpenAPI specs from a provider nightly). But the bootstrap skill itself only runs at planning time. We can note where ongoing validation is needed later (see Freshness below).


10. **Capability Freshness:** Finally, integrate this with the Knowledge Freshness approach (research #1). For each selected capability, record the source of information and date. E.g. “Official provider endpoint documentation consulted on YYYY-MM-DD; exact version and compatibility still to be confirmed.” Plan periodic reviews or triggers (e.g. “re-verify email send after 6 months or on failure”).  


This workflow is *human-guided*: at each step, the skill asks clarifying questions (e.g. “Is offline operation required?”, “Who will own the account?”). It never automatically enables a service; it only gathers evidence and options. It should explicitly note if the environment is air-gapped (no network, so skip MCP) or if vendor lock-in is to be minimized. 


## Capability vs Tool vs Provider Distinctions  
We must be precise in documentation and templates to separate *what we need* from *what we can use*. For example, consider a requirement “Send email notifications”. We might record:  
- **Requirement ID:** REQ-21 – Send email.  
- **Capability intent:** “Deliver an email to a specified address with given subject/body.”  
- **Candidate providers:** e.g. SendGrid, AWS SES, Gmail, local SMTP server, or an MCP server “EmailMCP” if exists.  
- **Protocol option:** Direct API/SMTP vs. MCP wrapper.  


In the taxonomy record, we’d have fields like “requirementID, description, trust level, data category (sensitive vs public), integration models (API/MCP/local), etc.”. We keep separate columns for the *CAPABILITY* (e.g. “Email sending”) vs *tool/provider* (“SendGrid API” or “SMTP” or “ExampleCorp Email MCP server”). We note that a provider might offer multiple interface models: e.g. Gmail can be accessed via SMTP library, or via an MCP server wrapper. Those are separate rows in our matrix.  


### Example Capability Taxonomy (simplified)


| Req ID | Intent (Need)        | Functional Boundary       | Data Sensitivity | Provider / Tool         | API or MCP | Auth & Secrets            | Side Effects | Notes         |
|--------|----------------------|---------------------------|------------------|-------------------------|------------|---------------------------|--------------|---------------|
| REQ-21 | Send email           | Email to external address | Medium (contact) | SendGrid API           | API (REST) | API Key (owner uses env)  | Write/log    | Official SDK |
|        |                      |                           |                  | SMTP library (internal) | Native     | SMTP creds (owner)        | Write/log    | no external netreq |
|        |                      |                           |                  | “EmailMCP” (hypothetical/unverified) | MCP (HTTP) | Auth design TBD (elicitation is not MCP-client authorization) | Write/log | unvetted 3rd party |
| REQ-37 | Parse PDF documents  | Extract text/images       | Medium (doc)     | Tesseract (local)      | Native     | N/A                       | Read         | Embedded library |
|        |                      |                           |                  | “PDFParseMCP” (hypothetical/unverified)  | MCP (cloud) | Auth TBD                    | Read         | unverified example |
| ...    | ...                  | ...                       | ...              | ...                     | ...        | ...                       | ...          | ...           |


(These records would be stored in a project doc or tool, with unique IDs and references.) 


## Discovery and Selection Decision Criteria  
To guide choices, we establish high-level rules and a decision matrix:


- **Hard vetoes:**  
  - Do **not** use any capability that requires the agent to obtain new, unknown, or secret credentials without human involvement. (e.g. SSHing into user data).  
  - Do **not** integrate any tool with known severe security issues or heavy compliance burdens without mitigation.  
  - If a requirement can be met fully offline or with existing trusted tools, prefer that (avoid complexity of MCP).  
  - For destructive actions (writing data, financial ops), always involve a human confirmation step or use whitelists.  
  - *Never* assume access to a tool just because a planning agent can reach it; actual runtime env may differ.


- **Soft preferences:**  
  - **Native/Local vs. External:** If a maintained local library or built-in feature safely satisfies the requirement with reasonable effort, consider it before adding a remote service; test supply-chain, maintenance and permission exposure rather than assuming local means safe.  
  - **Direct API vs. MCP:** If a robust API/SDK exists (with good docs and offline testability), prefer it. Use MCP only if it notably simplifies multi-platform support or if no direct integration exists.  
  - **MCP wrapper vs API:** Use an MCP wrapper only if you want to expose the capability to *other LLM agents* in a uniform way. If only this application needs it, direct API is simpler.  
  - **Cloud vs. On-prem:** Select from actual data-flow, jurisdiction, confidentiality, operator and contractual constraints; neither on-prem alone nor cloud encryption alone establishes compliance.  
  - **Community vs. Official:** Official/maintained vendors (e.g. Google, AWS) are preferable to random GitHub projects for critical features.  
  - **MCP Registry trust:** Verified publisher metadata is useful provenance evidence, **not** a security approval. Validate published source/artifacts and requested permissions separately.


We can codify a decision matrix with axes like:


| Option Type           | Pros                                     | Cons                                      | When to Use                              |
|-----------------------|------------------------------------------|-------------------------------------------|------------------------------------------|
| **Build in-house**    | Full control, no external dependency     | High dev effort, slow if complex          | Simple/low-risk features, or unique need |
| **Use local SDK**     | Quick dev, no network dependency         | Limited to local environment, updates needed| When available and safe                 |
| **Managed API**       | Maintained by vendor, scalable           | Cost, need auth, vendor lock-in           | Well-known services (e.g. Twilio, SES)   |
| **MCP server (self)** | Standard interface for any agent, local  | Need to run server, manage tokens         | For on-prem data (e.g. internal DB)      |
| **MCP server (cloud)**| No local server to manage when vendor-hosted; client/version support still required      | Security, trust, uptime concerns          | Quick hack or multi-agent sharing        |
| **No integration**    | Zero tech risk, manual fallback          | No automation, user effort                | Rare/irrelevant tasks                    |


The skill should prompt or document which path is chosen and why. For example: *“CAP-99: Evaluate local inference versus a managed sentiment API; provider, pricing, region, permissions and data handling are **undecided**, with an evidence-gathering spike and human review before choosing.”*


## Security and Threat Model  
Integrating external capabilities introduces significant security challenges. We adapt the OWASP GenAI guidance to MCP context, summarizing key threats and mitigations:


- **Prompt Injection via Tools/Data:** If a tool returns data (or metadata) that the agent treats as input, it could be malicious. For example, an MCP server’s response might include unexpected commands or credentials. OWASP notes that LLMs do not distinguish instructions from data; therefore, any third-party content (tools output, documents, issue comments) can carry injected prompts. *Mitigation:* Sanitize and whitelist tool outputs. Do not rely on hidden context. When a tool can affect the agent, require human confirmation or use safe schemas.  


- **Malicious/Compromised MCP Server:** An attacker could publish a fake MCP server (e.g. on npm) that pretends to provide a useful capability but actually steals data or executes arbitrary code. OWASP explicitly warns to “Pin, sign, and verify every MCP server and tool package” as part of supply-chain risk management. We should therefore avoid blindly installing unknown MCP packages. The skill must flag any third-party MCP source and recommend verifying its origin (e.g. check domain identity, use hash pinning, or avoid).  


- **Typosquatting and Impersonation:** Attackers may publish MCP servers with names similar to popular ones. Directory sites list many servers, but inclusion is not endorsement. We must always cross-check registry DNS proofs and be wary of unregistered entries. The skill should encourage developers to search by exact provider (e.g. official domains) and review the actual official repository, package provenance, release signatures and independently reported advisories; WHOIS or star counts are not security evidence.  


- **Excessive Privileges (Confused Deputy):** If an MCP server operates under broad credentials (e.g. a Cloudflare server running with an org’s master API key), it could be tricked into acting on data it shouldn’t. Design principle: grant the MCP server *least privilege* possible. For example, if using a GitHub MCP server to open issues, use narrowly scoped, ideally resource-specific credentials granting only the exact actions needed; a broad GitHub `repo` scope is **not** itself evidence of least privilege. The skill should document required OAuth scopes and urge minimum rights.  


- **Data Exfiltration and Leakage:** Tools typically run in the agent context (so results come back via the LLM’s messages). A malicious tool could return sensitive data or send data externally. Mitigation: treat all tool call results as untrusted. Avoid using powerful tools on private data unless absolutely needed. Plan audit logs **without storing secret or personal payloads**; use bounded telemetry and authorized tests when an implementation exists.  


- **SSR, File, Shell, Network Attacks:** Although MCP is JSON-RPC, underlying tools might do I/O. For example, an MCP server might inadvertently accept user-supplied URLs and fetch them (leading to SSRF). Or a “shell” tool might allow arbitrary commands. The skill should note (in contracts) whether tools are safe vs. dangerous. For any shell or network tool, require explicit user sign-off and limit them to read-only modes if possible.  


- **Dynamic Changes:** An MCP server’s interface might change over time (new tools, changed schemas). We must record the **documented** proposed version and plan for re-verification on updates. Avoid auto-updating tools without review. Capturing an actual `server/discover`/primitive-list schema is a **future authorized test**, not an action performed by this planning-only skill.


In short, the security strategy is: treat every external capability as untrusted until approved. Use whitelists, authentication (OAuth with verified issuers), and human confirmations for high-risk actions. Always include *human oversight*: e.g. “Before sending money via payment API, require manual confirmation step.”  


## Multi-Agent and Governance Considerations  
When multiple human/agent stakeholders collaborate, define who can do what:  
- **Shared Catalog:** Maintain a central capability ledger (e.g. a shared doc) with who can approve new providers.  
- **Roles:** Distinguish roles: e.g. *Capability Owner* (owns access/credentials), *Integrator* (sets up integration), *Reviewer* (security check). For instance, only a designated “Security Officer” may approve a new external MCP server entry.  
- **Access Control:** Credentials for each capability should be stored securely (secret store) and only accessible by authorized roles. Do not hard-code in agents.  
- **Invoke Permissions:** The system should enforce agent-level policies: e.g. an agent should not call a bank transfer API without user consent. The skill should capture these policies: e.g. a contract might say “any request to this tool requires a two-step human prompt.”  
- **Team Governance:** If one agent discovers a capability in planning, it doesn’t automatically exist in deployment. For example, even if an LLM planning agent can reach Stripe’s API with a token, the actual running environment might not; we must get human to set up credentials in production. We must document that “agent had no direct runtime access; human needs to provision Stripe account.”  


Governance policies (like requiring dual sign-off for critical actions) should be recorded as rules or ADRs. For example: *“All financial API calls require offline confirmation via Upwork’s workflow.”* The skill might suggest these gates when encountering high-impact capabilities.  


## Integration Contracts and Specifications  
For each chosen capability, we produce a concrete **integration contract**. This is a technical specification (in ARCHITECTURE.md, ADR, or docs/specs) detailing exactly how the agent will use the tool/API. It should include: 
- Interface definition (method names, parameters, return schema). 
- Preconditions (e.g. “Environment var EMAIL_KEY must be set”). 
- Idempotency (what happens on retries). 
- Pagination or continuation strategies if needed (e.g. list APIs).
- Error codes and retry logic (e.g. “If API returns 429, apply exponential backoff up to 3 tries.”). 
- Rate limits and quotas (document expected limits, e.g. “100 req/min”).
- Versioning (expected API version, compatibility notes).
- Logging and observability (e.g. what to log, metrics). 
- Test dummies or stubs: e.g. “We will implement a mock email server for offline testing.” 
- Downgrade or fallback: “If the remote API is down, fall back to sending a local SMTP mail queue.”
- Security and auth: what tokens or OAuth scopes are used (but *never* embed actual tokens in docs).
- Human checks: if the action is destructive, note “confirm with user for every request”.


For example, a contract excerpt in YAML might look like:  


```yaml
capability: SendEmail
provider: SendGrid
endpoint: "https://api.sendgrid.com/v3/mail/send"
method: POST
headers:
  Authorization: "Bearer $SENDGRID_API_KEY"
body-schema:
  type: object
  properties:
    to: { type: string, format: email }
    subject: { type: string }
    body: { type: string }
auth:
  type: bearer
  scopes: TBD  # verify documented permission model
idempotency: to_be_established  # do not infer API retry semantics
retry:
  onStatus: [429, 503]
  strategy: exponential
security:
  secrets: [ SENDGRID_API_KEY ]
observability:
  logs: [request_id, status_code]
tests:
  - "Planned: reject invalid authorization without leaking credential details."
  - "Planned: validate request/error mapping using a mock; actual results TBD."
```


This contract would appear in docs (possibly in an `interfaces/` spec or as part of ARCHITECTURE.md). It ties directly to design: e.g. ARCHITECTURE.md can have a section **Integrations** listing these with rationale from ADRs. 


## Sample Documents and Templates  
Below are illustrative examples (for guidance, to be refined for each project). All examples are *illustrative/unapproved* templates.


**Capability Inventory (Markdown Table, example):**


| CapID | Requirement            | Intent                           | Proposed Solutions           | Priority | Status    |
|-------|------------------------|----------------------------------|------------------------------|----------|-----------|
| CAP-1 | REQ-21 (Send Email)    | Deliver email notifications      | Build SMTP / SendGrid API / XYZ-MCP Server | High     | Candidate |
| CAP-2 | REQ-37 (Parse PDF)     | Extract text/images from PDFs    | Tesseract / PDFMCP Cloud     | Med      | Candidate |
| CAP-3 | REQ-45 (User Auth)     | User login/authentication        | OAuth (Azure AD) / Keycloak  | High     | Deferred  |
| ...   | ...                    | ...                              | ...                          | ...      | ...       |


*Status*: Candidate=under review, Selected=approved **only after an actual human decision**, Blocked=rejected, Deferred=need more info. No candidate in this example is approved.


**Capability Scorecard (example for CAP-1 “Send Email”):**


| Criterion            | Build(SMTP lib)            | SendGrid (API)       | Example-MCP Server          |
|----------------------|----------------------------|----------------------|-----------------------------|
| Coverage (features)  | Lacks email templates      | ✔                    | ✔                           |
| Ease of integration  | Medium (SMTP config)       | High (SDK available) | Low (custom MCP setup)      |
| Security/Privacy     | SMTP delivery still crosses networks | Provider data handling TBD | Server unvetted |
| Cost                 | Software/license TBD; mail transport still costs | Pricing TBD | Pricing TBD |
| Vendor lock-in       | Low (open SMTP)           | High (SendGrid API)  | Medium (MCP format lock-in) |
| Maintenance          | Low (just library updates) | Medium (vendor SLA)  | Low (if OSS community active) |
| Overall Fit Score    | **Not scored**             | **Not scored**       | **Not scored**             |


*(All comparison cells are hypotheses for demonstration, not measured product claims. No provider was approved or demoed.)* Approval requires verified evidence, stakeholder weights and an explicit decision record.


**MCP Server Vetting Sheet (example fields):**


- Server Name / URL: `mcp.example.com` (GitHub: example/mcp-server)  
- Description: “Provides user management tools and resources”  
- Auth Model: OAuth (client ID required)  
- Identity Evidence: publisher ownership **unverified**; TLS and stars do not establish code trust.  
- Protocol Version: **claimed 2026-07-28; actual compatibility untested**  
- Dependencies: **unknown; runtime and image provenance to be checked**  
- Published: **unknown; verify source publication and release history**  
- Maintainers: ExampleCorp (contact: devs@example.com)  
- License: **claimed MIT; verify the actual publisher and license file**  
- Security notes: **no verified audit or advisory result; pending review**.  
- Data sent: username (may be personal data; classify and authorize before transfer).  
- Data fetched: basic profile (PUID, email).  
- Permissions requested (hypothetical): GitHub OAuth `read:user`; actual provider and scopes require verification.  
- Sandbox test: **not executed** (outside bootstrap scope)  
- Status: **candidate — human approval pending**.  


**Ownership / Permissions Ledger (YAML excerpt, no secrets; hypothetical planning state, NOT a configured vault or approved integration):**


```yaml
capabilities:
  - id: CAP-1
    name: SendEmail
    proposedOwner: team-svc-email  # role only; not an actual assignment
    proposedCredentials:          # names/references, never credential values
      - account: ExampleMailOrg
        user: devops@example.com
        credentialName: MAIL_API_KEY
    proposedPermissionScope: "mail.send"
    proposedSecretStorage:
      - name: MAIL_API_KEY
        store: undecided          # no vault configured or tested
        owner: undecided
    status: candidate             # no human approval recorded
    lastVerified: null            # no live integration verification performed
    installationVerified: false
    approvalEvidence: null
```


**Example ADR (Architecture Decision Record):**


- *Title:* Use Twilio for SMS vs. AWS SNS (2026-11-05)  
- *Decision:* **Hypothetical draft, NOT APPROVED:** compare direct SMS providers for approved requirements.  
- *Context:* Requirements needed global SMS with reliable delivery and compliance. Two options: AWS SNS vs Twilio.  
- *Considerations:* Both support OTP and long text. Price and operational fit are unverified here; provider selection requires a dated official pricing/features review and a human decision.  
- *Potential consequences if approved:* select an SDK, define a secret-owner/provisioning path, and add a traceable backlog task. No account, credential or implementation exists.  


**Backlog Tasks (Markdown list examples):**


- **[CAP-1]** *Implement SendGrid Email Integration.*  
  - **Prerequisite (human-owned):** authorize a sandbox/test account and define the secure credential provisioning method; do not ask the planning agent to collect keys.  
  - **Task:** Write `sendEmail(to,subject,body)` using SendGrid SDK.  
  - **AC:** Can send test email (log and manual check). Error if invalid address.  
  - **Verification:** Unit test mocking 200 OK and 400 error responses.  


- **[CAP-2]** *Evaluate Tesseract vs Cloud PDF APIs.* (Spike)  
  - Research if a free MCP PDF extractor exists; decide local vs remote.  
  - Outcome: Dev environment cannot use Internet, so plan Tesseract.  


- **[CAP-3]** *Add OAuth login via Okta.*  
  - Specify an approved user authorization flow and consent boundary; do not design live OAuth endpoints from an unapproved provider choice.  
  - Document in spec: “/auth/login endpoint triggers OAuth redirect.”  


**Verification & Evidence States:** For each capability/integration, track a maturity state (in BACKLOG.md or a status file):


- **Not researched:** No investigation done yet.  
- **Candidate:** Potential identified, but not approved.  
- **Approved:** Chosen for implementation (in backlog).  
- **Configured:** Credentials acquired, client stub written.  
- **Tested:** Integration tests executed successfully.  
- **Production:** Proven in deployed system.  
- **Blocked/Deprecated:** Not used due to risk or obsolescence.


Example: CAP-1 (SendGrid) might move from Candidate → Approved → Configured → Tested.


## Verification and Testing Plan  
During bootstrap (planning), our “verification” is research: e.g. we may have looked at service docs or quick trial. Post-bootstrap, actual testing is done in implementation. We propose:  


- **Static Checks:** Before coding, review schemas and interface docs of selected tools to ensure the integration contract is correct. For MCP servers, plan an **authorized post-bootstrap compatibility test** using the supported modern `server/discover` or legacy `initialize` path, followed by permission-scoped tool/resource contract checks.  
- **Unit/Contract Tests:** Mock the external service (e.g. stub HTTP) to test contract handling (schema, pagination, error codes).  
- **Auth/Permission Tests:** Verify that wrong credentials or missing scopes fail safely (e.g. the client handles 401/403).  
- **Red-Teaming:** Simulate malicious responses (e.g. unexpectedly large payload, or a tool returning `{"tool_name":"rm -rf /"}` in text) to check the agent’s filtering. OWASP suggests specifically testing prompt injection via tool outputs.  
- **Rate/Timeout Tests:** Induce 429 (rate limit) or network drops to ensure retries/timeouts are handled gracefully.  
- **Privacy Checks:** Ensure no secrets leak to logs or LLM outputs (leak detectors).  
- **Version Compatibility:** If using MCP, check with each supported client (Codex, Claude, etc.) in draft mode to ensure the MCP integration actually works at runtime (see interoperability below).


Each test result should update the status (Approved→Tested or Blocked).


## Ongoing Validation (“Freshness”)  
Since tools and services evolve, we incorporate triggers for re-validation:  
- **At Bootstrapping Time:** We already fetch spec versions and docs. We log source URLs and dates.  
- **Event-Driven Recheck:** When a capability is about to be implemented, re-query registries or docs to see if anything changed (e.g. new SDK version).  
- **Periodic Audits:** For long-lived projects, schedule periodic reviews (e.g. quarterly) of critical capabilities (check if APIs are deprecated, new vulnerabilities published). We can note next review dates.  
- **Fallbacks:** If a registry or endpoint is unavailable, the skill should treat its info as *unknown* and flag the need for manual check. For critical capabilities, an expiration window (e.g. 6 months) could be set after which re-approval is needed, especially if no fresh evidence is present.


## Platform Interoperability (Codex, OpenCode, etc.)  
Different AI platforms (Anthropic/Claude, OpenAI/ChatGPT/Codex, Google Gemini) may have varying MCP support. For example, [OpenAI Codex](https://developers.openai.com/learn/docs-mcp) and [OpenCode](https://opencode.ai/docs/mcp-servers) document MCP support, but actual compatibility depends on client version, transport and protocol era; OpenCode describes explicit modern-versus-legacy settings. ChatGPT/other agent integrations may expose multiple vendor-specific or MCP-backed mechanisms; identify the **specific product/runtime and its current documentation** rather than inferring a universal plugin protocol. Cursor.dev and other IDE-integrated agents often use MCP under the hood.  


We must not overfit to one: our design uses MCP *as an abstraction*, but if running under a non-MCP platform, integration code will differ (e.g. for ChatGPT we might need to implement in its plugin format or call external agent wrapper). We note: “Capability intent remains provider-neutral; a runtime-specific adapter (MCP, direct API, SDK, plugin or manual operation) remains a decision, and its availability must be verified before implementation.” This goes in the ADR or architecture notes.


## Limitations & Tradeoffs  
- By delaying credential provisioning to runtime, we avoid embedding secrets. However, this means planning is less precise (e.g. we can’t test for real until tokens exist).  
- Preferring native/SDK solutions may lead to more code to maintain than a one-line MCP call, but reduces attack surface.  
- Deferring full MCP support (e.g. leaving MCP.md) means the initial ZIP lacks runnable code; users must implement the integration tasks. We mitigate surprise by clear documentation and a promise: “This output is a spec/plan, not a shipped app.”  
- The Skill v0.1 can keep discovery lightweight, but **must not defer identifying and blocking serious privacy/permission risks**. Active penetration tests belong to later authorized implementation, while mandatory human approval, provenance, secret exclusion and least privilege are bootstrap constraints.  


## Prior Work and Context  
This investigation builds on Research #1–#3.  In #1 (Knowledge Freshness), we addressed verifying MCP spec versions and logging confidence on dynamic claims. Here we apply that by citing the 2026-07-28 spec and noting when features like “sampling” were deprecated. Research #2 (Bootstrap roadmap) emphasized turning decisions into backlog tasks and acceptance criteria; we extend that by specifying concrete tasks (e.g. “Integrate SendGrid for email”). #3 (Deployment-aware architecture) covered trust boundaries; here we apply it to MCP (identifying where secrets live, requiring out-of-band OAuth). Throughout, we cross-link: e.g. if in #3 we decided the service sits in the “trusted agent” zone, we now document how tokens are provisioned to it.  


## Recommendations & Next Steps  
- *Human Decisions:* Many choices require governance: e.g. whether to make capabilities shareable across projects, default registry preferences, or retry policies. We recommend establishing these as team policies.  
- *Pilot Tests:* For MVP, pick a couple of diverse scenarios (e.g. adding an open-source MCP for local data, and using a closed cloud API for work data) to validate this workflow end-to-end.  
- *Skill Enhancements:* Later versions could support partial automation (searching official registries by intent, scoring candidates via ML).  
- *Continue Research:* The MCP ecosystem evolves quickly. We should monitor OWASP GenAI updates and any MCP-specific security audits.  


## References  


- Model Context Protocol Specification v2026-07-28 (MCP Docs, includes discovery, tools/resources/prompts definitions).  
- MCP Registry documentation (server.json schema and trust model).  
- Anthropic MCP introduction (2024).  
- “What is MCP?” (Google Cloud overview, Sept. 2026).  
- OWASP GenAI Top 10 LLM Attacks (2026), especially Prompt Injection and Supply Chain sections.  
- RFC 9207 (OAuth 2.0 `iss` parameter, 2022).  
- MCP “Sampling” feature docs (deprecated in v2026-07-28).  
- MCP “Elicitation” docs (incl. URL-mode OAuth flows).  
- MCP Resources docs (server side) (defines resources for context).  
- Community MCP directory (mcpservers.org blog/listings).  


Each source was accessed Nov 2026. This report contains evidence-backed background plus **proposed design heuristics**, not an automatically approved MCP ecosystem configuration. Examples are untested unless explicitly marked with independent execution evidence; the original uncited vendor details have been qualified in this revision.


## Official Verification Anchors and Portable Handoff (12 November 2026)


**Primary references (check versions again at implementation):**


- [MCP 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28), [release notes](https://blog.modelcontextprotocol.io/posts/2026-07-28/), [architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture) — protocol primitives and the modern stateless lifecycle.
- [Official TypeScript SDK — protocol eras](https://ts.sdk.modelcontextprotocol.io/v2/protocol-versions), [official Go SDK — discovery](https://go.sdk.modelcontextprotocol.io/protocol/) — legacy initialization versus modern discovery and compatibility caveats.
- [MCP Registry](https://modelcontextprotocol.io/registry/about), [Registry API docs](https://registry.modelcontextprotocol.io/docs) — metadata/publisher identification, **not** a security certification.
- [MCP elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation), [MCP sampling](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling), [OAuth 2.0 Security BCP RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html), [RFC 9207](https://www.rfc-editor.org/rfc/rfc9207.html) — separate flows, security and deprecation conditions.
- [OpenAI Codex — MCP usage](https://developers.openai.com/learn/docs-mcp), [OpenCode — MCP servers](https://opencode.ai/docs/mcp-servers) — **host-specific** configuration and version support. OpenCode documents an explicit `legacy` versus `auto`/`2026-07-28` choice; do not assume universal negotiation behavior.
- [OWASP GenAI Security Project](https://genai.owasp.org/) and [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) — injection/supply-chain risks and secure development practices. They do not vet a specific MCP package or directory listing.


### Minimum capability discovery handoff — illustrative, NOT an installed integration


```yaml
capability_id: CAP-001
requirement_refs: [REQ-TBD]
intent: "Retrieve a needed data source for a validated task"
status: candidate  # candidate | proposed | approved | deferred | blocked | obsolete
options: [no_integration, local_library, direct_api, mcp_adapter]
selected_option: undecided
human_decision_owner: TBD
external_publisher_verified: false
runtime_support_verified: false
protocol_revision: TBD
transport: TBD
read_write_side_effects: TBD
scope_and_account_owner: TBD  # names/roles only; never credentials
cost_and_data_region: TBD
last_source_check: null  # sample record; check actual sources before selection
future_verification:
  - inspect official publisher and package provenance
  - verify actual target client and protocol era
  - test contract and least-privilege permissions only after authorization
  - test failure/offline path and revocation
mcp_connected: false
server_installed: false
tool_invoked: false
```


The four research reports remain **source documents**, not approved project policy, an integration catalog, or test execution evidence. The SDD v0.1 should discover capabilities *only when justified by a real requirement*, preserve a protocol-neutral semantic contract and allow a complete **no-MCP** path. An external MCP listing must not be loaded automatically. Future connect/install/invoke/credentials/billing actions require explicit human authorization and runtime-enforced boundaries.