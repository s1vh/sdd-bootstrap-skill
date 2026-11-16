# Research 01 — Multimodal Requirements Elicitation & Collaborative Discovery

> **Editorial review — 11 November 2026.** Revised from the original Deep Research report, preserving its research scope and examples. Previously missing inline references were checked and repaired where possible; unsupported empirical assertions were qualified or corrected. Bibliographic links are standalone URLs, not inaccessible session IDs. This is a reference document, not execution evidence. See `CORRECTIONS.md` and `VERIFICATION_REPORT.md` in the accompanying archive.


**Advanced knowledge reference for a provider-agnostic Spec-Driven Development Bootstrap Skill**
**State of the art reviewed: 11 November 2026, Europe/Madrid**

## Scope, epistemic stance, and state of the art

This chapter addresses the engineering problem that precedes specification and architecture: how to transform incomplete, heterogeneous, sometimes contradictory human material into a sufficiently trustworthy description of a technical problem that downstream specification, architecture, stack selection, backlog creation, testing strategy, and deployment preparation can begin.

The target system is not a generic conversational assistant. It is a **bootstrap engineering process** whose input may include prose, successive voice notes, screenshots, sketches, diagrams, existing documents, URLs, UI mock-ups, and conversations involving several people. Its output is not a finished application. The output is a development-ready project repository whose important claims, constraints, uncertainties, decisions, and next actions are explicit enough that implementation can begin without silently reconstructing the product intent.

Requirements engineering remains the correct disciplinary foundation for this problem. ISO/IEC/IEEE 29148 defines requirements engineering as an interdisciplinary activity concerned with discovering, eliciting, developing, analysing, verifying, validating, communicating, documenting, and managing requirements. The currently published standard remains ISO/IEC/IEEE 29148:2018, confirmed in 2024; however, as of 11 November 2026, a third-edition Draft International Standard is in ISO's enquiry stage and is intended to replace the 2018 edition. A knowledge base that simply says “29148:2018 is the current standard” without checking would therefore already be incomplete even though it is not yet wrong. ([ISO 29148:2018](https://www.iso.org/standard/72089.html); [ISO DIS 29148](https://www.iso.org/standard/94091.html))

SWEBOK V4.0a likewise treats software requirements as an activity spanning elicitation, analysis, specification, validation, and life-cycle management rather than as a document-writing exercise. Its current public material includes stakeholder identification, elicitation, observation, prototyping, natural-language specification, modelling, and requirements management. ([SWEBOK V4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering))

