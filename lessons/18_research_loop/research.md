# Research

## Research Results

<details>
<summary>What are best practices for implementing human-in-the-loop (HITL) feedback gates in autonomous AI agents for tasks like research?</summary>

### Source [1]: https://www.getmaxim.ai/articles/incorporating-human-in-the-loop-feedback-for-continuous-improvement-of-ai-agents/

Query: What are best practices for implementing human-in-the-loop (HITL) feedback gates in autonomous AI agents for tasks like research?

Answer: Best practices for implementing human-in-the-loop (HITL) feedback gates in autonomous AI agents revolve around strategically leveraging human judgment to validate, improve, and guide agent behavior. Effective HITL systems focus human attention on high-value scenarios, such as validating automated evaluations, investigating edge cases, analyzing user complaints, and reviewing interactions flagged as uncertain by automated systems. To maximize efficiency and impact, teams should:

- Identify which cases require human judgment and design workflows that direct human reviewers to genuinely ambiguous or novel scenarios.
- Streamline the review process so human oversight is applied only where it adds unique value, not on obvious passes or failures.
- Build data pipelines that systematically analyze raw human feedback, aggregating trends to detect quality regressions or validate improvements.
- Curate human feedback into evolving datasets, expanding test sets with challenging cases and leveraging disagreements between human and automated evaluations for future improvements.
- Implement real-time feedback integration, allowing agents to escalate ambiguous or high-stakes decisions to humans and enabling interactive correction during agent execution.
- Use production guardrails defined by human experts to prevent agents from taking high-risk actions without approval, maintaining safety while allowing autonomy in routine cases.

Teams report substantial efficiency gains (10-15x) when using structured HITL workflows compared to ad hoc manual review. Continuous dataset evolution from human feedback ensures agents adapt to new scenarios and maintain alignment with user expectations. Ultimately, automation and human oversight should be viewed as complementary, with human expertise reserved for quality-critical decisions and ambiguous cases, while routine assessments are handled by automated systems.

-----

-----

### Source [2]: https://galileo.ai/blog/human-in-the-loop-strategies-for-ai-agents

Query: What are best practices for implementing human-in-the-loop (HITL) feedback gates in autonomous AI agents for tasks like research?

Answer: Effective HITL feedback gates for autonomous AI agents include establishing robust feedback loops where every human intervention becomes a teaching moment for the AI. Human agents contribute to the knowledge base through structured feedback mechanisms. Key metrics to monitor for triggering human handoffs are:

- **AI confidence scores:** When the agent's confidence drops below a defined threshold, human review is initiated.
- **Keyword or compliance triggers:** Detection of specific words or regulatory flags prompts human involvement.
- **User frustration signals:** Patterns indicating user dissatisfaction or confusion call for human judgment.
- **Complex query indicators:** Queries that are too complex for automated handling are routed to humans.

By systematically monitoring these metrics, HITL gates ensure that ambiguous, risky, or novel situations are escalated for human review. Each human interaction is logged and utilized to train and refine the AI system, creating a continuous improvement cycle. This strategy ensures that the AI agent learns from real-world corrections and edge cases, enhancing its decision-making capabilities over time.

-----

-----

### Source [3]: https://workos.com/blog/why-ai-still-needs-you-exploring-human-in-the-loop-systems

Query: What are best practices for implementing human-in-the-loop (HITL) feedback gates in autonomous AI agents for tasks like research?

Answer: HITL is a purposeful design approach that incorporates human intervention at key points in the AI lifecycle. Best practices include:

- **Pre-processing gates:** Humans shape AI behavior before task execution by providing context and assumptions. This ensures the agent starts with correct parameters.
- **Mid-process feedback gates:** During execution, certain actions or decisions are paused until human input is received, making HITL a first-class control mechanism. Mechanisms include Slack bot approvals, dashboard status indicators, and API hooks that gate progression until sign-off.
- **Active learning & continual feedback:** Human corrections and overrides are logged and used as training data, enabling the system to learn and adapt over time to organizational norms and user preferences.
- **Auditability:** All human interventions, especially overrides and rejections, are logged with rationales, ensuring transparency and traceability, which is crucial for regulated environments.
- **Scalability and routing:** Systems must efficiently determine when human intervention is needed and route decisions to the appropriate reviewers, preventing bottlenecks.
- **Mitigation of human error:** Safeguards are necessary to validate and learn from human feedback, as human reviewers can be inconsistent or fatigued.

HITL is not just a manual override but a scalable, programmable principle where human judgment complements machine efficiency. This partnership elevates both safety and intelligence in autonomous agent workflows.

-----

-----

### Source [4]: https://xenoss.io/blog/human-in-the-loop-data-quality-validation

Query: What are best practices for implementing human-in-the-loop (HITL) feedback gates in autonomous AI agents for tasks like research?

Answer: Human-in-the-loop validation is optimal for enterprise AI dealing with complex, domain-specific tasks where data accuracy is critical. Best practices for HITL feedback gates include:

- **Combining automated and human review:** Use automated validation for scalable processing, but integrate human expertise where contextual judgment is needed, especially for high-stakes decisions.
- **Strategic deployment of human reviewers:** Route ambiguous or high-impact cases to human experts, ensuring that only the most critical decisions require human oversight, avoiding reviewer fatigue and inefficiency.
- **Quality assurance:** Human reviewers catch subtle errors that automated systems might miss, preventing cascading mistakes in downstream applications.
- **Continuous improvement:** Feedback from human reviewers is used to improve both the AI model and the validation pipeline, ensuring that the system learns from mistakes and edge cases.

This approach ensures scalable data processing while maintaining reliable quality assurance, particularly for research tasks where incorrect outputs could have significant consequences.

-----

</details>

<details>
<summary>How does concurrent execution of API calls, such as using Python's asyncio, improve the performance and cost-efficiency of LLM-based workflows?</summary>

### Source [5]: https://python.useinstructor.com/blog/2023/11/13/learn-async/

Query: How does concurrent execution of API calls, such as using Python's asyncio, improve the performance and cost-efficiency of LLM-based workflows?

Answer: Concurrent execution of API calls in LLM-based workflows using Python's asyncio provides significant improvements in both performance and cost-efficiency. Using methods like `asyncio.gather`, all tasks are executed concurrently, which drastically reduces overall execution time compared to sequential processing. For example, processing 7 items sequentially took 6.17 seconds, while using `asyncio.gather` reduced this to just 0.85 seconds. The method `asyncio.as_completed` enables results to be processed as soon as they complete, which is beneficial for streaming data and handling large datasets efficiently. Rate limiting can be integrated using semaphores to comply with API quotas and avoid service throttling, balancing throughput and resource consumption for production workloads. The guide highlights that `asyncio.gather` is fastest when ordered results are needed, while `asyncio.as_completed` is ideal for streaming workflows. Rate limiting ensures respect for external APIs and controls cost by reducing unnecessary calls and retries. Overall, these techniques enable faster, more resource-efficient, and cost-effective LLM-based processing.

-----

-----

### Source [6]: https://faun.pub/how-to-speed-up-your-python-scripts-with-asyncio-aeafd786c788

Query: How does concurrent execution of API calls, such as using Python's asyncio, improve the performance and cost-efficiency of LLM-based workflows?

Answer: Using asyncio for concurrent API calls in Python scripts enhances the performance of LLM-based workflows by allowing thousands of operations to be handled simultaneously without blocking the main thread. This leads to improved efficiency for I/O-bound tasks such as LLM API calls, reduced execution time since tasks run concurrently, and lower resource consumption because fewer threads are required compared to threading or multiprocessing. The result is faster workflows and enhanced responsiveness, making asyncio particularly suitable for applications like web servers or batch LLM inference where quick turnaround is essential.

-----

-----

### Source [7]: https://www.unite.ai/asynchronous-llm-api-calls-in-python-a-comprehensive-guide/

Query: How does concurrent execution of API calls, such as using Python's asyncio, improve the performance and cost-efficiency of LLM-based workflows?

Answer: Asynchronous programming in Python, such as with asyncio, allows multiple LLM API calls to be executed concurrently, which avoids blocking the main thread. This is especially valuable when processing large batches, such as generating summaries for 100 articles: a synchronous approach would process each call sequentially, taking several minutes, while an asynchronous approach can initiate all calls nearly simultaneously, dramatically reducing the total execution time. By leveraging `asyncio.gather` with a semaphore for rate limiting, you can maximize concurrency while respecting API usage limits, leading to both time and cost savings by improving throughput and reducing idle wait times.

-----

-----

### Source [8]: https://dev.to/leapcell/high-performance-python-asyncio-4jkj

Query: How does concurrent execution of API calls, such as using Python's asyncio, improve the performance and cost-efficiency of LLM-based workflows?

Answer: Asyncio's concurrent execution is highly efficient for I/O-bound tasks, such as LLM API calls, because it enables a large number of tasks to be managed with minimal overhead. Unlike multithreading, asyncio has a lower cost for task switching and can handle many more concurrent activities due to its coroutine-based design. This means that workflows that involve frequent and slow I/O operations, like batch LLM inference, benefit from higher throughput and reduced waiting times, which translates directly into better resource utilization and cost efficiency.

-----

-----

### Source [9]: https://www.dataleadsfuture.com/harnessing-multi-core-power-with-asyncio-in-python/

Query: How does concurrent execution of API calls, such as using Python's asyncio, improve the performance and cost-efficiency of LLM-based workflows?

Answer: Executing concurrent tasks with asyncio can utilize multiple CPU cores when integrated with multiprocessing, further accelerating LLM-based workflows by spreading the workload across all available cores. This multi-core approach, combined with asyncio's ability to efficiently manage thousands of concurrent tasks, results in much faster execution compared to traditional sequential or single-threaded methods. For LLM API calls, this means more requests can be processed in less time, improving both performance and cost-effectiveness, especially at scale.

-----

-----

### Source [10]: https://python.plainenglish.io/how-i-scaled-my-python-scripts-with-asyncio-from-slow-loops-to-lightning-fast-pipelines-4b2b3653ca0a

Query: How does concurrent execution of API calls, such as using Python's asyncio, improve the performance and cost-efficiency of LLM-based workflows?

Answer: By adopting asyncio for concurrent execution, Python scripts can be transformed from slow, blocking loops into high-throughput pipelines that handle thousands of I/O-bound operations efficiently. This non-blocking paradigm is particularly advantageous for LLM-based workflows, as it reduces idle time waiting for API responses and allows for better scaling without a proportional increase in resource usage. The net effect is faster processing, reduced infrastructure costs, and improved overall efficiency in handling large-scale LLM tasks.

-----

</details>

<details>
<summary>What are the advantages of using a specialized search API like Perplexity over a general-purpose LLM for building a research agent?</summary>

### Source [11]: https://alphacorp.ai/perplexity-search-api-vs-tavily-the-better-choice-for-rag-and-agents-in-2025/

Query: What are the advantages of using a specialized search API like Perplexity over a general-purpose LLM for building a research agent?

Answer: The Perplexity Search API is designed for ultra-low-latency, filtered web searches, providing results with metadata in under 400 milliseconds at median latency. This makes it highly suitable for agentic research systems that require frequent, iterative queries in multi-step research loops. Its per-request pricing (no token costs) simplifies budgeting, especially for agents that orchestrate many tool calls per session. Key advantages include:

- Sub-second response times support conversational flow and rapid multi-step reasoning.
- Flexible filtering by domain and recency allows programmatic narrowing of search space, critical for focused research.
- Agents can pair the Search API with custom extraction logic or escalate to Perplexity’s Grounded LLMs for deeper synthesis as needed, creating a modular research pipeline.
- The system excels in scenarios requiring high search volume, low cost per query, and integration with existing content extraction infrastructure.

In contrast to unified systems that return LLM-ready snippets, Perplexity’s approach gives developers more control over extraction and synthesis, optimizing for speed and filtering precision. This is particularly valuable for investigative tools, market intelligence bots, and technical research assistants where the retrieval layer must be both fast and programmable. The architecture is especially advantageous when strict latency budgets, cost transparency, and filtering flexibility are priorities.

-----

-----

### Source [12]: https://beam.ai/llm/perplexity/

Query: What are the advantages of using a specialized search API like Perplexity over a general-purpose LLM for building a research agent?

Answer: Perplexity provides several notable advantages over general-purpose LLMs for building research agents:

- Real-time information retrieval with source citations, ensuring up-to-date, accurate, and transparent responses.
- Significant reduction in hallucinations due to reliance on sourced, live search results rather than solely LLM-generated content.
- Superior response quality, with answers grounded in multiple sources and citations, increasing user trust and result reliability.
- Advanced support for complex, multi-step processes and workflows, enabling automation of sophisticated research tasks that would otherwise require human intervention.
- A range of specialized models (e.g., Sonar Pro, Sonar, Llama-3.1-sonar series) tailored to different use cases, each optimized for search grounding and advanced queries.

These features collectively make Perplexity especially well-suited for research agents that demand real-time, factual, and citation-backed outputs with the ability to handle iterative research and complex problem-solving.

-----

-----

### Source [13]: https://slashdot.org/software/comparison/LLM-API-vs-Perplexity-AI/

Query: What are the advantages of using a specialized search API like Perplexity over a general-purpose LLM for building a research agent?

Answer: Perplexity AI distinguishes itself from general-purpose LLM APIs by integrating live search functionality into its response generation pipeline. It is designed to provide precise and context-aware answers to both broad and detailed queries by summarizing information from multiple sources in real time. This approach ensures that research agents built on Perplexity can access current, accurate information, rather than relying solely on static, pre-trained model knowledge. The system supports fast, web-based retrieval, making it effective for research scenarios where up-to-date and multi-source information is essential.

-----

-----

### Source [14]: https://trilogyai.substack.com/p/comparative-analysis-of-deep-research

Query: What are the advantages of using a specialized search API like Perplexity over a general-purpose LLM for building a research agent?

Answer: Perplexity’s Deep Research offers high automation in knowledge extraction for research agents. Upon receiving a query, it autonomously conducts dozens of searches and reviews hundreds of sources, completing in minutes what would take a human many hours. For straightforward factual queries, Perplexity's agent demonstrates very strong accuracy (93.9% on the SimpleQA benchmark), outperforming most competitors in basic factual correctness. Its iterative search and refinement process, coupled with the ability to execute code (e.g., summarizing statistics from sources), provides robust support for agents that need to synthesize, aggregate, and reason over large volumes of information. The agent’s workflow—iterative searching, refining, and integration of coding—makes it particularly capable for automated, multi-step research tasks.

-----

</details>

<details>
<summary>What are effective strategies for autonomous query generation in AI research agents to identify and fill knowledge gaps?</summary>

### Source [15]: https://arxiv.org/html/2508.12752v1

Query: What are effective strategies for autonomous query generation in AI research agents to identify and fill knowledge gaps?

Answer: **Effective strategies for autonomous query generation in AI research agents** are detailed in the deep research pipeline, particularly in the 'Question Developing' stage. This stage emphasizes the need for agents to dynamically generate diverse and contextualized queries tailored to evolving sub-goals and accumulated evidence, rather than relying on static or pre-defined queries. Key strategies include:

- **Adaptive Query Generation**: Agents formulate queries based on the current sub-goal and previous evidence, ensuring queries are both precise and broad enough to gather relevant information and fill knowledge gaps.

- **Reinforcement Learning (RL) Optimization**: RL allows agents to optimize query generation policies by interacting with the search environment and receiving feedback based on task-specific rewards. These rewards may include answer accuracy, retrieval coverage, and search efficiency. For example, DeepRetrieval aligns query generation with retrieval metrics like Recall@K and NDCG@K, while MaskSearch combines format and accuracy into unified rewards linked to retrieval-augmented prediction.

- **Structured Multi-Agent Systems**: Modular approaches, such as ManuSearch, divide the query development process among specialized agents (e.g., planning, searching, evidence extraction), enabling transparent and controllable query generation. This modularity supports complex query decomposition and information synthesis.

- **Supervision-Driven Methods**: Agents can be fine-tuned or guided by supervised learning and rule-based templates, which mimic human-written queries. These methods improve query structure, semantic fidelity, and stability, especially in low-resource settings or noisy environments.

These strategies allow agents to reason about the utility of queries, adapt query behavior over time, and diagnose failures, thus effectively identifying and filling knowledge gaps in autonomous research tasks.

-----

-----

### Source [16]: https://gradientflow.substack.com/p/autonomous-ai-agents-are-changing

Query: What are effective strategies for autonomous query generation in AI research agents to identify and fill knowledge gaps?

Answer: Autonomous deep research tools employ several strategies to generate queries and fill knowledge gaps:

- **Multi-Agent Collaboration:** Agents are divided by roles, such as planners who decompose the main research query into sub-questions, and researcher agents who perform targeted web queries for each sub-question. This breakdown ensures coverage of different facets of a topic and reduces the risk of missing important information.

- **Iterative Search and Reasoning:** After gathering initial data, agents analyze findings and refine subsequent queries, iteratively deepening their investigation. This loop continues until the agents judge that knowledge gaps are sufficiently filled, or no further relevant information can be retrieved.

- **Hybrid System Integration:** These research agents combine conversational AI, autonomous web browsing, and tool use (such as document or PDF analysis), allowing them to access diverse data sources and formats, which broadens their ability to identify and address knowledge gaps.

- **Reinforcement Learning and Fine-Tuning:** Some advanced agents, like OpenAI’s Deep Research, utilize reinforcement learning to improve query strategies based on the accuracy and relevance of retrieved information. Regular fine-tuning helps agents adapt to new domains and user requirements.

- **Customizable Planning:** Platforms like Google Gemini’s Deep Research allow users to refine the agent’s research plan before execution, ensuring that initial query generation is tightly aligned with user intent and topic scope. This planning step helps agents focus on the most critical knowledge gaps from the outset.

- **Open Source Prototyping:** Projects such as GPT-Researcher use recursive branching and unbiased retrieval to autonomously build citation-rich, comprehensive reports, demonstrating effective query decomposition and gap identification in practice.

These strategies collectively enable autonomous agents to systematically identify, prioritize, and fill gaps in knowledge during complex research tasks.

-----

-----

### Source [17]: https://aws.amazon.com/blogs/aws-insights/the-rise-of-autonomous-agents-what-enterprise-leaders-need-to-know-about-the-next-wave-of-ai/

Query: What are effective strategies for autonomous query generation in AI research agents to identify and fill knowledge gaps?

Answer: Enterprise-focused autonomous AI agents employ strategies for query generation and knowledge gap filling that center on adaptability and multi-source integration:

- **Adaptive Approach:** Agents do not follow fixed workflows but instead adapt their process dynamically based on information gathered at each step. This enables them to identify gaps as they emerge and adjust queries accordingly.

- **Retrieval-Augmented Generation (RAG):** Agents access multiple knowledge bases and use RAG to enhance query relevance. By pulling information from various structured and unstructured sources, agents can cross-reference findings and spot inconsistencies or gaps.

- **Complex Query Execution:** Integration with internal APIs and databases allows agents to execute sophisticated queries beyond simple keyword searches, targeting specific knowledge gaps relevant to enterprise tasks (e.g., biomarker validation in biotech).

- **Feedback Loops:** Agents use feedback from query outcomes (such as retrieval success or failure) to inform subsequent query generation, iteratively refining their approach to close gaps in knowledge.

These strategies are designed to automate manual research efforts, accelerate innovation, and improve the completeness and accuracy of enterprise knowledge discovery.

-----

</details>

<details>
<summary>How does an iterative design process benefit the development of complex, multi-step AI agent workflows like a research loop?</summary>

### Source [18]: https://www.glean.com/ai-glossary/agent-loop

Query: How does an iterative design process benefit the development of complex, multi-step AI agent workflows like a research loop?

Answer: An iterative, loop-based approach is fundamental to AI agent workflows, especially in multi-step, complex processes such as a research loop. Agent loops allow AI agents to break down intricate tasks into manageable cycles. The agent performs actions, evaluates intermediate results, and refines its strategy or attempts corrections when failures occur. This cycle repeats until the task meets predefined criteria or achieves the desired outcome. Such a design enables more thorough problem-solving, as each iteration incorporates feedback and adjustments based on new data or results. This leads to higher-quality outcomes and more reliable automation, as the agent can respond dynamically to unforeseen challenges or incomplete information at each step. However, the source also notes the importance of balancing thoroughness with efficiency: overly complex loops may result in diminishing returns or increased resource consumption. Despite technical challenges and concerns about return on investment, iterative loops remain a backbone for robust, flexible AI automation in enterprise settings.

-----

-----

### Source [19]: https://www.neuralconcept.com/post/the-iterative-design-process-a-step-by-step-guide-the-role-of-deep-learning

Query: How does an iterative design process benefit the development of complex, multi-step AI agent workflows like a research loop?

Answer: The iterative design process enables continuous improvement by repeatedly testing and refining outputs using simulation and feedback. In the context of AI agent workflows, this means that each iteration allows for evaluation against objectives and requirements, supporting adaptation to changing needs, user feedback, or unforeseen constraints. The process encourages the exploration of multiple alternatives, increasing the chance of finding effective solutions for complex, multi-step problems. Deep learning and AI accelerate this cycle by enabling rapid simulation and evaluation, drastically reducing the time needed between iterations and allowing for scalability and long-term maintenance. The inclusion of stakeholders and users throughout the iterative process also ensures that the evolving workflow stays aligned with real-world needs and expectations. Ultimately, feedback and incremental improvements are essential for robust, adaptable AI agent workflows, especially when requirements or external factors evolve over time.

-----

-----

### Source [20]: https://dovetail.com/product-development/iterative-design/

