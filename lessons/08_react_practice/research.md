# Research

## Research Results

<details>
<summary>What official Gemini API documentation or blog posts describe how the Python SDK automatically converts a function’s signature and docstring into a tool schema that the model can call?</summary>

### Source [3]: https://googleapis.github.io/python-genai/

Query: What official Gemini API documentation or blog posts describe how the Python SDK automatically converts a function’s signature and docstring into a tool schema that the model can call?

Answer: The official documentation for the Google Gen AI Python SDK describes support for providing response schemas using Pydantic models or explicit JSON schema dictionaries. It shows how developers can define a schema for the expected response by passing a Pydantic model (or a JSON schema) to the `response_schema` parameter in the `GenerateContentConfig`. The documentation includes examples of this approach, but it does not mention or document any feature where the SDK automatically converts a function’s signature and docstring into a tool schema. The schema must be manually specified as a Pydantic model or a dictionary, rather than being inferred from a Python function's definition or docstring.

-----

-----

</details>

<details>
<summary>According to AI-engineering best-practice articles or conference papers, what are the key benefits of forcing an LLM to produce structured JSON (validated with Pydantic) versus free-form text when implementing a “Thought” phase in ReAct agents?</summary>

### Source [6]: https://python.useinstructor.com/blog/2023/09/11/generating-structured-output--json-from-llms/

Query: According to AI-engineering best-practice articles or conference papers, what are the key benefits of forcing an LLM to produce structured JSON (validated with Pydantic) versus free-form text when implementing a “Thought” phase in ReAct agents?

Answer: **Pydantic** validators play a key role in simplifying tasks such as re-asking or self-critique within LLM pipelines. By using Pydantic, developers can define models directly in Python that describe the desired structure for the LLM output. This approach offers several benefits:
- **Simplicity**: Developers can define expected outputs using familiar Python syntax.
- **Validation**: Pydantic ensures that the output strictly adheres to the specified schema, catching errors early and reducing the complexity of handling free-form text.
- **Framework Compatibility**: Since Pydantic is widely adopted across Python frameworks, integrating structured output from LLMs into existing applications becomes straightforward.
- **Reduced Complexity**: Compared to frameworks requiring manual JSON schema management, using Pydantic with LLMs streamlines the process, making it easier to control and validate model interactions.
This approach is particularly valuable for implementing phases like “Thought” in ReAct agents, where predictable and well-structured intermediate reasoning steps are essential for downstream logic and reliable agent behavior[1].

-----

-----

-----

### Source [7]: https://python.langchain.com/docs/how_to/structured_output/

Query: According to AI-engineering best-practice articles or conference papers, what are the key benefits of forcing an LLM to produce structured JSON (validated with Pydantic) versus free-form text when implementing a “Thought” phase in ReAct agents?

Answer: With LangChain, enforcing structured output from an LLM is straightforward: you pass a Pydantic class (or JSON schema) describing the expected output. The key benefits highlighted are:
- **Automatic Parsing and Validation**: The output is validated against the Pydantic class, ensuring fields are present and correctly typed. This eliminates the need for custom parsing of ambiguous free-form text responses.
- **Clear Documentation**: Using JSON schema or Pydantic models makes parameter expectations explicit, which aids both developers and the models in adhering to desired formats.
- **Direct Usability**: The structured response (as a Pydantic object or dictionary) can be directly used in downstream code, improving reliability and reducing the risk of runtime errors due to missing or misformatted fields.
- **Flexibility**: While Pydantic classes offer type safety and integration with Python code, JSON schema allows for more explicit documentation and can be used without Python-specific constructs, enhancing clarity at the cost of verbosity.
These benefits are especially relevant for the “Thought” phase in ReAct agents, where each reasoning step must be interpretable, validated, and easily processed by subsequent logic[2].

-----

-----

-----

### Source [8]: https://pydantic.dev/articles/llm-intro

Query: According to AI-engineering best-practice articles or conference papers, what are the key benefits of forcing an LLM to produce structured JSON (validated with Pydantic) versus free-form text when implementing a “Thought” phase in ReAct agents?

Answer: Pydantic provides a schema-based approach to validating structured outputs from LLMs. The advantages include:
- **Schema Validation**: By defining models with Pydantic, developers can ensure that LLM outputs are automatically checked for compliance with the expected structure and types.
- **Error Handling**: If the model output deviates from the schema (e.g., by including prose, markdown, or misformatted data), Pydantic validation will catch these issues immediately, allowing for robust error handling and retries.
- **Documentation and Code Generation**: The schema not only validates data but also serves as documentation and can generate JSON schemas for interoperability.
- **Reliable Integration**: Structured outputs facilitate reliable and predictable integration points, which is critical for agents performing multi-step reasoning where each phase’s output is fed into the next step.
This approach mitigates the risks and inconsistencies associated with parsing free-form text, resulting in more robust and maintainable agent implementations[3].

-----

-----

-----

### Source [9]: https://humanloop.com/blog/structured-outputs

Query: According to AI-engineering best-practice articles or conference papers, what are the key benefits of forcing an LLM to produce structured JSON (validated with Pydantic) versus free-form text when implementing a “Thought” phase in ReAct agents?

Answer: Structured outputs enforce strict formatting of LLM responses, which has several key benefits:
- **Consistency**: Outputs always follow the predefined structure, reducing ambiguity and simplifying downstream integration.
- **Error Reduction**: Validated responses decrease the likelihood of errors caused by missing or malformed data that are common with free-form text.
- **Type Safety**: By defining and validating against a schema (like JSON), structured outputs can be directly parsed into typed objects, making it easier to use the data in application logic.
- **Integration Readiness**: Structured outputs are easier to integrate into production systems, as they eliminate the need for complex parsing logic and handle edge cases systematically.
For ReAct agents, especially during the “Thought” phase, these benefits ensure that agent reasoning is transparent, reliably structured, and easily auditable, supporting robust orchestration and post-processing[4].

-----

-----

</details>

<details>
<summary>In tutorials or academic courses on agentic AI, why is a mock search tool frequently recommended over real web APIs, and what pedagogical or technical advantages are cited?</summary>

### Source [10]: https://www.datacamp.com/tutorial/agentic-rag-tutorial

Query: In tutorials or academic courses on agentic AI, why is a mock search tool frequently recommended over real web APIs, and what pedagogical or technical advantages are cited?

Answer: In the DataCamp tutorial on agentic Retrieval-Augmented Generation (RAG), a **mock search tool** is frequently recommended for use in educational settings. This approach is cited for several pedagogical and technical reasons:
- **Controlled Environment**: Using a mock search tool allows instructors to create a sandboxed, predictable environment where learners can focus on understanding the architecture and logic of agentic systems without being distracted by the unpredictability or variability of live web data.
- **Repeatability and Reproducibility**: Mock tools ensure that every student receives the same input and context, which is essential for structured learning, debugging, and consistent assessment.
- **Safety and Privacy**: Relying on mock search tools avoids exposing students’ queries or project data to real-world web APIs, mitigating privacy and security concerns.
- **Cost and Accessibility**: Avoiding real APIs eliminates the need for API keys, rate limits, or potential costs associated with commercial search APIs, making the tutorial more accessible to all students and reducing setup complexity.
- **Focus on Core Concepts**: By abstracting away the external dependencies and potential failures of real web searches, learners can better focus on agent orchestration, tool integration, and reasoning logic—core skills in agentic AI development.

The tutorial demonstrates that, once students are comfortable with these fundamentals, they can later integrate real web APIs as an extension or advanced exercise, but early learning benefits from the stability and transparency offered by mock tools.

-----

-----

-----

### Source [11]: https://www.youtube.com/watch?v=aijS9fWB854

Query: In tutorials or academic courses on agentic AI, why is a mock search tool frequently recommended over real web APIs, and what pedagogical or technical advantages are cited?

Answer: In the referenced video, the use of mock or built-in tools (as opposed to direct integration with real web APIs) is highlighted in the context of building agentic AI applications. The advantages discussed include:
- **Ease of Prototyping**: Built-in tools (including mock search tools) enable rapid prototyping and experimentation without the overhead of configuring real API access or handling authentication and error cases associated with live web services.
- **Reduced Technical Barriers**: Beginners can focus on the logic of agent orchestration and tool use without needing to manage the complexities of external API integration, which can be daunting or distracting for those new to agentic AI.
- **Modularity and Flexibility**: Mock tools can be easily swapped or extended, allowing students to iteratively build up their agent’s capabilities in a modular way before “graduating” to more complex, real-world integrations.

This approach is particularly effective in an educational setting where the primary objective is to teach the structure and reasoning of agentic systems, rather than the nuances of every possible external service.

-----

-----

</details>

<details>
<summary>How do developers identify and handle `function_call` objects in Gemini API responses—including extracting the function name, arguments, and managing unknown or malformed calls—when building a ReAct control loop?</summary>

### Source [12]: https://codelabs.developers.google.com/codelabs/gemini-function-calling

Query: How do developers identify and handle `function_call` objects in Gemini API responses—including extracting the function name, arguments, and managing unknown or malformed calls—when building a ReAct control loop?

Answer: Developers interact with the Gemini API by first **defining function declarations** within a tool, specifying what functions Gemini can call and their expected parameters. When the Gemini API determines that a function should be called based on the user’s input, it returns a **Function Call response** containing structured data with the **function name** and its **arguments**.

To handle this in a ReAct control loop:
- **Extract the function name and parameters** directly from the returned structured data.
- Use these to make an API request or call the relevant function in your application logic.
- After executing the function, **return the API response** to Gemini, allowing it to generate a user-facing response or possibly invoke additional functions.

If a function call is unknown or malformed, the handling logic is up to the developer—typically by validating the function name and arguments against the original declarations and gracefully managing errors or fallback behaviors. All **parameter extraction, validation, and error handling** is implemented in the application code, outside the Gemini API or SDK itself.

The developer is responsible for:
- **Identifying function calls** by parsing the response structure.
- **Extracting** and validating the function name and parameters.
- **Managing unknown or malformed calls** with custom error handling, such as logging, returning error messages, or prompting the model for clarification.
- **Continuing the loop** by passing results back to Gemini or handling additional required steps.

This process ensures robust interaction and error resilience in a ReAct-style control loop, as the Gemini function calling feature is designed to be flexible and developer-driven[1].

-----

-----

-----

### Source [13]: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling

Query: How do developers identify and handle `function_call` objects in Gemini API responses—including extracting the function name, arguments, and managing unknown or malformed calls—when building a ReAct control loop?

Answer: To implement function calling using the Gemini API, developers must:
- **Declare functions** using a Tool schema compatible with OpenAPI.
- **Submit a prompt and function declarations** to the Gemini model, which enables Gemini to reference and call these functions when generating responses.

In practice, the response from Gemini will include a **function_call object** specifying:
- The **function name** (matching one of the declared functions).
- The **arguments/parameters** as key-value pairs.

Developers parse this function_call object from the response, extract the **function name and arguments**, and then execute the corresponding logic or external API request. The workflow is:
1. **Parse the Gemini response** for function_call objects.
2. **Validate** the function name against the declared list.
3. **Extract and validate arguments** according to the function schema.
4. **Handle errors or unknown calls** by checking for unexpected function names or malformed parameters and implementing a fallback, such as sending a clarifying prompt or returning an error to the user.

This approach ensures that the application logic maintains control over function execution, input validation, and error management, which is critical for reliability in a ReAct loop[2].

-----

-----

-----

### Source [14]: https://geminibyexample.com/021-tool-use-function-calling/

Query: How do developers identify and handle `function_call` objects in Gemini API responses—including extracting the function name, arguments, and managing unknown or malformed calls—when building a ReAct control loop?

Answer: A Gemini API function calling implementation example follows these steps:
- Define a **function declaration** with a name and parameters (including type, description, and required fields).
- Configure the API client with the function declaration as a tool.

Upon sending a user prompt, the Gemini API response will have a **function_call object** located at, for example, `response.candidates.content.parts.function_call`.

Developers can **identify and extract** function call data as follows:
- Access `function_call.name` for the **function name**.
- Access `function_call.args` for the **arguments**.

Sample code:
```python
function_call = response.candidates[0].content.parts[0].function_call
print(f"Function to call: {function_call.name}")
print(f"Arguments: {function_call.args}")
```

For handling **unknown or malformed function calls**, developers should:
- Check if `function_call` exists in the response.
- Validate that `function_call.name` matches a declared function.
- Confirm that `function_call.args` contains all required parameters and types.
- Implement error handling or fallback logic when the function name is unrecognized or arguments are missing/incorrect.

This structured approach enables robust extraction and management of function calls in a ReAct loop, with validation and error handling fully controlled in the application code[3].

-----

-----

-----

### Source [15]: https://firebase.google.com/docs/ai-logic/function-calling

Query: How do developers identify and handle `function_call` objects in Gemini API responses—including extracting the function name, arguments, and managing unknown or malformed calls—when building a ReAct control loop?

Answer: When using function calling in a multi-turn chat interface with the Gemini API, developers provide a **set of tools (functions)** the model can use. The Gemini model, upon receiving a prompt, may respond with a **function call** that includes the function name and arguments.

To handle function calls in practice, application code should:
- **Detect** when a Gemini response contains a function call.
- **Extract** the function name and arguments from the response object.
- **Validate** that the function name matches one of the declared tools, and that all required arguments are present and well-formed.
- **Handle unknown or malformed calls** by implementing logic to reject, log, or prompt for clarification if the function name is not recognized or the arguments do not meet the schema requirements.

The application is responsible for:
- **Calling the appropriate function** with the extracted arguments, often by querying an external API.
- **Returning the function's response** to Gemini for further processing or user presentation.

This structure, with explicit validation and error handling, is necessary for maintaining robust and predictable ReAct control loops, since Gemini's function calling feature is flexible and leaves error management to the developer[4].

-----

-----

</details>

<details>
<summary>What design patterns (e.g., scratchpads, role-tagged messages) are recommended in agentic-AI literature for maintaining conversation state across multiple Thought-Action-Observation cycles in a ReAct loop?</summary>

### Source [16]: https://outshift.cisco.com/blog/how-agent-oriented-design-patterns-transform-system-development

Query: What design patterns (e.g., scratchpads, role-tagged messages) are recommended in agentic-AI literature for maintaining conversation state across multiple Thought-Action-Observation cycles in a ReAct loop?

Answer: Agentic-AI systems utilize several key design patterns for maintaining conversation state across multiple Thought-Action-Observation (TAO) cycles in a ReAct loop:

- **Persistent State Pattern**: Agents store data in external databases or in-memory data stores to recall information across multiple interactions. This is especially important in multi-turn dialogue systems, where context must be retained over several sessions or conversations. For example, an agent handling router configurations will keep the configuration data in a database, allowing contextual continuity even after long periods between interactions.
- **State Caching Pattern**: For session-limited needs, agents keep data in memory only for the duration of the session. This supports multi-turn discussions within a session, but data is discarded once the session ends, balancing performance and complexity.
- **Failsafe and Fallback Strategies**: Agents implement mechanisms to recover from tool failures or unexpected scenarios, such as switching to backup tools or retrying failed actions, ensuring robust and resilient operation throughout TAO cycles.

These patterns collectively enable agents to maintain and recover state efficiently, which is critical for effective ReAct-style reasoning and tool use over multiple conversational turns.

-----

-----

-----

### Source [17]: https://www.jit.io/resources/devsecops/its-not-magic-its-memory-how-to-architect-short-term-memory-for-agentic-ai

Query: What design patterns (e.g., scratchpads, role-tagged messages) are recommended in agentic-AI literature for maintaining conversation state across multiple Thought-Action-Observation cycles in a ReAct loop?

Answer: Jit.io discusses advanced memory management for agentic AI, highlighting these patterns for maintaining conversation state:

- **Dual Histories Pattern**: The system maintains two separate message histories:
  - A complete internal context, including tools, intermediate steps, and metadata, for LLM processing.
  - A streamlined, user-facing thread with only human and AI messages, ensuring a clean user experience.
  This separation allows for accurate multi-turn reasoning while keeping the frontend clear and concise.
- **Pre-Processing for State Hygiene**: Before each new execution cycle, transient and irrelevant state fields are cleared. This prevents state bloat and the risk of outdated information affecting subsequent tasks.
- **Summarization with Tool-Aware Context**: As message history approaches the LLM’s context window limit, the system summarizes the conversation. LangGraph’s langmem module generates a compact system message capturing key context, and older messages are trimmed. Importantly, the summarization process is "tool-aware," ensuring that necessary tool information is preserved for orchestrator agents, maintaining continuity across TAO cycles even after summarization.

These mechanisms support efficient, accurate, and robust state management in agentic AI workflows involving multiple ReAct cycles.

-----

-----

-----

### Source [18]: https://www.inviul.com/the-blueprint-of-intelligence-design-patterns-in-agentic-ai/

Query: What design patterns (e.g., scratchpads, role-tagged messages) are recommended in agentic-AI literature for maintaining conversation state across multiple Thought-Action-Observation cycles in a ReAct loop?

Answer: Inviul highlights design patterns that directly support maintaining state across TAO cycles:

- **Reflective Loop Pattern**: After each action, the agent reflects, evaluates, and potentially retries or improves upon its previous output. This self-awareness loop is implemented in systems like LangGraph and OpenAI’s function-calling and memory. The agent explicitly tracks results, assesses outcomes, and uses this evolving state for subsequent actions, thus supporting continuous, multi-step reasoning.
- **Graph-Based Planning Pattern**: Inspired by state machines (e.g., LangGraph), this pattern models each state as a task or decision, with transitions representing possible outcomes (including retries, branching, or human intervention). This explicit state representation makes each step and its context visible and trackable, supporting robust planning and execution over long, multi-turn agent workflows.

Both patterns emphasize explicit, structured state tracking and decision-making, which are essential for maintaining coherent context across extended ReAct loops.

-----

-----

-----

### Source [19]: https://research.aimultiple.com/agentic-ai-design-patterns/

Query: What design patterns (e.g., scratchpads, role-tagged messages) are recommended in agentic-AI literature for maintaining conversation state across multiple Thought-Action-Observation cycles in a ReAct loop?

Answer: AIMultiple describes these state-related patterns in agentic AI:

- **Planning Pattern**: Agents decompose large tasks into subtasks, organizing them into logical sequences or branches for parallel execution. This explicit planning structure maintains state by tracking sub-goals, task progress, and dependencies across multiple cycles.
- **Multi-Agent Pattern**: Complex workflows are managed by delegating subtasks to different specialized agents, each maintaining its own state relevant to its assigned responsibility. The overall system tracks state transitions, task assignments, and results aggregation, ensuring that context is preserved as the primary agent coordinates multiple cycles of action and observation.

These patterns enable robust, scalable, and organized state management for agentic-AI systems operating over multiple TAO cycles in ReAct frameworks.

-----

-----

</details>

<details>
<summary>Where does Google’s official Gemini Python SDK documentation (or blog posts) describe that simply passing a Python function to the `tools` config lets Gemini automatically derive the tool’s name, description, and parameter schema from the function’s signature and docstring?</summary>

### Source [20]: https://googleapis.github.io/python-genai/

Query: Where does Google’s official Gemini Python SDK documentation (or blog posts) describe that simply passing a Python function to the `tools` config lets Gemini automatically derive the tool’s name, description, and parameter schema from the function’s signature and docstring?

Answer: The official Google Gen AI Python SDK documentation explains that you can pass a Python function directly to the `tools` configuration when generating content with the Gemini model. The SDK will then perform automatic function calling. In the provided code examples, a function such as `get_current_weather(location: str) -> str` is passed to the `tools` parameter within the `GenerateContentConfig`. The function includes a docstring describing its purpose and parameters.

While the documentation demonstrates how to pass a Python function and notes that "if you also pass a python function as a tool, by default the SDK will perform automatic function calling," it does not explicitly state that the tool’s name, description, and parameter schema are **automatically derived** from the function’s signature and docstring. The examples imply this behavior, as the function is passed without additional schema or metadata, but there is no direct, explicit statement in this documentation section confirming that the function’s signature and docstring are parsed to set the tool’s name, description, or parameter schema.

Relevant example from the documentation:
```python
def get_current_weather(location: str) -> str:
    """Returns the current weather.
    Args:
        location: The city and state, e.g. San Francisco, CA
    """
    return "sunny"

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents="What is the weather like in Boston?",
    config=types.GenerateContentConfig(
        tools=[get_current_weather],
        # other configs omitted for brevity
    ),
)
```
However, the documentation does not include explanatory text confirming that the SDK will extract the **name**, **description**, or **parameter schema** from the function’s Python signature and docstring; it demonstrates usage but leaves the mechanics implied.

-----

-----

</details>

<details>
<summary>What official Gemini API or SDK resources explain how to configure structured (Pydantic/JSON) outputs and use `response.parsed` to obtain validated objects without manual JSON parsing?</summary>

### Source [24]: https://ai.google.dev/gemini-api/docs/structured-output

Query: What official Gemini API or SDK resources explain how to configure structured (Pydantic/JSON) outputs and use `response.parsed` to obtain validated objects without manual JSON parsing?

Answer: The official Gemini API documentation provides direct guidance on configuring structured (Pydantic/JSON) outputs:

- **Configuring JSON Output**: There are two ways to generate JSON using the Gemini API: by configuring a schema on the model or by providing a schema in a text prompt. Using schemas enables structured extraction and standardization of information, such as processing resumes into database-compatible structures.

- **Pydantic Models**: When you use a Pydantic type, the Gemini Python library automatically builds a JSON schema from your model and sends this schema to the API. This allows you to define key names, value types, and nested structures precisely.

- **Supported Types**: The Python library supports schemas based on basic types (`int`, `float`, `bool`, `str`, `list`), unions, dictionaries with homogeneous value types, and user-defined Pydantic models for more complex, nested structures.

- **JSON Schema Support**: Gemini 2.5 supports the direct use of JSON Schema for structured output via the `responseJsonSchema` field, with some limitations (e.g., only available in Gemini 2.5, constraints on recursive references, and `$ref` usage).

- **Output Handling**: The documentation references the use of Pydantic models for both schema definition and result validation, but does not explicitly mention a `.parsed` attribute for output handling. For more detailed usage (such as accessing validated objects via `response.parsed`), the documentation refers users to the Python library documentation for additional examples.

-----

-----

-----

### Source [25]: https://ai.pydantic.dev/output/

Query: What official Gemini API or SDK resources explain how to configure structured (Pydantic/JSON) outputs and use `response.parsed` to obtain validated objects without manual JSON parsing?

Answer: The Pydantic AI documentation describes how structured outputs are handled and validated using Pydantic:

- **Structured Output Modes**: Three output modes are supported—Tool Output, Native Output, and Prompted Output. All modes use Pydantic models to define the JSON schema and validate model responses.

- **Validation and Parsing**: When using structured output, Pydantic validates the data returned by the model according to the schema. If the model output does not match the schema, validation fails and the system may prompt the model to retry.

- **Prompted Output**: When using Prompted Output mode, the output type(s) are wrapped in a `PromptedOutput` marker class, which can customize the expected output and instructions template for the model. This provides flexibility in guiding the model to generate outputs that match the schema.

- **Accessing Validated Outputs**: While this documentation describes structured output and validation, it does not mention a `.parsed` attribute or a response object with such an attribute. The documentation focuses on schema creation, output modes, and validation, not on specific SDK response handling.

-----

-----

-----

### Source [26]: https://www.youtube.com/watch?v=c8DOxMnigWE

Query: What official Gemini API or SDK resources explain how to configure structured (Pydantic/JSON) outputs and use `response.parsed` to obtain validated objects without manual JSON parsing?

Answer: This official video tutorial on using structured output with the Gemini API covers the following relevant points:

- **System Prompts and Pydantic Models**: The tutorial demonstrates how to define structured schemas using Pydantic models and how to pass these schemas into Gemini API requests for structured JSON output.

- **Practical Example**: The video provides a step-by-step demonstration for Python developers, showing how to extract clean, structured JSON responses from Gemini and use them directly in applications such as chatbots or workflow automations.

- **Response Handling**: While the video shows how to process structured output, it does not explicitly mention the use of a `.parsed` attribute or direct access to validated Pydantic objects without manual JSON parsing.

-----

-----

-----

### Source [27]: https://ai.pydantic.dev/api/models/gemini/

Query: What official Gemini API or SDK resources explain how to configure structured (Pydantic/JSON) outputs and use `response.parsed` to obtain validated objects without manual JSON parsing?

Answer: The Pydantic AI models documentation for Gemini describes the implementation of a Gemini integration using the generativelanguage.googleapis.com API:

- **Implementation Details**: The documentation and source code show how the Gemini model is implemented to interact with the Gemini API, including schema handling and request construction.

- **Schema and Validation**: There is an emphasis on using Pydantic models to define schemas and validate outputs. The model uses these schemas to interpret and validate responses from the Gemini API.

- **Response Attributes**: The documentation does not explicitly mention a `response.parsed` attribute or how to access validated objects in a response. It focuses on the mechanics of schema usage and model interaction rather than SDK-specific response properties.

-----

-----

</details>

<details>
<summary>In developer guides or tutorials that integrate Gemini function calling into ReAct loops, how do they detect `function_call` objects, extract names/arguments, and gracefully handle unknown or malformed calls?</summary>

### Source [33]: https://ai.google.dev/gemini-api/docs/function-calling

Query: In developer guides or tutorials that integrate Gemini function calling into ReAct loops, how do they detect `function_call` objects, extract names/arguments, and gracefully handle unknown or malformed calls?

Answer: The official Gemini API documentation describes the end-to-end flow for function calling but does not provide explicit code for detecting `function_call` objects or handling malformed calls. However, it demonstrates the process for extracting the function name and arguments:

- When the Gemini model responds with a function call, the response includes the function name and any arguments as structured data.
- In Python, after executing the function (e.g., based on `tool_call.name` and its arguments), a function response part is created using `types.Part.from_function_response`, which includes the function name and result.
- This response is appended to the conversation history for the model to generate the next step.
- The documentation does not directly mention how to handle unknown or malformed calls, but the flow implies that developers are responsible for validating the existence of the function and the correctness of its arguments before executing external calls. Any exceptions or errors in this process should be handled in the application logic, outside the Gemini API itself.

The process generally involves:
- Extracting the function name (`tool_call.name`) and arguments from the model's response.
- Validating and executing the function in the application code.
- Returning the result (or handling errors) back into the Gemini conversation loop[1].

-----

-----

-----

### Source [34]: https://codelabs.developers.google.com/codelabs/gemini-function-calling

Query: In developer guides or tutorials that integrate Gemini function calling into ReAct loops, how do they detect `function_call` objects, extract names/arguments, and gracefully handle unknown or malformed calls?

Answer: This official Google Codelab offers a clear breakdown of the function calling workflow, including parameter extraction and error handling responsibilities:

- The Gemini API returns a **Function Call response** that contains the name of the function to call and its parameters as structured data.
- **Extraction**: Developers extract the function name and parameters from the response.
- **Execution**: The function (or external API) is called using these extracted values, typically implemented by the developer.
- If the function name is unknown or the parameters are malformed, the codelab implies that the developer's code should validate inputs before making the external call.
- Error handling for unknown or malformed calls is not performed by the Gemini API; instead, it is the developer’s responsibility to check for:
  - Valid function names (matching those registered and declared to the model).
  - Valid and complete parameters (according to function schema).
  - Any errors encountered should be caught in application logic and a suitable response should be passed back to Gemini, either as a function error or by clarifying the issue in the conversation.

The codelab emphasizes that all **API request and response handling**, including error and validation logic, occurs outside the Gemini API, within the application code[2].

-----

-----

</details>

<details>
<summary>Where do Google’s official Gemini SDK docs or engineering blog posts explicitly explain that passing a Python function to the tools parameter auto-generates the tool’s name, description, and parameter schema from its signature and docstring?</summary>

### Source [41]: https://codelabs.developers.google.com/codelabs/gemini-function-calling

Query: Where do Google’s official Gemini SDK docs or engineering blog posts explicitly explain that passing a Python function to the tools parameter auto-generates the tool’s name, description, and parameter schema from its signature and docstring?

Answer: This codelab demonstrates how to use the Gemini Python client library for function calling. It shows that function declarations must be registered explicitly using the `FunctionDeclaration` class, where the **name**, **description**, and **parameters** are manually specified in code. The guide emphasizes the importance of providing detailed information in the function and parameter descriptions, as the generative model uses this metadata for tool selection and parameter filling. However, the codelab does **not** state or imply that simply passing a Python function to the `tools` parameter will auto-generate the tool's name, description, or parameter schema from its signature or docstring. Instead, all metadata is shown as manually specified.

-----

-----

-----

### Source [42]: https://googleapis.github.io/python-genai/

Query: Where do Google’s official Gemini SDK docs or engineering blog posts explicitly explain that passing a Python function to the tools parameter auto-generates the tool’s name, description, and parameter schema from its signature and docstring?

Answer: The official Google Gen AI Python SDK documentation explicitly states that **you can pass a Python function directly** as a tool, and it will be "automatically called and responded." The example shows passing a Python function (with a docstring and type annotations) directly to the `tools` parameter of `GenerateContentConfig`. However, the documentation does **not explicitly state** that the tool's name, description, and parameter schema are auto-generated from the function's signature and docstring. The behavior is demonstrated via example, but there is no direct statement confirming that the SDK parses the function's metadata (such as the signature and docstring) to populate tool fields.

-----

-----

-----

### Source [43]: https://ai.google.dev/gemini-api/docs/function-calling

Query: Where do Google’s official Gemini SDK docs or engineering blog posts explicitly explain that passing a Python function to the tools parameter auto-generates the tool’s name, description, and parameter schema from its signature and docstring?

Answer: The official Gemini API documentation describes that function declarations must be supplied in a JSON-compatible schema, requiring explicit fields for **name**, **description**, and **parameters**. The documentation also states: "You can also construct FunctionDeclarations from Python functions directly using `types.FunctionDeclaration.from_callable(client=client, callable=your_function)`." This implies there is a mechanism to create function declarations from Python callables, but the documentation does **not explicitly explain** whether and how the tool's name, description, or parameters are auto-generated from the Python function’s signature or docstring. No clear statement is provided about the extraction or auto-generation process.

-----

-----

-----

### Source [44]: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling

Query: Where do Google’s official Gemini SDK docs or engineering blog posts explicitly explain that passing a Python function to the tools parameter auto-generates the tool’s name, description, and parameter schema from its signature and docstring?

Answer: This Vertex AI documentation focuses on best practices and manual schema creation for function calling. It emphasizes writing clear and detailed function names, parameter descriptions, and instructions, as well as demonstrating how to submit function declarations in OpenAPI-like schema format. The documentation does **not mention** automatic generation of tool metadata (name, description, parameter schema) from Python function signatures or docstrings, nor does it describe passing raw Python functions to the tools parameter.

-----

-----

</details>

<details>
<summary>Which tutorials or reference guides show how to parse Gemini API function_call objects, extract names/arguments, and implement robust error handling for unknown or malformed calls inside a ReAct control loop?</summary>

### Source [49]: https://codelabs.developers.google.com/codelabs/gemini-function-calling

Query: Which tutorials or reference guides show how to parse Gemini API function_call objects, extract names/arguments, and implement robust error handling for unknown or malformed calls inside a ReAct control loop?

Answer: This official codelab explains the step-by-step process for interacting with Gemini API function calls:

- **Function Call Parsing**: After submitting a user prompt and function declarations, the Gemini API returns a structured response containing the function name and parameters.
- **Extraction**: The returned object includes the function name and its arguments, which can be extracted programmatically from the response payload. The developer is responsible for parsing these fields to identify which function to invoke and with what arguments.
- **Error Handling**: While the codelab does not provide explicit error handling patterns, it emphasizes that the developer's application should handle the actual API request using the extracted function name and parameters. This implies that robust error handling for unknown or malformed calls should be implemented as part of the application logic, for example by validating function names against the list of declared functions and verifying argument structure and types before making the API call.
- **Control Loop**: The guide describes a loop where the response from the external function is returned to Gemini, which may then generate further function calls as needed. At each step, the application should ensure the integrity of the function call objects before proceeding, which is where error handling can be incorporated.

