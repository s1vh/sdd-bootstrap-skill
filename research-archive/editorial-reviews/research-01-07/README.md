# Research editorial archive — Research 01–07

**Archive purpose:** historical provenance, **not Skill runtime knowledge**.

This directory contains **the original shared editorial records** for the first seven research reports revised on 11 November 2026:

- [`CORRECTIONS.md`](CORRECTIONS.md) — final editorial correction summary for Research 01–07.
- [`VERIFICATION_REPORT.md`](VERIFICATION_REPORT.md) — final editorial verification scope, referenced sources, notable corrections and limitations.

These were obtained from the project's existing Google Drive research archive and are preserved **without rewriting**. They are **not seven independent pairs of logs**: this is one pair covering the seven reports jointly.

## Usage boundary

- The Skill does **not** need these files to elicit requirements, write specs, make architecture decisions, or generate project bootstraps.
- The files are intentionally outside `sdd-bootstrap/`, which is the installable Skill root. They should not be included in a standalone Skill installation or loaded automatically as runtime references.
- These logs describe a **historical editorial review of research sources**, not executable tests, evaluated pilot results, security assessments, or production readiness.
- The historical document references a separate original package manifest that is not included here. Its original checksums are not asserted or reconstructed; current archive integrity may be checked against the SHA-256 values below.
- They cover Research 01–07 only; Research 08 and later updates are not within their documented review scope.

## Current archive byte integrity

| Original archive file | SHA-256 of preserved bytes |
|---|---|
| `CORRECTIONS.md` | `06d8de64f416f311e11cc8cb350ef8325a66d7e8613aecf0264ac1b55c9e2025` |
| `VERIFICATION_REPORT.md` | `12d2907174d42dd53ecfd14a0140fbd2d708540ee4038e2f62ec1cd198d1ea11` |

The GitHub repository is a publishing and preservation medium. The research logs have **no effect on the authority of project-specific human decisions** and are never substitutes for fresh verification when a consequential claim is used.
