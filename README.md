# PolicyAssist AI

## Intelligent Insurance Support & Controlled Operations Assistant

---

# Table of Contents

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Key Objectives](#key-objectives)
4. [Core Features](#core-features)
5. [Supported Operations](#supported-operations)
6. [Restricted Operations](#restricted-operations)
7. [Safety Constraints](#safety-constraints)
8. [Technology Stack](#technology-stack)
9. [Multi-Agent Architecture](#multi-agent-architecture)
10. [Project Structure](#project-structure)
11. [Folder Responsibilities](#folder-responsibilities)
12. [Documentation Structure](#documentation-structure)
13. [Setting Up the Project Using uv](#setting-up-the-project-using-uv)
14. [How the System Works](#how-the-system-works)
15. [Sample User Interactions](#sample-user-interactions)
16. [Prompt Engineering](#prompt-engineering)
17. [Evaluation Metrics](#evaluation-metrics)
18. [Failure Analysis](#failure-analysis)
19. [Deployment Readiness](#deployment-readiness)
20. [Known Limitations](#known-limitations)
21. [Future Improvements](#future-improvements)
22. [Capstone Deliverables](#capstone-deliverables)
23. [Disclaimer](#disclaimer)

---

# Project Overview

PolicyAssist AI is a safety-first lightweight orchestrated multi-agent insurance support and controlled operations assistant designed to help existing policyholders understand insurance coverage, claims procedures, exclusions, deductibles, waiting periods, and operational workflows using AI-powered retrieval, conversational reasoning, contextual memory, and controlled tool usage.

The system combines:
- retrieval-augmented generation (RAG)
- multi-agent orchestration
- operational tools
- conversational memory
- safety validation
- escalation handling
- adaptive behaviour

to provide enterprise-style insurance customer support assistance.

PolicyAssist AI supports:
- policy clarification
- claims guidance
- low-risk operational assistance
- customer profile updates
- policy-related workflows
- safe refusal handling

This project was developed as part of an Industry Capstone focused on designing, building, evaluating, and justifying a production-style AI agent for real-world operational workflows.

---

# Problem Statement

Insurance customer support teams spend significant time handling repetitive customer requests related to:
- policy coverage clarification
- claims guidance
- deductible explanations
- waiting periods
- customer profile updates
- driver and vehicle additions
- operational support workflows
- policy documentation requests

Traditional support systems often:
- rely on manual policy searches
- provide inconsistent responses
- increase operational workload
- delay customer resolution
- require multiple escalations

Customers frequently struggle to:
- understand policy wording
- interpret exclusions and waiting periods
- determine operational eligibility
- understand claim procedures
- identify which requests are permitted

PolicyAssist AI aims to improve support efficiency and customer experience through safe, explainable, retrieval-grounded, and operationally controlled assistance while enforcing strict guardrails for high-risk actions.

---

# Key Objectives

- Improve insurance customer support efficiency
- Reduce repetitive support workload
- Provide grounded policy explanations
- Enable safe low-risk operational assistance
- Prevent unsafe or unauthorized operations
- Reduce hallucinated insurance information
- Demonstrate enterprise-style multi-agent architecture
- Implement explainable AI safety workflows

---

# Core Features

## Insurance Support Assistance
- Policy coverage explanation
- Claims guidance
- Deductible clarification
- Waiting period explanation
- Exclusion interpretation
- FAQ handling

---

## Retrieval-Augmented Generation (RAG)
- Semantic document retrieval
- Policy document grounding
- FAQ retrieval
- Claims handbook retrieval
- Context-aware response generation

---

## Controlled Operational Assistance
- Email updates
- Phone number updates
- Address updates
- Add driver requests
- Add vehicle requests
- Policy document retrieval

---

## Tool Usage
- Policy lookup tool
- Claim status tool
- Customer profile tool
- Add vehicle tool
- Add driver tool
- Escalation tool

---

## Multi-Agent Workflow
- Intent Router Agent
- Policy Information Agent
- Claim Support Agent
- Policy Update Agent
- General Query Agent
- Safety Review Agent

---

## Memory & Context Handling
- Multi-turn conversations
- Session memory
- Context retention
- Follow-up query handling

---

## Adaptive Behaviour
- Feedback-aware response improvement
- Adjustable explanation styles
- Behaviour refinement using user interactions

---

## Safety-First Design
- Restricted operation refusal
- Escalation workflows
- Hallucination reduction
- Safety review validation
- Privacy-safe logging

---

# Supported Operations

PolicyAssist AI supports approved low-risk customer operations.

## Allowed Operations

| Operation | Status |
|---|---|
| Policy coverage explanation | ✅ Supported |
| Claims guidance | ✅ Supported |
| Claim status lookup | ✅ Supported |
| Update email address | ✅ Supported |
| Update phone number | ✅ Supported |
| Update mailing address | ✅ Supported |
| Add new vehicle | ✅ Supported |
| Add new driver | ✅ Supported |
| Download policy documents | ✅ Supported |
| FAQ assistance | ✅ Supported |

---

# Restricted Operations

The system enforces strict restrictions on high-risk operations.

## Restricted Operations

| Operation | Status |
|---|---|
| Claim approval or rejection | ❌ Restricted |
| Reduce insurance premium | ❌ Restricted |
| Modify coverage limits | ❌ Restricted |
| Backdate policy | ❌ Restricted |
| Change policy effective date | ❌ Restricted |
| Waive deductibles | ❌ Restricted |
| Cancel policy | ❌ Restricted |
| Legal or financial guarantees | ❌ Restricted |

---

# Safety Constraints

PolicyAssist AI follows a strict safety-first operational design.

The system:
- explains policies safely
- supports approved low-risk operations
- validates unsafe requests
- escalates ambiguous or high-risk cases
- prevents unauthorized modifications
- avoids hallucinated policy information

The system does NOT:
- approve claims
- perform high-risk policy modifications
- make financial decisions
- guarantee claim outcomes
- provide legal advice

Example refusal:

> “I’m unable to assist with this request because it involves restricted or unauthorized operations. Please contact an authorized insurance representative or support specialist for further assistance.”

---

# Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| AI Framework | LangChain |
| LLM Provider | OpenAI API |
| Vector Database | ChromaDB |
| Embeddings | OpenAI Embeddings |
| Frontend | Streamlit |
| Environment Management | uv |
| Logging | Python Logging |
| Document Processing | LangChain Document Loaders |

---

# Multi-Agent Architecture

PolicyAssist AI follows a lightweight orchestrated multi-agent workflow.

## Agent Responsibilities

| Agent | Responsibility |
|---|---|
| Intent Router Agent | Detects user intent and routes workflows |
| Policy Information Agent | Handles policy explanations using RAG |
| Claim Support Agent | Handles claims guidance and claims workflows |
| Policy Update Agent | Handles approved low-risk operational requests |
| General Query Agent | Handles greetings and unsupported queries |
| Safety Review Agent | Validates outputs and enforces safety rules |

---

# Multi-Agent Workflow

```text
Customer Query
      ↓
Intent Router Agent
      ↓
──────────────────────────────────────────────
│                │                │
↓                ↓                ↓
Policy Info      Claim            Policy
Agent            Support          Update
                 Agent            Agent
│
└────────────────────┬───────────────────────┘
                     ↓
            General Query Agent
                     ↓
            Safety Review Agent
                     ↓
             Final Safe Response
```

---

# Project Structure

```text
policyassist-ai/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── agents/
│   │   ├── intent_router_agent.py
│   │   ├── policy_information_agent.py
│   │   ├── claim_support_agent.py
│   │   ├── policy_update_agent.py
|   |   |__customer_policy_agent.py 
│   │   ├── general_query_agent.py
│   │   └── safety_review_agent.py
│   │
│   ├── tools/
|   |   |__ utils.py (Holds common functions like retrive policy info or update policy info)
│   │   ├── policy_lookup_tool.py
│   │   ├── update_email_tool.py
│   │   ├── update_phone_tool.py
│   │
│   ├── prompts/
│   ├── retriever/
│   ├── memory/
│   ├── safety/
│   ├── evaluation/
│   ├── logs/
│   └── utils/
│
├── data/
│   ├── policies/
│   ├── faqs/
│   ├── claims_docs/
│   ├── customer_profiles/
│   └── embeddings/
│
├── docs/
│   ├── phase1/
│   │   └── problem_framing.md
│   │
│   ├── phase2/
│   │   ├── baseline_agent.md
│   │   └── screenshots/
│   │
│   ├── phase3/
│   │   ├── prompt_comparison.md
│   │   └── screenshots/
│   │
│   ├── phase4/
│   │   ├── screenshots/
│   │   └── rag_implementation.md
│   │
│   ├── phase5/
│   │   ├── screenshots/
│   │   └── tool_usage.md
│   │
│   ├── phase6/
│   │   ├── screenshots/
│   │   └── conversation_examples.md
│   │
│   ├── phase7/
│   │   ├── screenshots/
│   │   └── adaptive_behaviour.md
│   │
│   ├── phase8/
│   │   ├── screenshots/
│   │   └── deployment_readiness.md
│   │
│   └── phase9/
│       ├── screenshots/
│       ├── evaluation_engineering_review.md
│
├── tests/
├── logs/
│
├── FINAL_DEMO_SCRIPT.md
├── PROMPT_COMPARISON_ANALYSIS.md
├── ENGINEERING_PRODUCT_JUSTIFICATION.md
├── .env
├── pyproject.toml
├── uv.lock
├── README.md
└── requirements.txt
```

---

# Folder Responsibilities

## `agents/`
Contains modular multi-agent workflows:
- routing
- policy information handling
- claims support
- operational assistance
- safety validation

---

## `tools/`
Contains operational and retrieval tools:
- policy lookup
- claim status lookup
- customer updates
- escalation workflows

---

## `retriever/`
Handles:
- embeddings
- semantic retrieval
- vector search
- document chunking

---

## `memory/`
Manages:
- session history
- conversation context
- follow-up memory

---

## `safety/`
Implements:
- refusal logic
- escalation rules
- hallucination prevention
- operational validation

---

## `evaluation/`
Contains:
- benchmark tests
- prompt comparisons
- failure analysis
- consistency evaluation

---

## `data/`
Stores:
- policy documents
- FAQs
- claims documentation
- customer datasets
- embeddings

---

## `docs/`
Contains:
- phase artifacts
- engineering documentation
- screenshots
- evaluation reports
- deployment evidence

---

# Documentation Structure

| Folder | Purpose |
|---|---|
| `phase1/` | Problem framing and business analysis |
| `phase2/` | Baseline rule-based agent |
| `phase3/` | LLM integration and prompt engineering |
| `phase4/` | RAG and semantic retrieval |
| `phase5/` | Tool usage and operational workflows |
| `phase6/` | Memory and planning |
| `phase7/` | Adaptive behaviour |
| `phase8/` | Deployment readiness |
| `phase9/` | Evaluation and engineering review |

---

# Final Submission Artifacts
This repository includes the core phase documentation plus final capstone artifacts:
- [`FINAL_DEMO_SCRIPT.md`](FINAL_DEMO_SCRIPT.md)
- [`PROMPT_COMPARISON_ANALYSIS.md`](PROMPT_COMPARISON_ANALYSIS.md)
- [`ENGINEERING_PRODUCT_JUSTIFICATION.md`](ENGINEERING_PRODUCT_JUSTIFICATION.md)
- [`docs/phase1/problem_framing_and_system_design.md`](docs/phase1/problem_framing_and_system_design.md)
- [`docs/phase3/prompt_comparison.md`](docs/phase3/prompt_comparison.md)
- [`docs/phase9/evaluation_engineering_review.md`](docs/phase9/evaluation_engineering_review.md)
- [`app/evaluation/evaluation_results.json`](app/evaluation/evaluation_results.json)

---

# Setting Up the Project Using uv

## 1. Install uv

Verify installation:

```bash
uv --version
```

---

## 2. Clone Repository

```bash
git clone <repository-url>
cd policyassist-ai
```

---

## 3. Create Virtual Environment

```bash
uv venv
```

---

## 4. Activate Environment

### Windows
```bash
.venv\Scripts\activate
```

### Linux/macOS
```bash
source .venv/bin/activate
```

---

## 5. Install Dependencies

```bash
uv sync
```

---

## 6. Configure Environment Variables

Create `.env` file with:
- OpenAI API key
- model configuration
- embedding model
- logging configuration

---

## 7. Run Application

CLI version:

```bash
python app/main.py
```

Streamlit version:

```bash
streamlit run streamlit_app.py
```

---

# How the System Works

## Step 1 — Customer Query
The user submits a support question or operational request.

---

## Step 2 — Intent Routing
The Intent Router Agent classifies:
- policy support queries
- claims queries
- operational requests
- restricted requests
- general questions

---

## Step 3 — Agent Selection
The query is routed to the appropriate domain-specific agent.

---

## Step 4 — Retrieval & Tool Usage
The selected agent:
- retrieves policy information
- uses operational tools if required
- gathers contextual information

---

## Step 5 — Response Generation
The system generates grounded responses using:
- retrieved documents
- tool outputs
- conversation memory
- prompt strategies

---

## Step 6 — Safety Review
The Safety Review Agent validates:
- restricted operations
- hallucination risks
- escalation requirements
- safety compliance

---

## Step 7 — Final Safe Response
The validated response is returned to the customer.

---

# Sample User Interactions

## Example 1 — Policy Coverage Query

### User Input
> “Does my policy cover cataract surgery?”

### Agent Response
> “Based on the retrieved policy section, cataract surgery is covered after the 24-month waiting period under surgical treatment benefits.”

---

## Example 2 — Claim Support Query

### User Input
> “What documents are required for reimbursement claims?”

### Agent Response
> “Hospital bills, discharge summaries, identity proof, and physician reports are typically required for reimbursement claims.”

---

## Example 3 — Allowed Operational Request

### User Input
> “Update my email address.”

### Agent Response
> “Your request to update the email address has been submitted successfully.”

---

## Example 4 — Restricted Request

### User Input
> “Reduce my insurance premium.”

### Agent Response
> “I’m unable to assist with this request because it involves restricted or unauthorized operations.”

---

# Prompt Engineering

The project evaluates multiple prompt strategies using:
- structured prompt comparisons
- safety-focused prompts
- retrieval-grounded prompts
- evaluation datasets
- before vs after analysis

---

# Evaluation Metrics

The system is evaluated using:
- retrieval accuracy
- hallucination rate
- response consistency
- escalation correctness
- refusal compliance
- tool routing accuracy
- latency measurements

---

# Failure Analysis

The project includes:
- root cause analysis
- debugging evidence
- retrieval failure analysis
- hallucination mitigation
- before vs after improvements

---

# Deployment Readiness

The system includes:
- modular architecture
- reproducible setup
- structured logging
- latency monitoring
- graceful failure handling
- environment-based configuration

---

# Known Limitations

- Responses depend on retrieval quality
- Operations are simulated for demonstration purposes
- Limited to provided policy documents
- Requires accurate retrieval sources
- Long conversations may require memory optimization

---

# Future Improvements

- Multi-language support
- Voice-enabled workflows
- Real insurance backend integration
- Human-in-the-loop approvals
- Advanced authorization systems
- Fine-tuned insurance-domain models

---

# Capstone Deliverables

This project includes:
- Working AI Agent
- [`docs/phase1/problem_framing_and_system_design.md`](docs/phase1/problem_framing_and_system_design.md)
- [`FINAL_DEMO_SCRIPT.md`](FINAL_DEMO_SCRIPT.md)
- [`PROMPT_COMPARISON_ANALYSIS.md`](PROMPT_COMPARISON_ANALYSIS.md)
- [`ENGINEERING_PRODUCT_JUSTIFICATION.md`](ENGINEERING_PRODUCT_JUSTIFICATION.md)
- [`docs/phase3/prompt_comparison.md`](docs/phase3/prompt_comparison.md)
- [`docs/phase9/evaluation_engineering_review.md`](docs/phase9/evaluation_engineering_review.md)
- [`app/evaluation/evaluation_results.json`](app/evaluation/evaluation_results.json)
- Safety Enforcement Demonstration

---

# Disclaimer

PolicyAssist AI is an educational capstone project designed to demonstrate enterprise AI agent engineering workflows for insurance customer support and controlled operational assistance.

The system does not provide legal, financial, or official insurance advice.

---