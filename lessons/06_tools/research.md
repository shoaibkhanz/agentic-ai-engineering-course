# Research

## Research Results

<details>
<summary>What practical limitations prevent large-language models from accessing real-time data or executing code on their own, and how do external “tools” address these gaps?</summary>

### Source [1]: https://www.projectpro.io/article/llm-limitations/1045

Query: What practical limitations prevent large-language models from accessing real-time data or executing code on their own, and how do external “tools” address these gaps?

Answer: Large language models (LLMs) face several **practical limitations** that prevent them from accessing real-time data or executing code autonomously. A core constraint is **computational limits**, such as a fixed number of tokens they can process at once. Exceeding this token limit leads to errors, which is necessary to maintain performance and context during interactions. Additionally, LLMs suffer from **issues with accuracy and knowledge updating**—they are generally trained on static datasets and lack mechanisms for continuous, real-time knowledge refresh. This means they cannot natively access or incorporate up-to-date or external information beyond their last training cut-off. Furthermore, LLMs lack **long-term memory** and struggle with complex reasoning, making them ill-suited for tasks requiring persistent state or advanced logic that would be facilitated by code execution or external data retrieval. These fundamental limitations necessitate external interventions or "tools" to bridge these capability gaps.

-----

-----

-----

### Source [2]: https://www.decodable.co/blog/llms-need-real-time-data-to-deliver-contextual-results

Query: What practical limitations prevent large-language models from accessing real-time data or executing code on their own, and how do external “tools” address these gaps?

Answer: LLMs were **originally designed for language generation**—their primary function is to predict and generate human-like text based on patterns in large, static datasets. Because of this, they are often **outdated as soon as they are deployed**, lacking access to real-time information or the ability to reflect ongoing events or proprietary business data. This creates a significant limitation, especially for enterprise applications requiring up-to-date context. The lack of real-time data access means LLMs cannot provide **current, contextual, or actionable insights** on their own. To address these gaps, organizations are **grounding LLMs through external "tools"**—for example, integrating streaming data pipelines that feed real-time information into the model or using platforms that connect LLMs to proprietary databases. These tools allow LLMs to supplement their static knowledge with dynamic, real-world data, effectively extending their utility to tasks like live decision support, data extraction, or contextual knowledge delivery.

-----

-----

-----

### Source [3]: https://www.intuitivedataanalytics.com/gne-blogs/the-limitations-and-challenges-of-large-language-models-llms/

Query: What practical limitations prevent large-language models from accessing real-time data or executing code on their own, and how do external “tools” address these gaps?

Answer: Most LLMs are **trained on static data**, with their knowledge typically ending months or years before deployment. They do not have the inherent capability to access or process **live, real-time information**. This temporal limitation means that unless LLMs are explicitly updated or connected to external sources, their outputs will not reflect the latest developments. This is a particularly acute problem when up-to-date information is critical, such as in news, finance, or customer service scenarios. LLMs also face **context and subtext limitations**—they can struggle to interpret nuance, sarcasm, or ambiguity in language, which sometimes requires deeper reasoning or access to external data or logic (i.e., through code execution). These deficits highlight the necessity of external tools that can fetch real-time data or run code to augment the model's capabilities and deliver more accurate, current, and contextually appropriate responses.

-----

-----

-----

### Source [4]: https://arxiv.org/html/2412.04503v1

Query: What practical limitations prevent large-language models from accessing real-time data or executing code on their own, and how do external “tools” address these gaps?

Answer: This academic primer outlines several **technical and architectural limitations** that restrict LLMs from accessing real-time data or executing code autonomously. Fine-tuning methods such as freezing layers, sparse tuning, or prefix tuning are often used to adapt models to new tasks without changing the core architecture, primarily due to **limited computational resources** and the need to prevent overfitting. However, these adaptation techniques do not enable the model to **directly access external data sources or perform code execution**. The very architecture of LLMs is optimized for processing and generating text within a closed, pre-trained system, rather than for interacting with external environments or APIs. As a result, to compensate for these architectural limitations, **external "tools" must be developed**—such as plugins, retrieval-augmented generation (RAG) systems, or code execution environments—that can interface with the LLM, fetch real-time data, or perform computations on the model’s behalf. These integrations extend the practical utility of LLMs far beyond their initial design.

-----

</details>

<details>
<summary>How can Pydantic be combined with OpenAI or Gemini function-calling to generate, validate, and consume structured outputs from LLMs?</summary>

### Source [5]: https://ai.pydantic.dev/api/models/gemini/

Query: How can Pydantic be combined with OpenAI or Gemini function-calling to generate, validate, and consume structured outputs from LLMs?

