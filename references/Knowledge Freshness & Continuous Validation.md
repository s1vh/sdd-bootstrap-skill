# Knowledge Freshness & Continuous Validation


> **Editorial review — 12 November 2026.** Corrected unsupported quotations and vendor attributions, removed obsolete Android/PHP recommendations, clarified evidence and approval boundaries, and aligned proposal logging with the approved PROJECT_CONVENTIONS.md methodology baseline (D01–D10). The research concepts remain proposals for an SDD Bootstrap Skill, not implemented capabilities or a continuously running monitor. The source pointers below are verification anchors, not a claim that every example has been individually tested.


**Executive Summary:** The Skill's knowledge base should be treated as a *living repository* whose currency is actively verified. The following practices are recommended: (1) maintain metadata for each unit of knowledge (origin, version, date) and record validation evidence; (2) detect changes through event-driven triggers or scheduled checks (e.g., official feeds, APIs, ETag/Last-Modified headers, and hash comparisons); (3) classify sources by their level of authority (formal standards > official documentation > community sources > AI-generated/SEO content), applying critical-evaluation methods such as SIFT to corroborate claims; (4) assign each item a status: current/verified, change detected, obsolete/discouraged, incompatible, or unknown (distinguishing recency from correctness); (5) assess confidence (High/Medium/Low) on the basis of source reliability and agreement; (6) maintain an evidence log (section, claim, source URL, dates, reliability, contradictions, next review, hash), as illustrated by the YAML example below; and (7) generate alerts and proposed patches/diffs for human review—**without applying changes automatically**. The Skill should support *safe degradation*: inform the user when verification is not possible (due to lack of web access or other resources) and document manual follow-up actions. The minimum MVP includes basic metadata, a few critical checks (language versions, platform end-of-life dates, CVEs), online and offline modes, and a workflow for adding update tasks to the backlog. An incremental roadmap starts with a small number of critical checks and later expands to additional sources and automated processes.


## State of the Art


Modern knowledge-management practices emphasize the *active management* of information throughout its lifecycle. The term *knowledge drift* is used here descriptively: stored guidance can cease to match the authoritative state of a changing external system. The original quoted definition has been removed because its attribution was not verifiable in this draft. This is critical in AI-agent environments: an agent may continue producing fast answers while relying on outdated information. Retrieval-Augmented Generation (RAG) can help an agent consult external material, but retrieval alone guarantees neither freshness nor correctness; dated, attributable source evidence and validation remain necessary. An older official standard may still be current, while a newly indexed blog may already be wrong.


One possible **illustrative design pattern** is a seven-stage pipeline from source registration to controlled activation. The previous draft attributed this particular pipeline to Yepic (2026), but did not supply a verifiable primary citation; it should not be represented as a validated standard or attributed research result. First, authorized sources are inventoried; then additions, changes, and removals are detected using the strongest available signals (webhooks, feeds, ETags, or hash comparisons). Each candidate version is evaluated before activation (structural checks, retrieval tests) and then activated atomically to avoid mixing versions. Finally, outdated caches and derived artifacts are invalidated. The pipeline records timestamps (when information was observed, made ready, and used) to track the lifecycle. It also recommends classifying sources by their rate of change and criticality: for example, live operational data (APIs), emergency notices, controlled policies, and stable references, each with different latency targets.


DevSecOps guidance supports the idea of *knowledge as code*: version and validate knowledge in much the same way as policies or infrastructure as code. Under the *Security as Code* approach, development rules and practices should reside in repositories, with peer review and automated tests. This can improve traceability, but it does not by itself prove compliance or guarantee that checks ran. For source evaluation, methods such as SIFT recommend identifying key claims and tracing them to trustworthy sources, investigating author credibility, and seeking independent corroboration. Overall, the state of the art favors hybrid human–machine systems: agents make suggestions and perform validation, while experts retain final approval over changes.


## Definition and Boundaries of the Knowledge Base


The Skill's *knowledge base* includes all the formalized knowledge it uses: stable principles (e.g., SDD methodologies and requirements templates), project conventions (`/docs/PROJECT_CONVENTIONS.md`, `/docs/PRD.md`, etc.), and specific information (suggested technologies, known versions, common integrations). A distinction is needed between:


