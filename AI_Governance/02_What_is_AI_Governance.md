# Detailed Pointwise Notes: AI Governance vs. AI Security

Lecture 2 — AI Governance Fundamentals, Runtime Security, Evaluations, Guardrails, Red Teaming, and Observability

These notes follow the lecture's original flow, including the car-manufacturing analogy, the distinction between governance and security, the shared implementation components, the frameworks mentioned, and the practical responsibilities of developers and compliance teams.

## 1. The Main Objective of This Lecture

The lecturer wants to explain how developers and technical leads should approach AI governance without feeling that they must study every framework, risk category, regulation, and standard in exhaustive detail.

### The problem

- AI governance is a broad subject.
- There are numerous frameworks, regulations, standards, and risks to understand.
- Studying every framework in depth can be overwhelming for a developer or technical lead.
- Developers need to identify which concepts are essential for building and deploying AI agents responsibly.

### The proposed solution

The lecturer divides AI governance into two broad parts:

## 1. Technical Governance and Security

- Runtime controls and implementation.
- Agent security and access control.
- Observability, evaluations, and guardrails.
- Testing, threat mitigation, and incident response.

  Primary area of focus for developers and technical teams.

## 2. Strategic and Policy Governance

- Organizational policies.
- Applicable laws, standards, and regulatory requirements.
- Decisions about acceptable risks and required controls.
- Compliance requirements and organizational processes.

  Primarily concerned with defining what must be achieved and why.

## Trustworthy AI

The combination of appropriate policies, technical safeguards, and effective implementation.

Important distinction: This two-part division is the lecturer's teaching model. In real organizations, governance and security responsibilities often overlap, and technical teams also contribute to governance decisions.

### What should developers prioritize?

According to the lecturer:

- Understand the strategic and policy side sufficiently to know what is required.
- Become familiar with relevant governance frameworks and resources.
- Spend most implementation effort on the technical controls needed to satisfy those requirements.
- Build systems that can demonstrate and enforce appropriate behavior.

The lecturer's earlier governance dashboard is presented as a starting point for implementing the technical side.

## 2. Definition of AI Governance

The lecturer gives the following definition:

> AI governance is the framework of policies, processes, and controls that ensures AI systems are developed and operate responsibly, safely, securely, ethically, and in compliance with applicable laws and organizational standards.

The definition contains several important elements.

### 2.1 Policies

Policies establish the rules an AI system must follow.

Examples include:

- Which data an agent may access.
- Which actions an agent may perform.
- When human approval is required.
- Which information may be shared externally.
- What types of AI behavior are prohibited.

### 2.2 Processes

Processes describe how an organization applies and maintains those rules throughout the AI system's lifecycle.

Examples include:

- Reviewing an AI use case before deployment.
- Approving access to sensitive data.
- Testing an agent before production release.
- Investigating incidents.
- Reviewing and updating controls when requirements change.

### 2.3 Controls

Controls are mechanisms that help implement or verify the policies.

Examples include:

- Access-control systems.
- Input and output guardrails.
- Runtime authorization checks.
- Evaluations.
- Observability and logging.
- Red teaming and incident-response mechanisms.

### 2.4 Responsible, safe, secure, and ethical operation

These terms describe different objectives:

- Responsible: The system is developed and used with appropriate accountability.
- Safe: The system's behavior and potential consequences are controlled to an acceptable level.
- Secure: The system and its data, tools, and infrastructure are protected against threats.
- Ethical: The system is designed and used in accordance with relevant ethical principles.
- Compliant: The system satisfies applicable legal and organizational requirements.

### 2.5 Who does what?

The lecturer distinguishes the responsibilities of strategic stakeholders and implementation teams.

| Strategic or policy responsibilities   | Technical implementation responsibilities             |
| -------------------------------------- | ----------------------------------------------------- |
| Define required policies               | Implement controls that enforce policies              |
| Identify applicable regulations        | Translate requirements into technical checks          |
| Establish organizational processes     | Integrate guardrails, access controls, and monitoring |
| Define compliance expectations         | Collect evidence and report violations                |
| Determine acceptable risk requirements | Test the system and fix technical weaknesses          |