The codelab presents the broad workflow but does not provide detailed code snippets for error handling or unknown function names; these must be implemented by the developer based on their specific requirements[1].

-----

-----

-----

### Source [50]: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling

Query: Which tutorials or reference guides show how to parse Gemini API function_call objects, extract names/arguments, and implement robust error handling for unknown or malformed calls inside a ReAct control loop?

Answer: This Vertex AI documentation details the definition and declaration of functions (tools) for function calling:

- **Function Declaration**: Functions are declared in a schema compatible with OpenAPI, specifying required parameters, types, and descriptions. This declaration is crucial for downstream parsing and validation.
- **Parsing and Extraction**: The response from Gemini includes the function name and arguments as defined in the functionDeclarations. To parse, developers should reference the schema to extract the function name and parameter values from the returned JSON object.
- **Error Handling**: The documentation does not provide explicit examples for error handling of unknown or malformed calls. However, because the function declarations are strictly typed and limited to those provided in the request, developers can validate that returned function calls match the declared functions and that their parameters conform to the schema before execution.
- **ReAct Loop Integration**: The documentation implies that robust applications should validate incoming function calls at each step of the control loop, and handle cases where the model returns an undeclared or malformed function call by rejecting the call or returning an error to the user[2].

-----

-----

-----

### Source [51]: https://firebase.google.com/docs/ai-logic/function-calling

Query: Which tutorials or reference guides show how to parse Gemini API function_call objects, extract names/arguments, and implement robust error handling for unknown or malformed calls inside a ReAct control loop?

Answer: Firebase AI Logic documentation provides a practical walkthrough of function calling with Gemini, including parameter extraction:

- **Function Call Object Structure**: The documentation specifies how input parameters are structured (name, type, required, description), and how the application is expected to parse these from the Gemini model's response.
- **Extraction**: Upon receiving a function call from Gemini, the app extracts the function name and arguments from the JSON payload. The documentation describes how to map these extracted values to backend logic, such as calling an external weather API with the provided arguments.
- **Validation & Error Handling**: The guide suggests that developers should validate the extracted parameters against the expected input structure (types, required fields). If a function call is not recognized or the arguments are malformed, the application should handle these cases—though explicit code examples for these error scenarios are not provided.
- **ReAct Pattern**: The documentation encourages a multi-turn chat (ReAct) design: after the function is executed (or if an error occurs), the result or error is fed back to Gemini in the next turn, allowing the model to adapt or clarify as needed. This loop is where robust error handling and validation logic is critical[3].

-----

-----

-----

### Source [52]: https://ai.google.dev/gemini-api/docs/function-calling

Query: Which tutorials or reference guides show how to parse Gemini API function_call objects, extract names/arguments, and implement robust error handling for unknown or malformed calls inside a ReAct control loop?

Answer: This official Gemini API documentation shows how to work with function call objects in both Python and JavaScript:

- **Parsing**: When the Gemini model returns a response with a function call, developers can access the function name and parameters from the response object (e.g., `tool_call.name` and the corresponding parameters).
- **Extraction Example**: Example code demonstrates extracting the function call data and using it to execute logic in the application—such as making an API call or running a local function.
- **Error Handling**: The documentation does not provide explicit error handling for unknown or malformed calls. However, the example workflow suggests that after extracting the function call, developers should ensure the function name matches a known function and that parameters are valid before execution.
- **ReAct Loop**: The workflow involves appending the function call result (or presumably an error message, if applicable) to the conversation history before returning it to Gemini for further processing, fitting the ReAct pattern.
- **Implementation Responsibility**: It is implied that robust error handling—including checks for unknown function names, missing/invalid arguments, and malformed calls—should be implemented by the developer within the application logic, as these scenarios are not handled automatically by the API[4].

-----

</details>

<details>
<summary>Where do Gemini API examples demonstrate configuring structured JSON/Pydantic output and retrieving validated data via response.parsed, avoiding manual JSON parsing?</summary>

### Source [53]: https://ai.google.dev/gemini-api/docs/structured-output

Query: Where do Gemini API examples demonstrate configuring structured JSON/Pydantic output and retrieving validated data via response.parsed, avoiding manual JSON parsing?

Answer: The official Gemini API documentation provides explicit examples demonstrating how to configure structured JSON/Pydantic output and retrieve validated data without manual JSON parsing. The recommended approach is to configure a **response schema** directly on the model, which constrains the model to output JSON in the desired format.

#### Python Example

```python
from google import genai
from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="List a few popular cookie recipes, and include the amounts of ingredients.",
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Recipe],
    },
)

# Use the response as a JSON string.
print(response.text)

# Use instantiated objects.
my_recipes: list[Recipe] = response.parsed
```

- The `response_schema` constrains the model's output to match the specified Pydantic model.
- The `response.parsed` property returns **instantiated objects** of the schema type (here, a list of `Recipe`), delivering fully validated data.
- This approach **eliminates the need for manual JSON parsing**, as the Gemini API performs validation and object instantiation automatically.

The documentation also provides a JavaScript example using a similar schema-based approach, but the `response.parsed` pattern is specific to Python and Pydantic integration as shown above[3].

-----

-----

</details>

<details>
<summary>According to teaching resources or course tutorials on ReAct/RAG, why is a mock search tool preferred over live web APIs (e.g., pedagogical benefits, repeatability, no API keys)?</summary>

### Source [56]: https://www.singlestore.com/blog/a-guide-to-retrieval-augmented-generation-rag/

Query: According to teaching resources or course tutorials on ReAct/RAG, why is a mock search tool preferred over live web APIs (e.g., pedagogical benefits, repeatability, no API keys)?

Answer: The tutorial instructs users to add their OpenAI API key as an environment variable before running code examples involving Retrieval Augmented Generation (RAG). This reliance on live APIs introduces several challenges for teaching and reproducibility:
- **API Key Requirement:** Users must obtain and manage their own API keys, which can be a hurdle for students or those running tutorials in environments where sharing or exposing keys is not desirable.
- **Cost and Rate Limiting:** Live API usage may incur costs, and users can be limited by rate quotas or regional restrictions, potentially disrupting the learning experience.
- **Non-repeatability:** Results from live web APIs can change over time as underlying models or data sources update, making it difficult to ensure that all learners get the same results when they run code from a tutorial or teaching resource.
- **Pedagogical Consistency:** For classroom or workshop settings, having all students work with the same mock data ensures that the lesson is consistent and that troubleshooting and grading are simplified.

Although this source does not explicitly discuss mock search tools, the code examples and API key management requirements highlight why educators prefer mock tools for teaching: they eliminate external dependencies and ensure repeatable, controlled demonstrations.

-----

-----

-----

### Source [57]: https://hiringnet.com/exercise-4-and-5-rag-with-react-reflection-for-10-k-filings

Query: According to teaching resources or course tutorials on ReAct/RAG, why is a mock search tool preferred over live web APIs (e.g., pedagogical benefits, repeatability, no API keys)?

Answer: While this source focuses on RAG and ReAct exemplars, it implicitly supports the use of controlled, reproducible teaching scenarios:
- **Few-shot exemplars:** The original ReAct paper used human-annotated examples as templates, allowing the model to follow a specific reasoning process and action sequence. This approach is directly analogous to using a mock search tool in tutorials: it ensures that the learning process is based on known, repeatable data and steps.
- **Pedagogical value:** By using fixed examples, instructors can guarantee that every student or learner is exposed to the same inputs and expected outputs, facilitating easier diagnosis of errors and ensuring fairness in evaluation.

Although this section does not mention mock search tools directly, its emphasis on **repeatability and controlled examples** reflects the pedagogical benefits of using mock tools over live, unpredictable APIs.

-----

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>Generating Structured Output / JSON from LLMs</summary>

# Generating Structured Output / JSON from LLMs

Language models have seen significant growth. Using them effectively often requires complex frameworks. This post discusses how Instructor simplifies this process using Pydantic.

## The Problem with Existing LLM Frameworks

Current frameworks for Language Learning Models (LLMs) have complex setups. Developers find it hard to control interactions with language models. Some frameworks require complex JSON Schema setups.

## The OpenAI Function Calling Game-Changer

OpenAI's Function Calling feature provides a constrained interaction model. However, it has its own complexities, mostly around JSON Schema.

## Why Pydantic?

Instructor uses Pydantic to simplify the interaction between the programmer and the language model.

- **Widespread Adoption**: Pydantic is a popular tool among Python developers.
- **Simplicity**: Pydantic allows model definition in Python.
- **Framework Compatibility**: Many Python frameworks already use Pydantic.

```python
import pydantic
import instructor
from openai import OpenAI

# Enables the response_model
client = instructor.from_openai(OpenAI())

class UserDetail(pydantic.BaseModel):
    name: str
    age: int

    def introduce(self):
        return f"Hello I'm {self.name} and I'm {self.age} years old"

user: UserDetail = client.chat.completions.create(
    model="gpt-3.5-turbo",
    response_model=UserDetail,
    messages=[\
        {"role": "user", "content": "Extract Jason is 25 years old"},\
    ],
)
```

## Simplifying Validation Flow with Pydantic

Pydantic validators simplify features like re-asking or self-critique. This makes these tasks less complex compared to other frameworks.

```python
from typing_extensions import Annotated
from pydantic import BaseModel, BeforeValidator
from instructor import llm_validator

class QuestionAnswerNoEvil(BaseModel):
    question: str
    answer: Annotated[\
        str,\
        BeforeValidator(llm_validator("don't say objectionable things")),\
    ]
```

## The Modular Approach

Pydantic allows for modular output schemas. This leads to more organized code.

### Composition of Schemas

```python
class UserDetails(BaseModel):
    name: str
    age: int

class UserWithAddress(UserDetails):
    address: str
```

### Defining Relationships

```python
class UserDetail(BaseModel):
    id: int
    age: int
    name: str
    friends: List[int]

class UserRelationships(BaseModel):
    users: List[UserDetail]
```

### Using Enums

```python
from enum import Enum, auto

class Role(Enum):
    PRINCIPAL = auto()
    TEACHER = auto()
    STUDENT = auto()
    OTHER = auto()

class UserDetail(BaseModel):
    age: int
    name: str
    role: Role
```

### Flexible Schemas

```python
from typing import List

class Property(BaseModel):
    key: str
    value: str

class UserDetail(BaseModel):
    age: int
    name: str
    properties: List[Property]
```

### Chain of Thought

```python
class TimeRange(BaseModel):
    chain_of_thought: str
    start_time: int
    end_time: int

class UserDetail(BaseModel):
    id: int
    age: int
    name: str
    work_time: TimeRange
    leisure_time: TimeRange
```

## Language Models as Microservices

The architecture resembles FastAPI. Most code can be written as Python functions that use Pydantic objects. This eliminates the need for prompt chains.

### FastAPI Stub

```python
import fastapi
from pydantic import BaseModel

class UserDetails(BaseModel):
    name: str
    age: int

app = fastapi.FastAPI()

@app.get("/user/{user_id}", response_model=UserDetails)
async def get_user(user_id: int) -> UserDetails:
    return ...
```

### Using Instructor as a Function

```python
def extract_user(str) -> UserDetails:
    return client.chat.completions(
           response_model=UserDetails,
           messages=[]
    )
```

### Response Modeling

```python
class MaybeUser(BaseModel):
    result: Optional[UserDetail]
    error: bool
    message: Optional[str]
```

## Conclusion

Instructor, with Pydantic, simplifies interaction with language models. It is usable for both experienced and new developers.

</details>

<details>
<summary>How to Interact with APIs Using Function Calling in Gemini</summary>

# How to Interact with APIs Using Function Calling in Gemini

## What is function calling in Gemini?

The [Vertex AI Gemini API](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/overview) is a family of generative AI models developed by Google DeepMind that is designed for multimodal use cases. [Function calling](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/function-calling) is a feature of Gemini models that makes it easier for developers to get structured data outputs from generative models.

Developers can then use these outputs to call other APIs and return the relevant response data to the model. In other words, function calling helps you connect your generative models to external systems so that the generated content includes the most up-to-date and accurate information.

## How function calling works

Functions are described using function declarations, which helps the generative model understand the purpose and parameters within a function. After you pass function declarations in a query to a generative model, the model returns a structured object that includes the names of relevant functions and their arguments based on the user's query. Note that with function calling, the model doesn't actually call the function. Instead, you can use the returned function and parameters to call the function in any language, library, or framework that you'd like!

https://codelabs.developers.google.com/static/codelabs/gemini-function-calling/img/api-interface.png

## What you'll build

In this codelab, you'll build a generative AI pipeline with the Vertex AI Gemini API and Python. Using your app, users can ask about exchange rates, and the system will fetch the latest data from an external API and respond to the user with the answer.

## What you'll learn

- How to interact with the Gemini model using the Python client library
- How to define a function declaration and register it as a tool
- How to call Gemini and get a function call response
- How to return the function response to Gemini and respond to the user

## What you'll need

