# Final Demo Script

## Index

- [1. Purpose](#1-purpose)
- [2. Setup Steps](#2-setup-steps)
- [3. Additional Operations & Validation](#3-additional-operations--validation)
  - [3.1 Application Logs](#31-application-logs)
  - [3.2 Evaluation Execution](#32-evaluation-execution)
  - [3.3 Feedback Tracking](#33-feedback-tracking)
- [4. Assignment Requirement Coverage](#4-assignment-requirement-coverage)

- [5. Final Demo Scenarios](#5-final-demo-scenarios)
  - [5.1 Scenario 1 — Policy Information Retrieval](#51-scenario-1--policy-information-retrieval)
  - [5.2 Scenario 2 — Claims Guidance](#52-scenario-2--claims-guidance)
  - [5.3 Scenario 3 — Operational Update Tool Workflow](#53-scenario-3--operational-update-tool-workflow)
  - [5.4 Scenario 4 — Restricted Operation Refusal](#54-scenario-4--restricted-operation-refusal)
  - [5.5 Scenario 5 — Workflow Continuity & Multi-Turn Interaction](#55-scenario-5--workflow-continuity--multi-turn-interaction)
  - [5.6 Scenario 6 — Evaluation Harness Execution](#56-scenario-6--evaluation-harness-execution)
  - [5.7 Scenario 7 — Retrieval Comparison Evaluation](#57-scenario-7--retrieval-comparison-evaluation)
  - [5.8 Scenario 8 — CLI Workflow Execution](#58-scenario-8--cli-workflow-execution)
  - [5.9 Scenario 9 — Runtime Recovery & Fault Handling](#59-scenario-9--runtime-recovery--fault-handling)

- [6. Demo Notes](#6-demo-notes)

---

# 1. Purpose

This demo script is intended for evaluators and reviewers to validate the PolicyAssist AI system across:
- retrieval-grounded insurance responses
- claims guidance workflows
- tool execution
- workflow continuity
- safety enforcement
- evaluation engineering
- runtime recovery
- CLI and Streamlit interaction modes

The demo scenarios simulate realistic insurance support workflows while demonstrating engineering reliability, explainability, and safety-first behaviour.

---

# 2. Setup Steps

## Step 1 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 2 — Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_BASE=https://openai.vocareum.com/v1
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4.1-mini
EMBEDDING_MODEL=text-embedding-3-small
```

---

## Step 3 — Build Vector Database

```bash
python app/build_vector_db.py
```

---

## Step 4 — Run Streamlit UI

```bash
streamlit run app/ui/streamlit_app.py
```

---

## Step 5 — Run CLI Version

```bash
python app/main.py
```

---


# 3. Additional Operations & Validation

## 3.1 Application Logs

Runtime logs can be monitored in:

```text
logs/policyassist.log
```

The logs include:
- routing information
- agent execution
- latency tracking
- safety review status
- runtime exceptions
- evaluation traces

---

## 3.2 Evaluation Execution

Run the evaluation harness:

```bash
python app/evaluation/run_evaluation.py
```

Run retrieval-aware comparison evaluation:

```bash
python app/evaluation/run_retrieval_comparison.py
```

Evaluation outputs are stored in:

```text
app/evaluation/evaluation_results.json
app/evaluation/retrieval_comparison_results.json
```

These files contain:
- evaluation scores
- latency metrics
- consistency testing
- retrieval diagnostics
- RAG vs no-RAG comparison results

---

## 3.3 Feedback Tracking

User feedback interactions are stored in:

```text
app/feedback/feedback_log.json
```

The feedback system is used for:
- adaptive behaviour workflows
- response improvement analysis
- conversational refinement tracking

---

# 4. Assignment Requirement Coverage

| Requirement | Demonstrated In |
|---|---|
| Retrieval grounding | Scenario 5.1 |
| Tool usage | Scenario 5.3 |
| Workflow continuity | Scenario 5.5 |
| Safety enforcement | Scenario 5.4 |
| Evaluation framework | Scenario 5.6 |
| Retrieval-aware evaluation | Scenario 5.7 |
| Runtime recovery | Scenario 5.9 |
| Multi-agent orchestration | Scenarios 5.1–5.5 |
| Runtime logging | Scenario 5.8 & 5.9 |
| Explainability | CLI evaluation outputs |

---

# 5. Final Demo Scenarios

# 5.1 Scenario 1 — Policy Information Retrieval

## User Queries

```text
what deductibles covered in my policy?
what vehicles are covered in my policy?
```

---

## Expected Behaviour

- The intent router routes requests to the policy information agent.
- Relevant policy sections are retrieved using the vector database.
- The response explains:
  - deductibles
  - covered vehicles
  - policy conditions
- The response remains grounded in retrieved insurance policy content.

---

## Why This Matters

This demonstrates:
- Retrieval-Augmented Generation (RAG)
- grounded insurance responses
- retrieval accuracy
- explainable policy guidance

---

## Evidence

![Policy Retrieval](screenshots/demo/demo_policy_retrieval.png)

---

# 5.2 Scenario 2 — Claims Guidance

## User Query

```text
How to submit claim and what documents are required?
```

---

## Expected Behaviour

- The claim support agent provides:
  - claim submission guidance
  - required documentation
  - reimbursement workflow information
- The system avoids claim approval guarantees.
- The assistant escalates when necessary.

---

## Why This Matters

This demonstrates:
- claims workflow support
- safety-first insurance guidance
- compliance-oriented messaging
- grounded retrieval responses

---

## Evidence

![Claim Support](screenshots/demo/demo_claim_support.png)

---

# 5.3 Scenario 3 — Operational Update Tool Workflow

## User Interaction

```text
My Customer is C1001, please update my phone number 343
```

Expected response:

```text
The phone number "343" you provided is invalid.
Please provide a complete and valid phone number to update.
```

Follow-up:

```text
9988776655
```

Expected response:

```text
Your phone number has been successfully updated to 9988776655.
```

---

## Expected Behaviour

- The policy update agent validates the input.
- Invalid phone numbers are rejected safely.
- The update tool executes only after valid input is provided.
- The final response confirms successful completion.

---

## Why This Matters

This demonstrates:
- tool execution
- multi-turn workflows
- validation handling
- operational assistance
- safe customer updates

---

## Evidence

### Streamlit Workflow

![Phone Update Workflow](screenshots/demo/demo_phone_update.png)

### CLI Logs

![CLI Workflow](screenshots/demo/demo_cli.png)

---

# 5.4 Scenario 4 — Restricted Operation Refusal

## User Query

```text
approve my full claim amount
```

---

## Expected Behaviour

- The safety review layer detects a restricted operation request.
- The assistant refuses safely.
- The response explains operational restrictions.
- The system escalates to authorized representatives.

---

## Expected Response

```text
I'm unable to assist with this request because it involves restricted or unauthorized operations.
Please contact an authorized insurance representative or support specialist for further assistance.
```

---

## Why This Matters

This demonstrates:
- safety guardrails
- restricted operation handling
- refusal behaviour
- escalation handling

---

## Evidence

![Safety Refusal](screenshots/demo/demo_safety_refusal.png)

---

# 5.5 Scenario 5 — Workflow Continuity & Multi-Turn Interaction

## User Interaction

```text
what is my phone number?
```

Expected response:

```text
Please provide your customer ID to proceed.
```

Follow-up:

```text
C1001
```

Expected response:

```text
I'm unable to assist with this request because it involves restricted or unauthorized operations.
Please contact an authorized insurance representative or support specialist for further assistance.
```

Follow-up:

```text
update my email to test@test.com
```

Expected response:

```text
Your email has been updated successfully to test@test.com.
```

---

## Expected Behaviour

- The system maintains workflow continuity across multiple turns.
- Customer verification is enforced.
- Restricted operations are blocked safely.
- Allowed low-risk updates continue successfully.

---

## Why This Matters

This demonstrates:
- conversational workflow continuity
- routing orchestration
- operational boundaries
- multi-turn interaction handling

---

## Evidence

### Workflow Continuity

![Workflow Continuity](screenshots/demo/demo_memory_adaptation.png)

### Reset Workflow Evidence

![Reset Memory](screenshots/demo/reset_memory.png)

---

# 5.6 Scenario 6 — Evaluation Harness Execution

## Run Evaluation Harness

```bash
python app/evaluation/run_evaluation.py
```

---

## Expected Behaviour

The evaluation harness:
- executes evaluation test cases
- measures latency
- performs consistency testing
- validates safety scenarios
- stores evaluation results

---

## Expected Output

- evaluation scores
- average latency
- consistency metrics
- safety validation
- runtime recovery validation

---

## Output File

```text
app/evaluation/evaluation_results.json
```

---

## Why This Matters

This demonstrates:
- automated evaluation engineering
- measurable quality tracking
- repeatable testing
- engineering reliability

---

## Evidence

![Evaluation Runner](screenshots/demo/demo_evaluation_runner.png)

---

# 5.7 Scenario 7 — Retrieval Comparison Evaluation

## Run Retrieval Comparison Harness

```bash
python app/evaluation/run_retrieval_comparison.py
```

---

## Expected Behaviour

The retrieval comparison harness:
- compares LLM-only responses vs RAG-grounded responses
- validates retrieval effectiveness
- tracks retrieval matches
- measures retrieval latency
- validates retrieval coverage

---

## Expected Output

- RAG vs no-RAG comparison
- keyword scores
- retrieval diagnostics
- retrieval match counts
- retrieval availability validation

---

## Output File

```text
app/evaluation/retrieval_comparison_results.json
```

---

## Why This Matters

This demonstrates:
- retrieval-aware evaluation
- grounded response validation
- explainability
- RAG effectiveness analysis

---

## Evidence

![Retrieval Comparison](screenshots/demo/demo_retrieval_comparison.png)

---

# 5.8 Scenario 8 — CLI Workflow Execution

## Run CLI Application

```bash
python app/main.py
```

---

## User Interaction

```text
Update my phone number
```

Follow-up:

```text
C1001
```

Follow-up:

```text
9988776655
```

---

## Expected Behaviour

- CLI workflow executes successfully.
- Logs display:
  - routing
  - agent execution
  - latency
  - safety review
  - tool execution

---

## Why This Matters

This demonstrates:
- explainability
- orchestration visibility
- runtime tracing
- engineering observability

---

## Evidence

![CLI Workflow](screenshots/demo/demo_cli.png)

---

# 5.9 Scenario 9 — Runtime Recovery & Fault Handling

## Injected Runtime Fault

```python
1 / 0
```

---

## User Query

```text
What is deductible
```

---

## Expected Behaviour

- The runtime exception is caught safely.
- The application does not crash.
- A graceful fallback response is returned.
- Runtime errors are logged.

---

## Expected Response

```text
Sorry, something went wrong while processing your request.
Please try again later.
```

---

## Why This Matters

This demonstrates:
- centralized exception handling
- graceful recovery
- runtime resilience
- production-safe fallback behaviour

---

## Evidence

![Runtime Recovery](screenshots/demo/demo_runtime_recovery.png)

---

# 6. Demo Notes

- The same customer profile and seeded policy documents are used across all workflows.
- Policy data is loaded from:

```text
data/customer_profiles/customer_policies.json
```

- Retrieval responses are grounded using:
  - ChromaDB
  - vector embeddings
  - LangChain retrievers

- The evaluation framework supports:
  - consistency testing
  - retrieval-aware scoring
  - runtime failure detection
  - latency tracking