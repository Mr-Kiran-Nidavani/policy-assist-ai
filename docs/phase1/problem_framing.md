# PolicyAssist AI  
## Phase 1 — Problem Framing & Success Definition

# Project Description

PolicyAssist AI is a safety-first lightweight orchestrated multi-agent insurance support assistant designed to help users understand general insurance concepts, policy coverage information, claims procedures, exclusions, deductibles, and basic customer support workflows using AI-powered retrieval, conversational reasoning, contextual memory, and controlled tool usage.

The system follows a modular multi-agent architecture where specialized agents collaborate to:
- provide general insurance information using Retrieval-Augmented Generation (RAG)
- assist existing policyholders with policy-specific information using controlled tools
- support limited low-risk customer detail updates
- provide claims process guidance
- enforce operational safety restrictions and escalation handling

PolicyAssist AI supports:
- general insurance education
- policy coverage clarification
- existing policy information lookup
- claims process guidance
- basic customer detail updates
- safe refusal handling

The system allows only limited low-risk operations such as:
- updating email address
- updating phone number

The system strictly restricts high-risk policy modifications including:
- adding drivers
- adding vehicles
- changing policy effective dates
- modifying policy coverage
- claim approval promises
- reimbursement guarantees
- premium reduction requests

The system prioritizes:
- retrieval-grounded responses
- explainable assistance
- operational safety
- controlled tool access
- responsible AI behaviour

---

# Problem Statement

Insurance customers often struggle to understand:
- insurance terminology
- policy coverage
- deductibles
- exclusions
- claim submission procedures
- reimbursement workflows
- policy expiration details
- customer support processes

Customers also experience delays when trying to retrieve information about their existing insurance policy due to:
- manual customer support workflows
- repetitive support requests
- long response times
- inconsistent explanations from support teams

Insurance support teams frequently spend time handling repetitive low-risk informational requests such as:
- explaining policy terms
- answering coverage questions
- checking policy expiration dates
- explaining claims procedures
- updating customer contact details

This creates:
- operational inefficiencies
- increased support workload
- inconsistent customer experiences
- customer frustration
- delayed response handling

PolicyAssist AI aims to improve insurance support efficiency by providing safe, explainable, retrieval-grounded, and operationally controlled assistance while enforcing strict restrictions on unsafe or high-risk insurance operations.

---

# Primary User Persona

## Existing Insurance Policyholder

The primary user is an existing insurance customer seeking help with:
- policy information
- policy expiration details
- insurance terminology
- claims procedures
- required claim documents
- deductibles
- exclusions
- contact detail updates

---

# User Characteristics

| Attribute | Description |
|---|---|
| User Type | Existing policyholder |
| Technical Expertise | Low to Medium |
| Primary Goal | Quick and accurate insurance support |
| Pain Points | Complex policy wording and delayed support |
| Expectations | Safe, explainable, and trustworthy responses |

---

# Current Workflow (Without AI)

```text
Customer submits support request
        ↓
Human support agent reviews request
        ↓
Agent manually checks policy records
        ↓
Agent searches policy documents
        ↓
Agent explains coverage or process
        ↓
Operational verification is performed
        ↓
Escalation occurs for restricted requests
```

---

# Problems in Existing Workflow

| Problem | Impact |
|---|---|
| Manual policy lookup | Slow response times |
| Repetitive support requests | Increased support workload |
| Complex insurance terminology | Customer confusion |
| Inconsistent explanations | Reduced customer trust |
| High support volume | Operational inefficiency |
| Delayed operational verification | Poor customer experience |

---

# Multi-Agent System Architecture

PolicyAssist AI follows a lightweight orchestrated multi-agent architecture where specialized agents collaborate to handle different insurance support workflows.

| Agent | Responsibility |
|---|---|
| Query Orchestrator Agent | Detects user intent and routes requests to the correct workflow |
| General Policy Information Agent | Explains insurance concepts and policy terminology using RAG |
| Existing Policy Support Agent | Retrieves policyholder-specific information using controlled tools |
| Claims Support Agent | Provides claims process guidance and claim documentation support |
| Customer Details Update Agent | Handles approved low-risk customer detail updates |
| Safety Review Agent | Validates outputs, enforces restrictions, and handles escalation review |

---

# AI Agent Role

PolicyAssist AI is designed to:
- explain insurance concepts
- retrieve policy-related information
- assist existing policyholders with policy-specific queries
- guide users through claims procedures
- support approved low-risk customer detail updates
- refuse restricted operational requests
- avoid unsupported guarantees or promises
- validate responses before returning them to users

---

# Supported Operations

The system supports informational assistance and limited low-risk customer detail updates.

| Operation | Status |
|---|---|
| General insurance explanation | ✅ Supported |
| Policy coverage explanation | ✅ Supported |
| Existing policy information lookup | ✅ Supported |
| Claims process guidance | ✅ Supported |
| Claim document guidance | ✅ Supported |
| Update email address | ✅ Supported |
| Update phone number | ✅ Supported |

---

# Restricted Operations

The system enforces strict restrictions on high-risk operations and unsupported insurance actions.

| Operation | Status |
|---|---|
| Add new driver | ❌ Restricted |
| Add new vehicle | ❌ Restricted |
| Change policy effective date | ❌ Restricted |
| Modify policy coverage | ❌ Restricted |
| Reduce insurance premium | ❌ Restricted |
| Claim approval or rejection | ❌ Restricted |
| Promise early claim approval | ❌ Restricted |
| Waive deductibles | ❌ Restricted |
| Cancel policy | ❌ Restricted |
| Legal or financial guarantees | ❌ Restricted |

