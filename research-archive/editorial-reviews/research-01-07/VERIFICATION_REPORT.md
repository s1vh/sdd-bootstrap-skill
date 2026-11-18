# SDD Bootstrap Research 01–07 — Final editorial verification report

**Date:** 2026-11-11  
**Basis:** seven revised, user-provided Markdown studies (01–07) and their editorial correction log.  
**Research 08:** intentionally excluded.

## Scope and method

This is a targeted final pass. Original unresolvable Deep Research session citations were replaced by newly located relevant sources where possible; unsupported claims were qualified instead of being assigned invented citations. The original study structure, examples, and proposed SDD methodology were preserved. External checks included official standards/guidance (ISO records, SEI, NIST, OWASP, EDPB, CISA, GitHub, OpenSSF, SRE) and selected peer-reviewed/author-hosted research. A source URL supports a specific claim only to the extent its cited publication actually does so; in particular, studies from one context are not universal proof.

## Source repair summary

| Study | Former missing-citation occurrences independently replaced | Former missing-citation occurrences removed after qualification / no independent reference | Material text corrections |
|---|---:|---:|---:|
| Research 01 | 13 | 0 | 0 |
| Research 02 | 13 | 0 | 2 |
| Research 03 | 7 | 4 | 2 |
| Research 04 | 10 | 1 | 2 |
| Research 05 | 7 | 0 | 1 |
| Research 06 | 8 | 1 | 2 |
| Research 07 | 1 | 0 | 1 |

The counts above apply to source placeholders visibly unresolved in the *uploaded revised files*. They are not the number of historical Deep Research internal search IDs. Historical session IDs were intentionally deleted from the portable deliverables.

## Notable corrections

- **Research 01:** replaced missing references for the empirical study of evolving requirements during elicitation, viewpoint-oriented requirements engineering, AnnoteREI, contextual inquiry, cognitive bias, procedural prompting, the value of information and requirements-quality research with locatable works.

- **Research 02:** corrected a mistaken *2026* date for the empirical requirements-quality mapping study, first published in **2022**; cited the original publication. Added direct citations for 2026 EPIC (preprint) and the peer-reviewed ESEM 2026 null-result study, preserving the important distinction that the latter did **not** test SDD tools directly. Other repairs include industrial LLM requirements/test papers and official guidance.

- **Research 03:** removed specific unsubstantiated empirical assertions about CNCF serverless adoption and purportedly industry-validated multi-criteria technology-selection methods; retained narrower, defensible engineering trade-offs. Repaired references to evolutionary architecture, Fowler, OpenSSF, arc42 and architecture design-rationale research.

- **Research 04:** linked missing quality-attribute scenarios, SRE service objectives, CISA secure-by-design, GDPR and EDPB materials. Clarified that the **2026 EDPB DPIA template was in public consultation**, rather than an approved universal compliance standard. Reframed directory-trust advice as an engineering recommendation, not a purported survey finding.

- **Research 05:** restored official Git/GitHub, SemVer and Claude documentation references. Corrected an unrelated OpenAI model documentation URL previously shown as evidence for Codex AGENTS.md, replacing it with a Codex workflow source. Clarified Claude Code’s documented direct `AGENTS.md` support (besides `CLAUDE.md`).

- **Research 06:** recovered AWS formal-methods case study, LLM oracle and Meta test-generation studies, and the **July 2026 preprint on error propagation**. Qualified a too-specific mutation-testing generalization, maintaining the distinction between study observations and general best practices.

- **Research 07:** restored evolutionary database design source, and aligned the standalone JSON Schema example identifiers with the OpenAPI illustration. API examples remain illustrative until validated with spec-specific tools.

## Limitations and acceptance

This editorial verification checks the previously unresolved references plus selected high-impact source mappings and examples. It does **not** constitute an exhaustive paragraph-by-paragraph audit of every citation in hundreds of pages, a security audit, legal advice, a product test or proof of correctness for the proposed SDD heuristics. Sources that were already linked in the revised documents were largely retained rather than individually reverified. Any future Skill implementation should check volatile versions, APIs, laws and service behavior at decision time.