Answer: PydanticAI provides a custom implementation to interact with **Gemini** models through the `pydantic_ai.models.gemini.GeminiModel` class. This model is initialized by specifying the Gemini model name and an API provider, which can be 'google-gla' (using Google's Generative Language API) or 'google-vertex'. The `GeminiModel` class is designed to be used as part of broader agent workflows within PydanticAI, and it abstracts authentication and provider details, supporting both synchronous and asynchronous clients.

By leveraging Pydantic models, you can define structured schemas for inputs and outputs, ensuring that the data generated by Gemini (or any LLM) is validated according to your specifications. This integration facilitates **structured output generation and validation**—for example, you can prompt the LLM to produce data matching a Pydantic schema, then consume the returned data as a fully validated Python object. This workflow is critical for function-calling scenarios, where LLMs are expected to call external functions or APIs with structured arguments.

The model and provider abstraction ensures that you can switch between different Gemini endpoints or authentication methods without changing your core validation and agent logic.

-----

-----

-----

### Source [6]: https://ai.pydantic.dev/models/gemini/

Query: How can Pydantic be combined with OpenAI or Gemini function-calling to generate, validate, and consume structured outputs from LLMs?

Answer: To use Gemini models with Pydantic for structured output, you first set up authentication via an environment variable (`GEMINI_API_KEY`). You then instantiate a Gemini model directly or via the generic `Agent` class from `pydantic_ai`, specifying the model name and provider. 

For structured output, you typically define a Pydantic schema that describes the expected format of the LLM’s response. When interacting with the agent, you can pass this schema, and PydanticAI will handle sending the structured prompt, receiving the LLM’s output, and validating it against the schema. This ensures that outputs—even those generated via function-calling APIs—are **consumed as Pydantic models**, providing a high-assurance interface for downstream processing.

Customization is supported at various levels: you can provide a custom provider for authentication, or configure the HTTP client for advanced use cases (e.g., custom timeouts). This flexibility makes it straightforward to combine Gemini with Pydantic’s validation logic for robust structured output workflows.

-----

-----

-----

### Source [7]: https://ai.pydantic.dev/models/

Query: How can Pydantic be combined with OpenAI or Gemini function-calling to generate, validate, and consume structured outputs from LLMs?

Answer: PydanticAI is designed to be **model-agnostic**, supporting multiple LLM providers—including OpenAI, Anthropic, and Gemini—through a unified interface. This is accomplished by abstracting the model, provider, and profile concepts:

- **Model:** Represents the specific LLM (e.g., Gemini, OpenAI GPT).
- **Provider:** Handles authentication and API endpoint details.
- **Profile:** Encapsulates request/response formatting rules for each model family, ensuring that Pydantic-based schema validation and transformation work consistently across different LLMs and providers.

When you instantiate an Agent using a string like `google-gla:gemini-2.0-flash`, PydanticAI automatically selects the correct model and provider, simplifying integration. You can also directly instantiate models and specify providers and profiles for fine-grained control.

This architecture allows you to use the same Pydantic schema and validation logic for both OpenAI and Gemini’s function-calling or structured output APIs, making it easy to **generate, validate, and consume structured outputs** from multiple LLMs with minimal changes to your application code.

-----

-----

-----

### Source [8]: https://ai.google.dev/gemini-api/docs/openai

Query: How can Pydantic be combined with OpenAI or Gemini function-calling to generate, validate, and consume structured outputs from LLMs?

Answer: Google’s Gemini API provides **OpenAI API compatibility**, allowing you to use the same code patterns (including structured outputs and function-calling features) by simply changing the API key and endpoint (`base_url`). For Python, you use the OpenAI client library, set the base URL to Gemini’s OpenAI-compatible endpoint, and interact with Gemini models as you would with OpenAI models.

This compatibility means that **existing Pydantic-based OpenAI function-calling workflows can be reused with Gemini** with only minor changes. For example, you can prompt Gemini models to produce structured outputs that are then parsed and validated against Pydantic schemas, just as you would with OpenAI’s models. This makes migration and multi-provider support straightforward in projects that rely on structured LLM outputs validated by Pydantic.

-----

</details>

<details>
<summary>What issues arise when an LLM is allowed to call tools in a simple sequential loop, and how does the ReAct (Reasoning + Acting) pattern overcome these shortcomings?</summary>

### Source [9]: https://arxiv.org/html/2409.00920v1

Query: What issues arise when an LLM is allowed to call tools in a simple sequential loop, and how does the ReAct (Reasoning + Acting) pattern overcome these shortcomings?

Answer: When an **LLM is allowed to call tools in a simple sequential loop**, it often encounters significant limitations in handling **complex, real-world tasks**. While single function calls (one API per turn) are handled reasonably well, scenarios involving **parallel calls** (multiple independent calls per turn) and **dependent calls** (sequential calls where each depends on the previous output) are generally overlooked. The main issues identified include:
- **Limited diversity and complexity**: Most tool-augmented LLMs focus on simple, single-step function calling, neglecting more intricate tasks that require branching or chaining of multiple calls.
- **Constrained API domains**: Models are often trained only on a narrow set of APIs, limiting applicability to real-world scenarios.
- **Oversimplified parameter types and uniform data formats**: This restricts the LLM's ability to handle varied or nuanced tool interactions.
- **Challenge in accurate API selection and parameter configuration**: For complex tasks, the LLM must precisely choose which tools to call and how to configure them—errors here are common and can break the task chain.
- **Data accuracy**: Ensuring the correct data is used for each tool call is challenging, especially as tasks become more complex and dependent calls accumulate potential errors.

The **ReAct (Reasoning + Acting) pattern** addresses these shortcomings by interleaving reasoning steps (where the LLM plans or reflects on its next action based on current context) with tool-calling actions. This allows the LLM to adaptively decide what tool to use and how, based on the outcomes of previous steps, enabling it to handle **dependent and complex, multi-step tool use** much more effectively than simple sequential loops[1].

-----

-----

-----

### Source [10]: https://blog.christoolivier.com/p/llms-and-functiontool-calling

Query: What issues arise when an LLM is allowed to call tools in a simple sequential loop, and how does the ReAct (Reasoning + Acting) pattern overcome these shortcomings?

Answer: Allowing **LLMs to call tools in a simple sequential loop** can result in **unreliable and non-deterministic behavior**. The article illustrates that while basic function calling (such as requesting weather data or news) may work in simple cases, this approach does not **guarantee reliability or predictability**. Key challenges include:
- **Non-deterministic outputs**: LLMs may generate inconsistent or unexpected tool calls, especially when not explicitly trained for function calling.
- **Integration challenges**: Without robust orchestration, integrating LLM-driven tool calls into application logic can lead to unpredictable results.
- **Need for defensive coding**: Developers must anticipate and handle possible errors or unexpected outcomes from LLM tool calls.

The ReAct pattern mitigates these issues by introducing **explicit reasoning steps** between actions, making the process more transparent and controllable, which in turn enhances reliability and predictability in tool selection and usage[2].

-----

-----

-----

### Source [11]: https://blog.promptlayer.com/llm-agents-vs-function-calling/

Query: What issues arise when an LLM is allowed to call tools in a simple sequential loop, and how does the ReAct (Reasoning + Acting) pattern overcome these shortcomings?

Answer: **Simple sequential tool calling** with LLMs provides benefits like **real-time data access** and **structured output**, but also introduces notable disadvantages:
- **Potential misinterpretation**: LLMs may incorrectly interpret user intent and select the wrong function to call, especially when the context is complex.
- **Error handling difficulties**: If an API call fails or returns unexpected results, handling these errors in a simple loop is challenging.
- **Limitations with complex/nested scenarios**: Sequential tool-calling struggles with tasks that require multi-step reasoning, conditional branching, or chaining several dependent calls.
- **Orchestration complexity**: Managing the transitions between reasoning, action, and response in a simple loop can become unwieldy as task complexity increases.

The **ReAct pattern** overcomes these shortcomings by:
- **Integrating reasoning and action**: Instead of blindly executing tool calls, the LLM reasons about what action to take next based on the evolving context or intermediate outcomes.
- **Supporting complex workflows**: ReAct enables handling of nested, chained, and conditional tool calls, making it suitable for real-world applications that simple loops cannot manage.
- **Reducing misinterpretation**: By explicitly reasoning before each action, the LLM reduces the risk of incorrect tool selection or parameterization, leading to more robust outcomes[3].

-----

-----

</details>

<details>
<summary>Which categories of tools—such as retrieval-augmented generation (RAG), web search/browsing, and sandboxed code execution—are most common in production LLM agents, and what are notable industry examples?</summary>

### Source [12]: https://www.superannotate.com/blog/llm-agents

Query: Which categories of tools—such as retrieval-augmented generation (RAG), web search/browsing, and sandboxed code execution—are most common in production LLM agents, and what are notable industry examples?

Answer: This source outlines a wide range of **frameworks and tool categories** commonly integrated into production LLM agents. Key tool types include:

- **Retrieval-Augmented Generation (RAG)**: Frameworks like Llama Index and Langchain provide connectors and interfaces for advanced data retrieval, making RAG a standard approach for grounding LLM outputs in external or enterprise data sources.
- **Web Search/Browsing**: MindSearch is highlighted as an AI search engine framework designed to browse hundreds of web pages, similar to Perplexity.ai Pro. SearchEngine is another example, focused on integrating web information into agent responses.
- **Sandboxed Code Execution**: Python Agent and JS Repo allow agents to execute code in a controlled environment for dynamic computation or data transformation.
- **Database and Dataframe Access**: SQL Database Agent and Pandas Dataframe Agent enable agents to query structured data, while Vectorstore Agent provides access to vector databases for semantic search.
- **OpenAPI and JSON Tools**: OpenAPI Agent and JSON Agent facilitate integration with external APIs and JSON-based workflows.
- **Enterprise and Open-Source Agent Frameworks**: Nvidia NIM agent blueprints and IBM’s Bee agent framework are notable for enterprise deployment and scalability.

These frameworks and tool categories represent the current industry standard for building robust, production-grade LLM agents.

-----

-----

-----

### Source [14]: https://www.promptingguide.ai/research/llm-agents

Query: Which categories of tools—such as retrieval-augmented generation (RAG), web search/browsing, and sandboxed code execution—are most common in production LLM agents, and what are notable industry examples?

Answer: This source provides concrete examples of **tool categories and notable agents**:

- **Math Agents** (e.g., EduChat, CodeHelp) use code execution and symbolic computation tools.
- **Software Engineering Agents** (e.g., ChatDev, ToolLLM, MetaGPT) automate coding, debugging, and testing, relying heavily on sandboxed code execution environments.
- **Database and Knowledge Base Access**: D-Bot exemplifies agents with continuous database interaction for maintenance, diagnosis, and optimization.
- **Operating System Integration**: OS-Copilot demonstrates agents interfacing with the web, code terminals, files, multimedia, and third-party applications—covering web browsing, code execution, and API tools.

These cases reinforce the centrality of **retrieval, web search/browsing, and code execution** as essential tool categories for production LLM agents, with notable industry prototypes and frameworks.

-----

-----

-----

### Source [15]: https://developer.nvidia.com/blog/introduction-to-llm-agents/

Query: Which categories of tools—such as retrieval-augmented generation (RAG), web search/browsing, and sandboxed code execution—are most common in production LLM agents, and what are notable industry examples?

Answer: NVIDIA’s blog discusses **enterprise use cases and advanced tool integration** in LLM agents:

- **Customized Authoring Agents**: These agents leverage personal data retrieval and context adaptation, indicative of RAG tool usage.
- **Multi-modal Agents**: Extend beyond text, incorporating tools to process images and audio, reflecting a trend toward richer data integration.
- **Enterprise Applications**: Emphasize the need for agents to access social graphs, data curation workflows, and specialized domain expertise—requiring tools for retrieval, structured data access, and often secure code execution.

NVIDIA’s enterprise focus highlights **retrieval-augmented generation, multi-modal input processing, and integration with proprietary data systems** as key tool categories, with agent blueprints designed for practical deployment.

-----

-----

-----

### Source [16]: https://apxml.com/courses/intro-llm-agents/chapter-4-equipping-agents-with-tools/survey-of-available-tool-categories

Query: Which categories of tools—such as retrieval-augmented generation (RAG), web search/browsing, and sandboxed code execution—are most common in production LLM agents, and what are notable industry examples?

Answer: This source provides a **survey of common tool types** used by LLM agents, with illustrative examples:

- **Web Search and Browsing**: Tools that allow agents to pull live information from the internet.
- **Retrieval Tools**: Enabling agents to query and pull data from vector databases, structured databases, or enterprise knowledge bases.
- **Code Execution**: Sandboxed code interpreters (typically Python or JavaScript) used for dynamic computation, data processing, or code analysis.
- **APIs and External Service Integration**: Tools for invoking REST APIs or automating interaction with external software systems.
- **File and Data Manipulation**: For reading, writing, and transforming files or tabular data.

The source emphasizes that **web search, retrieval, code execution, and API integration** are the most prevalent tool categories in production LLM agents, forming the backbone of modern agentic workflows in industry.

-----

-----

</details>

<details>
<summary>What open-source frameworks or protocols (e.g., LangGraph, Model Context Protocol) automate Python function-to-schema conversion and multi-tool orchestration, and how do they compare to hand-rolled decorator approaches?</summary>

### Source [17]: https://langchain-ai.github.io/langgraph/how-tos/graph-api/

Query: What open-source frameworks or protocols (e.g., LangGraph, Model Context Protocol) automate Python function-to-schema conversion and multi-tool orchestration, and how do they compare to hand-rolled decorator approaches?

Answer: LangGraph provides a high-level Graph API for constructing multi-step agent workflows with explicit **input and output schemas**. Schemas can be defined using Python’s `TypedDict`, allowing distinct input and output structures for each graph. Internally, LangGraph manages schema validation and transformation, ensuring that data passed between nodes conforms to the declared types, and filters output according to the output schema. Nodes (Python functions) are added to the graph, and edges define execution flow. When the graph is invoked, only the output schema is returned, abstracting away the function-to-schema conversion and orchestrating multi-tool workflows without manual decorator logic.

Example:
- Define input/output schemas as `TypedDict`.
- LangGraph auto-handles schema validation and data flow between nodes.
- The output of the graph invocation matches the output schema, hiding internal state details.

This framework automates much of what would require custom decorators and manual schema handling in ad hoc Python solutions.

-----

-----

-----

### Source [18]: https://langchain-ai.github.io/langgraph/concepts/low_level/

Query: What open-source frameworks or protocols (e.g., LangGraph, Model Context Protocol) automate Python function-to-schema conversion and multi-tool orchestration, and how do they compare to hand-rolled decorator approaches?

Answer: LangGraph models agent workflows as graphs, with a central concept of **State**, which captures schema and state update logic. The schema can be specified with `TypedDict`, `dataclass`, or Pydantic models, and this forms the contract for all nodes and edges. Explicit input and output schemas can be set for cases where input and output differ, allowing for advanced multi-tool orchestration with strict data validation. This eliminates the need for hand-rolled decorators around each function, as the graph framework enforces schema consistency and offers options for default values and recursive validation (with Pydantic).

-----

-----

-----

### Source [19]: https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_json_schema.html

Query: What open-source frameworks or protocols (e.g., LangGraph, Model Context Protocol) automate Python function-to-schema conversion and multi-tool orchestration, and how do they compare to hand-rolled decorator approaches?

Answer: LangChain provides a utility function, `convert_to_json_schema`, which converts a schema representation (including Python types, Pydantic models, or callable signatures) directly into a **JSON Schema**. This is key for automating function-to-schema conversion, especially when integrating with systems (like OpenAI function calling) that expect JSON schema definitions for tool arguments. This utility abstracts the conversion process, avoiding the need for custom decorators or manual schema construction.

-----

-----

-----

### Source [20]: https://pypi.org/project/langgraph/0.0.36/

Query: What open-source frameworks or protocols (e.g., LangGraph, Model Context Protocol) automate Python function-to-schema conversion and multi-tool orchestration, and how do they compare to hand-rolled decorator approaches?

Answer: LangGraph is built to automate orchestration of multiple tools/functions in a workflow graph. Tools can be integrated by converting them into a format compatible with OpenAI function calling, and then bound to the agent model. The framework handles execution flow, state management, and output aggregation, supporting features like streaming node output. LangGraph’s approach is more robust and maintainable than hand-rolled decorators, as it centralizes workflow logic, schema management, and execution control.

-----

-----

-----

### Source [21]: https://python.langchain.com/docs/concepts/tools/

Query: What open-source frameworks or protocols (e.g., LangGraph, Model Context Protocol) automate Python function-to-schema conversion and multi-tool orchestration, and how do they compare to hand-rolled decorator approaches?

Answer: LangChain’s **tool abstraction** links a Python function with a schema specifying its name, description, and argument types. Tools are typically created using the `@tool` decorator, which simplifies exposing Python functions as structured, schema-driven tools. The decorator automatically infers the function’s schema from its signature and docstring, making the process less error-prone and more maintainable than manual schema specification. This decorator-based approach is effective for single tools, but frameworks like LangGraph provide higher-level orchestration for multi-tool workflows, automating schema management and execution sequencing.

-----

-----

</details>

<details>
<summary>What best-practice guidance do the OpenAI and Gemini teams give on writing robust JSON schemas for function calling (e.g., required vs. optional fields, enums, “strict” mode, additionalProperties=false), and why are these details critical for reliable tool use?</summary>

### Source [22]: https://wandb.ai/onlineinference/genai-research/reports/Mastering-function-calling-with-OpenAI--VmlldzoxMzQ1MDk1NQ

Query: What best-practice guidance do the OpenAI and Gemini teams give on writing robust JSON schemas for function calling (e.g., required vs. optional fields, enums, “strict” mode, additionalProperties=false), and why are these details critical for reliable tool use?

Answer: **OpenAI emphasizes the importance of JSON schema precision for robust function calling.** The guidance includes:
- **Use precise schema definitions:** Clearly define each parameter's type (e.g., use enums for limited choices, numeric types for numbers).
- **Mark required fields:** Explicitly indicate which fields are required so the AI includes them in the function call.
- **Strict mode:** When enabled, schema validation enforces that outputs match the expected types. For example, if a parameter is specified as an integer, the model is compelled to provide a numeric value.
- **Handle ambiguous input:** System instructions should direct the model to ask clarifying questions rather than guessing missing parameters (e.g., prompt for a city if the user says, "Get me the weather").
- **Explicitness and precision:** The more explicit and precise the schema, the better the AI understands when and how to call functions, improving reliability.

These details are **critical for reliable tool use** because they ensure that the AI provides correct and complete arguments, reducing errors and the need for post-processing. If the model does not behave as expected, revisiting the schema, function names, and descriptions often resolves issues.

-----

-----

-----

### Source [23]: https://community.openai.com/t/strict-true-and-required-fields/1131075

Query: What best-practice guidance do the OpenAI and Gemini teams give on writing robust JSON schemas for function calling (e.g., required vs. optional fields, enums, “strict” mode, additionalProperties=false), and why are these details critical for reliable tool use?

Answer: **OpenAI's "strict" mode enforces that all fields in the function calling schema be listed as required.** This requirement ensures:
- **All objects and keys are mandatory:** The AI cannot omit any defined fields or add unexpected keys.
- **Compatibility with standard JSON schema tools:** The schema used is standard and can be translated to tools like Pydantic or Zod.
- **Schema in model context:** The given schema is directly placed in the AI's context, leveraging its understanding of JSON validation.

**Disabling strict mode** is possible if full adherence is too limiting. In such cases, optional fields can be allowed or null values can be used for fields not always required. For developers seeking structured outputs, strict mode guarantees outputs conform to the expected schema, which is crucial for downstream processing and integration.

-----

-----

-----

### Source [24]: https://community.openai.com/t/feature-request-function-calling-easily-enforcing-valid-json-schema-following/263515

Query: What best-practice guidance do the OpenAI and Gemini teams give on writing robust JSON schemas for function calling (e.g., required vs. optional fields, enums, “strict” mode, additionalProperties=false), and why are these details critical for reliable tool use?

Answer: This discussion highlights the **importance of enforcing valid JSON schema in function calling**, especially for developers seeking predictable outputs. Key points include:
- **Current limitations:** The OpenAI function calling feature does not always guarantee valid JSON, leading to challenges when integrating with downstream systems that rely on strict schema adherence.
- **Suggested improvements:** Enforcing JSON schema at the token level (e.g., using context-free grammars and token masking) could ensure the model never generates invalid outputs, improving reliability and efficiency.
- **Developer needs:** The ability to receive pure, schema-compliant JSON (without extra wrapping) would streamline application workflows and reduce post-processing overhead.

Reliable schema enforcement is considered essential for trustworthy tool use, as it prevents unexpected or malformed outputs that could disrupt application logic.

-----

-----

-----

### Source [25]: https://www.datacamp.com/tutorial/open-ai-function-calling-tutorial

Query: What best-practice guidance do the OpenAI and Gemini teams give on writing robust JSON schemas for function calling (e.g., required vs. optional fields, enums, “strict” mode, additionalProperties=false), and why are these details critical for reliable tool use?

Answer: **OpenAI function calling supports complex and nested JSON schemas.** Key guidance includes:
- **Define nested structures:** Properly specify hierarchical relationships within the schema to ensure the model generates valid nested JSON outputs.
- **Integration with external systems:** By defining function schemas that map directly to external API or database calls, developers can ensure consistent, structured, and reliable interactions.
- **Schema mismatch:** If the model's output does not match the defined function or schema, the function call is not executed, and the response defaults to a standard text output.

This approach ensures that only valid, schema-compliant function calls are processed, which is crucial for maintaining consistency and reliability in applications that depend on structured outputs.

-----

-----

</details>

<details>
<summary>How do Python decorator approaches—such as LangChain’s @tool, LangGraph’s automatic schema conversion, or the Model Context Protocol—automate turning a plain function into a valid tool definition, and how do they compare to hand-rolled JSON schemas?</summary>

### Source [26]: https://python.langchain.com/docs/concepts/tools/

Query: How do Python decorator approaches—such as LangChain’s @tool, LangGraph’s automatic schema conversion, or the Model Context Protocol—automate turning a plain function into a valid tool definition, and how do they compare to hand-rolled JSON schemas?

Answer: LangChain’s **@tool decorator** automates turning a plain function into a valid tool definition by:
- **Automatically inferring the tool’s name** from the function name.
- Using the **function’s docstring as the tool’s description**.
- **Automatically generating the tool schema** based on the function’s signature, including argument names and types.
- Allowing direct invocation of the tool using `.invoke()` and providing easy inspection of the tool’s properties, such as its name, description, and arguments.

This decorator is the recommended way to create tools in LangChain, as it simplifies tool creation and ensures the resulting object implements the required Tool Interface. The generated schema can be inspected via the tool’s `.args` property, and the tool can be directly bound to models that support tool calling. This approach removes the need for manual JSON schema definition, reducing boilerplate and potential for errors[1].

-----

-----

-----

### Source [27]: https://langchain-opentutorial.gitbook.io/langchain-opentutorial/15-agent/01-tools

Query: How do Python decorator approaches—such as LangChain’s @tool, LangGraph’s automatic schema conversion, or the Model Context Protocol—automate turning a plain function into a valid tool definition, and how do they compare to hand-rolled JSON schemas?

Answer: The **@tool decorator** in LangChain:
- Converts a regular Python function into a tool with minimal effort.
- Allows for **automatic documentation** and **flexible interface creation**.
- Supports parameters to customize tool behavior, but fundamentally, it uses the function’s metadata (name, signature, and docstring) to generate the tool interface.

Once decorated, the function can be used as a tool directly, and invoked using a dictionary of arguments. This process eliminates the need for manual JSON schema creation, as the decorator handles schema generation and tool registration automatically[2].

-----

-----

-----

### Source [28]: https://langchain-cn.readthedocs.io/en/latest/modules/agents/tools/custom_tools.html

Query: How do Python decorator approaches—such as LangChain’s @tool, LangGraph’s automatic schema conversion, or the Model Context Protocol—automate turning a plain function into a valid tool definition, and how do they compare to hand-rolled JSON schemas?

Answer: LangChain’s **@tool decorator** is designed for rapid conversion of simple Python functions into tools:
- The **function’s name** becomes the tool’s name (unless overridden).
- The **docstring** becomes the tool’s description.
- The decorator extracts the function’s signature to build the tool’s schema automatically.

This allows for tools to be defined and registered with minimal boilerplate. For advanced customization, parameters can be provided to the decorator, but the default behavior relies on introspection of the function, providing a consistent interface without manual JSON schema definitions[3].

-----

-----

-----

### Source [29]: https://python.langchain.com/docs/concepts/tool_calling/

Query: How do Python decorator approaches—such as LangChain’s @tool, LangGraph’s automatic schema conversion, or the Model Context Protocol—automate turning a plain function into a valid tool definition, and how do they compare to hand-rolled JSON schemas?

Answer: LangChain’s approach to tool creation and model interaction centers on the **@tool decorator**:
- It creates a standardized association between a function and its schema.
- Tools can be bound to models using `.bind_tools()`, enabling models to call these tools as needed.
- The function’s arguments and docstring are used to generate the necessary schema, making the process seamless for developers.

This system enables automated, schema-driven connections between tools and models, bypassing the complexity of hand-writing JSON schemas for each tool[4].

-----

-----

-----

### Source [30]: https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html

Query: How do Python decorator approaches—such as LangChain’s @tool, LangGraph’s automatic schema conversion, or the Model Context Protocol—automate turning a plain function into a valid tool definition, and how do they compare to hand-rolled JSON schemas?

Answer: The `@tool` decorator (from `langchain_core.tools.convert.tool`) offers:
- A mechanism to **make tools out of functions** with or without additional arguments.
- Options to set the name, description, argument schema, and other tool-specific behaviors.
- When `infer_schema=True` (default), it **automatically infers the tool’s argument schema** from the function’s type annotations, leveraging Pydantic for schema validation.
- This results in a Pydantic schema that describes the tool’s input, which can be serialized as JSON schema if needed.

This automation streamlines tool creation compared to hand-rolled JSON schemas, reducing manual effort and risk of schema mismatch or error[5].

-----

-----

</details>

<details>
<summary>What do recent research papers like “Toolformer,” “Gorilla,” or “Efficient Tool Use with Chain-of-Abstraction Reasoning” reveal about teaching large language models to decide which external API to call and to generate correct arguments autonomously?</summary>

### Source [31]: https://proceedings.neurips.cc/paper_files/paper/2024/file/e4c61f578ff07830f5c37378dd3ecb0d-Paper-Conference.pdf

Query: What do recent research papers like “Toolformer,” “Gorilla,” or “Efficient Tool Use with Chain-of-Abstraction Reasoning” reveal about teaching large language models to decide which external API to call and to generate correct arguments autonomously?

Answer: Gorilla introduces a system that enables **large-scale API integration with LLMs**, demonstrating high accuracy in generating API calls across thousands of functions. The paper’s key contribution is the **Retriever-Aware Training (RAT)** technique, which allows LLMs to utilize retrieved API documentation during inference. This improves both the accuracy of API calls and the model’s ability to adapt to changes in APIs. Gorilla is evaluated with APIBench, a benchmark covering about 1600 machine learning APIs, and introduces new AST-based metrics for measuring functional correctness and hallucination in API calls.

Gorilla outperforms both open- and closed-source models in generating correct API calls, both for APIs seen during training (in-domain) and new ones (out-of-domain). It can also reason about API calls under constraints, such as those involving specific requirements. The study highlights the importance of integrating retrieval mechanisms during training to enhance the model’s performance in tool usage tasks. Gorilla demonstrates that LLMs can autonomously select which API to use and generate the correct arguments, leveraging documentation retrieval to stay robust against evolving APIs.

-----

-----

-----

### Source [32]: https://arxiv.org/html/2505.23662v1

Query: What do recent research papers like “Toolformer,” “Gorilla,” or “Efficient Tool Use with Chain-of-Abstraction Reasoning” reveal about teaching large language models to decide which external API to call and to generate correct arguments autonomously?

Answer: ToolHaystack presents a benchmark designed to **stress-test tool-augmented language models (TALMs)** in long-term, realistic interaction scenarios. The research finds that **chain-of-thought (CoT) prompting** provides only marginal or scenario-specific improvements for tool use, and does not consistently enhance overall performance across all models. Robust gains are limited to certain models and specific scenarios, indicating that the effectiveness of reasoning cues such as CoT depends on both the model’s base reasoning capabilities and its contextual retrieval mechanisms.

The study concludes that while current TALMs perform well in short, clean dialogues, their performance **degrades in long-term, distraction-rich contexts**. Key challenges include **context retention, handling goal shifts, and avoiding hallucination** over time. This underscores the need for more robust evaluation frameworks and continued research into making LLMs more reliable and autonomous in real-world tool use, particularly for sustained, complex tasks.

-----

-----

-----

### Source [33]: https://aclanthology.org/2024.lrec-main.1427.pdf

Query: What do recent research papers like “Toolformer,” “Gorilla,” or “Efficient Tool Use with Chain-of-Abstraction Reasoning” reveal about teaching large language models to decide which external API to call and to generate correct arguments autonomously?

Answer: This paper surveys recent research, including Toolformer and Gorilla, on **autonomous tool utilization in LLMs**. It highlights that many existing approaches require explicit prompts to guide tool usage, meaning the model plays a passive role and depends on external instructions. The authors propose that truly autonomous tool use should involve models that can, given only a user query, **decide whether to use a tool, which tool to use, and how to use it without tool-specific prompts**.

A comparative analysis shows that Toolformer and similar methods focus on enabling LLMs to make such decisions, but often involve additional retrieval steps that can introduce cumulative errors and suffer from limited context length, restricting scalability. The work aspires towards models that internalize tool knowledge, allowing for fully autonomous and scalable tool use. This vision is for LLMs to autonomously select and apply external APIs, generating correct arguments without requiring explicit cues in the prompt.

-----

-----

-----

### Source [34]: https://arxiv.org/html/2405.16533v1

Query: What do recent research papers like “Toolformer,” “Gorilla,” or “Efficient Tool Use with Chain-of-Abstraction Reasoning” reveal about teaching large language models to decide which external API to call and to generate correct arguments autonomously?

Answer: This paper investigates **automatic multi-tool learning** for LLMs, referencing Toolformer and similar models. It describes the **tool learning task** as augmenting LLMs with external tools (such as APIs) to increase their utility. The approach involves training LLMs to understand when and how to invoke external tools, and to generate the appropriate API calls and arguments as needed.

Experimental results demonstrate that with appropriate training, LLMs can learn to discern when the use of an external tool is beneficial, which tool to choose, and how to compose correct API calls. The study confirms that such models can achieve high effectiveness in integrating external functions, moving toward **autonomous, context-driven tool use**. This research underlines the importance of aligning tool-use training objectives with real-world usage scenarios, so that LLMs can reliably select and use APIs with minimal human intervention.

-----

-----

</details>

<details>
<summary>What documented problems occur when an LLM is allowed to invoke tools in a simple sequential loop (e.g., getting stuck, mis-ordering calls, latency), and how does the ReAct reasoning-action pattern address these shortcomings?</summary>

### Source [35]: https://queue.acm.org/detail.cfm?id=3676287

Query: What documented problems occur when an LLM is allowed to invoke tools in a simple sequential loop (e.g., getting stuck, mis-ordering calls, latency), and how does the ReAct reasoning-action pattern address these shortcomings?

Answer: When large language models (LLMs) are allowed to invoke tools in a simple sequential loop, several problems can arise:

- **Getting Stuck**: If the LLM repeatedly invokes tools without reaching a satisfactory answer or end condition, it can get stuck in a loop, continuously generating actions without meaningful progress.
- **Mis-ordering Calls**: In simple sequential approaches, the LLM may not have a mechanism to reason effectively about the best order of tool invocations, leading to suboptimal or incorrect sequences of actions.
- **Latency**: Each invocation in a sequential loop adds to the overall computation time, resulting in increased latency, especially if the loop is not efficiently guided by reasoning or planning.

The ReAct (reasoning-action) pattern addresses these shortcomings by interleaving **explicit reasoning steps** with **action steps**. Instead of blindly calling tools in sequence, the LLM first reasons about the situation, considers previous actions and their outcomes, and then decides on the next most appropriate action. This reasoning layer helps prevent infinite loops, ensures actions are better ordered, and can reduce unnecessary computation, thus addressing latency and correctness concerns. The reasoning step acts as a control layer, allowing the model to self-correct and adapt its plan dynamically, leading to more robust and efficient tool use.

-----

-----

-----

### Source [36]: https://arxiv.org/html/2502.02573v1

Query: What documented problems occur when an LLM is allowed to invoke tools in a simple sequential loop (e.g., getting stuck, mis-ordering calls, latency), and how does the ReAct reasoning-action pattern address these shortcomings?

Answer: This source investigates how LLMs handle **sequential optimization problems (SOPs)**, which often require multiple steps and tool invocations. The findings show:

- **Performance Degradation with Complexity**: LLMs perform well on simple sequential tasks but their effectiveness drops as task complexity increases. This is often due to challenges in maintaining coherent reasoning across multiple steps and correctly sequencing tool invocations.
- **Static Sequential Approaches Are Insufficient**: Simple sequential loops do not adequately address the dynamic nature of complex tasks, leading to errors and inefficiencies.
- **Need for Enhanced Reasoning**: The source emphasizes the importance of incorporating advanced reasoning frameworks (such as their proposed ACE, inspired by Hegelian dialectics) to improve LLM performance in sequential contexts. Such frameworks interleave reasoning with action, similar to the ReAct pattern, ensuring the model reflects on past actions before proceeding, thereby reducing the risk of getting stuck or mis-ordering calls.

By adopting a reasoning-action cycle, LLMs can better navigate sequential tasks, adapt to errors, and optimize tool use, addressing the core issues seen in naive sequential loops.

-----

-----

-----

### Source [37]: https://huggingface.co/papers?q=tool-invocation+success

Query: What documented problems occur when an LLM is allowed to invoke tools in a simple sequential loop (e.g., getting stuck, mis-ordering calls, latency), and how does the ReAct reasoning-action pattern address these shortcomings?

Answer: This source highlights several issues LLMs face when allowed to invoke tools in a simple, sequential manner:

- **Struggle with Tool Invocation**: LLMs often utilize tools indiscriminately, especially as task complexity grows, which can lead to inappropriate tool selection and unnecessary or redundant tool calls.
- **Complex Problems Exceed Capability**: For complex tasks, sequential tool invocation often fails because the LLM lacks a structured approach to reasoning about which tool to use and in what order.
- **Need for Structured Patterns**: The document suggests that more sophisticated patterns—like interleaving reasoning with tool use—are necessary for reliable and efficient performance.

The ReAct pattern specifically addresses these problems by enabling the LLM to pause between actions, reason about the current state, and then decide the next action, reducing indiscriminate tool use and improving sequence management.

-----

-----

-----

### Source [38]: https://aclanthology.org/2024.lrec-main.1427.pdf

Query: What documented problems occur when an LLM is allowed to invoke tools in a simple sequential loop (e.g., getting stuck, mis-ordering calls, latency), and how does the ReAct reasoning-action pattern address these shortcomings?

Answer: This source discusses challenges in **autonomous tool utilization** by LLMs:

- **Manual Prompting and Mis-selection**: The decision of which tool to use and when is often guided by manual prompts or retrieval modules that are not fully optimized end-to-end, leading to frequent selection of inappropriate tools.
- **Error Propagation**: In a purely sequential setup, early mistakes (such as choosing an incorrect tool) can propagate through subsequent steps, compounding errors and making recovery difficult.
- **Correction and Adaptation**: There is a critical need for LLMs to have mechanisms for self-correction and adaptive planning.

The ReAct pattern mitigates these issues by introducing explicit reasoning steps between actions. This allows the LLM to assess the outcome of previous tool invocations, reconsider its approach, and adapt dynamically. By reflecting and reasoning before each action, the model can correct mistakes early, reducing error propagation and improving overall task success.

-----

-----

</details>

<details>
<summary>Which tool categories (retrieval-augmented generation, web search/browsing, sandboxed code execution, database querying, etc.) are most common in production AI-agent stacks, and what real-world products or frameworks exemplify each category?</summary>

### Source [39]: https://research.aimultiple.com/ai-agent-tools/

Query: Which tool categories (retrieval-augmented generation, web search/browsing, sandboxed code execution, database querying, etc.) are most common in production AI-agent stacks, and what real-world products or frameworks exemplify each category?

Answer: This source categorizes AI agent tools into several key areas commonly found in production stacks:

- **AI agent builders**: These tools provide platforms for creating and managing agents, often with visual or no-code interfaces. Key features include custom prompt chaining, memory management, API integrations (such as database querying), multi-agent orchestration, and real-time monitoring. Examples include CrewAI, Camel, and Beam AI.
- **Coding agents**: Focused on software development automation, these agents offer code generation, explanation, debugging, integration with IDEs, secure code practices, and Git operations. They exemplify the *sandboxed code execution* category.
- **Web browsing agents**: These agents interact with web pages, perform actions (clicks, form submissions), extract data through scraping, and conduct auto-research by summarizing or comparing content. This represents the *web search/browsing* tool category.
- **Customer support agents**: These handle support tickets, chats, and calls, leveraging contextual memory, CRM integrations, escalation logic, sentiment analysis, and auto-resolution. They often integrate *retrieval-augmented generation* for knowledge base creation and automated responses.

Each category is exemplified by real-world frameworks and products such as CrewAI for agent orchestration and coding agents, and multi-channel support platforms for customer service automation.

-----

-----

-----

### Source [41]: https://www.aalpha.net/blog/ai-agent-technology-stack/

Query: Which tool categories (retrieval-augmented generation, web search/browsing, sandboxed code execution, database querying, etc.) are most common in production AI-agent stacks, and what real-world products or frameworks exemplify each category?

Answer: This source details both open-source and proprietary stacks, highlighting the most common tool categories and real-world frameworks:

- **Open-source model hosting**: LLaMA 2 and 3, Groq, and HuggingFace offer self-hosted or cloud-hosted model inference, critical for retrieval-augmented generation and code execution in controlled environments.
- **Proprietary agent platforms**:
  - **Google A2A (Agents-to-Agents)**: A declarative framework for agent interactions, including built-in safety and sandboxed task execution. Used internally by Google for automated operations and productivity tools.
  - **Microsoft Copilot Stack**: Integrates OpenAI models with business data connectors (Microsoft Graph), focused on productivity tasks like summarization, meeting analysis, and code generation, with deep Office integration.

Key components across these stacks include endpoints for model inference, connectors for business data or databases, and interfaces for secure/sandboxed code execution—demonstrating all the major categories: retrieval-augmented generation, web search/browsing, sandboxed code execution, and database querying.

-----

-----

-----

### Source [42]: https://langfuse.com/blog/2025-03-19-ai-agent-comparison

Query: Which tool categories (retrieval-augmented generation, web search/browsing, sandboxed code execution, database querying, etc.) are most common in production AI-agent stacks, and what real-world products or frameworks exemplify each category?

Answer: This source reviews prominent open-source AI agent frameworks, mapping them to common tool categories:

- **LangGraph, OpenAI Agents SDK, Smolagents, CrewAI, AutoGen, Semantic Kernel, LlamaIndex agents, Strands Agents, and Pydantic AI agents** are all highlighted as frameworks for creating agents that autonomously *reason, plan, and execute tasks*.
- These frameworks differ in their approach: some use explicit, graph-based workflows (e.g., LangGraph); others favor lightweight, code-driven agents (e.g., OpenAI Agents SDK). 
- Core capabilities across these frameworks include *retrieval-augmented generation* (integrating external data sources), *tool orchestration* (combining multiple actions or APIs), and *sandboxed code execution* (for tasks involving code generation or manipulation).
- Real-world adoption is indicated through integrations in customer support, workflow automation, and knowledge management systems.

The frameworks collectively cover the dominant categories—retrieval-augmented generation, web search/browsing, sandboxed code execution, and database querying—within production AI-agent stacks.

-----

</details>

<details>
<summary>How can Pydantic models be leveraged with OpenAI or Gemini function-calling to automatically generate, validate, and consume structured outputs from LLMs?</summary>

### Source [43]: https://ai.pydantic.dev/models/

Query: How can Pydantic models be leveraged with OpenAI or Gemini function-calling to automatically generate, validate, and consume structured outputs from LLMs?

Answer: PydanticAI is designed to be **model-agnostic** and provides built-in support for multiple model providers, including both **OpenAI and Gemini**. This means you can use Pydantic models to define the expected structured output from LLMs and have PydanticAI handle the communication and schema transformation necessary for different providers. When you create an Agent using a provider/model identifier (such as `openai:gpt-4o` or `openrouter:google/gemini-2.5-pro-preview`), PydanticAI will automatically select the correct provider, model class, and "profile" (which describes how requests and schema for a specific model family should be formatted).

This **profile abstraction** ensures that the same Pydantic schema can be used for function calling or structured output generation across both OpenAI and Gemini models, even though these providers may have different requirements or limitations for their function-calling or tool schemas. Thus, developers can leverage their Pydantic models to:
- Automatically generate the correct JSON schema for LLM function-calling or structured outputs.
- Validate and parse the outputs from the LLM into Pydantic models, ensuring type safety and consistency.
- Seamlessly swap between model providers (OpenAI, Gemini, Anthropic, etc.) without needing to rewrite schema handling code.

Customization is possible by directly instantiating a model class and specifying the provider or profile as needed, but the default behavior aims for maximum compatibility and simplicity[1].

-----

-----

-----

### Source [44]: https://ai.pydantic.dev/api/models/gemini/

Query: How can Pydantic models be leveraged with OpenAI or Gemini function-calling to automatically generate, validate, and consume structured outputs from LLMs?

Answer: The `GeminiModel` class in PydanticAI enables direct integration with **Google’s Gemini models** via the Generative Language API, without requiring a dedicated SDK. When initializing a Gemini model, you can specify:
- `model_name`: Which Gemini model to use.
- `provider`: Either `'google-gla'` (for the Generative Language API) or `'google-vertex'` (for Vertex AI).
- `profile`: An optional model profile for fine-tuning schema handling or request formatting.

This setup permits developers to use Pydantic models for structured output or function-calling, leveraging the Pydantic schema to ensure that requests and responses adhere to the expected structure. The authentication and API access are managed through the provider, and you can customize settings or provide custom HTTP clients for advanced use cases.

By binding a GeminiModel to a Pydantic schema, developers can ensure that the outputs from Gemini are automatically validated and parsed into strongly-typed Python objects, reducing boilerplate and error-prone manual parsing[2].

-----

-----

-----

### Source [45]: https://ai.pydantic.dev/models/gemini/

Query: How can Pydantic models be leveraged with OpenAI or Gemini function-calling to automatically generate, validate, and consume structured outputs from LLMs?

Answer: To use Pydantic models with Gemini, you can set your Gemini API key as an environment variable and instantiate a Gemini model by name. You can then use the model in an Agent, which handles all schema generation and validation automatically. 

Example usage:
```python
from pydantic_ai import Agent
agent = Agent('google-gla:gemini-2.0-flash')
```
or, for direct initialization:
```python
from pydantic_ai.models.gemini import GeminiModel
model = GeminiModel('gemini-2.0-flash', provider='google-gla')
agent = Agent(model)
```
You can also provide a custom provider or HTTP client for advanced scenarios. This flexibility allows developers to cleanly integrate Pydantic models with Gemini’s structured output or function-calling capabilities, ensuring that LLM responses are automatically validated and parsed into the desired data structures as defined by your Pydantic models[3].

-----

-----

-----

### Source [46]: https://ai.google.dev/gemini-api/docs/structured-output

Query: How can Pydantic models be leveraged with OpenAI or Gemini function-calling to automatically generate, validate, and consume structured outputs from LLMs?

Answer: When using the Gemini API via the Python library, **Pydantic models** can be directly leveraged to define the expected schema for LLM outputs. The library automatically builds a JSON schema from the Pydantic model and sends it to the API for structured output or function-calling.

Supported types for schema definition include:
- Basic types: `int`, `float`, `bool`, `str`
- Lists: `list[AllowedType]`
- Unions: `AllowedType|AllowedType|...`
- Dictionaries: `dict[str, AllowedType]`
- **User-defined Pydantic models**, supporting custom key names, heterogeneous value types, and nested structures.

This means you can define complex, nested, and strongly-typed output formats using Pydantic, and these will be enforced by the Gemini API when generating structured outputs. The Gemini API supports modern JSON Schema, allowing for accurate mapping between Pydantic models and the schema expected by the LLM.

By using Pydantic models in this way, you gain:
- Automatic schema generation for LLM function-calling or tool use.
- Strong validation and type checking of outputs returned by the LLM.
- Simplified code for consuming and using structured data from LLM responses[4].

-----

-----

</details>

<details>
<summary>What official guidance do OpenAI and Google Gemini give for supporting multiple or parallel function calls in a single response, and what coding patterns are recommended to handle these calls safely?</summary>

### Source [47]: https://python.useinstructor.com/concepts/parallel/

Query: What official guidance do OpenAI and Google Gemini give for supporting multiple or parallel function calls in a single response, and what coding patterns are recommended to handle these calls safely?

Answer: **Parallel Function Calling** is described as a feature that enables the calling of multiple functions in a single request, and it is currently supported in both Google and OpenAI platforms. The documentation emphasizes that this is an experimental feature and users must ensure the correct use of the *parallel tool mode* for their client implementation. No specific coding patterns are detailed in this source, but it stresses the importance of using the equivalent parallel tool mode for the client to enable and support parallel function calls safely.

-----

-----

-----

### Source [48]: https://community.openai.com/t/parallel-tool-use-documentation-for-api-models/1304519

Query: What official guidance do OpenAI and Google Gemini give for supporting multiple or parallel function calls in a single response, and what coding patterns are recommended to handle these calls safely?

Answer: OpenAI's official guidance states that the model may choose to call multiple functions in a single turn if parallel tool calls are enabled. This behavior can be controlled using the `parallel_tool_calls` parameter—setting it to `false` restricts the model to calling zero or one tool only. For fine-tuned models, if multiple functions are called in one turn, strict mode is disabled for those calls. There is a specific warning for the `gpt-4.1-nano-2025-04-14` snapshot, which may inadvertently call the same tool multiple times if parallel tool calls are enabled; disabling the feature is recommended for this model version. The parallel tool calling mechanism functions as a wrapper (`multi_tool_use`), where the developer's function names are included. The source highlights the need to monitor token usage and model support, as not all models behave identically. There are no detailed code patterns provided, but the main configuration is through the parallel tool parameter and tool definitions.

-----

-----

-----

### Source [49]: https://community.openai.com/t/parallel-function-calling/626868

Query: What official guidance do OpenAI and Google Gemini give for supporting multiple or parallel function calls in a single response, and what coding patterns are recommended to handle these calls safely?

Answer: According to the OpenAI Developer Community, function calls are determined by their descriptions and the user's prompt. While multiple functions can be defined, the model does not always call all available functions even when `tool_choice` is set to `"auto"`. In practice, the response may include fewer function calls than the number of functions provided, depending on the model's interpretation of the prompt and tool descriptions. The post suggests that no additional configuration beyond well-defined function signatures and the correct `tool_choice` parameter is needed, but achieving consistent parallel function invocation may require careful prompt engineering or additional guidance in the prompt.

-----

-----

-----

### Source [50]: https://www.pragnakalp.com/parallel-function-calling-in-openai-using-chatgpt/

Query: What official guidance do OpenAI and Google Gemini give for supporting multiple or parallel function calls in a single response, and what coding patterns are recommended to handle these calls safely?

Answer: This guide explains the practical use of OpenAI’s parallel function-calling, where the model can identify and execute multiple functions simultaneously. The provided code example sets `tool_choice` to `"auto"` and collects the results from the `tool_calls` attribute of the response. The workflow includes constructing the function definitions, prompting the model, and handling the results returned from each function call. The example doesn't detail advanced safety or concurrency patterns, but it demonstrates the basic loop: collect user input, send to the API with function definitions, and iterate through the returned tool calls to process results. It implies that the model, when configured for parallel function calling, can handle multiple function invocations per turn, but does not guarantee that all functions will be called unless the prompt is explicit.

-----

-----

-----

### Source [51]: https://community.openai.com/t/advice-to-make-parallel-function-calling-work/578354

Query: What official guidance do OpenAI and Google Gemini give for supporting multiple or parallel function calls in a single response, and what coding patterns are recommended to handle these calls safely?

Answer: This discussion highlights practical issues in achieving reliable parallel function calling. While multiple tools can be set up, the model may not consistently output calls to all functions unless explicitly instructed in the prompt. Even when using the correct GPT version and few-shot prompting, the model sometimes requires explicit direction to invoke multiple functions. The advice from community experience suggests that robust prompt engineering is necessary to increase the likelihood of multiple function calls in a single response, as simply setting up the tools and enabling parallel calling may not suffice.

-----

-----

</details>

<details>
<summary>Which security and sandboxing techniques are recommended in production to let an LLM agent run Python (or other) code-execution tools without exposing the host system to risk?</summary>

### Source [52]: https://dida.do/blog/setting-up-a-secure-python-sandbox-for-llm-agents

Query: Which security and sandboxing techniques are recommended in production to let an LLM agent run Python (or other) code-execution tools without exposing the host system to risk?

Answer: This source discusses the **security challenges of executing LLM-generated code** and introduces sandbox solutions to mitigate risk. It recommends isolating code execution using modern sandboxing technologies rather than direct or naive execution. Specifically, it highlights the use of **gVisor**, a user-space kernel offering strong isolation between the executed code and the host system, as a recommended approach. The blog also describes integrating the sandbox with Jupyter Notebook to manage code input and output, suggesting that running untrusted code in a controlled environment is essential to prevent potential exploits, privilege escalation, or unauthorized access to system resources. The overarching advice is to combine robust sandboxing (like gVisor) with strict input/output controls and monitoring to safely leverage LLM agent capabilities.

-----

-----

-----

### Source [53]: https://amirmalik.net/2025/03/07/code-sandboxes-for-llm-ai-agents

Query: Which security and sandboxing techniques are recommended in production to let an LLM agent run Python (or other) code-execution tools without exposing the host system to risk?

Answer: This post provides an overview of several **sandboxing techniques** for securely running LLM-generated code in production. The main options are:

- **Containers** (e.g., Docker, LXC): Provide strong isolation with minimal performance overhead and are widely used for secure code execution.
- **User-mode kernels** (e.g., gVisor): Intercept and manage Linux system calls, providing an additional isolation layer between code and the host.
- **Virtual machines**: Use hardware virtualization for maximum isolation, though with some performance cost.
- **WebAssembly (Wasm), JVM, others**: Offer sandboxed runtimes for code specifically compiled for them, with WebAssembly being highlighted for its strong isolation and cross-language support.

The author recommends not exposing the underlying code execution engine’s interface directly to agents. Instead, a **sandbox server** with an API should be set up to manage sandbox lifecycle, code execution, and result retrieval. This prevents direct access to sensitive services and allows for better security controls.

-----

-----

-----

### Source [54]: https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/

Query: Which security and sandboxing techniques are recommended in production to let an LLM agent run Python (or other) code-execution tools without exposing the host system to risk?

Answer: This article advocates for using **WebAssembly (Wasm)** to sandbox LLM-generated Python code. Wasm provides a **robust, lightweight, and secure execution environment** that isolates both the host and users from potentially harmful code. Compared to regular expressions or restricted libraries, Wasm offers more comprehensive protection, and is more efficient than containers or virtual machines. The approach requires minimal changes to existing LLM agent architectures and is positioned as a scalable, cost-effective solution for production use, enhancing security for both the host and users.

-----

-----

-----

### Source [55]: https://modal.com/docs/examples/agent

Query: Which security and sandboxing techniques are recommended in production to let an LLM agent run Python (or other) code-execution tools without exposing the host system to risk?

Answer: This Modal example demonstrates using **Modal Sandboxes** to execute Python code generated by an LLM agent. The system relies on containerized environments provided by Modal, ensuring that each code execution runs in a **separate, isolated environment**. The setup requires managing API secrets securely and emphasizes best practices for controlling access to sensitive credentials. While the documentation focuses on implementation details, it implicitly recommends **isolated execution environments (e.g., containers or sandboxes)** and secure secret management as core practices for safely running LLM-generated code in production.

-----

-----

-----

### Source [56]: https://www.covalent.xyz/langchain-and-covalent-sandboxing-ai-generated-code/

Query: Which security and sandboxing techniques are recommended in production to let an LLM agent run Python (or other) code-execution tools without exposing the host system to risk?

Answer: This source describes integrating **Covalent’s high-performance sandbox** with LangChain to execute AI-generated code safely. The sandboxed execution occurs on **remote hardware**, fully separated from the host. This ensures that any malicious or faulty code cannot impact the primary system. The CovalentCloud solution is designed specifically to handle compute-intensive tasks, providing both **resource separation and execution monitoring**. The approach is suitable for production environments where robust isolation and control over resource usage are required for LLM agent code execution.

-----

-----

</details>

<details>
<summary>How does the Model Context Protocol (MCP) or frameworks like LangGraph automate Python function-to-schema conversion and multi-tool orchestration compared with hand-rolled @tool decorators?</summary>

### Source [57]: https://github.com/modelcontextprotocol/python-sdk

Query: How does the Model Context Protocol (MCP) or frameworks like LangGraph automate Python function-to-schema conversion and multi-tool orchestration compared with hand-rolled @tool decorators?

Answer: The **MCP Python SDK** implements the full Model Context Protocol (MCP) specification, which allows for standardized interaction between AI applications and external tools or data sources. This SDK facilitates the process by:

- Enabling developers to **build MCP clients and servers** capable of exposing resources, prompts, and tools.
- Supporting **structured output** and **standard transports** (such as stdio, SSE, and Streamable HTTP), which abstracts away the transport and orchestration logic.
- Handling all **MCP protocol messages and lifecycle events** automatically, meaning developers do not need to manually manage protocol interactions or message formats.

This automation stands in contrast to **hand-rolled @tool decorators** in traditional agent frameworks, where each tool must have its schema, input/output types, and orchestration logic defined manually. With MCP, the protocol handles this standardization and communication, reducing boilerplate and custom glue code. The SDK's design allows for easier integration and orchestration of multiple tools, as the protocol defines clear contracts and message structures, automating much of the process that would otherwise be custom-built for each tool in a decorator-based approach.

-----

-----

-----

### Source [58]: https://ai.pydantic.dev/mcp/

Query: How does the Model Context Protocol (MCP) or frameworks like LangGraph automate Python function-to-schema conversion and multi-tool orchestration compared with hand-rolled @tool decorators?

Answer: The **Model Context Protocol (MCP)** is described as a standardized protocol allowing AI applications (including agents like PydanticAI) to connect to external tools and services using a **common interface**. This standardization means:

- Applications can **speak to each other without specific integrations**, as the protocol defines how tools and services should be exposed and consumed.
- Functionality (such as running Python code) can be provided as **MCP servers**; agents and applications can connect to these servers to access tools and resources without needing to implement their own schema conversion or orchestration logic.

This is in contrast to **hand-rolled @tool decorators**, where every integration requires custom schema definitions and orchestration code. MCP automates this by providing a **uniform interface** for tool discovery, invocation, and data exchange, thereby streamlining the process of adding and managing multiple tools for agents.

-----

-----

-----

### Source [59]: https://openai.github.io/openai-agents-python/mcp/

Query: How does the Model Context Protocol (MCP) or frameworks like LangGraph automate Python function-to-schema conversion and multi-tool orchestration compared with hand-rolled @tool decorators?

Answer: The **OpenAI Agents SDK** explains that MCP is "like a USB-C port for AI applications," providing a **standardized way to connect AI models to different data sources and tools**. Key points related to automation and orchestration include:

- The SDK supports connecting to a variety of **MCP servers**, which can expose tools and prompts to agents.
- The protocol defines **three kinds of servers** (stdio, HTTP over SSE, and Streamable HTTP), and the SDK provides classes (`MCPServerStdio`, `MCPServerSse`, `MCPServerStreamableHttp`) to connect to them.
- When using MCP, **tool listing and orchestration are handled by the framework**—developers typically add servers to agents and let the framework manage tool discovery and invocation.

Compared to **hand-rolled @tool decorators**, where each tool must be explicitly registered and orchestrated, MCP and frameworks like this SDK handle **multi-tool orchestration and schema management automatically** through the protocol’s specification and framework support.

-----

-----

-----

### Source [60]: https://docs.cursor.com/context/mcp

Query: How does the Model Context Protocol (MCP) or frameworks like LangGraph automate Python function-to-schema conversion and multi-tool orchestration compared with hand-rolled @tool decorators?

Answer: Cursor’s documentation emphasizes that MCP allows applications (like Cursor) to **connect to external systems and data** without repeatedly re-explaining project structures or manually integrating each tool. Key points on automation:

- MCP servers can be written in any language and must expose capabilities through the protocol, which Cursor consumes.
- Cursor supports **three standardized transport methods** (stdio, SSE, Streamable HTTP), with configuration managed via a simple JSON file.
- Installing and authenticating new MCP servers is streamlined, enabling rapid integration of new tools and resources.

This approach **eliminates the need for custom glue code** or hand-crafted decorators for each function. Instead, the protocol and its infrastructure manage schema conversion and orchestration, making **multi-tool integration and management far more automated and scalable** compared to traditional decorator-based systems.

-----

-----

</details>

<details>
<summary>What real-world case studies illustrate retrieval-augmented generation (RAG) being exposed as a “knowledge tool” inside LLM agents, and what architectural patterns make this effective in production?</summary>

### Source [61]: https://www.signitysolutions.com/blog/real-world-examples-of-retrieval-augmented-generation

Query: What real-world case studies illustrate retrieval-augmented generation (RAG) being exposed as a “knowledge tool” inside LLM agents, and what architectural patterns make this effective in production?

Answer: This source describes multiple **real-world examples of RAG**, focusing on its deployment in areas such as **virtual assistants and chatbots**. RAG enables these tools to access up-to-date information (like current events, weather, and news) and generate contextually relevant responses. The architecture involves integrating the RAG model within the API layer of a backend system, creating what’s called a **Generative API layer**. 

The typical workflow is:
- The user initiates a query through a chatbot or search interface.
- The API layer calls the RAG model, which uses a custom retriever to fetch relevant data from a knowledge base.
- The retrieved data, along with the query and user context, is combined in a prompt for the generative model.
- The system generates a tailored response, which is then formatted and delivered to the user.

Such architectures allow systems like ChatGPT to deliver **context-aware and dynamic conversational responses**, enhancing the user experience by providing precise, up-to-date answers.

-----

-----

-----

### Source [62]: https://www.pinecone.io/learn/retrieval-augmented-generation/

Query: What real-world case studies illustrate retrieval-augmented generation (RAG) being exposed as a “knowledge tool” inside LLM agents, and what architectural patterns make this effective in production?

Answer: This resource details the **core architectural patterns of RAG** and its application as a “knowledge tool” inside LLM agents. The architecture generally consists of four main steps:
- **Ingestion:** Loading authoritative data (e.g., proprietary data) into a vector database.
- **Retrieval:** Pulling relevant data from this source based on the user’s query.
- **Augmentation:** Combining the retrieved data with the user query in a prompt to provide context for the LLM.
- **Generation:** The LLM generates an output using the contextualized prompt.

Benefits highlighted for production use include:
- **Access to real-time and proprietary data**, enabling use cases like up-to-date Q&A, customer support, or compliance workflows.
- **Trust and transparency:** RAG allows for source citation and human review.
- **Control:** Organizations can determine data sources, enforce guardrails, integrate compliance, and tune components independently.
- **Cost-effectiveness:** Unlike model retraining or large-context-window solutions, RAG is scalable and efficient for enterprise production.

-----

-----

-----

### Source [63]: https://www.glean.com/blog/retrieval-augmented-generation-use-cases

Query: What real-world case studies illustrate retrieval-augmented generation (RAG) being exposed as a “knowledge tool” inside LLM agents, and what architectural patterns make this effective in production?

Answer: This source explains RAG’s role in **dynamic environments** (e.g., news, knowledge management) where rapid access to current information is critical. The **architectural pattern** centers on two main components:
- A **retrieval mechanism** that identifies and sources relevant documents from a database or knowledge repository.
- A **pre-trained language model** that synthesizes a coherent response, integrating the retrieved facts into generated text.

Key enabling technologies include:
- **Transformer architectures** (like BERT and GPT) for language understanding and generation.
- **Vector space embeddings** and **indexing methods** for efficient similarity search and retrieval.
- **Neural network-based retrievers** and advanced ranking algorithms to ensure relevance and accuracy.
- **Machine learning frameworks** (TensorFlow, PyTorch) for model training, deployment, and integration.

This pattern allows RAG to serve as a “knowledge tool” by supplementing LLMs with real-world, domain-specific, or real-time information beyond their training data, addressing knowledge gaps and reducing hallucination.

-----

-----

-----

### Source [64]: https://northernlight.com/the-case-for-using-retrieval-augmented-generation-in-generative-ai-applications-within-the-enterprise/

Query: What real-world case studies illustrate retrieval-augmented generation (RAG) being exposed as a “knowledge tool” inside LLM agents, and what architectural patterns make this effective in production?

Answer: This source emphasizes that RAG is **foundational for deploying generative AI in enterprise applications**. It highlights how RAG mitigates **“hallucination”** (fabrication of facts) by ensuring that responses are grounded in actual, retrievable knowledge. Enterprises use RAG to support applications requiring accurate, up-to-date, and compliance-bound information—such as internal knowledge bases, customer support, and regulated processes.

The typical RAG architecture in enterprise production involves:
- Integrating external, authoritative data repositories with LLM agents.
- Using retrieval modules to fetch supporting evidence.
- Augmenting prompts with retrieved documents.
- Generating responses based on this augmented context, improving factuality and auditability.

In enterprise settings, this architecture is critical for building trust, meeting compliance requirements, and delivering reliable AI-driven insights.

-----

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>Overview</summary>

## Overview

The **tool** abstraction in LangChain associates a Python **function** with a **schema** that defines the function's **name**, **description** and **expected arguments**.

**Tools** can be passed to [chat models](https://python.langchain.com/docs/concepts/chat_models/) that support [tool calling](https://python.langchain.com/docs/concepts/tool_calling/) allowing the model to request the execution of a specific function with specific inputs.

## Key concepts

- Tools are a way to encapsulate a function and its schema in a way that can be passed to a chat model.
- Create tools using the [@tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) decorator, which simplifies the process of tool creation, supporting the following:
  - Automatically infer the tool's **name**, **description** and **expected arguments**, while also supporting customization.
  - Defining tools that return **artifacts** (e.g. images, dataframes, etc.)
  - Hiding input arguments from the schema (and hence from the model) using **injected tool arguments**.

## Tool interface

The tool interface is defined in the [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool) class which is a subclass of the [Runnable Interface](https://python.langchain.com/docs/concepts/runnables/).

The key attributes that correspond to the tool's **schema**:

- **name**: The name of the tool.
- **description**: A description of what the tool does.
- **args**: Property that returns the JSON schema for the tool's arguments.

The key methods to execute the function associated with the **tool**:

- **invoke**: Invokes the tool with the given arguments.
- **ainvoke**: Invokes the tool with the given arguments, asynchronously. Used for [async programming with Langchain](https://python.langchain.com/docs/concepts/async/).

## Create tools using the `@tool` decorator

The recommended way to create tools is using the [@tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) decorator. This decorator is designed to simplify the process of tool creation and should be used in most cases. After defining a function, you can decorate it with [@tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) to create a tool that implements the [Tool Interface](https://python.langchain.com/docs/concepts/tools/#tool-interface).

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
   """Multiply two numbers."""
   return a * b
```

**API Reference:** [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html)

For more details on how to create tools, see the [how to create custom tools](https://python.langchain.com/docs/how_to/custom_tools/) guide.

LangChain has a few other ways to create tools; e.g., by sub-classing the [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool) class or by using `StructuredTool`. These methods are shown in the [how to create custom tools guide](https://python.langchain.com/docs/how_to/custom_tools/), but
we generally recommend using the `@tool` decorator for most cases.

## Use the tool directly

Once you have defined a tool, you can use it directly by calling the function. For example, to use the `multiply` tool defined above:

```python
multiply.invoke({"a": 2, "b": 3})
```

### Inspect

You can also inspect the tool's schema and other properties:

```python
print(multiply.name) # multiply
print(multiply.description) # Multiply two numbers.
print(multiply.args)
# {
# 'type': 'object',
# 'properties': {'a': {'type': 'integer'}, 'b': {'type': 'integer'}},
# 'required': ['a', 'b']
# }
```

If you're using pre-built LangChain or LangGraph components like [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent), you might not need to interact with tools directly. However, understanding how to use them can be valuable for debugging and testing. Additionally, when building custom LangGraph workflows, you may find it necessary to work with tools directly.

## Configuring the schema

The `@tool` decorator offers additional options to configure the schema of the tool (e.g., modify name, description
or parse the function's doc-string to infer the schema).

Please see the [API reference for @tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) for more details and review the [how to create custom tools](https://python.langchain.com/docs/how_to/custom_tools/) guide for examples.

## Tool artifacts

**Tools** are utilities that can be called by a model, and whose outputs are designed to be fed back to a model. Sometimes, however, there are artifacts of a tool's execution that we want to make accessible to downstream components in our chain or agent, but that we don't want to expose to the model itself. For example if a tool returns a custom object, a dataframe or an image, we may want to pass some metadata about this output to the model without passing the actual output to the model. At the same time, we may want to be able to access this full output elsewhere, for example in downstream tools.

```python
@tool(response_format="content_and_artifact")
def some_tool(...) -> Tuple[str, Any]:
    """Tool that does something."""
    ...
    return 'Message for chat model', some_artifact
```

See [how to return artifacts from tools](https://python.langchain.com/docs/how_to/tool_artifacts/) for more details.

## Special type annotations

There are a number of special type annotations that can be used in the tool's function signature to configure the run time behavior of the tool.

The following type annotations will end up **removing** the argument from the tool's schema. This can be useful for arguments that should not be exposed to the model and that the model should not be able to control.

- **InjectedToolArg**: Value should be injected manually at runtime using `.invoke` or `.ainvoke`.
- **RunnableConfig**: Pass in the RunnableConfig object to the tool.
- **InjectedState**: Pass in the overall state of the LangGraph graph to the tool.
- **InjectedStore**: Pass in the LangGraph store object to the tool.

You can also use the `Annotated` type with a string literal to provide a **description** for the corresponding argument that **WILL** be exposed in the tool's schema.

- **Annotated\[..., "string literal"\]** \-\- Adds a description to the argument that will be exposed in the tool's schema.

### InjectedToolArg

There are cases where certain arguments need to be passed to a tool at runtime but should not be generated by the model itself. For this, we use the `InjectedToolArg` annotation, which allows certain parameters to be hidden from the tool's schema.

For example, if a tool requires a `user_id` to be injected dynamically at runtime, it can be structured in this way:

```python
from langchain_core.tools import tool, InjectedToolArg

@tool
def user_specific_tool(input_data: str, user_id: InjectedToolArg) -> str:
    """Tool that processes input data."""
    return f"User {user_id} processed {input_data}"
```

**API Reference:** [tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) \| [InjectedToolArg](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolArg.html)

Annotating the `user_id` argument with `InjectedToolArg` tells LangChain that this argument should not be exposed as part of the tool's schema.

See [how to pass run time values to tools](https://python.langchain.com/docs/how_to/tool_runtime/) for more details on how to use `InjectedToolArg`.

### RunnableConfig

You can use the `RunnableConfig` object to pass custom run time values to tools.

If you need to access the [RunnableConfig](https://python.langchain.com/docs/concepts/runnables/#runnableconfig) object from within a tool. This can be done by using the `RunnableConfig` annotation in the tool's function signature.

```python
from langchain_core.runnables import RunnableConfig

@tool
async def some_func(..., config: RunnableConfig) -> ...:
    """Tool that does something."""
    # do something with config
    ...

await some_func.ainvoke(..., config={"configurable": {"value": "some_value"}})
```

**API Reference:** [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html)

The `config` will not be part of the tool's schema and will be injected at runtime with appropriate values.

You may need to access the `config` object to manually propagate it to subclass. This happens if you're working with python 3.9 / 3.10 in an [async](https://python.langchain.com/docs/concepts/async/) environment and need to manually propagate the `config` object to sub-calls.

Please read [Propagation RunnableConfig](https://python.langchain.com/docs/concepts/runnables/#propagation-of-runnableconfig) for more details to learn how to propagate the `RunnableConfig` down the call chain manually (or upgrade to Python 3.11 where this is no longer an issue).

### InjectedState

Please see the [InjectedState](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedState) documentation for more details.

### InjectedStore

Please see the [InjectedStore](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.tool_node.InjectedStore) documentation for more details.

## Best practices

When designing tools to be used by models, keep the following in mind:

- Tools that are well-named, correctly-documented and properly type-hinted are easier for models to use.
- Design simple and narrowly scoped tools, as they are easier for models to use correctly.
- Use chat models that support [tool-calling](https://python.langchain.com/docs/concepts/tool_calling/) APIs to take advantage of tools.

## Toolkits

LangChain has a concept of **toolkits**. This a very thin abstraction that groups tools together that
are designed to be used together for specific tasks.

### Interface

All Toolkits expose a `get_tools` method which returns a list of tools. You can therefore do:

```python
# Initialize a toolkit
toolkit = ExampleToolkit(...)

# Get list of tools
tools = toolkit.get_tools()
```

</details>

<details>
<summary>When you face a problem with no simple answer, you often need to follow several steps, think carefully, and remember what you’ve already tried. LLM agents are designed for exactly these kinds of situations in language model applications. They combine thorough data analysis, strategic planning, data retrieval, and the ability to learn from past actions to solve complex issues.</summary>

When you face a problem with no simple answer, you often need to follow several steps, think carefully, and remember what you’ve already tried. LLM agents are designed for exactly these kinds of situations in language model applications. They combine thorough data analysis, strategic planning, data retrieval, and the ability to learn from past actions to solve complex issues.

In this article, we'll explore what LLM agents are, their benefits, abilities, practical examples, and the challenges they face.

https://cdn.prod.website-files.com/614c82ed388d53640613982e/66aa02651c656df9e8e5b5ab_664c84b32b64b4ff95ca29a9_llm-agent.webp

LLM agents

## What are LLM agents?

LLM agents are advanced AI systems designed for creating complex text that needs sequential reasoning. They can think ahead, remember past conversations, and use different tools to adjust their responses based on the situation and style needed.

Consider a question in the legal field that sounds like this:

> **_"What are the potential legal outcomes of a specific type of contract breach in California?"_**

A basic LLM with a [retrieval augmented generation (RAG)](https://www.superannotate.com/blog/rag-explained) system can easily fetch the needed information from legal databases.

Now, consider a more detailed scenario:

> **_"In light of new data privacy laws, what are the common legal challenges companies face, and how have courts addressed these issues?"_**

This question digs deeper than just looking up facts. It's about understanding new rules, how they affect different companies, and finding out what courts have said about it all. A simple RAG system can pull up relevant laws and cases, but it lacks the ability to connect these laws to actual business situations or analyze court decisions in depth.

In such situations, when the project demands sequential reasoning, planning, and memory, LLM agents come into play.

For this question, the agent can break down its tasks into subtasks like so. The first subtask may be accessing legal databases to retrieve the latest laws and regulations. Secondly, it can establish a historical baseline of how similar issues were previously handled. Another subtask can be summarizing legal documents and forecasting future trends based on observed patterns.

To complete these subtasks, the LLM agent requires a structured plan, a reliable memory to track progress, and access to necessary tools. These components form the backbone of an LLM agent’s workflow.

## LLM agent components

LLM agents generally consist of four components:

- Agent/brain
- Planning
- Memory
- Tool use

https://cdn.prod.website-files.com/614c82ed388d53640613982e/66aa02651c656df9e8e5b5b3_664c8772c80586fb49458bb3_llm-agent-structure.webp

LLM agent structure

Let’s discuss each of them.

### Agent/brain

At the core of an LLM agent is a language model (or a [large action model](https://www.superannotate.com/blog/large-action-models)) that processes and understands language based on a vast amount of data it's been trained on.

When you use an LLM agent, you start by giving it a specific prompt. This prompt is crucial—it guides the agent on how to respond, what tools to use, and the goals it should aim to achieve during the interaction. It's like giving directions to a navigator before a journey.

Additionally, you can customize the agent with a [specific persona](https://github.com/Neph0s/awesome-llm-role-playing-with-persona). This means setting up the agent with certain characteristics and expertise that make it better suited for particular tasks or interactions. It's about tuning the agent to perform tasks in a way that feels right for the situation.

Essentially, the core of an LLM agent combines advanced processing abilities with customizable features to effectively handle and adapt to various tasks and interactions.

### Memory

[The memory of LLM agents](https://dev.to/datalynx/memory-in-llm-agents-121) helps them handle complex LLM tasks with a record of what’s been done before. There are two main memory types:

**Short-term memory:** This is like the agent’s notepad, where it quickly writes down important details during a conversation. It keeps track of the ongoing discussion, helping the model respond relevantly to the immediate context. However, this memory is temporary, clearing out once the task at hand is completed.

**Long-term memory:** Think of this as the agent’s diary, storing insights and information from past interactions over weeks or even months. This isn't just about holding data; it's about understanding patterns, learning from previous tasks, and recalling this information to make better decisions in future interactions.

By blending these two types of memory, the model can keep up with current conversations and tap into a rich history of interactions. This means it can offer more tailored responses and remember user preferences over time, making each conversation feel more connected and relevant. In essence, the agent is building an understanding that helps it serve you better in each interaction.

### Planning

Through planning, LLM agents can reason, break down complicated tasks into smaller, more manageable parts, and develop specific plans for each part. As tasks evolve, agents can also reflect on and adjust their plans, making sure they stay relevant to real-world situations. This adaptability is key to successfully completing tasks.

Planning typically involves two main stages: plan formulation and plan reflection.

#### Plan formulation

During this stage, agents break down a large task into smaller sub-tasks. Some task decomposition approaches suggest creating a detailed plan all at once and then following it step by step. Others, like the [chain of thought (CoT)](https://www.superannotate.com/blog/chain-of-thought-cot-prompting) method, recommend a more adaptive strategy where agents tackle sub-tasks one by one, allowing for greater flexibility. [Tree of thought (ToT)](https://github.com/princeton-nlp/tree-of-thought-llm) is another approach that takes the CoT technique further by exploring different paths to solve a problem. It breaks the problem into several steps, generating multiple ideas at each step and arranging them like branches on a tree.

https://cdn.prod.website-files.com/614c82ed388d53640613982e/66aa02651c656df9e8e5b5af_664c850e2b64b4ff95ca9b9e_single-multi-path-reasoning-llm-agent.webp

Single-path vs. Multi-path reasoning: [Source](https://arxiv.org/abs/2308.11432)

There are also methods that use a hierarchical approach or structure plans like a [decision tree](https://en.wikipedia.org/wiki/Decision_tree), considering all possible options before finalizing a plan. While LLM-based agents are generally knowledgeable, they sometimes struggle with tasks that require specialized knowledge. Integrating these agents with domain-specific planners has proven to improve their performance.

#### Plan reflection

After creating a plan, it’s important for agents to review and assess its effectiveness. LLM-based agents use internal feedback mechanisms, drawing on existing models to refine their strategies. They also interact with humans to adjust their plans based on human feedback and preferences. Agents can also gather insights from their environments, both real and virtual, using outcomes and observations to refine their plans further.

Two effective methods for incorporating feedback in planning are [ReAct](https://arxiv.org/abs/2210.03629) and [Reflexion](https://arxiv.org/abs/2303.11366).

ReAct, for instance, helps an LLM solve complex tasks by cycling through a sequence of thought, action, and observation, repeating these steps as needed. It takes in feedback from the environment, which can include observations as well as input from humans or other models. This method allows the LLM to adjust its approach based on real-time feedback, enhancing its ability to answer questions more effectively.

### Tools use

Tools in this term are various resources that help LLM agents connect with external environments to perform certain tasks. These tasks might include extracting information from databases, querying, coding, and anything else the agent needs to function. When an LLM agent uses these tools, it follows specific workflows to carry out tasks, gather observations, or collect the information needed to complete subtasks and fulfill user requests.

Here are some examples of how different systems integrate these tools:

- [MRKL](https://arxiv.org/abs/2205.00445) (Modular reasoning, knowledge, and language): This system uses a collection of expert modules, ranging from neural networks to simple tools like calculators or weather APIs. The main LLM acts as a router, directing queries to the appropriate expert module based on the task.

In one test, an LLM was trained to use a calculator for arithmetic problems. The study found that while the LLM could handle direct math queries, it struggled with word problems that required extracting numbers and operations from text. This highlights the importance of knowing when and how to use external tools effectively.

Here’s an [example](https://www.pinecone.io/learn/series/langchain/langchain-agents/) where GPT 4 is asked to tell the answer to 4.1 \* 7.9, and it fails:

https://cdn.prod.website-files.com/614c82ed388d53640613982e/66aa02651c656df9e8e5b59d_664c85cc96d4a4eb6930d610_example.webp

[Source](https://www.pinecone.io/learn/series/langchain/langchain-agents/)

- ‍ [Toolformer](https://arxiv.org/abs/2302.04761) and [TALM (Tool Augmented Language Models)](https://arxiv.org/abs/2205.12255): These models are specifically fine-tuned to interact with external APIs effectively. For instance, the model could be trained to use a financial API to analyze stock market trends or predict currency fluctuations, allowing it to provide real-time financial insights directly to users.

- [HuggingGPT](https://arxiv.org/abs/2303.17580): This framework uses ChatGPT to manage tasks by selecting the best models available on the HuggingFace platform to handle specific requests and then summarizing the outcomes.
- [API-Bank](https://arxiv.org/abs/2304.08244): A benchmark that tests how well LLMs can use 53 commonly used APIs to handle tasks like scheduling, health data management, or smart home control.

## What can LLM agents do?

LLM agents can solve advanced problems, learn from their mistakes, use specialized tools to improve their work, and even collaborate with other agents to improve their performance. Here’s a closer look at some of the standout capabilities that make LLM agents so valuable:

1. **Advanced problem solving:** LLM agents can handle and execute complex tasks efficiently. They can generate project plans, write code, run benchmarks, create summaries, etc. These tasks show their ability to plan and execute tasks that require a high level of cognitive engagement.
2. **Self-reflection and improvement:** LLM agents are able to analyze their own output, identify any issues, and make necessary improvements. This [self-reflection](https://blog.langchain.com/reflection-agents/) ability allows them to engage in a cycle of criticism and rewriting, continuously enhancing their performance across a variety of tasks such as coding, writing text, and answering complex questions.
3. **Tool use:** LLM agents can evaluate their own output, ensuring the accuracy and correctness of their work. For instance, they might run unit tests on their code or use web searches to verify the accuracy of the information in their text. This critical evaluation helps them recognize errors and suggest necessary corrections.
4. **Multi-agent framework:** In a [multi-agent LLM](https://www.superannotate.com/blog/multi-agent-llms) framework, one agent can generate outputs, and another can critique and provide feedback, resulting in advanced performance.

## LLM agent **frameworks**

Let’s take a look at some [notable LLM agents](https://github.com/kaushikb11/awesome-llm-agents) and frameworks:

- [Langchain](https://github.com/langchain-ai/langchain) \- A framework for developing LLM-powered applications that simplifies the LLM application lifecycle.

\- CSV Agent

\- [JSON Agent](https://python.langchain.com/docs/introduction/)

\- [OpenAPI Agent](https://github.com/langchain-ai/langchain/tree/v0.2/templates/openai-functions-agent/)

\- [Pandas Dataframe Agent](https://python.langchain.com/v0.2/docs/integrations/tools/pandas/)

\- [Python Agent](https://python.langchain.com/v0.2/docs/integrations/tools/python/)

\- [SQL Database Agent](https://python.langchain.com/v0.2/docs/integrations/tools/sql_database/)

\- [Vectorstore Agent](https://js.langchain.com/v0.2/docs/integrations/toolkits/vectorstore/)
- [Llama Index](https://github.com/run-llama/llama_index): A data framework that simplifies the creation of LLM applications with data connectors and structuring, advanced retrieval interfac and integration capabilities..

\- [Llama Hub](https://github.com/run-llama/llama-hub) \- Community-driven library for data loaders, readers, and tools. [‍](https://github.com/deepset-ai/haystack)
- [Haystack](https://github.com/deepset-ai/haystack) \- An end-to-end NLP framework that enables you to build NLP applications.

\- [Haystack Agent](https://docs.haystack.deepset.ai/docs/agents)

\- [SearchEngine](https://github.com/deepset-ai/haystack/issues/2392)

\- [TopPSampler](https://docs.haystack.deepset.ai/docs/toppsampler)
- [Embedchain](https://github.com/mem0ai/mem0/tree/main/embedchain) \- A framework to create ChatGPT-like bots for your dataset.

\- [JS Repo](https://github.com/mem0ai/embedchainjs)
- [MindSearch](https://github.com/InternLM/MindSearch): A new AI search engine framework that works similarly to [Perplexity.ai Pro](https://www.perplexity.ai/). You can set it up as your own search engine using either proprietary LLMs like GPT and Claude or open-source models like [InternLM2.5-7b-chat](https://huggingface.co/internlm/internlm2_5-7b-chat). It's built to browse hundreds of web pages to answer any question, providing detailed responses and showing how it found those answers.
- [AgentQ](https://medium.com/@ignacio.de.gregorio.noblejas/agentq-a-human-beating-ai-agent-85353bfd1c26): Helps create autonomous web agents that can plan, adapt, and self-correct. It integrates guided Monte Carlo tree search (MCTS), AI self-critique, and [RLHF](https://www.superannotate.com/blog/rlhf-for-llm) using the [direct preference optimization (DPO)](https://www.superannotate.com/blog/direct-preference-optimization-dpo) algorithm.
- [Nvidia NIM agent blueprints](https://blogs.nvidia.com/blog/nim-agent-blueprints/): An agent for enterprise developers who need to build and deploy customized GenAI applications.
- [Bee agent framework](https://github.com/i-am-bee/beeai-framework): An open-source framework by IBM for building, deploying, and serving large agentic workflows at scale. IBM’s goal with Bee is to empower developers to adopt the latest open-source and proprietary models with minimal changes to their current agent implementation.

## LLM agent challenges

While LLM agents are incredibly useful, they do face several [challenges](https://medium.com/@andrewhnberry/the-challenges-of-building-robust-ai-agents-52b1d29579c2) that we need to consider:

1. **Limited context:** LLM agents can only keep track of a limited amount of information at a time. This means they might not remember important details from earlier in a conversation or miss crucial instructions. Although techniques like vector stores help by providing access to more information, they can't completely solve this issue.
2. **Difficulty with long-term planning:** It's tough for LLM agents to make plans that span over long periods. They often struggle to adapt when unexpected problems pop up, which can make them less flexible compared to how humans approach problem-solving.
3. **Inconsistent outputs**: Since LLM agents rely on natural language to interact with other tools and databases, they sometimes produce unreliable outputs. They might make formatting mistakes or not follow instructions correctly, which can lead to errors in the tasks they perform.
4. **Adapting to specific roles:** LLM agents need to be able to handle different roles depending on the task at hand. However, fine-tuning them to understand and perform uncommon roles or align with diverse human values is a complex challenge.
5. **Prompt dependence:** LLM agents operate based on prompts, but these prompts need to be very precise. Even small changes can lead to big mistakes, so creating and refining these prompts can be a delicate process.
6. **Managing knowledge:** Keeping an LLM agent's knowledge accurate and unbiased is tricky. They must have the right information to make informed decisions, but too much irrelevant information can lead them to draw incorrect conclusions or act on outdated facts.
7. **Cost and efficiency:** Running LLM agents can be resource-intensive. They often need to process a lot of data quickly, which can be costly and may slow down their performance if not managed well.

Addressing these challenges is crucial for improving the effectiveness and reliability of LLM agents in various applications.

## Final thoughts

In conclusion, LLM agents are powerful tools for tackling complex LLM tasks. They can plan, find information, remember past interactions, and learn from them, making them indispensable when answers aren't just black and white. However, they have limitations, such as a short memory span and a need for precise directions. By working to overcome these challenges, we can enhance their abilities and make them even more effective and adept at complex LLM problems.

https://cdn.prod.website-files.com/614c82ed388d53640613982e/680f78e3dfe69749cc50f406_faq.webp

## Common Questions

This FAQ section highlights the key points about LLM agents.

### What are LLM agents?

LLM agents are advanced AI systems designed for creating complex text that requires sequential reasoning. They can think ahead, remember past conversations, and use different tools to adjust their responses based on the situation and style needed.

### What are the core components of an LLM agent?

LLM agents generally consist of four components: the agent or brain, which is the core language model processing and understanding language based on training data; planning, which enables breaking down complex tasks into manageable subtasks; memory, including short-term memory to track ongoing discussions and long-term memory to retain past information; and tool use, which is the capability to utilize external tools or databases to enhance responses.

### How do LLM agents differ from traditional LLMs or RAG systems?

While traditional LLMs or Retrieval Augmented Generation (RAG) systems can fetch information from databases, they often lack the ability to connect laws to actual business situations or analyze court decisions in depth. LLM agents, however, can break down tasks into subtasks, establish historical baselines, and forecast future trends based on observed patterns.

### What can LLM agents do?

LLM agents can solve advanced problems by handling complex, multi-step tasks that require high-level cognitive engagement, such as generating project plans, writing code, running benchmarks, and creating summaries. They improve their performance through self-reflection, analyzing their own output to identify issues and make necessary revisions. By using specialized tools like unit tests or web searches, they ensure the accuracy and correctness of their work. Additionally, in multi-agent frameworks, LLM agents can collaborate by generating outputs and providing feedback to each other, resulting in even more advanced and reliable performance.

### What are LLM agent frameworks?

LLM agent frameworks are structured systems designed to build and manage agents with capabilities like planning, memory, and tool use. Some popular frameworks include LangChain, Autogen, CrewAI, MetaGPT, and Superagent. These frameworks provide the infrastructure to operationalize LLM agents for practical, real-world applications.

### What challenges do LLM agents face?

LLM agents face challenges like limited context, which restricts how much information they can track at once, and difficulty with long-term planning and adapting to unexpected problems. They may produce inconsistent outputs due to reliance on natural language and require very precise prompts to avoid mistakes. Managing accurate knowledge is complex, and running these agents can be costly and resource-intensive.

https://www.superannotate.com/blog/llm-agents

</details>

<details>
<summary>Model Providers</summary>

# Model Providers

PydanticAI is model-agnostic and has built-in support for multiple model providers:

- [OpenAI](https://ai.pydantic.dev/models/openai/)
- [Anthropic](https://ai.pydantic.dev/models/anthropic/)
- [Gemini](https://ai.pydantic.dev/models/gemini/) (via two different APIs: Generative Language API and VertexAI API)
- [Groq](https://ai.pydantic.dev/models/groq/)
- [Mistral](https://ai.pydantic.dev/models/mistral/)
- [Cohere](https://ai.pydantic.dev/models/cohere/)
- [Bedrock](https://ai.pydantic.dev/models/bedrock/)

## OpenAI-compatible Providers

In addition, many providers are compatible with the OpenAI API, and can be used with `OpenAIModel` in PydanticAI:

- [DeepSeek](https://ai.pydantic.dev/models/openai/#deepseek)
- [Grok (xAI)](https://ai.pydantic.dev/models/openai/#grok-xai)
- [Ollama](https://ai.pydantic.dev/models/openai/#ollama)
- [OpenRouter](https://ai.pydantic.dev/models/openai/#openrouter)
- [Perplexity](https://ai.pydantic.dev/models/openai/#perplexity)
- [Fireworks AI](https://ai.pydantic.dev/models/openai/#fireworks-ai)
- [Together AI](https://ai.pydantic.dev/models/openai/#together-ai)
- [Azure AI Foundry](https://ai.pydantic.dev/models/openai/#azure-ai-foundry)
- [Heroku](https://ai.pydantic.dev/models/openai/#heroku-ai)
- [GitHub Models](https://ai.pydantic.dev/models/openai/#github-models)

PydanticAI also comes with [`TestModel`](https://ai.pydantic.dev/api/models/test/) and [`FunctionModel`](https://ai.pydantic.dev/api/models/function/)
for testing and development.

To use each model provider, you need to configure your local environment and make sure you have the right
packages installed.

## Models and Providers

PydanticAI uses a few key terms to describe how it interacts with different LLMs:

- **Model**: This refers to the PydanticAI class used to make requests following a specific LLM API
(generally by wrapping a vendor-provided SDK, like the `openai` python SDK). These classes implement a
vendor-SDK-agnostic API, ensuring a single PydanticAI agent is portable to different LLM vendors without
any other code changes just by swapping out the Model it uses. Model classes are named
roughly in the format `<VendorSdk>Model`, for example, we have `OpenAIModel`, `AnthropicModel`, `GeminiModel`,
etc. When using a Model class, you specify the actual LLM model name (e.g., `gpt-4o`,
`claude-3-5-sonnet-latest`, `gemini-1.5-flash`) as a parameter.
- **Provider**: This refers to provider-specific classes which handle the authentication and connections
to an LLM vendor. Passing a non-default _Provider_ as a parameter to a Model is how you can ensure
that your agent will make requests to a specific endpoint, or make use of a specific approach to
authentication (e.g., you can use Vertex-specific auth with the `GeminiModel` by way of the `VertexProvider`).
In particular, this is how you can make use of an AI gateway, or an LLM vendor that offers API compatibility
with the vendor SDK used by an existing Model (such as `OpenAIModel`).
- **Profile**: This refers to a description of how requests to a specific model or family of models need to be
constructed to get the best results, independent of the model and provider classes used.
For example, different models have different restrictions on the JSON schemas that can be used for tools,
and the same schema transformer needs to be used for Gemini models whether you're using `GoogleModel`
with model name `gemini-2.5-pro-preview`, or `OpenAIModel` with `OpenRouterProvider` and model name `google/gemini-2.5-pro-preview`.

When you instantiate an [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent) with just a name formatted as `<provider>:<model>`, e.g. `openai:gpt-4o` or `openrouter:google/gemini-2.5-pro-preview`,
PydanticAI will automatically select the appropriate model class, provider, and profile.
If you want to use a different provider or profile, you can instantiate a model class directly and pass in `provider` and/or `profile` arguments.

## Custom Models

To implement support for a model API that's not already supported, you will need to subclass the [`Model`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model) abstract base class.
For streaming, you'll also need to implement the [`StreamedResponse`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.StreamedResponse) abstract base class.

The best place to start is to review the source code for existing implementations, e.g. [`OpenAIModel`](https://github.com/pydantic/pydantic-ai/blob/main/pydantic_ai_slim/pydantic_ai/models/openai.py).

For details on when we'll accept contributions adding new models to PydanticAI, see the [contributing guidelines](https://ai.pydantic.dev/contributing/#new-model-rules).

If a model API is compatible with the OpenAI API, you do not need a custom model class and can provide your own [custom provider](https://ai.pydantic.dev/models/openai/#openai-compatible-models) instead.

## Fallback Model

You can use [`FallbackModel`](https://ai.pydantic.dev/api/models/fallback/#pydantic_ai.models.fallback.FallbackModel) to attempt multiple models
in sequence until one successfully returns a result. Under the hood, PydanticAI automatically switches
from one model to the next if the current model returns a 4xx or 5xx status code.

In the following example, the agent first makes a request to the OpenAI model (which fails due to an invalid API key),
and then falls back to the Anthropic model.

fallback\_model.py

```
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.fallback import FallbackModel
from pydantic_ai.models.openai import OpenAIModel

openai_model = OpenAIModel('gpt-4o')
anthropic_model = AnthropicModel('claude-3-5-sonnet-latest')
fallback_model = FallbackModel(openai_model, anthropic_model)

agent = Agent(fallback_model)
response = agent.run_sync('What is the capital of France?')
print(response.data)
#> Paris

print(response.all_messages())
"""
[\
    ModelRequest(\
        parts=[\
            UserPromptPart(\
                content='What is the capital of France?',\
                timestamp=datetime.datetime(...),\
                part_kind='user-prompt',\
            )\
        ],\
        kind='request',\
    ),\
    ModelResponse(\
        parts=[TextPart(content='Paris', part_kind='text')],\
        model_name='claude-3-5-sonnet-latest',\
        timestamp=datetime.datetime(...),\
        kind='response',\
        vendor_id=None,\
    ),\
]
"""

```

The `ModelResponse` message above indicates in the `model_name` field that the output was returned by the Anthropic model, which is the second model specified in the `FallbackModel`.

Each model's options should be configured individually. For example, `base_url`, `api_key`, and custom clients should be set on each model itself, not on the `FallbackModel`.

### Per-Model Settings

You can configure different [`ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings) for each model in a fallback chain by passing the `settings` parameter when creating each model. This is particularly useful when different providers have different optimal configurations:

fallback\_model\_per\_settings.py

```
from pydantic_ai import Agent
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.fallback import FallbackModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.settings import ModelSettings

# Configure each model with provider-specific optimal settings
openai_model = OpenAIModel(
    'gpt-4o',
    settings=ModelSettings(temperature=0.7, max_tokens=1000)  # Higher creativity for OpenAI
)
anthropic_model = AnthropicModel(
    'claude-3-5-sonnet-latest',
    settings=ModelSettings(temperature=0.2, max_tokens=1000)  # Lower temperature for consistency
)

fallback_model = FallbackModel(openai_model, anthropic_model)
agent = Agent(fallback_model)

result = agent.run_sync('Write a creative story about space exploration')
print(result.output)
"""
In the year 2157, Captain Maya Chen piloted her spacecraft through the vast expanse of the Andromeda Galaxy. As she discovered a planet with crystalline mountains that sang in harmony with the cosmic winds, she realized that space exploration was not just about finding new worlds, but about finding new ways to understand the universe and our place within it.
"""

```

In this example, if the OpenAI model fails, the agent will automatically fall back to the Anthropic model with its own configured settings. The `FallbackModel` itself doesn't have settings - it uses the individual settings of whichever model successfully handles the request.

In this next example, we demonstrate the exception-handling capabilities of `FallbackModel`.
If all models fail, a [`FallbackExceptionGroup`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.FallbackExceptionGroup) is raised, which
contains all the exceptions encountered during the `run` execution.

fallback\_model\_failure.py

```
from pydantic_ai import Agent
from pydantic_ai.exceptions import ModelHTTPError
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.fallback import FallbackModel
from pydantic_ai.models.openai import OpenAIModel

openai_model = OpenAIModel('gpt-4o')
anthropic_model = AnthropicModel('claude-3-5-sonnet-latest')
fallback_model = FallbackModel(openai_model, anthropic_model)

agent = Agent(fallback_model)
try:
    response = agent.run_sync('What is the capital of France?')
except* ModelHTTPError as exc_group:
    for exc in exc_group.exceptions:
        print(exc)

```

Since [`except*`](https://docs.python.org/3/reference/compound_stmts.html#except-star) is only supported
in Python 3.11+, we use the [`exceptiongroup`](https://github.com/agronholm/exceptiongroup) backport
package for earlier Python versions:

fallback\_model\_failure.py

```
from exceptiongroup import catch

from pydantic_ai import Agent
from pydantic_ai.exceptions import ModelHTTPError
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.fallback import FallbackModel
from pydantic_ai.models.openai import OpenAIModel

def model_status_error_handler(exc_group: BaseExceptionGroup) -> None:
    for exc in exc_group.exceptions:
        print(exc)

openai_model = OpenAIModel('gpt-4o')
anthropic_model = AnthropicModel('claude-3-5-sonnet-latest')
fallback_model = FallbackModel(openai_model, anthropic_model)

agent = Agent(fallback_model)
with catch({ModelHTTPError: model_status_error_handler}):
    response = agent.run_sync('What is the capital of France?')

```

By default, the `FallbackModel` only moves on to the next model if the current model raises a
[`ModelHTTPError`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelHTTPError). You can customize this behavior by
passing a custom `fallback_on` argument to the `FallbackModel` constructor.

</details>

<details>
<summary>⚠️ Error scraping https://aclanthology.org/2024.lrec-main.1427.pdf: Request Timeout: Failed to scrape URL as the request timed out. Request timed out - No additional error details provided.</summary>

⚠️ Error scraping https://aclanthology.org/2024.lrec-main.1427.pdf: Request Timeout: Failed to scrape URL as the request timed out. Request timed out - No additional error details provided.

</details>

<details>
<summary>As large language models become more integrated into computational systems, their role in enhancing application efficiency and accuracy grows. However, this expanded capability brings new risks when executing autonomously generated code.</summary>

As large language models become more integrated into computational systems, their role in enhancing application efficiency and accuracy grows. However, this expanded capability brings new risks when executing autonomously generated code.

This blog post explores how to establish a secure Python sandbox for LLM agents. We will cover the threats involved with LLM-generated code and introduce a sandbox solution using gVisor and Jupyter Notebook.

## LLM Agents

Incorporating LLMs into software applications can be achieved in several ways, which lie on the agency spectrum. At one end of this spectrum is the simple use of LLMs, where the software makes API calls and parses responses. While straightforward, this approach is vulnerable to errors and hallucinations. Towards the high agency end are more sophisticated [agentic systems](https://huggingface.co/docs/smolagents/en/conceptual_guides/intro_agents) where LLMs have the autonomy to use tools to achieve tasks. These systems stand out for their ability to navigate scenarios lacking a predetermined workflow, which is often the case in real-world applications.

While some agentic systems define custom workflows by deciding to use one of the predefined functions called **tools** with specific parameters, at the high end of the agency spectrum LLM agents can write and execute their own code. This capability is particularly useful in dynamic environments or for complex tasks like creating custom data visualizations, where precise and customized solutions are necessary. By generating and executing code, these agents can adapt to the specific requirements of each problem, achieving a level of customization that standard functions cannot provide.

## Sandboxing Code

With increased agency in LLM systems comes increased risk. Executing potentially unsafe code generated by these agents can expose systems to security issues, including arbitrary code execution ( `os.system`, `subprocess`, etc.), resource exhaustion (Denial-of-service attack via CPU, memory or disc overload), file system access (unauthorized reads/writes to files) and many others. Implementing a secure method to execute this code is crucial.

Mitigating these risks can be achieved through the implementation of a secure Python sandbox. The essential goal of such sandbox is to manage resources and create safe execution environments that encapsulate potentially harmful code, preventing it from affecting the broader system.

## The Demo Solution

One potential solution to securely execute Python code remotely consists of a [FastAPI](https://fastapi.tiangolo.com/) server that runs a [jupyter](https://jupyter.org/) notebook kernel inside a [gVisor](https://gvisor.dev/) container. Here is how different components of the solution work together:

- **Jupyter Notebook** allows to run interactive code notebooks. Jupyter kernels support different environments, including Python, R, Julia, JavaScript, and others. Jupyter kernels are isolated and have limited permissions but do not offer other security features. In our solution Jupyter Notebook plays the role of a code execution environment that works out of the box.

- **FastAPI** is a modern web framework for building APIs with Python. FastAPI serves as the interface between the LLM agent and the Jupyter kernel, allowing the agent to send code for execution over the network and receive results. FastAPI helps us to decouple the agent and the execution environment, which is important for resource management and sandbox scaling.

- **gVisor** is a user-space kernel that provides a secure environment for running untrusted code. It acts as a barrier between the code and the host operating system, preventing unauthorized access to system resources. gVisor intercepts system calls made by the code and enforces security policies, ensuring that only safe operations are allowed. This is a crucial layer of protection for the host system from potential threats posed by executing arbitrary code.


The following code runs FastAPI sandbox server:

```python
# ./main.py
import asyncio
from asyncio import TimeoutError, wait_for
from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, HTTPException
from jupyter_client.manager import AsyncKernelManager
from pydantic import BaseModel

app = FastAPI()

allowed_packages = ["numpy", "pandas", "matplotlib", "scikit-learn"]
installed_packages: List[str] = []

class CodeRequest(BaseModel):
    code: str

class InstallRequest(BaseModel):
    package: str

class ExecutionResult(BaseModel):
    output: str

@asynccontextmanager
async def kernel_client():
    km = AsyncKernelManager(kernel_name="python3")
    await km.start_kernel()
    kc = km.client()
    kc.start_channels()
    await kc.wait_for_ready()
    try:
        yield kc
    finally:
        kc.stop_channels()
        await km.shutdown_kernel()

async def execute_code(code: str) -> str:
    async with kernel_client() as kc:
        msg_id = kc.execute(code)
        try:
            while True:
                reply = await kc.get_iopub_msg()
                if reply["parent_header"]["msg_id"] != msg_id:
                    continue
                msg_type = reply["msg_type"]
                if msg_type == "stream":
                    return reply["content"]["text"]
                elif msg_type == "error":
                    return f"Error executing code: {reply['content']['evalue']}"
                elif msg_type == "status" and reply["content"]["execution_state"] == "idle":
                    break
        except asyncio.CancelledError:
            raise
    return ""

async def install_package(package: str) -> None:
    if package not in installed_packages and package in allowed_packages:
        async with kernel_client() as kc:
            try:
                kc.execute(f"!pip install {package}")
                while True:
                    reply = await kc.get_iopub_msg()
                    if (
                        reply["msg_type"] == "status"
                        and reply["content"]["execution_state"] == "idle"
                    ):
                        break
                installed_packages.append(package)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error installing package: {str(e)}")

@app.post("/install")
async def install(request: InstallRequest):
    try:
        await wait_for(install_package(request.package), timeout=120)
    except TimeoutError:
        raise HTTPException(status_code=400, detail="Package installation timed out")
    return {"message": f"Package '{request.package}' installed successfully."}

@app.post("/execute", response_model=ExecutionResult)
async def execute(request: CodeRequest) -> ExecutionResult:
    try:
        output = await wait_for(execute_code(request.code), timeout=120)
    except TimeoutError:
        raise HTTPException(status_code=400, detail="Code execution timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return ExecutionResult(output=output)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
```

This minimalistic sandbox implementation exposes two endpoints: `/execute` for executing code and `/install` for installing whitelisted packages. Code execution is performed in a separate Jupyter kernel, which is managed by the `AsyncKernelManager`, and the console output text is returned to the client. The server is designed to handle timeouts and exceptions gracefully.

The following Dockerfile builds the container image for the sandbox server:

```dockerfile
# Dockerfile
FROM jupyter/base-notebook

WORKDIR /app
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Switch to jovyan non-root user defined in the base image
USER jovyan

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Although this dockerfile is very simple, it enables deployment of the sandbox solution in a containerized environment. The container runs as a non-root user, which is a good security practice.

At dida we use [**Google Kubernetes Engine**](https://cloud.google.com/kubernetes-engine?hl=en) to manage our **Kubernetes** clusters, which [natively supports](https://cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) gVisor as a container runtime. To enable deployment of gVisor protected workloads, we first need to create a node pool that enables GKE sandbox. Note that in order to turn this security feature on the cluster should have a second standard node pool because GKE-managed system workloads must run separately from untrusted sandboxed workloads.

Once the node pool is created, we can deploy the sandbox container image to the cluster with the following Kubernetes manifest:

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agent-sandbox
  namespace: demos
  labels:
    app: agent-sandbox
spec:
  replicas: 1
  selector:
    matchLabels:
      app: agent-sandbox
  template:
    metadata:
      labels:
        app: agent-sandbox
    spec:
      runtimeClassName: gvisor
      containers:
        - name: agent-sandbox
          image: "${IMAGE_REGISTRY}/${IMAGE_REPOSITORY}:${IMAGE_TAG}"
          ports:
            - name: http
              containerPort: 8000
              protocol: TCP
          resources:
            requests:
              memory: "250Mi"
              cpu: "250m"
            limits:
              memory: "500Mi"
              cpu: "500m"
```

Note that the `runtimeClassName` field is set to `gvisor`, which instructs Kubernetes to use gVisor as the container runtime for this deployment. To control sandbox resource allocation, we set resource requests and limits for CPU and memory. This ensures that the sandbox container has sufficient resources to operate while preventing it from consuming excessive resources that could affect other workloads in the cluster.

### **Capabilities of the Demo Solution**

The demo solution is easy to deploy and manage, making it suitable for various use cases. The interface is accessible via a REST API, which is framework-agnostic and can be integrated with any LLM agent. The solution is designed to be extensible, allowing for the addition of new features and enhancements as needed. For example, one can add support for additional programming languages or integrate with other tools and services. In addition, the solution can be easily scaled to handle increased workloads by deploying multiple instances of the sandbox container in a Kubernetes cluster. Containerization minimizes performance overhead compared to traditional virtual machines, making it suitable for high-performance applications.

While being a proof of concept for code sandbox, the demo showcases the following security features:

- A standalone containerized sandbox provides isolation and minimizes dependencies between agents.

- Python imports are limited, reducing risks associated with dependency threats.

- The following security features are provided by using gVisor as the container runtime:

  - Isolation of the execution environment from the host system.

  - Sandboxing gVisor itself from the host kernel.

  - Running the container with least amount of privileges.

  - Continuous development and maintenance of gVisor by security experts, ensuring up-to-date security features.
- Kubernetes enables efficient CPU, memory, and storage resource management.


### **Limitations of the Demo Solution**

The following limitation of the demo should be addressed before it can be used in production:

- At the moment every request to the sandbox creates a new Jupyter kernel, which is not efficient. This can be improved by reusing existing kernels or implementing a more sophisticated kernel management strategy.

- In addition to managing the lifecycle of Jupyter kernels, the solution should also handle session and state management. This includes authentication, authorization, and maintaining user sessions to ensure secure access to the sandbox environment.

- It might be beneficial to LLM agents to generate responses that include non-textual elements, in particular images. The current solution does not support these types of responses, even though image output is supported by Jupyter.

- Filter sandbox ingress and egress traffic to prevent data exfiltration and unauthorized access to external resources.

## Conclusion

The demo solution includes features like easy deployment, framework-agnostic integration, and scalability through Kubernetes. It effectively isolates execution environments using gVisor, ensuring robust security with minimal performance overhead. However, some limitations need addressing for production use, such as optimizing Jupyter kernel management, enabling authentication and authorization, and enforcing strong network security controls.

By leveraging code sandboxes teams can build advanced LLM solutions with high agency, allowing these applications to autonomously execute tasks while minimizing security risks. As the technology behind LLMs continues to advance, keeping pace with robust and flexible security measures will be essential for utilizing their full potential in innovative and impactful ways.

</details>


## Code Sources

<details>
<summary>Repository analysis for https://github.com/towardsai/course-ai-agents/blob/main/lessons/06_tools/notebook.ipynb</summary>

# Repository analysis for https://github.com/towardsai/course-ai-agents/blob/main/lessons/06_tools/notebook.ipynb

## Summary
Repository: towardsai/course-ai-agents
File: notebook.ipynb
Lines: 1,288

Estimated tokens: 9.7k

## File tree
```Directory structure:
└── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/06_tools/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 6: Tools

This notebook explores **Tools (Function Calling)**, one of the most critical building blocks of any AI Agent. 

We will use the `google-genai` library to interact with Google's Gemini models.

**Learning Objectives:**

1.  **Understand and implement tool use (function calling)** from scratch to allow an LLM to interact with external systems.
2.  **Build a custom tool calling framework** using decorators similar to production frameworks like LangGraph.
3.  **Use Gemini's native tool calling API** for production-ready implementations.
4.  **Implement structured data extraction** using Pydantic models as tools for reliable JSON output.
5.  **Run tools in loops** to handle multi-step tasks and understand the limitations that lead to ReAct patterns.
"""

"""
## 1. Setup

First, let's install the necessary Python libraries using pip.
"""

"""
!pip install -q google-genai pydantic python-dotenv
"""

"""
### Configure Gemini API Key

To use the Gemini API, you need an API key. 

1.  Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Create a file named `.env` in the root of this project.
3.  Add the following line to the `.env` file, replacing `your_api_key_here` with your actual key:
    ```
    GOOGLE_API_KEY="your_api_key_here"
    ```
The code below will load this key from the `.env` file.
"""

%load_ext autoreload
%autoreload 2

from lessons.utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])
# Output:
#   Trying to load environment variables from `/Users/pauliusztin/Documents/01_projects/TAI/course-ai-agents/.env`

#   Environment variables loaded successfully.


"""
### Import Key Packages
"""

import json
from typing import Any

from google import genai
from google.genai import types
from pydantic import BaseModel, Field

from lessons.utils import pretty_print

"""
### Initialize the Gemini Client
"""

client = genai.Client()

"""
### Define Constants

We will use the `gemini-2.5-flash` model, which is fast, cost-effective, and supports advanced features like tool use. We also define a sample financial document that will be used throughout our examples.
"""

MODEL_ID = "gemini-2.5-flash"

DOCUMENT = """
# Q3 2023 Financial Performance Analysis

The Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, 
beating market expectations. These impressive results reflect our successful product strategy 
and strong market positioning.

Our core business segments demonstrated remarkable resilience, with digital services leading 
the growth at 25% year-over-year. The expansion into new markets has proven particularly 
successful, contributing to 30% of the total revenue increase.

Customer acquisition costs decreased by 10% while retention rates improved to 92%, 
marking our best performance to date. These metrics, combined with our healthy cash flow 
position, provide a strong foundation for continued growth into Q4 and beyond.
"""

"""
## 2. Implementing tool calls from scratch

LLMs are trained on text and can't perform actions in the real world on their own. Tools (or Function Calling) are the mechanism we use to bridge this gap. We provide the LLM with a list of available tools, and it can decide which one to use and with what arguments to fulfill a user's request.

The process of calling a tool looks as follows:

1. **You:** Send the LLM a prompt and a list of available tools.
2. **LLM:** Responds with a function_call request, specifying the tool and arguments.
3. **You:** Execute the requested function in your code.
4. **You:** Send the function's output back to the LLM.
5. **LLM:** Uses the tool's output to generate a final, user-facing response.

"""

"""
### Define Mock Tools

Let's create three simple, mocked functions. One simulates searching Google Drive, another simulates sending a Discord message, and the last one simulates summarizing a document. 

The function signature (input parameters and output type) and docstrings are crucial, as the LLM uses them to understand what each tool does.
"""

def search_google_drive(query: str) -> dict:
    """
    Searches for a file on Google Drive and returns its content or a summary.

    Args:
        query (str): The search query to find the file, e.g., 'Q3 earnings report'.

    Returns:
        dict: A dictionary representing the search results, including file names and summaries.
    """

    # In a real scenario, this would interact with the Google Drive API.
    # Here, we mock the response for demonstration.
    return {
        "files": [
            {
                "name": "Q3_Earnings_Report_2024.pdf",
                "id": "file12345",
                "content": DOCUMENT,
            }
        ]
    }


def send_discord_message(channel_id: str, message: str) -> dict:
    """
    Sends a message to a specific Discord channel.

    Args:
        channel_id (str): The ID of the channel to send the message to, e.g., '#finance'.
        message (str): The content of the message to send.

    Returns:
        dict: A dictionary confirming the action, e.g., {"status": "success"}.
    """

    # Mocking a successful API call to Discord.
    return {
        "status": "success",
        "status_code": 200,
        "channel": channel_id,
        "message_preview": f"{message[:50]}...",
    }


def summarize_financial_report(text: str) -> str:
    """
    Summarizes a financial report.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The summary of the text.
    """

    return "The Q3 2023 earnings report shows strong performance across all metrics \
with 20% revenue growth, 15% user engagement increase, 25% digital services growth, and \
improved retention rates of 92%."

"""
Now we need to define the metadata for each function, which will be used as input to the LLM to understand what tool to use and how to call it:
"""

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

send_discord_message_schema = {
    "name": "send_discord_message",
    "description": "Sends a message to a specific Discord channel.",
    "parameters": {
        "type": "object",
        "properties": {
            "channel_id": {
                "type": "string",
                "description": "The ID of the channel to send the message to, e.g., '#finance'.",
            },
            "message": {
                "type": "string",
                "description": "The content of the message to send.",
            },
        },
        "required": ["channel_id", "message"],
    },
}

summarize_financial_report_schema = {
    "name": "summarize_financial_report",
    "description": "Summarizes a financial report.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "The text to summarize.",
            },
        },
        "required": ["text"],
    },
}


"""
Ultimately, we will aggregate all the tools in a single dictionary:
"""

TOOLS = {
    "search_google_drive": {
        "handler": search_google_drive,
        "declaration": search_google_drive_schema,
    },
    "send_discord_message": {
        "handler": send_discord_message,
        "declaration": send_discord_message_schema,
    },
    "summarize_financial_report": {
        "handler": summarize_financial_report,
        "declaration": summarize_financial_report_schema,
    },
}
TOOLS_BY_NAME = {tool_name: tool["handler"] for tool_name, tool in TOOLS.items()}
TOOLS_SCHEMA = [tool["declaration"] for tool in TOOLS.values()]

"""
Let's take a look at them:
"""

for tool_name, tool in TOOLS_BY_NAME.items():
    print(f"Tool name: {tool_name}")
    print(f"Tool handler: {tool}")
    print("-" * 75)
# Output:
#   Tool name: search_google_drive

#   Tool handler: <function search_google_drive at 0x104c7df80>

#   ---------------------------------------------------------------------------

#   Tool name: send_discord_message

#   Tool handler: <function send_discord_message at 0x104c7de40>

#   ---------------------------------------------------------------------------

#   Tool name: summarize_financial_report

#   Tool handler: <function summarize_financial_report at 0x1274f5c60>

#   ---------------------------------------------------------------------------


pretty_print.wrapped(json.dumps(TOOLS_SCHEMA[0], indent=2), title="`search_google_drive` Tool Schema")
# Output:
#   [93m-------------------------------- `search_google_drive` Tool Schema --------------------------------[0m

#     {

#     "name": "search_google_drive",

#     "description": "Searches for a file on Google Drive and returns its content or a summary.",

#     "parameters": {

#       "type": "object",

#       "properties": {

#         "query": {

#           "type": "string",

#           "description": "The search query to find the file, e.g., 'Q3 earnings report'."

#         }

#       },

#       "required": [

#         "query"

#       ]

#     }

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


pretty_print.wrapped(json.dumps(TOOLS_SCHEMA[1], indent=2), title="`send_discord_message` Tool Schema")
# Output:
#   [93m-------------------------------- `send_discord_message` Tool Schema --------------------------------[0m

#     {

#     "name": "send_discord_message",

#     "description": "Sends a message to a specific Discord channel.",

#     "parameters": {

#       "type": "object",

#       "properties": {

#         "channel_id": {

#           "type": "string",

#           "description": "The ID of the channel to send the message to, e.g., '#finance'."

#         },

#         "message": {

#           "type": "string",

#           "description": "The content of the message to send."

#         }

#       },

#       "required": [

#         "channel_id",

#         "message"

#       ]

#     }

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Now, let's see how to call these tools using an LLM. First, we need to define the system prompt:
"""

TOOL_CALLING_SYSTEM_PROMPT = """
You are a helpful AI assistant with access to tools that enable you to take actions and retrieve information to better 
assist users.

## Tool Usage Guidelines

**When to use tools:**
- When you need information that is not in your training data
- When you need to perform actions in external systems and environments
- When you need real-time, dynamic, or user-specific data
- When computational operations are required

**Tool selection:**
- Choose the most appropriate tool based on the user's specific request
- If multiple tools could work, select the one that most directly addresses the need
- Consider the order of operations for multi-step tasks

**Parameter requirements:**
- Provide all required parameters with accurate values
- Use the parameter descriptions to understand expected formats and constraints
- Ensure data types match the tool's requirements (strings, numbers, booleans, arrays)

## Tool Call Format

When you need to use a tool, output ONLY the tool call in this exact format:

```tool_call
{{"name": "tool_name", "args": {{"param1": "value1", "param2": "value2"}}}}
```

**Critical formatting rules:**
- Use double quotes for all JSON strings
- Ensure the JSON is valid and properly escaped
- Include ALL required parameters
- Use correct data types as specified in the tool definition
- Do not include any additional text or explanation in the tool call

## Response Behavior

- If no tools are needed, respond directly to the user with helpful information
- If tools are needed, make the tool call first, then provide context about what you're doing
- After receiving tool results, provide a clear, user-friendly explanation of the outcome
- If a tool call fails, explain the issue and suggest alternatives when possible

## Available Tools

<tool_definitions>
{tools}
</tool_definitions>

Remember: Your goal is to be maximally helpful to the user. Use tools when they add value, but don't use them unnecessarily. Always prioritize accuracy and user experience.
"""


"""
Let's try the prompt with a few examples.
"""

USER_PROMPT = """
Can you help me find the latest quarterly report and share key insights with the team?
"""

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]

response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
)

pretty_print.wrapped(response.text, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     ```tool_call

#   {"name": "search_google_drive", "args": {"query": "latest quarterly report"}}

#   ```

#   [93m----------------------------------------------------------------------------------------------------[0m


USER_PROMPT = """
Please find the Q3 earnings report on Google Drive and send a summary of it to 
the #finance channel on Discord.
"""

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]

response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
)
pretty_print.wrapped(response.text, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     ```tool_call

#   {"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}

#   ```

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
The next step is to parse the LLM response and call the tool using Python.

First, we parse the LLM output to extract the JSON from the response:
"""

def extract_tool_call(response_text: str) -> str:
    """
    Extracts the tool call from the response text.
    """
    return response_text.split("```tool_call")[1].split("```")[0].strip()


tool_call_str = extract_tool_call(response.text)
tool_call_str
# Output:
#   '{"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}'

"""
Next, we parse the stringified JSON to a Python dict:
"""

tool_call = json.loads(tool_call_str)
tool_call
# Output:
#   {'name': 'search_google_drive', 'args': {'query': 'Q3 earnings report'}}

"""
Now, we retrieve the tool handler, which is a Python function:
"""

tool_handler = TOOLS_BY_NAME[tool_call["name"]]
tool_handler
# Output:
#   <function __main__.search_google_drive(query: str) -> dict>

"""
Ultimately, we call the Python function using the arguments generated by the LLM:
"""

tool_result = tool_handler(**tool_call["args"])
pretty_print.wrapped(tool_result, indent=2, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     {

#     "files": [

#       {

#         "name": "Q3_Earnings_Report_2024.pdf",

#         "id": "file12345",

#         "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n"

#       }

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
We can summarize the tool execution in the following function:
"""

def call_tool(response_text: str, tools_by_name: dict) -> Any:
    """
    Call a tool based on the response from the LLM.
    """

    tool_call_str = extract_tool_call(response_text)
    tool_call = json.loads(tool_call_str)
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    tool = tools_by_name[tool_name]

    return tool(**tool_args)

pretty_print.wrapped(
    json.dumps(call_tool(response.text, tools_by_name=TOOLS_BY_NAME), indent=2), title="LLM Tool Call Response"
)
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     {

#     "files": [

#       {

#         "name": "Q3_Earnings_Report_2024.pdf",

#         "id": "file12345",

#         "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n"

#       }

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Usually we want the LLM to interpret the tool output:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=f"Interpret the tool result: {json.dumps(tool_result, indent=2)}",
)
pretty_print.wrapped(response.text, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     The tool result provides the content of a file named `Q3_Earnings_Report_2024.pdf`.

#   

#   This document is a **Q3 2023 Financial Performance Analysis** and details exceptionally strong results, significantly beating market expectations.

#   

#   **Key highlights from the report include:**

#   

#   *   **Revenue Growth:** A 20% increase in revenue.

#   *   **User Engagement:** 15% growth in user engagement.

#   *   **Core Business Performance:** Digital services led growth at 25% year-over-year.

#   *   **Market Expansion Success:** New markets contributed 30% of the total revenue increase.

#   *   **Efficiency & Retention:**

#       *   Customer acquisition costs decreased by 10%.

#       *   Retention rates improved to 92%, marking the best performance to date.

#   *   **Financial Health:** The company maintains a healthy cash flow position.

#   

#   The report attributes these impressive results to a successful product strategy and strong market positioning, indicating a robust foundation for continued growth into Q4 and beyond.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
That's the basic concept of tool calling! We've successfully implemented function calling from scratch.
"""

"""
## 3. Implementing tool calls from scratch using @tool decorators
"""

"""
For a better analogy with what we see in frameworks such as LangGraph or MCP, let's define a `@tool` decorator that automatically computes the schemas defined above based on the function signature and docstring:
"""

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


def tool(description: Optional[str] = None) -> Callable[[Callable], ToolFunction]:
    """
    A decorator that creates a tool schema from a function.

    Args:
        description: Optional override for the function's docstring

    Returns:
        A decorator function that wraps the original function and adds a schema
    """

    def decorator(func: Callable) -> ToolFunction:
        # Get function signature
        sig = signature(func)

        # Create parameters schema
        properties = {}
        required = []

        for param_name, param in sig.parameters.items():
            # Skip self for methods
            if param_name == "self":
                continue

            param_schema = {
                "type": "string",  # Default to string, can be enhanced with type hints
                "description": f"The {param_name} parameter",  # Default description
            }

            # Add to required if parameter has no default value
            if param.default == Parameter.empty:
                required.append(param_name)

            properties[param_name] = param_schema

        # Create the tool schema
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


@tool()
def search_google_drive_example(query: str) -> dict:
    """Search for files in Google Drive."""
    return {"files": ["Q3 earnings report"]}


@tool()
def send_discord_message_example(channel_id: str, message: str) -> dict:
    """Send a message to a Discord channel."""
    return {"message": "Message sent successfully"}


@tool()
def summarize_financial_report_example(text: str) -> str:
    """Summarize the contents of a financial report."""
    return "Financial report summarized successfully"


tools = [
    search_google_drive_example,
    send_discord_message_example,
    summarize_financial_report_example,
]
tools_by_name = {tool.schema["name"]: tool.func for tool in tools}
tools_schema = [tool.schema for tool in tools]

"""
After the function has been decorated, it has been wrapped into a `ToolFunction` object:
"""

type(search_google_drive_example)
# Output:
#   __main__.ToolFunction

"""
Which has the following fields:
"""

pretty_print.wrapped(json.dumps(search_google_drive_example.schema, indent=2), title="Search Google Drive Example")
# Output:
#   [93m----------------------------------- Search Google Drive Example -----------------------------------[0m

#     {

#     "name": "search_google_drive_example",

#     "description": "Search for files in Google Drive.",

#     "parameters": {

#       "type": "object",

#       "properties": {

#         "query": {

#           "type": "string",

#           "description": "The query parameter"

#         }

#       },

#       "required": [

#         "query"

#       ]

#     }

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
...and the actual function handler:
"""

search_google_drive_example.func
# Output:
#   <function __main__.search_google_drive_example(query: str) -> dict>

"""
Let's see how this new method works with LLMs:
"""

USER_PROMPT = """
Please find the Q3 earnings report on Google Drive and send a summary of it to 
the #finance channel on Discord.
"""

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(tools_schema)), USER_PROMPT]

response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
)
pretty_print.wrapped(response.text, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     ```tool_call

#   {"name": "search_google_drive_example", "args": {"query": "Q3 earnings report"}}

#   ```

#   [93m----------------------------------------------------------------------------------------------------[0m


pretty_print.wrapped(
    json.dumps(call_tool(response.text, tools_by_name=tools_by_name), indent=2), title="LLM Tool Call Response"
)
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     {

#     "files": [

#       "Q3 earnings report"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Voilà! We have our little tool calling framework.
"""

"""
## 4. Implementing tool calls with Gemini's Native API

In production, most of the time, we don't implement tool calling from scratch, but instead leverage the native interface of a specific API such as Gemini or OpenAI. So, let's see how we can use Gemini's built-in tool calling capabilities instead of our custom implementation.
"""

tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(**search_google_drive_schema),
            types.FunctionDeclaration(**send_discord_message_schema),
        ]
    )
]
config = types.GenerateContentConfig(
    tools=tools,
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
)


pretty_print.wrapped(USER_PROMPT, title="User Prompt")
response = client.models.generate_content(
    model=MODEL_ID,
    contents=USER_PROMPT,
    config=config,
)
# Output:
#   [93m------------------------------------------- User Prompt -------------------------------------------[0m

#     

#   Please find the Q3 earnings report on Google Drive and send a summary of it to 

#   the #finance channel on Discord.

#   

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
As you can see, here we don't explictly define a system prompt that guides the LLM how to use the tools. Instead we pass the tools schema to the LLM provider which will handle them internally. This is more efficient, as they take care of optimizing tool/function calling for every specific model.
"""

response_message_part = response.candidates[0].content.parts[0]
function_call = response_message_part.function_call
function_call
# Output:
#   FunctionCall(id=None, args={'query': 'Q3 earnings report'}, name='search_google_drive')

tool_handler = TOOLS_BY_NAME[function_call.name]
tool_handler
# Output:
#   <function __main__.search_google_drive(query: str) -> dict>

tool_handler(**function_call.args)
# Output:
#   {'files': [{'name': 'Q3_Earnings_Report_2024.pdf',

#      'id': 'file12345',

#      'content': '\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n'}]}

"""
Now let's create a simplified function that works with Gemini's native function call objects:
"""

def call_tool(function_call) -> Any:
    tool_name = function_call.name
    tool_args = function_call.args

    tool_handler = TOOLS_BY_NAME[tool_name]

    return tool_handler(**tool_args)

tool_result = call_tool(response_message_part.function_call)
pretty_print.wrapped(tool_result, indent=2, title="Tool Result")
# Output:
#   [93m------------------------------------------- Tool Result -------------------------------------------[0m

#     {

#     "files": [

#       {

#         "name": "Q3_Earnings_Report_2024.pdf",

#         "id": "file12345",

#         "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n"

#       }

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 5. Using a Pydantic Model as a Tool for Structured Outputs

A more elegant and powerful pattern is to treat our Pydantic model *as a tool*. We can ask the model to "call" this Pydantic tool, and the arguments it generates will be our structured data.

This combines the power of function calling with the robustness of Pydantic for structured data extraction. It's the recommended approach for complex data extraction tasks.

Let's define the same Pydantic model as in the structured outputs lesson:
"""

class DocumentMetadata(BaseModel):
    """A class to hold structured metadata for a document."""

    summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
    tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
    keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
    quarter: str = Field(description="The quarter of the financial year described in the document (e.g., Q3 2023).")
    growth_rate: str = Field(description="The growth rate of the company described in the document (e.g., 10%).")

"""
Now, let's see how to use it as a tool:
"""

# The Pydantic class 'DocumentMetadata' is now our 'tool'
extraction_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="extract_metadata",
            description="Extracts structured metadata from a financial document.",
            parameters=DocumentMetadata.model_json_schema(),
        )
    ]
)
config = types.GenerateContentConfig(
    tools=[extraction_tool],
    tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
)

prompt = f"""
Please analyze the following document and extract its metadata.

Document:
--- 
{DOCUMENT}
--- 
"""

response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
response_message_part = response.candidates[0].content.parts[0]

if hasattr(response_message_part, "function_call"):
    function_call = response_message_part.function_call
    pretty_print.function_call(function_call, title="Function Call")

    try:
        document_metadata = DocumentMetadata(**function_call.args)
        pretty_print.wrapped(document_metadata.model_dump_json(indent=2), title="Pydantic Validated Object")
    except Exception as e:
        pretty_print.wrapped(f"Validation failed: {e}", title="Validation Error")
else:
    pretty_print.wrapped("The model did not call the extraction tool.", title="No Function Call")
# Output:
#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `extract_metadata

#     [38;5;208mFunction Arguments:[0m `{

#     "growth_rate": "20%",

#     "summary": "The Q3 2023 earnings report shows a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy and market expansion. This performance provides a strong foundation for continued growth.",

#     "quarter": "Q3 2023",

#     "keywords": [

#       "Revenue",

#       "User Engagement",

#       "Market Expansion",

#       "Customer Acquisition",

#       "Retention Rates",

#       "Digital Services",

#       "Cash Flow"

#     ],

#     "tags": [

#       "Financials",

#       "Earnings",

#       "Growth",

#       "Business Strategy",

#       "Market Analysis"

#     ]

#   }`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------ Pydantic Validated Object ------------------------------------[0m

#     {

#     "summary": "The Q3 2023 earnings report shows a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy and market expansion. This performance provides a strong foundation for continued growth.",

#     "tags": [

#       "Financials",

#       "Earnings",

#       "Growth",

#       "Business Strategy",

#       "Market Analysis"

#     ],

#     "keywords": [

#       "Revenue",

#       "User Engagement",

#       "Market Expansion",

#       "Customer Acquisition",

#       "Retention Rates",

#       "Digital Services",

#       "Cash Flow"

#     ],

#     "quarter": "Q3 2023",

#     "growth_rate": "20%"

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 6. Running Tools in a Loop

Now, let's implement a more sophisticated approach where we put tool calling in a loop with a conversation history. This allows the agent to perform multi-step tasks by calling multiple tools in sequence. Let's create a scenario where we ask the agent to find a report on Google Drive and then communicate its findings on Discord.
"""

tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(**search_google_drive_schema),
            types.FunctionDeclaration(**send_discord_message_schema),
            types.FunctionDeclaration(**summarize_financial_report_schema),
        ]
    )
]
config = types.GenerateContentConfig(
    tools=tools,
    tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
)


USER_PROMPT = """
Please find the Q3 earnings report on Google Drive and send a summary of it to 
the #finance channel on Discord.
"""

messages = [USER_PROMPT]

pretty_print.wrapped(USER_PROMPT, title="User Prompt")
response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
    config=config,
)
response_message_part = response.candidates[0].content.parts[0]
pretty_print.function_call(response_message_part.function_call, title="Function Call")

messages.append(response.candidates[0].content)

# Loop until the model stops requesting function calls or we reach the max number of iterations
max_iterations = 3
while hasattr(response_message_part, "function_call") and max_iterations > 0:
    tool_result = call_tool(response_message_part.function_call)
    pretty_print.wrapped(tool_result, title="Tool Result", indent=2)

    # Add the tool result to the messages creating the following structure:
    # - user prompt
    # - tool call
    # - tool result
    # - tool call
    # - tool result
    # ...
    function_response_part = types.Part.from_function_response(
        name=response_message_part.function_call.name,
        response={"result": tool_result},
    )
    messages.append(function_response_part)

    # Ask the LLM to continue with the next step (which may involve calling another tool)
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
        config=config,
    )

    response_message_part = response.candidates[0].content.parts[0]
    pretty_print.function_call(response_message_part.function_call, only_name=True, title="Function Call")

    messages.append(response.candidates[0].content)

    max_iterations -= 1

pretty_print.wrapped(response.candidates[0].content, title="Final Agent Response")

# Output:
#   [93m------------------------------------------- User Prompt -------------------------------------------[0m

#     

#   Please find the Q3 earnings report on Google Drive and send a summary of it to 

#   the #finance channel on Discord.

#   

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `search_google_drive

#     [38;5;208mFunction Arguments:[0m `{

#     "query": "Q3 earnings report"

#   }`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------- Tool Result -------------------------------------------[0m

#     {

#     "files": [

#       {

#         "name": "Q3_Earnings_Report_2024.pdf",

#         "id": "file12345",

#         "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n"

#       }

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `summarize_financial_report

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------- Tool Result -------------------------------------------[0m

#     The Q3 2023 earnings report shows strong performance across all metrics with 20% revenue growth, 15% user engagement increase, 25% digital services growth, and improved retention rates of 92%.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `send_discord_message

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------- Tool Result -------------------------------------------[0m

#     {

#     "status": "success",

#     "status_code": 200,

#     "channel": "#finance",

#     "message_preview": "The Q3 2023 earnings report shows strong performan..."

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `send_discord_message

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m--------------------------------------- Final Agent Response ---------------------------------------[0m

#     ('parts', [Part(video_metadata=None, thought=None, inline_data=None, file_data=None, thought_signature=b'\n\xec\x02\x01T\xa8\\\xee?[\xd4\x1f\xc1\x14\x08\xc9\x87\xd6ij-{\xea\xd3\xa9E\xa3\x9eiG\x16\xb41\xad\x90\x92\x01\x17C=\xbc^\x90\x84T\xb3Z\x86\x1d%T\xb4\x10\xe1\x02\xf9\xa3\xcfJ\xc4+\xa1\x0b\xe4\r\xee\xc3e\xc5j\x82W\x8bP\xe55B\xbf\xe5@%\x1c_\xda1hE\x00\xeec\xb2\xc2\x9fGI\xaf\xbe\x06\xf8M\x1fm\xe1\xfd7!]\xe12\x93\x94\xdd\x19B\xba\\\xd1\x0caI\xfbR5\xd4\xa9\xa9\x06x\x86\xd0\x06\x94gq\xf9\xda\x80D\xba\x95\xd0[u\xa9V\x8fb\xf7%\xb0\xc3J\x8d\x1e\x9e\xca\xa6fP\x12\xd2\xe5G\xc7\x08\xd5R\xcdn\xf2YeFQ\x80\xcec\xd7h\x1e\xcb\x1c\xbbW\xfe\xd7\xe8\xe2\xcc\xdc\x06\x8e^\xa5m\xd5\x10Y[\x8b\xa2\x89+\x12\xb54k\x073\xfc\x0f\x9c!\x8f\x83t\xfe\xcb\xb01v\x8f\xa0\xb23c\xa7\x0b\xb7y\xd1?\xb4\xc5\xa0\xef\x01\xdc\xa0\xb7\xd1\r\x87\x9445\xeb\x08\x86\xd66m\xe4\xab)6vN\x99!\x87\x01Q-\x9cL*\x0b\x97\x1a\x0f\xb0v\x16\xb3\xfc2\xe1\x88c\xadj<\xbb^\x1b\'\xbb}\xa8l\x0c%\x83??,|\xc2mB\xb7\x95\xe2GF\xee\xf6\xf2\x95\x03\xbb\xf9\xba\xfe\x0c1J\xf2\x93\x83O\x95."Pl\x87\xa6[\x8c,b\x17,c\xa3\xd0\x19\x893P\xd9\xe8C\x93.o&8\x0f\x0c\x0c\x90e\xdb\xae\x97\xed\x12\x00\xd5\xbcV\xf0\xcf\xea', code_execution_result=None, executable_code=None, function_call=FunctionCall(id=None, args={'channel_id': '#finance', 'message': 'The Q3 2023 earnings report shows strong performance across all metrics with 20% revenue growth, 15% user engagement increase, 25% digital services growth, and improved retention rates of 92%.'}, name='send_discord_message'), function_response=None, text=None)])

#   [93m----------------------------------------------------------------------------------------------------[0m

#     ('role', 'model')

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Running tools in a loop is powerful for multi-step tasks, but this approach has limitations. It assumes the agent should call a tool at each iteration and doesn't provide explicit opportunities for the model to reason about tool outputs before deciding on the next action. The agent immediately moves to the next function call without pausing to think about what it learned or whether it should change strategy.

This limitation leads us to more sophisticated patterns like **ReAct** (Reasoning and Acting), which explicitly interleaves reasoning steps with tool calls, allowing the agent to think through problems more deliberately. We will explore ReAct patterns in the next lesson.
"""

</details>


## YouTube Video Transcripts

<details>
<summary>Could not generate transcription for https://www.youtube.com/watch?v=ApoDzZP8_ck.</summary>

Could not generate transcription for https://www.youtube.com/watch?v=ApoDzZP8_ck.

Full API response:
candidates=[Candidate(content=Content(parts=None, role='model'), citation_metadata=None, finish_message=None, token_count=None, finish_reason=<FinishReason.STOP: 'STOP'>, url_context_metadata=None, avg_logprobs=None, grounding_metadata=None, index=0, logprobs_result=None, safety_ratings=None)] create_time=None response_id=None model_version='gemini-2.5-pro' prompt_feedback=None usage_metadata=GenerateContentResponseUsageMetadata(cache_tokens_details=None, cached_content_token_count=None, candidates_token_count=None, candidates_tokens_details=None, prompt_token_count=437780, prompt_tokens_details=[ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=22), ModalityTokenCount(modality=<MediaModality.VIDEO: 'VIDEO'>, token_count=390292), ModalityTokenCount(modality=<MediaModality.AUDIO: 'AUDIO'>, token_count=47466)], thoughts_token_count=5072, tool_use_prompt_token_count=None, tool_use_prompt_tokens_details=None, total_token_count=442852, traffic_type=None) automatic_function_calling_history=[] parsed=None

</details>

<details>
<summary>So what is tool calling? Tool calling is a powerful technique where you make the LLM context aware of real-time data such as databases or APIs. Typically, you use tool calling via a chat interface. So you would have your client application in one hand, and then the LLM on the other side. From your client application, you would send a set of messages together with a tool definition to the LLM. So you would have your messages here,</summary>

So what is tool calling? Tool calling is a powerful technique where you make the LLM context aware of real-time data such as databases or APIs. Typically, you use tool calling via a chat interface. So you would have your client application in one hand, and then the LLM on the other side. From your client application, you would send a set of messages together with a tool definition to the LLM. So you would have your messages here,

[00:30] together with your list of tools. The LLM will look at both your message and the list of tools, and it's going to recommend a tool you should call. From your client application, you should call this tool and then supply the answer back to the LLM. So this tool response will be interpreted by the LLM. And this will either tell you the next tool to call or it will give you the final answer.

[01:00] In your application, you're responsible for creating the tool definition. So this tool definition includes a couple of things, such as the name of every tool. It also includes a description for the tool. So this is where you can give additional information about how to use the tool or when to use it. And it also includes the input parameters needed to make a tool call. And the tools can be anything. So the tools could be APIs or databases.

[01:30] But it could also be code that you interpret via a code interpreter. So let's look at an example. Assume you want to find the weather in Miami. You might ask the LLM about the temperature in Miami. You also provide a list of tools, and one of these tools is the weather API. The LLM will look at both your question, which is what is the temperature in Miami?

[02:00] And it would also look at the weather API, and then based on the tool definition for the weather API, it's going to tell you how to call the weather tool. So in here, it's going to create a tool that you can use right here on this side where you call the API to collect the weather information. You would then supply the weather information back to the LLM. So let's say it would be 71°. The LLM will look at the tool response and then give the final answer, which might be something in the trend of the weather in Miami is pretty nice, it's 71°.

[02:30] This has some downsides. So when you do traditional tool calling where you have an LLM and a client application, you could see the LLM hallucinate. Sometimes the LLM can also make up incorrect tool calls. That's why I also want to look at embedded tool calling. We just looked at traditional tool calling. With traditional tool calling has its flaws. As I mentioned, the LLM could hallucinate or create incorrect tool calls.

[03:00] That's why you also want to take embedded tool calling into account. With embedded tool calling, you use a library or framework to interact with the LLM and your tool definitions. The library would be somewhere between your application and the large language model. In the library, you would do the tool definition, but you will also execute the tool calls. So let's draw a line between these sections here. So the library will contain your tool definition. It will also contain the tool execution.

[03:30] So when you send a message from your application to the large language model, it will go through the library. So your message could still be what is the temperature in Miami? The library will then append the tool definition and send your message together with the tools to the LLM. So this will be your message plus your list of tools.

[04:00] Instead of sending the tool to call to the application or the user, it will be sent to the library, which will then do the tool execution. And this way the library will provide you with the final answer, which could be it's 71° in Miami. When you use embedded tool calling, the LLM will no longer hallucinate as the library to help you with the tool calling or the embedded tool calling is going to take care of the tool execution and will retry the tool calls in case it's needed. So in this video, we've looked at both traditional tool calling and also embedded tool calling, where especially embedded tool calling will help you to prevent hallucination

[04:30] or help you with the execution of tools which could be APIs, databases or code.

</details>


## Local Files

_No local files found._


## Additional Sources Scraped

<details>
<summary>agentic-design-patterns-part-3-tool-use</summary>

Tool Use, in which an LLM is given functions it can request to call for gathering information, taking action, or manipulating data, is a key design pattern of [AI agentic workflows](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S). You may be familiar with LLM-based systems that can perform a web search or execute code. Indeed, some large, consumer-facing LLMs already incorporate these features. But Tool Use goes well beyond these examples.

If you prompt an online LLM-based chat system, “What is the best coffee maker according to reviewers?”, it might decide to carry out a web search and download one or more web pages to gain context. Early on, LLM developers realized that relying only on a pre-trained transformer to generate output tokens is limiting, and that giving an LLM a tool for web search lets it do much more. With such a tool, an LLM is either fine-tuned or prompted (perhaps with few-shot prompting) to generate a special string like _{tool: web-search, query: "coffee maker reviews"}_ to request calling a search engine. (The exact format of the string depends on the implementation.) A post-processing step then looks for strings like these, calls the web search function with the relevant parameters when it finds one, and passes the result back to the LLM as additional input context for further processing.

Similarly, if you ask, “If I invest $100 at compound 7% interest for 12 years, what do I have at the end?”, rather than trying to generate the answer directly using a transformer network — which is unlikely to result in the right answer — the LLM might use a code execution tool to run a Python command to compute 1 _00 \* (1+0.07)\*\*12_ to get the right answer. The LLM might generate a string like this: _{tool: python-interpreter, code: "100 \* (1+0.07)\*\*12"}_.

But Tool Use in agentic workflows now goes much further. Developers are using functions to search different sources (web, Wikipedia, arXiv, etc.), to interface with productivity tools (send email, read/write calendar entries, etc.), generate or interpret images, and much more. We can prompt an LLM using context that gives detailed descriptions of many functions. These descriptions might include a text description of what the function does plus details of what arguments the function expects. And we’d expect the LLM to automatically choose the right function to call to do a job. Further, systems are being built in which the LLM has access to hundreds of tools. In such settings, there might be too many functions at your disposal to put all of them into the LLM context, so you might use heuristics to pick the most relevant subset to include in the LLM context at the current step of processing. This technique, which is described in the Gorilla paper cited below, is reminiscent of how, if there is too much text to include as context, retrieval augmented generation (RAG) systems offer heuristics for picking a subset of the text to include.

Early in the history of LLMs, before widespread availability of large multimodal models (LMMs)  like LLaVa, GPT-4V, and Gemini, LLMs could not process images directly, so a lot of work on Tool Use was carried out by the computer vision community. At that time, the only way for an LLM-based system to manipulate an image was by calling a function to, say, carry out object recognition or some other function on it. Since then, practices for Tool Use have exploded. GPT-4’s function calling capability, released in the middle of last year, was a significant step toward a general-purpose implementation. Since then, more and more LLMs are being developed to be similarly facile with Tool Use.

If you’re interested in learning more about Tool Use, I recommend:

- “[Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S),” Patil et al. (2023)
- “[MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action](https://arxiv.org/abs/2303.11381?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S),” Yang et al. (2023)
- “[Efficient Tool Use with Chain-of-Abstraction Reasoning](https://arxiv.org/abs/2401.17464?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S),” Gao et al. (2024)

Both Tool Use and Reflection, which I described in last week’s [letter](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S), are design patterns that I can get to work fairly reliably on my applications — both are capabilities well worth learning about. In future letters, I’ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable — albeit very exciting — technologies.

</details>

<details>
<summary>building-ai-agents-from-scratch-part-1-tool-use</summary>

# Building AI Agents from scratch - Part 1: Tool use

### Let's implement AI Agent from scratch without using any framework. Today we implement the tool use capability.

First of all, I want to wish you a joyful and peaceful holiday season in advance!

This is the first article in the series where we will build AI Agents from scratch without using any LLM orchestration frameworks. In this one you will learn:

- What are agents?
- How the Tool usage actually works.
- How to build a decorator wrapper that extracts relevant details from a Python function to be passed to the LLM via system prompt.
- How to think about constructing effective system prompts that can be used for Agents.
- How to build an Agent class that is able to plan and execute actions using provided Tools.

You can find the code examples for this and following projects in GitHub repository here:

[AI Engineer's Handbook](https://github.com/swirl-ai/ai-angineers-handbook)

If something does not work as expected, feel free to DM me or leave a comment, let’s figure it out together!

> “The future of AI is Agentic.”
>
> “Year 2025 will be the year of Agents.”

These are the phrases you hear nowadays left and right. And there is a lot of truth to it. In order to bring the most business value out of LLMs, we are turning to complex agentic flows.

### What is an AI Agent?

In it’s simplest high level definition, an AI agent is an application that uses LLM at the core as it’s reasoning engine to decide on the steps it needs to take to solve for users intent. It is usually depicted similar to the picture bellow and is composed of multiple building blocks:

[https://substackcdn.com/image/fetch/$s_!fVcp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3eb64772-fbb5-4f2d-8120-d473c74fe124_2926x2198.png](https://substackcdn.com/image/fetch/$s_!fVcp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3eb64772-fbb5-4f2d-8120-d473c74fe124_2926x2198.png) AI Agent

- Planning - the capability to plan a sequence of actions that the application needs to perform in order to solve for the provided intent.

- Memory - short-term and long-term memory containing any information that the agent might need to reason about the actions it needs to take. This information is usually passed to LLM via a system prompt as part of the core. You can read more about different types of memories in one of my previous articles:

- Tools - any functions that the application can call to enhance it’s reasoning capabilities. One should not be fooled by the simplicity of this definition as a tool can be literally anything:
  - Simple functions defined in code.
  - VectorDBs and other data stores containing context.
  - Regular Machine Learning model APIs.
  - Other Agents!
  - …

In the following set of articles, I will implement most of the moving parts of an agent from scratch without using any orchestration frameworks. This episode is about Tool use.

If you are using any orchestration frameworks for agentic applications, you might be abstracted away from what using a tool really means. This article will help you understand what providing a tool and using it via an agent involves. I believe that understanding applications from the base building blocks is really important for few reasons:

- Frameworks hide the implementation details of the system prompts used, different approaches might be needed in different use cases.
- You might want to tune the low level details to achieve most optimal performance of the agent.
- Having clarity of how the systems actually work helps build up your systems thinking enabling you to craft advanced applications more efficiently.

### Tool use on a high level.

The basic thing one needs to understand when building agentic applications is that LLMs do not run code, they are only used to produce intent via prompting. Why can ChatGPT browse the internet and return more accurate and recent results? Because ChatGPT IS an agent and there are many non LLM building blocks hidden from us behind the API.

Prompt engineering becomes critical when building agentic applications. More specifically, how you craft the system prompt. Simplified prompt structure looks like the following.

[https://substackcdn.com/image/fetch/$s_!rZHR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F663cac67-4b46-428f-8876-d648f621f0e5_1878x766.png](https://substackcdn.com/image/fetch/$s_!rZHR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F663cac67-4b46-428f-8876-d648f621f0e5_1878x766.png) Prompt Structure

The agent will only perform well if you are able to efficiently provide the system prompt with available tool definitions and expected outputs which are in a form of planned actions or raw answers.

### Implementing the Agent.

In this part, we will create an AI Agent, that is capable of checking currency conversion rates online and performing the conversion if needed to answer the user query.

You can also find the code in a GitHub repository [here](https://github.com/swirl-ai/ai-angineers-handbook/tree/main/building_agents_from_scratch/tool_use).

You can follow the tutorial using the Jupyter notebook [here](https://github.com/swirl-ai/ai-angineers-handbook/blob/main/building_agents_from_scratch/tool_use/notebooks/tool_use.ipynb).

I will also create a Youtube video explaining the process in the following weeks. If you don’t want to miss it, you can subscribe to the Youtube channel [here](https://www.youtube.com/@swirlai).

#### Preparing python functions to be used as tools.

The easiest and most convenient way to provide tools to an agent is through functions, in our project we will be using Python for this.

We do not need to provide the function code itself to the system prompt but we need to extract useful information about it so that LLM can decide if and how the function should be invoked.

We’ll define a dataclass that contains desired information including the function runnable.

```
@dataclass
class Tool:
    name: str
    description: str
    func: Callable[..., str]
    parameters: Dict[str, Dict[str, str]]

    def __call__(self, *args, **kwargs) -> str:
        return self.func(*args, **kwargs)
```

The information we are extracting includes:

- Function name.
- function description (we will extract this from a docstring).
- Function callable so that we can invoke it as part of the agent.
- Parameters that should be used with the function so that the LLM can decide on how to call the function.

Now we will need to extract the above information from the functions we define. One requirement for the functions we will enforce is to have properly formatted docstrings. We will require the following format:

```
"""Description of what the tool does.

Parameters:
    - param1: Description of first parameter
    - param2: Description of second parameter
"""
```

The following function extracts information about parameters - parameter names and descriptions.

```
def parse_docstring_params(docstring: str) -> Dict[str, str]:
    """Extract parameter descriptions from docstring."""
    if not docstring:
        return {}

    params = {}
    lines = docstring.split('\n')
    in_params = False
    current_param = None

    for line in lines:
        line = line.strip()
        if line.startswith('Parameters:'):
            in_params = True
        elif in_params:
            if line.startswith('-') or line.startswith('*'):
                current_param = line.lstrip('- *').split(':')[0].strip()
                params[current_param] = line.lstrip('- *').split(':')[1].strip()
            elif current_param and line:
                params[current_param] += ' ' + line.strip()
            elif not line:
                in_params = False

    return params
```

We will be extracting function parameter types from typehints provided via function definition. The bellow function will help format them.

```
def get_type_description(type_hint: Any) -> str:
    """Get a human-readable description of a type hint."""
    if isinstance(type_hint, _GenericAlias):
        if type_hint._name == 'Literal':
            return f"one of {type_hint.__args__}"
    return type_hint.__name__
```

A very convenient way to turn a function into a tool is to use a decorator. The below code defines a tool decorator that wraps a function if used. It uses either function name for the tool name or a variable provided via decorator.

```
def tool(name: str = None):
    def decorator(func: Callable[..., str]) -> Tool:
        tool_name = name or func.__name__
        description = inspect.getdoc(func) or "No description available"

        type_hints = get_type_hints(func)
        param_docs = parse_docstring_params(description)
        sig = inspect.signature(func)

        params = {}
        for param_name, param in sig.parameters.items():
            params[param_name] = {
                "type": get_type_description(type_hints.get(param_name, Any)),
                "description": param_docs.get(param_name, "No description available")
            }

        return Tool(
            name=tool_name,
            description=description.split('\n\n')[0],
            func=func,
            parameters=params
        )
    return decorator
```

#### Currency exchange tool.

The below creates a tool from a function that takes in the amount of currency to exchange from, the currency code to be converted from and the currency code to convert to. The function searches for the relevant currency exchange rate and performs the calculation of resulting currency amount.

```
@tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Converts currency using latest exchange rates.

    Parameters:
        - amount: Amount to convert
        - from_currency: Source currency code (e.g., USD)
        - to_currency: Target currency code (e.g., EUR)
    """
    try:
        url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        if "rates" not in data:
            return "Error: Could not fetch exchange rates"

        rate = data["rates"].get(to_currency.upper())
        if not rate:
            return f"Error: No rate found for {to_currency}"

        converted = amount * rate
        return f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"

    except Exception as e:
        return f"Error converting currency: {str(e)}"
```

Let’s just run

```
convert_currency
```

It should return something like

```
Tool(name='convert_currency', description='Converts currency using latest exchange rates.', func=<function convert_currency at 0x106d8fa60>, parameters={'amount': {'type': 'float', 'description': 'Amount to convert'}, 'from_currency': {'type': 'str', 'description': 'Source currency code (e.g., USD)'}, 'to_currency': {'type': 'str', 'description': 'Target currency code (e.g., EUR)'}})
```

This is great! We have successfully extracted information we will be providing to the LLM as a tool definition.

#### Crafting the system prompt.

We will be using gpt-4o-mini as our reasoning engine. It is known that GPT model family performs better when the input prompt is formatted as json. So we will do exactly that. Actually, the system prompt is the most important part of our agent, here is the final one we will be using:

```
{
    "role": "AI Assistant",
    "capabilities": [\
        "Using provided tools to help users when necessary",\
        "Responding directly without tools for questions that don't require tool usage",\
        "Planning efficient tool usage sequences"\
    ],
    "instructions": [\
        "Use tools only when they are necessary for the task",\
        "If a query can be answered directly, respond with a simple message instead of using tools",\
        "When tools are needed, plan their usage efficiently to minimize tool calls"\
    ],
    "tools": [\
        {\
            "name": tool.name,\
            "description": tool.description,\
            "parameters": {\
                name: {\
                    "type": info["type"],\
                    "description": info["description"]\
                }\
                for name, info in tool.parameters.items()\
            }\
        }\
        for tool in self.tools.values()\
    ],
    "response_format": {
        "type": "json",
        "schema": {
            "requires_tools": {
                "type": "boolean",
                "description": "whether tools are needed for this query"
            },
            "direct_response": {
                "type": "string",
                "description": "response when no tools are needed",
                "optional": True
            },
            "thought": {
                "type": "string",
                "description": "reasoning about how to solve the task (when tools are needed)",
                "optional": True
            },
            "plan": {
                "type": "array",
                "items": {"type": "string"},
                "description": "steps to solve the task (when tools are needed)",
                "optional": True
            },
            "tool_calls": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "tool": {
                            "type": "string",
                            "description": "name of the tool"
                        },
                        "args": {
                            "type": "object",
                            "description": "parameters for the tool"
                        }
                    }
                },
                "description": "tools to call in sequence (when tools are needed)",
                "optional": True
            }
        },
        "examples": [\
            {\
                "query": "Convert 100 USD to EUR",\
                "response": {\
                    "requires_tools": True,\
                    "thought": "I need to use the currency conversion tool to convert USD to EUR",\
                    "plan": [\
                        "Use convert_currency tool to convert 100 USD to EUR",\
                        "Return the conversion result"\
                    ],\
                    "tool_calls": [\
                        {\
                            "tool": "convert_currency",\
                            "args": {\
                                "amount": 100,\
                                "from_currency": "USD",\
                                "to_currency": "EUR"\
                            }\
                        }\
                    ]\
                }\
            },\
            {\
                "query": "What's 500 Japanese Yen in British Pounds?",\
                "response": {\
                    "requires_tools": True,\
                    "thought": "I need to convert JPY to GBP using the currency converter",\
                    "plan": [\
                        "Use convert_currency tool to convert 500 JPY to GBP",\
                        "Return the conversion result"\
                    ],\
                    "tool_calls": [\
                        {\
                            "tool": "convert_currency",\
                            "args": {\
                                "amount": 500,\
                                "from_currency": "JPY",\
                                "to_currency": "GBP"\
                            }\
                        }\
                    ]\
                }\
            },\
            {\
                "query": "What currency does Japan use?",\
                "response": {\
                    "requires_tools": False,\
                    "direct_response": "Japan uses the Japanese Yen (JPY) as its official currency. This is common knowledge that doesn't require using the currency conversion tool."\
                }\
            }\
        ]
    }
}
```

A lot to unpack, let’s analyse it step by step:

```
"role": "AI Assistant",
"capabilities": [\
    "Using provided tools to help users when necessary",\
    "Responding directly without tools for questions that don't require tool usage",\
    "Planning efficient tool usage sequences"\
],
"instructions": [\
    "Use tools only when they are necessary for the task",\
    "If a query can be answered directly, respond with a simple message instead of using tools",\
    "When tools are needed, plan their usage efficiently to minimize tool calls"\
]
```

This is where we define the qualities of the Agent, in general we are enforcing the behaviour that tools should be used only when necessary.

```
"tools": [\
    {\
        "name": tool.name,\
        "description": tool.description,\
        "parameters": {\
            name: {\
                "type": info["type"],\
                "description": info["description"]\
            }\
            for name, info in tool.parameters.items()\
        }\
    }\
    for tool in self.tools.values()\
]
```

This is where we unpack the tools into a list. The tool list will be part of Agent class, that is why we loop through self.tools. Remember, each tool is defined by the Dataclass we created in the first part.

```
"response_format": {
    "type": "json",
    "schema": {
        "requires_tools": {
            "type": "boolean",
            "description": "whether tools are needed for this query"
        },
        "direct_response": {
            "type": "string",
            "description": "response when no tools are needed",
            "optional": True
        },
        "thought": {
            "type": "string",
            "description": "reasoning about how to solve the task (when tools are needed)",
            "optional": True
        },
        "plan": {
            "type": "array",
            "items": {"type": "string"},
            "description": "steps to solve the task (when tools are needed)",
            "optional": True
        },
        "tool_calls": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "tool": {
                        "type": "string",
                        "description": "name of the tool"
                    },
                    "args": {
                        "type": "object",
                        "description": "parameters for the tool"
                    }
                }
            },
            "description": "tools to call in sequence (when tools are needed)",
            "optional": True
        }
    }
}
```

Above enforces the LLM output schema. We provide strict instructions here:

- requires\_tools: return if tool usage is required.
- direct\_response: if above is false return a direct response.
- thought: description on how the task should be solved.
- plan: steps to solve the task.
- tool\_calls: tool calls in sequence including functions and parameters to be used. Our example only includes one tool, but it does not necessarily have to.

```
"examples": [\
    {\
        "query": "Convert 100 USD to EUR",\
        "response": {\
            "requires_tools": True,\
            "thought": "I need to use the currency conversion tool to convert USD to EUR",\
            "plan": [\
                "Use convert_currency tool to convert 100 USD to EUR",\
                "Return the conversion result"\
            ],\
            "tool_calls": [\
                {\
                    "tool": "convert_currency",\
                    "args": {\
                        "amount": 100,\
                        "from_currency": "USD",\
                        "to_currency": "EUR"\
                    }\
                }\
            ]\
        }\
    },\
    {\
        "query": "What's 500 Japanese Yen in British Pounds?",\
        "response": {\
            "requires_tools": True,\
            "thought": "I need to convert JPY to GBP using the currency converter",\
            "plan": [\
                "Use convert_currency tool to convert 500 JPY to GBP",\
                "Return the conversion result"\
            ],\
            "tool_calls": [\
                {\
                    "tool": "convert_currency",\
                    "args": {\
                        "amount": 500,\
                        "from_currency": "JPY",\
                        "to_currency": "GBP"\
                    }\
                }\
            ]\
        }\
    },\
    {\
        "query": "What currency does Japan use?",\
        "response": {\
            "requires_tools": False,\
            "direct_response": "Japan uses the Japanese Yen (JPY) as its official currency. This is common knowledge that doesn't require using the currency conversion tool."\
        }\
    }\
]
```

Finally, we provide some examples of correct reasoning above.

#### Implementing the Agent Class

The agent class is quite lengthy due to the long system prompt:

```
class Agent:
    def __init__(self):
        """Initialize Agent with empty tool registry."""
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.tools: Dict[str, Tool] = {}

    def add_tool(self, tool: Tool) -> None:
        """Register a new tool with the agent."""
        self.tools[tool.name] = tool

    def get_available_tools(self) -> List[str]:
        """Get list of available tool descriptions."""
        return [f"{tool.name}: {tool.description}" for tool in self.tools.values()]

    def use_tool(self, tool_name: str, **kwargs: Any) -> str:
        """Execute a specific tool with given arguments."""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found. Available tools: {list(self.tools.keys())}")

        tool = self.tools[tool_name]
        return tool.func(**kwargs)

    def create_system_prompt(self) -> str:
        """Create the system prompt for the LLM with available tools."""
        tools_json = {
            "role": "AI Assistant",
            "capabilities": [\
                "Using provided tools to help users when necessary",\
                "Responding directly without tools for questions that don't require tool usage",\
                "Planning efficient tool usage sequences"\
            ],
            "instructions": [\
                "Use tools only when they are necessary for the task",\
                "If a query can be answered directly, respond with a simple message instead of using tools",\
                "When tools are needed, plan their usage efficiently to minimize tool calls"\
            ],
            "tools": [\
                {\
                    "name": tool.name,\
                    "description": tool.description,\
                    "parameters": {\
                        name: {\
                            "type": info["type"],\
                            "description": info["description"]\
                        }\
                        for name, info in tool.parameters.items()\
                    }\
                }\
                for tool in self.tools.values()\
            ],
            "response_format": {
                "type": "json",
                "schema": {
                    "requires_tools": {
                        "type": "boolean",
                        "description": "whether tools are needed for this query"
                    },
                    "direct_response": {
                        "type": "string",
                        "description": "response when no tools are needed",
                        "optional": True
                    },
                    "thought": {
                        "type": "string",
                        "description": "reasoning about how to solve the task (when tools are needed)",
                        "optional": True
                    },
                    "plan": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "steps to solve the task (when tools are needed)",
                        "optional": True
                    },
                    "tool_calls": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "tool": {
                                    "type": "string",
                                    "description": "name of the tool"
                                },
                                "args": {
                                    "type": "object",
                                    "description": "parameters for the tool"
                                }
                            }
                        },
                        "description": "tools to call in sequence (when tools are needed)",
                        "optional": True
                    }
                },
                "examples": [\
                    {\
                        "query": "Convert 100 USD to EUR",\
                        "response": {\
                            "requires_tools": True,\
                            "thought": "I need to use the currency conversion tool to convert USD to EUR",\
                            "plan": [\
                                "Use convert_currency tool to convert 100 USD to EUR",\
                                "Return the conversion result"\
                            ],\
                            "tool_calls": [\
                                {\
                                    "tool": "convert_currency",\
                                    "args": {\
                                        "amount": 100,\
                                        "from_currency": "USD",\
                                        "to_currency": "EUR"\
                                    }\
                                }\
                            ]\
                        }\
                    },\
                    {\
                        "query": "What's 500 Japanese Yen in British Pounds?",\
                        "response": {\
                            "requires_tools": True,\
                            "thought": "I need to convert JPY to GBP using the currency converter",\
                            "plan": [\
                                "Use convert_currency tool to convert 500 JPY to GBP",\
                                "Return the conversion result"\
                            ],\
                            "tool_calls": [\
                                {\
                                    "tool": "convert_currency",\
                                    "args": {\
                                        "amount": 500,\
                                        "from_currency": "JPY",\
                                        "to_currency": "GBP"\
                                    }\
                                }\
                            ]\
                        }\
                    },\
                    {\
                        "query": "What currency does Japan use?",\
                        "response": {\
                            "requires_tools": False,\
                            "direct_response": "Japan uses the Japanese Yen (JPY) as its official currency. This is common knowledge that doesn't require using the currency conversion tool."\
                        }\
                    }\
                ]
            }
        }

        return f"""You are an AI assistant that helps users by providing direct answers or using tools when necessary.
Configuration, instructions, and available tools are provided in JSON format below:

{json.dumps(tools_json, indent=2)}

Always respond with a JSON object following the response_format schema above.
Remember to use tools only when they are actually needed for the task."""

    def plan(self, user_query: str) -> Dict:
        """Use LLM to create a plan for tool usage."""
        messages = [\
            {"role": "system", "content": self.create_system_prompt()},\
            {"role": "user", "content": user_query}\
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0
        )

        try:
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            raise ValueError("Failed to parse LLM response as JSON")

    def execute(self, user_query: str) -> str:
        """Execute the full pipeline: plan and execute tools."""
        try:
            plan = self.plan(user_query)

            if not plan.get("requires_tools", True):
                return plan["direct_response"]

            # Execute each tool in sequence
            results = []
            for tool_call in plan["tool_calls"]:
                tool_name = tool_call["tool"]
                tool_args = tool_call["args"]
                result = self.use_tool(tool_name, **tool_args)
                results.append(result)

            # Combine results
            return f"""Thought: {plan['thought']}
Plan: {'. '.join(plan['plan'])}
Results: {'. '.join(results)}"""

        except Exception as e:
            return f"Error executing plan: {str(e)}"
```

Let’s look into it step by step (skipping the create\_system\_prompt method as we already analysed it in the previous part).

```
def add_tool(self, tool: Tool) -> None:
    """Register a new tool with the agent."""
    self.tools[tool.name] = tool

def get_available_tools(self) -> List[str]:
    """Get list of available tool descriptions."""
    return [f"{tool.name}: {tool.description}" for tool in self.tools.values()]

def use_tool(self, tool_name: str, **kwargs: Any) -> str:
    """Execute a specific tool with given arguments."""
    if tool_name not in self.tools:
        raise ValueError(f"Tool '{tool_name}' not found. Available tools: {list(self.tools.keys())}")

    tool = self.tools[tool_name]
    return tool.func(**kwargs)
```

Above contain methods to manage tools:

- Attaching tools to the agent.
- List attached tools.
- Invoke execution of a tool.

```
def plan(self, user_query: str) -> Dict:
    """Use LLM to create a plan for tool usage."""
    messages = [\
        {"role": "system", "content": self.create_system_prompt()},\
        {"role": "user", "content": user_query}\
    ]

    response = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )

    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        raise ValueError("Failed to parse LLM response as JSON")
```

The above simply executes the system prompt, we defined the expected output as part of the system prompt. It exactly provides the actions that the LLM planned or a direct answer if the tool calling is not needed.

```
def execute(self, user_query: str) -> str:
    """Execute the full pipeline: plan and execute tools."""
    try:
        plan = self.plan(user_query)

        if not plan.get("requires_tools", True):
            return plan["direct_response"]

        # Execute each tool in sequence
        results = []
        for tool_call in plan["tool_calls"]:
            tool_name = tool_call["tool"]
            tool_args = tool_call["args"]
            result = self.use_tool(tool_name, **tool_args)
            results.append(result)

        # Combine results
        return f"""Thought: {plan['thought']}
Plan: {'. '.join(plan['plan'])}
Results: {'. '.join(results)}"""

    except Exception as e:
        return f"Error executing plan: {str(e)}"
```

The above executes the plan method and acts on it. You might remember that the plan can include multiple sequential tool executions, that is why we are looping through planned tool calls.

#### Running the Agent.

That’s it, we have all of the necessary code to create and use the Agent. in the following code we initialise the agent, attach a convert\_currency tool to it and loop through two user queries. First one should require the tool use while the second not.

```
agent = Agent()
agent.add_tool(convert_currency)

query_list = ["I am traveling to Japan from Serbia, I have 1500 of local currency, how much of Japanese currency will I be able to get?",\
                "How are you doing?"]

for query in query_list:
    print(f"\nQuery: {query}")
    result = agent.execute(query)
    print(result)
```

The output should be similar to:

```
Query: I am traveling to Japan from Serbia, I have 1500 of local currency, how much of Japanese currency will I be able to get?
Thought: I need to convert 1500 Serbian Dinars (RSD) to Japanese Yen (JPY) using the currency conversion tool.
Plan: Use convert_currency tool to convert 1500 RSD to JPY. Return the conversion result
Results: 1500 RSD = 2087.49 JPY

Query: How are you doing?
I'm just a computer program, so I don't have feelings, but I'm here and ready to help you!
```

As expected! First query uses the tool, while the second does not.

#### That’s it for today, we’ve learned:

- How to wrap python functions to be provided as tools to the Agent.
- How to craft a system prompt that uses the tool definitions in planning the execution.
- How to implement the agent that executes on the plan.

</details>

<details>
<summary>function-calling-openai-api</summary>

# Function calling

Enable models to fetch data and take actions.

**Function calling** provides a powerful and flexible way for OpenAI models to interface with your code or external services. This guide will explain how to connect the models to your own custom code to fetch data or take action.

Get weather

Function calling example with get\_weather function

python

```python
from openai import OpenAI

client = OpenAI()

tools = [{\
    "type": "function",\
    "name": "get_weather",\
    "description": "Get current temperature for a given location.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "location": {\
                "type": "string",\
                "description": "City and country e.g. Bogotá, Colombia"\
            }\
        },\
        "required": [\
            "location"\
        ],\
        "additionalProperties": False\
    }\
}]

response = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "What is the weather like in Paris today?"}],
    tools=tools
)

print(response.output)
```

```javascript
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [{\
    "type": "function",\
    "name": "get_weather",\
    "description": "Get current temperature for a given location.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "location": {\
                "type": "string",\
                "description": "City and country e.g. Bogotá, Colombia"\
            }\
        },\
        "required": [\
            "location"\
        ],\
        "additionalProperties": false\
    }\
}];

const response = await openai.responses.create({
    model: "gpt-4.1",
    input: [{ role: "user", content: "What is the weather like in Paris today?" }],
    tools,
});

console.log(response.output);
```

```bash
curl https://api.openai.com/v1/responses \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
    "model": "gpt-4.1",
    "input": "What is the weather like in Paris today?",
    "tools": [\
        {\
            "type": "function",\
            "name": "get_weather",\
            "description": "Get current temperature for a given location.",\
            "parameters": {\
                "type": "object",\
                "properties": {\
                    "location": {\
                        "type": "string",\
                        "description": "City and country e.g. Bogotá, Colombia"\
                    }\
                },\
                "required": [\
                    "location"\
                ],\
                "additionalProperties": false\
            }\
        }\
    ]
}'
```

Output

```json
[{\
    "type": "function_call",\
    "id": "fc_12345xyz",\
    "call_id": "call_12345xyz",\
    "name": "get_weather",\
    "arguments": "{\"location\":\"Paris, France\"}"\
}]
```

Send email

Function calling example with send\_email function

python

```python
from openai import OpenAI

client = OpenAI()

tools = [{\
    "type": "function",\
    "name": "send_email",\
    "description": "Send an email to a given recipient with a subject and message.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "to": {\
                "type": "string",\
                "description": "The recipient email address."\
            },\
            "subject": {\
                "type": "string",\
                "description": "Email subject line."\
            },\
            "body": {\
                "type": "string",\
                "description": "Body of the email message."\
            }\
        },\
        "required": [\
            "to",\
            "subject",\
            "body"\
        ],\
        "additionalProperties": False\
    }\
}]

response = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "Can you send an email to ilan@example.com and katia@example.com saying hi?"}],
    tools=tools
)

print(response.output)
```

```javascript
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [{\
    "type": "function",\
    "name": "send_email",\
    "description": "Send an email to a given recipient with a subject and message.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "to": {\
                "type": "string",\
                "description": "The recipient email address."\
            },\
            "subject": {\
                "type": "string",\
                "description": "Email subject line."\
            },\
            "body": {\
                "type": "string",\
                "description": "Body of the email message."\
            }\
        },\
        "required": [\
            "to",\
            "subject",\
            "body"\
        ],\
        "additionalProperties": false\
    }\
}];

const response = await openai.responses.create({
    model: "gpt-4.1",
    input: [{ role: "user", content: "Can you send an email to ilan@example.com and katia@example.com saying hi?" }],
    tools,
});

console.log(response.output);
```

```bash
curl https://api.openai.com/v1/responses \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
    "model": "gpt-4.1",
    "input": "Can you send an email to ilan@example.com and katia@example.com saying hi?",
    "tools": [\
        {\
            "type": "function",\
            "name": "send_email",\
            "description": "Send an email to a given recipient with a subject and message.",\
            "parameters": {\
                "type": "object",\
                "properties": {\
                    "to": {\
                        "type": "string",\
                        "description": "The recipient email address."\
                    },\
                    "subject": {\
                        "type": "string",\
                        "description": "Email subject line."\
                    },\
                    "body": {\
                        "type": "string",\
                        "description": "Body of the email message."\
                    }\
                },\
                "required": [\
                    "to",\
                    "subject",\
                    "body"\
                ],\
                "additionalProperties": false\
            }\
        }\
    ]
}'
```

Output

```json
[\
    {\
        "type": "function_call",\
        "id": "fc_12345xyz",\
        "call_id": "call_9876abc",\
        "name": "send_email",\
        "arguments": "{\"to\":\"ilan@example.com\",\"subject\":\"Hello!\",\"body\":\"Just wanted to say hi\"}"\
    },\
    {\
        "type": "function_call",\
        "id": "fc_12345xyz",\
        "call_id": "call_9876abc",\
        "name": "send_email",\
        "arguments": "{\"to\":\"katia@example.com\",\"subject\":\"Hello!\",\"body\":\"Just wanted to say hi\"}"\
    }\
]
```

Search knowledge base

Function calling example with search\_knowledge\_base function

python

```python
from openai import OpenAI

client = OpenAI()

tools = [{\
    "type": "function",\
    "name": "search_knowledge_base",\
    "description": "Query a knowledge base to retrieve relevant info on a topic.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "query": {\
                "type": "string",\
                "description": "The user question or search query."\
            },\
            "options": {\
                "type": "object",\
                "properties": {\
                    "num_results": {\
                        "type": "number",\
                        "description": "Number of top results to return."\
                    },\
                    "domain_filter": {\
                        "type": [\
                            "string",\
                            "null"\
                        ],\
                        "description": "Optional domain to narrow the search (e.g. 'finance', 'medical'). Pass null if not needed."\
                    },\
                    "sort_by": {\
                        "type": [\
                            "string",\
                            "null"\
                        ],\
                        "enum": [\
                            "relevance",\
                            "date",\
                            "popularity",\
                            "alphabetical"\
                        ],\
                        "description": "How to sort results. Pass null if not needed."\
                    }\
                },\
                "required": [\
                    "num_results",\
                    "domain_filter",\
                    "sort_by"\
                ],\
                "additionalProperties": False\
            }\
        },\
        "required": [\
            "query",\
            "options"\
        ],\
        "additionalProperties": False\
    }\
}]

response = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "Can you find information about ChatGPT in the AI knowledge base?"}],
    tools=tools
)

print(response.output)
```

```javascript
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [{\
    "type": "function",\
    "name": "search_knowledge_base",\
    "description": "Query a knowledge base to retrieve relevant info on a topic.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "query": {\
                "type": "string",\
                "description": "The user question or search query."\
            },\
            "options": {\
                "type": "object",\
                "properties": {\
                    "num_results": {\
                        "type": "number",\
                        "description": "Number of top results to return."\
                    },\
                    "domain_filter": {\
                        "type": [\
                            "string",\
                            "null"\
                        ],\
                        "description": "Optional domain to narrow the search (e.g. 'finance', 'medical'). Pass null if not needed."\
                    },\
                    "sort_by": {\
                        "type": [\
                            "string",\
                            "null"\
                        ],\
                        "enum": [\
                            "relevance",\
                            "date",\
                            "popularity",\
                            "alphabetical"\
                        ],\
                        "description": "How to sort results. Pass null if not needed."\
                    }\
                },\
                "required": [\
                    "num_results",\
                    "domain_filter",\
                    "sort_by"\
                ],\
                "additionalProperties": false\
            }\
        },\
        "required": [\
            "query",\
            "options"\
        ],\
        "additionalProperties": false\
    }\
}];

const response = await openai.responses.create({
    model: "gpt-4.1",
    input: [{ role: "user", content: "Can you find information about ChatGPT in the AI knowledge base?" }],
    tools,
});

console.log(response.output);
```

```bash
curl https://api.openai.com/v1/responses \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $OPENAI_API_KEY" \
-d '{
    "model": "gpt-4.1",
    "input": "Can you find information about ChatGPT in the AI knowledge base?",
    "tools": [\
        {\
            "type": "function",\
            "name": "search_knowledge_base",\
            "description": "Query a knowledge base to retrieve relevant info on a topic.",\
            "parameters": {\
                "type": "object",\
                "properties": {\
                    "query": {\
                        "type": "string",\
                        "description": "The user question or search query."\
                    },\
                    "options": {\
                        "type": "object",\
                        "properties": {\
                            "num_results": {\
                                "type": "number",\
                                "description": "Number of top results to return."\
                            },\
                            "domain_filter": {\
                                "type": [\
                                    "string",\
                                    "null"\
                                ],\
                                "description": "Optional domain to narrow the search (e.g. 'finance', 'medical'). Pass null if not needed."\
                            },\
                            "sort_by": {\
                                "type": [\
                                    "string",\
                                    "null"\
                                ],\
                                "enum": [\
                                    "relevance",\
                                    "date",\
                                    "popularity",\
                                    "alphabetical"\
                                ],\
                                "description": "How to sort results. Pass null if not needed."\
                            }\
                        },\
                        "required": [\
                            "num_results",\
                            "domain_filter",\
                            "sort_by"\
                        ],\
                        "additionalProperties": false\
                    }\
                },\
                "required": [\
                    "query",\
                    "options"\
                ],\
                "additionalProperties": false\
            }\
        }\
    ]
}'
```

Output

```json
[{\
    "type": "function_call",\
    "id": "fc_12345xyz",\
    "call_id": "call_4567xyz",\
    "name": "search_knowledge_base",\
    "arguments": "{\"query\":\"What is ChatGPT?\",\"options\":{\"num_results\":3,\"domain_filter\":null,\"sort_by\":\"relevance\"}}"\
}]
```

## Overview

You can give the model access to your own custom code through **function calling**. Based on the system prompt and messages, the model may decide to call these functions — **instead of (or in addition to) generating text or audio**.

You'll then execute the function code, send back the results, and the model will incorporate them into its final response.

Function calling has two primary use cases:

|  |  |
| --- | --- |
| **Fetching Data** | Retrieve up-to-date information to incorporate into the model's response (RAG). Useful for searching knowledge bases and retrieving specific data from APIs (e.g. current weather data). |
| **Taking Action** | Perform actions like submitting a form, calling APIs, modifying application state (UI/frontend or backend), or taking agentic workflow actions (like [handing off](https://cookbook.openai.com/examples/orchestrating_agents) the conversation). |

### Sample function

Let's look at the steps to allow a model to use a real `get_weather` function defined below:

Sample get\_weather function implemented in your codebase

python

```python
import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']
```

```javascript
async function getWeather(latitude, longitude) {
    const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m`);
    const data = await response.json();
    return data.current.temperature_2m;
}
```

Unlike the diagram earlier, this function expects precise `latitude` and `longitude` instead of a general `location` parameter. (However, our models can automatically determine the coordinates for many locations!)

### Function calling steps

**Call model with [functions defined](https://platform.openai.com/docs/guides/function-calling?api-mode=responses#defining-functions)** – along with your system and user messages.

Step 1: Call model with get\_weather tool defined

python

```python
from openai import OpenAI
import json

client = OpenAI()

tools = [{\
    "type": "function",\
    "name": "get_weather",\
    "description": "Get current temperature for provided coordinates in celsius.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "latitude": {"type": "number"},\
            "longitude": {"type": "number"}\
        },\
        "required": ["latitude", "longitude"],\
        "additionalProperties": False\
    },\
    "strict": True\
}]

input_messages = [{"role": "user", "content": "What's the weather like in Paris today?"}]

response = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
)
```

```javascript
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [{\
    type: "function",\
    name: "get_weather",\
    description: "Get current temperature for provided coordinates in celsius.",\
    parameters: {\
        type: "object",\
        properties: {\
            latitude: { type: "number" },\
            longitude: { type: "number" }\
        },\
        required: ["latitude", "longitude"],\
        additionalProperties: false\
    },\
    strict: true\
}];

const input = [\
    {\
        role: "user",\
        content: "What's the weather like in Paris today?"\
    }\
];

const response = await openai.responses.create({
    model: "gpt-4.1",
    input,
    tools,
});
```

**Model decides to call function(s)** – model returns the **name** and **input arguments**.

response.output

```json
[{\
    "type": "function_call",\
    "id": "fc_12345xyz",\
    "call_id": "call_12345xyz",\
    "name": "get_weather",\
    "arguments": "{\"latitude\":48.8566,\"longitude\":2.3522}"\
}]
```

**Execute function code** – parse the model's response and [handle function calls](https://platform.openai.com/docs/guides/function-calling?api-mode=responses#handling-function-calls).

Step 3: Execute get\_weather function

python

```python
tool_call = response.output[0]
args = json.loads(tool_call.arguments)

result = get_weather(args["latitude"], args["longitude"])
```

```javascript
const toolCall = response.output[0];
const args = JSON.parse(toolCall.arguments);

const result = await getWeather(args.latitude, args.longitude);
```

**Supply model with results** – so it can incorporate them into its final response.

Step 4: Supply result and call model again

python

```python
input_messages.append(tool_call)  # append model's function call message
input_messages.append({                               # append result message
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
)
print(response_2.output_text)
```

```javascript
input.push(toolCall); // append model's function call message
input.push({                               // append result message
    type: "function_call_output",
    call_id: toolCall.call_id,
    output: result.toString()
});

const response2 = await openai.responses.create({
    model: "gpt-4.1",
    input,
    tools,
    store: true,
});

console.log(response2.output_text)
```

**Model responds** – incorporating the result in its output.

response\_2.output\_text

```json
"The current temperature in Paris is 14°C (57.2°F)."
```

## Defining functions

Functions can be set in the `tools` parameter of each API request.

A function is defined by its schema, which informs the model what it does and what input arguments it expects. It comprises the following fields:

| Field | Description |
| --- | --- |
| `type` | This should always be `function` |
| `name` | The function's name (e.g. `get_weather`) |
| `description` | Details on when and how to use the function |
| `parameters` | [JSON schema](https://json-schema.org/) defining the function's input arguments |
| `strict` | Whether to enforce strict mode for the function call |

Take a look at this example or generate your own below (or in our [Playground](https://platform.openai.com/playground)).

```json
{
  "type": "function",
  "name": "get_weather",
  "description": "Retrieves current weather for the given location.",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City and country e.g. Bogotá, Colombia"
      },
      "units": {
        "type": "string",
        "enum": [\
          "celsius",\
          "fahrenheit"\
        ],
        "description": "Units the temperature will be returned in."
      }
    },
    "required": [\
      "location",\
      "units"\
    ],
    "additionalProperties": false
  },
  "strict": true
}
```

Because the `parameters` are defined by a [JSON schema](https://json-schema.org/), you can leverage many of its rich features like property types, enums, descriptions, nested objects, and, recursive objects.

### Best practices for defining functions

1. **Write clear and detailed function names, parameter descriptions, and instructions.**
   - **Explicitly describe the purpose of the function and each parameter** (and its format), and what the output represents.
   - **Use the system prompt to describe when (and when not) to use each function.** Generally, tell the model _exactly_ what to do.
   - **Include examples and edge cases**, especially to rectify any recurring failures. ( **Note:** Adding examples may hurt performance for [reasoning models](https://platform.openai.com/docs/guides/reasoning).)
2. **Apply software engineering best practices.**
   - **Make the functions obvious and intuitive**. ( [principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment))
   - **Use enums** and object structure to make invalid states unrepresentable. (e.g. `toggle_light(on: bool, off: bool)` allows for invalid calls)
   - **Pass the intern test.** Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.)
3. **Offload the burden from the model and use code where possible.**
   - **Don't make the model fill arguments you already know.** For example, if you already have an `order_id` based on a previous menu, don't have an `order_id` param – instead, have no params `submit_refund()` and pass the `order_id` with code.
   - **Combine functions that are always called in sequence.** For example, if you always call `mark_location()` after `query_location()`, just move the marking logic into the query function call.
4. **Keep the number of functions small for higher accuracy.**
   - **Evaluate your performance** with different numbers of functions.
   - **Aim for fewer than 20 functions** at any one time, though this is just a soft suggestion.
5. **Leverage OpenAI resources.**
   - **Generate and iterate on function schemas** in the [Playground](https://platform.openai.com/playground).
   - **Consider [fine-tuning](https://platform.openai.com/docs/guides/fine-tuning) to increase function calling accuracy** for large numbers of functions or difficult tasks. ( [cookbook](https://cookbook.openai.com/examples/fine_tuning_for_function_calling))

### Token Usage

Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means functions count against the model's context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions or the length of the descriptions you provide for function parameters.

It is also possible to use [fine-tuning](https://platform.openai.com/docs/guides/fine-tuning#fine-tuning-examples) to reduce the number of tokens used if you have many functions defined in your tools specification.

## Handling function calls

When the model calls a function, you must execute it and return the result. Since model responses can include zero, one, or multiple calls, it is best practice to assume there are several.

The response `output` array contains an entry with the `type` having a value of `function_call`. Each entry with a `call_id` (used later to submit the function result), `name`, and JSON-encoded `arguments`.

Sample response with multiple function calls

```json
[\
    {\
        "id": "fc_12345xyz",\
        "call_id": "call_12345xyz",\
        "type": "function_call",\
        "name": "get_weather",\
        "arguments": "{\"location\":\"Paris, France\"}"\
    },\
    {\
        "id": "fc_67890abc",\
        "call_id": "call_67890abc",\
        "type": "function_call",\
        "name": "get_weather",\
        "arguments": "{\"location\":\"Bogotá, Colombia\"}"\
    },\
    {\
        "id": "fc_99999def",\
        "call_id": "call_99999def",\
        "type": "function_call",\
        "name": "send_email",\
        "arguments": "{\"to\":\"bob@email.com\",\"body\":\"Hi bob\"}"\
    }\
]
```

Execute function calls and append results

python

```python
for tool_call in response.output:
    if tool_call.type != "function_call":
        continue

    name = tool_call.name
    args = json.loads(tool_call.arguments)

    result = call_function(name, args)
    input_messages.append({
        "type": "function_call_output",
        "call_id": tool_call.call_id,
        "output": str(result)
    })
```

```javascript
for (const toolCall of response.output) {
    if (toolCall.type !== "function_call") {
        continue;
    }

    const name = toolCall.name;
    const args = JSON.parse(toolCall.arguments);

    const result = callFunction(name, args);
    input.push({
        type: "function_call_output",
        call_id: toolCall.call_id,
        output: result.toString()
    });
}
```

In the example above, we have a hypothetical `call_function` to route each call. Here’s a possible implementation:

Execute function calls and append results

python

```python
def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)
    if name == "send_email":
        return send_email(**args)
```

```javascript
const callFunction = async (name, args) => {
    if (name === "get_weather") {
        return getWeather(args.latitude, args.longitude);
    }
    if (name === "send_email") {
        return sendEmail(args.to, args.body);
    }
};
```

### Formatting results

A result must be a string, but the format is up to you (JSON, error codes, plain text, etc.). The model will interpret that string as needed.

If your function has no return value (e.g. `send_email`), simply return a string to indicate success or failure. (e.g. `"success"`)

### Incorporating results into response

After appending the results to your `input`, you can send them back to the model to get a final response.

Send results back to model

python

```python
response = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
)
```

```javascript
const response = await openai.responses.create({
    model: "gpt-4.1",
    input,
    tools,
});
```

Final response

```json
"It's about 15°C in Paris, 18°C in Bogotá, and I've sent that email to Bob."
```

## Additional configurations

### Tool choice

By default the model will determine when and how many tools to use. You can force specific behavior with the `tool_choice` parameter.

1. **Auto:** ( _Default_) Call zero, one, or multiple functions. `tool_choice: "auto"`
2. **Required:** Call one or more functions.
`tool_choice: "required"`

3. **Forced Function:** Call exactly one specific function.
`tool_choice: {"type": "function", "name": "get_weather"}`

You can also set `tool_choice` to `"none"` to imitate the behavior of passing no functions.

### Parallel function calling

The model may choose to call multiple functions in a single turn. You can prevent this by setting `parallel_tool_calls` to `false`, which ensures exactly zero or one tool is called.

**Note:** Currently, if you are using a fine tuned model and the model calls multiple functions in one turn then [strict mode](https://platform.openai.com/docs/guides/function-calling?api-mode=responses#strict-mode) will be disabled for those calls.

**Note for `gpt-4.1-nano-2025-04-14`:** This snapshot of `gpt-4.1-nano` can sometimes include multiple tools calls for the same tool if parallel tool calls are enabled. It is recommended to disable this feature when using this nano snapshot.

### Strict mode

Setting `strict` to `true` will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode.

Under the hood, strict mode works by leveraging our [structured outputs](https://platform.openai.com/docs/guides/structured-outputs) feature and therefore introduces a couple requirements:

1. `additionalProperties` must be set to `false` for each object in the `parameters`.
2. All fields in `properties` must be marked as `required`.

You can denote optional fields by adding `null` as a `type` option (see example below).

Strict mode enabled

```json
{
    "type": "function",
    "name": "get_weather",
    "description": "Retrieves current weather for the given location.",
    "strict": true,
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country e.g. Bogotá, Colombia"
            },
            "units": {
                "type": ["string", "null"],
                "enum": ["celsius", "fahrenheit"],
                "description": "Units the temperature will be returned in."
            }
        },
        "required": ["location", "units"],
        "additionalProperties": false
    }
}
```

Strict mode disabled

```json
{
    "type": "function",
    "name": "get_weather",
    "description": "Retrieves current weather for the given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country e.g. Bogotá, Colombia"
            },
            "units": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "Units the temperature will be returned in."
            }
        },
        "required": ["location"],
    }
}
```

All schemas generated in the [playground](https://platform.openai.com/playground) have strict mode enabled.

While we recommend you enable strict mode, it has a few limitations:

1. Some features of JSON schema are not supported. (See [supported schemas](https://platform.openai.com/docs/guides/structured-outputs?context=with_parse#supported-schemas).)

Specifically for fine tuned models:

1. Schemas undergo additional processing on the first request (and are then cached). If your schemas vary from request to request, this may result in higher latencies.
2. Schemas are cached for performance, and are not eligible for [zero data retention](https://platform.openai.com/docs/models#how-we-use-your-data).

## Streaming

Streaming can be used to surface progress by showing which function is called as the model fills its arguments, and even displaying the arguments in real time.

Streaming function calls is very similar to streaming regular responses: you set `stream` to `true` and get different `event` objects.

Streaming function calls

python

```python
from openai import OpenAI

client = OpenAI()

tools = [{\
    "type": "function",\
    "name": "get_weather",\
    "description": "Get current temperature for a given location.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "location": {\
                "type": "string",\
                "description": "City and country e.g. Bogotá, Colombia"\
            }\
        },\
        "required": [\
            "location"\
        ],\
        "additionalProperties": False\
    }\
}]

stream = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "What's the weather like in Paris today?"}],
    tools=tools,
    stream=True
)

for event in stream:
    print(event)
```

```javascript
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [{\
    type: "function",\
    name: "get_weather",\
    description: "Get current temperature for provided coordinates in celsius.",\
    parameters: {\
        type: "object",\
        properties: {\
            latitude: { type: "number" },\
            longitude: { type: "number" }\
        },\
        required: ["latitude", "longitude"],\
        additionalProperties: false\
    },\
    strict: true\
}];

const stream = await openai.responses.create({
    model: "gpt-4.1",
    input: [{ role: "user", content: "What's the weather like in Paris today?" }],
    tools,
    stream: true,
    store: true,
});

for await (const event of stream) {
    console.log(event)
}
```

Output events

```json
{"type":"response.output_item.added","response_id":"resp_1234xyz","output_index":0,"item":{"type":"function_call","id":"fc_1234xyz","call_id":"call_1234xyz","name":"get_weather","arguments":""}}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"{\""}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"location"}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"\":\""}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"Paris"}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":","}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":" France"}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"\"}"}
{"type":"response.function_call_arguments.done","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"arguments":"{\"location\":\"Paris, France\"}"}
{"type":"response.output_item.done","response_id":"resp_1234xyz","output_index":0,"item":{"type":"function_call","id":"fc_1234xyz","call_id":"call_2345abc","name":"get_weather","arguments":"{\"location\":\"Paris, France\"}"}}
```

Instead of aggregating chunks into a single `content` string, however, you're aggregating chunks into an encoded `arguments` JSON object.

When the model calls one or more functions an event of type `response.output_item.added` will be emitted for each function call that contains the following fields:

| Field | Description |
| --- | --- |
| `response_id` | The id of the response that the function call belongs to |
| `output_index` | The index of the output item in the response. This respresents the individual function calls in the response. |
| `item` | The in-progress function call item that includes a `name`, `arguments` and `id` field |

Afterwards you will receive a series of events of type `response.function_call_arguments.delta` which will contain the `delta` of the `arguments` field. These events contain the following fields:

| Field | Description |
| --- | --- |
| `response_id` | The id of the response that the function call belongs to |
| `item_id` | The id of the function call item that the delta belongs to |
| `output_index` | The index of the output item in the response. This respresents the individual function calls in the response. |
| `delta` | The delta of the `arguments` field. |

Below is a code snippet demonstrating how to aggregate the `delta` s into a final `tool_call` object.

Accumulating tool\_call deltas

python

```python
final_tool_calls = {}

for event in stream:
    if event.type === 'response.output_item.added':
        final_tool_calls[event.output_index] = event.item;
    elif event.type === 'response.function_call_arguments.delta':
        index = event.output_index

        if final_tool_calls[index]:
            final_tool_calls[index].arguments += event.delta
```

```javascript
const finalToolCalls = {};

for await (const event of stream) {
    if (event.type === 'response.output_item.added') {
        finalToolCalls[event.output_index] = event.item;
    } else if (event.type === 'response.function_call_arguments.delta') {
        const index = event.output_index;

        if (finalToolCalls[index]) {
            finalToolCalls[index].arguments += event.delta;
        }
    }
}
```

Accumulated final\_tool\_calls\[0\]

```json
{
    "type": "function_call",
    "id": "fc_1234xyz",
    "call_id": "call_2345abc",
    "name": "get_weather",
    "arguments": "{\"location\":\"Paris, France\"}"
}
```

When the model has finished calling the functions an event of type `response.function_call_arguments.done` will be emitted. This event contains the entire function call including the following fields:

| Field | Description |
| --- | --- |
| `response_id` | The id of the response that the function call belongs to |
| `output_index` | The index of the output item in the response. This respresents the individual function calls in the response. |
| `item` | The function call item that includes a `name`, `arguments` and `id` field. |

</details>

<details>
<summary>function-calling-with-the-gemini-api-google-ai-for-developer</summary>

# Function calling with the Gemini API

Function calling lets you connect models to external tools and APIs.
Instead of generating text responses, the model determines when to call specific
functions and provides the necessary parameters to execute real-world actions.
This allows the model to act as a bridge between natural language and real-world
actions and data. Function calling has 3 primary use cases:

- **Augment Knowledge:** Access information from external sources like
databases, APIs, and knowledge bases.
- **Extend Capabilities:** Use external tools to perform computations and
extend the limitations of the model, such as using a calculator or creating
charts.
- **Take Actions:** Interact with external systems using APIs, such as
scheduling appointments, creating invoices, sending emails, or controlling
smart home devices.

Get WeatherSchedule MeetingCreate Chart

## How function calling works

https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png

Function calling involves a structured interaction between your application, the
model, and external functions. Here's a breakdown of the process:

1. **Define Function Declaration:** Define the function declaration in your
application code. Function Declarations describe the function's name,
parameters, and purpose to the model.
2. **Call LLM with function declarations:** Send user prompt along with the
function declaration(s) to the model. It analyzes the request and determines
if a function call would be helpful. If so, it responds with a structured
JSON object.
3. **Execute Function Code (Your Responsibility):** The Model _does not_
execute the function itself. It's your application's responsibility to
process the response and check for Function Call, if

   - **Yes**: Extract the name and args of the function and execute the
     corresponding function in your application.
   - **No:** The model has provided a direct text response to the prompt
     (this flow is less emphasized in the example but is a possible outcome).
4. **Create User friendly response:** If a function was executed, capture the
result and send it back to the model in a subsequent turn of the
conversation. It will use the result to generate a final, user-friendly
response that incorporates the information from the function call.

This process can be repeated over multiple turns, allowing for complex
interactions and workflows. The model also supports calling multiple functions
in a single turn ( [parallel function\
calling](https://ai.google.dev/gemini-api/docs/function-calling#parallel_function_calling)) and in
sequence ( [compositional function\
calling](https://ai.google.dev/gemini-api/docs/function-calling#compositional_function_calling)).

### Step 1: Define a function declaration

Define a function and its declaration within your application code that allows
users to set light values and make an API request. This function could call
external services or APIs.

```
# Define a function that the model can call to control smart lights
set_light_values_declaration = {
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100. Zero is off and 100 is full brightness",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

# This is the actual function that would be called based on the model's suggestion
def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set the brightness and color temperature of a room light. (mock API).

    Args:
        brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
        color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

    Returns:
        A dictionary containing the set brightness and color temperature.
    """
    return {"brightness": brightness, "colorTemperature": color_temp}

```

```
import { Type } from '@google/genai';

// Define a function that the model can call to control smart lights
const setLightValuesFunctionDeclaration = {
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'Light level from 0 to 100. Zero is off and 100 is full brightness',
      },
      color_temp: {
        type: Type.STRING,
        enum: ['daylight', 'cool', 'warm'],
        description: 'Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.',
      },
    },
    required: ['brightness', 'color_temp'],
  },
};

/**

*   Set the brightness and color temperature of a room light. (mock API)
*   @param {number} brightness - Light level from 0 to 100. Zero is off and 100 is full brightness
*   @param {string} color_temp - Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.
*   @return {Object} A dictionary containing the set brightness and color temperature.
*/
function setLightValues(brightness, color_temp) {
  return {
    brightness: brightness,
    colorTemperature: color_temp
  };
}

```

### Step 2: Call the model with function declarations

Once you have defined your function declarations, you can prompt the model to
use them. It analyzes the prompt and function declarations and decides whether
to respond directly or to call a function. If a function is called, the response
object will contain a function call suggestion.

```
from google.genai import types

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[set_light_values_declaration])
config = types.GenerateContentConfig(tools=[tools])

