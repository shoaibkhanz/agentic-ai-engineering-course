# Research

## Research Results

<details>
<summary>What are best practices for creating a practical cost-estimation model for LLM agent projects, including factors like token pricing, reasoning steps, and tool usage?</summary>

### Source [1]: https://www.pondhouse-data.com/blog/how-to-save-on-llm-costs

Query: What are best practices for creating a practical cost-estimation model for LLM agent projects, including factors like token pricing, reasoning steps, and tool usage?

Answer: The cost of running LLM agents is primarily influenced by **token pricing**, the **size of the model**, the **number of requests**, and the **computational resources required** per request. Most LLM providers bill by the number of tokens processed, so higher token counts directly increase costs. Selecting smaller, task-specific models can help reduce expenses as they consume fewer resources and process fewer tokens, compared to large general-purpose models. 

Best practices for cost-estimation modeling include:
- **Optimizing prompts** to minimize unnecessary tokens and ensure the most concise requests.
- **Using smaller, specialized models** for domain-specific tasks to reduce both token consumption and processing time.
- **Caching responses** to avoid repeated computation for identical queries, lowering the overall token usage.
- **Batching requests** when possible to maximize throughput and minimize per-request overhead.
- **Prompt compression**, **model quantization**, and **early stopping** techniques, which all contribute to reducing the computation required.
- **Fine-tuning** models for specific tasks can decrease both token usage and cost, as the model becomes more efficient.
- **Model distillation** and using retrieval-augmented generation (RAG) approaches can cut down the need to send large chunks of data to the LLM, further lowering costs.
- **Summarizing conversations** and responses can keep token usage lean.

Understanding these factors and applying these optimization strategies is fundamental to building a practical, scalable cost-estimation model for LLM agent projects.

-----

-----

</details>

<details>
<summary>How do different LLM orchestration frameworks like LangGraph compare to custom-built agent loops for managing state, checkpoints, and human-in-the-loop (HITL) interruptions?</summary>

### Source [5]: https://www.langchain.com/langgraph

Query: How do different LLM orchestration frameworks like LangGraph compare to custom-built agent loops for managing state, checkpoints, and human-in-the-loop (HITL) interruptions?

Answer: LangGraph is designed as a **controllable cognitive architecture** for building and scaling AI workloads, including conversational agents and complex task automation. It provides a **flexible framework** supporting diverse control flows, such as single-agent, multi-agent, hierarchical, and sequential structures. LangGraph stands out by offering robust support for **state management, checkpoints, and human-in-the-loop (HITL) interactions**. Built-in statefulness allows agents to collaborate with humans, enabling review and approval of actions before execution. Users can inspect agent actions, roll back ("time-travel") to previous states, and correct course as needed. Moderation and quality loops are easily added, preventing agents from deviating and allowing direct human intervention. The platform further allows templatization of cognitive architecture, making tools, prompts, and models configurable and reusable. In summary, LangGraph provides expressive, customizable agent workflows and strong mechanisms for reliability and human oversight.

-----

-----

-----

### Source [6]: https://docs.langchain.com/oss/python/langgraph/overview

Query: How do different LLM orchestration frameworks like LangGraph compare to custom-built agent loops for managing state, checkpoints, and human-in-the-loop (HITL) interruptions?

Answer: LangGraph is a **low-level orchestration framework and runtime** focused on building, managing, and deploying **long-running, stateful agents**. Core capabilities include **durable execution** (agents persist through failures and resume from checkpoints), comprehensive **memory management** (short-term and long-term), and **human-in-the-loop** (users can inspect and modify agent state at any point). LangGraph features deep debugging and observability through LangSmith, enabling visualization of execution paths, state transitions, and runtime metrics. The framework is **production-ready**, offering scalable infrastructure for stateful workflows. LangGraph does not abstract away prompts or architectures, providing flexibility for developers to customize agents. It integrates seamlessly with the broader LangChain ecosystem, enabling enhanced agent evaluation, observability, and deployment. Compared to custom-built loops, LangGraph offers standardized primitives for state, checkpointing, and HITL, reducing the need for bespoke implementation while improving reliability and visibility.

-----

-----

-----

### Source [7]: https://blog.langchain.com/how-to-think-about-agent-frameworks/

Query: How do different LLM orchestration frameworks like LangGraph compare to custom-built agent loops for managing state, checkpoints, and human-in-the-loop (HITL) interruptions?

Answer: LangGraph is an **event-driven framework** for agentic systems, utilizing a **declarative, graph-based syntax** where nodes represent units of work and edges represent transitions. The underlying logic remains imperative, allowing dynamic graph traversal. LangGraph incorporates a **built-in persistence layer**, facilitating fault tolerance, short-term and long-term memory, and enabling both “human-in-the-loop” and “human-on-the-loop” patterns (interrupt, approve, resume, time travel). Streaming support is provided for tokens, node updates, and events, which enhances user experience for long-running workflows. Debugging and observability are deeply integrated via LangSmith, allowing inspection of agent steps, inputs, and outputs. LangGraph’s **fault tolerance** allows for durable workflows with configurable retries. The framework enables capabilities that are often complex to build in custom agent loops, such as fine-grained HITL control, trajectory inspection, and rollback. While some features (e.g., short-term memory) are simple to implement custom, advanced features like human-on-the-loop and LLM-specific observability are more challenging and are natively supported in LangGraph.

-----

-----

-----

### Source [8]: https://xenoss.io/blog/llm-orchestrator-framework

Query: How do different LLM orchestration frameworks like LangGraph compare to custom-built agent loops for managing state, checkpoints, and human-in-the-loop (HITL) interruptions?

Answer: LangChain and its associated frameworks (including LangGraph) provide **open-source building blocks** for LLM applications, making orchestration of multi-step flows, retrieval, tool integration, and observability more accessible. LangChain’s ecosystem includes LangSmith for tracing and evaluation, LangServe for deployment, and LangGraph for managing stateful workflows. The platform supports a **declarative syntax** (LCEL) for composing reliable chains and offers extensive integration with models, vector stores, and tools. Its production tooling includes built-in tracing and evaluation features. LangChain/Graph is particularly suited for **orchestration-heavy RAG and agent systems** that require complex state, checkpoints, guardrails, and enterprise-scale observability. For custom-built agent loops, developers must manually implement state management, checkpointing, and HITL controls, which can be time-consuming and less reliable than using standardized orchestration frameworks like LangChain/LangGraph.

-----

-----

-----

### Source [9]: https://langchain-ai.github.io/langgraph/concepts/faq/

Query: How do different LLM orchestration frameworks like LangGraph compare to custom-built agent loops for managing state, checkpoints, and human-in-the-loop (HITL) interruptions?

Answer: LangGraph is characterized as a **low-level and highly controllable orchestration framework** for complex agentic systems, distinguishing itself from higher-level LangChain agents. It is more suitable for scenarios requiring fine-grained control, explicit state management, and advanced intervention mechanisms such as human-in-the-loop operations. Compared to custom-built agent loops, LangGraph provides standardized, reusable primitives for state and checkpoint management and is designed to be extensible for human interruption and guidance. This reduces the complexity and risk associated with developing these features from scratch, allowing developers greater reliability and observability in agent workflows.

-----

</details>

<details>
<summary>What are industry-standard evaluation frameworks and metrics for assessing the reliability and factuality of multi-agent LLM systems in production?</summary>

### Source [10]: https://galileo.ai/blog/benchmarks-multi-agent-ai

Query: What are industry-standard evaluation frameworks and metrics for assessing the reliability and factuality of multi-agent LLM systems in production?

Answer: Industry-standard evaluation frameworks for **multi-agent LLM systems** focus on both agent collaboration and competition, offering metrics and protocols tailored to production environments.

- **MultiAgentBench** is a comprehensive framework specifically designed for evaluating LLM-based multi-agent systems. It measures not only overall task completion but also the quality of agent collaboration and competition through milestone-based key performance indicators (KPIs). These KPIs track not just end results but intermediate milestones, providing granular insights into agent performance. The framework evaluates coordination protocols such as star, chain, tree, and graph topologies, as well as group discussion and cognitive planning strategies. This approach helps identify which coordination structures are most effective for given scenarios.

- The **modular design** of MultiAgentBench allows for flexible integration and replacement of components (agents, environments, LLM integrations). It supports hierarchical and cooperative execution modes and employs shared memory mechanisms for agent communication.

- **Enterprise-readiness** is a hallmark: MultiAgentBench uses Docker for reliable deployment, adheres to industrial software standards, and produces reproducible results, making it suitable for organizations moving from research to production.

Other notable frameworks:
- **BattleAgentBench** (focus: cooperation/competition, market simulation).
- **SOTOPIA-π** (focus: social intelligence, customer service).
- **MARL-EVAL** (focus: reinforcement learning, statistical rigor, coordination).
- **AgentVerse** (focus: diverse interaction paradigms).
- **SmartPlay** (focus: strategic reasoning, planning).

Each framework is suited to different domains and offers specialized metrics, but MultiAgentBench is highlighted for its comprehensive, production-grade evaluation of LLM-based multi-agent systems, particularly regarding reliability and factuality[1].

-----

-----

-----

### Source [11]: https://samiranama.com/posts/Evaluating-LLM-based-Agents-Metrics,-Benchmarks,-and-Best-Practices/

Query: What are industry-standard evaluation frameworks and metrics for assessing the reliability and factuality of multi-agent LLM systems in production?

Answer: This source provides a detailed breakdown of **key metrics and benchmarks** for evaluating LLM-based agents, including multi-agent systems, with a focus on reliability and factuality.

- **Task Success Rate and Stepwise Progress:** The standard metric is the success rate (fraction of episodes fully completed). Modern benchmarks (e.g., MultiAgentBench) break tasks into milestones or steps. Each agent’s KPI is based on the ratio of milestones completed, with progress tracked stepwise ("milestones achieved / total milestones"). This enables partial credit and diagnostic attribution of failures.

- **Action Advancement Metric:** Beyond binary correctness, each step is scored on whether it advances the agent toward the goal. This finer-grained metric reveals not just if the agent succeeded, but *how* it progressed through the task.

- **Tool Usage Metrics:** For systems using tools, metrics include tool-selection accuracy (was the right tool chosen?), parameter accuracy (was the tool/API used correctly?), and tool efficacy. These are essential for assessing reliability in production.

- **Coordination Efficiency and Communication Overhead:** For multi-agent setups, metrics include how efficiently agents coordinate, the amount of communication needed, and whether plans are high-quality and aligned. Group-level metrics assess fairness and alignment among agents.

- **Safety and Robustness:** Benchmarks also log safety checks and robustness to adversarial inputs.

Recent frameworks compared:
- **MultiAgentBench** (stepwise progress, milestone KPIs, modular).
- **MARBLE** (multi-agent benchmarks).
- **Self-Evolving Benchmark** and **Databricks’ DIBS** (diagnostics, scalability).

Key challenges for industry adoption include lack of standardization, need for better diagnostic tools, and scalability for real-world deployments. The best practice is to instrument all stages of agent reasoning and execution, not just outcome metrics, for holistic reliability and factuality assessment[2].

-----

-----

</details>

<details>
<summary>What are the architectural patterns for designing hybrid agent-workflow systems, particularly for triggering complex workflows via portable, tool-like interfaces?</summary>

### Source [12]: https://smythos.com/developers/agent-development/hybrid-agent-architectures/

Query: What are the architectural patterns for designing hybrid agent-workflow systems, particularly for triggering complex workflows via portable, tool-like interfaces?

Answer: Hybrid agent architectures are structured with two main layers: a **reactive layer** and a **deliberative layer**. The reactive layer provides instantaneous responses to environmental triggers, enabling agents to act quickly in urgent scenarios without the overhead of complex analysis. For instance, in workflow systems, this layer could allow an agent to immediately invoke or modify a workflow when a triggering event occurs. The deliberative layer, on the other hand, is responsible for strategic planning and decision-making, using symbolic models to analyze the environment and formulate multi-step plans. This layer manages complex workflow orchestration, evaluating options and sequencing actions to achieve long-term objectives.

These layers are organized in a way that allows seamless cooperation: the reactive layer handles immediate concerns (such as tool-like trigger interfaces), while the deliberative layer develops comprehensive strategies for workflow execution. This architecture is particularly suited to portable, tool-like interfaces, as the reactive layer can respond to user inputs or external events, quickly launching or adjusting workflows, while the deliberative layer ensures those workflows align with overarching system goals.

The main advantages of this dual-layer architecture include:
- **Enhanced adaptability:** Agents can shift between fast reactions and thoughtful planning as needed.
- **Efficient resource allocation:** Routine tasks are handled quickly, while complex decisions are reserved for deeper analysis, optimizing overall system performance.
- **Robustness and reliability:** If one layer encounters problems, the other can compensate, ensuring continued workflow execution.
- **Practical real-world applicability:** These architectures are well-suited to situations where both instant tool-like triggering and complex workflow orchestration are needed, such as robotics or intelligent assistants.

Hybrid architectures thus provide a foundation for systems that can trigger and manage complex workflows via portable interfaces, balancing immediate responsiveness with longer-term goal-directed behavior.

-----

-----

-----

### Source [13]: https://galileo.ai/blog/architectures-for-multi-agent-systems

Query: What are the architectural patterns for designing hybrid agent-workflow systems, particularly for triggering complex workflows via portable, tool-like interfaces?

Answer: Hybrid agent-workflow systems often use a **strategic center with tactical edges** architecture. In this pattern, centralized components handle strategic coordination and integrity (e.g., workflow orchestration, transaction management, global consistency), while decentralized agents at the edges execute tactical operations (e.g., local workflow steps, real-time optimizations, peer-to-peer interactions).

In practice, triggering complex workflows via portable, tool-like interfaces can be supported by:
- A **central orchestrator** that manages the initiation and integrity of workflows in response to user or system triggers.
- Regional or local agent clusters that take responsibility for executing workflow steps, negotiating resources, and optimizing outcomes based on local conditions.
- Agents at the edges may operate autonomously for tasks where speed and flexibility are needed, only escalating to the central orchestrator for issues requiring global oversight.

This hybrid approach enables:
- **Strategic oversight** for core workflow logic, data integrity, and auditing.
- **Tactical flexibility** for rapid adaptation, local optimization, and parallel processing.
- **Context-aware operation:** Centralized decisions for critical workflow triggers; local agents for execution or adjustment.

The architecture is particularly well-suited for portable interfaces, as agent clusters can expose tool-like interfaces (APIs, webhooks, natural language endpoints) for triggering workflows. The central orchestrator then coordinates the overall process, ensuring workflows are executed according to system goals, with agents handling local complexity.

Key considerations for this pattern include:
- Defining clear boundaries between centralized and decentralized workflow responsibilities.
- Ensuring agents know when to escalate to central coordination.
- Managing increased complexity in debugging and implementation due to distributed responsibilities.

-----

-----

-----

### Source [14]: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html

Query: What are the architectural patterns for designing hybrid agent-workflow systems, particularly for triggering complex workflows via portable, tool-like interfaces?

Answer: AWS describes **agentic patterns** as modular blueprints for designing agent-workflow systems that integrate AI agents, workflows, and event-driven triggers. Relevant architectural patterns include:

- **Reasoning agents and workflow orchestrators:** Individual agents can be designed to perceive inputs (from portable interfaces), reason about which workflows to trigger, and orchestrate complex sequences of actions.
- **Agentic workflow patterns:** These patterns define how multiple agents, tools, and environments interact to form autonomous systems. They cover task orchestration, delegation to subagents, event-driven coordination, and observability for auditability and control.
- **Event-driven architectures:** Portable, tool-like interfaces (such as APIs, natural language endpoints, or webhook triggers) connect to event buses or workflow engines. Agents respond to events by triggering workflows, with the system providing mechanisms for monitoring, logging, and controlling execution.

The guide emphasizes scalable, composable, and auditable architectures, supporting:
- **Flexible triggering mechanisms:** Agents can be invoked via portable interfaces and use LLMs for reasoning and planning, allowing for dynamic workflow selection and adaptation.
- **Modular workflow orchestration:** Task orchestration and subagent delegation are built into the architecture, facilitating the management of complex workflows through agent collaboration.
- **Production-grade system design:** Event-driven coordination ensures workflows can be triggered and monitored reliably, supporting both immediate responses and complex planning.

These patterns are mapped to AWS cloud-native services, but the architectural principles are applicable to any platform supporting agentic workflows and portable trigger interfaces.

-----

</details>

<details>
<summary>How does test-time parallel scaling (e.g., self-consistency with multiple attempts) compare to serial scaling (e.g., longer chain-of-thought) for improving reasoning reliability in state-of-the-art models?</summary>

### Source [15]: https://aclanthology.org/2025.acl-long.232.pdf

Query: How does test-time parallel scaling (e.g., self-consistency with multiple attempts) compare to serial scaling (e.g., longer chain-of-thought) for improving reasoning reliability in state-of-the-art models?

Answer: This source systematically compares **sequential (serial) and parallel test-time scaling** for state-of-the-art o1-like models. **Sequential scaling** increases the length of Chain-of-Thought (CoT) reasoning, prompting the model to self-revise its answers in multiple steps. However, experiments reveal that longer CoTs do not consistently improve accuracy; instead, more self-revision steps tend to degrade performance, as models more often change correct answers to incorrect ones rather than the reverse. This indicates **limited effectiveness of serial scaling** for these models.

In contrast, **parallel scaling** involves sampling multiple solutions in parallel and selecting the best (e.g., via majority vote or coverage metrics). Empirical results show that parallel scaling achieves **better coverage and scalability**: for a given computational budget, generating multiple independent solutions in parallel more reliably yields a correct answer than extending CoT length via serial self-revision. The study introduces "Shortest Majority Vote," a strategy that combines parallel scaling with insights about optimal CoT lengths, further improving reliability and test-time efficiency.

The key findings are:
- Serial scaling (longer CoT/self-revision) is less effective for improving reasoning reliability in o1-like models.
- Parallel scaling (multiple attempts/self-consistency) provides better coverage and accuracy for the same compute budget.
- The limitations of serial scaling are attributed to weak self-revision capabilities in current models.

This evidence suggests that for current state-of-the-art LLMs, **parallel test-time scaling is superior to serial scaling** for enhancing reasoning reliability and that hybrid strategies may yield further gains.

-----

-----

-----

### Source [16]: https://arxiv.org/html/2507.12549v1

Query: How does test-time parallel scaling (e.g., self-consistency with multiple attempts) compare to serial scaling (e.g., longer chain-of-thought) for improving reasoning reliability in state-of-the-art models?

Answer: This source advances the **Serial Scaling Hypothesis**, arguing from both theoretical and empirical perspectives that some problems in machine learning—especially those involving complex reasoning, planning, or sequential decision-making—are **inherently serial** and cannot be efficiently solved by parallel scaling alone. Complexity theory shows that certain tasks fundamentally require dependent, step-wise computation that cannot be parallelized without exponential resource costs.

Empirical evidence cited includes domains like mathematical reasoning, hard Sudoku, and many-body physics, where **models with greater serial computation (e.g., deeper networks, longer CoT)** achieve better generalization and performance. The authors caution that **relying solely on parallel scaling (multiple independent attempts)** may only work for problems that are not fundamentally sequential. For inherently serial tasks, models default to shallow heuristics at inference time if not given enough serial compute, limiting their ability to generalize and solve complex reasoning problems.

The authors recommend that:
- Model architectures should support deeper or more recurrent (serial) computation.
- Hardware should prioritize low-latency, sequential processing.
- Serial computation should be measured and reported distinctly from parallel compute.

In summary, this source contends that while parallel scaling is powerful for many tasks, **scaling serial computation is essential for reliably improving reasoning on problems that require multi-step, dependent computation**, and cannot be replaced by simply increasing parallel attempts.

-----

-----

-----

### Source [62]: https://arxiv.org/html/2502.12215v1

Query: How does test-time parallel scaling (e.g., self-consistency with multiple attempts) compare to serial scaling (e.g., longer chain-of-thought) for improving reasoning reliability in state-of-the-art models?

Answer: This study systematically compares **test-time parallel scaling** (e.g., self-consistency with multiple attempts) and **serial (sequential) scaling** (e.g., longer chain-of-thought, CoT) in state-of-the-art models such as QwQ, R1, and LIMO. Key findings include:

- **Longer CoTs do not consistently enhance accuracy**; correct solutions are often shorter than incorrect ones. Increasing CoT length (sequential scaling) does not continuously improve performance, indicating limited sequential-scaling capability.
- The primary limitation of sequential scaling is the model’s **insufficient self-revision capability**; during self-revision, models more often change correct answers to incorrect ones rather than correcting errors.
- In contrast, **parallel scaling**, which involves sampling multiple solutions in parallel and selecting the best one (e.g., via majority vote), achieves **better coverage (pass@k score)** and **superior scalability** compared to serial scaling. For a fixed compute budget (number of tokens), parallel scaling provides a larger improvement in finding a correct answer.
- Parallel scaling is also **computationally more efficient**: generating multiple short solutions in parallel is less costly than producing a single long chain-of-thought due to attention/computation over longer contexts in sequential methods.
- The paper proposes **Shortest Majority Vote**, a novel parallel scaling method prioritizing shorter, clustered solutions. This method further boosts performance beyond conventional majority voting.
- In experiments, sequential scaling (even with 40 self-revision steps) yielded diminishing returns, while parallel scaling's benefits scaled with more samples. Majority voting is effective only with at least three solutions; otherwise, its benefits are limited.

In summary, for o1-like models, **parallel scaling is more effective and efficient than serial scaling for improving reasoning reliability**[1].

-----

-----

-----

### Source [63]: https://aclanthology.org/2025.acl-long.232.pdf

Query: How does test-time parallel scaling (e.g., self-consistency with multiple attempts) compare to serial scaling (e.g., longer chain-of-thought) for improving reasoning reliability in state-of-the-art models?

Answer: This source analyzes the **test-time scaling** of o1-like models (QwQ, R1, LIMO), contrasting **sequential scaling** (longer chain-of-thought, CoT) with **parallel scaling** (multiple solutions, majority vote). Key points:

- **Sequential scaling** (longer CoT with self-revision) is ineffective in these models due to limited ability to correct mistakes. Empirically, models retain original (often incorrect) answers or sometimes convert correct answers to incorrect ones during revision. Thus, **self-revision ability is a bottleneck** for sequential scaling.
- **Parallel scaling**—sampling multiple solutions and selecting the best—provides **superior coverage (probability that at least one output is correct)** and **better scalability**. For the same compute (total tokens), parallel strategies outperform sequential ones.
- The proposed **Shortest Majority Vote** method leverages the observed trend that *shorter solutions* are more likely to be correct. By clustering solutions by answer and length, and prioritizing clusters with more and shorter solutions, this method further improves reliability over traditional majority voting.
- For both QwQ and R1, parallel scaling with majority vote or Shortest Majority Vote **substantially outperforms serial scaling** (even with 40 self-revision steps).
- Coverage is measured as the proportion of evaluation items where at least one candidate solution is correct; parallel scaling increases this more efficiently than serial.
- Finally, parallel scaling is less computationally demanding per correct answer since it avoids the need for models to process long contexts as in sequential scaling.

Thus, **parallel scaling is decisively more effective than serial scaling for test-time reliability improvements in these state-of-the-art models**[2].

-----

-----

-----

### Source [64]: https://arxiv.org/html/2507.12549v1

Query: How does test-time parallel scaling (e.g., self-consistency with multiple attempts) compare to serial scaling (e.g., longer chain-of-thought) for improving reasoning reliability in state-of-the-art models?

Answer: This source introduces the **Serial Scaling Hypothesis**, which asserts that for many complex reasoning and planning problems, **scaling parallel computation alone is insufficient**; instead, increasing **serial computation** (longer chains of reasoning, more search iterations) is essential.

- Theoretical and empirical evidence from complexity theory and domains like Sudoku, mathematical reasoning, and sequential decision-making show that **serial computation**—not just more parallel attempts—yields disproportionate gains for certain advanced tasks.
- Modern ML architectures, especially those relying on parallelism (e.g., Transformers), struggle with tasks that are inherently serial in nature. For such tasks, **longer or deeper serial reasoning steps** are critical.
- The authors recommend that as tasks become more challenging (e.g., requiring advanced reasoning, scientific discovery), model and hardware design should prioritize **deeper, more sequential architectures** and measure serial compute separately from total compute.

However, this work focuses on the limits of parallel scaling for specific classes of problems, asserting that for *some* tasks, **serial scaling is fundamentally necessary**, even as parallel scaling is easier to scale in practice[3].

-----

-----

</details>

<details>
<summary>What are the best practices for implementing human-in-the-loop (HITL) policies in LLM agent systems, including defining triggers, critical stop conditions, and approval gates?</summary>

### Source [19]: https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo

Query: What are the best practices for implementing human-in-the-loop (HITL) policies in LLM agent systems, including defining triggers, critical stop conditions, and approval gates?

Answer: **Best practices for implementing human-in-the-loop (HITL) policies in LLM agent systems** focus on carefully designing *where*, *when*, and *how* humans are involved in decision-making. Key patterns include:

- **Interrupt & Resume:** Agents pause mid-execution at critical checkpoints (e.g., tool calls, access approvals, potentially destructive actions). Human input (such as approval or denial) is gathered before the workflow resumes. This is ideal for inserting approval gates and handling long-running or sensitive workflows.
- **Human-as-a-Tool:** The agent treats a human as a callable resource. When uncertain, it routes queries for clarification or fact-checking to a designated human, then uses the response as context.

**Best practices include:**
- **Design for Decision Points:** Explicitly identify and enforce checkpoints where human input is needed, such as for approvals or sensitive actions.
- **Keep Prompts Contextual and Lightweight:** When requesting human approval, present clear, concise, and context-rich information—avoid overwhelming the reviewer with technical or raw data.
- **Use Policies, Not Hardcoded Logic:** Approval logic should reside in a policy engine for flexibility, versioning, and enforcement across all workflows instead of being hardcoded in the agent.
- **Comprehensive Logging:** Maintain audit trails for all requests, approvals, and denials. This supports compliance and enables review.
- **Support Asynchronous Reviews:** Not all approvals must be real-time. For lower-priority cases, route to asynchronous channels (like Slack or dashboards) to allow flexible human intervention.
- **Long-Term Pattern:** HITL is not a temporary fix but a foundational approach for trustworthy AI agents, ensuring oversight, safety, and operational boundaries even as autonomy increases.

Tools such as LangGraph, Permit.io, and LangChain MCP Adapters facilitate these best practices, making it easier to integrate permission and approval workflows without complex coding.

-----

-----

-----

### Source [20]: https://www.ninetwothree.co/blog/human-in-the-loop-for-llm-accuracy

Query: What are the best practices for implementing human-in-the-loop (HITL) policies in LLM agent systems, including defining triggers, critical stop conditions, and approval gates?

Answer: The "human in the loop" (HITL) approach in LLM agent systems is essential for achieving the highest levels of accuracy, particularly for tasks requiring nuanced judgment or domain expertise. The process typically involves:

- **Automated Processing:** LLMs handle the majority of routine or straightforward cases, often achieving around 80% accuracy.
- **Human Review for Complex Cases:** When the model’s output falls short—such as unclear, ambiguous, or high-stakes scenarios—human reviewers step in. They validate, correct, or complete the outputs, ensuring quality and compliance.
- **Iterative Training and Supervision:** Over time, human-in-the-loop interventions help train the model, steadily raising overall accuracy (sometimes into the high 90% range).

