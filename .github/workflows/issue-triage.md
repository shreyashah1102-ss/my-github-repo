---
name: Issue Triage
description: Apply one evidence-backed triage label and explain it on new issues.
intent: Help maintainers quickly understand and route newly opened issues.
on:
  issues:
    types: [opened]
  roles: all
permissions:
  issues: read
  copilot-requests: write
strict: true
tools:
  github:
    mode: gh-proxy
    toolsets: [issues, labels]
network:
  allowed: []
safe-outputs:
  add-labels:
    allowed: [bug, enhancement, documentation, question, accessibility]
    max: 1
    max-labels: 1
    target: triggering
    issues: true
    pull-requests: false
  add-comment:
    max: 1
    target: triggering
    issues: true
    pull-requests: false
---

# Issue Triage

Triage only the newly opened issue that triggered this run. Read its title, body, and existing labels; classify it using the strongest evidence in the issue:

- `bug`: a reproducible defect or unexpected behavior
- `enhancement`: a request for new or changed functionality
- `documentation`: a documentation correction or improvement
- `question`: a request for information without a clear defect or feature request
- `accessibility`: an accessibility barrier or improvement

If exactly one of these labels is clearly supported and is not already present, add that single label. Post one brief comment naming the label and explaining the evidence in the issue. Do not infer priority, assign people, or modify the issue title or body.

Call `noop` with a brief reason and take no visible action if the issue is a pull request, the evidence is insufficient or ambiguous, or it already has one of these triage labels. Do not add labels outside the configured list, close issues, or create issues.
