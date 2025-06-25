# Research based on provided article guidelines

## Research Results

---

<details>
<summary>What are the fundamental components and step-by-step implementation patterns for building modular LLM workflows, such as prompt chaining and routing, using base LLM APIs (e.g., OpenAI Chat Completions, Gemini, Claude)?</summary>

### Source: https://latitude-blog.ghost.io/blog/5-patterns-for-scalable-llm-service-integration/
The pipeline workflow pattern is a fundamental approach for building modular LLM workflows. It organizes LLM operations into sequential stages, with each stage responsible for a specific task such as data cleaning, prompt engineering, model inference, or output formatting. This modular design allows each stage to operate independently, enabling updates or adjustments to individual components without disrupting the entire workflow. This independence is particularly beneficial for integrating third-party tools, such as external APIs, databases, or analytics services, while ensuring the rest of the system remains unaffected.

The pipeline workflow is especially suitable for batch processing and parallel tasks, as each stage can be scaled independently. For example, in large-scale deployments like Uber's QueryGPT, the pipeline integrates retrieval-augmented generation (RAG), LLMs, and vector databases to efficiently process over 1.2 million queries each month. This modularity and scalability help organizations allocate resources to bottleneck stages and improve overall efficiency. The growing enterprise AI market underlines the need for such scalable and modular workflow patterns as companies move from experimentation to fully operational AI systems.

-----

### Source: https://www.modular.com/ai-resources/enhancing-llm-workflows-with-function-calling-best-practices-and-use-cases
Function calling is a key methodology for enhancing LLM workflows, serving as a bridge between the reasoning abilities of large language models and real-world applications. By leveraging function calling, developers can modularize workflow steps, allowing the LLM to decide when and how to invoke external functions or APIs during the processing of a prompt. This approach supports the construction of composable workflows, such as prompt chaining (where the output of one model call serves as the input to the next) and dynamic routing (where the LLM determines which function or API to use based on context).

Best practices include clearly defining the schema for function calls, maintaining separation of concerns between LLM reasoning and external logic, and ensuring robust error handling between workflow components. This methodology allows developers to build more reliable and extensible modular workflows using base LLM APIs like OpenAI Chat Completions, Gemini, or Claude.

-----

### Source: https://langchain-ai.github.io/langgraph/tutorials/workflows/
Workflows in the context of LLMs refer to systems in which LLMs and tools are orchestrated through predefined code paths. This orchestration enables modular composition, where each step in the workflow represents a distinct operation—such as prompt generation, external tool invocation, or data transformation. Workflow patterns like prompt chaining involve sequentially passing data between these steps, while routing enables conditional branching based on intermediate results or context.

In these modular workflows, the fundamental components include:
- Defined workflow steps (e.g., prompt templates, tool calls, data preprocessors)
- Orchestration logic (defining execution order and conditions)
- Routing mechanisms (to direct data or tasks to the appropriate component based on logic or LLM output)

Such patterns facilitate the creation of robust and flexible LLM applications using base APIs and predefined workflow definitions.

-----

### Source: https://www.tryhamilton.dev/tutorials-applications/llm-workflow
Hamilton provides practical tools for building modular LLM workflows, emphasizing clear separation of workflow stages. The platform supports common patterns such as:
- Sequential workflows, where each step (prompt creation, LLM inference, post-processing) is a distinct function.
- Branching and conditional logic, enabling routing based on the content or structure of intermediate results.
- Composition of small, reusable components that can be chained or combined to form larger workflows.

By structuring workflows in this way, developers can enhance maintainability, testability, and extensibility. These modular patterns are implemented using base LLM APIs, making it straightforward to adopt best practices for prompt chaining, output routing, and integration with external data sources or services.

-----

</details>

---

<details>
<summary>Why is breaking complex tasks into multiple chained LLM calls often more effective than using a single, large LLM call? What are the main benefits and challenges of this approach in terms of modularity, accuracy, debugging, and costs?</summary>

### Source: https://substack.com/home/post/p-164219315
Breaking complex tasks into multiple chained LLM calls is primarily justified by the need for specialization. Each segment of a chain can leverage a different model or configure the same model differently to address distinct sub-tasks. This approach is useful when a task can be divided into clearly discrete sub-tasks, especially if different expertise or modalities are needed (e.g., image processing, then reasoning, then code generation). Chaining is particularly advantageous if a single LLM struggles with a specific sub-task, as specialized models can significantly improve overall system performance.

However, this comes with notable challenges:
- **Latency:** Each model invocation adds inference and data transfer time.
- **Operational Overhead:** Managing multiple models, their versions, and configurations can increase complexity.
- **Debugging Challenges:** Tracing errors through a sequence is harder; errors in an upstream model can propagate downstream, making root-cause analysis complex.
- **Error Propagation:** Failures can cascade through the chain unless robust error handling is implemented.
- **Interface Contracts:** Data formats between models must be precisely defined and maintained, as changes can break the system.

The recommendation is to default to a single-model approach and only introduce chaining when the benefits of modularity, specialization, and accuracy clearly outweigh the increased complexity and operational burden.

-----

### Source: https://blog.promptlayer.com/what-is-prompt-chaining/
Prompt chaining involves decomposing a complex task into a series of smaller, interconnected prompts, each feeding into the next. This structured approach allows LLMs to follow a step-by-step reasoning process, leading to more accurate and comprehensive results.

Key benefits include:
- **Handling Context Limitations:** LLMs have restricted context windows; breaking tasks into steps ensures each prompt remains within manageable context size.
- **Reducing Hallucinations:** By explicitly guiding the LLM through each step, prompt chaining maintains relevant context and decreases the risk of generating outputs inconsistent with the task.
- **Easier Debugging:** Segmenting tasks into smaller parts allows for straightforward identification and correction of errors, improving the reliability of LLM-driven applications.

Overall, prompt chaining increases system modularity, enhances accuracy, and simplifies debugging, while also addressing some of the primary weaknesses of single-call LLM approaches.

-----

</details>

---

<details>
<summary>How can conditional logic and routing be integrated into LLM-powered workflows to enable dynamic, context-driven handling of user queries or tasks? What are practical example architectures and code patterns for implementing this in Python?</summary>

### Source: https://dev.to/jamesli/building-intelligent-llm-applications-with-conditional-chains-a-deep-dive-430a
This source emphasizes the importance of conditional chains in building robust LLM-powered applications. Conditional chains enable dynamic routing strategies that allow applications to choose different processing paths based on context, user input, or system state. Key recommendations include:

- **Route Design Principles**: Focus each route on a specific function, implement clear fallback paths for error handling or ambiguous cases, and monitor route performance with metrics.
- **Error Handling Guidelines**: Use graduated fallback strategies, comprehensive error logging, and alerting for critical failures to ensure system resilience.
- **Performance Optimization**: Cache common routing decisions, utilize concurrent processing when possible, and continually monitor and adjust routing thresholds to balance performance and cost.

The article concludes that conditional logic and routing are critical for context-driven workflows, enabling graceful degradation, robust error management, and optimized performance in LLM applications.

-----

### Source: https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Conditional_Router_Agent_Workflow.ipynb
This practical notebook demonstrates a "Conditional Router Agent Workflow" in Python, where an agent selects between multiple routes—including different LLMs or prompts—based on input characteristics. The code pattern typically involves:

- Using a lightweight classifier (could be rule-based, a small model, or keyword matching) to determine the intent or task type of the incoming user query.
- Based on the classification, dynamically choosing which LLM or prompt chain should handle the request.
- Implementing the router agent as a function or class that encapsulates this conditional logic.
- Example code might look like:
  ```python
  def router_agent(user_input):
      if is_translation_task(user_input):
          return translation_llm(user_input)
      elif is_summary_task(user_input):
          return summary_llm(user_input)
      else:
          return default_llm(user_input)
  ```
This architecture allows modular expansion—new task types or LLMs can be added to the router logic as needed.

-----

### Source: https://langchain-ai.github.io/langgraph/tutorials/workflows/
This source distinguishes between "workflows" (predefined code paths) and "agents" (dynamic, LLM-directed logic). In LLM-powered workflows, conditional logic is used to orchestrate which tools or models are called at each step, based on the evolving context or outputs from prior steps. This enables:

- Dynamic tool and model selection within a workflow,
- Context-driven branching,
- State management so that each model/tool has the necessary context for accurate responses.

Workflows can be implemented as directed graphs, where each node represents a decision point or task, and conditional logic determines the path through the graph.

-----

### Source: https://python.langchain.com/docs/how_to/routing/
LangChain provides concrete patterns for routing in Python LLM workflows. Two key methods are:

- **RunnableLambda (recommended)**: This approach uses a function to return the appropriate runnable (chain, tool, or model) based on the current input or state. Example:
  ```python
  def route_chain(input):
      if is_langchain_question(input):
          return langchain_chain
      elif is_anthropic_question(input):
          return anthropic_chain
      else:
          return default_chain
  routed = RunnableLambda(route_chain)
  ```
- **RunnableBranch (legacy)**: An earlier approach using explicit condition-action branches.

Routing enables non-deterministic chains, where the output of one step defines the next step, allowing for highly dynamic, context-aware workflows. This is especially useful for applications needing to switch between different LLMs, prompt templates, or tools based on user queries.

-----

### Source: https://portkey.ai/blog/task-based-llm-routing
This blog highlights "task-based LLM routing," where each incoming request is directed to the most suitable LLM based on the identified task. Key implementation details include:

- **Task Classification**: Use keyword matching, metadata tags, or a fast classification model to determine the type of task (e.g., summarization, translation, sentiment analysis).
- **Dynamic Routing**: After classification, route the query to the best-fit LLM or prompt chain for that task.
- **Robustness**: Plan for failures by defining fallback models for each task type and implementing retry logic.
- **Observability**: Log which model handled each task, the associated cost, response latency, and fallback usage. This observability is crucial for tuning and improving the routing logic over time.

This architecture supports both simple and advanced routing strategies and is designed for continuous improvement based on real-world data.

-----

</details>

---

<details>
<summary>What is the orchestrator-worker pattern in the context of LLM applications, and when should it be used over simpler chaining or routing approaches? How does it support the creation of flexible, agentic workflows?</summary>

### Source: https://javaaidev.com/docs/agentic-patterns/patterns/orchestrator-workers-workflow/
The Orchestrator-Workers Workflow pattern is a design where a central LLM (orchestrator) dynamically determines the best approach to complete a given task by selecting and coordinating various specialized agents or tools (workers). In this setup, all possible agents are registered as tools, and the orchestrator decides which tools to invoke for each subtask. This pattern is particularly effective when integrated with the Agent-as-Tool approach.

Implementing this pattern involves carefully crafted prompt templates and the registration of agents as tools. The orchestrator typically employs a reasoning model (such as DeepSeek R1 or OpenAI o1), which acts as the planner for task execution. This reasoning model is responsible for breaking down complex tasks into appropriate subtasks, which are then executed by standard models (workers), such as GPT-4o or GPT-4o-mini. The orchestrator’s use of a reasoning model simplifies the prompt engineering process, allowing for the handling of highly complex workflows.

A practical example of this pattern is incident management: the orchestrator uses workers to collect information from logs, metrics, traces, deployment history, and git commits. The orchestrator then synthesizes this information to identify potential causes of an outage and generates a report for developers. This approach is preferred over simpler chaining or routing when tasks require dynamic decomposition, flexible selection of tools, or synthesis of results from multiple sources. The orchestrator-worker pattern supports the creation of agentic workflows by enabling dynamic planning, execution, and result synthesis tailored to the specific requirements of each task.

### Source: https://latitude-blog.ghost.io/blog/5-patterns-for-scalable-llm-service-integration/
The Orchestrator-Worker pattern centralizes task management by delegating specific jobs to specialized workers. This approach helps balance performance, cost, and complexity in LLM service integration. It is most effective when the workflow involves multiple, variable, or interdependent tasks that require coordinated execution.

The orchestrator acts as a central brain that decides how to break down a user request, assigns subtasks to the most suitable workers, and then aggregates the results. This architecture is more flexible and scalable than simple chaining or routing, as it allows the orchestrator to dynamically determine the number and type of workers needed based on the task at hand.

You should use the orchestrator-worker pattern over simpler approaches when the workflow is complex, requires dynamic task decomposition, or needs to adapt to changing requirements. It supports flexible, agentic workflows by enabling the orchestrator to make intelligent decisions about task delegation and result synthesis, rather than relying on predefined chains or static routing logic.

### Source: https://langchain-ai.github.io/langgraphjs/tutorials/workflows/
In the orchestrator-workers workflow, a central LLM dynamically breaks down incoming tasks, delegates subtasks to specialized worker LLMs, and synthesizes their results to produce a final output. This pattern is well-suited for scenarios where tasks are complex, require coordination, or involve multiple data sources or processing steps.

The orchestrator is responsible for planning and managing the workflow, ensuring that each worker LLM is assigned tasks according to its expertise. The orchestrator also handles the integration of results from all workers, providing a cohesive and comprehensive response to the user’s request.

This pattern should be used over simpler chaining or routing approaches when the workflow involves dynamic, context-dependent task decomposition or when the number and nature of required subtasks cannot be predetermined. The orchestrator-worker pattern supports flexible, agentic workflows by allowing the orchestrator to adaptively manage task execution and result synthesis, making the system more robust and versatile.

### Source: https://docs.praison.ai/docs/features/orchestrator-worker
The Agentic Orchestrator Worker pattern involves a central orchestrator directing multiple worker LLMs to perform subtasks and synthesizing their outputs to deliver complex, coordinated operations. The orchestrator is responsible for breaking down the main task, assigning subtasks to the most appropriate workers, and then combining the results.

This pattern is especially useful for workflows that require the integration of multiple specialized agents or tools, where the orchestrator can dynamically adjust task assignments based on real-time requirements. It supports flexible and agentic workflows by allowing the orchestrator to make context-aware decisions about which workers to use and how to combine their outputs, leading to more adaptable and intelligent systems.

You should use the orchestrator-worker pattern over simpler chaining or routing when the workflow is complex, requires dynamic task management, or needs to coordinate between multiple specialized agents. The pattern enables the creation of robust, flexible, and intelligent workflows that can adapt to a wide range of scenarios.

</details>

---

<details>
<summary>What best practices and common pitfalls should AI engineers consider when designing, implementing, and debugging LLM workflow systems—particularly regarding prompt engineering, error handling, and optimization for cost, performance, and maintainability?</summary>

### Source: https://palantir.com/docs/foundry/aip/best-practices-prompt-engineering/
Palantir emphasizes the importance of prompt engineering for LLM workflow systems, outlining several best practices:

- **Prompt Clarity**: Ensure prompts are clear and unambiguous to reduce variability and improve output accuracy.
- **Specificity**: Detailed prompts yield more relevant and useful outputs compared to vague instructions.
- **Contextual Information**: Providing sufficient context within prompts improves the model’s ability to generate accurate responses.
- **Testing and Iteration**: Regularly test and iterate on prompts, as even small wording changes can significantly alter results.
- **Structured Output**: Request outputs in structured formats (e.g., JSON) to facilitate downstream parsing and integration.
- **Continuous Learning**: Stay informed about evolving prompt strategies to maintain prompt quality and output accuracy.

These practices are essential for optimizing performance and maintainability, and they help avoid common pitfalls such as ambiguous prompts, inconsistent formatting, and over-reliance on default model behaviors.

-----

### Source: https://savaslabs.com/blog/best-practices-llm-powered-solutions
Savas Labs provides a comprehensive set of best practices for integrating LLMs into workflow systems:

- **Selective Implementation**: Use LLMs only where traditional algorithms fall short, as conventional code is generally cheaper and faster for well-defined tasks.
- **Hybrid Systems**: Combine LLMs with rule-based or traditional systems to leverage the strengths of both; this can improve reliability and reduce costs.
- **Continuous Evaluation**: Regularly assess LLM-based components for performance and alignment with business goals.
- **Structured Output**: Instruct LLMs to generate outputs in predefined formats, making them easier to parse and integrate.
- **Function Calling**: Enable LLMs to call external functions or APIs for enhanced versatility; provide clear descriptions of available tools to ensure correct usage.
- **Reproducible Outputs**: Where possible, introduce controls (such as temperature settings or seeding) to increase determinism in LLM responses.
- **Caching**: Implement prompt and response caching to improve speed and reduce operational costs, especially for frequently-used workflows.

Neglecting these practices can lead to excessive costs, unpredictable outputs, increased maintenance burden, and integration difficulties.

-----

### Source: https://www.datadoghq.com/blog/llm-evaluation-framework-best-practices/
Datadog underlines the necessity of robust evaluation and monitoring for LLM workflows:

- **Metric Selection**: Choose evaluation metrics tailored to your use case—accuracy, latency, cost, and user satisfaction can all be relevant.
- **Pre-production Evaluation**: Conduct thorough evaluations before deployment to uncover performance issues and identify prompt weaknesses.
- **Production Monitoring**: Continuously monitor evaluations in live systems to detect drift, regressions, or emerging errors.
- **Optimization**: Use evaluation data to optimize costs, performance, and reliability. This includes refining prompts, tuning system parameters, and identifying bottlenecks.

A common pitfall is failing to monitor LLMs in production, which can result in undetected errors, degraded performance, or escalating costs. Datadog’s approach emphasizes the importance of ongoing assessment for maintainability and long-term optimization.

-----

### Source: https://stackoverflow.blog/2024/02/07/best-practices-for-building-llms/
Stack Overflow discusses broader system-level best practices and pitfalls:

- **Unified vs. Specialized Models**: Unified models can serve multiple tasks but require balanced, representative training data for each supported task; otherwise, task performance may suffer.
- **Diverse Model Selection**: Employing a diverse set of LLMs can improve focus and application performance—use heuristics or automation to route queries to the most appropriate model.
- **Evaluation Frameworks**: Use frameworks like EleutherAI’s Language Model Evaluation Harness for systematic evaluation and insight into model performance.
- **Balancing Cost and Accuracy**: Make final decisions about model selection at query time, factoring in accuracy, latency, and cost considerations.

