---
id: 2
title: "Update Chatbot Constitution Strict Requirements"
stage: constitution
date_iso: 2025-12-19
surface: agent
model: qwen
feature: none
branch: main
user: DELL LATITUDE
command: "/sp.constitution"
labels: ["constitution", "chatbot", "requirements"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
---

# Constitution Update for Book Content Chatbot - Strict Requirements

## Prompt Text

Our project goal: Build a chatbot for my book content.
Principles:
- Answers questions ONLY from the book.txt file
- Embeddable in my Vercel website
- No API keys exposed in frontend
- Fully automated file generation and deployment instructions

## Response Text

Updated the project constitution to reflect the stricter requirements for the book content chatbot with the following core principles:

1. Content-First Answers: Answers questions ONLY from the book.txt file
2. Embeddable Design: Solution must be embeddable in the Vercel website
3. Security First: No API keys exposed in frontend
4. Automated Generation: Fully automated file generation and deployment instructions

The constitution was updated from version 1.1.0 to 1.2.0 to reflect the changes in requirements, specifically emphasizing that answers must come ONLY from the book.txt file and removing the general knowledge capability provision.

## Outcome

Successfully updated the constitution file at `.specify/memory/constitution.md` with the project-specific requirements and principles. The new version (1.2.0) emphasizes strict adherence to using only book content for answers.