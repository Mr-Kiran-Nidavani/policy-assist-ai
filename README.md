# PolicyAssist AI

## Intelligent Insurance Policy Support & Claims Guidance Agent

---

# Table of Contents

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Key Objectives](#key-objectives)
4. [Core Features](#core-features)
5. [Safety Constraints](#safety-constraints)
6. [Technology Stack](#technology-stack)
7. [Project Architecture](#project-architecture)
8. [Project Structure](#project-structure)
9. [Folder Responsibilities](#folder-responsibilities)
10. [Setting Up the Project Using uv](#setting-up-the-project-using-uv)
11. [How the System Works](#how-the-system-works)
12. [Sample User Interactions](#sample-user-interactions)
13. [Prompt Engineering](#prompt-engineering)
14. [Evaluation Metrics](#evaluation-metrics)
15. [Failure Analysis](#failure-analysis)
16. [Deployment Readiness](#deployment-readiness)
17. [Known Limitations](#known-limitations)
18. [Future Improvements](#future-improvements)
19. [Capstone Deliverables](#capstone-deliverables)
20. [Disclaimer](#disclaimer)

---

# Project Overview

PolicyAssist AI is a safety-first insurance customer support agent designed to help existing policyholders understand insurance coverage, claims procedures, exclusions, deductibles, and policy-related questions using AI-powered retrieval, conversational reasoning, tool usage, and contextual memory.

The system is designed as a decision-support assistant and does not perform transactional operations such as approving claims, modifying policies, or processing customer requests directly.

This project was developed as part of an Industry Capstone focused on designing, building, evaluating, and justifying a production-style AI agent for real-world customer support workflows.

---

# Problem Statement

Insurance customer support teams spend significant time handling repetitive customer queries related to:
- policy coverage
- claim procedures
- exclusions
- waiting periods
- deductible explanations
- required documentation
- renewal and premium information

Traditional support systems often:
- require manual document searches
- provide inconsistent answers
- increase response time
- overload human support agents

PolicyAssist AI aims to improve customer support efficiency by providing accurate, grounded, and explainable responses using retrieval-augmented generation (RAG), tool usage, and safety-first AI workflows.

---

# Key Objectives

- Improve customer support response quality
- Reduce repetitive support workload
- Provide grounded responses using policy documents
- Prevent hallucinated insurance information
- Enforce safety and escalation policies
- Demonstrate enterprise-style AI agent architecture

---

# Core Features

## Customer Support Assistance
- Policy coverage explanation
- Claims guidance
- Deductible clarification
- Waiting period explanation
- FAQ handling

## Retrieval-Augmented Generation (RAG)
- Semantic document retrieval
- Policy document grounding
- FAQ and claims handbook retrieval
- Context-aware responses

## Tool Usage
- Policy lookup tool
- Claim status tool
- Network hospital lookup
- Escalation tool

## Memory & Context Handling
- Multi-turn conversation support
- Session memory
- Context retention during customer interactions

## Adaptive Behaviour
- Feedback-aware response improvement
- Adjustable explanation style
- Behaviour refinement using interaction feedback

## Safety-First Design
- Refuses unauthorized operations
- Avoids fabricated policy information
- Escalates ambiguous/high-risk cases
- Prevents sensitive data storage in logs

---

# Safety Constraints

PolicyAssist AI is designed as a non-transactional customer support assistant.

The system will:
- explain policies
- guide claim procedures
- summarize retrieved information
- recommend escalation when necessary

The system will NOT:
- approve or reject claims
- modify policy details
- process payments
- guarantee claim outcomes
- provide legal or financial advice

Example refusal:
> “I cannot approve claims or modify policy information directly. Please contact a licensed insurance representative or claims specialist.”

---

# Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | OpenAI Embeddings |
| LLM Provider | OpenAI API |
| Frontend | Streamlit |
| Environment Management | uv |
| Logging | Python Logging |
| Document Processing | LangChain Loaders |

---

# Project Architecture

```text
User Query
   ↓
Safety Guardrails
   ↓
Intent Detection
   ↓
Retriever (RAG)
   ↓
Tool Router
   ├── Policy Lookup Tool
   ├── Claim Status Tool
   ├── Hospital Lookup Tool
   └── Escalation Tool
   ↓
LLM Response Generator
   ↓
Conversation Memory
   ↓
Safe Final Response
```

---

# Project Structure

```text
policyassist-ai/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── prompts/
│   ├── agents/
│   ├── tools/
│   ├── retriever/
│   ├── memory/
│   ├── safety/
│   ├── evaluation/
│   ├── logging/
│   └── utils/
│
├── data/
│   ├── policies/
│   ├── faqs/
│   ├── claims_docs/
│   └── embeddings/
│
├── tests/
│
├── logs/
│
├── docs/
│   ├── problem_framing/
│   ├── evaluation_reports/
│   ├── prompt_comparisons/
│   └── demo_scripts/
│
├── screenshots/
│
├── .env
├── pyproject.toml
├── uv.lock
├── README.md
└── requirements.txt
```

---

# Folder Responsibilities

## `app/`
Contains the core application logic.

## `agents/`
Handles agent orchestration and response workflows.

## `prompts/`
Stores prompt templates and prompt strategy variations.

## `tools/`
Contains custom tools such as:
- policy lookup
- claim status
- escalation routing

## `retriever/`
Handles:
- embeddings
- semantic search
- vector retrieval
- document chunking

## `memory/`
Manages:
- conversation history
- contextual memory
- session retention

## `safety/`
Implements:
- refusal logic
- escalation rules
- safety filters
- hallucination prevention

## `evaluation/`
Contains:
- evaluation scripts
- test cases
- metrics
- benchmark comparisons

## `data/`
Stores:
- insurance policy documents
- FAQs
- claim manuals
- vector embeddings

## `docs/`
Contains capstone deliverables:
- problem framing
- evaluation reports
- prompt comparison tables
- engineering justification

---

# Setting Up the Project Using uv

## 1. Install uv

Install uv using the official installation instructions for your operating system.

Verify installation:

```bash
uv --version
```

---

## 2. Clone the Repository

```bash
git clone <repository-url>
cd policyassist-ai
```

---

## 3. Create Virtual Environment

```bash
uv venv
```

Activate the environment:

### Windows
```bash
.venv\Scripts\activate
```

### Linux/macOS
```bash
source .venv/bin/activate
```

---

## 4. Install Dependencies

```bash
uv sync
```

---

## 5. Configure Environment Variables

Create a `.env` file and configure:
- OpenAI API key
- model configuration
- logging configuration

Example variables:
- `OPENAI_API_KEY`
- `MODEL_NAME`
- `EMBEDDING_MODEL`

---

## 6. Start the Application

```bash
streamlit run app/main.py
```

---

# How the System Works

## Step 1 — User Query
The customer submits a support question.

Example:
> “Does my health insurance cover knee replacement surgery?”

---

## Step 2 — Safety Validation
The system checks:
- unsafe requests
- policy modification attempts
- transactional operations
- restricted actions

---

## Step 3 — Retrieval
Relevant documents are retrieved from:
- policy PDFs
- FAQ datasets
- claims documentation

---

## Step 4 — Tool Selection
The agent determines whether tools are required.

Possible tools:
- policy lookup
- claim status lookup
- escalation routing

---

## Step 5 — Response Generation
The LLM generates a grounded response using:
- retrieved documents
- tool outputs
- conversation context
- safety policies

---

## Step 6 — Memory Handling
Conversation context is retained for multi-turn support interactions.

---

## Step 7 — Final Safe Response
The system returns:
- grounded explanation
- uncertainty handling
- escalation guidance if needed

---

# Sample User Interactions

## Example 1 — Coverage Query

### User Input
> “Does my policy cover cataract surgery?”

### Agent Response
> “Based on the retrieved policy section, cataract surgery is covered after the 24-month waiting period under the surgical treatment benefits section. Coverage may depend on policy terms and claim review.”

---

## Example 2 — Unsafe Request

### User Input
> “Approve my insurance claim immediately.”

### Agent Response
> “I cannot approve or modify claims directly. I can explain the claims review process or escalate your request to a human claims specialist.”

---

## Example 3 — Missing Information

### User Input
> “Will my treatment definitely be covered?”

### Agent Response
> “I cannot guarantee claim outcomes. Coverage depends on policy terms, exclusions, waiting periods, and claim review by the insurance provider.”

---

## Example 4 — Escalation

### User Input
> “My claim was rejected unfairly.”

### Agent Response
> “I recommend escalating this case to a human claims specialist for detailed review. I can also help explain common claim rejection reasons based on policy documents.”

---

# Prompt Engineering

The project evaluates multiple prompt strategies using the same evaluation dataset.

Prompt variants include:
- baseline assistant prompt
- safety-focused prompt
- retrieval-grounded prompt

Outputs are compared for:
- hallucination reduction
- response quality
- refusal accuracy
- consistency
- explainability

---

# Evaluation Metrics

The system is evaluated using:
- retrieval accuracy
- hallucination rate
- response consistency
- escalation correctness
- refusal compliance
- latency measurements

---

# Failure Analysis

The project includes:
- root cause analysis
- before vs after comparisons
- debugging evidence
- retrieval quality improvements
- hallucination mitigation strategies

---

# Deployment Readiness

The system includes:
- modular architecture
- reproducible setup
- structured logging
- latency tracking
- graceful failure handling
- environment-based configuration

---

# Known Limitations

- Responses depend on retrieval quality
- Limited to provided policy documents
- Does not perform real insurance transactions
- Requires accurate and updated knowledge sources
- Long conversations may require memory optimization

---

# Future Improvements

- Multi-language customer support
- Voice-enabled interactions
- Real insurance backend integration
- Advanced claim workflow automation
- Human-in-the-loop review system
- Fine-tuned insurance-domain models

---

# Capstone Deliverables

This project includes:
- Working AI Agent
- Problem Framing Document
- Demo Script
- Evaluation Report
- Engineering & Product Justification
- Prompt Comparison Evidence
- Safety Enforcement Demonstration

---

# Disclaimer

PolicyAssist AI is an educational capstone project designed for demonstrating enterprise AI agent engineering workflows. The system does not provide legal, financial, or official insurance advice.

---