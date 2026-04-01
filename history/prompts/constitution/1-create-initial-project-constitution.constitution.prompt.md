---
id: 1
title: Create Initial Project Constitution
stage: constitution
date: 2025-12-30
surface: agent
model: gemini
feature: none
branch: main
user: {{USER}}
command: /sp.constitution
labels: [constitution,project-setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - "none"
---

## Prompt

/sp.constitution write constitution prompt as per my project requirements i am using speckit plus for writing textbook in my project 1. AI/Spec-Driven Book Creation: Write a book using Docusaurus and deploy it to GitHub Pages. You will use Spec-Kit Plus ( https://github.com/panaversity/spec-kit-plus/ ) and Claude Code ( https://www.claude.com/product/claude-code ) to write the book. for my project speckit plus first create a sp.constitution in my project to create a textbook /sp.constitution Project: Research paper on AI-native software development Core principles: - Accuracy through primary source verification - Clarity for academic audience (computer science background) - Reproducibility (all claims cited and traceable) - Rigor (peer-reviewed sources preferred) Key standards: - All factual claims must be traceable to sources - Citation format: APA style - Source types: minimum 50% peer-reviewed articles - Plagiarism check: 0% tolerance before submission - Writing clarity: Flesch-Kincaid grade 10-12 Constraints: - Word count: 5,000-7,000 words - Minimum 15 sources - Format: PDF with embedded citations Success criteria: - All claims verified against sources - Zero plagiarism detected - Passes fact-checking review

## Response snapshot

Created the initial project constitution in `.specify/memory/constitution.md` based on the user's requirements. The constitution defines core principles for the project, including accuracy, clarity, reproducibility, rigor, and integrity. Key standards, constraints, and success criteria were also documented. The constitution is versioned at 1.0.0.

## Outcome

- ✅ Impact: High. The constitution is a foundational document for the project.
- 🧪 Tests: None.
- 📁 Files: 1 file created/modified.
- 🔁 Next prompts: The user can now proceed with other spec-driven development commands.
- 🧠 Reflection: The process of extracting principles from the user's prompt and mapping them to the constitution template was successful.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-phr.sh` script did not produce the expected JSON output, likely due to a platform incompatibility (running a bash script on Windows). The fallback mechanism of reading the template and creating the file manually worked as expected.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Improve platform compatibility of helper scripts.