**Corpus status:** suitable as an **edited, source-navigable research reference set**, with remaining domain-specific validation required before an architecture-significant decision is adopted.

## Newly used primary or authoritative publications (selection)

- [Requirements evolution during elicitation (empirical study, 2022)](https://link.springer.com/article/10.1007/s00766-022-00383-7)
- [Finkelstein et al., Requirements Engineering Through Viewpoints (1993)](https://discovery.ucl.ac.uk/id/eprint/854/)
- [AnnoteREI! (IEEE RE 2022)](https://ieeexplore.ieee.org/document/9920036)
- [UK Government — Contextual inquiry](https://www.gov.uk/guidance/contextual-inquiry)
- [Cognitive biases in software engineering (IEEE TSE)](https://doi.org/10.1109/TSE.2018.2877759)
- [Numerical anchors in software effort estimates (2016)](https://doi.org/10.1016/j.jss.2015.03.015)
- [Procedural prompting in elicitation (2007)](https://doi.org/10.1111/j.1365-2575.2006.00240.x)
- [Letier, Stefan & Barr — Uncertainty, Risk, and Information Value (ICSE 2014)](https://doi.org/10.1145/2568225.2568239)
- [Empirical research on requirements quality: systematic mapping study (2022)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9110500/)
- [CMU/SEI — Deriving Architectural Tactics: A Step Toward Methodical Architectural Design](https://www.sei.cmu.edu/documents/704/2003_005_001_14213.pdf)
- [Google SRE — Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)
- [CISA — Secure by Design: Eliminating Default Passwords (2023)](https://www.cisa.gov/sites/default/files/2023-12/SbD-Alert-How-Software-Manufacturers-Can-Protect-Customers-by-Eliminating-Default-Passwords-508c_0.pdf)
- [GDPR Articles 5, 25 and 35 (EUR-Lex)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/)
- [EDPB — 2026 DPIA template (consultation-stage materials)](https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2026/edpb-dpia-template_en)
- [Git — gitworkflows/topic branches](https://git-scm.com/docs/gitworkflows)
- [GitHub Docs — About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [Context-aware LLMs for ambiguity detection (2026)](https://www.cambridge.org/core/journals/proceedings-of-the-design-society/article/contextaware-large-language-models-for-ambiguity-detection-in-requirements/E3685BED3A8F7EC801E42CA699D392A7)
- [Pasquale et al. — LLMs for Requirements Specification (IEEE RE 2025)](https://doi.org/10.1109/RE63999.2025.00045)
- [Gärtner & Göhlich — Formal logic and LLM requirements contradictions (2024)](https://doi.org/10.1007/s10515-024-00452-x)
- [Ferreira et al. — Acceptance Test Generation with LLMs (IEEE AST 2025)](https://doi.org/10.1109/AST66626.2025.00007)
- [EPIC SDD framework (2026 preprint)](https://arxiv.org/abs/2610.07534)
- [Hill — Specification Artifacts Do Not Reduce Defects (ESEM 2026)](https://doi.org/10.4230/LIPIcs.ESEM.2026.84)
- [Ford et al. — Building Evolutionary Architectures, fitness functions](https://evolutionaryarchitecture.com/precis.html)
- [Zhou et al. — LLMs Generating Architecture Design Rationale (ACM TOSEM 2026)](https://doi.org/10.1145/3785010)
- [Newcombe et al. — Use of Formal Methods at AWS (2014)](https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf)
- [Alshahwan et al. — Automated Unit Test Improvement at Meta (FSE 2024)](https://discovery.ucl.ac.uk/id/eprint/10199775/)
- [Molinelli et al. — Do LLMs Generate Useful Test Oracles? (ASE 2025)](https://doi.org/10.1109/ASE63991.2025.00031)
- [Konstantinou, Tambon & Papadakis — Coding Before Testing (2026 preprint)](https://arxiv.org/abs/2607.05139)
- [Sadalage & Fowler — Evolutionary Database Design](https://martinfowler.com/articles/evodb.html)