This is a division of emphasis, not a strict separation. Developers must understand the policies relevant to their systems, and compliance teams need technical input to define realistic requirements.

## 3. AI Governance vs. AI Security: Why the Confusion Exists

The lecturer raises a common question: are guardrails, observability, and gateways part of AI governance, AI security, or both?

The answer is that the concepts overlap.

- Some capabilities primarily support governance.
- Some primarily protect the system against security threats.
- Some serve both purposes.

The lecturer uses a Venn diagram to illustrate the relationship: governance and security have distinct responsibilities, but they share several important controls.

### The central principle

AI governance determines what requirements and rules should apply; AI security helps protect the system and enforce appropriate boundaries.

For example, an organization might establish a policy that confidential customer information must not be disclosed to unauthorized recipients. Security controls can then restrict access, validate recipient permissions, and block unauthorized transfers.

In this example:

- The confidentiality requirement is a governance concern.
- The mechanisms that protect the data are security controls.
- The evidence showing whether the system followed the rule supports both governance and security.

## 4. The Car-Manufacturing Analogy

The lecturer uses a multinational car manufacturer to explain the difference between governance and security.

Imagine a company manufacturing cars and selling them in India, Europe, China, and the United States.

The company must satisfy the requirements of the markets in which it operates. At the same time, it needs to build security and safety features into its vehicles.

This analogy maps to AI agents as follows:

| Car manufacturing                   | AI development                                          |
| ----------------------------------- | ------------------------------------------------------- |
| Car                                 | AI agent                                                |
| Country's vehicle regulations       | Applicable AI laws and organizational requirements      |
| Car manufacturer's engineering team | AI developers and technical teams                       |
| Speedometer                         | Observability                                           |
| Driving licence requirements        | Governance policies and authorization requirements      |
| Car lock and alarm                  | Security controls                                       |
| Vehicle safety testing              | AI evaluations                                          |
| Automatic emergency braking and ABS | Guardrails and preventive controls                      |
| Testing a vehicle against attacks   | AI red teaming                                          |
| Roadworthiness and market approval  | Meeting relevant production and compliance requirements |

The analogy is used to show that compliance requirements, technical controls, and measurement capabilities work together.

## 5. Governance Requirements Differ Across Regions

### 5.1 Different regions have different requirements

The lecturer mentions the United States, India, China, and the European Union as examples of regions that may have different rules.

A multinational organization must identify the requirements applicable to the jurisdictions in which its products operate.

The same principle applies to AI agents.

Depending on the applicable laws and use case, requirements may differ regarding:

- Data protection and privacy.
- Transparency.
- Risk assessment.
- Human oversight.
- Documentation and auditability.
- Security measures.
- Acceptable uses of AI.

### 5.2 The airbag example

The lecturer compares hypothetical or simplified vehicle configurations in different markets.

For example, a car might be sold with two airbags in one market and require six in another, according to the lecture's illustration.

The intended lesson is that the same product may require different configurations to meet different market requirements.

The precise airbag requirements depend on the actual jurisdiction and vehicle category; the numbers in this lecture are illustrative rather than a verified statement of current law.

### 5.3 Applying the lesson to AI agents

An AI agent may need different controls depending on:

- Where it is deployed.
- Which customers use it.
- What personal or confidential information it processes.
- What business decisions it influences.
- Which laws and organizational policies apply.

For example, a customer support agent handling personal data may require stricter access, retention, disclosure, and audit controls than an agent that only summarizes public documents.

Key takeaway: Governance requirements should be identified from the actual deployment context, rather than assuming one configuration is automatically appropriate everywhere.

## 6. Observability: The Speedometer of an AI Agent

The lecturer identifies observability as one of the fundamental components of runtime governance.

### 6.1 Understanding the speedometer analogy

A speedometer allows a driver to measure how fast a car is moving.

If a road has a speed limit, the driver needs to know the car's speed to determine whether the limit is being exceeded.

Without a speedometer, the driver cannot reliably monitor speed.

The lecturer applies the same idea to AI agents:

