## Global Context of the Lesson

- **What I'm planning to share:** This article introduces two of the foundational ingredients of agentic behavior: planning and reasoning. We'll discuss why LLMs inherently lack default planning capabilities, necessitating an "orchestrating agent" structure. We'll explore historical yet conceptually vital planning/reasoning strategies like ReAct and Plan-and-Execute, explaining their value in structuring agent thought processes, even as modern models (like o3/o4-mini) internalize some of these abilities. The article will cover how agents decompose goals and can self-correct.
- **Why I think it's valuable:** Understanding how to imbue LLMs with planning and reasoning capabilities is crucial for AI Engineers aiming to build autonomous agents that can tackle complex, multi-step tasks. While advanced models are increasingly capable, grasping these fundamental patterns provides a deeper insight into agent design, debugging, and the evolution of AI, allowing engineers to build more robust and intelligent systems.
- **Who the intended audience is:** AI Engineers and developers working on autonomous agent systems who need to understand the fundamental patterns of agent planning and reasoning.
- **Theory / Practice ratio:** 100% theory
- **Expected length of the article in words** (where 200-250 words ~= 1 minute of reading time): 1800-2000 words

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we solving? Why is it essential to solve it?
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger picture and next steps.

## Lesson Outline 

1. The Agent's Dilemma: Why LLMs Struggle with Complex Planning Tasks
2. Blueprints for Thinking: Foundational Planning & Reasoning Strategies
3. Advanced Agent Capabilities: Self-Correction and Real-World Applications

## Recurring Example

**Scenario: "Technical Research Assistant Agent"** - An agent tasked with researching and creating a comprehensive technical report on "Latest developments in edge AI deployment" including:
- Finding recent papers and articles
- Summarizing key findings
- Identifying trends and gaps
- Creating a structured report with conclusions

This example will be used throughout all sections to demonstrate:
- How the problem manifests without proper planning (Section 1)
- How ReAct would approach it step-by-step (Section 2)
- How Plan-and-Execute would approach it differently (Section 2)
- How advanced capabilities like self-correction apply (Section 3)

## Section 1: The Agent's Dilemma: Why LLMs Struggle with Complex Planning Tasks

**Following narrative flow: Problem identification + Why other solutions don't work**

- **The Problem:** Start with the recurring example - show how a naive LLM approach to the technical research task would fail:
    - LLM might hallucinate sources
    - No systematic way to verify information
    - Cannot iteratively refine based on findings
    - No memory of what was already researched
    
- **Recap:** What defines an agent (building on previous lessons – dynamic, goal-oriented).

- **Core Limitations of Standalone LLMs** for complex tasks:
    - **Statelessness:** Primarily next-token predictors with context window limitations; no built-in persistent memory or state tracking across multiple interactions/turns without external management.
    - **Lack of Default Planning:** Do not spontaneously create and follow multi-step plans to achieve a distant goal without specific prompting strategies or an external control loop.
    - **Implicit Reasoning:** While capable of impressive reasoning when prompted, making this reasoning actionable for multi-step complex tasks requires structure. AI Engineers provide this structure, how the LLM should reason to achieve the goal.
    - **No Innate World Interaction:** Cannot take actions (use tools, access external data) without an external system.

- **Why Traditional Solutions Fall Short:**
    - Simple prompting: Cannot handle multi-step dependencies
    - Chain-of-Thought alone: Not grounded in external world
    - Action-only approaches: Lack abstract reasoning about goals

- **The Need for Orchestration:** Introduce the "Orchestrating Agent System" or "Agent Core": The software component/loop that:
    - Manages the overall goal.
    - Maintains state/memory (e.g., scratchpad, conversation history).
    - Interacts with the LLM (the brain) for reasoning, planning, and action decisions.
    - Interfaces with tools or the external environment.
    - Facilitates the execution of tasks.

- **Section length:** 500-600 words

## Section 2: Blueprints for Thinking: Foundational Planning & Reasoning Strategies

**Following narrative flow: Theoretical solutions + Simple examples**

- **Historical Context: The Birth of ReAct:**
    - Explain how ReAct emerged from addressing the limitations of existing approaches. Prior to ReAct, language models were limited by two main paradigms: Chain-of-Thought (CoT) prompting, which enabled reasoning but wasn't grounded in the external world and relied solely on internal representations, and action-only approaches that could interact with environments but lacked abstract reasoning about high-level goals or working memory for long-horizon tasks.
    - Describe how researchers at Google Research identified this gap and proposed ReAct as a solution that synergizes reasoning and acting by allowing language models to generate both verbal reasoning traces and text actions in an interleaved manner.
    - Reference the key insight: actions affect the external environment and provide observation feedback, while reasoning traces affect the internal state of the model by updating context with useful information to support future reasoning and acting.