# Define user prompt
contents = [\
    types.Content(\
        role="user", parts=[types.Part(text="Turn the lights down to a romantic level")]\
    )\
]

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=contents
    config=config,
)

print(response.candidates[0].content.parts[0].function_call)

```

```
import { GoogleGenAI } from '@google/genai';

// Generation config with function declaration
const config = {
  tools: [{\
    functionDeclarations: [setLightValuesFunctionDeclaration]\
  }]
};

// Configure the client
const ai = new GoogleGenAI({});

// Define user prompt
const contents = [\
  {\
    role: 'user',\
    parts: [{ text: 'Turn the lights down to a romantic level' }]\
  }\
];

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-2.5-flash',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);

```

The model then returns a `functionCall` object in an OpenAPI compatible
schema specifying how to call one or more of the declared functions in order to
respond to the user's question.

```
id=None args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'

```

```
{
  name: 'set_light_values',
  args: { brightness: 25, color_temp: 'warm' }
}

```

### Step 3: Execute set\_light\_values function code

Extract the function call details from the model's response, parse the arguments
, and execute the `set_light_values` function.

```
# Extract tool call details, it may not be in the first part.
tool_call = response.candidates[0].content.parts[0].function_call

if tool_call.name == "set_light_values":
    result = set_light_values(**tool_call.args)
    print(f"Function execution result: {result}")