- A car's speedometer measures speed.
- An AI agent's observability system records and exposes relevant execution information.
- Governance requirements define what behavior is acceptable.
- Observability helps determine whether the agent's behavior is consistent with those requirements.

### 6.2 Why is observability essential?

Without observability, developers may struggle to determine:

- What an agent actually did.
- Which tools it called.
- What happened during a particular execution.
- Where a failure occurred.
- Whether a configured policy was violated.
- What information was associated with an unexpected action.

Observability provides evidence that can be used to monitor and investigate agent behavior.

### 6.3 An important qualification

The lecturer emphasizes that observability is a fundamental requirement for implementing governance effectively. However, observability alone does not guarantee compliance or prevent violations.

A system may log an unauthorized operation without blocking it. Therefore, observability should be combined with the appropriate access controls, policy checks, evaluations, and enforcement mechanisms.

Remember: Observability is the measurement and evidence layer. It helps you understand what happened, but additional controls may be needed to determine what is allowed and prevent prohibited actions.

## 7. Governance-Only Requirements: The Driving Licence Analogy

The lecturer next explains requirements that primarily belong to the governance side.

### 7.1 Driving licence example

A government establishes the requirement that a person must have a valid driving licence to drive legally.

The government also determines the relevant eligibility criteria and rules for issuing licences.

The car manufacturer does not independently decide whether a person is legally qualified to drive.

The analogy is:

- The government establishes the legal requirement.
- The relevant authority defines the licensing rules.
- The driver must meet those requirements.
- The car manufacturer builds the vehicle and its security features.

### 7.2 Applying this to AI agents

An organization or regulator may define requirements such as:

- Which uses of AI are permitted.
- Which uses require additional oversight.
- What information must be protected.
- Which actions require human approval.
- What documentation or assessments must be completed before deployment.

These requirements cannot be determined solely by a developer's personal preference.

Technical teams must understand the applicable requirements and implement the controls needed to satisfy them.

### 7.3 What the lecturer wants developers to understand

The lecturer does not expect every developer to become an expert in every regulation.

Instead, developers should understand:

1. Which requirements apply to their application.
2. What those requirements mean in practical terms.
3. Which technical controls are necessary.
4. How to test those controls.
5. How to produce evidence that they operate as intended.

The compliance or governance team may coordinate the interpretation of regulations and organizational policies, while technical teams implement and validate the relevant system behavior.

## 8. Security-Only Requirements: The Car Lock and Alarm Analogy

The lecturer distinguishes legal requirements from security mechanisms implemented by the manufacturer.

### 8.1 Car security example

Different cars may have different security features:

- Key-based unlocking.
- Electronic or remote unlocking.
- Alarm systems.
- Other access-control mechanisms.

These features help prevent unauthorized people from accessing or operating the vehicle.

A fundamental principle remains: an arbitrary person should not be able to start or use the car without appropriate authorization.

### 8.2 Applying this to AI agents

Security mechanisms protect the agent, its data, its tools, and the infrastructure it uses.

Examples include:

- Authentication and authorization.
- API gateway controls.
- Tool access restrictions.
- Secure handling of credentials.
- Model-weight protection.
- Secure computing environments.
- Protection against prompt injection and data poisoning.
- Rate limiting.

The exact controls depend on the application, its threats, and the resources it accesses.

### 8.3 Why security is not identical to governance

Governance may require that only authorized people or systems access particular information.

Security implements mechanisms that help enforce that requirement.

For example:

- Governance requirement: Only authorized support staff may access confidential customer records.
- Security implementation: Authenticate the user, verify permissions, and deny unauthorized database requests.

The requirement and its technical implementation are related, but they serve different purposes.

## 9. The Three Categories: Governance, Security, and Shared Controls

The lecturer's car analogy can now be summarized in three categories.

## A. Primarily governance

- Policies and organizational rules.
- Applicable regulations and standards.
- Compliance requirements.
- Decisions about acceptable use and required oversight.
- Risk-management and documentation requirements.

## B. Primarily security

- Gateways and access controls.
- Model-weight security.
- Secure compute environments.
- Threat mitigation.
- Protection against prompt injection and data poisoning.
- Rate limiting and infrastructure security.

