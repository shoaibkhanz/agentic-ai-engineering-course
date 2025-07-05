# AI Agents: Hands-On with Tools
### Unlock LLM power with tools

## Why Your AI Agent is Useless Without Tools

Everyone is talking about AI agents, but let's be real: most of them are useless. A Large Language Model (LLM) by itself is just a text generator. It’s a powerful brain, but a brain in a jar—it can't see, hear, or interact with the world. It can't check today's stock prices, book a meeting in your calendar, or even perform a simple, reliable calculation. Without the ability to act, an LLM is not an agent; it's just a very articulate parrot.

So, how do we give this brain hands and senses? The answer is **Tools**. Tools are the fundamental components that transform a passive LLM into an active agent capable of interacting with external systems. They are the bridge between the model's reasoning capabilities and the real world.

In this article, we'll cut through the hype and get straight to the engineering. We'll break down how tool calling works from the ground up, starting with a from-scratch Python implementation to understand the core mechanics. We'll then build a mini-framework, move to a production-grade API like Gemini, and explore advanced patterns. For any AI Engineer, understanding how to build and use tools isn't just a nice-to-have—it's a foundational skill for shipping AI applications that actually do something useful.

## Understanding Why Agents Need Tools

To build effective agents, we first need to accept the inherent limitations of Large Language Models. At their core, LLMs are sophisticated pattern matchers trained on static datasets of text and code. They generate responses by predicting the next most likely token based on the input they receive. This architecture makes them brilliant at language tasks but fundamentally incapable of interacting with anything outside their training data [1](https://www.mobihealthnews.com/news/apple-study-highlights-limitations-llms), [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11303832/).

An LLM cannot access real-time information because it has no knowledge of events after its training data was collected. It doesn't know today's weather, the latest news, or the current price of a stock. Similarly, it cannot interact with external systems like databases, third-party APIs, or local files. While an LLM can write code, it cannot run it, which means it struggles with precise mathematical calculations or any task requiring a computational environment [3](https://promptdrive.ai/llm-limitations/), [4](https://arxiv.org/html/2401.08664v3/). Furthermore, an LLM's memory limits it to the context window of a single conversation, preventing it from reliably remembering past interactions or user preferences over long periods [3](https://promptdrive.ai/llm-limitations/).

These limitations mean an LLM alone is a closed system. This is where tools come in. Tools are simply functions an agent can call to interact with the outside world. Think of the LLM as the central brain that reasons and makes decisions. The tools are its "hands and senses," allowing it to perceive and act on the environment beyond its text-based interface.
![Figure 1: A diagram showing the core components of an LLM agent: a central agent that interacts with planning, memory, and tools. The user request feeds into the agent.](https://cdn.prod.website-files.com/614c82ed388d53640613982e/66aa02651c656df9e8e5b5b3_664c8772c80586fb49458bb3_llm-agent-structure.webp)


An agent combines the core LLM (the brain), a planning module to break down tasks, memory to store information, and a set of tools to interact with the world. By calling a tool, the agent can retrieve current information, query a database, or execute an action. This interaction transforms the LLM from a passive text generator into a dynamic problem-solver [5](https://www.superannotate.com/blog/llm-agents).

## Building a Tool-Calling Agent From Scratch

To truly understand how agents work, we need to build one from the ground up. Forget the fancy frameworks for a moment. We will implement the entire tool-calling flow from scratch to see what happens under the hood. The process is a simple loop: the LLM decides which tool to use, you execute it, and you feed the result back to the LLM.
![Figure 2: A sequence diagram illustrating the tool-calling flow between the user, LLM, and an external tool.](```mermaid
sequenceDiagram
    participant You
    participant LLM
    participant External Tool

    You->>LLM: Prompt + Tool Definitions
    LLM->>You: Function Call Request (name, args)

    You->>External Tool: Execute Function(args)
    External Tool-->>You: Function Output
    You->>LLM: Function Output
    LLM->>You: Final Response
```
)

Let's break this down with code.

### Defining Tools and Their Schemas
First, you define Python functions that will act as your tools. These are simple, mocked functions to search a drive, send a message, and summarize text. The function signature and docstrings are critical because the LLM uses this information to understand what each tool does and when to use it [6](https://platform.openai.com/docs/guides/function-calling).

Here is the `search_google_drive` function:
```python
import json
from lessons.utils import DOCUMENT # A sample financial document

def search_google_drive(query: str) -> dict:
    """
    Searches for a file on Google Drive and returns its content or a summary.

    Args:
        query (str): The search query to find the file, e.g., 'Q3 earnings report'.

    Returns:
        dict: A dictionary representing the search results, including file names and summaries.
    """
    return {
        "files": [
            {
                "name": "Q3_Earnings_Report_2024.pdf",
                "id": "file12345",
                "content": DOCUMENT,
            }
        ]
    }
```
Next, you define the `send_discord_message` function:
```python
def send_discord_message(channel_id: str, message: str) -> dict:
    """
    Sends a message to a specific Discord channel.

    Args:
        channel_id (str): The ID of the channel to send the message to, e.g., '#finance'.
        message (str): The content of the message to send.

    Returns:
        dict: A dictionary confirming the action, e.g., {"status": "success"}.
    """
    return {
        "status": "success",
        "status_code": 200,
        "channel": channel_id,
        "message_preview": f"{message[:50]}...",
    }
```
Finally, you define the `summarize_financial_report` function:
```python
def summarize_financial_report(text: str) -> str:
    """
    Summarizes a financial report.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The summary of the text.
    """
    return "The Q3 2023 earnings report shows strong performance across all metrics with 20% revenue growth, 15% user engagement increase, 25% digital services growth, and improved retention rates of 92%."
```
Next, you must create a schema for each tool. This schema, typically in JSON format, describes the tool's name, purpose, and parameters. This is the information you will pass to the LLM so it knows what tools are available and how to call them. You are essentially creating a formal contract that the LLM can read and understand [7](https://docs.bentoml.com/en/latest/examples/function-calling.html).

Here is an example of the schema for `search_google_drive`:
```python
search_google_drive_schema = {
    "name": "search_google_drive",
    "description": "Searches for a file on Google Drive and returns its content or a summary.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query to find the file, e.g., 'Q3 earnings report'.",
            }
        },
        "required": ["query"],
    },
}
```
You then collect all these schemas and their corresponding Python functions into a dictionary for easy access and a list to pass to the LLM:
```python
TOOLS = {
    "search_google_drive": {
        "handler": search_google_drive,
        "declaration": search_google_drive_schema,
    },
    # ... other tools
}
TOOLS_BY_NAME = {tool_name: tool["handler"] for tool_name, tool in TOOLS.items()}
TOOLS_SCHEMA = [tool["declaration"] for tool in TOOLS.values()]
```

### Using the LLM to Call a Tool
Now, you create a system prompt that instructs the LLM on how to behave as a tool-calling agent. This prompt includes guidelines for when and how to use tools and, most importantly, the schemas of the available tools. This is how the LLM "discovers" the tools. LLMs are often fine-tuned to interpret these tool schema inputs and output tool calls [6](https://platform.openai.com/docs/guides/function-calling), [8](https://mirascope.com/blog/openai-function-calling).
```python
TOOL_CALLING_SYSTEM_PROMPT = """
You are a helpful AI assistant with access to tools.

<tool_definitions>
{tools}
</tool_definitions>

Use the tools to answer the user's request. If you need to call a tool, respond with a JSON object in the format:
```tool_call
{"name": "tool_name", "args": {"arg1": "value1", "arg2": "value2"}}```
If you have a final answer, respond with plain text.
"""

USER_PROMPT = "Please find the Q3 earnings report on Google Drive and send a summary of it to the #finance channel on Discord."

# We'll use the Gemini client for this example
import google.generativeai as genai
client = genai.Client()
MODEL_ID = "gemini-2.5-flash"

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]

response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
)
```
The LLM, which has been fine-tuned to recognize these schemas, responds not with text, but with a structured request to call a function. Its output is:
```
```tool_call
{"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}```
```

### Executing the Tool
Your application code then parses this structured output, identifies the function name (`search_google_drive`) and its arguments (`{"query": "Q3 earnings report"}`), and executes the corresponding Python function. The structured output is crucial here, as it allows your application to interpret the LLM's request properly.

First, you extract the tool call string and then define a function to call the tool:
```python
def extract_tool_call(response_text: str) -> str:
    return response_text.split("```tool_call")[1].split("```")[0].strip()

def call_tool(response_text: str, tools_by_name: dict):
    tool_call_str = extract_tool_call(response_text)
    tool_call = json.loads(tool_call_str)
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    tool = tools_by_name[tool_name]
    return tool(**tool_args)
```
Now, you execute the tool:
```python
tool_result = call_tool(response.text, tools_by_name=TOOLS_BY_NAME)
```
The `tool_result` from calling `search_google_drive` is:
```python
{'files': [{'name': 'Q3_Earnings_Report_2024.pdf', 'id': 'file12345', 'content': '...'}]}
```

### Interpreting the Tool Results with an LLM
The result of `search_google_drive` is then sent back to the LLM. Now, the model has the content of the report and can proceed with the next step of the user's request, which is to summarize it and send it to Discord. This simple, transparent flow is the foundation of all tool-based agents [9](https://friendli.ai/blog/ai-agents-function-calling), [10](https://nanonets.com/blog/langchain/).
```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=f"Interpret the tool result: {json.dumps(tool_result, indent=2)}",
)
```
The LLM's final response, interpreting the tool result, is:
```
The tool result provides the content of a financial document.

Here's an interpretation:

*   **File Name & ID:** The document is named "Q3_Earnings_Report_2024.pdf" with the ID "file12345".
*   **Document Title & Period:** The report is specifically titled "Q3 2023 Financial Performance Analysis." (Note: While the filename indicates "2024," the content clearly states "Q3 2023" as the period being analyzed.)
*   **Overall Performance:** The company had a strong Q3 2023, beating market expectations.
*   **Key Financial Highlights:**
    *   **Revenue:** Increased by 20%.
    *   **User Engagement:** Grew by 15%.
*   **Business Segment Performance:**
    *   **Digital Services:** Led growth with a 25% year-over-year increase.
    *   **New Market Expansion:** Contributed significantly, accounting for 30% of the total revenue increase.
*   **Efficiency & Customer Metrics:**
    *   **Customer Acquisition Costs:** Decreased by 10%.
    *   **Retention Rates:** Improved to 92%, marking the best performance to date.
*   **Financial Health:** The company maintains a healthy cash flow position.
*   **Outlook:** The results provide a strong foundation for continued growth into Q4 and beyond.

In summary, the Q3 2023 earnings report indicates excellent performance driven by revenue growth, increased user engagement, successful market expansion, and improved operational efficiency, positioning the company well for future growth.
```

## Automating Tool Schema Generation with Decorators

Manually writing JSON schemas for every function is repetitive and error-prone. This approach violates the Don't Repeat Yourself (DRY) software engineering principle, which advocates for reducing repetition of software patterns. In any real-world application, you want to automate this process to ensure consistency and efficiency. Production frameworks leverage decorators to handle this schema generation automatically, and we can build a simplified version ourselves to understand the underlying mechanics [11](https://langchain-opentutorial.gitbook.io/langchain-opentutorial/15-agent/01-tools), [12](https://leanpub.com/ollama/read).

To achieve this, we will create a `@tool` decorator. This Python decorator inspects a function's signature and docstring to automatically generate the JSON schema that we previously wrote by hand. This automation makes our code cleaner, more maintainable, and less prone to bugs, as the function's documentation and its schema remain synchronized. This is a crucial step towards building robust and scalable AI agent systems [12](https://leanpub.com/ollama/read).

The implementation involves using Python's built-in `inspect` module. This module allows us to examine live objects, including functions, to extract their name, parameters, and docstrings. We then format this extracted information into the required JSON schema structure.

Let's break down the code for our `@tool` decorator. First, the `ToolFunction` class acts as a wrapper for our original Python function, storing both the function and its auto-generated schema.
```python
from inspect import Parameter, signature
from typing import Any, Callable, Dict, Optional

class ToolFunction:
    def __init__(self, func: Callable, schema: Dict[str, Any]) -> None:
        self.func = func
        self.schema = schema
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.func(*args, **kwargs)
```
Second, the `tool` decorator contains the core logic. It uses `inspect.signature(func)` to get details about the function's parameters, iterating through them to build the `properties` and `required` fields of our JSON schema.
```python
def tool(description: Optional[str] = None) -> Callable[[Callable], ToolFunction]:
    """A decorator that creates a tool schema from a function."""
    def decorator(func: Callable) -> ToolFunction:
        sig = signature(func)
        properties = {}
        required = []

        for param_name, param in sig.parameters.items():
            if param_name == "self":
                continue
            param_schema = {
                "type": "string",
                "description": f"The {param_name} parameter",
            }
            if param.default == Parameter.empty:
                required.append(param_name)
            properties[param_name] = param_schema

        schema = {
            "name": func.__name__,
            "description": description or func.__doc__ or f"Executes the {func.__name__} function.",
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required,
            },
        }
        return ToolFunction(func, schema)
    return decorator
```
Now, we can define our tools much more elegantly by simply applying our new `@tool` decorator. This eliminates the need for separate, manually written JSON schema definitions.
```python
@tool()
def search_google_drive_example(query: str) -> dict:
    """Search for files in Google Drive."""
    return {"files": ["Q3 earnings report"]}

@tool()
def send_discord_message_example(channel_id: str, message: str) -> dict:
    """Send a message to a Discord channel."""
    return {"message": "Message sent successfully"}

tools = [
    search_google_drive_example,
    send_discord_message_example,
]
tools_by_name = {tool.schema["name"]: tool.func for tool in tools}
tools_schema = [tool.schema for tool in tools]
```
The decorator wraps our function in a `ToolFunction` object that holds both the callable function and its generated schema. The rest of the logic for prompting the LLM and executing the tool call remains the same, but our tool definition code is now much cleaner and more robust. Engineers design production systems using this modular approach.

## Using a Dedicated API for Tool Calling

While building from scratch is great for understanding, in production, you will use a dedicated API from a provider like Google, OpenAI, or Anthropic. Let's refactor our code to use Google's Gemini API for tool calling.

The core concepts remain identical: you define functions and provide their schemas to the model. However, the API handles the underlying prompt engineering and response parsing for you. Instead of crafting a complex system prompt and manually parsing a JSON string from the model's text output, the API returns a structured `function_call` object directly. This streamlined process is a standard across major LLM providers, with only minor interface differences [13](https://ai.google.dev/gemini-api/docs/function-calling).
![Figure 3: The function calling flow with the Gemini API.](https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png)


Here's how we adapt our previous code. We define our tool schemas and then package them into a `Tool` object for the Gemini client.
```python
from google.genai import types

# Schemas are the same as before
# search_google_drive_schema, send_discord_message_schema

tools_for_gemini = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(**search_google_drive_schema),
            types.FunctionDeclaration(**send_discord_message_schema),
        ]
    )
]
config = types.GenerateContentConfig(
    tools=tools_for_gemini,
    tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
)
```
Now, when we call the Gemini API with our user prompt and this configuration, the response is much cleaner.
```python
USER_PROMPT = "Please find the Q3 earnings report on Google Drive and send a summary of it to the #finance channel on Discord."

response = client.models.generate_content(
    model=MODEL_ID,
    contents=USER_PROMPT,
    config=config,
)

function_call = response.candidates[0].content.parts[0].function_call
```
The `function_call` object contains the name and arguments, ready for execution.
```python
# The function_call object looks like this:
# FunctionCall(name='search_google_drive', args={'query': 'Q3 earnings report'})

tool_handler = TOOLS_BY_NAME[function_call.name]
tool_result = tool_handler(**function_call.args)
```
Its output is:
```python
{'files': [{'name': 'Q3_Earnings_Report_2024.pdf', 'id': 'file12345', 'content': '...'}]}
```
As you can see, the API abstracts away the messy parts of prompting and parsing, but the fundamental flow of defining tools, letting the model choose one, executing it, and returning the result is unchanged. This is why understanding the from-scratch implementation is so valuable—it demystifies what these powerful APIs are doing behind the scenes.

## Structured Data Extraction with Pydantic Models

While dedicated APIs simplify the process of calling tools, their real power emerges when you control the structure of their output. One of the most practical applications of tool calling is to generate structured data on demand. Instead of just hoping the LLM outputs clean JSON, we can define a Pydantic model and pass it to the agent as a tool. The agent can then decide to "call" this tool, with the arguments being the structured data we need.

This pattern is incredibly useful in agentic workflows. For instance, an agent might perform several intermediate steps where it reasons using unstructured text, which is easy for an LLM to process. When an agent needs to produce a final output, it can call the Pydantic tool. This ensures the data is perfectly structured for downstream applications, such as saving to a database or feeding into another system [14](https://blog.kusho.ai/from-chaos-to-order-structured-json-with-pydantic-and-instructor-in-llms/).

Let's define a Pydantic model for document metadata.
```python
from pydantic import BaseModel, Field

class DocumentMetadata(BaseModel):
    """A class to hold structured metadata for a document."""
    summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
    tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
    keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
    quarter: str = Field(description="The quarter of the financial year... (e.g., Q3 2023).")
    growth_rate: str = Field(description="The growth rate... (e.g., 10%).")
```
We then create a tool declaration from this Pydantic model's schema and provide it to the Gemini API.
```python
from google.genai import types

extraction_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="extract_metadata",
            description="Extracts structured metadata from a financial document.",
            parameters=DocumentMetadata.model_json_schema(),
        )
    ]
)
config = types.GenerateContentConfig(tools=[extraction_tool])

