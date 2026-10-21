# Detailed Pointwise Notes: Introduction to AI Governance for AI Agents

## 1. Why Do We Need AI Governance?

Before learning how to implement AI governance, the lecturer establishes why it is necessary in real-world AI systems, particularly AI agents deployed in production environments.

### Key idea

- AI adoption is accelerating across industries.
- Organizations are moving from experimental AI projects and Proofs of Concept (POCs) toward production deployments.
- However, governance, security, and compliance mechanisms are not advancing at the same pace.
- This creates risks when AI agents can access data, call tools, modify databases, or perform actions autonomously.

The lecturer refers to two research reports to support the need for AI governance.

## 2. Research Report 1: Kiteworks

[Kiteworks Launches Data-Layer AI Governance Platform](https://images.openai.com/static-rsc-4/kNzc8dtElIkuAMgbMzocWhlo7RV8sq2JW7CxNtDzmUcO1cJKMA5TCulNVpT1qGLNS33c6B4AY2FL_JxacIpI0uKHcskmOquBine7yCRPEExWa8KVHXVqYKK00cOtpnAhG4yWfIJpLpIxUwxTWSetNorD5aJYLlthmtR1mkzK2mw?purpose=inline)

Research organization: Kiteworks

Topic: AI adoption, data security, governance and compliance

The lecturer refers to page 45 of the Kiteworks research report and highlights a statistic concerning the security and governance of production AI agents.

### Main findings discussed in the lecture

According to the lecturer's presentation of the report, approximately 55–63% of AI agents running in production lack important governance controls.

The controls highlighted include the following:

- Kill switch: The ability to stop an agent when it behaves unexpectedly or performs an unauthorized action.
- Purpose binding: Restricting an agent's access and actions to the specific purpose for which it was authorized.
- Least-privilege access: Ensuring an agent receives only the permissions necessary to perform its assigned task.
- Sandbox isolation: Running agents in isolated environments to limit the consequences of mistakes, malicious inputs, or unexpected behavior.

The statistic is presented as evidence of the gap between AI deployment and adequate governance.

## Four important governance controls

1\. Kill switch

Stop an agent's execution or revoke its ability to take further actions when a critical risk is detected.

2\. Purpose binding

Ensure the agent's actions remain within the authorized business objective.

3\. Least-privilege access

Prevent an agent from accessing more data, systems, or tools than it needs.

4\. Sandbox isolation

Limit the impact of an agent's execution by separating it from sensitive systems and resources.

### Why is this a serious concern?

Imagine an AI agent that can retrieve customer records and update support tickets.

If the agent misinterprets a request, it could modify the wrong customer's record. If it has excessive database permissions, it might access or change information unrelated to its task.

Without an effective kill switch, appropriate access restrictions, and isolation, the consequences can be more serious than an ordinary incorrect chatbot response.

Important takeaway: An AI agent needs more than intelligence. It also needs controlled access, defined boundaries, and mechanisms to stop unsafe actions.

Source note: The 55–63% statistic is reproduced as presented in the lecture transcript. The original Kiteworks report has not been independently checked here.

## 3. Research Report 2: Deloitte — State of AI in the Enterprise

[Deloitte Jobs - 24 offerte di lavoro - talendo](https://images.openai.com/static-rsc-4/qrj-qCTkmMvNGTDO2_qEIAzDUt7011Iyl9Eq6yGbZvRDANY-QrDg9TpTIose84tObmuk0eiogvkreABGzHUZ724FktDD09yED8NXscLd6J7cegIU8D0skYQ1gRIaNMD13QiaRSqM6j-vint7GDiNp3gs7yhFDLhBsHR2mHHJnNs?purpose=inline)

Research organization: Deloitte

Report discussed: State of AI in the Enterprise, January 2026

The second report is used to explain the expected growth of agentic AI adoption.

### The evolution of enterprise AI adoption

The lecturer describes the transition in three broad stages:

1\. 2023–2025: Experimentation and acceptance

- Organizations increasingly accepted generative AI.
- They began exploring agentic AI.
- Many organizations experimented with prototypes and POCs.

2\. 2026: Transition to production

- Organizations are increasingly interested in moving AI agents from experimental projects to production environments.
- Agents are expected to perform actual business tasks rather than merely demonstrate capabilities.

3\. The following two years: Expected expansion

- The lecturer highlights a projected increase in production use of agentic AI.
- This creates a need to establish governance before adoption scales significantly.

### Adoption figures cited in the lecture

The lecturer presents the following figures from the Deloitte report:

## 23%

Current adoption

The share of organizations or production use cases described by the lecturer as using agentic AI at least moderately.

## 74%

Projected adoption

The level of adoption the lecturer says is expected within the next two years.

Interpretation note: These percentages are stated as presented in the lecture. The precise survey denominator, wording of the adoption measure, and forecast assumptions should be checked against the original Deloitte report before citing them in a formal presentation.

### Why does the forecast matter?

The lecturer's central argument is that the scale of the governance problem may increase as organizations deploy more AI agents.

For example:

- More agents will interact with enterprise databases.
- More agents will call external and internal APIs.
- More agents will process confidential information.
- More agents will take actions with business consequences.
- More organizations will need to monitor agent behavior and demonstrate compliance.

If governance is inadequate while adoption accelerates, organizations may expose themselves to security incidents, unauthorized actions, privacy violations, and compliance failures.

Key takeaway: Governance should be built into AI deployments as they move toward production, rather than added only after an incident occurs.

## 4. Scope of AI Governance Covered in This Course

AI governance is a broad subject. The lecturer explicitly narrows the scope of this session to make it practical and relevant to developers building AI agents.

### AI governance can involve multiple areas

- Governance frameworks and standards.
- Security and access control.
- Safety and risk management.
- Ethics and responsible AI.
- Bias identification and fairness.
- Privacy and data protection.
- Regulatory and organizational compliance.
- Runtime monitoring and enforcement.

The lecturer does not intend to cover every aspect of governance in this particular session.

### The selected focus

The session concentrates on:

1. Execution and runtime governance — controlling and observing what an AI agent does while it is running.
2. AI agents — systems that use an LLM, tools, and contextual information to perform tasks.
3. Practical implementation — understanding how governance controls can be integrated into an existing agent.

The lecturer uses the 80/20 principle to describe the teaching approach: focus on the most useful concepts for governing AI agents rather than attempting to cover every theoretical and regulatory topic.

This does not mean that the selected concepts replace the need for comprehensive governance in a real organization. It means the course is prioritizing a practical starting point.

## 5. Demonstration: An AI-Powered Customer Support Agent

The lecturer introduces a working demonstration to show what runtime AI governance looks like in practice.

### 5.1 Purpose of the agent

The demonstration uses a conversational customer support assistant.

Its purpose is to assist human customer support representatives, not necessarily to replace them.

When a support ticket arrives, the agent can help the human representative understand the issue, retrieve relevant information, and prepare a resolution.

### 5.2 Capabilities of the agent

The agent has several capabilities:

- Understand natural-language requests.
- Review customer support tickets.
- Retrieve customer details.
- Access information stored in a SQL database.
- Modify customer support records.
- Add internal notes to tickets.
- Help prepare customer updates.
- Call tools to perform specific operations.

These capabilities make governance important because the agent is not merely generating text. It can interact with business systems and change data.

### 5.3 LLM used in the demonstration

The lecturer identifies the model as:

- Model: Llama 3.3 70B Versatile.
- Role: Provides the language understanding and reasoning capabilities used by the agent.
- Tools: Allow the agent to retrieve information or execute operations.
- Database: Stores customer and ticket information.
- Governance dashboard: Observes and records the agent's execution and policy-related events.

The LLM is the intelligence component, but the complete agent also includes tools, data access, execution logic, and governance mechanisms.

### Conceptual architecture

Human Support Representative

Submits a request or reviews a ticket

Customer Support AI Agent

Interprets the request and coordinates actions

LLM

Llama 3.3 70B Versatile

Tools

Ticket operations and data retrieval

SQL Database

Customer details, tickets, and internal notes

Runtime Governance Dashboard

Execution events, policy violations, context snapshots, tool activity, and token usage

This is a conceptual representation of the architecture described in the lecture, not a verified diagram of the implementation's internal wiring.

## 6. Preset Workflow 1: Approve a Support Update

The lecturer has created predefined prompts to demonstrate common workflows without requiring every request to be typed manually.

### Purpose

The workflow instructs the agent to:

- Review a particular support ticket.
- Add an authorized internal resolution note.
- Record the status of the issue.
- Prepare an update concerning the expected resolution timeline.

### Example used in the demonstration

The lecturer asks the agent to review ticket `11001` and add an internal note indicating:

- Duplicate charges are pending investigation.
- The customer should receive an update within five business days.

### Expected workflow

1. The user selects the preset.
2. The request is entered into the conversational interface.
3. The agent interprets the request.
4. The agent retrieves the relevant ticket information.
5. The agent uses the appropriate tool to add an internal note.
6. The system records the resulting activity.
7. The governance dashboard displays evidence of the execution.

The lecturer demonstrates that the agent returns a response and that the dashboard records the run.

### Why is this workflow useful for learning governance?

It illustrates a legitimate business operation that requires access to customer data.

Governance must allow authorized work to proceed while ensuring that the agent does not exceed its permissions.

For example, the agent should be permitted to update the designated ticket if the request is authorized, but it should not automatically gain permission to modify unrelated customer accounts.

## 7. Understanding the Governance Dashboard

The dashboard is the main demonstration of how runtime governance can be associated with agent execution.

The lecturer refreshes the dashboard and points out several types of information.

### 7.1 Runs and sessions

- A run represents an execution of the agent.
- A session groups interactions or activity associated with a particular conversational context, depending on the implementation.
- The dashboard displays multiple recorded runs and sessions.

These records allow a developer or auditor to examine agent activity rather than relying only on the final answer shown in the chat window.

### 7.2 Events

Events represent individual stages or actions that occur during an agent's execution.

The lecturer shows a sequence containing events such as:

1. Agent registration.
2. Intent declaration.
3. Context snapshot.
4. Subsequent execution and tool-related activity.

The event sequence provides a trace of what happened during a particular run.

Why it matters: If an agent performs an unexpected action, event records can help an investigator identify the steps that preceded it.

### 7.3 Policy violations

The dashboard shows policy-related information, including:

- Which policies were violated.
- Which policies were not violated.
- Which policies were not exercised during a particular run.
- How frequently violations occur.
- Classification information associated with the run.

These distinctions are important.

- Violated: The system detected behavior that breached a configured policy.
- Not violated: The policy was evaluated and no breach was detected.
- Not exercised: The policy may not have been relevant to the actions taken, or its applicable condition was not encountered.

The precise meaning depends on the dashboard's implementation.

A policy that was not exercised should not automatically be interpreted as proof that the agent was safe. The relevant risk may simply not have occurred during that run.

### 7.4 Context snapshots

A context snapshot captures relevant information about the agent's context at a particular point in execution.

Depending on the implementation, this may include items such as:

- The current task or declared intent.
- Relevant conversation state.
- Information provided to the model.
- Execution state or other contextual metadata.

Context snapshots can help investigate why the agent made a particular decision or attempted a particular action.

For example, if the agent tries to retrieve a confidential document, a context snapshot may help an investigator understand what request or contextual information led to that attempt.

The lecturer promises to explain the detailed role of context snapshots later in the course.

### 7.5 Memory attempts

The dashboard also displays memory attempts.

This indicates that the governance system tracks activity related to memory operations. The exact definition, stored information, and policy checks associated with these attempts depend on the implementation.

It is important to distinguish memory activity from ordinary conversational context: an agent may have temporary context for a single run as well as a separate mechanism for storing or retrieving information across interactions.

### 7.6 Token usage

The lecturer highlights token usage as part of the dashboard.

Token usage can provide information about:

- The amount of model input processed.
- The amount of model output generated.
- The computational consumption associated with a run.
- Potential cost or efficiency issues.

The dashboard also connects token information to tool-related activity, which the lecturer calls tool-bound observability.

This can help answer questions such as which execution consumed resources and what operations were performed during that execution.

However, token monitoring by itself does not establish whether an agent's actions were authorized or safe.

### 7.7 Tool-bound observability

The dashboard includes an action named `update support ticket`.

The lecturer points out that the system can associate activity and token usage with particular tool operations.

This is more informative than simply recording the final model response because it helps connect agent execution to concrete actions.

For example, the system can potentially distinguish between:

- A model answering a question without calling a tool.
- A model retrieving customer information.
- A model attempting to modify a ticket.
- A model executing a tool operation that violates a policy.

The precise level of detail depends on which events and tool metadata the implementation captures.

### Summary of dashboard components

| Dashboard component | Purpose                                        |
| ------------------- | ---------------------------------------------- |
| Runs                | Records agent executions                       |
| Sessions            | Groups related conversational activity         |
| Events              | Captures the sequence of execution events      |
| Policy violations   | Identifies detected policy breaches            |
| Context snapshots   | Preserves relevant execution context           |
| Memory attempts     | Tracks memory-related activity                 |
| Token usage         | Measures model consumption                     |
| Tool activity       | Connects execution to specific tool operations |

## 8. Preset Workflow 2: Send a Confidential Plan Personally

The lecturer then demonstrates a negative use case to show what happens when an agent is asked to perform a potentially unauthorized action.

### The request

The preset instructs the agent to:

1. Read a confidential plan.
2. Prepare a concise summary.
3. Email the summary to a specified email address.
4. Make the information available outside the organization's context.

This request is intentionally different from the authorized support-ticket workflow.

The central issue is not whether summarization or email generation is technically possible. It is whether the agent should be permitted to disclose confidential information to the requested recipient.

### What happens during the demonstration?

1. The lecturer selects the confidential-plan preset.
2. The request is entered into the agent.
3. The agent processes the request.
4. The lecturer demonstrates a response associated with the request.
5. The governance dashboard is refreshed.
6. The dashboard shows the new execution and policy-related information.
7. The lecturer inspects which policies were violated and the relevant execution flow.

The lecturer describes this as a negative use case because the requested action raises a confidentiality and authorization concern.

Important distinction: The transcript establishes that the dashboard records policy-related evidence for this request. It does not independently establish that an email was actually sent, that the confidential information was successfully exfiltrated, or that the policy system blocked the action.

Those outcomes would need to be verified in the application's actual execution records.

### Why is this example important?

An LLM can understand a request and generate an apparently appropriate response while the requested operation itself remains unsafe.

A governance system must therefore consider more than the linguistic quality of the answer.

It needs to examine questions such as:

- Is the requested document confidential?
- Is the requester authorized to access it?
- Is the recipient permitted to receive it?
- Is external disclosure allowed?
- Is the requested action consistent with the agent's declared purpose?
- Should the tool call be permitted, denied, or escalated for human approval?

This illustrates why runtime governance must account for the actions an agent attempts, not just the text it produces.

## 9. Observation-Only Governance vs. Active Enforcement

One of the most important distinctions in the lecture is that the demonstrated dashboard is currently operating in an observation-only mode.

### Observation-only mode

In this mode, the system primarily records and reports what the agent does.

It can provide evidence of:

- Agent execution.
- Tool calls and attempted actions.
- Context and event sequences.
- Token consumption.
- Detected policy violations.

The system helps developers understand what went wrong, but observing a violation does not necessarily stop it.

### Active enforcement mode

An actively enforcing governance system can intervene when a policy is violated.

Depending on its design, it may:

- Deny an unauthorized tool call.
- Block access to a confidential document.
- Prevent an external email from being sent.
- Require human approval before a sensitive action.
- Revoke an agent's permissions.
- Stop an agent's execution through a kill switch.

### Comparison

| Feature                        | Observation-only | Active enforcement                             |
| ------------------------------ | ---------------- | ---------------------------------------------- |
| Records agent activity         | Yes              | Yes, typically                                 |
| Reports policy violations      | Yes              | Yes, typically                                 |
| Helps investigate incidents    | Yes              | Yes                                            |
| Prevents unauthorized actions  | Not necessarily  | Yes, when the control is correctly implemented |
| Stops execution automatically  | Not necessarily  | Possible, if configured                        |
| Provides evidence for auditing | Yes              | Yes                                            |

A system can combine both approaches. In fact, monitoring and enforcement complement one another: monitoring provides visibility, while enforcement helps prevent unacceptable actions.

Critical lesson: A dashboard that reports a policy violation is not automatically a security control that prevents that violation.

## 10. Is AI Governance Related to Ethics?

The lecturer explains that ethics is one component of AI governance, but AI governance is broader than ethics alone.

### Major components mentioned

1\. Ethics

- Responsible use of AI.
- Consideration of the consequences of AI-driven decisions.
- Avoidance of inappropriate or harmful uses.

2\. Safety

- Preventing harmful or unintended behavior.
- Restricting dangerous operations.
- Providing mechanisms to stop unsafe execution.

3\. Bias identification

- Detecting potentially unfair or biased model outputs or decisions.
- Evaluating whether AI systems behave appropriately across relevant groups and scenarios.

4\. Security and access control

- Protecting sensitive data.
- Restricting tool permissions.
- Preventing unauthorized operations and information disclosure.

5\. Runtime observability

- Recording the agent's execution.
- Connecting tool calls to their context.
- Detecting and investigating policy violations.

6\. Compliance and accountability

- Producing evidence that helps demonstrate whether the system followed organizational policies.
- Supporting audits and investigations.
- Making it easier to understand which actions occurred and why.

### Why does the lecturer emphasize observability?

The lecturer argues that runtime governance needs an observability layer that is explicitly aligned with governance requirements.

Ordinary monitoring might tell a developer that a service failed or a model consumed too many tokens. Governance-oriented observability should also help explain whether an agent's behavior was authorized and compliant with the applicable policies.

For example:

- Ordinary observability: The agent called `update_support_ticket`.
- Governance-oriented observability: The agent called `update_support_ticket`, the request was associated with a declared purpose, and the operation was evaluated against the relevant authorization policy.

The second provides information that is more useful for governance, although the quality of the evidence depends on the implementation.

### Important limitation

Observability alone cannot fully implement AI governance. It does not automatically guarantee fairness, privacy, security, or compliance. These outcomes also require appropriate policies, evaluations, access controls, enforcement mechanisms, and organizational processes.

## 11. AI Governance vs. Guardrails vs. AI Security vs. Observability

The lecturer introduces several questions that will be discussed more explicitly later in the course. The following distinctions provide a useful preliminary understanding.

| Concept             | Main question it addresses                                                            | Example                                                     |
| ------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| AI governance       | What rules, responsibilities, and controls should govern AI behavior?                 | Defining who can approve an agent's access to customer data |
| Guardrails          | How can specified inputs, outputs, or actions be constrained?                         | Preventing a model from generating a prohibited response    |
| AI security         | How do we protect the AI system, its data, tools, and infrastructure against threats? | Preventing unauthorized access to a customer database       |
| Observability       | What happened during execution, and how can we investigate it?                        | Recording tool calls, errors, and token usage               |
| Runtime enforcement | How can a prohibited action be prevented or stopped while the agent is running?       | Denying an unauthorized email-sending tool call             |

These concepts overlap but are not interchangeable.

For instance, a guardrail can be part of a governance implementation, and an access-control mechanism can enforce a governance policy. Observability can provide the evidence needed to assess whether those controls worked.

A practical governance implementation usually needs several of these capabilities working together.

## 12. The Importance of the Runtime Boundary

The lecturer repeatedly describes the agent as being governed at the runtime boundary.

In this context, the runtime boundary is the point at which an executing agent interacts with its tools, data, and external systems.

Consider a customer support agent that can:

- Read a support ticket.
- Retrieve customer information.
- Add internal notes.
- Send emails.
- Modify customer records.

The governance system should not blindly trust every action merely because the LLM requested it.

Instead, it should evaluate relevant operations against the applicable rules.

For example:

Authorized action

The agent reads a ticket it is permitted to access and adds an approved internal note.

Expected outcome: Allow the operation and record appropriate evidence.

Unauthorized action

The agent attempts to send confidential customer information to an unapproved external recipient.

Expected outcome: Deny or hold the action, record the event, and escalate if required.

The exact enforcement point depends on the architecture. Ideally, sensitive operations are checked at a trusted tool or service boundary rather than relying solely on the model to follow instructions.

This is particularly important because an LLM may misinterpret a request, respond to prompt injection, or select an inappropriate tool.

## 13. How the Dashboard Connects to Governance Frameworks

The lecturer states that the dashboard's observability data is organized so it can be related to AI governance frameworks.

The idea is to connect operational evidence to governance requirements.

For example:

| Operational evidence     | Potential governance use                                       |
| ------------------------ | -------------------------------------------------------------- |
| Tool-call records        | Investigate whether an agent performed an authorized operation |
| Policy-violation records | Identify where configured rules were breached                  |
| Context snapshots        | Reconstruct relevant circumstances surrounding an action       |
| Execution events         | Trace the sequence of operations                               |
| Token usage              | Monitor resource consumption and investigate anomalies         |
| Session records          | Review activity within a conversational interaction            |

A governance framework may specify what an organization needs to control, document, evaluate, or audit. Runtime evidence can help demonstrate how those requirements are implemented in a particular AI application.

However, merely collecting these records does not prove that an organization complies with a framework. The records must be accurate, sufficiently complete, protected against tampering where necessary, and mapped to the actual requirements.

The lecturer plans to explain this relationship in more detail later.

## 14. GitHub Repository and Hands-On Exploration

The lecturer invites viewers to explore the demonstration through their GitHub profile and the associated repository.

The repository is intended to let learners investigate the implementation and experiment with the governance dashboard.

The transcript does not include an actual repository URL, so the precise repository cannot be identified from the provided text alone.

The lecturer also makes clear that learners do not need to understand every dashboard field immediately. The concepts will be revisited after the underlying governance philosophy is explained.

## 15. Key Questions the Remaining Course Will Address

The lecturer explicitly identifies several topics for later explanation.

- What is the meaning of each policy shown in the dashboard?
- What are context snapshots, and why are they necessary?
- What are memory attempts?
- How does the dashboard trace agent execution?
- How is AI governance different from ordinary observability?
- How is AI governance different from guardrails?
- How does AI governance relate to AI security?
- Which concepts overlap between governance and security?
- How can governance be implemented for AI agents in practice?
- How can runtime evidence be connected to governance frameworks?

These questions form the bridge between the initial demonstration and the detailed implementation lessons that follow.

## 16. Complete End-to-End Summary of the Lecture

The lecture follows a clear progression:

## 1

Establish the need

AI adoption is increasing, but the lecturer argues that governance controls are lagging behind.

## 2

Present industry research

Kiteworks is cited for gaps in agent controls, while Deloitte is cited for expected growth in agentic AI adoption.

## 3

Narrow the scope

Focus on runtime governance and AI agents rather than attempting to cover every governance framework and standard.

## 4

Demonstrate a real-world agent

Use a customer support agent with an LLM, SQL database, and tools that retrieve and modify ticket information.

## 5

Examine normal and risky workflows

Compare an authorized support-ticket update with a request to disclose a confidential plan externally.

## 6

Inspect governance evidence

Explore runs, events, policy violations, context snapshots, memory attempts, token usage, and tool activity.

## 7

Understand the limitation

The demonstrated system is initially observation-only, so recording a violation does not necessarily prevent the action.

## 8

Prepare for deeper concepts

The next lessons will explain policies, guardrails, AI security, observability, and the practical philosophy behind runtime governance.

## 17. Important Takeaways to Remember

1\. An AI agent is more than an LLM. It may have access to tools, databases, APIs, and the ability to modify real business data.

2\. Production deployment increases the importance of governance. An incorrect answer is one type of failure; an unauthorized tool action can have direct operational consequences.

3\. Least privilege is essential. Agents should receive only the access necessary to perform their authorized tasks.

4\. Purpose binding limits scope. The agent should not use its capabilities for unrelated or unauthorized objectives.

5\. Kill switches and isolation reduce risk. They provide additional protection when an agent behaves unexpectedly.

6\. Governance-oriented observability records more than final responses. It connects execution events, tool calls, contextual information, and policy evaluations.

7\. Normal and negative use cases should both be tested. A system must be evaluated not only on whether it completes legitimate requests but also on how it handles unsafe ones.

8\. Observation and prevention are different. A dashboard that detects and reports a violation does not necessarily stop it.

9\. AI governance is broader than ethics or guardrails. It includes policies, security, safety, accountability, compliance, monitoring, and enforcement.

10\. Runtime governance must be connected to actual controls. Logging is useful, but sensitive operations also need reliable authorization checks and enforcement at appropriate boundaries.

11\. Governance evidence supports audits but does not automatically prove compliance. The evidence must be mapped to real requirements and supported by effective controls.

12\. The objective of the course is practical implementation. The lecturer intends to focus on the runtime concepts most useful for governing AI agents.

### Final conceptual distinction

Remember this simple sequence:

AI agent → performs actions → governance policies define what is allowed → runtime controls evaluate those actions → observability records the evidence → enforcement prevents or stops prohibited operations where configured.

That is the central idea behind this introductory lecture: build AI agents that are not only capable of performing tasks, but also observable, accountable, and appropriately constrained.