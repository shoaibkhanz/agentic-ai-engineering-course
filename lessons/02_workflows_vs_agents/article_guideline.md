## Global Context

- **What I'm planning to share:** I want to talk about the two core methodologies of building AI applications, which are LLM Workflows (predefined, orchestrated steps) and Agentic Systems (dynamic, LLM-directed processes). We'll explain each method individually and then compare them by highlighting the pros and cons of each pattern. We'll explore use cases where each approach is most effective, emphasizing the core difference: developer-defined logic versus LLM-driven autonomy. We will conclude that most AI applications are a hybrid, a gradient, of both methods. Ultimately, we'll analyze the design and capabilities of prominent, state-of-the-art agent examples (as of 2025, such as deep research agents, coding agents, and task automation agents), deconstructing their operational mechanisms (e.g., planning, tool use, memory, multi-agent architecture) and highlighting common patterns and challenges.
- **Why I think it's valuable:** As an AI Engineer, when building AI applications, you will always have to make decisions between LLM Workflows and AI Agents. Choosing the right architecture is a critical early decision that impacts complexity, flexibility, and suitability for the AI project or product. Understanding where each method shines and how to integrate them effectively is one of the fundamental skills of a successful AI Engineer.
- **Who is the intended audience:** Aspiring AI Engineers learning for the first time about the specifics of LLM workflows, AI agents and how they are different.
- **Article length:** 2300 words (equal to a 9 - 11.5 minute read)


## Outline

1. Understanding the Spectrum: From Workflows to Agents
2. Choosing your path: PROs and CONs
3. Looking at State-of-the-Art (SOTA) examples (2025)
4. Zooming in on our favorite examples
5. Designing agents: Common patterns and challenges

## Section 1: Understanding the Spectrum: From Workflows to Agents

- In this section we want to take a brief look at what LLM Workflows and Agentic Systems are. At this point we don't care about the technical specifics of each, but more about their properties and how they are used.
- On **LLM Workflows** we care about:
	- Definition: Systems where a sequence of tasks, potentially involving LLM calls, is largely predefined and orchestrated by developer-written code.
	- Characteristics: The steps are defined in advance, translating to deterministic or rule-based paths with predictable execution and explicit control flow. 
	- Analogy: A well-defined assembly line.
	- Reference: Briefly mention Anthropic's distinctions if they provide a clear framework.
	- Attach an image from the research with a simple LLM Workflow.
- On **Agentic Systems** we care about:
	- Definition: Systems where an LLM (or multiple LLMs) plays a central role in dynamically deciding the sequence of steps, reasoning, and actions to achieve a goal. The steps are not defined in advance, but dynamically chosen based on the task and current state of the environment.
	- Characteristics: Adaptive, capable of handling novelty, LLM-driven autonomy in decision-making and execution path.
	- Analogy: A skilled human expert tackling an unfamiliar problem.
	- Attach an image from the research of how a simple Agentic System looks.
- **The Role of Orchestration:** Explain that both workflows and agents require an orchestration layer, but their nature differs. In workflows, it executes a defined plan; in agents, it facilitates the LLM's dynamic planning and execution.
- **Section length:** 400 words


## Section 2: Choosing your path: PROs and CONs

- In the previous section we defined each method independently, now we want to explore **their core differences**: Developer-defined logic (workflows) versus LLM-driven autonomy in reasoning and action selection (agents).
- **When to Use LLM Workflows:**
	- Examples: Structured data extraction and transformation, automated report generation from templates, content summarization followed by translation, form processing and content generation, such as articles or blogs (where the structure is well-defined and requires minimal human feedback).
	- Strengths: Predictability, reliability for well-defined tasks, easier debugging of fixed paths, potentially lower operational cost if simpler models can be used for sub-tasks.
	- Usually preferred in enterprises.