prompt = f"""
Please analyze the following document and extract its metadata.
Document:
--- 
{DOCUMENT}
--- 
"""

response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
function_call = response.candidates[0].content.parts[0].function_call

# The model 'calls' our Pydantic tool
document_metadata = DocumentMetadata(**function_call.args)
```
This process yields a perfectly validated Pydantic object. This technique guarantees data integrity, ensuring that LLM-generated data adheres to strict, predictable structures, which is essential for reliable communication in multi-agent systems, debugging, and monitoring [14](https://blog.kusho.ai/from-chaos-to-order-structured-json-with-pydantic-and-instructor-in-llms/), [15](https://developer-service.blog/a-practical-guide-on-structuring-llm-outputs-with-pydantic/), [16](https://python.useinstructor.com/blog/2023/09/11/generating-structured-output--json-from-llms/).

## Simple Tool Chaining

Naturally, the next step involves handling complex tasks that require multiple tools. We achieve this by running the tool-calling process in a loop. The agent calls a tool, gets a result, and then decides on the next action—which could be another tool call or a final answer. This allows the agent to chain tools together to solve multi-step problems.
![Figure 4: A flow diagram illustrating simple tool chaining, where the LLM decides an action, executes a tool, gets a result, and loops back to decide the next action until a final answer is reached.](```mermaid
graph TD
    A[User Prompt] --> B{LLM Decides Action};
    B --> C{Tool Call 1};
    C --> D[Execute Tool 1];
    D --> E[Tool 1 Result];
    E --> B;
    B --> F{Tool Call 2};
    F --> G[Execute Tool 2];
    G --> H[Tool 2 Result];
    H --> B;
    B --> I[Final Answer];