Pitfalls include underrepresentation of certain tasks in unified models, overfitting to specific datasets, and lack of automated query routing to optimize for cost and performance.

-----

### Source: https://www.modular.com/ai-resources/enhancing-llm-workflows-with-function-calling-best-practices-and-use-cases
Modular highlights best practices for function calling within LLM workflows:

- **Dynamic Integration**: Function calling allows LLMs to interact with external systems (APIs, databases, tools) in real time, supporting more complex and context-aware workflows.
- **Clear Function Descriptions**: Supply detailed usage instructions and examples so LLMs can invoke functions correctly and reliably.
- **Validation and Error Handling**: Implement robust validation and error-handling routines to manage failed calls or unexpected outputs gracefully.
- **Security and Permissions**: Enforce strict access controls and input validation to prevent unauthorized actions or data leaks when LLMs call sensitive functions.

Common pitfalls include providing insufficient or ambiguous function documentation, lack of error handling leading to system failures, and inadequate security controls, which can all compromise performance and maintainability.

</details>

---

<details>
<summary>What are the most common failure modes or bugs encountered by beginners when chaining multiple LLM calls or implementing routing logic (e.g., with base OpenAI or Gemini Python APIs), and how can these issues be diagnosed and fixed?</summary>

### Source: https://platform.openai.com/docs/guides/text
When chaining multiple LLM calls or implementing routing logic using the OpenAI Python API, beginners often encounter several common failure modes and bugs:

- Incorrect prompt formatting: Failing to structure prompts as expected by the model can lead to non-deterministic or irrelevant outputs. Beginners sometimes omit message arrays or use incorrect keys in the input structure, resulting in errors or unexpected responses.
- Misuse of input parameters: Not understanding or misconfiguring parameters such as `model`, `instructions`, or `input`. For example, using an unavailable model name or missing required fields will cause the API to reject the request.
- Response parsing errors: LLM outputs are often unstructured text. Beginners may assume JSON output without enforcing it in the prompt or fail to handle edge cases in parsing, causing bugs downstream.
- Synchronous/asynchronous handling: Failing to properly await responses when chaining calls, especially when using asynchronous libraries or frameworks, can result in incomplete or out-of-order results.
- Error handling and retry logic: Not checking for API errors (rate limits, server errors, malformed requests) or failing to implement retry logic can cause the chain to break unexpectedly.

To diagnose and fix these issues:
- Always consult the API documentation to ensure correct parameter usage and prompt formatting.
- Use explicit instructions in prompts to guide the model’s output format.
- Implement robust error checking for API responses and handle HTTP exceptions.
- Log requests and responses at each step to debug the flow and detect where the chain breaks or produces unexpected results.
- Test each step individually before chaining them together to isolate and fix bugs early.

These practices help ensure reliable chaining and routing logic in applications using the OpenAI API.

-----

### Source: https://platform.openai.com/docs/api-reference
According to the OpenAI API Reference, common technical pitfalls when chaining calls or implementing routing logic include:

- Incorrect model specification: Using an invalid or deprecated model ID in the request can result in immediate errors. Developers should ensure the model parameter (e.g., `gpt-4o`, `gpt-3.5-turbo`) matches an available model.
- Conversation state mishandling: For multi-turn workflows, not correctly passing the unique ID of the previous response (`parent_response_id` or similar) can break the conversation state, leading to incoherent or contextless outputs.
- Template misconfiguration: When using prompt templates, failing to correctly reference template variables or not matching the template structure expected by the API can cause runtime errors or misrouted logic.
- Parallel tool calls: When enabling parallel tool calls, not handling their responses properly or assuming synchronous behavior can introduce race conditions or missed outputs.
- Service tier and rate limits: Requests may be throttled or rejected if service tier settings are misconfigured or if rate limits are exceeded. This is especially likely in routing scenarios or high-frequency chaining.
- Missing or malformed parameters: Omitting required fields or sending malformed JSON objects leads to HTTP 400 errors.

To diagnose and fix:
- Validate all request parameters and payloads before sending.
- Carefully track conversation state for multi-turn interactions.
- Check API error responses for informative messages that indicate missing fields, rate limits, or invalid models.
- Log and monitor all API requests and responses, especially in chained/routed workflows, to quickly identify where failures occur.

-----

### Source: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-guide
When implementing routing logic and chaining LLM calls, Microsoft’s Azure OpenAI Gateway guide highlights several potential issues:

- Routing to unhealthy or overloaded endpoints: If routing logic does not account for endpoint health, requests might be sent to unresponsive or overloaded deployments, causing failures or degraded performance.
- Inadequate rate limiting: Without proper rate limiting, applications may exceed API quotas, resulting in throttling or dropped requests.
- Lack of monitoring and observability: Insufficient monitoring makes it difficult to diagnose where in the routing or chaining logic failures occur, or to distinguish between application bugs and platform issues.
- Poor error recovery: Failing to implement circuit breaking or fallback strategies can cause cascading failures when a particular model or endpoint goes down.
- Message queue mismanagement: When using asynchronous routing (e.g., queue-based load leveling), mishandling message queues can result in lost or delayed requests.

To diagnose and fix:
- Use health checks and circuit breakers in routing logic to avoid unhealthy endpoints.
- Employ rate limiting to control pressure on the LLM services.
- Integrate monitoring for usage, costs, and request/response logs.
- Use message queues judiciously and ensure proper acknowledgment and error handling.

These practices help maintain reliability and observability when orchestrating complex LLM workflows.

-----

</details>

---

<details>
<summary>What are the best practices for securely managing and loading API keys or secrets (like GOOGLE_API_KEY) in shared environments such as Google Colab notebooks, specifically to avoid accidentally exposing credentials?</summary>

### Source: https://drlee.io/how-to-use-secrets-in-google-colab-for-api-key-protection-a-guide-for-openai-huggingface-and-c1ec9e1277e0
To securely manage API keys in Google Colab, it is crucial to avoid making the secret values visible, especially during screen sharing or recording. Access management is also key, ensuring that API keys are not directly embedded in code. This source emphasizes the importance of keeping API keys confidential and secure, highlighting best practices to prevent accidental exposure.

### Source: https://support.google.com/googleapi/answer/6310037
Google provides guidelines for securely using API keys. It is advised not to embed API keys directly in code and avoid storing them in files within the application's source tree. API keys should be restricted to be used by only the IP addresses or services that need them. This approach helps prevent unauthorized access and reduces the risk of API key exposure.

### Source: https://www.strac.io/blog/sharing-and-storing-api-keys-securely
Storing API keys securely involves several best practices. It is recommended to store keys away from code, preferably in environmental variables. This keeps sensitive information separate from the main codebase and reduces the risk of accidental exposure in public repositories. Secure storage solutions with encryption are also recommended. Regularly rotating API keys (e.g., every 30 days) and deleting unused keys can minimize potential attack vectors. Additionally, implementing a principle of least privilege by granting API keys only the necessary permissions helps safeguard systems against unauthorized access.

</details>

---

<details>
<summary>How do modern LLMs handle intermediate output formats (e.g., JSON, structured lists) in chained workflows, and what are effective tips for handling cases where the model produces malformed responses?</summary>

### Source: https://platform.openai.com/docs/guides/structured-outputs
Modern LLMs, especially those offered by OpenAI, provide robust support for structured outputs through features like "Structured Outputs," which is an evolution of the earlier "JSON mode." While both features ensure that valid JSON is produced, only Structured Outputs guarantee strict adherence to a user-defined schema. This is essential in workflows where intermediate outputs (such as JSON or structured lists) are chained between tasks or systems. Structured Outputs help ensure that the generated content matches both the format and the schema required for downstream processing, reducing the risk of malformed or incomplete outputs. This schema adherence is crucial for reliable automation and integration in complex pipelines.

-----

### Source: https://www.vellum.ai/llm-parameters/structured-outputs
Vellum AI details the use of "Structured Outputs," a feature that allows developers to provide a JSON schema to which the LLM must adhere. By including this schema in the API call (using the response_format parameter), the model is guided to generate outputs that precisely match the expected structure. This is especially useful for intermediate results in chained workflows, as it allows for easy parsing and integration into user interfaces or subsequent system components. The process involves:

1. Defining the desired JSON schema.
2. Including the schema in the API call with response_format and strict validation.
3. Parsing the output, which is now guaranteed to match the schema, reducing the risk of malformed data.

This structured approach minimizes the need for complex post-processing or error correction, as the model output is directly validated against the schema before being utilized in downstream tasks.

-----

### Source: https://arxiv.org/html/2408.11061v1
The referenced research investigates the ability of LLMs to follow JSON response format instructions, particularly in zero-shot settings (i.e., without fine-tuning or structured decoding). The study introduces benchmarks that test LLMs on their capability to generate correctly structured JSON outputs, including lists and composite objects. It finds that while structured decoding methods (such as DOMINO) can enforce correct formatting, they may introduce latency and integration complexity.

A key finding is that, when relying solely on prompt instructions and zero-shot learning, LLMs can still make mistakes—such as producing syntactically incorrect or schema-inconsistent JSON—resulting in parse failures. The paper thus underscores the importance of both structured decoding methods and robust validation/parsing in the workflow. For error handling, the recommendation is to verify that the output can be parsed into the expected structure (correct keys and value types) and to apply correction or retry strategies if malformed responses are detected.

-----

</details>

---

<details>
<summary>What are the latest best practices for requesting and reliably parsing structured outputs (e.g., JSON or lists) from Gemini and Claude APIs, especially when chaining multiple LLM calls and handling malformed responses?</summary>

### Source: https://ai.google.dev/gemini-api/docs/structured-output
The Gemini API allows you to configure structured outputs for precise information extraction and standardization, which is especially useful for further automated processing such as building databases. Gemini can natively generate JSON or enum values as outputs. To do this reliably, you define the expected output structure using the `responseSchema` parameter, which takes a `Schema` object—a subset of the OpenAPI 3.0 schema. This schema specifies types, properties, required fields, enumerations, and property ordering. By using a well-defined schema, you help ensure that the model's output is both predictable and machine-parseable. This approach minimizes the risk of malformed responses, streamlining downstream parsing and validation. When chaining multiple LLM calls, consistently applying and validating against these schemas at each step helps maintain data integrity and reduces propagation of errors caused by malformed outputs.

-----

### Source: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output
Vertex AI on Google Cloud offers structured output functionality, also referred to as "controlling the generated output" of generative AI models. This feature allows developers to specify the desired format of responses, such as JSON, to facilitate reliable automated parsing and integration. By setting clear output constraints, you can ensure the generative model consistently produces responses that align with your application's requirements. This is particularly important when chaining multiple model calls, as it allows for robust validation and error handling between steps. The documentation recommends always validating the model's output against the expected schema and implementing fallback or correction routines for handling malformed or unexpected responses.

-----

### Source: https://github.com/googleapis/python-genai/issues/460
Gemini's structured output system supports a subset of the OpenAPI 3.0 schema, and recent updates (as of March 2025) have improved support for features like `anyOf`, which allows for union types in schema definitions. This enhancement increases flexibility in defining what constitutes a valid response, making it easier to handle complex data structures and reducing the likelihood of errors during parsing. The use of OpenAPI-style schemas enables systematic validation of outputs and more robust chaining in multi-step workflows, as each response can be checked against the schema before progressing to the next LLM call.

-----

### Source: https://dylancastillo.co/posts/gemini-structured-outputs.html
Gemini offers three primary methods for generating structured outputs:

- **Forced function calling (FC):** Forces the model to generate outputs matching function argument structures, creating JSON that aligns with specified parameters. However, this method may not be suitable for chain-of-thought reasoning and chaining multiple model calls.
- **Schema in prompt (JSON-Prompt):** Embeds a JSON schema directly in the prompt and requests output in `application/json` format. This approach gives some control over output structure.
- **Schema in model configuration (JSON-Schema):** Provides the schema in the model configuration and specifies `application/json` as the desired MIME type. This is the most reliable method for controlled generation and is recommended for use in chained LLM workflows, as it ensures the output strictly conforms to the predefined schema.

The article emphasizes that including schemas in the model configuration (JSON-Schema) is superior for ensuring reliable, parseable outputs, especially when chaining LLM calls. This method reduces the risk of malformed responses and enables seamless automated parsing and downstream processing.

-----

### Source: https://www.youtube.com/watch?v=npQx-11SwqU
A practical tutorial outlines how to implement structured outputs in APIs powered by Gemini AI on Google Cloud Platform. The structured output approach yields several benefits:

- Easier and more reliable parsing of API responses.
- Consistent data formats that facilitate validation and integration with downstream systems.
- Enhanced scalability and compatibility, as structured data is easier to manage and process programmatically.

The tutorial demonstrates step-by-step how to build and deploy an API that outputs structured JSON using Gemini AI, highlighting the importance of structured output for robust API development and reliable automation in real-world applications.

-----

</details>

---

<details>
<summary>How can API keys (especially GOOGLE_API_KEY or OpenAI API keys) be safely and securely managed when running LLM workflows in Colab or other shared environments, including strategies to avoid accidental exposure?</summary>

### Source: https://drlee.io/how-to-use-secrets-in-google-colab-for-api-key-protection-a-guide-for-openai-huggingface-and-c1ec9e1277e0
This source provides a step-by-step guide on securing API keys in Google Colab using the built-in Secrets feature. Key points include:
- Access the "Secrets" feature in Colab to add API keys securely.
- When adding a secret, you input its name and value. The name is permanent, but the value can be changed.
- You decide on a per-notebook basis whether a secret is accessible, allowing fine-grained sharing control.
- Use secrets in code by importing `userdata` from `google.colab` and retrieving the secret with `userdata.get('<secret_name>')`.
- If the secret is numeric, manually convert it from string to the required type.
- Secrets can be shared across notebooks, but access must be explicitly granted.
- For libraries expecting environment variables, import the secret first, then set the environment variable in code to avoid hard-coding sensitive values.
This approach prevents accidental exposure, such as printing secrets in output cells or leaking them if notebooks are shared or published.

-----

### Source: https://colab.research.google.com
This official Colab documentation introduces best practices for working with API keys, such as:
- Using the built-in "Secrets" manager to store and retrieve sensitive keys, rather than hard-coding them in notebooks.
- Encouraging separation of credentials from code to prevent accidental exposure when sharing notebooks.
- Recommending the use of environment variables or secure storage utilities provided by Colab for workflow integration with APIs like Google or OpenAI.
These practices ensure that API keys are not visible in shared or public code, reducing the risk of unauthorized access.

-----

### Source: https://labs.thinktecture.com/secrets-in-google-colab-the-new-way-to-protect-api-keys/
This source details the new "Colab Secrets" feature for protecting API keys:
- Navigate to the Secrets section in Colab to add a secret by specifying a unique name and its value.
- The global list of secrets is accessible in all notebooks, but you must toggle access for each notebook individually.
- Retrieve secrets in code with:
  ```python
  from google.colab import userdata
  my_secret_key = userdata.get('<name_of_your_secret>')
  ```
- For environment variable compatibility, manually set environment variables in code after retrieving the secret.
- Avoid exposing secrets by never hard-coding them or displaying them in notebook output cells.
- Grant access to secrets only for notebooks that require them, minimizing the exposure risk even within the same Colab environment.
This method addresses the risk of accidental exposure when notebooks are shared, published, or collaborated on.

-----

### Source: https://help.openai.com/en/articles/5008148-can-i-share-my-api-key-with-my-teammate-coworker
OpenAI’s official guidance on API key management emphasizes:
- Never share personal API keys, even with trusted team members, as this can compromise account security and obscure usage tracking.
- Use project-based API keys for collaboration: create distinct projects in the OpenAI dashboard, assign members, and generate keys with isolated rate limits and spend controls.
- Store API keys securely using environment variables or secret management tools, never in plaintext or committed to code repositories.
- Rotate keys promptly if exposure is suspected.
- For environment separation, create separate projects (e.g., staging, production, development) with unique API keys and users for each.
These recommendations reinforce the need for careful API key management to avoid accidental exposure in collaborative or shared environments like Colab.

</details>

---

<details>
<summary>Are there any new, authoritative code walkthroughs or up-to-date examples (from 2024) demonstrating orchestrator-worker LLM workflow patterns using ONLY base Python APIs (e.g., OpenAI, Gemini, Claude) without additional frameworks?</summary>

### Source: https://www.anthropic.com/research/building-effective-agents
Anthropic's official research article "Building Effective AI Agents" (December 2024) provides a detailed conceptual walkthrough of the orchestrator-worker workflow pattern specifically for LLMs. In this pattern, a central LLM (the orchestrator) dynamically decomposes a complex task into subtasks, delegates these to worker LLMs, and synthesizes their results. This approach is particularly useful for situations where the subtasks cannot be predefined, such as coding across multiple files or conducting in-depth research tasks.

Anthropic describes the orchestrator-worker workflow as more flexible than simple parallelization, since the orchestrator determines which subtasks are needed based on the initial input. The article outlines use cases such as software engineering (where task complexity and file modifications vary) and information retrieval (where search and analysis steps depend on evolving results).

While the article does not provide explicit code walkthroughs, it serves as a current, authoritative reference describing the workflow pattern using base APIs. It demonstrates the orchestration logic and the division of labor between orchestrator and worker LLMs, giving a blueprint for those looking to implement similar systems using only foundational LLM APIs (e.g., OpenAI, Claude, Gemini) without reliance on additional frameworks.

-----

