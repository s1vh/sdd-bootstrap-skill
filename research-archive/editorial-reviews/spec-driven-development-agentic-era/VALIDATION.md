# Editorial review and validation

**Review date** 2026-11-18. **Research snapshot** 2026-11-04. **Status** Proposed editorial update for human review.

## Changes

- Replaced the report’s session-local citations with standard Markdown links and a 42-source public bibliography. The [claim map](CLAIM_TO_SOURCE_MAP.md) records all 100 groups and traces the 192 original mentions to 65 distinct pointers.
- Reconnected named papers to their public publications or author material. Corrected the taxonomy’s dating, distinguished observed pull request artifacts from SDD tool outputs, and clarified the scope of benchmark and corpus results.
- Used pre-cutoff repository snapshots for Spec Kit and OpenSpec and versioned papers where the version affects the evidence. Marked living documentation and the limits of historical reconstruction in the [unresolved items ledger](UNRESOLVED_ITEMS.md).
- The report’s structure, proposed methodology and lifecycle diagram were preserved. The editorial files for this review are in their own directory. Research 01–07 is referenced for context only.

## Coverage and link outcomes

| Check | Result |
|---|---|
| Original group decisions | 79 supported by replacement evidence, 20 qualified, one partially supported. |
| Original pointer provenance | 65 of 65 distinct pointers unresolved. Publication matches found from prose and data are independent of pointer identity. |
| Public bibliography | 42 unique destinations. 35 inspected using public web retrieval, including the SWE-CC author repository. Seven commit-pinned GitHub links returned the exact file on public repositories through GitHub. |
| Access scope | Public catalogue, publisher and author records were checked where applicable. Some full-text standards or books may require purchase. Direct SWE-CC arXiv retrieval was inconsistent, so the report links the verified author repository. |
| Markdown rendering | Parsed the source and edited report as GitHub-flavored Markdown. Both have five tables. The edited report resolves 258 rendered link occurrences to 42 bibliography destinations. All internal evidence anchors in the claim map resolved. |
| Active citation cleanup | Zero original session tokens in the revised report. The bibliography uses public HTTPS destinations and does not rely on Google Drive or ChatGPT access. |
| Patch | Git whitespace validation and patch applicability both passed against the exact input. Applying the patch produced the same bytes as the revised report. Its only path is the report. |

## Input and output integrity

- The handoff identifies input commit `90957acec028f39350a5e3f0a2e60c29fcc8ecec`. The input and the main branch checked for this review at `bc40a5a55589936fdfc6d9c7229cecd8180c0bac` have the same report blob `25d3494594a97bf56fac4ac46df7acdcdd098fd1`.
- Untouched input SHA-256 `a8d6468f90969daf180fad105012b144fb0386176dcb0b072a2763f897370334`.
- Updated report SHA-256 `5ad9a8a9c30625d73de46e92a4ec81df6162e9d3ad236a9413f829fe225d295b`.

## Package layout

- [Revised report](../../../sdd-bootstrap/references/Spec-Driven%20Development%20in%20the%20Agentic%20Era.md) at its original repository-relative path.
- [Claim map](CLAIM_TO_SOURCE_MAP.md), [unresolved items](UNRESOLVED_ITEMS.md), this validation record and [unified diff](REPORT.diff) in the new editorial review directory.

The report can be copied into the repository for inspection in GitHub Desktop. The diff is a review aid and can also be applied to the untouched input as an alternative to copying the report.
