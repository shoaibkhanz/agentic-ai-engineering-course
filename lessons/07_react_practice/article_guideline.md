## Global Context

- **What I'm planning to share:** This lesson transitions from theory to practice. We will build a simple ReAct agent from the ground up using Python and a standard LLM API. The focus will be on the practical implementation of the `Thought -> Action -> Observation` loop. We will write the code for the main agentic control loop, define and use simple (or mocked) tools, parse the LLM's output to determine the next step, and manage the agent's state (its "scratchpad") across turns.
- **Why I think it's valuable:** Building an agent, even a very simple one, solidifies the conceptual understanding gained in the previous lesson. This hands-on experience is crucial for AI Engineers to grasp the core mechanics of agentic systems. It demystifies the process and provides a foundational codebase and mental model that can be extended to build more sophisticated and robust agents, making it easier to debug and customize them later.
- **Who the intended audience is:** People learning for the first time how reasoning and planning can be implemented with LLMs.
- **Expected length of the article in words** (where 200-250 words ~= 1 minute of reading time): 3000 words (15 minutes of reading time).

## Outline 

1. Building a Simple ReAct Agent from Scratch (Practical Notebook)

## Section 1: Building a Simple ReAct Agent from Scratch (Practical Notebook)

-   **Objective:** Guide the student through the implementation of a basic ReAct agent using Python and an LLM API Google AI. The agent's task will be simple, designed to require a tool lookup, such as answering a question using a mocked search tool.
-   Use code from the provided notebook below. Provide one code cell at a time (don't split it) and explain it. Also explain the code outputs if provided.
-   **Focus Areas for Learning:**
    -   **Prompt Engineering for ReAct:** Demonstrate how to meticulously craft the system prompt and iterative prompts to constrain the LLM's output to the desired `Thought/Action` format.
    -   **Parsing LLM Output:** Cover simple but effective string parsing techniques to extract the action and its arguments from the model's free-form text response.
    -   **State Management:** Explicitly show how to manage the agent's state by accumulating the `Thought-Action-Observation` trail in a "scratchpad" or history list, which is then fed back into the prompt for the next turn to provide context.
-   Provide clear, commented Python code snippets for each component to ensure the focus remains on the ReAct mechanics rather than on complex tool integrations or advanced error handling.
-   This section contains the whole code of the lesson. It should be comprehensive and detailed.

## Article code

Links to code that will be used to support the article. Always prioritize this code over every other piece of code found in the sources: 

- [Notebook code for the lesson](notebook.ipynb)

## Golden Sources

- [AI Agent Orchestration - IBM](https://www.ibm.com/think/topics/ai-agent-orchestration)
- [From LLM Reasoning to Autonomous AI Agents - ArXiv](https://arxiv.org/abs/2504.19678)
- [ReAct Agent - IBM](https://www.ibm.com/think/topics/react-agent)
- [AI Agent Planning - IBM](https://www.ibm.com/think/topics/ai-agent-planning)
- [Building ReAct Agents from Scratch using Gemini - Medium](https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae)

## Other Sources

None.