Query: How does an iterative design process benefit the development of complex, multi-step AI agent workflows like a research loop?

Answer: Iterative design provides rapid issue resolution and adaptability, both critical for complex, multi-step AI agent workflows like research loops. By breaking development into smaller, repeatable chunks, teams can identify and address problems early, implement changes at any stage, and track progress with greater clarity. This visibility into the process facilitates risk-taking and innovation, as new ideas can be trialed and refined without heavy upfront investment. Documentation and communication are also streamlined, which is particularly useful in multi-agent or collaborative workflows. Moreover, frequent prototyping and testing against real user behavior (rather than just stated requirements) helps ensure that the end-to-end workflow is truly effective and user-aligned.

-----

-----

### Source [21]: https://www.studiographene.com/blog/10-benefits-of-iterative-development-for-product-design-success

Query: How does an iterative design process benefit the development of complex, multi-step AI agent workflows like a research loop?

Answer: Iterative development in AI agent workflows promotes innovation, flexibility, and quality by leveraging continuous feedback and collaboration. Each iteration incorporates real user insights, which helps refine and align the workflow with evolving requirements or market conditions. This approach allows for faster project turnaround, early validation of concepts, and reduction of development risks. Testing and validation after each cycle enables early identification and correction of issues, preventing costly failures in later stages. The iterative process also increases engagement among stakeholders and fosters a culture of continuous improvement. Integrating regulatory compliance and operational feedback into each cycle ensures the final workflow is robust, efficient, and meets both user and business needs.

-----

-----

### Source [22]: https://www.pacific-research.com/5-advantages-of-iterative-design-and-prototyping-prl/

Query: How does an iterative design process benefit the development of complex, multi-step AI agent workflows like a research loop?

Answer: Iterative design and prototyping offer several advantages for developing complex AI agent workflows. These include increased efficiency and faster time to market, as problems are identified and addressed early in the cycle. Iterative methods lower overall development costs by reducing the number of major redesigns needed, since issues are resolved incrementally. Thorough testing at each stage ensures that the final workflow is robust and user-friendly, as each step is validated and improved before moving forward. The ongoing feedback and refinement also lead to solutions that better fit user needs and expectations, which is crucial in multi-step or research-oriented AI agent workflows.

-----

</details>

<details>
<summary>What are the best practices for designing server-hosted prompts in Model Context Protocol (MCP) to orchestrate multi-step, stateful agentic workflows?</summary>

### Source [23]: https://modelcontextprotocol.io/specification/2025-06-18/server/prompts

Query: What are the best practices for designing server-hosted prompts in Model Context Protocol (MCP) to orchestrate multi-step, stateful agentic workflows?

Answer: The official MCP specification describes best practices for designing server-hosted prompts that orchestrate multi-step, stateful agentic workflows:

- **Prompts are server-defined, user-controlled templates**. Servers expose prompts for clients to discover and invoke, typically via user-initiated commands in the UI.

- **Prompt Definition Structure:** Each prompt includes a unique `name`, human-readable `title` and `description`, and a list of customizable `arguments` for parameterization. This allows prompts to be tailored to each workflow instance.

- **Prompt Messages:** Prompts are composed of structured messages, each with a `role` ("user" or "assistant") and `content` (text or embedded resource). Messages can include annotations for metadata like audience, priority, and modification time. Embedded resources enable referencing server-side data (text or binary) directly within a prompt.

- **Discovery and Retrieval:** Servers must declare the `prompts` capability, support the `prompts/list` (paginated) and `prompts/get` methods, and may send notifications when prompt lists change. This ensures clients can always access the latest templates.

- **Error Handling:** Servers should use standard JSON-RPC errors for invalid prompt names, missing required arguments, or internal errors, and validate all prompt arguments before processing requests.

- **Stateful Orchestration:** By chaining multiple prompt messages (with roles and arguments), servers can encode multi-step workflows, guide agent behavior, and maintain state across interactions. Prompts can reference dynamic resources for richer, context-aware workflows.

- **Implementation Guidance:** Both servers and clients should respect capability negotiation, validate arguments, and handle prompt list pagination for scalability.

-----

-----

### Source [24]: https://machinelearningmastery.com/the-complete-guide-to-model-context-protocol/

Query: What are the best practices for designing server-hosted prompts in Model Context Protocol (MCP) to orchestrate multi-step, stateful agentic workflows?

Answer: The guide explains that MCP prompts are reusable templates encoding expert knowledge for specific tasks, simplifying complex model instructions. Prompts:

- **Contain arguments** for customization, allowing the same template to be adapted to different workflows or contexts.

- **Support dynamic context insertion**, i.e., the server expands the prompt by incorporating arguments and relevant context before returning it to the client. This mechanism is essential for multi-step workflows, as each step can reference the evolving context.

- **Are discovered via standardized methods** (`prompts/list`), supporting workflow composition and orchestration.

- **Prompt retrieval uses `prompts/get`** with specific arguments, ensuring precise control over prompt content and workflow state.

- **Workflow orchestration:** By combining prompt templates with dynamic arguments, servers can implement agentic workflows that evolve with user or environment state, with each prompt step reflecting the current context and requirements.

This approach ensures that agentic workflows are both stateful (arguments and context drive behavior) and modular (prompt templates can be reused and composed).

-----

-----

### Source [25]: https://openai.github.io/openai-agents-python/mcp/

Query: What are the best practices for designing server-hosted prompts in Model Context Protocol (MCP) to orchestrate multi-step, stateful agentic workflows?

Answer: The OpenAI Agents SDK documents MCP prompt usage for agentic orchestration:

- **Prompts are exposed as server-side templates**, with two main methods: `list_prompts()` for discovery and `get_prompt(name, arguments)` for instantiation.

- **Dynamic agent instructions:** Servers generate prompt content on demand, using passed arguments and context to tailor instructions for each workflow step.

- **Workflow composition:** Agents can retrieve instructions from prompts and use them to guide stepwise execution, e.g., fetching a prompt for code review ('generate_code_review_instructions'), inserting workflow-specific arguments ("focus": "security vulnerabilities", "language": "python"), and then configuring the agent's instructions accordingly.

- **Stateful orchestration:** By retrieving prompts with updated arguments at each workflow step, agents maintain state and context, supporting multi-step processes.

- **Integration example:** The agent's instructions are set from the prompt's message content, demonstrating how server-hosted prompts orchestrate agentic behavior in a modular, stateful fashion.

-----

-----

### Source [26]: https://datasciencedojo.com/blog/guide-to-model-context-protocol/

Query: What are the best practices for designing server-hosted prompts in Model Context Protocol (MCP) to orchestrate multi-step, stateful agentic workflows?

Answer: The Data Science Dojo guide outlines prompt best practices for MCP:

- **Prompts are predefined templates/instructions** that shape AI behavior for specific tasks, offering structure and clarity compared to free-form user input.

- **Server-side orchestration:** Servers expose prompt templates that clients use to initiate complex workflows, e.g., bug reports, code reviews, or data analysis.

- **Initialization rules:** Prompts and other capabilities are only available after protocol initialization, ensuring predictable workflow setup and state management.

- **Workflow structuring:** By providing structured prompts, servers enable agents to execute multi-step workflows more reliably, with each step defined and parameterized by the prompt template.

- **State management:** Prompts can encode the current state or required context, helping maintain continuity across agentic workflow steps.

-----

-----

### Source [27]: https://www.getknit.dev/blog/mcp-architecture-deep-dive-tools-resources-and-prompts-explained

Query: What are the best practices for designing server-hosted prompts in Model Context Protocol (MCP) to orchestrate multi-step, stateful agentic workflows?

Answer: This deep-dive article emphasizes the role of prompts in MCP agentic workflows:

- **Prompts structure interactions** for scalable, multi-step agent workflows by providing reusable templates that encode instructions and context.

- **Server-hosted templates:** Prompts are managed on the server, ensuring centralized control and versioning for complex workflows. Agents retrieve updated templates as needed for each workflow stage.

- **Workflow orchestration:** By chaining prompt templates and passing context as arguments, agents can perform multi-step, stateful operations, using server-hosted prompts to guide their logic and maintain consistency.

- **Integration with tools and resources:** Prompts often reference tools or resources available from the server, enabling agents to access data or capabilities as part of the workflow sequence.

-----

</details>

<details>
<summary>How does Perplexity's API pricing model, specifically the costs associated with 'reasoning tokens' and 'search queries' in models like Sonar Deep Research, impact budget management for iterative, multi-round research agents?</summary>

### Source [28]: https://www.withorb.com/blog/perplexity-pricing

Query: How does Perplexity's API pricing model, specifically the costs associated with 'reasoning tokens' and 'search queries' in models like Sonar Deep Research, impact budget management for iterative, multi-round research agents?

Answer: Perplexity's API pricing is structured as a hybrid of predictable subscription tiers (Pro, Max, Enterprise Pro) and usage-based, metered API billing. Each paid plan includes a $5/month API credit, after which usage is billed according to the tokens consumed and the specific AI model selected. For example, lightweight models cost around $0.002 per request, while advanced models may cost approximately $0.015 per 1,000 tokens. The billing is transparent, allowing users to track usage and costs directly from their account dashboard. This pricing mechanism enables scalability for high-usage customers and cost control for low-usage ones, adapting to unpredictable usage spikes without forcing customers to upgrade to higher fixed-rate plans. For iterative, multi-round research agents, this means that costs are directly tied to the number of search queries issued and the total tokens processed during reasoning, making budget management highly dependent on workflow efficiency and the complexity of each research task. The metered approach ensures that projects with extensive back-and-forth or deep research will incur higher costs, which need to be accounted for in budget planning.

-----

-----

### Source [29]: https://team-gpt.com/blog/perplexity-pricing

Query: How does Perplexity's API pricing model, specifically the costs associated with 'reasoning tokens' and 'search queries' in models like Sonar Deep Research, impact budget management for iterative, multi-round research agents?

Answer: Perplexity's API pricing for models such as Sonar and Open-Source Models is set between $0.2 and $5 per 1 million tokens, depending on the specific model used. Chat models are billed at a fixed cost per 1,000 requests, with additional charges for input and output token usage. For Enterprise users, flexible plans start at $40/month per seat and include a $5 API credit. For research agents that iterate over many rounds, both the number of queries (search calls) and the volume of processed tokens contribute to the final cost. Consequently, projects requiring repeated, multi-step reasoning will see their costs scale with both the complexity (token usage) and the frequency (number of queries) of their operations, making cost predictability a function of usage patterns and agent design.

-----

-----

### Source [30]: https://familypro.io/en/blog/how-much-does-perplexity-cost

Query: How does Perplexity's API pricing model, specifically the costs associated with 'reasoning tokens' and 'search queries' in models like Sonar Deep Research, impact budget management for iterative, multi-round research agents?

Answer: Perplexity AI's API pricing for Sonar models ranges from $0.2 to $5 per million tokens, while Chat models are priced per 1,000 requests plus variable token costs. Each Pro subscription comes with a $5 monthly API credit. The system is designed for developers, businesses, and content creators integrating search and research into their tools. For iterative, multi-round research agents, every reasoning step and query generates token usage and/or request count, directly impacting overall cost. Therefore, managing the agent's research strategy—such as minimizing redundant queries or optimizing token usage per response—is essential for effective budget control.

-----

-----

### Source [31]: https://www.eesel.ai/blog/perplexity-pricing

Query: How does Perplexity's API pricing model, specifically the costs associated with 'reasoning tokens' and 'search queries' in models like Sonar Deep Research, impact budget management for iterative, multi-round research agents?

Answer: The Perplexity API operates as a pay-as-you-go service, charging based on the number of tokens processed and the chosen AI model. API billing is separate from subscription plans like Pro or Enterprise Pro, though these plans include a $5 API credit. Substantial API usage—such as that generated by iterative, multi-round research agents—will be billed independently and can lead to significant variance in monthly costs. The model's pricing structure requires careful monitoring of both tokens used (in reasoning steps) and queries issued (search actions) to avoid unexpected overruns. For budget management, this necessitates tracking and optimizing agent operations, as heavy or inefficient use can quickly exceed included credits.

-----

-----

### Source [32]: https://docs.perplexity.ai/getting-started/pricing

Query: How does Perplexity's API pricing model, specifically the costs associated with 'reasoning tokens' and 'search queries' in models like Sonar Deep Research, impact budget management for iterative, multi-round research agents?

Answer: According to Perplexity's official documentation, the Search API is priced at $5.00 per 1,000 requests, and notably, there are no additional token-based charges for this API—pricing is per request only. This means that for search-specific operations (such as issuing web search queries), costs are entirely determined by the number of queries, not their complexity or token length. For multi-round research agents relying heavily on the Search API, budget management is simplified to tracking the number of search queries made, rather than monitoring token usage for these requests. However, if reasoning steps involve other models or APIs with token-based billing, those components will still require token tracking for budget control.

-----

</details>

<details>
<summary>What are the technical challenges and design patterns for implementing append-only, file-first systems for auditability in long-running AI agent workflows?</summary>

### Source [33]: https://www.tigrisdata.com/blog/append-only-storage/

Query: What are the technical challenges and design patterns for implementing append-only, file-first systems for auditability in long-running AI agent workflows?

Answer: Tigris describes an immutable, append-only architecture where all operations (PUT, DELETE) are entries in an append-only log. Files are never mutated or deleted in place; each new version is added as a new immutable object, and deletions are marked as logical tombstones. This approach supports auditability by maintaining a verifiable, unalterable trail of all changes. Append-only systems allow for O(1) snapshot creation—snapshots are just named timestamps over the log—making recovery and auditing efficient and reliable. The design avoids in-place updates and mutation, which simplifies system behavior and enhances safety. For multi-agent AI workflows, each agent can fork from a snapshot, process independently, and all actions are recorded without risk of data collision. This immutability ensures that experimental forks, audit trails, and recoveries are all transparent, traceable, and cryptographically verifiable.

-----

-----

### Source [34]: https://decoding.io/2023/11/reviewing-append-only-workflows/

Query: What are the technical challenges and design patterns for implementing append-only, file-first systems for auditability in long-running AI agent workflows?

Answer: Decoding.io highlights that append-only systems only add new information, never removing or modifying history, making them highly auditable. Every change is visible in the chain, including mistakes, providing a complete historical breadcrumb of actions and decisions. This design pattern is beneficial for capturing evolving ideas, maintaining file versions, and ensuring transparency. In long-running workflows, append-only logs can act as automatic journals, providing a persistent record of every event. The core challenge is the mindset shift required to accept and preserve all history, even erroneous or suboptimal states, rather than cleaning up or deleting past data.

-----

-----

### Source [35]: https://akka.io/blog/trustworthy-ai-with-akka

Query: What are the technical challenges and design patterns for implementing append-only, file-first systems for auditability in long-running AI agent workflows?

Answer: Akka describes technical patterns for trustworthy AI workflows using an immutable, append-only ledger. Every agent action and orchestration is cryptographically logged, ensuring a tamper-proof audit trail. Each action—such as LLM calls, tool executions—is logged as a discrete event with full context and agent state, allowing for traceable reasoning. Provenance is standardized to facilitate third-party audits, and workflow definitions are both versioned and cryptographically signed to prevent unauthorized changes. Security is enforced through authenticated endpoints and robust logging, enabling administrators to trace every agent action back to its human originator. This design emphasizes cryptographic verifiability and interoperability for auditability.

-----

-----

### Source [36]: https://www.leapfin.com/blog/building-luca-an-ai-agent-for-finance-and-accounting-workflows-that-auditors-actually-trust

Query: What are the technical challenges and design patterns for implementing append-only, file-first systems for auditability in long-running AI agent workflows?

Answer: Leapfin’s Luca system maintains records in an append-only fashion: once written, data cannot be modified or deleted by any party. Operational data is structured as a graph, encoding causality between events, which allows for tracing every financial outcome to its operational origins. The workflow engine is deterministic (pure functions), so every input state and output is recorded. Audit trails are twofold: execution trails (input state, workflows executed, outputs, timestamps, initiator identities) are written to immutable tables, and configuration trails (workflow changes) are stored in Git, tracking every edit, approval, and justification. This architecture enables auditors to trace every number back to its source, workflow, code version, and execution time, providing mathematical proof of correctness and complete transparency. Observability and auditability are treated as foundational, not afterthoughts.

-----

-----

### Source [37]: https://www.johnsnowlabs.com/enabling-regulatory-grade-human-in-the-loop-workflows-with-the-generative-ai-lab/

Query: What are the technical challenges and design patterns for implementing append-only, file-first systems for auditability in long-running AI agent workflows?

Answer: John Snow Labs’ Generative AI Lab maintains a comprehensive, append-only audit trail for every workflow task, completion, and review. Each audit entry captures the timestamp, authenticated user identity, and type of action (e.g., completion, review request, deletion). This design ensures full traceability and compliance for regulated environments. The append-only log makes all actions permanent, supporting robust auditability for long-running, multi-step AI workflows.

-----

-----

### Source [38]: https://www.knostic.ai/blog/ai-governance-measurement-audit

Query: What are the technical challenges and design patterns for implementing append-only, file-first systems for auditability in long-running AI agent workflows?

Answer: Knostic emphasizes that cryptographic hashing and append-only storage are technical foundations for strong audit trails in AI governance. These patterns support regulatory frameworks such as the NIST AI Risk Management Framework (RMF). Audit trails log granular events—access attempts, labeling changes, permission grants/denials—using consistent keys for users, sessions, and resources to facilitate cross-system joins. Append-only and hashed records enhance evidentiary value by making tampering detectable and supporting forensic investigations without exposing raw content.

-----

-----

### Source [39]: https://www.ais.com/practical-memory-patterns-for-reliable-longer-horizon-agent-workflows/

Query: What are the technical challenges and design patterns for implementing append-only, file-first systems for auditability in long-running AI agent workflows?

Answer: AIS describes a practical pattern for agent workflows: a write-once, append-only activity log, where larger files are stored in a secure document store. The best practice is to record each event as a discrete, timestamped entry. These logs provide reliable memory for agents and robust audit trails, ensuring that all actions are traceable. The append-only log is central to reliability and auditability, supporting long-running workflows by preserving every decision and state change for later review.

-----

</details>

<details>
<summary>How can Pydantic models be used with Perplexity's JSON Schema support to ensure reliable parsing and data validation for structured outputs in an AI research agent?</summary>

### Source [40]: https://docs.perplexity.ai/guides/structured-outputs

Query: How can Pydantic models be used with Perplexity's JSON Schema support to ensure reliable parsing and data validation for structured outputs in an AI research agent?

Answer: Perplexity's structured outputs allow you to enforce specific response formats from models using JSON Schema, which enables consistent, machine-readable data integration. For Python users, Perplexity recommends using the Pydantic library to generate JSON schemas. You can define a Pydantic BaseModel representing the structure you require, and then use the `.model_json_schema()` method to generate a valid JSON Schema object for the response. This schema is then passed to the Perplexity API under the `response_format` parameter, ensuring the model's output matches your structure.

For parsing and validating the model's response, you can use Pydantic's `.model_validate_json()` method. This ensures that the returned data not only matches the schema but also is type-safe and validated according to your model's constraints. If the output does not conform, Perplexity provides enhanced error handling with clear, actionable error messages and built-in recursion protection to prevent unsupported complex nested schemas. Notably, recursive schemas and unconstrained objects (such as `dict[str, Any]`) are not supported, and Perplexity will automatically detect and reject them, providing clear validation feedback. This integration of Pydantic models with Perplexity's JSON Schema support ensures reliable parsing and strict data validation for structured outputs in AI agent workflows.

-----

-----

### Source [41]: https://python.useinstructor.com/integrations/perplexity/

Query: How can Pydantic models be used with Perplexity's JSON Schema support to ensure reliable parsing and data validation for structured outputs in an AI research agent?

Answer: Using Pydantic models with Perplexity's JSON Schema support is straightforward and enables type-safe, validated responses from the model. You define your data structure as a Pydantic BaseModel. When making a request to Perplexity, you specify this model (e.g., as `response_model=User`). Perplexity then generates a response that matches the schema defined by your model. On receiving the response, Pydantic automatically validates and parses the data into a strongly-typed Python object.

This process works in both synchronous and asynchronous modes, and supports nested objects, allowing for complex, hierarchical data structures. The integration ensures that if the model's output does not fit the schema, you will receive immediate feedback via validation errors. The supported mode with Instructor (`PERPLEXITY_JSON`) allows for direct, reliable JSON response generation. This approach eliminates the need for manual parsing and error-prone type checking, making it highly suitable for robust AI research agents that need consistent, validated structured outputs.

-----

-----

### Source [42]: https://docs.pydantic.dev/latest/concepts/json_schema/

Query: How can Pydantic models be used with Perplexity's JSON Schema support to ensure reliable parsing and data validation for structured outputs in an AI research agent?

Answer: Pydantic automatically creates and customizes JSON schemas from models using the `BaseModel.model_json_schema()` or `TypeAdapter.json_schema()` methods. These produce JSON-serializable dictionary objects representing the schema, compliant with JSON Schema specifications. The schema includes field types, constraints (such as `max_length`), and can be customized for specific use cases. This schema can then be passed directly to APIs like Perplexity that require a JSON Schema for structured outputs.

When a model receives data, Pydantic uses the schema to validate the data, ensuring all required fields and types match the specified structure. If the data does not conform, Pydantic raises clear validation errors, which can be handled programmatically. The field mapping from Python types to JSON Schema is automatic, covering standard types and constraints, and supports advanced features like unions and nested models. This guarantees both reliable parsing and strict data validation in applications, including AI agents that interact with structured outputs from language models.