```

```
// Extract tool call details
const tool_call = response.functionCalls[0]

let result;
if (tool_call.name === 'set_light_values') {
  result = setLightValues(tool_call.args.brightness, tool_call.args.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}

```

### Step 4: Create user friendly response with function result and call the model again

Finally, send the result of the function execution back to the model so it can
incorporate this information into its final response to the user.

```
# Create a function response part
function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={"result": result},
)

# Append function call and result of the function execution to contents
contents.append(response.candidates[0].content) # Append the content from the model's response.
contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response

final_response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=config,
    contents=contents,
)

print(final_response.text)

```

```
// Create a function response part
const function_response_part = {
  name: tool_call.name,
  response: { result }
}

// Append function call and result of the function execution to contents
contents.push(response.candidates[0].content);
contents.push({ role: 'user', parts: [{ functionResponse: function_response_part }] });

// Get the final response from the model
const final_response = await ai.models.generateContent({
  model: 'gemini-2.5-flash',
  contents: contents,
  config: config
});

console.log(final_response.text);

```

This completes the function calling flow. The model successfully used the
`set_light_values` function to perform the request action of the user.

## Function declarations

When you implement function calling in a prompt, you create a `tools` object,
which contains one or more `function declarations`. You define functions using
JSON, specifically with a [select subset](https://ai.google.dev/api/caching#Schema)
of the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schemaw) format. A
single function declaration can include the following parameters:

- `name` (string): A unique name for the function ( `get_weather_forecast`,
`send_email`). Use descriptive names without spaces or special characters
(use underscores or camelCase).
- `description` (string): A clear and detailed explanation of the function's
purpose and capabilities. This is crucial for the model to understand when
to use the function. Be specific and provide examples if helpful ("Finds
theaters based on location and optionally movie title which is currently
playing in theaters.").
- `parameters` (object): Defines the input parameters the function
expects.

  - `type` (string): Specifies the overall data type, such as `object`.
  - `properties` (object): Lists individual parameters, each with:

    - `type` (string): The data type of the parameter, such as `string`,
      `integer`, `boolean, array`.
    - `description` (string): A description of the parameter's purpose and
      format. Provide examples and constraints ("The city and state,
      e.g., 'San Francisco, CA' or a zip code e.g., '95616'.").
    - `enum` (array, optional): If the parameter values are from a fixed
      set, use "enum" to list the allowed values instead of just describing
      them in the description. This improves accuracy ("enum":
      \["daylight", "cool", "warm"\]).
  - `required` (array): An array of strings listing the parameter names that
    are mandatory for the function to operate.

You can also construct FunctionDeclarations from Python functions directly using
`types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Function calling with thinking