```
)


Let's see this in action. We ask the agent to find a report, summarize it, and then send the summary to Discord. This requires three sequential tool calls.
```python
# Using the Gemini client and tools defined earlier
USER_PROMPT = "Please find the Q3 earnings report on Google Drive and send a summary of it to the #finance channel on Discord."
messages = [USER_PROMPT]
max_iterations = 3

while max_iterations > 0:
    response = client.models.generate_content(model=MODEL_ID, contents=messages, config=config)
    response_message_part = response.candidates[0].content.parts[0]
    
    if not hasattr(response_message_part, "function_call"):
        break # The agent is done and has a final answer

    # Execute the tool call
    tool_result = call_tool(response_message_part.function_call)

    # Append the tool call and result to the conversation history
    messages.append(response.candidates[0].content)
    messages.append(types.Part(
        function_response=types.FunctionResponse(
            name=response_message_part.function_call.name,
            response=tool_result if isinstance(tool_result, dict) else {"result": tool_result},
        )
    ))
    max_iterations -= 1
```
This looping approach works, but it is a brute-force method with significant limitations. An agent forced to call a tool at every step can become inefficient. It lacks the opportunity to pause, reflect on the results, and reason about its next move. This often leads to issues like getting stuck in infinite loops or making redundant calls, which can escalate API usage and costs [17](https://arxiv.org/html/2503.13657v2), [18](https://arxiv.org/html/2407.20859v1). Studies show that a significant portion of multi-agent system failures stem from step repetitions and degraded reasoning when higher-level planning or reflection is absent [17](https://arxiv.org/html/2503.13657v2).

This simple looping pattern misses a crucial component: explicit reasoning. The agent acts without thinking. This is precisely why we developed more sophisticated agentic patterns like **ReAct (Reasoning and Acting)**. ReAct interleaves "thought" steps with "action" steps, enabling the agent to reason about what it has learned and plan its next move more intelligently. We will explore ReAct in a future article, but it is important to recognize that simple tool chaining, while powerful, is just the first step toward building truly intelligent agents.

## Types of Tools for AI Agents

Now that we understand the mechanics of tool calling, let's survey the types of tools most commonly used in production-grade AI agents. We can broadly categorize these tools based on their function.

### Knowledge and Memory Access
This is perhaps the most critical category, as it directly addresses the LLM's limitation of having static, outdated knowledge. One key approach is **Retrieval-Augmented Generation (RAG)**, a technique that allows an agent to query external knowledge sources, such as vector databases or document stores, to retrieve relevant context [19](https://botpress.com/blog/llm-agent-framework). This forms the foundation of "agentic RAG," where the agent actively decides when to search and how to use the retrieved information. In practical applications, RAG tools are crucial for enterprise search platforms, providing answers grounded in internal company documents [20](https://northernlight.com/the-case-for-using-retrieval-augmented-generation-in-generative-ai-applications-within-the-enterprise/), [21](https://www.pingcap.com/article/how-rag-and-fine-tuning-enhance-llm-performance-case-studies/). For data stored in traditional relational databases, agents use **text-to-SQL tools**, where the LLM generates a SQL query from a natural language question for the tool to execute [22](https://www.getdynamiq.ai/post/llm-agents-explained-complete-guide-in-2025).

### Web Search and Browsing
To access up-to-the-minute information from the internet, agents need web search and browsing tools. These can be simple **Search API tools** that interface with engines like Google or Bing, allowing the agent to formulate a query and get back a list of results [23](https://aws.amazon.com/blogs/machine-learning/integrate-dynamic-web-content-in-your-generative-ai-application-using-a-web-search-api-and-amazon-bedrock-agents/). More advanced **web browsing tools** can fetch and parse the HTML content of a webpage, enabling agents to read articles, check prices, or find specific details beyond search snippets.

### Code Execution
This is one of the most powerful—and riskiest—tool categories. A **Python interpreter tool** gives the agent the ability to write and execute Python code. It is incredibly versatile, allowing the agent to perform precise calculations, manipulate data with libraries like Pandas, or create visualizations [24](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Building-an-LLM-Powered-Data-Analyst--Vmlldzo2Nzg5NjMx), [25](https://dev.to/intelliarts/using-react-agents-llms-to-draw-insights-from-tabular-data-2j6).

⚠️ **Security is Paramount:** Giving an agent the power to execute code is dangerous. The code must *always* be run in a sandboxed environment, completely isolated from the host system. Best practices include using container-based sandboxes, restricting network access, dropping unnecessary system permissions, and setting strict resource limits to prevent runaway costs or denial-of-service attacks [26](https://huggingface.co/docs/smolagents/en/tutorials/secure_code_execution), [27](https://unit42.paloaltonetworks.com/agentic-ai-threats/).

## Tools: The Foundation of Modern AI Agents

We've journeyed from the fundamental limitations of LLMs to the practical engineering of tool-based agents. It should now be clear that tools are not just an add-on; they are the essential bridge that connects an LLM's reasoning to the real world, transforming it from a text generator into a capable agent.

We started by building a tool-calling mechanism from scratch, opening the black box to see how an LLM selects a function and generates the right arguments. You saw how we then streamlined this process with a custom decorator, mirroring the design of production frameworks, before moving to a production-grade API like Gemini, which abstracts away the complexity but not the core principles.

You saw how to chain tools in a loop to tackle multi-step problems and, more importantly, understood the limitations of this simple approach, which paves the way for more advanced patterns like ReAct. Finally, we surveyed the landscape of industry-standard tools for knowledge retrieval, web search, and code execution. Mastering the art of designing, implementing, and securely deploying these tools is a fundamental skill for any AI Engineer looking to build applications that deliver real-world value.

## References

- [1] [Apple study highlights limitations of LLMs](https://www.mobihealthnews.com/news/apple-study-highlights-limitations-llms)
- [2] [The communicative and social harms of large language models](https://pmc.ncbi.nlm.nih.gov/articles/PMC11303832/)
- [3] [What are the limitations of large language models (LLMs)?](https://promptdrive.ai/llm-limitations/)
- [4] [Large Language Models in Education: A Focus on the Limitations of ChatGPT](https://arxiv.org/html/2401.08664v3)
- [5] [LLM Agents: A Guide to the Hottest Trend in AI](https://www.superannotate.com/blog/llm-agents)
- [6] [Function calling](https://platform.openai.com/docs/guides/function-calling)
- [7] [Function Calling with Llama 3.1](https://docs.bentoml.com/en/latest/examples/function-calling.html)
- [8] [How to use OpenAI Function Calling](https://mirascope.com/blog/openai-function-calling)
- [9] [Building an AI Agent That Can Call Multiple Functions (Tools)](https://friendli.ai/blog/ai-agents-function-calling)
- [10] [LangChain: The Ultimate Guide to Building LLM-Powered Applications](https://nanonets.com/blog/langchain/)
- [11] [Tools - LangChain](https://langchain-opentutorial.gitbook.io/langchain-opentutorial/15-agent/01-tools)
- [12] [Ollama Python and JavaScript Libraries](https://leanpub.com/ollama/read)
- [13] [Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)
- [14] [From Chaos to Order: Structured JSON with Pydantic and Instructor in LLMs](https://blog.kusho.ai/from-chaos-to-order-structured-json-with-pydantic-and-instructor-in-llms/)
- [15] [A Practical Guide on Structuring LLM Outputs with Pydantic](https://developer-service.blog/a-practical-guide-on-structuring-llm-outputs-with-pydantic/)
- [16] [Generating structured output & JSON from LLMs](https://python.useinstructor.com/blog/2023/09/11/generating-structured-output--json-from-llms/)
- [17] [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/html/2503.13657v2)
- [18] [Agentic AI Systems Are Not A "Solved Problem": An Empirical Analysis of How They Malfunction](https://arxiv.org/html/2407.20859v1)
- [19] [LLM Agent Frameworks: A Deep Dive](https://botpress.com/blog/llm-agent-framework)
- [20] [The Case for Using Retrieval-Augmented Generation in Generative AI Applications within the Enterprise](https://northernlight.com/the-case-for-using-retrieval-augmented-generation-in-generative-ai-applications-within-the-enterprise/)
- [21] [How RAG and Fine-tuning Enhance LLM Performance: Case Studies](https://www.pingcap.com/article/how-rag-and-fine-tuning-enhance-llm-performance-case-studies/)
- [22] [LLM Agents Explained: Complete Guide in 2025](https://www.getdynamiq.ai/post/llm-agents-explained-complete-guide-in-2025)
- [23] [Integrate dynamic web content in your generative AI application using a web search API and Amazon Bedrock Agents](https://aws.amazon.com/blogs/machine-learning/integrate-dynamic-web-content-in-your-generative-ai-application-using-a-web-search-api-and-amazon-bedrock-agents/)
- [24] [Building an LLM-Powered Data Analyst](https://wandb.ai/mostafaibrahim17/ml-articles/reports/Building-an-LLM-Powered-Data-Analyst--Vmlldzo2Nzg5NjMx)
- [25] [Using ReAct Agents & LLMs to Draw Insights from Tabular Data](https://dev.to/intelliarts/using-react-agents-llms-to-draw-insights-from-tabular-data-2j6)
- [26] [Secure Code Execution](https://huggingface.co/docs/smolagents/en/tutorials/secure_code_execution)
- [27] [Agentic AI Systems Under Attack: An Attacker-Driven Survey](https://unit42.paloaltonetworks.com/agentic-ai-threats/)