-----

</details>

<details>
<summary>What are effective strategies for implementing programmatic testing of individual tools within a larger AI agent framework before integrating them into the full workflow?</summary>

### Source [43]: https://galileo.ai/learn/test-ai-agents

Query: What are effective strategies for implementing programmatic testing of individual tools within a larger AI agent framework before integrating them into the full workflow?

Answer: To implement effective programmatic testing of individual tools within an AI agent framework before integration, follow these structured strategies:

- **Define clear objectives and break down the agent**: Use SMART criteria to set testing goals, and decompose the agent into testable components (e.g., tool selection accuracy, error recovery, planning coherence). This allows for targeted evaluation at the tool level.

- **Develop comprehensive test suites**: Create tests covering both routine scenarios and edge cases to simulate real-world conditions and catch issues in tool performance under diverse situations.

- **Use benchmark datasets**: Employ standard datasets for reproducibility and to compare tool performance against established baselines. Combine these with custom datasets tailored to your specific use cases for a thorough evaluation.

- **Leverage simulation environments**: Simulate controlled scenarios for tool testing, enabling detailed tracking of decisions and outputs. Ensure environment parity with production for reliable results and reproducibility through state persistence and versioned test datasets.

- **Select specialized testing frameworks**: Use frameworks like AgentBench, LangChain Testing, or AutoGen Evaluation, which provide built-in support for tool usage verification and conversation flow analysis. These frameworks improve the consistency and depth of tool-level testing.

- **Phase your testing approach**: Start with basic functional testing (unit test each tool’s API and logic), then assess reasoning patterns in tool invocation, and finally conduct end-to-end scenario testing to evaluate integration readiness.

- **Combine automated and human evaluation**: Use automated scoring for efficiency but include domain experts to judge real-world appropriateness and tool safety. LLMs can also serve as evaluators in some contexts.

- **Monitor key performance metrics**: Track metrics like tool accuracy, efficiency, and safety (e.g., prompt injection, PII handling, toxicity). Custom metrics can further tailor evaluation to your tool’s intended use.

This structured, phased approach ensures each tool is robust and reliable before full integration into the agent’s workflow.

-----

-----

### Source [44]: https://www.uipath.com/blog/ai/agent-builder-best-practices

Query: What are effective strategies for implementing programmatic testing of individual tools within a larger AI agent framework before integrating them into the full workflow?

Answer: UiPath recommends several detailed strategies for testing individual tools within an AI agent framework before broader integration:

- **Start small and focused**: Develop tools with single, clear responsibilities. Narrow scopes increase performance consistency and make testing more effective.

- **Iterative design and testing**: Use agent builder platforms to iteratively refine prompts, tool definitions, and task instructions. Build evaluation sets and test tools continuously as they are developed.

- **Maintain clarity in tool definitions**: Use simple, precise names and ensure they align exactly with prompt references to avoid ambiguity during automated tests.

- **Build robust evaluation datasets**: For each tool, create at least 30 evaluation cases simulating success, edge, and failure scenarios. Include simulated blocks or escalations to test error handling.

- **Evaluate for breadth and depth**: Assess multiple dimensions—outcome accuracy, reasoning quality, traceability, adaptability, and tool-use success—to ensure comprehensive tool validation.

- **End-to-end and isolated testing**: While isolated (unit) tests validate individual tool logic, perform integration (end-to-end) tests to check how tools interact with the agent and other components.

- **Use trace logs**: Regularly analyze trace logs to inspect tool invocation, decision processes, and error paths. This helps identify unexpected tool behaviors or inefficiencies.

- **Metrics and governance**: Track health and regression metrics for each tool. Gate progression to integration on passing defined thresholds.

- **Human feedback loop**: Use feedback from test runs, escalations, and evaluation logs to iteratively improve both tool logic and prompts.

- **Simulate production deployment**: Deploy tools in orchestrated environments to test lifecycle management, auditing, and compliance features before full integration.

These steps help ensure that each tool is reliable, transparent, and meets quality standards before being embedded into the agent’s end-to-end workflow.

-----

</details>

<details>
<summary>What are the practical challenges and trade-offs when implementing a multi-round research loop in an AI agent, particularly concerning cost, latency, and the risk of generating duplicative or low-quality queries in later rounds?</summary>

### Source [45]: https://amplifypartners.com/blog-posts/the-ai-research-experimentation-problem

Query: What are the practical challenges and trade-offs when implementing a multi-round research loop in an AI agent, particularly concerning cost, latency, and the risk of generating duplicative or low-quality queries in later rounds?

Answer: A multi-round research loop in AI faces significant practical challenges related to cost, latency, and quality of queries:

- **Cost and Compute Constraints**: Running multiple rounds of experiments quickly encounters compute bottlenecks, as there are often not enough GPUs/TPUs available to power large-scale research. This is exacerbated when multiple hypotheses or ideas are evaluated simultaneously within a single training run to save compute, but this multiplexing reduces the ability to attribute performance gains to specific interventions, undermining causal interpretability.

- **Latency and Feedback Loops**: Evaluations are typically run late in the process due to their slowness, which means failures are often discovered only after considerable time and resources have been consumed. Running evaluations during training could reduce this latency, but current tools are slow and evaluation is not always prioritized as part of the pipeline.

- **Duplication and Low-Quality Outputs**: Pressure to ship results and the complexity of experimental design can result in poorly controlled variables, leading to noisy or duplicative outputs. Multiplexed experiments designed to save resources can obscure the source of any observed improvements, making it hard to determine what actually works.

- **Organizational and Tooling Pressures**: Teams often prioritize rapid iteration and model deployment over rigorous experimentation and evaluation, especially in fast-paced markets. This increases the risk of shipping models that have not been robustly tested, with evaluation often under-resourced compared to training.

- **Systemic Complexity**: The scale of modern AI systems, the rapid evolution of tools, and the complexity of hardware and software stacks introduce further challenges in debugging, evaluation, and attributing failures.

All these factors make implementing a robust, multi-round research loop both costly and complex, with significant trade-offs between speed, interpretability, and resource allocation.

-----

-----

### Source [46]: https://papers.academic-conferences.org/index.php/icair/article/view/3051

Query: What are the practical challenges and trade-offs when implementing a multi-round research loop in an AI agent, particularly concerning cost, latency, and the risk of generating duplicative or low-quality queries in later rounds?

Answer: Practical implementation of AI systems, including multi-round research loops, faces a range of organizational and technical challenges. According to the literature review and consultancy insights presented:

- **Implementation Strategy Flaws**: Many failures stem from inadequate or flawed implementation strategies, such as over-reliance on the latest technology without proper integration into existing workflows. This can lead to increased costs and delays as new AI solutions struggle to mesh with legacy systems.

- **Resource Allocation**: Organizations often invest heavily in development but underestimate the resources required for robust evaluation and iteration. Insufficient budgeting for iterations can increase latency and reduce the quality of subsequent research rounds.

- **Integration and Change Management**: The success of multi-round loops depends on how well the system is integrated with organizational processes. Poor integration can result in duplicated efforts, inconsistent data handling, and low-quality outputs as teams repeat or overlook steps.

- **Trade-offs in Benefits vs. Costs**: There is often a gap between the expected and actual benefits of AI research loops. High costs, both in direct investment and in opportunity cost from delayed market entry, must be weighed against potential gains. Inefficient loops amplify these trade-offs, especially when duplicative or low-impact queries consume resources that could be better used elsewhere.

- **Mitigation Approaches**: The paper highlights the need for more robust planning, clear integration strategies, and iterative review processes to mitigate these issues.

-----

-----

### Source [47]: https://arxiv.org/html/2509.00109

Query: What are the practical challenges and trade-offs when implementing a multi-round research loop in an AI agent, particularly concerning cost, latency, and the risk of generating duplicative or low-quality queries in later rounds?

Answer: In multi-round research and feedback loops for AI (such as recommender systems), several challenges and trade-offs become apparent:

- **Bias Amplification and Evaluation Bias**: Most bias mitigation methods are evaluated on a single iteration, not accounting for the feedback loop effect. Over multiple rounds, biases can be amplified, and methods that work well initially may fail in the long run. This introduces a risk of generating duplicative or low-quality queries as the system learns from its own outputs.

- **Lack of Robust Evaluation Frameworks**: There is a shortage of shared simulators and consistent evaluation metrics for multi-round assessment. Most studies focus on either fairness or performance, but rarely both, limiting the ability to comprehensively evaluate trade-offs across rounds. Only a small fraction of research explicitly considers dynamic, multi-round effects, leading to possible oversight of long-term issues.

- **Latency and Cost**: Simulating multiple feedback rounds is resource-intensive in terms of both compute and time. This increases operational costs and delays actionable insights, especially when using slow evaluation harnesses or when only late-stage evaluations are performed.

- **Framework Complexity**: Newer frameworks like FADE and FairAgent attempt to address these issues by enforcing constraints during model updates, but they highlight the complexity of maintaining fairness and quality over many rounds. Designing and validating such frameworks requires significant engineering effort and can still be prone to generating low-quality outputs if not carefully managed.

-----

-----

### Source [48]: https://aws.amazon.com/blogs/machine-learning/multi-agent-collaboration-patterns-with-strands-agents-and-amazon-nova/

Query: What are the practical challenges and trade-offs when implementing a multi-round research loop in an AI agent, particularly concerning cost, latency, and the risk of generating duplicative or low-quality queries in later rounds?

Answer: When implementing multi-agent or multi-round research loops, several practical trade-offs and challenges arise:

- **Orchestrator Complexity**: The agent that coordinates multiple rounds or agents must make correct decisions regarding task delegation and result integration. Errors in orchestration (such as misinterpreting queries) can lead to suboptimal or duplicative outputs, reducing overall system quality.

- **Single Point of Failure**: The orchestrator agent becomes a critical dependency. If it fails or makes a poor decision, subsequent rounds or the entire research loop can be compromised, potentially generating unnecessary or repeated queries in later stages.

- **Initial Analysis and Workflow Design**: Defining the correct dependencies and workflow upfront is crucial. Incomplete or incorrect decomposition of tasks can result in redundant steps or missed research opportunities, leading to unnecessary costs and increased latency.

- **Under-utilization and Latency**: Strictly sequential multi-round workflows may be slower than parallelized approaches. This can increase latency, especially if each round waits for the previous one to complete before proceeding, leading to longer feedback cycles.

- **Domain Expertise Requirement**: Proper workflow design may require significant domain expertise to avoid generating low-quality or redundant research queries in subsequent rounds.

-----

-----

### Source [49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11144926/

Query: What are the practical challenges and trade-offs when implementing a multi-round research loop in an AI agent, particularly concerning cost, latency, and the risk of generating duplicative or low-quality queries in later rounds?

Answer: While this source primarily discusses broader challenges in AI adoption, it touches on issues relevant to multi-round research loops:

- **Autonomy and Oversight Risks**: As AI systems become more autonomous, there is a risk of allocating decision-making to agents that may generate low-quality or duplicative outputs if not carefully monitored. This can be particularly problematic in feedback or research loops where the output of one round heavily influences the next.

- **Human-in-the-Loop Needs**: Ensuring appropriate oversight and maintaining quality across multiple rounds may require continued human involvement, which introduces additional costs and can slow down the overall process, increasing latency.

-----

-----

### Source [50]: https://www.infoq.com/news/2025/11/codeclash-competitive-llm-coding/

Query: What are the practical challenges and trade-offs when implementing a multi-round research loop in an AI agent, particularly concerning cost, latency, and the risk of generating duplicative or low-quality queries in later rounds?

Answer: Multi-round evaluation of LLMs for complex tasks, such as in the CodeClash benchmark, reveals several relevant challenges:

- **Task Decomposition and Recursion**: Solving real-world problems requires recursive decomposition of high-level objectives into actionable steps. Each round potentially generates new sub-queries, amplifying resource costs and increasing the chance of redundancy or low-quality outputs if the decomposition is not effective.

- **Strategic Decision-Making**: The agent must prioritize and decide which avenues to pursue, balancing the need for thoroughness with resource constraints. Poor decision-making can lead to unnecessary rounds or repeated exploration of unproductive directions, increasing both cost and latency.

- **Benchmarking and Fairness**: Traditional evaluation methods (e.g., single-step or maintenance tasks) do not capture these challenges. Multi-round research loops must be designed to accurately reflect real-world complexity, requiring more sophisticated benchmarks and evaluation strategies.

-----

</details>

<details>
<summary>How can server-hosted prompts in the Model Context Protocol (MCP) be dynamically modified during invocation to inject human-in-the-loop (HITL) feedback gates without altering the underlying code?</summary>

### Source [51]: https://modelcontextprotocol.info/docs/concepts/prompts/

Query: How can server-hosted prompts in the Model Context Protocol (MCP) be dynamically modified during invocation to inject human-in-the-loop (HITL) feedback gates without altering the underlying code?

Answer: MCP prompts are reusable templates that can accept dynamic arguments, include external context, chain multiple interactions, and guide workflows. Servers define these prompts and expose them to clients, which can surface them in various UI formats (slash commands, forms, guided workflows, etc.). 

Prompts are defined as objects with arguments, and the server implementation allows for arguments to be injected at runtime. For example, the `get_prompt` handler uses the provided arguments to fill in the prompt template. This mechanism enables dynamic modification: the server can adjust the prompt or its workflow during invocation by including additional steps, such as human feedback gates, without changing the underlying prompt code. HITL feedback gates could be implemented by inserting intermediate prompts or checks using dynamic arguments or by chaining prompt interactions. 

Servers can notify clients of changes to prompts using the `prompts.listChanged` capability and the `notifications/prompts/list_changed` notification, ensuring that HITL modifications are surfaced promptly. Since prompts are defined and modified on the server, clients only need to re-fetch the prompt list or template to get the latest version with HITL gates injected.

-----

-----

### Source [52]: https://modelcontextprotocol.io/specification/2025-06-18/server/prompts

Query: How can server-hosted prompts in the Model Context Protocol (MCP) be dynamically modified during invocation to inject human-in-the-loop (HITL) feedback gates without altering the underlying code?

Answer: Prompts in MCP are designed to be user-controlled and server-hosted, allowing clients to discover, retrieve, and customize prompt templates. The protocol enables dynamic injection of arguments and metadata into prompts during invocation.

Prompt messages support annotations, such as audience, priority, and modification times, which can be used to flag messages for human review or introduce feedback gates. This means that HITL feedback can be injected by adding or modifying metadata in prompt messages or by including additional prompt steps that request human validation. 

Since prompt modification is handled via argument injection and metadata annotation at invocation time, the underlying prompt code remains unchanged; only the invoked template and its parameters are altered. Servers declare the `prompts` capability and may notify clients of prompt list changes with the `listChanged` flag and notification event. Error handling is standardized, which helps integrate HITL gates for validation or rejection of prompt invocations.

-----

-----

### Source [53]: https://openai.github.io/openai-agents-python/mcp/

Query: How can server-hosted prompts in the Model Context Protocol (MCP) be dynamically modified during invocation to inject human-in-the-loop (HITL) feedback gates without altering the underlying code?

Answer: MCP servers expose prompt templates through two main methods: `list_prompts()` for enumeration and `get_prompt(name, arguments)` for generating a concretized prompt with parameters. During invocation, arguments are passed dynamically, and the returned prompt may contain user instructions that were constructed based on these arguments.

To inject HITL feedback gates, the server can generate prompt messages that include explicit calls for human input or validation within the workflow. Since the prompt is rendered at invocation time using provided arguments, the server can modify the workflow or message structure on the fly, incorporating HITL checks without changing the underlying code for the prompt template. This dynamic construction enables seamless updates to the invocation logic, such as adding feedback gates or intermediate steps, while the core prompt definition remains unchanged.

-----

-----

### Source [54]: https://www.danliden.com/posts/20250921-mcp-prompts-resources.html

Query: How can server-hosted prompts in the Model Context Protocol (MCP) be dynamically modified during invocation to inject human-in-the-loop (HITL) feedback gates without altering the underlying code?

Answer: When using MCP prompts with clients like Claude Desktop, users can send custom prompts with arguments, which are filled in interactively via the UI. The client then sends the filled-in prompt to the server, which responds with the completed template. This process allows servers to dynamically modify the prompt content during invocation by adding steps or requests for human feedback.

If HITL feedback gates need to be injected, the server can update the prompt template or include additional interactive steps in the workflow presented to the user. Since the prompt content is generated on the server and surfaced in the client UI, these modifications can occur without any changes to the client code or the underlying prompt definition—only the arguments and workflow steps need to be updated server-side.

-----

</details>

<details>
<summary>What are best practices for designing LLM prompts that analyze existing research and article guidelines to generate gap-filling, high-quality web search queries with clear reasoning?</summary>

### Source [55]: https://latitude-blog.ghost.io/blog/10-best-practices-for-production-grade-llm-prompt-engineering/

Query: What are best practices for designing LLM prompts that analyze existing research and article guidelines to generate gap-filling, high-quality web search queries with clear reasoning?

Answer: For designing LLM prompts that analyze research and article guidelines to generate gap-filling, high-quality search queries with clear reasoning, several key practices stand out:

- **Provide Clear and Detailed Context**: Explicitly state what the model needs to analyze, specifying the scope and any relevant research or article standards. This ensures outputs are aligned with the intended domain and research objectives.

- **Customize Prompts for Each Task**: Tailor prompts for the unique structure of research analysis and gap identification, such as asking the model to first summarize article guidelines, then identify missing elements, and finally generate targeted search queries.

- **Break Complex Tasks into Steps**: Structure prompts to guide the model sequentially: e.g., Step 1: Analyze existing research; Step 2: Identify gaps; Step 3: Formulate search queries. This scaffolding supports clearer reasoning and more reliable outputs.

- **Define Output Specifications**: Clearly specify the format for search queries (e.g., bullet points, specific query templates) and require that reasoning steps are shown alongside each query, enhancing traceability and quality.

- **Validate and Preprocess Inputs**: Ensure input research and guidelines are complete, well-structured, and relevant. Preprocessing reduces ambiguity and improves the model's ability to extract gaps accurately.

- **Set Personas and Tone**: If search queries must align with a particular research audience or voice, specify this (e.g., queries intended for academic researchers versus general audiences).

- **Use Version Control and Continuous Testing**: Track prompt iterations and test outputs regularly to ensure prompts consistently yield high-quality, gap-filling queries with clear reasoning. Integrate prompt refinement into workflow pipelines for ongoing improvement.

-----

-----

### Source [56]: https://mirascope.com/blog/prompt-engineering-best-practices

Query: What are best practices for designing LLM prompts that analyze existing research and article guidelines to generate gap-filling, high-quality web search queries with clear reasoning?

Answer: Best practices for prompting LLMs to analyze research and generate high-quality, reasoning-rich search queries include:

- **Specify Exactly What You Want**: Directly instruct the model to analyze research and guidelines, identify knowledge gaps, and generate queries. Avoid vague instructions; instead, use commands like 'Analyze,' 'Identify,' or 'Generate.'

- **Use Clear, Action-Oriented Instructions**: Start prompts with strong verbs (e.g., 'Summarize the article guidelines and list gaps. Then generate web search queries to fill these gaps, with reasoning.') to ensure the model understands it must perform multiple, connected actions.

- **Guide the Model to Think Step-by-Step**: Employ stepwise or chain-of-thought prompting. For example, instruct the model: 'First, list the key points in the article guidelines. Next, identify missing topics. Finally, for each gap, generate a search query and explain the reasoning.'

Using these methods encourages transparency in reasoning, helps prevent hallucinations, and results in more precise, actionable search queries.

-----

-----

### Source [57]: https://www.lakera.ai/blog/prompt-engineering-guide

Query: What are best practices for designing LLM prompts that analyze existing research and article guidelines to generate gap-filling, high-quality web search queries with clear reasoning?

Answer: Advanced prompt engineering techniques for generating gap-filling, high-quality search queries from research analysis include:

- **Context-Rich Prompts**: When analyzing articles or research, provide the full text or detailed excerpts as input, so the model has access to all relevant information for accurate gap detection.

- **Completion-Style and Mixed Prompts**: Depending on the task, use completion-style prompts for generating creative or exploratory queries, or combine prompt types to ensure precision, particularly in high-stakes research settings.

- **Chain-of-Thought Reasoning**: Explicitly instruct the model to reason step by step, e.g., 'First, summarize the main findings. Then, identify what is missing. Finally, generate a search query with an explanation for why it addresses the gap.'

This approach improves the model’s ability to justify its outputs and ensures each query generated is directly linked to a well-identified gap in the research.

-----

-----

### Source [58]: https://www.digitalocean.com/resources/articles/prompt-engineering-best-practices

Query: What are best practices for designing LLM prompts that analyze existing research and article guidelines to generate gap-filling, high-quality web search queries with clear reasoning?

Answer: Key best practices for LLM prompts that analyze research and generate high-quality, gap-filling queries include:

- **Be Specific**: Include as many relevant details as possible about the research context and the expected structure of the search queries. Specificity minimizes ambiguity and increases the relevance of the generated queries.

- **Use Positive, Directive Instructions**: Instruct the model on what actions to take (e.g., 'Identify missing research areas and generate search queries') rather than what to avoid. This focuses the LLM’s capabilities on constructive analysis and output.

- **Avoid Overloading**: Provide enough information for clarity without overwhelming the model with irrelevant context, balancing guidance and model autonomy for optimal results.

-----

-----

### Source [59]: https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api

Query: What are best practices for designing LLM prompts that analyze existing research and article guidelines to generate gap-filling, high-quality web search queries with clear reasoning?