The human-centred design literature adds an important complementary principle: requirements cannot reliably be reconstructed from stated preferences alone. Context of use, actual work, environment, users, and organisational conditions matter. ISO 9241-210:2019, reconfirmed in 2025, remains current and provides requirements and recommendations for human-centred design throughout the life cycle of interactive systems. ([ISO 9241-210:2019](https://www.iso.org/standard/77520.html))

This chapter therefore rests on three evidence strata:

| Evidence class | Treatment in this chapter |
|---|---|
| **Established engineering guidance** | Standards, mature requirements-engineering practice, human-centred design, privacy/security principles, empirical software-engineering literature. Treated as the strongest foundation. |
| **Emerging evidence** | Human–AI requirements elicitation, automated follow-up questioning, multimodal model reliability, MCP security. Useful, but treated cautiously because the field is moving rapidly. |
| **Synthesised recommendations** | The adaptive interview scoring model, claim ledger schema, readiness gates, and bootstrap-specific algorithms proposed here. These are engineering proposals derived from the evidence, **not empirically validated standards**. |

A central finding of the literature is that no single elicitation method is universally best. Technique effectiveness varies with context, stakeholder characteristics, uncertainty, domain, project constraints, information sources, social environment, and the type of knowledge being sought. Reviews explicitly warn against defaulting indiscriminately to open interviews. ([Elicitation technique selection (2014)](https://doi.org/10.1016/j.infsof.2014.01.009))

That observation should become a first principle of the Bootstrap Skill:

> **Adaptive elicitation is not a shorter questionnaire. It is continuous selection of the next cheapest trustworthy action that materially reduces consequential uncertainty.**

The action may be a question. It may instead be inspection of a diagram, comparison with an uploaded document, contextual observation, a prototype, web research, consultation with another stakeholder, or deliberate deferral.

### What this chapter deliberately does not do

It does not repeat a full treatment of SDD, traceability, specification drift, architecture design, testing architecture, repository conventions, or implementation planning. Those belong to the project's existing knowledge and subsequent research chapters.

It also does not claim that requirements discovery can remove uncertainty. Empirical work shows that requirements evolve during elicitation; dialogue itself can change and refine the original idea. ([Requirements evolution during elicitation (empirical study, 2022)](https://link.springer.com/article/10.1007/s00766-022-00383-7)) The objective is therefore not to eliminate uncertainty but to **expose enough of the consequential uncertainty that later engineering decisions are intentional rather than accidental**.

## Foundations of collaborative technical discovery

### Stakeholders are sources, not interchangeable authorities

Early discovery begins by identifying who can provide information and who has authority over which decisions. SWEBOK emphasises identifying stakeholders early because different affected parties provide different requirements and feedback throughout a system's life cycle. ([SWEBOK V4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering))

A useful bootstrap classification is:

| Role | Typical contribution | Authority question |
|---|---|---|
| Sponsor / owner | Goals, budget boundaries, business constraints | Can this person approve scope or spending? |
| End user | Workflow, pain points, terminology, accessibility needs | Can they describe usage but not approve architecture? |
| Operator | Deployment, support, incidents, maintenance | Can they constrain operational design? |
| Domain expert | Rules, concepts, exceptions | Are they authoritative for domain semantics? |
| Security / privacy stakeholder | Data handling, regulatory constraints, threat concerns | Can they approve risk acceptance? |
| Developer / technical owner | Delivery capability, tooling, maintainability | Can they approve technical trade-offs? |
| External authority | Regulation, contract, platform/API specification | Is this an authoritative external constraint? |

The Skill should therefore never collapse “the user said X” into “X is approved.” It should retain **who said it, in what role, and with what authority**.

Viewpoint-oriented requirements engineering has long treated stakeholder perspectives as distinct, potentially inconsistent views that must be reconciled rather than flattened prematurely. ([Finkelstein et al., Requirements Engineering Through Viewpoints (1993)](https://discovery.ucl.ac.uk/id/eprint/854/))

A practical rule follows:

> **Contradiction is data before it is a defect.**

If the finance stakeholder says “use only free services” and the operations stakeholder says “99.95% availability with 24/7 managed support,” the Skill should record the conflict. It should not silently choose a cheap provider or silently weaken the availability requirement.

### Interviews are only one instrument

Interviews are common because they reveal goals, terminology, explanations, exceptions, priorities, and tacit assumptions. They are also cognitively demanding: the interviewer must listen, maintain topic coverage, formulate follow-up questions, detect contradictions, and preserve context. Research tools such as AnnoteREI were created specifically because transcription and annotation burden analysts during elicitation. ([AnnoteREI! (IEEE RE 2022)](https://ieeexplore.ieee.org/document/9920036))

Interview quality depends on preparation, domain knowledge, question structure, communication, and the context in which answers are produced. ([Requirements evolution during elicitation (empirical study, 2022)](https://link.springer.com/article/10.1007/s00766-022-00383-7); [AnnoteREI! (IEEE RE 2022)](https://ieeexplore.ieee.org/document/9920036))

But asking people what they do is not equivalent to observing what they do. Contextual inquiry combines observation and questioning in the participant's environment precisely because workflows, workarounds, environmental constraints, and tacit practices may not appear in retrospective descriptions. ([UK Government — Contextual inquiry](https://www.gov.uk/guidance/contextual-inquiry))

For the Bootstrap Skill, techniques should be selected according to uncertainty:

| Situation | Prefer |
|---|---|
| Stakeholder can clearly explain goals and constraints | Semi-structured conversation |
| Existing workflow is complex or tacit | Contextual inquiry / observation |
| User journey is fragmented | Story mapping |
| Domain has many events, actors, policies, exceptions | Collaborative domain modelling / EventStorming |
| Stakeholders disagree | Joint negotiation or explicit conflict ledger |
| Visual interaction matters | Mock-up/sketch review and scenario walkthrough |
| Requirement is difficult to verbalise | Prototype or concrete example |
| Existing system is being replaced | Document, API, data and workflow analysis |
| Requirement concerns external technology | Current authoritative web research |

Story mapping is a practitioner technique for retaining the larger user journey while decomposing it into stories and backlog slices. Jeff Patton's original material emphasises walking a map end-to-end with stakeholders rather than treating stories as isolated tickets. ([Story mapping (Patton)](https://jpattonassociates.com/user-story-mapping/))

EventStorming similarly provides a collaborative modelling format centred on domain events and shared exploration. Its own guidance warns against forcing the format where another technique better serves the workshop's purpose and encourages incremental notation rather than front-loading modelling complexity. ([EventStorming (Brandolini)](https://www.eventstorming.com/))

These are useful techniques, but the Skill should not treat either as scientifically proven to outperform alternatives. The broader empirical literature shows that elicitation effectiveness is heavily contextual. ([Elicitation techniques SLR (2018)](https://doi.org/10.1049/iet-sen.2017.0144); [Elicitation technique selection (2014)](https://doi.org/10.1016/j.infsof.2014.01.009))

### Establish a shared domain language before architecture

Terms used casually by stakeholders frequently hide architectural consequences.

Consider:

> “Every customer has an account.”

Possible interpretations include:

- one login per natural person;
- one organisational tenant containing several users;
- an anonymous customer record with no authentication;
- a billing account;
- an external identity-provider account;
- several identities linked to one person.

The correct first response is not “Which authentication framework shall we use?” It is to establish what *customer*, *account*, *organisation*, *user*, *member*, and *identity* mean in this domain.

The Skill should maintain a lightweight **domain vocabulary**:

```markdown
## Domain Vocabulary

| Term | Working definition | Source | Status |
|---|---|---|---|
| Workspace | Shared project area containing one or more members | Ana, voice-03 01:12 | confirmed |
| Owner | Member allowed to manage billing and delete workspace | meeting-02 | provisional |
| Customer | Ambiguous: sometimes person, sometimes paying organisation | multiple | unresolved |
```

This prevents the architecture from fossilising ambiguous language.

### Requirements negotiation is not averaging

Conflict resolution should distinguish:

1. **Different facts** — someone is wrong or evidence is stale.
2. **Different preferences** — trade-off is possible.
3. **Different responsibilities** — parties optimise different outcomes.
4. **Different scopes** — apparently conflicting statements concern different contexts.
5. **Real incompatibility** — both requirements cannot be simultaneously satisfied.
6. **Authority conflict** — it is unclear who may decide.

The Skill may explain the conflict, identify consequences, propose options, and request a decision. It should not manufacture consensus.

### Cognitive biases and communication hazards

Software engineering is not immune to cognitive bias. Mapping studies identify phenomena including anchoring and confirmation bias across development activities, while experiments show that numerical anchors can distort software effort estimates. ([Cognitive biases in software engineering (IEEE TSE)](https://doi.org/10.1109/TSE.2018.2877759); [Numerical anchors in software effort estimates (2016)](https://doi.org/10.1016/j.jss.2015.03.015))

Particularly relevant hazards include:

| Hazard | Elicitation manifestation | Countermeasure |
|---|---|---|
| Anchoring | First technology mentioned dominates later thinking | Ask about constraints before technologies |
| Confirmation bias | Agent asks only questions consistent with its initial interpretation | Maintain disconfirming evidence and contradictions |
| Solution fixation | “We need Firebase” becomes a requirement | Ask what capability or constraint motivated it |
| Authority bias | Senior stakeholder's claim overwrites user evidence | Preserve source and decision authority separately |
| Availability bias | Recent incident becomes assumed dominant requirement | Ask frequency and impact |
| Framing effect | “Wouldn't mobile push be better?” steers answer | Prefer neutral alternatives |
| Automation bias | ASR/model interpretation is treated as ground truth | Show uncertain interpretation and request correction |
| Premature closure | Interview stops after plausible first solution | Apply readiness gates rather than conversational satisfaction |

Procedural prompting has empirical support for helping analysts elicit additional meaningful requirements, but no checklist eliminates interviewer bias. ([Procedural prompting in elicitation (2007)](https://doi.org/10.1111/j.1365-2575.2006.00240.x))

For an AI interviewer, an especially important rule is:

> **Do not ask questions whose wording contains the architecture you hope the stakeholder will choose.**

Prefer:

> “Do users need to continue working when connectivity is unavailable?”

over:

> “Should we make the app offline-first with local SQLite?”

The first elicits a need. The second anchors a solution.

## Multimodal evidence, provenance, and the epistemic claim model

Multimodality changes requirements engineering because evidence no longer arrives as a clean document. It arrives as an evidence stream.

A robust system should therefore distinguish **source material** from **interpretation**.

### Source objects

Every ingestible artefact should receive a stable source identity.

```yaml
source:
  id: src-voice-004
  kind: audio
  original_name: "voice-note-4.m4a"
  received_at: "2026-11-11T10:31:00+01:00"
  contributors:
    - "stakeholder:operations-lead"
  language: "es-ES"
  consent:
    recording: known
    redistribution: false
  derived:
    transcript: "transcripts/voice-004.md"
  integrity:
    original_preserved: true
```

A claim extracted from that source should point not merely to the file but, where possible, to an exact segment:

```yaml
evidence:
  source_id: src-voice-004
  locator:
    start: "00:01:43.200"
    end: "00:01:58.900"
  transcript_span: "..."
```

For documents, locators might be page and paragraph; for screenshots, bounding boxes; for diagrams, labelled nodes or regions; for conversation, message IDs.

This is not bureaucratic decoration. It enables later questions such as:

- *Why do we believe this?*
- *Who said it?*
- *Was that an exact statement or our interpretation?*
- *Has the source since been superseded?*

### Audio, ASR, and speaker attribution

Speech transcription should be treated as a derived representation, not an authoritative replacement for audio.

ASR error rates are not uniform across speakers. A widely cited PNAS study found significant disparities among commercial ASR systems for Black versus white American English speakers; although commercial systems have evolved since 2020, the study demonstrates the enduring methodological lesson that transcription accuracy cannot be assumed to be population-independent. ([PNAS ASR disparity (2020)](https://doi.org/10.1073/pnas.1915768117))

Speaker diarisation has also improved substantially, but contemporary reviews still identify overlapping speech, noise, far-field recording, speaker similarity, and real-world conversational conditions as sources of error. ([Speaker diarization review (2025)](https://doi.org/10.3390/app15042002))

Therefore the Skill should:

- preserve the original audio where policy and consent allow;
- retain timestamps;
- label speaker attribution as uncertain when diarisation is uncertain;
- avoid turning uncertain words into exact requirements;
- flag low-confidence technical nouns, proper names, numbers, dates, units, prices, and negations;
- permit replay/reinspection of the exact segment;
- record transcription corrections without overwriting the original provenance.

A transcription such as:

> “We don't need payments in version one.”

is particularly dangerous if ASR loses *don't*.

Consequential negations should receive disproportionate validation attention.

Accessibility also matters: W3C guidance treats transcripts as important alternatives for prerecorded audio, and WCAG 2.2 includes explicit requirements for alternatives to prerecorded audio-only media. ([W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/))

### Sketches, screenshots, diagrams, and visual material

A screenshot can provide direct evidence that an element appears somewhere. It does not necessarily prove:

- that the element is required;
- that it is interactive;
- what happens when clicked;
- that the shown state is current;
- that visually similar components share semantics;
- that hidden states do not exist.

This distinction is increasingly important when multimodal foundation models interpret visual inputs. Recent benchmarks show persistent limitations in visual grounding, document/OCR reasoning, fine-grained perception, and cross-modal hallucination even among advanced multimodal systems. OCRBench v2 reported major remaining weaknesses in text recognition, layout perception, complex-element parsing, and logical reasoning; MERLIM and other 2025 benchmarks similarly documented cross-modal hallucination and object-recognition failures. ([OCRBench v2 (NeurIPS 2025)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8c2e6bb15be1894b8fb4e0f9bcad1739-Abstract-Datasets_and_Benchmarks_Track.html); [MERLIM (CVPRW 2025)](https://openaccess.thecvf.com/content/CVPR2025W/BEAM/html/Villa_Behind_the_Magic_MERLIM_Multi-modal_Evaluation_Benchmark_for_Large_Image-Language_CVPRW_2025_paper.html))

Consequently:

> **An AI description of an image is an interpretation of evidence, not the evidence itself.**

For a hand-drawn mock-up:

```text
Source observation:
  "Sketch contains three boxes labelled Home, Projects, Profile."

Interpretation:
  "The boxes may represent primary navigation."

Inference:
  "The user may expect three top-level application areas."

Question:
  "Are Home, Projects and Profile intended as main navigation destinations,
   or are they only examples of screens?"
```

The first statement can be validated against pixels. The latter two cannot.

OCR should follow the same rule. Recent research on degraded documents shows that multimodal models may hallucinate text rather than abstain when visual evidence is weak. ([OCRBench v2 (NeurIPS 2025)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8c2e6bb15be1894b8fb4e0f9bcad1739-Abstract-Datasets_and_Benchmarks_Track.html))

### References, URLs, and external documents

A stakeholder-supplied link may express any of several intentions:

- “copy this functionality”;
- “I like this visual style”;
- “we integrate with this API”;
- “this is an authoritative regulation”;
- “this is an example of the workflow.”

The Skill should ask or infer cautiously **why the reference matters**.

External sources should be tagged by authority:

| Source class | Typical reliability for technical claims |
|---|---|
| Standards / law / official protocol specification | Highest for normative claims |
| Vendor's official API/service documentation | Highest for that vendor's current capabilities |
| Peer-reviewed research | Strong for claims actually studied |
| Maintainer repository/release notes | Strong for implementation/version facts |
| Reputable technical secondary source | Useful interpretation |
| Community directory | Discovery, not authority |
| Forum / social post | Lead or anecdote, not default authority |

### Privacy, consent, and minimisation

Voice, images, screenshots and documents may contain personal, confidential, or regulated information. NIST's privacy engineering material recommends explicit privacy risk management, while its definition of minimisation limits collection, processing, storage and disclosure of personally identifiable information to what is necessary for the purpose. ([NIST Privacy Framework](https://www.nist.gov/privacy-framework))

Where the GDPR applies, Article 5 establishes purpose limitation, data minimisation, accuracy, and storage limitation, while Article 25 requires data protection by design and by default. ([EU GDPR consolidated text](https://eur-lex.europa.eu/eli/reg/2016/679/oj))

The Skill should therefore distinguish:

```text
Need to understand the evidence
        ≠
Need to permanently package the raw evidence in the project ZIP
```

A user's voice recording may be needed during discovery but not belong in the delivered source repository.

### The epistemic claim ledger

The project needs a representation richer than “requirement / not requirement” but lighter than a formal knowledge graph.

Recommended claim classes:

| Class | Meaning |
|---|---|
| **stated_fact** | Stakeholder explicitly presents something as true |
| **observed** | Directly visible/audible in supplied evidence |
| **interpretation** | Meaning assigned to an observation |
| **inference** | Conclusion derived from other claims |
| **assumption** | Provisional proposition used to make progress |
| **preference** | Desired option without mandatory force |
| **constraint** | Boundary the solution must respect |
| **hypothesis** | Proposition requiring testing |
| **proposal** | Candidate solution or decision |
| **decision** | Explicitly approved commitment |
| **question** | Material unresolved uncertainty |

An illustrative record:

```yaml
id: CLM-031
type: constraint
statement: "The public launch must support Spanish and English."
status: confirmed
owner: product-owner
authority: scope
confidence: high

evidence:
  - source: src-meeting-002
    locator: "00:12:14-00:12:31"

derived_from: []
conflicts_with: []

impact:
  architecture: medium
  ui: high
  testing: high
  deployment: low

history:
  - date: 2026-11-11
    change: created
```

Confidence should describe the quality of the interpretation, **not the probability that the stakeholder will remain committed**.

For example:

```text
High-confidence interpretation:
"The user explicitly said 10,000 concurrent users."

Low-confidence factual basis:
"The user admitted this number was a guess."
```

These are different dimensions.

A useful minimal uncertainty representation is:

```yaml
epistemic:
  interpretation_confidence: high
  source_reliability: medium
  stakeholder_certainty: low
  decision_status: unresolved
```

This prevents a dangerous collapse into a single “confidence: 0.82” whose meaning nobody can explain.

### Revision without bureaucratic overload

The ledger should be **append-and-revise**, not append-only in the user interface.

Old provenance remains traceable, but humans should see the current state.

```text
CLM-014 v1:
"Must run entirely offline."
superseded by stakeholder clarification.

CLM-014 v2:
"Primary field workflow must work offline;
sync may require connectivity."
```

The Skill does not need a claim entry for every sentence. Record claims when at least one is true:

- the claim constrains design;
- it affects scope or acceptance;
- it may conflict;
- it is uncertain but consequential;
- it defines a term;
- it has external authority;
- it will later justify a requirement or decision.

## Adaptive interviewing as uncertainty reduction

### Why adaptation matters

A fixed 80-question intake form optimises form completion, not discovery.

A structured two-page brief may already answer most questions. A sequence of twelve voice notes may contain more total information yet leave critical technical uncertainties unresolved. The interview process must therefore depend on **what is currently known**, **how reliable it is**, and **what downstream decisions depend on it**.

Recent requirements-engineering research provides encouraging but still limited evidence that LLMs can generate context-dependent follow-up questions and automate portions of elicitation. A 2025 RE study of LLMREI evaluated 33 simulated stakeholder interviews and reported context-sensitive interviewing capability, while another 2025 study investigated LLM-generated follow-up questions in controlled experiments. These results are promising, but their scale and experimental settings do not justify treating autonomous AI elicitation as solved. ([LLMREI (2025)](https://arxiv.org/abs/2507.02564); [Follow-up question generation (2025)](https://arxiv.org/abs/2507.02858))

A 2026 systematic mapping study of 74 peer-reviewed studies on automated requirements elicitation concluded that contemporary approaches span identification, structuring, consolidation and stakeholder validation; the continued presence of stakeholder validation is especially relevant to the bootstrap model proposed here. ([Automated elicitation mapping study (2026)](https://www.mdpi.com/2078-2489/17/8/777))

### Candidate-question generation

At any point the Skill should derive unresolved **information needs**, not immediately generate prose questions.

Example:

```text
Information need:
Can field technicians complete critical tasks without connectivity?

Why it matters:
Determines persistence/synchronisation architecture and test strategy.

Current evidence:
Voice note says "coverage is often poor" but never states required offline behaviour.

Possible resolution:
Ask product owner.
Observe workflow.
Review existing operating procedure.
```

Only then should it form a question.

### Information value

Decision theory provides a formal concept of **Value of Information**: additional information has value when reducing uncertainty can improve the decision. VOI has also been applied to software requirements and architecture uncertainty. ([Letier, Stefan & Barr — Uncertainty, Risk, and Information Value (ICSE 2014)](https://doi.org/10.1145/2568225.2568239))

The Bootstrap Skill does **not** have enough calibrated probabilities and utilities to perform formal VOI analysis in ordinary projects. Nevertheless, the principle is useful.

A practical, explicitly heuristic question score can be:

```text
priority(q) =
    consequence
  × uncertainty
  × dependency
  × decision_proximity
  × irreversibility_modifier
  × answerability
  − burden
```

All dimensions can use ordinal values such as `low / medium / high`, translated internally to simple ranks if needed.

This equation is a **synthesised engineering heuristic, not an empirically validated formula**.

An alternative implementation avoiding pseudo-precision:

| Condition | Score |
|---|---:|
| Blocks architecture or project bootstrap | +3 |
| Could create security/privacy/regulatory failure | +3 |
| Affects multiple downstream decisions | +2 |
| Hard or expensive to reverse | +2 |
| Evidence conflicts | +2 |
| Answer likely available from stakeholder | +1 |
| Can be answered from supplied evidence instead | −3 |
| Cosmetic or deferrable | −2 |
| User already answered it clearly | −5 |
| Question requires speculative detail unavailable now | −2 |

This should rank questions; it should not claim mathematical optimality.

### Question form

Use open questions to discover unknown structure:

> “Walk me through what happens from the moment a technician receives a job until it is closed.”

Use bounded clarification for ambiguity:

> “When you say ‘customers can share projects’, do you mean sharing with another registered user, sharing a public link, or both?”

Use confirmation only when an interpretation matters:

> “I understood that technicians may work for several hours without connectivity. Should creating and editing inspection records remain available during that time?”

Use trade-off questions only after the trade-off becomes real:

> “Keeping all data in the EU excludes some lower-cost services. Is EU-only processing a hard constraint or a preference?”

Avoid questions that merely externalise engineering work:

> “Which database should we use?”

unless the stakeholder actually owns that technical decision.

### Question sequencing

A useful sequence is:

```text
Purpose and actors
        ↓
Core flows and domain vocabulary
        ↓
Critical constraints and exceptions
        ↓
Data / security / integrations
        ↓
Scale / quality / operation
        ↓
Deployment and external accounts
        ↓
Decision conflicts and unresolved risks
        ↓
Readiness confirmation
```

This order is not rigid. A privacy-critical medical application should surface sensitive-data constraints almost immediately.

### Stop/continue criteria

Continue elicitation when an unanswered question:

- could invalidate the proposed system boundary;
- blocks a high-impact architectural decision;
- materially changes security/privacy posture;
- affects whether deployment is viable;
- changes an external dependency or account requirement;
- represents stakeholder conflict requiring authority;
- prevents a requirement from being made verifiable.

Stop asking when:

- remaining uncertainty is low consequence;
- information is unavailable until implementation/prototyping;
- multiple alternatives remain safely reversible;
- the decision can explicitly be deferred;
- additional questioning produces diminishing engineering value;
- the user's burden exceeds the likely value of clarification.

The result should be **conditional readiness**, not “all requirements known.”

Example:

```text
READY FOR BOOTSTRAP

Known:
- system boundary
- primary flows
- deployment class
- sensitive data categories
- initial integration dependencies

Deferred:
- exact CDN provider
- detailed typography
- analytics vendor

Blocking uncertainty:
- none

Documented assumptions:
- peak traffic estimate still provisional
```

### Short interview example

Input:

> “I want a simple portfolio site. Public pages, admin login, projects with images. I already own the domain. It needs Spanish and English. I expect fewer than 5,000 visits/month and want cheap hosting.”

High-value follow-ups may be only:

1. Who edits content—one administrator or several?
2. Does any visitor data need to be collected?
3. Are project images uploaded directly or referenced externally?
4. Is contact functionality needed, and if so where should submissions go?
5. Is the “cheap hosting” requirement a hard monthly budget or simply a preference?

Questions about offline mode, multi-tenant permissions, event buses, complex observability, or enterprise SSO should be skipped unless evidence makes them relevant.

### Complex interview example

Input:

- eight asynchronous voice notes from two founders;
- one paper sketch;
- screenshot of an existing competitor;
- CSV exported from an old system;
- statement that “everything must be instant”;
- uncertain traffic;
- one founder wants AI automation;
- the other says “no customer data may go to AI providers.”

The Skill should not fire a 40-question questionnaire.

It should first reconcile evidence:

```text
1. Determine actors and authority.
2. Extract core workflow from voice notes.
3. Identify visual observations separately from interpretation.
4. Inspect CSV fields for data sensitivity.
5. Register contradiction concerning AI processing.
6. Ask the smallest set of questions that unblock system boundary,
   privacy architecture and data flow.
7. Defer implementation-level choices.
```

## From discovery to technical and deployment requirements

Discovery must eventually cross a boundary. It cannot remain a conversational summary.

The bridge is:

```text
Evidence
  → claims
  → clarified needs
  → constraints
  → candidate requirements
  → verification condition
  → architecture questions
```

### Functional requirements

A functional requirement should describe observable behaviour or capability rather than an implementation choice.

Discovery:

> “When a warehouse loses Wi-Fi, workers still have to finish the current count.”

Candidate requirement:

```text
FR-OFF-01
The system shall allow an authenticated warehouse worker to record
inventory count changes during temporary loss of network connectivity.
```

This is not sufficient yet. Elicitation should discover:

- maximum expected offline duration;
- conflicts between concurrent edits;
- whether authentication must work offline;
- what data must remain available;
- whether synchronisation must be automatic;
- acceptable loss/retry behaviour.

Architecture determines *how* to satisfy the requirement later.

### User flows and edge cases

Core flows should be described before decomposing them.

```text
Technician accepts job
→ opens site
→ records inspection
→ captures photographs
→ obtains customer acknowledgement
→ submits report
```

Questions then target failures and branches:

- no connectivity;
- damaged photo;
- customer refuses acknowledgement;
- job reassigned mid-inspection;
- duplicate submission;
- device lost;
- report amended after submission.

The purpose is not exhaustive state modelling during the interview. It is to surface the edges capable of changing architecture, data design or acceptance tests.

### Quality requirements

Quality requirements should become measurable where the stakeholder can meaningfully specify a threshold.

Poor:

```text
The application must be fast.
```

Better discovery:

```text
Which interaction becomes unacceptable if it takes three seconds?
Under what connection conditions?
How many users are likely to perform it simultaneously?
```

The empirical requirements-quality literature repeatedly studies ambiguity, completeness and consistency, but also cautions that “quality” itself is not represented by one universally validated metric. ([Empirical research on requirements quality: systematic mapping study (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9110500/))

The Skill should therefore avoid fake specificity.

If nobody knows concurrent traffic, it should record:

```yaml
traffic:
  expected_monthly_users: unknown
  stakeholder_estimate: "probably below 20k"
  confidence: low
  design_implication: "avoid architecture dependent on exact forecast"
  revisit: "before production capacity planning"
```

rather than inventing:

```text
The system shall support 10,000 concurrent users.
```

### Important discovery dimensions

Every project does not require every question, but the information model should be capable of representing:

| Dimension | Examples |
|---|---|
| Actors | visitors, administrators, operators, external systems |
| Flows | create, edit, approve, search, pay, export |
| Data | personal, confidential, public, financial, health |
| Quality | latency, availability, accessibility, durability |
| Scale | users, requests, files, geographic distribution |
| Connectivity | always-online, intermittent, offline |
| Locale | languages, currencies, time zones, formatting |
| Accessibility | target users, assistive technology, compliance level |
| Integrations | APIs, webhooks, files, identity providers |
| Security | authentication, roles, privileged actions |
| Privacy | purposes, retention, regional processing |
| Cost | hosting, data transfer, storage, API usage, licences |
| Operations | monitoring, backups, support ownership |
| Deployment | environments, hosting model, domain, certificates |
| Legal/licensing | third-party licences, platform terms |

### Separate business scope from technical implications

The Bootstrap Skill receives business context but should not substitute for business validation.

Example:

> “We expect customers to pay €9.99/month.”

The Skill should not decide whether €9.99 is commercially viable.

It **should** ask technical questions if subscriptions are in scope:

- recurring billing or one-off payments?
- trial periods?
- tax/VAT handling?
- refunds?
- subscription state authoritative in the payment provider or local database?
- webhook processing?
- account deletion implications?
- development sandbox availability?

The boundary is:

```text
"Should this pricing strategy exist?"
    → business validation.

"What technical behaviour follows if subscriptions exist?"
    → technical discovery.
```

### Deployment is part of discovery

For an online system, “where and how will this run?” is not an afterthought.

The interview should identify enough deployment context to constrain later architecture:

```yaml
deployment_profile:
  service_type: public_web_application
  environments:
    - development
    - preview
    - production
  domain:
    owned: true
    registrar: unknown
  hosting:
    selected: false
  region_constraint:
    eu_only: provisional
  expected_scale:
    low_to_medium
  persistent_storage: required
  backups: required
  ci_cd: required
  observability: basic
```

Questions should surface:

**Hosting**
- Is there an existing cloud/vendor account?
- Is self-hosting required or prohibited?
- Is vendor lock-in important?
- Are managed services acceptable?

**Domains and DNS**
- Does the domain already exist?
- Who controls the registrar?
- Are subdomains required?

**Accounts and plans**
- Which external accounts must the user create?
- Does a suitable free tier exist?
- What happens if the free tier is exceeded?
- Does production usage require a paid plan?

**Cost categories**
- compute;
- database;
- object storage;
- bandwidth/CDN;
- email/SMS;
- observability;
- backups;
- third-party API use;
- domain/certificate where applicable;
- paid developer programmes.

The Skill should verify volatile pricing on the web at project-bootstrap time rather than store it as durable knowledge.

**Secrets**
- API keys;
- database credentials;
- OAuth client secrets;
- signing keys;
- deployment credentials.

OWASP recommends centralised secret-management practices and explicitly advises against hardcoding secrets in repositories or CI/CD configuration. Current guidance also encourages short-lived credentials/workload identity where supported. ([OWASP MCP Security](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html))

Therefore the generated project may include:

```dotenv
# .env.example
DATABASE_URL=
EMAIL_API_KEY=
OAUTH_CLIENT_ID=
OAUTH_CLIENT_SECRET=
```

but never actual values.

The Skill may say:

```text
Before production deployment, create an account with the selected email
provider and store EMAIL_API_KEY in the deployment platform's secret store.
Do not commit it to Git.
```

It must **not collect the secret for packaging in the ZIP**.

**Release environments**
- local development;
- test/CI;
- preview/staging if useful;
- production.

**Backups and recovery**
- which data matters;
- acceptable loss;
- restore ownership;
- retention.

**Observability**
- logs;
- error reporting;
- metrics;
- alerts;
- privacy constraints on telemetry.

**Regional/compliance concerns**
must be raised where data location, regulated processing, contractual restrictions or applicable law make them relevant. For EU personal data, GDPR requirements such as purpose limitation, minimisation and privacy by design may directly affect architecture and service selection. ([EU GDPR consolidated text](https://eur-lex.europa.eu/eli/reg/2016/679/oj))

The Skill does not deploy. It produces the specifications and backlog that make deployment an explicit part of development.

### When elicitation ends and architecture begins

Discovery should normally determine:

```text
WHAT must be possible
WHO needs it
UNDER WHAT constraints
HOW good it must be
WHAT evidence supports the claim
WHAT remains uncertain
```

Architecture then determines:

```text
HOW the system will satisfy those requirements
```

Some technical facts legitimately enter discovery:

> “The organisation mandates PostgreSQL because its operations team supports no other database.”

That is a constraint.

But:

> “This looks like a PostgreSQL app.”

is a proposal.

The distinction must remain visible.

## Capability discovery, MCP, and collaborative authority

### Capability before mechanism

During discovery, the Skill may conclude that development would benefit from a capability such as:

- querying an external API;
- manipulating design files;
- browser automation;
- database inspection;
- cloud deployment inspection;
- issue-tracker access;
- documentation retrieval.

It should then evaluate mechanisms.

| Mechanism | Prefer when |
|---|---|
| Library | Capability belongs inside application/runtime code |
| SDK | Vendor/service integration is part of the product |
| REST/GraphQL/API | Direct protocol integration is simple and stable |
| CLI | Developer/operator automation is the main use |
| Specialised Skill | Reusable reasoning/workflow expertise is needed |
| MCP server | Development agents need structured access to external tools/data |
| Human workflow | Automation creates disproportionate security or complexity |

A critical distinction is:

```text
Runtime product dependency
        ≠
Development-time agent capability
```

Example: a design MCP server used by coding agents does not necessarily become a production dependency of the application.

### MCP landscape as of 11 November 2026

The official MCP Registry is active and provides a public registry service for discovering MCP servers. ([MCP Registry](https://registry.modelcontextprotocol.io/docs))

The current MCP specification release is dated **28 July 2026**; the project's official announcement describes major changes including a stateless protocol core, updated authorisation mechanisms, formal extensions and updated Tier-1 SDKs. ([MCP specification](https://modelcontextprotocol.io/specification/2026-07-28))

The two community directories explicitly requested for this project also remain live as of the report date:

- `mcpservers.org` exposes a browsable catalogue and official-server listings. ([MCP Registry](https://registry.modelcontextprotocol.io/docs))
- `mcp.directory` exposes a searchable catalogue of MCP servers and agent skills. ([MCP specification (contextual source)](https://modelcontextprotocol.io/))

These directories are **discovery sources, not trust anchors**.

### MCP evaluation protocol

Before recommending an MCP server, evaluate:

| Dimension | Questions |
|---|---|
| Provenance | Who publishes it? Is there a verifiable upstream repository/vendor? |
| Maintenance | Is it actively maintained? Recent compatible releases? |
| Protocol version | Which MCP specification/SDK does it support? |
| Permissions | Which files, APIs, accounts or services can it access? |
| Credentials | How are tokens obtained and stored? |
| Transport | Local stdio? HTTP? Remote managed service? |
| Security | Tool poisoning, prompt injection, sandbox escape, confused deputy? |
| Supply chain | Package provenance, dependencies, integrity verification? |
| Licence | Is use compatible with the project? |
| Versioning | Can a reviewed version or digest be pinned? |
| Data handling | What leaves the machine or organisation? |
| Human approval | Which actions require confirmation? |

OWASP's current MCP security guidance identifies tool poisoning, rug pulls, cross-server interactions, excessive permissions, data exfiltration, confused-deputy problems, local-server host access, and public-registry supply-chain risks. It recommends source verification, least privilege, review of tool definitions, credential isolation, human approval for consequential operations, and avoiding automatic installation from untrusted web content. ([OWASP MCP Security](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html); [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))

This directly implies:

> **Discovery may recommend and prepare an MCP integration; it should not silently install or authorise it.**

A generated `docs/MCP.md` might contain:

```markdown
# Development Capabilities

## Candidate: Vendor X Design MCP

Purpose:
Allow development agents to inspect approved design artefacts.

Classification:
Development-time capability; not a runtime application dependency.

Source:
Official vendor repository.

Required permissions:
Read-only access to selected design workspace.

Credentials:
User-created OAuth authorisation; never committed to repository.

Status:
Proposed — human approval required before installation.

Review:
- Publisher verified
- Licence reviewed
- MCP protocol compatibility checked
- Permissions reviewed
- Version pinning available
```

A client configuration may be provided as an example with placeholders, but no real token should be embedded.

### Human–AI collaboration protocol

The agent should continuously separate three forms of authority:

```text
Evidence authority:
"Is this source credible?"

Domain authority:
"Does this stakeholder know this part of the problem?"

Decision authority:
"May this stakeholder commit the project to this choice?"
```

These often differ.

A security specialist may be the domain authority on credential handling but not the budget owner. The founder may approve spend but lack authority to reinterpret a statutory requirement.

### Turn-taking and asynchronous batches

Successive voice messages should normally be treated as a **batchable evidence stream**.

Poor behaviour:

```text
User sends voice 1.
Agent asks 5 questions.
User sends voice 2 that answers 4 of them.
```

Better:

```text
User indicates more notes are coming.
Agent ingests them.
Agent maintains provisional claims.
Agent waits until a natural batch boundary.
Agent asks only unresolved high-value questions.
```

When the user has not indicated whether more material is coming, a lightweight conversational probe is appropriate rather than a long questionnaire.

### Multilingual elicitation

The project language and stakeholder language need not be identical.

The Skill should preserve important source phrases where translation could alter meaning:

```yaml
source_text: "Tiene que funcionar sin cobertura."
language: es-ES

working_translation:
  text: "It has to work without network coverage."
  interpretation_confidence: high
```

Technical terminology should be normalised carefully rather than translated mechanically. Domain definitions belong in the project vocabulary.

### Memory and context management

The working conversation should not become the only memory of the project.

After meaningful increments, durable facts should migrate into explicit artefacts:

```text
conversation
    ↓
claim ledger
    ↓
requirements / decisions / unresolved questions
    ↓
handoff summary
```

This makes collaboration provider-agnostic: another agent can reconstruct the current state without receiving an opaque hidden conversational memory.

## Worked scenarios and evaluation

### Scenario A — structured public web application brief

#### Input

The stakeholder provides a concise document:

```text
Photography portfolio.
Public site, no visitor accounts.
One administrator.
Projects contain text + photographs.
Spanish and English.
Contact form.
Existing domain.
Budget target below €20/month.
Roughly 3,000 visitors/month.
Would prefer not to manage servers.
```

#### Source interpretation

| Claim | Class | Confidence |
|---|---|---|
| Public visitors do not need accounts | stated fact | high |
| One administrator edits content | stated fact | high |
| Multilingual content required | constraint | high |
| Managed hosting preferred | preference | high |
| €20/month | provisional constraint | medium |
| 3,000 visits/month | estimate | medium |

#### Questions skipped

The Skill should **not** ask about:

- enterprise SSO;
- offline mobile use;
- multi-tenant isolation;
- Kafka;
- Kubernetes;
- complex role hierarchies;
- native mobile push.

Nothing currently justifies them.

#### Questions worth asking

```text
Q1. Does the administrator upload full-resolution photographs directly,
or will images already exist in another service?

Q2. Should contact-form submissions be stored in the application,
forwarded by email, or both?

Q3. Does the site need analytics or any other visitor tracking?

Q4. Is €20/month a hard production ceiling or a target preference?

Q5. Should editors manage Spanish and English versions independently,
or must both languages always exist before publication?
```

#### Derived technical discovery

```yaml
system:
  class: content-driven-public-web-app

actors:
  visitor:
    authentication: none
  administrator:
    count: 1
    authentication: required

quality:
  accessibility: required
  seo: important
  multilingual: [es, en]

deployment:
  managed_service_preferred: true
  existing_domain: true
  budget_target: "<= EUR 20/month"
  deployment_execution_by_skill: false

data:
  public_content: true
  admin_identity: personal_data
  contact_submissions: pending_decision
```

#### Readiness

Architecture can begin once contact-form handling and image-storage implications are resolved. Exact framework, database, image CDN and hosting vendor remain architecture decisions.

### Scenario B — ambiguous voice notes plus sketch

#### Inputs

`voice-01`:

> “It's basically for technicians to inspect solar installations. They get their jobs in the morning and fill everything in on site.”

`voice-02`:

> “Coverage can be terrible in rural areas, but normally they have their phone.”

`voice-03`:

> “Photos are important because the office checks them later.”

Sketch:

```text
[ Jobs ]
   |
[ Inspection ]
   |
[ Photos ]
   |
[ Sign ]
```

`voice-04`:

> “The client signs and then the office closes it.”

#### Initial evidence extraction

```text
Observed from sketch:
A sequence labelled Jobs → Inspection → Photos → Sign.

Interpretation:
Likely represents a primary workflow.

Inference:
Photos and signature may belong to an inspection report.

Uncertainty:
Whether each stage must work offline.
Whether "signature" is legal acknowledgement or simple confirmation.
Whether office staff use same application.
Whether photographs are synchronised immediately.
```

#### Adaptive questions

The first question should target the architectural consequence of poor connectivity:

> **Agent:** You mentioned that coverage can be very poor. Which parts of the job must technicians still be able to complete without any connection: opening assigned jobs, filling the inspection, taking photos, obtaining the customer's signature, or all of them?

> **Stakeholder:** All of it except getting new jobs. They get the day's jobs before leaving.

That single answer resolves several potential questions.

> **Agent:** Then I will treat the day's assigned jobs and the full inspection workflow as offline-capable, with synchronisation when connectivity returns. One important edge case remains: if the office changes a job while the technician is offline, should the technician's completed inspection win automatically, or should the conflict be reviewed?

> **Stakeholder:** Reviewed. We can't lose the inspection.

> **Agent:** Understood. About the customer's signature: is it intended as legally binding electronic signature, or as evidence that the customer has seen the completed visit?

> **Stakeholder:** Just acknowledgement for now.

> **Agent:** Good. I won't assume a qualified or regulated e-signature service. Does the office need a separate desktop-oriented interface to review photos and close the job?

> **Stakeholder:** Yes.

This excerpt demonstrates three behaviours:

1. questions are driven by consequence;
2. later questions reuse answers rather than restating the questionnaire;
3. the agent explicitly prevents a strong architectural interpretation (“regulated e-signature”) from entering the project without evidence.

#### Derived requirements candidates

```text
FR-OFF-01
A technician shall be able to access previously assigned jobs without
network connectivity.

FR-OFF-02
A technician shall be able to create and modify an inspection,
attach photographs and capture customer acknowledgement while offline.

FR-SYNC-01
The system shall synchronise locally completed inspections after
connectivity returns.

FR-SYNC-02
A conflicting office-side modification shall not silently overwrite
a technician's completed offline inspection.

FR-REV-01
Office reviewers shall be able to inspect submitted evidence and
close a job.
```

#### Deployment implications

The final service is online even though field use is partly offline. The bootstrap must therefore include future work for:

- server-side sync API;
- conflict policy;
- durable media upload;
- authenticated device/user access;
- production deployment;
- backups;
- monitoring;
- secure secrets/configuration.

But it should not deploy any of them.

#### Readiness

Ready for architecture with one explicit unresolved question: maximum expected offline period/data volume, because this may influence local storage and synchronisation design.

### Scenario C — complex online service with contradictory stakeholders

#### Evidence

Founder:

> “We want AI to automatically classify all uploaded customer documents.”

Privacy lead:

> “Customer documents must never leave our controlled EU infrastructure.”

Operations lead:

> “We don't want to operate GPUs ourselves.”

Sales lead:

> “We promised customers that processing happens in Europe.”

CTO:

> “I'd rather use a managed external model API.”

#### Claim ledger

```yaml
- id: C-101
  type: proposal
  owner: founder
  statement: "Automatically classify uploaded documents using AI."

- id: C-102
  type: constraint
  owner: privacy-lead
  statement: "Customer document contents must not leave controlled EU infrastructure."

- id: C-103
  type: preference
  owner: operations
  statement: "Avoid self-operated GPU infrastructure."

- id: C-104
  type: stated_fact
  owner: sales
  statement: "Customers have been promised European processing."
  verification: "contract language not yet inspected"

- id: C-105
  type: preference
  owner: CTO
  statement: "Prefer managed model API."
```

#### The correct response is not vendor selection

The key questions are:

```text
1. Is "controlled EU infrastructure" a contractual/legal requirement,
an internal security policy, or the privacy lead's interpretation?

2. Does the customer commitment require EU data residency,
EU processing, EU-owned provider, or something else?

3. May data be sent to a managed AI service if processing and retention
remain contractually restricted to approved EU regions?

4. Is automatic classification mandatory for v1,
or could human-assisted classification satisfy the initial scope?
```

The Skill should request the actual contractual or policy source if available rather than choose a model provider based on hearsay.

#### Decision gate

Architecture selection is blocked until the external-processing constraint is clarified because the answer can radically change:

- model hosting;
- vendor eligibility;
- infrastructure cost;
- operational ownership;
- data flows;
- security controls.

#### Possible outcome

Suppose the contract says only that personal data must remain in approved EU data centres and an external processor is allowed under specified terms.

Then the original conflict dissolves partly:

```text
"Managed external model" and "EU-only processing"
may be simultaneously feasible.
```

The Skill can now research candidate services during architecture selection.

If the contract forbids external processing entirely, the contradiction remains real and requires a human decision about scope, operations or AI functionality.

#### Readiness

Not ready for stack selection until the policy authority is resolved.

Ready, however, to produce:

- system context;
- data-classification assumptions;
- unresolved policy question;
- candidate AI requirement;
- architectural decision gate;
- backlog item for approved AI-processing approach.

### Failure modes

#### Hallucinated requirement

Input:

> “Users upload invoices.”

Bad extraction:

```text
Users authenticate with Google and upload PDF invoices up to 10 MB.
```

Only the upload is evidenced.

#### Transcription error

Audio:

> “The administrator can **not** delete an approved report.”

Transcript:

> “The administrator can delete an approved report.”

Mitigation: consequential negations, permissions, quantities and dates receive source verification.

#### Visual overinterpretation

Sketch contains a bell icon.

Bad requirement:

```text
System shall provide real-time push notifications.
```

Correct representation:

```text
Observed: bell-shaped icon.
Interpretation: possibly notifications.
Status: unconfirmed.
```

#### Premature stack fixation

Stakeholder:

> “My friend said Supabase is easy.”

Wrong:

```text
Constraint: Supabase.
```

Better:

```text
Preference/proposal: Supabase.
Reason to investigate: stakeholder values low operational burden.
```

#### Specification theatre

A 60-page PRD can still hide:

```text
Who owns the production account?
What data are sensitive?
What happens offline?
Who can approve payment?
How is a failed deployment recovered?
```

Document volume is not readiness.

#### Over-questioning

The Skill asks:

> “How many requests per second?”

to a founder who has not launched and cannot reasonably know.

Correct approach:

```text
Expected early scale unknown.
Do not design around a fabricated traffic number.
Choose an architecture tolerant of plausible early growth.
Reassess before production capacity planning.
```

#### Insecure MCP adoption

The Skill finds an attractive MCP server in a directory and automatically installs it with filesystem and cloud credentials.

This conflicts with current OWASP guidance on supply-chain risk, excessive permissions and MCP installation security. ([OWASP MCP Security](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html))

### Evaluation metrics

Process quality should be measured independently from prose quality.

Recommended metrics:

| Metric | Interpretation |
|---|---|
| Source coverage | Important input artefacts actually considered |
| Provenance coverage | Consequential claims traceable to evidence |
| Unsupported-claim rate | Requirements with no valid source/inference chain |
| Contradiction recall | Known conflicts identified |
| Redundant-question rate | Questions whose answer already existed |
| Question utility | Asked questions that changed/clarified engineering state |
| User burden | Turns/questions/time required |
| Decision-authority accuracy | Decisions attributed to authorised parties |
| Uncertainty preservation | Unknowns represented rather than fabricated |
| Requirement verifiability | Candidate requirements with observable acceptance evidence |
| Architecture leakage | Premature solution choices disguised as requirements |
| Multimodal fidelity | Interpretations consistent with original audio/image/document |
| Deployment coverage | Required operational/deployment constraints discovered |
| Secret-handling safety | No real secret collected or packaged |
| Tool-recommendation safety | Candidate MCP/tool reviewed before authorisation |

Some can be computed automatically; others require human evaluation.

### Human evaluation rubric

Expert reviewers can score 1–5:

```text
A. Faithfulness to evidence
B. Coverage of consequential uncertainty
C. Neutrality of questions
D. Relevance of questions
E. Respect for stakeholder authority
F. Preservation of contradictions
G. Technical readiness
H. Deployment readiness
I. Security/privacy awareness
J. Interview burden
```

### Controlled experiments for Skill development

These are **research proposals**, not established empirical results.

#### Experiment: adaptive vs fixed questionnaire

Randomise identical project briefs across:

```text
A. fixed comprehensive questionnaire
B. adaptive evidence-aware interview
```

Measure:

- number of questions;
- uncovered seeded requirements;
- seeded contradictions detected;
- unsupported assumptions;
- perceived burden;
- time to readiness;
- architecture-critical omissions.

Hypothesis: adaptive elicitation will reduce redundant questions while preserving or improving discovery quality.

#### Experiment: text transcript vs source-linked multimodal evidence

Conditions:

```text
A. ASR transcript only
B. transcript + timestamps + audio verification
```

Seed difficult proper names, negations and numerical values.

Measure requirement transcription errors.

#### Experiment: epistemic ledger vs plain summary

Provide agents with:

```text
A. narrative project summary
B. claim ledger with source/status/owner/conflicts
```

Then introduce changed requirements.

Measure:

- obsolete decisions retained;
- contradictions detected;
- provenance accuracy;
- downstream specification errors.

#### Experiment: MCP recommendation safety

Seed candidate servers with combinations of:

- verified vendor source;
- abandoned repository;
- excessive permissions;
- ambiguous publisher;
- malicious-looking configuration;
- broad OAuth scopes.

Measure whether the Skill recommends, rejects, or escalates appropriately.

### Scenario D — intermittent connectivity in an offline field or creative project (editorial supplement)

This additional **hypothetical** discovery exercise tests whether the same method works when a web-first mental model is inappropriate. Suppose a small team says: *“The field app should always work, and when devices reconnect everything should be up to date.”* Those words do not establish a persistence technology, synchronization strategy, supported device, or acceptable conflict outcome.

**Available evidence:** a voice note describes unreliable network coverage; a screenshot depicts a locally editable item list; an existing CSV export includes stable-looking item identifiers. The screenshot does not prove local storage or actual offline support, and the CSV identifiers may be transient. The first job is to preserve those observations separately from interpretations.

| Claim or question | Status | Who could resolve it? | Consequence |
|---|---|---|---|
| Device operators may be offline during primary tasks | stakeholder statement | field operator | may require local working state |
| Editing must continue while disconnected | **unconfirmed inference** | product owner + representative operator | architectural driver if confirmed |
| Two devices may edit the same record offline | open question | operations/domain owner | conflict and ownership semantics |
| Data may be lost when a device is replaced | risk | domain/security owner | retention, recovery and encryption choices |
| All data can be shared with a cloud AI service | **not approved** | privacy/data owner | tool-access boundary |

**Minimum elicitation sequence:** ask for one complete offline workflow and a failure case; identify which events can occur locally; ask who or what is authoritative if changes conflict; inspect the CSV provenance; clarify maximum tolerated unavailability and acceptable data loss; and identify any protected data before deciding whether any sample may be sent to an external agent. Represent the resulting state transitions with a small table or diagram if lifecycle ambiguity persists.

**Bootstrap outcome:** a reviewed set of offline behavior requirements *if the stakeholder confirms them*, a synchronization decision explicitly deferred pending conflict evidence, a planned test for disconnected editing and resynchronization, a data-handling question, and a human-review gate before selecting local storage or a sync provider. Do **not** invent a SQLite schema, mobile SDK, IoT broker or executable synchronization test at this discovery stage.

**Falsification target for the future Skill:** a provider-agnostic agent should produce the same critical offline/conflict questions even when the source material consists only of a voice note, screenshot and CSV. Compare against a simple unstructured-interview baseline; record missed questions and unnecessary architecture commitments.

## Operational synthesis for the SDD Bootstrap Skill

### The core discovery loop

The process can be implemented conceptually as:

```text
INGEST
  ↓
NORMALISE SOURCES
  ↓
EXTRACT OBSERVATIONS / CLAIMS
  ↓
CLASSIFY EPISTEMIC STATUS
  ↓
RECONCILE DUPLICATES / CONTRADICTIONS
  ↓
MAP CONSEQUENTIAL UNCERTAINTIES
  ↓
SELECT HIGHEST-VALUE RESOLUTION ACTION
  ↓
ASK / INSPECT / RESEARCH / DEFER
  ↓
UPDATE CLAIM STATE
  ↓
CHECK READINESS GATES
  ↓
HAND OFF TO REQUIREMENTS + ARCHITECTURE
```

Illustrative pseudocode:

```python
while True:
    evidence = ingest_new_material()

    claims = extract_claims(evidence)
    ledger.merge(claims)

    ledger.detect_conflicts()
    ledger.mark_superseded_claims()

    unknowns = derive_consequential_unknowns(
        claims=ledger.current(),
        target_artifacts=bootstrap_targets
    )

    if readiness_gate_passes(ledger, unknowns):
        break

    candidates = []

    for u in unknowns:
        candidates.extend(
            possible_resolution_actions(u)
        )

    ranked = rank_by_heuristic(
        candidates,
        consequence=True,
        uncertainty=True,
        dependency=True,
        irreversibility=True,
        decision_proximity=True,
        user_burden=True,
        answerability=True
    )

    action = choose_best(ranked)

    if action.kind == "inspect_existing_evidence":
        inspect(action.source)

    elif action.kind == "web_verify":
        research_authoritative_source(action.topic)

    elif action.kind == "ask":
        ask_neutral_bounded_question(action.question)

    elif action.kind == "human_decision":
        present_options_and_request_authority(action)

    elif action.kind == "defer":
        ledger.record_deferred(action.issue)
```

Again, the ranking model is a design recommendation, not a validated quantitative optimiser.

### Minimal ambiguity and decision ledger

```markdown
# Discovery Ledger

## Open Questions

### Q-007 — Offline authentication
**Why it matters:** determines whether field users can enter the application
after credentials expire while offline.

**Evidence:** poor connectivity confirmed; offline re-login not discussed.

**Impact:** high
**Owner:** product + security
**Status:** unresolved

## Assumptions

### A-003 — Initial launch scale
Assume fewer than 5,000 monthly active users for bootstrap sizing only.

**Source:** founder estimate
**Confidence:** low
**Revisit:** before production capacity testing

## Conflicts

### C-002 — External AI processing
Privacy policy interpretation conflicts with proposed managed AI API.

**Resolution required before:** AI architecture selection.

## Decisions

### D-005 — Customer acknowledgement
Customer signature in v1 is acknowledgement, not regulated electronic signing.

**Approved by:** product owner
**Evidence:** interview-02 00:18:44
**Date:** 2026-11-11
```

### Discovery readiness checklist

The interview is sufficiently complete for bootstrap when the following are **known, deliberately deferred, or explicitly blocked**:

```text
[ ] System purpose and boundary understood
[ ] Primary stakeholder groups identified
[ ] Decision authority identified for consequential areas
[ ] Core user/system flows understood
[ ] Domain vocabulary sufficient to avoid major semantic ambiguity
[ ] Critical edge cases surfaced
[ ] Data categories understood at useful level
[ ] Sensitive/regulated data identified
[ ] Authentication/authorisation needs understood
[ ] Important external integrations identified
[ ] Connectivity/offline requirements addressed where relevant
[ ] Accessibility/localisation needs addressed where relevant
[ ] Material quality attributes surfaced
[ ] Scale assumptions recorded without invented precision
[ ] Deployment class identified
[ ] Required external accounts/services identified or deferred
[ ] Cost categories visible
[ ] Secrets handling requirements identified
[ ] Environments/CI-CD expectations identified
[ ] Backup/observability requirements surfaced
[ ] Regional/compliance constraints surfaced
[ ] Runtime dependencies separated from developer-agent capabilities
[ ] MCP/tool candidates reviewed rather than blindly trusted
[ ] Contradictions recorded
[ ] Assumptions recorded
[ ] Blocking decisions assigned to owners
[ ] Remaining uncertainty acceptable for architecture work
```

Readiness is **not**:

```text
"Every box checked with a final answer."
```

It is:

```text
"No consequential uncertainty is silently pretending to be a decision."
```

### Handoff into requirements and architecture

Discovery should end with a structured handoff such as:

```yaml
discovery_handoff:
  status: architecture_ready

  confirmed:
    - primary actors
    - core workflows
    - offline field requirement
    - sensitive data categories
    - production deployment required

  decisions:
    - id: D-005
      summary: "Customer signature is acknowledgement only."

  assumptions:
    - id: A-003
      summary: "Initial launch scale is low."
      revisit: "capacity planning"

  unresolved_nonblocking:
    - analytics provider
    - exact CDN choice

  blockers:
    []

  architecture_questions:
    - offline persistence and sync strategy
    - authentication/session model
    - image storage strategy
    - deployment platform
    - backup strategy

  capability_research:
    - purpose: "access approved design system during development"
      candidate_mechanisms:
        - vendor MCP
        - vendor CLI
      status: investigate

  first_specs:
    - "offline inspection workflow"
    - "synchronisation conflict handling"
    - "office review workflow"
    - "production deployment preparation"
```

The resulting bootstrap can then create prioritised backlog/spec work such as:

```text
P0 — establish application skeleton
P0 — implement identity boundary
P0 — implement domain persistence
P0 — implement core vertical slice
P0 — define production deployment pipeline
P1 — implement observability baseline
P1 — configure backup/restore
P1 — integrate approved development MCP
```

The user should receive an explicit handoff message stating that these are **development-ready specifications and next steps**, not evidence that the application, APK or production deployment already exists.

### Knowledge freshness protocol

This project explicitly requires the Skill to recognise that its knowledge base ages.

That requirement is justified by the present research itself. Two examples discovered during this investigation are enough to show why:

- ISO/IEC/IEEE 29148:2018 is still the published standard, but a replacement DIS is already in enquiry in 2026. ([ISO DIS 29148](https://www.iso.org/standard/94091.html))
- MCP's current protocol specification changed materially on 28 July 2026. ([MCP specification](https://modelcontextprotocol.io/specification/2026-07-28))

Knowledge should therefore carry a volatility class.

```yaml
knowledge_item:
  topic: "requirements engineering standard"
  volatility: slow
  checked_at: 2026-11-11
  authoritative_source: ISO
  status:
    published: "ISO/IEC/IEEE 29148:2018"
    forthcoming: "ISO/IEC/IEEE DIS 29148 edition 3"
```

Suggested classes:

| Class | Examples | Check policy |
|---|---|---|
| Stable | interviewing principles, provenance, stakeholder viewpoints | periodic |
| Slow-moving | standards, accessibility guidance | before major KB revision |
| Medium | security guidance, platform capabilities | when project-relevant |
| Fast | prices, free tiers, framework versions, API limits | always at bootstrap |
| Very fast | incidents, deprecations, service availability | immediately before consequential use |

#### Web-check source order

For volatile claims:

```text
1. Applicable law / standard / protocol authority
2. Official vendor or maintainer documentation
3. Primary research
4. Maintainer release/repository metadata
5. Trusted secondary technical source
6. Community directory
7. Forum/social material only as leads
```

A community page should never override official documentation without explicit reason.

#### Disagreement handling

When sources disagree:

```text
Do not silently choose the most convenient statement.
```

Instead:

```yaml
freshness_conflict:
  claim: "Feature X is supported"
  source_a:
    authority: vendor_documentation
    date: 2026-10-21
    says: true
  source_b:
    authority: old_project_kb
    date: 2025-03-04
    says: false

resolution:
  runtime_use: use_current_official_information
  kb_action: propose_update
  automatic_kb_rewrite: false
```

The Skill may use fresher authoritative information for the current bootstrap, but changes to its durable knowledge base should be **proposed for human approval rather than silently rewritten**.

### Stable conclusions for Skill v0.1

The strongest actionable conclusions from this research are:

1. **Treat all inputs as evidence objects with provenance, not merely conversation context.**
2. **Separate observations, interpretations, assumptions, proposals and approved decisions.**
3. **Optimise interviewing for consequential uncertainty rather than questionnaire coverage.**
4. **Use source inspection, observation and web research as alternatives to asking the user questions.**
5. **Never infer authority from who spoke first or most confidently.**
6. **Preserve contradictions until evidence or an authorised decision resolves them.**
7. **Treat ASR, diarisation, OCR and multimodal interpretation as fallible transformations.**
8. **Ask about architecture-changing needs early: offline behaviour, sensitive data, integrations, scale, security, regional constraints and deployment.**
9. **Treat deployment as part of the solution boundary but never execute deployment during bootstrap.**
10. **Never collect or package production secrets.**
11. **Discover developer capabilities first; then choose between library, SDK, API, CLI, Skill, MCP or human workflow.**
12. **Treat MCP registries/directories as discovery mechanisms, not trust authorities.**
13. **Allow MCP configuration to be prepared, but require review/authorisation before installation or credential access.**
14. **Stop interviewing when remaining uncertainty is safe to defer—not when every conceivable question has an answer.**
15. **Handoff must tell downstream agents exactly what is confirmed, assumed, unresolved, decided and blocking.**
16. **The knowledge base itself needs freshness metadata and a web-verification policy.**

### Annotated source map

**Requirements engineering standards and bodies of knowledge.** ISO/IEC/IEEE 29148:2018 remains the principal published requirements-engineering standard as of the report date; the third-edition DIS is under development. These sources anchor terminology and life-cycle treatment of requirements. ([ISO 29148:2018](https://www.iso.org/standard/72089.html); [ISO DIS 29148](https://www.iso.org/standard/94091.html)) SWEBOK V4.0a supplies a broader contemporary software-engineering body of knowledge and explicitly covers requirements elicitation, analysis, specification and validation. ([SWEBOK V4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering))

**Human-centred discovery.** ISO 9241-210:2019 provides the enduring human-centred design foundation; contextual-inquiry guidance demonstrates why observing work in context can reveal information that retrospective questioning misses. ([ISO 9241-210:2019](https://www.iso.org/standard/77520.html))

**Elicitation techniques and context dependence.** The systematic literature review by Méndez Fernández and related work on technique selection support the conclusion that elicitation methods must be matched to project, stakeholder, environmental and knowledge characteristics rather than applied universally. ([Elicitation techniques SLR (2018)](https://doi.org/10.1049/iet-sen.2017.0144); [Elicitation technique selection (2014)](https://doi.org/10.1016/j.infsof.2014.01.009))

**Interviewing and requirements evolution.** Empirical research shows that interviews shape requirements and that domain knowledge, communication structure, prompting and review matter. ([Requirements evolution during elicitation (empirical study, 2022)](https://link.springer.com/article/10.1007/s00766-022-00383-7); [Procedural prompting in elicitation (2007)](https://doi.org/10.1111/j.1365-2575.2006.00240.x))

**Human–AI elicitation.** 2025 IEEE RE research on LLMREI and follow-up question generation provides early empirical evidence that language models can support context-dependent requirements interviews, but sample sizes and simulated/controlled settings justify caution rather than autonomous authority. ([LLMREI (2025)](https://arxiv.org/abs/2507.02564); [Follow-up question generation (2025)](https://arxiv.org/abs/2507.02858)) A 2026 systematic mapping study shows rapid growth in AI-assisted elicitation while retaining stakeholder validation as a core stage. ([Automated elicitation mapping study (2026)](https://www.mdpi.com/2078-2489/17/8/777))

**Cognition and bias.** Systematic work on cognitive bias in software engineering and experimental anchoring research supports explicit countermeasures against premature fixation and leading questions. ([Cognitive biases in software engineering (IEEE TSE)](https://doi.org/10.1109/TSE.2018.2877759); [Numerical anchors in software effort estimates (2016)](https://doi.org/10.1016/j.jss.2015.03.015))

**Speech and multimodal reliability.** ASR disparity research demonstrates that transcription errors may vary systematically across populations; speaker-diarisation literature documents continuing real-world limitations. ([PNAS ASR disparity (2020)](https://doi.org/10.1073/pnas.1915768117); [Speaker diarization review (2025)](https://doi.org/10.3390/app15042002)) 2025 multimodal benchmarks document remaining visual, OCR and cross-modal hallucination problems, supporting explicit provenance and uncertainty rather than treating model perception as ground truth. ([MERLIM (CVPRW 2025)](https://openaccess.thecvf.com/content/CVPR2025W/BEAM/html/Villa_Behind_the_Magic_MERLIM_Multi-modal_Evaluation_Benchmark_for_Large_Image-Language_CVPRW_2025_paper.html); [OCRBench v2 (NeurIPS 2025)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8c2e6bb15be1894b8fb4e0f9bcad1739-Abstract-Datasets_and_Benchmarks_Track.html))

**Accessibility.** W3C/WCAG guidance supports making audio/video information accessible through appropriate alternatives and reinforces the value of transcripts while preserving media semantics. ([W3C media alternatives](https://www.w3.org/WAI/media/av/); [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/))

**Privacy.** NIST privacy engineering and the GDPR support minimisation, explicit risk management, purpose limitation and privacy-by-design thinking when ingesting potentially sensitive discovery material. ([NIST Privacy Framework](https://www.nist.gov/privacy-framework); [EU GDPR consolidated text](https://eur-lex.europa.eu/eli/reg/2016/679/oj))

**Information value.** Formal VOI literature provides the conceptual foundation for asking whether additional information is worth acquiring before making a decision; software-architecture research has applied this reasoning directly to uncertainty in requirements and architecture. The scoring algorithm in this chapter is nevertheless a heuristic adaptation rather than a validated VOI implementation. ([Letier, Stefan & Barr — Uncertainty, Risk, and Information Value (ICSE 2014)](https://doi.org/10.1145/2568225.2568239))

**Collaborative modelling.** Story mapping and EventStorming are useful practitioner-developed techniques for maintaining user-journey context and collectively exploring domain behaviour; they should be available to the Skill as situational techniques, not mandatory rituals. ([Story mapping (Patton)](https://jpattonassociates.com/user-story-mapping/); [EventStorming (Brandolini)](https://www.eventstorming.com/))

**MCP ecosystem.** The official MCP Registry is operational, the current protocol release is 2026-07-28, and the community directories `mcpservers.org` and `mcp.directory` remain active as of 11 November 2026. ([MCP Registry](https://registry.modelcontextprotocol.io/docs); [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28))

**MCP and secrets security.** Current OWASP guidance provides the strongest immediately actionable security baseline for MCP evaluation and reinforces least privilege, source verification, secure credential management, explicit consent and supply-chain review. ([OWASP MCP Security](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html); [OWASP prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/))

### Research limitations

The evidence base for traditional requirements engineering is much deeper than that for AI-led multimodal elicitation. In particular, current research does **not** establish a universally optimal AI interviewing policy, reliable numerical information-gain score, or general proof that autonomous LLM interviewers outperform experienced requirements engineers. The recent IEEE studies are promising but too limited to support such claims. ([Follow-up question generation (2025)](https://arxiv.org/abs/2507.02858); [LLMREI (2025)](https://arxiv.org/abs/2507.02564))

Multimodal model capability is changing rapidly. Benchmark results from 2025 establish that OCR, visual grounding and cross-modal hallucination remain material concerns; they should not be interpreted as permanent performance bounds for future models. ([OCRBench v2 (NeurIPS 2025)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8c2e6bb15be1894b8fb4e0f9bcad1739-Abstract-Datasets_and_Benchmarks_Track.html); [MERLIM (CVPRW 2025)](https://openaccess.thecvf.com/content/CVPR2025W/BEAM/html/Villa_Behind_the_Magic_MERLIM_Multi-modal_Evaluation_Benchmark_for_Large_Image-Language_CVPRW_2025_paper.html))

MCP is particularly volatile. Protocol revisions, SDK generations, registries, transports and security practices may change significantly between knowledge-base updates. The July 2026 specification itself demonstrates this volatility. ([MCP specification](https://modelcontextprotocol.io/specification/2026-07-28))

The practical schemas and adaptive-interview algorithm proposed here therefore belong in the project's **design hypothesis layer**. They are sufficiently grounded to implement and evaluate in Skill v0.1, but they should be instrumented, tested against representative project scenarios, compared with simpler baselines, and revised when empirical evidence contradicts them.

The resulting engineering principle for the bootstrap process is concise:

> **Preserve evidence, expose interpretation, ask only what matters, defer what can safely remain open, and never let uncertainty masquerade as an approved technical decision.**

## Source provenance and limitations

**Final editorial pass (11 November 2026).** Legacy Deep Research result identifiers have been removed because they cannot be resolved from a standalone Markdown export. Where possible, affected assertions now cite independently located, relevant primary publications or official specifications. If a specific empirical claim could not be supported, it was rewritten or qualified rather than assigning a different study as though it were the missing original. Broad design guidance may be an editorial synthesis rather than a direct quotation from a standard.

This review includes source checks for the assertions repaired here, consistency fixes, static formatting inspection and parsing of extractable YAML/JSON examples. It is **not** a claim that all historical citations have been exhaustively rechecked, that all linked pages will remain reachable, or that any described software, CI, API, migration, security control or deployment was implemented and tested. Publication and product versions are an as-of snapshot and should be refreshed before decisions that depend on them.

For the change log and exact validation scope, consult the adjacent `CORRECTIONS.md` and `VERIFICATION_REPORT.md` in this research bundle.
