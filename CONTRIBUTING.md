# DittoBench Contributor Guide

Welcome to DittoBench! This guide helps you contribute via scoped build bounties.

## Bounty Board
Visit our [DittoBench Bounty Board](https://github.com/ditto-assistant/ditto-subnet/projects/1) to find available tasks. Each card links to a GitHub issue with:
- **Scope**: Clear objectives and technical specs
- **Reward**: Fixed α-pool allocation
- **Deadline**: Submission window
- **Dependencies**: Required PRs/issues
- **Reviewer**: Assigned maintainer

## Claiming Work
1. Comment `/claim` on the GitHub issue
2. Wait for maintainer confirmation (prevents collisions)
3. Slot expires after 7 days of inactivity

## Submission Rules
1. Submit via exact commit hash in issue comments
2. Include:
   - Implementation code
   - Test artifacts
   - Acceptance evidence (benchmarks/logs)
3. Keep submissions under 128MiB

## Review Process
- Submissions retain slots during review
- Reviewers have 3 days to:
  - Accept (with optional revision requests)
  - Reject (with specific feedback)
- 3 failed attempts close the bounty

## Appeals
Dispute decisions via:
