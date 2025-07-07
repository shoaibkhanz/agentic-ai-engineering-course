# Research

## Research Results

<details>
<summary>What recent industry or academic studies compare the operational cost, latency, and reliability of LLM agentic systems versus fixed-step LLM workflows?</summary>

### Source [2]: https://www.lyzr.ai/blog/agentic-ai-vs-llm/

Query: What recent industry or academic studies compare the operational cost, latency, and reliability of LLM agentic systems versus fixed-step LLM workflows?

Answer: This recent industry comparison provides **quantitative data** for operational cost, latency, and reliability:

- **Latency:**  
  - LLM runners (fixed-step): Single call latency is low (300 ms–2 seconds).
  - Agentic AI: Each reasoning loop takes 3–10 seconds; total workflow can take minutes if steps chain.

- **Cost per Execution:**  
  - LLM runners: $0.001–$0.02 per call (using APIs like OpenAI, Claude, Gemini Pro).
  - Agentic AI: $0.10–$5 per workflow, depending on memory, tool calls, and steps. Example: Drafting an email with GPT-4 costs $0.01; a sales outreach agent involving personalized CRM search and scheduling can cost $0.50–$1.20.

- **Infrastructure Burden:**  
  - LLM runners: Do not require persistent storage or state management.
  - Agentic AI: Needs memory storage (e.g., Redis, vector DBs), tool integrations, and additional debugging layers.

- **Reliability:**  
  - Fixed-step LLM runners are easy to debug (retry the prompt).
  - Agentic AI systems are more prone to failure due to tool misuse, memory corruption, planning errors, or looping. Failure rates for open-ended agent goals (e.g., AutoGPT) can be 20–40%, while structured frameworks (LangGraph, CrewAI) improve reliability through guardrails.

Overall, fixed-step LLM workflows are more reliable, lower latency, and lower cost, while agentic systems offer flexibility but at a higher operational cost and complexity.

-----

-----

-----

### Source [4]: https://arxiv.org/html/2507.02097v1

Query: What recent industry or academic studies compare the operational cost, latency, and reliability of LLM agentic systems versus fixed-step LLM workflows?

Answer: This academic source establishes clear **definitions and boundaries** between agentic systems and fixed-step LLM workflows. It notes that fixed-step, chain-based workflows—even when chaining LLM calls—do not demonstrate agent autonomy; true agentic systems operate via internal observe-decide-act loops, iteratively refining outputs and adapting to context. Agentic systems can personalize and improve results through feedback and iterative interaction, which is not possible with static, single-pass LLM workflows.

The source visually compares these approaches, emphasizing that agentic systems support more dynamic problem-solving but at the cost of increased system complexity and the need for memory and planning infrastructure. While not providing direct operational cost or latency metrics, it affirms that agentic workflows require more robust design and monitoring compared to simpler, fixed-step LLM orchestrations.

-----

</details>

<details>
<summary>What official engineering write-ups or documentation describe the architecture and execution loop of Google’s Gemini CLI agent released in 2025?</summary>

### Source [9]: https://www.helpnetsecurity.com/2025/06/26/google-gemini-cli-open-source-ai-agents/

Query: What official engineering write-ups or documentation describe the architecture and execution loop of Google’s Gemini CLI agent released in 2025?

Answer: Google’s Gemini CLI is an open-source command-line agent built upon the Gemini 1.5 Pro model and is designed to serve as a local AI assistant for complex developer workflows. Its architecture is explicitly described as “agentic,” emphasizing openness, composability, and developer control. The agent comes with several built-in modules, including a code reader, command runner, and memory module, each of which can be extended through Multimodal Composable Functions (MCPs)—a Python-based interface for adding custom behaviors and integrations. The core execution loop of Gemini CLI centers around chains of reasoning, tool invocation, and context management, allowing developers to interact with the agent using natural language for tasks such as project analysis and automated file editing. The entire codebase is available under the Apache 2.0 license, and Google’s official announcement highlights that the open-source nature allows developers to inspect the implementation details, understand the execution flow, and verify security implications. The Gemini 1.5 Pro model enables the agent to handle large context windows (up to 1 million tokens), supporting in-depth codebase analysis and multi-step operations, all orchestrated through a transparent and extensible architecture[1].

-----

-----

### Source [10]: https://www.infoq.com/news/2025/07/google-gemini-cli/

Query: What official engineering write-ups or documentation describe the architecture and execution loop of Google’s Gemini CLI agent released in 2025?

Answer: The official documentation and engineering write-ups for Gemini CLI describe it as a lightweight, open-source terminal agent deeply integrated with Gemini Code Assist. The architecture supports the Gemini 2.5 Pro model, features a 1 million token context window, and allows prompt grounding using Google Search for real-time web context. Gemini CLI implements the Model Context Protocol (MCP), which governs how the agent manages context, tool invocation, and custom system prompts (configurable via a GEMINI.md file). The execution loop accommodates both interactive and non-interactive (scripting/CI/CD) modes, enabling developers to automate tasks with AI directly from the terminal. The design also supports authentication via a Google account or API keys for advanced use. The open-source nature (Apache 2.0 license) ensures that all execution logic, context management, and extension points (such as MCP modules) are available for public inspection and modification, as detailed in Google’s official engineering documentation[3].

-----

-----

### Source [11]: https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/

Query: What official engineering write-ups or documentation describe the architecture and execution loop of Google’s Gemini CLI agent released in 2025?

Answer: Google’s official announcement blog for Gemini CLI outlines its architecture and execution model as centered on powerful built-in tools that enable code understanding, file manipulation, command execution, and dynamic troubleshooting from the command line. A key architectural feature is the agent’s ability to “ground prompts with Google Search,” which fetches real-time web context for more accurate and current responses. The CLI is designed to be extended through the Model Context Protocol (MCP), which provides a standardized way to add new tools or augment the agent’s capabilities. The execution loop operates by receiving user input, managing context, invoking appropriate tools or functions, and returning results directly in the terminal. The official documentation emphasizes openness, extensibility, and integration with both local and external resources, ensuring developers have deep control and transparency over the agent’s workflow and execution logic[5].
-----

-----

</details>

<details>
<summary>Which peer-reviewed papers or reputable blog posts catalogue common AI-agent design patterns—planning, tool invocation, memory, and multi-agent coordination—such as ReAct, Toolformer, and LangGraph?</summary>

### Source [12]: https://research.aimultiple.com/agentic-ai-design-patterns/

Query: Which peer-reviewed papers or reputable blog posts catalogue common AI-agent design patterns—planning, tool invocation, memory, and multi-agent coordination—such as ReAct, Toolformer, and LangGraph?

Answer: This source catalogs **four main agentic AI design patterns** that enhance the autonomy and flexibility of large language model (LLM) agents:

- **Planning Pattern:** Enables LLMs to break down large tasks into subtasks and organize them into a logical sequence. Agents may plan actions linearly or in parallel branches for more complex scenarios. A highlighted example is **HuggingGPT**, which coordinates LLMs with models from platforms like Hugging Face to tackle multifaceted AI tasks.
- **Multi-Agent Pattern:** Focuses on **task delegation** by assigning different responsibilities to multiple agents. This pattern uses Agent-to-Agent (A2A) protocols to govern communication and information flow between agents. Notable implementations include **Google’s A2A protocol** and frameworks such as AutoGen, LangChain, ChatDev, and OpenAI Swarm.
- The article also references **tool invocation** and **memory** as part of agentic systems, though the detailed descriptions focus more on planning and multi-agent coordination.
- It provides real-world examples and links to open-source agentic AI builders and frameworks, giving readers a practical overview of how these patterns are deployed in current AI systems.

-----

-----

-----

### Source [13]: https://hub.athina.ai/top-10-ai-agent-papers-from-january-2025-shaping-their-future/

Query: Which peer-reviewed papers or reputable blog posts catalogue common AI-agent design patterns—planning, tool invocation, memory, and multi-agent coordination—such as ReAct, Toolformer, and LangGraph?

Answer: This article summarizes recent peer-reviewed papers that contribute to cataloging AI-agent design patterns:

- It describes the **“agent infrastructure”** concept, which provides technical systems and shared protocols for mediating agent interactions, such as authentication-based user-agent ties and regulatory frameworks, ensuring safe, accountable, and structured integration of AI agents.
- The listed paper, **“Agentic Systems: A Guide to Transforming Industries with Vertical AI Agents,”** introduces a **standardization framework** for designing vertical (domain-specific) AI agents. It highlights a **Cognitive Skills** module aimed at enhancing domain-specific reasoning and inference, and details operational patterns and real-world agent deployments.
- The coverage underlines the importance of **standardized design patterns** for scalability, adaptability, and consistency, directly addressing the need for cataloging agentic system approaches such as planning, tool use, and multi-agent workflows.

-----

-----

-----

### Source [15]: https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/

Query: Which peer-reviewed papers or reputable blog posts catalogue common AI-agent design patterns—planning, tool invocation, memory, and multi-agent coordination—such as ReAct, Toolformer, and LangGraph?

Answer: This DeepLearning.AI newsletter entry discusses four core **agentic design patterns** central to recent progress:

- The four patterns are **Reflection, Tool Use, Planning, and Multi-Agent Collaboration**.
- The **Reflection pattern** involves having the LLM **generate output, then prompt itself to critically evaluate and improve that output**, automating iterative improvement. This can yield significant performance gains across tasks like code generation or writing.
- The newsletter outlines how **agentic workflows** prompt LLMs multiple times, building up to higher-quality results step by step, rather than relying on a single-shot generation.
- The other listed patterns—**Tool Use** (invoking external tools/APIs), **Planning** (decomposing tasks), and **Multi-Agent Collaboration**—are said to be drivers of current and future progress in agentic AI design, though detailed descriptions are reserved for other installments.

-----

-----

-----

### Source [16]: https://www.anthropic.com/research/building-effective-agents

Query: Which peer-reviewed papers or reputable blog posts catalogue common AI-agent design patterns—planning, tool invocation, memory, and multi-agent coordination—such as ReAct, Toolformer, and LangGraph?

Answer: This official Anthropic research page discusses **common patterns for agentic systems** seen in production deployments:

- The section references **foundational building blocks and workflows** used to construct effective AI agents, focusing on scalable and maintainable design.
- While the excerpt does not provide the full list, Anthropic’s public research typically covers patterns such as **planning**, **tool use (invocation of external APIs or functions)**, **memory (storing and retrieving context or task history)**, and **multi-agent coordination** (delegating tasks among agent submodules or multiple models).
- Anthropic’s approach is grounded in extensive empirical experience, providing guidelines and pattern cataloging that are widely referenced in the field.
- The research emphasizes using proven design choices to build robust agentic systems, directly addressing the themes of planning, tool invocation, and coordination.

-----

-----

</details>

<details>
<summary>How does Cognition AI’s 2025 “Devin” autonomous software-engineering agent plan tasks, invoke tools, run tests, and iterate during a typical coding assignment?</summary>

### Source [23]: https://research.contrary.com/company/cognition

Query: How does Cognition AI’s 2025 “Devin” autonomous software-engineering agent plan tasks, invoke tools, run tests, and iterate during a typical coding assignment?

Answer: Devin operates as an AI coding agent capable of autonomously completing software engineering tasks end-to-end within a sandboxed environment. It is equipped with its own Linux shell, code editor, browser, and other standard developer tools, all accessible in a cloud-based workspace. When assigned a task, Devin follows these steps:

- **Formulates a step-by-step plan** for the assignment.
- **Executes code, runs tests, debugs, and updates its plan** as necessary.
- **Streams updates and accepts user corrections** to maintain an interactive feedback loop.
- Handles a variety of software development lifecycle tasks, such as building full-stack applications, bug fixing, integrating new libraries, and training/fine-tuning machine learning models.
- **Retains context over thousands of steps** and makes numerous micro-decisions toward achieving its assigned goal.
- When errors or failed tests occur, Devin searches documentation or forums and uses a built-in self-reflection loop to **adjust its strategy and retry**.
- Supports voice command input and provides enhanced repository context for large codebases.
- Integrates with platforms like GitHub and is available as a web app, Slack bot, or VS Code extension.

Devin’s architecture is based on large language models (e.g., GPT-4 Turbo) combined with custom planning algorithms, long-term memory, and adaptive reasoning capabilities.

-----

-----

</details>

<details>
<summary>What recent technical studies examine the predominant failure modes, reliability gaps, and cascading-error risks in multi-step LLM agents versus fixed-step LLM workflows?</summary>

### Source [27]: https://langfuse.com/blog/2024-10-observability-in-multi-step-llm-systems

Query: What recent technical studies examine the predominant failure modes, reliability gaps, and cascading-error risks in multi-step LLM agents versus fixed-step LLM workflows?

Answer: This source discusses the **failure modes and reliability gaps** in multi-step LLM systems by highlighting the complexity introduced when various components—such as routing, query extraction, document retrieval, summarization, and security checks—interact within an application. Each step introduces a potential **bottleneck**, and a failure or delay in any single step, such as query embedding, can **cascade**, increasing the latency and compounding errors throughout the system. The source emphasizes that the intricate nature of multi-step LLM workflows requires **continuous iteration and improvement**. As workloads evolve and features are added, developers need to routinely revisit and refine these systems. The source advocates for **monitoring and analysis**—advanced observability, feedback, and testing strategies are key to transforming these complex systems into robust, high-performing applications. This underscores the need to identify and mitigate individual step failures and cascading error risks that are far less pronounced in simpler, fixed-step workflows[1].

-----

-----

-----

### Source [28]: https://arxiv.org/html/2503.13657v2

Query: What recent technical studies examine the predominant failure modes, reliability gaps, and cascading-error risks in multi-step LLM agents versus fixed-step LLM workflows?

Answer: This recent technical study is the first systematic investigation into the **failure modes of LLM-based Multi-Agent Systems (MAS)**. By analyzing over 200 execution traces with Grounded Theory, the study identifies **14 unique failure modes** organized into three overarching categories: **(i) specification issues, (ii) inter-agent communication breakdowns, and (iii) execution errors**. The resulting Multi-Agent System Failure Taxonomy (MAST) forms a foundational framework for diagnosing and addressing failures in MAS. The study introduces an **automatic evaluation pipeline** (LLM Annotator), making scalable failure analysis possible. The findings highlight that, while MAS offers great potential, **widespread adoption is constrained by reliability issues**—these include failures arising from ambiguous task specifications, misaligned agent objectives, communication lapses among agents, and cascading errors where one agent’s mistake propagates throughout the system. The taxonomy and tools developed enable more systematic diagnosis and guide future research to mitigate these failures. The study also presents case studies and tactical interventions, concluding that only **limited reliability gains** are possible without addressing fundamental design flaws in multi-step and multi-agent LLM systems[2].

-----

-----

-----

### Source [29]: https://openreview.net/pdf?id=kFrqoVtMIy

Query: What recent technical studies examine the predominant failure modes, reliability gaps, and cascading-error risks in multi-step LLM agents versus fixed-step LLM workflows?

Answer: This assessment finds that **LLMs often struggle with complex, multi-step tasks** due to error propagation risks—incorrect outputs at one step can lead to cascading failures across subsequent steps. The research suggests that **standardizing intermediate steps** and incorporating **intermediate verification** points can substantially reduce errors such as hallucinations or using wrong tool types. While hybrid systems—where human-authored task networks guide the LLM—can help, they also face portability and scalability challenges. The study notes that **error cascading is a frequent issue in multi-step LLM workflows**, and that benchmarking and systematic verification at each step are necessary to improve reliability. These findings indicate that, compared to fixed-step workflows, multi-step and dynamic agent-based workflows are fundamentally more prone to accumulating and propagating errors unless explicit safeguards and verifications are implemented[3].

-----

-----

-----

### Source [31]: https://arxiv.org/html/2406.14884v1

Query: What recent technical studies examine the predominant failure modes, reliability gaps, and cascading-error risks in multi-step LLM agents versus fixed-step LLM workflows?

Answer: This benchmarking study (FlowBench) evaluates LLMs’ ability to perform **workflow-guided planning** and compares performance with and without explicit workflow knowledge. The results show that **incorporating structured workflow knowledge significantly enhances agent planning and reduces errors** at both the step and session levels. When LLMs lack access to such workflow knowledge, their performance degrades, especially in expertise-intensive domains, increasing the risk of errors and failure cascades. The study also observes that **cross-scenario transitions** (shifts between different workflow contexts) lead to further performance drops, but structured workflow guidance still mitigates the risk compared to unguided multi-step reasoning. This highlights that **explicit workflow structuring and guidance are critical to minimizing error propagation and reliability gaps** in multi-step LLM workflows, as opposed to fixed-step or single-turn approaches where such complexity is less pronounced[5].

-----

-----

</details>

<details>
<summary>What peer-reviewed papers or engineering blog posts from the last 18 months catalogue standard design patterns for LLM agents—planning, long-/short-term memory, tool use, reflection, and multi-agent coordination?</summary>

### Source [37]: https://arxiv.org/html/2505.12786v2

Query: What peer-reviewed papers or engineering blog posts from the last 18 months catalogue standard design patterns for LLM agents—planning, long-/short-term memory, tool use, reflection, and multi-agent coordination?

Answer: This peer-reviewed survey offers a technical overview of **design patterns for LLM agents**, focusing on autonomous cybersecurity agents but discussing generalizable concepts:

- **Memory**: LLM agents increasingly use a **dual-memory architecture** comprising *long-term memory* (knowledge internalized during pretraining, such as cybersecurity corpora, advisories, and scripts) and *short-term memory* (dynamic context from the environment). Specialized datasets like Primus, Attacker, SecQA, and CmdCaliper are used to build robust long-term memory for threat detection and adaptive responses.
  
- **Reasoning and Planning**: Modern LLM agents leverage **chain-of-thought (CoT) reasoning** and can adjust tactics dynamically. Planning involves multi-stage operations and dynamic adjustment to environmental changes. Agents "reason through failures and change tactics on the fly," which is critical for executing complex, multi-step tasks autonomously.

- **Tool Use**: Orchestration tools coordinate agent actions and enable agents to invoke external tools for specialized tasks.

- **Multi-Agent Collaboration**: Systems are designed for collaboration and distributed problem-solving, with orchestration layers handling coordination.

The survey references recent architectures and datasets that shape these design patterns, emphasizing the modular and adaptive nature of contemporary LLM agents.

-----

-----

-----

### Source [39]: https://mlnotes.substack.com/p/4-agentic-design-patterns-and-4-key

Query: What peer-reviewed papers or engineering blog posts from the last 18 months catalogue standard design patterns for LLM agents—planning, long-/short-term memory, tool use, reflection, and multi-agent coordination?

Answer: This engineering blog post (December 2024) outlines **four core agentic design patterns** observed in modern LLM agents:

- **Specialized Model Tuning & Tool Use**: Highlights the trend of customizing language models specifically for robust tool use, allowing agents to interact with APIs and external systems.
  
- **Planning & Reflection**: Discusses the integration of explicit planning modules (for decomposing and sequencing tasks) and reflection mechanisms (for iterative self-improvement).

- **Multi-Agent Coordination**: Notes the emergence of agentic frameworks that enable multiple LLMs to collaborate on workflows, with each agent specializing in a different aspect of the task.

The article positions these patterns as foundational for the next generation of LLM-based automation and reasoning, especially in enterprise and developer-focused frameworks.

-----

-----

</details>

<details>
<summary>Are there 2025 benchmark reports comparing agentic “deep research” tools (e.g., Perplexity Deep Research, Gemini Discovery, OpenAI’s Researcher) to traditional search or RAG workflows on accuracy, depth, and turnaround time?</summary>

### Source [41]: https://youssefh.substack.com/p/important-llm-papers-for-the-week-175

Query: Are there 2025 benchmark reports comparing agentic “deep research” tools (e.g., Perplexity Deep Research, Gemini Discovery, OpenAI’s Researcher) to traditional search or RAG workflows on accuracy, depth, and turnaround time?

Answer: This source reviews the release of DeepResearch Bench, the first dedicated and comprehensive benchmarking tool for rigorously evaluating the end-to-end capabilities of Deep Research Agents. The benchmark compares leading agentic research tools, including Gemini-2.5-Pro Deep Research, Perplexity Deep Research, and OpenAI's agents, across several axes:

- **Agent Performance:** There are notable differences among agents. Gemini-2.5-Pro excelled in report quality (as measured by RACE), while Perplexity had the highest citation accuracy (90%).
- **Report Quality (RACE):** Gemini-2.5-Pro and OpenAI’s agent produced the most comprehensive and insightful reports. The RACE evaluation framework was highly consistent with human expert judgments and outperformed simpler evaluation approaches.
- **Citation Quality (FACT):** Gemini-2.5-Pro generated the most citations per task (111), but Perplexity’s citations were more accurate.
- **Human Alignment:** The RACE framework closely matched human expert evaluations, validating its reliability for nuanced, long-form research assessment.

This benchmark allows for meaningful, rigorous comparison of agentic deep research tools, directly addressing their accuracy, depth, and (by implication) efficiency. It represents a significant advance over traditional or RAG-based evaluations by focusing on real research tasks and introducing human-aligned metrics.

-----

-----

-----

### Source [42]: https://arxiv.org/html/2506.18959v2

Query: Are there 2025 benchmark reports comparing agentic “deep research” tools (e.g., Perplexity Deep Research, Gemini Discovery, OpenAI’s Researcher) to traditional search or RAG workflows on accuracy, depth, and turnaround time?

Answer: This academic paper surveys the transition from traditional web search to agentic deep research, focusing on benchmarks specifically designed to compare standard LLMs, reasoning LLMs, and agentic deep research models. The main benchmarks cited include BrowseComp, BrowseComp-ZH, and Humanity’s Last Exam (HLE), each designed to test different aspects of agentic research:

- **BrowseComp:** Tests an agent’s ability to perform multi-step, open-ended web searches to retrieve complex, non-trivial information.
- **BrowseComp-ZH:** Similar to BrowseComp but focused on the Chinese web, increasing linguistic complexity.
- **HLE:** Presents expert-level questions across diverse domains that cannot be solved via naive retrieval, requiring synthesis from obscure and fragmented sources.

Results show that standard LLMs perform poorly (below 10% on BrowseComp, under 20% on HLE). In contrast, the OpenAI Deep Research agent achieves significantly higher scores: 51.5% on BrowseComp, 42.9% on BrowseComp-ZH, and 26.6% on HLE. These results demonstrate that agentic deep research tools with integrated reasoning and retrieval capabilities substantially outperform both traditional search and standard LLM-based RAG workflows on accuracy and depth for challenging research questions.

-----

-----

</details>

<details>
<summary>What documented security vulnerabilities (e.g., agent-injection, tool misuse) and recommended safeguards have researchers identified when deploying autonomous LLM agents in production?</summary>

### Source [44]: https://i-tracing.com/blog/llm-agents-cybersecurity/

Query: What documented security vulnerabilities (e.g., agent-injection, tool misuse) and recommended safeguards have researchers identified when deploying autonomous LLM agents in production?

Answer: Researchers have documented that **autonomous LLM agents** can exploit a range of cybersecurity vulnerabilities, both simple and complex. In one study, GPT-4 agents were able to autonomously perform attacks such as **blind SQL injection** and **Server-Side Template Injection (SSTI)**, retrieving sensitive data or reading files on the server without human intervention. These capabilities were demonstrated through multi-step attack chains that combined web navigation, information gathering, and payload execution. Notably, GPT-4 showed success in attacks where other models failed.

Further research focused on LLM agents exploiting **known vulnerabilities** (CVE-listed), automating exploit processes that previously required manual effort. Such automation indicates a potential shift from simple bots to more sophisticated, agent-driven offensive tools.

Another case involved the development of **ReaperAI**, an autonomous agent using large-scale language models to simulate and execute cyberattacks, successfully identifying and exploiting vulnerabilities in controlled environments. This underscores the risk of LLM agents being used for offensive operations at scale.

Recommended safeguards include rigorous **testing and evaluation of agents in controlled environments**, continuous monitoring for unexpected behaviors, and restricting agent capabilities to only what is absolutely necessary. Limiting access to sensitive tools and enforcing strict validation of agent actions are also suggested to prevent misuse and exploitation.

-----

-----

-----

### Source [45]: https://arxiv.org/html/2505.13076v1

Query: What documented security vulnerabilities (e.g., agent-injection, tool misuse) and recommended safeguards have researchers identified when deploying autonomous LLM agents in production?

Answer: This source details multiple **security vulnerabilities** specific to autonomous LLM agent deployments, particularly for agents with browsing or tool-invocation capabilities.

Key documented vulnerabilities include:

- **Tool Misuse**: Agents may call legitimate tools with malicious or unintended arguments, resulting in harmful actions such as data exfiltration or destructive edits. This can occur due to weak validation of tool input or argument overloading, where subtle manipulations bypass security checks.
- **Prompt-Template Tampering**: If runtime templates that structure prompts for the LLM are altered, either by attackers or faulty deployments, agents may receive instructions that disable safety constraints. For example, a debug template could remove all guardrails, leading to unsafe agent behavior.
- **Working Memory Poisoning**: Malicious data injected into the agent's memory can persist and be replayed in future prompts, contaminating reasoning and leading to unsafe actions (e.g., autofilling weak passwords).
- **Infinite-Step or Looping Plans**: Agents may generate recursive or cyclic plans, causing excessive resource consumption (API calls, tokens) and potential denial of service.
- **Tool-Registry Manipulation**: Attackers may modify the registry that maps agent tools, allowing unauthorized capabilities (such as shell execution) or disabling critical safety functions.

Recommended safeguards include:
- **Strict argument validation** for tool invocations.
- **Controlled access and integrity checks** for prompt templates and tool registries.
- **Input sanitization** for agent memory and persistent stores.
- **Execution limits and monitoring** to detect and halt infinite loops.
- **Isolation of agent environments** to minimize lateral movement or impact from compromised components.

-----

-----

-----

### Source [46]: https://arxiv.org/html/2404.08144v1

Query: What documented security vulnerabilities (e.g., agent-injection, tool misuse) and recommended safeguards have researchers identified when deploying autonomous LLM agents in production?

Answer: This research shows that **LLM agents can autonomously exploit one-day vulnerabilities**—recently disclosed vulnerabilities with public exploits, but not yet patched in all systems. In a controlled study, researchers provided GPT-4 agents with the CVE descriptions for 15 real-world vulnerabilities, including some with critical severity. The GPT-4 agents were able to exploit **87%** of these vulnerabilities, whereas other models and automated scanners (like ZAP and Metasploit) had zero success.

Importantly, the ability to exploit was highly dependent on the agent's access to **detailed vulnerability descriptions**. Without the CVE description, GPT-4 exploited only 7% of vulnerabilities.

The study raises concerns about deploying highly capable LLM agents in production, especially if they can access real-time vulnerability feeds or descriptions. This could allow for rapid, autonomous exploitation before human defenders can respond.

Safeguards suggested or implied include limiting agent access to sensitive vulnerability data, restricting outbound actions (especially those that can interact with system-level resources), and careful monitoring of agent activity for signs of exploitation or lateral movement.

-----

-----

</details>

<details>
<summary>Which technical write-ups describe the orchestration layer that coordinates multi-step LLM workflows versus agentic planners (for example, LangGraph, Ray Serve, or Amazon Bedrock Agents) and compare their design trade-offs?</summary>

### Source [47]: https://aws.amazon.com/blogs/machine-learning/build-multi-agent-systems-with-langgraph-and-amazon-bedrock/

Query: Which technical write-ups describe the orchestration layer that coordinates multi-step LLM workflows versus agentic planners (for example, LangGraph, Ray Serve, or Amazon Bedrock Agents) and compare their design trade-offs?

Answer: The integration of LangGraph with Amazon Bedrock is discussed in this post, highlighting how it advances multi-agent system development by providing a robust framework for sophisticated AI applications. LangGraph's orchestration capabilities and feature management in Amazon Bedrock create scalable, efficient systems that address challenges in multi-agent architectures through state management, agent coordination, and workflow orchestration. This integration offers features like memory management, error handling, and human-in-the-loop capabilities. LangGraph Studio's visualization and debugging tools enable efficient design and maintenance of complex agent interactions, providing a powerful foundation for next-generation multi-agent systems with effective workflow handling and optimal resource utilization.

-----

-----

### Source [48]: https://aws.amazon.com/blogs/machine-learning/design-multi-agent-orchestration-with-reasoning-using-amazon-bedrock-and-open-source-frameworks/

Query: Which technical write-ups describe the orchestration layer that coordinates multi-step LLM workflows versus agentic planners (for example, LangGraph, Ray Serve, or Amazon Bedrock Agents) and compare their design trade-offs?

Answer: This write-up provides step-by-step instructions for creating a collaborative multi-agent framework with reasoning capabilities using Amazon Bedrock and open-source frameworks like LangGraph. The graph-based approach is crucial for representing the structure of multi-agent systems, making it easier to analyze, simulate, and reason about emergent behaviors from agent interactions. The framework emphasizes a plug-and-play feature, allowing dynamic changes and flexibility to accommodate third-party agents. This adaptability enhances the system's versatility and usability, particularly in domains requiring complex, dynamic interactions between autonomous entities.

-----

-----

### Source [49]: https://slashdot.org/software/comparison/Amazon-Bedrock-vs-LangGraph/

Query: Which technical write-ups describe the orchestration layer that coordinates multi-step LLM workflows versus agentic planners (for example, LangGraph, Ray Serve, or Amazon Bedrock Agents) and compare their design trade-offs?

Answer: This comparison highlights the differences between Amazon Bedrock and LangGraph. Amazon Bedrock is a comprehensive service for developing and expanding generative AI applications by providing access to high-performance foundation models. It streamlines infrastructure management and offers a unified API for personalizing models. On the other hand, LangGraph is a platform for creating agents capable of managing intricate tasks, offering a flexible framework for various control mechanisms and ensuring reliability through moderation and quality loops. While Amazon Bedrock focuses on AI model integration, LangGraph emphasizes agent-driven application development and scalability.

-----

</details>

<details>
<summary>What benchmark reports released in 2025 compare Deep Research agents (Perplexity, Gemini Discovery, OpenAI’s Researcher, etc.) with traditional search or RAG pipelines on accuracy, citation quality, and turnaround time?</summary>

### Source [55]: https://huggingface.co/papers/2506.11763

Query: What benchmark reports released in 2025 compare Deep Research agents (Perplexity, Gemini Discovery, OpenAI’s Researcher, etc.) with traditional search or RAG pipelines on accuracy, citation quality, and turnaround time?

Answer: A comprehensive benchmark report titled **"DeepResearch Bench"** was released in June 2025 to systematically evaluate the capabilities of Deep Research Agents compared to traditional research and retrieval-augmented generation (RAG) pipelines. The benchmark consists of 100 PhD-level research tasks across 22 fields, all crafted by domain experts. It introduces two novel methodologies for evaluation:
- A **reference-based method** with adaptive criteria to assess the quality of generated research reports.
- A framework for evaluating agents' information retrieval and collection capabilities, specifically analyzing **effective citation count** and **overall citation accuracy**.

DeepResearch Bench is open-sourced and designed to provide strong alignment with human judgment, aiming to accelerate the development and objective comparison of LLM-based research agents on metrics such as **accuracy, citation quality, and turnaround time**.

Key highlights:
- The benchmark focuses explicitly on **research quality, information retrieval accuracy, effective citation count, and citation accuracy**.
- It provides a direct framework for comparing Deep Research Agents—such as those from Perplexity, Gemini, and OpenAI—against traditional search and RAG pipelines.
- The open-source nature allows for transparent, reproducible evaluations across the research community.

The benchmark and its methodology are available publicly, providing a standardized way to assess Deep Research Agents as of 2025[1].

-----

-----

-----

### Source [56]: https://www.helicone.ai/blog/openai-deep-research

Query: What benchmark reports released in 2025 compare Deep Research agents (Perplexity, Gemini Discovery, OpenAI’s Researcher, etc.) with traditional search or RAG pipelines on accuracy, citation quality, and turnaround time?

Answer: This report from February 2025 provides a comparative analysis of Deep Research solutions from **OpenAI, Perplexity, and Google Gemini**, including direct discussions of their performance on accuracy, citation quality, and turnaround time:

- **OpenAI Deep Research** is identified as the most powerful but also the most expensive. It excels at technical and academic research, offering **high accuracy** (with occasional errors), **generally reliable citations** (though some errors are noted), and **detailed output**. Turnaround time ranges from **5 to 30 minutes per query**.
- **Perplexity Deep Research** is highlighted for its **speed** (2–4 minutes per query), **high accuracy** (slightly below OpenAI), and **consistently reliable citations**. It is favored for real-time analysis and journalism due to its structured, concise, and well-cited summaries.
- **Gemini Deep Research** is more affordable but prone to **SEO-driven biases** and **citation inaccuracies**.

The comparison includes a table summarizing cost, level of detail, source diversity, process transparency, and output format. While all models show progress, reliability remains a challenge, especially for complex queries.

This report is among the most cited for practical, end-user-focused benchmarking of Deep Research agents as of early 2025[2].

-----

-----

-----

### Source [57]: https://www.youtube.com/watch?v=qnqW7ievln4

Query: What benchmark reports released in 2025 compare Deep Research agents (Perplexity, Gemini Discovery, OpenAI’s Researcher, etc.) with traditional search or RAG pipelines on accuracy, citation quality, and turnaround time?

Answer: A video published in June 2025 discusses the newly released **DeepResearch Bench** benchmark. The presenter reviews the structure and methodology of this benchmark:

- The benchmark was created using a dataset of **100,000 real-world user queries**, filtered and organized to focus on **22 research domains**.
- Evaluation involves two newly developed methods for assessing research quality and information retrieval effectiveness.
- The benchmark is described as more complex and challenging than previous ones, reflecting the advanced capabilities of modern LLM-based research agents.
- The video emphasizes that the benchmark directly compares **Deep Research Agents** (such as those from OpenAI, Perplexity, and Gemini) and highlights the importance of **citation accuracy, research depth, and turnaround time** as measured metrics.

This source confirms that DeepResearch Bench is recognized in the community as the new standard for benchmarking Deep Research Agents in 2025[3].

-----

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>4 Agentic AI Design Patterns & Real-World Examples [2025]</summary>

# 4 Agentic AI Design Patterns & Real-World Examples [2025]

[Agentic AI](https://research.aimultiple.com/agentic-ai/) design patterns enhance the autonomy of [large language models (LLMs)](https://research.aimultiple.com/large-language-models-examples/) like Llama, Claude, or GPT by leveraging tool-use, decision-making, and problem-solving. This brings a structured approach for creating and managing autonomous agents in several [use cases](https://research.aimultiple.com/agentic-ai-design-patterns/#agentic-workflows-use-cases).

## What are agentic workflows?

An agent is considered more intelligent if it consistently chooses actions that lead to outcomes more closely aligned with its objective function.

https://research.aimultiple.com/wp-content/uploads/2025/04/agentic-wokrflows-1224x512.png.webp_Agentic workflows_ [1](https://research.aimultiple.com/agentic-ai-design-patterns/#easy-footnote-bottom-1-1417491 "https://medium.com/machine-learning-bites/agentic-workflows-3b786c6dcb53")

**Automated workflows (rule-based, non-Al)**

Follow **predefined rules and processes**, typically based on fixed instructions. They are designed to handle repetitive tasks efficiently, often through systems like robotic process automation (RPA), where little to no decision-making is required.

**AI workflows (non-agentic)**

Systems where LLMs and tools are orchestrated through predefined code paths, with minimal thinking involved.  In a non-agentic workflow, an LLM generates an output from a prompt, like generating a list of recommendations based on input.

**Agentic workflows**

AI-driven processes where autonomous agents make decisions, take actions, and coordinate tasks with minimal human input. These workflows use key components like reasoning, planning, and tool utilization to handle complex tasks.

Compared to traditional automation, like [RPA](https://research.aimultiple.com/robotic-process-automation-use-cases/), which follows fixed rules and designs, agentic workflows are more “ **dynamic and flexible**”, adapting to real-time data and unexpected conditions.

https://research.aimultiple.com/wp-content/uploads/2025/04/unnamed.gif_Agentic workflow example_ [2](https://research.aimultiple.com/agentic-ai-design-patterns/#easy-footnote-bottom-2-1417492 "https://www.linkedin.com/posts/dipanjans_there-is-a-lot-of-hype-on-ai-agents-recently-activity-7249082921423110144-a5Uh/")

**In this workflow, the** [**AI agent**](https://research.aimultiple.com/ai-agent-tools/) **is answering the user query (Example: “Who won the Euro in 2024?”)**

1. **User query:** The user asks a question.

2. [**LLM**](https://research.aimultiple.com/large-language-models-examples/) **analysis:** The LLM interprets it and determines if external data is needed.

3. **External tool activation:** A search tool retrieves real-time info.

4. **Response creation:** The LLM combines the data and replies:

_“Spain won the Euro 2024 against England with a score of 2–1 in the Final in Berlin in July 2024.”_

## 4 types of agentic AI design patterns

## Reflection pattern

https://research.aimultiple.com/wp-content/uploads/2025/04/Reflection-pattern-1224x690.png.webp

The reflection pattern enhances agentic workflows with continuous self-improvement.

→ This pattern involves a self-feedback mechanism where an AI agent evaluates its outputs or decisions before finalizing its response or taking further action.

→ It allows the agent to analyze its own work, identify errors or gaps, and refine its approach, leading to better results over time. This process is not limited to a single iteration, agents can adjust their answers in subsequent interactions.

**Real-world example:**

AI agents such as **GitHub Copilot** can refine the code through self-reflection by examining and modifying its own structure and behavior at runtime, for example:

- **Initial response**: GitHub Copilot generates a code snippet based on a prompt.

- **Reflection process**: Reviews the generated code for errors, inefficiencies, or improvements. It may use a feedback loop, such as running the code in a sandbox environment, to identify bugs.

- **Self-iteration**: Evaluates whether the generated code functions as expected, refines its logic, and suggests optimizations.

## Tool use pattern

https://research.aimultiple.com/wp-content/uploads/2025/04/Tool-use-pattern-1224x690.png.webp

The **tool use pattern** in [agentic](https://research.aimultiple.com/agentic-ai-trends/) [AI](https://research.aimultiple.com/agentic-ai-trends/) enhances the capabilities of large language models (LLMs) by enabling them to interact dynamically with external tools and resources.

**Protocols** like the [Model Context Protocol (MCP)](https://research.aimultiple.com/model-context-protocol/) help standardize the tool use process.[3](https://research.aimultiple.com/agentic-ai-design-patterns/#easy-footnote-bottom-3-1417493 "https://docs.anthropic.com/en/docs/agents-and-tools/mcp")

This allows the AI to move beyond its pre-existing training data and perform real-world applications. With tool use patents and agentic models, can:

- access real-time information (via APIs), search the web
- interact with APIs to process and generate responses
- interact  with information retrieval systems
- retrieve specific datasets
- run scripts for data analysis
- leverage machine learning models to run specialized algorithms

_We used popular AI agents to test their tool use capabilities:_

- [Tool use benchmark results](https://research.aimultiple.com/ai-agents/#tool-use-benchmark-results)
- [Web search benchmark results](https://research.aimultiple.com/ai-agents/#web-search-benchmark-results)

**Real-world example:**

**Visual-textual synthesis project** uses **GPT-4** to interact dynamically with both external tools (such as CLIP for image analysis and GPT-4 for reasoning) and external resources (e.g., design tools, e-commerce platforms) to complete complex tasks.[4](https://research.aimultiple.com/agentic-ai-design-patterns/#easy-footnote-bottom-4-1417494 "https://arxiv.org/abs/2307.11661")

## Planning pattern

https://research.aimultiple.com/wp-content/uploads/2025/04/Planning-pattern-1224x690.png.webp

The **planning pattern** enables LLMs to break down large tasks into subtasks.

An LLM using the planning pattern will organize the sub-goals into a logical sequence. Depending on the complexity, the agent may plan actions in a linear order or create branches for parallel execution.

**Real-world example:**

A group of researchers demonstrated how LLM agents collaborate with models from platforms like Hugging Face to handle complex, larger tasks.

The approach was called **HuggingGPT**, an LLM-powered agent that leverages LLMs (e.g., ChatGPT) to connect various AI models in machine learning communities (e.g., Hugging Face) to solve AI tasks.[5](https://research.aimultiple.com/agentic-ai-design-patterns/#easy-footnote-bottom-5-1417495 "https://arxiv.org/abs/2303.17580")

## Multi-agent pattern

https://research.aimultiple.com/wp-content/uploads/2025/04/Multi-agent-pattern-1224x690.png.webp

The multi-agent patterns focus on task delegation, which involves assigning different agents to different tasks that can be created by prompting a single LLM (or multiple LLMs) to handle distinct responsibilities.

For example, to create a software developer agent, you could prompt the LLM: _“You are an expert in writing efficient, clear code. Please write the code to accomplish \[specific task\]_. _“_

In multi-agent systems, agents communicate using Agent-to-Agent (A2A) protocols that define the flow of information between them. For instance, **Google’s A2A protocol** is an open framework that equips agents with structured context and tools.[6](https://research.aimultiple.com/agentic-ai-design-patterns/#easy-footnote-bottom-6-1417496 "https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/")

**Real-world examples of multi-agent frameworks:**

- AutoGen
- LangChain
- ChatDev
- OpenAI Swarm

**For more:** [Open source agentic AI builders](https://research.aimultiple.com/ai-agent-builders/#open-source-frameworks) & frameworks

## Agentic workflow use cases

### 1\. Retrieval-augmented generation (RAG)

Agentic design patterns can be used in RAG systems to incorporate agents into the RAG pipeline.

**For more, see:**

→ [Discover Top 20+ Agentic RAG Systems](https://research.aimultiple.com/agentic-rag/)

→ [Compare Top 20+ Retrieval-Augmented Generation Tools](https://research.aimultiple.com/retrieval-augmented-generation/)

### 2\. Software development

- **Code generation & completion**:


  - **Cursor**: Automatically generates code snippets and entire functions based on natural language descriptions
  - **Devin:** Creates apps from scratch with minimal human oversight, using a browser or a command line interface.
- **Automated software testing**:


  - **Diffblue**: Automatically writes unit tests for Java code, ensuring coverage and code correctness.

  - **Snyk**: Detects and fixes security vulnerabilities in dependencies without human input.

### 3\. Gaming

- **Autonomous NPCs:**
  - **AI Dungeon**: Uses an LLM to generate fully autonomous text-based NPCs, reacting to player actions and creating narrative events.
  - **AgentRefine:** Enables AI agents and models to identify errors and autonomously correct them, improving their performance for general tasks.
- **Autonomous exploration:**
  - **Spore (AI-controlled evolution)**: AI agents reproduce, mutate, and evolve without human intervention, becoming increasingly intelligent and diverse with each generation.
- **Pathfinding:**
  - **NavMesh AI**: Autonomous pathfinding system in gaming, where agents can navigate dynamic environments.

### 4\. Multimedia creation

- **Turning GenAI search results into Wikipedia pages**
  - **Perplexity Pages:** When a user enters a search query, Perplexity Pages aggregates relevant information from multiple sources to turn search results into Wikipedia pages.
- **Automated video production**
  - **Pictory** autonomously turns text-based content into video.

### 5\. Research & data analysis

- **ChemCrow**: Running simulations and making autonomous recommendations.

for drug discovery.
- **AI2:** Provides data warehouse management through autonomous systems.

### 6\. Computer use

Computer-use agents (e.g., Anthropic’s Claude Computer Use, or Open Operator) can interact with GUIs, the buttons, menus, and text fields people see on a screen, just as humans do.

These agents can:

- Fill out online forms
- Search the web
- Book travel arrangements
- Automating workflows

### 7\. Customer service

[AI agents for customer service](https://research.aimultiple.com/ai-agents-customer-service/) respond to customer queries in natural language, interpret context, and generate human-like responses. These agents are commonly used for contact center automation. Some examples include:

- Zendesk AI
- Intercom’s Fim
- Kore.AI Agent

### 8\. Healthcare automation

[Agentic AI for healthcare](https://research.aimultiple.com/agentic-ai-healthcare/) aims to leverage healthcare systems to automate workflows in clinical operations. Tool examples include:

**General-purpose healthcare automation:**

- Sully.ai
- Hippocratic AI
- Innovacer
- Beam AI Healthcare agent
- Notable Health

**Patient support:**

- Amelia AI
- Cognigy

## Further reading

- [Top AI agent tools](https://research.aimultiple.com/ai-agent-tools/)
- [AI Agents: Operator vs Browser Use vs Project Mariner](https://research.aimultiple.com/ai-agents/)

</details>

<details>
<summary>Agentic AI vs LLM: Comparing What Scales Better in Task Runners</summary>

# Agentic AI vs LLM: Comparing What Scales Better in Task Runners

Picture a factory. One worker follows instructions from a manager and completes one task at a time. Another? Thinks, plans, uses tools, collaborates, and adjusts on the fly. Both are efficient in different ways — but scale them across thousands of workflows, and the differences start to matter.

That’s what enterprises are facing today with AI. Enterprise AI integrates artificial intelligence and machine learning into large-scale operations, accelerating problem-solving and improving business efficiency.

On one side: **LLM-based task runners** — simple, fast, and stateless. LLMs are primarily used for text generation, producing new content such as emails or dialogues. They are capable of generating human-like text for communication and automation. On the other: **Agentic AI systems**, goal-driven, multi-step thinkers with memory and tool usage. Unlike traditional AI, which relies on predefined rules and passive data processing, agentic AI exhibits goal oriented behavior and autonomy, focusing on achieving specific objectives.

This blog breaks down which approach scales better across different dimensions: performance, cost, complexity, and reliability. It’s not just about what works — it’s about what works _when_.

## 1\. Core Differences

#### What is a Task Runner?

LLM-based task runners are single-prompt systems powered by large language models (LLMs). Large language models (LLMs) are advanced AI systems designed to generate text and answer questions based on user prompts. A question goes in, and a response comes out. These models are used in workflows like summarization, email drafting, classification, or SQL generation—these are specific tasks that LLMs can perform. LLM workflows are explicitly defined, with clear steps and little room for adaptation. They don’t remember past tasks and don’t plan future steps. LLMs are capable of generating text for a variety of applications.

#### What is Agentic AI?

Agentic AI systems are composed of autonomous agents that can operate independently. These AI agents can act independently or collaborate within a multi-agent system to accomplish tasks and execute multi-step processes. They can reason through goals, break them into multi-step tasks, invoke external tools, access memory, and iterate until the job is done. Agentic AI works by following a structure: **planner + executor + memory + toolchain.** This structure enables AI agents to function effectively by integrating with external tools, breaking down objectives into multi-step tasks, and working together within multi-agent systems to achieve complex goals.

**Table: Key Architectural Differences**

| Feature | LLM Task Runner | Agentic AI System |
| --- | --- | --- |
| State | Stateless | Stateful (via memory) |
| Step count | Single-step | Multi-step |
| Control | User-driven | Goal-driven autonomy |
| Tool usage | Rare | Frequent |
| Complexity handling | Minimal | Supports nested logic |

## 2\. Scaling Workload and Complexity with Minimal Human Intervention

#### 2.1 Horizontal vs Vertical Scaling

- **LLM runners** scale horizontally, you can run 10,000 prompts in parallel with little orchestration.
- **Agentic AI** scales vertically, it handles complex workflows by chaining multiple steps, with some sub-tasks parallelized using multi-agent orchestration (e.g., CrewAI, LangGraph). Advanced AI models and AI tools, powered by machine learning, enable agentic systems to scale efficiently with minimal human input.

#### 2.2 Complexity Tradeoffs in Complex Tasks

Agentic systems are better at breaking down complex tasks (e.g., writing and testing a full codebase or handling end-to-end customer queries). Agentic AI can also be used for content creation, content generation, and code generation, streamlining software development by enabling AI agents to write code and solve complex problems through collaborative, automated workflows. But with complexity comes slower execution and greater engineering effort.

**Table: Scaling Comparison**

| Metric | LLM Runners | Agentic AI |
| --- | --- | --- |
| Throughput | High | Moderate |
| Task Complexity | Low | High |
| Parallel Execution | Easy | Needs orchestration |
| Developer Overhead | Low | High |

## 3\. Latency, Cost & Resource Impact

#### 3.1 Latency

- LLM runners: Single call = low latency (~300ms–2s).
- Agentic AI: 3–10s _per_ reasoning loop; total workflow can take minutes if steps chain.

#### 3.2 Cost Per Execution

- LLM runners: $0.001–$0.02 per call (OpenAI, Claude, Gemini Pro).
- Agentic AI: $0.10–$5 per workflow depending on memory use, tool calls, number of steps.

For example:

> Drafting 1 email using GPT-4 might cost $0.01.
>
> A sales outreach agent that searches CRM, writes the email, adds personalisation, and schedules the send might cost $0.50–$1.20.

#### 3.3 Infrastructure Burden

- LLM runners don’t need persistent storage or state management.
- Agentic AI systems often need:
  - Memory storage (e.g., Redis, vector DBs)
  - Tool integration (APIs, SDKs)
  - Logs, checkpoints, debugging layers

## 4\. Reliability, Monitoring & Risk

#### 4.1 Task Completion

Studies show basic agents fail or hallucinate when instructions become ambiguous. Without guardrails, agent loops can spiral into irrelevant sub-tasks.

- AutoGPT and similar systems often see 20–40% task failure in open-ended goals.
- Controlled environments (LangGraph, CrewAI) reduce failures via structured flows.

#### 4.2 Observability and Debugging

LLM runners are easy to debug — just retry the prompt.

Agentic AI, however, may fail due to:

- Bad tool usage
- Memory corruption
- Wrong planning logic
- Looping behavior

This requires logging at every step, trace visualizations, and often human-in-the-loop.

## 5\. Use Cases

#### 5.1 Where LLM Runners Shine

- Chatbots with tight scripts
- Classification & tagging
- Email summarization
- Extract-transform-load (ETL) operations

LLM runners excel at natural language understanding and text generation, making them ideal for chatbots and summarization tasks.

These don’t need memory or planning.

#### 5.2 Where Agentic AI Is Better

- Software QA bots: test, generate logs, file Jira tickets
- Customer agents: handle full complaint cycles from lookup to escalation
- Financial research agents: analyze quarterly results and build investment briefs. Agentic AI can leverage domain-specific knowledge and contextual awareness to deliver more accurate and relevant results in these tasks.
- Document processing: parse, summarize, validate, cross-reference data across files. Agentic AI can process real-time data and adapt to dynamic environments, ensuring up-to-date and flexible document handling.

## 6\. Maturity and Production Readiness

#### LLM Runners

- Mature and used at scale in enterprises
- Supported by platforms like OpenAI, Cohere, AWS Bedrock
- Minimal infra needed

#### Agentic Systems

- Still early-stage in production-grade stability
- Growing maturity through LangGraph, CrewAI, Autogen, Microsoft AutoGen
- Requires tighter control to meet enterprise standards (SOC2, PII handling, audit logs)

## Which One Scales Better?

Let’s break it down:

Before diving into the details, it’s important to highlight the key differences between LLM runners and agentic AI: LLM runners excel at handling a wide range of tasks simultaneously (horizontal scale), while agentic AI focuses on deeper, more autonomous decision-making and complex task execution (task depth).

https://i0.wp.com/www.lyzr.ai/wp-content/uploads/2025/06/Agentic-AI-vs-LLM-1.webp?resize=1024%2C577&ssl=1

| Dimension | LLM Runners | Agentic AI |
| --- | --- | --- |
| Horizontal Scale | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Task Depth | ⭐⭐ | ⭐⭐⭐⭐ |
| Cost Efficiency | ⭐⭐⭐⭐ | ⭐ |
| Observability | ⭐⭐⭐ | ⭐⭐ |
| Maturity | ⭐⭐⭐⭐ | ⭐⭐ |
| Engineering Need | ⭐ | ⭐⭐⭐⭐ |

LLM runners scale _wider_. Agentic AI scales _deeper_.

## The Hybrid Future

Most scalable AI workflows in production today are **hybrids**:

- Stateless LLM components handle fast responses.
- Agentic subsystems step in when workflows need judgment, planning, or context.

Agentic AI brings new capabilities to hybrid workflows by enabling autonomous operation, collaboration among multiple AI agents, and the facilitation of complex, structured workflows.

For example, a support agent might:

- Use LLM for instant replies to FAQs.
- Switch to an agentic flow for billing disputes: lookup → policy check → escalation.

Agentic AI represents a significant advancement in autonomous operations, allowing subsystems to operate independently and collaboratively to achieve complex goals.

As agent platforms mature and serving gets faster (e.g., Autellix reports 4–15× throughput improvements), more enterprises will layer agentic reasoning into LLM workflows — not replace them. Agentic AI operates within these hybrid architectures to enable more complex automation by actively managing tasks, adapting to new information, and making decisions autonomously.

## Wrapping up

Scalability isn’t just about volume — it’s about matching the right architecture to the right job.

- LLM-based task runners are efficient, fast, and production-ready for most single-step tasks.
- Agentic AI introduces autonomy and depth, but comes with cost, latency, and operational complexity.

The best systems don’t choose between the two — they blend both.

**Start simple. Scale smart. Automate what matters.**

</details>

<details>
<summary>Building effective agents</summary>

# Building effective agents

Published Dec 19, 2024

We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks.

Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.

In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents.

## What are agents?

"Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as **agentic systems**, but draw an important architectural distinction between **workflows** and **agents**:

- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems.

## When (and when not) to use agents

When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.

## When and how to use frameworks

There are many frameworks that make agentic systems easier to implement, including:

- [LangGraph](https://langchain-ai.github.io/langgraph/) from LangChain;
- Amazon Bedrock's [AI Agent framework](https://aws.amazon.com/bedrock/agents/);
- [Rivet](https://rivet.ironcladapp.com/), a drag and drop GUI LLM workflow builder; and
- [Vellum](https://www.vellum.ai/), another GUI tool for building and testing complex workflows.

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

See our [cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents) for some sample implementations.

## Building blocks, workflows, and agents

In this section, we’ll explore the common patterns for agentic systems we’ve seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents.

### Building block: The augmented LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png&w=3840&q=75The augmented LLM

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), which allows developers to integrate with a growing ecosystem of third-party tools with a simple [client implementation](https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients).

For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities.

### Workflow: Prompt chaining

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png&w=3840&q=75The prompt chaining workflow

**When to use this workflow:** This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

**Examples where prompt chaining is useful:**

- Generating Marketing copy, then translating it into a different language.
- Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.

### Workflow: Routing

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png&w=3840&q=75The routing workflow

**When to use this workflow:** Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

**Examples where routing is useful:**

- Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
- Routing easy/common questions to smaller models like Claude 3.5 Haiku and hard/unusual questions to more capable models like Claude 3.5 Sonnet to optimize cost and speed.

### Workflow: Parallelization

LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting:** Running the same task multiple times to get diverse outputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png&w=3840&q=75The parallelization workflow

**When to use this workflow:** Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

**Examples where parallelization is useful:**

- **Sectioning**:
  - Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response.
  - Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model’s performance on a given prompt.
- **Voting**:
  - Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem.
  - Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives.

### Workflow: Orchestrator-workers

In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png&w=3840&q=75The orchestrator-workers workflow

**When to use this workflow:** This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**Example where orchestrator-workers is useful:**

- Coding products that make complex changes to multiple files each time.
- Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information.

### Workflow: Evaluator-optimizer

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png&w=3840&q=75The evaluator-optimizer workflow

**When to use this workflow:** This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

**Examples where evaluator-optimizer is useful:**

- Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques.
- Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted.

### Agents

Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 ("Prompt Engineering your Tools").

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png&w=3840&q=75Autonomous agent

**When to use agents:** Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

**Examples where agents are useful:**

The following examples are from our own implementations:

- A coding Agent to resolve [SWE-bench tasks](https://www.anthropic.com/research/swe-bench-sonnet), which involve edits to many files based on a task description;
- Our [“computer use” reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), where Claude uses a computer to accomplish tasks.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png&w=3840&q=75High-level flow of a coding agent

## Combining and customizing these patterns

These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity _only_ when it demonstrably improves outcomes.

## Summary

Success in the LLM space isn't about building the most sophisticated system. It's about building the _right_ system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

When implementing agents, we try to follow three core principles:

1. Maintain **simplicity** in your agent's design.
2. Prioritize **transparency** by explicitly showing the agent’s planning steps.
3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.

Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users.

## Appendix 1: Agents in practice

Our work with customers has revealed two particularly promising applications for AI agents that demonstrate the practical value of the patterns discussed above. Both applications illustrate how agents add the most value for tasks that require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight.

### A. Customer support

Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because:

- Support interactions naturally follow a conversation flow while requiring access to external information and actions;
- Tools can be integrated to pull customer data, order history, and knowledge base articles;
- Actions such as issuing refunds or updating tickets can be handled programmatically; and
- Success can be clearly measured through user-defined resolutions.

Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness.

### B. Coding agents

The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because:

- Code solutions are verifiable through automated tests;
- Agents can iterate on solutions using test results as feedback;
- The problem space is well-defined and structured; and
- Output quality can be measured objectively.

In our own implementation, agents can now solve real GitHub issues in the [SWE-bench Verified](https://www.anthropic.com/research/swe-bench-sonnet) benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.

## Appendix 2: Prompt engineering your tools

No matter which agentic system you're building, tools will likely be an important part of your agent. [Tools](https://www.anthropic.com/news/tool-use-ga) enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a [tool use block](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#example-api-response-with-a-tool-use-content-block) in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools.

There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes.

Our suggestions for deciding on tool formats are the following:

- Give the model enough tokens to "think" before it writes itself into a corner.
- Keep the format close to what the model has seen naturally occurring in text on the internet.
- Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.

One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good _agent_-computer interfaces (ACI). Here are some thoughts on how to do so:

- Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it’s probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools.
- How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools.
- Test how the model uses your tools: Run many example inputs in our [workbench](https://console.anthropic.com/workbench) to see what mistakes the model makes, and iterate.
- [Poka-yoke](https://en.wikipedia.org/wiki/Poka-yoke) your tools. Change the arguments so that it is harder to make mistakes.

While building our agent for [SWE-bench](https://www.anthropic.com/research/swe-bench-sonnet), we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.

</details>

<details>
<summary>From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents</summary>

# From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents

Information retrieval is a cornerstone of modern knowledge acquisition, enabling billions of queries each day across diverse domains. However, traditional keyword-based search engines are increasingly inadequate for handling complex, multi-step information needs. Our position is that Large Language Models (LLMs), endowed with reasoning and agentic capabilities, are ushering in a new paradigm termed Agentic Deep Research. These systems transcend conventional information search techniques by tightly integrating autonomous reasoning, iterative retrieval, and information synthesis into a dynamic feedback loop. We trace the evolution from static web search to interactive, agent-based systems that plan, explore, and learn. We also introduce a test-time scaling law to formalize the impact of computational depth on reasoning and search. Supported by benchmark results and the rise of open-source implementations, we demonstrate that Agentic Deep Research not only significantly outperforms existing approaches, but is also poised to become the dominant paradigm for future information seeking.
All the related resources, including industry products, research papers, benchmark datasets, and open-source implementations, are collected for the community in [https://github.com/DavidZWZ/Awesome-Deep-Research](https://github.com/DavidZWZ/Awesome-Deep-Research "").

## 1 Introduction

“Introducing deep research: An agent that uses reasoning to synthesize large amounts of online information and complete multi-step research tasks for you.”

– OpenAI

Every day, billions of people search for information online  (Amendola et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib4 "")), and rely heavily on these online resources to make decisions across personal, professional, and societal contexts ( [Zhang et al., 2024a,](https://arxiv.org/html/2506.18959v2#bib.bib100 "")). For decades, traditional web search engines based on keyword matching have served as the primary gateway to digital information. While once revolutionary, these systems increasingly struggle with complex, multi-faceted queries that demand nuanced understanding and synthesis (Mo et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib55 "")). The growing inadequacy highlights their inherent limitations in contextual comprehension and knowledge integration.

Against this backdrop, information seeking and synthesis are undergoing a profound transformation with large language models (LLMs). Rather than merely enhancing traditional search paradigms, LLMs are poised to fundamentally replace them in addressing complex information needs.
Initially, we witnessed the rise of LLMs as standalone, knowledgeable chatbots, which challenged the dominance of web search by offering more direct answers and a degree of synthesis, thereby reducing the user’s burden of sifting through numerous links (Liu et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib48 "")). However, single LLMs are tethered to static, offline knowledge. The subsequent integration of search and retrieval-augmented generation (RAG) marked a step forward, grounding LLMs in external data and mitigating issues like hallucination (Ma et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib51 ""); Yang et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib93 "")). Nevertheless, these naive RAG methods still struggle with real-world questions that require sophisticated multi-hop reasoning and strategic search planning, as they often cannot plan correct search paths for complex problems ( [Yao et al., 2023b,](https://arxiv.org/html/2506.18959v2#bib.bib96 "")).

https://arxiv.org/html/x1.png  
Figure 1: The evolution of information search paradigms.

Recently, test-time scaling (TTS) has emerged as a potent paradigm for boosting the reasoning and agentic capabilities of LLMs (Snell et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib71 "")). It assigns additional computation during inference, enabling deeper problem-solving ( [Zou et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib113 ""); Gu et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib23 "")).
Equipped with TTS on reasoning and search, LLMs are set to drive a new search paradigm termed Agentic Deep Research systems, which are capable of autonomous reasoning, on-demand searching, and iterative information synthesis.
Demonstrations from deep research products launched by OpenAI and Google highlight several key advantages of this paradigm: (1) Comprehensive Understanding: Ability to dissect and address complex, multifaceted queries that overwhelm traditional methods (Wei et al.,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib89 "")); (2) Enhanced Synthesis: Excels at synthesizing information from diverse, potentially conflicting sources into coherent and insightful narratives (Cheng et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib19 "")); (3) Reduced User Burden: Significantly decreases the cognitive load and manual effort required from users by automating laborious search steps (Sami et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib65 "")).

Our position is that the LLM-driven Agentic Deep Research framework will inevitably become the dominant paradigm for future information search.
In this paper, we comprehensively investigate this paradigm shift and make four key contributions: (1) We systematically trace and analyze the evolutionary trajectory of information search paradigms, from traditional keyword-based search, through conversational LLM chatbots and naive search-augmented LLMs, and ultimately to the Agentic Deep Research; (2) We introduce the test-time scaling (TTS) law for Deep Research, a novel hypothesis formalizing the relationship between inference-time computational resources allocation and the resulting improvements in LLMs reasoning capabilities and knowledge depth;
(3) We conduct extensive evaluations on existing Agentic Deep Research models, coupled with analyses of open-source implementations to support our position; and (4) As the first to holistically summarize the field of Deep Research, we offer a detailed exploration of critical future research directions, outlining both opportunities and challenges. Our discussion outlines a clear roadmap for this rapidly evolving field, underscoring how this evolution is fundamentally reshaping human interaction with real-world information and guiding further advancement on Agentic Deep Research.

## 2 Traditional Information Search Paradigms

The evolution of search paradigms as in Figure [1](https://arxiv.org/html/2506.18959v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents") represents a fundamental transformation in how humans access and interact with information. This section examines three distinct frameworks that have shaped the landscape of information retrieval: traditional web search engines, Large Language Models (LLMs) as chatbots, and LLMs with Retrieval Augmented Generation (RAG) systems. Each paradigm offers unique capabilities and addresses prior information seeking challenges, from systematic web crawling and ranking to interactive dialogue and knowledge-augmented generation.

### 2.1 Web Search

Web search has fundamentally transformed information access in modern society, enabling near-instantaneous retrieval of knowledge that previously required days or months to locate (Brin and Page,, [1998](https://arxiv.org/html/2506.18959v2#bib.bib11 "")). This revolutionary technology has democratized knowledge acquisition, accelerated economic development through improved information flow, and catalyzed scientific discovery by providing researchers with rapid access to cutting-edge developments. As the primary infrastructure for information retrieval in the Internet era, online search engines like Google have continuously shaped how humans interact with the expanding information landscape (Page et al.,, [1999](https://arxiv.org/html/2506.18959v2#bib.bib59 "")).

The applications of web search span diverse contexts, from general-purpose engines handling broad information needs to specialized platforms optimized for specific domains. General search engines utilize sophisticated algorithms to address multifaceted user queries (Broder,, [2002](https://arxiv.org/html/2506.18959v2#bib.bib12 "")), while specialized systems like Google Scholar focus on academic literature, providing researchers with precise pathways to scholarly resources (Noruzi,, [2005](https://arxiv.org/html/2506.18959v2#bib.bib58 "")). Content platforms (TikTok), social networks (Facebook), and e-commerce sites have developed internal search capabilities tailored to their unique content types and user behaviors, demonstrating how web search has permeated virtually every digital sphere.

Basically, web search operates through three fundamental processes: crawling (Khder,, [2021](https://arxiv.org/html/2506.18959v2#bib.bib37 "")), indexing (Hendriksen et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib27 "")), and ranking (Robertson et al.,, [2009](https://arxiv.org/html/2506.18959v2#bib.bib64 "")). Crawlers systematically discover and collect web content, which is then analyzed and organized into inverted indices for efficient retrieval. When users submit queries, search engines employ complex algorithms to assess document relevance and importance (Fuhr,, [1992](https://arxiv.org/html/2506.18959v2#bib.bib21 "")). The PageRank algorithm revolutionized search by evaluating page authority based on the web’s citation graph, determining a page’s significance through its incoming links from other high-quality pages (Page et al.,, [1999](https://arxiv.org/html/2506.18959v2#bib.bib59 "")). Modern search systems have further evolved to incorporate semantic understanding, user behavior data, and personalization to deliver increasingly relevant results ( [Wang et al., 2024b,](https://arxiv.org/html/2506.18959v2#bib.bib85 "")). However, the contexts presented to the user may not always be relevant and accurate, due to the limited context for user-specific complex queries (Leake and Scherle,, [2001](https://arxiv.org/html/2506.18959v2#bib.bib40 "")) and the influence of advertisement bidding (Linden et al.,, [2009](https://arxiv.org/html/2506.18959v2#bib.bib47 "")).

### 2.2 LLMs as Chatbots

Leveraging recent advances in natural language processing (NLP) and hardware enhancements, large language models (LLMs) represent the latest evolution in information retrieval as user chatbots for tailored response generation. Models like ChatGPT Achiam et al., ( [2023](https://arxiv.org/html/2506.18959v2#bib.bib2 "")), Claude Anthropic, ( [2023](https://arxiv.org/html/2506.18959v2#bib.bib5 "")), and LLaMa Touvron et al., ( [2023](https://arxiv.org/html/2506.18959v2#bib.bib78 "")) transcend traditional static retrieval methods by engaging users through interactive dialogue with integrate and tailored solutions that not directly available online (Thirunavukarasu et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib77 ""); Kasneci et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib36 "")).
Unlike conventional search engines that process each query independently—requiring iterative user efforts in providing contextual information and content browsing, LLM chatbots maintain conversation history throughout interactions, Beyond that, they aggregate vast amounts of web-sourced knowledge within their parameters, effectively serving as compact representations of extensive online information (Zhang et al.,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib103 ""); Zeng et al.,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib99 "")).
Through supervised fine-tuning on conversation and instruction datasets (Iyer et al.,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib31 "")), coupled with reinforcement learning from human feedback (RLHF) (Bai et al.,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib8 "")), these models optimize their responses for accuracy, relevance, and alignment with user preferences. Additionally, targeted prompt engineering (Zhou et al.,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib110 "")) and optimization techniques (Li and Liang,, [2021](https://arxiv.org/html/2506.18959v2#bib.bib45 "")), alongside maintaining conversational context (Callison-Burch et al.,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib13 "")), further enhance the coherence and maturity of multi-turn interactions.

However, despite these advantages, relying exclusively on internal LLM knowledge presents notable challenges: (1) hallucinations, where models generate plausible but inaccurate content (Tam et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib76 ""); [Yao et al., 2023a,](https://arxiv.org/html/2506.18959v2#bib.bib95 ""); Zhao et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib105 "")); (2) lack of awareness of recent events, which compromises the timeliness of responses (Chen and Shu,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib14 "")); and (3) Limited context window, hindering a comprehensive understanding of complex queries ( [Wang et al., 2024c,](https://arxiv.org/html/2506.18959v2#bib.bib86 "")). Therefore, integrating external information sources and employing advanced reasoning to verify retrieved data are crucial strategies for addressing these limitations, thus ensuring LLM chatbots deliver accurate, relevant, and up-to-date information (Peng et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib60 "")).

### 2.3 LLMs with RAG

To address the inherent limitations of LLMs mentioned above, particularly their static knowledge and tendency to hallucinations, Retrieval Augmented Generation (RAG) has emerged as a promising paradigm (Prabhune and Berndt,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib62 "")). RAG integrates the generative capabilities of LLMs with retrieval systems to dynamically access relevant external information.
Early implementations of RAG primarily employed a straightforward "Retrieve-then-Read" workflow (Ma et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib51 "")), typically involving a single-step retrieval from a predefined local database or document collection. Although they improve upon purely parametric methods, such naive RAG systems can still struggle with inaccurate retrieval when faced with complex queries.

To solve this problem, multi-hop retrieval addresses the limitations of traditional single-hop retrieval by enabling iterative, sequential searches and reasoning steps across multiple data sources (Jiang et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib34 "")). Multi-hop retrieval incorporates iterative refinement, where intermediate retrieval outcomes guide subsequent queries, progressively building comprehensive context ( [Zhang et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib102 "")). Although multi-hop retrieval has strong power generation capabilities, it also suffers from limitations due to the underlying techniques it employs. Early stage errors in reasoning paths can propagate throughout subsequent retrieval and reasoning steps, severely influencing the final output integrity ( [Zhang et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib102 "")). Additionally, maintaining faithfulness to retrieved evidence poses ongoing difficulties, as language models frequently encounter conflicts between retrieved data and internal parametric knowledge ( [Zheng et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib107 "")).

## 3 Towards Agentic Deep Research

Many complex real-world problems, including open-domain question answering (Yang et al.,, [2015](https://arxiv.org/html/2506.18959v2#bib.bib94 ""); Chen and Yih,, [2020](https://arxiv.org/html/2506.18959v2#bib.bib15 "")) and scientific discovery (Lu et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib49 ""); [Wang et al., 2023b,](https://arxiv.org/html/2506.18959v2#bib.bib84 ""); Baek et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib7 ""); Schmidgall et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib67 "")), inherently require an iterative interplay between information retrieval and reasoning. A single search step often falls short of capturing comprehensive information, while isolated reasoning phases can fail to identify critical insights (Trivedi et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib79 "")). By tightly integrating search and reasoning in a multi-step and interactive manner, these systems can progressively enhance the relevance and depth of retrieved knowledge and simultaneously refine the reasoning process underlying query interpretation, ultimately producing more accurate and contextually nuanced responses.
Here, reasoning actively influences search (e.g., refining search queries based on intermediate deductions), while retrieved information recursively refines reasoning in a dynamic feedback loop. Unlike the previous LLM with RAG framework in Section [2.3](https://arxiv.org/html/2506.18959v2#S2.SS3 "2.3 LLMs with RAG ‣ 2 Traditional Information Search Paradigms ‣ From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents"), where retrieval and reasoning occur in discrete and sequential stages, this approach treats them as interdependent, continuously co-evolving.

This evolution in search methodologies gives rise to a transformative paradigm we define as Agentic Deep Research. In this paradigm, language models takes on the role of active information-seeking agents. Rather than a one-shot prompt + retrieve paradigm, an “agentic” LLM plans a series of steps: it can issue search queries, consult documents, browse on web, or even collaborate with other agents, all while refining its query understanding and response via iterative retrieval and reasoning. Inspired by the way human experts might research a question, we encapsulate this iterative synergy between reasoning and search in the term Deep Research highlighting its dynamic and interactive essence.
To substantiate our central position that LLM-driven Agentic Deep Research will inevitably become the predominant paradigm for future information-seeking—we ground our argument across three interlinked technical dimensions: reasoning capabilities as the foundation, principled approaches to incentivize search, and ecosystem-level momentum evidenced through benchmarks and implementations.

The evolution of reasoning capabilities in large language models represents a crucial stepping stone toward truly agentic systems, particularly in the context of deep research tasks. While Chain-of-Thought (CoT) prompting (Wei et al.,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib89 "")) initially demonstrated the possibility of explicit reasoning processes, the real breakthrough lies in how reasoning mechanisms enable autonomous decision-making and strategic planning, essential for conducting deep research.
The transformation from simple CoT to more sophisticated reasoning frameworks marks a fundamental shift in how AI systems approach complex tasks. Rather than merely following predetermined patterns, modern reasoning frameworks enable systems to dynamically plan, execute, and adjust their approach based on intermediate outcomes.
This capability is particularly evident in recent reinforcement learning-based optimization approaches (Jaech et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib32 ""); Guo et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib24 "")), which have demonstrated unprecedented abilities in managing complex search tasks. These systems can autonomously determine when to initiate searches, formulate appropriate queries, and synthesize findings into coherent understanding, forming the cornerstone of agentic behavior.

The DeepSeek-R1 (Guo et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib24 "")) represents a significant milestone in this evolution, demonstrating how reinforcement learning can optimize reasoning processes for complex mathematical tasks. By learning from experience and feedback, these systems develop sophisticated strategies for information gathering and synthesis, moving beyond simple pattern matching to true strategic planning. This advancement in reasoning capabilities provides the essential foundation for agentic deep research by enabling systems to autonomously evaluate information needs, strategically decompose complex queries, synthesize information across multiple sources while maintaining logical consistency, and adapt search strategies based on intermediate results and feedback (Jin et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib35 "")).
These capabilities, rooted in advanced reasoning mechanisms, establish the preliminary foundation necessary for conducting deep research tasks that require strategic planning, iterative refinement, and complex decision-making. The integration of reinforcement learning with reasoning frameworks represents a crucial step toward truly agentic systems capable of conducting sophisticated research autonomously, marking a significant advancement from traditional search and retrieval paradigms ( [Chen et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib17 "")).

### 3.1 Incentivizing Search with Reasoning Agents

Within this paradigm, reasoning is not merely an auxiliary component applied post-retrieval; rather, it constitutes the core mechanism that determines when, what, and how to search (Wu et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib91 "")). While prompting and supervised fine-tuning (SFT) serve as foundational techniques for instilling tool-use behaviors and basic query generation, they are inherently limited by their reliance on fixed instruction patterns and offline supervision ( [Wang et al., 2023a,](https://arxiv.org/html/2506.18959v2#bib.bib82 ""); Ghosh et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib22 "")). In contrast, reinforcement learning (RL) provides a principled framework for cultivating truly agentic behavior—enabling models to explore, self-correct, and adaptively optimize their retrieval strategies in open-ended, interactive environments (Singh et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib70 ""); Jin et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib35 ""); Song et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib72 "")). This shift toward RL-incentivized search marks a critical step toward developing autonomous agents capable of reasoning-driven information acquisition.

#### Prompting and In-Context Learning: Bridging Search and Reasoning.

Prompting methods have laid important groundwork for coupling reasoning with external information retrieval. ReAct ( [Yao et al., 2023c,](https://arxiv.org/html/2506.18959v2#bib.bib97 "")) and its successors ( [Li et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib43 ""); Alzubi et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib3 "")) introduced paradigms where LLMs alternate between reasoning steps and tool use, guiding models to break problems down and issue relevant search queries mid-process. This enables iterative refinement of reasoning with retrieved evidence, improving factuality and coherence.
Extensions such as Search-o1 ( [Li et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib43 "")) and Open Deep Search (ODS) (Alzubi et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib3 "")) prompt LLMs to actively consult web resources and integrate results into ongoing thought chains. In parallel, methods like Self-Ask (Press et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib63 "")) and IRCoT (Trivedi et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib79 "")) embed search directly within step-by-step reasoning, generating sub-questions and retrieving partial answers in a recursive loop.
These prompting approaches offer flexible templates to scaffold retrieval-enhanced reasoning. However, they rely on fixed prompting logic and do not provide incentives for exploring better search or reasoning paths, limiting their scalability for open-ended or high-stakes tasks.

#### Supervised Fine-Tuning: Hard-Coding Search Patterns.

Supervised fine-tuning (SFT) takes a more structured approach by directly training LLMs on datasets that combine reasoning and retrieval. Toolformer (Schick et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib66 "")) and INTERS (Zhu et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib111 "")) illustrate how models can be trained to learn when and how to query external tools, assess retrieved information, and integrate it logically into final outputs.
SFT data typically comes from two sources: synthetic data generation (e.g., Toolformer (Schick et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib66 "")), RAG-Studio (Mao et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib53 ""))) or instructional reformulation of existing datasets (e.g., INTERS (Zhu et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib111 "")), InstructRetro ( [Wang et al., 2024a,](https://arxiv.org/html/2506.18959v2#bib.bib83 ""))). These enable LLMs to follow structured retrieval-reasoning sequences. However, such methods primarily encode static behaviors learned from data, not dynamic, adaptive behaviors optimized for diverse environments.
While prompting and SFT offer controlled environments for building retrieval-aware reasoning, they impose fixed search patterns and predefined goals. They do not equip agents with the ability to explore the open-ended, uncertain nature of real-world search tasks.

#### Reinforcement Learning: Optimizing Reasoning-Driven Search in the Wild.

Reinforcement learning (RL) fundamentally changes the search paradigm by letting agents learn through trial and error in interactive environments. Instead of being told how to search, RL-trained agents are incentivized (through feedback or reward functions) to discover, refine, and adapt their reasoning and search strategies for specific goals.
Early systems like WebGPT (Nakano et al.,, [2021](https://arxiv.org/html/2506.18959v2#bib.bib57 "")) and RAG-RL ( [Huang et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib28 "")) demonstrated how reward signals (based on human feedback or factual correctness) can guide multi-step retrieval policies that improve response accuracy and trustworthiness. More modular designs like M-RAG ( [Wang et al., 2024d,](https://arxiv.org/html/2506.18959v2#bib.bib87 "")) separate reasoning and retrieval into specialized agents, each trained to collaborate via shared RL objectives.
Recent RL-based systems such as Search-R1 (Jin et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib35 "")), R1-Searcher (Song et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib72 "")), DeepResearcher ( [Zheng et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib106 "")), ZeroSearch ( [Sun et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib74 "")), and WebAgent-R1 [Wei et al., 2025b](https://arxiv.org/html/2506.18959v2#bib.bib90 "") operate in various search environments from static local corpora and open search APIs to real-world web interfaces. These agents learn to decompose complex tasks, plan query sequences, verify evidence, and adjust their strategies based on environment feedback. Such behaviors are difficult to teach through SFT or prompts alone.
Importantly, ReSearch ( [Chen et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib17 "")) and ReARTeR ( [Sun et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib75 "")) go a step further by optimizing not just factual correctness, but also alignment with transparent, interpretable reasoning. ReARTeR introduces a dual-model approach that incentivizes both outcome quality and step-wise explainability, offering a more human-aligned path to trustworthy automation.

### 3.2 Benchmarks and Open-Source Implementations:

https://arxiv.org/html/extracted/6574156/Figures/benchmark.png  
Figure 2: Benchmarks of 5 standard LLMs, 4 reasoning LLMs, and 1 agentic deep research model (OpenAI Deep Research) on BrowseComp, BrowseComp-ZH, and Humanity’s Last Exam.

#### Deep Research Benchmarks

To rigorously compare the capabilities of standard LLMs, reasoning LLMs, and agentic deep research models in realistic and high-stakes scenarios, we adopt and evaluate three representative benchmarks, including BrowseComp ( [Wei et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib88 "")), BrowseComp-ZH (Zhou et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib109 "")), and Humanity’s Last Exam (HLE) (Phan et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib61 "")), each targeting distinct dimensions of agentic deep research. BrowseComp assesses an agent’s ability to conduct multi-step, open-ended web searches to retrieve non-trivial information, while BrowseComp-ZH extends this challenge to the Chinese web, introducing additional linguistic complexity. In contrast, HLE focuses on presenting expert-level questions across diverse academic domains that cannot be solved through naive retrieval alone. These tasks require agents to synthesize evidence from obscure or fragmented sources (e.g., identifying policy changes from regional Chinese documents or resolving historical ambiguities) or to reason through abstract academic problems, where more details can be found in Appendix [A](https://arxiv.org/html/2506.18959v2#A1 "Appendix A Deep ReSearch Benchmarks ‣ From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents"). As shown in Figure 2, standard LLMs perform poorly across these benchmarks—typically below 10% on BrowseComp datasets and under 20% on HLE. In comparison, the OpenAI Deep Research agent achieves significantly higher scores—51.5% on BrowseComp, 42.9% on BrowseComp-ZH, and 26.6% on HLE—demonstrating the effectiveness of reasoning-integrated search in advancing the frontier of intelligent information-seeking systems.

#### Open-Source Implementations

To empirically ground the rising momentum behind Agentic Deep Research, we examine GitHub star trajectories for recent open-source implementations within this paradigm and we provide detailed information in Appendix [B](https://arxiv.org/html/2506.18959v2#A2 "Appendix B Open-Source Deep Research Implementations ‣ From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents"). After excluding the two most-starred repositories (to mitigate skew from viral or legacy projects) and the two least-starred (to reduce statistical noise), we observe a clear upward trajectory across nearly all remaining projects since early 2025. Notably, deep-searcher and deer-flow experienced rapid surges, reaching thousands of stars within weeks. Even smaller-scale efforts, including DeepResearcher and R1-Searcher, display a consistent upward trend, highlighting the breadth of innovation within the agentic search space. These patterns, along with the average Github star trends, indicate not only a technical transition but also a broader cultural and developmental shift: the open-source community is increasingly converging around reasoning-driven, agentic deep research as a leading framework for information seekin. This empirical momentum reinforces our position statement—that Agentic Deep Research LLM-cored Agentic Deep Research framework will inevitable become the dominant paradigm for future information search.

https://arxiv.org/html/extracted/6574156/Figures/star_history.png  
(a)GitHub star trend for open-source repositories.

https://arxiv.org/html/x2.png  
(b)Test-time scaling law for agentic deep research.

Figure 3: (a) Open-source star trend for agentic deep research. (star counts recorded up to 22 May 2025). (b) Test-time scaling (TTS) law for agentic deep research, where data before performance normalization for reasoning TTS is from S1 on AIME24 (Muennighoff et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib56 "")) and for search TTS is from IterDRAG on MuSiQue (Yue et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib98 "")). The TTS is measured in inference tokens.

## 4 Test-Time Scaling Law for Deep Research

Building upon the stated position, we introduce the Test-Time Scaling (TTS) law for Agentic Deep Research, an hypothesis predicting the performance improvements achievable through extended computational resources during inference. Figure [3(b)](https://arxiv.org/html/2506.18959v2#S3.F3.sf2 "In Figure 3 ‣ Open-Source Implementations ‣ 3.2 Benchmarks and Open-Source Implementations: ‣ 3 Towards Agentic Deep Research ‣ From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents") illustrates this hypothesis, normalized performance improve linearly through scaling of internal reasoning depth and external knowledge exploration. Data supporting this observation comes from two representative evaluations: S1 on the AIME24 dataset (Muennighoff et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib56 "")), which tests reasoning-based scaling on advanced multi-step mathematical reasoning problems, and IterDRAG on MuSiQue (Yue et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib98 "")), which focuses on search-based scaling via multi-hop retrieval tasks. As in Figure [3(b)](https://arxiv.org/html/2506.18959v2#S3.F3.sf2 "In Figure 3 ‣ Open-Source Implementations ‣ 3.2 Benchmarks and Open-Source Implementations: ‣ 3 Towards Agentic Deep Research ‣ From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents"), the diagonal plane connecting empirical data points interpolated in the three-dimensional plot represents our hypothetical TTS for Agentic Deep Research. Tasks requiring deeper internal knowledge utilization (reasoning), such as solving complex math problems and logic puzzles, are better aligned with the green plane, whereas tasks demanding extensive external knowledge exploration (search), like medical QA, will align more closely with the red plane. Here, we illustrate the TTS law and trade-offs along the search and reasoning axes.

### 4.1 Reasoning — TTS of Internal Knowledge Utilization

Recent studies have shown that LLMs do more than recall memorized facts or patterns. When given extra computational resource to “think”, they can also perform deeper reasoning steps. This pattern, known as the test-time scaling law for reasoning, indicates that as a model takes more inference steps, including building longer chains of thought ( [Chen et al., 2025c,](https://arxiv.org/html/2506.18959v2#bib.bib18 "")), iterative self-refinement (Madaan et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib52 "")), or self-consistency decoding (Hao et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib26 "")), its accuracy in complex tasks steadily improves.
This phenomenon also suggests that the internal knowledge embedded in LLMs is not fully exposed in a single forward pass. Instead, deeper understanding can be progressively uncovered through extended inference.
In the context of Agentic Deep Research, this highlights a key shift from producing one-shot answers to engaging in active, multi-step reasoning. Instead of relying solely on external retrieval or prompting tricks, the model’s internal knowledge becomes a reusable and expandable resource. This inference-time flexibility is crucial for handling complex, open-ended queries, and positions reasoning as a core axis of scalable capability in LLM-based research agents (Huang et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib29 "")).

### 4.2 Search — TTS of External Knowledge Exploration

In addition to making full use of the internal knowledge of LLMs, exploring abundant external knowledge effectively is another key to achieving TTS in Agentic Deep Research systems. When performing external knowledge search, it is often difficult to obtain all the important information in a single-step retrieval (Shao et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib68 ""); Jiang et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib33 "")). To overcome this bottleneck, consistent with the agentic RAG insights, existing work mainly explores the scaling potential of the search phase through iterative search and long-context RAG. Representatively, many works have explored improving the test-time retrieval performance through iterative RAG/search, which introduces a dynamic and multi-step retrieval to knowledge search via task decomposition (Trivedi et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib79 ""); Asai et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib6 ""); Xiong et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib92 "")). They generally show that iterative multi-step retrieval under a proper number of iterations can also enhance RAG’s performance. Yue et al., ( [2025](https://arxiv.org/html/2506.18959v2#bib.bib98 "")) recently further observed an important experimental phenomenon that under optimal inference parameters, the performance improves nearly linearly with increasing test-time computation.
The gradual expansion of knowledge retrieval from split local text chunks towards an increasingly precise retrieval executed within nearly global external knowledge bases would become a more powerful development trend in the test-time search process.

### 4.3 TTS Trade-offs for Search and Reasoning

Agentic Deep Research systems integrate both search and reasoning, each consuming part of a limited token budget. Under such constraints, a natural trade-off emerges: allocating more tokens to search (e.g., issuing broader or more detailed queries) reduces the capacity available for reasoning (e.g., multi-hop inference or synthesis), and vice versa. This balance is task-dependent. Search-heavy tasks such as multi-hop RAG (Xiong et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib92 ""); Shao et al.,, [2023](https://arxiv.org/html/2506.18959v2#bib.bib68 "")) or literature surveys prioritize broader content access, while reasoning-heavy tasks like causal analysis or math verification (Snell et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib71 "")) require deeper internal processing. Building systems that adaptively allocate token budgets between search and reasoning based on task characteristics is critical for maximizing effectiveness and efficiency in Agentic Deep Research. We anticipate the emergence of a test-time scaling law that governs the optimal balance between search and reasoning under different task conditions. Furthermore, training models that can dynamically allocate and manage budget across these two components is a defining capability of next-generation deep research systems.

## 5 Alternative View and Discussions

#### Retaining Human Primacy in Search

In contrast to the position advanced in this paper that the future of information seeking paradigm is LLM-driven Agentic Deep Research. An alternative viewpoint contends that search should remain fundamentally a human-led activity, with artificial intelligence systems serving primarily as assistive, not autonomous, tools. This counter-position emphasizes that human with primary involvement is indispensable for ensuring trust, interpretability, and epistemic responsibility in open-ended inquiry tasks (Mehrotra et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib54 "")).
First, despite the recent progress in agentic reasoning capabilities, autonomous systems still lack robust models of user intent, contextual nuance, and domain-specific ethics. These elements are often essential in complex or high-stakes search scenarios such as scientific research, legal interpretation, or public policy analysis. Advocates of human-led search argue that delegating the full pipeline (from information retrieval to reasoning and synthesis) to LLM agents risks introducing misaligned conclusions, opaque decision paths, and reduced user oversight.
In addition, from a trust and accountability perspective, human-directed systems afford greater transparency and traceability. While autonomous agents can produce fluent and plausible outputs, they also introduce increased risk of hallucinations, spurious correlations, or unjustified reasoning steps. Maintaining human control over search allows users to apply critical judgment, verify information provenance, and assume responsibility for downstream decisions, a particularly salient concern in regulated or high-risk domains  ( [Zou et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib114 ""); [Zou et al., 2025c,](https://arxiv.org/html/2506.18959v2#bib.bib115 "")).

## 6 Open Problems and Future Opportunities

#### Human-in-Loop and Trustworthy

This suggests that progress in AI search systems should prioritize augmenting human capabilities rather than replacing them. This includes building interfaces that support iterative refinement, expose intermediate reasoning steps, and enable meaningful user feedback. In this framing, AI functions less as an autonomous researcher and more as a powerful assistant embedded within a human-centered workflow (Shneiderman,, [2022](https://arxiv.org/html/2506.18959v2#bib.bib69 "")).
To build trustworthy Deep Research systems, human interactions play an important role. Several important research questions need to be solved.
(1) Search Content Access Control. Implementing fine-grained access control mechanisms ensures that users can only access information appropriate to their roles and permissions. This is particularly important in domains where role-based access to information is essential for privacy, regulatory compliance, or competitive confidentiality.
(2) Human Verification and Feedback Mechanisms. Incorporating human oversight at critical stages of the AI search process can significantly improve the accuracy and reliability of the system ( [Zou et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib114 ""); [Zou et al., 2025c,](https://arxiv.org/html/2506.18959v2#bib.bib115 "")). Designing systems that facilitate user feedback enables continuous learning and adaptation, aligning AI outputs more closely with user expectations (Zhong et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib108 ""); [Zou et al., 2025c,](https://arxiv.org/html/2506.18959v2#bib.bib115 "")) and user-specific requirements ( [Zhang et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib104 "")).

#### In-Domain Expert-Level Deep Research

Deep Research is emerging as the new internet traffic entrance and current Deep Research systems focus on general-purpose domains. However, in highly specialized fields such as medicine, law, and biology, in-domain expert-level deep research is essential to ensure accuracy, relevance, and usability. Domain-specific research poses unique challenges that general-purpose agents cannot meet. We highlight three key research directions:
(1) Domain-Specific Database Construction.
In many fields, data is scattered across fragmented databases with inconsistent coverage and interfaces—e.g., in bioinformatics (Benson et al.,, [2012](https://arxiv.org/html/2506.18959v2#bib.bib9 ""); UniProt Consortium,, [2018](https://arxiv.org/html/2506.18959v2#bib.bib80 ""); Dyer et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib20 "")) or medicine (Knox et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib38 ""); Landrum et al.,, [2018](https://arxiv.org/html/2506.18959v2#bib.bib39 "")). This fragmentation hampers retrieval and reasoning. Future systems must build unified, structured, and queryable domain-specific databases to enable effective deep research.
(2) Domain-Grounded Reasoning.
Reasoning paradigms vary by field: legal reasoning relies on precedent, medical reasoning on diagnostic codes, scientific reasoning on hypothesis testing. Agentic systems must align with these paradigms, adapting their planning and inference mechanisms to domain-specific logic and workflows.

#### Structure-Organized Deep Research Systems

Structured (graph) data, composed of nodes (representing entities) and edges (representing relationships), offers an intuitive and systematic way to represent complex relationships and knowledge associations (Hamilton et al.,, [2017](https://arxiv.org/html/2506.18959v2#bib.bib25 ""); Veličković et al.,, [2018](https://arxiv.org/html/2506.18959v2#bib.bib81 "")). This structured organization can significantly enhance the deep research process in the following ways: (1) Iterative Data Organization: There are many intermediate searching and reasoning contents during agentic retrieval and reasoning. Structuring these iterative contents helps agents maintain coherence and relevance in the long context (Li et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib42 "")). As structured data clarifies knowledge relationships, agents can follow these links effectively when generating answers. This allows them to find relevant content more clearly and avoid contradictions or illogical situations. (2) Multi-Agent Deep Research: Effective task allocation and coordination are essential in multi-agent collaboration. Graph structure helps agents understand task requirements based on their roles and relationships (Zhuge et al.,, [2024](https://arxiv.org/html/2506.18959v2#bib.bib112 ""); [Zhang et al., 2024b,](https://arxiv.org/html/2506.18959v2#bib.bib101 "")).
Further, in multi-agent collaboration, timely and accurate information exchange is vital. Graph data serves as an effective information carrier, allowing agents to structure complex information.
Learning (message passing) from this structured data enhances efficient information sharing among agents based on their relationships.

#### From Textual Space to Multi-Modality

For Agentic Deep Research systems to truly emulate human research capabilities, they must transcend textual limitations and integrate diverse information modalities including images, audio-visual content, and structured data. Different modalities inherently encode distinct knowledge types: text conveys abstract concepts and logical relationships, images provide visual instances and spatial information, while videos capture temporal dynamics and sequential processes. This evolution requires a qualitative cognitive leap in knowledge integration rather than merely expanding input channels. Critical research directions include: (1) Cross-modal Semantic Alignment: deep cross-modal semantic alignment within unified representational spaces that support context-aware reasoning across modalities ( [Li et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib41 "")); (2) Information Fusion and Conflict Resolution: robust information fusion with sophisticated conflict resolution mechanisms when modalities present inconsistent information (Bi et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib10 "")); and (3) Multi-modal Knowledge Acquisition: efficient multi-modal knowledge retrieval and comprehension from heterogeneous, large-scale data repositories (Abootorabi et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib1 "")).

#### Efficient Test-Time Scaling

As Agentic Deep Research systems advance, operational efficiency and cost management become critical scaling determinants. Optimization must target both reasoning and search: (1) Reasoning Efficiency, balancing computational depth against resource utilization through techniques like capability transfer to smaller models or latent reasoning approaches (Sui et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib73 "")). Such efficiency improvements potentially extend beyond mere compression of reasoning chains to manifest as higher-order intelligence through resource self-management( [Li et al., 2025d,](https://arxiv.org/html/2506.18959v2#bib.bib46 "")).
(2) Search Efficiency: Optimizing search beyond naive retrieval requires addressing scalable retrieval from massive heterogeneous sources, efficient long-context processing (Luo et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib50 "")), and iterative search with intelligent query refinement and adaptive stopping criteria (Singh et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib70 "")). Future systems must implement budget-aware strategies that dynamically adjust search workflows.

## 7 Conclusion

This paper has articulated a compelling trajectory from traditional web search paradigms towards the inevitable ascendancy of Agentic Deep Research. By systematically addressing the limitations of prior search engine systems and emphasizing the transformative potential of iterative reasoning and search enabled through advanced reinforcement learning frameworks, we demonstrate that agentic systems significantly outperform traditional models across complex benchmarks. The empirical trends observed in both academic evaluations and open-source implementations reinforce this shift, indicating broad recognition and adoption within different communities. Nevertheless, recognizing legitimate concerns regarding human oversight and transparency, future developments must incorporate hybrid frameworks that optimize both autonomous agentic capabilities and human-in-the-loop interactions. In proposing multiple open challenges and opportunities, we foresee Agentic Deep Research as not only the dominant paradigm but also a profoundly human-centered LLM-driven advancement in knowledge acquisition and synthesis.

## Appendix A Deep ReSearch Benchmarks

#### BrowseComp

( [Wei et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib88 ""))
is a benchmark introduced by OpenAI to evaluate the capabilities of AI agents in conducting complex web searches. Comprising 1,266 challenging questions, it assesses an agent’s ability to persistently navigate the internet to locate hard-to-find, entangled information. Unlike traditional benchmarks that focus on retrieving easily accessible facts, BrowseComp emphasizes tasks where answers are deliberately obscured, requiring agents to demonstrate advanced reasoning, strategic search planning, and adaptability. The benchmark’s design ensures that while answers are difficult to discover, they are straightforward to verify, facilitating reliable evaluation of agent performance. BrowseComp serves as a critical tool for advancing research in developing AI systems capable of sophisticated information retrieval and reasoning across the web.

#### BrowseComp-ZH

(Zhou et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib109 ""))
is a high-difficulty benchmark developed to evaluate the web browsing and reasoning capabilities of large language models (LLMs) within the Chinese information ecosystem. Recognizing that existing benchmarks like BrowseComp focus primarily on English-language contexts, BrowseComp-ZH addresses the unique challenges posed by the Chinese web, including linguistic complexity, fragmented information across diverse platforms, and varying search engine infrastructures.
The benchmark comprises 289 multi-hop questions spanning 11 diverse domains such as film, art, medicine, geography, history, and technology. Each question is meticulously reverse-engineered from a concise, objective, and easily verifiable answer (e.g., a date, number, or proper noun). A two-stage quality control protocol ensures high question difficulty and answer uniqueness. Notably, the questions are designed so that answers are not readily retrievable via standard search engines, requiring models to engage in complex reasoning and information synthesis.

#### Humanity’s Last Exam (HLE)

(Phan et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib61 "")) is a multi-modal benchmark designed to evaluate the reasoning and problem-solving capabilities of large language models (LLMs) across a broad spectrum of academic disciplines. Developed collaboratively by the Center for AI Safety and Scale AI, HLE comprises 3,000 expert-crafted questions spanning mathematics, humanities, natural sciences, and more.
Unlike BrowseComp and BrowseComp-ZH, where agents can locate and answer questions by analyzing information retrieved from the web, HLE presents ’closed-book’ academic challenges (the answers aren’t directly available online) that demand deep reasoning and specialized domain expertise, going well beyond what surface-level online searches can support. Each question in HLE is designed to be unambiguous and verifiable, yet not readily answerable through internet search, thereby testing the intrinsic reasoning abilities of LLMs.

## Appendix B Open-Source Deep Research Implementations

| Name | Base Model | Optimization | Training Data | Evaluation Data | Link |
| --- | --- | --- | --- | --- | --- |
| Agentic Reasoning (Wu et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib91 "")) | N/A | Prompt | N/A | GPQA | [Link](https://github.com/theworldofagents/Agentic-Reasoning "") |
| Search-o1 ( [Li et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib43 "")) | Qwen | Prompt | N/A | GPQA, MATH500, AMC2023, AIME2024, LiveCodeBench, Natural Questions, TriviaQA, HotpotQA, 2Wiki, MuSiQue, Bamboogle | [Link](https://github.com/sunnynexus/Search-o1 "") |
| Open Deep Search (Alzubi et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib3 "")) | DeepSeek, Llama | Prompt | N/A | SimpleQA, FRAME | [Link](https://github.com/sentient-agi/OpenDeepSearch "") |
| Search-R1 (Jin et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib35 "")) | Llama, Qwen | RL | NQ, HotpotQA | NQ, TriviaQA, PopQA, HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle | [Link](https://github.com/PeterGriffinJin/Search-R1 "") |
| DeepResearcher ( [Zheng et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib106 "")) | Qwen | RL | NQ, TQ, HotpotQA, 2WikiMultiHopQA | MuSiQue, Bamboogle, PopQA, NQ, TQ, HotpotQA, 2WikiMultiHopQA | [Link](https://github.com/GAIR-NLP/DeepResearcher "") |
| R1-Searcher (Song et al.,, [2025](https://arxiv.org/html/2506.18959v2#bib.bib72 "")) | Llama, Qwen | RL | HotpotQA, 2WikiMultiHopQA | HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle | [Link](https://github.com/RUCAIBox/R1-Searcher "") |
| ReSearch ( [Chen et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib16 "")) | Qwen | RL | MuSiQue | HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle | [Link](https://github.com/Agent-RL/ReSearch "") |
| ZeroSearch ( [Sun et al., 2025a,](https://arxiv.org/html/2506.18959v2#bib.bib74 "")) | Llama, Qwen | RL | NQ, HotpotQA | NQ, TriviaQA, PopQA, HotpotQA, 2WikiMultiHopQA, MuSiQue, Bamboogle | [Link](https://github.com/Alibaba-NLP/ZeroSearch "") |
| IKEA ( [Huang et al., 2025b,](https://arxiv.org/html/2506.18959v2#bib.bib30 "")) | Qwen | RL | NQ, HotpotQA | NQ, HotpotQA, PopQA, 2Wikimultihopqa | [Link](https://github.com/hzy312/knowledge-r1 "") |
| Webthinker ( [Li et al., 2025c,](https://arxiv.org/html/2506.18959v2#bib.bib44 "")) | Qwen | RL | SuperGPQA, WebWalkerQA, OpenThoughts, NaturalReasoning, NuminaMath | GPQA, GAIA, WebWalkerQA, Humanity’s Last Exam | [Link](https://github.com/RUC-NLPIR/WebThinker "") |
| gpt-researcher | OpenAI Series | Prompt | N/A | N/A | [Link](https://github.com/assafelovic/gpt-researcher "") |
| deep-searcher | DeepSeek, OpenAI Series, Claude, Gemini, Grok, Qwen, Llama, GLM | Prompt | N/A | N/A | [Link](https://github.com/zilliztech/deep-searcher "") |
| nanoDeepResearch | OpenAI Series, Claude | Prompt | N/A | N/A | [Link](https://github.com/liyuan24/nanoDeepResearch "") |
| DeerFlow | OpenAI Series, Qwen | Prompt | N/A | N/A | [Link](https://github.com/bytedance/deer-flow "") |
| deep-research | DeepSeek, OpenAI Series | Prompt | N/A | N/A | [Link](https://github.com/dzhng/deep-research "") |
| open-deep-research | OpenAI Series, DeepSeek, Claude, Gemini | Prompt | N/A | N/A | [Link](https://github.com/btahir/open-deep-research "") |
| r1-reasoning-rag | DeepSeek | Prompt | N/A | N/A | [Link](https://github.com/deansaco/r1-reasoning-rag "") |
| node-DeepResearch | Gemini, OpenAI Series | Prompt | N/A | N/A | [Link](https://github.com/jina-ai/node-DeepResearch "") |
| deep-research | Gemini, OpenAI Series, DeepSeek, Claude, Grok | Prompt | N/A | N/A | [Link](https://github.com/u14app/deep-research "") |

</details>

<details>
<summary>Large Language Models (LLMs) have shown impressive performance on various language processing tasks, but often struggle with complex, multi-step tasks such as travel planning. To address this challenge, extensions like LLM-modulo systems and agentic approaches have been proposed, each with its own strengths and limitations. This paper examines the unique strengths and limitations of these approaches, using the Travel Planner benchmark as a case study. We analyze the results and propose a new hybrid task planner approach to address the challenges of solving multi-step tasks with LLMs, highlighting implications for future research in this area.</summary>

Large Language Models (LLMs) have shown impressive performance on various language processing tasks, but often struggle with complex, multi-step tasks such as travel planning. To address this challenge, extensions like LLM-modulo systems and agentic approaches have been proposed, each with its own strengths and limitations. This paper examines the unique strengths and limitations of these approaches, using the Travel Planner benchmark as a case study. We analyze the results and propose a new hybrid task planner approach to address the challenges of solving multi-step tasks with LLMs, highlighting implications for future research in this area.

Large Language Models (LLMs) have emerged as a powerful tool for solving a variety of complex tasks. Currently, there is a growing interest in applying LLMs towards solving multi-step tasks such as travel planning or mission planning. However, LLMs have frequently shown disappointing results on these multi-step tasks. In benchmarks such as Travel Planner (Xie et al. 2024), even GPT-4 only achieves a $0 . 6 %$ success rate for solving a user request.

To improve the performance of LLMs on multi-step tasks, extensions to LLMs have been proposed such as LLMmodulo systems (Kambhampati et al. 2024b; Gundawar et al. 2024) and other agentic approaches (Yao et al. 2022; Fourney et al. 2024). Many of these approaches couple LLM(s) with external verifiers in order to provide guarantees on their accuracy. In this paper, we explore some of the challenges encountered by these approaches. Using the Travel Planner benchmark, we find that many LLM approaches lack an ability to generate a model of the problem they are solving and are unable to do planning about the solving process. Without explicit human guidance, this deficiency reduces the likelihood that LLM can successfully complete a given multi-step task.

To address this, we propose a new approach that provides additional planning guidance to the LLM. Our approach separates the task into Planning and Acting phases that mirror recent developments in planning (e.g., (Ghallab, Nau, and Traverso 2016)(Ghallab, Nau, and Traverso to appear)1):

• Planning phase: A Hierarchical Task Network planner provides guidance, via a plan, to an LLM that describes what needs to be done. • Acting phase: An agentic LLM operationalizes the plan by determining how to accomplish each action in it.

Together, these approaches limit the kinds of hallucination errors that an LLM typically produces.

We present preliminary results of our new approach showing that it more than doubles the success rate of an agentic LLM system in completing the initial steps of the Travel Planning task. We then provide a detailed analysis of the results and discuss the implications for future research in this area.

LLMs for planning: There is a large debate on whether LLMs are capable of classical planning tasks. There are many papers that directly apply LLMs toward planning tasks with varied success (Silver et al. 2024). There also exist survey papers of LLM-based agents planning that categorizing recent works into Task Decomposition, Plan Selection, External Module, Reflection, and Memory (Huang et al. 2024). On the other hand, there are also many other papers that suggest that LLMs lack the capability to plan (Verma, Bhambri, and Kambhampati 2024; Kambhampati 2024).

Beyond applying LLMs directly to planning, there have also been indirect approaches that couple an LLM with a classical planner in a similar manner to the HaoTP approach (Hao et al. 2024) discussed in this paper. One approach is to have the LLM translate a given planning problem into a PDDL specification and then use a classical planner to generate a solution (Liu et al. 2023). Other than this end-toend approach, LLMs have been applied to many domains to generate various planning representations such as temporal logic (Chen et al. 2023), task decompositions (Zhang et al. 2021), and PDDL (Guan et al. 2023).

Reasoning with LLMs: The advent of ChatGPT-o1 model changes the landscape of LLM reasoning capabilities. (Valmeekam et al. 2024) evaluate the planning capabilities of the o1-preview and o1-mini models on both planning and scheduling benchmarks. The “LLM as a Mastermind” paper (Zhang et al. 2024a) surveys the use of Large Language Models (LLMs) in strategic reasoning, a form of reasoning requiring understanding and predicting adversary actions in multi-agent settings, highlighting scopes, applications, methodologies, and evaluation metrics.

Agentic LLMs: Agentic LLMs are a compound or hybrid system to accomplish tasks. There has been growing interest in incorporating LLMs into agentic workflows. One of the first approaches in this area was the ReAct framework (Yao et al. 2022) where agent reasoning choices are interleaved with action selection in order to interact with external environments. Another paper introduced ExpeL (Zhao et al. 2024), an agent that learns from experiences and natural language to make informed decisions without requiring parametric updates, addressing the challenges of resourceintensive fine-tuning and limited access to state-of-the-art LLMs.

LLM Tool Use: To supplement capabilities in domains where LLMs have poor performance, it is common to allow LLMs to interface with external tools. These tools enhance the LLMs with capabilities that they might otherwise not have (Wang et al. 2024) and there are numerous papers covering various aspects of this field of research (Huang et al. 2024; Li et al. 2024).

LLMs and memory: One way to enhance the performance of language models on domain-specific tasks is known as Retrieval-Augmented Generation (RAG) (Izacard et al. 2023; Lewis et al. 2020). In this approach, the LLM is combined with a non-parametric memory index (e.g. a vector index) and retrieved data is fed back into the LLM context when needed. There are various mechanisms for enhancing LLMs with memory (Zhang et al. 2024b) including the notetaking method described in this paper.

Before we discuss how to solve multi-task problems, we need to describe them generally, and travel planner specifically. A multi-step task differs from a planning problem in classical planning.

In classical planning, a planning problem consists of a description (or model) of the problem, an initial condition of the world, a set of actions that can be used to change the state of the world, and a goal condition. In contrast, in a multi-step task, we assume that the problem description (or model) is not directly given (or fully provided) to the system. Instead, portions of the problem description are located in external databases. A solution to a multi-step task includes actions taken (e.g. API requests) to acquire necessary external data.

In the case of the Travel Planner benchmark, we can formulate a travel planning problem as multi-step task that contains a planning problem. Specifically, the Travel Planner task can be broken up into two model building problems (information gathering and external tool use) followed by a classical planning problem:

1. Information Gathering: The first step of the task is to gather information such as the user request, the constraints that need to be satisfied, and what tools are necessary and how to use them.

https://openreview.net/images/04c7239844d485ab5a81d9b0d513f2a7d1ddb1016fbd5f89cef7fffc329ca32f.jpg

Figure 1: Example JSON translation of an NL request

2. External Tool Use: The second step is to determine what calls to the external tools/APIs are necessary to solve a given user request. We assume that there are a set of external tools that are necessary to interact with to solve the problem (e.g. a flight search tool). The LLM could choose not to obey this step, but then it would be impossible to solve the problem.
3. Planning: After obtaining the data from external tools, the next step of the task is to combine the data into a viable travel plan.

In Xie et al. (2024), GPT4 was shown to achieve a $0 . 6 %$ success rate on the benchmark when applied to the travel planner task as an end-to-end system. In Hao et al. (2024), a success rate of $9 3 . 9 %$ (with limitations on its generalizability) was achieved when the LLM was used to solve the external tool use sub-problem and the $z 3$ library was used to solve the planning sub-problem.

In this paper, we will investigate the challenges of designing an LLM system that can solve a multi-step task. A system designed to solve multi-step tasks should satisfy the following criteria:

1. Generalizability: The system should not require the existence of a pre-built solution.
2. End-to-end: The system should solve both the model building and planning subproblems of a multi-step task.

We will first study the system from Hao et al. (2024), which we will term HaoTP to understand what parts of a multistep task LLMs are currently able to perform. HaoTP does not satisfy the two aforementioned criteria, so following this initial study, we will propose an agentic system designed as an end-to-end solution for multi-step tasks. For our implementations, we will employ Codestral-22b as the LLM.

To start off, we give a brief description of the approach from Hao et al. (2024) with respect to each of the three subproblems in Travel Planner.

1. Information Gathering: The first step of the approach is to take a Natural Language (NL) request and convert the request into a JavaScript Object Notation (JSON) request. An example output of this step can be seen in Fig. 1 which is the output of the system for a travel planning request for a trip from Detroit to San Diego from March 5th to Marth 7th, 2022 on a budget of $$ 3,000$ .

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| m Method |  | Process Step | Implementation |
| Information Gathering | Tool Use | Planning |
|  | End-to-End ReAct | LLM | LLM | LLM | (Xie et al. 2024) |
|  | LLM for constraint models | LLM | Few shot LLM | SMT solver | (Hao et al. 2024) |
| 45 | Agentic LLM system | LLM | LLM via Python | LLM via Python | This paper |
| 6 | Task Planner LLM | Guided | LLM via Python | LLM via Python | ； |

Table 1: LLM approaches and their solutions for Travel Planner subtasks

https://openreview.net/images/e3a53b099b2575d714e4726f4a6481cfb94573ec6dfb6b3d17ae9aab9405825e.jpg

Figure 2: Forward pass LLM system for Travel Planning

2. External Tool Use: The second step of the pipeline (JSON-Steps) involves feeding the JSON request from the previous step back into the LLM and asking for ”steps” or pseudo-code. The prompt for this step includes several examples of the pseudo-code. In this case, the tool use problem is selecting the correct python statements to make calls to the tool APIs.

The third step of the pipeline (Steps-Code) is also part of the tool use task where pseudo-code from the previous step is translated into actual python code that defines a constraint model using the z3 library. Like in the (JSONSteps) part of the pipeline, examples of python code are provided for the LLM to use as few-shot examples.

3. Planning: After the final python code is written, the entire file is executed, which calls an SMT solver (the z3 library) that returns a final solution to the travel planning request.

The pipeline can be seen in Fig. 2 where the LLM is used to generate each of the white boxes in the flow that start from the NL request.

Kambhampati et al. (2024a) found that LLMs are capable of implementing functions for checking the validity of individual constraints. Thus, it may be possible to directly generate the code or the constraints for an SMT solver without relying on prior examples. To test this hypothesis, we attempt to replicate the system from Hao et al. (2024) but without the few shot examples that are provided during the tool use task. For example, instead of an explicit example of the pseudocode we want to generate, we provide an explanation of the coding process as in Fig. 3.

Fig. 4 gives an example where this replication is successful. In the example, a flight time preference for flights that depart before 5PM is added to the original request. We can observe in the generated code that the LLM correctly adds additional constraints so that the chosen flights do not have DepTime after 1700 (5PM). In this case, the LLM is capable of adding simple constraints without any prior code examples. However, while testing this more general approach, we ran into several issues.

Lack of a world model One of the issues we noticed when we implemented this approach is that the LLM often overlooked certain constraints, particularly commonsense spatio-temporal ones that are implicit in the TravelPlanner benchmark. For example, consider a travel plan that involves traveling from city A to city B on day 1 with a flight from $1 0 \\mathrm { A M }$ to 2 PM. In this scenario, the LLM should logically infer that breakfast should take place in city A and dinner in city B. However, this type of spatio-temporal reasoning can be challenging for LLMs, and often they fail to maintain this constraint, even when explicitly instructed to do so.

A valid solution to a spatio-temporal constraint is quite complex compared to the free-form generated constraint in Fig. 4. To properly encode the constraint, it is necessary to calculate a temporal model of where the travel group is during the trip and the LLM is unable to reason that producing this model is necessary.

Higher order (meta) considerations The implementation of a constraint model can have a dramatic impact on the tractability of solving the model. In our experiments, we observed that the LLM does not take this principle into account at all. In Hao et al. (2024), the solution is constructed with backbone code such that for a travel plan with a destination of multiple cities, there is a loop that iterates through possible solution city selections (and will exit if one of these city selections results in a satisfiable problem). However, without this guidance, the LLM will choose to write a brute force constraint model where city assignments are also included as variables to solve for. The resulting model can easily end up being intractable.

Repair looping It is reasonable to assume that the code generated by an LLM does not compile or has runtime issues during the first generation pass (as is the case in most code that humans write). This could be due to a variety of reasons (such as hallucinating function names). We can ask the LLM to fix this issue using an LLM-modulo approach (Kambhampati et al. 2024a) where the code that is generated is then executed and the error message (if any) is then sent as a

The general outline for each section is:

1. Get data from tool if necessary.
2. Create z3 Arrays for necessary data column(s) from tool.
3. Create z3 Int variables to index the data.
4. Add constraints discussed above (there can be other constraints even $\\mathrm { i } +$ local constraint is null).
5. Calculate quantities needed for later sections.

Figure 3: An example of coding process instructions that would be given to an LLM for how to code a solution to the Trave Planning.

# add constraint: no evening flights after 5PM

for i, flight in enumerate(flights\_detroit\_to\_sandiego\['DepTime'\].values): s.add(If(variables\['flight\_index\_0'\] $\\scriptstyle = =$ i，Int(flight.split $( \\because )$ \[e\]) $<$ 17，True))

for i， flight in enumerate(flights\_sandiego\_to\_detroit\['DepTime'\].values): s.add(If(variables\['flight\_index\_2'\] $\\mathbf { \\Psi } = = \\mathbf { \\Psi } \\dot { \\mathbf { 1 } }$ ,Int(flight.split(':')\[0\]) $\\angle <$ 17，True))

Figure 4: An example of free form coding. The LLM is allowed the flexibility to generate arbitrary code to write constraints for unseen requests preferences (in this case for evening flights before 5PM)

https://openreview.net/images/b733d65944a9f54efaaa79f3e43b99eb5d4c139ae7bbdbddea8742ef82368797.jpg

Figure 5: Example LLM-modulo approach for code-repair.

back-prompt to the LLM to fix any code generation issues (see Fig. 5).

This process can be iterated until the code can pass through the code verifier. We have observed that this LLMmodulo approach is capable of fixing small errors and can sometimes address the problem of hallucinating functions. However, this approach does not work all of the time. Occasionally, the LLM will modify an error in generated code into another error and then in the subsequent pass modifying it back into the initial error. This creates a repair loop where the generated code will alternate between two erroneous solutions.

Although one can imagine that simply extending the context of the LLM may solve this issue, there is no reason to assume that the length of the repair loop has any limit. In more complex code, it could be the case that changing code in one location breaks functionality in a different location, and an iterative repair approach could loop through the steps of this cycle endlessly.

To design an end-to-end system to solve a multi-step task, we will investigate agentic LLM approaches.

In this paper, we define agentic LLMs as systems that are designed to interact with external tools (such as Wikipedia or other local databases) and incorporate LLMs as drivers of acting, planning, and/or evaluation; external here references anything that is external to the LLM model. For this section, we will study the capabilities and limitations of the agentic LLM system we developed that is displayed in Fig. 6. In this system, an agent LLM is responsible for giving orders to three other LLMs (coding, code repair, and verifier) in order to solve an overarching task. The agent LLM is prompted with a task specification and a list of actions and asked to choose an action. It is also allowed access to a note file which it can use to store short term memory. The goal of the agent LLM is to build a model of the problem in its short-term memory file and then use this model to instruct the other LLMs/system components to solve the problem. To the best of our knowledge, this is the first investigation into having the LLM determine by itself what to write down in a provided notes file.

https://openreview.net/images/f466fa011233c196bbed98d5be3dfa1f3426f095edc428c1d2bfff153e75fcfe.jpg

Figure 6: Simple agentic LLM approach

For this system, we define the following actions:

1. Read: open and read any of the permissible files (red and yellow boxes in Fig. 6).
2. Write: overwrite the text in any of the write-able files (yellow boxes in Fig. 6)
3. Code: send a coding request for a secondary coding LLM to produce code according to the contents of instructions.txt.
4. Execute: execute the Python script written by the coding LLM to solver.py.
5. Repair: send a request to a code repair LLM to attempt to fix the current working Python script.
6. Verify: send a request to a verifier LLM to check if the solution provided in output.txt is valid.

At each iteration of the agentic system, the agent LLM will respond with one of the above actions which is then processed accordingly by the external environment.

Like with the system from (Hao et al. 2024), we provide a description of how this agentic system solves each part of the Travel Planning problem.

1. Information Gathering: The first step of the approach is to read each of the relevant files in the files provided (e.g. problem specification, tool specification, user request) and summarize their contents in the notes file.
2. External Tool Use: The second step of the approach is to use the information recorded in the notes file and write python code for the tool calls. The LLM then needs to record the output of the tool calls for the subsequent planning step.
3. Planning: The last step is to solve the planning problem. The LLM can attempt to do this by itself (i.e. like in the ReAct approch) or can write a solver that plans over the data obtained from the tool calls in the previous step.

The agentic approach is capable of synthesizing information from multiple documents. An example of this capability can be seen in Fig. 8, where the LLM reads three independent files as its first three actions and subsequently summarizes the important points of these files in its short-term memory file.

The LLM is also capable of writing well-formed instructions for a coding LLM to execute as can be seen in Fig. 7. In the example shown in the figure, the LLM reads the Python source code for the Flights tool and correctly conveys the proper arguments to use the tool to the coding LLM.

While this is certainly a step in the right direction, the agentic LLM is not consistent in producing these results. For example, instead of choosing to record relevant facts about the problem in its short-term memory as in Fig. 8, the LLM could choose to only record a history of its goals. Although this record can be helpful for assisting the LLM in planning its next course of action, it is not helpful for solving the actual problem.

Another limitation is that the agent LLM does not always give the coding LLM enough information to work with. For example, the agent LLM could send an instruction “use the Flights tool to search for flights from Detroit to San Diego” without specifying how exactly to use the tool.

Unknown Unknowns A major recurring theme is that LLMs are unable to determine what information they lack when attempting to perform a task. In the dialogue between the agent LLM and the coding LLM, it is common that the agent LLM does not know that the coding LLM does not know how to use a given tool. Furthermore, it is even difficult to get a coding LLM to determine that it does not have enough information to provide a solution. This is true even if we directly prompt the coding LLM to reject coding requests that do not provide enough information. Instead of rejecting the instruction given by the agent LLM, it is more common for the coding LLM to hallucinate an answer to the instruction such as writing code to call erroneous functions (e.g. calling an erroneous search flights method instead of the correct run method).

We propose that a recurring theme throughout the limitations that we have discussed so far is that LLMs lack what we would term a recipe for solving multi-step problems. Beyond the direct problem of planning a given travel itinerary, we must also consider how the LLM chooses to solve a given problem.

In the hybrid approach from Hao et al. (2024), a major limitation is that the LLMs follow a strict structure for what they are allowed to generate. To support this, significant human effort is required to engineer a structural backbone which can make these two approaches impractical in many situations. In this case the LLM does not have a choice of how to solve the problem. This choice was already provided by the supporting code and prompts.

In our experiments on modifications to HaoTP, there is less of a supporting structure which allows for less human input required as well as greater solution creativity but also increases the likelihood of issues such as constraint blindness. Without knowing the exact steps to take to solve the

Use the Flights class to search for flights from the origin city to the destination city on the departure date.

- The Flights class provides a 'run' method that takes three arguments: origin， destination， and departure\_date
- Use the 'run' method to search for flights based on the traveler's preferences.
- For example, to search for flights from Detroit to San Diego on March 5，2022，use the following code:

  ``` python

  flights $\\mathbf { \\sigma } = \\mathbf { \\sigma }$ Flights()

  results $\\mathbf { \\tau } = \\mathbf { \\tau }$ flights.run("Detroit"，"San Diego"，"2022-03-05")

  -Theresults willbeaDataFramecontaininginformationabouttheflights，suchasflightnumber，price，departuretimearivaltimeand distance.
- If no flights are found, the results will be a message saying so.

  Action number 0: \['Read files/request.txt'\]

  Action number 1:\['Read files/problem\_specification.txt'\]

  Action number 2: \['Read files/tool\_specification.txt'\]

  User Preferences:
- Solo traveller
- Destination: Detroit to San Diego
- Duration:3 days (March 5th to March 7th，2022)
- Budget: $3,000
- Preference: No evening flights departing after 5PM
- Problem specification constraints: - Destination cities should not be repeated - Three restaurants per day (breakfast，lunch，dinner) - All specified cuisine types must be visited - Attraction choices should not be repeated - All specified attraction types must be visited - Accommodation minimum nights constraint - Budget constraint
- Tools available:

be decomposed, $p r e \_ { m }$ is a list of preconditions that specifies whether a method is applicable given a state $s$ and $s u b \_ { m }$ is a (possibly ordered) list of subtasks (primitive or compound). Planning proceeds by using the methods to recursively decompose tasks into smaller and smaller subtasks until primitive tasks are reached.

Using Fig. 10 as our task network, we can look at the method for decomposing choose flights:

• Task name: the task to decompose is choose flights

• Precondition: the preconditions are that the origin, destination(s), and dates of the travel plan are present in the notes.

• Subtasks: understand flights tool, choose departing flight, choose returning flight

In our planning domain, the state of the world consists of the contents of the files in the agentic LLM system (e.g. red and orange boxes Fig. 6). The preconditions and effects consist of arbitrary natural language statements (and their conjunctions, disjunctions, negations, etc.). To determine whether a given effect is satisfied, we will use an LLM verifier LLM evaluate the state of the world (e.g. the system files) with respect to the given effect.

problem, the LLM can miss important constraints such as spatio-temporal consistency.

In the agentic approach, there is the least supporting structure, but in return there is the greatest chance of process derailment. The LLM does not commit to a consistent process for gathering information, storing it, and conveying it. Consequently, it is easy for such systems to get stuck or hallucinate answers that they have not yet obtained sufficient information to provide.

To address the issues, we will combine the agentic LLM approach with a task planning subsystem. Specifically, we will employ a component based on Hierarchical Task Network (HTN) planning.

Formally, we define an HTN planning domain as $( S , A , T , M )$ where $S$ is the possible states of the world, $A$ is a set of primitive tasks, $T$ is a set of compound tasks, and $M$ is a set of decomposition methods that describe how a task can be decomposed into subtasks. Specifically, a method $m \\in M$ is $( t \_ { m } \\in T , p r e \_ { m } , s u b \_ { m } )$ , where $t \_ { m }$ is the task to

A task planning subsystem will contain a repository of recipes (i.e. Hierarchical Task Networks ) that describe how to solve problems. We leverage the two-pronged planning and acting approach of Ghallab, Nau, and Traverso (2016, to appear). The task planner creates a set of descriptive actions of what the LLM needs to do, as shown in Figure 10. At each iteration of the system, the LLM uses these descriptions to decide how to do the action; we use the approach from $\ S 5$ .

The general flow of this subsystem can be seen in Fig. 9. The agent LLM sends a verification request to the verifier LLM, which checks the completion of the current task with respect to the current state of the file system. If the check is successful, the current task is updated and the result of the verification request is sent back to the agent LLM.

For our subsystem we will use a hierarchical task network (HTN) to represent the recipes for how to solve problems. An example of such a task network for the Travel Planner problem can be seen in Fig. 10. The HTN breaks down the overarching planning task into smaller subtasks for the LLM to follow.

https://openreview.net/images/c86ac8b2275e1607dfb86d79089e2be4bd46f931957673465c0093016898e200.jpg

Figure 9: Task planning subsystem

https://openreview.net/images/b0cc3640476c6195890d683735f68be51facfc876bcf6ff00d19c9dd82092d52.jpg

Figure 10: An example task network for the Travel Planner problem

As an example, consider the understand user request task that the LLM needs to accomplish at the start of generating a travel plan. To successfully complete this task, the LLM needs to read the file that has the relevant user request and take notes on any information needed to generate a travel plan. A representation of this task node in JSON format can be seen in Fig. 11.

During the verification request, the verifier LLM is asked whether the information contained in the effect files satisfy the intended effect of the task. In this example, the intended effect of the understand user request task is that the agent LLM’s short term memory file contains information that matches the user request file.

https://openreview.net/images/7e6d47676ca299ff3b98c4296fbe8d086664ffe5f8e89c75d191ba3c94bbac45.jpg

Figure 11: Example of a primitive task node

For this work, we employ an LLM as the primary verifier, but we could also use external verifiers with guarantees for certain subtasks. The primary advantage of this setup is that the task network can guide the LLM towards a consistent process when solving problems.

To study the effectiveness of this additional task network component, we perform a ablation study on a modified version of the Travel Planner task which includes the information gathering step not evaluated in past work. The general task is as follows:

• Direct Prompt Information: The LLM agent is provided information about a list of accessible files and what their overarching goal is (e.g., to generate a travel plan) but none of the specific details of how to accomplish it. • Accessible Information: The LLM can access descriptions and the source code of various tools (e.g., FlightSearch) in the list of accessible files. We emphasize that this information is not provided in the prompt but only in files that the LLM can choose to read. • Metrics: Since it is computationally intensive to generate a full travel plan using an agentic LLM architecture, we limit the maximum number of system steps (where each step is a prompt to the agent LLM for an action to take) to 20. To evaluate the methods, we check whether the LLMs have successfully booked departing and returning flights between the origin and destination(s) in the user request.

To simplify our verification, we use requests from the train set from the Travel Planner benchmark that are coupled with ground truth annotated plans. The results on this limited set can be seen in Fig. 12.

Using the task planner helps avoid a common kind of hallucinations and eliminates the need for repair loops.

For example, the LLM needs a specification of what a tool does in its short term memory before trying to write code for that tool. Adding an explicit task to do this allows the task planner to facilitates such knowledge retrieval (rather than rely on the LLM), which reduces the occurrence of function name hallucinations, such as calling an erroneous search flights method instead of the correct run method. The reduction of these hallucinations in turn reduces the probability that the agentic LLM initializes an infinite repair loop which will prevent it from making further progress.

In our experiments with agentic LLMs, one concerning behavior we noticed was execution of out-of-scope code in Python. To sandbox our agent LLM, we set up the environment that processes agent commands to allow the LLM to only read and write to a pre-specified list of approved files (this list is also given to the LLM). However, we did not limit the corresponding code generation capabilities (to allow for greater problem solving creativity). This lack of limitations led to two critical unseen side effects:

https://openreview.net/images/8db6c8a8bd86e0fba4b96030a5f5fc99ab8bdc4b3d929ba5bb1c9f9c473feb89.jpg

Figure 12: Success rate of LLM, with and without a task planner, on the first steps of solving a task in the travel planner benchmark.

• Attempted code installation: In one instance, our agentic LLM generated code that depended on python libraries that were not installed in the development environment it was running in. Instead of changing the code to some supported library, it attempted to programmatically install the python library within the python script being written.

• File writing bypass: In several instances, in order to save the results from tool calls, the agent LLM will tell the coder LLM to save the retrieved data into a local text file. This file may not necessarily be on the list of approved files.

It is important to emphasize that prompt restrictions are not a sufficient guard against unintended agent behavior. In particular, the prompt for the agent LLM specifically mentions that it only has read/write access to the pre-approved file list and the prompt for the coding LLM includes an instruction to ignore requests to write to any other file.

In conclusion, we have discussed several distinct approaches to utilizing Large Language Models (LLMs) for various tasks. Our findings indicate that while LLMs can be successfully employed as form fillers and code editors (e.g., Hao et al. (2024)), their reliance on an existing codebase limits their applicability to other domains. The use of LLMs for free-form coding offers flexibility in handling user requests without a pre-existing codebase, but this flexibility also introduces challenges. Adjusting the structure of the response addresses some of these issues, but LLMs can still generate erroneous results.

A large number of errors when using an LLM for planning seem to be a failure to incorporate a world model into formulating problem solving process. Some problem solving paths for a given multi-step task are not sufficient or efficient computationally. To address these challenges, we propose an hybrid task planner agentic LLM system that interacts with external information gathering tools to construct a model of the task to be solved. The steps that the LLM takes are guided via planning on a Hierarchical Task Network. The task planning constrains the possible problem solving paths to be more limited thus increasing the likelihood that the LLM can successfully complete the multi-step task. By standardizing these steps and adding intermediate verification, we reduce several common errors such as hallucinating tool types or data that has not yet been seen. We plan to do more work on benchmarking the behavior of these hybrid systems on more domains and with stronger models (beyond Codestral-22b), especially on their ability to prevent error cascading that is frequently present in multi-step tasks.

The task networks in the hybrid task planner system are currently handwritten by a human. This can run into similar issues with portability as the approach from Hao et al. (2024). As mentioned in the related work section, there is a great deal of work for generating planning models such as PDDL from text descriptions using LLMs. It is conceivable that given documentation on the processes to solve multistep problems such as travel planner, an LLM could be used to generate these task networks. To increase the effectiveness this approach, we can borrow techniques from curriculum learning where the LLM can first start off by building task networks for simple tasks before gradually building up to more complex and longer tasks (e.g., growing the task network node by node). There are also alternative approaches such as LLM-based optimization which could be used to optimize over candidate task networks.

$#$ Add constraints: restaurants must be acesible based on arrival times and city list (asume restaurants are open 24/7).

# This constraint is already satisfied as we are searching for restaurants in the city where we arrive.

# If there are additional constraints， please specify them.

Figure A.1: LLM constraint generation error: the top comment line is the pseudo-code input and bottom two comment lines are the LLM’s response.

Sure,theerrorisbecauseyou'retryingtocalltheevaluate'methodnanArithRefobject,whichisnotcorect.Since‘m.evaluate (city\_Q\_index)o)wietuanitefectichadsfanithiceesinsoer，itdestaedirect methodslike‘evaluate'. Instead，you need to get the value by using the ‘eval’ method of the model $\\cdot \_ { m ^ { \\ast } }$ and then get the ‘as\_long^ value from the result.

Here is the modification you need to make:

Replace:

destinations\_for\_flights $\\mathbf { \\Psi } = \\mathbf { \\Psi }$ \[destinations\[m.evaluate(city\_0\_index).as\_long()\],destinations\[m.evaluate(city\_1\_index).as\_long()\],destinatiosm.evaluate(city\_1\_index).as\_long()\],destinations\[m.evaluate(city\_2\_index).as\_long()\]\]

with:

destinations\_for\_flights $\\mathbf { \\lambda } = \\mathbf { \\lambda }$ \[destinations\[m.eval(city\_0\_index).as\_long()\],destinations\[m.eval(city\_1\_index).as\_long()\],destinationsm.eval(city\_1\_index).as\_long()\], destinations\[m.eval(city\_2\_index).as\_long()\]\]

LINE START:86

LINE END:87

Sure,theerorisbecauseyou'retryingtocalltheeval methodonanrithRefbject,whichdoesn'thavethatatribute.Instead,you should use the‘as\_long()’ method to convert the‘Int’object into a python integer.

Replace the line:

``` python

destinations\_for\_flights $\\mathbf { \\Sigma } = \\mathbf { \\Sigma }$ \[destinations\[m.eval(city0\_index).as\_long()\],destinations\[m.eval(city\_1\_index).as\_long()\],destinationsmeal\
\
(city\_1\_index).as\_long()\],destinations\[m.eval(city\_2\_index).as\_long()\]\]

with:

\`python

destinations\_for\_flights $\\mathbf { \\tau } = \\mathbf { \\tau }$ \[destinations\[m.evaluate(city\_index).as\_long()\],destinations\[m.evaluate(city\_1\_index).as\_long()\],destinatiosm\
\
evaluate(city\_1\_index).as\_long()\],destinations\[m.evaluate(city\_2\_index).as\_long()\]\]

Line Start:86

Line End:87

Figure A.2: LLM repair looping error. The LLM corrects the code from m.evaluate (green) to m.eval (yellow) (top) and then on the subsequent editing pass from m.eval (yellow) to m.evaluate (green) (bottom).

I'1lnedtounderstandteuser'stravelpreferences，incdingthecitiestovisitattractions，iningpreferences，andadaion requirements.I\*1l also need to understand the constraints and requirements of the problem specification document.

Ilnedtounderstandthecostraintsandrequirementsoftheproblemspecificationdocuent，aswellastheforatandcapabiitiesofthe tools provided in the tool specification document.

I'll needtounderstandtheformatandcapabilitiesoftheFlightstoolbeforeusingittofindflightsfortheuser'stravelplan. I'lneetouderstandteforatandapabitiesoftheomdtiotolbeforeusingittofidacoodatiosfortheer'stravel plan .

I1l ned tounderstandtheformatandcapabiitiesoftheAtractionstolbeforeusingittofindatractionsfortheuser'stravelplan. I'1l nedtounderstandtheformatandcapabilitiesoftheRestaurantstoolbeforeusingittofindrestaurantsfortheuser'stravelplan. I'lneedtounderstandtheformatandcapabiitiesoftheDistancestolbeforeusingittocalculatedistancesfortheuser'stravelplan.

Figure A.3: LLM generated goal history. Instead of generating a summary of document contents in its short term memory as i Fig. 8, the LLM could instead choose to populate its short term memory with a history of its goals.

You are a coding LLM tasked with following the instructions written to flies/instructions.txt that are given by a leader LLM.The leader LLM does not know what information you need.Do not make any

assumptions on what information you need and ask for more information if you do not have it.For example, if the leader LLM tells you to:

- Use the Flights tool to search for Flights

  Then you should respond with:

  $\\ast \\ast \\ast \_ { \\mathsf { N O T } }$ ENOUGH INFORMATION\*\*\*

  Not enough information provided in files/instructions.txt，please specify import path,method parameters, and method output format.

Figure A.4: Instructions for a coding LLM in the agentic system to reject instructions with insufficient information. We attempt to encourage the coding LLM to reject orders from the leader LLM in cases where it does not have enough information to generate correct code. However, this is not sufficient and the coding LLM can choose to follow the instructions regardless of this constraint.

</details>


## Code Sources

_No code sources found._


## YouTube Video Transcripts

<details>
<summary>[00:00] Please welcome former Director of AI at Tesla, Andrej Karpathy.</summary>

[00:00] Please welcome former Director of AI at Tesla, Andrej Karpathy.

[00:18] Wow, a lot of people here. Hello.

[00:23] Um, okay, yeah, so I'm excited to be here today to talk to you about software in the era of AI.
[00:30] And I'm told that many of you are students, like bachelor's, master's, PhD and so on, and you're about to enter the industry. And I think it's actually like an extremely unique and very interesting time to enter the industry right now. And I think fundamentally the reason for that is that, uh, software is changing again.
[00:48] And I say again because I actually gave this talk already, um, but the problem is that software keeps changing, so I actually have a lot of material to create new talks.
[00:57] And I think it's changing quite fundamentally. I think roughly speaking,
[01:00] software has not changed much on such a fundamental level for 70 years, and then it's changed, I think about twice quite rapidly in the last few years. And so there's just a huge amount of work to do, a huge amount of software to write and rewrite.
[01:12] So let's take a look at maybe the realm of software. So if we kind of think of this as like the map of software, this is a really cool tool called Map of GitHub.
[01:21] Um, this is kind of like all the software that's written. Uh these are instructions to the computer for carrying out tasks in the digital space.
[01:26] So if you zoom in here, these are all different kinds of repositories, and this is all the code that has been written.
[01:31] And a few years ago, I kind of observed that um software was kind of changing and there was kind of like a new new type of software around, and I called this software 2.0 at the time.
[01:41] And the idea here was that software 1.0 is the code you write for the computer. Software 2.0 are basically neural networks, and in particular the weights of a neural network.
[01:52] You're not writing this code directly. You are most you are more kind of like tuning the data sets and then you're running an optimizer to create to create the parameters of this neural net.
[02:01] And I think at the time, neural nets were kind of seen as like just a different kind of classifier, like a decision tree or something like that. And so I think, uh, it was kind of like, um, I I think this framing was a lot more appropriate.
[02:11] And now actually what we have is kind of like an equivalent of GitHub in the realm of software 2.0. And I think the Hugging Face, uh, is basically equivalent of GitHub in software 2.0. And there's also model atlas and you can visualize all the code written there.
[02:24] In case you're curious, by the way, the giant circle, the the point in the middle, uh, these are the parameters of flux, the image generator.
[02:32] And anytime someone tunes a Lora on top of a flux model, you basically create a git commit uh, in this space and uh, you create a different kind of a image generator.
[02:41] So basically what we have is software 1.0 is the computer code that programs a computer.
[02:45] Software 2.0 are the weights, which program neural networks.
[02:50] Uh, and here's an example of AlexNet image recognizer neural network. Now, so far, all of the neural networks that we've been familiar with until recently, were kind of like fixed function computers.
[03:00] Image to uh, categories or something like that. And what's changed, and I think as a quite fundamental change is that neural networks became programmable with large language models.
[03:11] And so I I see this as quite new, unique. It's new kind of a computer and uh so in my mind, it's uh worth giving it a new designation of software 3.0.
[03:20] And basically your prompts are now programs that program the LLM. And uh remarkably, uh, these uh prompts are written in English.
[03:30] So it's kind of like a very interesting programming language. Um, so maybe uh, to, uh, summarize the difference, if you're doing sentiment classification, for example, you can imagine uh, writing some uh, amount of Python to to basically do sentiment classification, or you can train a neural net, or you can prompt a large language model.
[03:48] Uh, so here I'm this is a few shot prompt and you can imagine changing it and programming the computer in a slightly different way.
[03:54] So basically we have software 1.0, software 2.0, and I think we're seeing uh maybe you've seen a lot of GitHub code is not just like code anymore, there's a bunch of like English interspersed with code.
[04:04] And so I think kind of there's a growing category of new kind of code. So not only is it a new programming paradigm, it's also remarkable to me that it's in our native language of English.
[04:14] And so when this blew my mind uh a few, uh, I guess years ago now, uh I tweeted this and um I think it captured the attention of a lot of people and this is my currently pinned tweet.
[04:24] Uh, is that remarkably we're now programming computers in English. Now, when I was at uh Tesla, um, we were working on the uh autopilot and uh we were trying to get the car to drive.
[04:37] And I sort of showed this slide at the time, where you can imagine that the inputs to the car are on the bottom, and they're going through a software stack to produce the steering and acceleration.
[04:47] And I made the observation at the time that there was a ton of C++ code around in the autopilot, which was the software 1.0 code, and then there was some neural nets in there doing image recognition.
[04:57] And uh I kind of observed that over time as we made the autopilot better, basically the neural network grew in capability and size.
[05:04] And in addition to that, all the C++ code was being deleted and kind of like was um, and a lot of the kind of capabilities and functionality that was originally written in 1.0 was migrated to 2.0.
[05:17] So as an example, a lot of the stitching up of information across images from the different cameras and across time was done by a neural network and we were able to delete a lot of code.
[05:27] And so the software 2.0 stack literally ate through the software stack of the autopilot. So I thought this was really remarkable at the time.
[05:36] And I think we're seeing the same thing again where uh basically we have a new kind of software and it's eating through the stack. We have three completely different programming paradigms.
[05:44] And I think if you're entering the industry, it's a very good idea to be fluent in all of them because they all have slight pros and cons and you may want to program some functionality in 1.0 or 2.0 or 3.0.
[05:54] Are you going to train a neural net, are you going to just prompt an LLM? Should this be a piece of code that's explicit, etc. So we'll have to make these decisions and actually potentially, uh, fluidly transition between these paradigms.
[06:05] So, what I wanted to get into now is first, I want to in the first part, talk about LLMs and how to kind of like think of this new paradigm and the ecosystem and what that looks like.
[06:16] Like what are, what is this new computer? What does it look like? And what does the ecosystem look like?
[06:22] Um, I was struck by this quote from Andrew actually, uh many years ago now, I think. And I think Andrew is going to be speaking right after me.
[06:29] Uh, but he said at the time, AI is the new electricity. And I do think that it, um, kind of captures something very interesting in that LLMs certainly feel like they have properties of utilities right now.
[06:41] So, um, LLM labs like OpenAI, Gemini, Anthropics, etc, they spend CAPEX to train the LLMs, and this is kind of equivalent to building out a grid.
[06:51] And then there's OPEX to serve that intelligence over APIs to all of us. And this is done through metered access, where we pay per million tokens or something like that.
[07:01] And we have a lot of demands that are very utility-like demands out of this API. We demand low latency, high uptime, consistent quality, etc.
[07:09] In electricity, you would have a transfer switch, so you can transfer your electricity source from like grid and solar or battery or generator.
[07:16] In LLMs, we have maybe OpenRouter and easily switch between the different types of LLMs that exist. Because the LLMs are software, they don't compete for physical space, so it's okay to have basically like six electricity providers and you can switch between them, right, uh because they don't compete in such a direct way.
[07:31] And I think what's also really fascinating and we saw this in the last few days actually, a lot of the LLMs went down and people were kind of like stuck and unable to work.
[07:41] And I think it's kind of fascinating to me that when the state of the art LLMs go down, it's actually kind of like an intelligence brownout in the world. It's kind of like when the voltage is unreliable in the grid and uh the planet just gets dumber, the more reliance we have on these models, which already is like really dramatic and I think we'll continue to grow.
[08:00] But LLMs don't only have properties of utilities. I think it's also fair to say that they have some properties of fabs. And the reason for this is that the CAPEX required for building LLMs is actually quite large. Uh it's not just like building some uh power station or something like that, right?
[08:16] You're investing a huge amount of money, and I think the tech tree and uh for the technology is growing quite rapidly.
[08:23] So we're in a world where we have sort of deep tech trees, research and development, secrets that are centralizing inside the LLM labs.
[08:32] Uh and I think the analogy muddies a little bit also because as I mentioned, this is software. And software is a bit less defensible because it is so malleable.
[08:41] And so, um I think it's just an interesting kind of thing to think about potentially. There's many analogies you can make like a 4 nanometer process node may be something like a cluster with certain max flops.
[08:52] You can think about when you're when you're using NVIDIA GPUs and you're only doing the software and you're not doing the hardware, that's kind of like the fabless model.
[08:59] But if you're actually also building your own hardware and you're training on CPUs if you're Google, that's kind of like the Intel model where you own your fab.
[09:05] So I think there's some analogies here that make sense. But actually I think the analogy that makes the most sense perhaps is that in my mind, LLMs have very strong, um, kind of analogies to operating systems.
[09:16] Uh, in that this is not just electricity or water. It's not something that comes out of the tap as a commodity. Uh this is these are now increasingly complex software ecosystems.
[09:26] Right? So they're not just like simple commodities like electricity. It's kind of interesting to me that the ecosystem is shaping in a very similar kind of way where you have a few closed source providers like Windows or Mac OS, and then you have an open source alternative like Linux.
[09:41] And I think for uh, neural for LLMs as well, we have a kind of a few competing closed source uh providers, and then maybe the Llama ecosystem is currently like maybe a close approximation to something that may grow into something like Linux.
[09:55] Again, I think it's still very early because these are just simple LLMs, but we're starting to see that these are going to get increasingly complex.
[10:01] It's not just about the LLM itself, it's about all the tool use and the multimodalities and how all of that works. And so when I sort of had this realization a while back, I tried to sketch it out.
[10:10] And it kind of seemed to me like LLMs are kind of like a new operating system, right? So the LLM is a new kind of a computer, it's sitting, it's kind of like the CPU equivalent.
[10:19] Uh, the context windows are kind of like the memory. And then the LLM is orchestrating memory and compute, uh, for problem solving, um, using all of these uh abilities.
[10:31] And so definitely, if you look at it, looks very much like software operating system from that perspective. Um, a few more analogies.
[10:38] For example, if you want to download an app, say I go to VS code and I go to download, you can download VS code and you can run it on Windows, Linux, or Mac.
[10:49] In the same way, as you can take an LLM app like Cursor and you can run it on GPT or Claud or Gemini series, right? It's just a drop down.
[10:58] So it's kind of like similar in that way as well. More analogies that I think strike me is that we're kind of like in this 1960s-ish era where LLM compute is still very expensive for this new kind of a computer.
[11:11] And that forces the LLMs to be centralized in the cloud and we're all just uh sort of thin clients that interact with it over the network.
[11:20] And none of us have full utilization of these computers and therefore, it makes sense to use time sharing where we're all just, you know, a dimension of the batch when they're running the computer in the cloud.
[11:31] And this is very much what computers used to look like at during this time. The operating systems were in the cloud, everything was streamed around, and there was batching.
[11:39] And so the the personal computing revolution hasn't happened yet because it's just not economical, it doesn't make sense, but I think some people are trying.
[11:46] And it turns out that Mac Minis, for example, are a very good fit for some of the LLMs because it's all, if you're doing batch one inference, this is all super memory bound, so this actually works.
[11:57] And uh I think these are some early indications maybe of personal computing V2, but this hasn't happened yet. It's not clear what this looks like. Maybe some of you get to invent what what this is or how it works or what this should what it should be.
[12:11] Maybe one more analogy that I'll mention is whenever I talk to Chat GPT or some LLM directly in text, I feel like I'm talking to an operating system through the terminal.
[12:19] Like it just it's it's text, it's direct access to the operating system, and I think a GUI hasn't yet really been invented in like a general way.
[12:28] Like should ChaPT have a GUI, what different than just the tech bubbles? Uh certainly some of the apps that we're going to get into in a bit have GUI, but there's no like GUI across all the tasks at that makes sense.
[12:42] Uh there are some ways in which LLMs are different from kind of operating systems in some fairly unique way and from early computing. And I wrote about uh, this one particular property that strikes me as very different uh, this time around.
[12:56] It's that LLMs like flip, they flip the direction of technology diffusion that is usually uh, present in technology.
[13:05] So, for example, with electricity, cryptography, computing, flight, internet, GPS, lots of new transformative technologies that have not been around. Typically, it is the governments and corporations that are the first users because it's new and expensive, etc.
[13:18] And it only later diffuses to consumer. Uh but I feel like LLMs are kind of like flipped around. So maybe with early computers, it was all about ballistics and military use, but with LLMs, it's all about how do you boil an egg or something like that.
[13:31] This is certainly like a lot of my use. And so it's really fascinating to me that we have a new magical computer and it's like helping me boil an egg. It's not helping the government do something really crazy like some military ballistics or some special technology.
[13:43] Indeed, corporations and governments are lagging behind the adoption of all of us, of all of these technologies. So it's just backwards, and I think it informs maybe some of the uses of how we want to use this technology or like what are some of the first apps and so on.
[13:56] So, in summary so far, LLM labs fab LLMs. I think it's accurate language to use.
[14:03] But LLMs are complicated operating systems. They're circa 1960s in computing and we're redoing computing all over again.
[14:10] And they're currently available via time sharing, distributed like utility. What is new and unprecedented is that they're not in the hands of a few governments and corporations, they're in the hands of all of us because we all have a computer and it's all just software and ChatGPT was beamed down to our computers like to billions of people like instantly and overnight and this is insane.
[14:28] Uh, and it's kind of insane to me that this is the case. And now it is our time to enter the industry and program these computers. This is crazy. So, I think this is quite remarkable.
[14:39] Before we program LLMs, we have to kind of like spend some time to think about what these things are and I especially like to kind of talk about their psychology.
[14:48] So, the way I like to think about LLMs is that they're kind of like people spirits. Uh they are stochastic simulations of people.
[14:55] Um and the simulator in this case happens to be an autoregressive transformer. So transformer is a neural net. Uh it's and it just kind of like goes on the level of tokens, it goes chunk, chunk, chunk, chunk, chunk.
[15:07] And there's an almost equal amount of compute for every single chunk. Um, and um this simulator of course is is just it's basically there's some weights involved and we fit it to all of text that we have on the internet and so on.
[15:21] And you end up with this kind of a simulator. And because it is trained on humans, it's got this emergent psychology that is human-like.
[15:28] So the first thing you'll notice is of course, uh LLMs have encyclopedic knowledge and memory. Uh and they can remember lots of things, a lot more than any single individual human can because they've read so many things.
[15:39] It's, it actually kind of reminds me of this movie Rain Man, which I actually really recommend people watch, it's an amazing movie. I love this movie.
[15:45] Um, and Dustin Hoffman here is an autistic savant who has almost perfect memory. So he can read a, he can read like a phonebook and remember all of the names and uh phone numbers.
[15:55] And I kind of feel like LLMs are kind of like very similar. They can remember SHA hashes and lots of different things very very easily.
[16:02] So, they certainly have superpowers in some in some respects, but they also have a bunch of, I would say, cognitive uh deficits.
[16:09] So, they hallucinate quite a bit, um, and they kind of make up stuff and don't have a very good uh sort of internal model of self knowledge, or not sufficient at least.
[16:18] And this has gotten better, but not perfect. They display jagged intelligence. So they're going to be superhuman in some problem solving domains, and then they're going to make mistakes that basically no human will make.
[16:27] Like, you know, they will insist that 9.11 is greater than 9.9 or that there are two R's in strawberry. These are some famous examples.
[16:35] But basically, there are rough edges that you can trip on. So that's kind of I think also kind of unique. Uh they also kind of suffer from anterograde amnesia.
[16:44] Um so uh and I think I'm alluding to the fact that if you have a coworker who joins your organization, this coworker will over time learn your organization and uh they will understand and gain like a huge amount of context on the organization.
[16:58] And they go home and they sleep and they consolidate knowledge and they develop expertise over time. LLMs don't natively do this. And this is not something that has really been solved in the R&D of LLMs, I think.
[17:08] Um, and so context windows are really kind of like working memory and you have to sort of program the working memory quite directly because they don't just kind of like get smarter by by default.
[17:16] And I think a lot of people get tripped up by the analogies um, in this way. In popular culture, I recommend people watch these two movies, uh Memento and 50 First Dates.
[17:25] In both of these movies, the protagonists, their weights are fixed and their context window gets wiped every single morning. And it's really problematic to go to work or have relationships when this happens and this happens to all of them all the time.
[17:39] I guess one more thing I would point to is uh security kind of related limitations of the use of LLMs. So for example, LLMs are quite gullible.
[17:46] Uh, they are susceptible to prompt injection risks, they might leak your data, etc. And so um, and there's many other considerations security related. So, so basically long story short, you have to simultaneously think through this superhuman thing that has a bunch of cognitive deficits and issues.
[18:04] How do we and yet, they are extremely like useful. And so how do we program them? And how do we work around their deficits and enjoy their superhuman powers.
[18:16] So what I want to switch to now is talk about the opportunities of how do we use these models and what are some of the biggest opportunities? This is not a comprehensive list, just some of the things that I thought were interesting for this talk.
[18:26] The first thing I'm kind of excited about is what I would call partial autonomy apps. So for example, let's work with the example of coding.
[18:34] You can certainly go to ChatGPT directly and you can start copy pasting code around and copy pasting bug reports and stuff around and getting code and copy pasting everything around.
[18:43] Why would you, why would you do that? Why would you go directly to the operating system? It makes a lot more sense to have an app dedicated for this.
[18:50] And so I think many of you uh use uh Cursor. I do as well. Uh and uh Cursor is kind of like the thing you want instead.
[18:58] You don't want to just directly go to the ChatGPT. And I think Cursor is a very good example of an early LLM app that has a bunch of properties that I think are um useful across all the LLM apps.
[19:08] So in particular, you will notice that we have a traditional interface that allows a human to go in and do all the work manually, just as before.
[19:16] But in addition to that, we now have this LLM integration that allows us to go in bigger chunks. And so some of the properties of LLM apps that I think are shared and useful to point out.
[19:25] Number one, the LLMs basically do a ton of the context management.
[19:31] Uh number two, they orchestrate multiple calls to LLMs, right? So in the case of Cursor, there's under the hood embedding models for all your files, the actual chat models, models that apply diffs to the code, and this is all orchestrated for you.
[19:44] A really big one that uh I think also maybe not fully appreciated always is application specific uh GUI and the importance of it.
[19:52] Um, because you don't just want to talk to the operating system directly in text. Text is very hard to read, interpret, understand, and also like you don't want to take some of these actions natively in text.
[20:03] So, it's much better to just see a diff as like red and green change and you can see what's being added and subtracted.
[20:08] It's much easier to just do command Y to accept or command N to reject. I shouldn't have to type it in text, right? So a GUI allows a human to audit the work of these fallible systems and to go faster.
[20:19] I'm going to come back to this point a little bit later as well. And the last kind of feature I want to point out is that there's what I call the autonomy slider.
[20:27] So for example, in Cursor, you can just do tab completion, you're mostly in charge. You can select a chunk of code and command K to change just that chunk of code.
[20:36] You can do command L to change the entire file, or you can do command I, which just, you know, letter rip do whatever you want in the entire repo.
[20:43] And that's the sort of full autonomy agentic version. And so you are in charge of the autonomy slider, and depending on the complexity of the task at hand, you can uh tune the amount of autonomy that you're willing to give up uh for that task.
[20:57] Maybe to show one more example of a fairly successful LLM app, uh Perplexity. Uh it it also has very similar features to what I've just pointed out in Cursor.
[21:07] Uh it packages up a lot of the information, it orchestrates multiple LLMs, it's got a GUI that allows you to audit some of its work. So, for example, it will, uh, cite sources and you can imagine inspecting them.
[21:18] And it's got an autonomy slider. You can either just do a quick search or you can do research, or you can do deep research and come back 10 minutes later.
[21:24] So this is all just varying levels of autonomy that you give up to the tool. So I guess my question is, I feel like a lot of software will become partially autonomous.
[21:33] And I'm trying to think through like what does that look like? And for many of you who maintain products and services, how are you going to make your products and services partially autonomous?
[21:41] Can an LLM see everything that a human can see? Can an LLM act in all the ways that a human could act? And can humans supervise and stay in the loop of this activity?
[21:50] Because again, these are fallible systems that aren't yet perfect. And what does a diff look like in Photoshop or something like that, you know?
[21:58] And also a lot of the traditional software right now, it has all these switches and all this kind of stuff that's all designed for human. All of this has to change and become accessible to LLMs.
[22:08] So, one thing I want to stress with a lot of these LLM apps that I'm not sure gets uh as much attention as it should is, um we're now kind of like cooperating with AIs.
[22:17] And usually they are doing the generation and we as humans are doing the verification. It is in our interest to make this loop go as fast as possible so we're getting a lot of work done.
[22:27] There are two major ways that I think uh this can be done. Number one, you can speed up verification a lot, and I think GUI, for example, are extremely important to this because a GUI utilizes your computer vision GPU in all of our head.
[22:40] Reading text is effortful and it's not fun, but looking at stuff is fun and it's it's just a kind of like a highway to your brain.
[22:47] So I think GUI are very useful for auditing systems and visual representations in general.
[22:53] And number two, I would say is, we have to keep the AI on the leash. We can't, I think a lot of people are getting way over excited with AI agents.
[23:02] And uh, it's not useful to me to get a diff of 1,000 lines of code to my repo. Like, I have to, I'm still the bottleneck, right? Even though the 1,000 lines come out instantly, I have to make sure that this thing is not introducing bugs.
[23:14] It's just like, and that it's doing the correct thing, right? And that there's no security issues and so on.
[23:19] So, I think that um, yeah, basically, you have to sort of like, it's in our interest to make the the flow of these two go very, very fast.
[23:30] And we have to somehow keep the AI on the leash because it gets way too overreactive. It's uh, it's kind of like this. This is how I feel when I do AI-assisted coding.
[23:38] If I'm just vibe coding, everything is nice and great, but if I'm actually trying to get work done, uh it's not so great to have an overreactive uh agent doing all this kind of stuff.
[23:46] So, this slide is not very good, I'm sorry, but I guess I'm trying to develop like many of you, some ways of utilizing these agents in my coding workflow and to do AI assisted coding.
[23:57] And in my own work, I'm always scared to get way too big diffs. I always go in small incremental chunks. I want to make sure that everything is good.
[24:05] I want to spin this loop very, very fast and uh, I sort of work on small chunks of single concrete thing. Uh and so I think uh many of you are probably developing similar ways of working with the with LLMs.
[24:17] Um, I also saw a number of blog posts that try to develop these best practices for working with LLMs. And here's one that I read recently and I thought was quite good.
[24:26] And it kind of discussed some techniques and some of them have to do with how you keep the AI on the leash. And so as an example, if you are prompting, if your prompt is vague, then uh the AI might not do exactly what you wanted.
[24:38] And in that case, verification will fail. You're going to ask for something else. If verification fails, then you're going to start spinning. So it makes a lot more sense to spend a bit more time to be more concrete in your prompts, which increases the probability of successful verification and you can move forward.
[24:51] And so I think a lot of us are going to end up finding, um, kind of techniques like this. I think in my own work as well, I'm currently interested in uh, what education looks like in um, together with kind of like now that we have AI, uh and LLMs, what does education look like?
[25:05] And I think a a large amount of thought for me goes into how we keep AI on the leash. I don't think it just works to go to ChatGPT and be like, hey, teach me physics.
[25:14] I don't think this works because the AI is like, gets lost in the woods. And so for me, this is actually two separate apps for example.
[25:21] There's an app for a teacher that creates courses, and then there's an app that takes courses and serves them to students.
[25:27] And in both cases, we now have this intermediate artifact of a course that is auditable and we can make sure it's good, we can make sure it's consistent, and the AI is kept on the leash with respect to a certain syllabus, a certain like um, progression of projects, and so on.
[25:41] And so this is one way of keeping the AI on the leash and I think has a much higher likelihood of working. And the AI is not getting lost in the woods.
[25:49] One more kind of analogy I wanted to allude to is I'm not I'm no stranger to partial autonomy and I've kind of worked on this, I think for five years at Tesla.
[25:58] And this is also a partial autonomy product and it shares a lot of the features. Like, for example, right there in the instrument panel is the GUI of the autopilot.
[26:06] So it's showing me what the what the neural network sees and so on. And we have the autonomy slider where over the course of my tenure there, we did more and more autonomous tasks for the user.
[26:17] And maybe the story that I wanted to tell very briefly is, uh, actually the first time I drove a self-driving vehicle was in 2013.
[26:25] And I had a friend who worked at Waymo and uh he offered to give me a drive around Palo Alto. I took this picture using Google Glass at the time.
[26:33] And many of you are so young that you might not even know what that is. Uh but uh, yeah, this was like all the rage at the time.
[26:39] And we got into this car and we went for about a 30-minute drive around Palo Alto, highways, uh streets, and so on. And this drive was perfect. There was zero interventions.
[26:48] And this was in 2013, which is now 12 years ago. And it's kind of struck me because at the time when I had this perfect drive, this perfect demo, I felt like, wow, self-driving is imminent because this just works.
[27:01] This is incredible. Um, but here we are 12 years later and we are still working on autonomy. Um we are still working on driving agents.
[27:08] And even now, we haven't actually like fully solved the problem. Like you may see Waymos going around and they look driverless, but you know, there's still a lot of teleoperation and a lot of human in the loop of a lot of this driving.
[27:20] So we still haven't even like declared success, but I think it's definitely like going to succeed at this point, but it just took a long time.
[27:26] And so I think like like this is software is really tricky, I think in the same way that driving is tricky.
[27:33] And so when I see things like, oh, 2025 is the year of agents, I get very concerned and I kind of feel like, you know, this is the decade of agents.
[27:42] And this is going to be quite some time. We need humans in the loop, we need to do this carefully. This is software. Let's be serious here.
[27:50] One more uh kind of analogy that I always think through is the Iron Man suit. Uh I think this is I always loved Iron Man. I think it's like so um correct in a bunch of ways with respect to technology and how it will play out.
[28:04] And what I love about the Iron Man suit is that it's both an augmentation and Tony Stark can drive it, and it's also an agent.
[28:10] and in some of the movies, the Iron Man suit is quite autonomous and can fly around and find Tony and all this kind of stuff.
[28:15] And so this is the autonomy slider is we can be, we can build augmentations or we can build agents. And we kind of want to do a bit of both, but at this stage, I would say working with fallible LLMs and so on, I would say, you know, it's less Iron Man robots and more Iron Man suits that you want to build.
[28:33] It's less like building flashy demos of autonomous agents and more building partial autonomy products. And these products have custom GUIs and UI/UX, and we're trying to um, and this is done so that the generation verification loop with the human is very, very fast.
[28:47] And we're not losing the sight of the fact that it is in principle possible to automate this work. And there should be an autonomy slider in your product and you should be thinking about how you can slide that autonomy slider and make your product uh sort of um more autonomous over time.
[29:01] But this is kind of how I think there's lots of opportunities in these kinds of products. I want to now switch gears a little bit and talk about one other dimension that I think is very unique.
[29:09] Not only is there a new type of programming language that allows for autonomy in software, but also as I mentioned, it's programmed in English, which is this natural interface.
[29:18] And this is suddenly, everyone is a programmer because everyone speaks natural language like English. So this is extremely bullish and very interesting to me and also completely unprecedented, I would say.
[29:28] It it used to be the case that you need to spend 5 to 10 years studying something to be able to do something in software. This is not the case anymore.
[29:35] So I don't know if by any chance anyone has heard of vibe coding.
[29:41] This is the tweet that kind of like introduced this. But I'm told that this is now like a major meme.
[29:47] Fun story about this is that I've been on Twitter for like 15 years or something like that at this point, and I still have no clue which tweet will become viral and which tweet like fizzles and no one cares.
[29:58] And I thought that this tweet was going to be the ladder. I don't know, it's just like a shower of thoughts, but this became like a total meme and I really just can't tell, but I guess like it struck a chord and it gave a name to something that everyone was feeling but couldn't quite say in words.
[30:13] So now there's a Wikipedia page and everything.
[30:18] So it's like.
[30:24] Yeah, this is like a major contribution now or something like that. So.
[30:31] Uh Tom Wolf from Hugging Face shared this beautiful video that I really love.
[30:42] And I find that this is such a wholesome video. Like I love this video.
[30:46] Like how can you look at this video and feel bad about the future? The future is great.
[30:52] I think this will end up being like a gateway drug to software development.
[30:57] I'm not a doomer about the future of the generation and I think, yeah, I love this video.
[31:04] I tried vibe coding a little bit as well because it's so fun. Uh so vibe coding is so great when you want to build something super duper custom that doesn't appear to exist and you just want to wing it because it's a Saturday or something like that.
[31:14] So, I built this uh iOS app and I don't I can't actually program in Swift, but I was really shocked that I was able to build like a super basic app and I'm not going to explain it, that's really uh dumb.
[31:26] But uh I kind of like this was just like a day of work and this was running on my phone like later that day and I was like, wow, this is amazing.
[31:33] I didn't have to like read through Swift for like five days or something like that to like get started.
[31:37] I also vibe coded this app called MenuGen. And this is live, you can try it in menugen.app. And I basically had this problem where I show up at a restaurant and I read through the menu and I have no idea what any of the things are.
[31:48] And I need pictures. So this doesn't exist, so I was like, hey, I'm going to vibe code it. So, um, this is what it looks like.
[31:55] You go to menugen.app.
[31:59] Um, and uh, you take a picture of a of a menu and then menu gen generates the images.
[32:05] And everyone gets $5 in credits for free when you sign up. And therefore, this is a major cost center in my life. So, this is at negative negative uh revenue app for me right now.
[32:17] I've lost a huge amount of money on MenuGen.
[32:21] Okay. But the fascinating thing about MenuGen for me is that the code of the the vibe coding part, the code was the easiest part of of uh vibe coding menu gen.
[32:33] And most of it actually was when I tried to make it real so that you can actually have authentication and payments and a domain name and a vercel deployment.
[32:41] This was really hard and all of this was not code. All of this DevOps stuff was in me in the browser clicking things.
[32:48] And this was an extreme slog and took another week. So it was really fascinating that I had the MenuGen um basically demo working on my laptop in a few hours, and then it took me a week because I was trying to make it real.
[33:01] And the reason for this is this was just really annoying. Um, so for example, if you try to add Google login to your web page, I know this is very small, but just a huge amount of instructions of this uh Clerk library telling me how to integrate this.
[33:14] And this is crazy, like it's telling me, go to this URL, click on this drop down, choose this, go to this and click on that.
[33:21] And it's like telling me what to do. Like a computer is telling me the actions I should be taking. Like you do it. Why am I doing this?
[33:29] What the hell?
[33:31] I had to follow all these instructions. This was crazy. So I think the last part of my talk, therefore, focuses on, can we just build for agents?
[33:41] I don't want to do this work. Can agents do this? Thank you.
[33:47] Okay. So roughly speaking, I think there's a new category of consumer and manipulator of digital information.
[33:53] It used to be just humans through GUIs or computers through APIs. And now we have a completely new thing.
[33:59] And agents, they're computers, but they are human-like kind of, right? They're people spirits. There's people spirits on the internet and they need to interact with our software infrastructure.
[34:08] Like can we build for them? It's a new thing. So as an example, you can have robots.txt on your domain and you can instruct uh or like advise I suppose, um, web crawlers on how to behave on your website.
[34:19] In the same way you can have maybe LLMs.txt file, which is just a simple markdown that's telling LLMs what this domain is about.
[34:26] And this is very readable to to an LLM. If it had to instead get the HTML of your web page and try to parse it, this is very error prone and difficult and will screw it up and it's not going to work.
[34:36] So we can just directly speak to the LLM. It's worth it.
[34:39] Um a huge amount of documentation is currently written for people. So you will see things like lists and bold and pictures.
[34:46] And this is not directly accessible by an LLM. So I see some of the services now are transitioning a lot of their docs to be specifically for LLMs.
[34:55] So, Vercel and Stripe, as an example, are early movers here. Uh but there are uh a few more that I've seen already.
[35:02] And they offer their documentation in markdown. Markdown is super easy for LLMs to understand. This is great.
[35:10] Maybe one simple example from from uh my experience as well. Maybe some of you know 3Blue1Brown, he makes beautiful animation videos on YouTube.
[35:23] Yeah, I love this library, uh so that he wrote the uh Manim. And I wanted to make my own.
[35:28] And uh there's extensive documentation on how to use Manim, and so I didn't want to actually read through it.
[35:34] So I copy pasted the whole thing to an LLM and I described what I wanted and it just worked out of the box. Like LLM just vibe coded me an animation exactly what I wanted.
[35:42] And I was like, wow, this is amazing. So if we can make docs legible to LLMs, it's going to unlock a huge amount of um kind of use.
[35:50] And um I think this is wonderful and should should happen more. The other thing I wanted to point out is that you do unfortunately have to, it's not just about taking your docs and making them appear in markdown.
[36:01] That's the easy part. You actually have to change the docs because anytime your docs say click, this is bad. An LLM will not be able to natively take this action uh right now.
[36:10] So, Vercel for example is replacing every occurrence of click with the equivalent curl command that your LLM agent could take on your behalf.
[36:18] Um, and so I think this is very interesting. And then of course, there's a model context protocol from Anthropics and this is also another way, it's a protocol of speaking directly to agents as this new consumer and manipulator of digital information.
[36:29] So I'm very bullish on these ideas. The other thing I really like is a number of little tools here and there that are helping ingest data in like very LLM friendly formats.
[36:39] So for example, when I go to a GitHub repo like my Nano GPT repo, I can't feed this to an LLM and ask questions about it, uh because it's, you know, this is a human interface on GitHub.
[36:48] So when you just change the URL from GitHub to Gitingest, then uh this will actually concatenate all the files into a single giant text and it will create a directory structure, etc.
[36:57] And this is ready to be copy pasted into your favorite LLM and you can do stuff.
[37:02] Maybe even more a dramatic example of this is Deepwiki, where it's not just the raw content of these files, uh, this is from Devon, but also like they have Devon basically do analysis of the GitHub repo and Devon basically builds up a whole docs uh pages just for your repo.
[37:18] And you can imagine that this is even more helpful to copy paste into your LLM. So I love all the little tools that basically where you just change the URL and it makes something accessible to an LLM.
[37:27] So this is all well and great and uh, I think there should be a lot more of it.
[37:31] One more note I wanted to make is that it is absolutely possible that in the future, LLMs, it's not even future, this is today, they'll be able to go around and they'll be able to click stuff and so on.
[37:42] But I still think it's very worth uh basically meeting LLM halfway, LLMs halfway and making it easier for them to access all this information.
[37:51] Because this is still fairly expensive, I would say to use and uh a lot more difficult.
[37:56] And so I do think that lots of software, there will be a long tail where it won't uh like adapt because these are not like live player sort of repositories or digital infrastructure.
[38:05] And we will need these tools. Uh but I think for everyone else, I think it's very worth kind of like meeting in some middle point.
[38:11] So I'm bullish on both, if that makes sense.
[38:14] So in summary, what an amazing time to get into the industry. We need to rewrite a ton of code. A ton of code will be written by professionals and vibe coders.
[38:24] These LLMs are kind of like utilities, kind of like fabs, but they're kind of especially like operating systems, but it's so early. It's like 1960s of operating systems.
[38:34] And uh, and I think a lot of the analogies cross over. Um, and these LLMs are kind of like these fallible uh, you know, people spirits that we have to learn to work with.
[38:44] And in order to do that properly, we need to adjust our infrastructure towards it. So when you're building these LLM apps, I described some of the ways of working effectively with these LLMs and some of the tools that make that uh, kind of uh possible, and how you can spin this loop very, very quickly.
[38:58] And basically, uh, create partial autonomy products. And then, um, yeah, a lot of code has to also be written for the agents more directly.
[39:07] But in any case, going back to the Iron Man suit analogy, I think what we'll see over the next decade roughly is we're going to take this slider from left to right.
[39:15] And I'm very interesting, it's going to be very interesting to see what that looks like and I can't wait to build it with all of you.
[39:22] Thank you.
[39:24] Thank you

</details>

<details>
<summary>[00:00] (music) Hey everyone.</summary>

[00:00] (music) Hey everyone.
[00:15] Uh my name is Jerry, co-founder and CEO of LlamaIndex and today we'll be talking about how to build production ready RAG applications.
[00:21] Um, I think there's still time for a raffle for the bucket hat, so if you guys stop by our booth, uh please fill out the Google form.
[00:27] Okay.
[00:28] Let's get started. So, everybody knows that there's been a ton of amazing use cases in GenAI recently.
[00:34] You know, um, knowledge search and QA, conversational agents, uh workflow automation, document processing.
[00:40] These are all things that you can build uh especially using the reason capabilities of LLMs uh over your data.
[00:47] So, if we just do a quick refresher in terms of like paradigms for how do you actually get language models to understand data that hasn't been trained over.
[00:55] There's really like two main paradigms.
[00:58] One is retrieval augmentation where you you like fix the model and you basically create a data pipeline to put context into the prompt from some data source into the input prompt of the language model.
[01:09] Um, so like a vector database, uh you know, like unstructured text, SQL database, etc.
[01:14] The next paradigm here is fine-tuning.
[01:17] How can we bake knowledge into the weights of the network by actually updating the weights of the model itself, some adapter on top of the model, but basically some sort of training process over some new data to actually incorporate knowledge.
[01:30] We'll probably talk a little bit more about retrieval augmentation, but this is just like to help you get uh started and really understand the mission statement of of the company.
[01:39] Okay.
[01:40] Let's talk about RAG, retrieval augmented generation.
[01:44] Um, it's become kind of a buzzword recently, but we'll first walk through the current RAG stack for building a QA system.
[01:51] This really consists of two main components, uh data ingestion as well as data querying, which contains retrieval and synthesis.
[01:58] Uh if you're just getting started in LlamaIndex, you can basically do this in around like five-ish lines of code, uh so you don't really need to think about it.
[02:04] But if you do want to learn some of the lower level components, and I do encourage like every engineer, uh AI engineer to basically just like learn how these components work under the hood.
[02:13] Um I would encourage you to check out some of our docs to really understand how do you actually do data ingestion uh and data querying. Like how do you actually retrieve from a vector database and how do you synthesize that with an LLM.
[02:24] So, that's basically the key stack that's kind of emerging these days like for every sort of like chatbot, like you know, chat over your PDF, like over your unstructured data.
[02:35] Um a lot of these things are basically using the same principles of like how do you actually load data from some data source and actually, you know, um retrieve and query over it.
[02:45] But I think as developers are actually developing these applications, they're realizing that this isn't quite enough.
[02:51] Uh like there's there's certain issues that you're running into that are blockers for actually being able to productionize these applications.
[02:58] And so what are these challenges with naive RAG?
[03:02] One aspect here is just like uh the response and and this is the key thing that we're focused on, like the the response quality is not very good.
[03:08] You run into for instance like bad retrieval issues.
[03:11] Like uh during the retrieval stage from your vector database, if you're not actually returning the relevant chunks from your vector database, you're not going to be able to have the correct context actually put into the LLM.
[03:22] So this includes certain issues like low precision, not all chunks in the retrieved set are relevant.
[03:26] Uh this leads to like hallucination, like loss in the middle problems. You have a lot of fluff in the return response.
[03:32] This could mean low recall. like your top K isn't high enough or basically like the the the set of like information that you need to actually answer the question is just not there.
[03:40] Um and of course there's other issues too, like outdated information.
[03:43] And many of you who are building apps these days might be familiar with some of like key concepts of like why the LLM isn't always, you know, uh guaranteed to give you a correct answer.
[03:52] There's hallucination, irrelevance, like toxicity bias.
[03:55] There's a lot of issues on the LLM side as well.
[03:58] So, what can we do?
[04:01] Um what can we actually do to try to improve the performance of a retrieval augmented generation application?
[04:07] Um and and for many of you like you might be running into certain issues and it really runs the gamut across like the entire pipeline.
[04:14] There's stuff you can do on the data.
[04:16] Like, can we store additional information beyond just like the raw text chunks, right? That that you're putting in the vector database? Can you optimize that data pipeline somehow? Play around with chunk sizes, that type of thing.
[04:26] Can you optimize the embedding representation itself?
[04:29] A lot of times when you're using a pre-trained embedding model, it's not really optimal for giving you the best performance.
[04:35] Um there's the retrieval algorithm.
[04:36] You know, the default thing you do is just look up the top K most similar elements from your vector database to return to the LLM.
[04:44] Um many times that's not enough and and what are kind of like both simple things you can do as well as hard things.
[04:48] Uh and there's also synthesis.
[04:50] Like, uh why is there Yeah, there's like a V in the. Anyways, so so can we use LLMs for more than generation?
[04:55] Um and so basically like you can um use the LLM to actually help you with like reasoning as opposed to just like pure um uh pure uh just like uh just pure generation, right?
[05:06] You can actually use it to try to reason over, given a question, can you break it down into simpler questions, route to different data sources and kind of like uh have uh a more sophisticated way of like querying your data.
[05:18] Um, of course, like if you've kind of been around some of my recent talks, like I always say before you actually try any of these techniques, you need to be pretty task specific and make sure that you need a way to that you actually have a way to measure performance.
[05:31] So, I'll probably spend like two minutes talking about evaluation.
[05:35] Um Simon, my co-founder, just ran a workshop yesterday on really just like how do you evaluate, uh build a data set, evaluate RAG systems and help iterate on that.
[05:43] Uh if you missed the workshop, don't worry.
[05:44] I'll we'll have the slides and and materials uh available online so that you can take a look.
[05:49] Um, at a very high level, in terms of evaluation, it's important because you basically need to define a benchmark for your system to understand how are you going to iterate on and improve it.
[05:58] Uh and there's like a few different ways you can try to do evaluation.
[06:01] I think Anton from from Chroma was was just saying some of this, but like you basically need a way to um evaluate both the end-to-end solution.
[06:09] Like you have your input query as well as the output response.
[06:12] You also want to probably be able to evaluate like specific components.
[06:15] Like if you've diagnosed that the retrieval is is like the portion that needs improving, you need like retrieval metrics to really understand how can you improve your retrieval system.
[06:25] Um so there's retrieval and there's synthesis.
[06:28] Let's talk a little bit, just like 30 seconds on each one.
[06:31] Um evaluation on retrieval, what does this look like?
[06:34] You basically want to make sure that the stuff that's returned actually answers the query and that you're kind of, you know, not returning a bunch of fluff, uh and that the stuff that you're returned is relevant to the question.
[06:46] So, first you need an evaluation dataset.
[06:48] A lot of people uh have like human labeled data sets.
[06:50] If you're in uh building stuff in prod, you might have like user feedback as well.
[06:54] If not, you can synthetically generate a data set.
[06:56] This data set is input like query and output the IDs of like the returned documents are relevant to the query.
[07:03] So you need that somehow.
[07:04] Once you have that, you can measure stuff with ranking metrics, right?
[07:08] You can measure stuff like success rate, hit rate, MRR, NDCG, a variety of these things.
[07:13] And and so like once you are able to evaluate this, like this really isn't uh kind of like an LLM problem.
[07:19] This is like a IR problem. And this has been around for at least like a decade or two.
[07:23] Um but a lot of this is becoming like, you know, it's it's still very relevant in the face of actually building these LLM apps.
[07:31] The next piece here is um there's a retrieve portion, right, but then you generate a response from it.
[07:36] And then how do you actually evaluate the whole thing end to end?
[07:38] So evaluation of the final response uh given the input.
[07:42] You still want to generate some sort of data set.
[07:44] So you could do that through like human annotations, user feedback, you could have like ground truth reference answers given the query that really indicates like, hey, this is the proper answer to this question.
[07:54] Um and you can also just like, you know, synthetically generate it with like GPT-4.
[07:58] Uh you run this through the full RAG pipeline that you built, the retrieval and synthesis, uh and you can run like LLM-based evals.
[08:04] Um so label free evals with label evals, there's a lot of uh projects these days uh going on about how do you actually properly evaluate the outputs, predicted outputs of a language model.
[08:15] Once you've defined your eval benchmark, now you want to think about how do you actually optimize your RAG systems?
[08:21] So, I sent a teaser on this slide uh a few, like yesterday, but the way I think about this is that when you want to actually improve your system, there's like a million things that you can do to try to actually improve your RAG system.
[08:34] Uh and like you probably don't want to start with the hard stuff first, uh just because like, you know, part of the value of language models is how it's kind of democratized access to every developer.
[08:42] It's really just made it easier for people to get up and running.
[08:45] And so if for instance you're running into some performance issues with RAG, I'd probably start with the basics.
[08:50] Like, I call it like table stakes RAG techniques, uh better parsing, um so that you don't just split by even chunks, uh like adjusting your chunk sizes, trying out stuff that's already integrated with the vector database like hybrid search, as well as like metadata filters.
[09:04] There's also like advanced retrieval methods uh that you could try.
[09:07] This is like a little bit more advanced, some of it pulls from like traditional IR, some of it's more like kind of uh really like uh new in in this age of LLM based apps.
[09:16] There's like uh reranking, um that's a traditional concept.
[09:19] There's also concepts in LlamaIndex like recursive retrieval, like dealing with embedded tables, like uh small to big retrieval, and a lot of other stuff that we have that help you potentially improve the performance of your application.
[09:31] Uh and then the last bit, like this kind of gets into more expressive stuff that might be harder to implement, might incur a higher latency and cost, but is potentially more powerful and forward looking, is like agents.
[09:40] Like how do you incorporate agents towards better like RAG pipelines to better answer different types of questions and synthesize information? And how do you actually fine-tune stuff?
[09:50] Let's talk a little bit about the table stakes first.
[09:53] So, chunk sizes. Tuning your chunk size can have outsize impacts on performance, right?
[09:58] Uh if you've kind of like played around with RAG systems, uh this may or may not be obvious to you.
[10:03] What's interesting though is that like more retrieved tokens does not always equate to higher performance and that if you do like reranking of your retrieved tokens, it doesn't necessarily mean that your final generation response is going to be better.
[10:15] And this is again due to stuff like lost in the middle problems where stuff in the middle of the LLM context window tends to get lost whereas stuff at the end uh tends to be a little bit uh uh more well remembered by the LLM.
[10:27] Um and so I think we did a workshop with like Arize a few a week ago where we showed, you know, uh there is kind of like an optimal chunk size given your data set.
[10:35] And a lot of times when you try out stuff like reranking, it actually increases your error metrics.
[10:40] Metadata filtering.
[10:41] Uh this is another like very table stakes thing that I think everybody should look into.
[10:46] And I think vector databases, like, you know, Chroma, Pinecone, Re.AI, like the these uh vector databases are all implementing these uh capabilities under the hood.
[10:54] Metadata filtering is basically just like, how can you add structured context uh to your your chunks, like your text chunks.
[11:01] And you can use this for both like embeddings as well as synthesis, but it also integrates with the metadata, the metadata filter capabilities of a vector database.
[11:09] Um so metadata is just like, again, structured JSON dictionary.
[11:12] It could be like page number, it could be the document title, it could be the summary of adjacent chunks, you can get creative with it too.
[11:17] You could hallucinate like questions uh that the chunk answers.
[11:21] Um, and it can help retrieval, it can help augment your response quality, it also integrates with the vector database filters.
[11:28] As an example, um let's say the question uh is over like the SEC uh like 10Q document and like, can you tell me the risk factors in 2021?
[11:36] If you just do raw semantic search, typically it's very low precision.
[11:39] You're going to return a bunch of stuff that may or may not match this.
[11:42] You might even return stuff from like other years if you have a bunch of documents from different years in the same vector collection.
[11:47] And so like you're kind of like rolling the dice a little bit.
[11:53] But one idea here is basically, you know, if you have access to the metadata of the documents, um and you ask a question like this, you basically combine structured query capabilities by inferring the metadata filters, like a where clause in a SQL statement, like a year equals 2021, and you combine that with semantic search to return the most relevant candidates given your query.
[12:12] And this improves the precision of your uh of your results.
[12:17] Moving on to stuff that's maybe a bit more advanced, like advanced retrieval is one thing that we found generally helps is this idea of like small to big retrieval.
[12:27] Um so what does that mean?
[12:28] Basically, right now, when you embed a big text chunk, you also synthesize over that text chunk.
[12:34] And so it's a little suboptimal because what if like the embedding representations like biased because, you know, there's a bunch of fluff in that text chunk that contains a bunch of irrelevant information, you're not actually optimizing your retrieval quality.
[12:45] So, embedding a big text chunk sometimes feels a little suboptimal.
[12:49] One thing that you could do is basically embed text at the sentence level or on a smaller level, and then expand that window during synthesis time.
[12:56] And so this is contained in a variety of like LlamaIndex abstractions, but the idea is that you return, you retrieve on more granular pieces of information, so smaller chunks.
[13:05] This makes it so that these chunks are more likely to be retrieved when you actually ask a query over these specific pieces of context.
[13:11] But then you want to make sure that the LLM actually has access to more information to actually synthesize a proper result.
[13:18] So this leads to like more precise retrieval, right?
[13:20] So um we we tried this out.
[13:23] It it helps avoid like some lost in the middle problems.
[13:26] You can set a smaller top K value like K equals 2, uh whereas like, uh over this data set, if you set like K equals 5 for naive retrieval over big text chunks, you basically start returning a lot of context and that kind of leads into issues where, uh you know, maybe the relevant context is in the middle but you're not able to find out or or you're like the the LLM is is is not able to kind of uh synthesize over that information.
[13:51] A very related idea here is just like embedding a reference to the parent chunk, um as opposed to the actual text chunk itself.
[13:59] So for instance, if you want to embed like not just the raw text chunk or not the text chunk, but actually like a smaller chunk, um or a summary or questions that answer the chunk, we have found that that actually helps to improve retrieval performance a decent amount.
[14:12] Um and it's it kind of again, goes along with this idea like a lot of times you want to embed something that's more amenable for embedding based retrieval.
[14:19] Uh but then you want to return enough context so that the LLM can actually synthesize over that information.
[14:28] The next piece here is actually kind of even more advanced stuff, right?
[14:33] This goes on into agents and this goes on into that last pillar that I I mentioned, which is how can you use LLMs for for reasoning as opposed to just synthesis.
[14:42] The intuition here is that like for a lot of RAG, if you're just using the LLM at the end, you're one constrained by the quality of your retriever.
[14:49] And you're really only able to do stuff like question answering.
[14:52] And there's certain types of questions or more advanced analysis that you might want to launch that like top-K RAG can't really answer.
[14:58] Like it's not necessarily just a one-off question.
[15:01] You might need to have like an entire sequence of reasoning steps to actually pull together a piece of information or you might want to like summarize a document and compare it with like other documents.
[15:10] So, one kind of architecture we're we're exploring right now is this idea of like multi-document agents.
[15:15] What if like instead of just like RAG, we moved a little bit more into agent territory.
[15:20] We modeled each document not just as a sequence of text chunks, but actually as a set of tools that contains the ability to both like summarize that document as well as to do QA over that document over specific facts.
[15:31] Um and of course if you want to scale to like, you know, hundreds or thousands or millions of documents, um typically an agent can only have access to a limited window of tools.
[15:40] So you probably want to do some sort of retrieval on these tools similar to how you want to retrieve like text chunks from a document.
[15:47] The main difference is that because these are tools, you actually want to act upon them, you want to use them as opposed to just like taking the raw text and plugging it into the context window.
[15:55] So blending this combination of like um embedding based retrieval or any sort of retrieval as well as like agent tool use is a very interesting paradigm that I think is really only possible with this age of LLMs and hasn't really existed uh before this.
[16:13] Another kind of advanced concept is this idea of fine-tuning.
[16:17] Um and so fine-tuning, you know, so some other presenters have talked about this as well, but the idea of like fine-tuning in a RAG system is that it really optimizes specific pieces of this RAG pipeline for you to kind of better um improve the performance of either retrieval or synthesis capabilities.
[16:35] So one thing you can do is fine-tune your embeddings.
[16:37] I think uh Anton was talking about this as well.
[16:39] Like if you just use a pre-trained model, the embedding representations are not going to be optimized over your specific data.
[16:44] So sometimes you're just going to retrieve the wrong, wrong information.
[16:48] Um if you can somehow tune these embeddings so that given any sort of like relevant question that the user might ask that you're actually returning the relevant response, then you're going to have like better performance.
[17:00] So, the idea here, right, is to generate a synthetic query dataset from raw text chunks using LLMs and use this to fine-tune an embedding model.
[17:08] Um and you can do this, like..."
[17:10] Uh if we go back really quick actually, uh you can do this by basically, um kind of fine-tuning the base model itself.
[17:16] You can also fine-tune an adapter on top of the model.
[17:19] And fine-tuning an adapter on top of the model has a few advantages in that it you don't require the base model's weights to actually fine-tune stuff.
[17:26] And if you just fine-tune the query, you don't have to re-index your entire document corpus.
[17:33] There's also fine-tuning LLMs which, of course, like a lot of people are very interested in doing these days.
[17:39] Um an intuition here specifically for RAG is that if you have a weaker LLM, like 3.5 Turbo, like Llama 2 7B, like these weaker LLMs are bad at, are, are not bad at like, um, are, wait, yeah, weaker LLMs are are maybe a little bit worse at like response synthesis, reasoning, structured outputs, etc., um compared to like bigger models.
[17:59] So a solution here is what if you can generate a synthetic dataset using a bigger model like GPT-4, something we're exploring, and you actually distill that into 3.5 Turbo.
[18:08] So it gets better at chain of thought, longer response quality, um better structured outputs, and a lot of other possibilities as well.
[18:15] So, all these things are in our docs.
[18:17] There's production RAG, uh there's fine-tuning and I have two seconds left.
[18:20] So thank you very much.
[18:21] (audience applauding) (music)

</details>

<details>
<summary>[00:00] What most people call agents aren't agents. I've never really liked the term agent. Until I saw this recent article by Anthropic, where I totally agree and now see how we can call something an agent. The vast majority is simply API calls to a language model. This is this. A few lines of code and a prompt. This cannot act independently, make decisions, or do anything. It's simply replies to your users. Still, we call them agents.</summary>

[00:00] What most people call agents aren't agents. I've never really liked the term agent. Until I saw this recent article by Anthropic, where I totally agree and now see how we can call something an agent. The vast majority is simply API calls to a language model. This is this. A few lines of code and a prompt. This cannot act independently, make decisions, or do anything. It's simply replies to your users. Still, we call them agents.

[00:29] But this isn't what we need. We need real agents. But what is a real agent? Before we dive into serious agentic stuff, if you are a student, writer, blogger, or content creator like me, or would like help becoming one, you will love the sponsor of today's video with a clever name, originality.ai.

[00:47] Originality.ai is an awesome tool designed to detect AI generated content, check for plagiarism, grammar, readability, and even fact check your work. Everything you need to publish with integrity. Simply upload a document. In seconds, it flags any AI generated text, highlights plagiarism, and even checks grammar and readability with many useful tips and suggestions. I really love this feature. It also offers fact checking, ensuring every claim in your content stands up to scrutiny. Pretty cool when you work on important or technical work.

[01:19] All based on the most state-of-the-art language models and systems. Try originality.ai today with the first link in the description. So let's start over. We have an LLM accessed programmatically, which is through an API or accessed locally in your own server or machine. And then what? Well, we need it to take action or do something more than just generate text. How? By giving it access to tools and their documentation. We give them access to a tool like the ability to execute SQL queries in a database to access private knowledge. Specifically, we code all that ourselves to have our LLM generate SQL queries.

[02:00] And then our code will send and execute the query automatically in our database. We then send back the outputs so that it uses them to answer the user. This is what another great proportion of people call agents. They are still not agents. This is simply a process hardcoded or with small variations like routers that we discuss in the course. Of course, it's useful and it's super powerful. Yet, it's not an intelligent being or something independent. It's not an agent acting on our behalf. It's simply a program we made and control, or as Anthropic calls it, a workflow.

[02:36] Don't get me wrong. A workflow is pretty damn useful and it can be quite complex and advanced. We can implement intelligent routers to decide what tool to use and when to give it access to various databases. Have it decide which one to query and when. Have it execute tasks through action tools, through code, and more. Plus, you can have as many workflows as you wish.

[02:58] Yet, I simply want to state how different it is than a real agent. The type of agent we dream of and the type Ilya mentioned at a recent talk I attended at NeurIPS.

[03:08] So right now we have our incredible language models and the unbelievable chatbots and they can even do things, but they're also kind of strangely unreliable and they get confused when while also having dramatically superhuman performance on evals. So it's really unclear how to reconcile this. But eventually, sooner or later, the following will be achieved. Those systems are actually going to be agentic in a real ways, whereas right now the systems are not agents in any meaningful sense. Just very that might be too strong. They're very, very slightly agentic, just beginning.

[03:46] The next natural question might be, what exactly is a real agent? In simple terms, a real agent is something that functions independently. More specifically, it's something capable of employing processes like our system two thinking, able to genuinely reason, reflect, and recognize when it lacks knowledge. This is almost the opposite of our system one thinking, which is fast, automatic, and based purely on patterns and learned responses, like reflexes when you need to catch a dropping glass.

[04:16] By contrast, system two thinking might involve deciding whether to prevent the glass from falling in the first place, perhaps by using a nearby tool like a tray or moving the fragile object out of the way. A real agent then will not only know how to use tools, but also decide when and why to use them based on deliberate reasoning. OpenAI's new o1 and o3 series exemplify this shift, as they begin exploring system two-like approaches and try to make models reason by first discussing with themselves internally, mimicking a human-like approach to reasoning before speaking.

[04:52] Unlike traditional language models that rely on next-word or next-token prediction, essentially a system-one, instant thinking mechanism, purely based on what it knows and learned to guess the next instant thing to go with no plan, these new models aim to incorporate deeper reasoning capabilities, making a move toward the deliberate, reflective thinking associated with system two. Something required for a true agent to be.

[05:20] But we are diverging a bit too much with this Kahneman parenthesis. Let me clarify what I mean by a real agent by going back to workflows and what they really are. Workflows follow specific code lines and integrations and, other than the LLM's outputs, are pretty predictable. They are responsible for most of the advanced applications you see and use today, and for a reason. They are consistent, more predictable, and incredibly powerful when leveraged properly. As Anthropic wrote, "Workflows are systems where LLMs and tools are orchestrated through predefined code paths."

[05:55] Here's what a workflow looks like. We have our LLM, some tools or memory to retrieve for additional context, iterate a bit with multiple calls to the LLM, and then an output sent back to the user. As we discussed, when a system needs to sometimes do a task and sometimes another, depending on conditions, workflows can use a router with various conditions to select the right tool or the right prompt to use. They can even work in parallel to be more efficient.

[06:22] Better, we can have some sort of main model, which we refer to as an orchestrator, that selects all the different fellow models to call for specific tasks and synthesize the results, such as our SQL example, where we'd have the main orchestrator getting the user query and could decide if it needs to query a dataset or not. And if it does, ask the SQL agent to generate the SQL query and query the dataset and get it back and synthesize the final answer thanks to all the information provided. This is a workflow.

[06:54] Just like ChatGPT is a workflow, sometimes using canvas and sometimes just straight up answering your question. Even if complex and advanced, it is still all hardcoded.

[07:06] If you know what you need your system to do, you need a workflow. However advanced it may be. For instance, what CrewAI calls agents function like predefined workflows assigned to specific tasks. While Anthropic envisions an agent as a single system capable of reasoning through any task independently. Both approaches have merit. One is predictable and intuitive, while the other aims for flexibility and adaptability. However, the latter is far harder to achieve with current models and better fits an agent definition to me.

[07:39] So about those real agents. Agents are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks themselves. This is what Anthropic wrote, and it is what I agree the most with. Real agents make a plan by exchanging with you and understanding your needs, iterating at a reasoning level to decide on the steps to take to solve the problem or query. Ideally, it will even ask you if it needs more information or clarification instead of hallucinating as with current LLMs.

[08:14] Still, they cannot be simply built. They require a very powerful LLM, better than those we have now, and an environment to evolve in, like a discussion with you and some extra powers like tools that they can use themselves whenever they see fit and iterate. In short, you can see agents almost as replacing someone or a role, and a workflow replacing a task one would do. There is no hardcoded path. The agentic system will make its decisions. They are much more advanced and complex things that we still haven't built very successfully yet.

[08:49] This independence and trust in your system obviously makes it more susceptible of failures, more expensive to run and use, add latency, and worst of all, the results aren't that exciting now. When they are, they are completely inconsistent. So what is an actual good example of an agent?

[09:06] Two examples that quickly come to my mind are Devin's and Anthropic's computer use. Yet, they are for now disappointing agents. If you're curious about Devin, there's a really good blog from Hamel Husain sharing his experience using it. Devin offers an intriguing glimpse into the promise and challenges of agent-based systems. It's designed as a fully autonomous software engineer with its own computing environment and independently handles tasks like API integrations and real-time problem solving.

[09:37] However, as Hamel's extensive testing demonstrated, while Devin excelled at simpler, well-defined tasks, things that we can usually do quite easily, it struggled with complex or autonomous ones, often providing over-complicated solutions and pursuing unfeasible paths, whereas advanced workflows like Cursor don't have as many issues.

[09:58] These limitations reflect the broader challenges of building reliable, context-aware agents with current LLMs, even if you raise millions and millions. Here, Devin aligns more with Anthropic's vision, showcasing the promise and challenges of a reasoning agent. It can autonomously tackle complex problems but struggle with inconsistency. By contrast, workflows like those inspired by CrewAI are simpler and more robust for specific tasks, but lack the flexibility of true reasoning systems. Similarly, we have Anthropic's ambitious attempt at creating an autonomous agent having access to our computer, Anthropic computer use, which had lots of hype when it first came out and has since been quite forgotten.

[10:35] The system was undeniably complex and embodied the characteristics of a true agent: autonomous decision-making, dynamic tool usage, and the ability to interact with its environment. Its goal was also to replace anyone on a computer. Quite promising, or scary. Still, its decline also serves as a reminder of the challenges in creating practical agentic systems that not only work as intended, but do so systematically.

[11:09] In short, LLMs are simply not ready yet for becoming true agents, but it may be the case soon. For now, as with all things code related, we should always aim to find a solution to our problem that is as simple as possible. One that we can iterate easily and debug easily. Simple LLM calls are often the way to go. And it is often what people and companies sell as being an agent, but you won't be fooled anymore.

[11:36] You may want to complement LLMs with some external knowledge through the use of retrieval systems or light fine-tuning, but your money and time aiming for true agents should be saved for really complex problems that cannot be solved otherwise.

[11:51] I hope this video helped you understand the difference between workflows and a real agent and when to use both. If you found it useful, please share it with a friend in the AI community and don't forget to subscribe for more in-depth AI content. Thank you for watching.

[12:07] X @whats_ai. Let me know what you think in the comments! www.louisbouchard.ai

</details>


## Additional Sources Scraped

<details>
<summary>a-developer-s-guide-to-building-scalable-ai-workflows-vs-age</summary>

# A Developer’s Guide to Building Scalable AI: Workflows vs Agents

Understanding the architectural trade-offs between autonomous agents and orchestrated workflows — because someone needs to make this decision, and it might as well be you

https://towardsdatascience.com/wp-content/uploads/2025/06/agent-vs-workflow.jpegImage by author

There was a time not long ago — okay, like three months ago — when I fell deep into the agent rabbit hole.

I had just started experimenting with CrewAI and LangGraph, and it felt like I’d unlocked a whole new dimension of building. Suddenly, I didn’t just have tools and pipelines — I had _crews_. I could spin up agents that could reason, plan, talk to tools, and talk to each other. Multi-agent systems! Agents that summon other agents! I was practically architecting the AI version of a startup team.

Every use case became a candidate for a crew. Meeting prep? Crew. Slide generation? Crew. Lab report review? Crew.

It was exciting — until it wasn’t.

The more I built, the more I ran into questions I hadn’t thought through: _How do I monitor this? How do I debug a loop where the agent just keeps “thinking”? What happens when something breaks? Can anyone else even maintain this with me?_

That’s when I realized I had skipped a crucial question: _Did this really need to be agentic?_ Or was I just excited to use the shiny new thing?

Since then, I’ve become a lot more cautious — and a lot more practical. Because there’s a big difference (according to [Anthropic](https://www.anthropic.com/engineering/building-effective-agents)) between:

- A **workflow**: a structured LLM pipeline with clear control flow, where you define the steps — use a tool, retrieve context, call the model, handle the output.
- And an **agent**: an autonomous system where the LLM decides what to do next, which tools to use, and when it’s “done.”

Workflows are more like you calling the shots and the LLM following your lead. Agents are more like hiring a brilliant, slightly chaotic intern who figures things out on their own — sometimes beautifully, sometimes in terrifyingly expensive ways.

This article is for anyone who’s ever felt that same temptation to build a multi-agent empire before thinking through what it takes to maintain it. It’s not a warning, it’s a reality check — and a field guide. Because there _are_ times when agents are exactly what you need. But most of the time? You just need a solid workflow.

* * *

## The State of AI Agents: Everyone’s Doing It, Nobody Knows Why

You’ve probably seen the stats. [95% of companies are now using generative AI, with 79% specifically implementing AI agents](https://www.bain.com/insights/survey-generative-ai-uptake-is-unprecedented-despite-roadblocks/), according to Bain’s 2024 survey. That sounds impressive — until you look a little closer and find out only _1%_ of them consider those implementations “mature.”

Translation: most teams are duct-taping something together and hoping it doesn’t explode in production.

I say this with love — I was one of them.

There’s this moment when you first build an agent system that works — even a small one — and it _feels like magic_. The LLM decides what to do, picks tools, loops through steps, and comes back with an answer like it just went on a mini journey. You think: “Why would I ever write rigid pipelines again when I can just let the model figure it out?”

And then the complexity creeps in.

You go from a clean pipeline to a network of tool-wielding LLMs reasoning in circles. You start writing logic to correct the logic of the agent. You build an agent to supervise the other agents. Before you know it, you’re maintaining a distributed system of interns with anxiety and no sense of cost.

Yes, there are real success stories. [Klarna’s agent handles the workload of 700 customer service reps](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/). [BCG built a multi-agent design system that cut shipbuilding engineering time by nearly half.](https://www.bcg.com/publications/2025/how-ai-can-be-the-new-all-star-on-your-team) These are not demos — these are production systems, saving companies real time and money.

But those companies didn’t get there by accident. Behind the scenes, they invested in infrastructure, observability, fallback systems, budget controls, and teams who could debug prompt chains at 3 AM without crying.

For most of us? We’re not Klarna. We’re trying to get something working that’s reliable, cost-effective, and doesn’t eat up 20x more tokens than a well-structured pipeline.

So yes, agents _can_ be amazing. But we have to stop pretending they’re a default. Just because the model _can_ decide what to do next doesn’t mean it _should_. Just because the flow is dynamic doesn’t mean the system is smart. And just because everyone’s doing it doesn’t mean you need to follow.

Sometimes, using an agent is like replacing a microwave with a sous chef — more flexible, but also more expensive, harder to manage, and occasionally makes decisions you didn’t ask for.

Let’s figure out when it actually makes sense to go that route — and when you should just stick with something that works.

## Technical Reality Check: What You’re Actually Choosing Between

Before we dive into the existential crisis of choosing between agents and workflows, let’s get our definitions straight. Because in typical tech fashion, everyone uses these terms to mean slightly different things.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-115.pngimage by author

### Workflows: The Reliable Friend Who Shows Up On Time

Workflows are orchestrated. You write the logic: maybe retrieve context with a vector store, call a toolchain, then use the LLM to summarize the results. Each step is explicit. It’s like a recipe. If it breaks, you know exactly where it happened — and probably how to fix it.

This is what most “RAG pipelines” or prompt chains are. Controlled. Testable. Cost-predictable.

The beauty? You can debug them the same way you debug any other software. Stack traces, logs, fallback logic. If the vector search fails, you catch it. If the model response is weird, you reroute it.

Workflows are your dependable friend who shows up on time, sticks to the plan, and doesn’t start rewriting your entire database schema because it felt “inefficient.”

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-112.pngImage by author, inspired by [Anthropic](https://www.anthropic.com/engineering/building-effective-agents)

In this example of a simple customer support task, this workflow always follows the same classify → route → respond → log pattern. It’s predictable, debuggable, and performs consistently.

```python
def customer_support_workflow(customer_message, customer_id):
    """Predefined workflow with explicit control flow"""

    # Step 1: Classify the message type
    classification_prompt = f"Classify this message: {customer_message}\nOptions: billing, technical, general"
    message_type = llm_call(classification_prompt)

    # Step 2: Route based on classification (explicit paths)
    if message_type == "billing":
        # Get customer billing info
        billing_data = get_customer_billing(customer_id)
        response_prompt = f"Answer this billing question: {customer_message}\nBilling data: {billing_data}"

    elif message_type == "technical":
        # Get product info
        product_data = get_product_info(customer_id)
        response_prompt = f"Answer this technical question: {customer_message}\nProduct info: {product_data}"

    else:  # general
        response_prompt = f"Provide a helpful general response to: {customer_message}"

    # Step 3: Generate response
    response = llm_call(response_prompt)

    # Step 4: Log interaction (explicit)
    log_interaction(customer_id, message_type, response)

    return response
```

The deterministic approach provides:

- **Predictable execution**: Input A always leads to Process B, then Result C
- **Explicit error handling**: “If this breaks, do that specific thing”
- **Transparent debugging**: You can literally trace through the code to find problems
- **Resource optimization**: You know exactly how much everything will cost

[Workflow implementations deliver consistent business value](https://ascendix.com/blog/salesforce-success-stories/): OneUnited Bank achieved 89% credit card conversion rates, while Sequoia Financial Group saved 700 hours annually per user. Not as sexy as “autonomous AI,” but your operations team will love you.

### Agents: The Smart Kid Who Sometimes Goes Rogue

Agents, on the other hand, are built around loops. The LLM gets a goal and starts reasoning about how to achieve it. It picks tools, takes actions, evaluates outcomes, and decides what to do next — all inside a recursive decision-making loop.

This is where things get… fun.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-111.pngImage by author, inspired by [Anthropic](https://www.anthropic.com/engineering/building-effective-agents)

The architecture enables some genuinely impressive capabilities:

- **Dynamic tool selection**: “Should I query the database or call the API? Let me think…”
- **Adaptive reasoning**: Learning from mistakes within the same conversation
- **Self-correction**: “That didn’t work, let me try a different approach”
- **Complex state management**: Keeping track of what happened three steps ago

In the same example, the agent might decide to search the knowledge base first, then get billing info, then ask clarifying questions — all based on its interpretation of the customer’s needs. The execution path varies depending on what the agent discovers during its reasoning process:

```python
def customer_support_agent(customer_message, customer_id):
    """Agent with dynamic tool selection and reasoning"""

    # Available tools for the agent
    tools = {
        "get_billing_info": lambda: get_customer_billing(customer_id),
        "get_product_info": lambda: get_product_info(customer_id),
        "search_knowledge_base": lambda query: search_kb(query),
        "escalate_to_human": lambda: create_escalation(customer_id),
    }

    # Agent prompt with tool descriptions
    agent_prompt = f"""
    You are a customer support agent. Help with this message: "{customer_message}"

    Available tools: {list(tools.keys())}

    Think step by step:
    1. What type of question is this?
    2. What information do I need?
    3. Which tools should I use and in what order?
    4. How should I respond?

    Use tools dynamically based on what you discover.
    """

    # Agent decides what to do (dynamic reasoning)
    agent_response = llm_agent_call(agent_prompt, tools)

    return agent_response
```

Yes, that autonomy is what makes agents powerful. It’s also what makes them hard to control.

Your agent might:

- decide to try a new strategy mid-way
- forget what it already tried
- or call a tool 15 times in a row trying to “figure things out”

You can’t just set a breakpoint and inspect the stack. The “stack” is inside the model’s context window, and the “variables” are fuzzy thoughts shaped by your prompts.

When something goes wrong — and it will — you don’t get a nice red error message. You get a token bill that looks like someone mistyped a loop condition and summoned the OpenAI API 600 times. (I know, because I did this at least once where I forgot to cap the loop, and the agent just kept thinking… and thinking… until the entire system crashed with an “out of token” error).

* * *

To put it in simpler terms, you can think of it like this:

A **workflow** is a GPS.

You know the destination. You follow clear instructions. “Turn left. Merge here. You’ve arrived.” It’s structured, predictable, and you almost always get where you’re going — unless you ignore it on purpose.

An **agent** is different. It’s like handing someone a map, a smartphone, a credit card, and saying:

> “Figure out how to get to the airport. You can walk, call a cab, take a detour if needed — just make it work.”

They might arrive faster. Or they might end up arguing with a rideshare app, taking a scenic detour, and arriving an hour later with a $18 smoothie. (We all know someone like that).

**Both approaches can work**, but the real question is:

> **Do you actually need autonomy here, or just a reliable set of instructions?**

Because here’s the thing — agents _sound_ amazing. And they are, in theory. You’ve probably seen the headlines:

- “Deploy an agent to handle your entire support pipeline!”
- “Let AI manage your tasks while you sleep!”
- “Revolutionary multi-agent systems — your personal consulting firm in the cloud!”

These case studies are everywhere. And some of them are real. But most of them?

They’re like travel photos on Instagram. You see the glowing sunset, the perfect skyline. You don’t see the six hours of layovers, the missed train, the $25 airport sandwich, or the three-day stomach bug from the street tacos.

That’s what agent success stories often leave out: **the operational complexity, the debugging pain, the spiraling token bill**.

So yeah, agents _can_ take you places. But before you hand over the keys, make sure you’re okay with the route they might choose. And that you can afford the tolls.

## The Hidden Costs Nobody Talks About

On paper, agents seem magical. You give them a goal, and they figure out how to achieve it. No need to hardcode control flow. Just define a task and let the system handle the rest.

In theory, it’s elegant. In practice, it’s chaos in a trench coat.

Let’s talk about what it _really_ costs to go agentic — not just in dollars, but in complexity, failure modes, and emotional wear-and-tear on your engineering team.

### Token Costs Multiply — Fast

[According to Anthropic’s research](https://www.anthropic.com/engineering/built-multi-agent-research-system), agents consume 4x more tokens than simple chat interactions. Multi-agent systems? Try 15x more tokens. This isn’t a bug — it’s the whole point. They loop, reason, re-evaluate, and often talk to themselves several times before arriving at a decision.

Here’s how that math breaks down:

- **Basic workflows**: $500/month for 100k interactions
- **Single agent systems**: $2,000/month for the same volume
- **Multi-agent systems**: $7,500/month (assuming $0.005 per 1K tokens)

And that’s if everything is working as intended.

If the agent gets stuck in a tool call loop or misinterprets instructions? You’ll see spikes that make your billing dashboard look like a crypto pump-and-dump chart.

### Debugging Feels Like AI Archaeology

With workflows, debugging is like walking through a well-lit house. You can trace input → function → output. Easy.

With agents? It’s more like wandering through an unmapped forest where the trees occasionally rearrange themselves. You don’t get traditional logs. You get _reasoning traces_, full of model-generated thoughts like:

> “Hmm, that didn’t work. I’ll try another approach.”

That’s not a stack trace. That’s an AI diary entry. It’s poetic, but not helpful when things break in production.

The really “fun” part? **Error propagation in agent systems can cascade in completely unpredictable ways.** One incorrect decision early in the reasoning chain can lead the agent down a rabbit hole of increasingly wrong conclusions, like a game of telephone where each player is also trying to solve a math problem. Traditional debugging approaches — setting breakpoints, tracing execution paths, checking variable states — become much less helpful when the “bug” is that your AI decided to interpret your instructions creatively.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-113.pngImage by author, generated by GPT-4o

### New Failure Modes You’ve Never Had to Think About

[Microsoft’s research has identified](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/) entirely **new failure modes that didn’t exist before agents**. Here are just a few that aren’t common in traditional pipelines:

- **Agent Injection**: Prompt-based exploits that hijack the agent’s reasoning
- **Multi-Agent Jailbreaks**: Agents colluding in unintended ways
- **Memory Poisoning**: One agent corrupts shared memory with hallucinated nonsense

These aren’t edge cases anymore — they’re becoming common enough that entire subfields of “LLMOps” now exist just to handle them.

If your monitoring stack doesn’t track token drift, tool spam, or emergent agent behavior, you’re flying blind.

### You’ll Need Infra You Probably Don’t Have

Agent-based systems don’t just need compute — they need new layers of tooling.

You’ll probably end up cobbling together some combo of:

- **LangFuse**, **Arize**, or **Phoenix** for observability
- **AgentOps** for cost and behavior monitoring
- Custom token guards and fallback strategies to stop runaway loops

This tooling stack _isn’t optional_. It’s required to keep your system stable.

And if you’re not already doing this? You’re not ready for agents in production — at least, not ones that impact real users or money.

* * *

So yeah. It’s not that agents are “bad.” They’re just a lot more expensive — financially, technically, and emotionally — than most people realize when they first start playing with them.

The tricky part is that none of this shows up in the demo. In the demo, it looks clean. Controlled. Impressive.

But in production, things leak. Systems loop. Context windows overflow. And you’re left explaining to your boss why your AI system spent $5,000 calculating the best time to send an email.

## When Agents Actually Make Sense

_\[Before we dive into agent success stories, a quick reality check: these are patterns observed from analyzing current implementations, not universal laws of software architecture. Your mileage may vary, and there are plenty of organizations successfully using workflows for scenarios where agents might theoretically excel. Consider these informed observations rather than divine commandments carved in silicon.\]_

Alright. I’ve thrown a lot of caution tape around agent systems so far — but I’m not here to scare you off forever.

Because sometimes, agents are _exactly_ what you need. They’re brilliant in ways that rigid workflows simply can’t be.

The trick is knowing the difference between “I want to try agents because they’re cool” and “this use case actually needs autonomy.”

Here are a few scenarios where agents genuinely earn their keep.

### Dynamic Conversations With High Stakes

Let’s say you’re building a customer support system. Some queries are straightforward — refund status, password reset, etc. A simple workflow handles those perfectly.

But other conversations? They require adaptation. Back-and-forth reasoning. Real-time prioritization of what to ask next based on what the user says.

That’s where agents shine.

In these contexts, you’re not just filling out a form — you’re navigating a situation. Personalized troubleshooting, product recommendations, contract negotiations — things where the next step depends entirely on what just happened.

Companies implementing agent-based customer support systems have reported wild ROI — we’re talking [112% to 457%](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) increases in efficiency and conversions, depending on the industry. Because when done right, agentic systems _feel_ smarter. And that leads to trust.

### High-Value, Low-Volume Decision-Making

Agents are expensive. But sometimes, the decisions they’re helping with are _more_ expensive.

BCG helped a shipbuilding firm cut 45% of its engineering effort using a multi-agent design system. That’s worth it — because those decisions were tied to multi-million dollar outcomes.

If you’re optimizing how to lay fiber optic cable across a continent or analyzing legal risks in a contract that affects your entire company — burning a few extra dollars on compute isn’t the problem. The _wrong_ decision is.

Agents work here because the _cost of being wrong_ is way higher than the _cost of computing_.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/when-agents-win-683x1024.jpegImage by author

### Open-Ended Research and Exploration

There are problems where you literally can’t define a flowchart upfront — because you don’t know what the “right steps” are.

Agents are great at diving into ambiguous tasks, breaking them down, iterating on what they find, and adapting in real-time.

Think:

- Technical research assistants that read, summarize, and compare papers
- Product analysis bots that explore competitors and synthesize insights
- Research agents that investigate edge cases and suggest hypotheses

These aren’t problems with known procedures. They’re open loops by nature — and agents thrive in those.

### **Multi-Step, Unpredictable Workflows**

Some tasks have too many branches to hardcode — the kind where writing out all the “if this, then that” conditions becomes a full-time job.

This is where agent loops can actually _simplify_ things, because the LLM handles the flow dynamically based on context, not pre-written logic.

Think diagnostics, planning tools, or systems that need to factor in dozens of unpredictable variables.

If your logic tree is starting to look like a spaghetti diagram made by a caffeinated octopus — yeah, maybe it’s time to let the model take the wheel.

* * *

So no, I’m not anti-agent (I actually love them!) I’m pro-alignment — matching the tool to the task.

When the use case _needs_ flexibility, adaptation, and autonomy, then yes — bring in the agents. But only after you’re honest with yourself about whether you’re solving a real complexity… or just chasing a shiny abstraction.

## When Workflows Are Obviously Better (But Less Exciting)

_\[Again, these are observations drawn from industry analysis rather than ironclad rules. There are undoubtedly companies out there successfully using agents for regulated processes or cost-sensitive applications — possibly because they have specific requirements, exceptional expertise, or business models that change the economics. Think of these as strong starting recommendations, not limitations on what’s possible.\]_

Let’s step back for a second.

A lot of AI architecture conversations get stuck in hype loops — “Agents are the future!” “AutoGPT can build companies!” — but in actual production environments, most systems don’t need agents.

They need something that works.

That’s where workflows come in. And while they may not feel as futuristic, they are **incredibly effective** in the environments that most of us are building for.

### Repeatable Operational Tasks

If your use case involves clearly defined steps that rarely change — like sending follow-ups, tagging data, validating form inputs — a workflow will outshine an agent every time.

It’s not just about cost. It’s about stability.

You don’t want creative reasoning in your payroll system. You want the same result, every time, with no surprises. A well-structured pipeline gives you that.

There’s nothing sexy about “process reliability” — until your agent-based system forgets what year it is and flags every employee as a minor.

### Regulated, Auditable Environments

Workflows are deterministic. That means they’re traceable. Which means if something goes wrong, you can show exactly what happened — step-by-step — with logs, fallbacks, and structured output.

If you’re working in healthcare, finance, law, or government — places where **“we think the AI decided to try something new”** is not an acceptable answer — this matters.

You can’t build a safe AI system without transparency. Workflows give you that by default.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/when-workflows-win-683x1024.jpegImage by author

### High-Frequency, Low-Complexity Scenarios

There are entire categories of tasks where the **cost per request** matters more than the sophistication of reasoning. Think:

- Fetching info from a database
- Parsing emails
- Responding to FAQ-style queries

A workflow can handle thousands of these requests per minute, at predictable costs and latency, with zero risk of runaway behavior.

If you’re scaling fast and need to stay lean, a structured pipeline beats a clever agent.

### Startups, MVPs, and Just-Get-It-Done Projects

Agents require infrastructure. Monitoring. Observability. Cost tracking. Prompt architecture. Fallback planning. Memory design.

If you’re not ready to invest in all of that — and most early-stage teams aren’t — agents are probably too much, too soon.

Workflows let you move fast and learn how LLMs behave before you get into recursive reasoning and emergent behavior debugging.

Think of it this way: workflows are how you **get to production**. Agents are how you scale specific use cases once you understand your system deeply.

* * *

One of the best mental models I’ve seen (shoutout to [Anthropic’s engineering blog](https://www.anthropic.com/engineering/building-effective-agents)) is this:

> **Use workflows to build structure around the predictable. Use agents to explore the unpredictable.**

Most real-world AI systems are a mix — and many of them lean heavily on workflows because **production doesn’t reward cleverness**. It rewards **resilience**.

## A Decision Framework That Actually Works

Here’s something I’ve learned (the hard way, of course): most bad architecture decisions don’t come from a lack of knowledge — they come from moving too fast.

You’re in a sync. Someone says, “This feels a bit too dynamic for a workflow — maybe we just go with agents?”

Everyone nods. It sounds reasonable. Agents are flexible, right?

Fast forward three months: the system’s looping in weird places, the logs are unreadable, costs are spiking, and no one remembers who suggested using agents in the first place. You’re just trying to figure out why an LLM decided to summarize a refund request by booking a flight to Peru.

So, let’s slow down for a second.

This isn’t about picking the trendiest option — it’s about building something you can explain, scale, and actually maintain.

The framework below is designed to make you pause and think clearly before the token bills stack up and your nice prototype turns into a very expensive choose-your-own-adventure story.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/Mediamodifier-Design1.svgImage by author

### The Scoring Process: Because Single-Factor Decisions Are How Projects Die

This isn’t a decision tree that bails out at the first “sounds good.” It’s a structured evaluation. You go through **five dimensions**, score each one, and see what the system is really asking for — not just what sounds fun.

**Here’s how it works:**

> - Each dimension gives **+2 points** to either workflow or agents.
> - One question gives **+1 point** (reliability).
> - Add it all up at the end — and trust the result more than your agent hype cravings.

* * *

### Complexity of the Task (2 points)

Evaluate whether your use case has well-defined procedures. Can you write down steps that handle 80% of your scenarios without resorting to hand-waving?

- Yes → +2 for **workflows**
- No, there’s ambiguity or dynamic branching → +2 for **agents**

If your instructions involve phrases like “and then the system figures it out” — you’re probably in agent territory.

### Business Value vs. Volume (2 points)

Assess the cold, hard economics of your use case. Is this a high-volume, cost-sensitive operation — or a low-volume, high-value scenario?

- High-volume and predictable → +2 for **workflows**
- Low-volume but high-impact decisions → +2 for **agents**

Basically: if compute cost is more painful than getting something slightly wrong, workflows win. If being wrong is expensive and being slow loses money, agents might be worth it.

### Reliability Requirements (1 point)

Determine your tolerance for output variability — and be honest about what your business actually needs, not what sounds flexible and modern. How much output variability can your system tolerate?

- Needs to be consistent and traceable (audits, reports, clinical workflows) → +1 for **workflows**
- Can handle some variation (creative tasks, customer support, exploration) → +1 for **agents**

This one’s often overlooked — but it directly affects how much guardrail logic you’ll need to write (and maintain).

### Technical Readiness (2 points)

Evaluate your current capabilities without the rose-colored glasses of “we’ll figure it out later.” What’s your current engineering setup and comfort level?

- You’ve got logging, traditional monitoring, and a dev team that hasn’t yet built agentic infra → +2 for **workflows**
- You already have observability, fallback plans, token tracking, and a team that understands emergent AI behavior → +2 for **agents**

This is your system maturity check. Be honest with yourself. Hope is not a debugging strategy.

### Organizational Maturity (2 points)

Assess your team’s AI expertise with brutal honesty — this isn’t about intelligence, it’s about experience with the specific weirdness of AI systems. How experienced is your team with prompt engineering, tool orchestration, and LLM weirdness?

- Still learning prompt design and LLM behavior → +2 for **workflows**
- Comfortable with distributed systems, LLM loops, and dynamic reasoning → +2 for **agents**

You’re not evaluating intelligence here — just experience with a specific class of problems. Agents demand a deeper familiarity with AI-specific failure patterns.

* * *

### Add Up Your Score

After completing all five evaluations, calculate your total scores.

- **Workflow score ≥ 6** → Stick with workflows. You’ll thank yourself later.
- **Agent score ≥ 6** → Agents might be viable — _if_ there are no workflow-critical blockers.

**Important**: This framework doesn’t tell you what’s coolest. It tells you what’s sustainable.

A lot of use cases will lean workflow-heavy. That’s not because agents are bad — it’s because true agent readiness involves _many_ systems working in harmony: infrastructure, ops maturity, team knowledge, failure handling, and cost controls.

And if any one of those is missing, it’s usually not worth the risk — yet.

## The Plot Twist: You Don’t Have to Choose

Here’s a realization I wish I’d had earlier: you don’t have to pick sides. The magic often comes from **hybrid systems** — where workflows provide stability, and agents offer flexibility. It’s the best of both worlds.

Let’s explore how that actually works.

### Why Hybrid Makes Sense

Think of it as layering:

1. **Reactive layer** (your workflow): handles predictable, high-volume tasks
2. **Deliberative layer** (your agent): steps in for complex, ambiguous decisions

This is exactly how many real systems are built. The workflow handles the 80% of predictable work, while the agent jumps in for the 20% that needs creative reasoning or planning

### Building Hybrid Systems Step by Step

Here’s a refined approach I’ve used (and borrowed from hybrid best practices):

1. **Define the core workflow.**

Map out your predictable tasks — data retrieval, vector search, tool calls, response synthesis.
2. **Identify decision points.**

Where might you _need_ an agent to decide things dynamically?
3. **Wrap those steps with lightweight agents.**

Think of them as scoped decision engines — they plan, act, reflect, then return answers to the workflow .
4. **Use memory and plan loops wisely.**

Give the agent just enough context to make smart choices without letting it go rogue.
5. **Monitor and fail gracefully.**

If the agent goes wild or costs spike, fall back to a default workflow branch. Keep logs and token meters running.
6. **Human-in-the-loop checkpoint.**

Especially in regulated or high-stakes flows, pause for human validation before agent-critical actions

### When to Use Hybrid Approach

| Scenario | Why Hybrid Works |
| --- | --- |
| Customer support | Workflow does easy stuff, agents adapt when conversations get messy |
| Content generation | Workflow handles format and publishing; agent writes the body |
| Data analysis/reporting | Agents summarize & interpret; workflows aggregate & deliver |
| High-stakes decisions | Use agent for exploration, workflow for execution and compliance |

When to use hybrid approach

This aligns with how systems like WorkflowGen, n8n, and Anthropic’s own tooling advise building — stable pipelines with scoped autonomy.

### Real Examples: Hybrid in Action

#### A Minimal Hybrid Example

Here’s a scenario I used with LangChain and LangGraph:

- **Workflow stage**: fetch support tickets, embed & search
- **Agent cell**: decide whether it’s a refund question, a complaint, or a bug report
- **Workflow**: run the correct branch based on agent’s tag
- **Agent stage**: if it’s a complaint, summarize sentiment and suggest next steps
- **Workflow**: format and send response; log everything

The result? Most tickets flow through without agents, saving cost and complexity. But when ambiguity hits, the agent steps in and adds real value. No runaway token bills. Clear traceability. Automatic fallbacks.

This pattern splits the logic between a structured workflow and a scoped agent. ( **Note: this is a high-level demonstration**)

```python
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults

# 1. Workflow: set up RAG pipeline
embeddings = OpenAIEmbeddings()
vectordb = FAISS.load_local(
    "docs_index",
    embeddings,
    allow_dangerous_deserialization=True
)
retriever = vectordb.as_retriever()

system_prompt = (
    "Use the given context to answer the question. "
    "If you don't know the answer, say you don't know. "
    "Use three sentences maximum and keep the answer concise.\n\n"
    "Context: {context}"
)
prompt = ChatPromptTemplate.from_messages([\
    ("system", system_prompt),\
    ("human", "{input}"),\
])

llm = init_chat_model("openai:gpt-4.1", temperature=0)
qa_chain = create_retrieval_chain(
    retriever,
    create_stuff_documents_chain(llm, prompt)
)

# 2. Agent: Set up agent with Tavily search
search = TavilySearchResults(max_results=2)
agent_llm = init_chat_model("anthropic:claude-3-7-sonnet-latest", temperature=0)
agent = create_react_agent(
    model=agent_llm,
    tools=[search]
)

# Uncertainty heuristic
def is_answer_uncertain(answer: str) -> bool:
    keywords = [\
        "i don't know", "i'm not sure", "unclear",\
        "unable to answer", "insufficient information",\
        "no information", "cannot determine"\
    ]
    return any(k in answer.lower() for k in keywords)

def hybrid_pipeline(query: str) -> str:
    # RAG attempt
    rag_out = qa_chain.invoke({"input": query})
    rag_answer = rag_out.get("answer", "")

    if is_answer_uncertain(rag_answer):
        # Fallback to agent search
        agent_out = agent.invoke({
            "messages": [{"role": "user", "content": query}]
        })
        return agent_out["messages"][-1].content

    return rag_answer

if __name__ == "__main__":
    result = hybrid_pipeline("What are the latest developments in AI?")
    print(result)

```

**What’s happening here:**

- The workflow takes the first shot.
- If the result seems weak or uncertain, the agent takes over.
- You only pay the agent cost when you really need to.

Simple. Controlled. Scalable.

#### Advanced: Workflow-Controlled Multi-Agent Execution

If your problem _really_ calls for multiple agents — say, in a research or planning task — structure the system as a **graph**, not a soup of recursive loops. ( **Note: this is a high level demonstration**)

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import ToolNode
from langchain_core.messages import AnyMessage

# 1. Define your graph's state
class TaskState(TypedDict):
    input: str
    label: str
    output: str

# 2. Build the graph
graph = StateGraph(TaskState)

# 3. Add your classifier node
def classify(state: TaskState) -> TaskState:
    # example stub:
    state["label"] = "research" if "latest" in state["input"] else "summary"
    return state

graph.add_node("classify", classify)
graph.add_edge(START, "classify")

# 4. Define conditional transitions out of the classifier node
graph.add_conditional_edges(
    "classify",
    lambda s: s["label"],
    path_map={"research": "research_agent", "summary": "summarizer_agent"}
)

# 5. Define the agent nodes
research_agent = ToolNode([create_react_agent(...tools...)])
summarizer_agent = ToolNode([create_react_agent(...tools...)])

# 6. Add the agent nodes to the graph
graph.add_node("research_agent", research_agent)
graph.add_node("summarizer_agent", summarizer_agent)

# 7. Add edges. Each agent node leads directly to END, terminating the workflow
graph.add_edge("research_agent", END)
graph.add_edge("summarizer_agent", END)

# 8. Compile and run the graph
app = graph.compile()
final = app.invoke({"input": "What are today's AI headlines?", "label": "", "output": ""})
print(final["output"])

```

This pattern gives you:

- **Workflow-level control** over routing and memory
- **Agent-level reasoning** where appropriate
- **Bounded loops** instead of infinite agent recursion

This is how tools like LangGraph are designed to work: **structured autonomy**, not free-for-all reasoning.

## Production Deployment — Where Theory Meets Reality

All the architecture diagrams, decision trees, and whiteboard debates in the world won’t save you if your AI system falls apart the moment real users start using it.

Because that’s where things get messy — the inputs are noisy, the edge cases are endless, and users have a magical ability to break things in ways you never imagined. Production traffic has a personality. It will test your system in ways your dev environment never could.

And that’s where most AI projects stumble.

The demo works. The prototype impresses the stakeholders. But then you go live — and suddenly the model starts hallucinating customer names, your token usage spikes without explanation, and you’re ankle-deep in logs trying to figure out why everything broke at 3:17 a.m. (True story!)

This is the gap between a cool proof-of-concept and a system that actually holds up in the wild. It’s also where the difference between workflows and agents stops being philosophical and starts becoming very, very operational.

Whether you’re using agents, workflows, or some hybrid in between — once you’re in production, it’s a different game.

You’re no longer trying to prove that the AI _can_ work.

You’re trying to make sure it works **reliably, affordably, and safely** — every time.

So what does that actually take?

Let’s break it down.

### Monitoring (Because “It Works on My Machine” Doesn’t Scale)

Monitoring an agent system isn’t just “nice to have” — it’s survival gear.

You can’t treat agents like regular apps. Traditional APM tools won’t tell you why an LLM decided to loop through a tool call 14 times or why it burned 10,000 tokens to summarize a paragraph.

You need observability tools that speak the agent’s language. That means tracking:

- token usage patterns,
- tool call frequency,
- response latency distributions,
- task completion outcomes,
- and cost per interaction — **in real time**.

This is where tools like **LangFuse**, **AgentOps**, and **Arize Phoenix** come in. They let you peek into the black box — see what decisions the agent is making, how often it’s retrying things, and what’s going off the rails before your budget does.

Because when something breaks, “the AI made a weird choice” is not a helpful bug report. You need traceable reasoning paths and usage logs — not just vibes and token explosions.

Workflows, by comparison, are way easier to monitor.

You’ve got:

- response times,
- error rates,
- CPU/memory usage,
- and request throughput.

All the usual stuff you already track with your standard APM stack — Datadog, Grafana, Prometheus, whatever. No surprises. No loops trying to plan their next move. Just clean, predictable execution paths.

So yes — both need monitoring. But agent systems demand a whole new layer of visibility. If you’re not prepared for that, production will make sure you learn it the hard way.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-116.pngImage by author

### Cost Management (Before Your CFO Stages an Intervention)

Token consumption in production can spiral out of control faster than you can say “autonomous reasoning.”

It starts small — a few extra tool calls here, a retry loop there — and before you know it, you’ve burned through half your monthly budget debugging a single conversation. Especially with agent systems, costs don’t just add up — they compound.

That’s why smart teams treat **cost management like infrastructure**, not an afterthought.

Some common (and necessary) strategies:

- **Dynamic model routing** — Use lightweight models for simple tasks, save the expensive ones for when it actually matters.
- **Caching** — If the same question comes up a hundred times, you shouldn’t pay to answer it a hundred times.
- **Spending alerts** — Automated flags when usage gets weird, so you don’t learn about the problem from your CFO.

With agents, this matters even more.

Because once you hand over control to a reasoning loop, you lose visibility into how many steps it’ll take, how many tools it’ll call, and how long it’ll “think” before returning an answer.

If you don’t have real-time cost tracking, per-agent budget limits, and graceful fallback paths — you’re just one prompt away from a very expensive mistake.

Agents are smart. But they’re not cheap. Plan accordingly.

Workflows need cost management too.

If you’re calling an LLM for every user request, especially with retrieval, summarization, and chaining steps — the numbers add up. And if you’re using GPT-4 everywhere out of convenience? You’ll feel it on the invoice.

But workflows are _predictable_. You know how many calls you’re making. You can precompute, batch, cache, or swap in smaller models without disrupting logic. Cost scales linearly — and predictably.

### Security (Because Autonomous AI and Security Are Best Friends)

AI security isn’t just about guarding endpoints anymore — it’s about preparing for systems that can make their own decisions.

That’s where the concept of **shifting left** comes in — bringing security earlier into your development lifecycle.

> Instead of bolting on security after your app “works,” shift-left means designing with security from day one: during prompt design, tool configuration, and pipeline setup.

With **agent-based systems**, you’re not just securing a predictable app. You’re securing something that can autonomously decide to call an API, access private data, or trigger an external action — often in ways you didn’t explicitly program. That’s a very different threat surface.

This means your security strategy needs to evolve. You’ll need:

- **Role-based access control** for every tool an agent can access
- **Least privilege enforcement** for external API calls
- **Audit trails** to capture every step in the agent’s reasoning and behavior
- **Threat modeling** for novel attacks like prompt injection, agent impersonation, and collaborative jailbreaking (yes, that’s a thing now)

Most traditional app security frameworks assume the code defines the behavior. But with agents, the behavior is dynamic, shaped by prompts, tools, and user input. If you’re building with autonomy, you need **security controls designed for unpredictability**.

* * *

But what about **workflows**?

They’re easier — but not risk-free.

Workflows are deterministic. You define the path, you control the tools, and there’s no decision-making loop that can go rogue. That makes security simpler and more testable — especially in environments where compliance and auditability matter.

Still, workflows touch sensitive data, integrate with third-party services, and output user-facing results. Which means:

- Prompt injection is still a concern
- Output sanitation is still essential
- API keys, database access, and PII handling still need protection

For workflows, “shifting left” means:

- Validating input/output formats early
- Running prompt tests for injection risk
- Limiting what each component can access, even if it “seems safe”
- Automating red-teaming and fuzz testing around user inputs

It’s not about paranoia — it’s about protecting your system before things go live and real users start throwing unexpected inputs at it.

* * *

Whether you’re building agents, workflows, or hybrids, the rule is the same:

> **If your system can generate actions or outputs, it can be exploited.**

So build like someone _will_ try to break it — because eventually, someone probably will.

### Testing Methodologies (Because “Trust but Verify” Applies to AI Too)

Testing production AI systems is like quality-checking a very smart but slightly unpredictable intern.

They mean well. They usually get it right. But every now and then, they surprise you — and not always in a good way.

That’s why you need **layers of testing**, especially when dealing with agents.

For **agent systems**, a single bug in reasoning can trigger a whole chain of weird decisions. One wrong judgment early on can snowball into broken tool calls, hallucinated outputs, or even data exposure. And because the logic lives inside a prompt, not a static flowchart, you can’t always catch these issues with traditional test cases.

A solid testing strategy usually includes:

- **Sandbox environments** with carefully designed mock data to stress-test edge cases
- **Staged deployments** with limited real data to monitor behavior before full rollout
- **Automated regression tests** to check for unexpected changes in output between model versions
- **Human-in-the-loop reviews** — because some things, like tone or domain nuance, still need human judgment

For agents, this isn’t optional. It’s the only way to stay ahead of unpredictable behavior.

* * *

But what about **workflows**?

They’re easier to test — and honestly, that’s one of their biggest strengths.

Because workflows follow a deterministic path, you can:

- Write unit tests for each function or tool call
- Mock external services cleanly
- Snapshot expected inputs/outputs and test for consistency
- Validate edge cases without worrying about recursive reasoning or planning loops

You still want to test prompts, guard against prompt injection, and monitor outputs — but the surface area is smaller, and the behavior is traceable. You know what happens when Step 3 fails, because you wrote Step 4.

**Workflows don’t remove the need for testing — they make it testable.**

That’s a big deal when you’re trying to ship something that won’t fall apart the moment it hits real-world data.

## The Honest Recommendation: Start Simple, Scale Intentionally

If you’ve made it this far, you’re probably not looking for hype — you’re looking for a system that actually works.

So here’s the honest, slightly unsexy advice:

> **Start with workflows. Add agents only when you can clearly justify the need.**

Workflows may not feel revolutionary, but they are reliable, testable, explainable, and cost-predictable. They teach you how your system behaves in production. They give you logs, fallback paths, and structure. And most importantly: **they scale.**

That’s not a limitation. That’s maturity.

It’s like learning to cook. You don’t start with molecular gastronomy — you start by learning how to not burn rice. Workflows are your rice. Agents are the foam.

And when you do run into a problem that actually _needs_ dynamic planning, flexible reasoning, or autonomous decision-making — you’ll know. It won’t be because a tweet told you agents are the future. It’ll be because you hit a wall workflows can’t cross. And at that point, you’ll be ready for agents — and your infrastructure will be, too.

Look at the Mayo Clinic. [They run **14 algorithms on every ECG**](https://newsnetwork.mayoclinic.org/discussion/mayo-clinic-launches-new-technology-platform-ventures-to-revolutionize-diagnostic-medicine/#:~:text=Mayo%20Clinic%20and%20AI%2Ddriven%20health%20technology%20company,to%20Mayo%27s%20deep%20repository%20of%20medical%20data.)— not because it’s trendy, but because it improves diagnostic accuracy at scale. Or take [Kaiser Permanente](https://healthinnovation.ucsd.edu/news/11-health-systems-leading-in-ai), which says its AI-powered clinical support systems have helped save _hundreds of lives each year_.

These aren’t tech demos built to impress investors. These are real systems, in production, handling millions of cases — quietly, reliably, and with huge impact.

The secret? It’s not about choosing agents or workflows.

It’s about understanding the problem deeply, picking the right tools deliberately, and building for resilience — not for flash.

Because in the real world, value comes from what works.

Not what wows.

* * *

</details>

<details>
<summary>build-production-agentic-rag-with-llmops-at-its-core</summary>

## LLMOps for production agentic RAG

Welcome to Lesson 6 of Decoding ML’s **[Building Your Second Brain AI Assistant Using Agents, LLMs and RAG](https://github.com/decodingml/second-brain-ai-assistant-course/tree/main)** open-source course, where you will learn to architect and build a production-ready Notion-like AI research assistant.

Agents are the latest breakthrough in AI. For the first time in history, we give a machine complete control over its decisions without explicitly telling it. Agents do that through the LLM, the system's brain that interprets the queries and decides what to do next and through the tools that provide access to the external world, such as APIs and databases.

One of the agents' most popular use cases is Agentic RAG, in which agents access a tool that provides them with access to a vector database (or another type of database) to retrieve relevant context dynamically before generating an answer.

Agentic RAG differs from a standard RAG workflow in that the LLM can dynamically choose when it needs context or whether a single query to the database provides enough context.

Agents, relative to workflows, introduce even more randomness into the system. This is a core reason why adding LLMOp best practices such as prompt monitoring and LLM evaluation is a critical step in making your system easy to debug and maintain.

> LLMOps and evaluation are critical in any AI system, but they become even more crucial when working with agents!

In previous lessons of the course, we implemented all the offline pipelines that helped us prepare for advanced RAG, such as populating the MongoDB vector index with the proper data from our Second Brain and fine-tuning a summarization open-source small language model (SLM).

In this lesson, we will take the final step to glue everything together by adding an agentic layer on top of the vector index and an observability module on top of the agent to monitor and evaluate it. These elements will be part of our online inference pipelines, which will turn into the Second Brain AI assistant that the user interacts with, as seen in the demo below:

Thus, in this lesson, we will dive into the fundamentals of **agentic RAG**, exploring how agents powered by LLMs can go beyond traditional retrieval-based workflows to dynamically interact with multiple tools and external systems, such as vector databases.

Next, we will move to our **observability pipeline,** which evaluates the agents using techniques such as LLM-as-judges and heuristics to ensure they work correctly. We will monitor the prompt traces that power the agents to help us debug and understand what happens under the hood.

**While going through this lesson, we will learn the following:**

- Understand what an agent is, how it differs from workflows, and why it’s useful.

- Architect the Agentic RAG module, understanding its components and data flow.

- Build and monitor an agentic LLM application using SmolAgents and Opik.

- Implement prompt monitoring pipelines to track input/output, latency, and metadata.

- Explore RAG evaluation metrics like moderation, hallucination, and answer relevance.

- Create custom evaluation metrics, integrating heuristics and LLM judges.

- Automate observability, ensuring real-time performance tracking.

- Interact with the Second Brain AI assistant via CLI or a beautiful Gradio UI.


https://substackcdn.com/image/fetch/$s_!cdC1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F936af09a-fd2d-4559-905f-4a42e1a3ce9a_1166x1082.png

Let’s get started. Enjoy!

---

## 1. Understanding how LLM-powered agents work

LLM-powered agents combine a **language model, tools, and memory** to process information and take action.

They don’t just generate text—they **reason, retrieve data, and interact with external systems** to complete tasks.

At its core, an agent takes in an input, analyzes what needs to be done, and decides the best way to respond. Instead of working in isolation, it can tap into external tools like APIs, databases, or plugins to enhance its capabilities.

With the reasoning power of LLMs, the agent doesn’t just react—it strategizes. It breaks down the task, plans the necessary steps, and takes action to get the job done efficiently.

https://substackcdn.com/image/fetch/$s_!gLNT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67ffe267-55f2-4af7-9910-7410c7605550_1220x754.png

The most popular way to design agents is by using the ReAct framework, which models the agent as follows:

- **act:** the LLM calls specific tools
- **observe:** pass the tool output back to the LLM
- **reason:** the LLM reason about the tool output to decide what to do next (e.g., call another tool or respond directly)

Now, let’s understand how agents and RAG fit together.

---

## 2. Researching Agentic RAG

Unlike a traditional RAG setup's linear, step-by-step nature, Agentic RAG puts an agent at the center of decision-making.

Instead of passively retrieving and generating responses,the agent actively directs the process—deciding what to search for, how to refine queries, and when to use external tools, such as SQL, vector, or graph databases.

https://substackcdn.com/image/fetch/$s_!ZnV_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c59d9df-d60f-47bc-81de-cfd4fdebf5f8_1210x704.png

For example, instead of querying the vector database just once (what we usually do in a standard RAG workflow), the agent might decide that after its first query, it doesn’t have enough information to provide an answer, making another request to the vector database with a different query.

---

## 3. Exploring the difference between agents and workflows

Now that we’ve explored LLM-powered agents and Agentic RAGs, let’s take a step back and look at a broader question: “ **How do agents differ from workflows?”** While both help automate tasks, they operate in fundamentally different ways.

A workflow follows a fixed, predefined sequence—every step is planned in advance, making it reliable but rigid (more similar to classic programming).

In contrast, an agent **dynamically decides** what to do next **based on reasoning,** memory, and available tools. Instead of just executing steps, it adapts, learns, and makes decisions on the fly.

Think of a workflow as an assembly line, executing tasks in order, while an agent is like an intelligent assistant, capable of adjusting its approach in real time. This flexibility makes agents powerful for handling unstructured, complex problems that require dynamic decision-making.

https://substackcdn.com/image/fetch/$s_!yBni!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e64d5e0-7ef1-4e7f-b441-3bf1fef4ff9a_1276x818.png

Therefore, the trade-off between reliability and adaptability is key—workflows offer stability but are rigid, while agents provide flexibility by making dynamic decisions at the cost of consistency.

Now that we understand the basics of working with agents, let’s dive into the architecture of our Second Brain agent.

---

## 4. Architecting the Agentic RAG module

When architecting the Agentic RAG module, the goal is to build an intelligent system that efficiently combines retrieval, reasoning, and summarization to generate high-quality responses tailored to user queries.

#### What’s the interface of the pipeline?

The pipeline takes a user query as input (submitted through the Gradio UI).

The output is a refined answer generated by the agent after reasoning, retrieving relevant context from **[MongoDB](https://www.mongodb.com/products/platform/atlas-vector-search?utm_campaign=ai-pilot&utm_medium=creator&utm_term=iusztin&utm_source=blog)** through semantic search, and processing it through the summarization tool.

#### Offline vs. online pipelines

The Agentic RAG module fundamentally differs from the offline ML pipelines we’ve built in previous lessons.

This module is entirely decoupled from the pipelines in Lessons 1-5. It lives in a separate **[second-brain-online](https://github.com/decodingml/second-brain-ai-assistant-course/tree/main/apps/second-brain-online)** folder within our repository as its own standalone Python application.

This separation is intentional—by keeping the offline pipelines (feature and training) fully independent from the online inference system, we ensure a clean architectural divide.

As a quick reminder from Lesson 1, **offline pipelines** are batch pipelines that run on a schedule or trigger. They process input data and store the output artifacts in storage, allowing other pipelines or clients to consume them as needed.

These include the data collection pipeline, ETL pipeline, RAG feature pipeline, dataset generation pipeline, and training pipeline. They operate independently and are decoupled through various storage solutions such as document databases, vector databases, data registries, or model registries.

The Agentic RAG module, on the other hand, belongs to the category of **online pipelines**. It directly interacts with the user and must remain available at all times. The online pipelines available in this project are the agentic inference pipeline, the summarization inference pipeline, and the observability pipeline.

Unlike offline pipelines, these do not require orchestration and function similarly to RESTful APIs, ensuring minimal latency and efficient responses.

#### What does the pipeline’s architecture look like?

The Agentic RAG module operates in real time, instantly responding to user queries without redundant processing.

This module's core is an agent-driven system that reasons independently and dynamically invokes tools to handle user queries. They serve as extensions of the LLM model powering the agent, allowing it to perform tasks it wouldn’t efficiently handle on its own without specialized fine-tuning.

Our agent relies on three main components:

1. **The what can I do tool**, which helps users understand the usages of the system

2. **The retriever tool** that queries MongoDB’s vector index pre-populated during our offline processing

3. **The summarization tool** uses a REST API to call a different model specialized in summarizing web documents.

We specifically picked these ones as they are a perfect use case for showing how to use a tool that runs only with Python, one that calls a database, and one that calls an API (three of the most common scenarios).

The agent layer is powered by the **[SmolAgents](https://github.com/huggingface/smolagents)** framework (by Hugging Face) and orchestrates the reasoning process. A maximum number of steps can be set to ensure the reasoning remains focused and does not take unnecessary iterations to reach a response (avoiding skyrocketing bills).

To provide a seamless user experience, we integrated the agentic inference pipeline with a **[Gradio UI](https://www.gradio.app/)**, making interactions intuitive and accessible. This setup ensures that users can engage with the assistant as naturally as possible, simulating a conversational AI experience.

The interface allows us to track how the agent selects and uses tools during interactions.

For instance, we can see when it calls the **[MongoDB vector search tool](https://www.mongodb.com/products/platform/atlas-vector-search?utm_campaign=ai-pilot&utm_medium=creator&utm_term=iusztin&utm_source=blog)** to retrieve relevant data and how it cycles between retrieving information and reasoning before generating a response.

https://substackcdn.com/image/fetch/$s_!bqEU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb30a1f89-0c60-4a28-b87a-5390262f1500_1170x1065.png

The agentic inference pipeline is designed to handle user queries in real time, orchestrating a seamless data flow from input to response. To understand how information moves through the system, we break down the interaction between the user, the retrieval process, and the summarization mechanism.

When a user submits a query through the **Gradio UI**, the **Agentic Layer**, an LLM-powered agent, dynamically determines the most suitable tool to process the request.

If additional context is required, the **Retriever Tool** fetches relevant information from the MongoDB vector database, extracting the most relevant chunks. This vector database was previously populated through the RAG feature pipeline in Lesson 5, ensuring the system has preprocessed, structured knowledge readily available for retrieval.

The retrieved data is then refined using the **Summarization Tool**, which enhances clarity before generating the final response. For summarization, we can choose between a custom Summarization Inference Pipeline, which is powered by the Hugging Face model we trained in Lesson 4, or an OpenAI model.

The agent continues reasoning iteratively until it reaches the predefined step limit or it decides it has the final answer, ensuring efficiency while maintaining high response quality.

As a side note, given the simplicity of our use case, the Second Brain AI assistant could have been implemented using a traditional workflow, directly retrieving and responding to queries without an agentic approach.

However, by embracing this modular strategy, we achieve greater scalability and flexibility, allowing the system to integrate new data sources or tools easily in the future.

Now that we understand how the agent works, let’s dig into how we can evaluate it and then into the implementation.

---

## 5. Understanding how to evaluate an agentic RAG application

When evaluating an Agentic RAG application, it’s important to distinguish between two primary evaluation approaches: **LLM evaluation** and **Application/RAG evaluation**. Each serves a different purpose, and while LLM evaluation assesses the model in isolation, Application/RAG evaluation tests the entire application as a system.

In this case, our primary focus is evaluating the RAG pipeline as a black-box system, assessing how retrieval and reasoning work together to generate the final output.

However, we also provide a brief refresher on key insights from LLM evaluation in Lesson 4 to highlight its role in the broader evaluation process.

#### LLM evaluation

As a brief reminder, LLM evaluation measures response quality without retrieval. In Lesson 4, we tested this by analyzing the model’s ability to generate answers from its internal knowledge.

Popular methods for LLM evaluation include **benchmark-based evaluation** (using standardized datasets), **heuristic evaluation**(ROUGE, BLEU, regex matching, or custom heuristics), semantic-based evaluation (BERT Score), and **LLM-as-a-judge**, where another LLM evaluates the generated outputs.

Each method has strengths and trade-offs. Benchmark-based evaluation provides standardized comparisons but may not fully capture real-world performance, while heuristic methods may offer quick, interpretable insights but often fail to assess deeper contextual understanding. Additionally, LLM-as-a-judge is flexible and scalable, though it introduces potential biases from the evaluating model itself.

#### RAG evaluation

Unlike LLM evaluation, which assesses the model’s ability to generate responses from internal knowledge, RAG evaluation focuses on how well the retrieval and generation processes work together.

Evaluating a RAG application requires analyzing how different components interact. We focus on four key dimensions:

- **User input** – The query submitted by the user.
- **Retrieved context** – The passages or documents fetched from the vector database.
- **Generated output**– The final response produced by the LLM based on retrieved information.
- **Expected output** – The ideal or ground-truth answer, if available, for comparison.

By evaluating these dimensions, we can determine whether the retrieved context is relevant, the response is grounded in the retrieved data, and the system generates complete and accurate answers.

As mentioned, we break the process into two key steps to evaluate a RAG application correctly: retrieval and generation.

Since RAG applications rely on retrieving relevant documents before generating responses, retrieval quality plays a critical role in overall performance. If the retrieval step fails, the LLM will either generate incorrect answers or hallucinate information.

To assess **retrieval step** effectiveness, we can use various ranking-based metrics, including:

- **NDCG (Normalized Discounted Cumulative Gain)** – Measures how well the retrieved documents are ranked, prioritizing the most relevant ones at the top.
- **MRR (Mean Reciprocal Rank)** – Evaluates how early the first relevant document appears in the retrieved results, ensuring high-ranking relevance.

Another option is to visualize the embedding from your vector index (using algorithms such as t-SNE or UMAP) to see if there are any meaningful clusters within your vector space.

On the other hand, during **the generation step**, you can leverage similar strategies we looked at in the LLM evaluation subsection while considering the context dimension.

#### LLM application evaluation

For LLM application evaluation, we take a black-box approach, meaning we assess the entire Agentic RAG module rather than isolating individual components.

We evaluate the entire system by analyzing the input, output, and retrieved context instead of separating retrieval and generation into independent evaluations.

This approach allows us to identify system-wide failures and measure how well the retrieved knowledge contributes to generating accurate and relevant responses.

By evaluating the entire module, we can detect common RAG issues, such as hallucinations caused by missing context or low retrieval recall leading to incomplete answers, ensuring the system performs reliably in real-world scenarios.

#### **How many samples do we need to evaluate our LLM app?**

Naturally, using too few samples for evaluation can lead to misleading conclusions. For example, 5-10 examples are insufficient for capturing meaningful patterns, while 30-50 examples provide a reasonable starting point for evaluation.

Ideally, a dataset of over 400 samples ensures a more comprehensive assessment, helping to uncover biases and edge cases.

#### What else should be monitored along the LLM outputs?

Beyond output quality, **system performance metrics** like latency, throughput, reliability, and costs should be tracked to ensure scalability.

Additionally, **business metrics**—such as conversion rates, user engagement, or behavior influenced by the assistant—help measure the real-world impact of the LLM application.

#### Popular evaluation tools

Several tools specialize in RAG and LLM evaluation, offering similar capabilities for assessing retrieval quality and model performance.

For RAG evaluation, **RAGAS** is widely used to assess retrieval-augmented models, while **ARES** focuses on measuring how well the retrieved context supports the generated response.

**[Opik](https://github.com/comet-ml/opik)** stands out as an open-source solution that provides structured evaluations, benchmarking, and observability for LLM applications, ensuring assessment transparency and consistency.

Other proprietary alternatives include **Langfuse**, **Langsmith**, which is deeply integrated into the LangChain ecosystem for debugging and evaluation, and **Phoenix**.

---

## 6. Architecting the observability pipeline

​In our observability pipeline, implemented with **[Opik](https://github.com/comet-ml/opik)**, we combine monitoring and evaluation to ensure our application runs smoothly. Monitoring tracks all activities, while evaluation assesses performance and correctness.

#### What’s the interface of the pipeline?

LLMOps observability pipelines consist of two parts: one for monitoring prompts and another for evaluating the RAG module. These pipelines help us track system performance and ensure the application remains reliable.

The **prompt monitoring pipeline** captures entire prompt traces and metadata, such as prompt templates or models used within the chain. It also logs latency and system behavior while providing structured insights through dashboards that help detect and resolve inefficiencies.

The **RAG evaluation pipeline** tests the agentic RAG module using heuristics and LLM judges to assess performance. It receives a set of evaluation prompts and processes them to evaluate accuracy and reasoning quality. The pipeline outputs accuracy assessments, quality scores, and alerts for performance issues, helping maintain system reliability.

We utilize **[Opik](https://github.com/comet-ml/opik)** (by **[Comet ML](https://www.comet.com/site/products/ml-experiment-tracking?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)**), an open-source platform, to handle both the monitoring and evaluation of our application. Opik offers comprehensive tracing, automated evaluations, and production-ready dashboards, making it an ideal choice for our needs.

For evaluation, Opik automates performance assessments using both built-in and custom metrics. Users can define a threshold for any metric and configure alerts for immediate intervention if performance falls below the set value.

Now that we have an overview of the interfaces and components let’s dive into more details about each of the 2 pipelines.

#### **The prompt monitoring pipeline**

This component logs and monitors prompt traces. Prompt monitoring is essential to understand how our application interacts with users and identify areas for improvement. By tracking prompts and responses, we can debug issues in LLM reasoning or other issues like latency and costs.

Opik enables us to monitor latency across every phase of the generation process—pre-generation, generation, and post-generation—ensuring our application responds promptly to user inputs. ​

Latency is crucial to the user experience, as it includes multiple factors such as Time to First Token (TTFT), Time Between Tokens (TBT), Tokens Per Second (TPS), and Total Latency. Tracking these metrics helps us optimize response generation and manage hosting costs effectively.

Figure 5 provides an overview of how **[Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)** logs and tracks prompt traces, helping us analyze inputs, outputs, and execution times for better performance monitoring.

https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons

You can **[visualize](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)** details of the execution flow of a prompt, including its input, output, and latency at each step, as displayed in Figure 6. It helps us track the steps taken during processing, analyze latency at each stage, and identify potential inefficiencies.

https://substackcdn.com/image/fetch/$s_!qZDa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49ea5358-cfbd-4c22-80fb-e57555c9f5e4_2538x1356.png

Finally, in Figure 7, we can also **[visualize](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)** key metadata like retrieval parameters, system prompts, and model settings, providing deeper insights into prompt execution context:

https://substackcdn.com/image/fetch/$s_!3qUW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06a65f34-04cd-4daf-9044-6ff24083ce35_2522x1726.png

For more details on observability with Opik, check out their [documentation](https://www.comet.com/docs/opik/tracing/log_traces?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons):

[MORE ON OBSERVABILITY WITH OPIK](https://www.comet.com/docs/opik/tracing/log_traces?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)

The last step is to understand the RAG evaluation pipeline.

#### **The RAG evaluation pipeline**

As previously mentioned, the RAG evaluation pipeline assesses the performance of our agentic RAG module, which performs application/RAG evaluation.

The pipeline uses built-in heuristics such as Hallucination, Answer Relevance, and Moderation to evaluate response quality. Additionally, we define and integrate a custom metric and LLM judge, which assesses if the LLM's output has appropriate length and density.

This flow can also run as an offline batch pipeline during development to assess performance on test sets. Additionally, it integrates into the CI/CD pipeline to test the RAG application before deployment, ensuring any issues are identified early (similar to integration tests).

Post-deployment, it can run on a schedule to evaluate random samples from production, maintaining consistent application performance. If metrics fall below a certain threshold, we can hook an alarm system that notifies us to address potential issues promptly.

Figure 8 illustrates the results of an evaluation experiment conducted on our RAG module. It displays both the built-in and the custom performance metrics configured by us.

https://substackcdn.com/image/fetch/$s_!S27v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddae553e-205c-4c68-98a4-e52a9281c7bc_2908x1096.png

**[Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)** allows us to compare multiple experiments side by side. This comparison helps track performance trends over time, making refining and improving our models easier.

https://substackcdn.com/image/fetch/$s_!Dj6n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca348d2f-f918-4c2e-9868-ad82b8f6bde1_2912x1064.png

By implementing these components with Opik, we maintain a robust observability pipeline that ensures our application operates efficiently.

---

## 7. Implementing the agentic RAG module

Now that we’ve understood what it takes to build the agentic RAG and observability pipelines, let’s start implementing them.

The agentic RAG module is implemented using the SmolAgents Hugging Face frame, to build an agent that utilizes three key tools: the MongoDB retriever, the summarizer, and the "What Can I Do" tool.

Since prompt monitoring is closely tied to agent execution, here we will also cover how the system logs input/output data, latency, and other key details for each tool, ensuring full observability with Opik.

#### Building the agent

The core of our agentic RAG module starts with `get_agent()`, a method responsible for initializing the agent:

```python
def get_agent(retriever_config_path: Path) -> "AgentWrapper":
    agent = AgentWrapper.build_from_smolagents(
        retriever_config_path=retriever_config_path
    )
    return agent
```

This function builds an `AgentWrapper`, which is a custom class we implemented that extends the agent's functionality by incorporating Opik for tracking all the agent’s interactions.

Building the agent requires a retriever configuration to create the MongoDB retriever tool. As a reminder from Lesson 5, we support multiple retrieval strategies based on retriever type (e.g., parent or contextual), embedding models, and other parameters.

#### Wrapping the agent for monitoring

The `AgentWrapper` class extends the base agent to incorporate metadata tracking with Opik. This ensures that every action taken by the agent is logged and traceable:

```python
class AgentWrapper:
    def __init__(self, agent: MultiStepAgent) -> None:
        self.__agent = agent

    @property
    def input_messages(self) -> list[dict]:
        return self.__agent.input_messages

    @property
    def agent_name(self) -> str:
        return self.__agent.agent_name

    @property
    def max_steps(self) -> str:
        return self.__agent.max_steps
```

We use composition to wrap the `MultiStepAgent` from SmolAgents and expose its properties. The `MultiStepAgent` enables our agent to execute multi-step reasoning and decision-making processes.

Next, we define a method to build the agent, specifying the retriever configuration and integrating the 3 tools necessary for execution:

```python
@classmethod
def build_from_smolagents(cls, retriever_config_path: Path) -> "AgentWrapper":
    retriever_tool = MongoDBRetrieverTool(config_path=retriever_config_path)
    if settings.USE_HUGGINGFACE_DEDICATED_ENDPOINT:
        logger.warning(
            f"Using Hugging Face dedicated endpoint as the summarizer with URL: {settings.HUGGINGFACE_DEDICATED_ENDPOINT}"
        )
        summarizer_tool = HuggingFaceEndpointSummarizerTool()
    else:
        logger.warning(
            f"Using OpenAI as the summarizer with model: {settings.OPENAI_MODEL_ID}"
        )
        summarizer_tool = OpenAISummarizerTool(stream=False)

    model = LiteLLMModel(
        model_id=settings.OPENAI_MODEL_ID,
        api_base="https://api.openai.com/v1",
        api_key=settings.OPENAI_API_KEY,
    )

    agent = ToolCallingAgent(
        tools=[what_can_i_do, retriever_tool, summarizer_tool],
        model=model,
        max_steps=3,
        verbosity_level=2,
    )

    return cls(agent)
```

This method builds the agent by selecting the retriever configuration, which defines how the MongoDB retriever tool is created and configured.

> **It’s critical** that the retriever config matches the one used during the RAG feature pipeline used to populate the MongoDB vector index.

Next, we build the summarizer tool, which can either be the custom model trained in Lesson 4 and deployed on Hugging Face or an OpenAI model, depending on the settings.

After that, we initialize the LiteLLM model, which powers our AI agent.

Finally, all tools, along with the LLM model, are wrapped inside a `ToolCallingAgent` class with a maximum of three reasoning steps, ensuring structured decision-making and controlled execution flow.

Now that our agent is built, we can define its run function:

```python
@opik.track(name="Agent.run")
def run(self, task: str, **kwargs) -> Any:
    result = self.__agent.run(task, **kwargs)

    model = self.__agent.model
    metadata = {
        "system_prompt": self.__agent.system_prompt,
        "system_prompt_template": self.__agent.system_prompt_template,
        "tool_description_template": self.__agent.tool_description_template,
        "tools": self.__agent.tools,
        "model_id": self.__agent.model.model_id,
        "api_base": self.__agent.model.api_base,
        "input_token_count": model.last_input_token_count,
        "output_token_count": model.last_output_token_count,
    }
    if hasattr(self.__agent, "step_number"):
        metadata["step_number"] = self.__agent.step_number
    opik_context.update_current_trace(
        tags=["agent"],
        metadata=metadata,
    )

    return result
```

The `run` method tracks every execution of the agent using Opik’s `@track()` decorator. It logs key metadata, including the system prompt, tool descriptions, model details, and token counts within the current trace.

Having the skeleton of our agent in place, we can dig into each of the 3 tools that our model calls.

#### Building the MongoDB retriever tool

The first tool integrated is the `MongoDBRetrieverTool`, which allows the agent to find relevant documents using semantic search.

It matches a user query to the most relevant stored documents, helping the agent retrieve context when needed.

To integrate the tool with our agent, we must inherit from the `Tool ` class from SmolAgents. We also have to specify the name, description, inputs, and output type that the LLM uses to infer what the tool does and what its interface is. These are critical elements in integrating your tool with an LLM, as they are the only properties used to integrate the tool with the LLM:

```python
class MongoDBRetrieverTool(Tool):
    name = "mongodb_vector_search_retriever"
    description = """Use this tool to search and retrieve relevant documents from a knowledge base using semantic search.
    This tool performs similarity-based search to find the most relevant documents matching the query.
    Best used when you need to:
    - Find specific information from stored documents
    - Get context about a topic
    - Research historical data or documentation
    The tool will return multiple relevant document snippets."""

    inputs = {
        "query": {
            "type": "string",
            "description": """The search query to find relevant documents for using semantic search.
            Should be a clear, specific question or statement about the information you're looking for.""",
        }
    }
    output_type = "string"

    def __init__(self, config_path: Path, **kwargs):
        super().__init__(**kwargs)

        self.config_path = config_path
        self.retriever = self.__load_retriever(config_path)

    def __load_retriever(self, config_path: Path):
        config = yaml.safe_load(config_path.read_text())
        config = config["parameters"]

        return get_retriever(
            embedding_model_id=config["embedding_model_id"],
            embedding_model_type=config["embedding_model_type"],
            retriever_type=config["retriever_type"],
            k=5,
            device=config["device"],
        )
```

The retriever tool is initialized with parameters from one of the retriever config files defined in Lesson 5. The settings include essential parameters such as the embedding model and retrieval type.

Now, we get to the core part of the tool, which is the `forward` method. This method is called when the AI agent uses the tool to search for information.

```python
@track(name="MongoDBRetrieverTool.forward")
def forward(self, query: str) -> str:
    if hasattr(self.retriever, "search_kwargs"):
        search_kwargs = self.retriever.search_kwargs
    else:
        try:
            search_kwargs = {
                "fulltext_penalty": self.retriever.fulltext_penalty,
                "vector_score_penalty": self.retriever.vector_penalty,
                "top_k": self.retriever.top_k,
            }
        except AttributeError:
            logger.warning("Could not extract search kwargs from retriever.")

            search_kwargs = {}

    opik_context.update_current_trace(
        tags=["agent"],
        metadata={
            "search": search_kwargs,
            "embedding_model_id": self.retriever.vectorstore.embeddings.model,
        },
    )

    try:
        query = self.__parse_query(query)
        relevant_docs = self.retriever.invoke(query)

        formatted_docs = []
        for i, doc in enumerate(relevant_docs, 1):
            formatted_docs.append(
                f"""
<document id="{i}">
<title>{doc.metadata.get("title")}</title>
<url>{doc.metadata.get("url")}</url>
<content>{doc.page_content.strip()}</content>
</document>
"""
            )

        result = "\n".join(formatted_docs)
        result = f"""
<search_results>
{result}
</search_results>
When using context from any document, also include the document URL as reference, which is found in the <url> tag.
"""
        return result
    except Exception:
        logger.opt(exception=True).debug("Error retrieving documents.")

        return "Error retrieving documents."
```

In this code snippet, we search for documents that match the query and format them in an XML-like structure. Each document includes a title, URL, and content. Additionally, the results are wrapped in tags to make them easy for the AI agent to read.

#### Creating the summarizer tool

In our agentic RAG module, we provide two summarization options: one using Hugging Face’s API and another using OpenAI’s models. Both tools inherit from `Tool` in SmolAgents and are tracked by Opik, ensuring that every summarization step is logged and monitored.

The first option for summarization is the Hugging Face endpoint-based summarizer.

```python
class HuggingFaceEndpointSummarizerTool(Tool):
    name = "huggingface_summarizer"
    description = """Use this tool to summarize a piece of text. Especially useful when you need to summarize a document."""

    inputs = {
        "text": {
            "type": "string",
            "description": """The text to summarize.""",
        }
    }
    output_type = "string"

    SYSTEM_PROMPT = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
You are a helpful assistant specialized in summarizing documents. Generate a concise TL;DR summary in markdown format having a maximum of 512 characters of the key findings from the provided documents, highlighting the most significant insights

### Input:
{content}

### Response:
"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        assert settings.HUGGINGFACE_ACCESS_TOKEN is not None, (
            "HUGGINGFACE_ACCESS_TOKEN is required to use the dedicated endpoint. Add it to the .env file."
        )
        assert settings.HUGGINGFACE_DEDICATED_ENDPOINT is not None, (
            "HUGGINGFACE_DEDICATED_ENDPOINT is required to use the dedicated endpoint. Add it to the .env file."
        )

        self.__client = OpenAI(
            base_url=settings.HUGGINGFACE_DEDICATED_ENDPOINT,
            api_key=settings.HUGGINGFACE_ACCESS_TOKEN,
        )

@track
def forward(self, text: str) -> str:
    result = self.__client.chat.completions.create(
        model="tgi",
        messages=[
            {
                "role": "user",
                "content": self.SYSTEM_PROMPT.format(content=text),
            },
        ],
    )

    return result.choices[0].message.content
```

This function sends the input text to the Hugging Face API, applying the predefined system prompt. The generated response is then returned, providing a structured summary.

The second summarization option uses OpenAI’s models to generate summaries.

```python
class OpenAISummarizerTool(Tool):
    name = "openai_summarizer"
    description = """Use this tool to summarize a piece of text. Especially useful when you need to summarize a document or a list of documents."""

    inputs = {
        "text": {
            "type": "string",
            "description": """The text to summarize.""",
        }
    }
    output_type = "string"

    SYSTEM_PROMPT = """You are a helpful assistant specialized in summarizing documents.
Your task is to create a clear, concise TL;DR summary in plain text.
Things to keep in mind while summarizing:
- titles of sections and sub-sections
- tags such as Generative AI, LLMs, etc.
- entities such as persons, organizations, processes, people, etc.
- the style such as the type, sentiment and writing style of the document
- the main findings and insights while preserving key information and main ideas
- ignore any irrelevant information such as cookie policies, privacy policies, HTTP errors,etc.

Document content:
{content}

Generate a concise summary of the key findings from the provided documents, highlighting the most significant insights and implications.
Return the document in plain text format regardless of the original format.
"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__client = OpenAI(
            base_url="https://api.openai.com/v1",
            api_key=settings.OPENAI_API_KEY,
        )
```

Note that because the Hugging Face model was fine-tuned on summarizing documents, it doesn't require careful prompt engineering for the desired results (it has the logic embedded into it), resulting in fewer tokens/requests, which translates to lower costs and better latencies.

#### The "What Can I Do" tool

The third and last integrated tool is the "What Can I Do" tool, which provides a list of available capabilities within the Second Brain assistant and helps users explore relevant topics.

```python
@opik.track(name="what_can_i_do")
@tool
def what_can_i_do(question: str) -> str:
    """Returns a comprehensive list of available capabilities and topics in the Second Brain system.

    This tool should be used when:
    - The user explicitly asks what the system can do
    - The user asks about available features or capabilities
    - The user seems unsure about what questions they can ask
    - The user wants to explore the system's knowledge areas

    This tool should NOT be used when:
    - The user asks a specific technical question
    - The user already knows what they want to learn about
    - The question is about a specific topic covered in the knowledge base

    Args:
        question: The user's query about system capabilities. While this parameter is required,
                 the function returns a standard capability list regardless of the specific question.

    Returns:
        str: A formatted string containing categorized lists of example questions and topics
             that users can explore within the Second Brain system.

    Examples:
        >>> what_can_i_do("What can this system do?")
        >>> what_can_i_do("What kind of questions can I ask?")
        >>> what_can_i_do("Help me understand what I can learn here")
    """

    return """
You can ask questions about the content in your Second Brain, such as:

Architecture and Systems:
- What is the feature/training/inference (FTI) architecture?
- How do agentic systems work?
- Detail how does agent memory work in agentic applications?

LLM Technology:
- What are LLMs?
- What is BERT (Bidirectional Encoder Representations from Transformers)?
- Detail how does RLHF (Reinforcement Learning from Human Feedback) work?
- What are the top LLM frameworks for building applications?
- Write me a paragraph on how can I optimize LLMs during inference?

RAG and Document Processing:
- What tools are available for processing PDFs for LLMs and RAG?
- What's the difference between vector databases and vector indices?
- How does document chunk overlap affect RAG performance?
- What is chunk reranking and why is it important?
- What are advanced RAG techniques for optimization?
- How can RAG pipelines be evaluated?

Learning Resources:
- Can you recommend courses on LLMs and RAG?
"""
```

This tool is useful when users are unsure about what they can ask or want to explore different capabilities within the system. Like other tools, it is tracked by Opik for monitoring and observability.

https://substackcdn.com/image/fetch/$s_!77pD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F224265c3-6fd2-4b64-ac1e-39630ab9df4a_2522x1726.png

Here, we can see that the agent calls the MongoDB retriever tool, which in turn invokes the `forward` function. Each step is logged with latency values, providing insight into execution times at different stages.

Furthermore, all metadata related to the trace—including the system prompt, tool configurations, and token usage—is captured to ensure complete observability.

---

## 8. Building the LLM evaluation pipeline

Now that we have implemented the agentic RAG module, we need a structured way to evaluate its performance. This is where the **LLM evaluation pipeline** comes in, ensuring that our agentic RAG module consistently meets quality and reliability standards.

The evaluation pipeline is built using Opik, which helps us log, analyze, and score the agent’s responses. We will focus strictly on Opik's evaluation logic and how it tracks our agent’s outputs.

Before evaluating our agent, we first need to gather a suitable evaluation dataset. This dataset will help us consistently test performance and track improvements

#### Creating the evaluation dataset

To evaluate the agent properly, we use a dataset of ~30 predefined prompts that cover various scenarios the agent might encounter. This dataset allows us to consistently test our agent’s performance across different iterations, ensuring that changes do not degrade its capabilities.

```python
EVALUATION_PROMPTS: List[str] = [
    """\
Write me a paragraph on the feature/training/inference (FTI) pipelines architecture following the next structure:\
\
- introduction\
- what are its main components\
- why it's powerful\
\
Retrieve the sources when compiling the answer. Also, return the sources you used as context.\
""",
    "What is the feature/training/inference (FTI) pipelines architecture?",
    "What is the Tensorflow Recommenders Python package?",
    """How does RLHF: Reinforcement Learning from Human Feedback work?\
\
Explain to me:\
- what is RLHF\
- how it works\
- why it's important\
- what are the main components\
- what are the main challenges\
""",
    "List 3 LLM frameworks for building LLM applications and why they are important.",
    "Explain how does Bidirectional Encoder Representations from Transformers (BERT) work. Focus on what architecture it uses, how it's different from other models and how they are trained.",
    "List 5 ways or tools to process PDFs for LLMs and RAG",
    """How can I optimize my LLMs during inference?\
\
Provide a list of top 3 best practices, while providing a short explanation for each, which contains why it's important.\
""",
    "Explain to me in more detail how does an Agent memory work and why do we need it when building Agentic apps.",
    "What is the difference between a vector database and a vector index?",
    "Recommend me a course on LLMs and RAG",
    "How Document Chunk overlap affects a RAG pipeline and it's performance?",
    """What is the importance of reranking chunks for RAG?\
Explain to me:\
- what is reranking\
- how it works\
- why it's important\
- what are the main components\
- what are the main trade-offs\
""",
    "List the most popular advanced RAG techniques to optimize RAG performance and why they are important.",
    "List what are the main ways of evaluating a RAG pipeline and why they are important.",
]
```

We could have added more samples, but for the first iteration, having 30 samples is a sweet spot. The core idea is to expand this split with edge case samples you find while developing the application.

We use Opik to store and manage the dataset, as shown in the following code:

```python
def get_or_create_dataset(name: str, prompts: list[str]) -> opik.Dataset | None:
    client = opik.Opik()
    try:
        dataset = client.get_dataset(name=name)
    except Exception:
        dataset = None

    if dataset:
        logger.warning(f"Dataset '{name}' already exists. Skipping dataset creation.")

        return dataset

    assert prompts, "Prompts are required to create a dataset."

    dataset_items = []
    for prompt in prompts:
        dataset_items.append(
            {
                "input": prompt,
            }
        )

    dataset = create_dataset(
        name=name,
        description="Dataset for evaluating the agentic app.",
        items=dataset_items,
    )

    return dataset
```

#### Evaluating the agent

The core of the evaluation pipeline is the `evaluate_agent()` function. This function runs the set of predefined prompts through our agent and scores its responses using a combination of built-in and custom metrics.

```python
def evaluate_agent(prompts: list[str], retriever_config_path: Path) -> None:
    assert settings.COMET_API_KEY, (
        "COMET_API_KEY is not set. We need it to track the experiment with Opik."
    )

    logger.info("Starting evaluation...")
    logger.info(f"Evaluating agent with {len(prompts)} prompts.")

    def evaluation_task(x: dict) -> dict:
        """Call agentic app logic to evaluate."""
        agent = agents.get_agent(retriever_config_path=retriever_config_path)
        response = agent.run(x["input"])
        context = extract_tool_responses(agent)

        return {
            "input": x["input"],
            "context": context,
            "output": response,
        }
```

In this code section, we first ensure that Opik can log the experiment by asserting that the necessary API keys are set.

Then, we define the `evaluation_task()`, a method that retrieves an instance of our agent, runs an input prompt through it, and captures both the output and retrieval context.

Before running the actual evaluation, we either fetch an existing dataset or create a new one to store our evaluation prompts:

```python
# Get or create dataset
dataset_name = "second_brain_rag_agentic_app_evaluation_dataset"
dataset = opik_utils.get_or_create_dataset(name=dataset_name, prompts=prompts)
```

Once the dataset is set up, we retrieve our agent instance and configure the experiment. The `experiment_config` dictionary defines key parameters for tracking and logging the evaluation:

```python
# Evaluate
agent = agents.get_agent(retriever_config_path=retriever_config_path)
experiment_config = {
    "model_id": settings.OPENAI_MODEL_ID,
    "retriever_config_path": retriever_config_path,
    "agent_config": {
        "max_steps": agent.max_steps,
        "agent_name": agent.agent_name,
    },
}
```

Next, we define the scoring metrics used to evaluate the agent's performance. Opik provides built-in evaluation metrics, but we also include custom ones for deeper analysis.

```python
scoring_metrics = [
    Hallucination(),
    AnswerRelevance(),
    Moderation(),
    SummaryDensityHeuristic(),
    SummaryDensityJudge(),
]
```

> For **more details on the metrics above** or on how to build custom metrics, check out [Opik’s docs](https://www.comet.com/docs/opik/evaluation/metrics/overview?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons).

In addition to these built-in Opik metrics, we include two custom components. Both compute the response density (whether the answer is too long or too short) but with different techniques: heuristics or LLM-as-Judges. This is a good example of understanding the difference between the two.

- **SummaryDensityHeuristic**: Evaluates whether a response is too short, too long, or appropriately balanced.
- **SummaryDensityJudge**: Uses an external LLM to judge response density and conciseness.

Finally, we execute the evaluation process using the metrics defined and our evaluation dataset:

```python
if dataset:
    evaluate(
        dataset=dataset,
        task=evaluation_task,
        scoring_metrics=scoring_metrics,
        experiment_config=experiment_config,
        task_threads=2,
    )
else:
    logger.error("Can't run the evaluation as the dataset items are empty.")
```

This code ensures that evaluation runs only when a dataset is available. The `evaluate()` function runs the agent using the `evaluation_task()` method on the evaluation dataset and measures the defined scoring metrics. The [results are then logged in Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons) for further analysis and comparison.

[MORE ON OPIK'S METRICS](https://www.comet.com/docs/opik/evaluation/metrics/overview?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)

---

## 9. Running the code

The best way to set up and run the code is through our **[GitHub repository](https://github.com/decodingml/second-brain-ai-assistant-course/tree/main)**, where we have documented everything you need. We will keep the end-to-end instructions only in our GitHub to avoid having the documentation scattered throughout too many places (which is a pain to maintain and use).

First, you have to ensure that your MongoDB Docker container is running and that your RAG collection is populated.

Next, you can run the agent through the command-line interface (CLI) for a quick test or with a Gradio UI for a more interactive experience.

To quickly test the Agentic RAG inference on a predefined query, you can run the following command from the CLI:

```bash
make run_agent_query RETRIEVER_CONFIG=configs/compute_rag_vector_index_openai_parent.yaml
```

> _**Note**: The retriever config can be any of the ones defined in Lesson 5, depending on the retrieval strategy you want to use (but they have to match, between the RAG feature pipeline and the inference pipeline)._

For a more interactive experience, you can launch the Gradio UI by executing:

```bash
make run_agent_app RETRIEVER_CONFIG=configs/compute_rag_vector_index_openai_parent.yaml
```

Additionally, if you want to evaluate the agent’s performance, run the evaluation pipeline using:

```bash
make evaluate_agent RETRIEVER_CONFIG=configs/compute_rag_vector_index_openai_parent.yaml
```

All the runs, including inference and evaluation, can be tracked directly from the [Opik dashboards](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons), providing insights into performance and enabling better monitoring of experiments.

For the whole setup and running guide, go to our [GitHub](https://github.com/decodingml/second-brain-ai-assistant-course/tree/main/apps/second-brain-online):

[GO TO GITHUB](https://github.com/decodingml/second-brain-ai-assistant-course/tree/main/apps/second-brain-online)

---

## Conclusion

This was a long lesson—if you're still here, you’ve made it to the end of the **Building Your Second Brain AI Assistant** course. Congrats!

Throughout this lesson, we explored **LLM-powered agents** and how they differ from traditional workflows.

We designed and implemented the Agentic RAG module, integrating **[SmolAgents](https://github.com/huggingface/smolagents)**, **[Gradio](https://www.gradio.app/)**, and **[MongoDB](https://www.mongodb.com/products/platform/atlas-vector-search?utm_campaign=ai-pilot&utm_medium=creator&utm_term=iusztin&utm_source=blog)** to enable dynamic retrieval and reasoning. We then built an observability pipeline using **[Opik](https://github.com/comet-ml/opik)**, ensuring full monitoring and evaluation of our agentic system.

Beyond implementation, we focused on evaluating and improving the agent's performance. We explored prompt monitoring, latency tracking, and response evaluation using built-in and custom metrics, including heuristic-based scoring and LLM-as-a-judge techniques.

With this final lesson, you now have a complete, end-to-end understanding of **architecting, building, and evaluating LLM-powered AI assistants**.

If you haven’t read all the lessons from the Second Brain AI Assistant open-source course, consider starting with **[Lesson 1](https://decodingml.substack.com/p/build-your-second-brain-ai-assistant)** on architecting the end-to-end LLM system.

> 💻 Explore all the lessons and the code in our freely available **[GitHub repository](https://github.com/decodingml/second-brain-ai-assistant-course).**

If you have questions or need clarification, **feel free to ask**. See you in the next session!

</details>

<details>
<summary>building-effective-ai-agents-anthropic</summary>

# Building effective agents

Published Dec 19, 2024

We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks.

Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.

In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents.

## What are agents?

"Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as **agentic systems**, but draw an important architectural distinction between **workflows** and **agents**:

- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems.

## When (and when not) to use agents

When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.

## When and how to use frameworks

There are many frameworks that make agentic systems easier to implement, including:

- [LangGraph](https://langchain-ai.github.io/langgraph/) from LangChain;
- Amazon Bedrock's [AI Agent framework](https://aws.amazon.com/bedrock/agents/);
- [Rivet](https://rivet.ironcladapp.com/), a drag and drop GUI LLM workflow builder; and
- [Vellum](https://www.vellum.ai/), another GUI tool for building and testing complex workflows.

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

See our [cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents) for some sample implementations.

## Building blocks, workflows, and agents

In this section, we’ll explore the common patterns for agentic systems we’ve seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents.

### Building block: The augmented LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), which allows developers to integrate with a growing ecosystem of third-party tools with a simple [client implementation](https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients).

For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities.

### Workflow: Prompt chaining

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.

**When to use this workflow:** This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

**Examples where prompt chaining is useful:**

- Generating Marketing copy, then translating it into a different language.
- Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.

### Workflow: Routing

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

**When to use this workflow:** Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

**Examples where routing is useful:**

- Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
- Routing easy/common questions to smaller models like Claude 3.5 Haiku and hard/unusual questions to more capable models like Claude 3.5 Sonnet to optimize cost and speed.

### Workflow: Parallelization

LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting:** Running the same task multiple times to get diverse outputs.

**When to use this workflow:** Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

**Examples where parallelization is useful:**

- **Sectioning**:
  - Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response.
  - Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model’s performance on a given prompt.
- **Voting**:
  - Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem.
  - Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives.

### Workflow: Orchestrator-workers

In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

**When to use this workflow:** This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**Example where orchestrator-workers is useful:**

- Coding products that make complex changes to multiple files each time.
- Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information.

### Workflow: Evaluator-optimizer

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

**When to use this workflow:** This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

**Examples where evaluator-optimizer is useful:**

- Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques.
- Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted.

### Agents

Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 ("Prompt Engineering your Tools").

**When to use agents:** Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

**Examples where agents are useful:**

The following examples are from our own implementations:

- A coding Agent to resolve [SWE-bench tasks](https://www.anthropic.com/research/swe-bench-sonnet), which involve edits to many files based on a task description;
- Our [“computer use” reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), where Claude uses a computer to accomplish tasks.

## Combining and customizing these patterns

These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity _only_ when it demonstrably improves outcomes.

## Summary

Success in the LLM space isn't about building the most sophisticated system. It's about building the _right_ system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

When implementing agents, we try to follow three core principles:

1. Maintain **simplicity** in your agent's design.
2. Prioritize **transparency** by explicitly showing the agent’s planning steps.
3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.

Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users.

## Appendix 1: Agents in practice

Our work with customers has revealed two particularly promising applications for AI agents that demonstrate the practical value of the patterns discussed above. Both applications illustrate how agents add the most value for tasks that require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight.

### A. Customer support

Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because:

- Support interactions naturally follow a conversation flow while requiring access to external information and actions;
- Tools can be integrated to pull customer data, order history, and knowledge base articles;
- Actions such as issuing refunds or updating tickets can be handled programmatically; and
- Success can be clearly measured through user-defined resolutions.

Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness.

### B. Coding agents

The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because:

- Code solutions are verifiable through automated tests;
- Agents can iterate on solutions using test results as feedback;
- The problem space is well-defined and structured; and
- Output quality can be measured objectively.

In our own implementation, agents can now solve real GitHub issues in the [SWE-bench Verified](https://www.anthropic.com/research/swe-bench-sonnet) benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.

## Appendix 2: Prompt engineering your tools

No matter which agentic system you're building, tools will likely be an important part of your agent. [Tools](https://www.anthropic.com/news/tool-use-ga) enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a [tool use block](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#example-api-response-with-a-tool-use-content-block) in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools.

There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes.

Our suggestions for deciding on tool formats are the following:

- Give the model enough tokens to "think" before it writes itself into a corner.
- Keep the format close to what the model has seen naturally occurring in text on the internet.
- Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.

One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good _agent_-computer interfaces (ACI). Here are some thoughts on how to do so:

- Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it’s probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools.
- How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools.
- Test how the model uses your tools: Run many example inputs in our [workbench](https://console.anthropic.com/workbench) to see what mistakes the model makes, and iterate.
- [Poka-yoke](https://en.wikipedia.org/wiki/Poka-yoke) your tools. Change the arguments so that it is harder to make mistakes.

While building our agent for [SWE-bench](https://www.anthropic.com/research/swe-bench-sonnet), we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.

</details>

<details>
<summary>google-announces-gemini-cli-your-open-source-ai-agent</summary>

# Gemini CLI: your open-source AI agent

Jun 25, 2025

Free and open source, Gemini CLI brings Gemini directly into developers’ terminals — with unmatched access for individuals.

https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_CLI_Hero_Final.width-200.format-webp.webp

Gemini CLI

For developers, the command line interface (CLI) isn't just a tool; it's home. The terminal’s efficiency, ubiquity and portability make it the go-to utility for getting work done. And as developers' reliance on the terminal endures, so does the demand for integrated AI assistance.

That’s why we’re introducing [Gemini CLI](http://github.com/google-gemini/gemini-cli), an open-source AI agent that brings the power of Gemini directly into your terminal. It provides lightweight access to Gemini, giving you the most direct path from your prompt to our model. While it excels at coding, we built Gemini CLI to do so much more. It’s a versatile, local utility you can use for a wide range of tasks, from content generation and problem solving to deep research and task management.

We’ve also integrated Gemini CLI with Google’s AI coding assistant, [Gemini Code Assist](https://codeassist.google/), so that all developers — on free, Standard, and Enterprise Code Assist plans — get prompt-driven, AI-first coding in both VS Code and Gemini CLI.

https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/Gemini_CLI_GIF.gif

## Unmatched usage limits for individual developers

To use Gemini CLI free-of-charge, simply login with a personal Google account to get a free Gemini Code Assist license. That free license gets you access to Gemini 2.5 Pro and its massive 1 million token context window. To ensure you rarely, if ever, hit a limit during this preview, we offer the industry’s largest allowance: 60 model requests per minute and 1,000 requests per day at no charge.

If you’re a professional developer who needs to run multiple agents simultaneously, or if you prefer to use specific models, you can use a [Google AI Studio](https://aistudio.google.com/apikey) or [Vertex AI](https://console.cloud.google.com/vertex-ai/studio/multimodal) key for usage-based billing or get a Gemini Code Assist Standard or Enterprise license.

https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_CLI_infographic.width-1000.format-webp.webp

Gemini CLI offers the industry’s largest usage allowance at 60 model requests per minute and 1,000 model requests per day at no charge

## Powerful models in your command line

Now in preview, Gemini CLI provides powerful AI capabilities, from code understanding and file manipulation to command execution and dynamic troubleshooting. It offers a fundamental upgrade to your command line experience, enabling you to write code, debug issues and streamline your workflow with natural language.

Its power comes from built-in tools allowing you to:

- **Ground prompts with Google Search** so you can fetch web pages and provide real-time, external context to the model
- **Extend Gemini CLI’s capabilities** through built-in support for the Model Context Protocol (MCP) or bundled extensions
- **Customize prompts and instructions** to tailor Gemini for your specific needs and workflows
- **Automate tasks and integrate with existing workflows** by invoking Gemini CLI non-interactively within your scripts

Sorry, your browser doesn't support embedded videos, but don't worry, you can [download it](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/GenMedia_demo_keyword.mp4) and watch it with your favorite video player!

Gemini CLI can be used for a wide variety of tasks, including making a short video showing the story of a ginger cat’s adventures around Australia with Veo and Imagen

## Open and extensible

Because Gemini CLI is fully [open source (Apache 2.0)](https://github.com/google-gemini/gemini-cli/blob/main/LICENSE), developers can inspect the code to understand how it works and verify its security implications. We fully expect (and welcome!) a global community of developers to [contribute to this project](https://github.com/google-gemini/gemini-cli/blob/main/CONTRIBUTING.md) by reporting bugs, suggesting features, continuously improving security practices and submitting code improvements. [Post your issues](http://github.com/google-gemini/gemini-cli/issues) or [submit your ideas](http://github.com/google-gemini/gemini-cli/discussions) in our GitHub repo.

We also built Gemini CLI to be extensible, building on emerging standards like MCP, system prompts (via GEMINI.md) and settings for both personal and team configuration. We know the terminal is a personal space, and everyone deserves the autonomy to make theirs unique.

## Shared technology with Gemini Code Assist

Sometimes, an IDE is the right tool for the job. When that time comes, you want all the capabilities of a powerful AI agent by your side to iterate, learn and overcome issues quickly.

[Gemini Code Assist](https://codeassist.google/), Google’s AI coding assistant for students, hobbyists and professional developers, now shares the same technology with Gemini CLI. In VS Code, you can place any prompt into the chat window using agent mode, and Code Assist will relentlessly work on your behalf to write tests, fix errors, build out features or even migrate your code. Based on your prompt, Code Assist’s agent will build a multi-step plan, auto-recover from failed implementation paths and recommend solutions you may not have even imagined.

Sorry, your browser doesn't support embedded videos, but don't worry, you can [download it](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/gemini_cli_code_assist_demo_cut.mp4) and watch it with your favorite video player!

Gemini Code Assist’s chat agent is a multi-step, collaborative, reasoning agent that expands the capabilities of simple-command response interactions

Gemini Code Assist agent mode is available at no additional cost for all plans (free, Standard and Enterprise) through the [Insiders channel](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#before-you-begin). If you aren’t already using Gemini Code Assist, give it a try. Its free tier has the highest usage limit in the market today, and only takes less than a minute to [get started](https://codeassist.google/).

## Easy to get started

So what are you waiting for? Upgrade your terminal experience with Gemini CLI today. Get [started by installing Gemini CLI.](http://github.com/google-gemini/gemini-cli) All you need is an email address to get Gemini practically unlimited in your terminal.

</details>

<details>
<summary>introducing-operator-openai</summary>

# Introducing Operator

A research preview of an agent that can use its own browser to perform tasks for you. Available to Pro users in the U.S.

Today we’re releasing [Operator⁠(opens in a new window)](https://operator.chatgpt.com/), an agent that can go to the web to perform tasks for you. Using its own browser, it can look at a webpage and interact with it by typing, clicking, and scrolling. **It is currently a research preview**, meaning it has limitations and will evolve based on user feedback. Operator is one of our first agents, which are AIs capable of doing work for you independently—you give it a task and it will execute it.

Operator can be asked to handle a wide variety of repetitive browser tasks such as filling out forms, ordering groceries, and even creating memes. The ability to use the same interfaces and tools that humans interact with on a daily basis broadens the utility of AI, helping people save time on everyday tasks while opening up new engagement opportunities for businesses.

To ensure a safe and iterative rollout, we are starting small. Starting today, Operator is available to [Pro](https://openai.com/chatgpt/pricing/) users in the U.S. at [operator.chatgpt.com⁠(opens in a new window)](https://operator.chatgpt.com/). This research preview allows us to learn from our users and the broader ecosystem, refining and improving as we go. Our plan is to expand to Plus, Team, and Enterprise users and integrate these capabilities into ChatGPT in the future.

## How Operator works

Operator is powered by a new model called [Computer-Using Agent (CUA)](https://openai.com/index/computer-using-agent/). Combining GPT‑4o's vision capabilities with advanced reasoning through reinforcement learning, CUA is trained to interact with graphical user interfaces (GUIs)—the buttons, menus, and text fields people see on a screen.

Operator can “see” (through screenshots) and “interact” (using all the actions a mouse and keyboard allow) with a browser, enabling it to take action on the web without requiring custom API integrations.

If it encounters challenges or makes mistakes, Operator can leverage its reasoning capabilities to self-correct. When it gets stuck and needs assistance, it simply hands control back to the user, ensuring a smooth and collaborative experience.

While CUA is still in early stages and has limitations, it sets new state-of-the-art benchmark results in WebArena and WebVoyager, two key browser use benchmarks. Read more about evals and the research behind Operator in [our research blog post](https://openai.com/index/computer-using-agent/).

## How to use

To get started, simply describe the task you’d like done and Operator can handle the rest. Users can choose to take over control of the remote browser at any point, and Operator is trained to proactively ask the user to take over for tasks that require login, payment details, or when solving CAPTCHAs.

Users can personalize their workflows in Operator by adding custom instructions, either for all sites or for specific ones, such as setting preferences for airlines on Booking.com. Operator lets users save prompts for quick access on the homepage, ideal for repeated tasks like restocking groceries on Instacart. Similar to using multiple tabs on a browser, users can have Operator run multiple tasks simultaneously by creating new conversations, like ordering a personalized enamel mug on Etsy while booking a campsite on Hipcamp.

## Ecosystem & users

[Operator⁠(opens in a new window)](https://operator.chatgpt.com/) transforms AI from a passive tool to an active participant in the digital ecosystem. It will streamline tasks for users and bring the benefits of agents to companies that want innovative customer experiences and desire higher rates of conversion. We’re collaborating with companies like DoorDash, Instacart, OpenTable, Priceline, StubHub, Thumbtack, Uber, and others to ensure Operator addresses real-world needs while respecting established norms. In addition to these collaborations, we see a lot of potential to improve the accessibility and efficiency of certain workflows, particularly in public sector applications. To explore these use cases further, we’re working with organizations like the [City of Stockton⁠(opens in a new window)](https://www.stocktonca.gov/) to make it easier to enroll in city services and programs.

> “As we learn more about Operator during its research preview, we'll be better equipped to identify ways that AI can make civic engagement even easier for our residents.”

Jamil Niazi, Director of Information Technology at City of Stockton

By releasing Operator to a limited audience initially, we aim to learn quickly and refine its capabilities based on real-world feedback, ensuring we balance innovation with trust and safety. This collaborative approach helps ensure Operator delivers meaningful value to users, creators, businesses, and public sector organizations alike.

> “OpenAI's Operator is a technological breakthrough that makes processes like ordering groceries incredibly easy.”

Daniel Danker, Chief Product Officer at Instacart

## Safety and privacy

Ensuring Operator is safe to use is a top priority, with three layers of safeguards to prevent abuse and ensure users are firmly in control.

First, Operator is trained to ensure that the person using it is always in control and asks for input at critical points.

- **Takeover mode:** Operator asks the user to take over when inputting sensitive information into the browser, such as login credentials or payment information. When in takeover mode, Operator does not collect or screenshot information entered by the user.
- **User confirmations**: Before finalizing any significant action, such as submitting an order or sending an email, Operator should ask for approval.
- **Task limitations:** Operator is trained to decline certain sensitive tasks, such as banking transactions or those requiring high-stakes decisions, like making a decision on a job application.
- **Watch mode**: On particularly sensitive sites, such as email or financial services, Operator requires close supervision of its actions, allowing users to directly catch any potential mistakes.

Next, we’ve made it easy to manage data privacy in Operator.

- **Training opt out:** Turning off ‘Improve the model for everyone’ in ChatGPT settings means data in Operator will also not be used to train our models.
- **Transparent data management:** Users can delete all browsing data and log out of all sites with one click under the Privacy section of Operator settings. Past conversations in Operator can also be deleted with one click.

Lastly, we’ve built defenses against adversarial websites that may try to mislead Operator through hidden prompts, malicious code, or phishing attempts:

- **Cautious navigation**: Operator is designed to detect and ignore prompt injections.
- **Monitoring**: A dedicated “monitor model” watches for suspicious behavior and can pause the task if something seems off.
- **Detection pipeline**: Automated and human review processes continuously identify new threats and quickly update safeguards.

We know bad actors may try to misuse this technology. That’s why we’ve designed Operator to refuse harmful requests and block disallowed content. Our moderation systems can issue warnings or even revoke access for repeated violations, and we’ve integrated additional review processes to detect and address misuse. We’re also providing [guidance](https://openai.com/policies/using-operator-in-line-with-our-policies/) on how to interact with Operator in compliance with our [Usage Policies](https://openai.com/policies/usage-policies/).

While Operator is designed with these safeguards, no system is flawless and this is still a research preview; we are committed to continuous improvement through real-world feedback and rigorous testing. For more on our approach, [visit the safety section of the Operator research blog](https://openai.com/index/computer-using-agent/).

## Limitations

Operator is currently in an early research preview, and while it’s already capable of handling a wide range of tasks, it’s still learning, evolving and may make mistakes. For instance, it currently encounters challenges with complex interfaces like creating slideshows or managing calendars. Early user feedback will play a vital role in enhancing its accuracy, reliability, and safety, helping us make Operator better for everyone.

## What's next

**CUA in the API:** We plan to expose the model powering Operator, [CUA](https://openai.com/index/computer-using-agent/), in the API soon so that developers can use it to build their own computer-using agents.

**Enhanced Capabilities:** We’ll continue to improve Operator’s ability to handle longer and more complex workflows.

**Wider Access:** We plan to expand [Operator⁠(opens in a new window)](https://operator.chatgpt.com/) to Plus, Team, and Enterprise users and integrate its capabilities directly into ChatGPT in the future once we are confident in its safety and usability at scale, unlocking seamless real-time and asynchronous task execution.

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

- **Export & Share** \- You can then export the final report to a PDF or document, or convert it into a Perplexity Page and share it with colleagues or friends.


https://framerusercontent.com/images/Lc0634aprN2JYuFLQ8VfKthJnAk.png

### When to Use Deep Research

We built Deep Research to empower everyone to conduct expert-level analysis across a range of complex subject matters. Deep Research excels at creating work artifacts in domains including finance, marketing, and technology, and is equally useful as a personal consultant in areas such as health, product research, and travel planning. Here are a a few examples of how you might use Deep Research on Perplexity.

#### Finance

https://framerusercontent.com/images/trzwsXtuC3j68cIGyUb6k2lLk.png

#### Marketing

https://framerusercontent.com/images/n8ptzcWQs7qIv7JiMDS1ZwJmKA.png

#### Technology

https://framerusercontent.com/images/wRBHkQ4dqR8tLeYql0DyOUdh78.png

#### Current Affairs

https://framerusercontent.com/images/wug2dVncsmdZqLMr6KElOCtglhc.png

#### Health

https://framerusercontent.com/images/Sqc4r85ACZIQZTzC2pJhe1BCQYc.png

#### Biography

https://framerusercontent.com/images/tQO9LIHgnWvalzwrgmmLCVzqT4.png

#### Travel

https://framerusercontent.com/images/ofWFPGvvrYQWaFAr6BOBwOIvpk.png

### Humanity’s Last Exam

Deep Research on Perplexity attains a 21.1% accuracy score on Humanity’s Last Exam, significantly higher than Gemini Thinking, o3-mini, o1, DeepSeek-R1, and many other leading models. [Humanity’s Last Exam⁠](https://lastexam.ai/) is a comprehensive benchmark for AI systems consisting of over 3,000 questions across 100+ subjects ranging from mathematics and science to history and literature.

https://framerusercontent.com/images/hplibuiapLcxAxdbJQWfhnLmiJU.png

### SimpleQA

Scoring 93.9% accuracy on the [SimpleQA](https://arxiv.org/html/2411.04368v1) benchmark — a bank of several thousand questions that test for factuality — Perplexity Deep Research far exceeds the performance of leading models.

https://framerusercontent.com/images/ttftsapj52NTVpjPcXVOj8JfKw.png

### Runtime Stats

Deep Research on Perplexity not only attains high scores on industry benchmarks, but it does so while completing most research tasks in under 3 minutes — which we’re working to make even faster in the future.

https://framerusercontent.com/images/enepaQzuMoqWmDzgU6x5D9ydTqc.png

</details>

<details>
<summary>real-world-gen-ai-use-cases-from-the-world-s-leading-organiz</summary>

Exactly a year ago, we first published this list during Google Cloud Next 24. It numbered 101 entries.

It felt like a lot at the time, and served as a showcase of how much momentum both Google and the industry were seeing around generative AI adoption. In the brief period of gen AI being widely available, organizations of all sizes had begun experimenting with it and putting it into production across their work and across the world, doing so at [a speed rarely seen with new technology](https://cloud.google.com/transform/the-prompt-prototype-to-production-gen-ai).

What a difference a year makes. Our list has grown by 6X. And still, that’s just scratching the surface of what’s becoming possible with AI across the enterprise.

Many of these use cases are coming to life this week at [Google Cloud Next 25](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next25), as we join with these customers and partners and thousands more in Las Vegas and virtually around the globe.

To name just a few: Wendy’s, Papa John’s pizza, and Uber are all managing orders faster, whether that’s at the drive-thru or through their app with predictive AI tools. Mercedes Benz and General Motors have enhanced in-vehicle services while Samsung’s newest phones and even its in-home robot, Ballie, have more responsive features thanks to AI. Financial institutions like Citi, Deutsche Bank, and Intesa Sanpaolo are providing new services securely, monitoring markets faster, and combatting fraud in novel ways.

Given the incredible pace of innovation and progress we continue to see, we are confident that AI will grow beyond even our imagination as our customers continue to challenge us to design, build, deploy, and create value.

Hopefully you find something here that will propel our own AI endeavors together.

* * *

The list is organized by 11 major industry groups, and within those, six agent types: Customer, Employee, Creative, Code, Data, and Security. There are 280 new entries, denoted with an asterisk (\*) before the organization’s name.

Automotive & Logistics

### **Customer Agents**

- **Continental** is using Google's data and AI technologies to develop automotive solutions that are safe, efficient, and user-focused. One of the initial outcomes of this partnership is the integration of Google Cloud's conversational AI technologies into Continental's Smart Cockpit HPC, an in-vehicle speech-command solution.

- **General Motors**’ OnStar has been augmented with new AI features, including a virtual assistant powered by Google Cloud’s conversational AI technologies that are better able to recognize the speaker’s intent.

- \* **MercedesBenz** is providing conversational search and navigation in the new CLA series cars using Google Cloud’s industry-tuned Automotive AI Agent.

- **Mercedes Benz** is infusing e-commerce capabilities into its online storefront with a gen AI-powered smart sales assistant.

- **PODS** worked with the advertising agency Tombras to create the “World’s Smartest Billboard” using Gemini — a campaign on its trucks that could adapt to each neighborhood in New York City, changing in real-time based on data. It hit all 299 neighborhoods in just 29 hours, creating more than 6,000 unique headlines.

- **UPS Capital** launched DeliveryDefense Address Confidence, which uses machine learning and UPS data to provide a confidence score for shippers to help them determine the likelihood of a successful delivery.

- **Volkswagen of America** built a virtual assistant in the myVW app, where drivers can explore their owners’ manuals and ask questions, such as, “How do I change a flat tire?” or “What does this digital cockpit indicator light mean?” Users can also use Gemini’s multimodal capabilities to see helpful information and context on indicator lights simply by pointing their smartphone cameras at the dashboard.


### **Employee Agents**

- **704 Apps** creates applications serving the last-mile transportation segment, connecting thousands of drivers and passengers every day. During trips, the audio content of conversations between car occupants is sent to Gemini, which measures the emotional “temperature." Specific words such as “robbery”, “assault”, “kidnapping”, among others, can be classified as hostile by the tool, generating alerts to anticipate risky situations before they happen.

- **Oxa**, a developer of software for autonomous vehicles, uses Gemini for Google Workspace to build campaign templates for metrics reporting, write social posts in order to make marketing processes more efficient, create job descriptions, and proofread content across all teams, saving time and resources.

- \* **Rivian** uses Google Workspace with Gemini to enhance communication and collaboration across tech and marketing teams, resulting in faster, higher quality work.

- **Toyota** implemented an AI platform using Google Cloud's AI infrastructure to enable factory workers to develop and deploy machine learning models. This led to a reduction of over 10,000 man-hours per year and increased efficiency and productivity.

- **Uber** is using AI agents to help employees be more productive, save time, and be even more effective at work. For customer service representatives, the company launched new tools that summarize communications with users and can even surface context from previous interactions, so front-line staff can be more helpful and effective.

- \*Uber also uses Google Workspace with Gemini to save time on repetitive tasks, free up developers for higher-value work, reduce their agency spending, and to enhance employee retention.


### **Code Agents**

- \* **Renault Group**’s **Ampere**, an EV and software subsidiary created in 2023, is using an enterprise version of Gemini Code Assist, built for teams of developers and able to understand a company’s code base, standards, and conventions.


### **Data Agents**

- **BMW Group**, in collaboration with Monkeyway, developed the AI solution SORDI.ai to optimize industrial planning processes and supply chains with gen AI. This involves scanning assets and using Vertex AI to create 3D models that act as digital twins that perform thousands of simulations to optimize distribution efficiency.

- **Dematic** is using the multimodal features in Vertex AI and Gemini to build end-to-end fulfillment solutions for both ecommerce and omnichannel retailers.

- **Geotab**, a global leader in telematics, uses BigQuery and Vertex AI to analyze billions of data points per day from over 4.6 million vehicles. This enables real-time insights for fleet optimization, driver safety, transportation decarbonization, and macro-scale transportation analytics to drive safer and more sustainable cities.

- **Kinaxis** is building data-driven supply chain solutions to address logistics use cases including scenario modeling, planning, operations management, and automation.

- \* **Nuro**, an autonomous driving company, uses vector search in AlloyDB to enable their vehicles to accurately classify objects encountered on the road.

- \* **Picterra**, which calls itself a search engine for the physical world, adopted Google Kubernetes Engine to power its platform, providing the ability to quickly scale to meet the demands of geospatial AI workloads. With GKE, Picterra can model the terrain of entire countries quickly, even at ultra-high resolutions.

- **Prewave**, a supply chain risk intelligence platform, utilizes Google Cloud's AI services to provide end-to-end risk monitoring and ESG risk detection for businesses. This enables companies to gain transparency deep into their supply chains, ensuring resilience, sustainability, and compliance with regulations like the European CSDDD.

- \* **TruckHouse** specializes in expedition vehicles and speeds inventory tracking with Gemini in Sheets so they can spend more time in the great outdoors.

- **UPS** is building a digital twin of its entire distribution network, so both workers and customers can see where their packages are at any time.

- **Woven** – **Toyota**'s investment in the future of mobility — is partnering with Google to leverage vast amounts of data and AI to enable autonomous driving, supported by thousands of ML workloads on Google Cloud’s AI Hypercomputer. This has resulted in 50% total-cost-of-ownership savings to support automated driving.

Business & Professional Services

### **Customer Agents**

- \* **Accenture** is transforming customer support at a major retailer by offering convenient self-service options through virtual assistants, enhancing the overall customer experience.

- \* **Capgemini** is using Google Cloud to build AI agents that help optimize the ecommerce experience by helping retailers accept customer orders through new revenue channels and accelerate the order-to-cash process for digital stores.

- \* **Deloitte** offers a “Care Finder” agent, built with Google Cloud, as part of its Agent Fleet. The agent helps care seekers find in-network providers — often in less than a minute — significantly faster than the average call time of five to eight minutes.

- **Ferret.ai** uses AI to offer insights about the backgrounds of people in a user's personal and professional network, providing a curated relationship intelligence and monitoring solution for its users — increasingly important services in a world of growing reputational risks.

- \* **Intuit**, the makers of TurboTax, integrated Google Cloud’s visual recognition platform, Doc AI, and Gemini models into Intuit’s proprietary GenOS. This will expand the capabilities of Intuit’s “done-for-you” autofill of tax returns across the ten most common U.S. tax forms (variations of the 1099 and 1040 forms), helping users save time and boosting accuracy.

- \* **Stax AI**, which aims to revolutionize retirement planning with AI, uses MongoDB Atlas and Vertex AI to automate its manual processes and transform massive volumes of trust accounting data in minutes.

- **Sutherland**, a leading digital transformation company, is focused on bringing together human expertise and AI, including boosting its client-facing teams by automatically surfacing suggested responses and automating insights in real time.

- \* **Wagestream**, a financial wellbeing platform for employee benefits, is using Gemini models to handle more than 80% of its internal customer inquiries, including questions about payment dates, balances, and more.

- \* **WealthAPI**, the leading provider of wealth management interfaces in Germany, uses Gemini and DataStax Astra DB to deliver next-gen financial insights in real time to millions of customers for personalized guidance at scale.


### **Employee Agents**

- **Allegis Group**, a global leader in talent solutions, partnered with TEKsystems to implement AI models to streamline its recruitment process, including automating tasks such as updating candidate profiles, generating job descriptions, and analyzing recruiter-candidate interactions. The implementation resulted in significant improvements in recruiter efficiency and a reduction in technical debt.

- \* **BCG** uses Google Cloud to provide a sales optimization tool that improves the effectiveness and impact of insurance advisors.

- **Cintas** is using Vertex AI Search to develop an internal knowledge center for customer service and sales teams to easily find key information.

- \* **Beyond** is a technology consultancy that guides their clients through transformational journeys to unlock the potential of AI and cloud-based technology. Google Workspace with Gemini helps them reduce the time from project brief to project kickoff from months to weeks, and the time for first drafts of RFI responses from days to minutes.

- **Dun & Bradstreet**, a business research and intelligence service, built an email-generation tool with Gemini that helps sellers create tailored, personalized communications to prospects and customers for its research services. The company also developed intelligent search capabilities to help users with complex queries like, "Find me all the companies in this area with a high ESG rating."

- \* **Cognizant** used Vertex AI and Gemini built an AI agent to help legal teams draft contracts, assign risk scores and make recommendations for ways to optimize operational impact.

- \* **Equifax** adopted Google Workspace, launching a strategic change management campaign to ensure a smooth transition across more than 20 countries in one weekend. Workspace’s suite of Gemini-powered tools for communication, collaboration, and productivity offered a comprehensive and user-friendly solution that could be easily embraced by Equifax employees at all levels.

- \* **Finnt**, part of the Google for Startups Cloud AI Accelerator, provides AI automation solutions for corporate finance teams, helping to cut accounting procedures time by 90%, boost accuracy, and unlock unique insights.

- **Flashpoint** is improving efficiency and productivity across its workforce, using Google Workspace to communicate and collaborate more effectively, maximize ROI, and increase employee satisfaction, so they can dedicate more time to keeping customers secure.

- **Fluna**, a Brazilian digital services company, has automated the analysis and drafting of legal agreements using Vertex AI, Document AI, and Gemini 1.5 Pro, achieving an accuracy of 92% in data extraction while ensuring security and reliability for sensitive information.

- \* **FreshFields**, a global law firm, will roll out Gemini with Google Workspace across its practice and will also create groundbreaking AI products and bespoke AI agents to transform processes in the highly regulated legal industry.

- \* **Joe the Architect**, a 25-person architecture firm, catches up on long email chains with Gemini in Gmail to keep track of client needs across dozens of conversations.

- \* **KPMG** is building Google AI into their newly formed KPMG Law firm, as well as driving AI transformation within the banking industry, and the company is also implementing Agentspace to enhance its own workplace operations.

- **L+R**, a design and technology agency, leverages Gemini for Google Workspace Workspace to elevate performance and precision, streamlining workflows and empowering its team to achieve more impactful results.

- **Monks** used Google Gemini to help Hatch build a personalized ad campaign. The campaign delivered an 80% improved click-through rate, 46% more engaged site visitors, and a 31% improved cost-per-purchase over other campaigns. On top of this, by using AI the team was able to deliver the campaign much more efficiently, reducing time to investment by 50% and costs by 97%.

- **Own Your Brand** founder Lauren Magenta uses Google Workspace to run her business and Gemini for Google Workspace is transforming how she manages enrollment. Gemini helps her quickly draft personalized emails to potential clients in her own voice.

- **Randstad**, a large HR services and talent provider, is using Gemini for Workspace across its organization to transform its work culture, leading to a more culturally diverse and inclusive workplace that’s seen a double-digit reduction in sick days.

- \* **Sulamérica** adopted Google Workspace a decade ago to make collaboration among employees more agile, intuitive, and fluid. The insurance company recently started using Gemini in Workspace, making it available to 1,250 employees to increase operational efficiency, security, and productivity.

- \* **UKG**, an HR and workforce management solutions provider, enhances the workplace experience with UKG Bryte AI, a trusted conversational agent built with Google Cloud that enables HR administrators and people managers to request information about company policies, business insights, and more.


### **Creative Agents**

- **Agoda** is a digital travel platform that helps travelers see the world for less with its great value deals on a global network of over 4.5M hotels and holiday properties worldwide, plus flights, activities, and more. They’re now testing Imagen and Veo on Vertex AI to create visuals, allowing Agoda teams to generate unique images of travel destinations which would then be used to generate videos.

- \* **Kraft Heinz** is using Google’s media generation models, Imagen and Veo, on Vertex AI, speeding up campaign creations from eight weeks to eight hours.

- \* **Quom**, a financial inclusion specialist in Mexico, has developed AI-powered conversational agents that optimize and personalize user and customer support.

- \* **Salesrun**, the world’s first dedicated sales activity suite, sees Google Cloud gen AI as an alternative for analyzing information related to purchasing habits, enabling the optimization of cash flow and boosting sales for its retail customers.

- \* **Thoughtworks** is a global technology consultancy that helps businesses use technology to solve problems and innovate. They use Google Workspace with Gemini to improve internal and external communication across their company, including in non-native languages — from emails to documents and blogs.

- \* **Yazi** turns to Google Workspace with Gemini to accelerate marketing efforts so they can launch products faster; their dev teams also use it to write and deploy more code.


### **Code Agents**

- **Capgemini** has been using Code Assist to improve software engineering productivity, quality, security, and developer experience, with early results showing workload gains for coding and more stable code quality.

- \* **Tata Consultancy Services** ( **TCS**) helps build persona-based AI agents on Google Cloud, contextualized with enterprise knowledge to accelerate software development.


### **Data Agents**

- \* **The Colombian Security Council** developed a generative AI-based chatbot to improve data analysis and its chemical emergency management processes, allowing for quick responses to urgent situations.

- \* **Contraktor** developed a project to analyze contracts with AI. As a result, the company achieved a reduction of up to 75% in the time taken to analyze and review a contract, with the possibility of both reading and extracting relevant data from the documents.

- **Gamuda Berhad**, a Malaysian infrastructure and property management company, has developed Bot Unify, a platform that democratizes generative AI to allow users access to Gemini models and RAG frameworks to provide faster information and insights during construction projects.

- \* **Habi**, a Colombian real estate company, has implemented AI solutions to streamline and automate the management and verification of physical and digital documents. This improved validation operations and increased the efficiency and adaptability of employees.

- \* **HCLTech**, an industry-leading global technology company, launched HCLTech Insight — a manufacturing quality AI agent that helps predict and eliminate different types of defects on manufacturing using Vertex AI, Google Cloud’s Cortex Framework, and the Manufacturing Data Engine platform.

- **IPRally** built a custom machine-learning platform that uses natural language processing on the text of more than 120 million global patent documents, creating an accurate, easily searchable database that adds more than 200,000 new sources a week.

- **Ipsos** built a data analysis tool for its teams of market researchers, eliminating the need for time-consuming requests to data analysts. The tool is powered by Gemini 1.5 Pro and Flash models, as well as Grounding with Google Search, to enhance real-world accuracy from contemporaneous search information.

- **Juganu**, a SaaS provider for smart cities and smart stores, is working with Google Cloud to automate and digitize the physical store. The company has begun developing digital twins that give retailers virtual eyes in the store to help automate routine tasks, improve efficiency, and deliver better customer experiences.

- \* **Nowports** is harnessing the power of AI to revolutionize logistics and stand out from the competition. By analyzing key operational information, they aim to accurately predict market behavior, optimizing their entire supply chain.

- \* **Servicios** **Orienta**, a Mexican personal wellness and organizational efficiency company, has adopted AI-based solutions to analyze large volumes of data, interpret results, and provide recommendations that enhance the customer experience.

- **Workday** is using natural language processing in Vertex AI Search and Conversation to make data insights more accessible for technical and non-technical users alike.

- \* **Zenpli**, a digital identity partner for other businesses, leverages the multimodal capabilities of the models available in Vertex AI to provide its clients with a radically enhanced experience: a 90% faster onboarding process with contracts, a 50% reduction in costs thanks to AI-powered automation, and superior data quality that ensures regulatory compliance.

[Content continues with similar sections for each industry and agent type]

</details>

<details>
<summary>stop-building-ai-agents-use-smarter-llm-workflows</summary>

**Hugo:** I've taught and advised dozens of teams building LLM-powered systems. There's a common pattern I keep seeing, and honestly, it's frustrating.

Everyone reaches for agents first. They set up memory systems. They add routing logic. They create tool definitions and character backstories. It feels powerful and it feels like progress.

Until everything breaks. And when things go wrong (which they always do), nobody can figure out why.

**Was it the agent forgetting its task? Is the wrong tool getting selected? Too many moving parts to debug? Is the whole system fundamentally brittle?**

I learned this the hard way. Six months ago, I built a "research crew" with CrewAI: three agents, five tools, perfect coordination on paper. But in practice? The researcher ignored the web scraper, the summarizer forgot to use the citation tool And the coordinator gave up entirely when processing longer documents. It was a beautiful plan falling apart in spectacular ways.

This flowchart came from one of my lessons after debugging countless broken agent systems. Notice that tiny box at the end? That's how rarely you actually need agents. Yet everyone starts there.

[https://substackcdn.com/image/fetch/$s_!ooRJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd63636a1-51a8-41cb-886c-63047728b055_1600x785.png](https://substackcdn.com/image/fetch/$s_!ooRJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd63636a1-51a8-41cb-886c-63047728b055_1600x785.png)

This post is about what I learned from those failures, including how to avoid them entirely.

The patterns I'll walk through are inspired by [Anthropic's Building Effective Agents post](https://www.anthropic.com/engineering/building-effective-agents). But these aren't theory. This is real code, real failures, and real decisions I've made while teaching these systems. Every example here comes from actual projects I've built or debugged.

You'll discover why agents aren't the answer (most of the time). And more importantly, you'll learn what to build instead.

**What You'll Learn:**

- Why agents are usually not the right first step

- Five LLM workflow patterns that solve most problems

- When agents are the right tool and how to build them safely


> 🔗 All examples come from [this GitHub notebook](https://github.com/hugobowne/building-with-ai/blob/main/notebooks/01-agentic-continuum.ipynb)

## Don't Start with Agents

Everyone thinks agents are where you start. It's not their fault: frameworks make it seem easy, demo videos are exciting, and tech Twitter loves the hype.

But here's what I learned after building that CrewAI research crew: **most agent systems break down from too much complexity, not too little.**

In my demo, I had three agents working together:

- A researcher agent that could browse web pages

- A summarizer agent with access to citation tools

- A coordinator agent that managed task delegation


Pretty standard stuff, right? Except in practice:

- The researcher ignored the web scraper 70% of the time

- The summarizer completely forgot to use citations when processing long documents

- The coordinator threw up its hands when tasks weren't clearly defined


So wait: _“What exactly is an agent?”_ To answer that, we need to look at 4 characteristics of LLM systems.

1. **Memory:** Let the LLM remember past interactions

2. **Information Retrieval:** Add RAG for context

3. **Tool Usage:** Give the LLM access to functions and APIs

4. **Workflow Control:** The LLM output controls which tools are used and when

^ This makes an **agent**


[https://substackcdn.com/image/fetch/$s_!hKEL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43169d77-56ed-4b9d-8a58-891a5a1039f8_847x480.png](https://substackcdn.com/image/fetch/$s_!hKEL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43169d77-56ed-4b9d-8a58-891a5a1039f8_847x480.png) The augmented LLM - Image from **[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)** by Anthropic

When people say "agent," they mean that last step: the LLM output controls the workflow. Most people skip straight to letting the LLM control the workflow without realizing that **simpler patterns often work better**. Using an agent means handing control to the LLM. But unless your task is so dynamic that its flow can’t be defined upfront, that kind of freedom usually hurts more than it helps. Most of the time, simpler workflows with humans in charge still outperform full-blown agents.

I've debugged this exact pattern with dozens of teams:

1. We have multiple tasks that need automation

2. Agents seem like the obvious solution

3. We build complex systems with roles and memory

4. Everything breaks because coordination is harder than we thought

5. We realize simpler patterns would have worked better


> **🔎 Takeaway:** Start with simpler workflows like chaining or routing unless you know you need memory, delegation, and planning.

## Workflow patterns you should use

These five patterns come from [Anthropic's taxonomy](https://www.anthropic.com/engineering/building-effective-agents) – [implemented, tested, and demoed in my notebook](https://github.com/hugobowne/building-with-ai/blob/main/notebooks/01-agentic-continuum.ipynb):

### (1) Prompt Chaining

_Use case: “Writing personalized outreach emails based on LinkedIn profiles.”_

[https://substackcdn.com/image/fetch/$s_!f_-G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8710a8d3-bcbd-4175-9a3a-f09bba75635d_2242x507.webp](https://substackcdn.com/image/fetch/$s_!f_-G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8710a8d3-bcbd-4175-9a3a-f09bba75635d_2242x507.webp) The prompt chaining workflow - Image from **[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)** by Anthropic

You want to reach out to people at companies you’re interested in. Start by extracting structured data from a LinkedIn profile (name, role, company), then generate a tailored outreach email to start a conversation.

**Here are 3 simple steps:**

1. Turn raw LinkedIn profile text into structured data (e.g., name, title, company):


```
linkedin_data = extract_structured_data(raw_profile)
```

2. Add relevant company context for personalization (e.g., mission, open roles):


```
company_context = enrich_with_context(linkedin_data)
```

3. Generate a personalized outreach email using the structured profile + company context:


```
email = generate_outreach_email(linkedin_data, company_context)
```

#### Guidelines:

✅ Use when: Tasks flow sequentially

⚠️ Failure mode: Chain breaks if one step fails

💡 Simple to debug, predictable flow

### (2) Parallelization

_Use case: Extracting structured data from profiles_

Now that chaining works, you want to process many profiles at once and speed up the processing. Split each profile into parts — like education, work history, and skills, then run extract\_structured\_data() in parallel.

**Here are 2 simple steps:**

1. Define tasks to extract key profile fields in parallel:


```
tasks = [\
    extract_work_history(profile),   # Pull out work experience details\
    extract_skills(profile),         # Identify listed skills\
    extract_education(profile)       # Parse education background\
]
```

2. Run all tasks concurrently and gather results:


```
results = await asyncio.gather(*tasks)
```

#### Guidelines:

✅ Use when: Independent tasks run faster concurrently

⚠️ Failure mode: Race conditions, timeout issues

💡 Great for data extraction across multiple sources

### (3) Routing

_Use case: LLM classifies the input and sends it to a specialized workflow_

Say you’re building a support tool that handles product questions, billing issues, and refund requests. Routing logic classifies each message and sends it to the right workflow. If it’s unclear, fall back to a generic handler.

**Here are 2 simple steps:**

1. Choose a handler based on profile type:


```
if profile_type == "executive":
    handler = executive_handler()    # Use specialized logic for executives
elif profile_type == "recruiter":
    handler = recruiter_handler()    # Use recruiter-specific processing
else:
    handler = default_handler()      # Fallback for unknown or generic profiles
```

2. Process the profile with the selected handler:


```
result = handler.process(profile)
```

#### Guidelines:

✅ Use when: Different inputs need different handling

⚠️ Failure mode: Edge cases fall through routes

💡 Add catch-all routes for unknowns

### (4) Orchestrator-Worker

_Use case: LLM breaks down the task into 1 or more dynamic steps_

You’re generating outbound emails. The orchestrator classifies the target company as tech or non-tech, then delegates to a specialized worker that crafts the message for that context.

**Here are 2 simple steps:**

1. Use LLM to classify the profile as tech or non-tech:


```
industry = llm_classify(profile_text)
```

2. Route to the appropriate worker based on classification:


```
if industry == "tech":
    email = tech_worker(profile_text, email_routes)
else:
    email = non_tech_worker(profile_text, email_routes)
```

The orchestrator-worker pattern separates decision-making from execution:

- The orchestrator controls the flow: its output controls what needs to happen and in what order

- The workers carry out those steps: they handle specific tasks delegated to them


At first glance, this might resemble routing: a classifier picks a path, then a handler runs. But in routing, control is handed off entirely. In this example, the orchestrator retains control: it initiates the classification, selects the worker, and manages the flow from start to finish.

This is a minimal version of the orchestrator-worker pattern:

- The orchestrator controls the flow, making decisions and coordinating subtasks

- The workers carry out the specialized steps based on those decisions


You can scale this up with multiple workers, sequential steps, or aggregation logic (and I encourage you to! If you do so, [make a PR to the repository](https://github.com/hugobowne/building-with-ai/blob/main/notebooks/01-agentic-continuum.ipynb)), but the core structure stays the same.

#### Guidelines:

✅ Use when: Tasks need specialized handling

⚠️ Failure mode: Orchestrator delegates subtasks poorly or breaks down the task incorrectly

💡 Keep orchestrator logic simple and explicit

### (5) Evaluator-Optimizer

_Use case: Refining outreach emails to better match your criteria_

[https://substackcdn.com/image/fetch/$s_!lzd4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48d8175e-a3ab-47b1-8a55-4f409ba8aee2_1825x613.png](https://substackcdn.com/image/fetch/$s_!lzd4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48d8175e-a3ab-47b1-8a55-4f409ba8aee2_1825x613.png) The evaluator-optimizer workflow - Image from **[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)** byAnthropic

You’ve got an email generator running, but want to improve tone, structure, or alignment. Add an evaluator that scores each message and, If it doesn’t pass, send it back to the generator with feedback and loop until it meets your bar.

**Here are 2 simple steps:**

1. Generate an initial email from the profile:


```
content = generate_email(profile)
```

2. Loop until the email passes the evaluator or hits a retry limit:


```
while True:
    score = evaluate_email(content)
    if score.overall > 0.8 or score.iterations > 3:
        break
    content = optimize_email(content, score.feedback)
```

#### Guidelines:

✅ Use when: Output quality matters more than speed

⚠️ Failure mode: Infinite optimization loops

💡 Set clear stop conditions

> **🔎 Takeaway:** Most use cases don't need agents. They need better workflow structure.

## When to Use Agents (If You Really Have To)

Agents shine when you have a sharp human in the loop. Here's my hot take: agents excel at unstable workflows where human oversight can catch and correct mistakes.

_When agents actually work well:_

#### Example 1: Data Science Assistant

An agent that writes SQL queries, generates visualizations, and suggests analyses. You're there to evaluate results and fix logical errors. The agent's creativity in exploring data beats rigid workflows.

To build something like this, you’d give the LLM access to tools like run\_sql\_query(), plot\_data(), and summarize\_insights(). The agent routes between them based on the user’s request — for example, writing a query, running it, visualizing the result, and generating a narrative summary. Then, it feeds the result of each tool call back into another LLM request with its memory context. We walk through a live example of this pattern in our [Building with LLMs course](https://maven.com/hugo-stefan/building-llm-apps-ds-and-swe-from-first-principles?utm_campaign=paul-iusztin&utm_medium=affiliate&utm_source=maven&promoCode=PAUL).

[https://substackcdn.com/image/fetch/$s_!Aago!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf8727e9-f0c0-4420-8ce5-78d846fc15e5_1600x818.png](https://substackcdn.com/image/fetch/$s_!Aago!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf8727e9-f0c0-4420-8ce5-78d846fc15e5_1600x818.png)

#### Example 2: Creative Writing Partner

An agent brainstorming headlines, editing copy, and suggesting structures. The human judges quality and redirects when needed. Agents excel at ideation with human judgment.

#### Example 3: Code Refactoring Assistant

Proposing design patterns, catching edge cases, and suggesting optimizations. The developer reviews and approves changes. Agents spot patterns humans miss.

## When NOT to use agents

**Enterprise Automation**

Building stable, reliable software? Don't use agents. You can't have an LLM deciding critical workflows in production. Use orchestrator patterns instead.

- **High-Stakes Decisions**

Financial transactions, medical diagnoses, and legal compliance – these need deterministic logic, not LLM guesswork.


Back to my CrewAI research crew: the agents kept forgetting goals and skipping tools. Here's what I learned:

**Failure Point #1:** Agents assumed they had context that they didn’t

**Problem:** Long documents caused the summarizer to forget citations entirely

**What I'd do now:** Use explicit memory systems, not just role prompts

**Failure Point #2:** Agents failed to select the right tools

**Problem:** The researcher ignored the web scraper in favor of a general search

**What I'd do now:** Constrain choices with explicit tool menus

**Failure Point #3:** Agents did not handle coordination well

**Problem:** The coordinator gave up when tasks weren't clearly scoped

**What I'd do now:** Build explicit handoff protocols, not free-form delegation

> **🔎 Takeaway:** If you're building agents, treat them like full software systems. Don't skip observability.

[https://substackcdn.com/image/fetch/$s_!cv1W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bf927de-ab95-449f-b936-7ccb3ab5f448_1587x526.png](https://substackcdn.com/image/fetch/$s_!cv1W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bf927de-ab95-449f-b936-7ccb3ab5f448_1587x526.png) **Table: When to use an LLM, augmented LLM, or Agent (caption)**

* * *

## TL;DR

- ❌ Agents are overhyped and overused

- 🔁 Most cases need simple patterns, not agents

- 🤝 Agents excel in human-in-the-loop scenarios

- ⚠️ Don't use agents for stable enterprise systems

- 🧪 Build with observability and explicit control


Agents are overhyped and often overused. In most real-world applications, simple patterns and direct API calls work better than complex agent frameworks. Agents do have a role—in particular, they shine in human-in-the-loop scenarios where oversight and flexibility are needed. But for stable enterprise systems, they introduce unnecessary complexity and risk. Instead, aim to build with strong observability, clear evaluation loops, and explicit control.

</details>

<details>
<summary>what-are-ai-agents-definition-examples-and-types-google-clou</summary>

# What is an AI agent?

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt.

Their capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows.

## Key features of an AI agent

As explained above, while the key features of an AI agent are reasoning and acting (as described in [ReAct Framework](https://arxiv.org/pdf/2210.03629)) more features have evolved over time.

- **Reasoning:** This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context.
- **Acting**: The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes.
- **Observing**: Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions. This can involve various forms of perception, such as computer vision, natural language processing, or sensor data analysis.
- **Planning**: Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes. This often involves anticipating future states and considering potential obstacles.
- **Collaborating**: Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments. Collaboration requires communication, coordination, and the ability to understand and respect the perspectives of others.
- **Self-refining**: The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time. This can involve machine learning techniques, optimization algorithms, or other forms of self-modification.

## What is the difference between AI agents, AI assistants, and bots?

**AI assistants** are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision.

AI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.

|  | **AI agent** | **AI assistant** | **Bot** ﻿ |
| --- | --- | --- | --- |
| **Purpose** | Autonomously and proactively perform tasks | Assisting users with tasks | Automating simple tasks or conversations |
| **Capabilities** | Can perform complex, multi-step actions; learns and adapts; can make decisions independently | Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions | Follows pre-defined rules; limited learning; basic interactions |
| **Interaction** | Proactive; goal-oriented | Reactive; responds to user requests | Reactive; responds to triggers or commands |

### Key differences

- **Autonomy**: AI agents have the highest degree of autonomy, able to operate and make decisions independently to achieve a goal. AI assistants are less autonomous, requiring user input and direction. Bots are the least autonomous, typically following pre-programmed rules.
- **Complexity**: AI agents are designed to handle complex tasks and workflows, while AI assistants and bots are better suited for simpler tasks and interactions.
- **Learning**: AI agents often employ machine learning to adapt and improve their performance over time. AI assistants may have some learning capabilities, while bots typically have limited or no learning.

## How do AI agents work?

Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.

- **Persona**: A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role, evolving as the agent gains experience and interacts with its environment.
- **Memory**: The agent is equipped in general with short term, long term, consensus, and episodic memory. Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents. The agent can maintain context, learn from experiences, and improve performance by recalling past interactions and adapting to new situations.
- **Tools**: Tools are functions or external resources that an agent can utilize to interact with its environment and enhance its capabilities. They allow agents to perform complex tasks by accessing information, manipulating data, or controlling external systems, and can be categorized based on their user interface, including physical, graphical, and program-based interfaces. Tool learning involves teaching agents how to effectively use these tools by understanding their functionalities and the context in which they should be applied.
- **Model**: Large language models (LLMs) serve as the foundation for building AI agents, providing them with the ability to understand, reason, and act. LLMs act as the "brain" of an agent, enabling them to process and generate language, while other components facilitate reason and action.

## What are the types of agents in AI?

AI agents can be categorized in various ways based on their capabilities, roles, and environments. Here are some key categories of agents:

There are different definitions of agent types and agent categories.

### Based on interaction

One way to categorize agents is by how they interact with users. Some agents engage in direct conversation, while others operate in the background, performing tasks without direct user input:

- **Interactive partners** (also known as, surface agents) – Assisting us with tasks like customer service, healthcare, education, and scientific discovery, providing personalized and intelligent support. Conversational agents include Q&A, chit chat, and world knowledge interactions with humans. They are generally user query triggered and fulfill user queries or transactions.
- **Autonomous background processes** (also known as, background agents) – Working behind the scenes to automate routine tasks, analyze data for insights, optimize processes for efficiency, and proactively identify and address potential issues. They include workflow agents. They have limited or no human interaction and are generally driven by events and fulfill queued tasks or chains of tasks.

### Based on number of agents

- **Single agent**: Operate independently to achieve a specific goal. They utilize external tools and resources to accomplish tasks, enhancing their functional capabilities in diverse environments. They are best suited for well defined tasks that do not require collaboration with other AI agents. Can only handle one foundation model for its processing.
- **Multi-agent**: Multiple AI agents that collaborate or compete to achieve a common objective or individual goals. These systems leverage the diverse capabilities and roles of individual agents to tackle complex tasks. Multi-agent systems can simulate human behaviors, such as interpersonal communication, in interactive scenarios. Each agent can have different foundation models that best fit their needs.

### Benefits of using AI agents

AI agents can enhance the capabilities of language models by providing autonomy, task automation, and the ability to interact with the real world through tools and embodiment.

#### Efficiency and productivity

**Increased output**: Agents divide tasks like specialized workers, getting more done overall.

**Simultaneous execution**: Agents can work on different things at the same time without getting in each other's way.

**Automation**: Agents take care of repetitive tasks, freeing up humans for more creative work.

#### Improved decision-making

**Collaboration**: Agents work together, debate ideas, and learn from each other, leading to better decisions.

**Adaptability**: Agents can adjust their plans and strategies as situations change.

**Robust reasoning**: Through discussion and feedback, agents can refine their reasoning and avoid errors.

#### Enhanced capabilities

**Complex problem-solving**: Agents can tackle challenging real-world problems by combining their strengths.

**Natural language communication**: Agents can understand and use human language to interact with people and each other.

**Tool use**: Agents can interact with the external world by using tools and accessing information.

**Learning and self-improvement**: Agents learn from their experiences and get better over time.

#### Social interaction and simulation

**Realistic simulations**: Agents can model human-like social behaviors, such as forming relationships and sharing information.

**Emergent behavior**: Complex social interactions can arise organically from the interactions of individual agents.

## Challenges with using AI agents

While AI agents offer many benefits, there are also some challenges associated with their use:

**Tasks requiring deep empathy / emotional intelligence or requiring complex human interaction and social dynamics**– AI agents can struggle with nuanced human emotions. Tasks like therapy, social work, or conflict resolution require a level of emotional understanding and empathy that AI currently lacks. They may falter in complex social situations that require understanding unspoken cues.

**Situations with high ethical stakes** – AI agents can make decisions based on data, but they lack the moral compass and judgment needed for ethically complex situations. This includes areas like law enforcement, healthcare (diagnosis and treatment), and judicial decision-making.

**Domains with unpredictable physical environments** – AI agents can struggle in highly dynamic and unpredictable physical environments where real-time adaptation and complex motor skills are essential. This includes tasks like surgery, certain types of construction work, and disaster response.

**Resource-intensive applications** – Developing and deploying sophisticated AI agents can be computationally expensive and require significant resources, potentially making them unsuitable for smaller projects or organizations with limited budgets.

### Use cases for AI agents

Organizations have been deploying agents to address a variety [use cases](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders), which we group into six key broader categories:

### Customer agents

Customer agents deliver personalized customer experiences by understanding customer needs, answering questions, resolving customer issues, or recommending the right products and services. They work seamlessly across multiple channels including the web, mobile, or point of sale, and can be integrated into product experiences with voice or video.

### Employee agents

Employee agents boost productivity by streamlining processes, managing repetitive tasks, answering employee questions, as well as editing and translating critical content and communications.

### Creative agents

Creative agents supercharge the design and creative process by generating content, images, and ideas, assisting with design, writing, personalization, and campaigns.

### Data agents

Data agents are built for complex data analysis. They have the potential to find and act on meaningful insights from data, all while ensuring the factual integrity of their results.

### Code agents

Code agents accelerate software development with AI-enabled code generation and coding assistance, and to ramp up on new languages and code bases. Many organizations are seeing significant gains in productivity, leading to faster deployment and cleaner, clearer code.

### Security agents

Security agents strengthen security posture by mitigating attacks or increasing the speed of investigations. They can oversee security across various surfaces and stages of the security life cycle: prevention, detection, and response.

</details>