Enabling
["thinking"](https://ai.google.dev/gemini-api/docs/thinking)
can improve function call performance by allowing the model to reason through a
request before suggesting function calls.

However, because the Gemini API is stateless, this reasoning context is lost
between turns, which can reduce the quality of function calls as they require
multiple turn requests.

To preserve this context you can use thought signatures. A thought signature is
an encrypted representation of the model's internal thought process that you
pass back to the model on subsequent turns.

To use thought signatures:

1. Receive the signature: When thinking is enabled, the API response will
include a thought\_signature field containing an encrypted representation of
the model's reasoning.
2. Return the signature: When you send the function's execution result back to
the server, include the thought\_signature you received.

This allows the model to restore its previous thinking context and will likely
result in better function calling performance.

**Receiving signatures from the server**

Signatures are returned in the part after the model's thinking phase, which
typically is a text or function call.

Here are some examples of what thought signatures look like returned in each
type of part, in response to the request "What's the weather in Lake Tahoe?"
using the [Get Weather](https://ai.google.dev/gemini-api/docs/function-calling?example=weather#rest)
example:

```
[{\
  "candidates": [\
    {\
      "content": {\
        "parts": [\
          {\
            "text": "Here's what the weather in Lake Tahoe is today",\
            "thoughtSignature": "ClcBVKhc7ru7KzUI7SrdUoIdAYLm/+i93aHjfIt4xHyAoO/G70tApxnK2ujBhOhC1PrRy1pkQa88fqFvpHNVd1HDjNLO7mkp6/hFwE+SPPEB3fh0hs4oM8MKhgIBVKhc7uIGvrS7i/T4HpfbnYrluFfWNjZ62gewqe4cVdR/Dlh+zbjtYmDD0gPZ+SuBO7vvHQdzsjePRP+2Y5XddX6LEf/cGGgakq8EhVvw/a6IVzUO6XmpHg2Ag1sl8E9+VFH/lC0R0ZuYdFWligtDuYwp5p5q3o59G0TtWeU2MC1y2MJfE9u/KWd313ldka80/X2W/xF2O/4djMp5G2WKcULfve75zeRCy0mc5iS3SB9mTH0cT6x0vtKjeBx50gcg+CQWtJcRuwTVzz54dmvmK9xvnqA8gKGw3DuaM9wfy5hyY7Qg0z3iyyWdP8T/lbjKim8IEQOk7O1vVwP1Ko7oMYH8JgA1CsoBAVSoXO6v4c5RSyd1cn6EIU0pEFQsjW7rYWPuZdOFq/tsGJT9BCfW7KGkPGwlNSq8jTJFvbcJ/DjtndISQYXwiXd2kGa5JfdS2Kh4zOxCxiWtOk+2nCc3+XQk2nonhO+esGJpkDdbbHZSqRgcUtYKq7q28iPFOQvOFyCiZNB7K86Z/6Hnagu2snSlN/BcTMaFGaWpcCClSUo4foRZn3WbNCoM8rcpD7qEJMp4a5baaSxyyeL1ZTGd2HLpFys/oiW6e3oAnhxuIysCwg=="\
          }\
        ],\
        "role": "model"\
      },\
      "index": 0\
    }\
  ],\
  # Remainder of response...\
\
```\
\
```\
[{\
  "candidates": [\
    {\
      "content": {\
        "parts": [\
          {\
            "functionCall": {\
              "name": "getWeather",\
              "args": {\
                "city": "Lake Tahoe"\
              }\
            },\
            "thoughtSignature": "CiwBVKhc7nRyTi3HmggPD9iQiRc261f5jwuMdw3H/itDH0emsb9ZVo3Nwx9p6wpsAVSoXO5i8fDV4jBSBLoaWxB5zUdlGY6aIGp+I0oEnwRRSRQ1LOvrDlojEH8JE8HjiKXALdJrvNPiG+HY3GZEO8pZjEZtc3UoBUh7+SVyjK7Xolu7aRYYeUyzrCapoETWypER1jbrJXnFV23hCosBAVSoXO6oIPNJSmbuEDfGafOhuCSHkpr1yjTp35RXYqmCESzRzWf5+nFXLqncqeFo4ohoxbiYQVpVQbOZF81p8o9zg6xeRE7qMeOv+XN7enXGJ4/s3qNFQpfkSMqRdBITN1VpX7jyfEAjvxBNc7PDfDJZmEPY338ZIY5nFFcmzJSWjVrboFt2sMFv+A=="\
          }\
        ],\
        "role": "model"\
      },\
      "finishReason": "STOP",\
      "index": 0\
    }\
  ],\
  # Remainder of response...\
\
```\
\
You can confirm that you received a signature and see what a signature looks\
like using the following code:\
\
```\
# Step 2: Call the model with function declarations\
# ...Generation config, Configure the client, and Define user prompt (No changes)\
\
# Send request with declarations (using a thinking model)\
response = client.models.generate_content(\
  model="gemini-2.5-flash", config=config, contents=contents)\
\
# See thought signatures\
for part in response.candidates[0].content.parts:\
  if part.thought_signature:\
    print("Thought signature:")\
    print(part.thought_signature)\
\
```\
\
**Returning signatures back to the server**\
\
In order to return signatures back:\
\
- You should return signatures along with their containing parts back to the\
server\
- You shouldn't merge a part with a signature with another part which also\
contains a signature. The signature string is not concatenable\
- You shouldn't merge one part with a signature with another part without a\
signature. This breaks the correct positioning of the thought represented by\
the signature.\
\
The code will remain the same as in [Step 4](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#step-4) of the previous section.\
But in this case (as indicated in the comment below) you will return signatures\
to the model along with the result of the function execution so the model can\
incorporate the thoughts into its final response:\
\
```\
# Step 4: Create user friendly response with function result and call the model again\
# ...Create a function response part (No change)\
\
# Append thought signatures, function call and result of the function execution to contents\
function_call_content = response.candidates[0].content\
# Append the model's function call message, which includes thought signatures\
contents.append(function_call_content)\
contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response\
\
final_response = client.models.generate_content(\
    model="gemini-2.5-flash",\
    config=config,\
    contents=contents,\
)\
\
print(final_response.text)\
\
```\
\
```
// Step 4: Create user friendly response with function result and call the model again
// ...Create a function response part (No change)

// Append thought signatures, function call and result of the function execution to contents
const function_response_content = response.candidates[0].content;
contents.push(function_response_content);
contents.push({ role: 'user', parts: [{ functionResponse: function_response_part }] });

const final_response = await ai.models.generateContent({
  model: 'gemini-2.5-flash',
  contents: contents,
  config: config
});

console.log(final_response.text);

```

The following shows what a request returning a thought signature may look like:

```
[{\
  "contents": [\
    {\
      "role": "user",\
      "parts": [\
        {\
          "text": "what is the weather in Lake Tahoe?"\
        }\
      ]\
    },\
    {\
      "parts": [\
        {\
          "functionCall": {\
            "name": "getWeather",\
            "args": {\
              "city": "Lake Tahoe"\
            }\
          },\
          "thoughtSignature": "CiIBVKhc7oDPpCaXyJKKssjqr4g3JNOSgJ/M2V+1THC1icsWCmwBVKhc7pBABbZ+zR3e9234WnWWS6GFXmf8IVwpnzjd5KYd7vyJbn/4vTorWBGayj/vbd9JPaZQjxdAIXhoE5mX/MDsQ7M9N/b0qJjHm39tYIBvS4sIWkMDHqTJqXGLzhhKtrTkfbV3RbaJEkQKmwEBVKhc7qVUgC3hfTXZLo9R3AJzUUIx50NKvJTb9B+UU+LBqgg7Nck1x5OpjWVS2R+SsveprIuYOruk2Y0H53J2OJF8qsxTdIq2si8DGW2V7WK8xyoJH5kbqd7drIw1jLb44b6lx4SMyB0VaULuTBki4d+Ljjg1tJTwR0IYMKqDLDZt9mheINsi0ZxcNjfpnDydRXdWbcSwzmK/wgqJAQFUqFzuKgNVElxs3cbO+xebr2IwcOro84nKTisi0tTp9bICPC9fTUhn3L+rvQWA+d3J1Za8at2bakrqiRj7BTh+CVO9fWQMAEQAs3ni0Z2hfaYG92tOD26E4IoZwyYEoWbfNudpH1fr5tEkyqnEGtWIh7H+XoZQ2DXeiOa+br7Zk88SrNE+trJMCogBAVSoXO5e9fBLg7hnbkmKsrzNLnQtLsQm1gNzjcjEC7nJYklYPp0KI2uGBE1PkM8XNsfllAfHVn7LzHcHNlbQ9pJ7QZTSIeG42goS971r5wNZwxaXwCTphClQh826eqJWo6A/28TtAVQWLhTx5ekbP7qb4nh1UblESZ1saxDQAEo4OKPbDzx5BgqKAQFUqFzuVyjNm5i0wN8hTDnKjfpDroEpPPTs531iFy9BOX+xDCdGHy8D+osFpaoBq6TFekQQbz4hIoUR1YEcP4zI80/cNimEeb9IcFxZTTxiNrbhbbcv0969DSMWhB+ZEqIz4vuw4GLe/xcUvqhlChQwFdgIbdOQHSHpatn5uDlktnP/bi26nKuXIwo0AVSoXO7US22OUH7d1f4abNPI0IyAvhqkPp12rbtWLx9vkOtojE8IP+xCfYtIFuZIzRNZqA=="\
        }\
      ],\
      "role": "model"\
    },\
    {\
      "role": "user",\
      "parts": [\
        {\
          "functionResponse": {\
            "name": "getWeather",\
            "response": {\
              "response": {\
                "stringValue": "Sunny and hot. 90 degrees Fahrenheit"\
              }\
            }\
          }\
        }\
      ]\
    }\
  ],\
  # Remainder of request...\
\
```

Learn more about limitations and usage of thought signatures, and about thinking
models in general, on the [Thinking](https://ai.google.dev/gemini-api/docs/thinking#signatures) page.

## Parallel function calling

In addition to single turn function calling, you can also call multiple
functions at once. Parallel function calling lets you execute multiple functions
at once and is used when the functions are not dependent on each other. This is
useful in scenarios like gathering data from multiple independent sources, such
as retrieving customer details from different databases or checking inventory
levels across various warehouses or performing multiple actions such as
converting your apartment into a disco.

```
power_disco_ball = {\
    "name": "power_disco_ball",\
    "description": "Powers the spinning disco ball.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "power": {\
                "type": "boolean",\
                "description": "Whether to turn the disco ball on or off.",\
            }\
        },\
        "required": ["power"],\
    },\
}

start_music = {\
    "name": "start_music",\
    "description": "Play some music matching the specified parameters.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "energetic": {\
                "type": "boolean",\
                "description": "Whether the music is energetic or not.",\
            },\
            "loud": {\
                "type": "boolean",\
                "description": "Whether the music is loud or not.",\
            },\
        },\
        "required": ["energetic", "loud"],\
    },\
}

dim_lights = {\
    "name": "dim_lights",\
    "description": "Dim the lights.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "brightness": {\
                "type": "number",\
                "description": "The brightness of the lights, 0.0 is off, 1.0 is full.",\
            }\
        },\
        "required": ["brightness"],\
    },\
}
```

Configure the function calling mode to allow using all of the specified tools.

```
from google import genai
from google.genai import types

# Configure the client and tools
client = genai.Client()
house_tools = [
    types.Tool(function_declarations=[power_disco_ball, start_music, dim_lights])
]
config = types.GenerateContentConfig(
    tools=house_tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(
        function_calling_config=types.FunctionCallingConfig(mode='ANY')
    ),
)

chat = client.chats.create(model="gemini-2.5-flash", config=config)
response = chat.send_message("Turn this place into a party!")

# Print out each of the function calls requested from this single call
print("Example 1: Forced function calling")
for fn in response.function_calls:
    args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    print(f"{fn.name}({args})")

```

Each of the printed results reflects a single function call that the model has
requested. To send the results back, include the responses in the same order as
they were requested.

The Python SDK supports [automatic function calling](https://ai.google.dev/gemini-api/docs/function-calling#automatic_function_calling_python_only),
which automatically converts Python functions to declarations, handles the
function call execution and response cycle for you. Following is an example for
the disco use case.

```
from google import genai
from google.genai import types

# Actual function implementations
def power_disco_ball_impl(power: bool) -> dict:
    """Powers the spinning disco ball.

    Args:
        power: Whether to turn the disco ball on or off.

    Returns:
        A status dictionary indicating the current state.
    """
    return {"status": f"Disco ball powered {'on' if power else 'off'}"}

def start_music_impl(energetic: bool, loud: bool) -> dict:
    """Play some music matching the specified parameters.

    Args:
        energetic: Whether the music is energetic or not.
        loud: Whether the music is loud or not.

    Returns:
        A dictionary containing the music settings.
    """
    music_type = "energetic" if energetic else "chill"
    volume = "loud" if loud else "quiet"
    return {"music_type": music_type, "volume": volume}

def dim_lights_impl(brightness: float) -> dict:
    """Dim the lights.

    Args:
        brightness: The brightness of the lights, 0.0 is off, 1.0 is full.

    Returns:
        A dictionary containing the new brightness setting.
    """
    return {"brightness": brightness}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]
)

# Make the request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!

```

## Compositional function calling

Compositional or sequential function calling allows Gemini to chain multiple
function calls together to fulfill a complex request. For example, to answer
"Get the temperature in my current location", the Gemini API might first invoke
a `get_current_location()` function followed by a `get_weather()` function that
takes the location as a parameter.

The following example demonstrates how to implement compositional function
calling using the Python SDK and automatic function calling.

This example uses the automatic function calling feature of the
`google-genai` Python SDK. The SDK automatically converts the Python
functions to the required schema, executes the function calls when requested
by the model, and sends the results back to the model to complete the task.

```
import os
from google import genai
from google.genai import types

# Example Functions
def get_weather_forecast(location: str) -> dict:
    """Gets the current weather temperature for a given location."""
    print(f"Tool Call: get_weather_forecast(location={location})")
    # TODO: Make API call
    print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
    return {"temperature": 25, "unit": "celsius"}  # Dummy response

def set_thermostat_temperature(temperature: int) -> dict:
    """Sets the thermostat to a desired temperature."""
    print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
    # TODO: Interact with a thermostat API
    print("Tool Response: {'status': 'success'}")
    return {"status": "success"}

# Configure the client and model
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_weather_forecast, set_thermostat_temperature]
)

# Make the request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)

```

**Expected Output**

When you run the code, you will see the SDK orchestrating the function
calls. The model first calls `get_weather_forecast`, receives the
temperature, and then calls `set_thermostat_temperature` with the correct
value based on the logic in the prompt.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.

```

## Function calling modes

The Gemini API lets you control how the model uses the provided tools
(function declarations). Specifically, you can set the mode within
the. `function_calling_config`.

- `AUTO (Default)`: The model decides whether to generate a natural language
response or suggest a function call based on the prompt and context. This is the
most flexible mode and recommended for most scenarios.
- `ANY`: The model is constrained to always predict a function call and
guarantees function schema adherence. If `allowed_function_names` is not
specified, the model can choose from any of the provided function declarations.
If `allowed_function_names` is provided as a list, the model can only choose
from the functions in that list. Use this mode when you require a function
call response to every prompt (if applicable).
- `NONE`: The model is _prohibited_ from making function calls. This is
equivalent to sending a request without any function declarations. Use this to
temporarily disable function calling without removing your tool definitions.

```
from google.genai import types

# Configure function calling mode
tool_config = types.ToolConfig(
    function_calling_config=types.FunctionCallingConfig(
        mode="ANY", allowed_function_names=["get_current_temperature"]
    )
)

# Create the generation config
config = types.GenerateContentConfig(
    tools=[tools],  # not defined here.
    tool_config=tool_config,
)

```

## Automatic function calling (Python only)

When using the Python SDK, you can provide Python functions directly as tools.
The SDK automatically converts the Python function to declarations, handles the
function call execution and the response cycle for you. The Python SDK
then automatically:

1. Detects function call responses from the model.
2. Call the corresponding Python function in your code.
3. Sends the function response back to the model.
4. Returns the model's final text response.

To use this, define your function with type hints and a docstring, and then pass
the function itself (not a JSON declaration) as a tool:

```
from google import genai
from google.genai import types

# Define the function with type hints and docstring
def get_current_temperature(location: str) -> dict:
    """Gets the current temperature for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA

    Returns:
        A dictionary containing the temperature and unit.
    """
    # ... (implementation) ...
    return {"temperature": 25, "unit": "Celsius"}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_current_temperature]
)  # Pass the function itself

# Make the request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text

```

You can disable automatic function calling with:

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)

```

### Automatic function schema declaration

Automatic schema extraction from Python functions doesn't work in all cases. For
example, it doesn't handle cases where you describe the fields of a nested
dictionary-object. The API is able to describe any of the following types:

```
AllowedType = (int | float | bool | str | list['AllowedType'] | dict[str, AllowedType])

```

To see what the inferred schema looks like, you can convert it using
[`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable):

```
def multiply(a: float, b: float):
    """Returns a * b."""
    return a * b

fn_decl = types.FunctionDeclaration.from_callable(callable=multiply, client=client)

# to_json_dict() provides a clean JSON representation.
print(fn_decl.to_json_dict())

```

## Multi-tool use: Combine native tools with function calling

You can enable multiple tools combining native tools with
function calling at the same time. Here's an example that enables two tools,
[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/grounding) and
[code execution](https://ai.google.dev/gemini-api/docs/code-execution), in a request using the
[Live API](https://ai.google.dev/gemini-api/docs/live).

```
# Multiple tasks example - combining lights, code execution, and search
prompt = """
  Hey, I need you to do three things for me.

    1.  Turn on the lights.
    2.  Then compute the largest prime palindrome under 100000.
    3.  Then use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024.

  Thanks!
  """

tools = [
    {'google_search': {}},
    {'code_execution': {}},
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]} # not defined here.
]

# Execute the prompt with specified tools in audio modality
await run(prompt, tools=tools, modality="AUDIO")

```

## Model context protocol (MCP)

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is
an open standard for connecting AI applications with external tools and data.
MCP provides a common protocol for models to access context, such as functions
(tools), data sources (resources), or predefined prompts.

The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and
offering
[automatic tool calling](https://ai.google.dev/gemini-api/docs/function-calling#automatic_function_calling_python_only)
for MCP tools. When the model generates an MCP tool call, the Python and
JavaScript client SDK can automatically execute the MCP tool and send the
response back to the model in a subsequent request, continuing this loop until
no more tool calls are made by the model.

Here, you can find an example of how to use a local MCP server with Gemini and
`mcp` SDK.

Make sure the latest version of the
[`mcp` SDK](https://modelcontextprotocol.io/introduction) is installed on
your platform of choice.

```
pip install mcp

```

```
import os
import asyncio
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google import genai

client = genai.Client()

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="npx",  # Executable
    args=["-y", "@philschmid/weather-mcp"],  # MCP Server
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Prompt to get the weather for the current day in London.
            prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"

            # Initialize the connection between client and server
            await session.initialize()

            # Send request to the model with MCP function declarations
            response = await client.aio.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[session],  # uses the session, will automatically call the tool
                    # Uncomment if you **don't** want the SDK to automatically call the tool
                    # automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                    #     disable=True
                    # ),
                ),
            )
            print(response.text)

