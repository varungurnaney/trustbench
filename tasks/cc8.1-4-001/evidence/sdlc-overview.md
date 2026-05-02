# Software Development Lifecycle Overview

**Document ID:** DOC-SDLC-001
**Version:** 2.1

## Methodology

Stratos Inc. follows an Agile Scrum methodology with 2-week sprints. All development work is tracked in Jira.

## Environments

| Environment | Purpose | Access |
|-------------|---------|--------|
| Local | Developer workstations | All engineers |
| Staging | Pre-production testing | Engineering + QA |
| Production | Live customer-facing | SRE team (deployment only) |

## Code Review

- All code changes require a pull request in GitHub.
- PRs require at least one approval from a peer engineer.
- CI pipeline runs automated tests on every PR.
- PRs cannot be merged without passing CI.

## Release Cadence

- Feature releases: bi-weekly (aligned with sprint boundaries)
- Hotfixes: as needed, following emergency change process
- Infrastructure changes: monthly, during maintenance windows