## C. Shared governance and security controls

- Observability.
- Evaluations.
- Guardrails.
- Red teaming.
- Incident response.

These categories reflect the lecturer's conceptual diagram. The boundaries are not absolute: for example, access controls can be a security mechanism that directly enforces a governance policy.

The shared category is especially important because these controls can improve both the technical security of the agent and its ability to meet governance requirements.

## 10. Evaluations: Testing Whether an AI Agent Meets Requirements

The first shared control discussed in detail is AI evaluation.

### 10.1 The car safety-rating analogy

The lecturer refers to vehicle safety ratings, using ANCAP as an example.

A vehicle may receive a safety rating such as two, four, or five stars.

Imagine a hypothetical country that refuses to approve vehicles with a safety rating below three stars.

In that situation:

- A vehicle with a sufficient rating could meet that particular threshold.
- A vehicle below the threshold would fail the requirement.
- The vehicle's commercial usefulness would not override the minimum requirement.

The example demonstrates how evaluation results can influence whether a product is accepted for deployment.

### 10.2 Applying the analogy to AI agents

An AI agent can be evaluated on several dimensions, depending on its purpose.

Examples include:

- Answer correctness.
- Hallucination rate.
- Retrieval quality.
- Tool-use accuracy.
- Compliance with required policies.
- Resistance to adversarial inputs.
- Reliability across different scenarios.

The evaluation should measure the behaviors relevant to the intended application.

### 10.3 The hallucination example

The lecturer provides a hypothetical example involving an AI agent that must meet a specified accuracy threshold.

The scenario is:

- An imagined requirement allows a maximum hallucination rate of 25%.
- The agent is tested.
- The evaluation shows 60% acceptable results and 40% hallucinations.
- The agent fails to meet the assumed threshold.

The intended lesson is that the agent should not be deployed merely because its use case is valuable. It must also satisfy the relevant acceptance criteria.

Important: The lecturer's 75% accuracy requirement and 25% hallucination allowance are hypothetical examples, not verified requirements of the EU AI Act.

### 10.4 Why evaluations support both governance and security

Evaluations help establish whether an agent meets predefined requirements.

From a governance perspective, they can provide evidence that required performance or safety criteria have been met.

From a security perspective, they can test whether the agent handles malicious, adversarial, or unauthorized requests appropriately.

For example, an evaluation suite might check whether an agent correctly answers normal questions and refuses to disclose confidential customer information to an unauthorized requester.

### 10.5 Practical evaluation workflow

A practical implementation can follow this sequence:

1. Identify the agent's intended purpose.
2. Define measurable acceptance criteria.
3. Create representative test cases.
4. Run the agent against the test cases.
5. Measure its performance.
6. Investigate failures.
7. Improve the implementation.
8. Repeat the tests.
9. Compare the results against the required release thresholds.
10. Retain the results as evidence for review.

The exact criteria should be selected according to the application and its applicable requirements.

## 11. Guardrails: Preventive and Restrictive Controls

The next shared component is guardrails.

### 11.1 The vehicle safety analogy

The lecturer compares AI guardrails with vehicle safety features, including:

- Anti-lock braking systems (ABS).
- Advanced Driver Assistance Systems (ADAS).
- Lane-related assistance.
- Emergency braking systems.

These features can help prevent accidents or reduce the impact of dangerous situations.

The lecturer also points out that some safety features may be mandatory in particular markets.

A vehicle lacking a required feature may fail to satisfy the applicable market requirements.

### 11.2 Applying this to AI agents

Guardrails constrain inputs, outputs, or actions to reduce the risk of unwanted behavior.

The lecturer specifically mentions:

PII-related guardrails

PII means personally identifiable information. These controls can help detect or prevent inappropriate disclosure of personal information.

Toxicity checkers

These can identify potentially toxic or abusive content according to the criteria used by the implementation.

Bias checkers

These can help identify potential bias or unfairness in outputs or decisions.

Other guardrails may enforce content restrictions, validate structured outputs, or restrict certain tool operations.

### 11.3 Why guardrails matter for production deployment