**Key considerations and challenges:**
- **Resource Intensive:** HITL processes require ongoing human resources, which may limit scalability.
- **Critical Thinking and Specialized Knowledge:** Humans provide crucial oversight where the model lacks context or makes errors that only expert judgment can resolve.
- **Triggers and Approval Gates:** Triggers for human intervention typically include model uncertainty, ambiguous outputs, or critical business decisions. Approval gates are inserted at these points.
- **Evolving Partnership:** As LLMs improve, the human role may focus more on supervision, training, and edge-case management, but HITL remains vital for optimal accuracy.

While research continues into making LLMs more self-evaluative, HITL remains the most reliable method for ensuring high-stakes outputs are accurate and trustworthy.

-----

-----

-----

### Source [21]: https://humanloop.com/blog/llm-guardrails

Query: What are the best practices for implementing human-in-the-loop (HITL) policies in LLM agent systems, including defining triggers, critical stop conditions, and approval gates?

Answer: **Implementing guardrails and HITL policies for LLM agents** involves several best practices to ensure safe and aligned outputs:

- **Customized Constraints:** Tailor guardrails to the specific needs and risks of your domain, such as privacy requirements or ethical guidelines. This avoids over-generalization and ensures the model operates within defined boundaries.
- **Red Teaming and Vulnerability Assessments:** Regularly test the system for weaknesses, including prompt injection and manipulation risks. Identify points where human intervention is most needed—these become critical stop conditions or approval gates.
- **Continuous Monitoring and Real-Time Auditing:** Use monitoring tools to flag inappropriate, biased, or factually incorrect outputs. Triggers for human intervention include flagged outputs or anomalies. Real-time auditing systems ensure rapid human review when risks are detected.
- **Feedback Loops:** Integrate mechanisms for users and moderators to provide feedback on outputs. This feedback guides ongoing refinement of policies, stop conditions, and the model itself.

By combining customized rules, proactive testing, real-time monitoring, and continuous feedback, organizations can define precise triggers for human review and clearly establish stop conditions and approval gates for critical decisions.

-----

-----

</details>

<details>
<summary>What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?</summary>

### Source [22]: https://www.descope.com/learn/post/mcp

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: The **Model Context Protocol (MCP)** is a standardized protocol designed to facilitate connections between Large Language Models (LLMs) and external data sources or tools, enabling interoperability and tool portability. MCP employs a **client-server architecture** inspired by the Language Server Protocol (LSP), aiming to create a universal method for AI applications to interact with external systems by standardizing context exchange.

MCP comprises four main components:
- **Host application:** The platform housing the LLM (e.g., Claude Desktop, AI-powered IDEs, web chat interfaces).
- **MCP client:** Built into the host application, it manages communication with MCP servers and translates host requirements into MCP-compliant requests.
- **MCP server:** Provides context and exposes specific functions, such as access to GitHub repositories or database operations.
- **Transport layer:** Supports STDIO for local integrations and HTTP+SSE for remote connections.

All communication is standardized using **JSON-RPC 2.0**, ensuring consistent request, response, and notification formats. By establishing a uniform protocol and message structure, MCP enables AI applications and tools to work together seamlessly, making it easier to integrate tools across different LLM agents and client platforms like IDEs[1].

-----

-----

-----

### Source [23]: https://stytch.com/blog/model-context-protocol-introduction/

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: **Model Context Protocol (MCP)** functions as a **universal adapter** between AI models and external data sources or tools. By defining a standardized protocol based on **JSON-RPC 2.0**, MCP allows LLMs to invoke functions, fetch data, or use predefined prompts in a secure and structured manner.

AI-powered applications (such as chatbots, IDE assistants, or agents) act as hosts running an MCP client, while each external integration is represented by an MCP server. The server exposes its capabilities—functions, data resources, or prompt templates—via MCP, and the client connects to leverage these capabilities. This architecture eliminates the need for custom integration code for each tool or API, significantly improving **tool portability and interoperability**.

MCP enables seamless, secure access to external resources for LLMs, allowing for consistent interactions across different platforms and reducing the integration burden for developers. This standardization is especially valuable for environments like IDEs, where multiple tools and workflows need to be accessible to LLM-powered agents without bespoke connector code[2].

-----

-----

-----

### Source [24]: https://modelcontextprotocol.info/docs/

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: **Model Context Protocol (MCP)** is described as a standardized protocol for enhancing interactions between LLMs and applications by providing **structured context management**. Its documentation highlights several core features:
- **Standardization:** MCP offers unified interfaces and protocols, streamlining development and facilitating interoperability.
- **Efficiency:** The protocol is optimized for context management, allowing LLMs to interact more effectively with external resources.
- **Extensibility:** MCP’s flexible architecture supports custom extensions, enabling adaptation to diverse integration needs.
- **Ease of Use:** It provides simple, intuitive APIs, lowering the barrier to entry for developers.

By standardizing context and tool integration, MCP allows applications to expose capabilities to LLM agents, improving portability and reducing the complexity of connecting different tools to various clients, including IDEs[3].

-----

-----

-----

### Source [25]: https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: The **Model Context Protocol (MCP)** is presented as a standardized protocol that enables AI models to interact with external tools and resources in a **structured way**. It supports multiple transport mechanisms (such as STDIO and HTTP-based SSE), offering flexibility for integration in various environments.

The Java SDK implements MCP with a **three-layer architecture**:
- **MCP Client:** Responsible for establishing and managing connections to MCP servers, implementing the client side of the protocol.
- **MCP Server:** Provides tools, resources, and capabilities, implementing the server side.
- **Transport Layer:** Facilitates synchronous and asynchronous communication.

Spring AI offers dedicated starters for both clients and servers, supporting both STDIO and SSE transports. This setup enables developers to easily bootstrap AI applications with standardized MCP support, ensuring **tool portability and interoperability** between AI models and external resources across different client platforms, such as IDEs[4].

-----

-----

-----

### Source [26]: https://modelcontextprotocol.io/specification/2025-06-18

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: According to the **official MCP specification**, MCP is an open protocol that enables seamless integration between LLM applications and external data sources and tools. It allows applications to:
- Share contextual information with language models.
- Expose tools and capabilities to AI systems.
- Build composable integrations and workflows.

**Key protocol details include:**
- **JSON-RPC message format:** Ensures consistent communication.
- **Stateful connections:** Maintain session context.
- **Capability negotiation:** Servers and clients negotiate supported features.

**Server features:**
- **Resources:** Provide context and data.
- **Prompts:** Offer templated messages and workflows.
- **Tools:** Expose functions for LLMs to execute.
- **Sampling, Roots, Elicitation:** Advanced server-initiated behaviors and requests.

Additional utilities include configuration management, progress tracking, cancellation, error reporting, and logging. MCP’s composable, standardized approach enables **interoperability and tool portability** by allowing any LLM agent or client (such as an IDE) to connect to a wide array of tools using the same protocol, regardless of vendor or implementation[5].

-----

-----

-----

### Source [27]: https://modelcontextprotocol.io

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: MCP (Model Context Protocol) is described as an **open-source standard** for connecting AI applications to external systems. It allows applications like Claude or other LLM agents to utilize external tools efficiently by **standardizing the interface** for tool integration.

By providing a uniform protocol for connecting to various external systems, MCP enables **tool portability** (tools can be reused across different LLMs and clients) and **interoperability** (different agents and platforms can interact with the same set of tools without custom integration code). This makes it easier for developers to build flexible, modular AI-powered workflows across platforms, such as IDEs, chatbots, or other interfaces[6].

-----

-----

-----

### Source [28]: https://www.anthropic.com/news/model-context-protocol

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: Anthropic introduces the **Model Context Protocol (MCP)** as an open standard for connecting AI assistants to the systems where data resides, such as content repositories, databases, or business applications. MCP standardizes how AI models receive context and access external tools, enabling **plug-and-play compatibility**.

MCP’s approach allows organizations and developers to:
- Integrate new tools and data sources into AI workflows without custom connectors.
- Ensure consistent, secure, and structured interactions between LLMs and external systems.
- Promote **interoperability** between different AI agents and client applications, such as IDEs.

Anthropic positions MCP as a foundational protocol for building adaptable and extensible AI ecosystems, where agents can access and utilize a diverse range of tools regardless of the specific LLM or client platform in use[7].

-----

-----

-----

### Source [29]: https://docs.claude.com/en/docs/mcp

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: The Claude documentation describes MCP as an **open protocol** that standardizes how applications provide context to LLMs, likening it to a "USB-C port for AI applications." MCP allows applications to expose tools and contextual information to LLMs in a consistent format.

This standardization supports **tool portability** (tools work across different LLM agents and clients) and **interoperability** (multiple agents and IDEs can access the same tools). Developers benefit by not needing to write custom API connectors for each integration. Instead, MCP enables any compliant tool or data source to be used by any MCP-compatible client or agent, making it much easier to develop modular, reusable AI-powered systems in environments like IDEs[8].

-----

-----

-----

### Source [30]: https://docs.langchain.com/oss/python/langchain/mcp

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: LangChain’s documentation explains that **Model Context Protocol (MCP)** is an open protocol that standardizes how applications provide tools and context to LLMs. MCP enables LangChain agents to use tools defined on MCP servers, ensuring **interoperability** between agents, clients, and tools.

By establishing a standard method for defining and accessing tools and context, MCP allows for **tool portability**: tools and integrations can be reused across different agents and platforms (like IDEs) without needing to adapt custom connectors or code. This approach simplifies the development and deployment of AI-powered applications that require access to a variety of external systems or data sources[9].

-----

-----

-----

### Source [65]: https://www.descope.com/learn/post/mcp

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: The **Model Context Protocol (MCP)** establishes a standardized method for LLMs to connect with external data sources and tools, enabling seamless integration and interaction. MCP uses a **client-server architecture** inspired by the Language Server Protocol (LSP), aiming to provide a universal way for AI applications to interface with external systems. Its architecture consists of four primary elements:
- **Host application:** Where the LLM resides and user interactions occur (e.g., Claude Desktop, AI-powered IDEs, web LLM interfaces).
- **MCP client:** Embedded within the host, handling connections to MCP servers and translating between host requirements and the protocol.
- **MCP server:** Exposes specific functions and context, such as GitHub repository access or database operations, to AI apps.
- **Transport layer:** Facilitates communication, either locally via STDIO or remotely using HTTP+SSE.

All MCP communications use **JSON-RPC 2.0** for standardized message exchange. By abstracting the integration process, MCP facilitates **tool portability** and **interoperability** between various LLM agents and clients such as IDEs, allowing developers to avoid the need for custom integration code for each tool or API[1].

-----

-----

-----

### Source [66]: https://stytch.com/blog/model-context-protocol-introduction/

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: The **Model Context Protocol (MCP)** is an open standard acting as a **universal adapter** between AI applications and external tools or data sources. MCP defines a common protocol (based on JSON-RPC 2.0) that enables LLMs to invoke functions, retrieve data, and use predefined prompts from external systems in a structured, secure way. Instead of requiring custom integration code for each tool or API, MCP provides a **single standardized interface** for all interactions.

MCP utilizes a **client-server architecture**: the host application (such as a chatbot, IDE, or agent) runs an MCP client, while external integrations (APIs, databases, etc.) function as MCP servers. The servers expose capabilities, and the client connects to them to utilize these features. This separation enables AI models to interact with a variety of tools and data sources, **facilitating interoperability and portability** between different agents and clients, including IDEs and development environments[2].

-----

-----

-----

### Source [67]: https://modelcontextprotocol.info/docs/

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: According to the MCP documentation, the protocol is designed to enhance **interaction between LLMs and applications** by providing **structured context management**. MCP offers unified interfaces and standardized protocols that simplify development, optimize context management, and support extensibility for custom extensions.

Key features include:
- **Standardization:** Unified interfaces for easier development and integration.
- **Efficiency:** Optimized handling of context for better model interactions.
- **Extensibility:** Flexible architecture allowing custom extensions and tool integrations.
- **Ease of use:** Simple, intuitive APIs reduce barriers for developers.

MCP supports **sampling mechanisms, transport protocols, toolsets, architecture guidelines, and prompt engineering best practices**, all of which contribute to enabling **tool portability and interoperability** between LLM agents and diverse clients, such as IDEs[3].

-----

-----

-----

### Source [68]: https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: The **Model Context Protocol (MCP)** enables AI models to interact with external tools and resources in a structured manner and supports multiple transport mechanisms for flexibility across environments. The Java MCP SDK provides implementations for both client and server roles, allowing standardized interaction through synchronous and asynchronous patterns.

Key architectural components include:
- **MCP Client:** Manages connections with MCP servers, implementing the client side of the protocol.
- **MCP Server:** Provides tools, resources, and capabilities to clients, implementing the server side.

Spring AI integrates MCP via boot starters for clients and servers, supporting both STDIO and HTTP/SSE transport layers. This modular architecture and support for different transports allow developers to integrate and port tools easily across various LLM agents and client environments, including IDEs[4].

-----

-----

-----

### Source [69]: https://modelcontextprotocol.io/specification/2025-06-18

Query: What is the Model Context Protocol (MCP) and how does it facilitate tool portability and interoperability between different LLM agents and clients like IDEs?

Answer: The **Model Context Protocol (MCP)** is an open protocol that enables seamless integration between LLM applications and external data sources or tools. MCP provides a standardized way for applications to:
- Share contextual information with language models
- Expose tools and capabilities to AI systems
- Build composable integrations and workflows

MCP's entities are:
- **Hosts:** LLM applications initiating connections
- **Clients:** Connectors within the host application
- **Servers:** Services providing context and capabilities

Key protocol features:
- **JSON-RPC message format**
- **Stateful connections**
- **Server and client capability negotiation**

MCP servers can provide:
- **Resources:** Data and context for users or AI models
- **Prompts:** Predefined workflows and templated messages
- **Tools:** Executable functions for AI models
- **Sampling:** Agentic behaviors and recursive interactions
- **Roots & elicitation:** Server-initiated inquiries and requests for additional user input

Utilities include configuration, progress tracking, cancellation, error reporting, and logging. MCP's standardized approach is foundational for **portability and interoperability** across agents, tools, and client applications[5].

-----

-----

</details>

<details>
<summary>How do modern LLM reasoning models like OpenAI's o-series, Anthropic's extended thinking, and Gemini's Deep Research compare in their approaches to "series scaling" or allocating more inference-time compute for complex tasks?</summary>

### Source [31]: https://epochai.substack.com/p/how-far-can-reasoning-models-scale

Query: How do modern LLM reasoning models like OpenAI's o-series, Anthropic's extended thinking, and Gemini's Deep Research compare in their approaches to "series scaling" or allocating more inference-time compute for complex tasks?

Answer: OpenAI's o-series models, such as o1 and o3, demonstrate significant scaling in "reasoning training compute," which refers specifically to the compute used for training models' reasoning capabilities, distinct from total pre-training compute. OpenAI released data indicating that o3 was trained with 10× the reasoning training compute of o1, and this scaling led to substantial improvements on benchmarks like AIME, as well as better performance on math, science, and coding tasks.

The scaling law for reasoning compute appears to follow a roughly log-linear relationship with performance, similar to classic scaling laws observed in pre-training, implying that allocating more compute for reasoning—both at training and inference-time—continues to yield capability gains. The article also discusses DeepSeek-R1, a reasoning model whose RL-based reasoning training cost was about 20% of its pre-training, providing a useful baseline. While there are uncertainties in absolute compute numbers, the trend is clear: scaling reasoning training and inference compute is leading to rapid and dramatic improvements, though this growth rate may slow as it catches up to overall training compute.

The discussion does not provide direct details about Anthropic's or Gemini's approaches but notes that most frontier AI developers are keeping the specifics of their reasoning model training and inference strategies private. It is suggested that these methods—allocating more inference-time compute and refining reasoning training—will be key to near-term progress in LLM reasoning capabilities.

-----

-----

-----

### Source [32]: https://openai.com/index/introducing-o3-and-o4-mini/

Query: How do modern LLM reasoning models like OpenAI's o-series, Anthropic's extended thinking, and Gemini's Deep Research compare in their approaches to "series scaling" or allocating more inference-time compute for complex tasks?

Answer: OpenAI's official introduction to o3 and o4-mini highlights that these models improve reasoning by both scaling up reinforcement learning (RL) during training and increasing inference-time reasoning. The core approach is that "more compute = better performance" holds true for RL-based reasoning training just as it did for pre-training. By pushing an additional order of magnitude in both training compute and inference-time reasoning (e.g., allowing the model to "think" longer or harder before responding), OpenAI validated that performance continues to improve the more the model is allowed to process.

For inference-time scaling, OpenAI notes that o3 delivers higher performance at equal latency and cost to o1, but if allowed to use more inference-time compute (i.e., given more "reasoning effort" or "thinking budget"), its performance increases further. This principle is applied in high-reasoning-effort settings such as "o4-mini-high." Additionally, models are trained via RL to use tools and to reason about when to deploy tools, enabling more agentic behavior and better handling of complex, multi-step tasks.

-----

-----

-----

### Source [33]: https://techcrunch.com/2024/12/23/openais-o3-suggests-ai-models-are-scaling-in-new-ways-but-so-are-the-costs/

Query: How do modern LLM reasoning models like OpenAI's o-series, Anthropic's extended thinking, and Gemini's Deep Research compare in their approaches to "series scaling" or allocating more inference-time compute for complex tasks?

Answer: TechCrunch reports that OpenAI's o3 exemplifies "test-time scaling"—an approach where more compute is allocated during inference (as opposed to just during training) to improve performance on complex tasks. This method is seen as a promising way to continue scaling AI capabilities, even as traditional pre-training scaling faces diminishing returns. The article notes that o3's performance leap was achieved just three months after o1, showcasing rapid progress.

The report also references Anthropic's public commentary, which suggests that the future of LLM progress will involve "splicing together test-time scaling and traditional pre-training scaling methods" to optimize returns. This indicates that Anthropic, and likely Google (Gemini), are adopting similar strategies—allocating increased inference-time compute for complex tasks and combining it with traditional scaling.

The article underscores that while test-time scaling is effective, it comes with drawbacks, such as increased computational cost and latency. Nonetheless, the industry consensus is that this approach is a central driver of continued rapid advances in LLM reasoning.

-----

-----

-----

### Source [34]: https://arxiv.org/html/2410.13639v1

Query: How do modern LLM reasoning models like OpenAI's o-series, Anthropic's extended thinking, and Gemini's Deep Research compare in their approaches to "series scaling" or allocating more inference-time compute for complex tasks?

Answer: This comparative study analyzes OpenAI's o1 reasoning model alongside established test-time compute methods, including Bag-of-N (BoN), Step-wise BoN, Agent Workflow, and Self-Refine, using GPT-4o as a backbone. The research demonstrates that o1 achieves the best performance on most benchmarks covering math, code, and commonsense reasoning.

The study finds that test-time compute methods—strategies that allocate more inference-time compute—can significantly enhance LLM reasoning capabilities. In particular, methods that break down problems into sub-problems (such as Agent Workflow) and those that use domain-specific prompts for planning can outperform more naive approaches like simple BoN.

The paper concludes that optimizing inference-time compute allocation—through strategic workflow planning and response diversity—enables more effective reasoning in LLMs. This aligns with the trend exemplified by OpenAI's o-series, which leverages increased inference-time reasoning for better problem-solving.

-----

-----

-----

### Source [35]: https://openai.com/index/learning-to-reason-with-llms/

Query: How do modern LLM reasoning models like OpenAI's o-series, Anthropic's extended thinking, and Gemini's Deep Research compare in their approaches to "series scaling" or allocating more inference-time compute for complex tasks?

Answer: OpenAI's technical commentary on reasoning models explains their large-scale reinforcement learning algorithm, which trains models to use chain-of-thought reasoning efficiently. The process focuses on enabling the model to "think productively" by allocating more compute to reasoning steps during both training and inference.

The document highlights that reasoning models are specifically optimized to allocate more "thinking time" (inference-time compute) as needed for complex tasks, rather than applying a fixed compute budget to all queries. This dynamic allocation allows the models to better handle tasks that require extended reasoning, mirroring human-like deliberation.

The approach is data-efficient and aims to generalize across a wide range of reasoning problems, suggesting that scaling reasoning compute—both during RL training and at inference—remains a core pillar of OpenAI's strategy for advancing LLM reasoning.

-----

-----

-----

### Source [36]: https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/reasoning

Query: How do modern LLM reasoning models like OpenAI's o-series, Anthropic's extended thinking, and Gemini's Deep Research compare in their approaches to "series scaling" or allocating more inference-time compute for complex tasks?

Answer: According to Microsoft's documentation on Azure OpenAI reasoning models (including GPT-5 series, o3-mini, o1, and o1-mini), these models are specifically designed to handle complex tasks by leveraging more sophisticated reasoning capabilities. The documentation notes that these models are capable of "complex code generation" and advanced task handling because they are optimized to spend more compute on reasoning-heavy queries.

The models' architecture allows for flexible allocation of inference-time compute, enabling them to "think longer" about difficult problems, thus improving their reasoning and problem-solving abilities. This aligns with the broader industry trend of using inference-time compute scaling as a way to enhance LLM performance on complex or multistep tasks.

-----

-----

</details>

<details>
<summary>What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?</summary>

### Source [38]: https://www.anthropic.com/engineering/built-multi-agent-research-system

Query: What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?

Answer: Anthropic’s multi-agent research system utilizes an **orchestrator-worker architectural pattern**. Here, a lead agent (orchestrator) analyzes the user query, plans the research process, and spawns parallel subagents (workers) to explore different aspects simultaneously. These subagents act as intelligent filters, iteratively using search tools to gather information and returning their findings to the lead agent, which synthesizes the final output.

Key principles include:
- **Parallelization:** Multiple agents work concurrently, efficiently covering broad or exploratory queries by decomposing the main task into subtasks.
- **Dynamic, multi-step search:** Unlike static retrieval approaches, agents adaptively search, analyze, and refine based on findings at each step.
- **Scalability:** The architecture distributes work across agents with separate context windows, expanding token and reasoning capacity beyond single-agent limitations.
- **Evaluation and reliability:** The system outperforms single-agent designs for complex, breadth-first tasks, but is more resource-intensive and best suited for tasks with high value.
- **Context sharing:** Agents return filtered, relevant information for aggregation, but domains with high interdependency or need for shared context (like stateful writing workflows) may be less suited for pure parallelization.

This pattern supports a **flexible, exploratory research agent** (lead) coordinating with **structured, stateful workflow agents** (workers), balancing adaptivity with reliability and throughput.

-----

-----

-----

### Source [39]: https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system

Query: What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?

Answer: Google Cloud describes several **multi-agent system patterns**, notably the **swarm pattern** and hierarchical/collaborative workflows. The swarm pattern features a **dispatcher agent** that routes user requests to a collaborative group of specialized agents. Each agent can communicate with every other agent, allowing them to share findings, critique proposals, and build upon each other's work. This iterative, all-to-all communication is well suited to ambiguous, exploratory tasks that benefit from debate and refinement.

Key aspects:
- **Collaborative refinement:** Agents iteratively improve solutions by sharing perspectives and critiquing each other's outputs.
- **Task handoff and specialization:** Any agent can delegate to another better suited for a subsequent step, supporting both exploration and structured workflows.
- **Explicit exit conditions:** Required to prevent unproductive loops; e.g., consensus, iteration/time limits.
- **Complexity and cost:** Swarm systems are more challenging to implement and operate due to intricate inter-agent communication and increased computational overhead.
- **Applicability:** Swarm pattern is optimal for problems that blend open-ended exploration (research) with structured, multi-step workflows (writing), leveraging both flexible and stateful agent roles.

-----

-----

-----

### Source [40]: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns

Query: What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?

Answer: Microsoft’s Azure Architecture Center emphasizes **multi-agent orchestration patterns** for complex AI systems. These patterns enable breaking down problems into specialized units, assigning each to dedicated agents with domain-specific expertise.

Core benefits:
- **Specialization:** Agents focus on particular domains, reducing complexity and enabling targeted optimization.
- **Scalability and maintainability:** Agents can be added or modified independently, streamlining testing and debugging.
- **Optimization:** Each agent can use different models, tools, or strategies suited to its subtask.
- **Coordination patterns:** The guide covers proven orchestration patterns, enabling agents to reliably collaborate on tasks that combine exploratory research and stateful workflows.

These orchestration patterns directly support architectures where a **flexible research agent** can work alongside or coordinate with more **structured, stateful workflow agents**, delivering both adaptability and reliability.

-----

-----

-----

### Source [41]: https://www.confluent.io/blog/event-driven-multi-agent-systems/

Query: What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?

Answer: Confluent discusses four primary **event-driven multi-agent system patterns**:
- **Orchestrator-worker:** A central orchestrator delegates tasks to workers (agents) specialized for subtasks. This pattern is ideal for combining exploratory (flexible) agents with agents that handle structured, stateful workflows, as the orchestrator integrates results from various workers.
- **Hierarchical agent:** Agents are arranged in a hierarchy; higher-level agents coordinate lower-level agents, which may themselves delegate further. This supports both broad exploration and structured task execution.
- **Blackboard:** Agents interact via a shared blackboard (data store), posting partial solutions and building on each other's contributions. This enables flexible exploration but can also maintain state.
- **Market-based:** Agents negotiate or bid for tasks based on capabilities, promoting dynamic allocation and flexibility.

The **orchestrator-worker** and **hierarchical agent** patterns are especially suited for systems combining **exploratory research agents** and **stateful writing workflows**, offering both coordination and adaptability.

-----

-----

-----

### Source [42]: https://galileo.ai/blog/architectures-for-multi-agent-systems

Query: What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?

Answer: Galileo AI highlights **hierarchical and hybrid patterns** using graph-based workflows. The graph structure naturally models agent relationships, enabling both **reporting (structured, stateful workflows)** and **collaboration (exploratory research)**.

- **Hierarchical patterns:** Agents are organized in layers, with supervisors overseeing specialized agents. This allows a flexible research agent (at a higher level) to direct structured workflow agents (lower levels), maintaining both exploration and state.
- **Hybrid patterns:** Combine direct communication (collaborative, exploratory tasks) with hierarchical control (structured workflow management).

Graph-based workflows allow for dynamic, flexible task assignment and stateful process management, making them well-suited for multi-agent systems integrating both **flexible research** and **structured writing workflows**.

-----

-----

-----

### Source [59]: https://www.anthropic.com/engineering/built-multi-agent-research-system

Query: What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?

Answer: Anthropic describes a **multi-agent research system** based on an **orchestrator-worker pattern**. The architecture involves a lead agent that analyzes user queries, plans a research strategy, and spawns multiple specialized subagents to explore tasks in parallel. Each subagent uses tools to gather relevant information and reports its findings to the lead agent, who synthesizes the results into a final answer.

