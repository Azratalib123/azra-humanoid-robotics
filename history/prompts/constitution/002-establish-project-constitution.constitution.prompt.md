---
id: 2
title: Establish Project Constitution
stage: constitution
date: 2025-12-08
surface: agent
model: gemini
feature: none
branch: master
user:
command: /sp.constitution
labels: ["constitution", "setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests:
- none
---

## Prompt

/sp.constitution

Project: AI/Spec-Driven Book on AI-Native Software Development

Core Principles:
- Accuracy: All content verified against authoritative sources.
- Clarity: Target audience is CS/software readers; explanations must be precise.
- Reproducibility: Code and workflows must be traceable and testable.
- Rigor: Prefer peer-reviewed or official sources.
- Consistency: Maintain uniform terminology, style, and formatting.

Standards:
- Source Verification: Claims supported by credible sources.
- Citation: APA style.
- Sources: ≥50% peer-reviewed or official docs.
- Plagiarism: Zero tolerance.
- Code: Must run correctly and illustrate concepts.
- Writing: Flesch-Kincaid grade 10–12.

Constraints:
- Word Count: 15k–20k (per chapter adjustable).
- Chapters: Intro, explanations, examples, summary.
- Format: Markdown for Docusaurus, deployable to GitHub Pages.
- References: In-text + compiled at chapter end.

Success Criteria:
- All claims verified.
- Code runs reproducibly.
- Book deployable via Docusaurus + GitHub Pages.
- Zero plagiarism.
- Passes fact-checking.
- Clear and understandable for audience.

## Response snapshot

Updated the project constitution at `.specify/memory/constitution.md` with the provided principles, standards, constraints, and success criteria. Also verified that the other templates are in sync with the new constitution.

## Outcome

- ✅ Impact: High
- 🧪 Tests: None
- 📁 Files: 1 modified
- 🔁 Next prompts: None
- 🧠 Reflection: The process of updating the constitution and ensuring other templates are in sync is crucial for maintaining project consistency.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None