The lecturer's argument is that an AI agent may be prevented from entering production if it lacks required safeguards.

For example, an application handling sensitive personal information may need controls that reduce the risk of exposing that information.

Similarly, an application that generates user-facing content may require appropriate checks for prohibited content or other specified risks.

However, no single guardrail is sufficient for every use case. Requirements should be derived from the application's actual risk profile and applicable policies.

### 11.4 Guardrails are not the same as a complete governance system

Guardrails can enforce individual restrictions, but they do not necessarily cover every governance concern.

A guardrail may help prevent a model from disclosing personal information, but it does not by itself establish:

- Who approved the application.
- Which regulations apply.
- Whether the agent's permissions are appropriate.
- Whether its performance meets release criteria.
- Whether incidents are documented and investigated.

Therefore, guardrails should be considered one component of a broader governance and security implementation.

## 12. Red Teaming: Deliberately Trying to Break the System

The lecturer next discusses red teaming, using the example of professionals hired to find ways to break into a car.

### 12.1 The car analogy

Imagine that a manufacturer has developed a vehicle and wants to identify weaknesses before selling it.

The manufacturer engages a team of specialists to attempt to defeat its security mechanisms.

The team discovers weaknesses and reports them.

The manufacturer can then:

1. Understand the attack.
2. Identify the underlying weakness.
3. Fix the problem or introduce a suitable mitigation.
4. Retest the vehicle.

The purpose is to find weaknesses before attackers exploit them in the real world.

### 12.2 Connection to ethical hacking

The lecturer compares this approach with ethical hacking.

In ethical hacking, an organization authorizes security professionals to test a system within an agreed scope.

The testers attempt to discover vulnerabilities and report their findings so the organization can address them.

### 12.3 Red teaming for AI agents

AI red teaming applies a similar principle to AI systems.

A red team may test whether an agent can be manipulated into:

- Revealing confidential information.
- Ignoring its intended restrictions.
- Following malicious instructions.
- Misusing tools.
- Accessing unauthorized data.
- Producing harmful or otherwise prohibited outputs.

The exact tests depend on the agent's architecture, intended use, and threat model.

### 12.4 Why red teaming supports governance

Suppose an organization has a policy requiring its AI agent to protect confidential information.

A policy document alone does not establish that the agent will actually protect that information under adversarial conditions.

Red teaming can test whether the implemented controls withstand realistic attempts to bypass them.

The resulting report can provide evidence of:

- What was tested.
- Which weaknesses were discovered.
- Which risks remain.
- Which mitigations were introduced.
- Whether the weaknesses were retested.

If a specific applicable requirement mandates red-team testing or a related assessment, the organization must satisfy that requirement. The lecture does not establish that every AI system is subject to the same universal red-teaming obligation.

### 12.5 A practical red-teaming workflow

1. Define the system and the scope of testing.
2. Identify relevant threats.
3. Create adversarial scenarios.
4. Execute the tests in an authorized environment.
5. Record failures and their impact.
6. Prioritize the findings.
7. Implement mitigations.
8. Retest the system.
9. Document the results.

Key takeaway: Evaluations measure performance against defined criteria, while red teaming deliberately probes weaknesses and attempts to bypass the system's defenses. They can complement one another.

## 13. Incident Response

The lecturer identifies incident response as another component that bridges governance and security.

Incident response concerns how an organization handles an event in which something goes wrong.

Examples involving AI agents might include:

- An agent discloses confidential information.
- An unauthorized tool operation occurs.
- An agent is manipulated by a prompt-injection attack.
- A security control fails.
- The system behaves in a way that violates an organizational policy.

A practical incident-response process may include:

1. Detecting and recording the incident.
2. Assessing its severity and scope.
3. Containing the issue.
4. Stopping or restricting affected agent operations where appropriate.
5. Investigating the root cause.
6. Remediating the weakness.
7. Retesting the system.
8. Documenting the outcome.
9. Updating controls and procedures to reduce recurrence.

Incident response is a shared concern because it involves both operational security and organizational responsibilities, including escalation, reporting, accountability, and remediation.

## 14. Frameworks and Standards Mentioned in the Lecture