---

# Inputs & Outputs

## Inputs

The system accepts:
- customer support questions
- policy-related queries
- claims-related questions
- customer detail update requests
- conversation history
- retrieved policy documents
- simulated policy records

---

## Outputs

The system provides:
- insurance explanations
- policy information
- claims guidance
- customer detail update confirmations
- escalation recommendations
- safe refusal responses
- uncertainty-aware responses

---

# Constraints & Assumptions

## Constraints

| Constraint | Description |
|---|---|
| Restricted operational scope | High-risk actions are blocked |
| Retrieval dependency | Responses depend on available documents |
| Safety-first design | Unsafe requests must be refused |
| Limited operational permissions | Only approved updates allowed |
| No legal advice | Informational assistance only |
| Simulated backend tools | No real insurance backend integration |

---

## Assumptions

| Assumption | Description |
|---|---|
| Policy documents are accurate | Retrieval sources are trusted |
| Customer communicates in English | Initial version supports English only |
| Backend tools are simulated | Operations are demonstration-only |
| Internet access is optional | Retrieval may function locally |

---

# Example User Questions

## Existing Policy Questions
- “What is my policy expiration date?”
- “Does my policy include roadside assistance?”

---

## General Insurance Questions
- “What is collision coverage?”
- “What is a deductible?”

---

## Claims Support Questions
- “How do I submit a claim?”
- “What documents are required for reimbursement claims?”

---

## Allowed Operational Requests
- “Update my phone number.”
- “Update my email address.”

---

## Restricted Requests
- “Change my policy effective date.”
- “Add a new driver to my policy.”
- “Approve my insurance claim immediately.”

---

# Success Criteria

## Functional Success Criteria

| Criteria | Expected Outcome |
|---|---|
| Accurate retrieval | Correct policy clauses retrieved |
| Helpful responses | Clear and understandable guidance |
| Safe operational handling | Only approved updates allowed |
| Proper refusal handling | Restricted requests rejected |
| Proper escalation | High-risk requests escalated |
| Multi-turn understanding | Context maintained during conversations |

---

## Technical Success Criteria

| Metric | Goal |
|---|---|
| Retrieval relevance | High |
| Hallucination rate | Low |
| Response consistency | Stable |
| Tool routing accuracy | Correct |
| Safety validation accuracy | High |
| Failure handling | Graceful |

---

## User Experience Success Criteria

| Goal | Indicator |
|---|---|
| Faster support | Reduced response delays |
| Better clarity | Simplified insurance explanations |
| Higher trust | Grounded and explainable responses |
| Better escalation | Proper human handoff |
| Improved usability | Easier customer support experience |

---

# Failure Cases

| Failure Scenario | Potential Risk |
|---|---|
| Hallucinated policy coverage | Customer misinformation |
| Missing retrieval context | Incomplete responses |
| Unsafe operational approval | Unauthorized action |
| Incorrect tool routing | Workflow failure |
| Unsupported claim promise | Customer trust issues |
| Long conversations | Context loss |

---

# Edge Scenarios

| Edge Case | Expected Behaviour |
|---|---|
| Missing policy information | Ask clarifying questions |
| Unsupported request | Refuse safely |
| Unknown coverage details | Express uncertainty |
| High-risk operational request | Escalate or refuse |
| Conflicting policy clauses | Recommend human review |

---

# Safety Requirements

## Refusal Handling

The system must refuse:
- claim approval promises
- reimbursement guarantees
- policy modification requests
- policy effective date changes
- adding drivers or vehicles
- premium reduction requests
- legal or financial guarantees
- unauthorized operations

---

## Escalation Handling

The system must escalate:
- disputed claims
- policy conflicts
- legal complaints
- unresolved customer dissatisfaction
- unsupported operational requests
- high-risk requests requiring human approval

---

## Uncertainty Handling

The system must:
- avoid guessing
- explain uncertainty clearly
- avoid fabricated policy information
- avoid unsupported operational claims

---

## Logging Safety

The system must:
- avoid storing sensitive customer data
- mask customer identifiers in logs
- follow privacy-safe logging practices

---

# Workflow Overview

```text
Customer Query
      ↓
Query Orchestrator Agent
      ↓
──────────────────────────────────────────────
│                │                │
↓                ↓                ↓
General Policy   Existing         Claims
Information      Policy           Support
Agent            Support Agent    Agent
                                   │
                                   ↓
                        Customer Details
                           Update Agent
                                   ↓
                          Safety Review Agent
                                   ↓
                         Final Safe Response
```

---

# Expected Business Impact

PolicyAssist AI aims to:
- reduce repetitive customer support workload
- improve response consistency
- shorten customer response times
- improve customer understanding of insurance policies
- streamline low-risk customer support workflows
- improve escalation handling
- provide scalable insurance support assistance

---

# Conclusion

PolicyAssist AI is designed as a safe, explainable, retrieval-grounded, and operationally controlled lightweight multi-agent insurance support assistant focused on improving customer support workflows while maintaining strict operational and safety boundaries.

The system prioritizes:
- grounded responses
- operational safety
- explainability
- escalation awareness
- responsible AI behaviour
- controlled operational assistance

---