### Source: https://github.com/Leeroo-AI/leeroo_orchestrator
The Leeroo Orchestrator GitHub repository (2024) showcases a state-of-the-art open-source architecture for orchestrating multiple expert LLMs through a central orchestrator. The orchestrator dynamically selects and coordinates expert LLMs to achieve optimal task outcomes, refining its strategies via self-play and evaluation loops.

While the repository underscores its accessibility (deployable on consumer hardware or any cloud/on-prem setup) and strong performance benchmarks, it focuses primarily on the orchestration logic and the continual learning process for model selection. However, the documentation and code examples are oriented toward leveraging base Python APIs and open-source LLMs. The orchestrator interacts with various LLMs directly through their APIs, without depending on higher-level orchestration frameworks.

This repository provides practical up-to-date code and clear examples of orchestrator-worker patterns implemented using only Python and model APIs, making it a valuable resource for those seeking real-world, 2024 code walkthroughs of this workflow.

-----

</details>

---

<details>
<summary>What common errors or debugging challenges do beginners face when building prompt-chaining and routing workflows with low-level LLM APIs, and what are proven techniques to diagnose and fix these specific issues?</summary>

### Source: https://www.promptingguide.ai/techniques/prompt_chaining
Prompt chaining involves dividing a task into subtasks to improve reliability and performance with LLMs. Beginners often face errors such as:

- Overly complex chains: Attempting to chain too many prompts without clear intermediate goals can lead to confusion and incorrect outputs.
- Inadequate subtask definition: Not breaking the main task into well-defined, manageable subtasks may result in ambiguous prompts and unreliable results.
- Loss of context: Outputs from earlier prompts may not carry forward necessary context, causing the workflow to break down.

To diagnose and fix these challenges:

- Start with clear, minimal subtasks, and iteratively refine each.
- Ensure each prompt in the chain is specific and provides all necessary context for the next step.
- Test each subtask independently before chaining them together.
- Use prompt engineering best practices to clarify intent and expected output at every step.

These techniques help ensure that prompt chains function as intended and that errors are easier to trace and resolve.

-----

### Source: https://www.datacamp.com/tutorial/prompt-chaining-llm
Common errors and debugging challenges in prompt chaining include:

- Output validity issues: Intermediate prompts may generate unexpected or unusable outputs, breaking the workflow.
- Unhandled failures: If a prompt fails or returns irrelevant data, the entire chain can produce poor results.
- Lack of monitoring: Without detailed records, it is difficult to identify which step in the chain caused the error.

Proven techniques to diagnose and fix these issues:

- Robust error handling: Set up checks for output validity at each stage and use fallback prompts to recover from failures.
- Monitoring and logging: Record each prompt’s input, output, and any errors. This makes it easier to pinpoint where the chain failed and to refine problematic steps.
- Iterative improvement: Use the logs to analyze performance and make targeted adjustments to prompts or logic.

This structured approach results in more reliable and accurate prompt chains that are easier to debug and improve.

-----

### Source: https://mirascope.com/blog/llm-chaining
A frequent challenge is managing the flow of information between chained prompts, especially when the output of one prompt becomes the input for the next. Issues arise when:

- Manual intervention is needed for passing data between steps, which increases the risk of errors and makes debugging harder.
- Dependencies between prompts are not clearly defined, leading to execution order problems.

A proven technique to address these challenges is using computed fields or dynamic configuration to automate the passing of data between steps. This ensures:

- Seamless data flow: Outputs from one step become inputs for the next without manual copying or processing.
- Declarative workflow structure: Dependencies are resolved automatically, reducing errors related to execution order.

By structuring chains declaratively and leveraging dynamic configuration, beginners can reduce errors and make debugging more straightforward.

-----

### Source: https://reply.io/blog/prompt-chain-ai/
Beginners may encounter problems such as:

- Chaining prompts without ensuring the output of one step aligns with the input requirements of the next.
- Failing to validate outputs at each step, leading to cascading errors.

To diagnose and fix these:

- Validate intermediate outputs at every stage before proceeding.
- Make each prompt’s expected input and output explicit and test them independently.
- Use fallback strategies or alternate prompts if an output doesn’t meet criteria.

This disciplined approach helps maintain robustness and simplifies debugging in prompt-chaining workflows.

-----

### Source: https://blog.promptlayer.com/what-is-prompt-chaining/
Prompt chaining errors often stem from:

- Poor subtask decomposition: Tasks not broken down enough can cause prompts to be too broad or ambiguous.
- Ambiguous prompts: Unclear instructions in prompts lead to unpredictable results.
- Insufficient testing: Not evaluating each link in the chain can let undetected issues propagate.

Proven techniques include:

- Systematic subtask identification: Deconstruct complex tasks into clear, manageable prompts.
- Careful prompt design: Ensure each prompt is concise and specific about expectations.
- Logical chaining: Ensure outputs logically feed into subsequent inputs.
- Continuous testing and refinement: Regularly evaluate the chain and adjust prompts for accuracy and performance.

These practices increase reliability, transparency, and accuracy while minimizing errors throughout the prompt chain.

-----

</details>

---

## Sources Scraped From Research Results

---
<details>
<summary>5 Patterns for Scalable LLM Service Integration</summary>

**Want to scale LLM services without breaking your system or budget?** Here’s how:

Building scalable integrations for large language models (LLMs) involves solving challenges like handling traffic spikes, managing costs, and ensuring smooth third-party service connections. This article outlines **five proven patterns** to simplify the process:

- **Hybrid Architecture**: Combines monolithic and microservices for flexibility and cost efficiency.
- **Pipeline Workflow**: Breaks operations into stages, making scaling and updates easier.
- **Adapter Integration**: Acts as a translator between LLMs and legacy systems, simplifying compatibility.
- **Parallelization and Routing**: Speeds up processing by splitting tasks and routing queries to the best-fit model.
- **Orchestrator-Worker**: Centralizes task management, delegating specific jobs to specialized workers.

Each pattern balances performance, cost, and scalability, helping businesses integrate LLMs effectively while maintaining control and flexibility.

**Quick Comparison Table**:

| Pattern | Key Benefit | Best For | Cost Efficiency |
| --- | --- | --- | --- |
| Hybrid Architecture | Flexibility + low latency | Mixed workloads, sensitive data | High |
| Pipeline Workflow | Modular + scalable | Batch processing, multi-step tasks | High |
| Adapter Integration | Simplifies legacy integration | Gradual AI adoption | Medium |
| Parallelization & Routing | Faster + smarter processing | High-volume, diverse queries | Very High |
| Orchestrator-Worker | Centralized management | Complex workflows, fault tolerance | High |

**Which pattern fits your needs?** Dive into the details to find out how to scale LLM services effectively while minimizing costs and complexity.

## 1\. Hybrid Architecture Pattern

The hybrid architecture pattern tackles the challenge of scaling third-party large language model (LLM) integrations by blending two approaches: monolithic and microservices. The core LLM inference operates as a monolithic service to maximize efficiency, while auxiliary functions like data enrichment, caching, and analytics are handled by dedicated microservices. This setup ensures high-performance inference while maintaining the flexibility needed for smooth integrations with other systems.

### Scalability and Cost Efficiency

One of the major advantages of hybrid architectures is their ability to scale incrementally. Instead of forcing organizations into a full transition from monolithic to microservices, this pattern allows for gradual migration as business needs evolve. It ensures low latency for critical operations while enabling non-critical services to scale independently based on demand.

Most organizations rely on 3–4 LLMs to meet varying AI requirements. Hybrid architectures simplify managing these complexities and help optimize costs. By strategically distributing workloads - using on-premises deployments for sensitive data and cloud resources for less critical tasks - companies can reduce operational expenses by up to 35%.

To maintain efficiency, hybrid designs minimize inter-service communication, particularly in real-time scenarios, to avoid bottlenecks. This streamlined approach supports the seamless integration of third-party services.

### Simplified Integration with Third-Party Services

Hybrid architectures make it easier to integrate with third-party services by creating clear boundaries between internal operations and external connections. The monolithic core focuses on internal model inference, while microservices handle interactions with external APIs, data sources, and analytics tools. This separation allows third-party services to be swapped or updated without disrupting the core system.

A typical hybrid deployment often includes a control plane managed by the vendor, while the data plane remains within the customer’s infrastructure. This structure not only simplifies third-party integrations but also ensures sensitive operations stay under the organization’s control.

### Versatility and Adaptability

Hybrid architectures shine in their ability to adapt to varied use cases within a single system. They combine public and private LLM strategies, using public API models for general tasks and creative outputs, while reserving private, customer-hosted models for industry-specific or confidential queries.

The versatility of this model is evident in real-world applications. For instance, in the financial sector, hybrid setups use smaller models to process structured transaction data and LLMs for tasks like analyzing unstructured customer feedback or detecting fraud. Bank of America @https://www.bankofamerica.com/?ref=latitude-blog.ghost.io, for example, employs LLMs to provide real-time updates and fraud detection. Nearly 60% of its clients rely on these tools for guidance on insurance, investments, and retirement planning. This adaptability also enhances the system’s ability to connect seamlessly with external services, making it a robust choice for diverse enterprise needs.

## 2\. Pipeline Workflow Pattern

The pipeline workflow pattern organizes LLM operations into **sequential stages**, with each stage dedicated to a specific task - like data cleaning, prompt engineering @https://blog.latitude.so/prompt-engineering-developers/?ref=latitude-blog.ghost.io, model inference, or output formatting. This structured setup creates clear boundaries, making it easier to integrate third-party tools without disrupting the entire system.

In this pattern, each stage operates as an independent unit. This independence allows teams to **adjust or update individual stages without affecting the rest of the workflow**, which is especially useful when adding external APIs, databases, or analytics tools. Such modularity also lays the groundwork for scaling specific parts of the system, as explored in the following sections.

### Scalability

The pipeline workflow is particularly effective for **batch processing and parallel tasks**, making it a go-to choice for organizations handling large datasets. Since each stage can be scaled independently, resources can be allocated to bottleneck areas while keeping other stages efficient.

For example, Uber's QueryGPT processes around **1.2 million queries each month** using a pipeline that integrates RAG, LLMs, and vector databases. This setup saves Uber an estimated **140,000 hours per month**, time that would otherwise be spent on manual coding tasks.

The enterprise AI sector is seeing rapid growth, with projections of reaching **$13.8 billion in 2024**, more than six times the size of the market in 2023. This trend highlights the growing demand for scalable solutions like pipeline workflows as companies transition from experimental to fully operational AI systems.

### Flexibility

Pipeline workflows shine in **multi-step AI systems**, such as multi-turn dialogue platforms or document summarization tools. Their modular design allows each step to be fine-tuned without affecting the entire system.

Adding or modifying stages is straightforward. For instance, if you need to insert a data validation step or integrate a sentiment analysis tool, you can do so without rewriting existing components.

A great example of this adaptability comes from deepsense.ai @https://deepsense.ai/?ref=latitude-blog.ghost.io, which in June 2025 built a multi-agent document analysis system for a client. Using the Model Context Protocol (MCP), they created a simple interface between agents and the client’s document platform, as well as Databricks Delta Tables @https://docs.databricks.com/gcp/en/tables/delta-table?ref=latitude-blog.ghost.io. Each agent - responsible for tasks like orchestration, data processing, or insight extraction - was equipped with only the tools it needed. This approach reduced token usage while maintaining efficiency. The ability to easily integrate external services further underscores the pipeline’s versatility.

### Ease of Integration with Third-Party Services

The modular nature of pipelines simplifies third-party integration. External services can be added precisely where they’re needed - whether it’s for data enrichment at the start, advanced processing in the middle, or analytics at the end.

When designing APIs for pipeline integration, adopting an **LLM-first approach** is key. This involves making tools intuitive for language models to understand and use, while balancing between too much and too little functionality specification.

By limiting the tools available to each agent in the pipeline, organizations can improve reliability and reduce errors. This scoped approach not only enhances system robustness but also cuts token usage significantly, ensuring efficiency without sacrificing functionality.

### Cost Efficiency

Pipeline workflows also help **reduce costs** through smart design choices. For instance, caching layers between stages can prevent redundant LLM calls, improving both speed and cost-effectiveness.

**Batching inference requests** is another cost-saving measure. By processing multiple requests at once, organizations can make better use of GPUs or APIs, cutting down on per-request expenses. This is particularly beneficial when working with cloud-based LLM services.

Comprehensive monitoring and logging across the pipeline provide insights into bottlenecks and resource usage. This visibility allows teams to **reallocate resources wisely** and identify stages that are consuming more than their share, leading to better cost management.

## 3\. Adapter Integration Pattern

The adapter integration pattern acts as a **connector for incompatible systems**, allowing large language models (LLMs) to integrate smoothly with existing infrastructure without requiring extensive modifications. Essentially, it wraps the LLM's interface to align with the input and output formats expected by legacy systems or third-party APIs, making integration much simpler.

Think of it like a universal power adapter - it translates mismatched interfaces, enabling older systems to communicate effectively with modern LLMs.

### Simplifying Third-Party Service Integration

One of the key strengths of the adapter pattern is its ability to resolve mismatches in APIs, data formats, protocols, or data types. Instead of forcing existing systems to adapt, the adapter creates a translation layer that ensures everything works together seamlessly.

For example, consider TrendyWears, an e-commerce company that needed dependable email delivery. By using the adapter pattern, they integrated three email providers to ensure uninterrupted service during downtimes. They defined a common `Notifications` interface with a `sendEmail` method and developed an adapter class called `Notificator` to manage the three email clients. This setup allowed the company to automatically switch between providers when one failed, ensuring emails were reliably delivered even during outages.

> "The power of the Adapter Pattern lies in its ability to enhance system reliability, separate concerns among components, and adapt to changing conditions. It is a tool that empowers businesses to meet their commitments, even in the face of a dynamic and uncertain technological landscape."
>
> - Olorondu Chukwuemeka, Backend Engineer

This pattern also improves code maintainability by isolating client code from the service implementation. This separation reduces bugs, keeps the codebase cleaner, and makes it easier to test for integration issues early on.

### Adding Flexibility

Once compatibility is established, the adapter pattern can be used to introduce new AI capabilities without disrupting existing systems. It enables companies to incrementally integrate AI features while continuing to use their current infrastructure. This approach is particularly useful for organizations that want to modernize gradually.

For instance, a small business with a CRM system could use the adapter pattern to add LLM-powered email drafting functionality without rebuilding its entire setup. The adapter would handle the data translation between the CRM and the LLM, making the process seamless.

By abstracting direct dependencies between the client and the adapted service, the pattern also simplifies future updates. Systems can be modified or replaced without impacting other components, making it easier to adapt to new technologies.

### Supporting Scalability

As organizations grow, the adapter pattern helps manage the complexity of systems with multiple components or microservices. It ensures interoperability, allowing businesses to integrate new services without overhauling their architecture.

Adapters can dynamically switch between services based on availability or performance, which is especially useful for managing load variations. For example, organizations can implement load balancing across multiple service providers or automatically failover to backup services if a primary provider becomes unavailable.

For larger-scale applications, creating a centralized integration service to oversee multiple adapters can be beneficial. This approach ensures consistency, simplifies monitoring, and provides a single point of control for managing integrations.

### Cutting Costs

The adapter pattern offers a cost-effective way to integrate LLM capabilities. Instead of replacing existing systems, organizations can reuse their current infrastructure while adding new features. This approach significantly reduces implementation costs compared to a complete system overhaul.

Although there may be some overhead, adapters save money by simplifying integration and leveraging existing resources. They also provide flexibility in cost management by allowing businesses to switch between service providers based on pricing or performance. Since the adapter handles the translation, switching providers becomes a straightforward configuration change rather than a complex development project.

To implement the adapter pattern effectively, organizations should focus on user needs, assess their team's expertise with integration patterns, and consider requirements like latency and scalability. Cloud-native tools can also simplify complex architectures, making the process more manageable.

Platforms like Latitude @https://latitude.so/?ref=latitude-blog.ghost.io (https:// latitude @https://latitude.so/?ref=latitude-blog.ghost.io.so) make adapter implementation easier, bridging the gap between legacy systems and LLM technologies efficiently.

## 4\. Parallelization and Routing Pattern

The parallelization and routing pattern combines the power of simultaneous processing with smart query routing to boost performance when integrating large language models (LLMs) with third-party services. Here’s how it works: parallelization enables multiple LLMs to tackle the same task at once or break down complex requests into manageable subtasks. Meanwhile, routing ensures that each query is directed to the most appropriate workflow based on its characteristics. Together, these strategies streamline task distribution - parallelization speeds up response times by handling tasks concurrently, while routing ensures queries are processed by the best-suited LLM for the job.

### Scalability

This approach is all about optimizing resources by breaking tasks into independent subtasks and processing them simultaneously across various LLMs and services. For instance, Amazon Bedrock @https://aws.amazon.com/bedrock/?ref=latitude-blog.ghost.io's Intelligent Prompt Routing can cut costs by up to 30% by automatically directing requests within a model family without sacrificing accuracy. Additionally, dynamic model routing, which selectively activates LLMs for complex tasks, has been shown to reduce overall LLM usage by 37–46% while improving latency for simpler queries by 32–38%, resulting in a 39% reduction in AI processing costs. To maintain efficiency, it’s essential to monitor endpoint latency and error rates and proactively reroute traffic when needed.

### Flexibility

This pattern adapts dynamically, selecting the best model for each request based on its complexity. For example, an educational tutor assistant might use Amazon Titan Text G1 @https://docs.aws.amazon.com/bedrock/latest/userguide/titan-text-models.html?ref=latitude-blog.ghost.io to classify incoming questions as history or math. History-related queries would then be routed to one specialized model, while math questions are sent to another, with a fallback option for uncertain cases. Another example involves semantic routing with Amazon Titan Text Embeddings V2 @https://aws.amazon.com/blogs/machine-learning/get-started-with-amazon-titan-text-embeddings-v2-a-new-state-of-the-art-embeddings-model-on-amazon-bedrock/?ref=latitude-blog.ghost.io, which converts queries into embeddings stored in a FAISS @https://faiss.ai/?ref=latitude-blog.ghost.io vector database. Similarity searches within this database help determine the most suitable LLM for each query.