The lecturer names several governance frameworks and security-related resources.

It is important to distinguish a framework or standard from a technical implementation library.

### 14.1 Governance frameworks and standards

| Framework or standard             | How it is positioned in the lecture                            |
| --------------------------------- | -------------------------------------------------------------- |
| ISO/IEC 42001                     | AI management system standard                                  |
| NIST                              | Frameworks and guidance for risk management and trustworthy AI |
| EU AI Act                         | European Union legislation concerning AI                       |
| OWASP Top 10 for LLM Applications | Guidance on important security risks in LLM-based applications |

The lecturer groups these resources primarily under governance because they help define risks, requirements, and practices that organizations should consider.

A technical team can use them to understand what a system needs to address.

However, they are not interchangeable: ISO/IEC 42001 is a management-system standard, the EU AI Act is legislation, NIST provides frameworks and guidance, and OWASP provides security-oriented guidance.

### 14.2 Security mechanisms mentioned

The lecturer identifies the following as primarily security-related capabilities:

- Gateways.
- Access controls.
- Model-weight security.
- Secure compute environments.
- Threat mitigation for data poisoning.
- Threat mitigation for prompt injection.

These mechanisms protect the system and help prevent unauthorized access or manipulation.

### 14.3 Shared capabilities

The lecturer places the following in the overlap between governance and security:

- Evaluations.
- Guardrails.
- Red teaming.
- Incident response.
- Observability.

They support technical protection while also helping demonstrate that relevant requirements are being tested, monitored, and addressed.

## 15. The Complete Relationship Between Governance and Security

The lecture's model can be summarized as follows.

### Governance requirements

Policies, applicable laws, organizational standards, risk requirements, and expectations for responsible AI.

### Shared implementation and assurance layer

Observability, evaluations, guardrails, red teaming, and incident response.

### Security and runtime implementation

Access control, gateways, secure infrastructure, threat mitigation, rate limits, and other technical protections.

### Better-governed AI deployment

Evidence, enforcement, and technical safeguards work together to support trustworthy AI.

This is a conceptual relationship rather than a mandatory sequence. In practice, governance requirements, security architecture, testing, and monitoring are developed iteratively.

### What does trustworthy AI mean in this lecture?

The lecturer uses trustworthy AI as the outcome of combining governance and technical safeguards.

The goal is to build an AI agent that is:

- Appropriately controlled.
- Secure against relevant threats.
- Evaluated against its intended requirements.
- Monitored during execution.
- Tested for weaknesses.
- Supported by appropriate incident-response procedures.
- Suitable for deployment to real users when the applicable requirements are satisfied.

The lecturer describes the outcome as safer, more secure, more robust, and less harmful.

These controls reduce risk; they do not guarantee that an AI system is completely safe or incapable of failure.

## 16. What Should Developers Focus On?

The lecturer clarifies that developers and solution architects do not need to personally define every organizational policy or interpret every regulation from scratch.

However, they do need to implement the technical foundations that make those requirements actionable.

### Responsibilities of compliance and strategic teams

Depending on the organization, these may include:

- Identifying applicable requirements.
- Establishing organizational policies.
- Defining risk acceptance criteria.
- Coordinating compliance assessments.
- Establishing documentation and review processes.

### Responsibilities of developers and technical teams

These include:

- Implementing security controls.
- Applying access restrictions.
- Integrating appropriate guardrails.
- Building evaluation suites.
- Instrumenting the agent for observability.
- Conducting or supporting red-team testing.
- Maintaining secure execution environments.
- Implementing rate limits and other operational protections.
- Responding to technical findings and remediating weaknesses.

### Shared responsibilities

Some tasks require both teams to collaborate.

For example, the compliance team may specify that confidential information must not be disclosed to unauthorized recipients. Developers must implement and test the controls that enforce this rule.

The two teams then need to verify that the implementation satisfies the actual requirement.

Practical lesson: Developers do not need to memorize every regulation, but they must understand the requirements that affect their application and know how to implement the relevant controls.

## 17. Frameworks and Tools Recommended by the Lecturer