Key architectural insights:
- **Parallelism**: Subagents independently and simultaneously collect information, which enables the system to handle broad, exploratory research tasks more efficiently than a single-agent, sequential approach.
- **Dynamic Multi-Step Search**: Unlike traditional retrieval-augmented generation (RAG), this approach supports iterative, adaptive search—agents adjust their strategies based on new findings, which is especially valuable for complex, evolving research workflows.
- **Context Isolation**: Each agent operates with its own context window, increasing overall system capacity and enabling parallel reasoning across subagents.
- **Token Management**: Multi-agent systems can use significantly more tokens than single-agent systems, making them best suited for high-value tasks where parallelization outweighs cost.
- **Limitations**: Complex stateful workflows with strong inter-agent dependencies may not be ideal for current multi-agent architectures, which excel when tasks can be decomposed into relatively independent subtasks.

This pattern is well-suited for combining **flexible, exploratory research agents** (for breadth-first discovery) with the **structured, stateful writing workflow** handled by the lead/orchestrator agent.

-----

-----

-----

### Source [60]: https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system

Query: What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?

Answer: Google Cloud outlines several established **multi-agent patterns** relevant for combining flexible and structured agent workflows:

- **Decomposition and Specialization**: Break large objectives into sub-tasks assigned to specialized agents, facilitating modularity, scalability, and reliability.
- **Context Engineering**: Each agent receives a tailored context—such as history or constraints—to ensure effective operation. Techniques include isolating, persisting, or compressing context.
- **Orchestration Patterns**:
  - **Coordinator/Orchestrator Pattern**: A central agent assigns tasks, manages state, and aggregates responses, ideal for workflows requiring stepwise, stateful progression (e.g., writing).
  - **Swarm Pattern**: Agents communicate all-to-all, sharing and critiquing solutions for highly ambiguous or creative tasks. This is suited for flexible, exploratory work but requires explicit exit conditions and careful management to avoid unproductive loops.
- **Integration and Control**: The orchestrator (or dispatcher) ensures that specialized agents collaborate effectively, while context management and access controls maintain security and reliability.
- **Cost and Reliability Considerations**: Multi-agent systems require robust orchestration, precise context management, and can incur high operational costs due to parallel agent execution.

For a system that combines **exploratory research** (using flexible, debating agents) with **structured writing** (requiring stateful, stepwise orchestration), a **hybrid of the coordinator and swarm patterns** is recommended: use a lead agent (coordinator) to manage the structured workflow, and employ a swarm of specialized research agents for the exploratory phase.

-----

-----

-----

### Source [61]: https://www.confluent.io/blog/event-driven-multi-agent-systems/

Query: What are the established architectural patterns for designing a multi-agent system that combines a flexible, exploratory research agent with a structured, stateful writing workflow?

Answer: Confluent discusses **event-driven, multi-agent design patterns** that support scalable and efficient coordination among agents:

- **Context and Data Sharing**: Effective exchange of information among agents is critical; event-driven architectures help synchronize agents and ensure timely, accurate data dissemination.
- **Scalability and Fault Tolerance**: Event-driven patterns support scaling to many agents and enable graceful recovery from failures, making them suitable for complex workflows with diverse agent roles.
- **Integration Complexity**: Using events as the primary integration mechanism allows agents to interoperate with various tools and systems.
- **Decision Timeliness**: Real-time event propagation ensures agents can make decisions based on up-to-date information, essential for responsive research and writing tasks.
- **Safety and Validation**: Guardrails and validation logic are needed to prevent unintended actions and ensure quality—especially important when agents autonomously gather and synthesize information.

**Multi-agent design patterns** in this context emphasize flexible collaboration and coordination, leveraging events to manage both the exploratory research phase and the structured, stateful workflow inherent in writing tasks. This aligns with architectures that decouple agent roles and responsibilities while maintaining robust coordination and data integrity.

-----

-----

</details>

<details>
<summary>What is the most effective way to structure a practical, step-by-step decision framework for designing LLM agent systems, covering choices from model selection to orchestration and evaluation?</summary>

### Source [43]: https://www.promptingguide.ai/research/llm-agents

Query: What is the most effective way to structure a practical, step-by-step decision framework for designing LLM agent systems, covering choices from model selection to orchestration and evaluation?

Answer: A practical LLM agent framework consists of several core components crucial for decision-making and autonomy:

- **User Request:** The system begins with a user query or task.
- **Agent/Brain:** The central LLM acts as the coordinator, using a prompt template that defines operational details and accessible tools.
- **Planning:** Supports the agent in mapping out a sequence of actions to achieve the user's goal.
- **Memory:** Manages records of the agent’s previous actions, ensuring context continuity.

Agent profiling is a notable strategy for specifying the agent’s role, personality, or social context. Profiling can be handcrafted, generated by an LLM, or derived from data. Explicit role details are embedded directly in the agent’s prompt, influencing both behavior and decision logic. This modular separation enables systematic design and evaluation at each stage, facilitating clarity from model selection (in the agent/brain) to orchestration (via planning and memory) and ongoing evaluation (by maintaining structured logs and behavioral profiles)[1].

-----

-----

-----

### Source [44]: https://pangyoalto.com/en/a-guide-to-the-llm-agent-framework-for-the-average-developer/

Query: What is the most effective way to structure a practical, step-by-step decision framework for designing LLM agent systems, covering choices from model selection to orchestration and evaluation?

Answer: An effective LLM agent architecture is structured through four essential modules:

- **Profiling:** Defines the agent’s role, personality, and social context. Profiles can be manually specified, LLM-generated, or sourced from real datasets. Clear profiling ensures the agent behaves consistently according to its intended purpose.
- **Memory:** Records the agent’s past actions, enabling context-aware reasoning and continuity over time.
- **Planning:** Enables the agent to anticipate future steps, ensuring actions are goal-oriented and not reactive or isolated.
- **Action:** Converts agent decisions into outputs, closing the loop between reasoning and execution.

This modular framework guides the developer from role definition (profiling) through context management (memory), strategic sequencing (planning), and practical execution (action). Each module addresses a unique design challenge and collectively supports end-to-end orchestration and evaluation[2].

-----

-----

-----

### Source [45]: https://www.leanware.co/insights/llm-agent-architecture-guide

Query: What is the most effective way to structure a practical, step-by-step decision framework for designing LLM agent systems, covering choices from model selection to orchestration and evaluation?

Answer: A modular LLM agent system is organized into distinct components, each responsible for a critical aspect of autonomous operation:

- **Agent Core (Brain):** The LLM module orchestrates perception, planning, and action cycles. It uses prompt templates or custom policies for decision logic, managing goals by breaking them into actionable steps and selecting suitable tools or responses.
- **Memory Modules:** Short-term memory captures ongoing interactions; long-term memory (often managed through vector databases) preserves historical data, user preferences, and knowledge across sessions. Episodic memory may track sequences for learning or error avoidance.
- **Planning Mechanisms:** The system analyzes tasks, decomposes them into steps, and sequences actions.
- **Tool Use and Integration:** External APIs and functions are invoked as needed, expanding the agent’s practical capabilities.

The agent’s effectiveness depends on thoughtful model selection and control policies (for the core), robust context management (memory), and smart orchestration (planning and tool integration). Evaluation is supported by logging decisions, tracking outcomes, and learning from historical context[3].

-----

-----

-----

### Source [46]: https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf

Query: What is the most effective way to structure a practical, step-by-step decision framework for designing LLM agent systems, covering choices from model selection to orchestration and evaluation?

Answer: OpenAI’s practical guide emphasizes three foundational components for agent design:

- **Model:** The choice of LLM drives reasoning and decision-making. Model selection should begin with the most capable model to establish a performance baseline, followed by iterative substitution with smaller models to optimize cost and latency while maintaining accuracy.
- **Tools:** External functions or APIs extend the agent’s capacity to execute real-world actions.
- **Instructions:** Explicit guidelines and guardrails define how the agent should behave.

For orchestration, OpenAI recommends using a variety of models within the workflow—assigning simpler models to basic tasks and reserving advanced models for complex decisions. Performance evaluation relies on setting up systematic evaluation pipelines (evals) to measure accuracy, cost, and latency throughout development. This step-by-step process ensures that agents are reliable, well-calibrated, and cost-effective[4].

-----

-----

-----

### Source [47]: https://www.vellum.ai/blog/the-ultimate-llm-agent-build-guide

Query: What is the most effective way to structure a practical, step-by-step decision framework for designing LLM agent systems, covering choices from model selection to orchestration and evaluation?

Answer: Vellum AI’s guide outlines practical steps for building effective LLM agents:

- **Core Components:** Identify and implement MCP (model, context, prompt), tool use, context engineering, and memory management as the basis for agent design.
- **Architecture Selection:** Decide between simple agent loops or more autonomous, logic-rich systems with subagents for complex tasks.
- **Reliability Strategies:** Successful teams build agents incrementally, starting with minimal viable prototypes, refining through iterative testing, and expanding capabilities as reliability improves.
- **Decision Points:** Evaluate whether to build a custom agent stack or leverage existing platforms/frameworks based on use case complexity, team expertise, and operational requirements.

This framework covers all stages from initial model selection, context and memory engineering, integration of tools, orchestrating multi-step processes, and continuous end-to-end evaluation and testing to ensure practical utility and robustness[5].

-----

</details>

<details>
<summary>What are the latest industry best practices for creating a step-by-step decision framework for LLM agent system design, covering model selection, orchestration, and evaluation?</summary>

### Source [48]: https://www.classicinformatics.com/blog/how-llms-and-multi-agent-systems-work-together-2025

Query: What are the latest industry best practices for creating a step-by-step decision framework for LLM agent system design, covering model selection, orchestration, and evaluation?

Answer: The latest industry best practices for LLM agent system design emphasize the integration of **LLMs with Multi-Agent Systems (LLM-MAS)**, creating scalable and modular architectures capable of handling complex, real-world problems. The recommended step-by-step decision framework includes:

- **Phase 1: Define Roles**  
  Identify the roles for each agent within the system, such as Planner (task decomposition), Researcher (data gathering), Executor (task execution), and Evaluator (output validation). Select appropriate LLMs to power each role; these may differ depending on task specialization.

- **Phase 2: Set Up Communication**  
  Establish robust inter-agent communication protocols using frameworks like AutoGen or LangChain. Define data exchange formats (e.g., JSON, YAML) to ensure consistent and clear messaging between agents.

- **Scalability & Flexibility**  
  The modular nature of LLM-MAS allows for easy scaling and adaptation across industries. Specialized agents can independently or collaboratively handle tasks, improving efficiency and adaptability.

- **Real-time Adaptation & Coordination**  
  Systems are designed to dynamically adjust strategies based on real-time data, ensuring decisions are contextually relevant and up-to-date.

- **Distributed Problem Solving**  
  Collaboration among agents enables parallel task execution, speeding up problem-solving and decision-making.

Additional best practices include orchestrating communication, managing agent memory, and implementing trust mechanisms to ensure the system operates reliably and efficiently.

-----

-----

-----

### Source [49]: https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns

Query: What are the latest industry best practices for creating a step-by-step decision framework for LLM agent system design, covering model selection, orchestration, and evaluation?

Answer: Databricks provides actionable best practices for designing generative AI agent systems, focusing on stability and maintainability:

- **Start Simple**  
  Begin with the least complex architecture, such as a deterministic chain, and only escalate to single-agent or multi-agent systems as needs become more dynamic or complex.

- **Evolve Gradually**  
  Add complexity (like tool calling or multi-agent structures) only when justified by distinct domain needs or large tool sets.

- **Prompt Engineering**  
  Use clear, minimal prompts to avoid contradictory instructions and reduce hallucinations. Only provide agents with the specific tools and context required for their task.

- **Logging & Observability**  
  Implement detailed and secure logging for user requests, agent plans, and tool calls. Tools like MLflow Tracing help capture structured logs for debugging and monitoring.

- **Model Updates & Version Pinning**  
  Pin model versions and run frequent regression tests to maintain agent logic consistency, especially as LLM providers may update models unexpectedly. Combine MLflow with agent evaluation frameworks to streamline versioning and quality assessment.

These practices ensure robust orchestration, controlled evolution, and rigorous evaluation throughout the agent system lifecycle.

-----

-----

-----

### Source [50]: https://www.vellum.ai/blog/the-ultimate-llm-agent-build-guide

Query: What are the latest industry best practices for creating a step-by-step decision framework for LLM agent system design, covering model selection, orchestration, and evaluation?

Answer: Vellum AI’s guide outlines a practical, stepwise approach centered on reliability and scalability:

- **1) Start Small and Outline Goals**  
  Clearly define the problem, scope, and success criteria before coding. Document memory, context, and compliance requirements to reduce failure risks and accelerate iteration.

- **2) Model and Rule Selection**  
  Choose the LLM and set parameters like temperature, max tokens, and step limits. Define the system prompt, specifying agent role, style, tool usage, and escalation protocols.

- **3) Architecture Selection**  
  Select an agent architecture that matches use case complexity:
  - **Single-threaded agents**: Best for short, tightly coupled tasks.
  - **Multi-agent systems**: Preferable for open-ended, parallel, or research-heavy workflows.

- **Reliability and Safety**  
  Prioritize reliability by documenting failure modes and compliance requirements early. Clear acceptance criteria support faster, safer scaling and iteration.

This framework advocates for incremental development, rigorous requirements definition, and conscious architectural choices to ensure agent reliability and effectiveness.

-----

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open protocol that</summary>