- **When to Use Agentic Systems:**
	- Examples: Open-ended research and synthesis, dynamic problem-solving (e.g., debugging code, complex customer support), interactive task completion in unfamiliar environments, and creative content generation requiring iterative refinement (where the structure isn't well defined and needs more human feedback).
	- Strengths: Adaptability to new situations, flexibility to handle ambiguity and complexity as the steps are dynamically decided and potential for emergent solutions.
- **Hybrid Approaches:** Most real-world systems blend elements of both. Thus, in reality, we have a spectrum, a gradient between LLM Workflows and Agentic Systems, where a system adopts what's best from both worlds depending on its use cases.
- Highlight that when building an application you usually have an "autonomy slider" where you decide how much control to give to the user. As you go more manual you usually use an LLM workflow together with a human that verifies intermediate steps. As you go more automatic you give more control to the agent with fewer human-in-the-loop steps. Use the Cursor (CMD+K, CMD+L, CMD+I) and Perplexity (search, research, deep research) examples from the Andrej Karpathy "Software Is Changing (Again)" resource.
- The ultimate goal is to speed up the AI generation <-> Human verification loop, which is often achieved through good workflows/agentic architecture and well-designed UI/UX platforms (e.g., Cursor for coding).
- Attach an image from the research showing the gradient between LLM workflows and Agentic systems.
- **Section length:** 400 words


## Section 3: Looking at State-of-the-Art (SOTA) examples (2025)

- Introduce concrete LLM workflow examples, such as document summarization and analysis by Gemini in Google Workspace, which streamlines the summarization of emails, meetings, and documents, enhancing communication efficiency. Another significant application is in data-driven insights and decision-making, where companies like Geotab and Kinaxis utilize LLMs to analyze vast datasets, enabling real-time insights for supply chain optimization and fleet management. Additionally, content creation is transforming creative processes, with firms like Adobe and Procter & Gamble leveraging LLMs to generate localized marketing content and photo-realistic images, significantly reducing production time and costs. Lastly, legal and compliance automation is gaining traction, as seen with organizations like Fluna and FreshFields, which employ LLMs to automate legal document analysis and contract drafting, improving accuracy and reducing manual effort. 
- Introduce a selection of prominent, SOTA agent examples, such as deep research agents (from OpenAI or Perplexity), coding assistants (Codex, Claude code, Gemini's CLI, Cursor, or Windsurf), task automation and computer use agents (OpenAI's Operator, Claude computer use) or other relevant 2025 examples.
- For each example:
	- Briefly describe the problem it solves and its functionality. 
	- Highlight what makes it an agent or workflow based on the definitions in Sections 1 and 2.
	- Discuss its potential impact or novelty.
-  **Section length:** 300 words (keep the section short as we will dig into more details in the next section)

## Section 4: Zooming in on our favorite examples

- In Section 3 we briefly described some common examples of agents and workflows. Now, we want to dig deeper into some examples and quickly explain what they do, how they work, and how they combine both agents and workflows into cohesive products. 
- **Document summarization and analysis workflow by Gemini in Google Workspace**:
	- Explain how such a workflow would look. Explain that this is a pure workflow.
	- Create a suggestive mermaid diagram highlighting that this is a workflow.
- **Gemini CLI coding assistant:** 
	- Explain its likely operational loop:
		1. **Goal Understanding & Planning:** Decomposing the high-level coding task.
		2. **Environment Interaction:** Reading files, understanding project structure.
		3. **Code Generation/Modification:** Writing or editing code.
		4. **Execution & Testing:** Running the code, using a linter, running tests.
		5. **Debugging & Iteration:** Analyzing errors, modifying the plan, and trying again.
	- Tools used: File system access, code interpreter, web search (for documentation/solutions), version control.
	- Clarify how much it operates as an agent and as a workflow. 
	- Create a mermaid diagram showing how the operational loop works.
- **Perplexity deep research (e.g., for scientific discovery or market research):**
	- Explain the iterative multi-step process:
		1. **Query Formulation & Planning:** Defining research questions, planning search strategy.
		2. **Iterative Search:** Using search engine tools, accessing databases.
		3. **Information Extraction & Filtering:** Identifying relevant information from sources.
		4. **Synthesis & Analysis:** Combining information, identifying patterns, drawing conclusions.
		5. **Citation & Reporting:** Generating a structured output with proper sourcing.
	- Clarify how much it operates as an agent and as a workflow. 
	- Create a mermaid diagram showing how the iterative multi-step process works.
- **OpenAI's Operator:**
	- Explain the concept: Agents designed to operate computer applications or websites via GUIs or OS-level commands.
	- Key mechanisms: Vision capabilities (to understand screens), action mapping (mouse clicks, keyboard inputs), planning to achieve user goals within applications.
	- Challenges: Robustness to UI changes, interpreting visual information accurately.
-  **Section length:** 500 words (without counting the mermaid diagram code)

## Section 5: Designing agents: Common patterns and challenges

- As our course will be mostly on agents, in this last section we will start digging more deeply into agentic systems by presenting a brief summary of a common architecture of an AI agent, including its core components:
	- Planning (e.g., task decomposition, goal setting).
	- Tool Use (as a fundamental way to interact and act with the environment).
	- Memory (short-term for context, long-term for factual data).
	- Iterative Refinement / Self-Correction loops.
- The goal of this section is not for people to fully understand what an AI agent is, but just to build an intuition about what it takes to create one. In future articles, we will dig into all the necessary details. 
- Draw a mermaid diagram illustrating how the architectural patterns from above work together to form an agent.
- Conclude the section with some sentences about common issues encountered while building AI agents that require careful design choices, such as:
	- Reliability and consistency of LLM reasoning are compromised, as errors from each decision compound. 
	- Handling long-context and maintaining coherence over many steps.
	- Handling multi-modal data from multiple data sources, such as Slack, web, Zoom, SQL databases, data lakehouses, etc.
	- Scalability and cost of complex agent operations.
    - Security implications of autonomous agents with powerful writing tools. For example, write tools from sending emails to writing code or adding records to a database can be extremely dangerous if the agent doesn't work properly.
- **Section length:** 500 words

## Golden Sources

[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
[What is an AI agent?](https://cloud.google.com/discover/what-are-ai-agents)
[Real Agents vs. Workflows: The Truth Behind AI 'Agents'](https://www.youtube.com/watch?v=kQxr-uOxw2o&t=1s)
[Exploring the difference between agents and workflows](https://decodingml.substack.com/p/llmops-for-production-agentic-rag)
[A Developer’s Guide to Building Scalable AI: Workflows vs Agents](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/)


## Other Sources

[601 real-world gen AI use cases from the world's leading organizations](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
[Stop Building AI Agents: Here’s what you should build instead](https://decodingml.substack.com/p/stop-building-ai-agents)
[Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ)
[Building Production-Ready RAG Applications: Jerry Liu](https://www.youtube.com/watch?v=TRjq7t2Ms5I)
[Claude Code](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
[Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
[Introducing Operator](https://openai.com/index/introducing-operator/)