- **Stable Knowledge:** Engineering standards and patterns (e.g., “consider OpenAPI when an HTTP API contract is needed,” ISO/IEEE 29148 for requirements, and BDD/EARS for specifications). These evolve slowly, and their current versions are generally documented by official standards bodies.
- **Dynamic Knowledge:** Framework versions (Java 17 vs. 21), trending technologies (mobile frameworks, MCP-server directories), and market or security information (CVEs, end-of-life dates). These change rapidly.


The proposed approach is to restrict the knowledge base to authorized or referenced information: each item should cite its origin. Knowledge will be organized by domain (e.g., “technology stack,” “regulatory requirements,” and “development workflows”) and versioned (e.g., with Git, using `/docs/specs/` and `/docs/decisions/`). Each item will have metadata such as its source, effective date, and license. The distinction between *semantic contracts and implementation adapters* must remain clear: principles (e.g., “plan verification automation where useful” or “record consequential architecture decisions”) are separate from specific tools or implementations (GitHub Actions vs. GitLab CI). The Skill should not incorporate unverified external details—for example, it should not mandate a specific framework without checking whether its guidance is current. Knowledge-base versions can be managed through Git conventions (tags or version files) and timestamps; each area should have a “last reviewed” date that can trigger future checks.


## Detecting Obsolescence (Patterns and Architectures)


Several complementary mechanisms are suggested for identifying obsolete content:


- **Event-driven triggers:** Subscribe to changes in critical sources (e.g., repository *webhooks* or *RSS feeds*, release-note APIs, and security feeds). For example, a web connector could receive new-release notifications through a webhook for the Spring Boot repository. When a security advisory (CVE or other advisory) affects a dependency, an event could be generated. Configuration files (e.g., Gradle/Maven) may also be monitored with software composition analysis (SCA) tools.
- **Scheduled verification (polling/periodic checks):** For resources without feeds, perform periodic checks of `Last-Modified` or `ETag` fields on documentation or API URLs. For example, request the JSON version of the Python roadmap and compare its `ETag`; if it has changed, reassess the information. This follows the incremental-ingestion pattern described for RAG.
- **On-demand queries:** At the beginning of bootstrap, the Skill can run targeted checks (e.g., “Which Angular releases are currently supported for this project?”) using a small integrated search mechanism or a suitable API (e.g., PyPI or npm APIs). This reduces the need for continuous browsing: verification occurs at project initiation or when requested by the user.
- **Immutable structure plus validation:** When a change is detected, new content is ingested as a draft rather than overwriting the active knowledge base. Consistency checks are performed—for example, validating formats, running a sample information-retrieval query, and checking for regressions. Only after the checks pass is the new version activated atomically (e.g., by updating an alias or branch). This prevents partially updated knowledge from becoming active.
- **Cache-invalidation cascade:** Cache layers (agent responses and embedding indexes) are invalidated when relevant updates are detected. An invalidation event containing affected IDs and versions can be emitted so agents regenerate queries against the updated knowledge base.


These patterns are compatible with ordinary document-change detection, HTTP conditional requests, and controlled indexing. `ETag` and `Last-Modified` can help identify representation changes, but cannot by themselves establish semantic validity. The previous unattributed vendor quotation has been removed. Accordingly, when the Skill retrieves new information, it should include a verification step (e.g., ask, “Is there a discrepancy between my existing information and the source?”) and notify the user of uncertainty when confirmation is unavailable.


**Honest degradation:** Since internet access **may be blocked by the selected Codex environment or policy**,  the Skill must not assume connectivity. It should support an offline mode—for example, relying on preloaded information or suggesting manual searches. If a network operation fails, it should say: “X could not be verified; proceed at your own risk.” If an external query fails (timeout or insufficient permissions), the Skill should mark the item as *unknown/unverifiable* and continue.


## Source Classification


Not all sources are equally trustworthy. At least the following tiers are proposed:


