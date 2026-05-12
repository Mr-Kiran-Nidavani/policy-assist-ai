# Problem Framing — Phase 1

## Project Name
# PolicyAssist AI

## Project Description

PolicyAssist AI is a safety-first lightweight orchestrated multi-agent insurance support and controlled operations assistant designed to help existing policyholders understand insurance coverage, claims procedures, exclusions, deductibles, waiting periods, and operational workflows using AI-powered retrieval, conversational reasoning, contextual memory, and controlled tool usage.

The system combines:
- retrieval-augmented generation (RAG)
- multi-agent orchestration
- operational tools
- conversational memory
- safety validation
- escalation handling

to provide enterprise-style insurance customer support assistance.

PolicyAssist AI supports:
- policy clarification
- claims guidance
- low-risk operational assistance
- customer profile updates
- policy-related workflows
- safe refusal handling

The architecture follows a modular multi-agent workflow with dedicated responsibilities for:
- intent routing
- policy information support
- claims assistance
- operational request handling
- safety validation and escalation review

---

# Problem Statement

Insurance customers often struggle to understand:
- policy coverage
- claims procedures
- waiting periods
- deductibles
- exclusions
- operational workflows
- policy update procedures

due to:
- complex policy wording
- insurance terminology
- delayed support responses
- inconsistent support quality

Insurance support teams frequently handle repetitive customer requests that require:
- manual document searches
- operational verification
- repeated policy explanations
- escalation handling

This results in:
- delayed response times
- increased operational workload
- inconsistent customer experiences
- operational inefficiencies
- customer frustration

PolicyAssist AI aims to improve insurance support efficiency by providing safe, explainable, retrieval-grounded, and operationally controlled assistance while enforcing strict guardrails for high-risk actions.

---

# Primary User Persona

## Existing Insurance Policyholder

The primary user is an existing insurance customer seeking assistance regarding:
- policy coverage
- claims guidance
- waiting periods
- exclusions
- deductibles
- claim documentation
- customer profile updates
- driver and vehicle additions
- operational policy workflows

---

# User Characteristics

| Attribute | Description |
|---|---|
| User Type | Existing policyholder |
| Technical Expertise | Low to Medium |
| Primary Goal | Fast and accurate insurance support |
| Pain Points | Complex policy wording and delayed support |
| Expectations | Safe, explainable, and trustworthy responses |

---

# Current Workflow (Without AI)

```text
Customer submits support request
        ↓
Human support agent reviews request
        ↓
Agent manually searches policy documents
        ↓
Agent verifies operational permissions
        ↓
Agent explains policy or processes request
        ↓
Escalation occurs if request is high-risk
```

---

# Problems in Existing Workflow

| Problem | Impact |
|---|---|
| Manual document searches | Slow response times |
| Repetitive customer requests | Increased operational workload |
| Inconsistent policy explanations | Reduced customer trust |
| Complex policy terminology | Customer confusion |
| High support ticket volume | Support agent overload |
| Operational verification delays | Poor customer experience |

---

# Multi-Agent System Architecture

PolicyAssist AI follows a lightweight orchestrated multi-agent architecture.

The system contains multiple domain-specific agents with dedicated responsibilities.

| Agent | Responsibility |
|---|---|
| Intent Router Agent | Detects user intent and routes workflows |
| Policy Information Agent | Handles policy explanations using retrieval workflows |
| Claim Support Agent | Handles claims guidance and claim-related support |
| Policy Update Agent | Handles approved low-risk operational requests |
| General Query Agent | Handles greetings and unsupported requests |
| Safety Review Agent | Validates outputs and enforces safety policies |

---

# AI Agent Role

PolicyAssist AI is designed to:
- answer insurance policy-related questions
- retrieve relevant policy clauses
- explain policy coverage in simplified language
- guide customers through claims procedures
- assist with approved low-risk customer operations
- provide escalation guidance when required
- validate responses before returning them to customers

---

# Supported Operations

The system supports approved low-risk customer service operations.

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

---

# Restricted Operations

The system enforces strict restrictions on high-risk actions.

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

