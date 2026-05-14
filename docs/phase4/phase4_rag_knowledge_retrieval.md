# Phase 4: Knowledge Retrieval & RAG Integration

## Table of Contents

1. [Phase Objective](#1-phase-objective)
2. [Phase 4 Requirements Coverage](#2-phase-4-requirements-coverage)
3. [Architecture Overview](#3-architecture-overview)
4. [Document Preparation & Embedding Pipeline](#4-document-preparation--embedding-pipeline)
5. [Semantic Chunking Strategy](#5-semantic-chunking-strategy)
6. [Embedding & Vector Database Implementation](#6-embedding--vector-database-implementation)
7. [Retriever Implementation](#7-retriever-implementation)
8. [RAG Agent Integration](#8-rag-agent-integration)
9. [RAG Prompt Engineering](#9-rag-prompt-engineering)
10. [Safety & Governance Integration](#10-safety--governance-integration)
11. [Compare Responses With and Without Retrieval](#11-compare-responses-with-and-without-retrieval)
12. [Missing Information Handling](#12-missing-information-handling)
13. [Retrieval Quality Testing](#13-retrieval-quality-testing)
14. [Execution Evidence](#14-execution-evidence)
15. [Technical Challenges & Debugging](#15-technical-challenges--debugging)
16. [Key Learnings](#16-key-learnings)
17. [Phase Summary](#17-phase-summary)

---

# 1. Phase Objective

The objective of Phase 4 was to transform PolicyAssist AI from a generic LLM-based insurance assistant into a Retrieval-Augmented Generation (RAG) system capable of:

- retrieving policy-grounded information using semantic search
- reducing hallucinated insurance responses
- answering using embedded insurance documents
- supporting multiple insurance policy domains
- improving factual reliability
- handling missing information safely

This phase introduced:

- embeddings
- semantic retrieval
- vector databases
- Retrieval-Augmented Generation (RAG)
- retrieval-grounded prompting
- semantic chunking
- retrieval-quality validation

---

# 2. Phase 4 Requirements Coverage

## Official Phase 4 Requirements

### Coding Requirements

- Implement embeddings and retrieval
- Enable document or data reference
- Show improvement over baseline

### Required Skills & Concepts

- embeddings
- semantic search
- RAG concepts
- text chunking
- vector databases
- retrieval-quality testing

### Required Tasks

| Requirement | Implementation |
|---|---|
| Prepare documents or datasets for embedding | Health, Auto, and Home insurance policy documents created |
| Implement semantic search using embeddings | OpenAI embeddings + ChromaDB semantic retrieval |
| Connect retrieval results to agent responses | Retrieved chunks injected into RAG prompts |
| Compare responses with and without retrieval | Baseline vs RAG testing completed |
| Handle cases where relevant information is missing | Missing-information safeguards implemented |

## Final Completion Status

| Requirement | Status |
|---|---|
| Prepare documents or datasets for embedding | Completed |
| Implement semantic search using embeddings | Completed |
| Connect retrieval results to agent responses | Completed |
| Compare responses with and without retrieval | Completed |
| Handle cases where relevant information is missing | Completed |
| Retrieval-quality testing | Completed |
| Vector database integration | Completed |
| Grounded RAG prompting | Completed |

---

# 3. Architecture Overview

## RAG Workflow

```text
Insurance Policy Documents
        ↓
Document Loader
        ↓
Text Chunking
        ↓
OpenAI Embeddings
        ↓
Chroma Vector Database
        ↓
Semantic Retrieval
        ↓
Retrieved Context Injection
        ↓
RAG Prompt
        ↓
LLM Response
        ↓
Safety Review Agent
        ↓
Final Response
```

## Technologies Used

| Component | Technology |
|---|---|
| LLM | OpenAI GPT |
| Framework | LangChain |
| Embeddings | OpenAI Embeddings |
| Vector Database | ChromaDB |
| Retrieval | Semantic Similarity Search |
| Chunking | RecursiveCharacterTextSplitter |
| Logging | Loguru |

---

# 4. Document Preparation & Embedding Pipeline

## Insurance Policy Datasets

Multiple insurance domains were added for semantic retrieval testing.

### Health Insurance

- cataract surgery coverage
- maternity waiting periods
- reimbursement claims
- exclusions

### Auto Insurance

- collision coverage
- vehicle addition
- accident claims
- driver updates

### Home Insurance

- fire damage coverage
- theft coverage
- disaster coverage

## Supported File Types

The ingestion pipeline supports:

- TXT files
- PDF files

## Document Loader Features

Implemented capabilities:

- TXT loading
- PDF loading
- metadata extraction
- exception handling
- configurable policy directories

---

# 5. Semantic Chunking Strategy

## Why Chunking Was Needed

Insurance policy documents contain:

- long procedural sections
- exclusions
- waiting periods
- policy conditions
- dense insurance terminology

Chunking improves retrieval precision and semantic search quality.

## Chunk Configuration

```python
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
```

## Semantic Separators

```python
separators=[
    "\n\n",
    "\n",
    ". ",
    " ",
    ""
]
```

## Improvements Observed

Larger semantic chunks improved:

- policy continuity
- retrieval accuracy
- waiting-period retrieval
- contextual grounding

---

# 6. Embedding & Vector Database Implementation

## Embedding Model

```python
OpenAIEmbeddings(
    model="text-embedding-3-small"
)
```

## Vector Database

ChromaDB was selected because it supports:

- local persistence
- semantic retrieval
- metadata support
- LangChain integration
- configurable collections

## ChromaDB Configuration

```python
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=VECTOR_DB_PATH,
    collection_name="policy_assist"
)
```

## Persistence Location

```text
data/embeddings/
```

This prevents rebuilding embeddings every application run.

---

# 7. Retriever Implementation

## Semantic Retriever

The retriever loads persisted vectors and performs semantic similarity search.

## Retriever Configuration

```python
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)
```

## Retrieval Goals

The retriever was designed to:

- retrieve relevant policy chunks
- support multi-policy retrieval
- improve factual grounding
- reduce hallucinations

---

# 8. RAG Agent Integration

## Previous Baseline Flow

```text
User Query → LLM → Response
```

## Updated RAG Flow

```text
User Query
    ↓
Semantic Retrieval
    ↓
Relevant Policy Chunks
    ↓
RAG Prompt
    ↓
Grounded LLM Response
```

## Retrieved Context Injection

```python
context = "\n\n".join(
    [doc.page_content for doc in retrieved_docs]
)
```

## Benefits

- retrieval-grounded responses
- policy-specific answers
- improved factual reliability
- reduced hallucination risk

---

# 9. RAG Prompt Engineering

## Prompt Objectives

The RAG prompt was redesigned to enforce:

- retrieval grounding
- hallucination prevention
- uncertainty handling
- operational safety
- missing-information acknowledgment

## Key Prompt Constraints

```text
- Use ONLY the retrieved policy information
- Never fabricate policy details
- Do not generate unsupported assumptions
- Clearly acknowledge missing information
```

## Governance-Aware Prompting

The prompt also enforced:

- no claim approval guarantees
- no reimbursement guarantees
- escalation guidance
- professional communication

---

# 10. Safety & Governance Integration

## Safety Review Layer

All generated responses pass through a secondary safety review agent.

## Classification Categories

| Classification | Purpose |
|---|---|
| SAFE | Normal grounded informational responses |
| ESCALATE | Sensitive or ambiguous operational workflows |
| RESTRICTED | Unsafe or unauthorized operations |

## Governance Examples

| Query | Result |
|---|---|
| What is the maternity waiting period? | SAFE |
| Can you reduce my premium? | ESCALATE |
| Approve my insurance claim | RESTRICTED |

## Governance Improvements

The escalation workflow was refined to:

- reduce over-escalation
- separate escalation vs restriction
- preserve usability
- maintain operational safety

---

# 11. Compare Responses With and Without Retrieval

## Objective

Responses were compared before and after retrieval integration to evaluate:

- factual grounding
- policy specificity
- hallucination reduction
- semantic retrieval quality
- response reliability

---

## Without Retrieval (Baseline System)

### Architecture

```text
User Query → LLM Prompt → Response
```

### Observed Limitations

- generic insurance explanations
- estimated policy details
- unsupported assumptions
- inconsistent factual grounding
- hallucination risk

---

## With Retrieval (RAG System)

### Architecture

```text
User Query
    ↓
Semantic Retrieval
    ↓
Relevant Policy Chunks
    ↓
Retrieved Context Injection
    ↓
Grounded LLM Response
```

### Improvements Observed

- retrieval-grounded responses
- policy-specific answers
- reduced hallucinations
- improved factual consistency
- safer uncertainty handling

---

## Baseline vs RAG Comparison Table

| Query | Baseline Response | RAG Response |
|---|---|---|
| Does my policy cover cataract surgery? | Generic surgery explanation | Retrieved cataract surgery policy details |
| What is the waiting period for maternity coverage? | Estimated waiting period range | Exact 36-month waiting period |
| What is covered under collision coverage? | Generic auto explanation | Retrieved repair expense coverage |
| Does home insurance cover fire damage? | Generic fire coverage explanation | Retrieved structural repair coverage |
| Does my policy cover dental implants? | Risk of unsupported assumptions | Safe missing-information acknowledgment |

---

## Example Comparison

### Query

```text
What is the waiting period for maternity coverage?
```

### Baseline Response (Without Retrieval)

```text
The waiting period for maternity coverage varies by insurer and policy. It commonly ranges from 9 to 12 months.
```

### Problems in Baseline Response

- not grounded in policy documents
- estimated answer
- generic explanation
- hallucination risk

---

### RAG Response (With Retrieval)

```text
The waiting period for maternity benefits eligibility is 36 continuous months from the policy start date.
```

### Improvements

- exact policy-grounded answer
- retrieval-backed response
- reduced hallucination risk
- improved factual accuracy

---

# 12. Missing Information Handling

## Objective

Prevent hallucinated insurance responses when policy information is unavailable.

## Missing Information Rules

```text
- Clearly acknowledge missing information
- Do not fabricate policy details
- Recommend human review when needed
```

## Example Queries

| Query | Expected Behavior |
|---|---|
| Does my policy cover dental implants? | Acknowledge unavailable information |
| What is the LASIK surgery coverage limit? | Avoid unsupported assumptions |

## Benefits

This improved:

- operational safety
- response trustworthiness
- hallucination resistance
- compliance behavior

---

# 13. Retrieval Quality Testing

## Retrieval Validation Queries

| Query | Expected Retrieval |
|---|---|
| Cataract surgery | Health policy |
| Collision coverage | Auto policy |
| Fire damage | Home policy |
| Maternity waiting period | Health maternity section |

## Testing Goals

- validate semantic similarity search
- confirm correct policy retrieval
- ensure multi-domain retrieval
- evaluate grounding quality

## Retrieval Outcome

Semantic retrieval successfully:

- matched queries to correct policy domains
- retrieved relevant chunks
- improved response grounding

---

# 14. Execution Evidence

## Screenshot Index

| Screenshot | Purpose | Link |
|---|---|---|
| rag_execution_policy_info_1.png | Health policy retrieval | [View Screenshot](screenshots/rag_execution_policy_info_1.png) |
| rag_execution_policy_info_2.png | Multi-domain retrieval | [View Screenshot](screenshots/rag_execution_policy_info_2.png) |
| rag_execution_missing_info.png | Missing information handling | [View Screenshot](screenshots/rag_execution_missing_info.png) |
| rag_execution_escalation.png | Escalation and restriction workflows | [View Screenshot](screenshots/rag_execution_escalation.png) |
| rag_retrieval_logs.png | Embedding and vector database logs | [View Screenshot](screenshots/rag_retrieval_logs.png) |

---

## 14.1 Health Policy Retrieval

### Screenshot

```text
rag_execution_policy_info_1.png
```

### Queries Executed

```text
Does my policy cover cataract surgery?

What is the waiting period for maternity coverage?
```

### Evidence Demonstrated

- semantic retrieval
- grounded policy answers
- waiting period retrieval
- safe grounded responses

---

## 14.2 Multi-Domain Retrieval

### Screenshot

```text
rag_execution_policy_info_2.png
```

### Queries Executed

```text
What is covered under collision coverage?

Does home insurance cover fire damage?
```

### Evidence Demonstrated

- multi-policy retrieval
- semantic similarity search
- grounded policy responses

---

## 14.3 Missing Information Handling

### Screenshot

```text
rag_execution_missing_info.png
```

### Queries Executed

```text
Does my policy cover dental implants?

What is the coverage limit for LASIK surgery?
```

### Evidence Demonstrated

- hallucination prevention
- uncertainty handling
- safe limitation acknowledgment

---

## 14.4 Escalation & Restriction Governance

### Screenshot

```text
rag_execution_escalation.png
```

### Queries Executed

```text
Can you reduce my premium?

Why was my claim rejected?

Approve my insurance claim immediately.
```

### Evidence Demonstrated

- escalation workflows
- restricted operation blocking
- governance-aware orchestration

---

## 14.5 Retrieval Infrastructure Logs

### Screenshot

```text
rag_retrieval_logs.png
```

### Evidence Demonstrated

- document ingestion
- chunk generation
- embedding initialization
- ChromaDB persistence
- stored vector validation
- observability logging

---

# 15. Technical Challenges & Debugging

## Challenge 1: Empty Retrieval Context

### Issue

Retriever returned empty retrieval context despite embeddings being generated.

### Root Cause

Chroma collections were inconsistent because collection names were not shared.

### Fix

```python
collection_name="policy_assist"
```

was added to:

- vector creation
- vector loading

---

## Challenge 2: Fragmented Retrieval

### Issue

Small chunks fragmented policy sections.

### Fix

```python
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
```

Improved:

- retrieval continuity
- semantic context
- waiting period retrieval

---

## Challenge 3: Over-Escalation

### Issue

Safety reviewer escalated many informational responses.

### Fix

Reviewer logic was simplified to:

- prefer SAFE for informational responses
- reserve ESCALATE for sensitive workflows
- reserve RESTRICTED for unsafe operations

---

# 16. Key Learnings

## Technical Learnings

- semantic chunking strongly affects retrieval quality
- retrieval grounding reduces hallucinations
- Chroma collection management is important
- observability logging simplifies RAG debugging

## AI Safety Learnings

- over-aggressive safety review reduces usability
- uncertainty should not always trigger escalation
- governance workflows require balanced tuning

## Architecture Learnings

- RAG improves enterprise reliability
- grounded prompting improves factual consistency
- vector persistence improves performance
- semantic retrieval supports multi-domain systems

---

# 17. Phase Summary

Phase 4 successfully transformed PolicyAssist AI into a Retrieval-Augmented Generation (RAG) system capable of:

- semantic policy retrieval
- grounded insurance explanations
- vector-based search
- hallucination reduction
- multi-policy support
- governance-aware orchestration
- missing-information handling

The system now supports:

- embeddings
- semantic search
- ChromaDB persistence
- retrieval-grounded prompting
- multi-domain policy retrieval
- enterprise-style governance workflows

This phase established the foundational knowledge infrastructure required for scalable and reliable enterprise AI support systems.