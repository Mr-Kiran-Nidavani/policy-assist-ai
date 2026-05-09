# Problem Framing — Phase 1

## Project Name
# PolicyAssist AI

## Project Description

PolicyAssist AI is a safety-first insurance customer support agent designed to help existing policyholders understand insurance coverage, claims procedures, exclusions, deductibles, and policy-related queries using AI-powered retrieval, conversational reasoning, and contextual memory.

The system operates as a decision-support assistant and does not perform transactional actions such as approving claims, modifying policies, or processing payments.

---

# Problem Statement

Insurance customers often struggle to understand policy coverage, claims procedures, exclusions, and waiting periods due to complex policy documents and delayed customer support responses.

Customer support teams frequently handle repetitive queries that require manual document searches and policy interpretation, resulting in:
- delayed response times
- inconsistent support quality
- increased operational workload
- customer frustration

PolicyAssist AI aims to improve customer support efficiency by providing safe, explainable, and retrieval-grounded insurance support assistance while preventing unsafe or unauthorized actions.

---

# Primary User Persona

## Existing Insurance Policyholder

The primary user is an existing insurance customer seeking support regarding:
- policy coverage
- claims guidance
- exclusions
- deductibles
- waiting periods
- claim documentation requirements

---

# User Characteristics

| Attribute | Description |
|---|---|
| User Type | Existing policyholder |
| Technical Expertise | Low to Medium |
| Primary Goal | Fast and accurate policy clarification |
| Pain Points | Complex policy language and long support wait times |
| Expectations | Clear, trustworthy, explainable responses |

---

# Current Workflow (Without AI)

```text
Customer submits support query
        ↓
Human support agent reviews query
        ↓
Agent searches policy documents manually
        ↓
Agent interprets clauses and procedures
        ↓
Customer receives response
        ↓
Escalation if issue remains unresolved
```

---

# Problems in Existing Workflow

| Problem | Impact |
|---|---|
| Manual policy search | Slow support responses |
| Repetitive customer queries | Increased operational workload |
| Inconsistent interpretations | Reduced customer trust |
| Complex insurance terminology | Customer confusion |
| High support ticket volume | Agent overload |

---

# AI Agent Role

PolicyAssist AI is designed to:
- answer insurance policy-related support queries
- retrieve relevant policy clauses
- explain policy coverage in simplified language
- guide customers through claims procedures
- provide escalation guidance when necessary

---

# Agent Limitations

The AI agent will NOT:
- approve or reject claims
- modify policy information
- process payments
- provide legal guarantees
- fabricate policy information
- make financial decisions on behalf of customers

---

# Inputs & Outputs

# Inputs

The system accepts:
- customer support questions
- policy-related queries
- claim-related questions
- conversation history
- retrieved policy documents

---

# Outputs

The system provides:
- policy explanations
- claims guidance
- clause summaries
- escalation recommendations
- safe refusal responses
- uncertainty-aware responses

---

# Constraints & Assumptions

# Constraints

| Constraint | Description |
|---|---|
| Non-transactional system | Cannot modify claims or policies |
| Retrieval dependency | Responses depend on available documents |
| Safety-first design | Unsafe requests must be refused |
| Limited domain scope | Insurance support only |
| No legal advice | Informational assistance only |

---

# Assumptions

| Assumption | Description |
|---|---|
| Policy documents are accurate | Retrieval source is trusted |
| Customer communicates in English | Initial version supports English only |
| Backend tools are simulated | Mock tools used for demonstrations |
| Internet access is optional | Retrieval can function locally |

---

# Example User Questions

## Coverage Questions
- “Does my policy cover knee replacement surgery?”
- “What is the waiting period for maternity coverage?”

---

## Claims Questions
- “What documents are required for hospitalization claims?”
- “Why was my claim rejected?”

---

## Deductible Questions
- “How much deductible do I need to pay?”

---

## Unsafe Requests
- “Approve my insurance claim immediately.”
- “Add my spouse to the policy.”

---

# Success Criteria

# Functional Success Criteria

| Criteria | Expected Outcome |
|---|---|
| Accurate retrieval | Correct policy clauses retrieved |
| Helpful responses | Clear and understandable guidance |
| Safe refusal handling | Unsafe requests are rejected |
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
| Failure handling | Graceful |

---

# User Experience Success Criteria

| Goal | Indicator |
|---|---|
| Faster support | Reduced response delays |
| Better clarity | Simplified explanations |
| Higher trust | Grounded responses |
| Better escalation | Proper human handoff |

---

# Failure Cases

| Failure Scenario | Potential Risk |
|---|---|
| Hallucinated policy coverage | Customer misinformation |
| Missing retrieval context | Incomplete answers |
| Ambiguous customer queries | Incorrect interpretation |
| Unsafe tool usage | Unauthorized operations |
| Long conversations | Context loss |

---

# Edge Scenarios

| Edge Case | Expected Behaviour |
|---|---|
| Missing policy information | Ask clarifying questions |
| Unsupported request | Refuse safely |
| Unknown coverage details | Express uncertainty |
| Angry customer interactions | Escalate politely |
| Conflicting policy clauses | Recommend human review |

---

# Safety Requirements

## Refusal Handling

The system must refuse:
- claim approvals
- policy modifications
- payment processing
- legal guarantees
- unauthorized actions

---

## Escalation Handling

The system must escalate:
- disputed claims
- legal complaints
- fraud-related concerns
- unclear policy conflicts
- unresolved customer dissatisfaction

---

## Uncertainty Handling

The system must:
- avoid guessing
- explain uncertainty clearly
- avoid fabricated policy information

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
PolicyAssist AI
      ↓
Retrieve Relevant Policy Information
      ↓
Generate Safe & Grounded Response
      ↓
Escalate if Necessary
```

---

# Expected Business Impact

PolicyAssist AI aims to:
- reduce repetitive customer support workload
- improve response consistency
- shorten support response times
- improve customer understanding of policies
- provide scalable insurance support assistance

---

# Conclusion

PolicyAssist AI is designed as a safe, explainable, and retrieval-grounded insurance customer support assistant focused on improving policy clarification workflows while maintaining strict operational and safety boundaries.

The system prioritizes:
- grounded responses
- customer safety
- explainability
- escalation awareness
- responsible AI behaviour

---