- A Google Cloud Project
- A browser such as [Chrome](https://www.google.com/chrome/)
- A Python development environment such as [Colab](https://colab.google/) or [Colab Enterprise](https://cloud.google.com/colab/docs/introduction)

## Enable Vertex AI API

To enable the Vertex AI API, follow these steps:

1. In your browser, navigate to the [Vertex AI API Service Details page](https://console.cloud.google.com/apis/library/aiplatform.googleapis.com).
2. Click the **Enable** button to enable the Vertex AI API in your Google Cloud project.

## Install Python client library for Vertex AI

To install the Python client libraries for Vertex AI, follow these steps:

1. Open a terminal in your development environment.
2. Verify that you have a valid Python development environment, and refer to these [guidelines](https://cloud.google.com/python/docs/setup) if needed.
3. Run the following command to install the Python client library for Vertex AI:

```
pip install --upgrade google-cloud-aiplatform
```

4. If you're running in a notebook environment, then you might need to restart your runtime/kernel to use the newly installed packages.

Now you're ready to use the Vertex AI API!

## Understand the problem

Have you ever interacted with a large language model or generative AI model and asked it about real-time or current information, only to get a response with outdated information or inaccurate information?

Let's try it now! First, we'll import the relevant Python packages and initialize the Gemini model. You can run the following code in a Python development environment such as [Colab](https://colab.google/) or [Colab Enterprise](https://cloud.google.com/colab/docs/introduction) and by installing the latest version of the [Vertex AI SDK for Python](https://cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk):

```python
import vertexai
from vertexai.generative_models import GenerativeModel
model = GenerativeModel("gemini-1.5-pro-001")
```

Now, let's ask a question about the exchange rate for different currencies today:

```python
response = model.generate_content(
    "What's the exchange rate for euros to dollars today?"
)
print(response.text)
```

The model should generate a limited or outdated response for you similar to:

```
As an AI language model, I don't have access to real-time currency exchange
rates. However, as of my last update in September 2021, the approximate exchange
rate between euros (EUR) and US dollars (USD) was:

1 EUR ≈ 1.18 USD

Please note that currency exchange rates constantly fluctuate and can vary
depending on various factors such as economic conditions, supply and demand,
political events, and more. To obtain the most up-to-date and accurate exchange
rate, I recommend using a reliable currency converter or financial website that
provides live rates.

[...]
```

If an end-user received this type of response, they would need to switch contexts to look up the currencies that they're interested in, fetch the latest exchange rate, and perform any conversions on their own.

Ideally, a generative model pipeline could handle some or all of these tasks for the user. In the next section, you'll try some common workarounds for getting structured responses from generative models so that you can call external systems.

## Try common workarounds

When working with generative models in scenarios where you need up-to-date information or data from external sources, you could call an external API then feed the results back to the generative model for it to use in its response.

Before you call an external system, you need to determine the right function to use, extract the relevant parameters from the user, and put the parameters into a structured data object. This usually involves exhaustive prompt engineering to coerce the generative model to output valid structured data.

Let's revisit the question that we asked in the previous section and add some additional instructions for the model. Try sending the following request to the Gemini model:

```python
user_prompt = "What's the exchange rate from euros to US dollars today?"

response = model.generate_content("""
Your task is to extract parameters from the user's input and return it as a
structured JSON payload. The user will ask about the exchange rate and which
currency they are converting from and converting to.

User input: {user_prompt}

Please extract the currencies as parameters and put them in a JSON object.
""".format(user_prompt=user_prompt))
print(response.text)
```

This results is the following text response, which is not valid JSON and will be difficult for us to work with:

````
```json
{
"currency_from": "euros",
"currency_to": "US dollars"
}
```
````

In particular, the first and last lines of the text response include backticks to delimit the code block, the first line includes a language specifier, and the values in the JSON object are not the standard three-letter currency abbreviations that a currency exchange API would expect as input parameters.

We could try to use Python to post-process this text into valid JSON and a dictionary, add more instructions to the prompt, provide one or more examples of desired output, fine-tune the model, or make another call to the generative model asking it to clean up the JSON.

But there is a more deterministic way! Let's learn how to use function calling in Gemini to query for information in external services and return relevant responses to end-users.

## How function calling works

Before we get started with parameter extraction and function calling, let's walk through the steps of function calling and which components are used at runtime.

https://codelabs.developers.google.com/static/codelabs/gemini-function-calling/img/gemini-function-calling-overview.png

### User input to Gemini API

The prompt from the user is sent to the Gemini API, and in that API call to the Gemini model, the developer has defined one or more function declarations within a tool so that the Gemini model knows which functions it can call and how to call them.

### The Gemini API returns a Function Call

Based on the content of the user input and prompt, Gemini will return a Function Call response with structured data that includes the name of the function to call and the corresponding parameters to use.

### Make an API request

Then, you'll use the function name and parameters to make an API request to retrieve information from an external system or API. This API request and response is implemented by the developer in the application code and happens outside of the scope of the Gemini API and SDK. For example, you might use the `requests` library in Python to call a REST API and receive a JSON response. Or you can call the function using your preferred approach and client library.

### Return the API Response to Gemini

Finally, you'll pass the API response back to the Gemini model so that it can generate a response to the end-user's initial prompt or invoke another Function Call response if the Gemini model determines that it needs additional information.

## Choose your API

Now that you understand the overall flow and specific steps in function calling, you'll build a generative AI pipeline to fetch the latest currency exchange rates. First, we'll need to select which API that we want to use as a source of information.

For our currency exchange app, we'll use the REST API at [https://www.frankfurter.app/](https://www.frankfurter.app/) to fetch the latest information about global exchange rates.

To interact with this REST API, we might make a REST API call with `requests` in Python as:

```python
import requests
url = "https://api.frankfurter.app/latest"
response = requests.get(url)
response.text
```

or a `cURL` request such as:

```
curl https://api.frankfurter.app/latest
```

which returns a response similar to:

```
{
  "amount": 1,
  "base": "EUR",
  "date": "2023-12-20",
  "rates": {
    "AUD": 1.6186, "BGN": 1.9558, "BRL": 5.3287,
    "CAD": 1.4609, "CHF": 0.946, "CNY": 7.8121,
    "CZK": 24.538, "DKK": 7.4565, "GBP": 0.86555,
    "HKD": 8.5439, "HUF": 385.23, "IDR": 16994,
    "ILS": 3.9983, "INR": 91.06, "ISK": 150.3,
    "JPY": 157.12, "KRW": 1425.62, "MXN": 18.6867,
    "MYR": 5.0977, "NOK": 11.2895, "NZD": 1.7421,
    "PHP": 60.991, "PLN": 4.3413, "RON": 4.9699,
    "SEK": 11.129, "SGD": 1.4562, "THB": 38.252,
    "TRY": 31.883, "USD": 1.0944, "ZAR": 20.111
  }
}
```

Because function calling in Gemini does not actually make the external API call for you, there are no such restrictions on what type of API that you use! You could use a Cloud Run Service, a Cloud Function, an API request to a Google Cloud service, or any external REST API.

## Define a function and tool

Now that you've selected a REST API to use, we can now define an API specification and register the function in a tool.

Ensure that you've installed the latest version of the [Vertex AI SDK for Python](https://cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk).

Then, import the necessary modules from the Python SDK and initialize the Gemini model:

```python
from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerativeModel,
    Part,
    Tool,
)

model = GenerativeModel("gemini-1.5-pro-001")
```

Referring back to the REST API at [https://api.frankfurter.app/](https://www.frankfurter.app/), we can see that it accepts the following input parameters:

| Parameter    | Type   | Description                                                        |
| ------------ | ------ | ------------------------------------------------------------------ |
| `from`       | String | Currency to convert from                                           |
| `to`         | String | Currency to convert to                                             |
| `date`       | String | Date to fetch the exchange rate for                                |

Using these parameters, a partial OpenAPI specification for this REST API in YAML format looks like:

```yaml
openapi: 3.0.0
info:
  title: Frankfurter Exchange Rate API
  description: This API provides current and historical exchange rates
  version: 1.0.0
servers:
  - url: https://api.frankfurter.app
paths:
  /{date}:
    get:
      summary: Get the latest currency exchange rates.
      parameters:
        - name: date
          in: path
          description: Get currency rates for a specific date or 'latest' if a date is not specified
          required: true
          schema:
            type: string
        - name: from
          in: query
          description: The currency to convert from.
          required: true
          schema:
            type: string
        - name: to
          in: query
          description: The currency to convert to.
          schema:
            type: string
```

Now, let's register this as a `FunctionDeclaration` using the Python SDK for Gemini:

```python
get_exchange_rate_func = FunctionDeclaration(
    name="get_exchange_rate",
    description="Get the exchange rate for currencies between countries",
    parameters={
    "type": "object",
    "properties": {
        "currency_date": {
            "type": "string",
            "description": "A date that must always be in YYYY-MM-DD format or the value 'latest' if a time period is not specified"
        },
        "currency_from": {
            "type": "string",
            "description": "The currency to convert from in ISO 4217 format"
        },
        "currency_to": {
            "type": "string",
            "description": "The currency to convert to in ISO 4217 format"
        }
    },
         "required": [\
            "currency_from",\
            "currency_date",\
      ]
  },
)
```

Be sure to use as much detail as possible in the function and parameter descriptions since the generative model will use this information to determine which function to select and how to fill the parameters in the function call.

Finally, you'll define a `Tool` that includes the function declaration:

```python
exchange_rate_tool = Tool(
    function_declarations=[get_exchange_rate_func],
)
```

Here, you're using one function declaration within a tool, but note that you can register one or more function declarations in a tool, and the model will select the appropriate function to use at runtime. Refer to the documentation on [Function Calling in the Gemini API](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling) for more details on the `FunctionDeclaration`, `Tool`, and related classes in the Gemini SDK for Python.

You've completed the configuration of your function and tool definitions. In the next section, we'll call the generative model with this tool and get back a function call that we can use to call the REST API.

## Generate a function call

Now you can prompt the generative model and include the `tool` that you defined:

```python
prompt = """What is the exchange rate from Australian dollars to Swedish krona?
How much is 500 Australian dollars worth in Swedish krona?"""

response = model.generate_content(
    prompt,
    tools=[exchange_rate_tool],
)
```

Let's take a look at the response object:

```
print(response.candidates[0].content)

role: "model"
parts {
  function_call {
    name: "get_exchange_rate"
    args {
      fields {
        key: "currency_to"
        value {
          string_value: "SEK"
        }
      }
      fields {
        key: "currency_from"
        value {
          string_value: "AUD"
        }
      }
      fields {
        key: "currency_date"
        value {
          string_value: "latest"
        }
      }
    }
  }
}
```

It looks like the model selected the one available function and returned a function call for the `get_exchange_rate` function along with the parameters. And the parameters are in the correct format that we wanted. Hooray for getting structured responses from generative models!

In the next section, you'll use the information in the response to make an API request.

## Make an API request

Recall that function calling in Gemini does not actually make the external API call for you. Rather, you are free to use any language, library, or framework that you'd like!

Here you'll use the `requests` library in Python to call the exchange rate REST API.

Let's unpack the response into a Python dictionary:

```python
params = {}
for key, value in response.candidates[0].content.parts[0].function_call.args.items():
    params[key[9:]] = value
params
```

Now we can call `requests` or any other method:

```python
import requests
url = f"https://api.frankfurter.app/{params['date']}"
api_response = requests.get(url, params=params)
api_response.text
```

Which results in a response similar to:

```
'{"amount":1.0,"base":"AUD","date":"2024-01-16","rates":{"SEK":6.8682}}'
```

And we have our response from the REST API, with the latest exchange rate information from today. In the next section, we'll pass this information back to the model so that it can generate a relevant response for the user.

## Generate a response

Finally, let's generate a response for the user by passing back the function response to the model in the next conversation turn:

```python
response = model.generate_content(
    [\
    Content(role="user", parts=[\
        Part.from_text(prompt + """Give your answer in steps with lots of detail\
            and context, including the exchange rate and date."""),\
    ]),\
    Content(role="function", parts=[\
        Part.from_dict({\
            "function_call": {\
                "name": "get_exchange_rate",\
            }\
        })\
    ]),\
    Content(role="function", parts=[\
        Part.from_function_response(\
            name="get_exchange_rate",\
            response={\
                "content": api_response.text,\
            }\
        )\
    ]),\
    ],
    tools=[exchange_rate_tool],
)

response.candidates[0].content.parts[0].text
```

Once we pass the function response back to the model, it will respond to the user's prompt along with relevant information from the API response.

```
The exchange rate from Australian dollars to Swedish krona on January 16, 2024,
is 1 Australian dollar is equal to 6.8663 Swedish krona.

So, 500 Australian dollars would be worth 500 * 6.8663 = 3,433.15 Swedish krona.
```

## View the full code example

At this point, you could put your Python code in a backend API using a Cloud Run service, a Cloud Function, or another Cloud service and deploy a frontend app that uses this backend API to perform model queries and API calls.

Here's the full code example for our final solution:

```python
import requests
from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerativeModel,
    Part,
    Tool,
)

model = GenerativeModel("gemini-1.5-pro-001")

get_exchange_rate_func = FunctionDeclaration(
    name="get_exchange_rate",
    description="Get the exchange rate for currencies between countries",
    parameters={
    "type": "object",
    "properties": {
        "currency_date": {
            "type": "string",
            "description": "A date that must always be in YYYY-MM-DD format or the value 'latest' if a time period is not specified"
        },
        "currency_from": {
            "type": "string",
            "description": "The currency to convert from in ISO 4217 format"
        },
        "currency_to": {
            "type": "string",
            "description": "The currency to convert to in ISO 4217 format"
        }
    },
         "required": [\
            "currency_from",\
            "currency_date",\
      ]
  },
)

exchange_rate_tool = Tool(
    function_declarations=[get_exchange_rate_func],
)

prompt = """What is the exchange rate from Australian dollars to Swedish krona?
How much is 500 Australian dollars worth in Swedish krona?"""

response = model.generate_content(
    prompt,
    tools=[exchange_rate_tool],
)

response.candidates[0].content

params = {}
for key, value in response.candidates[0].content.parts[0].function_call.args.items():
    params[key[9:]] = value
params

import requests
url = f"https://api.frankfurter.app/{params['date']}"
api_response = requests.get(url, params=params)
api_response.text

response = model.generate_content(
    [\
    Content(role="user", parts=[\
        Part.from_text(prompt + """Give your answer in steps with lots of detail\
            and context, including the exchange rate and date."""),\
    ]),\
    Content(role="function", parts=[\
        Part.from_dict({\
            "function_call": {\
                "name": "get_exchange_rate",\
            }\
        })\
    ]),\
    Content(role="function", parts=[\
        Part.from_function_response(\
            name="get_exchange_rate",\
            response={\
                "content": api_response.text,\
            }\
        )\
    ]),\
    ],
    tools=[exchange_rate_tool],
)

response.candidates[0].content.parts[0].text
```

In this implementation, we used two requests to the generative model: one request to generate a function call and another request to return the function response. Note that this is only one method of handling function calls and function responses with Gemini. You can also make additional function calls to get more information for your query, or use function calling with chat and asynchronous methods.

For additional code samples, refer to the [sample notebook for function calling in Gemini](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb).

## Congratulations

Using function calling in Gemini, you've successfully built a generative AI pipeline that uses with the Vertex AI Gemini API and Python! Users can ask about exchange rates, and the system will fetch the latest data from an external API and respond with an answer.

Given a prompt from an end-user, function calling in Gemini takes care of selecting the appropriate function, extracting parameters from the prompt, and returning a structured data object for you to make an external API call.

The design of function calling in Gemini is intended to give you the best of both worlds for deterministically extracting parameters, while leaving the summarization and content creation to the generative model. Feel free to try out other APIs and prompts in your pipeline and explore the other functionality available related to [Vertex AI Gemini API](https://cloud.google.com/vertex-ai/docs/generative-ai/multimodal/overview).

https://codelabs.developers.google.com/static/codelabs/gemini-function-calling/img/api-interface.png

</details>

<details>
<summary>Introduction to function calling</summary>

# Introduction to function calling

**Function calling**, also known as _tool use_, provides the LLM with definitions of external tools (for example, a `get_current_weather` function). When processing a prompt, the model intelligently determines if a tool is needed and, if so, outputs structured data specifying the tool to call and its parameters (for example, `get_current_weather(location='Boston')`). Your application then executes this tool, feeds the result back to the model, allowing it to complete its response with dynamic, real-world information or the outcome of an action. This effectively bridges the LLM with your systems and extends its capabilities.

https://cloud.google.com/static/vertex-ai/generative-ai/docs/multimodal/images/function-calling.png

Function calling enables two primary use cases:

- **Fetching data**: Retrieve up-to-date information for model responses, such as current weather, currency conversion, or specific data from knowledge bases and APIs (RAG).
- **Taking action**: Perform external operations like submitting forms, updating application state, or orchestrating agentic workflows (e.g., conversation handoffs).

For more use cases and examples that are powered by function calling, see [Use cases](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#use-cases).

## Features and limitations

- The following models support function calling:

  - Gemini models:
    - [Gemini 2.5 Flash-Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite) previewPreview
    - [Gemini 2.5 Flash with Live API native audio](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash#live-api-native-audio) previewPreview
    - [Gemini 2.0 Flash with Live API](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash#live-api) previewPreview
    - [Vertex AI Model Optimizer](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/vertex-ai-model-optimizer) scienceExperimental
    - [Gemini 2.5 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro)
    - [Gemini 2.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash)
    - [Gemini 2.0 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash)
    - [Gemini 2.0 Flash-Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash-lite)
  - Open models:
    - [DeepSeek R1-0528](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/deepseek/r1-0528)
    - [Llama 4 Maverick](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/llama/llama4-maverick)
    - [Llama 4 Scout](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/llama/llama4-scout)
    - [Llama 3.3](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/llama/llama3-3)
- You can specify up to 512 [`FunctionDeclarations`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/python/latest/vertexai.generative_models.FunctionDeclaration)
- Define your functions in the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schema) format.
- For best practices related to the function declarations, including tips for names and descriptions, see [Best practices](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#best-practices).
- For Open Models, follow this [user guide](https://cloud.google.com/vertex-ai/generative-ai/docs/maas/capabilities/function-calling).

## How to create a function calling application

To use function calling, perform the following tasks:

1. [Submit function declarations and prompt to the model](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#submit-prompt).
2. [Provide the API output to the model](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#submit-api-output).

### Step 1: Submit the prompt and function declarations to the model

Declare a [`Tool`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/python/latest/vertexai.generative_models.Tool) in a schema format that's compatible with the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schema). For more information, see [Schema examples](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#schema-examples).

The following examples submit a prompt and function declaration to the Gemini models.

```
PROJECT_ID=myproject
LOCATION=us-central1
MODEL_ID=gemini-2.0-flash-001

curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://${LOCATION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
  -d '{
    "contents": [{\
      "role": "user",\
      "parts": [{\
        "text": "What is the weather in Boston?"\
      }]\
    }],
    "tools": [{\
      "functionDeclarations": [\
        {\
          "name": "get_current_weather",\
          "description": "Get the current weather in a given location",\
          "parameters": {\
            "type": "object",\
            "properties": {\
              "location": {\
                "type": "string",\
                "description": "The city name of the location for which to get the weather.",\
                "default": {\
                  "string_value": "Boston, MA"\
                }\
              }\
            },\
            "required": [\
              "location"\
            ]\
          }\
        }\
      ]\
    }]
  }'
```

You can specify the schema either manually using a Python dictionary or automatically with the `from_func` helper function. The following example demonstrates how to declare a function manually.

```
import vertexai
from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Part,
    Tool,
    ToolConfig
)

# Initialize Vertex AI
# TODO(developer): Update the project
vertexai.init(project="PROJECT_ID", location="us-central1")

# Initialize Gemini model
model = GenerativeModel(model_name="gemini-2.0-flash")

# Manual function declaration
get_current_weather_func = FunctionDeclaration(
    name="get_current_weather",
    description="Get the current weather in a given location",
    # Function parameters are specified in JSON schema format
    parameters={
        "type": "object",
        "properties": {
            "location": {
              "type": "string",
              "description": "The city name of the location for which to get the weather.",
              "default": {
                "string_value": "Boston, MA"
              }
           }
        },
    },
)

response = model.generate_content(
    contents = [\
      Content(\
        role="user",\
          parts=[\
              Part.from_text("What is the weather like in Boston?"),\
          ],\
      )\
    ],
    generation_config = GenerationConfig(temperature=0),
    tools = [\
      Tool(\
        function_declarations=[get_current_weather_func],\
      )\
    ]
)
```

Alternatively, you can declare the function automatically with the `from_func` helper function as shown in the following example:

```
def get_current_weather(location: str = "Boston, MA"):
  """
  Get the current weather in a given location

  Args:
      location: The city name of the location for which to get the weather.

  """
  # This example uses a mock implementation.
  # You can define a local function or import the requests library to call an API
  return {
    "location": "Boston, MA",
    "temperature": 38,
    "description": "Partly Cloudy",
    "icon": "partly-cloudy",
    "humidity": 65,
    "wind": {
        "speed": 10,
        "direction": "NW"
    }
  }
get_current_weather_func = FunctionDeclaration.from_func(get_current_weather)
```

This example demonstrates a text scenario with one function and one
prompt.

### Node.js

```
const {
  VertexAI,
  FunctionDeclarationSchemaType,
} = require('@google-cloud/vertexai');

const functionDeclarations = [\
  {\
    function_declarations: [\
      {\
        name: 'get_current_weather',\
        description: 'get weather in a given location',\
        parameters: {\
          type: FunctionDeclarationSchemaType.OBJECT,\
          properties: {\
            location: {type: FunctionDeclarationSchemaType.STRING},\
            unit: {\
              type: FunctionDeclarationSchemaType.STRING,\
              enum: ['celsius', 'fahrenheit'],\
            },\
          },\
          required: ['location'],\
        },\
      },\
    ],\
  },\
];

const functionResponseParts = [\
  {\
    functionResponse: {\
      name: 'get_current_weather',\
      response: {name: 'get_current_weather', content: {weather: 'super nice'}},\
    },\
  },\
];

/**
 * TODO(developer): Update these variables before running the sample.
 */
async function functionCallingStreamContent(
  projectId = 'PROJECT_ID',
  location = 'us-central1',
  model = 'gemini-2.0-flash-001'
) {
  // Initialize Vertex with your Cloud project and location
  const vertexAI = new VertexAI({project: projectId, location: location});

  // Instantiate the model
  const generativeModel = vertexAI.getGenerativeModel({
    model: model,
  });

  const request = {
    contents: [\
      {role: 'user', parts: [{text: 'What is the weather in Boston?'}]},\
      {\
        role: 'ASSISTANT',\
        parts: [\
          {\
            functionCall: {\
              name: 'get_current_weather',\
              args: {location: 'Boston'},\
            },\
          },\
        ],\
      },\
      {role: 'USER', parts: functionResponseParts},\
    ],
    tools: functionDeclarations,
  };
  const streamingResp = await generativeModel.generateContentStream(request);
  for await (const item of streamingResp.stream) {
    console.log(item.candidates[0].content.parts[0].text);
  }
}
```

This example demonstrates a text scenario with one function and one prompt.

### Go

```
import (
	"context"
	"fmt"
	"io"

	genai "google.golang.org/genai"
)

// generateWithFuncCall shows how to submit a prompt and a function declaration to the model,
// allowing it to suggest a call to the function to fetch external data. Returning this data
// enables the model to generate a text response that incorporates the data.
func generateWithFuncCall(w io.Writer) error {
	ctx := context.Background()

	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
	})
	if err != nil {
		return fmt.Errorf("failed to create genai client: %w", err)
	}

	weatherFunc := &genai.FunctionDeclaration{
		Description: "Returns the current weather in a location.",
		Name:        "getCurrentWeather",
		Parameters: &genai.Schema{
			Type: "object",
			Properties: map[string]*genai.Schema{
				"location": {Type: "string"},
			},
			Required: []string{"location"},
		},
	}
	config := &genai.GenerateContentConfig{
		Tools: []*genai.Tool{
			{FunctionDeclarations: []*genai.FunctionDeclaration{weatherFunc}},
		},
		Temperature: genai.Ptr(float32(0.0)),
	}

	modelName := "gemini-2.0-flash-001"
	contents := []*genai.Content{
		{Parts: []*genai.Part{
			{Text: "What is the weather like in Boston?"},
		},
			Role: "user"},
	}

	resp, err := client.Models.GenerateContent(ctx, modelName, contents, config)
	if err != nil {
		return fmt.Errorf("failed to generate content: %w", err)
	}

	var funcCall *genai.FunctionCall
	for _, p := range resp.Candidates[0].Content.Parts {
		if p.FunctionCall != nil {
			funcCall = p.FunctionCall
			fmt.Fprint(w, "The model suggests to call the function ")
			fmt.Fprintf(w, "%q with args: %v\n", funcCall.Name, funcCall.Args)
			// Example response:
			// The model suggests to call the function "getCurrentWeather" with args: map[location:Boston]
		}
	}
	if funcCall == nil {
		return fmt.Errorf("model did not suggest a function call")
	}

	// Use synthetic data to simulate a response from the external API.
	// In a real application, this would come from an actual weather API.
	funcResp := &genai.FunctionResponse{
		Name: "getCurrentWeather",
		Response: map[string]any{
			"location":         "Boston",
			"temperature":      "38",
			"temperature_unit": "F",
			"description":      "Cold and cloudy",
			"humidity":         "65",
			"wind":             `{"speed": "10", "direction": "NW"}`,
		},
	}

	// Return conversation turns and API response to complete the model's response.
	contents = []*genai.Content{
		{Parts: []*genai.Part{
			{Text: "What is the weather like in Boston?"},
		},
			Role: "user"},
		{Parts: []*genai.Part{
			{FunctionCall: funcCall},
		}},
		{Parts: []*genai.Part{
			{FunctionResponse: funcResp},
		}},
	}

	resp, err = client.Models.GenerateContent(ctx, modelName, contents, config)
	if err != nil {
		return fmt.Errorf("failed to generate content: %w", err)
	}

	respText := resp.Text()

	fmt.Fprintln(w, respText)

	// Example response:
	// The weather in Boston is cold and cloudy with a temperature of 38 degrees Fahrenheit. The humidity is ...

	return nil
}
```

This example demonstrates a text scenario with one function and one prompt.

### C\#

```
using Google.Cloud.AIPlatform.V1;
using System;
using System.Threading.Tasks;
using Type = Google.Cloud.AIPlatform.V1.Type;
using Value = Google.Protobuf.WellKnownTypes.Value;

public class FunctionCalling
{
    public async Task<string> GenerateFunctionCall(
        string projectId = "your-project-id",
        string location = "us-central1",
        string publisher = "google",
        string model = "gemini-2.0-flash-001")
    {
        var predictionServiceClient = new PredictionServiceClientBuilder
        {
            Endpoint = $"{location}-aiplatform.googleapis.com"
        }.Build();

        // Define the user's prompt in a Content object that we can reuse in
        // model calls
        var userPromptContent = new Content
        {
            Role = "USER",
            Parts =
            {
                new Part { Text = "What is the weather like in Boston?" }
            }
        };

        // Specify a function declaration and parameters for an API request
        var functionName = "get_current_weather";
        var getCurrentWeatherFunc = new FunctionDeclaration
        {
            Name = functionName,
            Description = "Get the current weather in a given location",
            Parameters = new OpenApiSchema
            {
                Type = Type.Object,
                Properties =
                {
                    ["location"] = new()
                    {
                        Type = Type.String,
                        Description = "Get the current weather in a given location"
                    },
                    ["unit"] = new()
                    {
                        Type = Type.String,
                        Description = "The unit of measurement for the temperature",
                        Enum = {"celsius", "fahrenheit"}
                    }
                },
                Required = { "location" }
            }
        };

        // Send the prompt and instruct the model to generate content using the tool that you just created
        var generateContentRequest = new GenerateContentRequest
        {
            Model = $"projects/{projectId}/locations/{location}/publishers/{publisher}/models/{model}",
            GenerationConfig = new GenerationConfig
            {
                Temperature = 0f
            },
            Contents =
            {
                userPromptContent
            },
            Tools =
            {
                new Tool
                {
                    FunctionDeclarations = { getCurrentWeatherFunc }
                }
            }
        };

        GenerateContentResponse response = await predictionServiceClient.GenerateContentAsync(generateContentRequest);

        var functionCall = response.Candidates[0].Content.Parts[0].FunctionCall;
        Console.WriteLine(functionCall);

        string apiResponse = "";

        // Check the function name that the model responded with, and make an API call to an external system
        if (functionCall.Name == functionName)
        {
            // Extract the arguments to use in your API call
            string locationCity = functionCall.Args.Fields["location"].StringValue;

            // Here you can use your preferred method to make an API request to
            // fetch the current weather

            // In this example, we'll use synthetic data to simulate a response
            // payload from an external API
            apiResponse = @"{ ""location"": ""Boston, MA"",
                    ""temperature"": 38, ""description"": ""Partly Cloudy""}";
        }

        // Return the API response to Gemini so it can generate a model response or request another function call
        generateContentRequest = new GenerateContentRequest
        {
            Model = $"projects/{projectId}/locations/{location}/publishers/{publisher}/models/{model}",
            Contents =
            {
                userPromptContent, // User prompt
                response.Candidates[0].Content, // Function call response,
                new Content
                {
                    Parts =
                    {
                        new Part
                        {
                            FunctionResponse = new()
                            {
                                Name = functionName,
                                Response = new()
                                {
                                    Fields =
                                    {
                                        { "content", new Value { StringValue = apiResponse } }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            Tools =
            {
                new Tool
                {
                    FunctionDeclarations = { getCurrentWeatherFunc }
                }
            }
        };

        response = await predictionServiceClient.GenerateContentAsync(generateContentRequest);

        string responseText = response.Candidates[0].Content.Parts[0].Text;
        Console.WriteLine(responseText);

        return responseText;
    }
}
```

### Java

```
import com.google.cloud.vertexai.VertexAI;
import com.google.cloud.vertexai.api.Content;
import com.google.cloud.vertexai.api.FunctionDeclaration;
import com.google.cloud.vertexai.api.GenerateContentResponse;
import com.google.cloud.vertexai.api.Schema;
import com.google.cloud.vertexai.api.Tool;
import com.google.cloud.vertexai.api.Type;
import com.google.cloud.vertexai.generativeai.ChatSession;
import com.google.cloud.vertexai.generativeai.ContentMaker;
import com.google.cloud.vertexai.generativeai.GenerativeModel;
import com.google.cloud.vertexai.generativeai.PartMaker;
import com.google.cloud.vertexai.generativeai.ResponseHandler;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;

public class FunctionCalling {
  public static void main(String[] args) throws IOException {
    // TODO(developer): Replace these variables before running the sample.
    String projectId = "your-google-cloud-project-id";
    String location = "us-central1";
    String modelName = "gemini-2.0-flash-001";

    String promptText = "What's the weather like in Paris?";

    whatsTheWeatherLike(projectId, location, modelName, promptText);
  }

  // A request involving the interaction with an external tool
  public static String whatsTheWeatherLike(String projectId, String location,
                                           String modelName, String promptText)
      throws IOException {
    // Initialize client that will be used to send requests.
    // This client only needs to be created once, and can be reused for multiple requests.
    try (VertexAI vertexAI = new VertexAI(projectId, location)) {

      FunctionDeclaration functionDeclaration = FunctionDeclaration.newBuilder()
          .setName("getCurrentWeather")
          .setDescription("Get the current weather in a given location")
          .setParameters(
              Schema.newBuilder()
                  .setType(Type.OBJECT)
                  .putProperties("location", Schema.newBuilder()
                      .setType(Type.STRING)
                      .setDescription("location")
                      .build()
                  )
                  .addRequired("location")
                  .build()
          )
          .build();

      System.out.println("Function declaration:");
      System.out.println(functionDeclaration);

      // Add the function to a "tool"
      Tool tool = Tool.newBuilder()
          .addFunctionDeclarations(functionDeclaration)
          .build();

      // Start a chat session from a model, with the use of the declared function.
      GenerativeModel model = new GenerativeModel(modelName, vertexAI)
          .withTools(Arrays.asList(tool));
      ChatSession chat = model.startChat();

      System.out.println(String.format("Ask the question: %s", promptText));
      GenerateContentResponse response = chat.sendMessage(promptText);

      // The model will most likely return a function call to the declared
      // function `getCurrentWeather` with "Paris" as the value for the
      // argument `location`.
      System.out.println("\nPrint response: ");
      System.out.println(ResponseHandler.getContent(response));

      // Provide an answer to the model so that it knows what the result
      // of a "function call" is.
      Content content =
          ContentMaker.fromMultiModalData(
              PartMaker.fromFunctionResponse(
                  "getCurrentWeather",
                  Collections.singletonMap("currentWeather", "sunny")));
      System.out.println("Provide the function response: ");
      System.out.println(content);
      response = chat.sendMessage(content);

      // See what the model replies now
      System.out.println("Print response: ");
      String finalAnswer = ResponseHandler.getText(response);
      System.out.println(finalAnswer);

      return finalAnswer;
    }
  }
}
```

If the model determines that it needs the output of a particular function, the
response that the application receives from the model contains the function name
and the parameter values that the function should be called with.

The following is an example of a model response to the user prompt "What is the weather like in Boston?". The model proposes calling
the `get_current_weather` function with the parameter `Boston, MA`.

```
candidates {
  content {
    role: "model"
    parts {
      function_call {
        name: "get_current_weather"
        args {
          fields {
            key: "location"
            value {
              string_value: "Boston, MA"
            }
          }
        }
      }
    }
  }
  ...
}
```

### Step 2: Provide the API output to the model

Invoke the external API and pass the API output back to the model.

The following example uses synthetic data to simulate a response payload from an
external API and submits the output back to the model.

```
PROJECT_ID=myproject
MODEL_ID=gemini-2.0-flash
LOCATION="us-central1"

curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
https://${LOCATION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
-d '{
"contents": [\
{\
  "role": "user",\
  "parts": {\
    "text": "What is the weather in Boston?"\
  }\
},\
{\
  "role": "model",\
  "parts": [\
    {\
      "functionCall": {\
        "name": "get_current_weather",\
        "args": {\
          "location": "Boston, MA"\
        }\
      }\
    }\
  ]\
},\
{\
  "role": "user",\
  "parts": [\
    {\
      "functionResponse": {\
        "name": "get_current_weather",\
        "response": {\
          "temperature": 20,\
          "unit": "C"\
        }\
      }\
    }\
  ]\
}\
],
"tools": [\
{\
  "function_declarations": [\
    {\
      "name": "get_current_weather",\
      "description": "Get the current weather in a specific location",\
      "parameters": {\
        "type": "object",\
        "properties": {\
          "location": {\
            "type": "string",\
            "description": "The city name of the location for which to get the weather."\
          }\
        },\
        "required": [\
          "location"\
        ]\
      }\
    }\
  ]\
}\
]
}'
```

```
function_response_contents = []
function_response_parts = []

# Iterates through the function calls in the response in case there are parallel function call requests
for function_call in response.candidates[0].function_calls:
    print(f"Function call: {function_call.name}")

    # In this example, we'll use synthetic data to simulate a response payload from an external API
    if (function_call.args['location'] == "Boston, MA"):
      api_response = { "location": "Boston, MA", "temperature": 38, "description": "Partly Cloudy" }
    if (function_call.args['location'] == "San Francisco, CA"):
      api_response = { "location": "San Francisco, CA", "temperature": 58, "description": "Sunny" }

    function_response_parts.append(
        Part.from_function_response(
            name=function_call.name,
            response={"contents": api_response}
        )
    )
    # Add the function call response to the contents
    function_response_contents = Content(role="user", parts=function_response_parts)

# Submit the User's prompt, model's response, and API output back to the model
response = model.generate_content(
  [\
    Content( # User prompt\
      role="user",\
      parts=[\
          Part.from_text("What is the weather like in Boston?"),\
      ],\
    ),\
    response.candidates[0].content,  # Function call response\
    function_response_contents   # API output\
  ],
  tools=[\
    Tool(\
      function_declarations=[get_current_weather_func],\
    )\
  ],
)
# Get the model summary response
print(response.text)
```

For best practices related to API invocation, see [Best practices - API invocation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#invoke-api-bp).

If the model had proposed several parallel function calls, the application must
provide all of the responses back to the model. To learn more, see
[Parallel function calling example](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#parallel-samples).

The model may determine that the
output of another function is necessary for responding to the prompt. In this case,
the response that the application receives from the model contains another
function name and another set of parameter values.

If the model determines that the API response is sufficient for responding to
the user's prompt, it creates a natural language response and returns it to the
application. The following is an example of a natural language response:

```
It is currently 38 degrees Fahrenheit in Boston, MA with partly cloudy skies.
```

## Parallel function calling

For prompts such as "Get weather details in Boston and San Francisco?",
the model may propose several parallel function calls. For a list of models that
support parallel function calling, see [Supported models](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#features).

This example demonstrates a scenario with one `get_current_weather` function.
The user prompt is "Get weather details in Boston and San Francisco?". The
model proposes two parallel `get_current_weather` function calls: one with the
parameter `Boston` and the other with the parameter `San Francisco`.

```
{
"candidates": [\
  {\
    "content": {\
      "role": "model",\
      "parts": [\
        {\
          "functionCall": {\
            "name": "get_current_weather",\
            "args": {\
              "location": "Boston"\
            }\
          }\
        },\
        {\
          "functionCall": {\
            "name": "get_current_weather",\
            "args": {\
              "location": "San Francisco"\
            }\
          }\
        }\
      ]\
    },\
    ...\
  }\
],
...
}
```

**Model request**

```
PROJECT_ID=my-project
MODEL_ID=gemini-2.0-flash
LOCATION="us-central1"
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
https://${LOCATION}-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
-d '{
"contents": [\
{\
  "role": "user",\
  "parts": {\
    "text": "What is difference in temperature in Boston and San Francisco?"\
  }\
},\
{\
  "role": "model",\
  "parts": [\
    {\
      "functionCall": {\
        "name": "get_current_weather",\
        "args": {\
          "location": "Boston"\
        }\
      }\
    },\
    {\
      "functionCall": {\
        "name": "get_current_weather",\
        "args": {\
          "location": "San Francisco"\
        }\
      }\
    }\
  ]\
},\
{\
  "role": "user",\
  "parts": [\
    {\
      "functionResponse": {\
        "name": "get_current_weather",\
        "response": {\
          "temperature": 30.5,\
          "unit": "C"\
        }\
      }\
    },\
    {\
      "functionResponse": {\
        "name": "get_current_weather",\
        "response": {\
          "temperature": 20,\
          "unit": "C"\
        }\
      }\
    }\
  ]\
}\
],
"tools": [\
{\
  "function_declarations": [\
    {\
      "name": "get_current_weather",\
      "description": "Get the current weather in a specific location",\
      "parameters": {\
        "type": "object",\
        "properties": {\
          "location": {\
            "type": "string",\
            "description": "The city name of the location for which to get the weather."\
          }\
        },\
        "required": [\
          "location"\
        ]\
      }\
    }\
  ]\
}\
]
}'
```

The natural language response created by the model is similar to the following:

**Model response**

```
[\
{\
    "candidates": [\
        {\
            "content": {\
                "parts": [\
                    {\
                        "text": "The temperature in Boston is 30.5C and the temperature in San Francisco is 20C. The difference is 10.5C. \n"\
                    }\
                ]\
            },\
            "finishReason": "STOP",\
            ...\
        }\
    ]\
    ...\
}\
]
```

This example demonstrates a scenario with one `get_current_weather` function.
The user prompt is "What is the weather like in Boston and San Francisco?".

```
import vertexai
from vertexai.generative_models import (
    Content,
    FunctionDeclaration,
    GenerationConfig,
    GenerativeModel,
    Part,
    Tool,
    ToolConfig
)

# Initialize Vertex AI
# TODO(developer): Update the project
vertexai.init(project="my-project", location="us-central1")

# Initialize Gemini model
model = GenerativeModel(model_name="gemini-2.0-flash")

# Manual function declaration
get_current_weather_func = FunctionDeclaration(
    name="get_current_weather",
    description="Get the current weather in a given location",
    # Function parameters are specified in JSON schema format
    parameters={
        "type": "object",
        "properties": {
            "location": {
              "type": "string",
              "description": "The city name of the location for which to get the weather.",
              "default": {
                "string_value": "Boston, MA"
              }
          }
        },
    },
)

response = model.generate_content(
    contents = [\
      Content(\
        role="user",\
          parts=[\
              Part.from_text("What is the weather like in Boston and San Francisco?"),\
          ],\
      )\
    ],
    generation_config = GenerationConfig(temperature=0),
    tools = [\
      Tool(\
        function_declarations=[get_current_weather_func],\
      )\
    ]
)
```

The following command demonstrates how you can provide the function output to
the model.

```
function_response_contents = []
function_response_parts = []

# You can have parallel function call requests for the same function type.
# For example, 'location_to_lat_long("London")' and 'location_to_lat_long("Paris")'
# In that case, collect API responses in parts and send them back to the model

for function_call in response.candidates[0].function_calls:
    print(f"Function call: {function_call.name}")

    # In this example, we'll use synthetic data to simulate a response payload from an external API
    if (function_call.args['location'] == "Boston, MA"):
      api_response = { "location": "Boston, MA", "temperature": 38, "description": "Partly Cloudy" }
    if (function_call.args['location'] == "San Francisco, CA"):
      api_response = { "location": "San Francisco, CA", "temperature": 58, "description": "Sunny" }

    function_response_parts.append(
        Part.from_function_response(
            name=function_call.name,
            response={"contents": api_response}
        )
    )
    # Add the function call response to the contents
    function_response_contents = Content(role="user", parts=function_response_parts)

function_response_contents

response = model.generate_content(
    contents = [\
        Content(\
        role="user",\
          parts=[\
              Part.from_text("What is the weather like in Boston and San Francisco?"),\
          ],\
        ),  # User prompt\
        response.candidates[0].content,  # Function call response\
        function_response_contents,  # Function response\
    ],
    tools = [\
      Tool(\
        function_declarations=[get_current_weather_func],\
      )\
    ]
)
# Get the model summary response
print(response.text)
```

## Forced function calling

Instead of allowing the model to choose between a natural language response and a function call, you can force it to only predict function calls. This is known as _forced function calling_. You can also choose to provide the model with a full set of function declarations, but restrict its responses to a subset of these functions.

| Mode | Description |
| --- | --- |
| `AUTO` | The default model behavior. The model decides whether to predict function calls or a natural language response. |
| `ANY` | The model is constrained to always predict a function call. If `allowed_function_names` is not provided, the model picks from all of the available function declarations. If `allowed_function_names` is provided, the model picks from the set of allowed functions. |
| `NONE` | The model must not predict function calls. This behaviour is equivalent to a model request without any associated function declarations. |

The following example is forced to predict only `get_weather` function calls.

```
response = model.generate_content(
    contents = [\
      Content(\
        role="user",\
          parts=[\
              Part.from_text("What is the weather like in Boston?"),\
          ],\
      )\
    ],
    generation_config = GenerationConfig(temperature=0),
    tools = [\
      Tool(\
        function_declarations=[get_weather_func, some_other_function],\
      )\
    ],
    tool_config=ToolConfig(
        function_calling_config=ToolConfig.FunctionCallingConfig(
            # ANY mode forces the model to predict only function calls
            mode=ToolConfig.FunctionCallingConfig.Mode.ANY,
            # Allowed function calls to predict when the mode is ANY. If empty, any of
            # the provided function calls will be predicted.
            allowed_function_names=["get_weather"],
        )
    )
)
```

## Function schema examples

Function declarations are compatible with the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schema). We support the following attributes: `type`, `nullable`, `required`, `format`, `description`, `properties`, `items`, `enum`, `anyOf`, `$ref`, and `$defs`. Remaining attributes are not supported.

**Function with object and array parameters**

```
extract_sale_records_func = FunctionDeclaration(
  name="extract_sale_records",
  description="Extract sale records from a document.",
  parameters={
      "type": "object",
      "properties": {
          "records": {
              "type": "array",
              "description": "A list of sale records",
              "items": {
                  "description": "Data for a sale record",
                  "type": "object",
                  "properties": {
                      "id": {"type": "integer", "description": "The unique id of the sale."},
                      "date": {"type": "string", "description": "Date of the sale, in the format of MMDDYY, e.g., 031023"},
                      "total_amount": {"type": "number", "description": "The total amount of the sale."},
                      "customer_name": {"type": "string", "description": "The name of the customer, including first name and last name."},
                      "customer_contact": {"type": "string", "description": "The phone number of the customer, e.g., 650-123-4567."},
                  },
                  "required": ["id", "date", "total_amount"],
              },
          },
      },
      "required": ["records"],
  },
)
```

**Function with enum parameter**

```
set_status_func = FunctionDeclaration(
  name="set_status",
  description="set a ticket's status field",
  # Function parameters are specified in JSON schema format
  parameters={
      "type": "object",
      "properties": {
        "status": {
          "type": "integer",
          "enum": [ "10", "20", "30" ],   # Provide integer (or any other type) values as strings.
        }
      },
  },
)
```

**Function with ref and def**

```
{
  "contents": ...,
  "tools": [\
    {\
      "function_declarations": [\
        {\
          "name": "get_customer",\
          "description": "Search for a customer by name",\
          "parameters": {\
            "type": "object",\
            "properties": {\
              "first_name": { "ref": "#/defs/name" },\
              "last_name": { "ref": "#/defs/name" }\
            },\
            "defs": {\
              "name": { "type": "string" }\
            }\
          }\
        }\
      ]\
    }\
  ]
}
```

Usage notes:

- Unlike, the OpenAPI schema, specify `ref` and `defs` without the `$` symbol.
- `ref` must refer to direct child of `defs`; no
external references.
- The maximum depth of nested schema is 32.
- Recursion depth in `defs` (self-reference) is limited to two.

**`from_func` with array parameter**

```
from typing import List

# Define a function. Could be a local function or you can import the requests library to call an API
def multiply_numbers(numbers: List[int] = [1, 1]) -> int:
  """
  Calculates the product of all numbers in an array.

  Args:
      numbers: An array of numbers to be multiplied.

  Returns:
      The product of all the numbers. If the array is empty, returns 1.
  """

  if not numbers:  # Handle empty array
      return 1

  product = 1
  for num in numbers:
      product *= num

  return product

multiply_number_func = FunctionDeclaration.from_func(multiply_numbers)

"""
multiply_number_func contains the following schema:

{'name': 'multiply_numbers',
  'description': 'Calculates the product of all numbers in an array.',
  'parameters': {'properties': {'numbers': {'items': {'type': 'INTEGER'},
    'description': 'list of numbers',
    'default': [1.0, 1.0],
    'title': 'Numbers',
    'type': 'ARRAY'}},
  'description': 'Calculates the product of all numbers in an array.',
  'title': 'multiply_numbers',
  'property_ordering': ['numbers'],
  'type': 'OBJECT'}}
"""
```

## Best practices for function calling

### Write clear and detailed function names, parameter descriptions, and instructions

- Function names should start with a letter or an underscore and contain only characters a-z, A-Z, 0-9, underscores, dots or dashes with a maximum length of 64.
- Function descriptions should be clear and verbose. For example, a `book_flight_ticket` function could have the description
`book flight tickets after confirming users' specific requirements, such as time, departure, destination, party size and preferred airline`

### Use strong typed parameters

If the parameter values are from a finite set, add an `enum` field instead of putting the set of values into the description. If the parameter value is always an integer, set the type to `integer` rather than `number`.

### Use system instructions

When using functions with date, time, or location parameters, include the
current date, time, or relevant location information (for example, city and
country) in the system instruction. This provides the model with the necessary
context to process the request accurately, even if the user's prompt lacks
details.

### Update user prompt

For best results, prepend the user prompt with the following details:

- Additional context for the model—for example, `You are a flight API assistant to help with searching flights based on user preferences.`
- Details or instructions on how and when to use the functions—for example, `Don't make assumptions on the departure or destination airports. Always use a future date for the departure or destination time.`
- Instructions to ask clarifying questions if user queries are ambiguous—for example, `Ask clarifying questions if not enough information is available.`

### Use generation configuration

For the temperature parameter, use `0` or another low value. This instructs
the model to generate more confident results and reduces hallucinations.

### Validate the API call

If the model proposes the invocation of a function that would send an order,
update a database, or otherwise have significant consequences, validate the
function call with the user before executing it.

## Pricing

The pricing for function calling is based on the number of characters within the
text inputs and outputs. To learn more, see
[Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing).

Here, text input (prompt)
refers to the user prompt for the current conversation turn, the function
declarations for the current conversation turn, and the history of the
conversation. The history of the conversation includes the queries, the function
calls, and the function responses of previous conversation turns.
Vertex AI truncates the history of the conversation at 32,000 characters.

Text output (response) refers to the function calls and the text responses
for the current conversation turn.

## Use cases of function calling

You can use function calling for the following tasks:

| Use Case | Example description | Example link |
| --- | --- | --- |
| Integrate with external APIs | Get weather information using a meteorological API | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb) |
| Convert addresses to latitude/longitude coordinates | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb) |
| Convert currencies using a currency exchange API | [Codelab](https://codelabs.developers.google.com/codelabs/gemini-function-calling) |
| Build advanced chatbots | Answer customer questions about products and services | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb) |
| Create an assistant to answer financial and news questions about companies | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/use_case_company_news_and_insights.ipynb) |
| Structure and control function calls | Extract structured entities from raw log data | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb) |
| Extract single or multiple parameters from user input | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/function_calling_data_structures.ipynb) |
| Handle lists and nested data structures in function calls | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/function_calling_data_structures.ipynb) |
| Handle function calling behavior | Handle parallel function calls and responses | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/parallel_function_calling.ipynb) |
| Manage when and which functions the model can call | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/forced_function_calling.ipynb) |
| Query databases with natural language | Convert natural language questions into SQL queries for BigQuery | [Sample app](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/function-calling/sql-talk-app) |
| Multimodal function calling | Use images, videos, audio, and PDFs as input to trigger function calls | [Notebook tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/multimodal_function_calling.ipynb) |

Here are some more use cases:

- **Interpret voice commands**: Create functions that correspond with in-vehicle tasks. For example, you can create functions that turn on the radio or activate the air conditioning. Send audio files of the user's voice commands to the model, and ask the model to convert the audio into text and identify the function that the user wants to call.

- **Automate workflows based on environmental triggers**: Create functions to represent processes that can be automated. Provide the model with data from environmental sensors and ask it to parse and process the data to determine whether one or more of the workflows should be activated. For example, a model could process temperature data in a warehouse and choose to activate a sprinkler function.

- **Automate the assignment of support tickets**: Provide the model with support tickets, logs, and context-aware rules. Ask the model to process all of this information to determine who the ticket should be assigned to. Call a function to assign the ticket to the person suggested by the model.

- **Retrieve information from a knowledge base**: Create functions that retrieve academic articles on a given subject and summarize them. Enable the model to answer questions about academic subjects and provide citations for its answers.

## What's next

- See the [API reference for function calling](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/function-calling).
- Learn about [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview).

</details>

<details>
<summary>Structured output</summary>

# Structured output

You can configure Gemini for structured output instead of unstructured text,
allowing precise extraction and standardization of information for further processing.
For example, you can use structured output to extract information from resumes,
standardize them to build a structured database.

Gemini can generate either [JSON](https://ai.google.dev/gemini-api/docs/structured-output#generating-json)
or [enum values](https://ai.google.dev/gemini-api/docs/structured-output#generating-enums) as structured output.

## Generating JSON

There are two ways to generate JSON using the Gemini API:

- Configure a schema on the model
- Provide a schema in a text prompt

Configuring a schema on the model is the **recommended** way to generate JSON,
because it constrains the model to output JSON.

### Configuring a schema (recommended)

To constrain the model to generate JSON, configure a `responseSchema`. The model
will then respond to any prompt with JSON-formatted output.

```
from google import genai
from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="List a few popular cookie recipes, and include the amounts of ingredients.",
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Recipe],
    },
)
# Use the response as a JSON string.
print(response.text)

# Use instantiated objects.
my_recipes: list[Recipe] = response.parsed

```

```
import { GoogleGenAI, Type } from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents:
      "List a few popular cookie recipes, and include the amounts of ingredients.",
    config: {
      responseMimeType: "application/json",
      responseSchema: {
        type: Type.ARRAY,
        items: {
          type: Type.OBJECT,
          properties: {
            recipeName: {
              type: Type.STRING,
            },
            ingredients: {
              type: Type.ARRAY,
              items: {
                type: Type.STRING,
              },
            },
          },
          propertyOrdering: ["recipeName", "ingredients"],
        },
      },
    },
  });

  console.log(response.text);
}

main();

```

```
package main

import (
    "context"
    "fmt"
    "log"

    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, nil)
    if err != nil {
        log.Fatal(err)
    }

    config := &genai.GenerateContentConfig{
        ResponseMIMEType: "application/json",
        ResponseSchema: &genai.Schema{
            Type: genai.TypeArray,
            Items: &genai.Schema{
                Type: genai.TypeObject,
                Properties: map[string]*genai.Schema{
                    "recipeName": {Type: genai.TypeString},
                    "ingredients": {
                        Type:  genai.TypeArray,
                        Items: &genai.Schema{Type: genai.TypeString},
                    },
                },
                PropertyOrdering: []string{"recipeName", "ingredients"},
            },
        },
    }

    result, err := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash",
        genai.Text("List a few popular cookie recipes, and include the amounts of ingredients."),
        config,
    )
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(result.Text())
}

```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-d '{
      "contents": [{\
        "parts":[\
          { "text": "List a few popular cookie recipes, and include the amounts of ingredients." }\
        ]\
      }],
      "generationConfig": {
        "responseMimeType": "application/json",
        "responseSchema": {
          "type": "ARRAY",
          "items": {
            "type": "OBJECT",
            "properties": {
              "recipeName": { "type": "STRING" },
              "ingredients": {
                "type": "ARRAY",
                "items": { "type": "STRING" }
              }
            },
            "propertyOrdering": ["recipeName", "ingredients"]
          }
        }
      }
}' 2> /dev/null | head

```

The output might look like this:

```
[\
  {\
    "recipeName": "Chocolate Chip Cookies",\
    "ingredients": [\
      "1 cup (2 sticks) unsalted butter, softened",\
      "3/4 cup granulated sugar",\
      "3/4 cup packed brown sugar",\
      "1 teaspoon vanilla extract",\
      "2 large eggs",\
      "2 1/4 cups all-purpose flour",\
      "1 teaspoon baking soda",\
      "1 teaspoon salt",\
      "2 cups chocolate chips"\
    ]\
  },\
  ...\
]

```

### Providing a schema in a text prompt

Instead of configuring a schema, you can supply a schema as natural language or
pseudo-code in a text prompt. This method is **not recommended**, because it
might produce lower quality output, and because the model is not constrained to
follow the schema.

Here's a generic example of a schema provided in a text prompt:

```
List a few popular cookie recipes, and include the amounts of ingredients.

Produce JSON matching this specification:

Recipe = { "recipeName": string, "ingredients": array<string> }
Return: array<Recipe>

```

Since the model gets the schema from text in the prompt, you might have some
flexibility in how you represent the schema. But when you supply a schema inline
like this, the model is not actually constrained to return JSON. For a more
deterministic, higher quality response, configure a schema on the model, and
don't duplicate the schema in the text prompt.

## Generating enum values

In some cases you might want the model to choose a single option from a list of
options. To implement this behavior, you can pass an _enum_ in your schema. You
can use an enum option anywhere you could use a `string` in the
`responseSchema`, because an enum is an array of strings. Like a JSON schema, an
enum lets you constrain model output to meet the requirements of your
application.

For example, assume that you're developing an application to classify
musical instruments into one of five categories: `"Percussion"`, `"String"`,
`"Woodwind"`, `"Brass"`, or " `"Keyboard"`". You could create an enum to help
with this task.

In the following example, you pass an enum as the
`responseSchema`, constraining the model to choose the most appropriate option.

```
from google import genai
import enum

class Instrument(enum.Enum):
  PERCUSSION = "Percussion"
  STRING = "String"
  WOODWIND = "Woodwind"
  BRASS = "Brass"
  KEYBOARD = "Keyboard"

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='What type of instrument is an oboe?',
    config={
        'response_mime_type': 'text/x.enum',
        'response_schema': Instrument,
    },
)

print(response.text)
# Woodwind

```

```
import { GoogleGenAI, Type } from "@google/genai";

const ai = new GoogleGenAI({});

const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "What type of instrument is an oboe?",
    config: {
      responseMimeType: "text/x.enum",
      responseSchema: {
        type: Type.STRING,
        enum: ["Percussion", "String", "Woodwind", "Brass", "Keyboard"],
      },
    },
  });

console.log(response.text);

```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -d '{
          "contents": [{\
            "parts":[\
              { "text": "What type of instrument is an oboe?" }\
            ]\
          }],
          "generationConfig": {
            "responseMimeType": "text/x.enum",
            "responseSchema": {
              "type": "STRING",
              "enum": ["Percussion", "String", "Woodwind", "Brass", "Keyboard"]
            }
          }
    }'

```

The Python library will translate the type declarations for the API. However,
the API accepts a subset of the OpenAPI 3.0 schema
( [Schema](https://ai.google.dev/api/caching#schema)).

There are two other ways to specify an enumeration. You can use a
[`Literal`](https://docs.pydantic.dev/1.10/usage/types/#literal-type):

```
Literal["Percussion", "String", "Woodwind", "Brass", "Keyboard"]

```

And you can also pass the schema as JSON:

```
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='What type of instrument is an oboe?',
    config={
        'response_mime_type': 'text/x.enum',
        'response_schema': {
            "type": "STRING",
            "enum": ["Percussion", "String", "Woodwind", "Brass", "Keyboard"],
        },
    },
)

print(response.text)
# Woodwind

```

Beyond basic multiple choice problems, you can use an enum anywhere in a JSON
schema. For example, you could ask the model for a list of recipe titles and
use a `Grade` enum to give each title a popularity grade:

```
from google import genai

import enum
from pydantic import BaseModel

class Grade(enum.Enum):
    A_PLUS = "a+"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    F = "f"

class Recipe(BaseModel):
  recipe_name: str
  rating: Grade

client = genai.Client()
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='List 10 home-baked cookie recipes and give them grades based on tastiness.',
    config={
        'response_mime_type': 'application/json',
        'response_schema': list[Recipe],
    },
)

print(response.text)

```

The response might look like this:

```
[\
  {\
    "recipe_name": "Chocolate Chip Cookies",\
    "rating": "a+"\
  },\
  {\
    "recipe_name": "Peanut Butter Cookies",\
    "rating": "a"\
  },\
  {\
    "recipe_name": "Oatmeal Raisin Cookies",\
    "rating": "b"\
  },\
  ...\
]

```

## About JSON schemas

Configuring the model for JSON output using `responseSchema` parameter relies on
`Schema` object to define its structure. This object represents a select
subset of the [OpenAPI 3.0 Schema object](https://spec.openapis.org/oas/v3.0.3#schema-object),
and also adds a `propertyOrdering` field.

Here's a pseudo-JSON representation of all the `Schema` fields:

```
{
  "type": enum (Type),
  "format": string,
  "description": string,
  "nullable": boolean,
  "enum": [\
    string\
  ],
  "maxItems": integer,
  "minItems": integer,
  "properties": {
    string: {
      object (Schema)
    },
    ...
  },
  "required": [\
    string\
  ],
  "propertyOrdering": [\
    string\
  ],
  "items": {
    object (Schema)
  }
}

```

The `Type` of the schema must be one of the OpenAPI
[Data Types](https://spec.openapis.org/oas/v3.0.3#data-types), or a union of
those types (using `anyOf`). Only a subset of fields is valid for each `Type`.
The following list maps each `Type` to a subset of the fields that are valid for
that type:

- `string` -\> `enum`, `format`, `nullable`
- `integer` -\> `format`, `minimum`, `maximum`, `enum`, `nullable`
- `number` -\> `format`, `minimum`, `maximum`, `enum`, `nullable`
- `boolean` -\> `nullable`
- `array` -\> `minItems`, `maxItems`, `items`, `nullable`
- `object` -\> `properties`, `required`, `propertyOrdering`, `nullable`

Here are some example schemas showing valid type-and-field combinations:

```
{ "type": "string", "enum": ["a", "b", "c"] }

{ "type": "string", "format": "date-time" }

{ "type": "integer", "format": "int64" }

{ "type": "number", "format": "double" }

{ "type": "boolean" }

{ "type": "array", "minItems": 3, "maxItems": 3, "items": { "type": ... } }

{ "type": "object",
  "properties": {
    "a": { "type": ... },
    "b": { "type": ... },
    "c": { "type": ... }
  },
  "nullable": true,
  "required": ["c"],
  "propertyOrdering": ["c", "b", "a"]
}

```

For complete documentation of the Schema fields as they're used in the Gemini
API, see the [Schema reference](https://ai.google.dev/api/caching#Schema).

### Property ordering

When you're working with JSON schemas in the Gemini API, the order of properties
is important. By default, the API orders properties alphabetically and does not
preserve the order in which the properties are defined (although the
[Google Gen AI SDKs](https://ai.google.dev/gemini-api/docs/sdks) may preserve this order). If you're
providing examples to the model with a schema configured, and the property
ordering of the examples is not consistent with the property ordering of the
schema, the output could be rambling or unexpected.

To ensure a consistent, predictable ordering of properties, you can use the
optional `propertyOrdering[]` field.

```
"propertyOrdering": ["recipeName", "ingredients"]

```

`propertyOrdering[]` – not a standard field in the OpenAPI specification
– is an array of strings used to determine the order of properties in the
response. By specifying the order of properties and then providing examples with
properties in that same order, you can potentially improve the quality of
results. `propertyOrdering` is only supported when you manually create
`types.Schema`.

### Schemas in Python

When you're using the Python library, the value of `response_schema` must be one
of the following:

- A type, as you would use in a type annotation (see the Python
[`typing` module](https://docs.python.org/3/library/typing.html))
- An instance of
[`genai.types.Schema`](https://googleapis.github.io/python-genai/genai.html#genai.types.Schema)
- The `dict` equivalent of `genai.types.Schema`

The easiest way to define a schema is with a Pydantic type (as shown in the
previous example):

```
config={'response_mime_type': 'application/json',
        'response_schema': list[Recipe]}

```

When you use a Pydantic type, the Python library builds out a JSON schema for
you and sends it to the API. For additional examples, see the
[Python library docs](https://googleapis.github.io/python-genai/index.html#json-response-schema).

The Python library supports schemas defined with the following types (where
`AllowedType` is any allowed type):

- `int`
- `float`
- `bool`
- `str`
- `list[AllowedType]`
- `AllowedType|AllowedType|...`
- For structured types:
  - `dict[str, AllowedType]`. This annotation declares all dict values to
    be the same type, but doesn't specify what keys should be included.
  - User-defined
    [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/). This
    approach lets you specify the key names and define different types for the
    values associated with each of the keys, including nested structures.

### JSON Schema support

[JSON Schema](https://json-schema.org/) is a more recent specification than
OpenAPI 3.0, which the [Schema](https://ai.google.dev/api/caching#Schema) object is based on.
Support for JSON Schema is available as a preview using the field
[`responseJsonSchema`](https://ai.google.dev/api/generate-content#FIELDS.response_json_schema) which
accepts any JSON Schema with the following limitations:

- It only works with Gemini 2.5.
- While all JSON Schema properties can be passed, not all are supported. See
the [documentation](https://ai.google.dev/api/generate-content#FIELDS.response_json_schema) for the
field for more details.
- Recursive references can only be used as the value of a non-required object
property.
- Recursive references are unrolled to a finite degree, based on the size of
the schema.
- Schemas that contain `$ref` cannot contain any properties other than those
starting with a `$`.

Here's an example of generating a JSON Schema with Pydantic and submitting it to
the model:

```
curl "https://generativelanguage.googleapis.com/v1alpha/models/\
gemini-2.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY"\
    -H 'Content-Type: application/json' \
    -d @- <<EOF
{
  "contents": [{\
    "parts":[{\
      "text": "Please give a random example following this schema"\
    }]\
  }],
  "generationConfig": {
    "response_mime_type": "application/json",
    "response_json_schema": $(python3 - << PYEOF
from enum import Enum
from typing import List, Optional, Union, Set
from pydantic import BaseModel, Field, ConfigDict
import json

class UserRole(str, Enum):
    ADMIN = "admin"
    VIEWER = "viewer"

class Address(BaseModel):
    street: str
    city: str

class UserProfile(BaseModel):
    username: str = Field(description="User's unique name")
    age: Optional[int] = Field(ge=0, le=120)
    roles: Set[UserRole] = Field(min_items=1)
    contact: Union[Address, str]
    model_config = ConfigDict(title="User Schema")

# Generate and print the JSON Schema
print(json.dumps(UserProfile.model_json_schema(), indent=2))
PYEOF
)
  }
}
EOF

```

Passing JSON Schema directly is not yet supported when using the SDK.

## Best practices

Keep the following considerations and best practices in mind when you're using a
response schema:

- The size of your response schema counts towards the input token limit.
- By default, fields are optional, meaning the model can populate the fields or
skip them. You can set fields as required to force the model to provide a
value. If there's insufficient context in the associated input prompt, the
model generates responses mainly based on the data it was trained on.
- A complex schema can result in an `InvalidArgument: 400` error. Complexity
might come from long property names, long array length limits, enums with
many values, objects with lots of optional properties, or a combination of
these factors.

If you get this error with a valid schema, make one or more of the following
changes to resolve the error:

  - Shorten property names or enum names.
  - Flatten nested arrays.
  - Reduce the number of properties with constraints, such as numbers with
    minimum and maximum limits.
  - Reduce the number of properties with complex constraints, such as
    properties with complex formats like `date-time`.
  - Reduce the number of optional properties.
  - Reduce the number of valid values for enums.
- If you aren't seeing the results you expect, add more context to your input
prompts or revise your response schema. For example, review the model's
response without structured output to see how the model responds. You can then
update your response schema so that it better fits the model's output.


## What's next

Now that you've learned how to generate structured output, you might want to try
using Gemini API tools:

- [Function calling](https://ai.google.dev/gemini-api/docs/function-calling)
- [Code execution](https://ai.google.dev/gemini-api/docs/code-execution)
- [Grounding with Google Search](https://ai.google.dev/gemini-api/docs/grounding)

</details>


## Code Sources

<details>
<summary>Repository analysis for https://github.com/towardsai/course-ai-agents/blob/main/lessons/08_react_practice/notebook.ipynb</summary>

# Repository analysis for https://github.com/towardsai/course-ai-agents/blob/main/lessons/08_react_practice/notebook.ipynb

## Summary
Repository: towardsai/course-ai-agents
File: notebook.ipynb
Lines: 569

Estimated tokens: 5.0k

## File tree
```Directory structure:
└── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/08_react_practice/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 7: ReAct

This Jupyter notebook demonstrates a practical implementation of the ReAct (Reasoning and Acting) framework using Google's Gemini model. It includes three main components: a mock search tool for demonstration, a thought generation phase using structured outputs, and an action phase with function calling capabilities. The notebook implements a complete ReAct control loop that alternates between thinking, acting, and observing, allowing the AI agent to break down complex problems iteratively.
"""

"""
## Setup

First, let's install the necessary Python libraries using pip.
"""

!pip install -q google-genai
# Output:
#   

#   [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m A new release of pip is available: [0m[31;49m24.3.1[0m[39;49m -> [0m[32;49m25.1.1[0m

#   [1m[[0m[34;49mnotice[0m[1;39;49m][0m[39;49m To update, run: [0m[32;49mpip install --upgrade pip[0m


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
#   Trying to load environment variables from `/Users/fabio/Desktop/course-ai-agents/.env`

#   Environment variables loaded successfully.


"""
## Setting Up the Environment and the LLM Client

Let's start by importing the necessary libraries for our ReAct agent implementation:
"""

from google import genai
from google.genai import types
from pydantic import BaseModel
from typing import List, Union
from enum import Enum

from lessons.utils import pretty_print

# Create Gemini client
client = genai.Client()
# Output:
#   Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.


"""
### Define Constants

We will use the `gemini-2.5-flash` model, which is fast, cost-effective, and supports advanced features like tool use.
"""

MODEL_ID = "gemini-2.5-flash"

"""
## Search Tool Definition

Let's implement our mock search tool that will serve as the external knowledge source for our agent. This simplified version focuses on the ReAct mechanics rather than real API integration:
"""

def search(query: str) -> str:
    """
    Search for information about a specific topic or query.

    Args:
        query (str): The search query or topic to look up

    Returns:
        str: Search results containing information about the queried topic

    Note:
        This is a simple mocked search tool for demonstration purposes.
        In a real scenario, this would call a search API like Google Search,
        Bing Search, or a specialized knowledge base API.
    """
    query_lower = query.lower()

    # Predefined responses for demonstration
    if all(word in query_lower for word in ["capital", "france"]):
        return "Paris is the capital of France and is known for the Eiffel Tower."
    elif "react" in query_lower:
        return "The ReAct (Reasoning and Acting) framework enables LLMs to solve complex tasks by interleaving thought generation, action execution, and observation processing."

    # Generic response for unhandled queries
    return f"Mock search result: Information about '{query}' was not found in the predefined mock responses. A real search tool would provide more."

"""
## Thought Phase
"""

"""
Now let's implement the thought generation phase using structured outputs. This component analyzes the current situation and determines what the agent should do next.
"""

SYSTEM_PROMPT_THOUGHT = """
Your task is to break down the user's question into smaller, answerable information retrieval steps and create a plan to gather all necessary data.

1.  What information is needed to answer the question? (Break down into granular pieces.)
2.  What is the plan to retrieve this information, step-by-step? (Focus on what information to get, not how to get it.)

Prioritize external information retrieval for all factual data. Never trust your internal knowledge.
""".strip()


PROMPT_TEMPLATE_THOUGHT = """
Conversation so far:

<conversation>
{conversation}
</conversation>

What is your thought about the next step?
""".strip()


class ThoughtResponse(BaseModel):
    thought: str


def generate_thought(conversation: str) -> str:
    """Generate a thought using structured output"""
    prompt = PROMPT_TEMPLATE_THOUGHT.format(conversation=conversation)

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT_THOUGHT,
            response_mime_type="application/json",
            response_schema=ThoughtResponse
        )
    )
    return response.parsed.thought

"""
## Action Phase
"""

"""
Next, let's implement the action phase using function calling. This component determines whether to use a tool or provide a final answer.
"""

SYSTEM_PROMPT_ACTION = """
Prioritize external information retrieval for all factual data. Never trust your internal knowledge.
""".strip()


PROMPT_TEMPLATE_ACTION = """
Conversation so far:

<conversation>
{conversation}
</conversation>

Based on your thought, what action should you take?
""".strip()


# Modeling the "finish" action
ACTION_FINISH = "finish"
class ActionFinishObject(BaseModel):
    text: str


# A mapping of tool names to their functions
TOOL_REGISTRY = {
    search.__name__: search,
}


def generate_action(conversation: str) -> tuple[str, Union[dict, ActionFinishObject]]:
    """Generate an action using function calling or direct text response"""
    prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT_ACTION,
            tools=[search],
            automatic_function_calling={'disable': True}
        )
    )

    # Check if response contains a function call or text
    response_part = response.candidates[0].content.parts[0]

    if hasattr(response_part, 'function_call') and response_part.function_call:
        function_call = response_part.function_call
        action_name = function_call.name
        action_params = dict(function_call.args)
        return action_name, action_params
    else:
        # It's a text response (final answer)
        return ACTION_FINISH, ActionFinishObject(text=response.text)

"""
## ReAct Control Loop
"""

"""
Now let's create the main ReAct control loop that orchestrates the thought-action-observation cycle. Let's model each step of the ReAct loop first.
"""

class MessageRole(str, Enum):
    """Enumeration for the different roles a message can have."""
    USER = "user"
    THOUGHT = "thought"
    TOOL_REQUEST = "tool request"
    OBSERVATION = "observation"
    FINAL_ANSWER = "final answer"


class Message(BaseModel):
    """A message with a role and content, used for all message types."""
    role: MessageRole
    content: str

    def __str__(self) -> str:
        """Provides a user-friendly string representation of the message."""
        return f"{self.role.value.capitalize()}: {self.content}"

"""
Then, let's prepare a function that generates the final answer in case that the ReAct loops has reached its maximum number of iterations.
"""

PROMPT_TEMPLATE_FINAL_ANSWER = """
<conversation>
{conversation}
</conversation>

Given the conversation above, write a final answer to the original question.
""".strip()


def generate_final_answer(conversation: str) -> str:
    prompt = PROMPT_TEMPLATE_FINAL_ANSWER.format(conversation=conversation)
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    return response.text

"""
We'll manage a list of messages, where each message is a ReAct step, in a variable called `scratchpad` (as it was called this way originally in the ReAct paper). The following helper function converts this list of messages to a string representation that we can use in the prompts.
"""

def format_scratchpad_for_llm(scratchpad: List[Message]) -> str:
    """Formats the scratchpad content into a string for the LLM."""
    conversation = "\n".join([str(message) for message in scratchpad])
    return conversation

"""
Here we define another helper function that leverages our `pretty_print` module to show each step of the ReAct loop in a beautiful and colored way.
"""

def pretty_print_message(message: Message, turn: int, max_turns: int, header_color: str = pretty_print.Color.YELLOW, is_forced_final_answer: bool = False) -> None:
    if not is_forced_final_answer:
        title = f"{message.role.value.capitalize()} (Turn {turn}/{max_turns}):"
    else:
        title = f"{message.role.value.capitalize()} (Forced):"

    pretty_print.wrapped(
        text=message.content,
        title=title,
        header_color=header_color,
    )

"""
We can now implement the ReAct loop.
"""

def react_agent_loop(initial_question: str, max_turns: int = 5, verbose: bool = False) -> str:
    """
    Implements the main ReAct (Thought -> Action -> Observation) control loop.
    Uses a unified message class for the scratchpad.
    """
    # The scratchpad stores the history of messages.
    scratchpad: List[Message] = []

    for turn in range(1, max_turns + 1):
        # If it's the first turn, add the user's question to the scratchpad
        if not scratchpad:
            user_message = Message(role=MessageRole.USER, content=initial_question)
            scratchpad.append(user_message)
            if verbose:
                pretty_print_message(user_message, turn, max_turns, pretty_print.Color.RESET)

        # Generate a thought based on the current scratchpad
        thought_content = generate_thought(format_scratchpad_for_llm(scratchpad))
        thought_message = Message(role=MessageRole.THOUGHT, content=thought_content)
        scratchpad.append(thought_message)
        if verbose:
            pretty_print_message(thought_message, turn, max_turns, pretty_print.Color.ORANGE)

        # Generate an action based on the current scratchpad
        action_name, action_params = generate_action(format_scratchpad_for_llm(scratchpad))

        # Handle the finish action
        if action_name == ACTION_FINISH:
            final_answer = action_params.text
            final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
            scratchpad.append(final_message)
            if verbose:
                pretty_print_message(final_message, turn, max_turns, pretty_print.Color.CYAN)
            return final_answer

        # Handle a tool request action
        params_str = ", ".join([f"{k}='{v}'" for k, v in action_params.items()])
        action_content = f"{action_name}({params_str})"
        action_message = Message(role=MessageRole.TOOL_REQUEST, content=action_content)
        scratchpad.append(action_message)
        if verbose:
            pretty_print_message(action_message, turn, max_turns, pretty_print.Color.GREEN)

        # Run the action and get the observation
        observation_content = ""
        if action_name in TOOL_REGISTRY:
            tool_function = TOOL_REGISTRY[action_name]
            try:
                # Use ** to unpack the dictionary of parameters into function arguments
                observation_content = tool_function(**action_params)
            except Exception as e:
                observation_content = f"Error executing tool '{action_name}': {e}"
        else:
            available_tools_str = ", ".join(TOOL_REGISTRY.keys())
            observation_content = f"Error - Unknown action '{action_name}'. Available tools are [{available_tools_str}]."

        # Add the observation to the scratchpad
        observation_message = Message(role=MessageRole.OBSERVATION, content=observation_content)
        scratchpad.append(observation_message)
        if verbose:
            pretty_print_message(observation_message, turn, max_turns, pretty_print.Color.YELLOW)


        # Check if the maximum number of turns has been reached. If so, force generating a final answer
        if turn == max_turns:
            final_answer = generate_final_answer(format_scratchpad_for_llm(scratchpad))
            final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
            scratchpad.append(final_message)
            if verbose:
                pretty_print_message(final_message, turn, max_turns, pretty_print.Color.CYAN, is_forced_final_answer=True)
            return final_answer

"""
Let's test our ReAct agent with a simple factual question that requires a search:
"""

# A straightforward question requiring a search.
question = "What is the capital of France?"
final_answer = react_agent_loop(question, max_turns=2, verbose=True)
# Output:
#   [0m----------------------------------------- User (Turn 1/2): -----------------------------------------[0m

#     What is the capital of France?

#   [0m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 1/2): ---------------------------------------[0m

#     The user is asking a factual question about the capital of France. The next step is to retrieve this specific piece of information.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------- Tool request (Turn 1/2): -------------------------------------[0m

#     search(query='capital of France')

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------- Observation (Turn 1/2): -------------------------------------[0m

#     Paris is the capital of France and is known for the Eiffel Tower.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 2/2): ---------------------------------------[0m

#     The user asked for the capital of France. The previous tool call successfully identified "Paris" as the capital. The next step is to output this answer to the user.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [96m------------------------------------- Final answer (Turn 2/2): -------------------------------------[0m

#     Paris is the capital of France.

#   [96m----------------------------------------------------------------------------------------------------[0m


"""
Now let's test with a more complex conceptual question that our mock search tool has knowledge about:
"""

# A question about a concept the mock search tool might know.
question = "Can you explain the ReAct framework in AI?"
final_answer = react_agent_loop(question, max_turns=2, verbose=True)
# Output:
#   [0m----------------------------------------- User (Turn 1/2): -----------------------------------------[0m

#     Can you explain the ReAct framework in AI?

#   [0m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 1/2): ---------------------------------------[0m

#     The user is asking for an explanation of the ReAct framework in AI. This requires retrieving factual information about the framework. I need to gather details such as its full name, core concept, how it operates (the iterative process), its advantages, and typical use cases. I will prioritize external information retrieval for all these details.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------- Tool request (Turn 1/2): -------------------------------------[0m

#     search(query='ReAct framework AI')

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------- Observation (Turn 1/2): -------------------------------------[0m

#     The ReAct (Reasoning and Acting) framework enables LLMs to solve complex tasks by interleaving thought generation, action execution, and observation processing.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 2/2): ---------------------------------------[0m

#     The user wants a detailed explanation of the ReAct framework. I have a high-level definition from the previous search result. I need to expand on the core mechanism (how 'thought', 'action', and 'observation' interleave), the specific steps involved in its operation, its key advantages, and typical use cases. I will perform further searches to gather these details.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------- Tool request (Turn 2/2): -------------------------------------[0m

#     search(query='ReAct framework mechanism thought action observation')

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------- Observation (Turn 2/2): -------------------------------------[0m

#     The ReAct (Reasoning and Acting) framework enables LLMs to solve complex tasks by interleaving thought generation, action execution, and observation processing.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [96m-------------------------------------- Final answer (Forced): --------------------------------------[0m

#     The ReAct (Reasoning and Acting) framework is an AI methodology that enables Large Language Models (LLMs) to solve complex tasks by interleaving **thought generation**, **action execution**, and **observation processing**.

#   

#   Here's how it works:

#   

#   1.  **Thought:** The LLM first generates an internal "thought" to decide the next step. This thought is a natural language explanation of its reasoning, what it intends to do, or what information it needs.

#   2.  **Action:** Based on the thought, the LLM then specifies an "action" to be taken. This action typically involves using external tools (like search engines, calculators, code interpreters, or APIs) to gather information or interact with the environment.

#   3.  **Observation:** After the action is executed, the LLM receives an "observation" – the result or output from the tool or environment.

#   

#   This cycle of Thought-Action-Observation repeats iteratively. The LLM uses the new observation to refine its understanding, correct mistakes, and plan the next thought and action, continually progressing towards solving the original task.

#   

#   **Key advantages of ReAct:**

#   

#   *   **Improved Reasoning:** By explicitly articulating its thoughts, the LLM can engage in more deliberate, step-by-step reasoning, making its problem-solving process more transparent and robust.

#   *   **Tool Use:** It seamlessly integrates external tools, allowing LLMs to access real-time information, perform calculations, or interact with systems beyond their pre-trained knowledge.

#   *   **Error Correction:** The iterative process allows the LLM to identify and correct errors by observing the results of its actions and adjusting its subsequent steps.

#   *   **Handling Complexity:** It breaks down complex problems into smaller, manageable steps, making it effective for tasks that require multiple stages of reasoning and interaction.

#   

#   **Typical Use Cases:**

#   

#   *   **Complex Question Answering:** Answering questions that require looking up information, performing calculations, and synthesizing data.

#   *   **Interactive Problem Solving:** Tasks that involve interacting with APIs, databases, or web services to achieve a goal.

#   *   **Code Generation and Debugging:** Where the LLM might write code (action), run it (observation), and then debug based on errors.

#   *   **Data Analysis:** Using tools to retrieve, process, and analyze data to draw conclusions.

#   [96m----------------------------------------------------------------------------------------------------[0m


"""
Last, let's test with a question that our mock search tool doesn't have knowledge about:
"""

# A question about a concept the mock search tool doesn't know.
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, max_turns=2, verbose=True)
# Output:
#   [0m----------------------------------------- User (Turn 1/2): -----------------------------------------[0m

#     What is the capital of Italy?

#   [0m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 1/2): ---------------------------------------[0m

#     The user is asking a factual question about the capital of Italy. The next step is to retrieve this specific piece of information. The information needed is the name of Italy's capital city. The plan is to perform a targeted search query like 'capital of Italy' and extract the answer from reliable sources.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------- Tool request (Turn 1/2): -------------------------------------[0m

#     search(query='capital of Italy')

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------- Observation (Turn 1/2): -------------------------------------[0m

#     Mock search result: Information about 'capital of Italy' was not found in the predefined mock responses. A real search tool would provide more.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 2/2): ---------------------------------------[0m

#     The previous attempt to find the capital of Italy failed as the mock search did not provide a result. The information needed is still the capital city of Italy. The plan is to retry the search query 'capital of Italy' to obtain this specific factual information.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------- Tool request (Turn 2/2): -------------------------------------[0m

#     search(query='capital of Italy')

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------- Observation (Turn 2/2): -------------------------------------[0m

#     Mock search result: Information about 'capital of Italy' was not found in the predefined mock responses. A real search tool would provide more.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [96m-------------------------------------- Final answer (Forced): --------------------------------------[0m

#     I apologize, but I was unable to find the capital of Italy using my current tools.

#   [96m----------------------------------------------------------------------------------------------------[0m

</details>


## YouTube Video Transcripts

_No YouTube video transcripts found._


## Local Files

_No local files found._


## Additional Sources Scraped

<details>
<summary>arxiv-org</summary>

# ABSTRACT

While large language models (LLMs) have demonstrated impressive performance across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines in addition to improved human interpretability and trustworthiness. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes prevalent issues of hallucination and error propagation in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generating human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. Furthermore, on two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of $34 %$ and $10 %$ respectively, while being prompted with only one or two in-context examples.

# 1 INTRODUCTION

A unique feature of human intelligence is the ability to seamlessly combine task-oriented actions with verbal reasoning (or inner speech, Alderson-Day & Fernyhough, 2015), which has been theorized to play an important role in human cognition for enabling self-regulation or strategization (Vygotsky, 1987; Luria, 1965; Fernyhough, 2010) and maintaining a working memory (Baddeley, 1992). Consider the example of cooking up a dish in the kitchen. Between any two specific actions, we may reason in language in order to track progress (“now that everything is cut, I should heat up the pot of water”), to handle exceptions or adjust the plan according to the situation (“I don’t have salt, so let me use soy sauce and pepper instead”), and to realize when external information is needed (“how do I prepare dough? Let me search on the Internet”). We may also act (open a cookbook to read the recipe, open the fridge, check ingredients) to support the reasoning and to answer questions (“What dish can I make right now?”). This tight synergy between “acting” and “reasoning” allows humans to learn new tasks quickly and perform robust decision making or reasoning, even under previously unseen circumstances or facing information uncertainties.

Recent results have hinted at the possibility of combining verbal reasoning with interactive decision making in autonomous systems. On one hand, properly prompted large language models (LLMs) have demonstrated emergent capabilities to carry out several steps of reasoning traces to derive answers from questions in arithmetic, commonsense, and symbolic reasoning tasks (Wei et al., 2022). However, this “chain-of-thought” reasoning is a static black box, in that the model uses its own internal representations to generate thoughts and is not grounded in the external world, which limits its ability to reason reactively or update its knowledge. This can lead to issues like fact hallucination and error propagation over the reasoning process (Figure 1 (1b)). On the other hand, recent work has explored the use of pre-trained language models for planning and acting in interactive environments (Ahn et al., 2022; Nakano et al., 2021; Yao et al., 2020; Huang et al., 2022a), with a focus on predicting actions via language priors. These approaches usually convert multi-modal observations into text, use a language model to generate domain-specific actions or plans, and then use a controller to choose or execute them. However, they do not employ language models to reason abstractly about high-level goals or maintain a working memory to support acting, barring Huang et al. (2022b) who perform a limited form of verbal reasoning to reiterate spatial facts about the current state. Beyond such simple embodied tasks to interact with a few blocks, there have not been studies on how reasoning and acting can be combined in a synergistic manner for general task solving, and if such a combination can bring systematic benefits compared to reasoning or acting alone.

https://arxiv.org/pdf/images/dd0e9f64b42d2cab71cdcecddd80ea2cf5aa212b5bf9a21882834d8e50a5302d.jpg

Figure 1: (1) Comparison of 4 prompting methods, (a) Standard, (b) Chain-of-thought (CoT, Reason Only), (c) Act-only, and (d) ReAct (Reason+Act), solving a HotpotQA (Yang et al., 2018) question. (2) Comparison of (a) Act-only and (b) ReAct prompting to solve an AlfWorld (Shridhar et al., 2020b) game. In both domains, we omit in-context examples in the prompt, and only show task solving trajectories generated by the model (Act, Thought) and the environment (Obs).

In this work, we present ReAct, a general paradigm to combine reasoning and acting with language models for solving diverse language reasoning and decision making tasks (Figure 1). ReAct prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an interleaved manner, which allows the model to perform dynamic reasoning to create, maintain, and adjust high-level plans for acting (reason to act), while also interact with the external environments (e.g. Wikipedia) to incorporate additional information into reasoning (act to reason).

We conduct empirical evaluations of ReAct and state-of-the-art baselines on four diverse benchmarks: question answering (HotPotQA, Yang et al., 2018), fact verification (Fever, Thorne et al., 2018), text-based game (ALFWorld, Shridhar et al., 2020b), and webpage navigation (WebShop, Yao et al., 2022). For HotPotQA and Fever, with access to a Wikipedia API that the model can interact with, ReAct outperforms vanilla action generation models while being competitive with chain-ofthought reasoning (CoT) (Wei et al., 2022). The best approach overall is a combination of ReAct and CoT that allows for the use of both internal knowledge and externally obtained information during reasoning. On ALFWorld and WebShop, two or even one-shot ReAct prompting is able to outperform imitation or reinforcement learning methods trained with $1 0 ^ { 3 } \sim \mathrm { { \bar { 1 0 } } ^ { 5 } }$ task instances, with an absolute improvement of $34 %$ and $10 %$ in success rates respectively. We also demonstrate the importance of sparse, versatile reasoning in decision making by showing consistent advantages over controlled baselines with actions only. Besides general applicability and performance boost, the combination of reasoning and acting also contributes to model interpretability, trustworthiness, and diagnosability across all domains, as humans can readily distinguish information from model’s internal knowledge versus external environments, as well as inspect reasoning traces to understand the decision basis of model actions.

To summarize, our key contributions are the following: (1) we introduce ReAct, a novel promptbased paradigm to synergize reasoning and acting in language models for general task solving; (2) we perform extensive experiments across diverse benchmarks to showcase the advantage of ReAct in a few-shot learning setup over prior approaches that perform either reasoning or action generation in isolation; (3) we present systematic ablations and analysis to understand the importance of acting in reasoning tasks, and reasoning in interactive tasks; (4) we analyze the limitations of ReAct under the prompting setup (i.e. limited support of reasoning and acting behaviors), and perform initial finetuning experiments showing the potential of ReAct to improve with additional training data. Scaling up ReAct to train and operate on more tasks and combining it with complementary paradigms like reinforcement learning could further unlock the potential of large language models.

# 2 REACT: SYNERGIZING REASONING + ACTING

Consider a general setup of an agent interacting with an environment for task solving. At time step $t$ , an agent receives an observation $o _ { t } \in \mathcal { O }$ from the environment and takes an action $a _ { t } \in \mathcal A$ following some policy $\pi ( \boldsymbol { a } _ { t } \| \boldsymbol { c } _ { t } )$ , where $c _ { t } = \left( o _ { 1 } , a _ { 1 } , \cdot \cdot \cdot , o _ { t - 1 } , a _ { t - 1 } , o _ { t } \right)$ is the context to the agent. Learning a policy is challenging when the mapping $c _ { t } \mapsto a _ { t }$ is highly implicit and requires extensive computation. For example, the agent shown in Figure 1(1c) is unable to generate the correct final action (Act 4) to finish the QA task as it requires complex reasoning over the trajectory context (Question, Act 1-3, Obs 1-3). Similarly, the agent shown in Figure 1(2a) fails to comprehend from the context that sinkbasin 1 does not contain peppershaker 1, thus keep producing hallucinating actions.

The idea of ReAct is simple: we augment the agent’s action space to ${ \hat { \mathcal { A } } } = { \mathcal { A } } \cup { \mathcal { L } }$ , where $\mathcal { L }$ is the space of language. An action $\hat { a } _ { t } \in \mathcal { L }$ in the language space, which we will refer to as a thought or a reasoning trace, does not affect the external environment, thus leading to no observation feedback. Instead, a thought $\hat { a } _ { t }$ aims to compose useful information by reasoning over the current context $c _ { t }$ , and update the context $\boldsymbol c _ { t + 1 } = \left( c _ { t } , \hat { a } _ { t } \right)$ to support future reasoning or acting. As shown in Figure 1, there could be various types of useful thoughts, e.g. decomposing task goals and create action plans (2b, Act 1; 1d, Thought 1), injecting commonsense knowledge relevant to task solving (2b, Act 1), extracting important parts from observations (1d, Thought2, 4), track progress and transit action plans (2b, Act 8), handle exceptions and adjust action plans (1d, Thought 3), and so on.

However, as the language space $\mathcal { L }$ is unlimited, learning in this augmented action space is difficult and requires strong language priors. In this paper, we mainly focus on the setup where a frozen large language model, PaLM-540B (Chowdhery et al., 2022)1, is prompted with few-shot in-context examples to generate both domain-specific actions and free-form language thoughts for task solving (Figure 1 (1d), (2b)). Each in-context example is a human trajectory of actions, thoughts, and environment observations to solve a task instance (see Appendix C). For the tasks where reasoning is of primary importance (Figure 1(1)), we alternate the generation of thoughts and actions so that the task-solving trajectory consists of multiple thought-action-observation steps. In contrast, for decision making tasks that potentially involve a large number of actions (Figure 1(2)), thoughts only need to appear sparsely in the most relevant positions of a trajectory, so we let the language model decide the asynchronous occurrence of thoughts and actions for itself.

Since decision making and reasoning capabilities are integrated into a large language model, ReAct enjoys several unique features: A) Intuitive and easy to design: Designing ReAct prompts is straightforward as human annotators just type down their thoughts in language on top of their actions taken. No ad-hoc format choice, thought design, or example selection is used in this paper. We detail prompt design for each task in Sections 3 and 4. B) General and flexible: Due to the flexible thought space and thought-action occurrence format, ReAct works for diverse tasks with distinct action spaces and reasoning needs, including but not limited to QA, fact verification, text game, and web navigation. C) Performant and robust: ReAct shows strong generalization to new task instances while learning solely from one to six in-context examples, consistently outperforming baselines with only reasoning or acting across different domains. We also show in Section 3 additional benefits when finetuning is enabled, and in Section 4 how ReAct performance is robust to prompt selections. D) Human aligned and controllable: ReAct promises an interpretable sequential decision making and reasoning process where humans can easily inspect reasoning and factual correctness. Moreover, humans can also control or correct the agent behavior on the go by thought editing, as shown in Figure 5 in Section 4.

# 3 KNOWLEDGE-INTENSIVE REASONING TASKS

We begin with knowledge-intensive reasoning tasks like multi-hop question answering and fact verification. As shown in Figure 1(1d), by interacting with a Wikipedia API, ReAct is able to retrieve information to support reasoning, while also use reasoning to target what to retrieve next, demonstrating a synergy of reasoning and acting.

# 3.1 SETUP

Domains We consider two datasets challenging knowledge retrieval and reasoning: (1) HotPotQA (Yang et al., 2018), a multi-hop question answering benchmark that requires reasoning over two or more Wikipedia passages, and (2) FEVER (Thorne et al., 2018), a fact verification benchmark where each claim is annotated SUPPORTS, REFUTES, or NOT ENOUGH INFO, based on if there exists a Wikipedia passage to verify the claim. In this work, we operate in a question-only setup for both tasks, where models only receive the question/claim as input without access to support paragraphs, and have to rely on their internal knowledge or retrieve knowledge via interacting with an external environment to support reasoning.

Action Space We design a simple Wikipedia web API with three types of actions to support interactive information retrieval: (1) search[entity], which returns the first 5 sentences from the corresponding entity wiki page if it exists, or else suggests top-5 similar entities from the Wikipedia search engine, (2) lookup[string], which would return the next sentence in the page containing string, simulating $\mathrm { C t r l + F }$ functionality on the browser. (3) finish[answer], which would finish the current task with answer. We note that this action space mostly can only retrieve a small part of a passage based on exact passage name, which is significantly weaker than state-of-theart lexical or neural retrievers. The purpose is to simulate how humans would interact with Wikipedia, and force models to retrieve via explicit reasoning in language.

# 3.2 METHODS

ReAct Prompting For HotpotQA and Fever, we randomly select 6 and 3 cases2 from the training set and manually compose ReAct-format trajectories to use as few-shot exemplars in the prompts. Similar to Figure 1(d), each trajectory consists of multiple thought-action-observation steps (i.e. dense thought), where free-form thoughts are used for various purposes. Specifically, we use a combination of thoughts that decompose questions (“I need to search x, find y, then find $\boldsymbol { z } ^ { \flat }$ ), extract information from Wikipedia observations $\mathbf { \epsilon } ^ { * } \mathbf { \epsilon } _ { \mathbf { X } }$ was started in $1 8 4 4 ^ { , 9 }$ , “The paragraph does not tell x”), perform commonsense ( ${ } ^ { ** } \mathbf { X }$ is not y, so z must instead be...”) or arithmetic reasoning $^ { \cdot \cdot } 1 8 4 4 < 1 9 8 9 ^ { , 3 } ,$ ), guide search reformulation (“maybe I can search/look up x instead”), and synthesize the final answer (“...so the answer is x”).

# 3.3 RESULTS AND OBSERVATIONS

ReAct outperforms Act consistently Table 1 shows HotpotQA and Fever results using PaLM540B as the base model with different prompting methods. We note that ReAct is better than Act on both tasks, demonstrating the value of reasoning to guide acting, especially for synthesizing the final answer, as shown in Figure 1 (1c-d). Fine-tuning results 3 also confirm the benefit of reasoning traces for more informed acting.

ReAct vs. CoT On the other hand, ReAct outperforms CoT on Fever (60.9 vs. 56.3) and slightly lags behind CoT on HotpotQA (27.4 vs. 29.4). Fever claims for SUPPORTS/REFUTES might only differ by a slight amount (see Appendix D.1), so acting to retrieve accurate and up-to-date knowledge is vital. To better understand the behavioral difference between ReAct and CoT on HotpotQA, we randomly sampled 50 trajectories with correct and incorrect answers (judged by EM) from ReAct and CoT respectively (thus 200 examples in total), and manually labeled their success and failure modes in Table 2.

A) Hallucination is a serious problem for CoT, resulting in much higher false positive rate than ReAct $14 %$ vs. $6 %$ ) in success mode, and make up its major failure mode $( 5 6 % )$ . In contrast, the problem solving trajectory of $\scriptstyle { \mathrm { R e A c t } }$ is more grounded, fact-driven, and trustworthy, thanks to the access of an external knowledge base.

B) While interleaving reasoning, action and observation steps improves ReAct’s groundedness and trustworthiness, such a structural constraint also reduces its flexibility in formulating reasoning steps, leading to more reasoning error rate than CoT. we note that there is one frequent error pattern specific to ReAct, in which the model repetitively generates the previous thoughts and actions, and we categorize it as part of “reasoning error” as the model fails to reason about what the proper next action to take and jump out of the $\mathrm { l o o p ^ { 4 } }$ .

C) For ReAct, successfully retrieving informative knowledge via search is critical. Noninformative search, which counts for $23 %$ of the error cases, derails the model reasoning and gives it a hard time to recover and reformulate thoughts. This is perhaps an expected trade-off between factuality and flexibility, which motivates our proposed strategies of combining two methods.

We provide examples for each success and failure modes in Appendix E.1. We also find some HotpotQA questions may contain outdated answer labels, see Figure 4 for example.

ReAct $^ +$ CoT-SC perform best for prompting LLMs The best prompting method on HotpotQA and Fever are $\mathtt { R e A c t } \to \mathtt { C o T } \mathrm { - } \mathrm { S C }$ and $\mathtt { C o T - S C } \to \mathtt { R e A c t }$ respectively. Furthermore, Figure 2 shows how different methods perform with respect to the number of $\mathrm { C o T - S C }$ samples used.

ReAct performs best for fine-tuning Figure 3 shows the scaling effect of prompting/finetuning four methods (Standard, CoT, Act, ReAct) on HotpotQA. With PaLM-8/62B, prompting ReAct performs worst among four methods due to the difficulty to learn both reasoning and acting from in-context examples. However, when finetuned with just 3,000 examples, ReAct becomes the best method among the four, with PaLM-8B finetuned ReAct outperforming all PaLM-62B prompting methods, and PaLM-62B finetuned ReAct outperforming all 540B prompting methods.

# 4 DECISION MAKING TASKS

We also test ReAct on two language-based interactive decision-making tasks, ALFWorld and WebShop, both of which feature complex environments that require agents to act over long horizons with sparse rewards, warranting the need for reasoning to act and explore effectively.

ALFWorld ALFWorld (Shridhar et al., 2020b) (Figure 1(2)) is a synthetic text-based game designed to align with the embodied ALFRED benchmark (Shridhar et al., 2020a). It includes 6 types of tasks in which an agent needs to achieve a high-level goal (e.g. examine paper under desklamp) by navigating and interacting with a simulated household via text actions (e.g. go to coffeetable 1, take paper 2, use desklamp 1). A task instance can have more than 50 locations and take an expert policy more than 50 steps to solve, thus challenging an agent to plan and track subgoals, as well as explore systematically (e.g. check all desks one by one for desklamp). In particular, one challenge built into ALFWorld is the need to determine likely locations for common household items (e.g. desklamps will likely be on desks, shelfs, or dressers), making this environment a good fit for LLMs to exploit their pretrained commonsense knowledge.

WebShop Can ReAct also interact with noisy real-world language environments for practical applications? We investigate WebShop (Yao et al., 2022), a recently proposed online shopping website environment with 1.18M real-world products and $1 2 \mathrm { k }$ human instructions. Unlike ALFWorld, Webshop contains a high variety of structured and unstructured texts (e.g. product titles, descriptions, and options crawled from Amazon), and requires an agent to purchase a product based on a user instruction (e.g. “I am looking for a nightstand with drawers. It should have a nickel finish, and priced lower than $$ 140$ ) through web interactions (e.g. search “nightstand drawers”, choose buttons such as “color: modern-nickel-white” or “back to search”).

Results ReAct outperforms Act on both ALFWorld (Table 3) and Webshop (Table 4). On ALFWorld, the best ReAct trial achieves an average success rate of $71 %$ , significantly outperforming the best Act $( 4 5 % )$ and BUTLER $( 3 7 % )$ trials. Moreover, the advantage of $\scriptstyle { \mathrm { R e a c t } }$ over Act is consistent across six controlled trials, with relative performance gain ranging from $33 %$ to $90 %$ and averaging $62 %$ . Qualitatively, we saw that, without any thoughts at all, Act fails to correctly decompose goals into smaller subgoals, or loses track of the current state of the environment.

On Webshop, one-shot Act prompting already performs on par with IL and $\scriptstyle \mathrm { I L + R L }$ methods. With additional sparse reasoning, ReAct achieves significantly better performance, with an absolute $10 %$ improvement over the previous best success rate.

On the value of internal reasoning vs. external feedback To our knowledge, ReAct is the first demonstration of combined reasoning and action using an LLM applied to an interactive environment within a closed-loop system. Perhaps the closest prior work is Inner Monologue (IM), from Huang et al. (2022b), in which actions from an embodied agent are motivated by an eponymous “inner monologue”. However, IM’s “inner monologue” is limited to observations of the environment state and what needs to be completed by the agent for the goal to be satisfied. In contrast, the reasoning traces in ReAct for decision making is flexible and sparse, allowing diverse reasoning types (see Section 2) to be induced for different tasks.

To demonstrate the differences between ReAct and IM, and to highlight the importance of internal reasoning vs. simple reactions to external feedback, we ran an ablation experiment using a thought pattern composed of IM-like dense external feedback. As can be seen in Table 3, ReAct substantially outperforms IM-style prompting (ReAct-IM) (71 vs. 53 overall success rate), with consistent advantages on five out of six tasks.

# C PROMPTS

## Hotpot QA Prompts

Original Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?  
Answer: 1,800 to 7,000 ft

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?  
Answer: Richard Nixon

Question Answer: Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture?  
Question: The Saimaa Gesture What profession does Nicholas Ray and Elia Kazan have in common?  
Answer: director, screenwriter, actor

Question Answer: Which magazine was started first Arthur's Magazine or First for Women? Arthur's Magazine  
Question: Were Pavel Urysohn and Leonid Levin known for the same type of work?  
Answer Act: Yes

**Example ReAct reasoning:**

Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
- Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area.
- Action 1: Search[Colorado orogeny]
- Observation: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas.
- Thought 2: It does not mention the eastern sector. So I need to look up eastern sector.
- Action 2: Lookup[eastern sector]
- Observation 2: (Result 1 / 1) The eastern sector extends into the High Plains and is called the Central Plains orogeny.
- Thought 3: The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range.
- Action 3: Search[High Plains]
- [Intermediate steps...]
- Thought 4: High Plains refers to one of two distinct land regions. I need to instead search High Plains (United States).
- Action 4: Search[High Plains (United States)]
- Observation 4: High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).
- Action 5: Finish[1,800 to 7,000 ft]

---

Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
- Thought 1: I need to search Milhouse, find out who he was named after.
- Action 1: Search[Milhouse]
- Observation: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons...
- Thought 2: The paragraph does not tell who Milhouse is named after; maybe I can look up "named after".
- Action 2: Lookup[named after]
- Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous.
- Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
- Action 3: Finish[Richard Nixon]

---

Question: Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture?
- Thought 1: I need to search Adam Clayton Powell and The Saimaa Gesture, and find which documentary is about Finnish rock groups.
- Action 1: Search[Adam Clayton Powell]
- Observation 1: Could not find [Adam Clayton Powell]. Similar: ['Adam Clayton Powell III', ...]
- Thought 2: To find the documentary, I can search Adam Clayton Powell (film).
- Action 2: Search[Adam Clayton Powell (film)]
- Observation 2: Adam Clayton Powell is a 1989 American documentary film...
- Thought 3: Adam Clayton Powell (film) is a documentary about an African-American politician, not Finnish rock groups. So the documentary about Finnish rock groups must instead be The Saimaa Gesture.
- Action 3: Finish[The Saimaa Gesture]

---

Question: What profession does Nicholas Ray and Elia Kazan have in common?
- Thought 1: I need to search Nicholas Ray and Elia Kazan, find their professions, then find the profession they have in common.
- Action 1: Search[Nicholas Ray]
- Observation 1: Nicholas Ray (born Raymond Nicholas Kienzle Jr., August 7, 1911 - June 16, 1979) was an American film director, screenwriter, and actor...
- Thought 2: Professions of Nicholas Ray are director, screenwriter, and actor.
- Action 2: I need to search Elia Kazan next and find his professions. Search[Elia Kazan]
- Observation 2: Elia Kazan was an American film and theatre director, producer, screenwriter and actor.
- Thought 3: Professions of Elia Kazan are director, producer, screenwriter, and actor. So profession Nicholas Ray and Elia Kazan have in common is director, screenwriter, and actor.
- Action 3: Finish[director, screenwriter, actor]

---

Question: Which magazine was started first Arthur's Magazine or First for Women?
- Thought 1: I need to search Arthur's Magazine and First for Women, and find which was started first.
- Action 1: Search[Arthur's Magazine]
- Observation 1: Arthur's Magazine (1844-1846) was an American literary periodical published in Philadelphia in the 19th century
- Thought 2: Arthur's Magazine was started in 1844. I need to search First for Women next.
- Action 2: Search[First for Women]
- Observation 2: First for Women is a woman's magazine published by Bauer Media Group in the USA. The magazine was started in 1989.
- Thought 3: First for Women was started in 1989. 1844 (Arthur's Magazine) < 1989 (First for Women), so Arthur's Magazine was started first.
- Action 3: Finish[Arthur's Magazine]

---

Question: Were Pavel Urysohn and Leonid Levin known for the same type of work?
- Thought 1: I need to search Pavel Urysohn and Leonid Levin, find their types of work, then find if they are the same.
- Action 1: Search[Pavel Urysohn]
- Observation 1: Pavel Samuilovich Urysohn (February 3, 1898 - August 17, 1924) was a Soviet mathematician...
- Thought 2: Pavel Urysohn is a mathematician. I need to search Leonid Levin next and find its type of work.
- Action 2: Search[Leonid Levin]
- Observation 2: Leonid Anatolievich Levin is a Soviet-American mathematician and computer scientist.
- Thought 3: Leonid Levin is a mathematician and computer scientist. So Pavel Urysohn and Leonid Levin have the same type of work.
- Action 3: Finish[yes]

---

## FEVER Prompts

Claim: Nikolaj Coster-Waldau worked with the Fox Broadcasting Company.
- Thought 1: I need to search Nikolaj Coster-Waldau and find if he has worked with the Fox Broadcasting Company.
- Action 1: Search[Nikolaj Coster-Waldau]
- Observation 1: Nikolaj William Coster-Waldau ... played a detective in the short-lived Fox television series New Amsterdam (2008), and appeared in the 2009 Fox television film Virtuality, originally intended as a pilot.
- Thought 2: Because he "appeared in the 2009 Fox television film Virtuality," he should have worked with the Fox Broadcasting Company.
- Action 2: Finish[SUPPORTS]

Claim: Stranger Things is set in Bloomington, Indiana.
- Thought 1: I should search for Stranger Things, and see if it is set in Bloomington, Indiana.
- Action 1: Search[Stranger Things]
- Observation 1: Stranger Things is ... Set in the 1980s, primarily in the fictional town of Hawkins, Indiana...
- Thought 2: The observation says that it is set in a "fictional town of Hawkins, Indiana", so it is not set in Bloomington.
- Action 2: Finish[REFUTES]

Claim: Beautiful reached number two on the Billboard Hot 100 in 2003.
- Thought 1: I need to search the song Beautiful and find if it reached number two on the Billboard Hot 100 in 2003.
- Action 1: Search[Beautiful]
- Observation 1: Could not find [Beautiful]. Similar: ['Beautiful', 'Beautiful, Beautiful', ... 'Beautiful (Christina Aguilera song)', ...]
- Thought 2: From suggestions, I should search "Beautiful (Christina Aguilera song)" to find the song.
- Action 2: Search[Beautiful (Christina Aguilera song)]
- Observation 2: "Beautiful" is a song recorded by American singer Christina Aguilera for her fourth studio album, Stripped (2002).
- Thought 3: It does not mention Billboard, so I need to look up "Billboard Hot 100" to find if it reached number two on it in 2003.
- Action 3: Lookup[Billboard Hot 100]
- Observation 3: (Result 1 / 3) The song peaked at number two on the Billboard Hot 100 in the United States, where it was certified Gold for 500,000 units shipped.
- Thought 4: It only says the song peaked at number two on the Billboard Hot 100, but not if it was in 2003. I am not sure if this claim is true or not.
- Action 4: Finish[NOT ENOUGH INFO]

---

## ALFWorld Prompts

You are in the middle of a room. Looking quickly around you, you see a cabinet 13, a cabinet 12, ..., a sinkbasin 1, a stoveburner 4, ..., a toaster 1. Your task is to: put a clean lettuce in diningtable.

> think: To solve the task, I need to find and take a lettuce, then clean it with sinkbasin, then put it in diningtable.

OK.

> think: First I need to find a lettuce. A lettuce is more likely to appear in fridge (1), diningtable (1), sinkbasin (1), stoveburner (1-3), cabinet (1-13). I can check one by one, starting with fridge 1.

OK.

> go to fridge 1

> The fridge 1 is closed.

> open fridge 1

> You open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a potato 3, and a potato 2.

> go to diningtable 1

> On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.

> think: Now I find a lettuce (1). Next, I need to take it.

OK.

> take lettuce 1 from diningtable 1

> You pick up the lettuce 1 from the diningtable 1.

> think: Now I take a lettuce (1). Next, I need to go to sinkbasin (1) and clean it.

OK.

> go to sinkbasin 1

> On the sinkbasin 1, you see a apple 2, a ladle 2, a spoon 1, and a tomato 3.

> clean lettuce 1 with sinkbasin 1

> You clean the lettuce 1 using the sinkbasin 1.

> think: Now I clean a lettuce (1). Next, I need to put it in/on diningtable 1. OK.

> go to diningtable 1

> On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork 2, a knife 2, a knife 1, a ladle 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.

> put lettuce 1 in/on diningtable 1

> You put the lettuce 1 in/on the diningtable 1.

---

## WebShop Prompt (ReAct Example)

Instruction: I would like a 3 ounce bottle of bright citrus deodorant for sensitive skin, and price lower than 50.00 dollars

Action: search 3 ounce bright citrus deodorant sensitive skin  
Observation: Back to Search Page 1 (Total results: 50) ... B078GWRC1J Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce $10.99 ...

Action: click B078GWRC1J  
Observation: [Options, product details]

Action: think[B078GWRC1J and B078GTKVXY are bright citrus deodorant less than 50 dollars. I can check B078GWRC1J first.]
Observation: OK.

Action: click[bright citrus]  
Observation: You have clicked bright citrus.

Action: click[3 ounce (pack of 1)]  
Observation: You have clicked 3 ounce (pack of 1).

Action: click[Buy Now]

---

## Example Trajectories & Analysis

### ALFWorld: ReAct Trace

You are in the middle of a room. Looking quickly around you, you see a cabinet 5, a cabinet 4, ..., a countertop 3, a countertop 2, a countertop 1, ...

Your task is to: put a clean knife in countertop.

> think: To solve the task, I need to find and take a knife, then clean it with the sinkbasin, then put it on a countertop.

> go to countertop 2  
> take knife 1 from countertop 2  
> go to sinkbasin 1  
> clean knife 1 with sinkbasin 1  
> go to countertop 1  
> put knife 1 in/on countertop 1

---

### WebShop: ReAct Trace

Instruction: get me a sixteen pack of apple cinnamon freeze dried banana chips, and price lower than 50.00 dollars

- Action: search[sixteen pack apple cinnamon freeze dried banana chips]
    - Observation: ... [shows relevant products]
- Action: think[B0061IVFZE is strawberry banana, not apple cinnamon. B096H2P6G2 is fruit snacks, not freeze dried banana chips. B092JLLYK6 is banana crisps, not apple cinnamon. I can check B092JLLYK6 first.]
    - Observation: OK.
- Action: click[B092JLLYK6]
    - Observation: ... [shows options, including 'apple cinnamon', '0.53 ounce (pack of 16)']
- Action: think[For sixteen pack of apple cinnamon freeze dried banana chips, the item has options 'apple cinnamon' and '0.53 ounce (pack of 16)' and seems good to buy.]
    - Observation: OK.
- Action: click[apple cinnamon]
- Action: click[0.53 ounce (pack of 16)]
- Action: click[Buy Now]

---

This cleaned markdown contains only the main article, methodology, example ReAct traces, and illustrative prompts, removing unrelated headers, footers, references, appendices, and other ancillary content.

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

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png&w=3840&q=75

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), which allows developers to integrate with a growing ecosystem of third-party tools with a simple [client implementation](https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients).

For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities.

### Workflow: Prompt chaining

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png&w=3840&q=75

**When to use this workflow:** This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

**Examples where prompt chaining is useful:**

- Generating Marketing copy, then translating it into a different language.
- Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.

### Workflow: Routing

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png&w=3840&q=75

**When to use this workflow:** Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

**Examples where routing is useful:**

- Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
- Routing easy/common questions to smaller models like Claude 3.5 Haiku and hard/unusual questions to more capable models like Claude 3.5 Sonnet to optimize cost and speed.

### Workflow: Parallelization

LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting:** Running the same task multiple times to get diverse outputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png&w=3840&q=75

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

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png&w=3840&q=75

**When to use this workflow:** This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**Example where orchestrator-workers is useful:**

- Coding products that make complex changes to multiple files each time.
- Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information.

### Workflow: Evaluator-optimizer

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png&w=3840&q=75

**When to use this workflow:** This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

**Examples where evaluator-optimizer is useful:**

- Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques.
- Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted.

### Agents

Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 ("Prompt Engineering your Tools").

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png&w=3840&q=75

**When to use agents:** Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

**Examples where agents are useful:**

The following examples are from our own implementations:

- A coding Agent to resolve [SWE-bench tasks](https://www.anthropic.com/research/swe-bench-sonnet), which involve edits to many files based on a task description;
- Our [“computer use” reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), where Claude uses a computer to accomplish tasks.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png&w=3840&q=75

## Combining and customizing these patterns

These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity _only_ when it demonstrably improves outcomes.

## Summary

Success in the LLM space isn't about building the most sophisticated system. It's about building the _right_ system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

When implementing agents, we try to follow three core principles:

1. Maintain **simplicity** in your agent's design.
2. Prioritize **transparency** by explicitly showing the agent’s planning steps.
3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.

Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users.

### Acknowledgements

Written by Erik Schluntz and Barry Zhang. This work draws upon our experiences building agents at Anthropic and the valuable insights shared by our customers, for which we're deeply grateful.

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
<summary>building-react-agents-from-scratch-a-hands-on-guide-using-ge</summary>

# Building ReAct Agents from Scratch: A Hands-On Guide using Gemini

`tldr` **:** _ReAct (Reason + Act) is a powerful framework for building AI agents that seamlessly integrates reasoning and decision-making with task execution. By leveraging large language models (LLMs) like Gemini, ReAct agents can dynamically analyze problems, choose appropriate tools, and iteratively work towards solutions. This article explores the foundations of ReAct, provides a step-by-step guide to building a ReAct agent from scratch, and discusses its implications for the future of generative AI. It includes a_ [_GitHub repo_](https://github.com/arunpshankar/react-from-scratch) _with all the code and artifacts needed to get started quickly. Even though the post uses Gemini, the underlying LLM can easily be replaced with any foundational models._

https://miro.medium.com/v2/resize:fit:700/1*o307XLpR20oxEXi6iZEe7g.jpeg

Throughout human history, tool use has been a defining characteristic of our species, shaping our evolution and cognitive development. Tools have been instrumental in human evolution, enhancing both our physical and mental abilities. They’ve enabled us to surpass our natural limitations, fostering cognitive growth and a deeper understanding of cause and effect. Through tools, we’ve developed increasingly compact technologies and learned to view external objects as extensions of ourselves, significantly expanding our capabilities to interact with and shape our environment. As we venture into the era of artificial intelligence (AI), we find ourselves at a fascinating juncture where AI agents are beginning to mirror this fundamental aspect of human behavior. By incorporating tool use and complex reasoning, AI agents are pushing the boundaries of what machines can accomplish, potentially revolutionizing how AI interacts with and understands the world around it.

Before we dive into the building process, it’s important to clearly define AI agents and distinguish them from traditional AI systems that perform similar tasks. Let’s examine these concepts in detail:

# What is an AI Agent?

An AI agent is a system designed to perceive its environment, reason about it, and execute actions to achieve specified objectives. It operates by decomposing complex goals into manageable subtasks, selecting appropriate tools (such as search engines, database queries, code execution environments, API calls, and other agents) for each subtask, and iteratively executing these tools while analyzing the resulting observations. The agent adapts its strategy based on intermediate outcomes, refines inputs to optimize tool usage, and maintains a historical context to avoid repeating ineffective approaches. Throughout this process, the agent balances short-term subtasks with its overarching objective, efficiently aggregating and synthesizing results to formulate a comprehensive solution.

In this post, we’ll focus on ReAct as a methodology for creating AI agents capable of performing quite complex tasks given a set of tools. Note that there are other popular approaches to this, like _function calling_, which we’ll cover in a later post.

# The ReAct Framework: A Paradigm Shift

The ReAct framework introduces a unified architecture for AI agents that capitalizes on recent advancements in LLM capabilities. Unlike traditional designs that compartmentalize reasoning and action, ReAct integrates these functionalities into a single, cohesive system. This innovative approach allows AI agents to seamlessly combine thought processes and actions, potentially leading to more efficient and adaptable artificial intelligence systems. This paradigm shift is characterized by three key features:

1. _Unified Reasoning and Acting_: ReAct agents utilize LLMs as centralized components that concurrently reason about the environment and determine appropriate actions. This unification allows the agent to process observations, generate plans, and execute actions seamlessly, eliminating the need for separate, manually designed modules. By integrating reasoning and acting, the agent can adapt more fluidly to complex and dynamic environments.
2. _Dynamic Tool Utilization_: ReAct agents can incorporate a variety of external tools and APIs, selecting and employing them based on the current context and objectives. The LLM facilitates tool selection by analyzing the user’s task and past observations to determine the most appropriate resources to leverage. This dynamic integration enables the agent to extend its capabilities on-the-fly, accessing search engines, databases, code execution environments, and other utilities as needed to achieve its goals.
3. _Iterative Problem Solving_: The framework empowers agents to address complex tasks through an iterative cycle of thought, action, and observation. This feedback loop allows the agent to evaluate the outcomes of its actions, refine its strategies based on effectiveness, and plan subsequent steps accordingly. The iterative process is guided by user-provided prompts, which can include few-shot examples if needed to better illustrate the task. The LLM utilizes both current and historical observations to inform decision-making. Incorporating a memory component to trace the interaction history further enhances the agent’s adaptability and learning over time.

By adopting an integrated approach, ReAct agents overcome the limitations of traditional architectures, particularly in scenarios that require flexible reasoning and adaptive behavior. The fusion of reasoning and acting within an LLM-centric framework enables more sophisticated and context-aware problem-solving capabilities.

At the heart of a ReAct agent lies a LLM, such as Gemini Pro 1.5 as covered in this article. These models serve as the “ _brain_” of the agent and are capable of natural language understanding and generation, complex reasoning and decision-making, maintaining context and utilizing past observations, and generating structured outputs for tool selection and execution.

By framing the agent’s thought processes and actions as a sequence of natural language interactions, the ReAct framework allows agents to leverage the full power of LLMs. This approach facilitates navigation through complex problem-solving scenarios, enabling agents to adapt dynamically to new information and challenges while maintaining a coherent strategy toward achieving their objectives.

# I. Building a ReAct Agent with Gemini

Now that we’ve established the foundations, let’s explore the process of building a ReAct agent using Gemini as our LLM of choice.

https://miro.medium.com/v2/resize:fit:1000/1*TQspcqCDuqzbv5bCiIG26w.png

ReAct Agent — A 1000 foot view

## Overview of ReAct Agent Design

ReAct agents bring a new approach to AI by combining reasoning and action in a continuous cycle. As we learned previously, traditional AI systems separate decision-making from execution, whereas ReAct agents are designed to think and act in a loop. They take in a task, break it down, use external resources to gather information, and adapt based on what they learn. This makes them ideal for handling dynamic tasks that require constant adjustment and interaction with external environments. A 1000-foot overview of the agent architecture is shown above. Let’s break it down one by one:

1. **Input**: The agent starts by receiving a task in natural language. This task goes into the core language model (LLM), like Gemini Pro, which interprets what needs to be done. Thus, the LLM acts as the agent’s “brain,” setting the task in motion. The task is provided by the user. The goal here for the agent is to leverage the tools available at hand to solve the task.
2. **Reasoning**: The LLM analyzes the task and breaks it down into steps. It plans which actions to take and decides how to approach the problem based on available information and tools.
3. **Action with External Environments**: In our current setup, the agent has access to two main environments — Google Search and Wikipedia. Using specific tools connected via APIs, it can look up information on Google for the latest updates or gather facts from Wikipedia. Each action the agent takes depends on what it determines to be the best source for the task. By connecting to these external environments, the agent can quickly find relevant information or get additional context.
4. **Observation and Memory**: After executing each action, the agent observes the results and saves relevant information in its memory. This tracing allows it to keep track of past actions and build on previous observations, so it doesn’t repeat itself or lose context. Each new piece of information enriches the agent’s understanding of the task, making future actions more informed.
5. **Feedback Loop**: The agent cycles through reasoning, action, and observation steps continuously. Every time it gathers new information, it goes back to the reasoning stage, where the LLM considers the updated knowledge. This iterative loop helps the agent refine its approach and stay aligned with the task. The reasoning loop can be either constrained based on an end condition or capped by max iterations. Note that we leverage past observations here from the memory component.
6. **Response**: Finally, once it has gathered enough information and reached a solid understanding, the agent generates a response based on all the information it has collected and refined over multiple cycles. Again, this can be solely decided by the LLM or based on an end condition, or we may fail to arrive at an outcome given the constrained number of iterations.

By continuously interacting with external sources, storing observations, and revisiting its reasoning, the ReAct agent can tackle complex problems in a more flexible and adaptable way than traditional models. This design enables it to handle real-time information, respond to changing scenarios, and produce high-quality results with minimal human intervention.

Now that we have an understanding of the overall architecture we want to build, let’s start breaking it down into individual steps one by one.

## Step 1: Setting Up the Environment

For this exercise, we can choose between two types of search environments: Google Search and Wikipedia Search. Google Search is available via the SERP API, while Wikipedia has its own API. Our goal is to provide tools — Python functions that encapsulate API calling logic — which take a query (search term) and return the results from these environments.

For Google Search, we receive the top 10 results ranked and have the following information: rank, title, link, and snippet. A snippet in Google is a brief summary or description of a web page that appears in a search result. Snippets are designed to help users understand the content of a page and decide whether to click on it. While providing minimal information, snippets often pack crisp pieces of information that we need.

In the case of Wikipedia, we get the title and summary — a short paragraph about the topic we search for.

The tools for these searches are implemented in `serp.py` and `wiki.py` under the `src/tools` directory.

## Step 2: Defining the Agent Structure and Supporting Classes

To build our ReAct agent, we need to define several classes and structures that work together. Let’s explore each of these components:

**2.1 Enums and Custom Types**

First, we’ll define enums and custom types for use throughout our implementation. Enums will map the tool choices, while a custom type will capture observations during each iteration of tool usage. The complete code for the ReAct agent is located in `agent.py` under the `src/react` directory.

```
from enum import Enum, auto
from typing import Union, Callable

class Name(Enum):
    """Enumeration for tool names available to the agent."""
    WIKIPEDIA = auto()
    GOOGLE = auto()
    NONE = auto()
    def __str__(self) -> str:
        return self.name.lower()

Observation = Union[str, Exception]
```

**2.2 Message and Choice Models**

Next, we’ll define Pydantic models for messages and tool choices:

```
from pydantic import BaseModel, Field

class Message(BaseModel):
    role: str = Field(..., description="The role of the message sender.")
    content: str = Field(..., description="The content of the message.")

class Choice(BaseModel):
    name: Name = Field(..., description="The name of the tool chosen.")
    reason: str = Field(..., description="The reason for choosing this tool.")
```

**2.3 Tool Class**

The `Tool` class encapsulates the functionality of individual tools:

```
class Tool:
    def __init__(self, name: Name, func: Callable[[str], str]):
            self.name = name
            self.func = func

        def use(self, query: str) -> Observation:
            try:
                return self.func(query)
            except Exception as e:
                logger.error(f"Error executing tool {self.name}: {e}")
                return str(e)
```

**2.4 Agent Class**

Now, let’s look into the `Agent` class and its methods. This class defines the agent responsible for executing queries and handling tool interactions.

```
class Agent:
    def __init__(self, model: GenerativeModel) -> None:
        self.model = model
        self.tools: Dict[Name, Tool] = {}
        self.messages: List[Message] = []
        self.query = ""
        self.max_iterations = 5
        self.current_iteration = 0
        self.template = self.load_template()

    def load_template(self) -> str: ...

    def register(self, name: Name, func: Callable[[str], str]) -> None: ...

    def trace(self, role: str, content: str) -> None: ...

    def get_history(self) -> str: ...

    def think(self) -> None: ...

    def decide(self, response: str) -> None: ...

    def act(self, tool_name: Name, query: str) -> None: ...

    def execute(self, query: str) -> str: ...

    def ask_gemini(self, prompt: str) -> str: ...
```

These classes and structures work together to create a flexible and powerful ReAct agent. By organizing our code this way, we’ve built a modular and extensible framework for ReAct agents. This structure allows for easy addition of new tools, modification of the reasoning process, and integration with different LLMs or external services. Next, we’ll dive into the actual implementation of the most crucial component — the think-act-observe loop.

## Step 3: Implementing the Think-Act-Observe Loop

The core of the ReAct agent is its ability to think, act, and observe in an iterative loop. A high-level flow diagram below illustrates how a ReAct agent functions in this loop. The core pieces are the thinking (reasoning) phase, the acting phase (calling APIs and accessing the environment through tool use), and finally, the observation phase (collecting results). This cycle repeats, allowing the agent to improve and move towards a common goal set initially. In the following sections, we’ll examine each component of this loop in detail.

https://miro.medium.com/v2/resize:fit:700/1*O8k5Oy65KYhkNFQ13PRpUA.png

Think-Act-Observe loop

**_Think_**

The `think` method forms the core of this ReAct agent's cognitive loop. It manages iteration tracking, dynamically constructs prompts using the current context, interacts with the Gemini language model, and logs the agent's thoughts. By calling the `decide` method based on the model's response, it initiates the next phase of reasoning or action.

```
def think(self) -> None:
    self.current_iteration += 1
    if self.current_iteration > self.max_iterations:
        logger.warning("Reached maximum iterations. Stopping.")
        return
    prompt = self.prompt_template.format(
        query=self.query,
        history=self.get_history(),
        tools=', '.join([str(tool.name) for tool in self.tools.values()])
    )
    response = self.ask_gemini(prompt)
    self.trace("assistant", f"Thought: {response}")
    self.decide(response)
```

**_Decide_**

The `decide` method is another pivotal component in the ReAct agent’s decision-making process, directly following the `think` component. It parses the JSON response from the language model (Gemini), determining whether to take an action using a specific tool or to provide a final answer. If an action is required, it calls the `act` method with the chosen tool and input. For final answers, it logs the result. The method includes error handling to manage parsing issues or unexpected response formats, reverting to the `think` method if problems arise. This approach ensures a robust cycle of thought and action, allowing the agent to navigate complex queries by seamlessly transitioning between reflection and tool utilization until a satisfactory answer is reached or the iteration limit is met.

```
def decide(self, response: str) -> None:
    try:
        parsed_response = json.loads(response.strip().strip('`').strip())
        if "action" in parsed_response:
            action = parsed_response["action"]
            tool_name = Name[action["name"].upper()]
            self.act(tool_name, action.get("input", self.query))
        elif "answer" in parsed_response:
            self.trace("assistant", f"Final Answer: {parsed_response['answer']}")
        else:
            raise ValueError("Invalid response format")
    except Exception as e:
        logger.error(f"Error processing response: {str(e)}")
        self.think()
```

**_Act_**

The `act` method completes the ReAct agent's cognitive cycle, following the `think` and `decide` phases. It executes the chosen tool based on Gemini decision, applying it to the current query or a refined input. Crucially, after every action, the method captures and logs the tool's output as an observation, integrating it into the agent's memory through the `trace` method. These observations, both current and accumulated from past iterations, are incorporated into the next `think` cycle, enabling the agent to reason based on a growing pool of information.

This iterative process of action, observation, and reflection allows the ReAct agent to build upon its knowledge incrementally, making increasingly informed decisions as it progresses through complex queries. By tying each action to logged observations, the agent maintains a comprehensive trace of its problem-solving journey, facilitating both effective reasoning and transparent decision-making.

```
def act(self, tool_name: Name, query: str) -> None:
    tool = self.tools.get(tool_name)
    if tool:
        result = tool.use(query)
        observation = f"Observation from {tool_name}: {result}"
        self.trace("system", observation)
        self.think()
    else:
        logger.error(f"No tool registered for choice: {tool_name}")
        self.think()
```

The complete code for the ReAct agent is located in `agent.py` under the `src/react` directory.

## Step 4: Crafting the Prompt Template

Crafting an effective ReAct prompt template is crucial after understanding the reasoning loop. This well-structured prompt guides the agent’s behavior and decision-making process, serving as the initial seed for interactions. A ReAct prompt typically includes four key components: i) the current query, ii) any previous reasoning steps and observations, iii) available tools, and iv) output format instructions. These instructions cover reasoning for tool selection, insights from past observations, and guidelines for concluding the reasoning loop.

Prompts can be either _zero-shot_, providing instructions without examples, or _few-shot_, which includes examples of reasoning and actions. For this exercise, we use a zero-shot approach. The prompt’s goal is to effectively teach the model to adopt ReAct-like behavior through carefully crafted instructions. It structures the agent’s thought process, encouraging it to break down problems, seek information, and take appropriate steps. By incorporating these elements, the prompt facilitates a structured approach to problem-solving, enabling the language model to navigate complex tasks more effectively.

The prompt template we used for building our ReAct agent is shown below. Note that except for the tool name within parentheses, everything else is agnostic to the genre and is not tied to anything specific we are building here.

```
You are a ReAct (Reasoning and Acting) agent tasked with answering the following query:

Query: {query}

Your goal is to reason about the query and decide on the best course of action to answer it accurately.

Previous reasoning steps and observations: {history}

Available tools: {tools}

Instructions:
1. Analyze the query, previous reasoning steps, and observations.
2. Decide on the next action: use a tool or provide a final answer.
3. Respond in the following JSON format:

If you need to use a tool:
{{
    "thought": "Your detailed reasoning about what to do next",
    "action": {{
        "name": "Tool name (wikipedia, google, or none)",
        "reason": "Explanation of why you chose this tool",
        "input": "Specific input for the tool, if different from the original query"
    }}
}}

If you have enough information to answer the query:
{{
    "thought": "Your final reasoning process",
    "answer": "Your comprehensive answer to the query"
}}

Remember:
- Be thorough in your reasoning.
- Use tools when you need more information.
- Always base your reasoning on the actual observations from tool use.
- If a tool returns no results or fails, acknowledge this and consider using a different tool or approach.
- Provide a final answer only when you're confident you have sufficient information.
- If you cannot find the necessary information after using available tools, admit that you don't have enough information to answer the query confidently.
```

You can find the prompt template in the shared repo [here](https://github.com/arunpshankar/react-from-scratch/blob/main/data/input/react.txt).

# II. Comparing Approaches: Traditional vs. ReAct Agents

https://miro.medium.com/v2/resize:fit:700/1*8xI6wr1Pj32h5ylDU5Tr1w.jpeg

To appreciate the power and flexibility of the ReAct framework, comparing it to traditional methods for tool selection and query processing reveals key differences. Traditional systems often rely on predefined rules or pattern matching, such as routing biographical queries to Wikipedia and location queries to Google. ReAct, however, leverages a language model to dynamically analyze and select tools based on context, offering distinct advantages:

Traditional systems are inherently rigid, bound by preset logic, which limits flexibility. ReAct, by contrast, adapts fluidly to a wide range of queries, using its reasoning capability for multi-step decisions. This context-driven approach enables ReAct to maintain conversation history, track prior interactions, and craft more effective responses. Moreover, unlike traditional systems that require code updates to integrate new tools, ReAct seamlessly incorporates new capabilities using only tool descriptions. Its natural language understanding also enhances error handling, providing constructive suggestions and supporting complex, multi-step problem-solving.

For a simple example, consider `src/tools/manager.py`, which demonstrates a rule-driven approach to selecting tools based on query cues, without using an LLM like Gemini. Here, the manager routes queries based on prefixes: `/people` queries go to Wikipedia for biographical information, while `/location` queries go to Google for location-based searches. However, this structure forces us to pre-format queries and encode rigid rules, creating a bottleneck. To expand capabilities, we must add more rules and modify the code—a limitation that ReAct addresses effortlessly by dynamically interpreting context.

```
class Manager:
    """
    Manages tool registration, selection, and execution.
    """
    def __init__(self) -> None:
        self.tools: Dict[Name, Tool] = {}

    def register(self, name: Name, func: Callable[[str], str]) -> None:
        """
        Register a new tool.
        """
        self.tools[name] = Tool(name, func)

    def act(self, name: Name, query: str) -> Observation:
        """
        Retrieve and use a registered tool to process the given query.

        Parameters:
            name (Name): The name of the tool to use.
            query (str): The input query string.

        Returns:
            Observation: The result of the tool's execution or an error.
        """
        if name not in self.tools:
            raise ValueError(f"Tool {name} not registered")

        processed_query = query.split(' ', 1)[1] if ' ' in query else query
        return self.tools[name].use(processed_query)

    def choose(self, query: str) -> Choice:
        """
        Choose the appropriate tool based on the query prefix.
        """
        if query.startswith("/people"):
            return Choice(
                name=Name.WIKIPEDIA,
                reason="Query starts with /people, using Wikipedia for biographical information."
            )
        elif query.startswith("/location"):
            return Choice(
                name=Name.GOOGLE,
                reason="Query starts with /location, using Google for location-specific information."
            )
        else:
            raise ValueError("Unsupported query. Use /people or /location prefix.")
```

# III. ReAct in Action: Analyzing the Output Trace

To better understand how a ReAct agent operates, let’s examine some output traces from real interactions. We’ll look at three example queries with diverse complexity.

## **Example 1: Streamlined 3-Step Query**

Let’s start with the first example, which demonstrates the agent’s thought process as it answers a simple question requiring current world knowledge. The agent retrieves the latest information from its environment using provided tools. The query is: _Who is older, Cristiano Ronaldo or Lionel Messi?_

Imagine how a human would figure this out — using Google and Wikipedia. We’d either go to Wikipedia to get the birthdates of both players and compare them, or do the same with Google. However, we’d have to break the question into two parts, one for each player, and perform the same type of search for both before finally comparing to arrive at the answer. Let’s see how this process is emulated by our ReAct agent.

Our ReAct agent solves this correctly in three iterations, as shown below, giving us a peek into its thought process.

**Iteration 1: Initial Analysis and Tool Selection**

```
Thought: {
 "thought": "The query asks for a comparison of age between Cristiano Ronaldo and Lionel Messi. To determine who is older, I need to find their birth dates and compare.",
 "action": {
  "name": "wikipedia",
  "reason": "Wikipedia is a reliable source for biographical information, including birth dates of famous individuals.",
  "input": "Cristiano Ronaldo"
 }
}

Action: Using wikipedia tool
Observation: [Wikipedia summary for Cristiano Ronaldo, including his birth date: February 5, 1985]
```

In this first iteration, the agent:

1. Analyzes the query and identifies the need for birth dates.
2. Chooses the Wikipedia tool as a reliable source for this information.
3. Decides to look up Cristiano Ronaldo first.

**Iteration 2: Gathering Additional Information**

```
Thought: {
 "thought": "I have found Cristiano Ronaldo's birth date from Wikipedia: February 5, 1985. Now I need to find Lionel Messi's birth date to compare and determine who is older.",
 "action": {
  "name": "wikipedia",
  "reason": "Wikipedia is a reliable source for biographical information, and I need to find Lionel Messi's birth date to compare with Cristiano Ronaldo's.",
  "input": "Lionel Messi"
 }
}

Action: Using wikipedia tool
Observation: [Wikipedia summary for Lionel Messi, including his birth date: June 24, 1987]
```

In the second iteration, the agent:

1. Acknowledges the information gathered about Ronaldo.
2. Identifies the need for Messi’s birth date to complete the comparison.
3. Again chooses Wikipedia as the appropriate tool.

**Iteration 3: Final Analysis and Answer**

```
Thought: {
 "thought": "I now have Cristiano Ronaldo's birth date (February 5, 1985) and Lionel Messi's birth date (June 24, 1987) from Wikipedia. I can compare these dates to determine who is older.",
 "answer": "Cristiano Ronaldo is older than Lionel Messi. Ronaldo was born on February 5, 1985, while Messi was born on June 24, 1987."
}

Final Answer: Cristiano Ronaldo is older than Lionel Messi. Ronaldo was born on February 5, 1985, while Messi was born on June 24, 1987.
```

In the final iteration, the agent:

1. Synthesizes the information gathered from both Wikipedia searches.
2. Compares the birth dates to determine who is older.
3. Provides a clear, concise answer to the original query.

This trace demonstrates several key aspects of the ReAct framework: the agent uses iterative reasoning by breaking down the problem into steps, gathering necessary information before making a final decision; it utilizes tools effectively, such as the Wikipedia tool, to gather relevant data; it exhibits adaptive behavior by adjusting its actions based on the information it has and what it still needs; and its decision-making process is transparent, with each thought clearly articulated, showing how the agent arrives at its decisions and final answer. By examining this trace, we see how the ReAct agent combines reasoning and action to solve queries in a structured, transparent, and effective manner. You can find the complete trace of the agent [here](https://github.com/arunpshankar/react-from-scratch/blob/main/data/output/trace_1.txt).

## **Example 2:** Multi-Step Research Query

Now let’s test it with a more challenging query: “ _What is the average temperature in the capital city of the country where the current FIFA World Cup champion’s team captain was born?_”

This query contains several unknowns. To solve it, we need to break it down into subtasks and solve them in order. More importantly, we need to use a combination of tools at our disposal — both Wikipedia and Google — and know which tool to use when. Let’s take a look at how our agent solves this in four iterations.

**Iteration 1: Query Breakdown**

```
Thought: To answer this query, I need to break it down into smaller steps:
1. Find out who the current FIFA World Cup champion team captain is.
2. Find out where they were born.
3. Determine the capital city of that country.
4. Look up the average temperature in that capital city.

Action: Use Wikipedia to search for "2022 FIFA World Cup"
```

**Explanation**:

- **Thought**: The agent breaks down the query into steps: identifying the FIFA World Cup champion team captain, determining their birthplace, finding the capital of that country, and then looking up the average temperature in the capital city.
- **Action**: The agent begins by using Wikipedia to search for “2022 FIFA World Cup” to identify the champion team captain.
- **Observation**: The Wikipedia search reveals that Lionel Messi was the captain of the Argentinian team that won the 2022 FIFA World Cup.

**Iteration 2: Finding Messi’s Birthplace**

```
Thought: The Wikipedia summary tells us that Lionel Messi was the captain of the Argentinian team that won the 2022 FIFA World Cup. Now I need to find out where Lionel Messi was born.

Action: Use Wikipedia to search for "Lionel Messi"
```

**Explanation**:

- **Thought**: With Lionel Messi identified as the team captain, the agent now focuses on finding Messi’s birthplace to answer the next step of the query.
- **Action**: It searches Wikipedia for “Lionel Messi.”
- **Observation**: The Wikipedia page on Lionel Messi confirms that he was born in Rosario, Argentina.

**Iteration 3: Capital City and Temperature**

```
Thought: The Wikipedia summary on Lionel Messi states that he was born in Rosario, Argentina. To answer the query, I need to find the average temperature in Buenos Aires, the capital of Argentina.

Action: Use Google to search for "average temperature in Buenos Aires"
```

**Explanation**:

- **Thought**: Knowing Messi was born in Rosario, Argentina, the agent identifies Buenos Aires as the capital of Argentina, where it needs to find the average temperature.
- **Action**: The agent uses Google to search for the “average temperature in Buenos Aires.”
- **Observation**: Google results provide average temperature data for Buenos Aires, with several sources mentioning an average of around 18°C (64°F).

**Iteration 4: Final Answer**

```
Thought: I have gathered all the necessary information. Lionel Messi, captain of the 2022 FIFA World Cup winning team, was born in Argentina. The capital of Argentina is Buenos Aires. Google search results show that the average temperature in Buenos Aires varies throughout the year, but several sources mention an average temperature of around 18°C (64°F).

Answer: The average temperature in the capital city of the country where the current FIFA World Cup champion's team captain was born is approximately 18°C (64°F). This refers to Buenos Aires, Argentina, the birthplace of Lionel Messi.
```

**Explanation**:

- **Thought**: The agent has gathered all the necessary information: Lionel Messi, captain of the 2022 FIFA World Cup-winning team, was born in Argentina. The capital city is Buenos Aires, with an average temperature of approximately 18°C (64°F).
- **Action**: It constructs a response summarizing these findings.
- **Observation**: The agent provides a complete answer: “ _The average temperature in the capital city of the country where the current FIFA World Cup champion’s team captain was born is approximately 18°C (64°F), referring to Buenos Aires, Argentina, the birthplace of Lionel Messi._”

The complete agent trace can be accessed at this [location](https://github.com/arunpshankar/react-from-scratch/blob/main/data/output/trace_2.txt).

## Example 3: Comparative Analysis Query

Let’s consider a more complex query that requires advanced reasoning and critical thinking. This type of question doesn’t have a definitive answer, but rather involves exploring multiple sub-questions in a hierarchical manner. The goal is to compare and synthesize all the information gathered to arrive at a comprehensive conclusion. We’ll examine how our React-based agent performs in handling this type of sophisticated, multi-layered analysis.

Query: “ _What is the most common ingredient in the national dishes of the top 5 countries by GDP?_”

**Iteration 1: Initial Query and Breakdown**

```
{
  "thought": "To answer this query, I need to break it down into steps:\n1. Identify the top 5 countries by GDP.\n2. Determine the national dish of each country.\n3. Identify the ingredients in each national dish.\n4. Analyze the ingredients to find the most common one.\n\nI need to use a tool to get the information for steps 1 and 2.",
  "action": {
    "name": "google",
    "reason": "Google can provide a list of the top 5 countries by GDP and information about their national dishes.",
    "input": "top 5 countries by GDP and their national dishes"
  }
}
```

**Explanation**:

- **Thought**: The agent structures the query into four logical steps: identifying GDP rankings, discovering national dishes, listing ingredients, and analyzing commonalities.
- **Action**: It chooses Google to retrieve a list of countries with high GDP and corresponding national dishes.
- **Observation**: The tool returns general results on high GDP countries, but without a clear, unified list of national dishes.

**Iteration 2: Refining the Search**

```
{
  "thought": "The Google search results provided lists of countries by GDP and some information about national dishes, but not a clear and consistent pairing of the two for the top 5 countries. I need to refine my search to get more specific information.",
  "action": {
    "name": "google",
    "reason": "Google is still the best tool to find this information, but I need to be more specific in my query.",
    "input": "National dish of each of the top 5 countries by GDP"
  }
}
```

**Explanation**:

- **Thought**: Observing that the previous search didn’t yield a cohesive list, the agent decides to refine the query by explicitly requesting the “National dish of each of the top 5 countries by GDP.”
- **Action**: The agent queries Google again with this refined search.
- **Observation**: Google still provides general results about national dishes and GDP rankings but lacks a structured pairing of each country with its national dish.

**Iteration 3: Switching to Wikipedia for Specificity**

```
{
  "thought": "The Google search results still don't offer a clear and readily available list of national dishes for the top 5 economies. Wikipedia might have more detailed information about national dishes for each country. I can search for each country individually on Wikipedia and look for information about their national dish.",
  "action": {
    "name": "wikipedia",
    "reason": "Wikipedia is a more comprehensive source for information about specific topics like national dishes.",
    "input": "United States national dish"
  }
}
```

**Explanation**:

- **Thought**: The agent, realizing that Google results lack specificity, considers Wikipedia as a better source for individually searching each country’s national dish, starting with the United States.
- **Action**: It queries Wikipedia for “United States national dish.”
- **Observation**: Wikipedia does not yield a definitive “national dish” for the U.S., highlighting that this approach may not work universally across countries.

**Iteration 4: Expanding Scope to Popular Dishes**

```
{
  "thought": "The Wikipedia search for \"United States national dish\" returned no results. This suggests that a direct search for a single national dish for each country might not be the most effective approach. National dishes can be subjective and vary by region or cultural group. Instead of searching for a single dish, I should broaden my search to include popular or common dishes in each country. I can then analyze the ingredients of these dishes to identify any commonalities.",
  "action": {
    "name": "google",
    "reason": "Google is a better tool for broader searches and can provide a wider range of information about popular dishes in each country.",
    "input": "Popular dishes in the United States"
  }
}
```

**Explanation**:

- **Thought**: Noting Wikipedia’s limitations for national dishes, the agent broadens its scope to search for “popular dishes” instead. This broader approach should yield enough data on common foods, even if a single national dish is elusive.
- **Action**: It switches back to Google with the broader query “Popular dishes in the United States.”
- **Observation**: Google successfully provides a list of popular U.S. dishes, enabling the agent to compile a useful list of notable foods.

**Iteration 5: Continuing with Popular Dishes for Each Country**

```
{
  "thought": "The Google search provided a list of popular dishes in the United States. I can now repeat this process for the remaining top 4 countries by GDP (China, Japan, Germany, and India) to gather information about their popular dishes. Once I have a list of popular dishes for each country, I can then research common ingredients in those dishes to determine the most common one.",
  "action": {
    "name": "google",
    "reason": "Google is effective for finding lists of popular dishes in specific countries.",
    "input": "Popular dishes in China"
  }
}
```

**Explanation**:

- **Thought**: Satisfied with the U.S. results, the agent decides to repeat this search process for China, Japan, Germany, and India to collect popular dishes from each.
- **Action**: It queries Google with “Popular dishes in China” to gather similar data for China.
- **Observation**: Google provides relevant results for popular dishes in China, enabling the agent to proceed confidently with this approach for each remaining country.

**Iteration 6: Gathering Dishes for Japan**

```
{
  "thought": "I've successfully found lists of popular dishes for the United States and China. I need to continue this process for Japan, Germany, and India to get a comprehensive list of popular dishes for all five countries. Once I have those lists, I can research common ingredients and identify the most frequent one.",
  "action": {
    "name": "google",
    "reason": "Google is effective for finding lists of popular dishes in specific countries.",
    "input": "Popular dishes in Japan"
  }
}
```

**Explanation**:

- **Thought**: With data on the U.S. and China, the agent moves on to Japan, maintaining the plan to compile popular dishes for each of the top 5 GDP countries.
- **Action**: It uses Google to search “Popular dishes in Japan.”
- **Observation**: Google successfully provides a list of popular Japanese dishes, further supporting this method for gathering culinary data country-by-country.

**Iteration 7: Researching Germany’s Popular Dishes**

```
{
  "thought": "I now have lists of popular dishes for the United States, China, and Japan. I need to find similar lists for Germany and India to complete my data on the top 5 economies. I will use Google again as it has been effective for this purpose.",
  "action": {
    "name": "google",
    "reason": "Google is effective for finding lists of popular dishes in specific countries.",
    "input": "Popular dishes in Germany"
  }
}
```

**Explanation**:

- **Thought**: With data on three countries, the agent turns to Germany as it continues gathering popular dishes for each of the top 5 GDP countries.
- **Action**: It queries Google with “Popular dishes in Germany.”
- **Observation**: Google returns a comprehensive list of German dishes, allowing the agent to proceed confidently with its plan.

**Iteration 8: Compiling India’s Popular Dishes**

```
{
  "thought": "I have successfully gathered lists of popular dishes for the United States, China, Japan, and Germany. I need to find a similar list for India to complete my data on the top 5 economies. I will use Google again as it has been effective for this purpose.",
  "action": {
    "name": "google",
    "reason": "Google is effective for finding lists of popular dishes in specific countries.",
    "input": "Popular dishes in India"
  }
}
```

**Explanation**:

- **Thought**: With lists for four countries completed, India is the final country needed to round out the data set for the top five GDP countries.
- **Action**: The agent queries Google with “Popular dishes in India.”
- **Observation**: Google successfully provides a list of popular Indian dishes, completing the agent’s data gathering.

**Iteration 9: Planning to Analyze Ingredients**

```
{
  "thought": "I have now gathered lists of popular dishes for all five countries: the United States, China, Japan, Germany, and India. My next step is to analyze these lists and identify common ingredients across the dishes. However, this task is too complex to perform without a tool. I need a way to efficiently research the ingredients of multiple dishes across different cuisines. Since there isn't a specific tool for this purpose, I will try using Google to research the ingredients of each dish individually and note any recurring patterns.",
  "action": {
    "name": "google",
    "reason": "While there isn't a perfect tool for this task, Google can be used to research the ingredients of each dish individually. I will manually analyze the results for commonalities.",
  "input": "Ingredients in [Dish Name]"
 }
}
```

**Explanation**:

- **Thought**: With popular dishes identified for each country, the agent now plans to analyze the ingredients for these dishes to spot commonalities. Recognizing that this analysis is complex, the agent decides to look up each dish individually.
- **Action**: The agent begins a series of Google searches focused on identifying ingredients in each specific dish.
- **Observation**: As Google yields results for each dish’s ingredients, the agent proceeds to manually compare and analyze these ingredients to find any common patterns.

**Iteration 10: Realizing Complexity and Focusing on Common Themes**

```
{
  "thought": "The last Google search returned a list of recipe websites and ingredient resources, but not specific ingredient lists for popular dishes. It seems that finding a single most common ingredient across such diverse cuisines will be difficult. Many ingredients like salt, sugar, and cooking oil are likely used in almost every dish but are not very insightful. Additionally, directly comparing ingredient frequency across vastly different cooking styles and cultural preferences might not be the best way to approach the query. \n\nInstead of focusing on a single ingredient, I can aim for a more general answer about common ingredient types or flavor profiles. To do this, I will research common ingredients and cooking styles for each country's cuisine and look for overarching themes or similarities.",
  "action": {
    "name": "google",
    "reason": "Google can provide information about common ingredients and cooking styles for each country's cuisine.",
    "input": "Common ingredients in [Country] cuisine"
 }
}
```

**Explanation**:

- **Thought**: The agent realizes that pinpointing a single common ingredient is impractical due to the diversity in cooking styles and ingredient usage. Instead, it shifts focus to identifying broad ingredient types or flavor profiles that are common across these cuisines.
- **Action**: It adjusts its queries to gather general data on common ingredients and cooking styles for each country.
- **Observation**: Google provides information about the general culinary profiles and common ingredients, allowing the agent to summarize overarching themes instead of finding a single ingredient.

**Iteration 11: Gathering U.S. Ingredient Data**

```
{
  "thought": "The previous attempts to find a single most common ingredient across the national dishes of the top 5 GDP countries highlighted the difficulty of directly comparing ingredients across diverse culinary traditions.  It's clear that a more nuanced approach is needed. Instead of looking for a single ingredient, I can provide a more insightful answer by identifying common ingredient types or flavor profiles prevalent in these countries' cuisines. I will research common ingredients and cooking styles for each country and then synthesize the information to identify overarching themes.",
  "action": {
    "name": "google",
    "reason": "Google can provide information about common ingredients and cooking styles for each country's cuisine.",
    "input": "Common ingredients in United States cuisine"
 }
}
```

**Explanation**:

- **Thought**: Having determined that ingredient themes are more insightful, the agent begins by collecting information on common ingredients in American cuisine, expecting to identify regional or staple ingredients that define U.S. culinary styles.
- **Action**: The agent searches Google with “Common ingredients in United States cuisine.”
- **Observation**: Google provides detailed information on core American ingredients, including wheat, corn, and various proteins, underscoring the diversity within American food traditions.

**Iteration 12: Researching Chinese Cuisine Ingredients**

```
{
  "thought": "The Google search provided insights into common ingredients in US cuisine, highlighting the diversity and regional variations. To effectively compare culinary trends across the top 5 GDP countries, I need to gather similar information about common ingredients and cooking styles for China, Japan, Germany, and India. Once I have a better understanding of each country's culinary landscape, I can then analyze for common themes or patterns.",
  "action": {
    "name": "google",
    "reason": "Google is effective for gathering information about culinary traditions and common ingredients in different countries.",
    "input": "Common ingredients in Chinese cuisine"
 }
}
```

**Explanation**:

- **Thought**: With U.S. data gathered, the agent continues with China, aiming to identify common ingredients and cooking methods that characterize Chinese cuisine.
- **Action**: It queries Google with “Common ingredients in Chinese cuisine.”
- **Observation**: Google reveals staple Chinese ingredients such as soy sauce, ginger, and garlic, giving the agent a foundation of core components in Chinese cooking.

**Iteration 13: Researching Japanese Cuisine Ingredients**

```
{
  "thought": "I've started gathering information about common ingredients and cooking styles in the cuisines of the top 5 GDP countries. I have data for the United States and China, but I still need to research Japan, Germany, and India. Once I have a better understanding of the culinary landscape for all five countries, I can analyze the information for common themes or patterns and provide a more insightful answer than simply identifying a single ingredient.",
  "action": {
    "name": "google",
    "reason": "Google is effective for gathering information about culinary traditions and common ingredients in different countries.",
    "input": "Common ingredients in Japanese cuisine"
 }
}
```

**Explanation**:

- **Thought**: After obtaining data on U.S. and Chinese cuisines, the agent moves to Japan to further capture common ingredient patterns and culinary themes.
- **Action**: The agent uses Google to search for “Common ingredients in Japanese cuisine.”
- **Observation**: Google provides a list of Japanese staples, such as soy sauce, miso, and rice, which helps the agent outline fundamental elements of Japanese cuisine.

**Iteration 14: Researching German Cuisine Ingredients**

```
{
  "thought": "I have gathered information about common ingredients and cooking styles for three out of the five countries: the United States, China, and Japan. To make a comprehensive analysis and identify overarching themes across the top 5 GDP countries' cuisines, I need to gather similar information for Germany and India.  I will continue using Google as it has been effective for this research.",
  "action": {
    "name": "google",
    "reason": "Google is effective for gathering information about culinary traditions and common ingredients in different countries.",
    "input": "Common ingredients in German cuisine"
 }
}
```

**Explanation**:

- **Thought**: With information on three countries, the agent turns to Germany, aiming to gather data on the essential ingredients and cooking styles characteristic of German food.
- **Action**: It searches Google for “Common ingredients in German cuisine.”
- **Observation**: Google lists ingredients like potatoes, sausages, and cabbage, helping the agent understand the staples of German cuisine.

**Iteration 15: Researching Indian Cuisine Ingredients**

```
{
  "thought": "I have gathered information about common ingredients and cooking styles for four out of the five countries: the United States, China, Japan, and Germany. To make a comprehensive analysis and identify overarching themes across the top 5 GDP countries' cuisines, I need to gather similar information for India.  I will continue using Google as it has been effective for this research.",
  "action": {
    "name": "google",
    "reason": "Google is effective for gathering information about culinary traditions and common ingredients in different countries.",
    "input": "Common ingredients in Indian cuisine"
 }
}
```

**Explanation**:

- **Thought**: Having researched the first four countries, the agent now focuses on India, the final country, to complete its dataset of common ingredients across the top five GDP nations.
- **Action**: The agent queries Google with “Common ingredients in Indian cuisine.”
- **Observation**: Google provides typical Indian ingredients, including spices like turmeric and cumin as well as staples like rice and lentils, rounding out the agent’s ingredient data for all five countries.

**Iteration 16: Summary of Outcomes**

```
{
  "thought": "I have successfully gathered information about common ingredients and cooking styles for all five countries: the United States, China, Japan, Germany, and India. Now I can analyze this information to identify overarching themes or similarities in ingredient types or flavor profiles. I don't need to use a tool for this step, as I can reason based on the information I've already collected.",
  "answer": "It's challenging to pinpoint a single most common ingredient across the national dishes of the top 5 GDP countries due to their diverse culinary traditions. However, analyzing common ingredients and cooking styles reveals some overarching themes:\n\n* **Starchy Staples:** All five countries heavily feature starchy staples in their cuisines. In the US, it's wheat (bread, pasta) and corn. China relies on rice and noodles. Japan emphasizes rice and noodles (ramen, udon). Germany favors potatoes and bread. India heavily uses rice and wheat (naan, roti).\n* **Protein Variety:** While specific proteins vary, all five countries incorporate a variety of protein sources. The US includes beef, pork, and chicken. China features pork, chicken, duck, and seafood. Japan utilizes seafood, chicken, and pork. Germany commonly uses pork, beef, and poultry. India, with diverse dietary preferences, incorporates chicken, seafood, lamb, and plant-based proteins like lentils.\n* **Flavor Profiles:** While specific flavor combinations are diverse, some common themes emerge. The US leans towards savory and sweet flavors. China often balances sweet, sour, spicy, and salty. Japan emphasizes umami, often achieved through ingredients like soy sauce and dashi. Germany favors hearty and savory flavors. India is renowned for its diverse and aromatic spice blends, often combining heat, sweetness, sourness, and earthiness.\n\nIn conclusion, while a single most common ingredient is difficult to define, these culinary powerhouses share a reliance on starchy staples and diverse protein sources, while expressing unique flavor profiles through their individual culinary traditions."
}
```

**Explanation**:

- **Thought**: With comprehensive data on common ingredients for the U.S., China, Japan, Germany, and India, the agent is ready to synthesize overarching themes or commonalities in ingredient types and culinary profiles across these cuisines.
- **Action**: No additional search is required; the agent begins to analyze and formulate a response based on the data collected.
- **Observation**: The agent concludes that, while a single common ingredient is impractical to define, there are shared themes among the cuisines: reliance on starchy staples, diverse protein sources, and unique flavor profiles.

You can find the full agent trace [here](https://github.com/arunpshankar/react-from-scratch/blob/main/data/output/trace_3.txt). All code files associated with everything we covered here are available in this [GitHub repository](https://github.com/arunpshankar/react-from-scratch/tree/main).

# Future Directions

The ReAct framework opens up numerous possibilities for enhanced functionality and adaptability in agent-based systems. Future developments could focus on integrating the ability to process diverse data types such as images, audio, and video, enabling agents to interpret a broader spectrum of information for richer, context-aware decisions. Organizing agents into layered hierarchies, where primary agents delegate specialized tasks to sub-agents, would improve efficiency and task segmentation. Additionally, empowering agents to collaborate by sharing observations, tools, and resources would amplify insights and support cohesive decision-making in complex, multi-perspective environments. Higher-level agents can dynamically guide and coordinate other agents, orchestrating actions across a multi-agent setup to handle complex, multi-step tasks efficiently.

In future posts, we’ll explore a multi-agent scenario where a single steering agent interacts with multiple sub-agents, each fulfilling distinct tasks and communicating their findings back for a cohesive outcome. This will extend our current exercise, building a foundation for scalable, collaborative agent networks.

Thanks for reading the article and for your engagement. Your follow and claps mean a lot. If you have any questions or doubts about the content or the shared notebooks, feel free to contact me at [_arunpshankar@google.com_](mailto:arunprsh@amazon.com) or [_shankar.arunp@gmail.com_](mailto:shankar.arunp@gmail.com). You can also find me on [https://www.linkedin.com/in/arunprasath-shankar/](https://www.linkedin.com/in/arunprasath-shankar/)

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)[REST](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#rest)More

```
from google import genai
from google.genai import types

# Define the function declaration for the model
schedule_meeting_function = {
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of people attending the meeting.",
            },
            "date": {
                "type": "string",
                "description": "Date of the meeting (e.g., '2024-07-29')",
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting (e.g., '15:00')",
            },
            "topic": {
                "type": "string",
                "description": "The subject or topic of the meeting.",
            },
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[schedule_meeting_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about the Q3 planning.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = schedule_meeting(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)

```

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const scheduleMeetingFunctionDeclaration = {
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      attendees: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of people attending the meeting.',
      },
      date: {
        type: Type.STRING,
        description: 'Date of the meeting (e.g., "2024-07-29")',
      },
      time: {
        type: Type.STRING,
        description: 'Time of the meeting (e.g., "15:00")',
      },
      topic: {
        type: Type.STRING,
        description: 'The subject or topic of the meeting.',
      },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-2.5-flash',
  contents: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning.',
  config: {
    tools: [{\
      functionDeclarations: [scheduleMeetingFunctionDeclaration]\
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await scheduleMeeting(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}

```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "role": "user",\
        "parts": [\
          {\
            "text": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning."\
          }\
        ]\
      }\
    ],
    "tools": [\
      {\
        "functionDeclarations": [\
          {\
            "name": "schedule_meeting",\
            "description": "Schedules a meeting with specified attendees at a given time and date.",\
            "parameters": {\
              "type": "object",\
              "properties": {\
                "attendees": {\
                  "type": "array",\
                  "items": {"type": "string"},\
                  "description": "List of people attending the meeting."\
                },\
                "date": {\
                  "type": "string",\
                  "description": "Date of the meeting (e.g., '2024-07-29')"\
                },\
                "time": {\
                  "type": "string",\
                  "description": "Time of the meeting (e.g., '15:00')"\
                },\
                "topic": {\
                  "type": "string",\
                  "description": "The subject or topic of the meeting."\
                }\
              },\
              "required": ["attendees", "date", "time", "topic"]\
            }\
          }\
        ]\
      }\
    ]
  }'

```

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
in a single turn ( [parallel function\\
calling](https://ai.google.dev/gemini-api/docs/function-calling#parallel_function_calling)) and in
sequence ( [compositional function\\
calling](https://ai.google.dev/gemini-api/docs/function-calling#compositional_function_calling)).

### Step 1: Define a function declaration

Define a function and its declaration within your application code that allows
users to set light values and make an API request. This function could call
external services or APIs.

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

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

Enabling " [thinking](https://ai.google.dev/gemini-api/docs/thinking)" can improve function call
performance by allowing the model to reason through a request before suggesting
function calls. The Gemini API is stateless, the model's reasoning context will
be lost between turns in a multi-turn conversation. To preserve this context,
you can use thought signatures. A thought signature is an encrypted
representation of the model's internal thought process that you pass back to
the model on subsequent turns.

The [standard pattern for multi-turn tool](https://ai.google.dev/gemini-api/docs/function-calling?example=weather#step-4)
use is to append the model's complete previous response to the conversation
history. The `content` object includes the `thought_signatures` automatically.
If you follow this pattern **No code changes are required**.

### Manually managing thought signatures

If you modify the conversation history manually—instead of sending the complete previous response and want to benefit from thinking you must correctly handle the `thought_signature` included in the model's turn.

Follow these rules to ensure the model's context is preserved:

- Always send the `thought_signature` back to the model inside its original `Part`.
- Don't merge a `Part` containing a signature with one that does not. This breaks the positional context of the thought.
- Don't combine two `Parts` that both contain signatures, as the signature strings cannot be merged.

### Inspecting Thought Signatures

While not necessary for implementation, you can inspect the response to see the
`thought_signature` for debugging or educational purposes.

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

```
import base64
# After receiving a response from a model with thinking enabled
# response = client.models.generate_content(...)

# The signature is attached to the response part containing the function call
part = response.candidates[0].content.parts[0]
if part.thought_signature:
  print(base64.b64encode(part.thought_signature).decode("utf-8"))

```

```
// After receiving a response from a model with thinking enabled
// const response = await ai.models.generateContent(...)

// The signature is attached to the response part containing the function call
const part = response.candidates[0].content.parts[0];
if (part.thoughtSignature) {
  console.log(part.thoughtSignature);
}

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

```
power_disco_ball = {
    "name": "power_disco_ball",
    "description": "Powers the spinning disco ball.",
    "parameters": {
        "type": "object",
        "properties": {
            "power": {
                "type": "boolean",
                "description": "Whether to turn the disco ball on or off.",
            }
        },
        "required": ["power"],
    },
}

start_music = {
    "name": "start_music",
    "description": "Play some music matching the specified parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "energetic": {
                "type": "boolean",
                "description": "Whether the music is energetic or not.",
            },
            "loud": {
                "type": "boolean",
                "description": "Whether the music is loud or not.",
            },
        },
        "required": ["energetic", "loud"],
    },
}

dim_lights = {
    "name": "dim_lights",
    "description": "Dim the lights.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "number",
                "description": "The brightness of the lights, 0.0 is off, 1.0 is full.",
            }
        },
        "required": ["brightness"],
    },
}

```

```
import { Type } from '@google/genai';

const powerDiscoBall = {
  name: 'power_disco_ball',
  description: 'Powers the spinning disco ball.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      power: {
        type: Type.BOOLEAN,
        description: 'Whether to turn the disco ball on or off.'
      }
    },
    required: ['power']
  }
};

const startMusic = {
  name: 'start_music',
  description: 'Play some music matching the specified parameters.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      energetic: {
        type: Type.BOOLEAN,
        description: 'Whether the music is energetic or not.'
      },
      loud: {
        type: Type.BOOLEAN,
        description: 'Whether the music is loud or not.'
      }
    },
    required: ['energetic', 'loud']
  }
};

const dimLights = {
  name: 'dim_lights',
  description: 'Dim the lights.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'The brightness of the lights, 0.0 is off, 1.0 is full.'
      }
    },
    required: ['brightness']
  }
};

```

Configure the function calling mode to allow using all of the specified tools.
To learn more, you can read about
[configuring function calling](https://ai.google.dev/gemini-api/docs/function-calling#function_calling_modes).

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

```
from google import genai
from google.genai import types

# Configure the client and tools
client = genai.Client()
house_tools = [\
    types.Tool(function_declarations=[power_disco_ball, start_music, dim_lights])\
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

```
import { GoogleGenAI } from '@google/genai';

// Set up function declarations
const houseFns = [powerDiscoBall, startMusic, dimLights];

const config = {
    tools: [{\
        functionDeclarations: houseFns\
    }],
    // Force the model to call 'any' function, instead of chatting.
    toolConfig: {
        functionCallingConfig: {
            mode: 'any'
        }
    }
};

// Configure the client
const ai = new GoogleGenAI({});

// Create a chat session
const chat = ai.chats.create({
    model: 'gemini-2.5-flash',
    config: config
});
const response = await chat.sendMessage({message: 'Turn this place into a party!'});

// Print out each of the function calls requested from this single call
console.log("Example 1: Forced function calling");
for (const fn of response.functionCalls) {
    const args = Object.entries(fn.args)
        .map(([key, val]) => `${key}=${val}`)
        .join(', ');
    console.log(`${fn.name}(${args})`);
}

```

Each of the printed results reflects a single function call that the model has
requested. To send the results back, include the responses in the same order as
they were requested.

The Python SDK supports [automatic function calling](https://ai.google.dev/gemini-api/docs/function-calling#automatic_function_calling_python_only),
which automatically converts Python functions to declarations, handles the
function call execution and response cycle for you. Following is an example for
the disco use case.

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)More

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

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

This example shows how to use JavaScript/TypeScript SDK to do comopositional
function calling using a manual execution loop.

```
import { GoogleGenAI, Type } from "@google/genai";

// Configure the client
const ai = new GoogleGenAI({});

// Example Functions
function get_weather_forecast({ location }) {
  console.log(`Tool Call: get_weather_forecast(location=${location})`);
  // TODO: Make API call
  console.log("Tool Response: {'temperature': 25, 'unit': 'celsius'}");
  return { temperature: 25, unit: "celsius" };
}

function set_thermostat_temperature({ temperature }) {
  console.log(
    `Tool Call: set_thermostat_temperature(temperature=${temperature})`,
  );
  // TODO: Make API call
  console.log("Tool Response: {'status': 'success'}");
  return { status: "success" };
}

const toolFunctions = {
  get_weather_forecast,
  set_thermostat_temperature,
};

const tools = [\
  {\
    functionDeclarations: [\
      {\
        name: "get_weather_forecast",\
        description:\
          "Gets the current weather temperature for a given location.",\
        parameters: {\
          type: Type.OBJECT,\
          properties: {\
            location: {\
              type: Type.STRING,\
            },\
          },\
          required: ["location"],\
        },\
      },\
      {\
        name: "set_thermostat_temperature",\
        description: "Sets the thermostat to a desired temperature.",\
        parameters: {\
          type: Type.OBJECT,\
          properties: {\
            temperature: {\
              type: Type.NUMBER,\
            },\
          },\
          required: ["temperature"],\
        },\
      },\
    ],\
  },\
];

// Prompt for the model
let contents = [\
  {\
    role: "user",\
    parts: [\
      {\
        text: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",\
      },\
    ],\
  },\
];

// Loop until the model has no more function calls to make
while (true) {
  const result = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents,
    config: { tools },
  });

  if (result.functionCalls && result.functionCalls.length > 0) {
    const functionCall = result.functionCalls[0];

    const { name, args } = functionCall;

    if (!toolFunctions[name]) {
      throw new Error(`Unknown function call: ${name}`);
    }

    // Call the function and get the response.
    const toolResponse = toolFunctions[name](args);

    const functionResponsePart = {
      name: functionCall.name,
      response: {
        result: toolResponse,
      },
    };

    // Send the function response back to the model.
    contents.push({
      role: "model",
      parts: [\
        {\
          functionCall: functionCall,\
        },\
      ],
    });
    contents.push({
      role: "user",
      parts: [\
        {\
          functionResponse: functionResponsePart,\
        },\
      ],
    });
  } else {
    // No more function calls, break the loop.
    console.log(result.text);
    break;
  }
}

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
OK. It's 25°C in London, so I've set the thermostat to 20°C.

```

Compositional function calling is a native [Live\\
API](https://ai.google.dev/gemini-api/docs/live) feature. This means Live API
can handle the function calling similar to the Python SDK.

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

```
# Light control schemas
turn_on_the_lights_schema = {'name': 'turn_on_the_lights'}
turn_off_the_lights_schema = {'name': 'turn_off_the_lights'}

prompt = """
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
  """

tools = [\
    {'code_execution': {}},\
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]}\
]

await run(prompt, tools=tools, modality="AUDIO")

```

```
// Light control schemas
const turnOnTheLightsSchema = { name: 'turn_on_the_lights' };
const turnOffTheLightsSchema = { name: 'turn_off_the_lights' };

const prompt = `
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
`;

const tools = [\
  { codeExecution: {} },\
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] }\
];

await run(prompt, tools=tools, modality="AUDIO")

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


[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

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

```
import { FunctionCallingConfigMode } from '@google/genai';

// Configure function calling mode
const toolConfig = {
  functionCallingConfig: {
    mode: FunctionCallingConfigMode.ANY,
    allowedFunctionNames: ['get_current_temperature']
  }
};

// Create the generation config
const config = {
  tools: tools, // not defined here.
  toolConfig: toolConfig,
};

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)More

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)More

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)More

```
AllowedType = (int | float | bool | str | list['AllowedType'] | dict[str, AllowedType])

```

To see what the inferred schema looks like, you can convert it using
[`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable):

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)More

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

```
# Multiple tasks example - combining lights, code execution, and search
prompt = """
  Hey, I need you to do three things for me.

    1.  Turn on the lights.
    2.  Then compute the largest prime palindrome under 100000.
    3.  Then use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024.

  Thanks!
  """

tools = [\
    {'google_search': {}},\
    {'code_execution': {}},\
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]} # not defined here.\
]

# Execute the prompt with specified tools in audio modality
await run(prompt, tools=tools, modality="AUDIO")

```

```
// Multiple tasks example - combining lights, code execution, and search
const prompt = `
  Hey, I need you to do three things for me.

    1.  Turn on the lights.
    2.  Then compute the largest prime palindrome under 100000.
    3.  Then use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024.

  Thanks!
`;

const tools = [\
  { googleSearch: {} },\
  { codeExecution: {} },\
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] } // not defined here.\
];

// Execute the prompt with specified tools in audio modality
await run(prompt, {tools: tools, modality: "AUDIO"});

```

Python developers can try this out in the [Live API Tool Use\\
notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb).

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

[Python](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#python)[JavaScript](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#javascript)More

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

Make sure the latest version of the `mcp` SDK is installed on your platform
of choice.

```
npm install @modelcontextprotocol/sdk

```

```
import { GoogleGenAI, FunctionCallingConfigMode , mcpToTool} from '@google/genai';
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// Create server parameters for stdio connection
const serverParams = new StdioClientTransport({
  command: "npx", // Executable
  args: ["-y", "@philschmid/weather-mcp"] // MCP Server
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

// Configure the client
const ai = new GoogleGenAI({});

// Initialize the connection between client and server
await client.connect(serverParams);

// Send request to the model with MCP tools
const response = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: `What is the weather in London in ${new Date().toLocaleDateString()}?`,
  config: {
    tools: [mcpToTool(client)],  // uses the session, will automatically call the tool
    // Uncomment if you **don't** want the sdk to automatically call the tool
    // automaticFunctionCalling: {
    //   disable: true,
    // },
  },
});
console.log(response.text)

// Close the connection
await client.close();

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

- Only a [subset of the OpenAPI\\
schema](https://ai.google.dev/api/caching#FunctionDeclaration) is supported.
- Supported parameter types in Python are limited.
- Automatic function calling is a Python SDK feature only.

</details>

<details>
<summary>react-agent-from-scratch-with-gemini-2-5-and-langgraph-gemin</summary>

# ReAct agent from scratch with Gemini 2.5 and LangGraph

LangGraph is a framework for building stateful LLM applications, making it a good choice for constructing ReAct (Reasoning and Acting) Agents.

ReAct agents combine LLM reasoning with action execution. They iteratively think, use tools, and act on observations to achieve user goals, dynamically adapting their approach. Introduced in ["ReAct: Synergizing Reasoning and Acting in Language Models"](https://arxiv.org/abs/2210.03629) (2023), this pattern tries to mirror human-like, flexible problem-solving over rigid workflows.

While LangGraph offers a prebuilt ReAct agent ( [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)), it shines when you need more control and customization for your ReAct implementations.

LangGraph models agents as graphs using three key components:

- `State`: Shared data structure (typically `TypedDict` or `Pydantic BaseModel`) representing the application's current snapshot.
- `Nodes`: Encodes logic of your agents. They receive the current State as input, perform some computation or side-effect, and return an updated State, such as LLM calls or tool calls.
- `Edges`: Define the next `Node` to execute based on the current `State`, allowing for conditional logic and fixed transitions.

If you don't have an API Key yet, you can get one for free at the [Google AI Studio](https://aistudio.google.com/app/apikey).

```
pip install langgraph langchain-google-genai geopy requests

```

Set your API key in the environment variable `GEMINI_API_KEY`.

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")

```

To better understand how to implement a ReAct agent using LangGraph, let's walk through a practical example. You will create a simple agent whose goal is to use a tool to find the current weather for a specified location.

For this weather agent, its `State` will need to maintain the ongoing conversation history (as a list of messages) and a counter for the number of steps taken to further illustrate state management.

LangGraph provides a convenient helper, `add_messages`, for updating message lists in the state. It functions as a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers), meaning it takes the current list and new messages, then returns a combined list. It smartly handles updates by message ID and defaults to an "append-only" behavior for new, unique messages.

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int

```

Next, you define your weather tool.

```
from langchain_core.tools import tool
from geopy.geocoders import Nominatim
from pydantic import BaseModel, Field
import requests

geolocator = Nominatim(user_agent="weather-app")

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd). Returns a list dictionary with the time and temperature for each hour."""
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return {time: temp for time, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"])}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}

tools = [get_weather_forecast]

```

Next, you initialize your model and bind the tools to the model.

```
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-2.5-pro",
    temperature=1.0,
    max_retries=2,
    google_api_key=api_key,
)

# Bind tools to the model
model = llm.bind_tools([get_weather_forecast])

# Test the model with tools
res=model.invoke(f"What is the weather in Berlin on {datetime.today()}?")

print(res)

```

The last step before you can run your agent is to define your nodes and edges. In this example, you have two nodes and one edge.
\- `call_tool` node that executes your tool method. LangGraph has a prebuilt node for this called [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).
\- `call_model` node that uses the `model_with_tools` to call the model.
\- `should_continue` edge that decides whether to call the tool or the model.

The number of nodes and edges is not fixed. You can add as many nodes and edges as you want to your graph. For example, you could add a node for adding structured output or a self-verification/reflection node to check the model output before calling the tool or the model.

```
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig

tools_by_name = {tool.name: tool for tool in tools}

# Define our tool node
def call_tool(state: AgentState):
    outputs = []
    # Iterate over the tool calls in the last message
    for tool_call in state["messages"][-1].tool_calls:
        # Get the tool by name
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # Invoke the model with the system prompt and the messages
    response = model.invoke(state["messages"], config)
    # We return a list, because this will get added to the existing messages state using the add_messages reducer
    return {"messages": [response]}

# Define the conditional edge that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    # If the last message is not a tool call, then we finish
    if not messages[-1].tool_calls:
        return "end"
    # default to continue
    return "continue"

```

Now you have all the components to build your agent. Let's put them together.

```
from langgraph.graph import StateGraph, END

# Define a new graph with our state
workflow = StateGraph(AgentState)

# 1. Add our nodes
workflow.add_node("llm", call_model)
workflow.add_node("tools",  call_tool)
# 2. Set the entrypoint as `agent`, this is the first node called
workflow.set_entry_point("llm")
# 3. Add a conditional edge after the `llm` node is called.
workflow.add_conditional_edges(
    # Edge is used after the `llm` node is called.
    "llm",
    # The function that will determine which node is called next.
    should_continue,
    # Mapping for where to go next, keys are strings from the function return, and the values are other nodes.
    # END is a special node marking that the graph is finish.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)
# 4. Add a normal edge after `tools` is called, `llm` node is called next.
workflow.add_edge("tools", "llm")

# Now we can compile and visualize our graph
graph = workflow.compile()

```

You can visualize your graph using the `draw_mermaid_png` method.

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))

```

https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png

Now let's run the agent.

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()

```

You can now continue with your conversation and for example ask for the weather in another city or let it compare it.

```
state["messages"].append(("user", "Would it be in Munich warmer?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()

```

</details>

<details>
<summary>scraping-failed</summary>

⚠️ Error scraping https://arxiv.org/pdf/2504.19678: Internal Server Error: Failed to scrape URL. (Internal server error) - Scrape resulted in unsupported file: File size exceeds 10MB - No additional error details provided.

</details>

<details>
<summary>what-is-a-react-agent-ibm</summary>

# What is a ReAct agent?

A ReAct agent is an [AI agent](https://www.ibm.com/think/topics/ai-agents) that uses the “reasoning and acting” (ReAct) framework to combine [chain of thought (CoT)](https://www.ibm.com/think/topics/chain-of-thoughts) reasoning with external tool use. The ReAct framework enhances the ability of a [large language model (LLM)](https://www.ibm.com/think/topics/large-language-models) to handle complex tasks and decision-making in [agentic workflows](https://www.ibm.com/think/topics/agentic-workflows).

First introduced by Yao and others in the 2023 paper, “ReACT: Synergizing Reasoning and Acting in Language Models,” ReAct can be understood most generally as a [machine learning](https://www.ibm.com/think/topics/machine-learning) (ML) paradigm to integrate the reasoning and action-taking capabilities of LLMs.

More specifically, ReAct is a conceptual framework for building AI agents that can interact with their environment in a structured but adaptable way, by using an LLM as the agent’s “brain” to coordinate anything from simple [retrieval augmented generation (RAG)](https://research.ibm.com/blog/retrieval-augmented-generation-RAG) to intricate [multiagent](https://www.ibm.com/think/topics/multiagent-system) workflows.

Unlike traditional artificial intelligence (AI) systems, ReAct agents don’t separate decision-making from task execution. Therefore, the development of the ReAct paradigm was an important step in the evolution of [generative AI (gen AI)](https://www.ibm.com/think/topics/generative-ai) beyond mere conversational [chatbots](https://www.ibm.com/think/topics/chatbots) and toward complex problem-solving.

ReAct agents and derivative approaches continue to power AI applications that can autonomously plan, execute and adapt to unforeseen circumstances.

## How do ReAct agents work?

The ReAct framework is inspired by the way humans can intuitively use natural language—often through our own inner monologue—in the step-by-step planning and execution of complex tasks.

Rather than implementing rule-based or otherwise predefined workflows, ReAct agents rely on their LLM’s reasoning capabilities to dynamically adjust their approach based on new information or the results of previous steps.

Imagine packing for a brief trip. You might start by identifying key considerations (“ _What will the weather be like while I’m there?_”), then actively consult external sources (“ _I’ll check the local weather forecast_”).

By using that new information (“ _It’s going to be cold_”), you determine your next consideration (“ _What warm clothes do I have?_”) and action (“ _I’ll check my closet_”). Upon taking that action, you might encounter an unexpected obstacle (“ _All of my warm clothes are in storage_”) and adjust your next step accordingly (“ _What clothes can I layer together?_”).

In a similar fashion, the ReAct framework uses [prompt engineering](https://www.ibm.com/topics/prompt-engineering) to structure an AI agent’s activity in a formal pattern of alternating thoughts, actions and observations:

- The verbalized CoT reasoning steps ( _thoughts_) help the model decompose the larger task into more manageable subtasks.

- Predefined _actions_ enable the model to use tools, make [application programming interface (API)](https://www.ibm.com/think/topics/api) calls and gather more information from external sources (such as search engines) or knowledge bases (such as an internal docstore).

- After taking an action, the model then reevaluates its progress and uses that _observation_ to either deliver a final answer or inform the next _thought_. The observation might ideally also consider prior information, whether from earlier in the model’s standard context window or from an external memory component.

Because the performance of a ReAct agent depends heavily on the ability of its central LLM to “verbally” think its way through complex tasks, ReAct agents benefit greatly from highly capable models with advanced reasoning and instruction-following ability.

To minimize cost and [latency](https://www.ibm.com/think/topics/latency), a multiagent ReAct framework might rely primarily on a larger, more performant model to serve as the central agent whose reasoning process or actions might involve delegating subtasks to more agents built using smaller, more efficient models.

### ReAct agent loops

This framework inherently creates a feedback loop in which the model problem-solves by iteratively repeating this interleaved _thought-action-observation_ process.

Each time this loop is completed—that is, each time the agent has taken an action and made an observation based on the results of that action—the agent must then decide whether to repeat or end the loop.

When and how to end the reasoning loop is an important consideration in the design of a ReAct agent. Establishing a maximum number of loop iterations is a simple way to limit latency, costs and token usage, and avoid the possibility of an endless loop.

Conversely, the loop can be set to end when some specific condition is met, such as when the model has identified a potential final answer that exceeds a certain confidence threshold.

To implement this kind of reasoning and acting loop, ReAct agents typically use some variant of _ReAct prompting_, whether in the system prompt provided to the LLM or in the context of the user query itself.

## ReAct prompting

ReAct prompting is a specific prompting technique designed to guide an LLM to follow the ReAct paradigm of _thought_, _action_ and _observation_ loops. While the explicit use of conventional ReAct prompting methods is not strictly necessary to build a ReAct agent, most ReAct-based agents implement or at least take direct inspiration from it.

First outlined in the original ReAct paper, ReAct prompting’s primary function is to instruct an LLM to follow the ReAct loop and establish which tools can be used—that is, which actions can be taken—when handling user queries.

Whether through explicit instructions or the inclusion of [few-shot](https://www.ibm.com/think/topics/few-shot-learning) examples, ReAct prompting should:

- **Guide the model to use chain of thought reasoning:** Prompt the model to reason its way through tasks by thinking step by step, interleaving thoughts with actions.

- **Define actions:** Establish the specific actions available to the model. An action might entail the generation of a specific type of next thought or subprompt but usually involves [using external tools](https://www.ibm.com/think/topics/tool-calling) or making APIs.

- **Instruct the model to make observations:** Prompt the model to reassess its context after each action step and use that updated context to inform the next reasoning step.

- **Loop:** Instruct the model to repeat the previous steps if necessary. You could provide specific conditions for ending that loop, such as a maximum number of loops, or instruct the agent to end its reasoning process whenever it feels it has arrived at the correct final output.

- **Output final answer:** Whenever those end conditions have been met, provide the user with the final output in response to their initial query. As with many uses of LLMs, as reasoning models employing chain of thought reasoning before determining a final output, ReAct agents are often prompted to conduct their reasoning process within a [“scratchpad.”](https://arxiv.org/abs/2112.00114)

A classic demonstration of ReAct prompting is the system prompt for the prebuilt ZERO\_SHOT\_REACT-DESCRIPTION ReAct agent module in [Langchain](https://www.ibm.com/think/topics/langchain)’s LangGraph. It’s called “ [zero-shot](https://www.ibm.com/think/topics/zero-shot-learning)” because, with this predefined system prompt, the LLM being used with the module does not need any further examples to behave as a ReAct agent.

```
Answer the following questions as best you can. You have access to the following tools:

Wikipedia: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.
duckduckgo_search: A wrapper around DuckDuckGo Search. Useful for when you need to answer questions about current events. Input should be a search query.
Calculator: Useful for when you need to answer questions about math.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Wikipedia, duckduckgo_search, Calculator]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
```

## Benefits of ReAct agents

The introduction of the ReAct framework was an important step in the advancement of LLM-driven [agentic workflows](https://www.ibm.com/think/topics/agentic-workflows). From grounding LLMs in real time, real-world external information through (RAG) to contributing to subsequent breakthroughs—such as [Reflexion](https://arxiv.org/abs/2303.11366), which led to modern reasoning models—ReAct has helped catalyze the use of LLMs for tasks well beyond text generation.

The utility of ReAct agents is drawn largely from some of the inherent qualities of the ReAct framework:

- **Versatility:** ReAct agents can be configured to work with a wide variety of external tools and APIs. Though [fine-tuning](https://www.ibm.com/think/topics/fine-tuning) relevant ReAct prompts (using relevant tools) can improve performance, no prior configuration of the model is required to execute [tool calls](https://www.ibm.com/think/topics/tool-calling).

- **Adaptability:** This versatility, along with the dynamic and situational nature of how they determine the appropriate tool or API to call, means that ReAct agents can use their reasoning process to adapt to new challenges. Especially when operating within a lengthy context window or augmented with external memory, they can learn from past mistakes and successes to tackle unforeseen obstacles and situations. This makes ReAct agents flexible and resilient.

- **Explainability:** The verbalized reasoning process of a ReAct agent is simple to follow, which facilitates debugging and helps make them relatively user-friendly to build and optimize.

- **Accuracy:** As the original ReAct paper asserts, chain of thought (CoT) reasoning alone has many benefits for LLMs, but also runs an increased risk of hallucination. ReAct’s combination of CoT with a connection external to information sources significantly reduces [hallucinations](https://www.ibm.com/think/topics/ai-hallucinations), making ReAct agents more accurate and trustworthy.

## ReAct agents vs. function calling

Another prominent paradigm for agentic AI is function calling, originally [introduced by OpenAI in June 2023](https://openai.com/index/function-calling-and-other-api-updates/) to supplement the agentic abilities of its [GPT models](https://www.ibm.com/think/topics/gpt).

The function calling paradigm entails [fine-tuning](https://www.ibm.com/think/topics/fine-tuning) models to recognize when a particular situation should result in a tool call and output a structured [JSON](https://www.ibm.com/docs/en/baw/24.x?topic=formats-javascript-object-notation-json-format) object containing the arguments necessary to call those functions.

Many proprietary and open source LLM families, [including IBM® Granite®](https://www.ibm.com/granite/docs/models/granite/#function-calling), Meta’s [Llama](https://www.ibm.com/think/news/meta-llama-3-2-models) series, Anthropic’s [Claude](https://www.ibm.com/think/topics/claude-ai) and [Google Gemini](https://www.ibm.com/think/topics/google-gemini), now support function calling.

Whether ReAct or function calling is “better” will generally depend on the nature of your specific use case. In scenarios involving relatively straightforward (or at least predictable) tasks, function calling can execute faster, save tokens, and be simpler to implement than a ReAct agent.

In such circumstances, the number of tokens that would be spent on a ReAct agent’s iterative loop of CoT reasoning might be seen as inefficient.

The inherent tradeoff is a relative lack of ability to customize how and when the model chooses which tool to use. Likewise, when an agent handles tasks that call for complex reasoning, or scenarios that are dynamic or unpredictable, the rigidity of function calling might limit the agent’s adaptability. In such situations, it’s often beneficial to be able to view the step-by-step reasoning that led to a specific tool call.

## Getting started with ReAct agents

ReAct agents can be designed and implemented in multiple ways, whether coded from scratch in Python or developed with the help of open source frameworks such as [BeeAI](https://research.ibm.com/blog/bee-ai-app). The popularity and staying power of the ReAct paradigm have yielded extensive literature and tutorials for ReAct agents on GitHub and other developer communities.

As an alternative to developing custom ReAct agents, many agentic AI frameworks, including BeeAI, [LlamaIndex](https://www.ibm.com/think/topics/llamaindex) and LangChain’s LangGraph, offer [preconfigured ReAct agent modules](https://github.com/i-am-bee/beeai-framework/blob/main/python/examples/agents/react.py) for [specific use cases](https://beeai.dev/agents).

</details>

<details>
<summary>what-is-ai-agent-orchestration-ibm</summary>

# What is AI agent orchestration?

[Artificial intelligence (AI)](https://www.ibm.com/think/artificial-intelligence) agent orchestration is the process of coordinating multiple specialized [AI agents](https://www.ibm.com/think/topics/ai-agents) within a unified system to efficiently achieve shared objectives.

Rather than relying on a single, general-purpose AI solution, AI agent orchestration employs a network of AI agents, each designed for specific tasks, working together to automate complex workflows and processes.

To fully understand AI agent orchestration, it's essential to first understand AI agents themselves. This involves [understanding the differences](https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai) between two key types of AI: [generative AI](https://www.ibm.com/think/topics/generative-ai), which creates original content based on a user’s prompt, and [agentic AI](https://www.ibm.com/think/insights/agentic-ai), which autonomously makes decisions and acts to pursue complex goals with minimal supervision.

AI assistants exist on a continuum, starting with rule-based chatbots, progressing to more advanced virtual assistants and evolving into generative AI and [large language model (LLM)](https://www.ibm.com/think/topics/large-language-models)-powered assistants capable of handling single-step tasks. At the top of this progression are AI agents, which operate autonomously. These agents make decisions, design workflows and use function calling to connect with external tools—such as [application programming interfaces (APIs)](https://www.ibm.com/think/topics/api), data sources, web searches and even other AI agents—to fill gaps in their knowledge. This is agentic AI.

AI agents are specialized, meaning each one is optimized for a particular function. Some agents focus on business and customer-facing tasks like billing, troubleshooting, scheduling and decision-making, while others handle more technical functions like [natural language processing (NLP),](https://www.ibm.com/think/topics/natural-language-processing) data retrieval and process automation. Advanced LLMs such as OpenAI's ChatGPT-4o or Google's Gemini often power these agents, with generative AI capabilities enabling them to create human-like responses and handle complex tasks autonomously.

Multi-agent systems (MAS) emerge when multiple AI agents collaborate, either in a structured or decentralized manner, to solve complex tasks more efficiently than a single agent might.

In practice, AI agent orchestration functions like a digital symphony. Each agent has a unique role and the system is guided by an orchestrator—either a central AI agent or framework —that manages and coordinates their interactions. The orchestrator helps synchronize these specialized agents, ensuring that the right agent is activated at the right time for each task. This coordination is crucial for handling multifaceted workflows that involve various tasks, helping ensure that processes are run seamlessly and efficiently.

For example, as part of [customer service automation](https://www.ibm.com/think/topics/customer-service-automation), the orchestrator agent (the system responsible for managing AI agents) might determine whether to engage a billing agent versus a technical support agent, helping ensure that customers receive seamless and relevant assistance. In MAS, agents might coordinate without a single orchestrator, dynamically communicating to collaboratively solve problems (see “Types of AI orchestration” below)

The benefits of AI agent orchestration are significant in industries with complex, dynamic needs such as telecommunications, banking and healthcare. By deploying specialized agents that are trained on targeted datasets and workflows, businesses can enhance [operational efficiency](https://www.ibm.com/think/topics/operational-efficiency), improve decision-making and deliver more accurate, efficient and context-aware results for both employees and customers.

## Why AI agent orchestration is important

As AI systems grow more advanced, a single AI model or agent is often insufficient for handling complex tasks. Autonomous systems frequently struggle to collaborate because they are built across multiple clouds and applications, leading to siloed operations and inefficiencies. AI agent orchestration bridges these gaps, enabling multiple AI agents to work together efficiently and ensuring that sophisticated tasks are run seamlessly.

In large-scale applications such as healthcare, finance and customer service, multiple agents often need to work together to handle different aspects of a task. For example, in healthcare, AI agents can coordinate between diagnostic tools, patient management systems and administrative workflows to streamline operations and enhance treatment accuracy. Without orchestration, these agents might work in isolation, leading to inefficiencies, redundancies or gaps in execution.

By managing interactions between multi-agent systems, orchestration helps ensure that each agent contributes effectively toward a shared goal. It optimizes workflows, minimizes errors and enhances interoperability, allowing AI systems to dynamically allocate resources, prioritize tasks and respond to changing conditions in real time. This capability is valuable in fields requiring continuous optimization such as supply chain management and personalized digital assistants.

As AI systems continue to evolve, AI agent orchestration becomes increasingly essential for unlocking their full potential.

## Types of AI agent orchestration

There are several types of AI agent orchestration. Real-world systems often combine multiple orchestration styles for more effective results.

**Centralized orchestration**: A single AI orchestrator agent acts as the "brain" of the system, directing all the other agents, assigning tasks and making final decisions. This structured approach helps ensure consistency, control and predictable workflows.

**Decentralized orchestration**: This model shifts away from a single, controlling entity, allowing MAS to function through direct communication and collaboration. Agents make independent decisions or reach a consensus as a group. This makes the system more scalable and resilient since no single failure can bring it down.

**Hierarchical orchestration**: Here, AI agents are arranged in layers, resembling a tiered command structure. Higher-level orchestrator agents oversee and manage lower-level agents, striking a balance between strategic control and task-specific execution. This allows for more organized workflows while still enabling specialized agents to operate with some autonomy. If the hierarchy becomes too rigid, adaptability can suffer.

**Federated orchestration**: This approach focuses on collaboration between independent AI agents or separate organizations, allowing them to work together without fully sharing data or relinquishing control over their individual systems. This is especially useful in situations where privacy, security or regulatory constraints prevent unrestricted data sharing, such as in healthcare, banking or cross-company collaborations.

## Comparing AI agent orchestration with related practices

**AI orchestration** manages and automates various AI components—like machine learning models, data pipelines and APIs—to help ensure that they work together efficiently within a system. It focuses on optimizing performance, automating repetitive tasks, supporting scalability and system-wide performance.

**AI agent orchestration** is a subset of AI orchestration that focuses specifically on coordinating autonomous AI agents—software entities that can make independent decisions and take actions. It helps ensure that agents collaborate effectively, assigning tasks and structuring workflows.

**Multi-agent orchestration** goes a step further, managing multiple AI agents working together on complex problems. It deals with communication, role allocation and conflict resolution to help ensure seamless collaboration between agents.

## AI agent orchestration steps

AI agent orchestration is a structured process to help ensure seamless collaboration between AI agents. The goal is to manage specialized agents effectively so they can autonomously complete tasks, share data flow and optimize workflows.

Initial steps involving design, configuration and implementation are performed by humans, including as AI engineers, developers and business strategists. Once the orchestrator agent is set up, it autonomously manages AI applications, assigning tasks, coordinating workflows and facilitating real-time collaboration.

The process generally follows these key steps:

- Assessment and planning
- Selection of specialized AI agents
- Orchestration framework implementation
- Agent selection and assignment
- Workflow coordination and execution
- Data sharing and context management
- Continuous optimization and learning

### Assessment and planning (human-driven)

Before orchestration begins, organizations assess their existing AI ecosystem and identify processes that might benefit from multi-agent orchestration. The orchestration team defines clear objectives, determines the scope of integration and selects the appropriate AI technologies.

### Selection of specialized AI agents (human-driven)

AI engineers and developers choose task-specific AI agents, such as those specializing in data analysis, automation or decision-making. These agents use gen AI and machine learning models to enhance their functions.

### Orchestration framework implementation (human-driven)

System architects integrate selected AI agents into a unified orchestration framework, establishing workflows that facilitate smooth agent-to-agent communication. This involves:

- Defining task execution sequences

- Setting up API integrations for data access

- Implementing open source orchestration tools such as IBM watsonx Orchestrate, Microsoft Power Automate and LangChain

Once this is complete, the orchestrator agent takes over real-time execution.

### Agent selection and assignment (orchestrator-driven)

The orchestrator dynamically identifies the best-suited AI agents for each task based on real-time data, workload balancing and predefined rules.

### Workflow coordination and execution (orchestrator-driven)

The orchestrator platform manages task sequencing and execution, helping to ensure smooth collaboration between agents. This includes:

- Breaking down tasks into subtasks

- Assigning the right AI agents to handle each step

- Managing inter-agent dependencies

- Integrating with external systems through API calls to access necessary data and services

### Data sharing and context management (orchestrator-driven)

To help ensure accuracy and prevent redundant work, AI agents continuously exchange information, maintaining a shared knowledge base. The orchestrator updates agents with real-time context.

### Continuous optimization and learning (orchestrator + human input)

The orchestrator monitors agent performance, detects inefficiencies and can autonomously adjust workflows. Human oversight is often required for refining orchestration strategies, retraining AI models or modifying orchestration rules for long-term improvements.

## AI agent orchestration benefits

AI agent orchestration offers several key benefits across various industries, making it a valuable approach for businesses aiming to enhance their operations and customer interactions.

**Enhanced efficiency**: Coordinating multiple specialized agents helps businesses streamline workflows, reduce redundancies and improve overall operational performance.

**Agility and flexibility**: AI agent orchestration allows organizations to adapt their operations rapidly as market conditions change.

**Improved experiences**: Orchestrated AI agents can enhance operational efficiency and provide more accurate and personalized support, resulting in more satisfying experiences for customers and employees.

**Increased reliability and fault tolerance**: The failure of one agent can be mitigated by others, which enhances system reliability and helps ensure continuous service delivery.

**Self-improving workflows**: Unlike traditional integration patterns, agent orchestration enables the creation of workflows that can autonomously adapt to new data and evolving requirements, improving over time.

**Scalability**: AI agent orchestration allows organizations to handle increased demand without compromising performance or accuracy.

## AI agent orchestration challenges

AI agent orchestration comes with several challenges, but each has potential solutions. By addressing these challenges, AI agent orchestration can be more efficient, scalable and resilient.

**Multi-agent dependencies**: When deploying multi-agent frameworks, there is a risk of malfunction. Systems built on the same foundation models may be susceptible to shared vulnerabilities, which might lead to a widespread failure of all agents that are involved or make them more prone to external attacks. This underscores the importance of data governance in building foundation models and thorough training and testing processes.

**Coordination and communication**: If agents don’t interact properly, they can end up working against each other or duplicating efforts. To prevent this, it’s important to establish clear protocols, standardized APIs and reliable message-passing systems to keep everything running smoothly.

**Scalability**: As the number of AI agents increases, maintaining system performance and manageability becomes more complex. A poorly designed orchestration system may struggle with increased workloads, leading to delays or system failures. This can be avoided by using decentralized or hierarchical orchestration models that distribute decision-making, preventing a single point of failure or congestion.

**Decision-making complexity**: In multi-agent environments, determining how tasks should be allocated and executed can become highly complex. Without a clear structure, agents may struggle to make decisions, particularly in dynamic environments where conditions frequently change. Reinforcement learning, prioritization algorithms and predefined roles can help ensure that agents can autonomously determine their tasks while maintaining efficiency.

**Fault tolerance**: What happens if an agent or the orchestrator itself fails? Fault tolerance is crucial and needs to be reinforced by designing failover mechanisms, redundancy strategies and self-healing architectures that allow the system to recover automatically without human intervention.

**Data privacy and security**: AI agents frequently process and share sensitive information, raising concerns about data security and privacy. To mitigate these risks, organizations should implement strong encryption protocols, enforce strict access controls and use federated learning techniques that allow AI models to improve collaboratively without exposing raw data.

**Adaptability and learning**: AI agents must continuously adapt to new tasks and challenges. Systems that require constant manual updates can become inefficient and costly to maintain. To enhance adaptability, machine learning techniques, continuous monitoring and feedback loops can be integrated into the orchestration process. These methods enable AI agents to refine their behavior over time, improving individual and system-wide performance without requiring frequent human intervention.

</details>

<details>
<summary>what-is-ai-agent-planning-ibm</summary>

# What is AI agent planning?

AI agent planning refers to the process by which an artificial intelligence (AI) agent determines a sequence of actions to achieve a specific goal. It involves decision-making, goal prioritization and action sequencing, often using various planning algorithms and frameworks.

[AI agent](https://www.ibm.com/think/topics/ai-agents) planning is a [module common to many types of agents](https://www.ibm.com/think/topics/components-of-ai-agents) that exists alongside other modules such as perception, reasoning, decision-making, action, memory, communication and learning. Planning works in conjunction with these other modules to help ensure that agents achieve outcomes desired by their designers.

Not all agents can plan. Unlike simple reactive agents that respond immediately to inputs, planning agents anticipate future states and generate a structured action plan before execution. This makes AI planning essential for [automation](https://www.ibm.com/think/topics/enterprise-automation) tasks that require multistep decision-making, optimization and adaptability.

## How AI agent planning works

Advances in [large language models](https://www.ibm.com/think/topics/large-language-models) (LLMs) such as OpenAI’s [GPT](https://www.ibm.com/think/topics/gpt) and related techniques involving [machine learning algorithms](https://www.ibm.com/think/topics/machine-learning-algorithms) resulted in the [generative AI](https://www.ibm.com/think/topics/generative-ai) (gen AI) boom of recent years, and further advancements have led to the emerging field of autonomous agents.

By integrating tools, APIs, hardware interfaces and other external resources, agentic AI systems are increasingly autonomous, capable of real-time decision-making and adept at problem-solving across various use cases.

Complex agents can’t act without making a decision, and they can’t make good decisions without first making a plan. Agentic planning consists of several key components that work together to encourage optimal decision-making.

### Goal definition

The first and most critical step in AI planning is defining a clear objective. The goal serves as the guiding principle for the agent’s decision-making process, determining the end state it seeks to achieve. Goals can either be static, remaining unchanged throughout the planning process, or dynamic, adjusting based on environmental conditions or user interactions.

For instance, a self-driving car might have a goal of reaching a specific destination efficiently while adhering to safety regulations. Without a well-defined goal, an agent would lack direction, leading to erratic or inefficient behavior.

If the goal is complex, agentic [AI models](https://www.ibm.com/think/topics/ai-model) will break it down into smaller, more manageable sub-goals in a process called task decomposition. This allows the system to focus on complex tasks in a hierarchical manner.

LLMs play a vital role in task decomposition, breaking down a high-level goal into smaller subtasks and then executing those subtasks through various steps. For instance, a user might ask a [chatbot](https://www.ibm.com/think/topics/chatbots) with a natural language prompt to plan a trip.

The agent would first decompose the task into components such as booking flights, finding hotels and planning an itinerary. Once decomposed, the agent can use [application programming interfaces (APIs)](https://www.ibm.com/think/topics/api) to fetch real-time data, check pricing and even suggest destinations.

### State representation

To plan effectively, an agent must have a structured understanding of its environment. This understanding is achieved through state representation, which models the current conditions, constraints and contextual factors that influence decision-making.

Agents have some built-in knowledge from their training data or [datasets](https://www.ibm.com/think/topics/dataset) representing previous interactions, but perception is required for agents to have a real-time understanding of their environment. Agents collect data through sensory input, allowing it to model its environment, along with user input and data describing its own internal state.

The complexity of state representation varies depending on the task. For example, in a chess game, the state includes the position of all pieces on the board, while in a robotic navigation system, the state might involve spatial coordinates, obstacles and terrain conditions.

The accuracy of state representation directly impacts an agent’s ability to make informed decisions, as it determines how well the agent can predict the outcomes of its actions.

### Action sequencing

Once the agent has established its goal and assessed its environment, it must determine a sequence of actions that will transition it from its current state to the desired goal state. This process, known as action sequencing, involves structuring a logical and efficient set of steps that the agent must follow.

The agent needs to identify potential actions, reduce that list to optimal actions, prioritize them and identifying dependencies between actions and conditional steps based on potential changes in the environment. The agent might allocate resources to each step in the sequence, or schedule actions based on environmental constraints.

For example, a robotic vacuum cleaner needs to decide the most effective path to clean a room, ensuring it covers all necessary areas without unnecessary repetition. If the sequence of actions is not well planned, the AI agent might take inefficient or redundant steps, leading to wasted resources and increased execution time.

The ReAct framework is a methodology used in AI for handling dynamic decision-making. In the ReAct framework, reasoning refers to the cognitive process where the agent determines what actions or strategies are required to achieve a specific goal.

This phase is similar to the planning phase in agentic AI, where the agent generates a sequence of steps to solve a problem or fulfill a task. Other emerging frameworks include ReWOO, RAISE and Reflexion, each of which has its own strengths and weaknesses.

### Optimization and evaluation

AI planning often involves selecting the most optimal path to achieving a goal, especially when multiple options are available. Optimization helps ensure that an agent's chosen sequence of actions is the most efficient, cost-effective or otherwise beneficial given the circumstances. This process often requires evaluating different factors such as time, resource consumption, risks and potential rewards.

For example, a warehouse robot tasked with retrieving items must determine the shortest and safest route to avoid collisions and reduce operational time. Without proper optimization, AI agents might execute plans that are functional but suboptimal, leading to inefficiencies. Several methods can be used to optimize decision-making, including:

#### Heuristic search

Heuristic search algorithms help agents find optimal solutions by estimating the best path toward a goal. These algorithms rely on heuristic functions—mathematical estimates of how close a given state is to the desired goal. Heuristic searches are particularly effective for structured environments where agents need to find optimal paths quickly.

#### Reinforcement learning

Reinforcement learning enables agents to optimize planning through trial and error, learning which sequences of actions lead to the best outcomes over time. An agent interacts with an environment, receives feedback in the form of rewards or penalties, and refines its strategies accordingly.

#### Probabilistic planning

In real-world scenarios, AI agents often operate in uncertain environments where outcomes are not deterministic. Probabilistic planning methods account for uncertainty by evaluating multiple possible outcomes and selecting actions with the highest expected utility.

### Collaboration

Single agent planning is one thing, but in a [multiagent system](https://www.ibm.com/think/topics/multiagent-system), AI agents must work autonomously while interacting with each other to achieve individual or collective goals.

The planning process for AI agents in a multiagent system is more complex than for a single agent because agents must not only plan their own actions but also consider the actions of other agents and how their decisions interact with those of others.

Depending on the [agentic architecture](https://www.ibm.com/think/topics/agentic-architecture), each agent in the system typically has its own individual goals, which might involve accomplishing specific tasks or maximizing a reward function. In many multiagent systems, agents need to work together to achieve shared goals.

These goals could be defined by an overarching system or emerge from the agents’ interactions. Agents need mechanisms to communicate and align their goals, especially in cooperative scenarios. This could be done through explicit messaging, shared task definitions or implicit coordination.

Planning in multiagent systems can be centralized, where a single entity or controller—likely an LLM agent—generates the plan for the entire system.

Each agent receives instructions or plans from this central authority. It can also be decentralized, where agents generate their own plans but work collaboratively to help ensure that they align with each other and contribute to global objectives, often requiring communication and negotiation.

This collaborative decision-making process enhances efficiency, reduces [biases](https://www.ibm.com/think/topics/ai-bias) in task execution, helps to avoid [hallucinations](https://www.ibm.com/think/topics/ai-hallucinations) through cross-validation and consensus-building and encourages the agents to work toward a common goal.

## After planning

The phases in agentic [AI workflows](https://www.ibm.com/think/topics/ai-workflow) do not always occur in a strict step-by-step linear fashion. While these phases are often distinct in conceptualization, in practice, they are frequently interleaved or iterative, depending on the nature of the task and the complexity of the environment in which the agent operates.

AI solutions can differ depending on their design, but in a typical [agentic workflow](https://www.ibm.com/think/topics/agentic-workflows), the next phase after planning is action execution, where the agent carries out the actions defined in the plan. This involves performing tasks and interacting with external systems or knowledge bases with [retrieval augmented generation (RAG)](https://www.ibm.com/think/topics/retrieval-augmented-generation), tool use and function calling ( [tool calling](https://www.ibm.com/think/topics/tool-calling)).

Building [AI agents](https://www.ibm.com/ai-agents) for these capabilities might involve [LangChain](https://www.ibm.com/think/topics/langchain). Python scripts, JSON data structures and other programmatic tools enhance the AI’s ability to make decisions.

After executing plans, some agents can use memory to learn from their experiences and iterate their behavior accordingly.

In dynamic environments, the planning process must be adaptive. Agents continuously receive feedback about the environment and other agents’ actions and must adjust their plans accordingly. This might involve revising goals, adjusting action sequences, or adapting to new agents entering or leaving the system.

When an agent detects that its current plan is no longer feasible (for example, due to a conflict with another agent or a change in the environment), it might engage in replanning to adjust its strategy. Agents can adjust their strategies using [chain of thought](https://www.ibm.com/think/topics/chain-of-thoughts) reasoning, a process where they reflect on the steps needed to reach their objective before taking action.

</details>