- **Official sources and standards:** Recognized organizations (ISO, IEEE, W3C, governments, and official language/platform documentation). High authority. Examples: ISO/IEC/IEEE 29148 for requirements and MDN/W3C for web technologies.
- **Official vendor documentation:** Framework or language websites (e.g., React and Angular documentation or Python.org). High to very high confidence, although these sources may change (as reflected in release notes).
- **Academic or certified publications:** For example, significant research papers and applicable industry standards.
- **Reputable community and industry sources:** Recognized technical blogs, tutorials by leading companies (such as Google's Medium publications or other industry organizations), established sites such as Hackernoon, and moderated forums (Stack Overflow). Medium confidence; additional corroboration required.
- **Secondary and AI-generated/SEO sources:** AI-generated content, aggressively SEO-optimized or outdated websites, and unverified Q&A. Low confidence. For example, anonymous low-quality posts or aggregated content without a clear author should be treated skeptically.


Credibility assessment is based on the SIFT approach: identify key claims, corroborate them through reliable sources, investigate the author/publisher, and seek independent confirmation. In practice, the Skill would perform cross-source checks: if it encounters a claim (e.g., “Java 21 is LTS”), it would verify that claim against an official source (e.g., an Oracle page) and at least one additional source. Conflicts should be reported.


**Source contamination:** Unsafe links and unauthorized content should be avoided. Web access introduces risks (according to OpenAI, enabling internet access exposes agents to *prompt injection* from malicious content). Connections should therefore be limited to preapproved official sites and APIs, or strict sanitization should be applied to responses. Retrieved material is treated as *untrusted data* until validated; it should not be inserted directly into the knowledge base without review. Licenses must also be respected: copyrighted content should not simply be copied into the knowledge base; prefer short summaries or citations. When text extraction is necessary, review the permissions governing its use (e.g., `robots.txt`, licensing terms, etc.).


## Knowledge Status Taxonomy


Each knowledge-base section or item should carry one of the following statuses:


- **Current/Verified:** The information has been confirmed to be current and valid for the project's objectives. Example: “Version X of this library is recommended.”
- **Change Detected:** A new version or relevant fact has been found and awaits review. Example: “React 18 exists whereas the current information refers to React 17.”
- **Obsolete:** Superseded by a newer version or standard. Example: “Java 8 is obsolete for new projects.”
- **Discouraged:** Still functional, but no longer recommended. Example: “Framework A will be discontinued in 2027; use B.”
- **Incompatible:** Incompatible with current requirements or dependencies. Example: “Node 14 does not support the modern syntax being used.”
- **Unknown/Unverifiable:** Insufficient information is available, or a source could not be consulted. Example: “The update feed could not be accessed; its status is therefore unknown.”
- **Historical/Reference:** Retained for reference only, not for use in new projects (e.g., older versions documented for completeness).


It is also important to distinguish *recent* from *correct*: being newer does not automatically make something better. Migration decisions should consider both the risks and benefits of change. For example, if Python 3.12 becomes available but a project has already validated Python 3.11, the Skill should evaluate compatibility and support plans before treating migration as critical.


## Confidence and Evidence Logging


Instead of assigning a falsely precise percentage, reliability should be expressed on a High/Medium/Low scale based on source authority and consistency. Each actual verification should generate a structured **evidence record**. The following YAML is a **schema illustration only**, not a completed lookup, confirmed support recommendation, computed hash, or human-approved update:


```yaml
evidence:
  - section: "Java runtime support"
    claim: "Check whether the proposed JDK release is supported for the project's deployment."
    source: "Official vendor support policy — check pending"
    url: "https://www.oracle.com/java/technologies/java-se-glance.html"
    published: null             # not established for this sample
    checked: null               # no lookup performed for this sample
    status: "unknown/unverified"
    confidence: null            # assess High/Medium/Low after evidence review
    contradictions: []
    dependencies: ["Selected JDK distribution", "Target platform"]
    nextReview: "before approving the runtime choice"
    humanDecision: "pending"
    notes: "Illustrative record; no version, approval or support claim is verified here."
    hash: null                  # populate only from an actual computed digest
```


Fields include the claim or recommendation, source URL, publication date (when available), consultation date, confidence level, any conflicting sources, relevant dependencies, suggested next review date, human decision (e.g., “update” or “ignore with justification”), and a content hash where useful. This provides traceability once populated with real observations: the evidence supporting each decision remains identifiable. Null fields in the sample are intentionally **not evidence**.


## Collaborative Process and Change Management


The Skill does not modify the knowledge base automatically. Instead, it **alerts and proposes**. For example, when a new advisory is found, the Skill should create a **proposed review item in a backlog/decision queue**: “Check whether advisory X affects dependency Y; evidence and decision pending.” It must not put an unexecuted remediation in `/docs/UPDATES.md`, which the conventions draft reserves for actually performed work and its evidence. Likewise, it can add backlog tasks describing necessary actions (“Update Spring Boot to vX; test compatibility”). Where ambiguity or conflicting information exists, it should ask questions during the interview stage (“Would you like to migrate to Angular 17, knowing that it depends on these components?”). Every proposal should include a diff or suggested replacement text for the affected section.


Versioning and rollback must be supported: changes to the knowledge base (e.g., suggested modifications to specifications or templates) should be versioned as internal pull requests. If an update causes problems, the previous documented version can be restored. Authorized exceptions are also possible: if a user deliberately retains obsolete technology (for legacy compatibility), the Skill should record that decision in its evidence. All reviews are documented (in `/docs/decisions/` or `/docs/verification/`) for auditability, avoiding silent changes.


This process follows continuous-compliance practices: similarly to *policy as code*, each rule or recommendation becomes a versioned and tested artifact. Final human review should be encouraged before critical changes are applied.


## Lightweight MVP and Iterative Plan


For a practical first prototype, prioritize the essentials:


- **Basic metadata:** An evidence-record structure (YAML/JSON) containing status, date, and source fields.
- **Targeted checks:** A small set of key checks (e.g., verify the end-of-life date of a proposed Python version, check the latest Java LTS release through an official API, and look for CVEs affecting common dependencies). These checks can use predefined searches or simple API calls.
- **Offline mode:** If there is no connection, report “verification unavailable” without interrupting the bootstrap workflow.
- **Simple alerts:** Clear messages explaining what is being proposed and why (e.g., *“The current version of X is in maintenance mode; updating to Y is recommended.”*).


Acceptance criteria and test cases (matrix):


- **Cloud-hosted web/API service:** If an unsupported PHP release is proposed, the Skill checks the official [PHP support schedule](https://www.php.net/supported-versions.php), records the as-of date, and proposes a **currently supported, application-compatible** release. It must not suggest PHP 8.0 merely because its major version is higher; PHP 8.0 is itself unsupported.
- **Mobile application:** If an outdated Android level is proposed, the Skill distinguishes **`minSdk` device compatibility** from **`targetSdk` publication requirements**, checks the actual distribution channel, and cites [Google Play target-API requirements](https://developer.android.com/google/play/requirements/target-sdk) when relevant. There is no universal “Android 11 current minimum” for every Android application.
- **Offline/air-gapped project:** Simulate an environment without internet access; the Skill should skip external checks and report “Could not verify…”.
- **Unsupported technology:** Propose an obsolete Windows stack (e.g., Windows 7); the Skill should warn about end of support (linking to Microsoft) and suggest alternatives.
- **Critical vulnerability:** If an unsupported OpenSSL branch is proposed, the Skill checks official support status and applicable security advisories, then proposes a maintained, compatible alternative. It must not infer a specific CVE from a product family without a version and affected-configuration match.
- **Updated standard:** For example, if the knowledge base cites Swagger/OpenAPI 2.0 while a later specification is required by the approved contract, flag a compatibility review and a migration decision; newer versions are not automatically mandatory.
- **Conflicting sources:** If two sources disagree (Stack Overflow vs. official documentation), the Skill marks the issue as “sources disagree” and requests manual validation.
- **Connection failure:** Simulate an unavailable API and verify graceful error handling.
- **Old document:** If a section makes **time-sensitive** claims without recent evidence, mark those claims for revalidation; publication date alone does not invalidate stable principles.


The first version (MVP) will leave many areas for later iteration. For example, it will initially use isolated checks rather than automating a complete pipeline. Later versions can expand the sources consulted (security APIs, local RAG, MCP agents), introduce automated triggers, and integrate caching techniques to optimize costs.


## Implications for Agent Environments (Codex, OpenCode, etc.)


A provider-agnostic Skill must not assume a particular model. For example, in some **Codex hosted environments**, internet access is constrained or disabled unless configured; the Skill must therefore support workflows without web access. If the user enables external access, there are risks (prompt injection from malicious pages), so connections should be restricted to trusted domains and reviewed. In environments such as OpenCode (or environments with browser plugins), browsing may be available, but the Skill's verification logic should remain independent of its tool layer. In other words, it should separate the **semantic contract** (“check PHP version”) from any technology-specific adapter (`curl`, `fetch`, or an API library).


No specific cloud provider is assumed: architecture and deployment specifications should be expressed in generic terms. Suggested changes must not be coupled to ChatGPT's UI or a particular IDE; the Skill should generate neutral artifacts (Markdown and YAML) that any environment can interpret.


## Query Costs and Efficiency


To control costs (tokens, latency, API rate limits):


- **Local caching:** Store recent results of important searches. For example, save the most recent verification of “stable version of X” with its date, and check again only after a reasonable period (e.g., one month) or in response to a triggering event.
- **Retrieve only what is necessary:** Rather than loading entire webpages, use dedicated APIs (e.g., GitHub API for releases and NVD API for CVEs). This reduces token consumption and execution time.
- **Incremental verification:** As data-ingestion guidance recommends, avoid needlessly rescanning all content; prefer targeted requests (“changes since the last check”). A full snapshot is expensive.
- **Pre-filtering:** Before running complex queries, exclude low-volatility topics (e.g., long-established theoretical concepts or standards, which need checking less frequently).
- **Batching related checks:** If several sections depend on similar sources, group them into one query (e.g., “Which LTS versions are available for these components?”).
- **Free and paid plans:** Prefer free or no-cost APIs; if a paid service is required (e.g., CI/CD services or hosted checks with potentially billable usage), inform the user during the interview stage so that any required accounts can be created.


In any case, without continuous-monitoring infrastructure, the Skill must not promise 24/7 surveillance: it is sufficient to report the need for periodic verification. Every cost (execution time or tokens) should be justified by its impact on project security or quality.


## Supporting Studies, Standards, and Patterns


There is no single standard for knowledge freshness in this context, but ideas from several fields converge:


- **Knowledge Management:** Standards such as ISO 30401 emphasize systems built around continuous improvement, although they do not prescribe updates to specific pieces of content. Knowledge-management practices nevertheless recommend governance and periodic review. The W3C PROV model provides a framework for provenance metadata, as noted by Yepic.
- **Software Supply Chain:** The Software Bill of Materials (SBOM) movement promotes dependency inventories, which are analogous to recording versions of knowledge. NIST's supply-chain trust approach (SSDF, SP 800-161) is similarly relevant: audit each link (knowledge source) and apply controls.
- **Requirements Engineering:** ISO/IEC/IEEE 29148 (requirements), EARS/BDD models, and SDD frameworks (especially Spec Kit and Kiro) emphasize clear and traceable specifications. The need to avoid *spec drift* is documented in the literature, including work on Spec-Driven Development in agentic environments.
- **Continuous Compliance and DevOps:** DevSecOps provides the concept of *security as code*, applied here to governing policies and specifications in repositories with CI/CD so their currency can be checked continuously. By 2026, this approach is increasingly becoming a baseline, with regulatory frameworks demanding ongoing monitoring.
- **RAG and AI:** The concept of an agent with updateable “memory” appears in emerging literature on RAG and hybrid agents. For example, NVIDIA's blog highlights how RAG can provide verifiable sources (using the term “footnotes”) to increase confidence in responses.
- **Industry Practice:** Commercial knowledge-management tools (e.g., Slite and Document360) address drift detection and automated curation in practical ways (suggesting updates based on usage analysis and change patterns). Although the evidence often comes from corporate blogs, it provides use cases: Slite emphasizes automatically detecting inconsistencies by cross-checking against original sources.


In summary, the proposed design aligns with trends in *Knowledge Management*, *DevOps*, and *responsible AI*: comprehensive versioning, traceability, risk-based freshness targets, human–agent collaboration, and continuous auditing.


## Conclusion and Incremental Roadmap


**Minimum Viable Design:**


- Define a data model representing each item with its status, sources, and metadata (version, dates, authority).
- Implement a workflow that responds to a *trigger* (e.g., bootstrap initiation or a manual user request) by querying key sources (e.g., language APIs, CVE feeds, and standards).
- Classify results and produce outputs: YAML/Markdown evidence logs, recommendation messages, and proposed backlog/review-queue tasks (`/docs/BACKLOG.md` where that convention is adopted), without falsely recording completed work.
- Handle failures: when a query fails, transition to an “unknown” state and notify the user.
- Establish a simple caching mechanism (save short summaries of recent results and when they were checked).


**Future Iterations:**


1. **Source expansion:** Add more APIs and feeds (e.g., Dependabot, NVD, and framework websites).
2. **Intelligent automation:** Add a small semantic-search mechanism or local RAG for validating free text in documents.
3. **UI/UX improvements:** If the Skill interacts with users, create interview prompts that prioritize relevant checks.
4. **MCP integration:** Use tool-oriented MCP servers (e.g., an MCP server for Git) to retrieve repository information dynamically.
5. **Post-bootstrap monitoring:** If infrastructure permits, optionally plan authorized periodic rechecks and create review proposals; write to `/docs/UPDATES.md` only when a documented action has actually occurred.


**Risks and Limitations:**


- Dependence on external connectivity (mitigated through a safe offline mode).
- False positives/negatives in obsolescence detection (requiring initial human calibration).
- Query costs (controlled through caching and selectivity).
- Unanticipated new sources (requiring periodic review of the source framework).
- The proposed data model will need to evolve in response to feedback from real-world tests.


**Open Decisions:**


- Exact criteria for transitioning an item from “change detected” to “obsolete” (e.g., is being two versions behind sufficient?).
- Confidence thresholds and risk tolerance (e.g., temporarily accepting an insecure dependency).
- Human oversight policies: what level of human confirmation is required to mark a change as critical?
- Final architecture: store the complete knowledge base (e.g., in a vector database for RAG), or perform on-demand queries?


This proposal establishes a foundation for the SDD Bootstrap Skill, emphasizing the **currency** and **reliability** of knowledge without assuming rigid infrastructure. Detailed analysis of sources and mechanisms (cited above) will inform the Skill's specific design in later iterations, maintaining a pragmatic, incremental approach that always remains subject to human review.


## Verified Reference Anchors and Editorial Limits (12 November 2026)


Primary or institutional resources checked for the corrected guidance:


- [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): conditional requests and HTTP validators are about representations, not verification of the truth of content. [IETF RFC 9111 — HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html) supplies related caching semantics.
- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/): provenance can represent the entities, activities, and agents involved in an information artifact's history.
- [Mike Caulfield's SIFT method, university library guide](https://guides.umd.umich.edu/SIFT): Stop, Investigate the source, Find better coverage, Trace claims to the original context. SIFT is a verification heuristic, not a ranking of standards by universal authority.
- [PHP — Supported Versions](https://www.php.net/supported-versions.php) and [Google Play target API policy](https://developer.android.com/google/play/requirements/target-sdk): examples of **volatile** official requirements. Recheck before deciding a stack or publication target.
- [NIST National Vulnerability Database](https://nvd.nist.gov/) and [GitHub Advisory Database](https://github.com/advisories): vulnerability leads; applicability requires affected-version and configuration checks, not a keyword match.
- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final): secure development lifecycle guidance; this does not certify the resulting skill.


**Unverified secondary claims retained as design motivation only:** the earlier vendor-specific description of a seven-stage freshness pipeline, broad statements about commercial RAG/knowledge-drift products, and claims of automatic compliance improvement lack traceable evidence in the original draft. They must not be treated as empirical findings. **No background surveillance or automated document mutation is provided by the research or by the proposed v0.1.**


**Status discipline:** `reviewed source` is not `up-to-date claim`, `drafted recommendation` is not `approved decision`, and `planned verification` is not `executed verification`. Changed official sources trigger review; they do not license unapproved automatic edits.