Andrew Ng captures this adaptability well:

> "Rather than having to choose whether or not something is an agent in a binary way, I thought, it would be more useful to think of systems as being agent-like to different degrees".

This flexibility also allows businesses to incorporate their own rules into the routing logic, making it easier to adjust strategies as needs evolve.

### Ease of Integration with Third-Party Services

Integrating this pattern with third-party services is straightforward, thanks to a unified interface that distributes requests across multiple providers. Static routing works well for applications with distinct UI components handling specific tasks, while dynamic routing is ideal for apps with a single UI component, such as virtual assistants. The routing system can even switch automatically between services based on availability, performance, or cost. Starting with a simple architecture and gradually adding components as needed helps keep the system manageable while maintaining scalability.

### Cost Efficiency

Dynamic routing also shines when it comes to cost savings. By reserving premium models for only the most complex queries, costs can be slashed by as much as 85%. A tiered model strategy - where simpler requests are handled by open-source or smaller proprietary models, and only the toughest queries are escalated to premium options - ensures resources are used wisely. This approach encourages asking a key question: "What’s the smallest model that can confidently handle this query well?"

Platforms like Latitude (https://latitude.so) can simplify the implementation of these patterns, making it easier to balance performance, cost, and integration complexity for scalable LLM services.

## 5\. Orchestrator-Worker Pattern

The orchestrator-worker pattern is all about centralizing complex requests while delegating specific tasks to specialized workers. This approach ensures tasks are efficiently assigned and managed, with each worker focusing on its unique role. Unlike earlier decentralized methods, this pattern simplifies the management of intricate workflows by consolidating decision-making into a single orchestrator.

Using Kafka @https://kafka.apache.org/?ref=latitude-blog.ghost.io's keying strategy, the orchestrator evenly distributes tasks across partitions. Worker agents then pull tasks from these partitions, ensuring balanced workloads. Kafka @https://kafka.apache.org/?ref=latitude-blog.ghost.io's Consumer Rebalance Protocol plays a key role here, maintaining equilibrium even when agents are added or removed.

Anthropic provides a practical example of this pattern through its coding agent, which tackles SWE-bench tasks by editing multiple files based on task descriptions. Another example is their "computer use" implementation, where Claude uses a computer to complete tasks. As Anthropic engineers highlight:

> "Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks".

### Scalability

This pattern shines when it comes to scaling AI capabilities. By enabling the seamless addition or removal of worker agents as workloads fluctuate, it ensures flexibility. These agents, functioning much like a Kafka consumer group, benefit from built-in mechanisms for coordination, scaling, and fault recovery. Looking ahead, LLM orchestration is projected to become a core aspect of AI development by 2025. This scalability lays the groundwork for managing third-party services in a flexible and integrated manner.

### Flexibility

The centralized coordination in this pattern fosters loose coupling between components, ensuring that each service operates independently with its own API interface. This design improves workflow efficiency, enhances separation of concerns, and simplifies the integration of new services. Additionally, the orchestrator can handle failures by rerouting tasks or employing fallback strategies, boosting the system's reliability.

### Ease of Integration with Third-Party Services

Consider a payment gateway system as an example. Here, the orchestrator oversees a sequence of service calls - such as payment authorization, risk management, PCI compliance, and transaction processing - and returns a transaction status. This approach simplifies integration by requiring only one connection to the orchestrator, rather than multiple point-to-point setups. However, effective orchestration demands careful planning and a deep understanding of business processes to maintain efficiency and manageability.

### Cost Efficiency

The orchestrator-worker pattern also offers notable cost-saving opportunities through smarter resource allocation and model selection. For instance, one team reduced their monthly expenses by 14× by switching from GPT-4 @https://openai.com/index/gpt-4-research/?ref=latitude-blog.ghost.io to a smaller model and batching non-urgent queries. To put costs into perspective, GPT-4 @https://openai.com/index/gpt-4-research/?ref=latitude-blog.ghost.io with an 8K context length is priced at around $0.03 per 1,000 input tokens and $0.06 per 1,000 output tokens, while the 32K version costs roughly double. Given the rising costs of AI training, strategies like using prompt routers, model distillation, and batching requests are becoming increasingly important.

Platforms like Latitude (https://latitude.so) provide tools to implement these orchestration patterns effectively, helping you strike the right balance between performance, cost, and complexity when scaling LLM services.

## Scalability Considerations and Best Practices

Creating scalable integrations for large language model (LLM) services requires careful attention to performance. With predictions suggesting **750 million apps will use LLMs by 2025**, focusing on the fundamentals is more critical than ever.

### Monitoring and Observability

Effective monitoring goes beyond simply checking if your system is online. You need tracing tools that follow each request from the user's input to the final output, covering every component in your LLM application. This is especially important for managing the unpredictable outputs that LLMs often produce compared to traditional models.

A solid observability setup starts with **structured logging**. This means logging prompts and responses along with metadata like template versions, API endpoints, and errors encountered. It's also important to monitor resource usage - CPU, GPU, memory - and response times. For systems using third-party APIs, tracking response latency can help ensure you meet service level agreements. Additionally, keeping an eye on token metrics, such as input/output token counts, can help you identify bottlenecks and control costs.

As Datadog @https://www.datadoghq.com/?ref=latitude-blog.ghost.io highlights:

> "LLM observability provides tools, techniques, and methodologies to help teams manage and understand LLM application and language model performance, detect drifts or biases, and resolve issues before they have significant impact on the business or end-user experience."

This foundation of observability supports the modular designs and cost-saving strategies outlined below.

### Modularity and Architecture Design

Breaking your LLM system into **modular components** simplifies troubleshooting, allows for independent scaling, and makes integration with other systems more straightforward. For example, you can separate functions like data management, training, deployment, and inference into distinct services with clear boundaries and interfaces.

A microservices architecture can be particularly useful for LLM applications. For instance, an enterprise content analysis system could divide its operations into separate microservices. Using containerization and orchestration tools further simplifies deployment and scaling, ensuring efficient communication between services.

### Cost Management and Request Prioritization

Managing costs effectively often involves **dynamic model routing**, where simpler tasks are sent to lightweight models, reserving more powerful models for complex queries. The cost difference here is stark - GPT-4o Mini @https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/?ref=latitude-blog.ghost.io costs $0.75 per million tokens, while GPT-4o is priced at $20.00 per million tokens.

**Caching strategies** are another key approach to cutting expenses. Response caching can reduce costs by 15–30% for most applications. Semantic caching, which leverages the similarity between queries, can reduce API calls by up to 70%, as approximately 31% of LLM queries are semantically similar to previous ones.

Optimizing prompts is also a game changer. For example, LLMLingua @https://llmlingua.com/?ref=latitude-blog.ghost.io has achieved up to 20x compression of prompts. Fine-tuning smaller models for specific tasks can save even more. Using smaller LLMs like GPT-J @https://www.eleuther.ai/artifacts/gpt-j?ref=latitude-blog.ghost.io in a cascading setup has been shown to cut costs by 80% while improving accuracy by 1.5% compared to GPT-4.

| Task Complexity | Recommended Model Tier | Cost Efficiency |
| --- | --- | --- |
| Simple text completion | GPT-4o Mini / Mistral Large 2 @https://mistral.ai/news/mistral-large-2407?ref=latitude-blog.ghost.io | High |
| Standard reasoning | Claude 3.7 Sonnet / Llama 3.1 @https://ai.meta.com/blog/meta-llama-3-1/?ref=latitude-blog.ghost.io | Medium |
| Complex analysis | GPT-4.5 / Gemini 2.5 Pro Experimental @https://deepmind.google/models/gemini/pro/?ref=latitude-blog.ghost.io | Low |

### Auto-Scaling and Resource Allocation

**Auto-scaling** adjusts resources in real time to handle traffic spikes and reduce expenses during quieter periods. Tools like AWS Application Auto Scaling @https://aws.amazon.com/autoscaling/?ref=latitude-blog.ghost.io can automatically allocate resources based on metrics like CPU usage or network activity.

Some organizations have achieved significant cost reductions through innovative techniques. For example, Snowflake @https://www.snowflake.com/en/?ref=latitude-blog.ghost.io's SwiftKV @https://www.snowflake.com/en/blog/up-to-75-lower-inference-cost-llama-meta-llm/?ref=latitude-blog.ghost.io with vLLM @https://docs.vllm.ai/?ref=latitude-blog.ghost.io cut Meta LLaMa @https://www.meta.ai/?ref=latitude-blog.ghost.io inference costs by up to 75% using methods like self-distillation and KV cache reuse. Similarly, Amazon Bedrock's distilled agent models reduced latency by 72% and delivered outputs 140% faster than larger models. These strategies work hand-in-hand with the practices discussed earlier to ensure scalability across the board.

### User Feedback and Continuous Improvement

To maintain efficiency over time, you need a system of continuous improvement. By collecting and analyzing user feedback, you can determine if your application is meeting expectations. This feedback loop helps identify when model outputs deviate from desired behavior, allowing for timely adjustments. Regular audits can also reveal inefficiencies in how LLMs are being used, encouraging a focus on cost-effectiveness without sacrificing performance.

Platforms like Latitude (https://latitude.so) offer tools to help you implement these best practices, enabling you to strike a balance between performance, cost, and complexity as your LLM integrations expand.

## Conclusion

Selecting the right architectural pattern for integrating LLM services hinges on your specific needs. Consider factors like user expectations, your team's expertise, latency requirements, and future scalability when making a decision. For instance, a **monolithic architecture** might be a better fit during the early phases, while **microservices** offer greater flexibility as your system grows.

Each approach - whether it's hybrid, orchestrator-worker, or another pattern - offers a roadmap to effectively scale and enhance your LLM services. Focus on optimizing latency by choosing the right setup: **hybrid architectures** work well for real-time applications, **RAG** suits dynamic datasets, and **CAG** is ideal for static contexts.

Leveraging **cloud-native tools** like managed Kubernetes, serverless functions, and API gateways can simplify even the most intricate designs.

To make an informed choice, start with a detailed analysis. Measure the size of your knowledge base, evaluate latency and throughput requirements, and assess your team's ability to manage complex systems. This groundwork ensures you build a solid foundation that can adapt to your business's evolving needs.

Keep in mind, architectural patterns aren't set in stone - they serve as flexible frameworks. By implementing a design that can adapt and grow, you’ll maintain the performance, cost-efficiency, and scalability your users demand. Platforms like **Latitude** (https://latitude.so) can support these decisions, offering tools to balance complexity and performance as your LLM services mature.

## FAQs

### How do I choose the right integration pattern for scalable LLM services in my organization?

To determine the most suitable integration pattern for scalable LLM services in your organization, start by identifying your specific needs. Think about factors such as **how much scalability you require**, the **complexity of your use cases**, and the **type of operational environment** you’re working in. For example, if you’re dealing with dynamic, high-demand applications, microservices might be the way to go. On the other hand, simpler patterns could be a better fit for straightforward deployments.

You’ll also want to consider the nature of your data, the skill set of your team, and how much risk your organization is willing to take on. These elements can help you choose an architecture that aligns with both your technical goals and business priorities. Ultimately, the best choice will strike a balance between what your systems can handle and what your business needs to achieve.

### What strategies can help reduce costs when scaling LLM services?

To keep expenses in check while scaling large language model (LLM) services, there are several practical approaches worth considering:

- **Streamline prompts** to minimize token usage and cut down costs.
- Opt for **smaller models** when they can deliver the needed performance.
- Use **response caching** to avoid repeating the same processing tasks.
- **Group requests** together to enhance processing efficiency.
- Explore methods like **prompt compression** and **model quantization** to conserve resources.

You might also look into **dynamic model routing**, which pairs tasks with the most cost-effective models, or **hybrid setups** that balance cloud and on-premise solutions. Another option is **fine-tuning smaller models** for specific tasks. These strategies can help you achieve cost efficiency without sacrificing scalability.

### How do the architectural patterns in the article support seamless and scalable integration with third-party services?

When it comes to integrating third-party services with language models, the architectural patterns discussed in the article focus on making the process smoother and more efficient. By using unified protocols, like Anthropic’s Model Context Protocol (MCP), communication is standardized. This creates a consistent way for tools to connect with language models, cutting down on complexity and boosting reliability.

On top of that, embracing an **LLM-first design approach**, restricting tool access for each agent, and using modular abstractions can significantly streamline interactions. These methods help keep token usage low, improve scalability, and ensure the integration stays efficient and easy to maintain over time.

## Related posts

- How to Build Scalable LLM Features: A Step-by-Step Guide @https://latitude-blog.ghost.io/https://latitude.so/blog/how-to-build-scalable-llm-features-a-step-by-step-guide/
- The Ultimate Guide to LLM Feature Development @https://latitude-blog.ghost.io/https://latitude.so/blog/the-ultimate-guide-to-llm-feature-development/
- Scaling Open-Source LLMs: Infrastructure Costs Breakdown @https://latitude-blog.ghost.io/https://latitude.so/blog/scaling-open-source-llms-infrastructure-costs-breakdown/
- How to Build Scalable Serverless AI Workflows @https://latitude-blog.ghost.io/https://latitude.so/blog/how-to-build-scalable-serverless-ai-workflows/

### Original URL
https://latitude-blog.ghost.io/blog/5-patterns-for-scalable-llm-service-integration/
</details>

---
<details>
<summary>Enhancing LLM Workflows with Function Calling: Best Practices and Use Cases - AI Resources</summary>

# Enhancing LLM Workflows with Function Calling: Best Practices and Use Cases

### Original URL
https://www.modular.com/ai-resources/enhancing-llm-workflows-with-function-calling-best-practices-and-use-cases
</details>

---
<details>
<summary>Workflows & agents</summary>

Skip to content @https://langchain-ai.github.io/langgraph/tutorials/workflows/#workflows-and-agents

Edit this page @https://github.com/langchain-ai/langgraph/edit/main/docs/docs/tutorials/workflows.md "Edit this page"

# Workflows and Agents ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#workflows-and-agents "Permanent link"

This guide reviews common patterns for agentic systems. In describing these systems, it can be useful to make a distinction between "workflows" and "agents". One way to think about this difference is nicely explained in Anthropic's @https://python.langchain.com/docs/integrations/providers/anthropic/ `Building Effective Agents` blog post:

> Workflows are systems where LLMs and tools are orchestrated through predefined code paths.
> Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Here is a simple way to visualize these differences:

!Agent Workflow @https://langchain-ai.github.io/langgraph/concepts/img/agent_workflow.png

When building agents and workflows, LangGraph offers a number of benefits including persistence, streaming, and support for debugging as well as deployment.

## Set up ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#set-up "Permanent link"

You can use any chat model @https://python.langchain.com/docs/integrations/chat/ that supports structured outputs and tool calling. Below, we show the process of installing the packages, setting API keys, and testing structured outputs / tool calling for Anthropic.

Install dependencies

```md-code__content
pip install langchain_core langchain-anthropic langgraph

```

Initialize an LLM

_API Reference: ChatAnthropic @https://python.langchain.com/api_reference/anthropic/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html_

```md-code__content
import os
import getpass

from langchain_anthropic import ChatAnthropic

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("ANTHROPIC_API_KEY")

llm = ChatAnthropic(model="claude-3-5-sonnet-latest")

```

## Building Blocks: The Augmented LLM ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#building-blocks-the-augmented-llm "Permanent link"

LLM have augmentations that support building workflows and agents. These include structured outputs @https://python.langchain.com/docs/concepts/structured_outputs/ and tool calling @https://python.langchain.com/docs/concepts/tool_calling/, as shown in this image from the Anthropic blog on `Building Effective Agents`:

!augmented_llm.png @https://langchain-ai.github.io/langgraph/tutorials/workflows/img/augmented_llm.png

```md-code__content
# Schema for structured output
from pydantic import BaseModel, Field

class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Query that is optimized web search.")
    justification: str = Field(
        None, description="Why this query is relevant to the user's request."
    )

# Augment the LLM with schema for structured output
structured_llm = llm.with_structured_output(SearchQuery)

# Invoke the augmented LLM
output = structured_llm.invoke("How does Calcium CT score relate to high cholesterol?")

# Define a tool
def multiply(a: int, b: int) -> int:
    return a * b

# Augment the LLM with tools
llm_with_tools = llm.bind_tools([multiply])

# Invoke the LLM with input that triggers the tool call
msg = llm_with_tools.invoke("What is 2 times 3?")

# Get the tool call
msg.tool_calls

```

## Prompt chaining ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#prompt-chaining "Permanent link"

In prompt chaining, each LLM call processes the output of the previous one.

As noted in the Anthropic blog on `Building Effective Agents`:

> Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.
>
> When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

!prompt_chain.png @https://langchain-ai.github.io/langgraph/tutorials/workflows/img/prompt_chain.png

Graph API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_1_1Functional API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_1_2

```md-code__content
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display

# Graph state
class State(TypedDict):
    topic: str
    joke: str
    improved_joke: str
    final_joke: str

# Nodes
def generate_joke(state: State):
    """First LLM call to generate initial joke"""

    msg = llm.invoke(f"Write a short joke about {state['topic']}")
    return {"joke": msg.content}

def check_punchline(state: State):
    """Gate function to check if the joke has a punchline"""

    # Simple check - does the joke contain "?" or "!"
    if "?" in state["joke"] or "!" in state["joke"]:
        return "Pass"
    return "Fail"

def improve_joke(state: State):
    """Second LLM call to improve the joke"""

    msg = llm.invoke(f"Make this joke funnier by adding wordplay: {state['joke']}")
    return {"improved_joke": msg.content}

def polish_joke(state: State):
    """Third LLM call for final polish"""

    msg = llm.invoke(f"Add a surprising twist to this joke: {state['improved_joke']}")
    return {"final_joke": msg.content}

# Build workflow
workflow = StateGraph(State)

# Add nodes
workflow.add_node("generate_joke", generate_joke)
workflow.add_node("improve_joke", improve_joke)
workflow.add_node("polish_joke", polish_joke)

# Add edges to connect nodes
workflow.add_edge(START, "generate_joke")
workflow.add_conditional_edges(
    "generate_joke", check_punchline, {"Fail": "improve_joke", "Pass": END}
)
workflow.add_edge("improve_joke", "polish_joke")
workflow.add_edge("polish_joke", END)

# Compile
chain = workflow.compile()

# Show workflow
display(Image(chain.get_graph().draw_mermaid_png()))

# Invoke
state = chain.invoke({"topic": "cats"})
print("Initial joke:")
print(state["joke"])
print("\n--- --- ---\n")
if "improved_joke" in state:
    print("Improved joke:")
    print(state["improved_joke"])
    print("\n--- --- ---\n")

    print("Final joke:")
    print(state["final_joke"])
else:
    print("Joke failed quality gate - no punchline detected!")

```

**LangSmith Trace**

@https://smith.langchain.com/public/a0281fca-3a71-46de-beee-791468607b75/r

**Resources:**

**LangChain Academy**

See our lesson on Prompt Chaining here @https://github.com/langchain-ai/langchain-academy/blob/main/module-1/chain.ipynb.

```md-code__content
from langgraph.func import entrypoint, task

# Tasks
@task
def generate_joke(topic: str):
    """First LLM call to generate initial joke"""
    msg = llm.invoke(f"Write a short joke about {topic}")
    return msg.content

def check_punchline(joke: str):
    """Gate function to check if the joke has a punchline"""
    # Simple check - does the joke contain "?" or "!"
    if "?" in joke or "!" in joke:
        return "Fail"

    return "Pass"

@task
def improve_joke(joke: str):
    """Second LLM call to improve the joke"""
    msg = llm.invoke(f"Make this joke funnier by adding wordplay: {joke}")
    return msg.content

@task
def polish_joke(joke: str):
    """Third LLM call for final polish"""
    msg = llm.invoke(f"Add a surprising twist to this joke: {joke}")
    return msg.content

@entrypoint()
def prompt_chaining_workflow(topic: str):
    original_joke = generate_joke(topic).result()
    if check_punchline(original_joke) == "Pass":
        return original_joke

    improved_joke = improve_joke(original_joke).result()
    return polish_joke(improved_joke).result()

# Invoke
for step in prompt_chaining_workflow.stream("cats", stream_mode="updates"):
    print(step)
    print("\n")

```

**LangSmith Trace**

@https://smith.langchain.com/public/332fa4fc-b6ca-416e-baa3-161625e69163/r

## Parallelization ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#parallelization "Permanent link"

With parallelization, LLMs work simultaneously on a task:

> LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations: Sectioning: Breaking a task into independent subtasks run in parallel. Voting: Running the same task multiple times to get diverse outputs.
>
> When to use this workflow: Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

!parallelization.png @https://langchain-ai.github.io/langgraph/tutorials/workflows/img/parallelization.png

Graph API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_2_1Functional API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_2_2

```md-code__content
# Graph state
class State(TypedDict):
    topic: str
    joke: str
    story: str
    poem: str
    combined_output: str

# Nodes
def call_llm_1(state: State):
    """First LLM call to generate initial joke"""

    msg = llm.invoke(f"Write a joke about {state['topic']}")
    return {"joke": msg.content}

def call_llm_2(state: State):
    """Second LLM call to generate story"""

    msg = llm.invoke(f"Write a story about {state['topic']}")
    return {"story": msg.content}

def call_llm_3(state: State):
    """Third LLM call to generate poem"""

    msg = llm.invoke(f"Write a poem about {state['topic']}")
    return {"poem": msg.content}

def aggregator(state: State):
    """Combine the joke and story into a single output"""

    combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
    combined += f"STORY:\n{state['story']}\n\n"
    combined += f"JOKE:\n{state['joke']}\n\n"
    combined += f"POEM:\n{state['poem']}"
    return {"combined_output": combined}

# Build workflow
parallel_builder = StateGraph(State)

# Add nodes
parallel_builder.add_node("call_llm_1", call_llm_1)
parallel_builder.add_node("call_llm_2", call_llm_2)
parallel_builder.add_node("call_llm_3", call_llm_3)
parallel_builder.add_node("aggregator", aggregator)

# Add edges to connect nodes
parallel_builder.add_edge(START, "call_llm_1")
parallel_builder.add_edge(START, "call_llm_2")
parallel_builder.add_edge(START, "call_llm_3")
parallel_builder.add_edge("call_llm_1", "aggregator")
parallel_builder.add_edge("call_llm_2", "aggregator")
parallel_builder.add_edge("call_llm_3", "aggregator")
parallel_builder.add_edge("aggregator", END)
parallel_workflow = parallel_builder.compile()

# Show workflow
display(Image(parallel_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = parallel_workflow.invoke({"topic": "cats"})
print(state["combined_output"])

```

**LangSmith Trace**

@https://smith.langchain.com/public/3be2e53c-ca94-40dd-934f-82ff87fac277/r

**Resources:**

**Documentation**

See our documentation on parallelization here @https://langchain-ai.github.io/langgraph/how-tos/branching/.

**LangChain Academy**

See our lesson on parallelization here @https://github.com/langchain-ai/langchain-academy/blob/main/module-1/simple-graph.ipynb.

```md-code__content
@task
def call_llm_1(topic: str):
    """First LLM call to generate initial joke"""
    msg = llm.invoke(f"Write a joke about {topic}")
    return msg.content

@task
def call_llm_2(topic: str):
    """Second LLM call to generate story"""
    msg = llm.invoke(f"Write a story about {topic}")
    return msg.content

@task
def call_llm_3(topic):
    """Third LLM call to generate poem"""
    msg = llm.invoke(f"Write a poem about {topic}")
    return msg.content

@task
def aggregator(topic, joke, story, poem):
    """Combine the joke and story into a single output"""

    combined = f"Here's a story, joke, and poem about {topic}!\n\n"
    combined += f"STORY:\n{story}\n\n"
    combined += f"JOKE:\n{joke}\n\n"
    combined += f"POEM:\n{poem}"
    return combined

# Build workflow
@entrypoint()
def parallel_workflow(topic: str):
    joke_fut = call_llm_1(topic)
    story_fut = call_llm_2(topic)
    poem_fut = call_llm_3(topic)
    return aggregator(
        topic, joke_fut.result(), story_fut.result(), poem_fut.result()
    ).result()

# Invoke
for step in parallel_workflow.stream("cats", stream_mode="updates"):
    print(step)
    print("\n")

```

**LangSmith Trace**

@https://smith.langchain.com/public/623d033f-e814-41e9-80b1-75e6abb67801/r

## Routing ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#routing "Permanent link"

Routing classifies an input and directs it to a followup task. As noted in the Anthropic blog on `Building Effective Agents`:

> Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.
>
> When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

!routing.png @https://langchain-ai.github.io/langgraph/tutorials/workflows/img/routing.png

Graph API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_3_1Functional API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_3_2

```md-code__content
from typing_extensions import Literal
from langchain_core.messages import HumanMessage, SystemMessage

# Schema for structured output to use as routing logic
class Route(BaseModel):
    step: Literal["poem", "story", "joke"] = Field(
        None, description="The next step in the routing process"
    )

# Augment the LLM with schema for structured output
router = llm.with_structured_output(Route)

# State
class State(TypedDict):
    input: str
    decision: str
    output: str

# Nodes
def llm_call_1(state: State):
    """Write a story"""

    result = llm.invoke(state["input"])
    return {"output": result.content}

def llm_call_2(state: State):
    """Write a joke"""

    result = llm.invoke(state["input"])
    return {"output": result.content}

def llm_call_3(state: State):
    """Write a poem"""

    result = llm.invoke(state["input"])
    return {"output": result.content}

def llm_call_router(state: State):
    """Route the input to the appropriate node"""

    # Run the augmented LLM with structured output to serve as routing logic
    decision = router.invoke(
        [\
            SystemMessage(\
                content="Route the input to story, joke, or poem based on the user's request."\
            ),\
            HumanMessage(content=state["input"]),\
        ]
    )

    return {"decision": decision.step}

# Conditional edge function to route to the appropriate node
def route_decision(state: State):
    # Return the node name you want to visit next
    if state["decision"] == "story":
        return "llm_call_1"
    elif state["decision"] == "joke":
        return "llm_call_2"
    elif state["decision"] == "poem":
        return "llm_call_3"

# Build workflow
router_builder = StateGraph(State)

# Add nodes
router_builder.add_node("llm_call_1", llm_call_1)
router_builder.add_node("llm_call_2", llm_call_2)
router_builder.add_node("llm_call_3", llm_call_3)
router_builder.add_node("llm_call_router", llm_call_router)

# Add edges to connect nodes
router_builder.add_edge(START, "llm_call_router")
router_builder.add_conditional_edges(
    "llm_call_router",
    route_decision,
    {  # Name returned by route_decision : Name of next node to visit
        "llm_call_1": "llm_call_1",
        "llm_call_2": "llm_call_2",
        "llm_call_3": "llm_call_3",
    },
)
router_builder.add_edge("llm_call_1", END)
router_builder.add_edge("llm_call_2", END)
router_builder.add_edge("llm_call_3", END)

# Compile workflow
router_workflow = router_builder.compile()

# Show the workflow
display(Image(router_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = router_workflow.invoke({"input": "Write me a joke about cats"})
print(state["output"])

```

**LangSmith Trace**

@https://smith.langchain.com/public/c4580b74-fe91-47e4-96fe-7fac598d509c/r

**Resources:**

**LangChain Academy**

See our lesson on routing here @https://github.com/langchain-ai/langchain-academy/blob/main/module-1/router.ipynb.

**Examples**

Here @https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/ is RAG workflow that routes questions. See our video here @https://www.youtube.com/watch?v=bq1Plo2RhYI.

```md-code__content
from typing_extensions import Literal
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage

# Schema for structured output to use as routing logic
class Route(BaseModel):
    step: Literal["poem", "story", "joke"] = Field(
        None, description="The next step in the routing process"
    )

# Augment the LLM with schema for structured output
router = llm.with_structured_output(Route)

@task
def llm_call_1(input_: str):
    """Write a story"""
    result = llm.invoke(input_)
    return result.content

@task
def llm_call_2(input_: str):
    """Write a joke"""
    result = llm.invoke(input_)
    return result.content

@task
def llm_call_3(input_: str):
    """Write a poem"""
    result = llm.invoke(input_)
    return result.content

def llm_call_router(input_: str):
    """Route the input to the appropriate node"""
    # Run the augmented LLM with structured output to serve as routing logic
    decision = router.invoke(
        [\
            SystemMessage(\
                content="Route the input to story, joke, or poem based on the user's request."\
            ),\
            HumanMessage(content=input_),\
        ]
    )
    return decision.step

# Create workflow
@entrypoint()
def router_workflow(input_: str):
    next_step = llm_call_router(input_)
    if next_step == "story":
        llm_call = llm_call_1
    elif next_step == "joke":
        llm_call = llm_call_2
    elif next_step == "poem":
        llm_call = llm_call_3

    return llm_call(input_).result()

# Invoke
for step in router_workflow.stream("Write me a joke about cats", stream_mode="updates"):
    print(step)
    print("\n")

```

**LangSmith Trace**

@https://smith.langchain.com/public/5e2eb979-82dd-402c-b1a0-a8cceaf2a28a/r

## Orchestrator-Worker ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#orchestrator-worker "Permanent link"

With orchestrator-worker, an orchestrator breaks down a task and delegates each sub-task to workers. As noted in the Anthropic blog on `Building Effective Agents`:

> In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.
>
> When to use this workflow: This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

!worker.png @https://langchain-ai.github.io/langgraph/tutorials/workflows/img/worker.png

Graph API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_4_1Functional API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_4_2

```md-code__content
from typing import Annotated, List
import operator

# Schema for structured output to use in planning
class Section(BaseModel):
    name: str = Field(
        description="Name for this section of the report.",
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section.",
    )

class Sections(BaseModel):
    sections: List[Section] = Field(
        description="Sections of the report.",
    )

# Augment the LLM with schema for structured output
planner = llm.with_structured_output(Sections)

```

**Creating Workers in LangGraph**

Because orchestrator-worker workflows are common, LangGraph **has the `Send` API to support this**. It lets you dynamically create worker nodes and send each one a specific input. Each worker has its own state, and all worker outputs are written to a _shared state key_ that is accessible to the orchestrator graph. This gives the orchestrator access to all worker output and allows it to synthesize them into a final output. As you can see below, we iterate over a list of sections and `Send` each to a worker node. See further documentation here @https://langchain-ai.github.io/langgraph/how-tos/map-reduce/ and here @https://langchain-ai.github.io/langgraph/concepts/low_level/#send.

```md-code__content
from langgraph.constants import Send

# Graph state
class State(TypedDict):
    topic: str  # Report topic
    sections: list[Section]  # List of report sections
    completed_sections: Annotated[\
        list, operator.add\
    ]  # All workers write to this key in parallel
    final_report: str  # Final report

# Worker state
class WorkerState(TypedDict):
    section: Section
    completed_sections: Annotated[list, operator.add]

# Nodes
def orchestrator(state: State):
    """Orchestrator that generates a plan for the report"""

    # Generate queries
    report_sections = planner.invoke(
        [\
            SystemMessage(content="Generate a plan for the report."),\
            HumanMessage(content=f"Here is the report topic: {state['topic']}"),\
        ]
    )

    return {"sections": report_sections.sections}

def llm_call(state: WorkerState):
    """Worker writes a section of the report"""

    # Generate section
    section = llm.invoke(
        [\
            SystemMessage(\
                content="Write a report section following the provided name and description. Include no preamble for each section. Use markdown formatting."\
            ),\
            HumanMessage(\
                content=f"Here is the section name: {state['section'].name} and description: {state['section'].description}"\
            ),\
        ]
    )

    # Write the updated section to completed sections
    return {"completed_sections": [section.content]}

def synthesizer(state: State):
    """Synthesize full report from sections"""

    # List of completed sections
    completed_sections = state["completed_sections"]

    # Format completed section to str to use as context for final sections
    completed_report_sections = "\n\n---\n\n".join(completed_sections)

    return {"final_report": completed_report_sections}

# Conditional edge function to create llm_call workers that each write a section of the report
def assign_workers(state: State):
    """Assign a worker to each section in the plan"""

    # Kick off section writing in parallel via Send() API
    return [Send("llm_call", {"section": s}) for s in state["sections"]]

# Build workflow
orchestrator_worker_builder = StateGraph(State)

# Add the nodes
orchestrator_worker_builder.add_node("orchestrator", orchestrator)
orchestrator_worker_builder.add_node("llm_call", llm_call)
orchestrator_worker_builder.add_node("synthesizer", synthesizer)

# Add edges to connect nodes
orchestrator_worker_builder.add_edge(START, "orchestrator")
orchestrator_worker_builder.add_conditional_edges(
    "orchestrator", assign_workers, ["llm_call"]
)
orchestrator_worker_builder.add_edge("llm_call", "synthesizer")
orchestrator_worker_builder.add_edge("synthesizer", END)

# Compile the workflow
orchestrator_worker = orchestrator_worker_builder.compile()

# Show the workflow
display(Image(orchestrator_worker.get_graph().draw_mermaid_png()))

# Invoke
state = orchestrator_worker.invoke({"topic": "Create a report on LLM scaling laws"})

from IPython.display import Markdown
Markdown(state["final_report"])

```

**LangSmith Trace**

@https://smith.langchain.com/public/78cbcfc3-38bf-471d-b62a-b299b144237d/r

**Resources:**

**LangChain Academy**

See our lesson on orchestrator-worker here @https://github.com/langchain-ai/langchain-academy/blob/main/module-4/map-reduce.ipynb.

**Examples**

Here @https://github.com/langchain-ai/report-mAIstro is a project that uses orchestrator-worker for report planning and writing. See our video here @https://www.youtube.com/watch?v=wSxZ7yFbbas.

```md-code__content
from typing import List

# Schema for structured output to use in planning
class Section(BaseModel):
    name: str = Field(
        description="Name for this section of the report.",
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section.",
    )

class Sections(BaseModel):
    sections: List[Section] = Field(
        description="Sections of the report.",
    )

# Augment the LLM with schema for structured output
planner = llm.with_structured_output(Sections)

@task
def orchestrator(topic: str):
    """Orchestrator that generates a plan for the report"""
    # Generate queries
    report_sections = planner.invoke(
        [\
            SystemMessage(content="Generate a plan for the report."),\
            HumanMessage(content=f"Here is the report topic: {topic}"),\
        ]
    )

    return report_sections.sections

@task
def llm_call(section: Section):
    """Worker writes a section of the report"""

    # Generate section
    result = llm.invoke(
        [\
            SystemMessage(content="Write a report section."),\
            HumanMessage(\
                content=f"Here is the section name: {section.name} and description: {section.description}"\
            ),\
        ]
    )

    # Write the updated section to completed sections
    return result.content

@task
def synthesizer(completed_sections: list[str]):
    """Synthesize full report from sections"""
    final_report = "\n\n---\n\n".join(completed_sections)
    return final_report

@entrypoint()
def orchestrator_worker(topic: str):
    sections = orchestrator(topic).result()
    section_futures = [llm_call(section) for section in sections]
    final_report = synthesizer(
        [section_fut.result() for section_fut in section_futures]
    ).result()
    return final_report

# Invoke
report = orchestrator_worker.invoke("Create a report on LLM scaling laws")
from IPython.display import Markdown
Markdown(report)

```

**LangSmith Trace**

@https://smith.langchain.com/public/75a636d0-6179-4a12-9836-e0aa571e87c5/r

## Evaluator-optimizer ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#evaluator-optimizer "Permanent link"

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop:

> In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.
>
> When to use this workflow: This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

!evaluator_optimizer.png @https://langchain-ai.github.io/langgraph/tutorials/workflows/img/evaluator_optimizer.png

Graph API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_5_1Functional API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_5_2

```md-code__content
# Graph state
class State(TypedDict):
    joke: str
    topic: str
    feedback: str
    funny_or_not: str

# Schema for structured output to use in evaluation
class Feedback(BaseModel):
    grade: Literal["funny", "not funny"] = Field(
        description="Decide if the joke is funny or not.",
    )
    feedback: str = Field(
        description="If the joke is not funny, provide feedback on how to improve it.",
    )

# Augment the LLM with schema for structured output
evaluator = llm.with_structured_output(Feedback)

# Nodes
def llm_call_generator(state: State):
    """LLM generates a joke"""

    if state.get("feedback"):
        msg = llm.invoke(
            f"Write a joke about {state['topic']} but take into account the feedback: {state['feedback']}"
        )
    else:
        msg = llm.invoke(f"Write a joke about {state['topic']}")
    return {"joke": msg.content}

def llm_call_evaluator(state: State):
    """LLM evaluates the joke"""

    grade = evaluator.invoke(f"Grade the joke {state['joke']}")
    return {"funny_or_not": grade.grade, "feedback": grade.feedback}

# Conditional edge function to route back to joke generator or end based upon feedback from the evaluator
def route_joke(state: State):
    """Route back to joke generator or end based upon feedback from the evaluator"""

    if state["funny_or_not"] == "funny":
        return "Accepted"
    elif state["funny_or_not"] == "not funny":
        return "Rejected + Feedback"

# Build workflow
optimizer_builder = StateGraph(State)

# Add the nodes
optimizer_builder.add_node("llm_call_generator", llm_call_generator)
optimizer_builder.add_node("llm_call_evaluator", llm_call_evaluator)

# Add edges to connect nodes
optimizer_builder.add_edge(START, "llm_call_generator")
optimizer_builder.add_edge("llm_call_generator", "llm_call_evaluator")
optimizer_builder.add_conditional_edges(
    "llm_call_evaluator",
    route_joke,
    {  # Name returned by route_joke : Name of next node to visit
        "Accepted": END,
        "Rejected + Feedback": "llm_call_generator",
    },
)

# Compile the workflow
optimizer_workflow = optimizer_builder.compile()

# Show the workflow
display(Image(optimizer_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = optimizer_workflow.invoke({"topic": "Cats"})
print(state["joke"])

```

**LangSmith Trace**

@https://smith.langchain.com/public/86ab3e60-2000-4bff-b988-9b89a3269789/r

**Resources:**

**Examples**

Here @https://github.com/langchain-ai/local-deep-researcher is an assistant that uses evaluator-optimizer to improve a report. See our video here @https://www.youtube.com/watch?v=XGuTzHoqlj8.

Here @https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_adaptive_rag_local/ is a RAG workflow that grades answers for hallucinations or errors. See our video here @https://www.youtube.com/watch?v=bq1Plo2RhYI.

```md-code__content
# Schema for structured output to use in evaluation
class Feedback(BaseModel):
    grade: Literal["funny", "not funny"] = Field(
        description="Decide if the joke is funny or not.",
    )
    feedback: str = Field(
        description="If the joke is not funny, provide feedback on how to improve it.",
    )

# Augment the LLM with schema for structured output
evaluator = llm.with_structured_output(Feedback)

# Nodes
@task
def llm_call_generator(topic: str, feedback: Feedback):
    """LLM generates a joke"""
    if feedback:
        msg = llm.invoke(
            f"Write a joke about {topic} but take into account the feedback: {feedback}"
        )
    else:
        msg = llm.invoke(f"Write a joke about {topic}")
    return msg.content

@task
def llm_call_evaluator(joke: str):
    """LLM evaluates the joke"""
    feedback = evaluator.invoke(f"Grade the joke {joke}")
    return feedback

@entrypoint()
def optimizer_workflow(topic: str):
    feedback = None
    while True:
        joke = llm_call_generator(topic, feedback).result()
        feedback = llm_call_evaluator(joke).result()
        if feedback.grade == "funny":
            break

    return joke

# Invoke
for step in optimizer_workflow.stream("Cats", stream_mode="updates"):
    print(step)
    print("\n")

```

**LangSmith Trace**

@https://smith.langchain.com/public/f66830be-4339-4a6b-8a93-389ce5ae27b4/r

## Agent ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#agent "Permanent link"

Agents are typically implemented as an LLM performing actions (via tool-calling) based on environmental feedback in a loop. As noted in the Anthropic blog on `Building Effective Agents`:

> Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully.
>
> When to use agents: Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

!agent.png @https://langchain-ai.github.io/langgraph/tutorials/workflows/img/agent.png

_API Reference: tool @https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html_

```md-code__content
from langchain_core.tools import tool

# Define tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b

# Augment the LLM with tools
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)

```

Graph API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_6_1Functional API @https://langchain-ai.github.io/langgraph/tutorials/workflows/#__tabbed_6_2

```md-code__content
from langgraph.graph import MessagesState
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

# Nodes
def llm_call(state: MessagesState):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [\
            llm_with_tools.invoke(\
                [\
                    SystemMessage(\
                        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."\
                    )\
                ]\
                + state["messages"]\
            )\
        ]
    }

def tool_node(state: dict):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}

# Conditional edge function to route to the tool node or end based upon whether the LLM made a tool call
def should_continue(state: MessagesState) -> Literal["environment", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]
    # If the LLM makes a tool call, then perform an action
    if last_message.tool_calls:
        return "Action"
    # Otherwise, we stop (reply to the user)
    return END

# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("environment", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    {
        # Name returned by should_continue : Name of next node to visit
        "Action": "environment",
        END: END,
    },
)
agent_builder.add_edge("environment", "llm_call")

# Compile the agent
agent = agent_builder.compile()

# Show the agent
display(Image(agent.get_graph(xray=True).draw_mermaid_png()))

# Invoke
messages = [HumanMessage(content="Add 3 and 4.")]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()

```

**LangSmith Trace**

@https://smith.langchain.com/public/051f0391-6761-4f8c-a53b-22231b016690/r

**Resources:**

**LangChain Academy**

See our lesson on agents here @https://github.com/langchain-ai/langchain-academy/blob/main/module-1/agent.ipynb.

**Examples**

Here @https://github.com/langchain-ai/memory-agent is a project that uses a tool calling agent to create / store long-term memories.

```md-code__content
from langgraph.graph import add_messages
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    BaseMessage,
    ToolCall,
)

@task
def call_llm(messages: list[BaseMessage]):
    """LLM decides whether to call a tool or not"""
    return llm_with_tools.invoke(
        [\
            SystemMessage(\
                content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."\
            )\
        ]
        + messages
    )

@task
def call_tool(tool_call: ToolCall):
    """Performs the tool call"""
    tool = tools_by_name[tool_call["name"]]
    return tool.invoke(tool_call)

@entrypoint()
def agent(messages: list[BaseMessage]):
    llm_response = call_llm(messages).result()

    while True:
        if not llm_response.tool_calls:
            break

        # Execute tools
        tool_result_futures = [\
            call_tool(tool_call) for tool_call in llm_response.tool_calls\
        ]
        tool_results = [fut.result() for fut in tool_result_futures]
        messages = add_messages(messages, [llm_response, *tool_results])
        llm_response = call_llm(messages).result()

    messages = add_messages(messages, llm_response)
    return messages

# Invoke
messages = [HumanMessage(content="Add 3 and 4.")]
for chunk in agent.stream(messages, stream_mode="updates"):
    print(chunk)
    print("\n")

```

**LangSmith Trace**

@https://smith.langchain.com/public/42ae8bf9-3935-4504-a081-8ddbcbfc8b2e/r

#### Pre-built ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#pre-built "Permanent link"

LangGraph also provides a **pre-built method** for creating an agent as defined above (using the `create_react_agent` @https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.chat_agent_executor.create_react_agent "<code class=\"doc-symbol doc-symbol-heading doc-symbol-function\"></code>            <span class=\"doc doc-object-name doc-function-name\">create_react_agent</span>" function):

@https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/

_API Reference: create\_react\_agent @https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent_

```md-code__content
from langgraph.prebuilt import create_react_agent

# Pass in:
# (1) the augmented LLM with tools
# (2) the tools list (which is used to create the tool node)
pre_built_agent = create_react_agent(llm, tools=tools)

# Show the agent
display(Image(pre_built_agent.get_graph().draw_mermaid_png()))

# Invoke
messages = [HumanMessage(content="Add 3 and 4.")]
messages = pre_built_agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()

```

**LangSmith Trace**

@https://smith.langchain.com/public/abab6a44-29f6-4b97-8164-af77413e494d/r

## What LangGraph provides ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#what-langgraph-provides "Permanent link"

By constructing each of the above in LangGraph, we get a few things:

### Persistence: Human-in-the-Loop ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#persistence-human-in-the-loop "Permanent link"

LangGraph persistence layer supports interruption and approval of actions (e.g., Human In The Loop). See Module 3 of LangChain Academy @https://github.com/langchain-ai/langchain-academy/tree/main/module-3.

### Persistence: Memory ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#persistence-memory "Permanent link"

LangGraph persistence layer supports conversational (short-term) memory and long-term memory. See Modules 2 @https://github.com/langchain-ai/langchain-academy/tree/main/module-2 and 5 @https://github.com/langchain-ai/langchain-academy/tree/main/module-5 of LangChain Academy:

### Streaming ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#streaming "Permanent link"

LangGraph provides several ways to stream workflow / agent outputs or intermediate state. See Module 3 of LangChain Academy @https://github.com/langchain-ai/langchain-academy/blob/main/module-3/streaming-interruption.ipynb.

### Deployment ¶ @https://langchain-ai.github.io/langgraph/tutorials/workflows/\#deployment "Permanent link"

LangGraph provides an easy on-ramp for deployment, observability, and evaluation. See module 6 @https://github.com/langchain-ai/langchain-academy/tree/main/module-6 of LangChain Academy.

Back to top

### Original URL
https://langchain-ai.github.io/langgraph/tutorials/workflows/
</details>

---
<details>
<summary>What is Prompt Chaining? A Guide to Thinking With LLMs</summary>

Prompt chaining is an AI technique that enhances the capabilities of large language models (LLMs). It involves breaking down a complex task into a series of interconnected prompts, where the output of one prompt becomes the input for the next. This structured approach guides the LLM through a more nuanced reasoning process, leading to more accurate and comprehensive results.

## What is Prompt Chaining?

Prompt chaining leverages the power of LLMs by creating a sequence of interconnected prompts. Instead of presenting a single, complex prompt, the task is divided into smaller, more manageable steps. Each step's output feeds into the next, forming a chain that leads the LLM to the desired outcome.

## Why is Prompt Chaining Important?

LLMs, while revolutionary, have limitations. Their context length restricts the amount of information processed in a single prompt, hindering complex task handling. Prompt chaining overcomes this by segmenting the task into smaller, digestible pieces.

Context hallucination, where the model generates outputs inconsistent with the given context, is another challenge. Prompt chaining mitigates this by maintaining context throughout the chain, guiding the LLM and reducing hallucinations.

Finally, prompt chaining simplifies fault analysis by isolating the problem into multiple sections, making it easier to pinpoint and rectify errors in the reasoning process, resulting in more reliable LLM applications.

## How Does Prompt Chaining Work?

Prompt chaining systematically guides an LLM through a series of prompts. It begins with an initial prompt establishing context and providing the first instruction. The subsequent prompts use the output of the previous ones as input, forming a chain leading to the desired result.

## Types of Prompt Chains

- **Linear Chains:** Prompts follow a sequential order, each building upon the previous one. Suitable for tasks requiring a step-by-step approach, like summarizing a document or generating code.
- **Branching Chains:** Incorporate conditional logic. The next prompt depends on the previous prompt's output. Useful for tasks with varying decision paths, such as customer service or scenario-based problem-solving.
- **Recursive Chains:** Repeat a set of prompts until a condition is met. Helpful for tasks requiring iterative refinement, like creative writing or data analysis.

## Implementing Prompt Chaining

1. **Identify Subtasks:** Deconstruct the complex task into smaller, manageable subtasks.
2. **Design Prompts:** Craft clear and concise prompts for each subtask.
3. **Chain the Prompts:** Link prompts logically, ensuring each output feeds into the next input.
4. **Test and Refine:** Evaluate the chain, refining prompts to optimize accuracy and performance.

## Advantages of Prompt Chaining

- **Improved Accuracy:** Focusing on one aspect at a time leads to more accurate and relevant responses.
- **Enhanced Control:** Greater control over the LLM's reasoning process guides the model towards the desired outcome.
- **Increased Transparency:** The LLM's decision-making becomes more transparent, clarifying how conclusions are reached.
- **Reduced Error Rate:** More focused input and context minimize errors in LLM outputs.

## Disadvantages of Prompt Chaining

- **Increased Complexity:** Managing interconnected prompts can be more complex than single prompts.
- **Dependency on Initial Prompt:** The chain's success relies heavily on the initial prompt's quality.
- **Potential for Increased Latency:** Multiple API calls can introduce processing delays.

## When to Use (and Not Use) Prompt Chaining

Prompt chaining excels in complex tasks broken down into smaller steps, maintaining context over multiple LLM interactions, and verifying responses for correctness. However, it's less suitable for simple tasks where a single prompt suffices or tasks requiring rapid responses due to potential latency from multiple API calls.

## Use Cases and Examples

- **Content Creation:** Generate various content types (articles, blog posts) by chaining prompts for outlining, writing introductions, and elaborating on sections.
- **Code Generation:** Assist developers by chaining prompts for generating functions, testing, and refactoring.
- **Data Analysis:** Guide LLMs in data collection, analysis, and interpretation by chaining prompts for analyzing sales data, identifying trends, and predicting future figures.
- **Customer Service:** Create interactive chatbots handling complex queries by chaining prompts to analyze issues, provide solutions, and draft responses.

## Prompt Chaining with PromptLayer

PromptLayer offers a comprehensive platform for implementing prompt chaining, enabling users to visually create, manage, and deploy complex workflows involving Large Language Models (LLMs). This approach allows for the breakdown of intricate tasks into a series of interconnected steps, enhancing the AI's ability to handle sophisticated problems effectively.

**Key Features of PromptLayer's Prompt Chaining:**

- **Visual Workflow Builder:** Design prompt chains through an intuitive interface, facilitating collaboration among team members, including non-technical stakeholders.
- **Version Control:** Maintain a history of workflow iterations, enabling users to track changes and revert to previous versions as needed.
- **Interactive Playground:** Test workflows dynamically, allowing initiation or termination at any node to assess performance and identify potential improvements.
- **A/B Testing:** Conduct experiments based on user segments to optimize workflow performance and determine the most effective prompt sequences.
- **Release Labels:** Manage different environments, such as production and development, directly through the dashboard without requiring code changes.
- **Parallelized Execution:** Automatically parallelize workflows to enhance performance and reduce latency.
- **Chain Comparison:** Analyze and compare the performance of various prompt chains, both simple and complex, to identify the most efficient configurations.

PromptLayer streamlines the development and deployment of prompt chains, facilitating more controlled and detailed interactions with AI models.

## Conclusion

Prompt chaining is a valuable technique that amplifies LLM capabilities and enables the creation of more sophisticated AI applications. By segmenting complex tasks and maintaining context, it elevates accuracy, control, and transparency in LLM interactions. While some limitations exist, its benefits position it as a crucial tool for developers and researchers across various domains. As LLMs advance, prompt chaining will likely play an even greater role in shaping the future of AI.

### Original URL
https://blog.promptlayer.com/what-is-prompt-chaining/
</details>

---
<details>
<summary>Building Effective AI Agents \ Anthropic</summary>

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

- LangGraph @https://langchain-ai.github.io/langgraph/ from LangChain;
- Amazon Bedrock's AI Agent framework @https://aws.amazon.com/bedrock/agents/;
- Rivet @https://rivet.ironcladapp.com/, a drag and drop GUI LLM workflow builder; and
- Vellum @https://www.vellum.ai/, another GUI tool for building and testing complex workflows.

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

See our cookbook @https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents for some sample implementations.

## Building blocks, workflows, and agents

In this section, we’ll explore the common patterns for agentic systems we’ve seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents.

### Building block: The augmented LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol @https://www.anthropic.com/news/model-context-protocol, which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation @https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients.

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

- A coding Agent to resolve SWE-bench tasks @https://www.anthropic.com/research/swe-bench-sonnet, which involve edits to many files based on a task description;
- Our “computer use” reference implementation @https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo, where Claude uses a computer to accomplish tasks.

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

In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified @https://www.anthropic.com/research/swe-bench-sonnet benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.

## Appendix 2: Prompt engineering your tools

No matter which agentic system you're building, tools will likely be an important part of your agent. Tools @https://www.anthropic.com/news/tool-use-ga enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block @https://docs.anthropic.com/en/docs/build-with-claude/tool-use#example-api-response-with-a-tool-use-content-block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools.

There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes.

Our suggestions for deciding on tool formats are the following:

- Give the model enough tokens to "think" before it writes itself into a corner.
- Keep the format close to what the model has seen naturally occurring in text on the internet.
- Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.

One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good _agent_-computer interfaces (ACI). Here are some thoughts on how to do so:

- Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it’s probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools.
- How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools.
- Test how the model uses your tools: Run many example inputs in our workbench @https://console.anthropic.com/workbench to see what mistakes the model makes, and iterate.
- Poka-yoke @https://en.wikipedia.org/wiki/Poka-yoke your tools. Change the arguments so that it is harder to make mistakes.

While building our agent for SWE-bench @https://www.anthropic.com/research/swe-bench-sonnet, we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.

### Original URL
https://www.anthropic.com/research/building-effective-agents
</details>

---

## Additional Sources Scraped

---
<details>
<summary>Prompt Chaining | Prompt Engineering Guide </summary>

To improve the reliability and performance of LLMs, one of the important prompt engineering techniques is to break tasks into its subtasks. Once those subtasks have been identified, the LLM is prompted with a subtask and then its response is used as input to another prompt. This is what's referred to as prompt chaining, where a task is split into subtasks with the idea to create a chain of prompt operations.

Prompt chaining is useful to accomplish complex tasks which an LLM might struggle to address if prompted with a very detailed prompt. In prompt chaining, chain prompts perform transformations or additional processes on the generated responses before reaching a final desired state.

Besides achieving better performance, prompt chaining helps to boost the transparency of your LLM application, increases controllability, and reliability. This means that you can debug problems with model responses much more easily and analyze and improve performance in the different stages that need improvement.

Prompt chaining is particularly useful when building LLM-powered conversational assistants and improving the personalization and user experience of your applications.

Prompt chaining can be used in different scenarios that could involve several operations or transformations. For instance, one common use case of LLMs involves answering questions about a large text document. It helps if you design two different prompts where the first prompt is responsible for extracting relevant quotes to answer a question and a second prompt takes as input the quotes and original document to answer a given question. In other words, you will be creating two different prompts to perform the task of answering a question given in a document.

The first prompt below extracts the relevant quotes from the document given the question. Note that for simplicity, we have added a placeholder for the document `{{document}}`. To test the prompt you can copy and paste an article from Wikipedia such as this page for prompt engineering (opens in a new tab) @https://en.wikipedia.org/wiki/Prompt_engineering. Due to larger context used for this task, we are using the `gpt-4-1106-preview` model from OpenAI. You can use the prompt with other long-context LLMs like Claude.

Prompt 1:

```nx-border-black nx-border-opacity-[0.04] nx-bg-opacity-[0.03] nx-bg-black nx-break-words nx-rounded-md nx-border nx-py-0.5 nx-px-[.25em] nx-text-[.9em] dark:nx-border-white/10 dark:nx-bg-white/10
You are a helpful assistant. Your task is to help answer a question given in a document. The first step is to extract quotes relevant to the question from the document, delimited by ####. Please output the list of quotes using <quotes></quotes>. Respond with "No relevant quotes found!" if no relevant quotes were found.

####
{{document}}
####
```

Output of Prompt 1:

```nx-border-black nx-border-opacity-[0.04] nx-bg-opacity-[0.03] nx-bg-black nx-break-words nx-rounded-md nx-border nx-py-0.5 nx-px-[.25em] nx-text-[.9em] dark:nx-border-white/10 dark:nx-bg-white/10
<quotes>
- Chain-of-thought (CoT) prompting[27]
- Generated knowledge prompting[37]
- Least-to-most prompting[38]
- Self-consistency decoding[39]
- Complexity-based prompting[41]
- Self-refine[42]
- Tree-of-thought prompting[43]
- Maieutic prompting[45]
- Directional-stimulus prompting[46]
- Textual inversion and embeddings[59]
- Using gradient descent to search for prompts[61][62][63][64]
- Prompt injection[65][66][67]
</quotes>
```

The quotes that were returned in the first prompt can now be used as input to the second prompt below. Note that you can clean up the quotes a bit more, i.e., remove the citations. Those citations could be removed or utilized as part of another prompt in the chain but you can ignore this for now. The second prompt then takes the relevant quotes extracted by prompt 1 and prepares a helpful response to the question given in the document and those extracted quotes. The second prompt can be the following:

Prompt 2:

```nx-border-black nx-border-opacity-[0.04] nx-bg-opacity-[0.03] nx-bg-black nx-break-words nx-rounded-md nx-border nx-py-0.5 nx-px-[.25em] nx-text-[.9em] dark:nx-border-white/10 dark:nx-bg-white/10
Given a set of relevant quotes (delimited by <quotes></quotes>) extracted from a document and the original document (delimited by ####), please compose an answer to the question. Ensure that the answer is accurate, has a friendly tone, and sounds helpful.

####
{{document}}
####

<quotes>
- Chain-of-thought (CoT) prompting[27]
- Generated knowledge prompting[37]
- Least-to-most prompting[38]
- Self-consistency decoding[39]
- Complexity-based prompting[41]
- Self-refine[42]
- Tree-of-thought prompting[43]
- Maieutic prompting[45]
- Directional-stimulus prompting[46]
- Textual inversion and embeddings[59]
- Using gradient descent to search for prompts[61][62][63][64]
- Prompt injection[65][66][67]
</quotes>
```

Output of Prompt 2:

```nx-border-black nx-border-opacity-[0.04] nx-bg-opacity-[0.03] nx-bg-black nx-break-words nx-rounded-md nx-border nx-py-0.5 nx-px-[.25em] nx-text-[.9em] dark:nx-border-white/10 dark:nx-bg-white/10
The prompting techniques mentioned in the document include:

1. Chain-of-thought (CoT) prompting[27]
2. Generated knowledge prompting[37]
3. Least-to-most prompting[38]
4. Self-consistency decoding[39]
5. Complexity-based prompting[41]
6. Self-refine[42]
7. Tree-of-thought prompting[43]
8. Maieutic prompting[45]
9. Directional-stimulus prompting[46]
10. Textual inversion and embeddings[59]
11. Using gradient descent to search for prompts[61][62][63][64]
12. Prompt injection[65][66][67]

Each of these techniques employs unique strategies to enhance or specify the interactions with large language models to produce the desired outcomes.
```

As you can see, simplifying and creating prompt chains is a useful prompting approach where the responses need to undergo several operations or transformations. As an exercise, feel free to design a prompt that removes the citations (e.g., \[27\]) from the response before sending this as a final response to the user of your application.

You can also find more examples of prompt chaining in this documentation (opens in a new tab) @https://docs.anthropic.com/claude/docs/prompt-chaining that leverages the Claude LLM. Our example is inspired and adapted from their examples.

### Original URL
https://www.promptingguide.ai/techniques/prompt_chaining
</details>

---
<details>
<summary>Claude 4 prompt engineering best practices - Anthropic</summary>

This guide provides specific prompt engineering techniques for Claude 4 models (Opus 4 and Sonnet 4) to help you achieve optimal results in your applications. These models have been trained for more precise instruction following than previous generations of Claude models.

## General principles

### Be explicit with your instructions

Claude 4 models respond well to clear, explicit instructions. Being specific about your desired output can help enhance results. Customers who desire the “above and beyond” behavior from previous Claude models might need to more explicitly request these behaviors with Claude 4.

Example: Creating an analytics dashboard

**Less effective:**

```text
Create an analytics dashboard

```

**More effective:**

```text
Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.

```

### Add context to improve performance

Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude 4 better understand your goals and deliver more targeted responses.

Example: Formatting preferences

**Less effective:**

```text
NEVER use ellipses

```

**More effective:**

```text
Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them.

```

Claude is smart enough to generalize from the explanation.

### Be vigilant with examples & details

Claude 4 models pay attention to details and examples as part of instruction following. Ensure that your examples align with the behaviors you want to encourage and minimize behaviors you want to avoid.

## Guidance for specific situations

### Control the format of responses

There are a few ways that we have found to be particularly effective in steering output formatting in Claude 4 models:

1. **Tell Claude what to do instead of what not to do**
   - Instead of: “Do not use markdown in your response”
   - Try: “Your response should be composed of smoothly flowing prose paragraphs.”
2. **Use XML format indicators**
   - Try: “Write the prose sections of your response in <smoothly\_flowing\_prose\_paragraphs> tags.”
3. **Match your prompt style to the desired output**

The formatting style used in your prompt may influence Claude’s response style. If you are still experiencing steerability issues with output formatting, we recommend as best as you can matching your prompt style to your desired output style. For example, removing markdown from your prompt can reduce the volume of markdown in the output.

### Leverage thinking & interleaved thinking capabilities

Claude 4 offers thinking capabilities that can be especially helpful for tasks involving reflection after tool use or complex multi-step reasoning. You can guide its initial or interleaved thinking for better results.

Example prompt

```text
After receiving tool results, carefully reflect on their quality and determine optimal next steps before proceeding. Use your thinking to plan and iterate based on this new information, and then take the best next action.

```

For more information on thinking capabilities, see Extended thinking.

### Optimize parallel tool calling

Claude 4 models excel at parallel tool execution. They have a high success rate in using parallel tool calling without any prompting to do so, but some minor prompting can boost this behavior to ~100% parallel tool use success rate. We have found this prompt to be most effective:

Sample prompt for agents

```text
For maximum efficiency, whenever you need to perform multiple independent operations, invoke all relevant tools simultaneously rather than sequentially.

```

### Reduce file creation in agentic coding

Claude 4 models may sometimes create new files for testing and iteration purposes, particularly when working with code. This approach allows Claude to use files, especially python scripts, as a ‘temporary scratchpad’ before saving its final output. Using temporary files can improve outcomes particularly for agentic coding use cases.

If you’d prefer to minimize net new file creation, you can instruct Claude to clean up after itself:

Sample prompt

```text
If you create any temporary new files, scripts, or helper files for iteration, clean up these files by removing them at the end of the task.

```

### Enhance visual and frontend code generation

For frontend code generation, you can steer Claude 4 models to create complex, detailed, and interactive designs by providing explicit encouragement:

Sample prompt

```text
Don't hold back. Give it your all.

```

You can also improve Claude’s frontend performance in specific areas by providing additional modifiers and details on what to focus on:

- “Include as many relevant features and interactions as possible”
- “Add thoughtful details like hover states, transitions, and micro-interactions”
- “Create an impressive demonstration showcasing web development capabilities”
- “Apply design principles: hierarchy, contrast, balance, and movement”

### Avoid focusing on passing tests and hard-coding

Frontier language models can sometimes focus too heavily on making tests pass at the expense of more general solutions. To prevent this behavior and ensure robust, generalizable solutions:

Sample prompt

```text
Please write a high quality, general purpose solution. Implement a solution that works correctly for all valid inputs, not just the test cases. Do not hard-code values or create solutions that only work for specific test inputs. Instead, implement the actual logic that solves the problem generally.

Focus on understanding the problem requirements and implementing the correct algorithm. Tests are there to verify correctness, not to define the solution. Provide a principled implementation that follows best practices and software design principles.

If the task is unreasonable or infeasible, or if any of the tests are incorrect, please tell me. The solution should be robust, maintainable, and extendable.

```

## Migration considerations

When migrating from Sonnet 3.7 to Claude 4:

1. **Be specific about desired behavior**: Consider describing exactly what you’d like to see in the output.

2. **Frame your instructions with modifiers**: Adding modifiers that encourage Claude to increase the quality and detail of its output can help better shape Claude’s performance. For example, instead of “Create an analytics dashboard”, use “Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.”

3. **Request specific features explicitly**: Animations and interactive elements should be requested explicitly when desired.

### Original URL
https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
</details>

---
<details>
<summary>Building Effective AI Agents \ Anthropic</summary>

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

- LangGraph @https://langchain-ai.github.io/langgraph/ from LangChain;
- Amazon Bedrock's AI Agent framework @https://aws.amazon.com/bedrock/agents/;
- Rivet @https://rivet.ironcladapp.com/, a drag and drop GUI LLM workflow builder; and
- Vellum @https://www.vellum.ai/, another GUI tool for building and testing complex workflows.

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

See our cookbook @https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents for some sample implementations.

## Building blocks, workflows, and agents

In this section, we’ll explore the common patterns for agentic systems we’ve seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents.

### Building block: The augmented LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released Model Context Protocol @https://www.anthropic.com/news/model-context-protocol, which allows developers to integrate with a growing ecosystem of third-party tools with a simple client implementation @https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients.

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

- A coding Agent to resolve SWE-bench tasks @https://www.anthropic.com/research/swe-bench-sonnet, which involve edits to many files based on a task description;
- Our “computer use” reference implementation @https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo, where Claude uses a computer to accomplish tasks.

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

In our own implementation, agents can now solve real GitHub issues in the SWE-bench Verified @https://www.anthropic.com/research/swe-bench-sonnet benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.

## Appendix 2: Prompt engineering your tools

No matter which agentic system you're building, tools will likely be an important part of your agent. Tools @https://www.anthropic.com/news/tool-use-ga enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a tool use block @https://docs.anthropic.com/en/docs/build-with-claude/tool-use#example-api-response-with-a-tool-use-content-block in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools.

There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes.

Our suggestions for deciding on tool formats are the following:

- Give the model enough tokens to "think" before it writes itself into a corner.
- Keep the format close to what the model has seen naturally occurring in text on the internet.
- Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.

One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good _agent_-computer interfaces (ACI). Here are some thoughts on how to do so:

- Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it’s probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools.
- How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools.
- Test how the model uses your tools: Run many example inputs in our workbench @https://console.anthropic.com/workbench to see what mistakes the model makes, and iterate.
- Poka-yoke @https://en.wikipedia.org/wiki/Poka-yoke your tools. Change the arguments so that it is harder to make mistakes.

While building our agent for SWE-bench @https://www.anthropic.com/research/swe-bench-sonnet, we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.

### Original URL
https://www.anthropic.com/engineering/building-effective-agents
</details>

---
<details>
<summary>Chain complex prompts for stronger performance - Anthropic</summary>

Anthropic home page![light logo @https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg!dark logo @https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg](https://docs.anthropic.com/)

English

Search...

Ctrl K

Search...

Navigation

Prompt engineering

Chain complex prompts for stronger performance

Welcome @https://docs.anthropic.com/en/home Developer Guide @https://docs.anthropic.com/en/docs/intro API Guide @https://docs.anthropic.com/en/api/overview Claude Code @https://docs.anthropic.com/en/docs/claude-code/overview Model Context Protocol (MCP) @https://docs.anthropic.com/en/docs/mcp Resources @https://docs.anthropic.com/en/resources/overview Release Notes @https://docs.anthropic.com/en/release-notes/overview

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models here @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips.

When working with complex tasks, Claude can sometimes drop the ball if you try to handle everything in a single prompt. Chain of thought (CoT) prompting is great, but what if your task has multiple distinct steps that each require in-depth thought?

Enter prompt chaining: breaking down complex tasks into smaller, manageable subtasks.

## ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#why-chain-prompts%3F  Why chain prompts?

1. **Accuracy**: Each subtask gets Claude’s full attention, reducing errors.
2. **Clarity**: Simpler subtasks mean clearer instructions and outputs.
3. **Traceability**: Easily pinpoint and fix issues in your prompt chain.

* * *

## ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#when-to-chain-prompts  When to chain prompts

Use prompt chaining for multi-step tasks like research synthesis, document analysis, or iterative content creation. When a task involves multiple transformations, citations, or instructions, chaining prevents Claude from dropping or mishandling steps.

**Remember:** Each link in the chain gets Claude’s full attention!

**Debugging tip**: If Claude misses a step or performs poorly, isolate that step in its own prompt. This lets you fine-tune problematic steps without redoing the entire task.

* * *

## ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#how-to-chain-prompts  How to chain prompts

1. **Identify subtasks**: Break your task into distinct, sequential steps.
2. **Structure with XML for clear handoffs**: Use XML tags to pass outputs between prompts.
3. **Have a single-task goal**: Each subtask should have a single, clear objective.
4. **Iterate**: Refine subtasks based on Claude’s performance.

### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#example-chained-workflows%3A  Example chained workflows:

- **Multi-step analysis**: See the legal and business examples below.
- **Content creation pipelines**: Research → Outline → Draft → Edit → Format.
- **Data processing**: Extract → Transform → Analyze → Visualize.
- **Decision-making**: Gather info → List options → Analyze each → Recommend.
- **Verification loops**: Generate content → Review → Refine → Re-review.

**Optimization tip**: For tasks with independent subtasks (like analyzing multiple docs), create separate prompts and run them in parallel for speed.

### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#advanced%3A-self-correction-chains  Advanced: Self-correction chains

You can chain prompts to have Claude review its own work! This catches errors and refines outputs, especially for high-stakes tasks.

Example: Self-correcting research summary

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-1  Prompt 1

| Role | Content |
| --- | --- |
| User | Summarize this medical research paper.<br><paper>{{RESEARCH\_PAPER}}</paper><br>Focus on methodology, findings, and clinical implications. |
| Assistant<br>{{SUMMARY}} | Methodology: Double-blind RCT with 500 Type 2 diabetes patients. Group A (n=250) received novel GLP-1/GIP dual agonist; Group B (n=250) received standard GLP-1 agonist. 24-week trial, primary endpoint: HbA1c reduction.<br>Findings:<br>\- Group A: 1.8% mean HbA1c reduction<br>\- Group B: 1.1% mean HbA1c reduction<br>\- 68% of Group A vs. 52% of Group B achieved HbA1c <7%<br>\- Group A: 5.2kg mean weight loss<br>\- Group B: 3.1kg mean weight loss<br>Safety: Similar adverse event profiles, no serious events attributed to treatment.<br>Clinical Implications: Dual agonist shows superior glycemic control and weight loss compared to standard therapy. Could be a game-changer, especially for obese diabetics. |

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-2  Prompt 2

| Role | Content |
| --- | --- |
| User | Your task is to provide feedback on a research paper summary. Here is a summary of a medical research paper:<br><summary><br>{{SUMMARY}}<br></summary><br>Here is the research paper:<br><paper><br>{{RESEARCH\_PAPER}}<br></paper><br>Review this summary for accuracy, clarity, and completeness on a graded A-F scale. |
| Assistant<br>{{FEEDBACK}} | 1\. Accuracy: A<br> \- Correctly reported key stats: HbA1c reductions, weight loss.<br> \- Accurately noted safety profile and lack of serious adverse events.<br> \- Assertion of “game-changer” is justified by significantly better outcomes.<br>2\. Clarity: A-<br> \- Concise and well-structured with clear sections.<br> \- Good use of comparative language (e.g., “up 3% from Q1”) for context.<br> \- Minor issue: Acronyms like “RCT,” “GLP-1,” and “GIP” not defined. Consider spelling out first use.<br>3\. Completeness: B+<br> \- Covers all requested areas: methodology, findings, clinical implications.<br> \- Missing: Baseline characteristics of groups (were they well-matched?).<br> \- Missing: Any secondary endpoints (e.g., blood pressure, lipids).<br> \- Consider: Long-term implications or need for further research.<br>Overall, the summary is accurate and clear, providing key insights for a quick grasp of the study. To elevate to A+, define acronyms, mention group baseline stats, note any secondary outcomes, and briefly touch on the need for long-term studies. |

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-3  Prompt 3

| Role | Content |
| --- | --- |
| User | Your task is to improve a paper summary given feedback. Here is the first draft of a medical research paper:<br><summary><br>{{SUMMARY}}<br></summary><br>Here is the research paper:<br><paper><br>{{RESEARCH\_PAPER}}<br></paper><br>Here is the feedback:<br><feedback><br>{{FEEDBACK}}<br></feedback><br>Update the summary based on the feedback. |
| Assistant | Methodology: Double-blind randomized controlled trial (RCT) with 500 Type 2 diabetes patients. Group A (n=250) received a novel glucagon-like peptide-1/glucose-dependent insulinotropic polypeptide (GLP-1/GIP) dual agonist; Group B (n=250) received a standard GLP-1 agonist. The 24-week trial’s primary endpoint was HbA1c reduction. Groups were well-matched for age, BMI, and baseline HbA1c.<br>Findings:<br>\- Group A: 1.8% mean HbA1c reduction<br>\- Group B: 1.1% mean HbA1c reduction<br>\- 68% of Group A vs. 52% of Group B achieved HbA1c <7%<br>\- Group A: 5.2kg mean weight loss<br>\- Group B: 3.1kg mean weight loss<br>Secondary endpoints showed improvements in blood pressure and lipid profiles for both groups, with Group A showing slightly better results.<br>Safety: Similar adverse event profiles, with no serious events attributed to either treatment.<br>Clinical Implications: The dual GLP-1/GIP agonist demonstrates superior glycemic control and weight loss compared to standard GLP-1 therapy. These results suggest it could be a significant advancement, particularly for obese diabetics. However, longer-term studies are needed to confirm sustained efficacy and safety, as well as to investigate potential benefits on cardiovascular outcomes. |

* * *

## ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#examples  Examples

Example: Analyzing a legal contract (without chaining)

Note that Claude misses the instruction to provide proposed changes in its email draft.

| Role | Content |
| --- | --- |
| User | You’re our Chief Legal Officer. Review this SaaS contract for risks, focusing on data privacy, SLAs, and liability caps.<br><contract><br>{{CONTRACT}}<br></contract><br>Then draft an email to the vendor with your concerns and proposed changes. |
| Assistant | After reviewing the SaaS contract, I’ve identified several concerns:<br>1\. Data Privacy (Section 7):<br> \- Issue: Vendor has broad rights to use client data for “service improvement.”<br> \- Risk: Could lead to unauthorized data sharing or monetization.<br>2\. SLAs (Section 5):<br> \- Issue: 99.5% uptime guarantee is below industry standard.<br> \- Risk: Excessive downtime could impact our operations.<br>3\. Liability (Section 9):<br> \- Issue: Cap set at 3 months of fees.<br> \- Risk: Inadequate for potential data breaches or service failures.<br>Draft email:<br>Dear {{VENDOR}},<br>After reviewing the SaaS agreement, we have concerns:<br>1\. Data Privacy: We require that our data only be used for direct service provision, not broad “service improvement.” Please amend Section 7.<br>2\. SLAs: 99.5% uptime is insufficient. We need 99.99% with clearly defined penalties. Please revise Section 5.<br>3\. Liability: The current cap of 3 months’ fees is inadequate. We propose a cap of 12 months’ fees, with no cap for data breaches or willful misconduct.<br>We value our potential partnership and believe these changes will set us up for success. Please send a revised agreement.<br>Best regards,<br>{{CLO\_NAME}} |

Example: Analyzing a legal contract (with chaining)

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-1-2  Prompt 1

| Role | Content |
| --- | --- |
| User | You’re our Chief Legal Officer. Review this SaaS contract for risks, focusing on data privacy, SLAs, and liability caps.<br><contract><br>{{CONTRACT}}<br></contract><br>Output your findings in <risks> tags. |
| Assistant<br>{{CONCERNS}} | 1\. Data Privacy (Section 7):<br> \- Issue: Vendor has broad rights to use client data for “service improvement.”<br> \- Risk: Could lead to unauthorized data sharing or monetization of client data.<br> \- Impact: Potential breach of client trust, regulatory fines (GDPR, CCPA).<br>2\. SLAs (Section 5):<br> \- Issue: 99.5% uptime guarantee is below industry standard (typically 99.99%).<br> \- Risk: Up to 43.8 hours of downtime per year vs. 52.6 minutes at 99.99%.<br> \- Impact: Operational disruptions, revenue loss, client dissatisfaction.<br>3\. Liability (Section 9):<br> \- Issue: Liability cap set at 3 months of fees.<br> \- Risk: Inadequate for potential data breaches, IP theft, or prolonged service failures.<br> \- Impact: Insufficient compensation for damages that could far exceed the cap, like class-action lawsuits or regulatory fines. |

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-2-2  Prompt 2

| Role | Content |
| --- | --- |
| User | Draft an email to a SaaS product vendor outlining the following concerns and proposing changes. Here are the concerns:<br><concerns><br>{{CONCERNS}}<br></concerns> |
| Assistant<br>{{EMAIL}} | Dear {{VENDOR}},<br>After a thorough review of the proposed SaaS agreement, our legal team has identified several high-priority concerns that must be addressed before we can proceed:<br>1\. Data Privacy (Section 7):<br> \- Current: Broad rights to use client data for “service improvement.”<br> \- Concern: Potential unauthorized data sharing or monetization.<br> \- Proposed Change: Limit data use to direct service provision. Any use for improvement, analytics, or marketing must be opt-in, revocable, and anonymized.<br>2\. SLAs (Section 5):<br> \- Current: 99.5% uptime guarantee.<br> \- Concern: Up to 43.8 hours of downtime per year, risking operational disruptions.<br> \- Proposed Change: 99.99% uptime with tiered service credits. E.g., 10% credit for <99.99%, 25% for <99.9%, 50% for <99.5%.<br>3\. Liability (Section 9):<br> \- Current: Cap at 3 months of fees.<br> \- Concern: Grossly inadequate for data breaches, IP theft, or prolonged outages.<br> \- Proposed Change: 12 months’ fees for general liability. Uncapped for data breaches, willful misconduct, IP infringement.<br>These changes are non-negotiable for us. They align with industry standards and our commitment to data security, operational excellence, and fiduciary responsibility. We value the potential of our partnership, and addressing these will set a strong foundation.<br>Please have your legal team review and incorporate these changes. We’re happy to discuss further to ensure mutual understanding and agreement.<br>Best regards,<br>{{CLO\_NAME}} |

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-3-2  Prompt 3

| Role | Content |
| --- | --- |
| User | Your task is to review an email and provide feedback. Here is the email:<br><email><br>{{EMAIL}}<br></email><br>Give feedback on tone, clarity, and professionalism. |
| Assistant | 1\. Tone:<br> \- Professional and assertive without being confrontational.<br> \- Use of “non-negotiable” is strong but justified given the criticality of the issues.<br> \- Collaborative language (“we value,” “happy to discuss”) balances the firmness, maintaining a constructive tone.<br>2\. Clarity:<br> \- Excellent structuring: Current state, concern, and proposed change for each issue.<br> \- Technical terms (e.g., “EBITDA,” “tiered service credits”) are appropriate for a B2B SaaS context.<br> \- Action items are clear: vendor’s legal team to review and incorporate changes.<br>3\. Professionalism:<br> \- Focuses on mutual benefit and industry standards, not just our demands.<br> \- Mentions broader responsibilities (data security, operational excellence, fiduciary duty), elevating the discussion.<br> \- Offers further discussion, showing commitment to understanding and resolving issues.<br>Overall, the email strikes the right balance of assertiveness and collaboration. It clearly articulates our concerns, proposes specific solutions, and maintains a professional, partnership-oriented tone. No revisions needed; proceed with sending. |

Example: Multitenancy strategy review

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-1-3  Prompt 1

| Role | Content |
| --- | --- |
| User | As a senior solutions architect, review and analyze this multitenancy strategy for our new enterprise SaaS product.<br><strategy><br>{{STRATEGY}}<br></strategy><br>Focus on scalability, security, and cost-effectiveness. |
| Assistant<br>{{ANALYSIS}} | 1\. Scalability:<br> \+ Database sharding by tenant reduces contention, supports high growth.<br> \+ Microservices allow independent scaling of components.<br> \- Shared app servers could bottleneck under extreme load.<br> \- No mention of auto-scaling or load balancing for app tier.<br>2\. Security:<br> \+ Tenant data isolation via sharding mitigates data leaks.<br> \+ JWT with short expiry and refresh tokens is industry best practice.<br> \- No mention of encryption (at rest, in transit) or key management.<br> \- IAM strategy lacks detail on roles, permissions, or RBAC.<br>3\. Cost-effectiveness:<br> \+ Shared app servers reduce idle resource costs.<br> \+ Serverless functions for infrequent tasks optimize costs.<br> \- Per-tenant DB could increase costs at scale vs. optimized multi-tenant DB.<br> \- No discussion of reserved instances or spot instances for cost saving. |

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-2-3  Prompt 2

| Role | Content |
| --- | --- |
| User | Draft a strategy review document for engineering leadership based on this analysis of a multitenancy strategy.<br><strategy><br>{{STRATEGY}}<br></strategy><br><analysis><br>{{ANALYSIS}}<br></analysis><br>Include an executive summary, detailed analysis, and recommendations. |
| Assistant<br>{{STRATEGY\_DOC}} | \# Multitenancy Strategy Review: SaaS Enterprise Product<br>\## Executive Summary<br>The proposed strategy demonstrates a solid foundation in scalability and security principles but has gaps in implementation details. It excels in data isolation and component-level scaling but lacks robust app-tier scaling and advanced security measures. Cost optimizations are present but may falter at high scale. With targeted enhancements, this strategy can effectively support our enterprise SaaS ambitions.<br>\## Detailed Analysis<br>\### 1\. Scalability: B+<br>Strengths:<br>\- Database sharding by tenant is excellent. It minimizes query latency, supports high data growth, and facilitates seamless per-tenant scaling.<br>\- Microservices architecture allows scaling individual components based on demand, crucial for handling diverse enterprise workloads.<br>Weaknesses:<br>\- Shared application servers risk becoming a bottleneck. As tenant count and traffic grow, these could degrade performance across all tenants.<br>\- Absence of auto-scaling and load balancing for the app tier is a critical oversight. These are essential for handling traffic spikes without over-provisioning.<br>\### 2\. Security: B-<br>Strengths:<br>\- Sharded databases provide strong tenant data isolation, mitigating risks of data leaks or unauthorized access between tenants.<br>\- JWT with short expiry and refresh tokens align with OWASP best practices, reducing token vulnerability windows.<br>Weaknesses:<br>\- No mention of data encryption at rest or in transit (TLS 1.3). This is non-negotiable for enterprise data.<br>\- Key management strategy is missing. How are encryption keys, JWT secrets, and DB credentials managed and rotated?<br>\- IAM lacks depth. We need RBAC with well-defined roles, attribute-based access control (ABAC) for fine-grained permissions, and integration with enterprise identity providers (SAML, OIDC).<br>\### 3\. Cost-effectiveness: B<br>Strengths:<br>\- Shared app servers reduce idle capacity costs, good for steady-state traffic.<br>\- Serverless for infrequent tasks (e.g., reporting) is smart; pay only when these resources are used.<br>Weaknesses:<br>\- Per-tenant databases may not be cost-effective at scale compared to a well-designed multi-tenant database with robust data partitioning.<br>\- No mention of cost-saving measures like reserved instances for predictable workloads or spot instances for fault-tolerant tasks.<br>\- Lack of app-tier auto-scaling could lead to over-provisioning, increasing costs.<br>\## Recommendations<br>1\. **App Tier Resilience**: Implement auto-scaling with Kubernetes or cloud-native services (EKS, GKE). Deploy across availability zones with a CDN for static assets.<br>2\. **Security Hardening**:<br> a. Encrypt data at rest (AES-256) and in transit (TLS 1.3).<br> b. Use a managed KMS (AWS KMS, GCP KMS) for key management.<br> c. Enhance IAM with RBAC, ABAC, and SAML/OIDC for enterprise SSO.<br>3\. **Cost Optimization**:<br> a. Evaluate columnar multi-tenant DB (e.g., Snowflake) vs. sharding at scale.<br> b. Use reserved instances for app servers, spot instances for non-critical workloads.<br> c. Implement proactive monitoring and right-sizing to avoid overprovisioning.<br>4\. **Proof of Concept (PoC)**: Before full implementation, conduct a PoC with a high-scale simulation:<br> a. Test sharded DB vs. optimized multi-tenant DB for cost and performance.<br> b. Stress-test app tier with simulated enterprise-level traffic spikes.<br> c. Conduct third-party security audit, focusing on data isolation and access controls.<br>With these enhancements, our multi-tenancy strategy will be enterprise-grade: scalable, secure, and cost-effective. The PoC will validate our design choices and instill confidence in our enterprise clients. |

#### ​ @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts\#prompt-3-3  Prompt 3

| Role | Content |
| --- | --- |
| User | Grade this strategy review document for clarity, actionability, and alignment with enterprise priorities. <br><priorities><br>{{PRIORITIES}}<br></priorities><br><strategy\_doc><br>{{STRATEGY\_DOC}}<br></strategy\_doc> |
| Assistant | 1\. Clarity: A<br> \+ Clear structure with Executive Summary, Detailed Analysis, and Recommendations.<br> \+ Analysis uses a grading system (B+, B-) for quick grasp of strengths/weaknesses.<br> \+ Technical terms (RBAC, ABAC, TLS) are explained or contextualized, aiding non-technical leadership.<br> \+ Visual aids (bullet points, indentation) enhance readability.<br>2\. Actionability: A-<br> \+ Recommendations are specific and technical (e.g., “Implement auto-scaling with Kubernetes”).<br> \+ PoC plan with clear objectives provides a roadmap.<br> \+ Missing: Timelines, resource requirements, or team assignments for each recommendation.<br> \+ Consider: Add a “Next Steps” section with immediate actions, roles, and a high-level timeline.<br>3\. Enterprise Alignment: A+<br> \+ Directly addresses enterprise priorities:<br> \- Scalability: Discusses handling enterprise-level traffic spikes.<br> \- Security: Focuses on data isolation, encryption, and enterprise IAM.<br> \- Cost: Strategies align with enterprise FinOps (reserved instances, right-sizing).<br> \+ PoC with “high-scale simulation” and security audit shows commitment to enterprise-grade quality.<br> \+ Language resonates with enterprise concerns: “unacceptable risk,” “enterprise-grade,” “instill confidence.”<br>Overall, the document excels in clarity and enterprise alignment. The actionability is strong but could be elevated to A+ with a “Next Steps” section. The technical depth, coupled with clear explanations, makes this highly effective for both technical and non-technical leadership. Great work! |

* * *

**Prompt library** \\
\\
Get inspired by a curated selection of prompts for various tasks and use cases. @https://docs.anthropic.com/en/resources/prompt-library/library **GitHub prompting tutorial** \\
\\
An example-filled tutorial that covers the prompt engineering concepts found in our docs. @https://github.com/anthropics/prompt-eng-interactive-tutorial **Google Sheets prompting tutorial** \\
\\
A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet. @https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8

Was this page helpful?

YesNo

Prefill Claude's response @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response Long context tips @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips

On this page

- Why chain prompts? @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts#why-chain-prompts%3F
- When to chain prompts @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts#when-to-chain-prompts
- How to chain prompts @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts#how-to-chain-prompts
- Example chained workflows: @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts#example-chained-workflows%3A
- Advanced: Self-correction chains @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts#advanced%3A-self-correction-chains
- Examples @https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts#examples

### Original URL
https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts
</details>

---
<details>
<summary>Workflows and Agents</summary>

This guide reviews common patterns for agentic systems. In describing these systems, it can be useful to make a distinction between "workflows" and "agents". One way to think about this difference is nicely explained here by Anthropic:

> Workflows are systems where LLMs and tools are orchestrated through predefined code paths.
> Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Here is a simple way to visualize these differences:

When building agents and workflows, LangGraph offers a number of benefits including persistence, streaming, and support for debugging as well as deployment.

## Prompt chaining

In prompt chaining, each LLM call processes the output of the previous one.

As noted in the Anthropic blog:

> Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.
>
> When to use this workflow: This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

## Routing

Routing classifies an input and directs it to a followup task. As noted in the Anthropic blog:

> Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.
>
> When to use this workflow: Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

## Orchestrator-Worker

With orchestrator-worker, an orchestrator breaks down a task and delegates each sub-task to workers. As noted in the Anthropic blog:

> In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.
>
> When to use this workflow: This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

### Original URL
https://langchain-ai.github.io/langgraphjs/tutorials/workflows/#routing
</details>