Answer: For effective prompt engineering when generating research-driven search queries:

- **Use the Latest Model**: Newer LLMs show better understanding and are easier to prompt for complex reasoning tasks.

- **Put Instructions at the Beginning**: Start prompts with clear task instructions, using separators (such as ### or """) to distinguish instructions from context (e.g., research excerpts or guidelines). This clarifies prompt structure and ensures the model focuses on the key task.

- **Explicit Task Separation**: If the prompt includes multiple steps (analysis, gap identification, query generation), make each step explicit and clearly divided, so the model handles each action in sequence.

-----

-----

### Source [60]: https://cloud.google.com/discover/what-is-prompt-engineering

Query: What are best practices for designing LLM prompts that analyze existing research and article guidelines to generate gap-filling, high-quality web search queries with clear reasoning?

Answer: Effective prompt engineering for analyzing research and generating high-quality queries involves:

- **Providing Context and Examples**: Supply relevant context (e.g., article abstracts, guideline excerpts) and, if possible, example outputs to guide the model toward the desired format and depth.

- **Fine-Tuning and Adaptation**: For domain-specific tasks, fine-tune prompts or models on representative research data. Continuously adapt prompts based on output quality and user feedback to refine performance over time.

- **Iterative Improvement**: Use an iterative approach, adjusting prompts based on observed model performance for ongoing enhancement in both reasoning and result quality.

-----

</details>

<details>
<summary>How does Perplexity's API use of Pydantic models for structured outputs compare to other LLM providers, specifically regarding schema definition, error handling, and support for complex nested data?</summary>

### Source [61]: https://python.useinstructor.com/integrations/perplexity/

Query: How does Perplexity's API use of Pydantic models for structured outputs compare to other LLM providers, specifically regarding schema definition, error handling, and support for complex nested data?

Answer: Perplexity's API integrates with Pydantic models to enable structured outputs, ensuring type-safe and validated responses. Developers can define Pydantic models to specify the expected schema for LLM outputs, including support for primitive types and complex nested structures. The API supports both synchronous and asynchronous workflows, and it can enforce schemas such that the model’s output is automatically parsed and validated against the provided Pydantic definition.

For nested data, users can define classes that include lists or other models, and Perplexity's Sonar models will output data that fits the nested schema precisely. Error handling is implicitly present: if the output does not conform to the Pydantic model, validation errors are raised, which can be caught and handled in user code. Perplexity supports direct JSON response generation, minimizing the need for post-processing or custom parsing.

Compared to other LLM providers, this approach is similar to OpenAI’s function calling and structured output features, but Perplexity’s API is compatible with Instructor and other OpenAI-compatible wrappers, making migration or integration straightforward. The combination of Pydantic model validation and Perplexity’s JSON output mode provides robust schema enforcement and developer-friendly error handling.

-----

-----

### Source [62]: https://docs.perplexity.ai/guides/structured-outputs

Query: How does Perplexity's API use of Pydantic models for structured outputs compare to other LLM providers, specifically regarding schema definition, error handling, and support for complex nested data?

Answer: Perplexity's structured outputs guide demonstrates direct support for enforcing output formats via Pydantic models. The guide provides examples where developers define strict schemas (via Pydantic's BaseModel) and pass them as the response_model parameter. This allows Perplexity to generate outputs that are directly validated against the schema, including complex types such as optional fields, lists, and nested objects.

Perplexity’s API handles errors by raising exceptions when the output cannot be parsed to the model, allowing developers to catch and handle schema mismatches programmatically. This approach streamlines integration with downstream systems that require predictable, machine-readable output formats. The guide makes clear that Perplexity’s structured output features are designed to ensure consistency and validity, which is particularly important for tasks involving financial analysis, data extraction, and other domains requiring precise structure.

This schema enforcement and error handling is on par with OpenAI’s function calling and Anthropic’s tool use, but the use of Pydantic enables more flexible, Python-native model definitions and validation logic.

-----

-----

### Source [63]: https://oxylabs.io/blog/perplexity-web-scraping

Query: How does Perplexity's API use of Pydantic models for structured outputs compare to other LLM providers, specifically regarding schema definition, error handling, and support for complex nested data?

Answer: The Oxylabs tutorial confirms that Perplexity’s API, when combined with Pydantic and Instructor, allows developers to strictly constrain the output format of LLM responses. By passing a Pydantic model as response_model, the API generates outputs that must match the schema, which is particularly useful for extracting structured information from unstructured text, such as web scraping results.

This strict schema enforcement supports both flat and nested data models, ensuring that outputs such as lists of items, objects with multiple attributes, or hierarchical data can be reliably extracted. The tutorial highlights that naming conventions and field definitions in Pydantic can help guide the LLM to produce more accurate results. Error handling is managed by Pydantic, which raises validation errors if the output does not match the schema, allowing for robust exception handling and integration with automated pipelines.

Compared to other LLM providers, Perplexity’s support for Pydantic models is similar to OpenAI’s function calling, but with a particular emphasis on developer control and Python-native validation.

-----

-----

### Source [64]: https://ai.pydantic.dev/models/overview/

Query: How does Perplexity's API use of Pydantic models for structured outputs compare to other LLM providers, specifically regarding schema definition, error handling, and support for complex nested data?

Answer: Pydantic AI’s documentation notes that the system supports OpenAI-compatible providers, including Perplexity. Developers can supply their own custom providers as long as the API is OpenAI-compatible, allowing Perplexity to work seamlessly with Pydantic-based agents. The documentation also describes advanced error handling features such as model fallback: if one model (e.g., Perplexity) fails due to a schema or output error, the system can automatically try another model (e.g., OpenAI or Anthropic).

Error handling is further enhanced by exception catching and custom error handlers, allowing developers to manage model failures and schema validation errors programmatically. This approach allows for resilient pipelines that maintain high reliability even when LLM outputs are inconsistent or invalid. The documentation emphasizes the importance of schema definition and validation for both flat and nested data, ensuring that complex outputs can be handled robustly across providers.

-----

</details>

<details>
<summary>What are effective strategies for implementing programmatic, end-to-end tests for an AI agent's research loop that verify the flow from query generation to Perplexity integration and file-based result logging?</summary>

### Source [65]: https://galileo.ai/blog/ai-agent-testing-behavioral-validation

Query: What are effective strategies for implementing programmatic, end-to-end tests for an AI agent's research loop that verify the flow from query generation to Perplexity integration and file-based result logging?

Answer: Effective strategies for implementing programmatic, end-to-end tests for an AI agent’s research loop include several structured methodologies designed to validate the entire workflow from query generation, through API/tool integration (such as Perplexity), to result logging. Key approaches:

- **End-to-end task flow validation**: Test not just isolated API calls, but the entire workflow by providing a natural-language request, tracing each decision, intermediate output, and tool choice until the final result. Capture each reasoning step to spot loops, unnecessary tool calls, or missing safeguards.

- **Layered output evaluation**: Use automated factuality checks (link verification, numerical consistency, contradiction detection) to detect hallucinations or logical gaps. Compare chosen tools against an 'optimal path' to identify inefficient or incorrect reasoning. Analyze reasoning patterns for redundant loops and unnecessary executions to optimize speed and compute cost.

- **Response quality and robustness testing**: Track factual accuracy, coherence, and relevance with automated text metrics. Replay synthetic edge cases (malformed inputs, contradictory instructions) and record pass rates to ensure robustness under unexpected scenarios.

- **Prompt-level validation**: Test prompts separately to locate failures in the prompt or instruction layer, using automated metrics to provide direct feedback and prevent expensive fixes later on.

- **Continuous validation in staging environments**: Route traffic through test environments, recording decision paths, speed, and success metrics after every model or prompt update. Trigger behavioral regression tests to catch drift and block problematic releases.

- **Regression test suites and A/B testing**: Build regression suites capturing previously failing scenarios and verify future versions don’t reintroduce them. Use A/B tests to compare different configurations on task completion, speed, and hallucination rates.

-----

-----

### Source [66]: https://dev.to/kuldeep_paul/best-practices-for-ensuring-ai-agent-performance-and-reliability-4ok0

Query: What are effective strategies for implementing programmatic, end-to-end tests for an AI agent's research loop that verify the flow from query generation to Perplexity integration and file-based result logging?

Answer: Best practices for programmatic, end-to-end testing of AI agents encompass simulation, dataset design, and continuous integration:

- **Scenario-Based Simulations**: Simulate agent behavior across varied real-world scenarios and user personas using platforms such as Maxim AI. Multi-turn, multi-agent simulations surface brittle logic, edge cases, and context gaps early.

- **Synthetic and Real Data Mix**: Blend synthetic test cases with real production data to ensure the simulation environment reflects actual user behavior and evolving requirements.

- **Regression and Stress Testing**: Automate regression tests to catch performance drops following changes to prompts, tools, or agent logic. Conduct stress tests (e.g., burst traffic, ambiguous queries) to identify latency, cost, and failure modes.

- **Human-in-the-Loop (HITL) Evaluation**: For high-stakes or ambiguous tasks, integrate human review pipelines to manually evaluate outputs when automated confidence scores are low.

- **Continuous Feedback Loops**: Integrate evaluation into CI/CD pipelines so every agent update triggers automated and, where appropriate, human evaluations. This ensures updated versions do not regress on critical metrics.

These practices collectively ensure reliability and robustness from query generation through external tool integration to final result logging.

-----

-----

### Source [67]: https://www.uipath.com/blog/ai/agent-builder-best-practices

Query: What are effective strategies for implementing programmatic, end-to-end tests for an AI agent's research loop that verify the flow from query generation to Perplexity integration and file-based result logging?

Answer: UiPath recommends several best practices for reliable, governed AI agents, relevant to programmatic end-to-end testing:

- **Evaluate for Breadth and Depth**: Cover multiple dimensions in tests—accuracy of outcomes, reasoning, traceability, adaptability, and tool-use success.

- **End-to-end Testing**: Evaluate agents within full automation contexts, not in isolation. This involves testing all integrations, communications between components, recovery from errors, and handling of failure modes.

- **Use Tracing**: Regularly review trace logs to inspect the agent’s reasoning loop, decisions, and tool usage. Trace logs help identify errors, inefficiencies, and unexpected behaviors throughout the workflow.

- **Evaluation Datasets and Regression Metrics**: Use evaluation datasets, thoroughly review trace logs, and apply regression metrics to validate accuracy, tool use, and safety. This process should be repeatable and scalable.

These principles ensure that the agent's behavior and integration with systems such as Perplexity and file-based logging are validated comprehensively.

-----

-----

### Source [68]: https://www.zendesk.com/blog/zip1-building-realistic-multi-turn-tests-for-ai-agents/

Query: What are effective strategies for implementing programmatic, end-to-end tests for an AI agent's research loop that verify the flow from query generation to Perplexity integration and file-based result logging?

Answer: Zendesk’s methodology for realistic, multi-turn end-to-end testing of AI agents includes:

- **Intent and Procedure Generation**: Use a language model to generate user intents and detailed agent procedures for fulfilling them. Procedures define the required API/tool calls at each step, which are essential for verifying proper agent behavior.

- **Conversation Graph Construction**: Build directed flowgraphs simulating all execution paths (normal, branches, dead-ends, detours). This ensures comprehensive coverage of possible agent behaviors.

- **Noise Injection**: Add realism by injecting interruptions, clarifying questions, or context shifts into conversations, testing agent resilience and reliability.

- **Path Sampling and Dialogue Synthesis**: Sample multiple paths through the conversation graph; synthesize full dialogues with the LLM handling user and agent turns.

- **Test Extraction and Validation**: Split conversations into individual test cases with expected API outcomes. Automated validation and manual review confirm correctness and robustness at each step.

This approach ensures agents are tested for consistent, reliable execution from initial query through external integration and result logging.

-----

-----

### Source [69]: https://testrigor.com/blog/different-evals-for-agentic-ai/

Query: What are effective strategies for implementing programmatic, end-to-end tests for an AI agent's research loop that verify the flow from query generation to Perplexity integration and file-based result logging?

Answer: testRigor highlights key strategies relevant to robust, programmatic end-to-end testing for agentic AI:

- **Testing Robustness and Security**: Due to LLMs’ probabilistic nature, they are vulnerable to prompt injection, which is a major security risk. testRigor enables injection of adversarial or contradictory prompts to test the agent’s guardrails and resilience.

- **Stability in Dynamic Environments**: Agent UIs and the tools they interact with often change. Traditional testing tools may break when underlying code changes, but testRigor relies on AI-based element identification and self-healing tests to maintain test stability and reliability despite changes.

These strategies support resilient and secure end-to-end test flows, ensuring the agent’s research loop (from query to external API to logging) remains robust under evolving conditions.

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>Prompt Engineering Best Practices: Tips, Tricks, and Tools</summary>

# Prompt Engineering Best Practices: Tips, Tricks, and Tools