# Inputs & Outputs

# Inputs

The system accepts:
- customer support questions
- operational requests
- policy-related queries
- claims-related questions
- conversation history
- retrieved policy documents

---

# Outputs

The system provides:
- policy explanations
- claims guidance
- operational assistance
- escalation recommendations
- safe refusal responses
- uncertainty-aware responses
- contextual follow-up responses

---

# Constraints & Assumptions

# Constraints

| Constraint | Description |
|---|---|
| Restricted operational scope | High-risk actions are blocked |
| Retrieval dependency | Responses depend on available documents |
| Safety-first design | Unsafe requests must be refused |
| Limited domain scope | Insurance workflows only |
| No legal advice | Informational assistance only |
| Simulated backend operations | No real insurance backend integration |

---

# Assumptions

| Assumption | Description |
|---|---|
| Policy documents are accurate | Retrieval sources are trusted |
| Customer communicates in English | Initial version supports English only |
| Backend tools are simulated | Operations are demonstration-only |
| Internet access is optional | Retrieval may function locally |

---

# Example User Questions

## Policy Coverage Questions
- “Does my policy cover knee replacement surgery?”
- “What is the waiting period for maternity coverage?”
- “Is cataract surgery included in my plan?”

---

## Claims Questions
- “What documents are required for reimbursement claims?”
- “Why was my claim rejected?”
- “What is the current status of my claim?”

---

## Operational Requests
- “Update my email address.”
- “Add a new driver to my policy.”
- “Add a vehicle to my insurance plan.”

---

## Restricted Requests
- “Reduce my insurance premium.”
- “Change my policy effective date.”
- “Approve my insurance claim immediately.”

---

# Success Criteria

# Functional Success Criteria

| Criteria | Expected Outcome |
|---|---|
| Accurate retrieval | Correct policy clauses retrieved |
| Helpful responses | Clear and understandable guidance |
| Safe operational handling | Approved operations handled safely |
| Proper refusal handling | Restricted requests rejected |
| Proper escalation | High-risk queries escalated |
| Multi-turn understanding | Context maintained during conversations |

---

# Technical Success Criteria

| Metric | Goal |
|---|---|
| Retrieval relevance | High |
| Hallucination rate | Low |
| Response consistency | Stable |
| Tool routing accuracy | Correct |
| Safety validation accuracy | High |
| Failure handling | Graceful |

---

# User Experience Success Criteria

| Goal | Indicator |
|---|---|
| Faster support | Reduced response delays |
| Better clarity | Simplified policy explanations |
| Higher trust | Grounded and explainable responses |
| Better escalation | Proper human handoff |
| Improved usability | Easier operational assistance |

---

# Failure Cases

| Failure Scenario | Potential Risk |
|---|---|
| Hallucinated policy coverage | Customer misinformation |
| Missing retrieval context | Incomplete answers |
| Unsafe operational approval | Unauthorized action |
| Incorrect tool routing | Workflow failure |
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
- claim approvals
- premium reductions
- high-risk policy modifications
- payment processing
- legal guarantees
- unauthorized operations

---

## Escalation Handling

The system must escalate:
- disputed claims
- fraud-related concerns
- policy conflicts
- legal complaints
- unresolved customer dissatisfaction
- operational requests requiring human approval

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
- avoid storing personal customer data
- mask sensitive information in logs
- follow privacy-safe logging practices

---

# Workflow Overview

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

# Expected Business Impact

PolicyAssist AI aims to:
- reduce repetitive customer support workload
- improve response consistency
- shorten customer response times
- improve customer understanding of policies
- streamline low-risk operational assistance
- improve escalation workflows
- provide scalable insurance support assistance

---

# Conclusion

PolicyAssist AI is designed as a safe, explainable, retrieval-grounded, and operationally controlled lightweight orchestrated multi-agent insurance support assistant focused on improving customer support workflows while maintaining strict operational and safety boundaries.

The system prioritizes:
- grounded responses
- operational safety
- explainability
- escalation awareness
- responsible AI behaviour
- controlled operational assistance

---