- **Solution 1: ReAct (Reason + Act):**
    - **Core Concept:** LLM iteratively generates a Thought (reasoning about the current state and next step) followed by an Action (what to do, e.g., use a tool or provide a final answer). After the action is executed, an Observation (result of the action) is fed back to the LLM to inform the next Thought-Action pair.
    - **Simple Example with Recurring Scenario:** Show how ReAct would handle the technical research task:
        - Thought: "I need to find recent papers on edge AI deployment"
        - Action: Search for "edge AI deployment 2024 papers"
        - Observation: [search results with 5 relevant papers]
        - Thought: "I found some good papers, let me examine the most recent one first"
        - Action: Read paper title and abstract from first result
        - Observation: [paper content]
        - Thought: "This paper mentions quantization techniques, I should search for more on this specific aspect"
        - Action: Search for "edge AI quantization techniques 2024"
        - And so on...
    - **Why it's Better:** Makes the agent's "internal monologue" explicit, aids interpretability, helps the LLM stay on track for complex tasks, provides natural way to integrate tool use.
    - **Mermaid Diagram:** ReAct loop showing cyclical flow.

- **Solution 2: Plan-and-Execute:**
    - **Core Concept:**
        1. **Planning Phase:** The LLM first generates a complete, step-by-step plan to achieve the given goal.
        2. **Execution Phase:** The agent executes each step of the plan, in parallel or sequentially, depending on the task.
    - **Simple Example with Recurring Scenario:** Show how Plan-and-Execute would handle the same task:
        - **Planning Phase:** 
            1. Search for recent academic papers on edge AI deployment
            2. Search for industry reports and blog posts
            3. Identify key trends and technologies mentioned
            4. Summarize findings from each source
            5. Analyze gaps and future directions
            6. Structure final report with introduction, findings, trends, conclusions
        - **Execution Phase:** Execute each step sequentially, potentially refining the plan as new information is discovered.
    - **Why it's Better:** Useful for tasks where high-level strategy can be determined upfront. Provides structured approach. Plan can be refined during execution.
    - **Mermaid Diagram:** Plan-and-Execute workflow showing two distinct phases.

- **Comparison of Approaches:** Using the recurring example, highlight when to use each:
    - ReAct: Better for exploratory tasks where the path isn't clear upfront
    - Plan-and-Execute: Better for well-defined tasks where the overall strategy is known

- **Section length:** 800-900 words

## Section 3: Advanced Agent Capabilities: Self-Correction and Real-World Applications

**Following narrative flow: Advanced theory + Complex examples + Connection to bigger picture**

- **Advanced Capability 1: Goal Decomposition:**
    - **Theoretical Foundation:** Explain that both ReAct and Plan-and-Execute rely on breaking down high-level, complex goals into smaller, manageable sub-goals.
    - **Complex Example:** Extend the recurring example to show hierarchical decomposition:
        - Main goal: Create technical report
        - Sub-goals: Research, Analysis, Writing
        - Sub-sub-goals: For Research: Find papers, Find industry sources, Find expert opinions
    - **LLM Prompting Techniques:** How to prompt LLMs for effective decomposition

- **Advanced Capability 2: Self-Correction:**
    - **Theoretical Foundation:** Explain the importance of detecting failures, deviations, or contradictory information
    - **Complex Example:** Show how self-correction would work in the research scenario:
        - Agent finds conflicting information between sources
        - Recognizes the conflict through reasoning
        - Decides to search for more recent or authoritative sources
        - Updates its understanding and adjusts the plan
    - **Mechanisms for Self-Correction:**
        - Re-prompting/re-trying with error information
        - Trying different tools or approaches
        - Re-evaluating the plan
        - Asking for clarification (if interactive)
    - **Connection to ReAct:** How the "Observation" step provides feedback for correction

- **Why These Patterns Remain Valuable:**
    - Even if modern reasoning models (o3/o4-mini) "internalize" similar processes through extensive post-training:
        - Designing effective prompts for complex reasoning tasks (reference to context engineering lesson)
        - Structuring the agent's control loop
        - Debugging agent behavior by surfacing implicit reasoning steps
        - Providing mental models for how agents "think"

- **Connection to Bigger Picture:**
    - How these foundational patterns evolve into more sophisticated agent architectures
    - Preview of next lessons: memory systems, tool use, multi-agent coordination
    - The role of reasoning models in the future of agent development

- **Section length:** 500-600 words

## Golden Sources

- [Agentic Reasoning - IBM](https://www.ibm.com/think/topics/agentic-reasoning)
- [AI Agent Orchestration - IBM](https://www.ibm.com/think/topics/ai-agent-orchestration)
- [ReAct Agent - IBM](https://www.ibm.com/think/topics/react-agent)
- [Building effective agents - Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629)

## Other Sources

- [AI Agents in 2025: Expectations vs Reality - IBM](https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality)
- [Reasoning AI Agents Transform Decision Making - NVIDIA](https://blogs.nvidia.com/blog/reasoning-ai-agents-decision-making/)
- [From LLM Reasoning to Autonomous AI Agents - arXiv](https://arxiv.org/pdf/2504.19678)
- [A practical guide to building agents - OpenAI](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [AI Agent Planning - IBM](https://www.ibm.com/think/topics/ai-agent-planning)
- [ReAct - Google](https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models)