[Model Context Protocol](https://modelcontextprotocol.io/) (MCP) is an open protocol that
enables seamless integration between LLM applications and external data sources and
tools. Whether you’re building an AI-powered IDE, enhancing a chat interface, or creating
custom AI workflows, MCP provides a standardized way to connect LLMs with the context
they need.This specification defines the authoritative protocol requirements, based on the
TypeScript schema in
[schema.ts](https://github.com/modelcontextprotocol/specification/blob/main/schema/2025-06-18/schema.ts).For implementation guides and examples, visit
[modelcontextprotocol.io](https://modelcontextprotocol.io/).The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD
NOT”, “RECOMMENDED”, “NOT RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be
interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14)
\[ [RFC2119](https://datatracker.ietf.org/doc/html/rfc2119)\]
\[ [RFC8174](https://datatracker.ietf.org/doc/html/rfc8174)\] when, and only when, they
appear in all capitals, as shown here.

## Overview

MCP provides a standardized way for applications to:

- Share contextual information with language models
- Expose tools and capabilities to AI systems
- Build composable integrations and workflows

The protocol uses [JSON-RPC](https://www.jsonrpc.org/) 2.0 messages to establish
communication between:

- **Hosts**: LLM applications that initiate connections
- **Clients**: Connectors within the host application
- **Servers**: Services that provide context and capabilities

MCP takes some inspiration from the
[Language Server Protocol](https://microsoft.github.io/language-server-protocol/), which
standardizes how to add support for programming languages across a whole ecosystem of
development tools. In a similar way, MCP standardizes how to integrate additional context
and tools into the ecosystem of AI applications.

## Key Details

### Base Protocol

- [JSON-RPC](https://www.jsonrpc.org/) message format
- Stateful connections
- Server and client capability negotiation

### Features

Servers offer any of the following features to clients:

- **Resources**: Context and data, for the user or the AI model to use
- **Prompts**: Templated messages and workflows for users
- **Tools**: Functions for the AI model to execute

Clients may offer the following features to servers:

- **Sampling**: Server-initiated agentic behaviors and recursive LLM interactions
- **Roots**: Server-initiated inquiries into uri or filesystem boundaries to operate in
- **Elicitation**: Server-initiated requests for additional information from users

### Additional Utilities

- Configuration
- Progress tracking
- Cancellation
- Error reporting
- Logging

## Security and Trust & Safety

The Model Context Protocol enables powerful capabilities through arbitrary data access
and code execution paths. With this power comes important security and trust
considerations that all implementors must carefully address.

### Key Principles

1. **User Consent and Control**   - Users must explicitly consent to and understand all data access and operations
   - Users must retain control over what data is shared and what actions are taken
   - Implementors should provide clear UIs for reviewing and authorizing activities
2. **Data Privacy**   - Hosts must obtain explicit user consent before exposing user data to servers
   - Hosts must not transmit resource data elsewhere without user consent
   - User data should be protected with appropriate access controls
3. **Tool Safety**   - Tools represent arbitrary code execution and must be treated with appropriate
        caution.
     - In particular, descriptions of tool behavior such as annotations should be
       considered untrusted, unless obtained from a trusted server.
   - Hosts must obtain explicit user consent before invoking any tool
   - Users should understand what each tool does before authorizing its use
4. **LLM Sampling Controls**   - Users must explicitly approve any LLM sampling requests
   - Users should control:
     - Whether sampling occurs at all
     - The actual prompt that will be sent
     - What results the server can see
   - The protocol intentionally limits server visibility into prompts

### Implementation Guidelines

While MCP itself cannot enforce these security principles at the protocol level,
implementors **SHOULD**:

1. Build robust consent and authorization flows into their applications
2. Provide clear documentation of security implications
3. Implement appropriate access controls and data protections
4. Follow security best practices in their integrations
5. Consider privacy implications in their feature designs

## Learn More

Explore the detailed specification for each protocol component:

[**Architecture**](https://modelcontextprotocol.io/specification/2025-06-18/architecture) [**Base Protocol**](https://modelcontextprotocol.io/specification/2025-06-18/basic) [**Server Features**](https://modelcontextprotocol.io/specification/2025-06-18/server) [**Client Features**](https://modelcontextprotocol.io/specification/2025-06-18/client) [**Contributing**](https://modelcontextprotocol.io/community/communication)

</details>

<details>
<summary>The provided markdown content is an academic research paper titled "The Serial Scaling Hypothesis". The article guidelines describe a practical, engineering-focused lesson on "Agent System Design". There is no overlap in content between the two. The research paper discusses the theoretical computer science concepts of serial vs. parallel computation, while the lesson guidelines outline a step-by-step framework for designing LLM agent systems.</summary>

The provided markdown content is an academic research paper titled "The Serial Scaling Hypothesis". The article guidelines describe a practical, engineering-focused lesson on "Agent System Design". There is no overlap in content between the two. The research paper discusses the theoretical computer science concepts of serial vs. parallel computation, while the lesson guidelines outline a step-by-step framework for designing LLM agent systems.

Given the task is to *only remove* irrelevant sections and keep content pertinent to the guidelines, and since *none* of the provided markdown content is pertinent to the lesson described, the correct output is to return nothing.

</details>


## Code Sources

_No code sources found._


## YouTube Video Transcripts

_No YouTube video transcripts found._


## Additional Sources Scraped

<details>
<summary>building-with-extended-thinking-claude-docs</summary>

Extended thinking gives Claude enhanced reasoning capabilities for complex tasks, while providing varying levels of transparency into its step-by-step thought process before it delivers its final answer.

## Supported models

Extended thinking is supported in the following models:

- Claude Sonnet 4.5 ( `claude-sonnet-4-5-20250929`)
- Claude Sonnet 4 ( `claude-sonnet-4-20250514`)
- Claude Sonnet 3.7 ( `claude-3-7-sonnet-20250219`)
- Claude Haiku 4.5 ( `claude-haiku-4-5-20251001`)
- Claude Opus 4.1 ( `claude-opus-4-1-20250805`)
- Claude Opus 4 ( `claude-opus-4-20250514`)

API behavior differs across Claude Sonnet 3.7 and Claude 4 models, but the API shapes remain exactly the same.For more information, see [Differences in thinking across model versions](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#differences-in-thinking-across-model-versions).

## How extended thinking works

When extended thinking is turned on, Claude creates `thinking` content blocks where it outputs its internal reasoning. Claude incorporates insights from this reasoning before crafting a final response.The API response will include `thinking` content blocks, followed by `text` content blocks.Here’s an example of the default response format:

```
{
  "content": [\
    {\
      "type": "thinking",\
      "thinking": "Let me analyze this step by step...",\
      "signature": "WaUjzkypQ2mUEVM36O2TxuC06KN8xyfbJwyem2dw3URve/op91XWHOEBLLqIOMfFG/UvLEczmEsUjavL...."\
    },\
    {\
      "type": "text",\
      "text": "Based on my analysis..."\
    }\
  ]
}

```

For more information about the response format of extended thinking, see the [Messages API Reference](https://docs.claude.com/en/api/messages).

## How to use extended thinking

Here is an example of using extended thinking in the Messages API:

Shell

Python

TypeScript

Java

```
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-sonnet-4-5",
    "max_tokens": 16000,
    "thinking": {
        "type": "enabled",
        "budget_tokens": 10000
    },
    "messages": [\
        {\
            "role": "user",\
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?"\
        }\
    ]
}'

```

To turn on extended thinking, add a `thinking` object, with the `type` parameter set to `enabled` and the `budget_tokens` to a specified token budget for extended thinking.The `budget_tokens` parameter determines the maximum number of tokens Claude is allowed to use for its internal reasoning process. In Claude 4 models, this limit applies to full thinking tokens, and not to [the summarized output](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#summarized-thinking). Larger budgets can improve response quality by enabling more thorough analysis for complex problems, although Claude may not use the entire budget allocated, especially at ranges above 32k.`budget_tokens` must be set to a value less than `max_tokens`. However, when using [interleaved thinking with tools](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking), you can exceed this limit as the token limit becomes your entire context window (200k tokens).

### Summarized thinking

With extended thinking enabled, the Messages API for Claude 4 models returns a summary of Claude’s full thinking process. Summarized thinking provides the full intelligence benefits of extended thinking, while preventing misuse.Here are some important considerations for summarized thinking:

- You’re charged for the full thinking tokens generated by the original request, not the summary tokens.
- The billed output token count will **not match** the count of tokens you see in the response.
- The first few lines of thinking output are more verbose, providing detailed reasoning that’s particularly helpful for prompt engineering purposes.
- As Anthropic seeks to improve the extended thinking feature, summarization behavior is subject to change.
- Summarization preserves the key ideas of Claude’s thinking process with minimal added latency, enabling a streamable user experience and easy migration from Claude Sonnet 3.7 to Claude 4 models.
- Summarization is processed by a different model than the one you target in your requests. The thinking model does not see the summarized output.

Claude Sonnet 3.7 continues to return full thinking output.In rare cases where you need access to full thinking output for Claude 4 models, [contact our sales team](mailto:sales@anthropic.com).

### Streaming thinking

You can stream extended thinking responses using [server-sent events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents).When streaming is enabled for extended thinking, you receive thinking content via `thinking_delta` events.For more documention on streaming via the Messages API, see [Streaming Messages](https://docs.claude.com/en/docs/build-with-claude/streaming).Here’s how to handle streaming with thinking:

Shell

Python

TypeScript

Java

```
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-sonnet-4-5",
    "max_tokens": 16000,
    "stream": true,
    "thinking": {
        "type": "enabled",
        "budget_tokens": 10000
    },
    "messages": [\
        {\
            "role": "user",\
            "content": "What is 27 * 453?"\
        }\
    ]
}'

```

Example streaming output:

```
event: message_start
data: {"type": "message_start", "message": {"id": "msg_01...", "type": "message", "role": "assistant", "content": [], "model": "claude-sonnet-4-5", "stop_reason": null, "stop_sequence": null}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "Let me solve this step by step:\n\n1. First break down 27 * 453"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "\n2. 453 = 400 + 50 + 3"}}

// Additional thinking deltas...

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "signature_delta", "signature": "EqQBCgIYAhIM1gbcDa9GJwZA2b3hGgxBdjrkzLoky3dl1pkiMOYds..."}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": "27 * 453 = 12,231"}}

// Additional text deltas...

event: content_block_stop
data: {"type": "content_block_stop", "index": 1}

event: message_delta
data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": null}}

event: message_stop
data: {"type": "message_stop"}

```

When using streaming with thinking enabled, you might notice that text sometimes arrives in larger chunks alternating with smaller, token-by-token delivery. This is expected behavior, especially for thinking content.The streaming system needs to process content in batches for optimal performance, which can result in this “chunky” delivery pattern, with possible delays between streaming events. We’re continuously working to improve this experience, with future updates focused on making thinking content stream more smoothly.

## Extended thinking with tool use

Extended thinking can be used alongside [tool use](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview), allowing Claude to reason through tool selection and results processing.When using extended thinking with tool use, be aware of the following limitations:

1. **Tool choice limitation**: Tool use with thinking only supports `tool_choice: {"type": "auto"}` (the default) or `tool_choice: {"type": "none"}`. Using `tool_choice: {"type": "any"}` or `tool_choice: {"type": "tool", "name": "..."}` will result in an error because these options force tool use, which is incompatible with extended thinking.
2. **Preserving thinking blocks**: During tool use, you must pass `thinking` blocks back to the API for the last assistant message. Include the complete unmodified block back to the API to maintain reasoning continuity.

Example: Passing thinking blocks with tool results

Here’s a practical example showing how to preserve thinking blocks when providing tool results:

Python

TypeScript

Java

```
weather_tool = {
    "name": "get_weather",
    "description": "Get current weather for a location",
    "input_schema": {
        "type": "object",
        "properties": {
            "location": {"type": "string"}
        },
        "required": ["location"]
    }
}

# First request - Claude responds with thinking and tool request
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    tools=[weather_tool],
    messages=[\
        {"role": "user", "content": "What's the weather in Paris?"}\
    ]
)

```

The API response will include thinking, text, and tool\_use blocks:

```
{
    "content": [\
        {\
            "type": "thinking",\
            "thinking": "The user wants to know the current weather in Paris. I have access to a function `get_weather`...",\
            "signature": "BDaL4VrbR2Oj0hO4XpJxT28J5TILnCrrUXoKiiNBZW9P+nr8XSj1zuZzAl4egiCCpQNvfyUuFFJP5CncdYZEQPPmLxYsNrcs...."\
        },\
        {\
            "type": "text",\
            "text": "I can help you get the current weather information for Paris. Let me check that for you"\
        },\
        {\
            "type": "tool_use",\
            "id": "toolu_01CswdEQBMshySk6Y9DFKrfq",\
            "name": "get_weather",\
            "input": {\
                "location": "Paris"\
            }\
        }\
    ]
}

```

Now let’s continue the conversation and use the tool

Python

TypeScript

Java

```
# Extract thinking block and tool use block
thinking_block = next((block for block in response.content
                      if block.type == 'thinking'), None)
tool_use_block = next((block for block in response.content
                      if block.type == 'tool_use'), None)

# Call your actual weather API, here is where your actual API call would go
# let's pretend this is what we get back
weather_data = {"temperature": 88}

# Second request - Include thinking block and tool result
# No new thinking blocks will be generated in the response
continuation = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    tools=[weather_tool],
    messages=[\
        {"role": "user", "content": "What's the weather in Paris?"},\
        # notice that the thinking_block is passed in as well as the tool_use_block\
        # if this is not passed in, an error is raised\
        {"role": "assistant", "content": [thinking_block, tool_use_block]},\
        {"role": "user", "content": [{\
            "type": "tool_result",\
            "tool_use_id": tool_use_block.id,\
            "content": f"Current temperature: {weather_data['temperature']}°F"\
        }]}\
    ]
)

```

The API response will now **only** include text

```
{
    "content": [\
        {\
            "type": "text",\
            "text": "Currently in Paris, the temperature is 88°F (31°C)"\
        }\
    ]
}

```

### Preserving thinking blocks

During tool use, you must pass `thinking` blocks back to the API, and you must include the complete unmodified block back to the API. This is critical for maintaining the model’s reasoning flow and conversation integrity.

While you can omit `thinking` blocks from prior `assistant` role turns, we suggest always passing back all thinking blocks to the API for any multi-turn conversation. The API will:

- Automatically filter the provided thinking blocks
- Use the relevant thinking blocks necessary to preserve the model’s reasoning
- Only bill for the input tokens for the blocks shown to Claude

When Claude invokes tools, it is pausing its construction of a response to await external information. When tool results are returned, Claude will continue building that existing response. This necessitates preserving thinking blocks during tool use, for a couple of reasons:

1. **Reasoning continuity**: The thinking blocks capture Claude’s step-by-step reasoning that led to tool requests. When you post tool results, including the original thinking ensures Claude can continue its reasoning from where it left off.
2. **Context maintenance**: While tool results appear as user messages in the API structure, they’re part of a continuous reasoning flow. Preserving thinking blocks maintains this conceptual flow across multiple API calls. For more information on context management, see our [guide on context windows](https://docs.claude.com/en/docs/build-with-claude/context-windows).

**Important**: When providing `thinking` blocks, the entire sequence of consecutive `thinking` blocks must match the outputs generated by the model during the original request; you cannot rearrange or modify the sequence of these blocks.

### Interleaved thinking

Extended thinking with tool use in Claude 4 models supports interleaved thinking, which enables Claude to think between tool calls and make more sophisticated reasoning after receiving tool results.With interleaved thinking, Claude can:

- Reason about the results of a tool call before deciding what to do next
- Chain multiple tool calls with reasoning steps in between
- Make more nuanced decisions based on intermediate results

To enable interleaved thinking, add [the beta header](https://docs.claude.com/en/api/beta-headers) `interleaved-thinking-2025-05-14` to your API request.Here are some important considerations for interleaved thinking:

- With interleaved thinking, the `budget_tokens` can exceed the `max_tokens` parameter, as it represents the total budget across all thinking blocks within one assistant turn.
- Interleaved thinking is only supported for [tools used via the Messages API](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview).
- Interleaved thinking is supported for Claude 4 models only, with the beta header `interleaved-thinking-2025-05-14`.
- Direct calls to the Claude API allow you to pass `interleaved-thinking-2025-05-14` in requests to any model, with no effect.
- On 3rd-party platforms (e.g., [Amazon Bedrock](https://docs.claude.com/en/api/claude-on-amazon-bedrock) and [Vertex AI](https://docs.claude.com/en/api/claude-on-vertex-ai)), if you pass `interleaved-thinking-2025-05-14` to any model aside from Claude Opus 4.1, Opus 4, or Sonnet 4, your request will fail.

Tool use without interleaved thinking

Python

TypeScript

Java

```
import anthropic

client = anthropic.Anthropic()

# Define tools
calculator_tool = {
    "name": "calculator",
    "description": "Perform mathematical calculations",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "Mathematical expression to evaluate"
            }
        },
        "required": ["expression"]
    }
}

database_tool = {
    "name": "database_query",
    "description": "Query product database",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "SQL query to execute"
            }
        },
        "required": ["query"]
    }
}

# First request - Claude thinks once before all tool calls
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    tools=[calculator_tool, database_tool],
    messages=[{\
        "role": "user",\
        "content": "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"\
    }]
)

# Response includes thinking followed by tool uses
# Note: Claude thinks once at the beginning, then makes all tool decisions
print("First response:")
for block in response.content:
    if block.type == "thinking":
        print(f"Thinking (summarized): {block.thinking}")
    elif block.type == "tool_use":
        print(f"Tool use: {block.name} with input {block.input}")
    elif block.type == "text":
        print(f"Text: {block.text}")

# You would execute the tools and return results...
# After getting both tool results back, Claude directly responds without additional thinking

```

In this example without interleaved thinking:

1. Claude thinks once at the beginning to understand the task
2. Makes all tool use decisions upfront
3. When tool results are returned, Claude immediately provides a response without additional thinking

Tool use with interleaved thinking

Python

TypeScript

Java

```
import anthropic

client = anthropic.Anthropic()

# Same tool definitions as before
calculator_tool = {
    "name": "calculator",
    "description": "Perform mathematical calculations",
    "input_schema": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "Mathematical expression to evaluate"
            }
        },
        "required": ["expression"]
    }
}

database_tool = {
    "name": "database_query",
    "description": "Query product database",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "SQL query to execute"
            }
        },
        "required": ["query"]
    }
}

# First request with interleaved thinking enabled
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    tools=[calculator_tool, database_tool],
    betas=["interleaved-thinking-2025-05-14"],
    messages=[{\
        "role": "user",\
        "content": "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"\
    }]
)

print("Initial response:")
thinking_blocks = []
tool_use_blocks = []

for block in response.content:
    if block.type == "thinking":
        thinking_blocks.append(block)
        print(f"Thinking: {block.thinking}")
    elif block.type == "tool_use":
        tool_use_blocks.append(block)
        print(f"Tool use: {block.name} with input {block.input}")
    elif block.type == "text":
        print(f"Text: {block.text}")

# First tool result (calculator)
calculator_result = "7500"  # 150 * 50

# Continue with first tool result
response2 = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    tools=[calculator_tool, database_tool],
    betas=["interleaved-thinking-2025-05-14"],
    messages=[\
        {\
            "role": "user",\
            "content": "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"\
        },\
        {\
            "role": "assistant",\
            "content": [thinking_blocks[0], tool_use_blocks[0]]\
        },\
        {\
            "role": "user",\
            "content": [{\
                "type": "tool_result",\
                "tool_use_id": tool_use_blocks[0].id,\
                "content": calculator_result\
            }]\
        }\
    ]
)

print("\nAfter calculator result:")
# With interleaved thinking, Claude can think about the calculator result
# before deciding to query the database
for block in response2.content:
    if block.type == "thinking":
        thinking_blocks.append(block)
        print(f"Interleaved thinking: {block.thinking}")
    elif block.type == "tool_use":
        tool_use_blocks.append(block)
        print(f"Tool use: {block.name} with input {block.input}")

# Second tool result (database)
database_result = "5200"  # Example average monthly revenue

# Continue with second tool result
response3 = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    tools=[calculator_tool, database_tool],
    betas=["interleaved-thinking-2025-05-14"],
    messages=[\
        {\
            "role": "user",\
            "content": "What's the total revenue if we sold 150 units of product A at $50 each, and how does this compare to our average monthly revenue from the database?"\
        },\
        {\
            "role": "assistant",\
            "content": [thinking_blocks[0], tool_use_blocks[0]]\
        },\
        {\
            "role": "user",\
            "content": [{\
                "type": "tool_result",\
                "tool_use_id": tool_use_blocks[0].id,\
                "content": calculator_result\
            }]\
        },\
        {\
            "role": "assistant",\
            "content": thinking_blocks[1:] + tool_use_blocks[1:]\
        },\
        {\
            "role": "user",\
            "content": [{\
                "type": "tool_result",\
                "tool_use_id": tool_use_blocks[1].id,\
                "content": database_result\
            }]\
        }\
    ]
)

print("\nAfter database result:")
# With interleaved thinking, Claude can think about both results
# before formulating the final response
for block in response3.content:
    if block.type == "thinking":
        print(f"Final thinking: {block.thinking}")
    elif block.type == "text":
        print(f"Final response: {block.text}")

```

In this example with interleaved thinking:

1. Claude thinks about the task initially
2. After receiving the calculator result, Claude can think again about what that result means
3. Claude then decides how to query the database based on the first result
4. After receiving the database result, Claude thinks once more about both results before formulating a final response
5. The thinking budget is distributed across all thinking blocks within the turn

This pattern allows for more sophisticated reasoning chains where each tool’s output informs the next decision.

## Extended thinking with prompt caching

[Prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching) with thinking has several important considerations:

Extended thinking tasks often take longer than 5 minutes to complete. Consider using the [1-hour cache duration](https://docs.claude.com/en/docs/build-with-claude/prompt-caching#1-hour-cache-duration) to maintain cache hits across longer thinking sessions and multi-step workflows.

**Thinking block context removal**

- Thinking blocks from previous turns are removed from context, which can affect cache breakpoints
- When continuing conversations with tool use, thinking blocks are cached and count as input tokens when read from cache
- This creates a tradeoff: while thinking blocks don’t consume context window space visually, they still count toward your input token usage when cached
- If thinking becomes disabled, requests will fail if you pass thinking content in the current tool use turn. In other contexts, thinking content passed to the API is simply ignored

**Cache invalidation patterns**

- Changes to thinking parameters (enabled/disabled or budget allocation) invalidate message cache breakpoints
- [Interleaved thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking) amplifies cache invalidation, as thinking blocks can occur between multiple [tool calls](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#extended-thinking-with-tool-use)
- System prompts and tools remain cached despite thinking parameter changes or block removal

While thinking blocks are removed for caching and context calculations, they must be preserved when continuing conversations with [tool use](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#extended-thinking-with-tool-use), especially with [interleaved thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking).

### Understanding thinking block caching behavior

When using extended thinking with tool use, thinking blocks exhibit specific caching behavior that affects token counting:**How it works:**

1. Caching only occurs when you make a subsequent request that includes tool results
2. When the subsequent request is made, the previous conversation history (including thinking blocks) can be cached
3. These cached thinking blocks count as input tokens in your usage metrics when read from the cache
4. When a non-tool-result user block is included, all previous thinking blocks are ignored and stripped from context

**Detailed example flow:****Request 1:**

```
User: "What's the weather in Paris?"

```

**Response 1:**

```
[thinking_block_1] + [tool_use block 1]

```

**Request 2:**

```
User: ["What's the weather in Paris?"],
Assistant: [thinking_block_1] + [tool_use block 1],
User: [tool_result_1, cache=True]

```

**Response 2:**

```
[thinking_block_2] + [text block 2]

```

Request 2 writes a cache of the request content (not the response). The cache includes the original user message, the first thinking block, tool use block, and the tool result.**Request 3:**

```
User: ["What's the weather in Paris?"],
Assistant: [thinking_block_1] + [tool_use block 1],
User: [tool_result_1, cache=True],
Assistant: [thinking_block_2] + [text block 2],
User: [Text response, cache=True]

```

Because a non-tool-result user block was included, all previous thinking blocks are ignored. This request will be processed the same as:

```
User: ["What's the weather in Paris?"],
Assistant: [tool_use block 1],
User: [tool_result_1, cache=True],
Assistant: [text block 2],
User: [Text response, cache=True]

```

**Key points:**

- This caching behavior happens automatically, even without explicit `cache_control` markers
- This behavior is consistent whether using regular thinking or interleaved thinking

System prompt caching (preserved when thinking changes)

Python

TypeScript

```
from anthropic import Anthropic
import requests
from bs4 import BeautifulSoup

client = Anthropic()

def fetch_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Get text
    text = soup.get_text()

    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

# Fetch the content of the article
book_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
book_content = fetch_article_content(book_url)
# Use just enough text for caching (first few chapters)
LARGE_TEXT = book_content[:5000]

SYSTEM_PROMPT=[\
    {\
        "type": "text",\
        "text": "You are an AI assistant that is tasked with literary analysis. Analyze the following text carefully.",\
    },\
    {\
        "type": "text",\
        "text": LARGE_TEXT,\
        "cache_control": {"type": "ephemeral"}\
    }\
]

MESSAGES = [\
    {\
        "role": "user",\
        "content": "Analyze the tone of this passage."\
    }\
]

# First request - establish cache
print("First request - establishing cache")
response1 = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=20000,
    thinking={
        "type": "enabled",
        "budget_tokens": 4000
    },
    system=SYSTEM_PROMPT,
    messages=MESSAGES
)

print(f"First response usage: {response1.usage}")

MESSAGES.append({
    "role": "assistant",
    "content": response1.content
})
MESSAGES.append({
    "role": "user",
    "content": "Analyze the characters in this passage."
})
# Second request - same thinking parameters (cache hit expected)
print("\nSecond request - same thinking parameters (cache hit expected)")
response2 = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=20000,
    thinking={
        "type": "enabled",
        "budget_tokens": 4000
    },
    system=SYSTEM_PROMPT,
    messages=MESSAGES
)

print(f"Second response usage: {response2.usage}")

# Third request - different thinking parameters (cache miss for messages)
print("\nThird request - different thinking parameters (cache miss for messages)")
response3 = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=20000,
    thinking={
        "type": "enabled",
        "budget_tokens": 8000  # Changed thinking budget
    },
    system=SYSTEM_PROMPT,  # System prompt remains cached
    messages=MESSAGES  # Messages cache is invalidated
)

print(f"Third response usage: {response3.usage}")

```

Messages caching (invalidated when thinking changes)

Python

TypeScript

Java

```
from anthropic import Anthropic
import requests
from bs4 import BeautifulSoup

client = Anthropic()

def fetch_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Get text
    text = soup.get_text()

    # Break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

# Fetch the content of the article
book_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
book_content = fetch_article_content(book_url)
# Use just enough text for caching (first few chapters)
LARGE_TEXT = book_content[:5000]

# No system prompt - caching in messages instead
MESSAGES = [\
    {\
        "role": "user",\
        "content": [\
            {\
                "type": "text",\
                "text": LARGE_TEXT,\
                "cache_control": {"type": "ephemeral"},\
            },\
            {\
                "type": "text",\
                "text": "Analyze the tone of this passage."\
            }\
        ]\
    }\
]

# First request - establish cache
print("First request - establishing cache")
response1 = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=20000,
    thinking={
        "type": "enabled",
        "budget_tokens": 4000
    },
    messages=MESSAGES
)

print(f"First response usage: {response1.usage}")

MESSAGES.append({
    "role": "assistant",
    "content": response1.content
})
MESSAGES.append({
    "role": "user",
    "content": "Analyze the characters in this passage."
})
# Second request - same thinking parameters (cache hit expected)
print("\nSecond request - same thinking parameters (cache hit expected)")
response2 = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=20000,
    thinking={
        "type": "enabled",
        "budget_tokens": 4000  # Same thinking budget
    },
    messages=MESSAGES
)

print(f"Second response usage: {response2.usage}")

MESSAGES.append({
    "role": "assistant",
    "content": response2.content
})
MESSAGES.append({
    "role": "user",
    "content": "Analyze the setting in this passage."
})

# Third request - different thinking budget (cache miss expected)
print("\nThird request - different thinking budget (cache miss expected)")
response3 = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=20000,
    thinking={
        "type": "enabled",
        "budget_tokens": 8000  # Different thinking budget breaks cache
    },
    messages=MESSAGES
)

print(f"Third response usage: {response3.usage}")

```

Here is the output of the script (you may see slightly different numbers)

```
First request - establishing cache
First response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 17, output_tokens: 700 }

Second request - same thinking parameters (cache hit expected)

Second response usage: { cache_creation_input_tokens: 0, cache_read_input_tokens: 1370, input_tokens: 303, output_tokens: 874 }

Third request - different thinking budget (cache miss expected)
Third response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 747, output_tokens: 619 }

```

This example demonstrates that when caching is set up in the messages array, changing the thinking parameters (budget\_tokens increased from 4000 to 8000) **invalidates the cache**. The third request shows no cache hit with `cache_creation_input_tokens=1370` and `cache_read_input_tokens=0`, proving that message-based caching is invalidated when thinking parameters change.

## Max tokens and context window size with extended thinking

In older Claude models (prior to Claude Sonnet 3.7), if the sum of prompt tokens and `max_tokens` exceeded the model’s context window, the system would automatically adjust `max_tokens` to fit within the context limit. This meant you could set a large `max_tokens` value and the system would silently reduce it as needed.With Claude 3.7 and 4 models, `max_tokens` (which includes your thinking budget when thinking is enabled) is enforced as a strict limit. The system will now return a validation error if prompt tokens + `max_tokens` exceeds the context window size.

You can read through our [guide on context windows](https://docs.claude.com/en/docs/build-with-claude/context-windows) for a more thorough deep dive.

### The context window with extended thinking

When calculating context window usage with thinking enabled, there are some considerations to be aware of:

- Thinking blocks from previous turns are stripped and not counted towards your context window
- Current turn thinking counts towards your `max_tokens` limit for that turn

The diagram below demonstrates the specialized token management when extended thinking is enabled:https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=3ad289c01610a87c8ec1214faa09578dThe effective context window is calculated as:

```
context window =
  (current input tokens - previous thinking tokens) +
  (thinking tokens + encrypted thinking tokens + text output tokens)

```

We recommend using the [token counting API](https://docs.claude.com/en/docs/build-with-claude/token-counting) to get accurate token counts for your specific use case, especially when working with multi-turn conversations that include thinking.

### The context window with extended thinking and tool use

When using extended thinking with tool use, thinking blocks must be explicitly preserved and returned with the tool results.The effective context window calculation for extended thinking with tool use becomes:

```
context window =
  (current input tokens + previous thinking tokens + tool use tokens) +
  (thinking tokens + encrypted thinking tokens + text output tokens)

```

The diagram below illustrates token management for extended thinking with tool use:https://mintcdn.com/anthropic-claude-docs/LF5WV0SNF6oudpT5/images/context-window-thinking-tools.svg?fit=max&auto=format&n=LF5WV0SNF6oudpT5&q=85&s=557310c0bf57d88b7a6e550abd35bc75

### Managing tokens with extended thinking

Given the context window and `max_tokens` behavior with extended thinking Claude 3.7 and 4 models, you may need to:

- More actively monitor and manage your token usage
- Adjust `max_tokens` values as your prompt length changes
- Potentially use the [token counting endpoints](https://docs.claude.com/en/docs/build-with-claude/token-counting) more frequently
- Be aware that previous thinking blocks don’t accumulate in your context window

This change has been made to provide more predictable and transparent behavior, especially as maximum token limits have increased significantly.

## Thinking encryption

Full thinking content is encrypted and returned in the `signature` field. This field is used to verify that thinking blocks were generated by Claude when passed back to the API.

It is only strictly necessary to send back thinking blocks when using [tools with extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#extended-thinking-with-tool-use). Otherwise you can omit thinking blocks from previous turns, or let the API strip them for you if you pass them back.If sending back thinking blocks, we recommend passing everything back as you received it for consistency and to avoid potential issues.

Here are some important considerations on thinking encryption:

- When [streaming responses](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#streaming-thinking), the signature is added via a `signature_delta` inside a `content_block_delta` event just before the `content_block_stop` event.
- `signature` values are significantly longer in Claude 4 models than in previous models.
- The `signature` field is an opaque field and should not be interpreted or parsed - it exists solely for verification purposes.
- `signature` values are compatible across platforms (Claude APIs, [Amazon Bedrock](https://docs.claude.com/en/api/claude-on-amazon-bedrock), and [Vertex AI](https://docs.claude.com/en/api/claude-on-vertex-ai)). Values generated on one platform will be compatible with another.

### Thinking redaction

Occasionally Claude’s internal reasoning will be flagged by our safety systems. When this occurs, we encrypt some or all of the `thinking` block and return it to you as a `redacted_thinking` block. `redacted_thinking` blocks are decrypted when passed back to the API, allowing Claude to continue its response without losing context.When building customer-facing applications that use extended thinking:

- Be aware that redacted thinking blocks contain encrypted content that isn’t human-readable
- Consider providing a simple explanation like: “Some of Claude’s internal reasoning has been automatically encrypted for safety reasons. This doesn’t affect the quality of responses.”
- If showing thinking blocks to users, you can filter out redacted blocks while preserving normal thinking blocks
- Be transparent that using extended thinking features may occasionally result in some reasoning being encrypted
- Implement appropriate error handling to gracefully manage redacted thinking without breaking your UI

Here’s an example showing both normal and redacted thinking blocks:

```
{
  "content": [\
    {\
      "type": "thinking",\
      "thinking": "Let me analyze this step by step...",\
      "signature": "WaUjzkypQ2mUEVM36O2TxuC06KN8xyfbJwyem2dw3URve/op91XWHOEBLLqIOMfFG/UvLEczmEsUjavL...."\
    },\
    {\
      "type": "redacted_thinking",\
      "data": "EmwKAhgBEgy3va3pzix/LafPsn4aDFIT2Xlxh0L5L8rLVyIwxtE3rAFBa8cr3qpPkNRj2YfWXGmKDxH4mPnZ5sQ7vB9URj2pLmN3kF8/dW5hR7xJ0aP1oLs9yTcMnKVf2wRpEGjH9XZaBt4UvDcPrQ..."\
    },\
    {\
      "type": "text",\
      "text": "Based on my analysis..."\
    }\
  ]
}

```

Seeing redacted thinking blocks in your output is expected behavior. The model can still use this redacted reasoning to inform its responses while maintaining safety guardrails.If you need to test redacted thinking handling in your application, you can use this special test string as your prompt: `ANTHROPIC_MAGIC_STRING_TRIGGER_REDACTED_THINKING_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB`

When passing `thinking` and `redacted_thinking` blocks back to the API in a multi-turn conversation, you must include the complete unmodified block back to the API for the last assistant turn. This is critical for maintaining the model’s reasoning flow. We suggest always passing back all thinking blocks to the API. For more details, see the [Preserving thinking blocks](https://docs.claude.com/en/docs/build-with-claude/extended-thinking#preserving-thinking-blocks) section above.

Example: Working with redacted thinking blocks

This example demonstrates how to handle `redacted_thinking` blocks that may appear in responses when Claude’s internal reasoning contains content flagged by safety systems:

Python

TypeScript

Java

```
import anthropic

client = anthropic.Anthropic()

# Using a special prompt that triggers redacted thinking (for demonstration purposes only)
response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[{\
        "role": "user",\
        "content": "ANTHROPIC_MAGIC_STRING_TRIGGER_REDACTED_THINKING_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB"\
    }]
)

# Identify redacted thinking blocks
has_redacted_thinking = any(
    block.type == "redacted_thinking" for block in response.content
)

if has_redacted_thinking:
    print("Response contains redacted thinking blocks")
    # These blocks are still usable in subsequent requests

    # Extract all blocks (both redacted and non-redacted)
    all_thinking_blocks = [\
        block for block in response.content\
        if block.type in ["thinking", "redacted_thinking"]\
    ]

    # When passing to subsequent requests, include all blocks without modification
    # This preserves the integrity of Claude's reasoning

    print(f"Found {len(all_thinking_blocks)} thinking blocks total")
    print(f"These blocks are still billable as output tokens")

```

## Differences in thinking across model versions

The Messages API handles thinking differently across Claude Sonnet 3.7 and Claude 4 models, primarily in redaction and summarization behavior.See the table below for a condensed comparison:

| Feature | Claude Sonnet 3.7 | Claude 4 Models |
| --- | --- | --- |
| **Thinking Output** | Returns full thinking output | Returns summarized thinking |
| **Interleaved Thinking** | Not supported | Supported with `interleaved-thinking-2025-05-14` beta header |

## Pricing

Extended thinking uses the standard token pricing scheme:

| Model | Base Input Tokens | Cache Writes | Cache Hits | Output Tokens |
| --- | --- | --- | --- | --- |
| Claude Opus 4.1 | $15 / MTok | $18.75 / MTok | $1.50 / MTok | $75 / MTok |
| Claude Opus 4 | $15 / MTok | $18.75 / MTok | $1.50 / MTok | $75 / MTok |
| Claude Sonnet 4.5 | $3 / MTok | $3.75 / MTok | $0.30 / MTok | $15 / MTok |
| Claude Sonnet 4 | $3 / MTok | $3.75 / MTok | $0.30 / MTok | $15 / MTok |
| Claude Sonnet 3.7 | $3 / MTok | $3.75 / MTok | $0.30 / MTok | $15 / MTok |

The thinking process incurs charges for:

- Tokens used during thinking (output tokens)
- Thinking blocks from the last assistant turn included in subsequent requests (input tokens)
- Standard text output tokens

When extended thinking is enabled, a specialized system prompt is automatically included to support this feature.

When using summarized thinking:

- **Input tokens**: Tokens in your original request (excludes thinking tokens from previous turns)
- **Output tokens (billed)**: The original thinking tokens that Claude generated internally
- **Output tokens (visible)**: The summarized thinking tokens you see in the response
- **No charge**: Tokens used to generate the summary

The billed output token count will **not** match the visible token count in the response. You are billed for the full thinking process, not the summary you see.

## Best practices and considerations for extended thinking

### Working with thinking budgets

- **Budget optimization:** The minimum budget is 1,024 tokens. We suggest starting at the minimum and increasing the thinking budget incrementally to find the optimal range for your use case. Higher token counts enable more comprehensive reasoning but with diminishing returns depending on the task. Increasing the budget can improve response quality at the tradeoff of increased latency. For critical tasks, test different settings to find the optimal balance. Note that the thinking budget is a target rather than a strict limit—actual token usage may vary based on the task.
- **Starting points:** Start with larger thinking budgets (16k+ tokens) for complex tasks and adjust based on your needs.
- **Large budgets:** For thinking budgets above 32k, we recommend using [batch processing](https://docs.claude.com/en/docs/build-with-claude/batch-processing) to avoid networking issues. Requests pushing the model to think above 32k tokens causes long running requests that might run up against system timeouts and open connection limits.
- **Token usage tracking:** Monitor thinking token usage to optimize costs and performance.

### Performance considerations

- **Response times:** Be prepared for potentially longer response times due to the additional processing required for the reasoning process. Factor in that generating thinking blocks may increase overall response time.
- **Streaming requirements:** Streaming is required when `max_tokens` is greater than 21,333. When streaming, be prepared to handle both thinking and text content blocks as they arrive.

### Feature compatibility

- Thinking isn’t compatible with `temperature` or `top_k` modifications as well as [forced tool use](https://docs.claude.com/en/docs/agents-and-tools/tool-use/implement-tool-use#forcing-tool-use).
- When thinking is enabled, you can set `top_p` to values between 1 and 0.95.
- You cannot pre-fill responses when thinking is enabled.
- Changes to the thinking budget invalidate cached prompt prefixes that include messages. However, cached system prompts and tool definitions will continue to work when thinking parameters change.

### Usage guidelines

- **Task selection:** Use extended thinking for particularly complex tasks that benefit from step-by-step reasoning like math, coding, and analysis.
- **Context handling:** You do not need to remove previous thinking blocks yourself. The Claude API automatically ignores thinking blocks from previous turns and they are not included when calculating context usage.
- **Prompt engineering:** Review our [extended thinking prompting tips](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips) if you want to maximize Claude’s thinking capabilities.

</details>

<details>
<summary>gemini-deep-research-your-personal-research-assistant</summary>

## What is Deep Research

Get up to speed on just about anything with Deep Research, an agentic feature in Gemini that can automatically browse up to hundreds of websites on your behalf, think through its findings, and create insightful multi-page reports in minutes.

With the Gemini 2.5 model, Deep Research is even better at all stages of research, from planning to delivering even more insightful and detailed reports.

### Planning

Deep Research transforms your prompt into a personalized multi-point research plan

### Searching

Deep Research autonomously searches and deeply browses the web to find relevant, up-to-date information

### Reasoning

Deep Research shows its thoughts as it reasons over information gathered iteratively and thinks before making its next move

### Reporting

Deep Research provides comprehensive custom research reports with more detail and insights, generated in minutes and available as an Audio Overview, saving you hours of time

## How to use Deep Research

Gemini Deep Research is designed to tackle your complex research tasks by breaking them down, exploring the web to find answers, and synthesizing findings into comprehensive results.

Now, you can upload your own files to Deep Research, and make your reports even more immersive by turning them into interactive content, quizzes, Audio Overviews, and more in Canvas.

### Competitive analysis

Understanding the landscape of competitors for a new product, including offerings, pricing, marketing and customer feedback.

### Due diligence

Investigating a potential sales lead, analyzing a company's products, funding history, team and competitive environment.

### Topic understanding

Diving deep into subjects by comparing and contrasting key concepts, identifying relationships between ideas and explaining underlying principles.

### Product comparison

Evaluating different models of an appliance based on features, performance, price and customer reviews.

It’s a step towards more agentic AI that can move beyond simple question-answering to become a true collaborative partner capable of sophisticated thinking and execution.

## How we built the first Deep Research

The day after we pioneered the Deep Research product category on Gemini in December 2024, we gathered some of the team behind the product for a discussion.

### An agentic system

To build Deep Research, we developed a new planning system that enables Gemini app to work through complex problems. For Deep Research, we trained Gemini models to be capable of:

- **Breaking down the problem:** When presented with a complex user query, the system first formulates a detailed research plan, breaking the problem into a series of smaller, manageable sub-tasks. You’re in control of the plan: Gemini presents it to you, and you can refine it to make sure it’s focused on the right areas.

- **Research**: The model oversees the execution of this plan, and intelligently determines which sub-tasks can be tackled simultaneously and which need to be done sequentially. The model can use tools like search and web browsing to fetch information & reason over it. At each step the model reasons over information available to decide its next move. We introduced a thinking panel for users to follow what the model has learnt so far & what it intends to do next.

- **Synthesis:** Once the model determines enough information has been gathered, it synthesizes the findings into a comprehensive report. In building the report, Gemini critically evaluates the information, identifies key themes and inconsistencies, and structures the report in a logical and informative way, even performing multiple passes of self-critique to enhance clarity and detail.


### New category, new problems, new solutions

In building Deep Research, we had to work through three significant technical challenges:

#### Multi-step planning

Research tasks require multiple steps of iterative planning. At each step, the model has to ground itself on all information gathered so far, then identify missing information and discrepancies it wants to explore — all while trading off comprehensiveness with compute and user wait time. Training the model to be effective at long multi-step planning in a data efficient manner enabled us to make Deep Research function in an open domain setting across all topics.

#### Long-running inference

A typical Deep Research task involves many model calls over several minutes. This creates a challenge for building agents: It has to be built so that a single failure doesn’t mean having to restart the task from the beginning.

To address this, we developed a novel asynchronous task manager that maintains a shared state between the planner and task models, allowing for graceful error recovery without restarting the entire task. This system is truly asynchronous: you can hop to a different app or quite literally turn off your computer after starting a Deep Research project and the next time you visit Gemini, you’ll get notified when your research is done.

#### Context management

Over the course of a research session, Gemini can process hundreds of pages of content. To maintain continuity and enable follow-up questions, we use Gemini’s industry-leading 1 million token context window complemented with a RAG setup. This effectively allows the system to "remember" everything it has learned during that chat session, making it smarter the longer you interact with it.

### Evolving with new models

When Deep Research launched in December it was powered by Gemini 1.5 Pro. With the introduction of Gemini 2.0 Flash Thinking (experimental) we were able to dramatically improve both the quality and serving efficiency of this product. With thinking models, Gemini takes more time to plan out its approach before it makes its next steps. This innate characteristic of self-reflection and planning makes it a great fit for these kinds of long running agentic tasks. What we see is that now Gemini is even better at all stages of research and delivers more detailed reports. At the same time, the compute-efficiency of the Flash model allows us to expand access to Deep Research to far more users. We’re really excited about developing on flash and thinking models in general and expect deep research to keep getting better and better.

And with our most capable model, Gemini 2.5, Deep Research is even better at all stages of research, delivering even more insightful and detailed reports

### What’s next

We built the system to be versatile, so over time we can expand its capabilities by giving you more control over what it can browse and giving it sources beyond the open web.

We are excited to see how people use Deep Research, and these real-world experiences will inform how we continue to build and improve Deep Research. Ultimately, our goal is a truly agentic and universally helpful AI assistant.

</details>

<details>
<summary>introducing-openai-o3-and-o4-mini-openai</summary>

Today, we’re releasing OpenAI **o3** and **o4-mini,** the latest in our o-series of models trained to think for longer before responding. These are the smartest models we’ve released to date, representing a step change in ChatGPT's capabilities for everyone from curious users to advanced researchers. For the first time, our reasoning models can agentically use and combine every tool within ChatGPT—this includes searching the web, analyzing uploaded files and other data with Python, reasoning deeply about visual inputs, and even generating images. Critically, these models are trained to reason about when and how to use tools to produce detailed and thoughtful answers in the right output formats, typically in under a minute, to solve more complex problems. This allows them to tackle multi-faceted questions more effectively, a step toward a more agentic ChatGPT that can independently execute tasks on your behalf. The combined power of state-of-the-art reasoning with full tool access translates into significantly stronger performance across academic benchmarks and real-world tasks, setting a new standard in both intelligence and usefulness.

## What’s changed

**OpenAI o3** is our most powerful reasoning model that pushes the frontier across **coding, math, science, visual perception**, and more. It sets a new SOTA on benchmarks including Codeforces, SWE-bench (without building a custom model-specific scaffold), and MMMU. It’s ideal for complex queries requiring multi-faceted analysis and whose answers may not be immediately obvious. It performs especially strongly at visual tasks like analyzing images, charts, and graphics. In evaluations by external experts, o3 makes 20 percent fewer major errors than OpenAI o1 on difficult, real-world tasks—especially excelling in areas like programming, business/consulting, and creative ideation. Early testers highlighted its analytical rigor as a thought partner and emphasized its ability to generate and critically evaluate novel hypotheses—particularly within biology, math, and engineering contexts.

**OpenAI o4-mini** is a smaller model optimized for fast, cost-efficient reasoning—it achieves remarkable performance for its size and cost, particularly in **math, coding, and visual tasks**. It is the best-performing benchmarked model on AIME 2024 and 2025. Although access to a computer meaningfully reduces the difficulty of the AIME exam, we also found it notable that o4-mini achieves 99.5% pass@1 (100% consensus@8) on AIME 2025 when given access to a Python interpreter. While these results should not be compared to the performance of models without tool access, they are one example of how effectively o4-mini leverages available tools; o3 shows similar improvements on AIME 2025 from tool use (98.4% pass@1, 100% consensus@8).

In expert evaluations, o4-mini also outperforms its predecessor, o3‑mini, on non-STEM tasks as well as domains like data science. Thanks to its efficiency, o4-mini supports significantly higher usage limits than o3, making it a strong high-volume, high-throughput option for questions that benefit from reasoning. External expert evaluators rated **both models** as demonstrating improved instruction following and more useful, verifiable responses than their predecessors, thanks to improved intelligence and the inclusion of web sources. Compared to previous iterations of our reasoning models, these two models should also feel more natural and conversational, especially as they reference memory and past conversations to make responses more personalized and relevant.

o1o3-minio3 (no tools)o4-mini (no tools)Accuracy (%)74.387.391.693.4AIME 2024Competition Math

o1o3-minio3 (no tools)o4-mini (no tools)Accuracy (%)79.286.588.992.7AIME 2025Competition Math

o1o3-minio3 (with terminal)o4-mini (with terminal)ELO1891207327062719CodeforcesCompetition Code

o1o3-minio3 (no tools)o4-mini (no tools)Accuracy (%)78.077.083.381.4GPQA DiamondPhD-Level Science Questions

o1-proo3-minio3 (no tools)o3 (python + browsing\*\*tools)o4-mini (no tools)o4-mini (with python +browsing\*\* tools)Deep researchAccuracy (%)8.1213.4020.3224.9014.2817.7026.60Humanity’s Last ExamExpert-Level Questions Across Subjects

### Multimodal

o1o3o4-miniAccuracy (%)77.682.981.6MMMUCollege-level visual problem-solving

o1o3o4-miniAccuracy (%)71.886.884.3MathVistaVisual Math Reasoning

o1o3o4-miniAccuracy (%)55.178.672.0CharXiv-ReasoningScientific Figure Reasoning

### Coding

o1-higho3-mini-higho3-higho4-mini-high050000100000150000Dollars earned$43,958$33,833$86,100$65,792SWE-Lancer: IC SWE DiamondFreelance Coding Tasks

o1o3-minio3o4-miniAccuracy (%)48.949.369.168.1SWE-Bench Verified (n=477)Software Engineering

_All SWE-bench evaluation runs use a fixed subset of n=477 verified tasks which have been validated on our internal infrastructure._

o1-higho3-mini-higho3-higho4-mini-highAccuracy (%)64.4%(whole)61.7%(diff)66.7%(whole)60.4%(diff)81.3%(whole)79.6%(diff)68.9%(whole)58.2%(diff)Aider PolyglotCode Editing

### Instruction following and agentic tool use

o1o3-minio3o4-miniAccuracy (%)44.9339.8956.5142.99Scale MultiChallengeMulti-turn instruction following

4o + browsingo3 with python +browsing\*o4-mini with python +browsing\*\*Deep researchAccuracy (%)1.949.728.351.5BrowseCompAgentic Browsing

o1-higho3-mini-higho3-higho4-mini-highAccuracy (%)50.0%(Airline)70.8%(Retail)32.4%(Airline)57.6%(Retail)52.0%(Airline)73.9%(Retail)49.2%(Airline)71.8%(Retail)70.4%65.6%Tau-benchFunction Calling

_All models are evaluated at high ‘reasoning effort’ settings—similar to variants like ‘o4-mini-high’ in ChatGPT._

## Continuing to scale reinforcement learning

Throughout the development of OpenAI o3, we’ve observed that large-scale reinforcement learning exhibits the same **“more compute = better performance**” trend observed in GPT‑series pretraining. By retracing the scaling path—this time in RL—we’ve pushed an additional order of magnitude in both training compute and inference-time reasoning, yet still see clear performance gains, validating that the models’ performance continues to improve the more they’re allowed to think. At equal latency and cost with OpenAI o1, o3 delivers higher performance in ChatGPT—and we've validated that if we let it think longer, its performance keeps climbing.

We also trained both models to **use tools through reinforcement learning**—teaching them not just how to use tools, but to reason about when to use them. Their ability to deploy tools based on desired outcomes makes them more capable in open-ended situations—particularly those involving visual reasoning and multi-step workflows. This improvement is reflected both in academic benchmarks and real-world tasks, as reported by early testers.

## Thinking with imageshttps://images.ctfassets.net/kftzwdyauwt9/5xCw1KgHHs0BQI0Fz1bOLM/1ca4ddcca658fddd65815dd3aa288773/thinking_with_images_static.png?w=3840&q=90&fm=webp

For the first time, these models can integrate images directly into their chain of thought. They don’t just see an image—they think with it. This unlocks a new class of problem-solving that blends visual and textual reasoning, reflected in their state-of-the-art performance across multimodal benchmarks.

People can upload a photo of a whiteboard, a textbook diagram, or a hand-drawn sketch, and the model can interpret it—even if the image is blurry, reversed, or low quality. With tool use, the models can manipulate images on the fly—rotating, zooming, or transforming them as part of their reasoning process.

These models deliver best-in-class accuracy on visual perception tasks, enabling it to solve questions that were previously out of reach. Check out the [visual reasoning research blog⁠](https://openai.com/index/thinking-with-images/) to learn more.

## Toward agentic tool use

OpenAI o3 and o4-mini have full access to tools within ChatGPT, as well as your own custom tools via function calling in the API. These models are trained to reason about how to solve problems, choosing when and how to use tools to produce detailed and thoughtful answers in the right output formats quickly—typically in under a minute.

For example, a user might ask: “How will summer energy usage in California compare to last year?” The model can search the web for public utility data, write Python code to build a forecast, generate a graph or image, and explain the key factors behind the prediction, chaining together multiple tool calls. Reasoning allows the models to react and pivot as needed to information it encounters. For example, they can search the web multiple times with the help of search providers, look at results, and try new searches if they need more info.

This flexible, strategic approach allows the models to tackle tasks that require access to up-to-date information beyond the model’s built-in knowledge, extended reasoning, synthesis, and output generation across modalities.

_All examples were completed with OpenAI o3._

## OpenAI o3

Solve the following very hard math problem using your in-built knowledge of the literature:

Construct a degree 19 polynomial \ (p(x)) \ in \ mathbb{C}\[x\] such that \ (X := \ {\\, p(x) = p(y) \\, \\} \ subset \ mathbb{P}^{1} \ times \ mathbb{P}^{1}\ ) has at least 3 (but not all linear) irreducible components over \ mathbb{C}. Choose \ (p(x)\ ) to be odd, monic, have real coefficients and linear coefficient \ (-19\ ) and calculate \ (p(19)\ ).

Reasoned about polynomial construction for 55 seconds

- The curve defined by p(x) = p(y) factors if p(x) is decomposable or has repeated factors. Actually, p(x)-p(y) always factors, and it’s divisible by (x-y). This gives one factor, and the rest is a degree d-1 polynomial in x and y. For the curve to have at least three irreducible components, p(x)-p(y) must factor into at least three nontrivial factors. Each factor corresponds to a component in projective space, and at least one must be nonlinear.
- I’m checking the Dickson polynomials D\_n(x,a) and focusing on their coefficients. With a=1, it seems the leading coefficient is always 1, confirming that Dickson polynomials are monic. The linear coefficient for odd n is following a predictable sign pattern: for n=19, it gives a coefficient of -19, which is exactly what I need. So the Dickson polynomial D\_n(x,1) with odd n fits nicely with the linear coefficient I was looking for.
- I've confirmed that the linear coefficient for p(x)=D19(x)p(x) = D\_{19}(x)p(x)=D19​(x) is correct, with the necessary scaling factor to match. Now for the next step, I need to compute D19(19)D\_{19}(19)D19​(19). Since Tn(z)T\_n(z)Tn​(z) grows quickly for real z>1z > 1z>1, I plan to compute this value using Python, leveraging the recurrence to avoid mistakes—it's going to be a big number. I'll make sure to present the numeric result neatly so it's understandable since the coefficients are integers.
- The Dickson polynomial D\_{19}(x,1) is confirmed to have the required properties: monic, odd, real coefficients, and a linear coefficient of -19. The factorization of D\_{19}(x) into irreducible components is also verified and satisfies the condition of having at least 10 components (1 linear + 9 quadratics). To compute p(19), we'll use the recurrence relation for Dickson polynomials, but there's also a closed-form expression involving cosine that could be handy here. I'll proceed accordingly!
- I confirmed the linear coefficient is working correctly, which means now I need to calculate p(19)=D19(19)p(19) = D\_{19}(19)p(19)=D19​(19). This involves evaluating T19(9.5)T\_{19}(9.5)T19​(9.5), which grows rapidly. To ensure I get an accurate result, I'll compute this using recurrence in Python. The result is a large number: 1,876,572,071,974,094,803,391,179. I'll use the commas to make it easier to read: p(19)=1,876,572,071,974,094,803,391,179p(19) = 1,876,572,071,974,094,803,391,179p(19)=1,876,572,071,974,094,803,391,179.
- For a = 1, there’s a relationship between Dickson polynomials and Chebyshev polynomials: D\_n(x, 1) = 2^(n-1) T\_n(x/2). Checking this, we see that the definition of D\_n(u + 1/u) aligns well with Chebyshev’s formula. By setting x = 2 cos(θ), we find that D\_n(x) equals 2 T\_n(x/2). Importantly, the leading coefficient works out to 1, confirming the identity holds. This is nice!
- Now, I need to verify that p(x)−p(y)p(x) - p(y)p(x)−p(y) factors as desired, relying on the known Dickson polynomial factorization. According to the literature (like Fried and Jarden), the difference Dn(x)−Dn(y)D\_n(x) - D\_n(y)Dn​(x)−Dn​(y) factors into a product involving (x−y)(x - y)(x−y) and other expressions. I'll provide the explicit polynomial D19(x,1)D\_{19}(x, 1)D19​(x,1), list the coefficients, and explain how it satisfies the desired properties: monic, odd, etc. Lastly, I'll compute p(19)p(19)p(19).

Done

A convenient way to force many factors in

p(x)−p(y)p(x) \\;-\\; p(y)p(x)−p(y) is to use a **Dickson polynomial** of the first kind.

For a parameter a∈Ca \\in \\mathbb{C}a∈C in math these are defined by

D0 ⁣(x,a)=2,D1 ⁣(x,a)=x,Dn ⁣(x,a)=xDn−1 ⁣(x,a)−aDn−2 ⁣(x,a)(n≥2),D\_0\\!\\left(x,\\, a\\right) = 2,\\;
D\_1\\!\\left(x,\\, a\\right) = x,\\;
D\_n\\!\\left(x,\\, a\\right) = x\\,D\_{n-1}\\!\\left(x,\\, a\\right)
\- a\\,D\_{n-2}\\!\\left(x,\\, a\\right)\\quad (n \\ge 2),D0​(x,a)=2,D1​(x,a)=x,Dn​(x,a)=xDn−1​(x,a)−aDn−2​(x,a)(n≥2),

and satisfy the functional identity

Dn ⁣(u+au,a)=un+anun.D\_n\\!\\left(u + \\frac{a}{u},\\, a\\right) = u^{n} + \\frac{a^{n}}{u^{n}}.Dn​(u+ua​,a)=un+unan​.

* * *

**1\. Choosing the polynomial**

Take a=1a = 1a=1 and n=19n=19n=19.

Because nnn is odd, D19 ⁣(x,1)D\_{19}\\!\\left(x,\\, 1\\right)D19​(x,1) is an **odd** polynomial; the recurrence immediately shows it is **monic** and has **integer (hence real) coefficients**.

The coefficient of xxx is x=(−1)n−12n=−19,x = (-1)^{\\frac{n-1}{2}}\\,n = -19,x=(−1)2n−1​n=−19, so all requested normalisations are satisfied.

Writing it out gives

p(x)=D19 ⁣(x,1)=x19−19x17+152x15−665x13+1729x11−2717x9+2508x7−1254x5+285x3−19x.
\\boxed{%
p(x) = D\_{19}\\!\\left(x,1\\right)
= x^{19} - 19x^{17} + 152x^{15} - 665x^{13}
\+ 1729x^{11} - 2717x^{9} + 2508x^{7}
\- 1254x^{5} + 285x^{3} - 19x%
}\\,.
p(x)=D19​(x,1)=x19−19x17+152x15−665x13+1729x11−2717x9+2508x7−1254x5+285x3−19x​.

* * *

**2\. Irreducible components of fX={p(x)=p(y)}fX \\;=\\; \\bigl\\{\\, p(x) = p(y) \\,\\bigr\\}fX={p(x)=p(y)}**

For Dickson polynomials one has the classical factorisation

Dn ⁣(x,1)−Dn ⁣(y,1)=(x−y)∏j=1n−12(x2+y2−2cos⁡ ⁣(2πjn)xy−4sin⁡2 ⁣(πjn)),D\_n\\!\\left(x,1\\right) \\;-\\; D\_n\\!\\left(y,1\\right)
\\;=\\;
(x - y)\\,
\\prod\_{j=1}^{\\frac{n-1}{2}}
\\Bigl(
x^{2} + y^{2}
\- 2\\cos\\!\\bigl(\\tfrac{2\\pi j}{n}\\bigr)\\,xy
\- 4\\sin^{2}\\!\\bigl(\\tfrac{\\pi j}{n}\\bigr)
\\Bigr),Dn​(x,1)−Dn​(y,1)=(x−y)∏j=12n−1​​(x2+y2−2cos(n2πj​)xy−4sin2(nπj​)),

where each quadratic factor is irreducible over C\\mathbb{C}C (see, e.g., Lidl–Niederreiter, _Finite Fields_, §3.6).

For n=19n=19n=19 this gives

- **one linear** component x=y;x=y;x=y;
- **nine quadratic** components (corresponding to (j=1,…,9).\\bigl(j = 1,\\,\\ldots,\\,9\\bigr).(j=1,…,9).

Hence X⊂P1×P1X \\subset \\mathbb{P}^{1} \\times \\mathbb{P}^{1}X⊂P1×P1 has 101010 irreducible components, at least three of them and not all linear, as required.

* * *

**3\. Evaluating p(19)p(19)p(19)**

Using the recurrence (or the identity Dn ⁣(x,1)=2Tn ⁣(x2)D\_n\\!\\left(x,\\,1\\right) \\;=\\; 2\\,T\_n\\!\\bigl(\\tfrac{x}{2}\\bigr)Dn​(x,1)=2Tn​(2x​) with Chebyshev TnT\_nTn​ one obtains

p(19)=D19 ⁣(19,1)=1876572071974094803391179.p(19) \\;=\\; D\_{19}\\!\\left(19,\\,1\\right)
\\;=\\; 1\\,876\\,572\\,071\\,974\\,094\\,803\\,391\\,179.p(19)=D19​(19,1)=1876572071974094803391179.

* * *

Thus the polynomial above fulfils every condition, and

p(19)=1,876,572,071,974,094,803,391,179.\\boxed{%
p(19) \\;=\\; 1{,}876{,}572{,}071{,}974{,}094{,}803{,}391{,}179
}.p(19)=1,876,572,071,974,094,803,391,179​.

## OpenAI o1

Solve the following very hard math problem using your in-built knowledge of the literature:

Construct a degree 19 polynomial \ (p(x)) \ in \ mathbb{C}\[x\] such that \ (X := \ {\\, p(x) = p(y) \\, \\} \ subset \ mathbb{P}^{1} \ times \ mathbb{P}^{1}\ ) has at least 3 (but not all linear) irreducible components over \ mathbb{C}. Choose \ (p(x)\ ) to be odd, monic, have real coefficients and linear coefficient \ (-19\ ) and calculate \ (p(19)\ ).

Thought for 1m 19s

I’m piecing together a degree 19 polynomial with only odd powers and a linear coefficient of -19, like: p(x)=x19+a17x17+…+a1xp(x) = x^{19} + a\_{17}x^{17} + \\ldots + a\_1xp(x)=x19+a17​x17+…+a1​x.

I'm examining if the polynomial p(x)=x19+a17x17+…+a3x3−19xp(x) = x^{19} + a\_{17}x^{17} + \\ldots + a\_3x^3 - 19xp(x)=x19+a17​x17+…+a3​x3−19x has a notable classical form, considering symmetry or factorization for multiple irreducible components.

To ensure p(x)p(x)p(x) has three or more irreducible components, I’m considering the factorization of p(x)−p(y)p(x) - p(y)p(x)−p(y) into at least three irreducible factors in C\[x,y\]\\mathbb{C}\[x,y\]C\[x,y\].

I'm working through x19−y19x^{19} - y^{19}x19−y19 to ensure it balances linear and nonlinear factors, aiming for a polynomial with at least three irreducible components that aren't all linear.

Taking a closer look at how p(x)−p(y)p(x) - p(y)p(x)−p(y) can be factored into three distinct polynomials in xxx, aiming to achieve the desired irreducible components.

I'm thinking about how composing ppp with simpler polynomials, like xm−cx^m - cxm−c, could result in multiple irreducible components, achieving at least three distinct factors.

I’m exploring the factorization of p(x)−p(y)p(x) - p(y)p(x)−p(y) with cyclotomic polynomials. This method generates nnn linear irreducible factors, which might not achieve the required three distinct components.

I'm focusing on constructing an "odd" and monic polynomial, ensuring all exponents are odd and the leading term is x19x^{19}x19. This approach aims to achieve the desired factorization.

I'm working with the Chebyshev polynomials to ensure p(x)−p(y)p(x) - p(y)p(x)−p(y) has at least three irreducible components, leveraging their even or odd properties to manage coefficients.

Considering the odd Chebyshev polynomial T19(x)T\_{19}(x)T19​(x) for potential factorization, while also examining composite polynomials of lower degrees to enhance factorization properties.

I'm analyzing how a polynomial composed of lower-degree polynomials, like (x3−3x)k(x^3 - 3x)^k(x3−3x)k, could yield p(x)−p(y)p(x) - p(y)p(x)−p(y) with at least three irreducible components.

Piecing together polynomials with integer coefficients, like (x3−3x)k(x^3 - 3x)^k(x3−3x)k, to achieve factorization in p(x)−p(y)p(x) - p(y)p(x)−p(y) with at least three irreducible components, aiming for degree 19.

I’m examining how p(x)=(x3−3x)kp(x) = (x^3 - 3x)^kp(x)=(x3−3x)k or p(x)=x19−19xp(x) = x^19 - 19xp(x)=x19−19x might yield p(x)−p(y)p(x) - p(y)p(x)−p(y) with three irreducible components, focusing on ensuring the polynomial is of degree 19.

I’m analyzing p(x)−p(y)p(x) - p(y)p(x)−p(y) into (x−y)(x18+x17y+…+y18−19)(x-y)(x^{18} + x^{17}y + \\ldots + y^{18} - 19)(x−y)(x18+x17y+…+y18−19) to identify irreducible components. The polynomial factor x18+x17y+…+y18−19x^{18} + x^{17}y + \\ldots + y^{18} - 19x18+x17y+…+y18−19 remains challenging to factor further.

I’m thinking through a new approach: adjusting the Chebyshev polynomial T19(x)T\_{19}(x)T19​(x) to make it monic, aiming to achieve at least three irreducible components in p(x)−p(y)p(x) - p(y)p(x)−p(y).

OK, let's think through. I’m tweaking T19(x)T\_{19}(x)T19​(x)'s coefficients to keep the polynomial monic and check if it simplifies into multiple irreducible components.

I'm thinking over various factorization strategies for a monic polynomial of degree 19. The goal is to ensure at least one non-linear factor and achieve at least three irreducible components in p(x)−p(y)p(x) - p(y)p(x)−p(y).

I’m updating my approach to factor x2+xy+y2−1x^2 + xy + y^2 - 1x2+xy+y2−1 over complex numbers by exploring change of variables and third roots of unity. This helps in achieving the desired polynomial structure.

I'm combining x3−xx^3 - xx3−x with x19−19xx^{19} - 19xx19−19x to tweak the polynomial's coefficients and complexity, aiming to include more non-linear factors for the desired irreducibility.

Piecing together p(x)=x19−x3−19xp(x) = x^{19} - x^3 - 19xp(x)=x19−x3−19x to ensure it’s odd, monic, and has the required linear coefficient. This targets the desired irreducible factorizations.

I’m mapping out the second factor x18+…+y18−x2−xy−y2−19x^{18} + \\ldots + y^{18} - x^2 - xy - y^2 - 19x18+…+y18−x2−xy−y2−19 to see if it can split into three irreducible components.

I’m considering methods to factorize the polynomial by making it divisible by x−yx - yx−y and ensuring the remaining factor splits into exactly two irreducible components, aiming for a less complex factorization.

I’m examining the polynomial x18+x17y+…+y18x^{18} + x^{17}y + \\ldots + y^{18}x18+x17y+…+y18 and noting it simplifies to x19−y19x−y\\frac{x^{19} - y^{19}}{x - y}x−yx19−y19​, which might reveal further irreducible factors.

I’m mapping out the polynomial x(x18−1)−y(y18−1)x−y\\frac{x(x^{18}-1) - y(y^{18}-1)}{x-y}x−yx(x18−1)−y(y18−1)​ for further factorization. This might yield just two irreducible components, which falls short of three.

I’m exploring whether the polynomial p(x)=x19−(x3)p(x) = x^19 - (x^3)p(x)=x19−(x3) can be expressed as the composition of a smaller polynomial with xkx^kxk, potentially revealing multiple irreducible components.

I'm examining if the polynomial T19(x)T\_{19}(x)T19​(x) can be factored using trigonometric identities, seeking partial factorization without fully linearizing, to gain multiple irreducible components.

OK, let me see. Trigonometric identities show multiple solutions for θ\\thetaθ and ϕ\\phiϕ, likely leading to 19 or 38 linear factors for T19(x)T\_{19}(x)T19​(x).

I’m examining how the equation arccos⁡x=±arccos⁡y+2kπ19\\arccos x = \\pm \\arccos y + \\frac{2k\\pi}{19}arccosx=±arccosy+192kπ​ leads to possible multiple branches, potentially irreducible in the algebraic sense, and needing an example with at least three non-linear irreducible components.

OK, let me see. I’m pulling together details on the polynomial x3(x2−1)8+xx^3 (x^2 - 1)^8 + xx3(x2−1)8+x. It’s monic, with x19x^{19}x19 as the leading term, ensuring it meets key criteria.

I’m noting that the polynomial p(x)=x3(x2−1)8+xp(x) = x^3 (x^2 - 1)^8 + xp(x)=x3(x2−1)8+x is odd, with its linear coefficient patterning to -19.

I’m figuring out how to adjust the linear coefficient of polynomial p(x)p(x)p(x) to -19 by adding a constant factor ccc in front of xxx to ensure it’s adequately modified.

By tweaking the linear coefficient of p(x)=x3(x2−1)8+cxp(x) = x^3 (x^2 - 1)^8 + c xp(x)=x3(x2−1)8+cx to -19, it ensures the polynomial remains monic, odd, and real.

I’m working on adding a constant factor ccc to xxx in p(x)=x3(x2−1)8+cxp(x) = x^3 (x^2 - 1)^8 + c xp(x)=x3(x2−1)8+cx to ensure the linear coefficient is -19, making the polynomial monic, odd, and real.

I'm piecing together the polynomial p(x)=x3(x−1)8(x+1)8p(x) = x^3 (x-1)^8 (x+1)^8p(x)=x3(x−1)8(x+1)8 and considering how p(x)−p(y)p(x) - p(y)p(x)−p(y) might factor with factors like x−yx-yx−y.

I’m confirming p(x)p(x)p(x) is monic, odd, and real, with a linear coefficient of -19, by expanding x3(x2−1)8x^3 (x^2 -1)^8x3(x2−1)8 to set the constant ccc.

I found that for p(x) to have a coefficient of -19 for the x term, c must be -19. The polynomial, p(x), incorporates this constant and preserves the original polynomial's structure.

Below is one concrete example (over the reals) of an odd, monic, degree 19 polynomial with linear coefficient −19-19−19 whose zero-locus relation {p(x)=p(y)} in P1×P1\\{\\,p(x)=p(y)\\,\\}\ \\text{in }\\mathbb{P}^{1}\\times\\mathbb{P}^{1}{p(x)=p(y)}in P1×P1 splits into at least three irreducible components (and not all components are linear). We then compute p(19)p(19)p(19).

* * *

**1\. The polynomial**

Consider

p(x)=x3(x2−1)8−19x.p(x) \\;=\\; x^{3}\\,\\bigl(x^{2}-1\\bigr)^{8} \\;-\\; 19x.p(x)=x3(x2−1)8−19x.

We can expand

x3(x2−1)8=x19−8x17+28x15−56x13+70x11−56x9+28x7−8x5+x3.x^{3}\\,\\bigl(x^{2}-1\\bigr)^{8}
\\;=\\;
x^{19}\\;-\\;8x^{17}\\;+\\;28x^{15}\\;-\\;56x^{13}\\;+\\;70x^{11}
\\;-\\;56x^{9}\\;+\\;28x^{7}\\;-\\;8x^{5}\\;+\\;x^{3}.x3(x2−1)8=x19−8x17+28x15−56x13+70x11−56x9+28x7−8x5+x3.

Hence

p(x)=x19−8x17+28x15−56x13+70x11−56x9+28x7−8x5+x3−19x.p(x) \\;=\\; x^{19} \\;-\\; 8x^{17} \\;+\\; 28x^{15} \\;-\\; 56x^{13} \\;+\\; 70x^{11}
\\;-\\; 56x^{9} \\;+\\; 28x^{7} \\;-\\; 8x^{5} \\;+\\; x^{3} \\;-\\; 19x.p(x)=x19−8x17+28x15−56x13+70x11−56x9+28x7−8x5+x3−19x.

**Checking the required properties**

**Degree 19, monic:**

The leading term is x19x^{19}x19with coefficient 111.

**Odd polynomial:**

All exponents are odd (19,17,…,3,1),\\bigl(19,\\,17,\\,\\ldots,\\,3,\\,1\\bigr),(19,17,…,3,1), and the constant term is 000. Indeed,

p(−x)=−p(x),p(-x) \\;=\\; -\\,p(x),p(−x)=−p(x),

which makes ppp an odd polynomial.

**Real coefficients:**

All coefficients are real integers.

**Linear coefficient −19-19−19:**

The coefficient of xxx is clearly −19-19−19.

**At least three irreducible components, not all linear:**

Over C\\mathbb{C}C, the locus

X={(x,y):p(x)=p(y)}⊂P1×P1X \\;=\\; \\bigl\\{\\, (x,y) : p(x)=p(y) \\,\\bigr\\} \\;\\subset\\; \\mathbb{P}^{1}\\times\\mathbb{P}^{1}X={(x,y):p(x)=p(y)}⊂P1×P1

factors in part because p(x)p(x)p(x) has (for instance) the repeated factors (x2−1)8\\bigl(x^{2}-1\\bigr)^{8}(x2−1)8 in the big piece x3(x2−1)8x^{3}\\,\\bigl(x^{2}-1\\bigr)^{8}x3(x2−1)8. One sees that {p(x)=p(y)}\\{\\,p(x)=p(y)\\,\\}{p(x)=p(y)} contains (at least) the divisor $${x=y\\}$$ plus further factors coming from the roots x=0orx=±1,x = 0 \\;\\text{or}\\; x = \\pm 1,x=0orx=±1, ensuring multiple irreducible components (and not all of them are hyperplanes).

* * *

**2\. Computing p(19)p(19)p(19)**

A direct substitution x=19x=19x=19 gives a large integer. Symbolic expansion or a computer algebra system yields

p(19)=1934999285524070399999639.p(19) \\;=\\; 1934999285524070399999639.p(19)=1934999285524070399999639.

Hence the required value is

\\boxed{\\,p(19) \\;=\\; 1934999285524070399999639\\,}. \\\] &#8203;:contentReference\[oaicite:0\]{index=0}&#8203;

OpenAI o3 gets the response correctly without using search, whereas o1 fails to deliver a correct response.

### Advancing cost-efficient reasoning

##### Cost vs performance: o3-mini and o4-minihttps://images.ctfassets.net/kftzwdyauwt9/1HaJwt63QmevA8n6A8rOys/0d76297d0023935057e9404124a62669/o3-o4_mini_AIME2025.png?w=3840&q=90&fm=webphttps://images.ctfassets.net/kftzwdyauwt9/4Gw2tlDup1LN9WcMiiuyUr/2210496f5a2b2edf06898f9b0d87806b/o3-o4_mini_GPQA-Pass.png?w=3840&q=90&fm=webp

##### Cost vs performance: o1 and o3https://images.ctfassets.net/kftzwdyauwt9/1NDcqcms5r7NFdbdlhVdCX/008e39fe5112baa135c727f15c569508/o3-o4_AIME2025.png?w=3840&q=90&fm=webphttps://images.ctfassets.net/kftzwdyauwt9/2HpQv67tCNmBJ8MtGfnTNS/f0d69d710fbb5ed2e9d36e828b07ccf5/o3-o4_GPQA-Pass.png?w=3840&q=90&fm=webp

OpenAI o3 and o4-mini are the most intelligent models we have ever released, and they’re also often more efficient than their predecessors, OpenAI o1 and o3‑mini. For example, on the 2025 AIME math competition, the cost-performance frontier for o3 strictly improves over o1, and similarly, o4-mini's frontier strictly improves over o3‑mini. More generally, we expect that for most real-world usage, o3 and o4-mini will also be both smarter and cheaper than o1 and o3‑mini, respectively.

## Safety

Each improvement in model capabilities warrants commensurate improvements to safety. For OpenAI o3 and o4-mini, we completely rebuilt our safety training data, adding new refusal prompts in areas such as biological threats (biorisk), malware generation, and jailbreaks. This refreshed data has led o3 and o4-mini to achieve strong performance on our internal refusal benchmarks (e.g., [instruction hierarchy⁠](https://openai.com/index/the-instruction-hierarchy/), jailbreaks). In addition to strong performance for model refusals, we have also developed system-level mitigations to flag dangerous prompts in frontier risk areas. Similar to our earlier work in [image generation⁠](https://openai.com/index/introducing-4o-image-generation/), we trained a reasoning LLM monitor which works from human-written and interpretable safety specifications. When applied to biorisk, this monitor successfully flagged ~99% of conversations in our human red‑teaming campaign.

We stress tested both models with our most rigorous safety program to date. In accordance with our updated [Preparedness Framework⁠](https://openai.com/index/updating-our-preparedness-framework/), we evaluated o3 and o4-mini across the three tracked capability areas covered by the Framework: biological and chemical, cybersecurity, and AI self-improvement. Based on the results of these evaluations, we have determined that both o3 and o4‑mini remain below the Framework's "High" threshold in all three categories. We have published the detailed results from these evaluations in the accompanying [system card⁠.⁠](https://openai.com/index/o3-o4-mini-system-card/)

## Codex CLI: frontier reasoning in the terminal

We’re also sharing a new experiment: Codex CLI, a lightweight coding agent you can run from your terminal. It works directly on your computer and is designed to maximize the reasoning capabilities of models like o3 and o4-mini, with upcoming support for additional API models like [GPT‑4.1⁠](https://openai.com/index/gpt-4-1/).

You can get the benefits of multimodal reasoning from the command line by passing screenshots or low fidelity sketches to the model, combined with access to your code locally. We think of it as a minimal interface to connect our models to users and their computers. Codex CLI is fully open-source at [github.com/openai/codex⁠(opens in a new window)](http://github.com/openai/codex) today.

## Access

ChatGPT Plus, Pro, and Team users will see o3, o4-mini, and o4-mini-high in the model selector starting today, replacing o1, o3‑mini, and o3‑mini‑high. ChatGPT Enterprise and Edu users will gain access in one week. Free users can try o4-mini by selecting 'Think' in the composer before submitting their query. Rate limits across all plans remain unchanged from the prior set of models.

We expect to release OpenAI o3‑pro in a few weeks with full tool support. For now, Pro users can still access o1‑pro.

Both o3 and o4-mini are also available to developers today via the Chat Completions API and Responses API (some developers will need to [verify their organizations⁠(opens in a new window)](https://help.openai.com/en/articles/10910291-api-organization-verification) to access these models). The Responses API supports reasoning summaries, the ability to preserve reasoning tokens around function calls for better performance, and will soon support built-in tools like web search, file search, and code interpreter within the model’s reasoning. To get started, [explore our docs⁠⁠(opens in a new window)](https://platform.openai.com/docs/guides/reasoning?api-mode=responses) and stay tuned for more updates.

## What's next

Today's updates reflect the direction our models are heading in: we’re converging the specialized reasoning capabilities of the o-series with more of the natural conversational abilities and tool use of the GPT‑series. By unifying these strengths, our future models will support seamless, natural conversations alongside proactive tool use and advanced problem-solving.

</details>

<details>
<summary>introducing-perplexity-deep-research</summary>

# Introducing Perplexity Deep Research

**Today we’re launching Deep Research** to save you hours of time by conducting in-depth research and analysis on your behalf. When you ask a Deep Research question, Perplexity performs dozens of searches, reads hundreds of sources, and reasons through the material to autonomously deliver a comprehensive report. It excels at a range of expert-level tasks—from finance and marketing to product research—and attains high benchmarks on Humanity’s Last Exam.

We believe everyone should have access to powerful research tools. That’s why we’re making Deep Research free for all. Pro subscribers get unlimited Deep Research queries, while non-subscribers will have access to a limited number of answers per day. Deep Research is available on Web starting today and will soon be rolling out to iOS, Android, and Mac. (Be sure update your apps to the latest version.)

To give it a try, go to [perplexity.ai and select “Deep Research”](https://www.perplexity.ai/?model_id=deep_research) from the mode selector in the search box before submitting your query.

### How It Works

Perplexity already excels at answering questions. Deep Research takes question answering to the next level by spending 2-4 minutes doing the work it would take a human expert many hours to perform. Here’s how it works:

- **Research with reasoning** \- Equipped with search and coding capabilities, Perplexity’s Deep Research mode iteratively searches, reads documents, and reasons about what to do next, refining its research plan as it learns more about the subject areas. This is similar to how a human might research a new topic, refining one’s understanding throughout the process.

- **Report writing** \- Once the source materials have been fully evaluated, the agent then synthesizes all the research into a clear and comprehensive report.

- **Export & Share** \- You can then export the final report to a PDF or document, or convert it into a Perplexity Page and share it with colleagues or friends.https://framerusercontent.com/images/Lc0634aprN2JYuFLQ8VfKthJnAk.png?width=2292&height=1880

### When to Use Deep Research

We built Deep Research to empower everyone to conduct expert-level analysis across a range of complex subject matters. Deep Research excels at creating work artifacts in domains including finance, marketing, and technology, and is equally useful as a personal consultant in areas such as health, product research, and travel planning. Here are a a few examples of how you might use Deep Research on Perplexity.

#### Financehttps://framerusercontent.com/images/trzwsXtuC3j68cIGyUb6k2lLk.png?width=3840&height=5188

#### Marketinghttps://framerusercontent.com/images/n8ptzcWQs7qIv7JiMDS1ZwJmKA.png?width=3840&height=5188

#### Technologyhttps://framerusercontent.com/images/wRBHkQ4dqR8tLeYql0DyOUdh78.png?width=3840&height=5188

#### Current Affairshttps://framerusercontent.com/images/wug2dVncsmdZqLMr6KElOCtglhc.png?width=3840&height=5188

#### Healthhttps://framerusercontent.com/images/Sqc4r85ACZIQZTzC2pJhe1BCQYc.png?width=3840&height=5188

#### Biographyhttps://framerusercontent.com/images/tQO9LIHgnWvalzwrgmmLCVzqT4.png?width=3840&height=5188

#### Travelhttps://framerusercontent.com/images/ofWFPGvvrYQWaFAr6BOBwOIvpk.png?width=3840&height=5188

### Humanity’s Last Exam

Deep Research on Perplexity attains a 21.1% accuracy score on Humanity’s Last Exam, significantly higher than Gemini Thinking, o3-mini, o1, DeepSeek-R1, and many other leading models. [Humanity’s Last Exam⁠](https://lastexam.ai/) is a comprehensive benchmark for AI systems consisting of over 3,000 questions across 100+ subjects ranging from mathematics and science to history and literature.https://framerusercontent.com/images/hplibuiapLcxAxdbJQWfhnLmiJU.png?width=3840&height=2160

### SimpleQA

Scoring 93.9% accuracy on the [SimpleQA](https://arxiv.org/html/2411.04368v1) benchmark — a bank of several thousand questions that test for factuality — Perplexity Deep Research far exceeds the performance of leading models.https://framerusercontent.com/images/ttftsapj52NTVpjPcXVOj8JfKw.png?width=3840&height=2160

### Runtime Stats

Deep Research on Perplexity not only attains high scores on industry benchmarks, but it does so while completing most research tasks in under 3 minutes — which we’re working to make even faster in the future.https://framerusercontent.com/images/enepaQzuMoqWmDzgU6x5D9ydTqc.png?width=3840&height=1524

</details>

<details>
<summary>learning-to-reason-with-llms-openai</summary>

Our large-scale reinforcement learning algorithm teaches the model how to think productively using its chain of thought in a highly data-efficient training process. We have found that the performance of o1 consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute). The constraints on scaling this approach differ substantially from those of LLM pretraining, and we are continuing to investigate them.https://images.ctfassets.net/kftzwdyauwt9/3OO9wpK8pjcdemjd7g50xk/5ec2cc9d11f008cd754e8cefbc1c99f5/compute.png?w=3840&q=90&fm=webp

o1 performance smoothly improves with both train-time and test-time compute

## Evals

To highlight the reasoning improvement over GPT‑4o, we tested our models on a diverse set of human exams and ML benchmarks. We show that o1 significantly outperforms GPT‑4o on the vast majority of these reasoning-heavy tasks. Unless otherwise specified, we evaluated o1 on the maximal test-time compute setting.https://cdn.openai.com/reasoning-evals/v3/headline-mobile-0.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/headline-mobile-0-dark.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/headline-mobile-1.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/headline-mobile-1-dark.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/headline-mobile-2.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/headline-mobile-2-dark.png?w=3840&q=90&fm=webp

o1 greatly improves over GPT-4o on challenging reasoning benchmarks. Solid bars show pass@1 accuracy and the shaded region shows the performance of majority vote (consensus) with 64 samples.https://cdn.openai.com/reasoning-evals/v3/headline-desktop.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/headline-desktop-dark.png?w=3840&q=90&fm=webp

o1 greatly improves over GPT-4o on challenging reasoning benchmarks. Solid bars show pass@1 accuracy and the shaded region shows the performance of majority vote (consensus) with 64 samples.https://cdn.openai.com/reasoning-evals/v3/breakdown.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/breakdown-dark.png?w=3840&q=90&fm=webp

o1 improves over GPT-4o on a wide range of benchmarks, including 54/57 MMLU subcategories. Seven are shown for illustration.https://cdn.openai.com/reasoning-evals/v3/breakdown-mobile-left.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/breakdown-mobile-left-dark.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/breakdown-mobile-right.png?w=3840&q=90&fm=webphttps://cdn.openai.com/reasoning-evals/v3/breakdown-mobile-right-dark.png?w=3840&q=90&fm=webp

o1 improves over GPT-4o on a wide range of benchmarks, including 54/57 MMLU subcategories. Seven are shown for illustration.

In many reasoning-heavy benchmarks, o1 rivals the performance of human experts. Recent frontier models[1](https://openai.com/index/learning-to-reason-with-llms/#citation-bottom-1) do so well on MATH[2](https://openai.com/index/learning-to-reason-with-llms/#citation-bottom-2)and GSM8K that these benchmarks are no longer effective at differentiating models. We evaluated math performance on AIME, an exam designed to challenge the brightest high school math students in America. On the 2024 AIME exams, GPT‑4o only solved on average 12% (1.8/15) of problems. o1 averaged 74% (11.1/15) with a single sample per problem, 83% (12.5/15) with consensus among 64 samples, and 93% (13.9/15) when re-ranking 1000 samples with a learned scoring function. A score of 13.9 places it among the top 500 students nationally and above the cutoff for the USA Mathematical Olympiad.

We also evaluated o1 on GPQA diamond, a difficult intelligence benchmark which tests for expertise in chemistry, physics and biology. In order to compare models to humans, we recruited experts with PhDs to answer GPQA-diamond questions. We found that o1 surpassed the performance of those human experts, becoming the first model to do so on this benchmark. These results do not imply that o1 is more capable than a PhD in all respects — only that the model is more proficient in solving some problems that a PhD would be expected to solve. On several other ML benchmarks, o1 improved over the state-of-the-art. With its vision perception capabilities enabled, o1 scored 78.2% on MMMU, making it the first model to be competitive with human experts. It also outperformed GPT‑4o on 54 out of 57 MMLU subcategories.

## Chain of Thought

Similar to how a human may think for a long time before responding to a difficult question, o1 uses a chain of thought when attempting to solve a problem. Through reinforcement learning, o1 learns to hone its chain of thought and refine the strategies it uses. It learns to recognize and correct its mistakes. It learns to break down tricky steps into simpler ones. It learns to try a different approach when the current one isn’t working. This process dramatically improves the model’s ability to reason. To illustrate this leap forward, we showcase the chain of thought from o1‑preview on several difficult problems below.

## Hiding the Chains of Thought

We believe that a hidden chain of thought presents a unique opportunity for monitoring models. Assuming it is faithful and legible, the hidden chain of thought allows us to "read the mind" of the modeland understand its thought process. For example, in the future we may wish to monitor the chain of thought for signs of manipulating the user. However, for this to work the model must have freedom to express its thoughts in unaltered form, so we cannot train any policy compliance or user preferences onto the chain of thought. We also do not want to make an unaligned chain of thought directly visible to users.

Therefore, after weighing multiple factors including user experience, competitive advantage, and the option to pursue the chain of thought monitoring, we have decided not to show the raw chains of thought to users. We acknowledge this decision has disadvantages. We strive to partially make up for it by teaching the model to reproduce any useful ideas from the chain of thought in the answer. For the o1 model series we show a model-generated summary of the chain of thought.

</details>

<details>
<summary>llm-system-design-and-model-selection-o-reilly</summary>

Choosing the right LLM has become a full-time job. New models appear almost daily, each offering different capabilities, prices, and quirks, from reasoning strengths to cost efficiency to code generation. This competition creates strong incentives for AI labs to carve out a niche and gives new startups room to emerge, resulting in a fragmented landscape where one model may excel at reasoning, another at code, and a third at cost efficiency.

AI, in one sense, is getting cheaper faster than any previous technology, at least per _unit of intelligence_. For example, input tokens for Gemini 2.5 Flash-Lite are approximately 600 times cheaper than what OpenAI’s GPT-3 (davinci-002) cost in August 2022, while outperforming it on every metric. At the same time, access to frontier capabilities is also becoming more expensive than ever. The reason is simple: we can now pay directly for more capability, which has led to the rise of $300+ per month Pro subscription tiers.

Today, any developer can run capable open-weight models locally for negligible marginal cost using tools like Ollama. At the same time, enterprise systems can experience sharp cost increases, depending on the model size (number of parameters, such as 3 billion, 70 billion, or even in the trillions), the number of internal processing steps, and the volume of input data. For developers, these are central system design choices that directly affect feasibility and cost structure. For end users, this complexity explains why a basic subscription differs so much from a premium plan with higher limits on advanced models.

The choices you make in these broader development decisions also determine which LLM and inference settings are optimal for your use case.

## **The Shifting Foundations of Model Capability**

While early gains in LLM performance tracked closely with increases in pretraining compute, larger datasets, bigger models, and more training steps, this approach now yields diminishing returns.

Recent improvements come from a broader mix of strategies. Pretraining-data quality has become just as important as quantity, with better filtering and AI-generated synthetic data contributing to stronger models. Architectural efficiency, like the innovations introduced by DeepSeek, has started to close the gap between size and capability. And post-training techniques, especially instruction tuning and reinforcement learning from human or AI feedback (RLHF/RLAIF), have made models more aligned, controllable, and responsive in practice.

The more fundamental shift, however, is happening at inference time. Since late 2024, with models like OpenAI’s o1, we’ve entered a new phase where models can trade compute for reasoning _on demand_. Rather than relying solely on what was baked in during training, they can now “think harder” at runtime, running more internal steps, exploring alternative answers, or chaining thoughts before responding. This opens up new capability ceilings, but also introduces new cost dynamics.

These varied improvement strategies have led to a clear divergence among AI labs and models, a rapid expansion in model choice, and in some cases, an explosion in model usage costs.

## **The Modern Cost Explosion: How Inference Scaling Changed the Game**

Inference-time compute scaling has introduced a new dynamic in LLM system design: We’ve gone from a single lever model size, to at least four distinct ways to trade cost for capability at runtime. The result is a widening gap in inference cost across models and use cases, sometimes by factors of 10,000x or more.

**Larger models (size scaling):** The most obvious lever is sheer model size. Frontier LLMs, like GPT-4.5, often built with mixture of experts (MoE) architectures, can have input token costs 750 times higher than streamlined models like Gemini Flash-Lite. Larger parameter counts mean more compute per token, especially when multiple experts are active per query.

**Series scaling (“thinking tokens”):** Newer “reasoning” LLMs perform more internal computational steps, or a longer chain of thought, before producing their final answer. For example, OpenAI’s o1 used ~30x more compute than GPT-4o on average, and often 5x more output tokens per task. Agentic systems introduce an additional method of series scaling and an extra layer of cost multiplication. As these agents think, plan, act, reassess, plan, act, and so on, they often make many LLM steps in a loop, each incurring additional cost.

**Parallel scaling:** Here, the system runs multiple model instances on the same task and then automatically selects the best output via automated methods, such as majority voting (which assumes the most common answer is likely correct) or self-confidence scores (where the model output claiming the highest confidence in its response is taken as the best). The o3-pro model likely runs 5–10x parallel instances over o3. This multiplies the cost by the number of parallel attempts (with some nuance).

**Input context scaling:** In RAG pipelines, the number of retrieved chunks and their size directly influence input token costs and the LLM’s ability to synthesize a good answer. More context can often improve results, but this comes at a higher cost and potential latency. Context isn’t free; it’s another dimension of scaling that developers must budget for.

Taken together, these four factors represent a fundamental shift in how model cost scales. For developers designing systems for high-value problems, **10,000x to 1,000,000x differences in API costs to solve a problem based on architectural choices are now realistic possibilities**. Reasoning LLMs, although only prominent for about nine months, reversed the trend of declining access costs to the very best models. This transforms the decision from “Which LLM should I use?” to include “How much reasoning do I _want to pay for_?”

This shift changes how we think about selection. Choosing an LLM is no longer about chasing the highest benchmark score; it’s about finding the balance point where capability, latency, and cost align with your use case.

## **Core Model Selection Criteria**

When choosing a model we find it is important to first clearly identify your use case and the minimum core AI capabilities and attributes needed to deliver it.

A common first step is to take a look at standard benchmark scores (for example LiveBench, MMLU-Pro, SWE-Bench). These benchmarks are a useful starting point, but some models are tuned on benchmark data, and real-world performance on tasks that are actually relevant to you will often vary. Filtering benchmark tests and scores by your industry and task category is a valuable step here. An LLM optimized for software development might perform poorly in creative writing or vice versa. The match between a model’s training focus and your application domain can outweigh general-purpose benchmarks.

Leaderboards like [LMArena](https://lmarena.ai/leaderboard) and [Artificial Analysis](https://artificialanalysis.ai/) offer broader human‑preference comparisons but still don’t replace custom real-world testing. It helps to have a set of your own example questions or tasks at hand to test out a new model for yourself and see how it performs. This should include a mix of easy tasks to establish a baseline and tough edge cases where it’s easy for a model to make mistakes.

As you move beyond ad hoc testing, for any serious development effort, **custom evaluations are non-negotiable.** They must be tailored to your use case and the types of problems you solve. This is the only way to truly know if a model, or a change to your system, is genuinely improving things for _your_ users and _your_ specific business goals.

Here are some core factors we consider:

**Multimodality** is emerging as a major differentiator. Models like GPT-4o and Gemini can handle not just text but also images, audio, and in some cases video, unlocking applications that pure text models can’t support.

**Context window** and effective **context window utilization** are also key: How many tokens or documents can the model process and how much of that advertised context window can the LLM _actually use_ effectively without performance degradation relative to tasks that use less context?

**Latency** is especially critical for interactive applications. In general, smaller or cheaper models tend to respond faster, while reasoning-heavy models introduce delays due to deeper internal computation.

**Reasoning** is the ability to scale inference-time compute and perform multistep problem-solving, planning, or deep analysis.

**Privacy and security** are often key considerations here. For example, if you want to keep your intellectual property private, you must use a model that won’t train on your inputs, which often points toward self-hosted or specific enterprise-grade API solutions.

**Trustworthiness** is also becoming important and can come down to the reputation and track record of the AI lab. A model that produces erratic, biased, or reputationally damaging outputs is a liability, regardless of its benchmark scores. For instance, Grok has had well-publicized issues with its alignment. Even if such issues are supposedly fixed, it creates a lingering question of trust: How can one be sure it won’t behave similarly in the future?

Additionally, the **knowledge cutoff date** also matters if it is to be used in a fast-moving field.

After working out if a model meets your minimum capability, the next decision is often on optimizing trade-offs among cost, reliability, security, and latency. A key rule of thumb we find useful here: If the reliability gain from a more expensive model or more inference time saves more of your or your users’ time (valued in terms of pay) than the model costs, going with the larger model is a good decision!

## **The Pros and Cons of Open-Weight and Closed-API LLMs**

The rise of increasingly competitive open-weight LLMs, such as Meta’s Llama series, Mistral, DeepSeek, Gemma, Qwen, and now OpenAI’s GPT-OSS has added a critical dimension to the model selection landscape. Momentum behind this open ecosystem surged with the release of DeepSeek’s R1 reasoning model, competitive with OpenAI’s o1 but priced at roughly 30x lower API **costs**. This sparked debate around efficiency versus scale and intensified the broader AI rivalry between China and the US. Reactions ranged from “OpenAI and Nvidia are obsolete” to “DeepSeek’s costs must be fabricated,” but regardless of hype, the release was a milestone. It showed that architectural innovation, not just scale, could deliver frontier-level performance with far greater cost efficiency.

This open-model offensive has continued with strong contributions from other Chinese labs like Alibaba (Qwen), Kimi, and Tencent (Hunyuan), and has put competitive pressure on Meta after its open-weight Llama models fell behind. China’s recent leadership in open-weight LLMs has raised new security/IP issues with some US- and European-based organizations, though we note accessing these model weights and running the model on your own infrastructure doesn’t require sending data to China.

This brings us back to the pros and cons of open weights. While closed-API LLMs still lead at the frontier of capability, the primary advantage of open-weight models is quick and affordable local testing, unparalleled flexibility, and increased data security when run internally. Organizations can also perform **full fine-tuning**, adapting the model’s core weights and behaviors to their specific domain, language, and tasks. Open models also provide **stability and predictability**—you control the version you deploy, insulating your production systems from unexpected changes or degradations that can sometimes occur with unannounced updates to proprietary API-based models.

Public closed-model APIs from major providers benefit from immense economies of scale and highly optimized GPU utilization by batching requests from thousands of users, an efficiency that is difficult for a single organization to replicate. This often means that using a closed-source API can be cheaper per inference than self-hosting an open model. Security and compliance are also more nuanced than they first appear. While some organizations must use self-hosted models to simplify compliance with regulations like GDPR by keeping data entirely within their own perimeter, this places the entire burden of securing the infrastructure on the internal team—a complex and expensive undertaking. Top API providers also often offer dedicated instances, private cloud endpoints, and contractual agreements that can guarantee data residency, zero-logging, and meet stringent regulatory standards. The choice, therefore, is not a simple open-versus-closed binary.

The boundary between open and closed models is also becoming increasingly blurred. Open-weight models are increasingly offered via API by third-party LLM inference platforms, combining the flexibility of open models with the simplicity of hosted access. This hybrid approach often strikes a practical balance between control and operational complexity.

## **Leading Closed LLMs**

Below, we present some key costs and metrics for leading closed-source models available via API. Many of these models have additional complexity and varied pricing including options for fast modes, thinking modes, context caching, and longer context.

We present the latest LiveBench benchmark score for each model as one measure for comparison. LiveBench is a continuously updated benchmark designed to provide a “contamination-free” evaluation of large language models by regularly releasing new questions with objective, verifiable answers. It scores models out of 100 on a diverse set of challenging tasks, with a significant focus on capabilities like reasoning, coding, and data analysis. The similar LiveBench scores between GPT-4.5 and 2.5 Flash-Lite, despite 750x input token cost variation, highlights both that smaller models are now very capable but also that not all capabilities are captured in a single benchmark!https://www.oreilly.com/radar/wp-content/uploads/sites/3/2025/08/AI-Model-Pricing1.png_Source: Towards AI, Company Reports, [LiveBench AI](https://livebench.ai/)_

## **Leading open-weight LLMs**

Below, we also present key costs, the LiveBench benchmark score, and context length for leading open-weight models available via API. We compare hosted versions of these models for easy comparison. Different API providers may choose to host open-weight models with different levels of quantization, different context lengths, and different pricing, so performance can vary between providers.https://www.oreilly.com/radar/wp-content/uploads/sites/3/2025/08/AI-Model-Pricing-and-Specifications.png_Source: Towards AI, Company Reports, [LiveBench AI](https://livebench.ai/)_

Whether hosted or self-deployed, selecting a model only solves part of the problem. In practice, most of the complexity and opportunity lies in how that model is used: how it’s prompted, extended, fine-tuned, or embedded within a broader workflow. These system-level decisions often have a greater impact on performance and cost than the model choice itself.

## **A Practical Guide to Designing an LLM System**

Simply picking the biggest or newest LLM is rarely the optimal strategy. A more effective approach starts with a deep understanding of the developer’s toolkit: knowing which technique to apply to which problem to achieve the desired capability and reliability without unnecessary cost. This is all part of the constant “ **march of nines” as you develop LLM systems modularly to solve for more reliability and capability.** There is a need to prioritize the easiest wins that deliver tangible value before investing in further incremental and often costly accuracy improvements. The reality will always vary on a case-by-case basis, but here is a quick guide to navigating this process.

### **Step 1: Open Versus Closed?**

This is often your first decision.

- **Go with a closed-API model (e.g., from OpenAI, Google, Anthropic) if:** Your priority is accessing the absolute state-of-the-art models with maximum simplicity.
- **Go with an open-weight model (e.g., Llama, Mistral, Qwen, DeepSeek) if:**
  - **Data security and compliance are paramount:** If you need to guarantee that sensitive data never leaves your own infrastructure.
  - **You need deep customization and control:** If your goal is to fine-tune a model on proprietary data and to create a specialized expert that you control completely.

If you went open, what can you _realistically_ run? Your own GPU infrastructure is a hard constraint. Assess your cluster size and memory to determine if you can efficiently run a large, leading 1 trillion+ parameter MoE model, such as Kimi K2, or if you are better served by a medium-size model such as Gemma 3 27B or a much smaller model like Gemma 3n that can even run on mobile.

### **Step 2: Gauging the Need for Reasoning**

Does your task require the model to simply blast out a response, or does it need to _think_ first?

- **Reasoning:** For tasks that involve complex, multistep problem-solving, brainstorming, strategic planning, intricate code generation, or deep analysis, you need a dedicated reasoning model such as o3, Gemini 2.5 Pro, DeepSeek R1, or Claude 4. In some cases these models can be used in high-reasoning mode, which encourages the model to think for longer before responding.
- **No reasoning:** For straightforward tasks like simple Q&A, summarization of a single document, data extraction, or classification, a powerful reasoning model is overkill.
- **The middle ground:** For tasks requiring moderate reasoning, such as generating a structured report from a few data points or performing basic data analysis at scale, a “mini” reasoning model, like OpenAI’s o4-mini or Gemini Flash 2.5, offers a balance of capability and cost.

### **Step 3: Pinpointing Key Model Attributes**

Beyond general intelligence and reasoning, modern LLMs are specialists. Your choice should be guided by the specific attributes and “superpowers” your application needs.

- **Prioritize accuracy over cost** for high-value tasks where mistakes are costly or where a human expert’s time is being saved. o3-pro is a standout model here and it can even be used as a fact checker to meticulously check the details of an earlier LLM output.
- **Prioritize speed and cost over accuracy:** For user-facing, real-time applications like chatbots or high-volume, low-value tasks like simple data categorization, latency and cost are paramount. Choose a hyper-efficient “flash” or “mini” model such as Gemini 2.5 Flash-Lite. Qwen3-235B models can also be a great option here but are too complex to inference yourself.
- **Do you need a deep, long-context researcher?** For tasks that require synthesizing information from massive documents, entire codebases, or extensive legal contracts, a model with a vast and highly effective context window is crucial. **Gemini 2.5 Pro** excels here.
- **Is multimodality essential?** If your application needs to understand or generate images, process audio in real time, or analyze video, your choice narrows to models like **GPT-4o** or the **Gemini** family. For one-shot YouTube video processing, Gemini is the standout.
- **Is it a code-specific task?** While many models can code, some are explicitly tuned for it. In the open world, Codestral and Gemma do a decent job. But Claude has won hearts and minds, at least for now.
- **Do you need live, agentic web search?** For answering questions about current events or topics beyond the model’s knowledge cutoff, consider a model with a built-in, reliable web search, such as **o3.**
- Do you need complex **dialogue and emotional nuance?** GPT-4.5, Kimi K2, Claude Opus 4.0, or Grok 4 do a great job.

### **Step 4: Prompting, Then RAG, Then Evaluation**

Before you dive into more complex and costly development, always see how far you can get with the simplest techniques. This is a path of escalating complexity. Model choice for RAG pipelines is often centered around latency for end users, but recently more complex agentic RAG workflows or long-context RAG tasks require reasoning models or longer context capabilities.

1. **Prompt engineering first:** Your first step is always to maximize the model’s inherent capabilities through clear, well-structured prompting. Often, a better prompt with a more capable model is all you need.
2. **Move to retrieval-augmented generation (RAG):** If your model’s limitation is a lack of specific, private, or up-to-date _knowledge_, RAG is the next logical step. This is the best approach for reducing hallucinations, providing answers based on proprietary documents, and ensuring responses are current. However, RAG is not a panacea. Its effectiveness is entirely dependent on the quality and freshness of your dataset, and building a retrieval system that consistently finds and uses the _most_ relevant information is a significant engineering challenge. RAG also comes with many associated decisions, such as the quantity of data to retrieve and feed into the model’s context window, and just how much use you make of long-context capabilities and context caching.
3. **Iterate with advanced RAG:** To push performance, you will need to implement more advanced techniques like hybrid search (combining keyword and vector search), re-ranking retrieved results for relevance, and query transformation.
4. **Build custom evaluation**: Ensure iterations on your system design, additions of new advanced RAG techniques, or updates to the latest model are always moving progress forward on your key metrics!

### **Step 5: Fine-Tune or Distill for Deep Specialization**

If the model’s core _behavior_—not its knowledge—is still the problem, then it’s time to consider fine-tuning. Fine-tuning is a significant undertaking that requires a high-quality dataset, engineering effort, and computational resources. However, it can enable a smaller, cheaper open-weight model to outperform a massive generalist model on a specific, narrow task, making it a powerful tool for optimization and specialization.

- **Fine-tuning is for changing behavior, not adding knowledge.** Use it to teach a model a specific skill, style, or format. For example:
  - To reliably output data in a complex, structured format like specific JSON or XML schemas.
  - To master the unique vocabulary and nuances of a highly specialized domain (e.g., legal, medical).
  - Some closed-source models are available for fine-tuning via API such as Gemini 2.5 Flash and various OpenAI models. Larger models are normally not available.
  - **In open-weight models,** Llama 3.3 70B and Qwen 70B are fine-tuning staples. The process is more complex to fine-tune an open-weight model yourself.
- Model **distillation** can also serve as a production-focused optimization step. In its simplest form, this consists of generating synthetic data from larger models to create fine-tuning datasets to improve the capabilities of smaller models.
- **Reinforcement fine-tuning (RFT) for problem-solving accuracy**

Instead of just imitating correct answers, the model learns by trial, error, and correction. It is rewarded for getting answers right and penalized for getting them wrong.
  - **Use RFT to:** Create a true “expert model” that excels at complex tasks with objectively correct outcomes.
  - **The advantage:** RFT is incredibly data-efficient, often requiring only a few dozen high-quality examples to achieve significant performance gains.
  - **The catch:** RFT requires a reliable, automated “grader” to provide the reward signal. Designing this grader is a critical engineering challenge.

### **Step 6: Orchestrated Workflows Versus Autonomous Agents**

The critical decision here is how much freedom to grant. Autonomous agents are also more likely to need more expensive reasoning models with greater levels of inference scaling. Parallel inference scaling methods with multiple agents are also beginning to deliver great results. Small errors can accumulate and multiply during many successive agentic steps so the investment in a stronger more capable model can make all the difference in building a usable product.

- **Choose an orchestrated workflow for predictable tasks**

You design a specific, often linear, sequence of steps, and the LLM acts as a powerful component at one or more of those steps.
  - **Use when:** You are automating a known, repeatable business process (e.g., processing a customer support ticket, generating a monthly financial summary). The goal is reliability, predictability, and control.
  - **Benefit:** You maintain complete control over the process, ensuring consistency and managing costs effectively because the number and type of LLM calls are predefined.
- **Build hybrid pipelines:** Often, the best results will come from combining many LLMs, open and closed, within a pipeline.
  - This means using different LLMs for different stages of a workflow: a fast, cheap LLM for initial query routing; a specialized LLM for a specific subtask; a powerful reasoning LLM for complex planning; and perhaps another LLM for verification or refinement.
- **Choose an autonomous agent for open-ended problems.** You give the LLM a high-level goal, a set of tools (e.g., APIs, databases, code interpreters), and the autonomy to figure out the steps to achieve that goal.
  - **Use when:** The path to the solution is unknown and requires dynamic problem-solving, exploration, or research (e.g., debugging a complex software issue, performing deep market analysis, planning a multistage project).
  - **The critical risk—runaway costs:** An agent that gets stuck in a loop, makes poor decisions, or explores inefficient paths can rapidly accumulate enormous API costs. **Implementing strict guardrails is critical:**
    - **Budget limits:** Set hard caps on the cost per task.
    - **Step counters:** Limit the total number of “thoughts” or “actions” an agent can take.
    - **Human-in-the-loop:** Require human approval for potentially expensive or irreversible actions.
  - Gemini 2.5 Pro and o3 are our favourite closed-API models for agent pipelines, while in open-weight models we like Kimi K2.

Working through these steps helps translate a vague problem into a concrete implementation plan, one that’s grounded in clear trade-offs and tailored to your needs. This structured approach often yields systems that are not only more capable and reliable but also far more effective for specific tasks than a general-purpose chatbot ever could be.

## **Conclusion**

The open-versus-closed race gives us rapid access to strong LLMs but also creates complexity. Selecting and deploying them demands both engineering discipline and economic clarity.

Developing in the LLM ecosystem demands a new level of engineering discipline and keen economic awareness. No single LLM is a cure-all. A practical, evolving toolkit is essential, but knowing which tool to pull out for which job is the real art. The challenge isn’t just picking a model from a list; it’s about architecting a solution. This requires a systematic approach, moving from high-level strategic decisions about data and security down to the granular, technical choices of development and implementation.

The success of specialized “LLM wrapper” applications like Anyscale/Cursor for coding or Perplexity for search, some of which are now valued at over $10 billion, underscores the immense value in this tailored approach. These applications aren’t just thin wrappers; they are sophisticated systems that leverage foundation LLMs but add significant value through custom workflows, fine-tuning, data integration, and user experience design.

Ultimately, success hinges on informed pragmatism. Developers and organizations need a sharp understanding of their problem space and a firm grasp of how cost scales across model choice, series and parallel reasoning, context usage, and agentic behavior. Above all, custom evaluation is non-negotiable because your use case, not a benchmark, is the only standard that truly matters.

</details>

<details>
<summary>overview</summary>

# Human-in-the-loop

To review, edit, and approve tool calls in an agent or workflow, [use LangGraph's human-in-the-loop features](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/) to enable human intervention at any point in a workflow. This is especially useful in large language model (LLM)-driven applications where model output may require validation, correction, or additional context.https://langchain-ai.github.io/langgraph/concepts/img/human_in_the_loop/tool-call-review.png

## Key capabilities

- **Persistent execution state**: Interrupts use LangGraph's [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) layer, which saves the graph state, to indefinitely pause graph execution until you resume. This is possible because LangGraph checkpoints the graph state after each step, which allows the system to persist execution context and later resume the workflow, continuing from where it left off. This supports asynchronous human review or input without time constraints.

There are two ways to pause a graph:


  - [Dynamic interrupts](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/#pause-using-interrupt): Use `interrupt` to pause a graph from inside a specific node, based on the current state of the graph.
  - [Static interrupts](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/#debug-with-interrupts): Use `interrupt_before` and `interrupt_after` to pause the graph at pre-defined points, either before or after a node executes.https://langchain-ai.github.io/langgraph/concepts/img/breakpoints.pngAn example graph consisting of 3 sequential steps with a breakpoint before step\_3.

- **Flexible integration points**: Human-in-the-loop logic can be introduced at any point in the workflow. This allows targeted human involvement, such as approving API calls, correcting outputs, or guiding conversations.


## Patterns

There are four typical design patterns that you can implement using `interrupt` and `Command`:

- [Approve or reject](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/#approve-or-reject): Pause the graph before a critical step, such as an API call, to review and approve the action. If the action is rejected, you can prevent the graph from executing the step, and potentially take an alternative action. This pattern often involves routing the graph based on the human's input.
- [Edit graph state](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/#review-and-edit-state): Pause the graph to review and edit the graph state. This is useful for correcting mistakes or updating the state with additional information. This pattern often involves updating the state with the human's input.
- [Review tool calls](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/#review-tool-calls): Pause the graph to review and edit tool calls requested by the LLM before tool execution.
- [Validate human input](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/add-human-in-the-loop/#validate-human-input): Pause the graph to validate human input before proceeding with the next step.

</details>

<details>
<summary>pricing-openai</summary>

# API Pricing

## Flagship models

Our frontier models are designed to spend more time thinking before producing a response, making them ideal for complex, multi-step problems.

## GPT-5

The best model for coding and agentic tasks across industries

### Price

Input:

$1.250 / 1M tokens

Cached input:

$0.125 / 1M tokens

Output:

$10.000 / 1M tokens

## GPT-5 mini

A faster, cheaper version of GPT-5 for well-defined tasks

### Price

Input:

$0.250 / 1M tokens

Cached input:

$0.025 / 1M tokens

Output:

$2.000 / 1M tokens

## GPT-5 nano

The fastest, cheapest version of GPT-5—great for summarization and classification tasks

### Price

Input:

$0.050 / 1M tokens

Cached input:

$0.005 / 1M tokens

Output:

$0.400 / 1M tokens

## GPT-5 pro

The smartest and most precise model

### Price

Input:

$15.00 / 1M tokens

Cached input:

-

Output:

$120.00 / 1M tokens

</details>

<details>
<summary>revisiting-the-test-time-scaling-of-o1-like-models-do-they-t</summary>

# Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?

###### Abstract

The advent of test-time scaling in large language models (LLMs), exemplified by OpenAI’s o1 series, has advanced reasoning capabilities by scaling computational resource allocation during inference. While successors like QwQ, Deepseek-R1 (R1) and LIMO replicate these advancements, whether these models truly possess test-time scaling capabilities remains underexplored. This study found that longer CoTs of these o1-like models do not consistently enhance accuracy; in fact, correct solutions are often shorter than incorrect ones for the same questions. Further investigation shows this phenomenon is closely related to models’ self-revision capabilities - longer CoTs contain more self-revisions, which often lead to performance degradation. We then compare sequential and parallel scaling strategies on QwQ, R1 and LIMO, finding that parallel scaling achieves better coverage and scalability. Based on these insights, we propose “Shortest Majority Vote”, a method that combines parallel scaling strategies with CoT length characteristics, significantly improving models’ test-time scalability compared to conventional majority voting approaches.

## Introduction

The release of the OpenAI o1 series models marked a pivotal advancement in the reasoning capabilities of Large Language Models (LLMs), introducing a novel scaling paradigm, test-time scaling, which allocates more compute resources during test time. The test-time scaling have two dimensions, sequential and parallel. Sequential scaling increase test-time compute by scaling the length of Chain-of-Thought (CoT), while parallel scaling parallely samples multiple solutions and pick the best one.

Following o1’s success, models such as QwQ, Deepseek-R1 (R1) and LIMO have emerged as leading open-source successors, replicating o1’s achievements and demonstrating comparable reasoning abilities. Although both QwQ, R1 and LIMO demonstrate strong reasoning capabilities and the ability to generate lengthy CoT at test time, the existence of true test-time scaling where performance consistently improves with longer CoTs remains to be verified for these models.

To explore this question, we systematically investigate the relationship between CoT length and reasoning performance in QwQ, R1 and LIMO, challenging the conventional assumption that extended reasoning chains inherently lead to improved accuracy. Contrary to expectations, our analysis reveals that longer CoTs do not consistently improve accuracy of these o1-like models.
Notably, we found that the average length of correct solutions is shorter than that of incorrect ones for the same questions, which is shown in Figure 1. This counterintuitive finding underscores the need for a deeper understanding of the test-time scaling of o1-like models.

To understand why the longer CoTs do not lead to the better performance, we compared the difference between long CoTs and short CoTs, finding that long CoTs contain more self-revisions (“Wait”, “Alternatively”) than the short CoTs, which is shown in Appendix E. Inspired by that, we iteratively prompted QwQ, R1 and LIMO for more self-revisions. Our observations revealed that QwQ and R1-Distill-1.5b exhibited performance degradation as the length of reflection increased. In contrast, R1-Distill-14b, R1-Distill-32b, and LIMO demonstrated initial performance improvements during early revisions, followed by oscillatory behavior in subsequent iterations. To further understand the limitations of sequential scaling, we evaluated the models’ capacity to revise incorrect answers. Our findings indicate that QwQ, R1 and LIMO all demonstrated limited ability to convert incorrect answers to correct ones during the revision process. Most revisions retained the original answers, and more concerning, both QwQ and R1-Distill-1.5b showed a higher propensity to change correct answers to incorrect ones rather than vice versa. These results reveal that self-revision ability is a key factor in the effectiveness of sequential scaling for o1-like models.

Given the limited effectiveness of sequential scaling, we explored an alternative test-time scaling strategie, parallel scaling. Our comparative analysis of sequential and parallel scaling revealed that parallel scaling not only achieves the better coverage (pass@k score) but also offers superior scalability compared to sequential scaling for QwQ and R1, which demonstrates that o1-like models have limited sequential-scaling capability, but strong parallel-scaling capability.

Building on these findings, we propose a novel test-time scaling method, Shortest Majority Vote, which incorporate parallel scaling approaches with our insight on sequential scaling. In particular, this method leverages the observation that shorter solutions tend to lead to better performance compared to longer ones. Shortest Majority Vote improves majority vote by prioritizing clusters that have both more solutions and shorter solution lengths. Experimental results demonstrate that Shortest Majority Vote substantially outperforms conventional Majority Vote, significantly improving the test-time scalability of both QwQ and R1 models.

Our contributions are as follows:

1. 1)

We systematically investigate the test-time scaling capabilities of o1-like models QwQ, R1 and LIMO, and find that their performance can not be continuously improved through increasing CoT length.

2. 2)

We reveal that insufficient self-revision capability of o1-like models is the primary reason for their failure in sequential scaling.

3. 3)

We find that parallel scaling achieves better coverage and scalability than sequential revision for o1-like models.

4. 4)

Based on our insights into sequential and parallel scaling, we propose Shortest Majority Vote, a test-time scaling method that enhances majority voting by considering solution length, significantly outperforming traditional methods.

Figure 1: The average length of correct solutions versus incorrect solutions evaluated on the same questions. For each question, solution lengths were averaged separately for correct and incorrect responses, then averaged across all questions.

## Related Work

The success of o1 has ushered in a new scaling paradigm, test-time compute scaling, which enables continuous improvements in model performance by increasing computational expenditure during inference. Currently, scaling test-time compute can be approached in two dimensions: parallel scaling and sequential scaling.

#### Parallel Scaling

Parallel scaling typicallly samples multiple solutions in parallel and pick one according to some guidence signal like reward. Notable examples of parallel scaling include Best-of-N Search, which is based on a reward model, and Majority Vote, which exploits model uncertainty. The primary distinction between these approaches lies in the method used to select the final solution or answer after sampling multiple candidates. Both Best-of-N Search and Majority Vote are parallel scaling techniques at the solution level, while Tree-Search algorithms can be viewed as parallel scaling at the token or step level. Beam-Search and MCTS are classic examples of Tree-Search algorithms. All parallel scaling methods rely on guidance signals to select the optimal token, step, or solution from a set of candidates.

#### Sequential Scaling

Sequential scaling enhances test-time computation by generating progressively longer solutions along the sequence dimension. The most prevalent method of sequential scaling is Self-Revision, where models first generate an initial response and then iteratively evaluate and refine it based on self-assessment. In contrast, other approaches leverage external feedback—such as signals from a code execution environment—rather than self-evaluation to enhance solutions.

The effectiveness of sequential scaling with self-revision remains a contentious issue. Some argue that models cannot achieve effective self-refinement without external feedback. Conversely, some researchers posit that evaluating a solution’s correctness is inherently easier than generating a correct solution, suggesting that LLMs have the capacity for self-evaluation. Other studies show that it is possible to teach LLM to self-refine through reinforcement learning or supervised fine-tuning. One comparison of various test-time scaling algorithms found that when feedback accuracy exceeds 90%, Self-Revision outperforms Best-of-N Search.

#### o1-like Models

The release of o1 has further underscored the significance of sequential scaling, as o1’s CoT length is substantially greater than that of conventional models. The research community has made significant efforts to reproduce the capabilities of o1, with QwQ and R1 and LIMO emerging as the most successful attempts. However, Our findings reveal that for R1 and QwQ, extending solution length does not necessarily yield better performance due to the models’ limited self-revision capabilities. Parallel findings attribute this phenomenon to model underthinking, where models initially reach correct intermediate solutions but subsequently deviate toward incorrect conclusions during extended reasoning.

## The Failure of Sequential Scaling

### Invalid Scaling of CoT Length: Longer CoTs Do not Improve Performance

To investigate whether the accuracy of QwQ, R1 and LIMO genuinely improves with increasing CoT length, we sampled each model five times on the same question and sorted the five solutions by length in ascending order. We grouped the solutions based on their rank in this sorted list, with the i-th ranked solutions forming a distinct group. For instance, all the longest solutions (rank 5) from different questions formed one group, while all the shortest solutions (rank 1) formed another, resulting in 5 comprehensive solution groups for analysis.

We present the average lengths of the five groups of solutions in Figure 2(a). Since the grouping of solutions is based on their lengths, the differences in length between the groups are pronounced. The average length of the longest solutions is approximately twice that of the shortest solutions. This indicates that long-chain-of-thought (CoT) models like QwQ, R1 and LIMO exhibit a high diversity in the lengths of the solutions they sample.

There is no clear correlation between the length of solutions and the model’s size. For example, R1-Distill-1.5b produces the longest solutions while QwQ (32b) generates the shortest. A comparison of solution lengths across different datasets shows that solutions for simpler datasets, such as Math, are significantly shorter than those for more difficult datasets, like AIME. This suggests that the model adjusts the solution length based on the difficulty of the problem.

The accuracy of the five groups of solutions is presented in Figure 2(b). Although there is a significant disparity in solution lengths across the groups, the differences in accuracy are much less pronounced. Notably, we do not observe a consistent improvement in accuracy for either QwQ or R1 as solution length increases. This trend holds true across all model variants as well as across all evaluated datasets. In some cases, we even observe an inverse scaling phenomenon, where accuracy decreases with increasing CoT length, especially on more difficult datasets like AIME and Omini-MATH. These findings cast doubt on the presumed test-time scaling capabilities of o1-like models, challenging the assumption that extended reasoning chains inherently yield superior problem-solving performance.

To make the relationship between CoT length and accuracy more clear, we compared the lengths of correct and incorrect solutions for the same question. First, we identified questions that had both correct and incorrect answers. For each of these questions, we calculated the average length of correct and incorrect solutions. We then averaged these values across all questions to determine the overall average length for correct and incorrect solutions. The results are shown in Figure 1. We found that, for QwQ, R1 and LIMO, across all model sizes and datasets, the length of correct solutions is consistently shorter than that of incorrect solutions. This observation suggests that longer CoTs do not necessarily lead to better performance and may even be associated with lower accuracy. Moreover, we observed that for weaker models, such as QwQ and R1-Distill-1.5B, the gap in solution length between correct and incorrect solutions is significantly larger than for stronger models, such as R1-671b. This suggests that the invalid scaling phenomenon is more pronounced in the weaker models.

### Explaining Invalid Scaling: The Key Factor is the Failure of Self-Revision

In Section 4.1, we observed the phenomenon that long solutions exhibit lower accuracy compared to short solutions. In this section, we investigate the underlying reasons for this phenomenon. We first analyzed how the maximum token limitation affects generation performance and confirmed that the observed invalid scaling phenomenon was not caused by constraints in the maximum token length. Next, we examined the differences between long and short solutions, finding that long solutions exhibit a higher frequency of self-revision. Moreover, our analysis suggests a strong correlation between self-revision, solution length, and accuracy.

#### Difference between Short and Long CoT

To understand why long solutions of QwQ, R1 and LIMO is not better than short solutions, we analyzed their differences. We observed that QwQ, R1 and LIMO all primarily extend solution length through self-revision, characterized by markers such as “Wait” and “Alternatively”. We show some examples of that in Appendix E. To quantify this phenomenon, we counted the occurrences of “wait” in solutions of QwQ, R1 and LIMO in Figure 3(b). The results demonstrates a strong linear correlation between solution length and the frequency of self-correction markers for all models. This suggests that the mechanisms of self-revision may play a significant role in generating longer solutions.

#### Scaling Solution Length with Self-Revision

We have tried to investigate the revision behaviors inside the sampled solutions, however, it is difficult to extract the initial solution and the following revision exactly from QwQ, R1 and LIMO’s solutions. Alternatively to that, we prompted the models to continue thinking based on their sampled solutions.

QwQ, R1 and LIMO often conclude their solutions with phrases like “final answer: …”, and R1 additionally outputs a ‘</think>’ tag followed by a final response. To facilitate smoother continuation of the reasoning process, we removed the “final answer” portion from the solutions. We then used the keyword “Wait” or “Alternatively” as the prompt to encourage self-revision. We calculated the probabilities of the model predicting the next token as “Wait” or “Alternatively” and selected the one with the higher probability as the prompt.

We prompted QwQ, R1 and LIMO to continue reasoning for 40 additional steps on the AIME benchmark. We show the results in Figure 4(c), from which we observe that the solution length increase almost linearly with additional steps. After 40 steps, the solution length of QwQ and R1 is almost third as their original length.

We show the accuracy after sequential revision in Figure 4(a) and 4(b). Our results reveal that the accuracy of QwQ and R1-Distill-1.5b decreases constantly as the number of reasoning steps increases, while the accuracy of R1-Distill-32b, R1-Distill-14b and LIMO initially improves and then oscillates with further reasoning steps. Further analysis in Appendix B reveal that the improvement on R1-Distill-32b, R1-Distill-14b and LIMO during revisions mainly comes from the revision on short solutions. These results corroborate our previous experimental findings, suggesting that longer solutions do not improve performance, especially for weaker models such as QwQ and R1-Distill-1.5b. These findings suggest that the reason why longer solutions do not consistently lead to better performance in QwQ, R1 and LIMO may lie in the failure of self-revision.

#### Investigating Self-Revision Behavior

To further investigate the effectiveness of self-revision, we analyzed the proportion of cases where the model corrected an initial incorrect answer to a correct one versus changing an initial correct answer to an incorrect one during scaling solution length. We found that, the proportions of changing a incorrect answer to an correct one is extremely low, always below 10%. Notably, for QwQ and R1-Distill-1.5b, the proportion of changing a correct answer to an incorrect one was even higher than that of correcting an incorrect answer to a correct one. This observation helps explain why prompting QwQ and R1-Distill-1.5b to continue reasoning led to a decrease in accuracy. For simplicty, we call the proportions of changing a incorrect answer to an correct one as the successful-revision rate, while the reverse as the failed-revision rate.

Although R1-Distill-32b, R1-Distill-14b and LIMO exhibit a higher successful-revision rate than failed-revision rate, the increase of successful-revision rate plateaus after approximately 10 steps, with further revisions providing no additional benefits. This observation explains why their accuracy during sequential scaling initially increases with multiple rounds of revision but later stabilizes with fluctuations.

The successful-revision rate of QwQ, R1 and LIMO are all below 10%, what is the outcome of the model’s self-revision in unsuccessful cases? We hypothesize that, in most instances, the model simply keeps its original answer unchanged. To validate that, we computed the proportion of instances where the model persists with its original answer, even when it is incorrect, and the results were as expected. As shown in Figure 5, when the original answer is wrong, both R1-Distill-32b and R1-Distill-14b maintain the original answer in over 70% of cases. Although retaining the original answer does not reduce accuracy, it also makes the scaling solution length ineffective. This phenomenon suggests that the model’s ability to early stop may also be a critical factor influencing whether its performance improves with an increasing solution length.

The above analysis indicates that the key factor determining whether o1-like models’ performance improve with an increase in solution length is their ability to self-revise. The model’s accuracy increases with the more incorrect answers revised to correct and vice versa.

## Sequential Scaling vs. Parallel Scaling

Based on our experimental findings presented in Section 4.2, sequential scaling demonstrates limited effectiveness for QwQ, R1 and LIMO. An alternative approach to scaling test-time compute is parallel scaling, which generates multiple solutions in parallel and selects the best one as the final answer.

We compared the performance of sequential scaling and parallel scaling in terms of the coverage (pass@k score) and accuracy of QwQ and R1, which are shown in Figure 6(a) and 6(b) respectively. For sequential scaling, we iteratively prompt models to self-revise for 40 steps. While for parallel scaling, we parallely sample 10 solutions. The coverage is evaluated by counting the proportion of whether multiple candidate answers contain a correct one. In parallel scaling, coverage increases by one if at least one sampled solution is correct. Similarly, in sequential scaling, coverage increases by one if at least one revision iteration succeeds.

Our findings show that, for the same number of generated tokens, parallel scaling provides a significantly larger improvement in coverage compared to sequential scaling, for both R1-Distill-32b and QwQ. However, a practical parallel scaling method must select a final answer from a set of candidate answers. We implement parallel scaling using majority vote and sequential scaling by taking the answer from the last revision as the final answer. Since majority voting requires at least three solutions to be effective, it does not provide any benefit when scaling the number of solutions from 1 to 2. In contrast, sequential revision is effective for R1-Distill-32b when scaling the number of tokens to 10k, but further scaling does not yield additional benefits. Additionally, because sequential scaling involves attention over a longer context, its computational cost is much higher than that of parallel scaling when generating the same number of tokens.

## Application of Our Findings: Shortest Majority Vote

Given the limitation of sequential scaling of the current o1-like models, we turn to parallel scaling techniques and incorperate it with our insight on sequential scaling. Specifically, we propose a new Parallel Scaling algorithm: Shortest Majority Vote. Shortest Majority Vote is an extension of Majority Vote, but it accounts for the length of the solutions generated by the model. In the original Majority Vote, solutions with the same answer are grouped into a single category, and the number of solutions in each category is counted, with the answer corresponding to the category with the most solutions selected as the final answer. In contrast, Shortest Majority Vote not only counts the number of solutions in each category, but also computes the average length of the solutions in each category. Let the number of solutions in the i-th category be c_i and the average solution length in that category be l_i. The score for category i in Shortest Majority Vote is computed as:

`s_i = c_i / log(l_i)`

and the final answer is chosen from the category with the highest score. The score s_i is designed with the assumption that the correct answer is more likely to appear in categories with a larger number of solutions and shorter solution lengths. Shortest Majority Vote offers two key advantages: first, it is particularly effective for some o1-like models, where performance deteriorates with increasing solution length; second, it enables the use of solution length as a guidence signal for identifying superior solutions when candidate solutions are limited, especially in cases where conventional Majority Vote becomes ineffective due to having only two candidate solutions.

We evaluated the performance of Shortest Majority Vote and Majority Vote through experiments on the AIME and GPQA benchmarks, sampling 16 solutions from QwQ, R1 and LIMO models. We implemented a simple baseline approach, denoted as "Shortest," which selects the answer from the solution with the minimal length. The experimental results are presented in Table 2 and Figure 7. Table 2 demonstrates that Shortest Majority Vote significantly outperforms both Majority Vote and Shortest methods, particularly on the AIME benchmark. Figure 7 illustrates the parallel-scaling performance of these three methods, showing that as the number of generated tokens increases, Shortest Majority Vote maintains superior performance over both alternatives on AIME. The corresponding parallel-scaling results for GPQA are provided in Appendix C. Notably, while Shortest performs better than Majority Vote when only two solutions are sampled, it exhibits inferior performance in all other scenarios. These empirical findings strongly support the effectiveness of the Shortest Majority Vote approach.

## Conclusion

In this study, we challenged the assumption that o1-like models like QwQ and R1 models have test-time scaling capability.
We found that shorter solutions often outperform longer ones, and that sequential scaling through self-revision has limited effectiveness. Based on these insights, we developed Shortest Majority Vote, a parallel scaling method that considers solution length, which significantly outperformed traditional majority vote.

</details>

<details>
<summary>what-is-the-model-context-protocol-mcp-model-context-protoco</summary>

MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems.Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks.Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.https://mintcdn.com/mcp/bEUxYpZqie0DsluH/images/mcp-simple-diagram.png?fit=max&auto=format&n=bEUxYpZqie0DsluH&q=85&s=35268aa0ad50b8c385913810e7604550

## [​](https://modelcontextprotocol.io/docs/getting-started/intro\#what-can-mcp-enable%3F)  What can MCP enable?

- Agents can access your Google Calendar and Notion, acting as a more personalized AI assistant.
- Claude Code can generate an entire web app using a Figma design.
- Enterprise chatbots can connect to multiple databases across an organization, empowering users to analyze data using chat.
- AI models can create 3D designs on Blender and print them out using a 3D printer.

## [​](https://modelcontextprotocol.io/docs/getting-started/intro\#why-does-mcp-matter%3F)  Why does MCP matter?

Depending on where you sit in the ecosystem, MCP can have a range of benefits.

- **Developers**: MCP reduces development time and complexity when building, or integrating with, an AI application or agent.
- **AI applications or agents**: MCP provides access to an ecosystem of data sources, tools and apps which will enhance capabilities and improve the end-user experience.
- **End-users**: MCP results in more capable AI applications or agents which can access your data and take actions on your behalf when necessary.

</details>


## Local Files

<details>
<summary>_Users_omar_Documents_ai_repos_course-ai-agents_lessons_14_agent_system_design_nova_system_design_notes</summary>

## Nova Research Agent — System Design

### Purpose
- **What**: A research automation agent built on the Model Context Protocol (MCP), split into an MCP server that exposes research tools/resources/prompts and an MCP client that orchestrates an LLM-driven ReAct loop to call those tools.
- **Where**: Server in `src/nova/mcp_server`, client in `src/nova/mcp_client`.
- **Why**: To execute the research workflow described in `mcp_server/src/prompts/research_instructions_prompt.py` and produce a comprehensive `research.md` from guidelines and web sources.

---

## High-level architecture

### Components
- **MCP Server** (`mcp_server`)
  - Entry point: `src/nova/mcp_server/src/server.py`
    - Builds a `FastMCP` instance and registers:
      - Tools: `src/nova/mcp_server/src/routers/tools.py`
      - Resources: `src/nova/mcp_server/src/routers/resources.py`
      - Prompts: `src/nova/mcp_server/src/routers/prompts.py`
  - Tool implementations in `src/nova/mcp_server/src/tools/` call application handlers in `src/nova/mcp_server/src/app/` and use helpers in `src/nova/mcp_server/src/utils/`.
  - Configuration and constants in `src/nova/mcp_server/src/config/`.

- **MCP Client** (`mcp_client`)
  - Entry point: `src/nova/mcp_client/src/client.py`
    - Transport options:
      - In-memory: imports the server and runs it in-process
      - Stdio: spawns `uv run -m src.server --transport stdio` under the server directory
    - On startup, lists server tools/resources/prompts and prints them.
    - Interactive loop: accepts user input and orchestrates an LLM ReAct loop to decide which MCP tools to call.
  - Message/agent helpers in `src/nova/mcp_client/src/utils/`:
    - `handle_message_utils.py`: routes user commands and normal messages
    - `handle_agent_loop_utils.py`: runs the LLM/tool ReAct loop and executes tools via `client.call_tool`
    - `llm_utils.py`: prepares Gemini tool schemas from MCP tools and parses LLM responses

### Communication
- The client queries server capabilities (`list_tools`, `list_resources`, `list_prompts`) and executes tools by name (`call_tool("toolName", {args...})`).
- The client maps MCP tool metadata to Gemini function declarations so the LLM can propose function calls. Automatic function calling is disabled; the client explicitly inspects the LLM response and executes tools accordingly.

---

## How the client and server work together

1. The client starts and establishes an MCP connection (in-memory or stdio).
2. The client fetches and prints available tools/resources/prompts.
3. The user can load the workflow prompt via `/prompt/full_research_instructions_prompt`, which inserts the instructions into the conversation history.
4. The user asks for a task (e.g., “Run the full research workflow for directory X”).
5. The client starts the ReAct loop:
   - Converts MCP tools into Gemini tool schemas.
   - Calls the LLM with conversation history.
   - If the LLM proposes a function call matching an MCP tool, the client executes it via `client.call_tool` and appends the tool result to the conversation.
   - Repeats until the LLM emits a final answer instead of a function call.

Notes:
- The research prompt encourages parallelism for certain steps; the current client loop executes tools sequentially (one function call at a time). Several server tools internally run concurrent workloads (e.g., web/YT scraping), so you still get parallelism inside tool execution.

---

### Prompts
- `full_research_instructions_prompt` → returns the workflow instructions from `prompts/research_instructions_prompt.py`.

---

## Workflow mapping (from research_instructions_prompt.py)
Below, each step from the prompt is mapped to the exact tool(s) on the server with precise inputs/outputs as implemented.

### Step 1 — Setup
- User loads the instructions (optional but recommended) via `/prompt/full_research_instructions_prompt`.
- All subsequent tools require a `research_directory` that contains:
  - `article_guideline.md` (the prompt references this as `ARTICLE_GUIDELINE_FILE`)
  - A hidden `.nova/` folder that tools will create/populate as needed

### Step 1.3 — Extract URLs from guidelines
- MCP Tool: `extract_guidelines_urls(research_directory: str)`
  - Implementation: `tools/extract_guidelines_urls_tool.py`
  - Reads: `article_guideline.md`
  - Writes: `.nova/guidelines_filenames.json`
  - Output (dict):
    - `status`: "success"
    - `github_sources_count`: int
    - `youtube_sources_count`: int
    - `web_sources_count`: int
    - `local_files_count`: int
    - `output_path`: absolute path to `.nova/guidelines_filenames.json`
    - `message`: human-readable summary
  - File schema written to `.nova/guidelines_filenames.json` (keys):
    - `github_urls`: list[str]
    - `youtube_videos_urls`: list[str]
    - `other_urls`: list[str]
    - `local_file_paths`: list[str]
  - Important: Downstream tools expect different key names for local files (see callouts below).

---

## Step 2 — Process extracted resources (tools can be run independently)

### 2.1 Local files
- MCP Tool: `process_local_files(research_directory: str)`
  - Implementation: `tools/process_local_files_tool.py`
  - Reads: `.nova/guidelines_filenames.json`
  - Writes: `.nova/local_files_from_research/` copies or converted notebooks
  - Output (dict):
    - `status`: "success" or "warning" (if 0 files processed)
    - `files_processed`: int
    - `files_total`: int
    - `processed_files`: list[str] (filenames saved inside destination)
    - `warnings`: list[str]
    - `errors`: list[str]
    - `output_directory`: absolute path to `.nova/local_files_from_research/`
    - `message`: summary string
  - Expected JSON keys: The implementation uses `data.get("local_files", [])`. However, the extractor writes `local_file_paths`. If you run this step as-is, no files will be processed unless `.nova/guidelines_filenames.json` contains `local_files`. Adjustments may be required (see “Notable implementation notes”).

### 2.2 Other HTTP/HTTPS URLs (non-GitHub, non-YouTube)
- MCP Tool: `scrape_and_clean_other_urls(research_directory: str, concurrency_limit: int = 4)`
  - Implementation: `tools/scrape_and_clean_other_urls_tool.py`
  - Reads: `.nova/guidelines_filenames.json` → `other_urls`, `article_guideline.md`
  - Internals: Concurrent scraping with Firecrawl; LLM-based markdown cleaning; filenames generated safely
  - Writes: `.nova/urls_from_guidelines/*.md`
  - Output (dict):
    - `status`: "success" or "warning" (if 0 successful scrapes)
    - `urls_processed`: int (successful scrapes)
    - `urls_total`: int (attempted)
    - `files_saved`: int
    - `output_directory`: absolute path to `.nova/urls_from_guidelines/`
    - `saved_files`: list[str]
    - `message`: summary string

### 2.3 GitHub URLs
- MCP Tool: `process_github_urls(research_directory: str)`
  - Implementation: `tools/process_github_urls_tool.py`
  - Reads: `.nova/guidelines_filenames.json` → `github_urls`
  - Internals: Uses `gitingest.ingest_async` to summarize repo, tree, and content; truncates and strips base64 images; sequential by URL
  - Writes: `.nova/urls_from_guidelines_code/*.md`
  - Output (dict):
    - `status`: "success" or "warning"
    - `urls_processed`: int
    - `urls_total`: int
    - `files_saved`: int
    - `output_directory`: absolute path to `.nova/urls_from_guidelines_code/`
    - `message`: summary

### 2.4 YouTube URLs
- MCP Tool: `transcribe_youtube_urls(research_directory: str)`
  - Implementation: `tools/transcribe_youtube_videos_tool.py`
  - Reads: `.nova/guidelines_filenames.json` → `youtube_videos_urls`
  - Internals: Gemini-based transcription with retries, limited concurrency
  - Writes: `.nova/urls_from_guidelines_youtube_videos/*.md`
  - Output (dict):
    - `status`: "success"
    - `videos_processed`: int
    - `videos_total`: int
    - `output_directory`: absolute path to `.nova/urls_from_guidelines_youtube_videos/`
    - `message`: summary

---

## Step 3 — Research loop (repeatable)

### 3.1 Generate next queries
- MCP Tool: `generate_next_queries(research_directory: str, n_queries: int = 5)`
  - Implementation: `tools/generate_next_queries_tool.py`
  - Reads: `article_guideline.md`, `.nova/perplexity_results.md` (if exists), `.nova/urls_from_guidelines/*.md`
  - Writes: `.nova/next_queries.md` (overwrites)
  - Output (dict):
    - `status`: "success"
    - `queries_count`: int
    - `queries`: list[tuple[str, str]] → [(query, reason), ...]
    - `output_path`: absolute path to `.nova/next_queries.md`
    - `message`: summary + formatted query list

### 3.2 Run Perplexity research for those queries
- MCP Tool: `run_perplexity_research(research_directory: str, queries: list[str])`
  - Implementation: `tools/run_perplexity_research_tool.py`
  - Reads: None mandatory; creates/updates results file
  - Internals: Structured Perplexity call, appends normalized “Source [id]” sections
  - Writes: `.nova/perplexity_results.md` (appends)
  - Output (dict):
    - `status`: "success"
    - `queries_processed`: int
    - `sources_added`: int (number of source blocks appended)
    - `output_path`: absolute path to `.nova/perplexity_results.md`
    - `message`: summary

---

## Step 4 — Filter Perplexity results by quality

### 4.1 Select sources to keep
- MCP Tool: `select_research_sources_to_keep(research_directory: str)`
  - Implementation: `tools/select_research_sources_to_keep_tool.py`
  - Reads: `article_guideline.md`, `.nova/perplexity_results.md`
  - Writes:
    - `.nova/perplexity_sources_selected.md`: comma-separated IDs
    - `.nova/perplexity_results_selected.md`: filtered markdown containing only selected source blocks
  - Output (dict):
    - `status`: "success"
    - `sources_selected_count`: int
    - `selected_source_ids`: list[int]
    - `sources_selected_path`: absolute path to IDs file
    - `results_selected_path`: absolute path to filtered results file
    - `message`: summary

---

## Step 5 — Identify accepted sources to scrape fully

### 5.1 Select research sources to scrape
- MCP Tool: `select_research_sources_to_scrape(research_directory: str, max_sources: int = 5)`
  - Implementation: `tools/select_research_sources_to_scrape_tool.py`
  - Reads: `article_guideline.md`, `.nova/perplexity_results_selected.md`, content from `.nova/urls_from_guidelines/*.md`
  - Writes: `.nova/urls_to_scrape_from_research.md` (one URL per line)
  - Output (dict):
    - `status`: "success"
    - `urls_selected_count`: int
    - `selected_urls`: list[str]
    - `selection_reasoning`: str
    - `urls_output_path`: absolute path to `.nova/urls_to_scrape_from_research.md`
    - `message`: summary

### 5.2 Scrape selected research URLs (full content)
- MCP Tool: `scrape_research_urls(research_directory: str, concurrency_limit: int = 4)`
  - Implementation: `tools/scrape_research_urls_tool.py`
  - Reads: `.nova/urls_to_scrape_from_research.md`; optionally deduplicates against `.nova/guidelines_filenames.json` (`other_urls` + `github_urls`)
  - Categorizes: YouTube vs other URLs; transcribes YouTube; scrapes/cleans other URLs concurrently
  - Writes: `.nova/urls_from_research/*.md`
  - Output (dict):
    - `status`: "success" or "warning"
    - `urls_processed`: int (successful scrapes for non-YouTube; YouTube transcriptions are not counted in `urls_processed` but appear in the report message)
    - `urls_total`: int (new URLs after deduplication, both categories)
    - `original_urls_count`: int (before deduplication)
    - `deduplicated_count`: int
    - `files_saved`: int
    - `output_directory`: absolute path to `.nova/urls_from_research/`
    - `saved_files`: list[str]
    - `message`: summary

---

## Step 6 — Generate final research file

### 6.1 Create `research.md`
- MCP Tool: `create_research_file(research_directory: str)`
  - Implementation: `tools/create_research_file_tool.py`
  - Reads (if present):
    - Preferred: `.nova/perplexity_results_selected.md`
    - Fallback: `.nova/perplexity_results.md`
    - Plus sections from:
      - `.nova/urls_from_research/*.md`
      - `.nova/urls_from_guidelines_code/*.md`
      - `.nova/urls_from_guidelines_youtube_videos/*.md`
      - `.nova/urls_from_guidelines/*.md`
  - Writes: `research.md` at the root of `research_directory`
  - Output (dict):
    - `status`: "success"
    - `markdown_file`: absolute path to `research.md`
    - `research_results_count`: int (number of grouped query sections)
    - `scraped_sources_count`: int (from `urls_from_research`)
    - `code_sources_count`: int (from `urls_from_guidelines_code`)
    - `youtube_transcripts_count`: int (from `urls_from_guidelines_youtube_videos`)
    - `additional_sources_count`: int (from `urls_from_guidelines`)
    - `message`: summary

---

## Files, folders, and constants
Key constants from `mcp_server/src/config/constants.py`:
- Files written under `.nova/`:
  - `guidelines_filenames.json`
  - `perplexity_results.md`
  - `perplexity_results_selected.md`
  - `perplexity_sources_selected.md`
  - `next_queries.md`
  - `urls_to_scrape_from_research.md`
  - Folders: `urls_from_guidelines/`, `urls_from_guidelines_code/`, `urls_from_guidelines_youtube_videos/`, `local_files_from_research/`, `urls_from_research/`
- Root files:
  - `article_guideline.md` (input)
  - `research.md` (final output)

---

## Notable implementation notes and edge cases
- **Local files key mismatch**:
  - Extractor writes `local_file_paths` in `.nova/guidelines_filenames.json`.
  - `process_local_files_tool` reads `local_files`.
  - If unchanged, no local files will be processed by step 2.1. Resolve by aligning the key (either update the extractor to write `local_files` or adjust the processing tool to read `local_file_paths`).
- **Parallelism**:
  - The server tools implement async concurrency internally (web/YT scraping and transcription). The client’s ReAct loop executes tools one at a time; true cross-tool parallelism would require client-side orchestration changes.
- **Perplexity result format**:
  - Results are appended as normalized blocks: `### Source [id]: <url>`, plus `Query:` and `Answer:` sections, separated by `-----`. Several downstream parsers depend on this format.
- **YouTube transcription**:
  - Concurrency limited via `YOUTUBE_TRANSCRIPTION_MAX_CONCURRENT_REQUESTS`; retried on server errors, timeouts are handled with messages written to files.
- **GitHub processing**:
  - `gitingest` output is sanitized to remove base64 image payloads and truncated if too long.
- **Scraping**:
  - Uses Firecrawl with a 1-week cache for speed; content cleaned via LLM prompt constrained to removal of non-content elements.

---

## End-to-end flow summary
1. Load instructions prompt (optional).
2. Run `extract_guidelines_urls` to seed `.nova/guidelines_filenames.json`.
3. Process extracted resources:
   - `process_local_files` (requires `local_files` key) → copies/exports referenced files
   - `scrape_and_clean_other_urls` → `.nova/urls_from_guidelines/`
   - `process_github_urls` → `.nova/urls_from_guidelines_code/`
   - `transcribe_youtube_urls` → `.nova/urls_from_guidelines_youtube_videos/`
4. Repeat research loop:
   - `generate_next_queries` → `.nova/next_queries.md`
   - `run_perplexity_research` → append to `.nova/perplexity_results.md`
5. Curate results:
   - `select_research_sources_to_keep` → filter IDs and selected results
   - `select_research_sources_to_scrape` → write `.nova/urls_to_scrape_from_research.md`
6. Scrape full sources: `scrape_research_urls` → `.nova/urls_from_research/`
7. Compile final output: `create_research_file` → `research.md`.

</details>