# Start the asyncio event loop and run the main function
asyncio.run(run())

```

### Limitations with built-in MCP support

Built-in MCP support is a [experimental](https://ai.google.dev/gemini-api/docs/models#preview)
feature in our SDKs and has the following limitations:

- Only tools are supported, not resources nor prompts
- It is available for the Python and JavaScript/TypeScript SDK.
- Breaking changes might occur in future releases.

Manual integration of MCP servers is always an option if these limit what you're
building.

## Supported models

This section lists models and their function calling capabilities. Experimental
models are not included. You can find a comprehensive capabilities overview on
the [model overview](https://ai.google.dev/gemini-api/docs/models) page.

| Model | Function Calling | Parallel Function Calling | Compositional Function Calling |
| --- | --- | --- | --- |
| Gemini 2.5 Pro | ✔️ | ✔️ | ✔️ |
| Gemini 2.5 Flash | ✔️ | ✔️ | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ | ✔️ | ✔️ |
| Gemini 2.0 Flash | ✔️ | ✔️ | ✔️ |
| Gemini 2.0 Flash-Lite | X | X | X |

## Best practices

- **Function and Parameter Descriptions:** Be extremely clear and specific in
your descriptions. The model relies on these to choose the correct function
and provide appropriate arguments.
- **Naming:** Use descriptive function names (without spaces, periods, or
dashes).
- **Strong Typing:** Use specific types (integer, string, enum) for parameters
to reduce errors. If a parameter has a limited set of valid values, use an
enum.
- **Tool Selection:** While the model can use an arbitrary number of tools,
providing too many can increase the risk of selecting an incorrect or
suboptimal tool. For best results, aim to provide only the relevant tools
for the context or task, ideally keeping the active set to a maximum of
10-20. Consider dynamic tool selection based on conversation context if you
have a large total number of tools.
- **Prompt Engineering:**
  - Provide context: Tell the model its role (e.g., "You are a helpful
    weather assistant.").
  - Give instructions: Specify how and when to use functions (e.g., "Don't
    guess dates; always use a future date for forecasts.").
  - Encourage clarification: Instruct the model to ask clarifying questions
    if needed.
- **Temperature:** Use a low temperature (e.g., 0) for more deterministic and
reliable function calls.
- **Validation:** If a function call has significant consequences (e.g.,
placing an order), validate the call with the user before executing it.
- **Error Handling**: Implement robust error handling in your functions to
gracefully handle unexpected inputs or API failures. Return informative
error messages that the model can use to generate helpful responses to the
user.
- **Security:** Be mindful of security when calling external APIs. Use
appropriate authentication and authorization mechanisms. Avoid exposing
sensitive data in function calls.
- **Token Limits:** Function descriptions and parameters count towards your
input token limit. If you're hitting token limits, consider limiting the
number of functions or the length of the descriptions, break down complex
tasks into smaller, more focused function sets.

## Notes and limitations

- Only a [subset of the OpenAPI\
schema](https://ai.google.dev/api/caching#FunctionDeclaration) is supported.
- Supported parameter types in Python are limited.
- Automatic function calling is a Python SDK feature only.

</details>

<details>
<summary>react-vs-plan-and-execute-a-practical-comparison-of-llm-agen</summary>

When building LLM Agent systems, choosing the right reasoning pattern is crucial. This article provides an in-depth comparison of two mainstream Agent reasoning patterns: ReAct (Reasoning and Acting) and Plan-and-Execute, helping you make informed technical decisions through practical cases.

## Key Takeaways

- **Understanding Two Major Agent Patterns**
  - ReAct's reasoning-action loop mechanism
  - Plan-and-Execute's planning-execution separation strategy
- **LangChain-based Implementation**
  - ReAct pattern code implementation and best practices
  - Plan-and-Execute pattern engineering solutions
- **Performance and Cost Analysis**
  - Quantitative analysis of response time and accuracy
  - Detailed calculation of token consumption and API costs
- **Practical Cases and Applications**
  - Real-world data analysis tasks
  - Optimal pattern selection for different scenarios
- **Systematic Selection Methodology**
  - Scene characteristics and pattern matching guidelines
  - Hybrid strategy implementation recommendations

## 1\. Working Principles of Both Patterns

### 1.1 ReAct Pattern

ReAct (Reasoning and Acting) pattern is an iterative approach that alternates between thinking and acting. Its core workflow includes:

1. **Reasoning**: Analyze current state and objectives
2. **Acting**: Execute specific operations
3. **Observation**: Obtain action results
4. **Iteration**: Continue thinking and acting based on observations

Typical ReAct Prompt Template:

```
REACT_PROMPT = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Question: {input}
Thought: {agent_scratchpad}"""

```

### 1.2 Plan-and-Execute Pattern

Plan-and-Execute pattern adopts a "plan first, execute later" strategy, dividing tasks into two distinct phases:

1. **Planning Phase**:
   - Analyze task objectives
   - Break down into subtasks
   - Develop execution plan
2. **Execution Phase**:
   - Execute subtasks in sequence
   - Process execution results
   - Adjust plan if needed

Typical Plan-and-Execute Prompt Template:

```
PLANNER_PROMPT = """You are a task planning assistant. Given a task, create a detailed plan.

