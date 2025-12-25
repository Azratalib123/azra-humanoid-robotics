---
id: 1
title: "Update Chatbot Constitution"
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

# Constitution Update for Book Content Chatbot

## Prompt Text

Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync.

Project Goal: Build a chatbot for my book content and general questions.
Principles:
- Primary answers MUST come from the book content in "C:\\Users\\DELL LATITUDE\\Desktop\\humanoid-robotics-book +chatbot\\book.txt"
- For questions outside the book, chatbot should provide relevant general answers
- Must have a clean, user-friendly interface that can be embedded in my Vercel website: https://azra-humanoid-robotics.vercel.app
- No API keys should be exposed in the frontend
- Fully automated generation of backend, frontend, and deployment instructions

I have a local book content file at s\\DELL LATITUDE\\Desktop\\humanoid-robotics-book +chatbot\\book.txt".

Please create a chatbot that:
- Answers questions ONLY from this book content
- Can also answer general questions outside the book
- Has a clean, user-friendly interface that can be embedded in my Vercel website: https://azra-humanoid-robotics.vercel.app
- Does NOT expose any API keys in the frontend
- Generates all necessary backend files (server.js), frontend chat widget files (chat-widget.js), deployment configurations, and step-by-step deployment instructions
- Explains each generated file briefly

## Response Text

Updated the project constitution to reflect the requirements for the book content chatbot with the following core principles:

1. Content-First Answers: Primary answers MUST come from the book content file
2. General Knowledge Capability: Providing relevant general answers for questions outside the book
3. Clean Interface Design: User-friendly interface that can be embedded in the Vercel website
4. Security First: No API keys exposed in the frontend
5. Automated Generation: Fully automated generation of backend, frontend, and deployment instructions

The constitution is now properly configured with these requirements and follows the governance guidelines.

## Outcome

Successfully created and updated the constitution file at `.specify/memory/constitution.md` with the project-specific requirements and principles.