In the latter part of the lecture, the lecturer discusses tools and frameworks covered in a course syllabus.

These are presented as learning resources for implementing the shared governance and security capabilities.

### 17.1 Guardrails

The lecturer mentions three approaches or tools:

- Demo guardrails: The transcript refers to a guardrails demonstration or implementation, but does not identify a specific framework by this name.
- AWS guardrails: Guardrails relevant to AI applications deployed in AWS environments.
- Guardrails AI: A framework the lecturer says is covered in depth, with demonstrations of integrating guardrails into an AI agent.

The objective is to learn how to implement practical constraints rather than merely understand the concept theoretically.

### 17.2 Evaluations

The lecturer identifies two evaluation frameworks.

[Beyond Semantic Search: Measuring Technical Answer Quality with RAGAS — Part 2 | by Retheesh Ravi | Medium](https://images.openai.com/static-rsc-4/ASMJcmpLBn2oG9Q84iZjXxrKLmxoOKHqLNzc3epBoYOFw1Qj2PjCwN9qSz6iJXdlbjIIaAxR8KWuFrPpAI-yKsSlHrPTTTQEO4k__qY7vuYFjINoq0XnM2VsNhTzhBV0-HTicIE4krUpG6jSAlxhCrCn9Cco6xoDAokE0S1iDQY?purpose=inline)

RAGAS

Used for evaluating retrieval-augmented generation (RAG) systems. It can help assess aspects such as retrieval quality and the relationship between retrieved context and generated answers.

The lecturer particularly recommends it for RAG-related use cases.

[Third-party Scorers | MLflow](https://images.openai.com/static-rsc-4/mrVMeCK19dVjDf6qYDwFuVz2aqBtcFKeZL-GaNkzPhOWIDyL2oeGZnxqqeHjmbGFKad3ZEV8QWbz94F7imaniBIsMW0XaKOdpLHkk3LyiGDI5mFZKHC_sNAzFSej3SZohCS0PRRHbaivgx6fGKPYiWQEVV-ckWAdWEfLozlz_-k?purpose=inline)

DeepEval

An LLM evaluation framework that can be used to assess different aspects of model and application behavior through tests and evaluation metrics.

The lecturer refers to this as “DP wells” in the transcript; the intended framework appears to be DeepEval.

The lecturer suggests that RAGAS is useful for many RAG use cases and presents DeepEval as a broader evaluation option for agent applications.

These frameworks support testing, but they do not independently establish regulatory compliance.

### 17.3 Red teaming

The lecturer also covers red teaming, intended to help developers identify weaknesses in AI applications by deliberately testing problematic or adversarial scenarios.

The transcript does not identify a particular red-teaming framework in this section.

### 17.4 Observability

The lecturer highlights two observability tools:

[LangSmith: Agent & LLM Observability Platform](https://images.openai.com/static-rsc-4/6PEdiaisqawILFCVEkEtct1o3_AYcGeqGrMdFgCGa4gDRcbd4Ye_3uqFI6sqrUY0TZc-ZIbrtE997QPbYH5O7veac1gkxC9vsXUVWQ9zngXJEqjwehwxHnG1ohlWQzsTGvsRC3_zeGVDJBXd6KciZKDLOrecPAOLrduro4dKuIE?purpose=inline)

LangSmith

Used to trace and inspect LLM application execution, helping developers understand the sequence of operations and investigate problems.

[Debugging & Monitoring with Pydantic Logfire - Pydantic AI](https://images.openai.com/static-rsc-4/u8rZU002_Kwls9-NHYMDk18Tw-l_vlfue_nUy7VGyM2YhxyyKDyGA5_qPa4PizC6f9XnLj4DZrRV9QUQ0Fl4G4ZWt-751kNxdtILg6Q0Esetysh5aE9YLMYQEukmFn4nTxHSC6MXZGGTNHSdQ7wW6D-uEN4OS9AjTBLWk8HuLE8?purpose=inline)

Pydantic Logfire

An observability tool that can provide visibility into application execution and help developers diagnose behavior and failures.

The lecturer emphasizes that observability remains fundamental even when an application uses evaluation and guardrail frameworks.

The agent's execution needs to be traced and inspected so that developers can understand what happened and investigate failures.

## 18. Why Observability Comes Before Advanced Governance Controls

The lecturer returns to observability toward the end of the session.

Even if a developer implements evaluations, guardrails, and red teaming, they still need a way to inspect the application's behavior.

Consider an agent that fails an evaluation or produces an unexpected result.

Without useful traces, it may be difficult to establish:

- Which model call produced the output.
- Which information was retrieved.
- Which tool was called.
- What sequence of actions occurred.
- Where an error originated.
- Whether a policy check ran.
- Which part of the implementation needs improvement.

Observability helps connect a test failure or incident to the actual execution.

### The recommended learning sequence implied by the lecture

1. Understand observability and tracing.
2. Learn to inspect agent execution.
3. Add and test guardrails.
4. Build evaluation suites.
5. Conduct red-team testing.
6. Integrate incident-response procedures.
7. Map the resulting controls and evidence to applicable governance requirements.

This is a practical learning order, not a rule that every project must implement these steps strictly one after another. In real projects, these activities often develop in parallel.

## 19. Key Distinctions to Remember

| Concept                  | Main purpose                                                   | Car analogy                                             |
| ------------------------ | -------------------------------------------------------------- | ------------------------------------------------------- |
| AI governance            | Establish rules, responsibilities, and compliance requirements | Vehicle laws and licensing requirements                 |
| AI security              | Protect the system from unauthorized access and threats        | Locks and alarm systems                                 |
| Observability            | Measure and inspect system behavior                            | Speedometer                                             |
| Evaluations              | Test whether requirements are met                              | Vehicle safety ratings                                  |
| Guardrails               | Constrain unwanted behavior                                    | ABS and emergency braking                               |
| Red teaming              | Discover weaknesses by deliberately challenging the system     | Authorized attempts to break into a vehicle             |
| Incident response        | Handle and recover from incidents                              | Investigating and addressing a vehicle security failure |
| Frameworks and standards | Provide structured requirements or guidance                    | Applicable vehicle standards and regulations            |

The analogy is useful for remembering the distinctions, but it is not a formal classification of every control.

## 20. Final Revision Notes

The following are the most important points to retain from this lecture.

1\. AI governance has a strategic side and a technical side. Strategic governance defines requirements, while technical teams implement the controls that help satisfy them.

2\. AI governance and AI security overlap. They are related but not identical.

3\. Governance requirements depend on the deployment context. Different jurisdictions, applications, and data types may require different controls.

4\. Observability is foundational. Like a speedometer in a car, it helps measure and inspect system behavior. It does not automatically prevent unsafe actions.

5\. Governance policies and security mechanisms serve different roles. A policy defines what is allowed; security controls help enforce the appropriate boundaries.

6\. Evaluations test an AI system against specified criteria. An agent should meet the applicable acceptance thresholds before deployment.

7\. Guardrails constrain inputs, outputs, or actions. Examples include PII checks, toxicity checks, and bias-related checks.

8\. Red teaming deliberately searches for weaknesses. It tests whether an agent can be manipulated or its restrictions bypassed.

9\. Incident response handles failures and security events. It includes detection, containment, investigation, remediation, and documentation.

10\. Know the resources mentioned. The lecture names ISO/IEC 42001, NIST, the EU AI Act, OWASP Top 10 for LLM Applications, Guardrails AI, RAGAS, DeepEval, LangSmith, and Pydantic Logfire.

11\. Use the right tool for the right task. Observability, evaluations, guardrails, and red teaming provide different but complementary capabilities.

12\. Compliance is not established by tools alone. An organization must identify the relevant requirements, implement appropriate controls, test them, and retain evidence that supports its compliance assessment.

13\. The overall objective is trustworthy AI. Governance, security, testing, monitoring, and incident management must work together to make AI deployments more reliable and appropriately controlled.

### One-line summary

Governance defines what an AI agent must comply with; security protects its boundaries; observability shows what it does; evaluations measure whether it meets requirements; guardrails constrain unwanted behavior; red teaming exposes weaknesses; and incident response addresses failures.