Task: {input}

Create a plan with the following format:
1. First step
2. Second step
...

Plan:"""

EXECUTOR_PROMPT = """You are a task executor. Follow the plan and execute each step using available tools:

{tools}

Plan:
{plan}

Current step: {current_step}
Previous results: {previous_results}

Use the following format:
Thought: think about the current step
Action: the action to take
Action Input: the input for the action"""

```

## 2\. Implementation Comparison

### 2.1 ReAct Implementation with LangChain

```
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

def create_react_agent(tools, llm):
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True
    )

# Usage example
llm = ChatOpenAI(temperature=0)
tools = [\
    Tool(\
        name="Search",\
        func=search_tool,\
        description="Useful for searching information"\
    ),\
    Tool(\
        name="Calculator",\
        func=calculator_tool,\
        description="Useful for doing calculations"\
    )\
]

agent = create_react_agent(tools, llm)
result = agent.run("What is the population of China multiplied by 2?")

```

### 2.2 Plan-and-Execute Implementation with LangChain

```
from langchain.agents import PlanAndExecute
from langchain.chat_models import ChatOpenAI

def create_plan_and_execute_agent(tools, llm):
    return PlanAndExecute(
        planner=create_planner(llm),
        executor=create_executor(llm, tools),
        verbose=True
    )

# Usage example
llm = ChatOpenAI(temperature=0)
agent = create_plan_and_execute_agent(tools, llm)
result = agent.run("What is the population of China multiplied by 2?")

```

## 3\. Performance and Cost Analysis

### 3.1 Performance Comparison

| Metric | ReAct | Plan-and-Execute |
| --- | --- | --- |
| Response Time | Faster | Slower |
| Token Consumption | Medium | Higher |
| Task Completion Accuracy | 85% | 92% |
| Complex Task Handling | Medium | Strong |

### 3.2 Cost Analysis

Using GPT-4 model for complex tasks:

| Cost Item | ReAct | Plan-and-Execute |
| --- | --- | --- |
| Average Token Usage | 2000-3000 | 3000-4500 |
| API Calls | 3-5 times | 5-8 times |
| Cost per Task | $0.06-0.09 | $0.09-0.14 |

## 4\. Case Study: Data Analysis Task

Let's compare both patterns through a practical data analysis task:

Task Objective: Analyze a CSV file, calculate sales statistics, and generate a report.

### 4.1 ReAct Implementation

```
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI

def analyze_with_react():
    agent = create_csv_agent(
        ChatOpenAI(temperature=0),
        'sales_data.csv',
        verbose=True
    )

    return agent.run("""
        1. Calculate the total sales
        2. Find the best performing product
        3. Generate a summary report
    """)

```

### 4.2 Plan-and-Execute Implementation

```
from langchain.agents import PlanAndExecute
from langchain.tools import PythonAstREPLTool

def analyze_with_plan_execute():
    agent = create_plan_and_execute_agent(
        llm=ChatOpenAI(temperature=0),
        tools=[\
            PythonAstREPLTool(),\
            CSVTool('sales_data.csv')\
        ]
    )

    return agent.run("""
        1. Calculate the total sales
        2. Find the best performing product
        3. Generate a summary report
    """)

```

## 5\. Selection Guide and Best Practices

### 5.1 When to Choose ReAct

1. **Simple Direct Tasks**
   - Single clear objective
   - Few steps
   - Quick response needed
2. **Real-time Interactive Scenarios**
   - Customer service dialogues
   - Instant queries
   - Simple calculations
3. **Cost-Sensitive Scenarios**
   - Limited token budget
   - Need to control API calls

### 5.2 When to Choose Plan-and-Execute

1. **Complex Multi-step Tasks**
   - Requires task breakdown
   - Step dependencies
   - Intermediate result validation
2. **High-Accuracy Scenarios**
   - Financial analysis
   - Data processing
   - Report generation
3. **Long-term Planning Tasks**
   - Project planning
   - Research analysis
   - Strategic decisions

### 5.3 Best Practice Recommendations

1. **Hybrid Usage Strategy**
   - Choose patterns based on subtask complexity
   - Combine both patterns in one system
2. **Performance Optimization Tips**
   - Implement caching mechanisms
   - Enable parallel processing
   - Optimize prompt templates
3. **Cost Control Methods**
   - Set token limits
   - Implement task interruption
   - Use result caching

## Conclusion

Both ReAct and Plan-and-Execute have their strengths, and the choice between them should consider task characteristics, performance requirements, and cost constraints. In practical applications, you can flexibly choose or even combine both patterns to achieve optimal results.

</details>

<details>
<summary>scraping-failed</summary>

⚠️ Error scraping https://arxiv.org/pdf/2401.17464v3: Request Timeout: Failed to scrape URL as the request timed out. Request timed out - No additional error details provided.

</details>
