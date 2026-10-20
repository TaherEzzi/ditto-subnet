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
1. Use the miner CLI to submit a hotkey-signed claim with a valid CLA signature and verified GitHub link to your work.
2. Pay the alpha entry fee, initiating a 30-minute unpaid hold on the slot.
3. Delivery deadline begins immediately after fee confirmation. The Platform automatically manages slot allocation.

## Submission Rules
1. Submit via exact commit hash in issue comments before the deadline (starts at fee confirmation).
2. Include:
   - Implementation code
   - Test artifacts
   - Acceptance evidence (benchmarks/logs)
3. Keep submissions under 128MiB

## Review Process
- Submissions are evaluated against per-revision targets defined in the bounty specs.
- The Platform serves as the final authority for acceptance decisions.
- Three failed submission attempts result in permanent bounty closure.

## Appeals
Dispute decisions via the DittoBench Governance Committee through `appeals@ditto.com`.