A range of [AI business tools](https://www.digitalocean.com/resources/article/ai-tools-in-business)—from Chat GPT to Claude 3—have become cornerstones of the AI revolution, weaving their way into everyday life and business operations. These advanced chatbots are used by individuals and professionals alike to perform various personal and professional tasks. According to [DigitalOcean’s bi-annual Currents survey](https://www.digitalocean.com/currents/november-2023#AI-ML), 45% of respondents acknowledged that AI and machine learning tools have made their job easier. However, there’s a catch: 43% of those surveyed also feel that the effectiveness of these tools is often over-hyped and exaggerated.

This disparity in user satisfaction may be traced to one crucial factor: the art of prompt engineering or the lack thereof. Crafting the right prompt can mean the difference between an AI delivering a valuable output that streamlines your workflow and receiving an inadequate response that leaves you more frustrated than relieved, forcing you to tackle the task independently. As the AI revolution charges forward, the skill of prompt engineering has emerged as a distinct discipline; prompt engineer has [become a lucrative and sought-after role within organizations](https://time.com/6272103/ai-prompt-engineer-job/).

This article delves into prompt engineering, providing best practices and a few examples to help your business extract maximum value from these large language models.

## What is prompt engineering?

Prompt engineering is the craft of designing and refining inputs (prompts) to elicit the desired output from AI language models. It requires a blend of creativity, understanding of the model’s capabilities, and strategic structuring of the question or statement to guide the AI towards providing accurate, relevant, and useful responses. Prompt engineering improves communication between humans and machines, ensuring the resulting interaction is efficient and effective.

## Why is prompt engineering important?

Prompt engineering is crucial because it influences the performance and utility of AI language models. The quality of the input determines the relevance and accuracy of the AI’s response, making prompt engineering a pivotal skill for anyone looking to harness the full potential of these powerful tools. Prompt engineering is not only for prompt engineers. By effectively communicating with AI, anyone can unlock insights, generate ideas, and solve problems more efficiently.

Here are several reasons why prompt engineering is important:

-   **Improves accuracy**: Well-crafted prompts lead to more precise answers, reducing the likelihood of misinterpretation or irrelevant responses from the AI.

-   **Saves time**: Prompt engineering streamlines interactions with the AI by getting the desired information in fewer attempts, saving valuable time for users.

-   **Facilitates complex tasks**: Complex tasks require complex understanding; good prompts translate intricate questions into a form that AI can process effectively.

-   **Improves user experience**: A user’s experience with an AI system can greatly improve when the prompts lead to clear, concise, and contextually appropriate answers.

-   **Enables better outcomes**: In areas such as coding, content creation, and data analysis, well-engineered prompts can lead to higher-quality outcomes by leveraging AI’s capabilities to the fullest.

-   **Drives innovation**: As we better understand how to communicate with AI, we can push the boundaries of what’s possible, leading to innovative applications and solutions.

## 10 Prompt engineering best practices

Crafting effective prompts for AI can improve the quality and relevance of the responses you receive. This expertise requires a nuanced understanding of how AI interprets and processes natural language inputs. Ahead, we explore ten AI prompt engineering best practices to help you communicate with AI more effectively:

### 1\. Be as specific as possible

Specificity is key to obtaining the most accurate and relevant information from an AI when writing prompts. A specific prompt minimizes ambiguity, allowing the AI to understand the request’s context and nuance, preventing it from providing overly broad or unrelated responses. To achieve this, include as many relevant details as possible without overloading the AI with superfluous information. This balance ensures that the AI has just enough guidance to produce the specific outcome you’re aiming for.

When creating the best prompts for an AI, ask for the following specifics:

-   **Detailed context**: Provide the AI with enough background information to understand the scenario you’re inquiring about. This includes the subject matter, scope, and any relevant constraints.

-   **Desired format**: Clearly specify the format in which you want the information to be presented, whether it’s a list, a detailed report, bullet points, or a summary. Mention any structural preferences, such as headings, subheadings, or paragraph limits.

-   **Output length**: Detail how long you want the AI’s response, whether “3 paragraphs” or “250 words.”

-   **Level of detail**: Indicate the level of detail required for the response, from high-level overviews to in-depth analysis, to ensure the model’s output matches your informational needs.

-   **Tone and style**: Request the preferred tone and style, whether it’s formal, conversational, persuasive, or informational, to make sure the output aligns with your intended audience or purpose.

-   **Examples and comparisons**: Ask the AI to include examples, analogies, or comparisons to clarify complex concepts or make the information more relatable and easily understood.

**💡 Prompt Example:**

Please provide an outline for a comprehensive report that analyzes the current trends in social media marketing for technology companies, focusing on the developments from 2020 onward.

The outline should include an introduction, three main sections addressing different aspects of social media trends, and a conclusion summarizing the findings. Please suggest the types of graphs that could illustrate user engagement trends and list bullet points that summarize key marketing strategies in each section.

### 2\. Supply the AI with examples

Incorporating examples into your prompts is a powerful technique to steer the AI’s responses in the desired direction. By providing examples as you write prompts, you set a precedent for the type of information or response you expect. This practice is particularly useful for complex tasks where the desired output might be ambiguous or for creative tasks with more than one correct answer.

When you supply the AI with examples, ensure they represent the quality and style of your desired result. This strategy clarifies your expectations and helps the AI model its responses after the examples provided, leading to more accurate and tailored outputs.

Here are some example types you could provide to an AI to help guide it toward generating the best response possible:

-   **Sample texts**: Share excerpts reflecting the style, tone, and content you want the AI to replicate.

-   **Data formats**: To guide the AI’s output, provide specific data structures, such as table layouts or spreadsheet formats.

-   **Templates for documents**: Offer templates to ensure the AI’s response follows a desired structure and format.

-   **Code snippets**: Provide code examples if you need help with programming tasks to ensure correct syntax and logic.

-   **Graphs and charts examples**: If you’re asking the AI to create similar graphics, share samples of visual data representation.

-   **Marketing copy**: If you’re crafting marketing content, present ad copy that aligns with your brand’s voice for the AI to mimic.

**💡 Prompt Example:**

Create a comparison table for two project management tools, Tool A and Tool B.

Include the following categories: Price, Key Features, User Reviews, and Support Options. For instance, under Key Features, list things like ‘Task Assignment’, ‘Time Tracking’, and ‘File Sharing’.

The format should mirror something like this:

| Feature | Tool A | Tool B |
|--------|-------|-------|
| Price | $X per user/month | $Y per user/month |
| Key Features | Task Assignment | File Sharing |
| User Reviews | X stars | Y stars |
| Support Options | 24/7 Live Chat, Email | Business Hours Phone, Email |

Please ensure the table is concise and suitable for inclusion in a business report.

### 3\. Get better answers by providing data

Incorporating specific and relevant data into your prompts significantly enhances the quality of AI-generated responses, providing a solid foundation for the AI to understand the context and craft precise answers. Providing data that includes numerical values, dates, or categories, organized in a clear and structured way, allows for detailed analysis and decision-making. It’s essential to give context to the data and, when possible, to cite its source, lending credibility and clarity to the specific task, whether for quantitative analysis or comparisons.

To ensure the AI delivers the most relevant and insightful answers, always use updated and well-organized information, and if comparisons are needed, establish clear parameters. Supplying the AI with concrete, contextualized data transforms raw figures into intelligible and actionable insights. Data-driven prompts are particularly valuable in tasks requiring a deep dive into numbers, trends, or patterns, enabling the AI to generate outputs that can effectively inform business strategies or research conclusions.

**💡 Prompt Example:**

Please analyze the sales data from the first quarter of 2024 provided in the attached PDF document. I need a summary that identifies our best-selling product, the overall sales trend, and any notable patterns in customer purchases.

The PDF contains detailed monthly sales units for three products: Product A, Product B, and Product C. After reviewing the data, summarize your findings in a concise paragraph that is suitable for a business meeting. Highlight significant increases or decreases in sales and offer insights into potential factors driving these trends.

### 4\. Specify your desired output

When engaging with AI, articulate the precise format and structure you expect in the response. Specify whether you require a detailed report, a summary, bullet points, or a narrative form to ensure the AI tailors its output to your needs.

Indicate any preferences such as tone, style, and the inclusion of certain elements like headings or subheadings. By clearly defining your desired output, you guide the AI to deliver information that aligns seamlessly with your intended use.

**💡 Prompt Example:**

Create a comprehensive overview of the key milestones in the history of software development. The output should be structured as a timeline with bullet points, each bullet including the year, the milestone event, and a brief description of its significance. Start from the 1980s. The tone should be educational. Please limit the overview to ten major milestones to maintain conciseness.

### 5\. Provide instructions on what to do instead of what *not* to do

When constructing prompts for AI, it’s more effective to direct the system toward the desired action rather than detailing what it should avoid. This positive instruction approach reduces ambiguity and focuses the AI’s processing power on generating constructive outcomes.

Negative instructions often require the AI to interpret and invert them, increasing the cognitive load and potential for misunderstanding. By clearly stating the intended actions, you enable the AI to apply its capabilities directly to fulfilling the task at hand, improving the efficiency and accuracy of the response.

**💡 Prompt Examples:**

-   Avoid: "Don’t write too much detail. → Use Instead: “Please provide a concise summary.”

-   Avoid: “Avoid using technical jargon.” → Use Instead: “Use clear and simple language accessible to a general audience.”

-   Avoid: “Don’t give examples from before the year 2000.” → Use Instead: “Provide examples from the year 2000 onwards.”

### 6\. Give the model a persona or frame of reference

Assigning a persona or a specific frame of reference to an AI model can significantly enhance the relevance and precision of its output. By doing so, you get more relevant responses, aligned with a particular perspective or expertise, ensuring that the information provided meets the unique requirements of your query.

This approach is especially beneficial in business contexts where domain-specific knowledge is pivotal, as it guides the AI to utilize a tone and terminology appropriate for the given scenario. The persona also helps set the right expectations and can make interactions with the AI more relatable and engaging for the end user.

**💡 Prompt Example:**

Imagine you are a seasoned marketing consultant. Please draft an email to a new startup client outlining three digital marketing strategies tailored for their upcoming product launch (see attached PDF for details).

Include key performance indicators (KPIs) for each strategy that will help track their campaign’s success. Ensure the tone is encouraging and professional, imparting confidence in your expertise.

### 7\. Try chain of thought prompting

Chain of thought prompting is a technique that elicits a more deliberate and explanatory response from an AI by specifically asking it to detail the reasoning behind its answer. By prompting the AI to articulate the steps it takes to reach a conclusion, users can better understand the logic employed and the reliability of the response.

This approach is particularly useful when tackling complex problems or when the reasoning process itself is as important as the answer. It ensures a deeper level of problem-solving and provides a learning opportunity for the user to see a modeled approach to reasoning.

**💡 Prompt Example:**

Imagine you are a software engineer tasked with optimizing this piece of software for performance:

\[Insert code block\]

Use the following chain of thought to guide your approach:

-   Performance profiling: Start with how you would profile the software to identify current performance bottlenecks.

-   Optimization techniques: Discuss the specific techniques you would consider to address the identified bottlenecks, such as algorithm optimization, code refactoring, or hardware acceleration.

-   Testing and validation: Describe your method for testing the optimized software to ensure that the changes have had the desired effect and have not introduced new issues.

-   Implementation strategy: Finally, outline how you would safely implement the optimized code into the production environment, ensuring minimal disruption.

Conclude with a summary of the key steps in the optimization process and how you would document and maintain the improvements over time.

### 8\. Split complex tasks into simpler ones

When dealing with complex tasks, breaking them into simpler, more manageable components can make them more approachable for an AI. Using step by step instructions helps prevent the AI from becoming overwhelmed and ensures that each part of the task is handled with attention to detail.

Additionally, this approach allows for easier monitoring and adjustment of each step, facilitating better quality control throughout the process. By compartmentalizing tasks, the AI can also use its resources more efficiently, allocating the necessary attention where it’s most needed, resulting in a more effective problem-solving strategy.

**💡 Prompt Example:**

Avoid a single broad prompt:

-   “Write a 1500-word article on the impact of AI on remote work.”

Try an initial prompt and follow-up prompts instead:

-   “Develop a detailed outline for a 1500-word article titled ‘Revolutionizing Remote Work: The Role of AI for Tech Professionals.’ The outline should include an engaging introduction, three main sections titled ‘Enhancing Productivity with AI Tools,’ ‘AI-Driven Communication Optimization,’ and ‘Advanced Project Management through AI,’ plus a conclusion that offers a perspective on future developments.”

-   “Compose a detailed introduction for the article ‘Revolutionizing Remote Work: The Role of AI for Tech Professionals.’ The introduction should be 150-200 words, setting the stage for how AI is changing the game for remote workers in the tech industry, and providing a hook that will entice tech professionals to continue reading.”

### 9\. Understand the model’s shortcomings

In crafting prompts for an AI, recognize the model’s limitations to set realistic expectations. Prompting AI to perform tasks it’s not designed for, such as interacting with external databases or providing real-time updates, will lead to ineffective and potentially misleading outputs called [AI hallucinations](https://www.digitalocean.com/resources/article/ai-hallucination).

Here are some known shortcomings of AI models:

-   Lack of real-time data processing, as the knowledge is up-to-date only until the last training cut-off.

-   Inability to access or retrieve personal data unless it has been shared during the interaction.

-   No direct interaction with external software, databases, or live web content.

-   Potential bias in the data, as AI models can inadvertently learn and replicate biases present in their training data.

-   Limited understanding of context can lead to less nuanced responses in complex or ambiguous situations.

-   The absence of personal experiences or emotions means the AI cannot form genuine, empathetic connections or offer personal anecdotes.

### 10\. Take an experimental approach to prompting

Prompt engineering is an emergent field that necessitates an experimental mindset. As you navigate this new territory, use an iterative process to test various prompts, paying careful attention to how slight modifications can significantly alter the AI’s responses. You’ll only learn how models respond by testing them.

While maintaining a commitment to [AI privacy](https://www.digitalocean.com/resources/article/ai-and-privacy) and ethical standards is key, don’t hesitate to explore diverse phrasings and structures to discover the most effective prompts. This trial-and-error process can yield better results and contribute to a broader understanding of how large language models interpret and act on different types of instructions.

</details>

<details>
<summary>Overview</summary>

## Overview

Structured outputs enable you to enforce specific response formats from Perplexity’s models, ensuring consistent, machine-readable data that can be directly integrated into your applications without manual parsing.We currently support two types of structured outputs: **JSON Schema** and **Regex**. LLM responses will work to match the specified format, except for the following cases:

- The output exceeds `max_tokens`

Enabling the structured outputs can be done by adding a `response_format` field in the request:

**JSON Schema**

- `response_format: { type: "json_schema", json_schema: {"schema": object} }` .
- The schema should be a valid JSON schema object.

**Regex** (only available for `sonar` right now)

- `response_format: { type: "regex", regex: {"regex": str} }` .
- The regex is a regular expression string.

**Improve Schema Compliance**: Give the LLM some hints about the output format in your prompts to improve adherence to the structured format.For example, include phrases like “Please return the data as a JSON object with the following structure…” or “Extract the information and format it as specified in the schema.”

The first request with a new JSON Schema or Regex expects to incur delay on the first token. Typically, it takes 10 to 30 seconds to prepare the new schema, and may result in timeout errors. Once the schema has been prepared, the subsequent requests will not see such delay.

## Examples

### 1. Financial Analysis with JSON Schema

```
from perplexity import Perplexity
from typing import List, Optional
from pydantic import BaseModel

class FinancialMetrics(BaseModel):
    company: str
    quarter: str
    revenue: float
    net_income: float
    eps: float
    revenue_growth_yoy: Optional[float] = None
    key_highlights: Optional[List[str]] = None

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[\
        {\
            "role": "user",\
            "content": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics."\
        }\
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "schema": FinancialMetrics.model_json_schema()
        }
    }
)

metrics = FinancialMetrics.model_validate_json(completion.choices[0].message.content)
print(f"Revenue: ${metrics.revenue}B")
```

### 2. Extract Contact Information with Regex

```
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar",
    messages=[\
        {\
            "role": "user",\
            "content": "Find the direct email address for the investor relations contact at Tesla Inc."\
        }\
    ],
    response_format={
        "type": "regex",
        "regex": {
            "regex": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        }
    }
)

email = completion.choices[0].message.content
print(f"Investor Relations Email: {email}")
```

## Best Practices

### Generating responses in a JSON Format

For Python users, we recommend using the Pydantic library to [generate JSON schema](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema).**Unsupported JSON Schemas**Recursive JSON schema is not supported. As a result of that, unconstrained objects are not supported either. Here’s a few example of unsupported schemas:

```
# UNSUPPORTED!

from typing import Any

class UnconstrainedDict(BaseModel):
   unconstrained: dict[str, Any]

class RecursiveJson(BaseModel):
   value: str
   child: list["RecursiveJson"]
```

**Links in JSON Responses**: Requesting links as part of a JSON response may not always work reliably and can result in hallucinations or broken links. Models may generate invalid URLs when forced to include links directly in structured outputs.To ensure all links are valid, use the links returned in the `citations` or `search_results` fields from the API response. Never count on the model to return valid links directly as part of the JSON response content.

### Generating responses using a regex

**Supported Regex**

- Characters: `\d`, `\w`, `\s` , `.`
- Character classes: `[0-9A-Fa-f]` , `[^x]`
- Quantifiers: `*`, `?` , `+`, `{3}`, `{2,4}` , `{3,}`
- Alternation: `|`
- Group: `( ... )`
- Non-capturing group: `(?: ... )`

**Unsupported Regex**

- Contents of group: `\1`
- Anchors: `^`, `$`, `\b`
- Positive lookahead: `(?= ... )`
- Negative lookahead: `(?! ... )`
- Positive look-behind: `(?<= ... )`
- Negative look-behind: `(?<! ... )`
- Recursion: `(?R)`

## Perplexity’s JSON Schema Implementation

Perplexity’s structured outputs implementation has several key differences compared to other providers:

### Simplified Schema Definition

- **Optional naming**: Unlike other providers that require explicit schema names, Perplexity automatically handles schema naming with sensible defaults
- **Flexible strictness**: Schema validation is handled automatically without requiring manual strictness configuration
- **Streamlined syntax**: You only need to provide the core schema object without additional wrapper fields

**Other Providers:**

```
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "financial_data",
      "strict": true,
      "schema": { /* your schema */ }
    }
  }
}
```

**Perplexity:**

```
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "schema": { /* your schema */ }
    }
  }
}
```

### Enhanced Error Handling

- **Clear error messages**: When schemas fail validation, you’ll receive specific, actionable error messages
- **Recursion protection**: Built-in safeguards prevent infinite recursion in complex nested schemas
- **Constraint validation**: Automatic detection and clear messaging for unsupported features like unconstrained objects

### Schema Compatibility

While Perplexity supports standard JSON Schema syntax, some advanced features may not be available:

- Recursive schemas are not supported for performance and reliability reasons
- Unconstrained objects (like `dict[str, Any]`) are automatically detected and rejected
- Complex reference patterns may require simplification

This approach prioritizes reliability and performance while maintaining compatibility with most common JSON Schema use cases.

## Structured Outputs for Reasoning Models

When using structured outputs with reasoning models like `sonar-reasoning-pro`, the response will include a `<think>` section containing reasoning tokens, immediately followed by the structured output. The `response_format` parameter does not remove these reasoning tokens from the output, so the final response will need to be parsed manually.**Sample Response:**

```
<think>
I need to provide information about France in a structured JSON format with specific fields: country, capital, population, official_language.

For France:
- Country: France
- Capital: Paris
- Population: About 67 million (as of 2023)
- Official Language: French

Let me format this information as required.
</think>
{"country":"France","capital":"Paris","population":67750000,"official_language":"French"}
```

For a reusable implementation to extract JSON from reasoning model outputs, see our [example utility on GitHub](https://github.com/ppl-ai/api-discussion/blob/main/utils/extract_json_reasoning_models.py).

</details>

<details>
<summary>Structured Outputs with Perplexity AI</summary>

# Structured Outputs with Perplexity AI

This guide demonstrates how to use Perplexity AI with Instructor to generate structured outputs. You'll learn how to use Perplexity's Sonar models with Pydantic to create type-safe, validated responses.

Perplexity AI provides access to powerful language models through their API. Instructor supports structured outputs with Perplexity's models using the OpenAI-compatible API.

Perplexity AI currently supports the following mode with Instructor:

- `PERPLEXITY_JSON`: Direct JSON response generation

## Additional Resources

- [Perplexity API Documentation](https://docs.perplexity.ai/)
- [Perplexity API Reference](https://docs.perplexity.ai/reference/post_chat_completions)

</details>


## Local Files From Research

<details>
<summary>Lesson 17: Research Loop with Query Generation and Human-in-the-Loop Feedback</summary>

# Lesson 17: Research Loop with Query Generation and Human-in-the-Loop Feedback

In this lesson, we'll dive deep into the research loop that forms the heart of our research agent's intelligence. We'll explore how the agent generates relevant search queries based on content gathered in previous lessons and uses Perplexity to expand its knowledge base. We'll see also how to integrate human feedback into the research workflow. This creates a powerful human-in-the-loop system that allows users to guide the research direction while leveraging the agent's analytical capabilities.

Learning Objectives:
- Learn how to generate contextual research queries using LLMs and structured outputs
- Understand how to integrate external research services like Perplexity for comprehensive web search
- Implement human-in-the-loop feedback mechanisms in agentic workflows
- Explore the iterative design process behind building effective AI research agents

## 1. Setup

First, we define some standard Magic Python commands to autoreload Python packages whenever they change:

```python
%load_ext autoreload
%autoreload 2
```


### Set Up Python Environment

To set up your Python virtual environment using `uv` and load it into the Notebook, follow the step-by-step instructions from the `Course Admin` lesson from the beginning of the course.

**TL/DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.

### Configure Required APIs

To run this lesson, you'll need several API keys configured:

1. **Gemini API Key**, `GOOGLE_API_KEY` variable: Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. **Perplexity API Key**, `PPLX_API_KEY` variable: Get your key from [Perplexity](https://www.perplexity.ai/settings/api).
3. **Firecrawl API Key**, `FIRECRAWL_API_KEY` variable: Get your key from [Firecrawl](https://firecrawl.dev/). They have a free tier that allows you to scrape 500 pages.

```python
from utils import env

env.load(required_env_vars=["GOOGLE_API_KEY", "PPLX_API_KEY", "FIRECRAWL_API_KEY"])
```

**Output:**
```
Environment variables loaded from `/Users/fabio/Desktop/course-ai-agents/.env`
Environment variables loaded successfully.
```


### Import Key Packages

```python
import nest_asyncio
nest_asyncio.apply() # Allow nested async usage in notebooks
```


## 2. Understanding the Research Loop

The research loop is where our agent becomes truly intelligent. After gathering initial content from guidelines (as we saw in previous lessons), the agent enters a 3-round research cycle designed to fill knowledge gaps and expand understanding.

From the MCP prompt workflow, here's how the research loop works. We'll see its implementation in the next sections.

```markdown
3. Repeat the following research loop for 3 rounds:

    3.1. Run the "generate_next_queries" tool to analyze the ARTICLE_GUIDELINE_FILE, the already-scraped guideline
    URLs, and the existing PERPLEXITY_RESULTS_FILE. The tool identifies knowledge gaps, proposes new web-search
    questions, and writes them - together with a short justification for each - to the NEXT_QUERIES_FILE within
    NOVA_FOLDER.

    3.2. Run the "run_perplexity_research" tool with the new queries. This tool executes the queries with
    Perplexity and appends the results to the PERPLEXITY_RESULTS_FILE within NOVA_FOLDER.
```

## 3. The Philosophy: Plugging Into Specialized Services

Before diving into the implementation, it's important to understand our architectural philosophy. Similar to our approach with web scraping using Firecrawl, we're leveraging Perplexity for web search rather than building our own solution.

**Why use external services like Perplexity?**

Perplexity is an AI-powered search engine that combines the capabilities of large language models with real-time web search.

When there's a general problem faced by many in the industry, it's often more efficient to plug into dedicated tools rather than building every element yourself, similarly to what we did in the previous lesson with Firecrawl for scraping. Companies like Perplexity make LLM-based web search their entire business, investing heavily in:

- Comprehensive source coverage across the web
- Real-time information retrieval
- Advanced ranking and relevance algorithms
- Handling of dynamic content and paywalls
- Rate limiting and API reliability

This allows us to focus on the unique elements of our research agent: the intelligent query generation, human feedback integration, and workflow orchestration.

## 4. Query Generation: The Brain of the Research Loop

The `generate_next_queries` tool is where the magic happens. It analyzes all available context and intelligently identifies knowledge gaps to fill.

### 4.1 Understanding the Implementation

Let's examine the core implementation:

Source: _mcp_server/src/tools/generate_next_queries_tool.py_

```python
async def generate_next_queries_tool(research_directory: str, n_queries: int = 5) -> Dict[str, Any]:
    """
    Generate candidate web-search queries for the next research round.

    Analyzes the article guidelines, already-scraped content, and existing Perplexity
    results to identify knowledge gaps and propose new web-search questions.
    Each query includes a rationale explaining why it's important for the article.
    Results are saved to next_queries.md in the research directory.
    """
    # Convert to Path object
    research_path = Path(research_directory)
    nova_path = research_path / NOVA_FOLDER

    # Gather context from the research folder
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    results_path = nova_path / PERPLEXITY_RESULTS_FILE
    urls_from_guidelines_dir = nova_path / URLS_FROM_GUIDELINES_FOLDER

    article_guidelines = read_file_safe(guidelines_path)
    past_research = read_file_safe(results_path)

    # Collect all scraped content for context
    scraped_ctx_parts: List[str] = []
    if urls_from_guidelines_dir.exists():
        for md_file in sorted(urls_from_guidelines_dir.glob(f"*{MARKDOWN_EXTENSION}")):
            scraped_ctx_parts.append(md_file.read_text(encoding="utf-8"))
    scraped_ctx_str = "\n\n".join(scraped_ctx_parts)

    # Generate queries using LLM
    queries_and_reasons = await generate_queries_with_reasons(
        article_guidelines, past_research, scraped_ctx_str, n_queries=n_queries
    )

    # Write to next_queries.md (overwrite)
    next_q_path = nova_path / NEXT_QUERIES_FILE
    write_queries_to_file(next_q_path, queries_and_reasons)

    return {
        "status": "success",
        "queries_count": len(queries_and_reasons),
        "queries": queries_and_reasons,
        "output_path": str(next_q_path.resolve()),
        "message": f"Successfully generated {len(queries_and_reasons)} candidate queries..."
    }
```

The tool gathers three types of context:

1. **Article Guidelines** (`article_guidelines`): The original requirements and scope read from the `ARTICLE_GUIDELINE_FILE`. This provides the foundational understanding of what the article should cover.

2. **Past Research** (`past_research`): Previous Perplexity results read from the `PERPLEXITY_RESULTS_FILE`. This ensures the LLM doesn't generate duplicate queries and can identify gaps in existing research.

3. **Scraped Content** (`scraped_ctx_str`): All content from guideline URLs (web pages, GitHub repos, YouTube transcripts) concatenated together. This provides comprehensive background context that helps the LLM understand what information is already available.

The LLM analyzes all three contexts simultaneously. It uses the article guidelines to understand the target scope, reviews past research to see what's already been covered, and examines scraped content to understand the existing knowledge base. This comprehensive analysis enables it to generate queries that specifically target knowledge gaps. For example, if the article guidelines mention "error handling in AI agents" but neither past research nor scraped content covers this topic adequately, the LLM will prioritize generating queries about error handling strategies.

### 4.2 The LLM-Powered Query Generation

The actual query generation happens in the `generate_queries_with_reasons` function:

Source: _mcp_server/src/app/generate_queries_handler.py_

```python
async def generate_queries_with_reasons(
    article_guidelines: str,
    past_research: str,
    scraped_ctx: str,
    n_queries: int = 5,
) -> List[Tuple[str, str]]:
    """Return a list of tuples (query, reason)."""

    prompt = PROMPT_GENERATE_QUERIES_AND_REASONS.format(
        n_queries=n_queries,
        article_guidelines=article_guidelines or "<none>",
        past_research=past_research or "<none>",
        scraped_ctx=scraped_ctx or "<none>",
    )

    chat_llm = get_chat_model(settings.query_generation_model, GeneratedQueries)
    response = await chat_llm.ainvoke(prompt)

    queries_and_reasons = [(item.question, item.reason) for item in response.queries]
    return queries_and_reasons[:n_queries]
```

This is the prompt used for query generation. It can potentially have contexts of ~100k tokens or more:

Source: _mcp_server/src/config/prompts.py_

```python
PROMPT_GENERATE_QUERIES_AND_REASONS = """
You are a research assistant helping to craft an article.

Your task: propose {n_queries} diverse, insightful web-search questions
that, taken **as a group**, will collect authoritative sources for the
article **and** provide a short explanation of why each question is
important.

<article_guidelines>
{article_guidelines}
</article_guidelines>

<past_research>
{past_research}
</past_research>

<scraped_context>
{scraped_ctx}
</scraped_context>

Guidelines for the set of queries:
• Give priority to sections/topics from the article guidelines that
  currently lack supporting sources in <past_research> and
  <scraped_context>.
• Cover any remaining major sections to ensure balanced coverage.
• Avoid duplication; each query should target a distinct aspect.
• The web search queries should be natural language questions, not just keywords.
""".strip()
```

This prompt explicitly instructs the LLM to identify missing information and ensures queries cover different aspects rather than duplicating.

Last, the `generate_queries_with_reasons` function uses Pydantic models to ensure consistent, structured responses:

Source: _mcp_server/src/models/query_models.py_

```python
class QueryAndReason(BaseModel):
    """A single web-search query and the reason for it."""

    question: str = Field(description="The web-search question to research.")
    reason: str = Field(description="The reason why this question is important for the research.")

class GeneratedQueries(BaseModel):
    """A list of generated web-search queries and their reasons."""

    queries: List[QueryAndReason] = Field(description="A list of web-search queries and their reasons.")
```

This structured approach ensures the LLM returns exactly what we need: queries paired with clear justifications. These justifications have multiple purposes:
1. They help the LLM understand why each query is important for the research, similarly to how chain of thought prompts work.
2. They help us understand the LLM's thought process when generating queries, which is useful for debugging and improving the prompt. It's also useful for the human in the loop for providing useful feedback to the agent.

Let's test the `generate_queries_with_reasons` function to see how it works in practice:

```python
from research_agent_part_2.mcp_server.src.app.generate_queries_handler import generate_queries_with_reasons

# Example inputs (simplified for demonstration)
article_guidelines = '''
# Article: Advanced Function Calling with LLMs

## Sections to cover:
1. Error handling strategies
2. Performance optimization
3. Security considerations
4. Best practices for production
'''

past_research = '''
### Source [1]: https://example.com/basic-function-calling
Query: What is function calling in LLMs?
Answer: Function calling allows LLMs to invoke external tools and APIs...

### Source [2]: https://example.com/simple-examples  
Query: How to implement basic function calling?
Answer: Basic implementation involves defining function schemas...
'''

scraped_ctx = '''
# Function Calling Documentation
This guide covers the fundamentals of function calling...
[Basic examples and simple use cases already covered]
'''

# Generate queries based on this context
queries_and_reasons = await generate_queries_with_reasons(
    article_guidelines=article_guidelines,
    past_research=past_research,
    scraped_ctx=scraped_ctx,
    n_queries=3
)

for query, reason in queries_and_reasons:
    print(f"Query: {query}")
    print(f"Reason: {reason}")
    print("---")
```

**Output:**
```
/Users/fabio/Desktop/course-ai-agents/.venv/lib/python3.12/site-packages/pydantic/_internal/_fields.py:198: UserWarning: Field name "schema" in "FewShotExampleStructuredOutputCompliance" shadows an attribute in parent "BaseModel"
  warnings.warn(
/Users/fabio/Desktop/course-ai-agents/.venv/lib/python3.12/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
  from .autonotebook import tqdm as notebook_tqdm
```

**Output:**
```
Query: What are the most common security vulnerabilities when giving LLMs access to external tools via function calling, and what are the established mitigation strategies?
Reason: This question directly targets the 'Security considerations' section, a critical topic for production systems that is not covered in the existing research. It seeks to find authoritative sources on risks and specific, actionable solutions.
---
Query: How can latency be minimized and token usage be optimized when using chained or parallel function calls with large language models?
Reason: This addresses the 'Performance optimization' section. It focuses on advanced, practical challenges like speed and cost-efficiency, especially in complex scenarios that go beyond single, basic function calls.
---
Query: What are robust error handling patterns for LLM function calling when external API calls fail, return unexpected data, or the LLM hallucinates a function call?
Reason: This covers the 'Error handling strategies' section. It aims to find expert advice on building resilient systems, which is a cornerstone of production-readiness and a key theme for an 'advanced' article.
---
```

**Output:**
```
[32m2025-09-23 10:07:20.276[0m | [31m[1mERROR   [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | Research folder does not exist: /path/to/research_folder
[32m2025-09-23 10:07:20.467[0m | [1mINFO    [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | Exception in execute request:
[31m---------------------------------------------------------------------------[39m
[31mValueError[39m                                Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[5][39m[32m, line 5[39m
[32m      3[39m [38;5;66;03m# Update this path to your actual sample research folder[39;00m
[32m      4[39m research_folder = [33m"[39m[33m/path/to/research_folder[39m[33m"[39m
[32m----> [39m[32m5[39m result = [38;5;28;01mawait[39;00m generate_next_queries_tool(research_directory=research_folder, n_queries=[32m3[39m)
[32m      6[39m [38;5;28mprint[39m(result)

[36mFile [39m[32m~/Desktop/course-ai-agents/lessons/research_agent_part_2/mcp_server/src/tools/generate_next_queries_tool.py:76[39m, in [36mgenerate_next_queries_tool[39m[34m(research_directory, n_queries)[39m
[32m     73[39m nova_path = research_path / NOVA_FOLDER
[32m     75[39m [38;5;66;03m# Validate folders and files[39;00m
[32m---> [39m[32m76[39m [43mvalidate_research_folder[49m[43m([49m[43mresearch_path[49m[43m)[49m
[32m     78[39m [38;5;66;03m# Create NOVA_FOLDER directory if it doesn't exist[39;00m
[32m     79[39m nova_path.mkdir(parents=[38;5;28;01mTrue[39;00m, exist_ok=[38;5;28;01mTrue[39;00m)

[36mFile [39m[32m~/Desktop/course-ai-agents/lessons/research_agent_part_2/mcp_server/src/utils/file_utils.py:38[39m, in [36mvalidate_research_folder[39m[34m(research_path)[39m
[32m     36[39m     msg = [33mf[39m[33m"[39m[33mResearch folder does not exist: [39m[38;5;132;01m{[39;00mresearch_path[38;5;132;01m}[39;00m[33m"[39m
[32m     37[39m     logger.error(msg)
[32m---> [39m[32m38[39m     [38;5;28;01mraise[39;00m [38;5;167;01mValueError[39;00m(msg)
[32m     40[39m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m research_path.is_dir():
[32m     41[39m     msg = [33mf[39m[33m"[39m[33mPath is not a directory: [39m[38;5;132;01m{[39;00mresearch_path[38;5;132;01m}[39;00m[33m"[39m

[31mValueError[39m: Research folder does not exist: /path/to/research_folder
[32m2025-09-23 10:07:55.201[0m | [1mINFO    [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | HTTP Request: POST https://api.perplexity.ai/chat/completions "HTTP/1.1 200 OK"
[32m2025-09-23 10:08:02.384[0m | [1mINFO    [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | HTTP Request: POST https://api.perplexity.ai/chat/completions "HTTP/1.1 200 OK"
[32m2025-09-23 10:08:23.489[0m | [33m[1mWARNING [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | File not found: /Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova...
```


**Understanding the Output**

When you run this code, you'll see output similar to this example:

```
Query: What are the most common security vulnerabilities when implementing LLM function calling and how can they be mitigated?
Reason: This question directly targets the 'Security considerations' section of the article, which is not covered by existing research...

Query: What are effective strategies for optimizing the performance and reducing latency of function calling in large language models?
Reason: This question addresses the 'Performance optimization' section. The existing research covers basic implementation...

Query: What are the best practices for error handling and ensuring reliability in production-level LLM function calling systems?
Reason: This question is designed to gather information for the 'Error handling strategies' and 'Best practices for production' sections...
```

Observe the following:

1. **Gap Analysis**: Notice how the LLM identified that the existing research only covers "basic function calling" and "simple examples", then generated queries specifically targeting the missing advanced topics (security, performance, error handling).

2. **Section Mapping**: Each generated query directly maps to sections mentioned in the article guidelines that lack coverage. The LLM demonstrates sophisticated understanding by connecting article requirements to knowledge gaps.

3. **Query Quality**: The queries are well-crafted, specific, and actionable. Instead of generic questions like "What is security?", it asks targeted questions like "What are the most common security vulnerabilities when implementing LLM function calling?"

4. **Reasoning Transparency**: Each query comes with clear reasoning explaining why it's important and which article section it addresses. This transparency helps users understand the LLM's decision-making process.

5. **Progressive Complexity**: The LLM naturally progresses from basic concepts (already covered) to advanced topics (security, performance, production practices), showing an understanding of knowledge hierarchies.

This intelligent gap analysis is what makes the research loop so powerful - it doesn't just generate random queries, but strategically identifies exactly what information is missing to complete the article's objectives.


## 5. Perplexity Integration

Once we have our queries, we need to execute them efficiently. The `run_perplexity_research_tool` tool handles this integration with concurrent execution and structured outputs.

### 5.1 The Research Tool Implementation

The `run_perplexity_research_tool` is the orchestrator that manages the entire Perplexity research process:

Source: _mcp_server/src/tools/run_perplexity_research_tool.py_

```python
async def run_perplexity_research_tool(research_directory: str, queries: List[str]) -> Dict[str, Any]:
    """
    Run Perplexity research queries for the research folder.

    Executes the provided queries using Perplexity's Sonar-Pro model and appends
    the results to perplexity_results.md in the research directory. Each query
    result includes the answer and source citations.
    """
    research_path = Path(research_directory)
    nova_path = research_path / NOVA_FOLDER
    results_path = nova_path / PERPLEXITY_RESULTS_FILE

    if not queries:
        return {
            "status": "success",
            "message": "No queries provided – nothing to do.",
            "queries_processed": 0,
            "sources_added": 0,
        }

    # Execute all queries concurrently
    tasks = [run_perplexity_search(query) for query in queries]
    search_results = await asyncio.gather(*tasks)

    # Process and append search results to file
    total_sources = append_search_results_to_file(results_path, queries, search_results)

    return {
        "status": "success",
        "queries_processed": len(queries),
        "sources_added": total_sources,
        "output_path": str(results_path.resolve()),
        "message": f"Successfully completed Perplexity research round..."
    }
```

**How this function works:**

1. **Path Setup**: It establishes the file paths for storing results, specifically the `PERPLEXITY_RESULTS_FILE` in the `.nova` folder.

2. **Concurrent Execution of Perplexity Searches**: The key performance optimization is concurrent execution. Instead of running queries sequentially (which would be slow), it creates a list of tasks using `[run_perplexity_search(query) for query in queries]` and executes them all at once with `asyncio.gather(*tasks)`.

3. **Result Processing**: The `append_search_results_to_file` function processes all the search results and appends them to the persistent results file, maintaining unique source IDs across multiple research rounds.

4. **Cumulative Storage**: Results from each round are appended (not overwritten) to the same file, building up a comprehensive research database over the 3 rounds.

This design ensures fast execution while maintaining a complete audit trail of all research conducted.

### 5.2 Structured Perplexity Responses

The core Perplexity integration uses structured outputs to ensure consistent, parseable results. This is important: we're not just getting raw text responses, but structured data that our system can reliably process.

Source: _mcp_server/src/app/perplexity_handler.py_

```python
class SourceAnswer(BaseModel):
    """A single source answer with URL and content."""

    url: str = Field(description="The URL of the source")
    answer: str = Field(description="The detailed answer extracted from that source")

class PerplexityResponse(BaseModel):
    """Structured response from Perplexity search containing multiple sources."""

    sources: List[SourceAnswer] = Field(description="List of sources with their answers")

async def run_perplexity_search(query: str) -> Tuple[str, Dict[int, str], Dict[int, str]]:
    """Run a Perplexity Sonar-Pro search and return full answer + parsed sections."""
    
    llm = get_chat_model("perplexity", PerplexityResponse)
    prompt = PROMPT_WEB_SEARCH.format(query=query)
    
    response = await llm.ainvoke(prompt)
    
    # Convert structured response to expected format
    answer_by_source = {}
    citations = {}
    for i, source in enumerate(response.sources, 1):
        answer_by_source[i] = source.answer
        citations[i] = source.url

    return full_answer, answer_by_source, citations
```

When you run a Perplexity search as above, you get a structured response like this:

```python
# Example of what run_perplexity_search returns for a query about "LLM function calling best practices"

full_answer = '''### [1]: https://openai.com/docs/guides/function-calling
Function calling allows models to connect to external tools and APIs...

### [2]: https://docs.anthropic.com/claude/docs/tool-use
Claude can use tools to perform actions beyond text generation...

### [3]: https://ai.google.dev/gemini-api/docs/function-calling
Gemini models support function calling for structured interactions...
'''

answer_by_source = {
    1: "Function calling allows models to connect to external tools and APIs. Best practices include defining clear schemas, handling errors gracefully, and validating inputs...",
    2: "Claude can use tools to perform actions beyond text generation. Key considerations include security, rate limiting, and proper error handling...",
    3: "Gemini models support function calling for structured interactions. Important aspects include schema design, response validation, and performance optimization..."
}

citations = {
    1: "https://openai.com/docs/guides/function-calling",
    2: "https://docs.anthropic.com/claude/docs/tool-use", 
    3: "https://ai.google.dev/gemini-api/docs/function-calling"
}
```

This structured format ensures that:
- **Each source is clearly separated** and can be processed independently
- **URLs are preserved** for citation and potential full scraping later
- **Content is substantial** (up to 300 words per source) for comprehensive coverage
- **Data is parseable** by downstream processing tools

### 5.3 The Perplexity Search Prompt

The prompt used for Perplexity searches is designed to extract maximum value:

```python
PROMPT_WEB_SEARCH = """
Question: {query}

Provide a detailed answer to the question above.
The answer should be organized into source sections, where each source section
contains all the information coming from a single source.
Never use multiple source citations in the same source section. A source section should refer to a single source.
Focus on the official sources and avoid personal opinions.
For each source, write as much information as possible coming from the source
and that is relevant to the question (at most 300 words).

Return a list of objects, where each object represents a source and has the following fields:
- url: The URL of the source
- answer: The detailed answer extracted from that source
""".strip()
```

This prompt ensures that each source is clearly identified and separated, that up to 300 words per source for detailed information, and that the output is in a consistent format for parsing and storage.

## 6 Testing the tools

### 6.1 Testing the Query Generation Tool

Let's test the query generation tool programmatically to understand its output:

```python
from research_agent_part_2.mcp_server.src.tools import generate_next_queries_tool

# Update this path to your actual sample research folder
research_folder = "/path/to/research_folder"
result = await generate_next_queries_tool(research_directory=research_folder, n_queries=3)
print(result)
```

**Output:**
```
{'status': 'success', 'queries_count': 3, 'queries': [('What are the fundamental limitations of large language models that necessitate the use of external tools?', 'This question addresses the core "why" behind function calling, directly supporting the "Understanding why agents need tools" section of the article. The provided text explains *how* to use tools with a specific API, but this query will find sources that explain the foundational reasons, such as the inability to access real-time data, perform precise calculations, or interact with private APIs.'), ('How do the function calling or tool use APIs of major LLM providers like OpenAI, Gemini, and Anthropic compare in terms of features and implementation?', "The supplied context is exclusively about the Gemini API. To create a balanced and authoritative article, it's crucial to compare this with other major platforms. This query will uncover differences in syntax, capabilities (like parallel vs. sequential calling), and terminology, providing a comprehensive market overview for the reader."), ('What are the established design patterns and best practices for building robust, multi-tool LLM agents, particularly regarding error handling and security?', "The provided documentation covers simple tool-use cases but doesn't delve into the complexities of real-world agentic systems. This query targets advanced, practical knowledge on topics like the ReAct framework, managing conversational state, handling tool failures gracefully, and ensuring the secure execution of actions, which is critical for developers building production-level applications.")], 'output_path': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/next_queries.md', 'message': 'Successfully generated 3 candidate queries for research folder \'/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder\'. Queries and reasons saved to: .nova/next_queries.md\n\nGenerated Queries:\n\n1. What are the fundamental limitations of large language models that necessitate the use of external tools?\nReason: This question addresses the core "why" behind function calling, directly supporting the "Understanding why agents need tools" section of the article. The provided text explains *how* to use tools with a specific API, but this query will find sources that explain the foundational reasons, such as the inability to access real-time data, perform precise calculations, or interact with private APIs.\n\n2. How do the function calling or tool use APIs of major LLM providers like OpenAI, Gemini, and Anthropic compare in terms of features and implementation?\nReason: The supplied context is exclusively about the Gemini API. To create a balanced and authoritative article, it\'s crucial to compare this with other major platforms. This query will uncover differences in syntax, capabilities (like parallel vs. sequential calling), and terminology, providing a compre...
```


The output will show a structured summary like:

```json
{
  "status": "success",
  "queries_count": 3,
  "queries": [
    ("What are the latest best practices for implementing function calling with LLMs?", "This query addresses implementation details that may not be fully covered in the basic documentation from the guidelines."),
    ("How do different LLM providers handle function calling differently?", "Understanding provider-specific approaches will help create more comprehensive guidance."),
    ("What are common pitfalls and debugging techniques for function calling?", "Practical troubleshooting information is essential for developers implementing these systems.")
  ],
  "output_path": "/path/to/research_folder/.nova/next_queries.md",
  "message": "Successfully generated 3 candidate queries for research folder..."
}
```

### 6.2 Testing the Perplexity Research Tool

Now let's test the Perplexity research functionality:

```python
from research_agent_part_2.mcp_server.src.tools import run_perplexity_research_tool

# Example queries to test
test_queries = [
    "What are the latest developments in LLM function calling?",
    "How do you handle errors in AI agent tool execution?"
]

result = await run_perplexity_research_tool(
    research_directory=research_folder, 
    queries=test_queries
)
print("Tool call output:")
print(result)
print()

print("Content of the resulting file:")
with open(result["output_path"], "r") as f:
    print(f.read())
```

**Output:**
```
Tool call output:
{'status': 'success', 'queries_processed': 2, 'sources_added': 7, 'output_path': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/perplexity_results.md', 'message': "Successfully completed Perplexity research round for research folder '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder'. Processed 2 queries and added 7 source sections to perplexity_results.md"}

Content of the resulting file:
### Source [1]: https://arxiv.org/html/2505.20192v1

Query: What are the latest developments in LLM function calling?

Answer: The paper introduces **FunReason**, a novel framework designed to enhance large language models’ (LLMs) function calling capabilities. FunReason addresses the challenge of combining detailed reasoning with accurate function execution—a known limitation of prior approaches—by employing an automated data refinement strategy and a Self-Refinement Multiscale Loss (SRML) technique. This approach allows LLMs to generate high-quality training examples, focusing on three aspects: query parseability, reasoning coherence, and function call precision. The SRML dynamically balances reasoning and function call accuracy during training, overcoming the typical trade-off between these factors. The authors report that FunReason achieves performance on par with GPT-4o and effectively mitigates catastrophic forgetting during fine-tuning. The work positions function calling as central for LLM practical utility, highlighting a shift from prompt engineering to more data-driven and fine-tuned approaches, including reinforcement learning (RL)-based optimization for task success. The availability of code and datasets is emphasized, supporting reproducibility and practical adoption.

-----

### Source [2]: https://aclanthology.org/2025.naacl-industry.9.pdf

Query: What are the latest developments in LLM function calling?

Answer: This research explores strategies to enhance function-calling capabilities in LLMs, particularly for autonomous agents. Key advances include: (1) using instruction-following data to improve both function-calling accuracy and the ability to detect relevant functions, (2) experimenting with different prompt formats, including the integration of function descriptions and a novel Decision Token for conditional prompts, (3) blending function-calling and instruction-following data in training, (4) employing chain-of-thought reasoning to clarify the steps leading to a function call, and (5) introducing a translation pipeline to overcome multilingual challenges in function calling. Results show that combining instruction-following and function-calling data yields better performance than training on either type alone, and chain-of-thought reasoning further enhances interpretability and accuracy, especially in complex or multilingual scenarios.

-----

### Source [3]: https://arxiv.org/html/2509.18076v1

Query: What are the l...
```


## 7. Human-in-the-Loop

One of the most powerful aspects of our research agent is its ability to integrate human feedback directly into the workflow. This transforms the agent from a fully automated system into a collaborative research partner.

### 7.1 How Human Feedback Works

The agent can be instructed to pause after generating queries and ask for human approval before proceeding. This is accomplished by modifying the workflow instructions when triggering the MCP prompt.

When the user starts the research workflow, they can specify modifications like:
- "Ask for my feedback after generating each set of queries"
- "Show me the proposed queries and wait for my approval before running them"
- "Let me select which queries to run from the generated list"

Let's see how to run the complete research agent with human-in-the-loop feedback. We'll start the MCP client and demonstrate how to request user feedback integration.

```python
from research_agent_part_2.mcp_client.src.client import main as client_main
import sys

async def run_client():
    _argv_backup = sys.argv[:]
    sys.argv = ["client"]
    try:
        await client_main()
    finally:
        sys.argv = _argv_backup

# Start client with in-memory server 
await run_client()
```

**Output:**
```
🛠️  Available tools: 11
📚 Available resources: 2
💬 Available prompts: 1

Available Commands: /tools, /resources, /prompts, /prompt/<name>, /resource/<uri>, /model-thinking-switch, /quit


[1m[95m🤔 LLM's Thoughts:[0m
[35m**Ready to Begin the Research Workflow!**

Okay, so I'm geared up and ready to dive into this research project. The user has given me the go-ahead, so let's get rolling. First things first, I need to outline the workflow. I'll make sure the user understands what I'm about to do, so they know what to expect.

Here's the plan, in a nutshell:

1.  **Setting the Stage (Setup):**  I'll start by taking a look at the `ARTICLE_GUIDELINE_FILE` to grab any URLs and local files that are relevant. It's like collecting my starting ingredients.

2.  **Processing the Resources (In Parallel):**  This is the bulk of the action.  I'll be working in parallel to speed things up. I'll be copying the local files, scraping and cleaning content from those websites, processing GitHub links (summarizing and collecting the content), and even transcribing YouTube videos. Efficiency is key!

3.  **The Research Loop (3 Rounds):** Time to start generating new web search queries. Based on what I've learned, I'll generate new queries and use Perplexity to get the latest info. This is my "knowledge loop," and I'll do this three times to get a broader view.

4.  **Filtering Perplexity Results:** Now it's time to refine those results. I'll need to sift through all of the Perplexity results and pick the best sources. I'm looking for trustworthiness, authority, and real relevance to the topic. I will weed out anything questionable.

5.  **Finding Full Sources:** I'll pick the best 5 sources for the full scrape. These are the "keepers."  Once I have them, I'll scrape all of the content of the selected sources.

6.  **Writing the Research Document:**  Finally, I'll synthesize everything into a complete `RESEARCH_MD_FILE`. This is where all the data, research, and insights come together. This will be the output!

Now, before I jump into all of that, I need to get the `research_directory` from the user. And, I need to know if they want me to start at a specific step or add any feedback. This is important to ensure I'm on the same page and that I'm delivering exactly what they're looking for. Once I've got that, I'm ready to kick things off at step 1.3: `extract_guidelines_urls`. I'm excited to see where this leads![0m

[37m💬 LLM Response: [0mHere's a breakdown of the research workflow steps:

1.  **Setup**: Extracts URLs (GitHub, YouTube, other web links) and local file references from your `ARTICLE_GUIDELINE_FILE`.
2.  **Process Extracted Resources**: Simultaneously processes the extracted resources:
    *   Copies referenced local files to a dedicated folder.
    *   Scrapes and cleans content from other web URLs.
    *   Processes GitHub URLs to create summaries and content.
    *   Transcribes YouTube videos.
3.  **Research Loop**: Repeats for 3 rounds:
    ...
```

**Output:**
```
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1758615120.793915 3155870 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
```

**Output:**
```
[1m[95m🤔 LLM's Thoughts:[0m
[35m**Navigating the Research Workflow**

Okay, here's the deal. I've successfully completed the initial steps of this research project. I've extracted the guidelines' URLs (Step 1.3), checked for local files (there were none, Step 2.1), and scraped & cleaned other URLs (Step 2.2). Now, I need to execute Steps 2.3 and 2.4 concurrently - that's the next logical move, and it aligns perfectly with the requested workflow.

The real shift happens at Step 3, the research loop. The user wants me to be more interactive here. I have to pause after generating each set of research queries and get approval before running them through Perplexity. That's a key modification, and I'll need to implement that specifically.

Just to be clear, the research directory is `/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder`, and my task is to halt the process after Step 3. No need to move on to steps 4, 5, or 6. That's the objective. I'm ready to tackle 2.3 and 2.4, and then jump into the modified research loop.[0m


[1m[36m🔧 Function Call (Tool):[0m
[36m  Tool: [0m[1m[36mprocess_github_urls[0m
[36m  Arguments: [0m[36m{
  "research_directory": "/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder"
}[0m

[36m⚡ Executing tool 'process_github_urls' via MCP server...[0m
[36m✅ Tool execution successful![0m

[1m[95m🤔 LLM's Thoughts:[0m
[35m**Okay, Here's My Plan**

Alright, I'm at the point where I'm ready to dive back in. I've got the setup done and the resources are prepped and ready, thanks to the parallel processing. Now, I need to get started with the YouTube transcription part - that's step 2.4. Once that's done, I'll be in the heart of the research loop.

The key thing is, the user wants a more interactive approach this time. They want to provide feedback and approve the direction of the research. So, after I generate the queries in the research loop (step 3.1), I need to *immediately* loop back and present those queries for their input. No running ahead! Then, *only* after getting their green light (step 3.2), will I actually send those queries over to Perplexity. It's a much more controlled, deliberate process.

I'm aiming to go through this query-feedback-approval cycle three times. Then, I need to remember to *stop* the whole workflow right after that research loop is complete (step 3). No extra steps, just exactly what's been requested. Let's get these YouTube URLs transcribed and get moving.[0m


[1m[36m🔧 Function Call (Tool):[0m
[36m  Tool: [0m[1m[36mtranscribe_youtube_urls[0m
[36m  Arguments: [0m[36m{
  "research_directory": "/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder"
}[0m

[36m⚡ Executing tool 'transcribe_youtube_urls' via MCP server...[0m
[36m✅ Tool execution successful![0m

[1m[95m🤔 LLM's Thoughts:[0m
[35m**My Research Workflow - Iteration 1*...
```


Once the client is running, try these commands in sequence:

1. **Start the workflow with feedback**: `/prompt/full_research_instructions_prompt`

2. **Request human feedback integration**: When the agent asks for the research directory and workflow modifications, respond with:
   ```
   The research folder is /path/to/your/research_folder. Please modify the workflow to ask for my feedback after generating each set of queries in the research loop. Show me the proposed queries and wait for my approval before running them with Perplexity. Run up to step 3 of the workflow and then stop there, don't run the rest of the workflow from step 4 onwards.
   ```
   Otherwise, if you've run steps 1 and 2 of the workflow already, you can request the following:
   ```
   The research folder is /path/to/your/research_folder. Please modify the workflow to ask for my feedback after generating each set of queries in the research loop. Show me the proposed queries and wait for my approval before running them with Perplexity. Run only step 3 of the workflow and then stop there, don't run the rest of the workflow from step 4 onwards. Don't run steps 1 and 2 of the workflow.
   ```
3. **Observe the agent behavior**: The agent will:
   - Run the initial data ingestion (steps 1-2)
   - Generate the first set of research queries
   - **Pause and show you the queries**
   - Wait for your feedback before proceeding, allowing you to approve, modify, or reject queries

4. **Provide feedback**: You can respond with:
   - "Approve all queries" to proceed as planned
   - "Only run queries 1, 3, and 5" to select specific queries
   - "Replace query 2 with: [your custom query]" to modify the research direction

5. **Continue the loop**: The agent will repeat this process for each of the 3 research rounds. You can stop the loop by responding with `/quit"`.

</details>


## Code Sources

_No code sources found._


## YouTube Video Transcripts

_No YouTube video transcripts found._


## Additional Sources Scraped

<details>
<summary>chat-completions-perplexity</summary>

```markdown
Chat Completions

```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "model": "sonar-deep-research",
  "messages": [\
    {\
      "role": "system",\
      "content": "Be precise and concise."\
    },\
    {\
      "role": "user",\
      "content": "How many stars are there in our galaxy?"\
    }\
  ]
}'
```

```
{
  "id": "<string>",
  "model": "<string>",
  "created": 123,
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 123,
    "total_tokens": 123,
    "search_context_size": "<string>",
    "citation_tokens": 123,
    "num_search_queries": 123,
    "reasoning_tokens": 123
  },
  "object": "chat.completion",
  "choices": [\
    {\
      "index": 123,\
      "finish_reason": "stop",\
      "message": {\
        "content": "<string>",\
        "role": "system"\
      }\
    }\
  ],
  "search_results": [\
    {\
      "title": "<string>",\
      "url": "<string>",\
      "date": "2023-12-25"\
    }\
  ],
  "videos": [\
    {\
      "url": "<string>",\
      "thumbnail_url": "<string>",\
      "thumbnail_width": 123,\
      "thumbnail_height": 123,\
      "duration": 123\
    }\
  ]
}
```

POST

/

chat

/

completions

Chat Completions

```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "model": "sonar-deep-research",
  "messages": [\
    {\
      "role": "system",\
      "content": "Be precise and concise."\
    },\
    {\
      "role": "user",\
      "content": "How many stars are there in our galaxy?"\
    }\
  ]
}'
```

```
{
  "id": "<string>",
  "model": "<string>",
  "created": 123,
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 123,
    "total_tokens": 123,
    "search_context_size": "<string>",
    "citation_tokens": 123,
    "num_search_queries": 123,
    "reasoning_tokens": 123
  },
  "object": "chat.completion",
  "choices": [\
    {\
      "index": 123,\
      "finish_reason": "stop",\
      "message": {\
        "content": "<string>",\
        "role": "system"\
      }\
    }\
  ],
  "search_results": [\
    {\
      "title": "<string>",\
      "url": "<string>",\
      "date": "2023-12-25"\
    }\
  ],
  "videos": [\
    {\
      "url": "<string>",\
      "thumbnail_url": "<string>",\
      "thumbnail_width": 123,\
      "thumbnail_height": 123,\
      "duration": 123\
    }\
  ]
}
```

#### Authorizations

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Body

application/json

model

enum<string>

required

The name of the model that will complete your prompt. Choose from our available Sonar models: sonar (lightweight search), sonar-pro (advanced search), sonar-deep-research (exhaustive research), sonar-reasoning (fast reasoning), or sonar-reasoning-pro (premier reasoning).

Available options:

`sonar`,

`sonar-pro`,

`sonar-deep-research`,

`sonar-reasoning`,

`sonar-reasoning-pro`

Example:

`"sonar-deep-research"`

messages

Message · object\[\]

required

A list of messages comprising the conversation so far.

Showchild attributes

Example:

```
[\
  {\
    "role": "system",\
    "content": "Be precise and concise."\
  },\
  {\
    "role": "user",\
    "content": "How many stars are there in our galaxy?"\
  }\
]
```

search\_mode

enum<string>

default:web

Controls search mode: 'academic' prioritizes scholarly sources, 'sec' prioritizes SEC filings, 'web' uses general web search. See [academic guide](https://docs.perplexity.ai/guides/academic-filter-guide) and [SEC guide](https://docs.perplexity.ai/guides/sec-guide).

Available options:

`academic`,

`sec`,

`web`

reasoning\_effort

enum<string>

**Perplexity-Specific**: Controls how much computational effort the AI dedicates to each query for deep research models. 'low' provides faster, simpler answers with reduced token usage, 'medium' offers a balanced approach, and 'high' delivers deeper, more thorough responses with increased token usage. This parameter directly impacts the amount of reasoning tokens consumed. **WARNING: This parameter is ONLY applicable for sonar-deep-research.** Defaults to 'medium' when used with sonar-deep-research.

Available options:

`low`,

`medium`,

`high`

max\_tokens

integer

**OpenAI Compatible**: The maximum number of completion tokens returned by the API. Controls the length of the model's response. If the response would exceed this limit, it will be truncated. Higher values allow for longer responses but may increase processing time and costs.

temperature

number

default:0.2

The amount of randomness in the response, valued between 0 and 2. Lower values (e.g., 0.1) make the output more focused, deterministic, and less creative. Higher values (e.g., 1.5) make the output more random and creative. Use lower values for factual/information retrieval tasks and higher values for creative applications.

Required range: `0 <= x < 2`

top\_p

number

default:0.9

**OpenAI Compatible**: The nucleus sampling threshold, valued between 0 and 1. Controls the diversity of generated text by considering only the tokens whose cumulative probability exceeds the top\_p value. Lower values (e.g., 0.5) make the output more focused and deterministic, while higher values (e.g., 0.95) allow for more diverse outputs. Often used as an alternative to temperature.

language\_preference

string

**Perplexity-Specific**: Specifies the preferred language for the chat completion response (i.e., English, Korean, Spanish, etc.) of the response content. This parameter is supported only by the `sonar` and `sonar-pro` models. Using it with other models is on a best-effort basis and may not produce consistent results.

search\_domain\_filter

any\[\]

A list of domains to limit search results to. Currently limited to 20 domains for Allowlisting and Denylisting. For Denylisting, add a `-` at the beginning of the domain string. More information about this [here](https://docs.perplexity.ai/guides/search-domain-filters).

return\_images

boolean

default:false

**Perplexity-Specific**: Determines whether search results should include images.

return\_related\_questions

boolean

default:false

**Perplexity-Specific**: Determines whether related questions should be returned.

search\_recency\_filter

string

**Perplexity-Specific**: Filters search results based on time (e.g., 'week', 'day').

search\_after\_date\_filter

string

**Perplexity-Specific**: Filters search results to only include content published after this date. Format should be %m/%d/%Y (e.g. 3/1/2025)

search\_before\_date\_filter

string

**Perplexity-Specific**: Filters search results to only include content published before this date. Format should be %m/%d/%Y (e.g. 3/1/2025)

last\_updated\_after\_filter

string

**Perplexity-Specific**: Filters search results to only include content last updated after this date. Format should be %m/%d/%Y (e.g. 3/1/2025)

last\_updated\_before\_filter

string

**Perplexity-Specific**: Filters search results to only include content last updated before this date. Format should be %m/%d/%Y (e.g. 3/1/2025)

top\_k

number

default:0

**OpenAI Compatible**: The number of tokens to keep for top-k filtering. Limits the model to consider only the k most likely next tokens at each step. Lower values (e.g., 20) make the output more focused and deterministic, while higher values allow for more diverse outputs. A value of 0 disables this filter. Often used in conjunction with top\_p to control output randomness.

stream

boolean

default:false

**OpenAI Compatible**: Determines whether to stream the response incrementally.

presence\_penalty

number

default:0

**OpenAI Compatible**: Positive values increase the likelihood of discussing new topics. Applies a penalty to tokens that have already appeared in the text, encouraging the model to talk about new concepts. Values typically range from 0 (no penalty) to 2.0 (strong penalty). Higher values reduce repetition but may lead to more off-topic text.

frequency\_penalty

number

default:0

**OpenAI Compatible**: Decreases likelihood of repetition based on prior frequency. Applies a penalty to tokens based on how frequently they've appeared in the text so far. Values typically range from 0 (no penalty) to 2.0 (strong penalty). Higher values (e.g., 1.5) reduce repetition of the same words and phrases. Useful for preventing the model from getting stuck in loops.

response\_format

object

Enables structured JSON output formatting.

disable\_search

boolean

default:false

**Perplexity-Specific**: When set to true, disables web search completely and the model will only use its training data to respond. This is useful when you want deterministic responses without external information. More information about this [here](https://docs.perplexity.ai/guides/search-control-guide#disabling-search-completely).

enable\_search\_classifier

boolean

default:false

**Perplexity-Specific**: Enables a classifier that decides if web search is needed based on your query. See more [here](https://docs.perplexity.ai/guides/search-control-guide#search-classifier).

web\_search\_options

object

**Perplexity-Specific**: Configuration for using web search in model responses.

Showchild attributes

Example:

```
{ "search_context_size": "high" }
```

media\_response

object

**Perplexity-Specific**: Configuration for controlling media content in responses, such as videos and images. Use the overrides property to enable specific media types.

Showchild attributes

Example:

```
{
  "overrides": {
    "return_videos": true,
    "return_images": true
  }
}
```

#### Response

200

application/json

OK

id

string

required

A unique identifier for the chat completion.

model

string

required

The model that generated the response.

created

integer

required

The Unix timestamp (in seconds) of when the chat completion was created.

usage

object

required

Showchild attributes

object

string

default:chat.completion

required

The type of object, which is always `chat.completion`.

choices

ChatCompletionsChoice · object\[\]

required

A list of chat completion choices. Can be more than one if `n` is greater than 1.

Showchild attributes

search\_results

ApiPublicSearchResult · object\[\] \| null

A list of search results related to the response.

Showchild attributes

videos

VideoResult · object\[\] \| null

A list of video results when media\_response.overrides.return\_videos is enabled. Contains video URLs and metadata.

Showchild attributes
```

</details>

<details>
<summary>openai-compatibility-perplexity</summary>

## OpenAI compatibility at a glance

Perplexity’s Sonar API was designed with OpenAI compatibility in mind, matching the Chat Completions API interface. You can seamlessly use your existing OpenAI client libraries by simply changing the base URL and providing your Perplexity API key.

Keep using your existing OpenAI SDKs to get started fast; switch to our [native SDKs](https://docs.perplexity.ai/guides/perplexity-sdk) later as needed.

## Configuring OpenAI SDKs to call Sonar

To start using Sonar with OpenAI’s client libraries, pass your Perplexity API key and change the base_url to `https://api.perplexity.ai`:

```
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.perplexity.ai"
)

resp = client.chat.completions.create(
    model="sonar-pro",
    messages=[\
        {"role": "user", "content": "Hello!"}\
    ]
)
print(resp.choices[0].message.content)
```

Your responses will match OpenAI’s format exactly. See the [response structure](https://docs.perplexity.ai/guides/chat-completions-guide?utm_source=chatgpt.com#response-structure) section below for complete field details.

## API compatibility

### Standard OpenAI parameters

These parameters work exactly the same as OpenAI’s API:

- `model` \- Model name (use Perplexity model names)
- `messages` \- Chat messages array
- `temperature` \- Sampling temperature (0-2)
- `max_tokens` \- Maximum tokens in response
- `top_p` \- Nucleus sampling parameter
- `frequency_penalty` \- Frequency penalty (-2.0 to 2.0)
- `presence_penalty` \- Presence penalty (-2.0 to 2.0)
- `stream` \- Enable streaming responses

### Perplexity-specific parameters

These Perplexity-specific parameters are also included:

- `search_domain_filter` \- Limit or exclude specific domains
- `search_recency_filter` \- Filter by content recency
- `return_images` \- Include image URLs in response
- `return_related_questions` \- Include related questions
- `search_mode` \- “web” (default) or “academic” mode selector.

See [API Reference](https://docs.perplexity.ai/api-reference) for parameter details and models.

## Examples with OpenAI’s client libraries

### Basic Usage

Start with these simple examples to make your first API calls:

```
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.perplexity.ai"
)

response = client.chat.completions.create(
    model="sonar-pro",
    messages=[\
        {"role": "user", "content": "What are the latest developments in AI?"}\
    ]
)

print(response.choices[0].message.content)
```

### Advanced Examples

For more control over search behavior and response generation:

```
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.perplexity.ai"
)

response = client.chat.completions.create(
    model="sonar-pro",
    messages=[\
        {"role": "user", "content": "Latest climate research findings"}\
    ],
    extra_body={
        "search_domain_filter": ["nature.com", "science.org"],
        "search_recency_filter": "month"
    }
)

print(response.choices[0].message.content)
print(f"Sources: {len(response.search_results)} articles found")
```

## Response structure

Perplexity API responses include both standard OpenAI fields and additional search metadata:

### Standard OpenAI Fields

- `choices[0].message.content` \- The AI-generated response
- `model` \- The model name used
- `usage` \- Token consumption details
- `id`, `created`, `object` \- Standard response metadata

### Perplexity-Specific Fields

- `search_results` \- Array of web sources with titles, URLs, and dates
- `usage.search_context_size` \- Search context setting used

```
# Access the main response
content = response.choices[0].message.content
print(content)

# Access search sources
for result in response.search_results:
    print(f"Source: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Date: {result['date']}")
    print("---")

# Check token usage
print(f"Tokens used: {response.usage.total_tokens}")
```

Search results are returned even when streaming is enabled, but they arrive in the final chunk of the stream. See the [Streaming Guide](https://docs.perplexity.ai/guides/streaming-responses) for details.

## Unsupported and notable differences

While compatibility is high, note the following differences from OpenAI:

- **Model names**: Use Perplexity models like `sonar-pro`, `sonar-reasoning`.
- **Search controls**: Perplexity adds web/academic search parameters via `extra_body` (Python) or root fields (TypeScript) as shown above.

If you previously used OpenAI-only fields that aren’t applicable to Perplexity search controls, remove or ignore them. Check the API Reference for the current list of supported fields.

## Technical notes

- **Error format**: Same as OpenAI’s API for compatibility
- **Rate limiting**: Apply standard rate limiting practices
- **Model names**: Use Perplexity model names (`sonar-pro`, `sonar-reasoning`, etc.)
- **Authentication**: Use `Bearer` token format in Authorization header

</details>

<details>
<summary>pricing-perplexity</summary>

This page shows **pricing information** to help you understand API costs. For **billing setup**, payment methods, and usage monitoring, visit the [Admin section](https://docs.perplexity.ai/getting-started/api-groups).

## Search API Pricing

| API | Price per 1K requests | Description |
| --- | --- | --- |
| **Search API** | $5.00 | Raw web search results with advanced filtering |

**No token costs:** Search API charges per request only, with no additional token-based pricing.

## Grounded LLM Pricing

**Total cost per query** = Token costs + Request fee (varies by search context size, applies to Sonar, Sonar Pro, Sonar Reasoning, and Sonar Reasoning Pro models only)

- Token Pricing

- Request Pricing

## Token Pricing

**Token pricing** is based on the number of tokens in your request and response.

| Model | Input Tokens ($/1M) | Output Tokens ($/1M) | Citation Tokens ($/1M) | Search Queries ($/1K) | Reasoning Tokens ($/1M) |
| --- | --- | --- | --- | --- | --- |
| **Sonar** | $1 | $1 | - | - | - |
| **Sonar Pro** | $3 | $15 | - | - | - |
| **Sonar Reasoning** | $1 | $5 | - | - | - |
| **Sonar Reasoning Pro** | $2 | $8 | - | - | - |
| **Sonar Deep Research** | $2 | $8 | $2 | $5 | $3 |

Token and Cost Glossary

### Input Tokens

The number of tokens in your prompt or message to the API. This includes:

- Your question or instruction
- Any context or examples you provide
- System messages and formatting

**Example:** “What is the weather in New York?” = ~8 input tokens

### Output Tokens

The number of tokens in the API’s response. This includes:

- The generated answer or content
- Any explanations or additional context
- Search results and references

**Example:** “The weather in New York is currently sunny with a temperature of 72°F.” = ~15 output tokens

### Citation Tokens

Tokens used specifically for generating search results and references in responses. Only applies to **Sonar Deep Research** model.**Example:** Including source links, reference numbers, and bibliographic information

### Search Context Size vs Context Window

**Search context size** is _not_ the same as the **context window**.

- **Search context size**: How much web information is retrieved during search (affects request pricing)
- **Context window**: Maximum tokens the model can process in one request (affects token limits)

### Search Queries

The number of individual searches conducted by **Sonar Deep Research** during query processing. This is separate from your initial user query.

- The model automatically determines how many searches are needed
- You cannot control the exact number of search queries
- The `reasoning_effort` parameter influences the number of searches performed
- Only applies to **Sonar Deep Research** model

### Reasoning Tokens

Tokens used for step-by-step logical reasoning and problem-solving. Only applies to **Sonar Deep Research** model.**Example:** Breaking down a complex math problem into sequential steps with explanations

**Token Calculation:** 1 token ≈ 4 characters in English text. The exact count may vary based on language and content complexity.

## Cost Examples

## Sonar Web Search Example

**Sonar** • 500 input + 200 output tokens

- Low

- Medium

- High

| Component | Cost |
| --- | --- |
| Input tokens | $0.0005 |
| Output tokens | $0.0002 |
| Request fee | $0.005 |
| **Total** | **$0.0057** |

## Deep Research Example

**Sonar Deep Research**

- Low

- Medium

- High

| Component | Cost |
| --- | --- |
| Input tokens (33) | $0.000066 |
| Output tokens (7163) | $0.057304 |
| Citation tokens (20016) | $0.040032 |
| Reasoning tokens (73997) | $0.221991 |
| Search queries (18) | $0.09 |
| **Total** | **$0.409393** |

## Choosing the Right API

### Search API

| API | Description | Best For |
| --- | --- | --- |
| **Search API** | Raw web search results with advanced filtering | Custom search engines, research tools, competitive intelligence, news aggregation |

### Sonar Models (Chat Completions)

| Model | Description | Best For |
| --- | --- | --- |
| **Sonar** | Lightweight, cost-effective search model | Quick facts, news updates, simple Q&A, high-volume applications |
| **Sonar Pro** | Advanced search with deeper content understanding | Complex queries, competitive analysis, detailed research |
| **Sonar Reasoning** | Quick problem-solving with step-by-step logic and search | Logic puzzles, math problems, transparent reasoning |
| **Sonar Reasoning Pro** | Enhanced multi-step reasoning with web search | Complex problem-solving, research analysis, strategic planning |
| **Sonar Deep Research** | Exhaustive research and detailed report generation with search | Academic research, market analysis, comprehensive reports |

**Need help choosing?** Use Search API when you want raw data to process yourself. Use Sonar models when you want AI-generated answers with search grounding.

</details>

<details>
<summary>prompts-model-context-protocol</summary>

**Protocol Revision**: 2025-06-18

The Model Context Protocol (MCP) provides a standardized way for servers to expose prompt
templates to clients. Prompts allow servers to provide structured messages and
instructions for interacting with language models. Clients can discover available
prompts, retrieve their contents, and provide arguments to customize them.

## User Interaction Model

Prompts are designed to be **user-controlled**, meaning they are exposed from servers to
clients with the intention of the user being able to explicitly select them for use.Typically, prompts would be triggered through user-initiated commands in the user
interface, which allows users to naturally discover and invoke available prompts.For example, as slash commands:
https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/specification/2025-06-18/server/slash-command.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=7f003e36d881dd6f3e5b8cbdd85e5ca5
However, implementors are free to expose prompts through any interface pattern that suits
their needs—the protocol itself does not mandate any specific user interaction
model.

## Capabilities

Servers that support prompts **MUST** declare the `prompts` capability during
[initialization](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle#initialization):

```
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the server will emit notifications when the list of
available prompts changes.

## Protocol Messages

### Listing Prompts

To retrieve available prompts, clients send a `prompts/list` request. This operation
supports [pagination](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination).
**Request:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "prompts/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}
```

**Response:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "prompts": [\
      {\
        "name": "code_review",\
        "title": "Request Code Review",\
        "description": "Asks the LLM to analyze code quality and suggest improvements",\
        "arguments": [\
          {\
            "name": "code",\
            "description": "The code to review",\
            "required": true\
          }\
        ]\
      }\
    ],
    "nextCursor": "next-page-cursor"
  }
}
```

### Getting a Prompt

To retrieve a specific prompt, clients send a `prompts/get` request. Arguments may be
auto-completed through [the completion API](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/completion).
**Request:**

```
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "prompts/get",
  "params": {
    "name": "code_review",
    "arguments": {
      "code": "def hello():\n    print('world')"
    }
  }
}
```

**Response:**

```
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "description": "Code review prompt",
    "messages": [\
      {\
        "role": "user",\
        "content": {\
          "type": "text",\
          "text": "Please review this Python code:\ndef hello():\n    print('world')"\
        }\
      }\
    ]
  }
}
```

### List Changed Notification

When the list of available prompts changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:

```
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

## Message Flow

ServerClientServerClientDiscoveryUsageChangesopt\[listChanged\]prompts/listList of promptsprompts/getPrompt contentprompts/list\_changedprompts/listUpdated prompts

## Data Types

### Prompt

A prompt definition includes:

- `name`: Unique identifier for the prompt
- `title`: Optional human-readable name of the prompt for display purposes.
- `description`: Optional human-readable description
- `arguments`: Optional list of arguments for customization

### PromptMessage

Messages in a prompt can contain:

- `role`: Either “user” or “assistant” to indicate the speaker
- `content`: One of the following content types:

All content types in prompt messages support optional
[annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) for
metadata about audience, priority, and modification times.

#### Text Content

Text content represents plain text messages:

```
{
  "type": "text",
  "text": "The text content of the message"
}
```

This is the most common content type used for natural language interactions.

#### Image Content

Image content allows including visual information in messages:

```
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/png"
}
```

The image data **MUST** be base64-encoded and include a valid MIME type. This enables
multi-modal interactions where visual context is important.

#### Audio Content

Audio content allows including audio information in messages:

```
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```

The audio data MUST be base64-encoded and include a valid MIME type. This enables
multi-modal interactions where audio context is important.

#### Embedded Resources

Embedded resources allow referencing server-side resources directly in messages:

```
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "mimeType": "text/plain",
    "text": "Resource content"
  }
}
```

Resources can contain either text or binary (blob) data and **MUST** include:

- A valid resource URI
- The appropriate MIME type
- Either text content or base64-encoded blob data

Embedded resources enable prompts to seamlessly incorporate server-managed content like
documentation, code samples, or other reference materials directly into the conversation
flow.

## Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

- Invalid prompt name: `-32602` (Invalid params)
- Missing required arguments: `-32602` (Invalid params)
- Internal errors: `-32603` (Internal error)

## Implementation Considerations

1. Servers **SHOULD** validate prompt arguments before processing
2. Clients **SHOULD** handle pagination for large prompt lists
3. Both parties **SHOULD** respect capability negotiation

## Security

Implementations **MUST** carefully validate all prompt inputs and outputs to prevent
injection attacks or unauthorized access to resources.

</details>

<details>
<summary>sonar-pro-perplexity</summary>

# Sonar Pro

Advanced search with enhanced search results

An advanced search model designed for complex queries, delivering deeper content understanding with enhanced search result accuracy and 2x more search results than standard Sonar.

## Pricing

[See the full pricing and search context size guide.](https://docs.perplexity.ai/getting-started/pricing)

### Input Tokens

$3

Per 1M Tokens

### Output Tokens

$15

Per 1M Tokens

### Price Per 1K Requests

$14$10$6

HighMediumLow

## Features

### Non-reasoning model

### Optimized for complex, multi-step Q&A tasks

### 200K context length

### Advanced information retrieval architecture

### 2x more search results than standard Sonar

### No training on customer data

## Real World Use Cases

### Complex research questions requiring depth

### Comparative analysis across multiple sources

### Information synthesis and detailed reporting

```
curl --request POST \
  --url https://api.perplexity.ai/chat/completions \
  --header "Authorization: Bearer <token>" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "sonar-pro",
    "messages": [\
      {\
        "role": "user",\
        "content": "Analyze the competitive positioning of Perplexity in the AI search market and evaluate how Comet compares to similar offerings from other companies."\
      }\
    ]
  }' | jq
```

**Sample Response Metadata**

```
{
"id": "12572668-b12a-4ce5-a697-57e22816a2ce",
"model": "sonar-pro",
"created": 1756486047,
"usage": {
  "prompt_tokens": 26,
  "completion_tokens": 832,
  "total_tokens": 858,
  "search_context_size": "low",
  "cost": {
    "input_tokens_cost": 0.0,
    "output_tokens_cost": 0.012,
    "request_cost": 0.006,
    "total_cost": 0.019
  }
},
"citations": [\
  "https://explodingtopics.com/blog/perplexity-ai-stats",\
  "https://opentools.ai/news/perplexity-ceo-challenges-googles-ai-strategy-in-the-browser-wars",\
  "https://taptwicedigital.com/stats/perplexity",\
  "https://www.leanware.co/insights/comet-perplexity-everything-you-need-to-know",\
  "https://www.index.dev/blog/perplexity-statistics"\
],
"search_results": [\
  {\
    "title": "The Latest Perplexity AI Stats (2025)",\
    "url": "https://explodingtopics.com/blog/perplexity-ai-stats",\
    "date": "2025-06-23",\
    "last_updated": "2025-08-29",\
    "snippet": "As of 2025, the AI space is valued at approximately $600 billion, with projections to increase by 500% over the next 5 years."\
  },\
  {\
    "title": "Perplexity CEO Challenges Google's AI Strategy in the ...",\
    "url": "https://opentools.ai/news/perplexity-ceo-challenges-googles-ai-strategy-in-the-browser-wars",\
    "date": "2025-07-17",\
    "last_updated": "2025-07-17",\
    "snippet": "For example, Perplexity's AI-driven browser, Comet, represents a direct challenge to Google's traditional search engine model by prioritizing ..."\
  },\
  {\
    "title": "7 Perplexity AI Statistics (2025): Revenue, Valuation, ...",\
    "url": "https://taptwicedigital.com/stats/perplexity",\
    "date": "2025-04-19",\
    "last_updated": "2025-08-29",\
    "snippet": "Perplexity AI holds a 6.2% market share in the AI search market. Perplexity AI is valued at $18 billion as of March 2025. Perplexity AI has ..."\
  },\
  {\
    "title": "Comet Perplexity: Everything You Need to Know - Leanware",\
    "url": "https://www.leanware.co/insights/comet-perplexity-everything-you-need-to-know",\
    "date": "2025-07-25",\
    "last_updated": "2025-08-28",\
    "snippet": "Learn what Perplexity Comet is, how it works, and why it's changing the AI landscape, from real-world uses and tech insights to pricing, ..."\
  },\
  {\
    "title": "50+ Perplexity AI Stats to Know in 2025",\
    "url": "https://www.index.dev/blog/perplexity-statistics",\
    "date": "2025-08-01",\
    "last_updated": null,\
    "snippet": "As of May 2025, Perplexity AI processes over 780 million monthly search queries, up from just 230 million in mid-2024. That's more than 30 ..."\
  }\
],
"object": "chat.completion",
"choices": [\
  {\
    "index": 0,\
    "finish_reason": "stop",\
    "message": {\
      "role": "assistant",\
      "content": "Perplexity occupies a rapidly expanding and influential position in the AI search market, characterized by robust user growth, significant market share, and disruptive innovation through products like the Comet browser[1][3][5]. Comet, Perplexity's AI-driven browser, stands out by favoring a user-centric, agentic browsing experience, in marked contrast to traditional browsers and search tools built around advertising ecosystems[2][4].\n\n**Competitive Positioning of Perplexity:**\n- **Market Share & Growth**: Perplexity has achieved a 6.2% market share in AI search, with an $18 billion valuation as of March 2025[3]. The platform saw visits surge from 52.4 million in March 2024 to 159.7 million in March 2025—a nearly 192% increase in monthly visitors—and now processes over 780 million monthly queries[1][5].\n- **User Base**: With approximately 15 million active monthly users, Perplexity is among the most adopted AI search platforms[1].\n- **Strategic Focus**: Its strategy centers on synthesizing information from multiple sources, rather than relying on a single proprietary index or algorithm[3].\n- **Ecosystem Independence**: By launching its own browser, Perplexity extends beyond plug-ins and integrations, directly challenging the dominance of Google (Chrome/Search), Microsoft (Edge/Bing), and Apple (Safari)[4].\n\n**Comet's Distinct Approach Compared to Competitors:**\n\n| Feature                        | Comet (Perplexity)                       | Google Chrome/Search     | Microsoft Edge/Bing     | Others (e.g., Safari, Firefox)   |\n|-------------------------------|------------------------------------------|--------------------------|------------------------|----------------------------------|\n| **Business Model**            | Subscription-based, low ad reliance      | Ad-driven               | Mixed (ads + services) | Mainly traditional browsing      |\n| **AI Integration**            | Deeply agentic, task automation          | Incipient (AI summaries)| Embedded search AI     | Limited or add-on only           |\n| **User Experience Focus**     | Automation, personalization              | Traffic/ads optimization| Integration w/ Windows | Privacy, open-source emphasis    |\n| **Ecosystem Independence**    | Fully standalone browser; own assistant  | Chrome Store dependence | Tied to Windows        | Add-ons, less AI-focused         |\n\n**Key Innovations of Comet vs. Competitors:**\n- **Agentic Browsing**: Comet enables autonomous execution of user intent—tasks beyond search, suchs as form completion or navigation—leveraging AI agents to streamline workflows[2][4].\n- **Contextual Awareness**: Maintains session and browsing context for more relevant, personalized assistance[4].\n- **Cross-Tab Functionality**: Performs tasks across all tabs and logged-in sites, surpassing limitations of plug-ins or browser extensions[4].\n- **User-Centric Model**: Moves away from ad-driven monetization, focusing on delivering value through direct service and subscription[2].\n\n**Competitive Landscape and Impact:**\n- **Direct Challenge to Market Leaders**: Comet attacks the core of Google's and Microsoft's value proposition, offering a radically different vision centered on user benefit rather than maximizing ad engagement[2][4].\n- **Potential Market Shift**: The shift toward premium, AI-enhanced browsing reflects growing consumer willingness to pay for advanced features, potentially leading to reduced reliance on advertising industry-wide[2].\n- **Risk and Opportunities**: While incumbents possess vast resources, Perplexity's rapid innovation and its Comet ecosystem present a legitimate threat to traditional models—if it maintains reliability and continues scaling its offerings[3][4].\n\n**Summary**\nPerplexity's Comet browser redefines competition in the AI search and browsing space by prioritizing intelligence, agentic workflows, and user-centric design over the prevailing ad-driven model. Its suite of features and rapidly growing user base set it apart from legacy offerings from Google, Microsoft, Apple, and Mozilla, positioning Perplexity as a leader in the evolving landscape of AI-powered digital information services[1][2][3][4][5]."\
    },\
    "delta": {\
      "role": "assistant",\
      "content": ""\
    }\
  }\
]
}
```

Cost Breakdown for Sample Request

**Token Usage**

- Prompt Tokens: 26
- Completion Tokens: 832
- Search Context Size: Low

1

Calculate Input Tokens Cost

26 tokens ÷ 1,000,000 × 3=3 = 3=0.000078

2

Calculate Output Tokens Cost

832 tokens ÷ 1,000,000 × 15=15 = 15=0.01248

3

Calculate Search Context Cost

1 request × 6÷1,000=6 ÷ 1,000 = 6÷1,000=0.006

4

Calculate Total Cost

0.000078+0.000078 + 0.000078+0.01248 + 0.006=0.006 = 0.006=0.018558

**Total cost for this request: $0.018558**

</details>

<details>
<summary>structured-outputs-guide-perplexity</summary>

## Overview

Structured outputs enable you to enforce specific response formats from Perplexity’s models, ensuring consistent, machine-readable data that can be directly integrated into your applications without manual parsing.

We currently support two types of structured outputs: **JSON Schema** and **Regex**. LLM responses will work to match the specified format, except for the following cases:

- The output exceeds `max_tokens`

Enabling the structured outputs can be done by adding a `response_format` field in the request:

**JSON Schema**

- `response_format: { type: "json_schema", json_schema: {"schema": object} }` .
- The schema should be a valid JSON schema object.

**Regex** (only available for `sonar` right now)

- `response_format: { type: "regex", regex: {"regex": str} }` .
- The regex is a regular expression string.

**Improve Schema Compliance**: Give the LLM some hints about the output format in your prompts to improve adherence to the structured format.For example, include phrases like “Please return the data as a JSON object with the following structure…” or “Extract the information and format it as specified in the schema.”

The first request with a new JSON Schema or Regex expects to incur delay on the first token. Typically, it takes 10 to 30 seconds to prepare the new schema, and may result in timeout errors. Once the schema has been prepared, the subsequent requests will not see such delay.

## Examples

### 1. Financial Analysis with JSON Schema

```
from perplexity import Perplexity
from typing import List, Optional
from pydantic import BaseModel

class FinancialMetrics(BaseModel):
    company: str
    quarter: str
    revenue: float
    net_income: float
    eps: float
    revenue_growth_yoy: Optional[float] = None
    key_highlights: Optional[List[str]] = None

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[\
        {\
            "role": "user",\
            "content": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics."\
        }\
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "schema": FinancialMetrics.model_json_schema()
        }
    }
)

metrics = FinancialMetrics.model_validate_json(completion.choices[0].message.content)
print(f"Revenue: ${metrics.revenue}B")
```

### 2. Extract Contact Information with Regex

```
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar",
    messages=[\
        {\
            "role": "user",\
            "content": "Find the direct email address for the investor relations contact at Tesla Inc."\
        }\
    ],
    response_format={
        "type": "regex",
        "regex": {
            "regex": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        }
    }
)

email = completion.choices[0].message.content
print(f"Investor Relations Email: {email}")
```

## Best Practices

### Generating responses in a JSON Format

For Python users, we recommend using the Pydantic library to [generate JSON schema](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema).

**Unsupported JSON Schemas**
Recursive JSON schema is not supported. As a result of that, unconstrained objects are not supported either. Here’s a few example of unsupported schemas:

```
# UNSUPPORTED!

from typing import Any

class UnconstrainedDict(BaseModel):
   unconstrained: dict[str, Any]

class RecursiveJson(BaseModel):
   value: str
   child: list["RecursiveJson"]
```

**Links in JSON Responses**: Requesting links as part of a JSON response may not always work reliably and can result in hallucinations or broken links. Models may generate invalid URLs when forced to include links directly in structured outputs.To ensure all links are valid, use the links returned in the `citations` or `search_results` fields from the API response. Never count on the model to return valid links directly as part of the JSON response content.

### Generating responses using a regex

**Supported Regex**

- Characters: `\d`, `\w`, `\s` , `.`
- Character classes: `[0-9A-Fa-f]` , `[^x]`
- Quantifiers: `*`, `?` , `+`, `{3}`, `{2,4}` , `{3,}`
- Alternation: `|`
- Group: `( ... )`
- Non-capturing group: `(?: ... )`

**Unsupported Regex**

- Contents of group: `\1`
- Anchors: `^`, `$`, `\b`
- Positive lookahead: `(?= ... )`
- Negative lookahead: `(?! ... )`
- Positive look-behind: `(?<= ... )`
- Negative look-behind: `(?<! ... )`
- Recursion: `(?R)`

## Perplexity’s JSON Schema Implementation

Perplexity’s structured outputs implementation has several key differences compared to other providers:

### Simplified Schema Definition

- **Optional naming**: Unlike other providers that require explicit schema names, Perplexity automatically handles schema naming with sensible defaults
- **Flexible strictness**: Schema validation is handled automatically without requiring manual strictness configuration
- **Streamlined syntax**: You only need to provide the core schema object without additional wrapper fields

**Other Providers:**

```
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "financial_data",
      "strict": true,
      "schema": { /* your schema */ }
    }
  }
}
```

**Perplexity:**

```
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "schema": { /* your schema */ }
    }
  }
}
```

### Enhanced Error Handling

- **Clear error messages**: When schemas fail validation, you’ll receive specific, actionable error messages
- **Recursion protection**: Built-in safeguards prevent infinite recursion in complex nested schemas
- **Constraint validation**: Automatic detection and clear messaging for unsupported features like unconstrained objects

### Schema Compatibility

While Perplexity supports standard JSON Schema syntax, some advanced features may not be available:

- Recursive schemas are not supported for performance and reliability reasons
- Unconstrained objects (like `dict[str, Any]`) are automatically detected and rejected
- Complex reference patterns may require simplification

This approach prioritizes reliability and performance while maintaining compatibility with most common JSON Schema use cases.

## Structured Outputs for Reasoning Models

When using structured outputs with reasoning models like `sonar-reasoning-pro`, the response will include a `<think>` section containing reasoning tokens, immediately followed by the structured output. The `response_format` parameter does not remove these reasoning tokens from the output, so the final response will need to be parsed manually.

**Sample Response:**

```
<think>
I need to provide information about France in a structured JSON format with specific fields: country, capital, population, official_language.

For France:
- Country: France
- Capital: Paris
- Population: About 67 million (as of 2023)
- Official Language: French

Let me format this information as required.
</think>
{"country":"France","capital":"Paris","population":67750000,"official_language":"French"}
```

For a reusable implementation to extract JSON from reasoning model outputs, see our [example utility on GitHub](https://github.com/ppl-ai/api-discussion/blob/main/utils/extract_json_reasoning_models.py).

</details>

<details>
<summary>what-is-model-context-protocol-mcp-a-guide-google-cloud</summary>

The provided markdown content describes the Model Context Protocol (MCP) in general, its architecture, how it works, its benefits, security considerations, and deployment on Google Cloud. This content is *not* pertinent to the specific article guidelines for Lesson 18, which focuses on building a research loop with query generation, Perplexity integration, and human-in-the-loop feedback using MCP. Lesson 18 assumes prior knowledge of MCP (referencing Lesson 16) and focuses on practical implementation steps within an MCP-based research agent.

Therefore, as per the instructions to "Focus on keeping only the core textual content (and code content if there are code sections) that is pertinent to the article guidelines provided" and "only removing all irrelevant sections", the entire provided markdown content is irrelevant to the specific scope of Lesson 18.

Here is the cleaned markdown:

</details>
