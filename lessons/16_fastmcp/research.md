# Research

## Research Results

<details>
<summary>What are best practices for structuring a Python FastMCP server with multiple routers for tools, resources, and prompts?</summary>

### Source [1]: https://pypi.org/project/fastmcp/2.2.0/

Query: What are best practices for structuring a Python FastMCP server with multiple routers for tools, resources, and prompts?

Answer: FastMCP is designed to make building MCP servers and clients simple and intuitive for Python developers. The core object is the `FastMCP` server, which handles connection management, protocol details, and routing. You create a server instance with a name and, optionally, dependencies needed for deployment. The server is then populated with tools, resources, and prompts using decorators.

**Tools** are defined by decorating Python functions (sync or async) with `@mcp.tool()`. These functions can perform computations, call external APIs, or execute side effects. FastMCP automatically generates the MCP schema from Python type hints and docstrings, and supports Pydantic models for complex inputs. Tools are ideal for actions that change state or interact with external systems.

**Resources** expose read-only data, analogous to GET endpoints in a web API. While the PyPI page does not explicitly show the `@mcp.resource()` decorator, it emphasizes that resources are a core concept, allowing you to load information into the LLM’s context. Resources are typically defined by associating a Python function with a URI.

**Prompts** are reusable templates for interaction patterns, though the PyPI page does not provide a code example for prompts. The documentation suggests that prompts are another building block alongside tools and resources.

The server can be run locally using the `fastmcp run server.py` command. FastMCP abstracts away protocol and server management, letting you focus on defining your tools, resources, and prompts in clean, Pythonic code. The decorator-based approach is central to structuring your server, making it easy to organize and maintain as your application grows.

-----

-----

### Source [2]: https://github.com/modelcontextprotocol/python-sdk

Query: What are best practices for structuring a Python FastMCP server with multiple routers for tools, resources, and prompts?

Answer: The official Python SDK for Model Context Protocol provides detailed examples and advanced patterns for structuring FastMCP servers. A key feature is the **lifespan context**, which allows you to manage application-wide resources (like database connections) in a type-safe way. You define an async context manager (`app_lifespan`) that yields an application context object (e.g., `AppContext` containing a database). This context is passed to the `FastMCP` constructor, making it available to all tools via the `Context` parameter.

**Tools** can access the lifespan context to utilize initialized resources (e.g., a database). This pattern is useful for dependency injection and ensures resources are properly initialized and cleaned up. The example shows a tool (`query_db`) that uses the database from the lifespan context.

The SDK emphasizes **strong typing** throughout, including for tool inputs, outputs, and application context. This helps maintain clarity and safety as your server grows. While the example focuses on tools and lifespan management, the same principles apply to organizing resources and prompts: define them as decorated functions, and use context objects for shared state or dependencies.

This source does not explicitly discuss multiple routers, but the pattern of grouping related tools, resources, and prompts into modules—each potentially with its own context—is a natural extension of the provided examples. The lifespan and context system is especially valuable for larger, modular servers.

-----

-----

### Source [3]: https://github.com/jlowin/fastmcp

Query: What are best practices for structuring a Python FastMCP server with multiple routers for tools, resources, and prompts?

Answer: The jlowin/fastmcp repository provides comprehensive documentation on core FastMCP concepts. The **FastMCP Server** is the central object that holds your tools, resources, and prompts, manages connections, and supports configuration (e.g., authentication).

**Tools** are added via the `@mcp.tool` decorator on Python functions. FastMCP generates schemas from type hints and docstrings, supporting both synchronous and asynchronous functions. Tools can return a variety of types, including JSON-serializable objects, text, or media (with helper classes).

**Resources** expose read-only data and are defined with the `@mcp.resource("your://uri")` decorator. You can create both static and dynamic resources; dynamic resources use `{placeholders}` in the URI to accept parameters, enabling clients to request specific data subsets (e.g., `users://{user_id}/profile`).

**Prompts** are mentioned as a core concept but are not detailed in the provided snippet. The documentation suggests that prompts, like tools and resources, are registered with the server instance.

The repository encourages organizing your server by **grouping related tools, resources, and prompts into logical modules**. For example, you might have separate modules for user management, analytics, and system configuration, each exposing their own tools and resources. The server instance acts as the central registry and router for all these components.

Configuration (e.g., host, port, log level) can be passed directly to the `FastMCP` constructor for easy setup. The decorator-based approach and modular organization make it straightforward to scale and maintain complex MCP servers.

-----

-----

### Source [4]: https://apidog.com/blog/fastmcp/

Query: What are best practices for structuring a Python FastMCP server with multiple routers for tools, resources, and prompts?

Answer: Apidog’s beginner’s guide to FastMCP provides practical examples for structuring a server. You start by creating a `FastMCP` instance, optionally passing server settings (e.g., `port`, `host`, `log_level`) as keyword arguments.

**Tools** are added by decorating functions with `@mcp.tool()`. FastMCP leverages Python type hints to define input and output schemas, making tools self-documenting and type-safe. Example tools include simple computations (`add`) and greetings (`greet`).

**Resources** are exposed via the `@mcp.resource()` decorator, which takes a URI string. Resources return data (e.g., application config) and are read-only. The example shows a static resource (`data://config`) returning a dictionary.

The guide emphasizes **modularity**: you can define tools and resources in separate Python files and import them into your main server file. This makes it easy to organize a larger codebase, with each module focusing on a specific domain (e.g., authentication, data access, utilities). The `FastMCP` instance serves as the central router, collecting all registered components.

While the guide does not discuss prompts, the pattern is clear: use Python modules and imports to logically separate your tools, resources, and (by extension) prompts, then register them all with the central server instance. This approach scales well and keeps your codebase maintainable.

-----

-----

### Source [6]: https://modelcontextprotocol.io/docs/develop/build-server

Query: What are best practices for structuring a Python FastMCP server with multiple routers for tools, resources, and prompts?

Answer: This source reiterates that the `FastMCP` class uses Python type hints and docstrings to automatically generate tool definitions, making it easy to create and maintain MCP tools. However, it does not provide specific guidance on structuring a server with multiple routers or organizing tools, resources, and prompts into separate modules. The focus is on the ease of tool creation rather than architectural patterns.

-----

</details>

<details>
<summary>What are the benefits of using server-hosted prompts in MCP for defining and reusing agent workflows across different clients?</summary>

### Source [16]: https://modelcontextprotocol.info/docs/concepts/prompts/

Query: What are the benefits of using server-hosted prompts in MCP for defining and reusing agent workflows across different clients?

Answer: The Model Context Protocol (MCP) allows servers to define, store, and serve reusable prompt templates and workflows, which clients—such as different AI agents or applications—can easily access and use[1]. By hosting prompts on the server, developers can centralize the management of prompt logic, ensuring that updates and improvements are propagated automatically to all clients. Each prompt can specify required and optional arguments (e.g., code to explain, programming language), enabling flexible, context-aware interactions. For instance, a "git-commit" prompt might require a description of changes, while an "explain-code" prompt could take both code and an optional language parameter. Clients request prompts by name and provide the necessary arguments, receiving back structured messages ready for LLM consumption. This approach abstracts prompt engineering from client implementation, allowing non-expert users or applications to leverage sophisticated, pre-tested prompts without needing to understand their internal structure. The server can validate requests, handle errors (e.g., missing prompts), and return appropriate responses, making the system robust and user-friendly. Overall, server-hosted prompts in MCP streamline the development of agent workflows by promoting reuse, consistency, and maintainability across diverse clients and use cases[1].

-----

-----

### Source [17]: https://skywork.ai/skypage/en/ai-potential-prompts-library/1979031702181892096

Query: What are the benefits of using server-hosted prompts in MCP for defining and reusing agent workflows across different clients?

Answer: The Prompts Library MCP Server exemplifies how server-hosted prompts bring order and structure to prompt management by treating prompts as first-class, versioned assets accessible programmatically to any MCP-compatible client[2]. Prompts are stored as Markdown files with YAML frontmatter for metadata (e.g., version, author, tags), enabling easy creation, editing, and organization without a database. The server provides a live, interactive API for CRUD operations, allowing both users and AI agents to dynamically manage the prompt library during conversations. Real-time file watching ensures that edits are instantly reflected, eliminating the need for server restarts. This setup contrasts with static or Git-based prompt collections, which are less interactive and not natively accessible to AI agents. By centralizing prompts on a server, teams avoid the “prompt chaos” of scattered templates and custom integrations, instead benefiting from a single source of truth that is both human- and machine-accessible. The lightweight, open-source architecture (TypeScript/Node.js) ensures the solution is easy to deploy and customize. In summary, the Prompts Library MCP Server demonstrates how server-hosted prompts enable dynamic, organized, and scalable management of agent workflows across clients, fostering collaboration and reducing integration overhead[2].

-----

-----

### Source [18]: https://realpython.com/python-mcp/

Query: What are the benefits of using server-hosted prompts in MCP for defining and reusing agent workflows across different clients?

Answer: MCP servers support prompts as one of three core primitives (alongside resources and tools), allowing developers to define reusable templates that guide LLM interactions[3]. These prompts can accept arguments, reference external context, and orchestrate multi-step workflows, making them far more powerful than static text snippets. By storing prompts on the server, teams can reuse effective instructions across different projects and clients, ensuring consistency and reducing duplication. For example, a prompt for summarizing customer reviews can be defined once and invoked by any client with the appropriate context and question. This not only saves development time but also ensures that best practices in prompt engineering are shared organization-wide. The ability to parameterize prompts and embed them in larger workflows enables sophisticated, context-aware agent behaviors that are easy to maintain and evolve. Server-hosted prompts thus act as a shared knowledge base for LLM interactions, streamlining the development of complex, multi-agent systems and making it easier to onboard new clients or applications[3].

-----

-----

### Source [19]: https://directus.io/docs/guides/ai/mcp/prompts/

Query: What are the benefits of using server-hosted prompts in MCP for defining and reusing agent workflows across different clients?

Answer: Directus highlights that server-hosted prompts in MCP enable the creation of reusable interactions for AI assistants, which is particularly valuable for standardizing responses, creating guided workflows, and ensuring consistent content creation across clients[4]. By storing prompts in a dedicated collection (database table), organizations can manage them centrally, applying permissions and access controls as needed. This setup allows different clients (e.g., various AI assistants or applications) to fetch and execute the same prompts, ensuring that all interactions follow the same rules and quality standards. The system supports both creating new prompt collections and adapting existing ones, with automatic validation to ensure all required fields are present. Directus also emphasizes the importance of setting appropriate permissions so that only authorized users or clients can read or modify prompts. In practice, this means that updates to prompts—whether for improving clarity, fixing issues, or adding new features—are immediately available to all clients, reducing the risk of inconsistency or fragmentation. Server-hosted prompts thus provide a scalable, secure, and maintainable way to define and reuse agent workflows in heterogeneous client environments[4].

-----

</details>

<details>
<summary>How can you implement and test a ReAct-style agent loop in a Python MCP client that performs capability discovery and tool execution?</summary>

### Source [20]: https://neo4j.com/blog/developer/react-agent-langgraph-mcp/

Query: How can you implement and test a ReAct-style agent loop in a Python MCP client that performs capability discovery and tool execution?

Answer: The implementation of a **ReAct-style agent loop in a Python MCP client** can be achieved using LangGraph and MCP adapters. The process is as follows:

- **Agent Workflow**:
  - The agent receives an input question from the user.
  - It decides which tool to call in order to answer the question.
  - Executes the chosen tool.
  - Appends the tool execution result to the context.
  - Analyzes the updated context, deciding if further tool calls or reasoning are needed.
  - This loop (steps 2–5) is repeated until the agent has enough context to answer.
  - Returns the final answer to the user.

- **Setup and Imports**:
  - Required libraries include `langchain_core`, `langgraph`, `langchain_mcp_adapters`, and `mcp` for the Python MCP client.
  - Tools can be loaded from the MCP server using `load_mcp_tools`.
  - Both MCP-hosted tools and locally defined tools can be incorporated.

- **Agent Creation**:
  - Use `create_react_agent` from LangGraph to instantiate the agent, providing it with the language model and the set of discovered tools.
  - Example: The agent can choose between tools like `find_movie_recommendations` or Neo4j-specific tools such as `get_neo4j_schema` and `read_neo4j_cypher` based on the question.

- **Testing**:
  - The agent can be tested via a command-line chat interface (e.g., running `python3 agent.py`).
  - It is observed to correctly select and sequence tool invocations, such as fetching a schema before querying.

- **Adaptation**:
  - For different databases or application domains, update the `.env` file for credentials, swap out tool definitions, and adjust the system prompt accordingly.

This structure provides a template for building and testing ReAct loop agents that leverage both capability discovery (via MCP) and tool execution in Python.

-----

-----

-----

### Source [21]: https://octopus.com/blog/agentic-ai-with-mcp

Query: How can you implement and test a ReAct-style agent loop in a Python MCP client that performs capability discovery and tool execution?

Answer: A **ReAct-style agent loop** using a Python MCP client can be implemented and tested using the following approach:

- **Multi-Server MCP Client**:
  - Use `MultiServerMCPClient` to interact with multiple MCP servers, enabling dynamic tool discovery and execution from different sources (e.g., Octopus and GitHub MCP servers).

- **Agent Construction**:
  - Retrieve tools supported by the MCP servers with `await client.get_tools()`.
  - Create the agent using `create_react_agent`, supplying the language model and the discovered tools.

- **Agent Loop Execution**:
  - Provide the agent with a prompt describing the multi-step task.
  - The agent internally decides which tools to invoke for each step, executes them, and incorporates results into its context before reasoning on the next step.

- **Response Handling**:
  - Utility functions can process and clean the agent's response (e.g., stripping `<think>...</think>` tags).
  - The agent's output can be printed or programmatically evaluated.

- **Testing**:
  - The agent is run asynchronously (`asyncio.run(main())`), performing end-to-end tasks such as retrieving projects, releases, and diffs, then summarizing risks.
  - The observed behavior demonstrates correct sequencing of tool calls, cross-server data retrieval, and synthesis into a final answer.

- **Prompt and Model Dependency**:
  - The agent’s performance depends on both the prompt quality and the underlying language model's ability to select and use tools effectively. Prompt engineering is sometimes necessary to guide the agent to the correct actions.

This example demonstrates practical implementation and testing of a ReAct-style agent loop, highlighting dynamic tool discovery and orchestration through a Python MCP client in complex, multi-system environments.

-----

-----

</details>

<details>
<summary>What are common security practices for MCP servers, specifically regarding authentication and authorization when moving from local development (stdio) to a deployed environment?</summary>

### Source [22]: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices

Query: What are common security practices for MCP servers, specifically regarding authentication and authorization when moving from local development (stdio) to a deployed environment?

Answer: The official MCP specification outlines key **security practices** for MCP servers, especially regarding authentication and authorization in production environments. 

- **Authentication**: MCP servers **MUST NOT use sessions for authentication**. Instead, secure, non-deterministic session IDs (such as UUIDs) generated with secure random number generators are required. Avoid predictable or sequential session identifiers to prevent guessing by attackers.
- **Session Management**: Session IDs should be rotated or expired to further reduce risk. MCP servers should bind session IDs to user-specific information (e.g., `<user_id>:<session_id>`) so that even if a session ID is guessed, impersonation is not possible.
- **Authorization**: All inbound requests **MUST be verified**. Authorization checks must be enforced systematically.
- **Transport Security**: When using stdio transport for local development, access can be limited to the MCP client. For HTTP transports, restrict access by requiring an authorization token and using IPC mechanisms like Unix domain sockets with restricted access.
- **Consent and Privilege Management**: For one-click local MCP server configuration, explicit user consent is mandatory before executing commands. Users must see the full command, warnings about potentially dangerous operations, and be allowed to cancel. Sandboxing and minimal privilege execution are recommended.
- **Mitigation Measures**: 
  - Warn users about commands accessing sensitive locations or containing dangerous patterns (e.g., `sudo`, `rm -rf`).
  - Default execution in sandboxed environments with restricted file system and network access.
  - Mechanisms for explicit privilege escalation by user consent.
  - Use platform-specific sandboxing tools (containers, chroot, etc.).
  - Prevent unauthorized usage from malicious processes by restricting transport access and requiring tokens or secure IPC.

These practices help transition MCP servers from local development to secure deployment, with strong emphasis on authentication, authorization, consent, and process isolation[1].

-----

-----

</details>

<details>
<summary>What are best practices for implementing a Python MCP client that can switch between in-memory and stdio transports for development and testing?</summary>

### Source [25]: https://modelcontextprotocol.io/docs/develop/build-client

Query: What are best practices for implementing a Python MCP client that can switch between in-memory and stdio transports for development and testing?

Answer: The official MCP documentation provides best practices and code examples for implementing a Python MCP client that can flexibly switch between in-memory and stdio transports, crucial for development and testing scenarios.

- **Client Structure:** Use classes to encapsulate client logic, managing session objects and asynchronous resources using `AsyncExitStack`. This enables easy cleanup and flexible context management for different transports.
- **Transport Switching:** To connect over stdio (e.g., spawning a subprocess and communicating via its stdin/stdout), use `StdioServerParameters` and `stdio_client`:
    ```python
    server_params = StdioServerParameters(command="python", args=[server_script_path])
    stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
    self.stdio, self.write = stdio_transport
    self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))
    ```
    The design allows the transport to be swapped (for example, you could replace `stdio_client` with an in-memory transport for testing).
- **Error Handling:** Always wrap tool calls and connection logic in try-catch blocks, and provide meaningful error messages. Gracefully handle connection issues to improve reliability and testability.
- **Initialization:** After establishing the transport and session, explicitly call `initialize()` and confirm tool availability (e.g., via `list_tools()`).
- **Environment Management:** Use environment variables (e.g., via `dotenv`) to control configuration parameters such as server paths and transport types, allowing overrides for development vs. production.
- **Development and Testing:** By abstracting transport creation and using dependency injection (passing in the desired transport), the client can easily switch between stdio (for integration with real servers) and in-memory transports (for unit testing and mock scenarios).

This approach ensures flexibility and maintainability, making it straightforward to adapt the client for different environments without code duplication or complex branching logic[1].

-----

-----

-----

### Source [26]: https://composio.dev/blog/mcp-client-step-by-step-guide-to-building-from-scratch

Query: What are best practices for implementing a Python MCP client that can switch between in-memory and stdio transports for development and testing?

Answer: This step-by-step guide demonstrates building a terminal-based MCP client from scratch, with a focus on structure and modularity that supports switching transports for development and testing.

- **Workspace Organization:** Create a clear directory structure separating servers, clients, and workspace/results. This modular setup aids in managing different client and server implementations, including those with different transports.
- **Virtual Environment:** Use a Python virtual environment for dependency isolation, making it easier to manage packages and configurations for various development and test setups.
- **Client Invocation:** The client is designed to connect to any MCP server using a command-line invocation, e.g., `python <path-to-client> <path-to-server>`. This makes it easy to switch between local (stdio) and potentially in-memory or remote servers via command-line arguments or environment variables.
- **Result Verification:** The guide encourages testing interactions (such as file operations) and verifying results in a dedicated workspace directory. This supports both manual and automated testing, regardless of the underlying transport.
- **Extensibility:** The design makes it straightforward to integrate with hosted MCP servers or switch to different backend repositories, further supporting the ability to change transports as needed for development or production.

Although the guide does not explicitly show in-memory vs. stdio transport switching, its emphasis on modularity, clear separation of client/server logic, and command-line configurability provides a strong foundation for implementing such a feature[2].

-----

-----

-----

### Source [27]: https://modelcontextprotocol.info/docs/best-practices/

Query: What are best practices for implementing a Python MCP client that can switch between in-memory and stdio transports for development and testing?

Answer: The architectural best practices for MCP development emphasize configuration management and environment-specific overrides, which are directly relevant to implementing flexible transport layers in a client.

- **Configuration Management:** Externalize all configuration, such as the choice of transport (in-memory vs. stdio), using environment variables or configuration files (`.env`, YAML, etc.). This enables seamless switching of client behavior without code changes.
- **Validation:** Use robust configuration validation (with libraries like `pydantic`) to ensure that all parameters, including those affecting transport, are set correctly for each environment.
- **Environment Overrides:** Provide different configuration files or environment variable sets for development, testing, and production. For example, a development config could specify in-memory transport, while production uses stdio.
- **Security and Consistency:** Consistent configuration handling reduces the risk of accidental misconfiguration and ensures that the client can be reliably tested under different scenarios.

These practices allow for clean separation between code and environment, making it trivial to switch transports by changing configuration rather than modifying code[3].

-----

-----

</details>

<details>
<summary>How can Pydantic settings be effectively used in a FastMCP server to manage configuration for different environments, such as development and production?</summary>

### Source [28]: https://gofastmcp.com/servers/server

Query: How can Pydantic settings be effectively used in a FastMCP server to manage configuration for different environments, such as development and production?

Answer: FastMCP server configuration can be managed using a combination of initialization arguments, global settings, and transport-specific settings. FastMCP supports configuration for different environments via **global settings** that are set using environment variables (prefixed with `FASTMCP_`) or through a `.env` file. This allows the separation of configuration logic for development, production, or other environments without changing code.

Key settings include:
- **`log_level`** (`FASTMCP_LOG_LEVEL`): Controls logging verbosity. Set to `"DEBUG"` for development or `"INFO"`/`"ERROR"` for production.
- **`mask_error_details`** (`FASTMCP_MASK_ERROR_DETAILS`): Hides error details from clients, typically enabled in production for security.
- **`resource_prefix_format`** (`FASTMCP_RESOURCE_PREFIX_FORMAT`): Adjusts resource naming conventions.
- **`strict_input_validation`** (`FASTMCP_STRICT_INPUT_VALIDATION`): Controls validation strictness, useful for enforcing stricter input validation in production.
- **`include_fastmcp_meta`** (`FASTMCP_INCLUDE_FASTMCP_META`): Toggles inclusion of FastMCP metadata.
- **`env_file`** (`FASTMCP_ENV_FILE`): Specifies the path to the environment file, allowing distinct `.env` files for development and production.

This approach leverages Pydantic settings under the hood, meaning changes to environment variables or `.env` files are automatically reflected in FastMCP’s configuration. For example, you can have `.env.production` and `.env.development` files, selecting which to use with `FASTMCP_ENV_FILE`. This pattern supports best practices for environment-specific configuration management, keeping secrets and operational settings outside the codebase[1].

-----

-----

-----

### Source [29]: https://ai.pydantic.dev/mcp/client/

Query: How can Pydantic settings be effectively used in a FastMCP server to manage configuration for different environments, such as development and production?

Answer: Pydantic AI provides a mechanism to load MCP servers from a JSON configuration file using `load_mcp_servers()`. This allows you to define different server configurations externally and switch between them for different environments (e.g., development vs. production) without modifying application code.

Configuration is specified in a JSON file under the `"mcpServers"` key, with each server definition containing unique parameters such as `command`, `args`, or `url`. For example:
```json
{
  "mcpServers": {
    "dev-server": {
      "url": "http://localhost:8000/mcp"
    },
    "prod-server": {
      "url": "https://api.example.com/mcp"
    }
  }
}
```
You can then load and use these settings in your application:
```python
from pydantic_ai.mcp import load_mcp_servers
servers = load_mcp_servers('mcp_config.json')
```
This method enables the separation of configuration from code and supports environment-specific deployment patterns by simply switching configuration files. It aligns with the principle of using external, version-controlled configuration for managing different environments[2].

-----

-----

-----

### Source [31]: https://github.com/modelcontextprotocol/python-sdk/pull/1244

Query: How can Pydantic settings be effectively used in a FastMCP server to manage configuration for different environments, such as development and production?

Answer: This update to the FastMCP constructor ensures that only explicitly provided parameters are passed to the Pydantic Settings constructor, respecting Pydantic’s intended priority order for configuration sources. This means FastMCP will correctly prioritize settings from environment variables, `.env` files, and defaults as defined by Pydantic’s configuration system.

As a result, developers can confidently use environment variables or `.env` files to override configuration for different environments (development, production, etc.), knowing that only explicitly set values are passed and the correct precedence is maintained. This improves reliability and predictability in configuration management for MCP servers, especially when deploying across multiple environments[4].

-----

-----

</details>

<details>
<summary>What is the role of the MCP Inspector tool in the development and debugging workflow of a FastMCP server and client?</summary>

### Source [32]: https://www.firecrawl.dev/blog/fastmcp-tutorial-building-mcp-servers-python

Query: What is the role of the MCP Inspector tool in the development and debugging workflow of a FastMCP server and client?

Answer: The MCP Inspector serves as a built-in debugging interface that significantly simplifies the development and testing process for FastMCP servers. Developers can launch the Inspector by running `mcp dev document_reader.py`, which starts a web interface at `http://127.0.0.1:6274` for testing all server components.

The Inspector provides a comprehensive testing workflow that includes several key capabilities. First, developers establish server communication by clicking a "Connect" button. Once connected, they can test each tool with various input parameters to verify functionality. The Inspector also enables resource validation, allowing developers to verify resource access and test dynamic parameter handling. Additionally, it provides prompt preview functionality, letting developers preview prompt templates with different argument values to ensure they work as expected.

A particularly valuable feature is the ability to test error scenarios with invalid inputs, helping developers ensure their error handling is robust. This interactive approach makes it much easier to identify and fix issues during development compared to manual testing methods. The web-based interface provides immediate feedback on how the server responds to different requests, streamlining the debugging process and helping developers build more reliable MCP servers.

-----

-----

### Source [33]: https://modelcontextprotocol.io/docs/tools/inspector

Query: What is the role of the MCP Inspector tool in the development and debugging workflow of a FastMCP server and client?

Answer: The MCP Inspector is an interactive developer tool designed specifically for testing and debugging MCP servers. It runs directly through `npx` without requiring installation, making it easily accessible with commands like `npx @modelcontextprotocol/inspector <command>`.

The Inspector supports multiple ways to inspect servers, including servers from npm or PyPI packages, as well as locally developed servers or those downloaded as repositories. For npm/PyPI packages, developers use commands like `npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem /Users/username/Desktop`. For local servers, the typical command is `npx @modelcontextprotocol/inspector node path/to/server/index.js args...`.

The Inspector's interface provides several organized features through different tabs and panes. The **Server connection pane** allows selecting the transport for connecting to the server and supports customizing command-line arguments and environment for local servers. The **Resources tab** lists all available resources, shows resource metadata including MIME types and descriptions, allows resource content inspection, and supports subscription testing. The **Prompts tab** displays available prompt templates, shows prompt arguments and descriptions, enables prompt testing with custom arguments, and previews generated messages.

The **Tools tab** lists available tools, shows tool schemas and descriptions, enables tool testing with custom inputs, and displays tool execution results. Finally, the **Notifications pane** presents all logs recorded from the server and shows notifications received from the server, providing comprehensive visibility into server operations during development and debugging.

-----

-----

### Source [34]: https://github.com/jlowin/fastmcp

Query: What is the role of the MCP Inspector tool in the development and debugging workflow of a FastMCP server and client?

Answer: The FastMCP framework emphasizes efficient testing capabilities through its client implementation. The `fastmcp.Client` plays a crucial role in the development workflow by supporting various transports including Stdio, SSE, and critically, **In-Memory** transport. This in-memory testing capability is particularly significant for development and debugging workflows.

The client enables efficient in-memory testing of servers by connecting directly to a `FastMCP` server instance via the `FastMCPTransport`, eliminating the need for process management or network calls during tests. This approach significantly streamlines the testing process compared to traditional methods that require spinning up separate processes or network connections.

The testing pattern is straightforward: developers can create a FastMCP server instance and then connect to it directly using the Client in an async context. For example, by passing the server instance directly to the Client constructor (`async with Client(mcp) as client:`), developers can test their server's tools, resources, and prompts without the overhead of external processes.

Additionally, the Client supports connecting to multiple servers through a single unified client using the standard MCP configuration format, which is valuable for testing complex scenarios involving multiple server interactions. The client can interact with any MCP server programmatically, allowing developers to test tool calls, list available tools, access resources, and verify the entire MCP server functionality. This programmatic access makes it easy to integrate automated tests into development workflows, ensuring servers behave correctly before deployment.

-----

</details>

<details>
<summary>What are common patterns for parsing user commands versus agent-bound messages in a ReAct-style agent loop within an MCP client?</summary>

### Source [35]: https://neo4j.com/blog/developer/react-agent-langgraph-mcp/

Query: What are common patterns for parsing user commands versus agent-bound messages in a ReAct-style agent loop within an MCP client?

Answer: A ReAct agent built with LangGraph and MCP in an MCP client separates **user command parsing** from **agent-bound messages** by employing a conversational loop and context management.

- **User commands** are captured as raw text input from the command line and passed into the agent loop. The client recognizes exit commands such as `exit`, `quit`, or `q` to terminate the session. This pattern ensures that only genuine user queries proceed to the agent, while control commands are intercepted at the client level before agent processing.
- The agent uses a **pre-model hook** to preprocess messages before passing them to the model, enabling token counting and message trimming, which is essential for context management in long conversations.
- **Agent-bound messages** (such as tool invocation results or system messages) are appended to the conversation context and managed via an in-memory checkpoint (e.g., `InMemorySaver`). This preserves agent state and conversation structure across turns.
- The agent loop proceeds by: receiving user input, invoking tools as needed (via MCP or local mechanisms), appending results to the context, analyzing updated context, and repeating until a final response is ready. Only after the agent processes and synthesizes context—including both user queries and tool results—is a response returned to the user.
- The separation is thus primarily handled via input filtering (for user commands) and structured context management (for agent messages), with clear demarcation between user-originated input and agent/tool-generated context[1].

-----

-----

-----

### Source [36]: https://composio.dev/blog/mcp-client-step-by-step-guide-to-building-from-scratch

Query: What are common patterns for parsing user commands versus agent-bound messages in a ReAct-style agent loop within an MCP client?

Answer: In the Composio MCP client guide, **user command parsing** and **agent-bound message handling** follow distinct patterns:

- The agent enters a **chat loop** that waits for user input. User commands (queries) are accepted as text, which is sent to the agent for processing.
- The loop continuously processes input until the user types a control command (`quit`), which is intercepted by the client and terminates the session. This ensures that only non-control user input reaches the agent.
- **Agent-bound messages**—including tool responses and formatted outputs—are handled within the loop, formatted using a custom JSON encoder, and printed to the console for the user. The agent receives user queries, determines necessary tool invocations, and integrates the results into its response.
- The separation is enforced by the client’s main loop: it filters user input for control commands before forwarding to the agent, while agent-bound messages (tool results, responses) are formatted and output after agent processing.
- The use of **Server-Sent Events (SSE)** for the MCP connection allows real-time streaming of agent-bound messages, further distinguishing agent responses from raw user input and enabling asynchronous message handling[2].

-----

-----

-----

### Source [37]: https://becomingahacker.org/integrating-agentic-rag-with-mcp-servers-technical-implementation-guide-1aba8fd4e442

Query: What are common patterns for parsing user commands versus agent-bound messages in a ReAct-style agent loop within an MCP client?

Answer: This technical guide for integrating Agentic RAG with MCP servers describes message patterns as follows:

- **User command ingestion** is the first stage: the agent receives a natural language query or command from the user interface.
- The agent then performs **planning**—analyzing the user request and deciding which MCP-bound tools or servers to invoke. This is typically a step-by-step process (e.g., retrieve data, process results, compose final output).
- **Agent-bound messages** are generated through standardized MCP API calls (e.g., invoking methods like `searchDocuments` or `getRecord`). These messages encapsulate tool invocation requests and responses, formatted as JSON or structured RPC messages.
- The agent’s main loop distinguishes between user-originated queries and agent-originated tool action requests/responses. User queries are only parsed at the beginning of each loop, while agent-bound messages (tool results, intermediate calculations) are handled internally and appended to the agent’s prompt/context for subsequent reasoning.
- The clear separation is maintained by passing only user commands into the agent’s initial planning step and handling agent-bound tool and context messages via the MCP client’s standardized API and internal context management[3].

-----

-----

-----

### Source [38]: https://modelcontextprotocol.io/docs/develop/build-client

Query: What are common patterns for parsing user commands versus agent-bound messages in a ReAct-style agent loop within an MCP client?

Answer: The official MCP documentation for building a client outlines the message handling flow:

- The client accepts **user commands** as text input, which are sent to the agent via the MCP protocol.
- The client differentiates between user commands (queries) and control commands (such as session management or shutdown). Control commands are intercepted and handled by the client, not forwarded to the agent.
- The agent processes user messages and may generate **agent-bound messages** such as tool invocation requests, context updates, or server queries. These are managed by the MCP client and routed to the appropriate MCP servers using standardized communication (e.g., STDIO, HTTP, or SSE).
- Responses from MCP servers (tool results, data retrieval) are formatted and sent back to the agent, which may use them for further reasoning before generating a final response.
- The separation is achieved by explicit client-side message filtering (for user commands and control signals) and structured routing of agent-bound messages to and from MCP servers, in accordance with the MCP protocol specification[4].

-----

-----

</details>

<details>
<summary>What are the key security considerations and best practices when moving an MCP server from a local `stdio` development environment to a deployed production environment that might use a networked transport?</summary>

### Source [39]: https://www.truefoundry.com/blog/mcp-server-security-best-practices

Query: What are the key security considerations and best practices when moving an MCP server from a local `stdio` development environment to a deployed production environment that might use a networked transport?

Answer: When deploying an MCP server from a local `stdio` development environment to a production system using networked transport, the following key security considerations and best practices must be addressed:

- **Strong Authentication:** Use OAuth 2.0 or OIDC with enterprise identity providers (such as Okta, Azure AD, Auth0) to ensure robust authentication. Avoid static tokens in production since they are hard to rotate and audit. Prefer short-lived tokens and implement PKCE for added resilience against interception attacks. Integrate with federated identity providers for single sign-on (SSO) and centralized control.

- **Fine-Grained Authorization (RBAC):** Implement role-based access control to limit actions to authorized users only. Assign tool-level permissions to ensure only specific roles can trigger sensitive tasks, and always follow the principle of least privilege so no more access is granted than necessary.

- **Input Validation & Schema Enforcement:** Validate all incoming JSON-RPC requests against schemas to reject malformed or unrecognized inputs, thereby preventing prompt injection attacks. Sanitize data before execution, especially when tools perform database or file operations.

These practices ensure that MCP servers are protected against authentication and authorization risks, input manipulation, and privilege escalation when exposed to networked environments[1].

-----

-----

-----

### Source [40]: https://scalesec.com/blog/mcp-server-security-best-practices

Query: What are the key security considerations and best practices when moving an MCP server from a local `stdio` development environment to a deployed production environment that might use a networked transport?

Answer: When transitioning MCP servers to production and using networked transport, several critical security controls must be implemented:

- **Principle of Least Privilege:** Each AI agent should have granular permissions—dedicated, scoped credentials for each tool or integration. Avoid shared service accounts and use time-limited credentials. Advanced configurations leverage Zero Standing Privilege, where agents get just-in-time, short-lived access only for approved actions.

- **Input Validation and Sanitation:** Multi-layer validation is crucial. Use API gateways or reverse proxies to block malformed requests and injection patterns before they reach the MCP server. Implement sanitization services for inspecting AI-generated queries and file operations. Deploy behavioral monitoring and anomaly detection to flag unexpected activity.

- **Network Segmentation and Isolation:** Host MCP servers in dedicated network zones (subnets or VLANs), restrict firewall rules to only necessary systems and ports, and block unauthorized outbound connections. Regularly test segmentation controls through red team simulations.

- **Comprehensive Logging and Monitoring:** Record full-context logs (prompts, commands, results) and aggregate logs centrally. Use anomaly detection systems trained on normal AI agent behavior. Retain logs long enough for forensic investigations.

- **Regular Security Assessments:** Include AI-specific tests for prompt injection, privilege escalation, and supply chain manipulation. Simulate realistic attacks and validate that controls prevent unauthorized actions and capture sufficient audit data.

Security teams should start with a thorough inventory of existing deployments and privileges before applying these practices[2].

-----

-----

-----

### Source [41]: https://modelcontextprotocol.io/specification/draft/basic/security_best_practices

Query: What are the key security considerations and best practices when moving an MCP server from a local `stdio` development environment to a deployed production environment that might use a networked transport?

Answer: The MCP protocol specification outlines several security best practices essential for moving MCP servers to production, especially when using networked transport:

- **Session Management:** MCP servers must use secure, non-deterministic session IDs (e.g., UUIDs generated by secure random number generators). Predictable or sequential session IDs must be avoided. Rotating or expiring session IDs further reduces risk.

- **Authorization Verification:** Every inbound request must be verified for authorization. Sessions must not be used as authentication mechanisms, and session data should be bound to user-specific information (e.g., storing session IDs as `<user_id>:<session_id>`).

- **Consent and Command Execution:** If a client supports one-click local server configuration, explicit user consent must be obtained before executing commands. Display full command details, warn about dangerous operations, and require explicit approval.

- **Sandboxing and Privilege Restriction:** Execute server commands in sandboxed environments with minimal privileges. Restrict access to the file system, network, and system resources by default, with mechanisms for explicit privilege escalation only when necessary.

- **Transport Security:** When using HTTP transport, require authorization tokens. Use Unix domain sockets or IPC mechanisms with restricted access to limit exposure.

These practices protect MCP servers from session hijacking, event injection, unauthorized code execution, and privilege escalation, which are critical when transitioning to a networked production environment[3].

-----

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>MCP Python SDK</summary>

# MCP Python SDK

**Python implementation of the Model Context Protocol (MCP)**

[https://camo.githubusercontent.com/e6ba71e25e692956bce8d9b0b4e043d9b7171186941670af455088139928be55/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f6d63702e737667](https://pypi.org/project/mcp/)[https://camo.githubusercontent.com/98147347f1be2b00361083e2aac1a18781acb3109ca688b1cd1940980e9f1201/68747470733a2f2f696d672e736869656c64732e696f2f707970692f6c2f6d63702e737667](https://github.com/modelcontextprotocol/python-sdk/blob/main/LICENSE)[https://camo.githubusercontent.com/b33b4fb36a9335985026e9b5b20cf5b1e548b7fff9f215b25abd31c9eaaa04ff/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f6d63702e737667](https://www.python.org/downloads/)[https://camo.githubusercontent.com/4f3fd5d9d842ca7951267b8ff579068d91caf8e23c4a2cf6cd12fe7321228111/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f63732d707974686f6e2d2d73646b2d626c75652e737667](https://modelcontextprotocol.github.io/python-sdk/)[https://camo.githubusercontent.com/adb94bad0e5b3ec2d49ac1ac5a133395fe15daf7b7e93fd3200c3efbefbf50e5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f70726f746f636f6c2d6d6f64656c636f6e7465787470726f746f636f6c2e696f2d626c75652e737667](https://modelcontextprotocol.io/)[https://camo.githubusercontent.com/0e20327998ce56e7a24c9b61227bb10976c5c3b6188551c2bd37e357ad67e7da/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f737065632d737065632e6d6f64656c636f6e7465787470726f746f636f6c2e696f2d626c75652e737667](https://modelcontextprotocol.io/specification/latest)

## Table of Contents

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk#mcp-python-sdk)
  - [Overview](https://github.com/modelcontextprotocol/python-sdk#overview)
  - [Installation](https://github.com/modelcontextprotocol/python-sdk#installation)
    - [Adding MCP to your python project](https://github.com/modelcontextprotocol/python-sdk#adding-mcp-to-your-python-project)
    - [Running the standalone MCP development tools](https://github.com/modelcontextprotocol/python-sdk#running-the-standalone-mcp-development-tools)
  - [Quickstart](https://github.com/modelcontextprotocol/python-sdk#quickstart)
  - [What is MCP?](https://github.com/modelcontextprotocol/python-sdk#what-is-mcp)
  - [Core Concepts](https://github.com/modelcontextprotocol/python-sdk#core-concepts)
    - [Server](https://github.com/modelcontextprotocol/python-sdk#server)
    - [Resources](https://github.com/modelcontextprotocol/python-sdk#resources)
    - [Tools](https://github.com/modelcontextprotocol/python-sdk#tools)
      - [Structured Output](https://github.com/modelcontextprotocol/python-sdk#structured-output)
    - [Prompts](https://github.com/modelcontextprotocol/python-sdk#prompts)
    - [Images](https://github.com/modelcontextprotocol/python-sdk#images)
    - [Context](https://github.com/modelcontextprotocol/python-sdk#context)
      - [Getting Context in Functions](https://github.com/modelcontextprotocol/python-sdk#getting-context-in-functions)
      - [Context Properties and Methods](https://github.com/modelcontextprotocol/python-sdk#context-properties-and-methods)
    - [Completions](https://github.com/modelcontextprotocol/python-sdk#completions)
    - [Elicitation](https://github.com/modelcontextprotocol/python-sdk#elicitation)
    - [Sampling](https://github.com/modelcontextprotocol/python-sdk#sampling)
    - [Logging and Notifications](https://github.com/modelcontextprotocol/python-sdk#logging-and-notifications)
    - [Authentication](https://github.com/modelcontextprotocol/python-sdk#authentication)
    - [FastMCP Properties](https://github.com/modelcontextprotocol/python-sdk#fastmcp-properties)
    - [Session Properties and Methods](https://github.com/modelcontextprotocol/python-sdk#session-properties-and-methods)
    - [Request Context Properties](https://github.com/modelcontextprotocol/python-sdk#request-context-properties)
  - [Running Your Server](https://github.com/modelcontextprotocol/python-sdk#running-your-server)
    - [Development Mode](https://github.com/modelcontextprotocol/python-sdk#development-mode)
    - [Claude Desktop Integration](https://github.com/modelcontextprotocol/python-sdk#claude-desktop-integration)
    - [Direct Execution](https://github.com/modelcontextprotocol/python-sdk#direct-execution)
    - [Streamable HTTP Transport](https://github.com/modelcontextprotocol/python-sdk#streamable-http-transport)
      - [CORS Configuration for Browser-Based Clients](https://github.com/modelcontextprotocol/python-sdk#cors-configuration-for-browser-based-clients)
    - [Mounting to an Existing ASGI Server](https://github.com/modelcontextprotocol/python-sdk#mounting-to-an-existing-asgi-server)
      - [StreamableHTTP servers](https://github.com/modelcontextprotocol/python-sdk#streamablehttp-servers)
        - [Basic mounting](https://github.com/modelcontextprotocol/python-sdk#basic-mounting)
        - [Host-based routing](https://github.com/modelcontextprotocol/python-sdk#host-based-routing)
        - [Multiple servers with path configuration](https://github.com/modelcontextprotocol/python-sdk#multiple-servers-with-path-configuration)
        - [Path configuration at initialization](https://github.com/modelcontextprotocol/python-sdk#path-configuration-at-initialization)
      - [SSE servers](https://github.com/modelcontextprotocol/python-sdk#sse-servers)
  - [Advanced Usage](https://github.com/modelcontextprotocol/python-sdk#advanced-usage)
    - [Low-Level Server](https://github.com/modelcontextprotocol/python-sdk#low-level-server)
      - [Structured Output Support](https://github.com/modelcontextprotocol/python-sdk#structured-output-support)
    - [Pagination (Advanced)](https://github.com/modelcontextprotocol/python-sdk#pagination-advanced)
    - [Writing MCP Clients](https://github.com/modelcontextprotocol/python-sdk#writing-mcp-clients)
    - [Client Display Utilities](https://github.com/modelcontextprotocol/python-sdk#client-display-utilities)
    - [OAuth Authentication for Clients](https://github.com/modelcontextprotocol/python-sdk#oauth-authentication-for-clients)
    - [Parsing Tool Results](https://github.com/modelcontextprotocol/python-sdk#parsing-tool-results)
    - [MCP Primitives](https://github.com/modelcontextprotocol/python-sdk#mcp-primitives)
    - [Server Capabilities](https://github.com/modelcontextprotocol/python-sdk#server-capabilities)
  - [Documentation](https://github.com/modelcontextprotocol/python-sdk#documentation)
  - [Contributing](https://github.com/modelcontextprotocol/python-sdk#contributing)
  - [License](https://github.com/modelcontextprotocol/python-sdk#license)

## Overview

The Model Context Protocol allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction. This Python SDK implements the full MCP specification, making it easy to:

- Build MCP clients that can connect to any MCP server
- Create MCP servers that expose resources, prompts and tools
- Use standard transports like stdio, SSE, and Streamable HTTP
- Handle all MCP protocol messages and lifecycle events

## Installation

### Adding MCP to your python project

We recommend using [uv](https://docs.astral.sh/uv/) to manage your Python projects.

If you haven't created a uv-managed project yet, create one:

```
uv init mcp-server-demo
cd mcp-server-demo
```

Then add MCP to your project dependencies:

```
uv add "mcp[cli]"
```

Alternatively, for projects using pip for dependencies:

```
pip install "mcp[cli]"
```

### Running the standalone MCP development tools

To run the mcp command with uv:

```
uv run mcp
```

## Quickstart

Let's create a simple MCP server that exposes a calculator tool and some data:

```
"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."
```

_Full example: [examples/snippets/servers/fastmcp\_quickstart.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/fastmcp_quickstart.py)_

You can install this server in [Claude Desktop](https://claude.ai/download) and interact with it right away by running:

```
uv run mcp install server.py
```

Alternatively, you can test it with the MCP Inspector:

```
uv run mcp dev server.py
```

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) lets you build servers that expose data and functionality to LLM applications in a secure, standardized way. Think of it like a web API, but specifically designed for LLM interactions. MCP servers can:

- Expose data through **Resources** (think of these sort of like GET endpoints; they are used to load information into the LLM's context)
- Provide functionality through **Tools** (sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
- Define interaction patterns through **Prompts** (reusable templates for LLM interactions)
- And more!

## Core Concepts

### Server

The FastMCP server is your core interface to the MCP protocol. It handles connection management, protocol compliance, and message routing:

```
"""Example showing lifespan support for startup/shutdown with strong typing."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

# Mock database class for example
class Database:
    """Mock database class for example."""

    @classmethod
    async def connect(cls) -> "Database":
        """Connect to database."""
        return cls()

    async def disconnect(self) -> None:
        """Disconnect from database."""
        pass

    def query(self) -> str:
        """Execute a query."""
        return "Query result"

@dataclass
class AppContext:
    """Application context with typed dependencies."""

    db: Database

@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""
    # Initialize on startup
    db = await Database.connect()
    try:
        yield AppContext(db=db)
    finally:
        # Cleanup on shutdown
        await db.disconnect()

# Pass lifespan to server
mcp = FastMCP("My App", lifespan=app_lifespan)

# Access type-safe lifespan context in tools
@mcp.tool()
def query_db(ctx: Context[ServerSession, AppContext]) -> str:
    """Tool that uses initialized resources."""
    db = ctx.request_context.lifespan_context.db
    return db.query()
```

_Full example: [examples/snippets/servers/lifespan\_example.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lifespan_example.py)_

### Resources

Resources are how you expose data to LLMs. They're similar to GET endpoints in a REST API - they provide data but shouldn't perform significant computation or have side effects:

```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Resource Example")

@mcp.resource("file://documents/{name}")
def read_document(name: str) -> str:
    """Read a document by name."""
    # This would normally read from disk
    return f"Content of {name}"

@mcp.resource("config://settings")
def get_settings() -> str:
    """Get application settings."""
    return """{
  "theme": "dark",
  "language": "en",
  "debug": false
}"""
```

_Full example: [examples/snippets/servers/basic\_resource.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/basic_resource.py)_

### Tools

Tools let LLMs take actions through your server. Unlike resources, tools are expected to perform computation and have side effects:

```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Tool Example")

@mcp.tool()
def sum(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def get_weather(city: str, unit: str = "celsius") -> str:
    """Get weather for a city."""
    # This would normally call a weather API
    return f"Weather in {city}: 22degrees{unit[0].upper()}"
```

_Full example: [examples/snippets/servers/basic\_tool.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/basic_tool.py)_

Tools can optionally receive a Context object by including a parameter with the `Context` type annotation. This context is automatically injected by the FastMCP framework and provides access to MCP capabilities:

```
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

mcp = FastMCP(name="Progress Example")

@mcp.tool()
async def long_running_task(task_name: str, ctx: Context[ServerSession, None], steps: int = 5) -> str:
    """Execute a task with progress updates."""
    await ctx.info(f"Starting: {task_name}")

    for i in range(steps):
        progress = (i + 1) / steps
        await ctx.report_progress(
            progress=progress,
            total=1.0,
            message=f"Step {i + 1}/{steps}",
        )
        await ctx.debug(f"Completed step {i + 1}")

    return f"Task '{task_name}' completed"
```

_Full example: [examples/snippets/servers/tool\_progress.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/tool_progress.py)_

#### Structured Output

Tools will return structured results by default, if their return type
annotation is compatible. Otherwise, they will return unstructured results.

Structured output supports these return types:

- Pydantic models (BaseModel subclasses)
- TypedDicts
- Dataclasses and other classes with type hints
- `dict[str, T]` (where T is any JSON-serializable type)
- Primitive types (str, int, float, bool, bytes, None) - wrapped in `{"result": value}`
- Generic types (list, tuple, Union, Optional, etc.) - wrapped in `{"result": value}`

Classes without type hints cannot be serialized for structured output. Only
classes with properly annotated attributes will be converted to Pydantic models
for schema generation and validation.

Structured results are automatically validated against the output schema
generated from the annotation. This ensures the tool returns well-typed,
validated data that clients can easily process.

**Note:** For backward compatibility, unstructured results are also
returned. Unstructured results are provided for backward compatibility
with previous versions of the MCP specification, and are quirks-compatible
with previous versions of FastMCP in the current version of the SDK.

**Note:** In cases where a tool function's return type annotation
causes the tool to be classified as structured _and this is undesirable_,
the classification can be suppressed by passing `structured_output=False`
to the `@tool` decorator.

##### Advanced: Direct CallToolResult

For full control over tool responses including the `_meta` field (for passing data to client applications without exposing it to the model), you can return `CallToolResult` directly:

```
"""Example showing direct CallToolResult return for advanced control."""

from typing import Annotated

from pydantic import BaseModel

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, TextContent

mcp = FastMCP("CallToolResult Example")

class ValidationModel(BaseModel):
    """Model for validating structured output."""

    status: str
    data: dict[str, int]

@mcp.tool()
def advanced_tool() -> CallToolResult:
    """Return CallToolResult directly for full control including _meta field."""
    return CallToolResult(
        content=[TextContent(type="text", text="Response visible to the model")],
        _meta={"hidden": "data for client applications only"},
    )

@mcp.tool()
def validated_tool() -> Annotated[CallToolResult, ValidationModel]:
    """Return CallToolResult with structured output validation."""
    return CallToolResult(
        content=[TextContent(type="text", text="Validated response")],
        structuredContent={"status": "success", "data": {"result": 42}},
        _meta={"internal": "metadata"},
    )

@mcp.tool()
def empty_result_tool() -> CallToolResult:
    """For empty results, return CallToolResult with empty content."""
    return CallToolResult(content=[])
```

_Full example: [examples/snippets/servers/direct\_call\_tool\_result.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/direct_call_tool_result.py)_

**Important:** `CallToolResult` must always be returned (no `Optional` or `Union`). For empty results, use `CallToolResult(content=[])`. For optional simple types, use `str | None` without `CallToolResult`.

```
"""Example showing structured output with tools."""

from typing import TypedDict

from pydantic import BaseModel, Field

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Structured Output Example")

# Using Pydantic models for rich structured data
class WeatherData(BaseModel):
    """Weather information structure."""

    temperature: float = Field(description="Temperature in Celsius")
    humidity: float = Field(description="Humidity percentage")
    condition: str
    wind_speed: float

@mcp.tool()
def get_weather(city: str) -> WeatherData:
    """Get weather for a city - returns structured data."""
    # Simulated weather data
    return WeatherData(
        temperature=22.5,
        humidity=45.0,
        condition="sunny",
        wind_speed=5.2,
    )

# Using TypedDict for simpler structures
class LocationInfo(TypedDict):
    latitude: float
    longitude: float
    name: str

@mcp.tool()
def get_location(address: str) -> LocationInfo:
    """Get location coordinates"""
    return LocationInfo(latitude=51.5074, longitude=-0.1278, name="London, UK")

# Using dict[str, Any] for flexible schemas
@mcp.tool()
def get_statistics(data_type: str) -> dict[str, float]:
    """Get various statistics"""
    return {"mean": 42.5, "median": 40.0, "std_dev": 5.2}

# Ordinary classes with type hints work for structured output
class UserProfile:
    name: str
    age: int
    email: str | None = None

    def __init__(self, name: str, age: int, email: str | None = None):
        self.name = name
        self.age = age
        self.email = email

@mcp.tool()
def get_user(user_id: str) -> UserProfile:
    """Get user profile - returns structured data"""
    return UserProfile(name="Alice", age=30, email="alice@example.com")

# Classes WITHOUT type hints cannot be used for structured output
class UntypedConfig:
    def __init__(self, setting1, setting2):  # type: ignore[reportMissingParameterType]
        self.setting1 = setting1
        self.setting2 = setting2

@mcp.tool()
def get_config() -> UntypedConfig:
    """This returns unstructured output - no schema generated"""
    return UntypedConfig("value1", "value2")

# Lists and other types are wrapped automatically
@mcp.tool()
def list_cities() -> list[str]:
    """Get a list of cities"""
    return ["London", "Paris", "Tokyo"]
    # Returns: {"result": ["London", "Paris", "Tokyo"]}

@mcp.tool()
def get_temperature(city: str) -> float:
    """Get temperature as a simple float"""
    return 22.5
    # Returns: {"result": 22.5}
```

_Full example: [examples/snippets/servers/structured\_output.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/structured_output.py)_

### Prompts

Prompts are reusable templates that help LLMs interact with your server effectively:

```
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP(name="Prompt Example")

@mcp.prompt(title="Code Review")
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"

@mcp.prompt(title="Debug Assistant")
def debug_error(error: str) -> list[base.Message]:
    return [\
        base.UserMessage("I'm seeing this error:"),\
        base.UserMessage(error),\
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),\
    ]
```

_Full example: [examples/snippets/servers/basic\_prompt.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/basic_prompt.py)_

### Icons

MCP servers can provide icons for UI display. Icons can be added to the server implementation, tools, resources, and prompts:

```
from mcp.server.fastmcp import FastMCP, Icon

# Create an icon from a file path or URL
icon = Icon(
    src="icon.png",
    mimeType="image/png",
    sizes="64x64"
)

# Add icons to server
mcp = FastMCP(
    "My Server",
    website_url="https://example.com",
    icons=[icon]
)

# Add icons to tools, resources, and prompts
@mcp.tool(icons=[icon])
def my_tool():
    """Tool with an icon."""
    return "result"

@mcp.resource("demo://resource", icons=[icon])
def my_resource():
    """Resource with an icon."""
    return "content"
```

_Full example: [examples/fastmcp/icons\_demo.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/fastmcp/icons_demo.py)_

### Images

FastMCP provides an `Image` class that automatically handles image data:

```
"""Example showing image handling with FastMCP."""

from PIL import Image as PILImage

from mcp.server.fastmcp import FastMCP, Image

mcp = FastMCP("Image Example")

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")
```

_Full example: [examples/snippets/servers/images.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/images.py)_

### Context

The Context object is automatically injected into tool and resource functions that request it via type hints. It provides access to MCP capabilities like logging, progress reporting, resource reading, user interaction, and request metadata.

#### Getting Context in Functions

To use context in a tool or resource function, add a parameter with the `Context` type annotation:

```
from mcp.server.fastmcp import Context, FastMCP

mcp = FastMCP(name="Context Example")

@mcp.tool()
async def my_tool(x: int, ctx: Context) -> str:
    """Tool that uses context capabilities."""
    # The context parameter can have any name as long as it's type-annotated
    return await process_with_context(x, ctx)
```

#### Context Properties and Methods

The Context object provides the following capabilities:

- `ctx.request_id` \- Unique ID for the current request
- `ctx.client_id` \- Client ID if available
- `ctx.fastmcp` \- Access to the FastMCP server instance (see [FastMCP Properties](https://github.com/modelcontextprotocol/python-sdk#fastmcp-properties))
- `ctx.session` \- Access to the underlying session for advanced communication (see [Session Properties and Methods](https://github.com/modelcontextprotocol/python-sdk#session-properties-and-methods))
- `ctx.request_context` \- Access to request-specific data and lifespan resources (see [Request Context Properties](https://github.com/modelcontextprotocol/python-sdk#request-context-properties))
- `await ctx.debug(message)` \- Send debug log message
- `await ctx.info(message)` \- Send info log message
- `await ctx.warning(message)` \- Send warning log message
- `await ctx.error(message)` \- Send error log message
- `await ctx.log(level, message, logger_name=None)` \- Send log with custom level
- `await ctx.report_progress(progress, total=None, message=None)` \- Report operation progress
- `await ctx.read_resource(uri)` \- Read a resource by URI
- `await ctx.elicit(message, schema)` \- Request additional information from user with validation

```
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

mcp = FastMCP(name="Progress Example")

@mcp.tool()
async def long_running_task(task_name: str, ctx: Context[ServerSession, None], steps: int = 5) -> str:
    """Execute a task with progress updates."""
    await ctx.info(f"Starting: {task_name}")

    for i in range(steps):
        progress = (i + 1) / steps
        await ctx.report_progress(
            progress=progress,
            total=1.0,
            message=f"Step {i + 1}/{steps}",
        )
        await ctx.debug(f"Completed step {i + 1}")

    return f"Task '{task_name}' completed"
```

_Full example: [examples/snippets/servers/tool\_progress.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/tool_progress.py)_

### Completions

MCP supports providing completion suggestions for prompt arguments and resource template parameters. With the context parameter, servers can provide completions based on previously resolved values:

Client usage:

```
"""
cd to the `examples/snippets` directory and run:
    uv run completion-client
"""

import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import PromptReference, ResourceTemplateReference

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",  # Using uv to run the server
    args=["run", "server", "completion", "stdio"],  # Server with completion support
    env={"UV_INDEX": os.environ.get("UV_INDEX", "")},
)

async def run():
    """Run the completion client example."""
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available resource templates
            templates = await session.list_resource_templates()
            print("Available resource templates:")
            for template in templates.resourceTemplates:
                print(f"  - {template.uriTemplate}")

            # List available prompts
            prompts = await session.list_prompts()
            print("\nAvailable prompts:")
            for prompt in prompts.prompts:
                print(f"  - {prompt.name}")

            # Complete resource template arguments
            if templates.resourceTemplates:
                template = templates.resourceTemplates[0]
                print(f"\nCompleting arguments for resource template: {template.uriTemplate}")

                # Complete without context
                result = await session.complete(
                    ref=ResourceTemplateReference(type="ref/resource", uri=template.uriTemplate),
                    argument={"name": "owner", "value": "model"},
                )
                print(f"Completions for 'owner' starting with 'model': {result.completion.values}")

                # Complete with context - repo suggestions based on owner
                result = await session.complete(
                    ref=ResourceTemplateReference(type="ref/resource", uri=template.uriTemplate),
                    argument={"name": "repo", "value": ""},
                    context_arguments={"owner": "modelcontextprotocol"},
                )
                print(f"Completions for 'repo' with owner='modelcontextprotocol': {result.completion.values}")

            # Complete prompt arguments
            if prompts.prompts:
                prompt_name = prompts.prompts[0].name
                print(f"\nCompleting arguments for prompt: {prompt_name}")

                result = await session.complete(
                    ref=PromptReference(type="ref/prompt", name=prompt_name),
                    argument={"name": "style", "value": ""},
                )
                print(f"Completions for 'style' argument: {result.completion.values}")

def main():
    """Entry point for the completion client."""
    asyncio.run(run())

if __name__ == "__main__":
    main()
```

_Full example: [examples/snippets/clients/completion\_client.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/completion_client.py)_

### Elicitation

Request additional information from users. This example shows an Elicitation during a Tool Call:

```
from pydantic import BaseModel, Field

from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

mcp = FastMCP(name="Elicitation Example")

class BookingPreferences(BaseModel):
    """Schema for collecting user preferences."""

    checkAlternative: bool = Field(description="Would you like to check another date?")
    alternativeDate: str = Field(
        default="2024-12-26",
        description="Alternative date (YYYY-MM-DD)",
    )

@mcp.tool()
async def book_table(date: str, time: str, party_size: int, ctx: Context[ServerSession, None]) -> str:
    """Book a table with date availability check."""
    # Check if date is available
    if date == "2024-12-25":
        # Date unavailable - ask user for alternative
        result = await ctx.elicit(
            message=(f"No tables available for {party_size} on {date}. Would you like to try another date?"),
            schema=BookingPreferences,
        )

        if result.action == "accept" and result.data:
            if result.data.checkAlternative:
                return f"[SUCCESS] Booked for {result.data.alternativeDate}"
            return "[CANCELLED] No booking made"
        return "[CANCELLED] Booking cancelled"

    # Date available
    return f"[SUCCESS] Booked for {date} at {time}"
```

_Full example: [examples/snippets/servers/elicitation.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/elicitation.py)_

Elicitation schemas support default values for all field types. Default values are automatically included in the JSON schema sent to clients, allowing them to pre-populate forms.

The `elicit()` method returns an `ElicitationResult` with:

- `action`: "accept", "decline", or "cancel"
- `data`: The validated response (only when accepted)
- `validation_error`: Any validation error message

### Sampling

Tools can interact with LLMs through sampling (generating text):

```
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

mcp = FastMCP(name="Sampling Example")

@mcp.tool()
async def generate_poem(topic: str, ctx: Context[ServerSession, None]) -> str:
    """Generate a poem using LLM sampling."""
    prompt = f"Write a short poem about {topic}"

    result = await ctx.session.create_message(
        messages=[\
            SamplingMessage(\
                role="user",\
                content=TextContent(type="text", text=prompt),\
            )\
        ],
        max_tokens=100,
    )

    if result.content.type == "text":
        return result.content.text
    return str(result.content)
```

_Full example: [examples/snippets/servers/sampling.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/sampling.py)_

### Logging and Notifications

Tools can send logs and notifications through the context:

```
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

mcp = FastMCP(name="Notifications Example")

@mcp.tool()
async def process_data(data: str, ctx: Context[ServerSession, None]) -> str:
    """Process data with logging."""
    # Different log levels
    await ctx.debug(f"Debug: Processing '{data}'")
    await ctx.info("Info: Starting processing")
    await ctx.warning("Warning: This is experimental")
    await ctx.error("Error: (This is just a demo)")

    # Notify about resource changes
    await ctx.session.send_resource_list_changed()

    return f"Processed: {data}"
```

_Full example: [examples/snippets/servers/notifications.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/notifications.py)_

### Authentication

Authentication can be used by servers that want to expose tools accessing protected resources.

`mcp.server.auth` implements OAuth 2.1 resource server functionality, where MCP servers act as Resource Servers (RS) that validate tokens issued by separate Authorization Servers (AS). This follows the [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) and implements RFC 9728 (Protected Resource Metadata) for AS discovery.

MCP servers can use authentication by providing an implementation of the `TokenVerifier` protocol:

```
"""
Run from the repository root:
    uv run examples/snippets/servers/oauth_server.py
"""

from pydantic import AnyHttpUrl

from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings
from mcp.server.fastmcp import FastMCP

class SimpleTokenVerifier(TokenVerifier):
    """Simple token verifier for demonstration."""

    async def verify_token(self, token: str) -> AccessToken | None:
        pass  # This is where you would implement actual token validation

# Create FastMCP instance as a Resource Server
mcp = FastMCP(
    "Weather Service",
    # Token verifier for authentication
    token_verifier=SimpleTokenVerifier(),
    # Auth settings for RFC 9728 Protected Resource Metadata
    auth=AuthSettings(
        issuer_url=AnyHttpUrl("https://auth.example.com"),  # Authorization Server URL
        resource_server_url=AnyHttpUrl("http://localhost:3001"),  # This server's URL
        required_scopes=["user"],
    ),
)

@mcp.tool()
async def get_weather(city: str = "London") -> dict[str, str]:
    """Get weather data for a city"""
    return {
        "city": city,
        "temperature": "22",
        "condition": "Partly cloudy",
        "humidity": "65%",
    }

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

_Full example: [examples/snippets/servers/oauth\_server.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/oauth_server.py)_

For a complete example with separate Authorization Server and Resource Server implementations, see [`examples/servers/simple-auth/`](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-auth).

**Architecture:**

- **Authorization Server (AS)**: Handles OAuth flows, user authentication, and token issuance
- **Resource Server (RS)**: Your MCP server that validates tokens and serves protected resources
- **Client**: Discovers AS through RFC 9728, obtains tokens, and uses them with the MCP server

See [TokenVerifier](https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/auth/provider.py) for more details on implementing token validation.

### FastMCP Properties

The FastMCP server instance accessible via `ctx.fastmcp` provides access to server configuration and metadata:

- `ctx.fastmcp.name` \- The server's name as defined during initialization
- `ctx.fastmcp.instructions` \- Server instructions/description provided to clients
- `ctx.fastmcp.website_url` \- Optional website URL for the server
- `ctx.fastmcp.icons` \- Optional list of icons for UI display
- `ctx.fastmcp.settings` \- Complete server configuration object containing:
  - `debug` \- Debug mode flag
  - `log_level` \- Current logging level
  - `host` and `port` \- Server network configuration
  - `mount_path`, `sse_path`, `streamable_http_path` \- Transport paths
  - `stateless_http` \- Whether the server operates in stateless mode
  - And other configuration options

```
@mcp.tool()
def server_info(ctx: Context) -> dict:
    """Get information about the current server."""
    return {
        "name": ctx.fastmcp.name,
        "instructions": ctx.fastmcp.instructions,
        "debug_mode": ctx.fastmcp.settings.debug,
        "log_level": ctx.fastmcp.settings.log_level,
        "host": ctx.fastmcp.settings.host,
        "port": ctx.fastmcp.settings.port,
    }
```

### Session Properties and Methods

The session object accessible via `ctx.session` provides advanced control over client communication:

- `ctx.session.client_params` \- Client initialization parameters and declared capabilities
- `await ctx.session.send_log_message(level, data, logger)` \- Send log messages with full control
- `await ctx.session.create_message(messages, max_tokens)` \- Request LLM sampling/completion
- `await ctx.session.send_progress_notification(token, progress, total, message)` \- Direct progress updates
- `await ctx.session.send_resource_updated(uri)` \- Notify clients that a specific resource changed
- `await ctx.session.send_resource_list_changed()` \- Notify clients that the resource list changed
- `await ctx.session.send_tool_list_changed()` \- Notify clients that the tool list changed
- `await ctx.session.send_prompt_list_changed()` \- Notify clients that the prompt list changed

```
@mcp.tool()
async def notify_data_update(resource_uri: str, ctx: Context) -> str:
    """Update data and notify clients of the change."""
    # Perform data update logic here

    # Notify clients that this specific resource changed
    await ctx.session.send_resource_updated(AnyUrl(resource_uri))

    # If this affects the overall resource list, notify about that too
    await ctx.session.send_resource_list_changed()

    return f"Updated {resource_uri} and notified clients"
```

### Request Context Properties

The request context accessible via `ctx.request_context` contains request-specific information and resources:

- `ctx.request_context.lifespan_context` \- Access to resources initialized during server startup
  - Database connections, configuration objects, shared services
  - Type-safe access to resources defined in your server's lifespan function
- `ctx.request_context.meta` \- Request metadata from the client including:
  - `progressToken` \- Token for progress notifications
  - Other client-provided metadata
- `ctx.request_context.request` \- The original MCP request object for advanced processing
- `ctx.request_context.request_id` \- Unique identifier for this request

```
# Example with typed lifespan context
@dataclass
class AppContext:
    db: Database
    config: AppConfig

@mcp.tool()
def query_with_config(query: str, ctx: Context) -> str:
    """Execute a query using shared database and configuration."""
    # Access typed lifespan context
    app_ctx: AppContext = ctx.request_context.lifespan_context

    # Use shared resources
    connection = app_ctx.db
    settings = app_ctx.config

    # Execute query with configuration
    result = connection.execute(query, timeout=settings.query_timeout)
    return str(result)
```

_Full lifespan example: [examples/snippets/servers/lifespan\_example.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lifespan_example.py)_

## Running Your Server

### Development Mode

The fastest way to test and debug your server is with the MCP Inspector:

```
uv run mcp dev server.py

# Add dependencies
uv run mcp dev server.py --with pandas --with numpy

# Mount local code
uv run mcp dev server.py --with-editable .
```

### Claude Desktop Integration

Once your server is ready, install it in Claude Desktop:

```
uv run mcp install server.py

# Custom name
uv run mcp install server.py --name "My Analytics Server"

# Environment variables
uv run mcp install server.py -v API_KEY=abc123 -v DB_URL=postgres://...
uv run mcp install server.py -f .env
```

### Direct Execution

For advanced scenarios like custom deployments:

```
"""Example showing direct execution of an MCP server.

This is the simplest way to run an MCP server directly.
cd to the `examples/snippets` directory and run:
    uv run direct-execution-server
    or
    python servers/direct_execution.py
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")

@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

def main():
    """Entry point for the direct execution server."""
    mcp.run()

if __name__ == "__main__":
    main()
```

_Full example: [examples/snippets/servers/direct\_execution.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/direct_execution.py)_

Run it with:

```
python servers/direct_execution.py
# or
uv run mcp run servers/direct_execution.py
```

Note that `uv run mcp run` or `uv run mcp dev` only supports server using FastMCP and not the low-level server variant.

### Streamable HTTP Transport

> **Note**: Streamable HTTP transport is superseding SSE transport for production deployments.

```
"""
Run from the repository root:
    uv run examples/snippets/servers/streamable_config.py
"""

from mcp.server.fastmcp import FastMCP

# Stateful server (maintains session state)
mcp = FastMCP("StatefulServer")

# Other configuration options:
# Stateless server (no session persistence)
# mcp = FastMCP("StatelessServer", stateless_http=True)

# Stateless server (no session persistence, no sse stream with supported client)
# mcp = FastMCP("StatelessServer", stateless_http=True, json_response=True)

# Add a simple tool to demonstrate the server
@mcp.tool()
def greet(name: str = "World") -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

# Run server with streamable_http transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

_Full example: [examples/snippets/servers/streamable\_config.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_config.py)_

You can mount multiple FastMCP servers in a Starlette application:

```
"""
Run from the repository root:
    uvicorn examples.snippets.servers.streamable_starlette_mount:app --reload
"""

import contextlib

from starlette.applications import Starlette
from starlette.routing import Mount

from mcp.server.fastmcp import FastMCP

# Create the Echo server
echo_mcp = FastMCP(name="EchoServer", stateless_http=True)

@echo_mcp.tool()
def echo(message: str) -> str:
    """A simple echo tool"""
    return f"Echo: {message}"

# Create the Math server
math_mcp = FastMCP(name="MathServer", stateless_http=True)

@math_mcp.tool()
def add_two(n: int) -> int:
    """Tool to add two to the input"""
    return n + 2

# Create a combined lifespan to manage both session managers
@contextlib.asynccontextmanager
async def lifespan(app: Starlette):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(echo_mcp.session_manager.run())
        await stack.enter_async_context(math_mcp.session_manager.run())
        yield

# Create the Starlette app and mount the MCP servers
app = Starlette(
    routes=[\
        Mount("/echo", echo_mcp.streamable_http_app()),\
        Mount("/math", math_mcp.streamable_http_app()),\
    ],
    lifespan=lifespan,
)

# Note: Clients connect to http://localhost:8000/echo/mcp and http://localhost:8000/math/mcp
# To mount at the root of each path (e.g., /echo instead of /echo/mcp):
# echo_mcp.settings.streamable_http_path = "/"
# math_mcp.settings.streamable_http_path = "/"
```

_Full example: [examples/snippets/servers/streamable\_starlette\_mount.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_starlette_mount.py)_

For low level server with Streamable HTTP implementations, see:

- Stateful server: [`examples/servers/simple-streamablehttp/`](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-streamablehttp)
- Stateless server: [`examples/servers/simple-streamablehttp-stateless/`](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-streamablehttp-stateless)

The streamable HTTP transport supports:

- Stateful and stateless operation modes
- Resumability with event stores
- JSON or SSE response formats
- Better scalability for multi-node deployments

#### CORS Configuration for Browser-Based Clients

If you'd like your server to be accessible by browser-based MCP clients, you'll need to configure CORS headers. The `Mcp-Session-Id` header must be exposed for browser clients to access it:

```
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

# Create your Starlette app first
starlette_app = Starlette(routes=[...])

# Then wrap it with CORS middleware
starlette_app = CORSMiddleware(
    starlette_app,
    allow_origins=["*"],  # Configure appropriately for production
    allow_methods=["GET", "POST", "DELETE"],  # MCP streamable HTTP methods
    expose_headers=["Mcp-Session-Id"],
)
```

This configuration is necessary because:

- The MCP streamable HTTP transport uses the `Mcp-Session-Id` header for session management
- Browsers restrict access to response headers unless explicitly exposed via CORS
- Without this configuration, browser-based clients won't be able to read the session ID from initialization responses

### Mounting to an Existing ASGI Server

By default, SSE servers are mounted at `/sse` and Streamable HTTP servers are mounted at `/mcp`. You can customize these paths using the methods described below.

For more information on mounting applications in Starlette, see the [Starlette documentation](https://www.starlette.io/routing/#submounting-routes).

#### StreamableHTTP servers

You can mount the StreamableHTTP server to an existing ASGI server using the `streamable_http_app` method. This allows you to integrate the StreamableHTTP server with other ASGI applications.

##### Basic mounting

```
"""
Basic example showing how to mount StreamableHTTP server in Starlette.

Run from the repository root:
    uvicorn examples.snippets.servers.streamable_http_basic_mounting:app --reload
"""

from starlette.applications import Starlette
from starlette.routing import Mount

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("My App")

@mcp.tool()
def hello() -> str:
    """A simple hello tool"""
    return "Hello from MCP!"

# Mount the StreamableHTTP server to the existing ASGI server
app = Starlette(
    routes=[\
        Mount("/", app=mcp.streamable_http_app()),\
    ]
)
```

_Full example: [examples/snippets/servers/streamable\_http\_basic\_mounting.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_http_basic_mounting.py)_

##### Host-based routing

```
"""
Example showing how to mount StreamableHTTP server using Host-based routing.

Run from the repository root:
    uvicorn examples.snippets.servers.streamable_http_host_mounting:app --reload
"""

from starlette.applications import Starlette
from starlette.routing import Host

from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("MCP Host App")

@mcp.tool()
def domain_info() -> str:
    """Get domain-specific information"""
    return "This is served from mcp.acme.corp"

# Mount using Host-based routing
app = Starlette(
    routes=[\
        Host("mcp.acme.corp", app=mcp.streamable_http_app()),\
    ]
)
```

_Full example: [examples/snippets/servers/streamable\_http\_host\_mounting.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_http_host_mounting.py)_

##### Multiple servers with path configuration

```
"""
Example showing how to mount multiple StreamableHTTP servers with path configuration.

Run from the repository root:
    uvicorn examples.snippets.servers.streamable_http_multiple_servers:app --reload
"""

from starlette.applications import Starlette
from starlette.routing import Mount

from mcp.server.fastmcp import FastMCP

# Create multiple MCP servers
api_mcp = FastMCP("API Server")
chat_mcp = FastMCP("Chat Server")

@api_mcp.tool()
def api_status() -> str:
    """Get API status"""
    return "API is running"

@chat_mcp.tool()
def send_message(message: str) -> str:
    """Send a chat message"""
    return f"Message sent: {message}"

# Configure servers to mount at the root of each path
# This means endpoints will be at /api and /chat instead of /api/mcp and /chat/mcp
api_mcp.settings.streamable_http_path = "/"
chat_mcp.settings.streamable_http_path = "/"

# Mount the servers
app = Starlette(
    routes=[\
        Mount("/api", app=api_mcp.streamable_http_app()),\
        Mount("/chat", app=chat_mcp.streamable_http_app()),\
    ]
)
```

_Full example: [examples/snippets/servers/streamable\_http\_multiple\_servers.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_http_multiple_servers.py)_

##### Path configuration at initialization

```
"""
Example showing path configuration during FastMCP initialization.

Run from the repository root:
    uvicorn examples.snippets.servers.streamable_http_path_config:app --reload
"""

from starlette.applications import Starlette
from starlette.routing import Mount

from mcp.server.fastmcp import FastMCP

# Configure streamable_http_path during initialization
# This server will mount at the root of wherever it's mounted
mcp_at_root = FastMCP("My Server", streamable_http_path="/")

@mcp_at_root.tool()
def process_data(data: str) -> str:
    """Process some data"""
    return f"Processed: {data}"

# Mount at /process - endpoints will be at /process instead of /process/mcp
app = Starlette(
    routes=[\
        Mount("/process", app=mcp_at_root.streamable_http_app()),\
    ]
)
```

_Full example: [examples/snippets/servers/streamable\_http\_path\_config.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/streamable_http_path_config.py)_

#### SSE servers

> **Note**: SSE transport is being superseded by [Streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http).

You can mount the SSE server to an existing ASGI server using the `sse_app` method. This allows you to integrate the SSE server with other ASGI applications.

```
from starlette.applications import Starlette
from starlette.routing import Mount, Host
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")

# Mount the SSE server to the existing ASGI server
app = Starlette(
    routes=[\
        Mount('/', app=mcp.sse_app()),\
    ]
)

# or dynamically mount as host
app.router.routes.append(Host('mcp.acme.corp', app=mcp.sse_app()))
```

When mounting multiple MCP servers under different paths, you can configure the mount path in several ways:

```
from starlette.applications import Starlette
from starlette.routing import Mount
from mcp.server.fastmcp import FastMCP

# Create multiple MCP servers
github_mcp = FastMCP("GitHub API")
browser_mcp = FastMCP("Browser")
curl_mcp = FastMCP("Curl")
search_mcp = FastMCP("Search")

# Method 1: Configure mount paths via settings (recommended for persistent configuration)
github_mcp.settings.mount_path = "/github"
browser_mcp.settings.mount_path = "/browser"

# Method 2: Pass mount path directly to sse_app (preferred for ad-hoc mounting)
# This approach doesn't modify the server's settings permanently

# Create Starlette app with multiple mounted servers
app = Starlette(
    routes=[\
        # Using settings-based configuration\
        Mount("/github", app=github_mcp.sse_app()),\
        Mount("/browser", app=browser_mcp.sse_app()),\
        # Using direct mount path parameter\
        Mount("/curl", app=curl_mcp.sse_app("/curl")),\
        Mount("/search", app=search_mcp.sse_app("/search")),\
    ]
)

# Method 3: For direct execution, you can also pass the mount path to run()
if __name__ == "__main__":
    search_mcp.run(transport="sse", mount_path="/search")
```

For more information on mounting applications in Starlette, see the [Starlette documentation](https://www.starlette.io/routing/#submounting-routes).

## Advanced Usage

### Low-Level Server

For more control, you can use the low-level server implementation directly. This gives you full access to the protocol and allows you to customize every aspect of your server, including lifecycle management through the lifespan API:

```
"""
Run from the repository root:
    uv run examples/snippets/servers/lowlevel/lifespan.py
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

# Mock database class for example
class Database:
    """Mock database class for example."""

    @classmethod
    async def connect(cls) -> "Database":
        """Connect to database."""
        print("Database connected")
        return cls()

    async def disconnect(self) -> None:
        """Disconnect from database."""
        print("Database disconnected")

    async def query(self, query_str: str) -> list[dict[str, str]]:
        """Execute a query."""
        # Simulate database query
        return [{"id": "1", "name": "Example", "query": query_str}]

@asynccontextmanager
async def server_lifespan(_server: Server) -> AsyncIterator[dict[str, Any]]:
    """Manage server startup and shutdown lifecycle."""
    # Initialize resources on startup
    db = await Database.connect()
    try:
        yield {"db": db}
    finally:
        # Clean up on shutdown
        await db.disconnect()

# Pass lifespan to server
server = Server("example-server", lifespan=server_lifespan)

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools."""
    return [\
        types.Tool(\
            name="query_db",\
            description="Query the database",\
            inputSchema={\
                "type": "object",\
                "properties": {"query": {"type": "string", "description": "SQL query to execute"}},\
                "required": ["query"],\
            },\
        )\
    ]

@server.call_tool()
async def query_db(name: str, arguments: dict[str, Any]) -> list[types.TextContent]:
    """Handle database query tool call."""
    if name != "query_db":
        raise ValueError(f"Unknown tool: {name}")

    # Access lifespan context
    ctx = server.request_context
    db = ctx.lifespan_context["db"]

    # Execute query
    results = await db.query(arguments["query"])

    return [types.TextContent(type="text", text=f"Query results: {results}")]

async def run():
    """Run the server with lifespan management."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

_Full example: [examples/snippets/servers/lowlevel/lifespan.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/lifespan.py)_

The lifespan API provides:

- A way to initialize resources when the server starts and clean them up when it stops
- Access to initialized resources through the request context in handlers
- Type-safe context passing between lifespan and request handlers

```
"""
Run from the repository root:
uv run examples/snippets/servers/lowlevel/basic.py
"""

import asyncio

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

# Create a server instance
server = Server("example-server")

@server.list_prompts()
async def handle_list_prompts() -> list[types.Prompt]:
    """List available prompts."""
    return [\
        types.Prompt(\
            name="example-prompt",\
            description="An example prompt template",\
            arguments=[types.PromptArgument(name="arg1", description="Example argument", required=True)],\
        )\
    ]

@server.get_prompt()
async def handle_get_prompt(name: str, arguments: dict[str, str] | None) -> types.GetPromptResult:
    """Get a specific prompt by name."""
    if name != "example-prompt":
        raise ValueError(f"Unknown prompt: {name}")

    arg1_value = (arguments or {}).get("arg1", "default")

    return types.GetPromptResult(
        description="Example prompt",
        messages=[\
            types.PromptMessage(\
                role="user",\
                content=types.TextContent(type="text", text=f"Example prompt text with argument: {arg1_value}"),\
            )\
        ],
    )

async def run():
    """Run the basic low-level server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(run())
```

_Full example: [examples/snippets/servers/lowlevel/basic.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/basic.py)_

Caution: The `uv run mcp run` and `uv run mcp dev` tool doesn't support low-level server.

#### Structured Output Support

The low-level server supports structured output for tools, allowing you to return both human-readable content and machine-readable structured data. Tools can define an `outputSchema` to validate their structured output:

```
"""
Run from the repository root:
    uv run examples/snippets/servers/lowlevel/structured_output.py
"""

import asyncio
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

server = Server("example-server")

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    """List available tools with structured output schemas."""
    return [\
        types.Tool(\
            name="get_weather",\
            description="Get current weather for a city",\
            inputSchema={\
                "type": "object",\
                "properties": {"city": {"type": "string", "description": "City name"}},\
                "required": ["city"],\
            },\
            outputSchema={\
                "type": "object",\
                "properties": {\
                    "temperature": {"type": "number", "description": "Temperature in Celsius"},\
                    "condition": {"type": "string", "description": "Weather condition"},\
                    "humidity": {"type": "number", "description": "Humidity percentage"},\
                    "city": {"type": "string", "description": "City name"},\
                },\
                "required": ["temperature", "condition", "humidity", "city"],\
            },\
        )\
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    """Handle tool calls with structured output."""
    if name == "get_weather":
        city = arguments["city"]

        # Simulated weather data - in production, call a weather API
        weather_data = {
            "temperature": 22.5,
            "condition": "partly cloudy",
            "humidity": 65,
            "city": city,  # Include the requested city
        }

        # low-level server will validate structured output against the tool's
        # output schema, and additionally serialize it into a TextContent block
        # for backwards compatibility with pre-2025-06-18 clients.
        return weather_data
    else:
        raise ValueError(f"Unknown tool: {name}")

async def run():
    """Run the structured output server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="structured-output-example",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(run())
```

_Full example: [examples/snippets/servers/lowlevel/structured\_output.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/structured_output.py)_

Tools can return data in four ways:

1. **Content only**: Return a list of content blocks (default behavior before spec revision 2025-06-18)
2. **Structured data only**: Return a dictionary that will be serialized to JSON (Introduced in spec revision 2025-06-18)
3. **Both**: Return a tuple of (content, structured\_data) preferred option to use for backwards compatibility
4. **Direct CallToolResult**: Return `CallToolResult` directly for full control (including `_meta` field)

When an `outputSchema` is defined, the server automatically validates the structured output against the schema. This ensures type safety and helps catch errors early.

##### Returning CallToolResult Directly

For full control over the response including the `_meta` field (for passing data to client applications without exposing it to the model), return `CallToolResult` directly:

```
"""
Run from the repository root:
    uv run examples/snippets/servers/lowlevel/direct_call_tool_result.py
"""

import asyncio
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import NotificationOptions, Server
from mcp.server.models import InitializationOptions

server = Server("example-server")

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    """List available tools."""
    return [\
        types.Tool(\
            name="advanced_tool",\
            description="Tool with full control including _meta field",\
            inputSchema={\
                "type": "object",\
                "properties": {"message": {"type": "string"}},\
                "required": ["message"],\
            },\
        )\
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict[str, Any]) -> types.CallToolResult:
    """Handle tool calls by returning CallToolResult directly."""
    if name == "advanced_tool":
        message = str(arguments.get("message", ""))
        return types.CallToolResult(
            content=[types.TextContent(type="text", text=f"Processed: {message}")],
            structuredContent={"result": "success", "message": message},
            _meta={"hidden": "data for client applications only"},
        )

    raise ValueError(f"Unknown tool: {name}")

async def run():
    """Run the server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="example",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(run())
```

_Full example: [examples/snippets/servers/lowlevel/direct\_call\_tool\_result.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/lowlevel/direct_call_tool_result.py)_

**Note:** When returning `CallToolResult`, you bypass the automatic content/structured conversion. You must construct the complete response yourself.

### Pagination (Advanced)

For servers that need to handle large datasets, the low-level server provides paginated versions of list operations. This is an optional optimization - most servers won't need pagination unless they're dealing with hundreds or thousands of items.

#### Server-side Implementation

```
"""
Example of implementing pagination with MCP server decorators.
"""

from pydantic import AnyUrl

import mcp.types as types
from mcp.server.lowlevel import Server

# Initialize the server
server = Server("paginated-server")

# Sample data to paginate
ITEMS = [f"Item {i}" for i in range(1, 101)]  # 100 items

@server.list_resources()
async def list_resources_paginated(request: types.ListResourcesRequest) -> types.ListResourcesResult:
    """List resources with pagination support."""
    page_size = 10

    # Extract cursor from request params
    cursor = request.params.cursor if request.params is not None else None

    # Parse cursor to get offset
    start = 0 if cursor is None else int(cursor)
    end = start + page_size

    # Get page of resources
    page_items = [\
        types.Resource(uri=AnyUrl(f"resource://items/{item}"), name=item, description=f"Description for {item}")\
        for item in ITEMS[start:end]\
    ]

    # Determine next cursor
    next_cursor = str(end) if end < len(ITEMS) else None

    return types.ListResourcesResult(resources=page_items, nextCursor=next_cursor)
```

_Full example: [examples/snippets/servers/pagination\_example.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/servers/pagination_example.py)_

#### Client-side Consumption

```
"""
Example of consuming paginated MCP endpoints from a client.
"""

import asyncio

from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
from mcp.types import PaginatedRequestParams, Resource

async def list_all_resources() -> None:
    """Fetch all resources using pagination."""
    async with stdio_client(StdioServerParameters(command="uv", args=["run", "mcp-simple-pagination"])) as (
        read,
        write,
    ):
        async with ClientSession(read, write) as session:
            await session.initialize()

            all_resources: list[Resource] = []
            cursor = None

            while True:
                # Fetch a page of resources
                result = await session.list_resources(params=PaginatedRequestParams(cursor=cursor))
                all_resources.extend(result.resources)

                print(f"Fetched {len(result.resources)} resources")

                # Check if there are more pages
                if result.nextCursor:
                    cursor = result.nextCursor
                else:
                    break

            print(f"Total resources: {len(all_resources)}")

if __name__ == "__main__":
    asyncio.run(list_all_resources())
```

_Full example: [examples/snippets/clients/pagination\_client.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/pagination_client.py)_

#### Key Points

- **Cursors are opaque strings** \- the server defines the format (numeric offsets, timestamps, etc.)
- **Return `nextCursor=None`** when there are no more pages
- **Backward compatible** \- clients that don't support pagination will still work (they'll just get the first page)
- **Flexible page sizes** \- Each endpoint can define its own page size based on data characteristics

See the [simple-pagination example](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/servers/simple-pagination) for a complete implementation.

### Writing MCP Clients

The SDK provides a high-level client interface for connecting to MCP servers using various [transports](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports):

```
"""
cd to the `examples/snippets/clients` directory and run:
    uv run client
"""

import asyncio
import os

from pydantic import AnyUrl

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
from mcp.shared.context import RequestContext

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",  # Using uv to run the server
    args=["run", "server", "fastmcp_quickstart", "stdio"],  # We're already in snippets dir
    env={"UV_INDEX": os.environ.get("UV_INDEX", "")},
)

# Optional: create a sampling callback
async def handle_sampling_message(
    context: RequestContext[ClientSession, None], params: types.CreateMessageRequestParams
) -> types.CreateMessageResult:
    print(f"Sampling request: {params.messages}")
    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text="Hello, world! from model",
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, sampling_callback=handle_sampling_message) as session:
            # Initialize the connection
            await session.initialize()

            # List available prompts
            prompts = await session.list_prompts()
            print(f"Available prompts: {[p.name for p in prompts.prompts]}")

            # Get a prompt (greet_user prompt from fastmcp_quickstart)
            if prompts.prompts:
                prompt = await session.get_prompt("greet_user", arguments={"name": "Alice", "style": "friendly"})
                print(f"Prompt result: {prompt.messages[0].content}")

            # List available resources
            resources = await session.list_resources()
            print(f"Available resources: {[r.uri for r in resources.resources]}")

            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")

            # Read a resource (greeting resource from fastmcp_quickstart)
            resource_content = await session.read_resource(AnyUrl("greeting://World"))
            content_block = resource_content.contents[0]
            if isinstance(content_block, types.TextContent):
                print(f"Resource content: {content_block.text}")

            # Call a tool (add tool from fastmcp_quickstart)
            result = await session.call_tool("add", arguments={"a": 5, "b": 3})
            result_unstructured = result.content[0]
            if isinstance(result_unstructured, types.TextContent):
                print(f"Tool result: {result_unstructured.text}")
            result_structured = result.structuredContent
            print(f"Structured tool result: {result_structured}")

def main():
    """Entry point for the client script."""
    asyncio.run(run())

if __name__ == "__main__":
    main()
```

_Full example: [examples/snippets/clients/stdio\_client.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/stdio_client.py)_

Clients can also connect using [Streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http):

```
"""
Run from the repository root:
    uv run examples/snippets/clients/streamable_basic.py
"""

import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    # Connect to a streamable HTTP server
    async with streamablehttp_client("http://localhost:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        # Create a session using the client streams
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")

if __name__ == "__main__":
    asyncio.run(main())
```

_Full example: [examples/snippets/clients/streamable\_basic.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/streamable_basic.py)_

### Client Display Utilities

When building MCP clients, the SDK provides utilities to help display human-readable names for tools, resources, and prompts:

```
"""
cd to the `examples/snippets` directory and run:
    uv run display-utilities-client
"""

import asyncio
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.shared.metadata_utils import get_display_name

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",  # Using uv to run the server
    args=["run", "server", "fastmcp_quickstart", "stdio"],
    env={"UV_INDEX": os.environ.get("UV_INDEX", "")},
)

async def display_tools(session: ClientSession):
    """Display available tools with human-readable names"""
    tools_response = await session.list_tools()

    for tool in tools_response.tools:
        # get_display_name() returns the title if available, otherwise the name
        display_name = get_display_name(tool)
        print(f"Tool: {display_name}")
        if tool.description:
            print(f"   {tool.description}")

async def display_resources(session: ClientSession):
    """Display available resources with human-readable names"""
    resources_response = await session.list_resources()

    for resource in resources_response.resources:
        display_name = get_display_name(resource)
        print(f"Resource: {display_name} ({resource.uri})")

    templates_response = await session.list_resource_templates()
    for template in templates_response.resourceTemplates:
        display_name = get_display_name(template)
        print(f"Resource Template: {display_name}")

async def run():
    """Run the display utilities example."""
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            print("=== Available Tools ===")
            await display_tools(session)

            print("\n=== Available Resources ===")
            await display_resources(session)

def main():
    """Entry point for the display utilities client."""
    asyncio.run(run())

if __name__ == "__main__":
    main()
```

_Full example: [examples/snippets/clients/display\_utilities.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/display_utilities.py)_

The `get_display_name()` function implements the proper precedence rules for displaying names:

- For tools: `title` \> `annotations.title` \> `name`
- For other objects: `title` \> `name`

This ensures your client UI shows the most user-friendly names that servers provide.

### OAuth Authentication for Clients

The SDK includes [authorization support](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) for connecting to protected MCP servers:

```
"""
Before running, specify running MCP RS server URL.
To spin up RS server locally, see
    examples/servers/simple-auth/README.md

cd to the `examples/snippets` directory and run:
    uv run oauth-client
"""

import asyncio
from urllib.parse import parse_qs, urlparse

from pydantic import AnyUrl

from mcp import ClientSession
from mcp.client.auth import OAuthClientProvider, TokenStorage
from mcp.client.streamable_http import streamablehttp_client
from mcp.shared.auth import OAuthClientInformationFull, OAuthClientMetadata, OAuthToken

class InMemoryTokenStorage(TokenStorage):
    """Demo In-memory token storage implementation."""

    def __init__(self):
        self.tokens: OAuthToken | None = None
        self.client_info: OAuthClientInformationFull | None = None

    async def get_tokens(self) -> OAuthToken | None:
        """Get stored tokens."""
        return self.tokens

    async def set_tokens(self, tokens: OAuthToken) -> None:
        """Store tokens."""
        self.tokens = tokens

    async def get_client_info(self) -> OAuthClientInformationFull | None:
        """Get stored client information."""
        return self.client_info

    async def set_client_info(self, client_info: OAuthClientInformationFull) -> None:
        """Store client information."""
        self.client_info = client_info

async def handle_redirect(auth_url: str) -> None:
    print(f"Visit: {auth_url}")

async def handle_callback() -> tuple[str, str | None]:
    callback_url = input("Paste callback URL: ")
    params = parse_qs(urlparse(callback_url).query)
    return params["code"][0], params.get("state", [None])[0]

async def main():
    """Run the OAuth client example."""
    oauth_auth = OAuthClientProvider(
        server_url="http://localhost:8001",
        client_metadata=OAuthClientMetadata(
            client_name="Example MCP Client",
            redirect_uris=[AnyUrl("http://localhost:3000/callback")],
            grant_types=["authorization_code", "refresh_token"],
            response_types=["code"],
            scope="user",
        ),
        storage=InMemoryTokenStorage(),
        redirect_handler=handle_redirect,
        callback_handler=handle_callback,
    )

    async with streamablehttp_client("http://localhost:8001/mcp", auth=oauth_auth) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")

            resources = await session.list_resources()
            print(f"Available resources: {[r.uri for r in resources.resources]}")

def run():
    asyncio.run(main())

if __name__ == "__main__":
    run()
```

_Full example: [examples/snippets/clients/oauth\_client.py](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/snippets/clients/oauth_client.py)_

For a complete working example, see [`examples/clients/simple-auth-client/`](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/clients/simple-auth-client).

### Parsing Tool Results

When calling tools through MCP, the `CallToolResult` object contains the tool's response in a structured format. Understanding how to parse this result is essential for properly handling tool outputs.

```
"""examples/snippets/clients/parsing_tool_results.py"""

import asyncio

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

async def parse_tool_results():
    """Demonstrates how to parse different types of content in CallToolResult."""
    server_params = StdioServerParameters(
        command="python", args=["path/to/mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Example 1: Parsing text content
            result = await session.call_tool("get_data", {"format": "text"})
            for content in result.content:
                if isinstance(content, types.TextContent):
                    print(f"Text: {content.text}")

            # Example 2: Parsing structured content from JSON tools
            result = await session.call_tool("get_user", {"id": "123"})
            if hasattr(result, "structuredContent") and result.structuredContent:
                # Access structured data directly
                user_data = result.structuredContent
                print(f"User: {user_data.get('name')}, Age: {user_data.get('age')}")

            # Example 3: Parsing embedded resources
            result = await session.call_tool("read_config", {})
            for content in result.content:
                if isinstance(content, types.EmbeddedResource):
                    resource = content.resource
                    if isinstance(resource, types.TextResourceContents):
                        print(f"Config from {resource.uri}: {resource.text}")
                    elif isinstance(resource, types.BlobResourceContents):
                        print(f"Binary data from {resource.uri}")

            # Example 4: Parsing image content
            result = await session.call_tool("generate_chart", {"data": [1, 2, 3]})
            for content in result.content:
                if isinstance(content, types.ImageContent):
                    print(f"Image ({content.mimeType}): {len(content.data)} bytes")

            # Example 5: Handling errors
            result = await session.call_tool("failing_tool", {})
            if result.isError:
                print("Tool execution failed!")
                for content in result.content:
                    if isinstance(content, types.TextContent):
                        print(f"Error: {content.text}")

async def main():
    await parse_tool_results()

if __name__ == "__main__":
    asyncio.run(main())
```

### MCP Primitives

The MCP protocol defines three core primitives that servers can implement:

| Primitive | Control | Description | Example Use |
| --- | --- | --- | --- |
| Prompts | User-controlled | Interactive templates invoked by user choice | Slash commands, menu options |
| Resources | Application-controlled | Contextual data managed by the client application | File contents, API responses |
| Tools | Model-controlled | Functions exposed to the LLM to take actions | API calls, data updates |

### Server Capabilities

MCP servers declare capabilities during initialization:

| Capability | Feature Flag | Description |
| --- | --- | --- |
| `prompts` | `listChanged` | Prompt template management |
| `resources` | `subscribe`<br>`listChanged` | Resource exposure and updates |
| `tools` | `listChanged` | Tool discovery and execution |
| `logging` | - | Server logging configuration |
| `completions` | - | Argument completion suggestions |

## Documentation

- [API Reference](https://modelcontextprotocol.github.io/python-sdk/api/)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification/latest)
- [Officially supported servers](https://github.com/modelcontextprotocol/servers)

## Contributing

We are passionate about supporting contributors of all levels of experience and would love to see you get involved in the project. See the [contributing guide](https://github.com/modelcontextprotocol/python-sdk/blob/main/CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

</details>

<details>
<summary>The central piece of a FastMCP application is the `FastMCP` server class. This class acts as the main container for your application’s tools, resources, and prompts, and manages communication with MCP clients.</summary>

The central piece of a FastMCP application is the `FastMCP` server class. This class acts as the main container for your application’s tools, resources, and prompts, and manages communication with MCP clients.

## [​](https://gofastmcp.com/servers/server\#creating-a-server)  Creating a Server

Instantiating a server is straightforward. You typically provide a name for your server, which helps identify it in client applications or logs.

```
from fastmcp import FastMCP

# Create a basic server instance
mcp = FastMCP(name="MyAssistantServer")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="HelpfulAssistant",
    instructions="""
        This server provides data analysis tools.
        Call get_average() to analyze numerical data.
    """,
)

```

The `FastMCP` constructor accepts several arguments:

## FastMCP Constructor Parameters

[​](https://gofastmcp.com/servers/server#param-name)

name

str

default:"FastMCP"

A human-readable name for your server

[​](https://gofastmcp.com/servers/server#param-instructions)

instructions

str \| None

Description of how to interact with this server. These instructions help clients understand the server’s purpose and available functionality

[​](https://gofastmcp.com/servers/server#param-version)

version

str \| None

Version string for your server. If not provided, defaults to the FastMCP library version

[​](https://gofastmcp.com/servers/server#param-website-url)

website\_url

str \| None

`New in version: 2.14.0` URL to a website with more information about your server. Displayed in client applications

[​](https://gofastmcp.com/servers/server#param-icons)

icons

list\[Icon\] \| None

`New in version: 2.14.0` List of icon representations for your server. Icons help users visually identify your server in client applications. See [Icons](https://gofastmcp.com/servers/icons) for detailed examples

[​](https://gofastmcp.com/servers/server#param-auth)

auth

OAuthProvider \| TokenVerifier \| None

Authentication provider for securing HTTP-based transports. See [Authentication](https://gofastmcp.com/servers/auth/authentication) for configuration options

[​](https://gofastmcp.com/servers/server#param-lifespan)

lifespan

AsyncContextManager \| None

An async context manager function for server startup and shutdown logic

[​](https://gofastmcp.com/servers/server#param-tools)

tools

list\[Tool \| Callable\] \| None

A list of tools (or functions to convert to tools) to add to the server. In some cases, providing tools programmatically may be more convenient than using the `@mcp.tool` decorator

[​](https://gofastmcp.com/servers/server#param-include-tags)

include\_tags

set\[str\] \| None

Only expose components with at least one matching tag

[​](https://gofastmcp.com/servers/server#param-exclude-tags)

exclude\_tags

set\[str\] \| None

Hide components with any matching tag

[​](https://gofastmcp.com/servers/server#param-on-duplicate-tools)

on\_duplicate\_tools

Literal\["error", "warn", "replace"\]

default:"error"

How to handle duplicate tool registrations

[​](https://gofastmcp.com/servers/server#param-on-duplicate-resources)

on\_duplicate\_resources

Literal\["error", "warn", "replace"\]

default:"warn"

How to handle duplicate resource registrations

[​](https://gofastmcp.com/servers/server#param-on-duplicate-prompts)

on\_duplicate\_prompts

Literal\["error", "warn", "replace"\]

default:"replace"

How to handle duplicate prompt registrations

[​](https://gofastmcp.com/servers/server#param-strict-input-validation)

strict\_input\_validation

bool

default:"False"

`New in version: 2.13.0` Controls how tool input parameters are validated. When `False` (default), FastMCP uses Pydantic’s flexible validation that coerces compatible inputs (e.g., `"10"` → `10` for int parameters). When `True`, uses the MCP SDK’s JSON Schema validation to validate inputs against the exact schema before passing them to your function, rejecting any type mismatches. The default mode improves compatibility with LLM clients while maintaining type safety. See [Input Validation Modes](https://gofastmcp.com/servers/tools#input-validation-modes) for details

[​](https://gofastmcp.com/servers/server#param-include-fastmcp-meta)

include\_fastmcp\_meta

bool

default:"True"

`New in version: 2.11.0` Whether to include FastMCP metadata in component responses. When `True`, component tags and other FastMCP-specific metadata are included in the `_fastmcp` namespace within each component’s `meta` field. When `False`, this metadata is omitted, resulting in cleaner integration with external systems. Can be overridden globally via `FASTMCP_INCLUDE_FASTMCP_META` environment variable

## [​](https://gofastmcp.com/servers/server\#components)  Components

FastMCP servers expose several types of components to the client:

### [​](https://gofastmcp.com/servers/server\#tools)  Tools

Tools are functions that the client can call to perform actions or access external systems.

```
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

```

See [Tools](https://gofastmcp.com/servers/tools) for detailed documentation.

### [​](https://gofastmcp.com/servers/server\#resources)  Resources

Resources expose data sources that the client can read.

```
@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}

```

See [Resources & Templates](https://gofastmcp.com/servers/resources) for detailed documentation.

### [​](https://gofastmcp.com/servers/server\#resource-templates)  Resource Templates

Resource templates are parameterized resources that allow the client to request specific data.

```
@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: int) -> dict:
    """Retrieves a user's profile by ID."""
    # The {user_id} in the URI is extracted and passed to this function
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}

```

See [Resources & Templates](https://gofastmcp.com/servers/resources) for detailed documentation.

### [​](https://gofastmcp.com/servers/server\#prompts)  Prompts

Prompts are reusable message templates for guiding the LLM.

```
@mcp.prompt
def analyze_data(data_points: list[float]) -> str:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"

```

See [Prompts](https://gofastmcp.com/servers/prompts) for detailed documentation.

## [​](https://gofastmcp.com/servers/server\#tag-based-filtering)  Tag-Based Filtering

`New in version: 2.8.0` FastMCP supports tag-based filtering to selectively expose components based on configurable include/exclude tag sets. This is useful for creating different views of your server for different environments or users.Components can be tagged when defined using the `tags` parameter:

```
@mcp.tool(tags={"public", "utility"})
def public_tool() -> str:
    return "This tool is public"

@mcp.tool(tags={"internal", "admin"})
def admin_tool() -> str:
    return "This tool is for admins only"

```

The filtering logic works as follows:

- **Include tags**: If specified, only components with at least one matching tag are exposed
- **Exclude tags**: Components with any matching tag are filtered out
- **Precedence**: Exclude tags always take priority over include tags

To ensure a component is never exposed, you can set `enabled=False` on the component itself. To learn more, see the component-specific documentation.

You configure tag-based filtering when creating your server:

```
# Only expose components tagged with "public"
mcp = FastMCP(include_tags={"public"})

# Hide components tagged as "internal" or "deprecated"
mcp = FastMCP(exclude_tags={"internal", "deprecated"})

# Combine both: show admin tools but hide deprecated ones
mcp = FastMCP(include_tags={"admin"}, exclude_tags={"deprecated"})

```

This filtering applies to all component types (tools, resources, resource templates, and prompts) and affects both listing and access.

## [​](https://gofastmcp.com/servers/server\#running-the-server)  Running the Server

FastMCP servers need a transport mechanism to communicate with clients. You typically start your server by calling the `mcp.run()` method on your `FastMCP` instance, often within an `if __name__ == "__main__":` block in your main server script. This pattern ensures compatibility with various MCP clients.

```
# my_server.py
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    mcp.run()

    # To use a different transport, e.g., HTTP:
    # mcp.run(transport="http", host="127.0.0.1", port=9000)

```

FastMCP supports several transport options:

- STDIO (default, for local tools)
- HTTP (recommended for web services, uses Streamable HTTP protocol)
- SSE (legacy web transport, deprecated)

The server can also be run using the FastMCP CLI.For detailed information on each transport, how to configure them (host, port, paths), and when to use which, please refer to the [**Running Your FastMCP Server**](https://gofastmcp.com/deployment/running-server) guide.

## [​](https://gofastmcp.com/servers/server\#custom-routes)  Custom Routes

When running your server with HTTP transport, you can add custom web routes alongside your MCP endpoint using the `@custom_route` decorator. This is useful for simple endpoints like health checks that need to be served alongside your MCP server:

```
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

if __name__ == "__main__":
    mcp.run(transport="http")  # Health check at http://localhost:8000/health

```

Custom routes are served alongside your MCP endpoint and are useful for:

- Health check endpoints for monitoring
- Simple status or info endpoints
- Basic webhooks or callbacks

For more complex web applications, consider [mounting your MCP server into a FastAPI or Starlette app](https://gofastmcp.com/deployment/http#integration-with-web-frameworks).

## [​](https://gofastmcp.com/servers/server\#composing-servers)  Composing Servers

`New in version: 2.2.0` FastMCP supports composing multiple servers together using `import_server` (static copy) and `mount` (live link). This allows you to organize large applications into modular components or reuse existing servers.See the [Server Composition](https://gofastmcp.com/servers/composition) guide for full details, best practices, and examples.

```
# Example: Importing a subserver
from fastmcp import FastMCP
import asyncio

main = FastMCP(name="Main")
sub = FastMCP(name="Sub")

@sub.tool
def hello():
    return "hi"

# Mount directly
main.mount(sub, prefix="sub")

```

## [​](https://gofastmcp.com/servers/server\#proxying-servers)  Proxying Servers

`New in version: 2.0.0` FastMCP can act as a proxy for any MCP server (local or remote) using `FastMCP.as_proxy`, letting you bridge transports or add a frontend to existing servers. For example, you can expose a remote SSE server locally via stdio, or vice versa.Proxies automatically handle concurrent operations safely by creating fresh sessions for each request when using disconnected clients.See the [Proxying Servers](https://gofastmcp.com/servers/proxy) guide for details and advanced usage.

```
from fastmcp import FastMCP, Client

backend = Client("http://example.com/mcp/sse")
proxy = FastMCP.as_proxy(backend, name="ProxyServer")
# Now use the proxy like any FastMCP server

```

## [​](https://gofastmcp.com/servers/server\#openapi-integration)  OpenAPI Integration

`New in version: 2.0.0` FastMCP can automatically generate servers from OpenAPI specifications or existing FastAPI applications using `FastMCP.from_openapi()` and `FastMCP.from_fastapi()`. This allows you to instantly convert existing APIs into MCP servers without manual tool creation.See the [FastAPI Integration](https://gofastmcp.com/integrations/fastapi) and [OpenAPI Integration](https://gofastmcp.com/integrations/openapi) guides for detailed examples and configuration options.

```
import httpx
from fastmcp import FastMCP

# From OpenAPI spec
spec = httpx.get("https://api.example.com/openapi.json").json()
mcp = FastMCP.from_openapi(openapi_spec=spec, client=httpx.AsyncClient())

# From FastAPI app
from fastapi import FastAPI
app = FastAPI()
mcp = FastMCP.from_fastapi(app=app)

```

## [​](https://gofastmcp.com/servers/server\#server-configuration)  Server Configuration

Servers can be configured using a combination of initialization arguments, global settings, and transport-specific settings.

### [​](https://gofastmcp.com/servers/server\#server-specific-configuration)  Server-Specific Configuration

Server-specific settings are passed when creating the `FastMCP` instance and control server behavior:

```
from fastmcp import FastMCP

# Configure server-specific settings
mcp = FastMCP(
    name="ConfiguredServer",
    include_tags={"public", "api"},              # Only expose these tagged components
    exclude_tags={"internal", "deprecated"},     # Hide these tagged components
    on_duplicate_tools="error",                  # Handle duplicate registrations
    on_duplicate_resources="warn",
    on_duplicate_prompts="replace",
    include_fastmcp_meta=False,                  # Disable FastMCP metadata for cleaner integration
)

```

### [​](https://gofastmcp.com/servers/server\#global-settings)  Global Settings

Global settings affect all FastMCP servers and can be configured via environment variables (prefixed with `FASTMCP_`) or in a `.env` file:

```
import fastmcp

# Access global settings
print(fastmcp.settings.log_level)        # Default: "INFO"
print(fastmcp.settings.mask_error_details)  # Default: False
print(fastmcp.settings.resource_prefix_format)  # Default: "path"
print(fastmcp.settings.strict_input_validation)  # Default: False
print(fastmcp.settings.include_fastmcp_meta)   # Default: True

```

Common global settings include:

- **`log_level`**: Logging level (“DEBUG”, “INFO”, “WARNING”, “ERROR”, “CRITICAL”), set with `FASTMCP_LOG_LEVEL`
- **`mask_error_details`**: Whether to hide detailed error information from clients, set with `FASTMCP_MASK_ERROR_DETAILS`
- **`resource_prefix_format`**: How to format resource prefixes (“path” or “protocol”), set with `FASTMCP_RESOURCE_PREFIX_FORMAT`
- **`strict_input_validation`**: Controls tool input validation mode (default: False for flexible coercion), set with `FASTMCP_STRICT_INPUT_VALIDATION`. See [Input Validation Modes](https://gofastmcp.com/servers/tools#input-validation-modes)
- **`include_fastmcp_meta`**: Whether to include FastMCP metadata in component responses (default: True), set with `FASTMCP_INCLUDE_FASTMCP_META`
- **`env_file`**: Path to the environment file to load settings from (default: “.env”), set with `FASTMCP_ENV_FILE`. Useful when your project uses a `.env` file with syntax incompatible with python-dotenv

### [​](https://gofastmcp.com/servers/server\#transport-specific-configuration)  Transport-Specific Configuration

Transport settings are provided when running the server and control network behavior:

```
# Configure transport when running
mcp.run(
    transport="http",
    host="0.0.0.0",           # Bind to all interfaces
    port=9000,                # Custom port
    log_level="DEBUG",        # Override global log level
)

# Or for async usage
await mcp.run_async(
    transport="http",
    host="127.0.0.1",
    port=8080,
)

```

### [​](https://gofastmcp.com/servers/server\#setting-global-configuration)  Setting Global Configuration

Global FastMCP settings can be configured via environment variables (prefixed with `FASTMCP_`):

```
# Configure global FastMCP behavior
export FASTMCP_LOG_LEVEL=DEBUG
export FASTMCP_MASK_ERROR_DETAILS=True
export FASTMCP_RESOURCE_PREFIX_FORMAT=protocol
export FASTMCP_STRICT_INPUT_VALIDATION=False
export FASTMCP_INCLUDE_FASTMCP_META=False

```

### [​](https://gofastmcp.com/servers/server\#custom-tool-serialization)  Custom Tool Serialization

`New in version: 2.2.7` By default, FastMCP serializes tool return values to JSON when they need to be converted to text. You can customize this behavior by providing a `tool_serializer` function when creating your server:

```
import yaml
from fastmcp import FastMCP

# Define a custom serializer that formats dictionaries as YAML
def yaml_serializer(data):
    return yaml.dump(data, sort_keys=False)

# Create a server with the custom serializer
mcp = FastMCP(name="MyServer", tool_serializer=yaml_serializer)

@mcp.tool
def get_config():
    """Returns configuration in YAML format."""
    return {"api_key": "abc123", "debug": True, "rate_limit": 100}

```

The serializer function takes any data object and returns a string representation. This is applied to **all non-string return values** from your tools. Tools that already return strings bypass the serializer.This customization is useful when you want to:

- Format data in a specific way (like YAML or custom formats)
- Control specific serialization options (like indentation or sorting)
- Add metadata or transform data before sending it to clients

If the serializer function raises an exception, the tool will fall back to the default JSON serialization to avoid breaking the server.

</details>


## Code Sources

<details>
<summary>Repository analysis for https://github.com/jlowin/fastmcp</summary>

# Repository analysis for https://github.com/jlowin/fastmcp

## Summary
Repository: jlowin/fastmcp
Files analyzed: 631

Estimated tokens: 1.2M

## File tree
```Directory structure:
└── jlowin-fastmcp/
    ├── README.md
    ├── AGENTS.md
    ├── CODE_OF_CONDUCT.md
    ├── justfile
    ├── LICENSE
    ├── logo.py
    ├── pyproject.toml
    ├── SECURITY.md
    ├── .ccignore
    ├── .pre-commit-config.yaml
    ├── .python-version
    ├── CLAUDE.md -> AGENTS.md
    ├── docs/
    │   ├── changelog.mdx
    │   ├── docs.json
    │   ├── updates.mdx
    │   ├── .ccignore
    │   ├── assets/
    │   │   └── schemas/
    │   │       └── mcp_server_config/
    │   │           ├── latest.json
    │   │           └── v1.json
    │   ├── clients/
    │   │   ├── client.mdx
    │   │   ├── elicitation.mdx
    │   │   ├── logging.mdx
    │   │   ├── messages.mdx
    │   │   ├── progress.mdx
    │   │   ├── prompts.mdx
    │   │   ├── resources.mdx
    │   │   ├── roots.mdx
    │   │   ├── sampling.mdx
    │   │   ├── tools.mdx
    │   │   ├── transports.mdx
    │   │   └── auth/
    │   │       ├── bearer.mdx
    │   │       └── oauth.mdx
    │   ├── community/
    │   │   ├── README.md
    │   │   └── showcase.mdx
    │   ├── css/
    │   │   ├── banner.css
    │   │   ├── python-sdk.css
    │   │   ├── style.css
    │   │   └── version-badge.css
    │   ├── deployment/
    │   │   ├── fastmcp-cloud.mdx
    │   │   ├── http.mdx
    │   │   ├── running-server.mdx
    │   │   └── server-configuration.mdx
    │   ├── development/
    │   │   ├── contributing.mdx
    │   │   ├── releases.mdx
    │   │   ├── tests.mdx
    │   │   └── upgrade-guide.mdx
    │   ├── getting-started/
    │   │   ├── installation.mdx
    │   │   ├── quickstart.mdx
    │   │   └── welcome.mdx
    │   ├── integrations/
    │   │   ├── anthropic.mdx
    │   │   ├── auth0.mdx
    │   │   ├── authkit.mdx
    │   │   ├── aws-cognito.mdx
    │   │   ├── azure.mdx
    │   │   ├── chatgpt.mdx
    │   │   ├── claude-code.mdx
    │   │   ├── claude-desktop.mdx
    │   │   ├── cursor.mdx
    │   │   ├── descope.mdx
    │   │   ├── eunomia-authorization.mdx
    │   │   ├── fastapi.mdx
    │   │   ├── gemini-cli.mdx
    │   │   ├── gemini.mdx
    │   │   ├── github.mdx
    │   │   ├── google.mdx
    │   │   ├── mcp-json-configuration.mdx
    │   │   ├── openai.mdx
    │   │   ├── openapi.mdx
    │   │   ├── permit.mdx
    │   │   ├── scalekit.mdx
    │   │   └── workos.mdx
    │   ├── patterns/
    │   │   ├── cli.mdx
    │   │   ├── contrib.mdx
    │   │   ├── decorating-methods.mdx
    │   │   ├── testing.mdx
    │   │   └── tool-transformation.mdx
    │   ├── public/
    │   │   └── schemas/
    │   │       └── fastmcp.json/
    │   │           ├── latest.json
    │   │           └── v1.json
    │   ├── python-sdk/
    │   │   ├── fastmcp-cli-__init__.mdx
    │   │   ├── fastmcp-cli-cli.mdx
    │   │   ├── fastmcp-cli-install-__init__.mdx
    │   │   ├── fastmcp-cli-install-claude_code.mdx
    │   │   ├── fastmcp-cli-install-claude_desktop.mdx
    │   │   ├── fastmcp-cli-install-cursor.mdx
    │   │   ├── fastmcp-cli-install-gemini_cli.mdx
    │   │   ├── fastmcp-cli-install-mcp_json.mdx
    │   │   ├── fastmcp-cli-install-shared.mdx
    │   │   ├── fastmcp-cli-run.mdx
    │   │   ├── fastmcp-client-__init__.mdx
    │   │   ├── fastmcp-client-auth-__init__.mdx
    │   │   ├── fastmcp-client-auth-bearer.mdx
    │   │   ├── fastmcp-client-auth-oauth.mdx
    │   │   ├── fastmcp-client-client.mdx
    │   │   ├── fastmcp-client-elicitation.mdx
    │   │   ├── fastmcp-client-logging.mdx
    │   │   ├── fastmcp-client-messages.mdx
    │   │   ├── fastmcp-client-oauth_callback.mdx
    │   │   ├── fastmcp-client-progress.mdx
    │   │   ├── fastmcp-client-roots.mdx
    │   │   ├── fastmcp-client-sampling.mdx
    │   │   ├── fastmcp-client-transports.mdx
    │   │   ├── fastmcp-exceptions.mdx
    │   │   ├── fastmcp-mcp_config.mdx
    │   │   ├── fastmcp-prompts-__init__.mdx
    │   │   ├── fastmcp-prompts-prompt.mdx
    │   │   ├── fastmcp-prompts-prompt_manager.mdx
    │   │   ├── fastmcp-resources-__init__.mdx
    │   │   ├── fastmcp-resources-resource.mdx
    │   │   ├── fastmcp-resources-resource_manager.mdx
    │   │   ├── fastmcp-resources-template.mdx
    │   │   ├── fastmcp-resources-types.mdx
    │   │   ├── fastmcp-server-__init__.mdx
    │   │   ├── fastmcp-server-auth-__init__.mdx
    │   │   ├── fastmcp-server-auth-auth.mdx
    │   │   ├── fastmcp-server-auth-jwt_issuer.mdx
    │   │   ├── fastmcp-server-auth-middleware.mdx
    │   │   ├── fastmcp-server-auth-oauth_proxy.mdx
    │   │   ├── fastmcp-server-auth-oidc_proxy.mdx
    │   │   ├── fastmcp-server-auth-providers-__init__.mdx
    │   │   ├── fastmcp-server-auth-providers-auth0.mdx
    │   │   ├── fastmcp-server-auth-providers-aws.mdx
    │   │   ├── fastmcp-server-auth-providers-azure.mdx
    │   │   ├── fastmcp-server-auth-providers-bearer.mdx
    │   │   ├── fastmcp-server-auth-providers-descope.mdx
    │   │   ├── fastmcp-server-auth-providers-github.mdx
    │   │   ├── fastmcp-server-auth-providers-google.mdx
    │   │   ├── fastmcp-server-auth-providers-in_memory.mdx
    │   │   ├── fastmcp-server-auth-providers-introspection.mdx
    │   │   ├── fastmcp-server-auth-providers-jwt.mdx
    │   │   ├── fastmcp-server-auth-providers-scalekit.mdx
    │   │   ├── fastmcp-server-auth-providers-supabase.mdx
    │   │   ├── fastmcp-server-auth-providers-workos.mdx
    │   │   ├── fastmcp-server-auth-redirect_validation.mdx
    │   │   ├── fastmcp-server-context.mdx
    │   │   ├── fastmcp-server-dependencies.mdx
    │   │   ├── fastmcp-server-elicitation.mdx
    │   │   ├── fastmcp-server-http.mdx
    │   │   ├── fastmcp-server-low_level.mdx
    │   │   ├── fastmcp-server-middleware-__init__.mdx
    │   │   ├── fastmcp-server-middleware-caching.mdx
    │   │   ├── fastmcp-server-middleware-error_handling.mdx
    │   │   ├── fastmcp-server-middleware-logging.mdx
    │   │   ├── fastmcp-server-middleware-middleware.mdx
    │   │   ├── fastmcp-server-middleware-rate_limiting.mdx
    │   │   ├── fastmcp-server-middleware-timing.mdx
    │   │   ├── fastmcp-server-middleware-tool_injection.mdx
    │   │   ├── fastmcp-server-openapi.mdx
    │   │   ├── fastmcp-server-proxy.mdx
    │   │   ├── fastmcp-server-server.mdx
    │   │   ├── fastmcp-settings.mdx
    │   │   ├── fastmcp-tools-__init__.mdx
    │   │   ├── fastmcp-tools-tool.mdx
    │   │   ├── fastmcp-tools-tool_manager.mdx
    │   │   ├── fastmcp-tools-tool_transform.mdx
    │   │   ├── fastmcp-utilities-__init__.mdx
    │   │   ├── fastmcp-utilities-auth.mdx
    │   │   ├── fastmcp-utilities-cli.mdx
    │   │   ├── fastmcp-utilities-components.mdx
    │   │   ├── fastmcp-utilities-exceptions.mdx
    │   │   ├── fastmcp-utilities-http.mdx
    │   │   ├── fastmcp-utilities-inspect.mdx
    │   │   ├── fastmcp-utilities-json_schema.mdx
    │   │   ├── fastmcp-utilities-json_schema_type.mdx
    │   │   ├── fastmcp-utilities-logging.mdx
    │   │   ├── fastmcp-utilities-mcp_config.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-__init__.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-v1-__init__.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-v1-environments-__init__.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-v1-environments-base.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-v1-environments-uv.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-v1-mcp_server_config.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-v1-sources-__init__.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-v1-sources-base.mdx
    │   │   ├── fastmcp-utilities-mcp_server_config-v1-sources-filesystem.mdx
    │   │   ├── fastmcp-utilities-openapi.mdx
    │   │   ├── fastmcp-utilities-tests.mdx
    │   │   ├── fastmcp-utilities-types.mdx
    │   │   └── fastmcp-utilities-ui.mdx
    │   ├── servers/
    │   │   ├── composition.mdx
    │   │   ├── context.mdx
    │   │   ├── elicitation.mdx
    │   │   ├── icons.mdx
    │   │   ├── logging.mdx
    │   │   ├── middleware.mdx
    │   │   ├── progress.mdx
    │   │   ├── prompts.mdx
    │   │   ├── proxy.mdx
    │   │   ├── resources.mdx
    │   │   ├── sampling.mdx
    │   │   ├── server.mdx
    │   │   ├── storage-backends.mdx
    │   │   ├── tools.mdx
    │   │   └── auth/
    │   │       ├── authentication.mdx
    │   │       ├── full-oauth-server.mdx
    │   │       ├── oauth-proxy.mdx
    │   │       ├── oidc-proxy.mdx
    │   │       ├── remote-oauth.mdx
    │   │       └── token-verification.mdx
    │   ├── snippets/
    │   │   ├── local-focus.mdx
    │   │   ├── version-badge.mdx
    │   │   └── youtube-embed.mdx
    │   ├── tutorials/
    │   │   ├── create-mcp-server.mdx
    │   │   ├── mcp.mdx
    │   │   └── rest-api.mdx
    │   └── .cursor/
    │       └── rules/
    │           └── mintlify.mdc
    ├── examples/
    │   ├── complex_inputs.py
    │   ├── config_server.py
    │   ├── desktop.py
    │   ├── echo.py
    │   ├── get_file.py
    │   ├── in_memory_proxy_example.py
    │   ├── memory.fastmcp.json
    │   ├── memory.py
    │   ├── mount_example.fastmcp.json
    │   ├── mount_example.py
    │   ├── sampling.py
    │   ├── sampling_fallback.py
    │   ├── screenshot.fastmcp.json
    │   ├── screenshot.py
    │   ├── serializer.py
    │   ├── simple_echo.py
    │   ├── tags_example.py
    │   ├── text_me.py
    │   ├── atproto_mcp/
    │   │   ├── README.md
    │   │   ├── demo.py
    │   │   ├── fastmcp.json
    │   │   ├── pyproject.toml
    │   │   └── src/
    │   │       └── atproto_mcp/
    │   │           ├── __init__.py
    │   │           ├── __main__.py
    │   │           ├── py.typed
    │   │           ├── server.py
    │   │           ├── settings.py
    │   │           ├── types.py
    │   │           └── _atproto/
    │   │               ├── __init__.py
    │   │               ├── _client.py
    │   │               ├── _posts.py
    │   │               ├── _profile.py
    │   │               ├── _read.py
    │   │               └── _social.py
    │   ├── auth/
    │   │   ├── authkit_dcr/
    │   │   │   ├── README.md
    │   │   │   ├── client.py
    │   │   │   └── server.py
    │   │   ├── aws_oauth/
    │   │   │   ├── README.md
    │   │   │   ├── client.py
    │   │   │   ├── requirements.txt
    │   │   │   └── server.py
    │   │   ├── azure_oauth/
    │   │   │   ├── README.md
    │   │   │   ├── client.py
    │   │   │   └── server.py
    │   │   ├── github_oauth/
    │   │   │   ├── README.md
    │   │   │   ├── client.py
    │   │   │   └── server.py
    │   │   ├── google_oauth/
    │   │   │   ├── README.md
    │   │   │   ├── client.py
    │   │   │   └── server.py
    │   │   ├── scalekit_oauth/
    │   │   │   ├── README.md
    │   │   │   ├── client.py
    │   │   │   └── server.py
    │   │   └── workos_oauth/
    │   │       ├── README.md
    │   │       ├── client.py
    │   │       └── server.py
    │   ├── fastmcp_config/
    │   │   ├── env_interpolation_example.json
    │   │   ├── fastmcp.json
    │   │   ├── full_example.fastmcp.json
    │   │   ├── server.py
    │   │   └── simple.fastmcp.json
    │   ├── fastmcp_config_demo/
    │   │   ├── README.md
    │   │   ├── fastmcp.json
    │   │   └── server.py
    │   └── smart_home/
    │       ├── README.md
    │       ├── hub.fastmcp.json
    │       ├── lights.fastmcp.json
    │       ├── pyproject.toml
    │       └── src/
    │           └── smart_home/
    │               ├── __init__.py
    │               ├── __main__.py
    │               ├── hub.py
    │               ├── py.typed
    │               ├── settings.py
    │               └── lights/
    │                   ├── __init__.py
    │                   ├── hue_utils.py
    │                   └── server.py
    ├── scripts/
    │   ├── auto_close_duplicates.py
    │   └── auto_close_needs_mre.py
    ├── src/
    │   └── fastmcp/
    │       ├── __init__.py
    │       ├── exceptions.py
    │       ├── mcp_config.py
    │       ├── py.typed
    │       ├── settings.py
    │       ├── cli/
    │       │   ├── __init__.py
    │       │   ├── cli.py
    │       │   ├── run.py
    │       │   └── install/
    │       │       ├── __init__.py
    │       │       ├── claude_code.py
    │       │       ├── claude_desktop.py
    │       │       ├── cursor.py
    │       │       ├── gemini_cli.py
    │       │       ├── mcp_json.py
    │       │       └── shared.py
    │       ├── client/
    │       │   ├── __init__.py
    │       │   ├── client.py
    │       │   ├── elicitation.py
    │       │   ├── logging.py
    │       │   ├── messages.py
    │       │   ├── oauth_callback.py
    │       │   ├── progress.py
    │       │   ├── roots.py
    │       │   ├── sampling.py
    │       │   ├── transports.py
    │       │   └── auth/
    │       │       ├── __init__.py
    │       │       ├── bearer.py
    │       │       └── oauth.py
    │       ├── contrib/
    │       │   ├── README.md
    │       │   ├── bulk_tool_caller/
    │       │   │   ├── README.md
    │       │   │   ├── __init__.py
    │       │   │   ├── bulk_tool_caller.py
    │       │   │   └── example.py
    │       │   ├── component_manager/
    │       │   │   ├── README.md
    │       │   │   ├── __init__.py
    │       │   │   ├── component_manager.py
    │       │   │   ├── component_service.py
    │       │   │   └── example.py
    │       │   └── mcp_mixin/
    │       │       ├── README.md
    │       │       ├── __init__.py
    │       │       ├── example.py
    │       │       └── mcp_mixin.py
    │       ├── experimental/
    │       │   ├── sampling/
    │       │   │   ├── __init__.py
    │       │   │   └── handlers/
    │       │   │       ├── __init__.py
    │       │   │       ├── base.py
    │       │   │       └── openai.py
    │       │   ├── server/
    │       │   │   └── openapi/
    │       │   │       ├── README.md
    │       │   │       ├── __init__.py
    │       │   │       ├── components.py
    │       │   │       ├── routing.py
    │       │   │       └── server.py
    │       │   └── utilities/
    │       │       └── openapi/
    │       │           ├── README.md
    │       │           ├── __init__.py
    │       │           ├── director.py
    │       │           ├── formatters.py
    │       │           ├── json_schema_converter.py
    │       │           ├── models.py
    │       │           ├── parser.py
    │       │           └── schemas.py
    │       ├── prompts/
    │       │   ├── __init__.py
    │       │   ├── prompt.py
    │       │   └── prompt_manager.py
    │       ├── resources/
    │       │   ├── __init__.py
    │       │   ├── resource.py
    │       │   ├── resource_manager.py
    │       │   ├── template.py
    │       │   └── types.py
    │       ├── server/
    │       │   ├── __init__.py
    │       │   ├── context.py
    │       │   ├── dependencies.py
    │       │   ├── elicitation.py
    │       │   ├── http.py
    │       │   ├── low_level.py
    │       │   ├── openapi.py
    │       │   ├── proxy.py
    │       │   ├── server.py
    │       │   ├── auth/
    │       │   │   ├── __init__.py
    │       │   │   ├── auth.py
    │       │   │   ├── jwt_issuer.py
    │       │   │   ├── middleware.py
    │       │   │   ├── oauth_proxy.py
    │       │   │   ├── oidc_proxy.py
    │       │   │   ├── redirect_validation.py
    │       │   │   ├── handlers/
    │       │   │   │   └── authorize.py
    │       │   │   └── providers/
    │       │   │       ├── __init__.py
    │       │   │       ├── auth0.py
    │       │   │       ├── aws.py
    │       │   │       ├── azure.py
    │       │   │       ├── bearer.py
    │       │   │       ├── descope.py
    │       │   │       ├── github.py
    │       │   │       ├── google.py
    │       │   │       ├── in_memory.py
    │       │   │       ├── introspection.py
    │       │   │       ├── jwt.py
    │       │   │       ├── scalekit.py
    │       │   │       ├── supabase.py
    │       │   │       └── workos.py
    │       │   ├── middleware/
    │       │   │   ├── __init__.py
    │       │   │   ├── caching.py
    │       │   │   ├── error_handling.py
    │       │   │   ├── logging.py
    │       │   │   ├── middleware.py
    │       │   │   ├── rate_limiting.py
    │       │   │   ├── timing.py
    │       │   │   └── tool_injection.py
    │       │   └── sampling/
    │       │       └── handler.py
    │       ├── tools/
    │       │   ├── __init__.py
    │       │   ├── tool.py
    │       │   ├── tool_manager.py
    │       │   └── tool_transform.py
    │       └── utilities/
    │           ├── __init__.py
    │           ├── auth.py
    │           ├── cli.py
    │           ├── components.py
    │           ├── exceptions.py
    │           ├── http.py
    │           ├── inspect.py
    │           ├── json_schema.py
    │           ├── json_schema_type.py
    │           ├── logging.py
    │           ├── mcp_config.py
    │           ├── openapi.py
    │           ├── tests.py
    │           ├── types.py
    │           ├── ui.py
    │           └── mcp_server_config/
    │               ├── __init__.py
    │               └── v1/
    │                   ├── __init__.py
    │                   ├── mcp_server_config.py
    │                   ├── schema.json
    │                   ├── environments/
    │                   │   ├── __init__.py
    │                   │   ├── base.py
    │                   │   └── uv.py
    │                   └── sources/
    │                       ├── __init__.py
    │                       ├── base.py
    │                       └── filesystem.py
    ├── tests/
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── test_examples.py
    │   ├── test_mcp_config.py
    │   ├── cli/
    │   │   ├── __init__.py
    │   │   ├── test_cli.py
    │   │   ├── test_config.py
    │   │   ├── test_cursor.py
    │   │   ├── test_install.py
    │   │   ├── test_mcp_server_config_integration.py
    │   │   ├── test_mcp_server_config_schema.py
    │   │   ├── test_project_prepare.py
    │   │   ├── test_run.py
    │   │   ├── test_run_config.py
    │   │   ├── test_server_args.py
    │   │   ├── test_shared.py
    │   │   └── test_with_argv.py
    │   ├── client/
    │   │   ├── __init__.py
    │   │   ├── test_client.py
    │   │   ├── test_elicitation.py
    │   │   ├── test_logs.py
    │   │   ├── test_notifications.py
    │   │   ├── test_oauth_callback_xss.py
    │   │   ├── test_openapi_experimental.py
    │   │   ├── test_openapi_legacy.py
    │   │   ├── test_progress.py
    │   │   ├── test_roots.py
    │   │   ├── test_sampling.py
    │   │   ├── test_sse.py
    │   │   ├── test_stdio.py
    │   │   ├── test_streamable_http.py
    │   │   ├── auth/
    │   │   │   ├── __init__.py
    │   │   │   └── test_oauth_client.py
    │   │   └── transports/
    │   │       ├── __init__.py
    │   │       └── test_uv_transport.py
    │   ├── contrib/
    │   │   ├── __init__.py
    │   │   ├── test_bulk_tool_caller.py
    │   │   ├── test_component_manager.py
    │   │   └── test_mcp_mixin.py
    │   ├── deprecated/
    │   │   ├── __init__.py
    │   │   ├── test_bearer_auth_provider.py
    │   │   ├── test_dependencies.py
    │   │   ├── test_deprecated.py
    │   │   ├── test_mount_import_arg_order.py
    │   │   ├── test_mount_separators.py
    │   │   ├── test_output_schema_false.py
    │   │   ├── test_proxy_client.py
    │   │   ├── test_resource_prefixes.py
    │   │   ├── test_route_type_ignore.py
    │   │   └── test_settings.py
    │   ├── experimental/
    │   │   ├── README.md
    │   │   ├── __init__.py
    │   │   ├── openapi_parser/
    │   │   │   ├── README.md
    │   │   │   ├── __init__.py
    │   │   │   ├── conftest.py
    │   │   │   ├── server/
    │   │   │   │   ├── __init__.py
    │   │   │   │   └── openapi/
    │   │   │   │       ├── __init__.py
    │   │   │   │       ├── test_comprehensive.py
    │   │   │   │       ├── test_deepobject_style.py
    │   │   │   │       ├── test_end_to_end_compatibility.py
    │   │   │   │       ├── test_openapi_features.py
    │   │   │   │       ├── test_openapi_performance.py
    │   │   │   │       ├── test_parameter_collisions.py
    │   │   │   │       ├── test_performance_comparison.py
    │   │   │   │       └── test_server.py
    │   │   │   └── utilities/
    │   │   │       ├── __init__.py
    │   │   │       └── openapi/
    │   │   │           ├── __init__.py
    │   │   │           ├── conftest.py
    │   │   │           ├── test_allof_requestbody.py
    │   │   │           ├── test_direct_array_schemas.py
    │   │   │           ├── test_director.py
    │   │   │           ├── test_legacy_compatibility.py
    │   │   │           ├── test_models.py
    │   │   │           ├── test_nullable_fields.py
    │   │   │           ├── test_parser.py
    │   │   │           ├── test_schemas.py
    │   │   │           └── test_transitive_references.py
    │   │   └── sampling/
    │   │       └── test_openai_handler.py
    │   ├── integration_tests/
    │   │   ├── __init__.py
    │   │   ├── conftest.py
    │   │   ├── test_github_mcp_remote.py
    │   │   └── auth/
    │   │       ├── __init__.py
    │   │       └── test_github_provider_integration.py
    │   ├── prompts/
    │   │   ├── __init__.py
    │   │   ├── test_prompt.py
    │   │   └── test_prompt_manager.py
    │   ├── resources/
    │   │   ├── __init__.py
    │   │   ├── test_file_resources.py
    │   │   ├── test_function_resources.py
    │   │   ├── test_resource_manager.py
    │   │   ├── test_resource_template.py
    │   │   ├── test_resource_template_meta.py
    │   │   └── test_resources.py
    │   ├── server/
    │   │   ├── __init__.py
    │   │   ├── test_app_state.py
    │   │   ├── test_auth_integration.py
    │   │   ├── test_context.py
    │   │   ├── test_experimental_openapi_feature_flag.py
    │   │   ├── test_file_server.py
    │   │   ├── test_icons.py
    │   │   ├── test_import_server.py
    │   │   ├── test_input_validation.py
    │   │   ├── test_log_level.py
    │   │   ├── test_logging.py
    │   │   ├── test_mount.py
    │   │   ├── test_resource_prefix_formats.py
    │   │   ├── test_run_server.py
    │   │   ├── test_server.py
    │   │   ├── test_server_interactions.py
    │   │   ├── test_server_lifespan.py
    │   │   ├── test_streamable_http_no_redirect.py
    │   │   ├── test_tool_annotations.py
    │   │   ├── test_tool_exclude_args.py
    │   │   ├── test_tool_transformation.py
    │   │   ├── auth/
    │   │   │   ├── __init__.py
    │   │   │   ├── test_auth_provider.py
    │   │   │   ├── test_enhanced_error_responses.py
    │   │   │   ├── test_jwt_issuer.py
    │   │   │   ├── test_jwt_provider.py
    │   │   │   ├── test_oauth_consent_flow.py
    │   │   │   ├── test_oauth_mounting.py
    │   │   │   ├── test_oauth_proxy.py
    │   │   │   ├── test_oauth_proxy_redirect_validation.py
    │   │   │   ├── test_oauth_proxy_storage.py
    │   │   │   ├── test_oidc_proxy.py
    │   │   │   ├── test_redirect_validation.py
    │   │   │   ├── test_remote_auth_provider.py
    │   │   │   ├── test_static_token_verifier.py
    │   │   │   └── providers/
    │   │   │       ├── __init__.py
    │   │   │       ├── test_auth0.py
    │   │   │       ├── test_aws.py
    │   │   │       ├── test_azure.py
    │   │   │       ├── test_descope.py
    │   │   │       ├── test_github.py
    │   │   │       ├── test_google.py
    │   │   │       ├── test_introspection.py
    │   │   │       ├── test_scalekit.py
    │   │   │       ├── test_supabase.py
    │   │   │       └── test_workos.py
    │   │   ├── http/
    │   │   │   ├── __init__.py
    │   │   │   ├── test_bearer_auth_backend.py
    │   │   │   ├── test_custom_routes.py
    │   │   │   ├── test_http_auth_middleware.py
    │   │   │   ├── test_http_dependencies.py
    │   │   │   └── test_http_middleware.py
    │   │   ├── middleware/
    │   │   │   ├── __init__.py
    │   │   │   ├── test_caching.py
    │   │   │   ├── test_error_handling.py
    │   │   │   ├── test_initialization_middleware.py
    │   │   │   ├── test_logging.py
    │   │   │   ├── test_middleware.py
    │   │   │   ├── test_rate_limiting.py
    │   │   │   ├── test_timing.py
    │   │   │   └── test_tool_injection.py
    │   │   ├── openapi/
    │   │   │   ├── __init__.py
    │   │   │   ├── conftest.py
    │   │   │   ├── test_advanced_behavior.py
    │   │   │   ├── test_basic_functionality.py
    │   │   │   ├── test_configuration.py
    │   │   │   ├── test_deepobject_style.py
    │   │   │   ├── test_description_propagation.py
    │   │   │   ├── test_explode_integration.py
    │   │   │   ├── test_openapi_compatibility.py
    │   │   │   ├── test_openapi_path_parameters.py
    │   │   │   ├── test_optional_parameters.py
    │   │   │   ├── test_parameter_collisions.py
    │   │   │   └── test_route_map_fn.py
    │   │   └── proxy/
    │   │       ├── __init__.py
    │   │       ├── test_proxy_client.py
    │   │       ├── test_proxy_server.py
    │   │       └── test_stateful_proxy_client.py
    │   ├── tools/
    │   │   ├── __init__.py
    │   │   ├── test_tool.py
    │   │   ├── test_tool_future_annotations.py
    │   │   ├── test_tool_manager.py
    │   │   └── test_tool_transform.py
    │   └── utilities/
    │       ├── __init__.py
    │       ├── test_cli.py
    │       ├── test_components.py
    │       ├── test_inspect.py
    │       ├── test_json_schema.py
    │       ├── test_json_schema_type.py
    │       ├── test_logging.py
    │       ├── test_tests.py
    │       ├── test_typeadapter.py
    │       ├── test_types.py
    │       └── openapi/
    │           ├── __init__.py
    │           ├── conftest.py
    │           ├── test_nullable_fields.py
    │           ├── test_openapi.py
    │           ├── test_openapi_advanced.py
    │           ├── test_openapi_fastapi.py
    │           └── test_openapi_output_schemas.py
    ├── .cursor/
    │   ├── worktrees.json
    │   └── rules/
    │       └── core-mcp-objects.mdc
    └── .github/
        ├── dependabot.yml
        ├── pull_request_template.md
        ├── release.yml
        ├── copilot-instructions.md -> AGENTS.md
        ├── ISSUE_TEMPLATE/
        │   ├── bug.yml
        │   ├── config.yml
        │   └── enhancement.yml
        └── workflows/
            ├── auto-close-duplicates.yml
            ├── auto-close-needs-mre.yml
            ├── martian-issue-triage.yml
            ├── marvin-dedupe-issues.yml
            ├── marvin-label-triage.yml
            ├── marvin.yml
            ├── publish.yml
            ├── run-static.yml
            ├── run-tests.yml
            ├── update-config-schema.yml
            └── update-sdk-docs.yml

```

## Extracted content
================================================
FILE: README.md
================================================
<div align="center">

<!-- omit in toc -->

<picture>
  <source width="550" media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/wordmark-watercolor-waves-dark.png">
  <source width="550" media="(prefers-color-scheme: light)" srcset="docs/assets/brand/wordmark-watercolor-waves.png">
  <img width="550" alt="FastMCP Logo" src="docs/assets/brand/wordmark-watercolor-waves.png">
</picture>

# FastMCP v2 🚀

<strong>The fast, Pythonic way to build MCP servers and clients.</strong>

*Made with ☕️ by [Prefect](https://www.prefect.io/)*

[![Docs](https://img.shields.io/badge/docs-gofastmcp.com-blue)](https://gofastmcp.com)
[![Discord](https://img.shields.io/badge/community-discord-5865F2?logo=discord&logoColor=white)](https://discord.gg/uu8dJCgttd)
[![PyPI - Version](https://img.shields.io/pypi/v/fastmcp.svg)](https://pypi.org/project/fastmcp)
[![Tests](https://github.com/jlowin/fastmcp/actions/workflows/run-tests.yml/badge.svg)](https://github.com/jlowin/fastmcp/actions/workflows/run-tests.yml)
[![License](https://img.shields.io/github/license/jlowin/fastmcp.svg)](https://github.com/jlowin/fastmcp/blob/main/LICENSE)

<a href="https://trendshift.io/repositories/13266" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13266" alt="jlowin%2Ffastmcp | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

> [!Note]
>
> #### FastMCP 2.0: The Standard Framework
>
> FastMCP pioneered Python MCP development, and FastMCP 1.0 was incorporated into the [official MCP SDK](https://github.com/modelcontextprotocol/python-sdk) in 2024.
>
> **This is FastMCP 2.0** — the actively maintained, production-ready framework that extends far beyond basic protocol implementation. While the SDK provides core functionality, FastMCP 2.0 delivers everything needed for production: advanced MCP patterns (server composition, proxying, OpenAPI/FastAPI generation, tool transformation), enterprise auth (Google, GitHub, WorkOS, Azure, Auth0, and more), deployment tools, testing utilities, and comprehensive client libraries.
>
> **For production MCP applications, install FastMCP:** `pip install fastmcp`

---

**FastMCP is the standard framework for building MCP applications**, providing the fastest path from idea to production.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is a standardized way to provide context and tools to LLMs. FastMCP makes building production-ready MCP servers simple, with enterprise auth, deployment tools, and a complete ecosystem built in.

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

Run the server locally:

```bash
fastmcp run server.py
```

### 📚 Documentation

FastMCP's complete documentation is available at **[gofastmcp.com](https://gofastmcp.com)**, including detailed guides, API references, and advanced patterns. This readme provides only a high-level overview.

Documentation is also available in [llms.txt format](https://llmstxt.org/), which is a simple markdown standard that LLMs can consume easily.

There are two ways to access the LLM-friendly documentation:

- [`llms.txt`](https://gofastmcp.com/llms.txt) is essentially a sitemap, listing all the pages in the documentation.
- [`llms-full.txt`](https://gofastmcp.com/llms-full.txt) contains the entire documentation. Note this may exceed the context window of your LLM.

**Community:** Join our [Discord server](https://discord.gg/uu8dJCgttd) to connect with other FastMCP developers and share what you're building.

---

<!-- omit in toc -->
## Table of Contents

- [FastMCP v2 🚀](#fastmcp-v2-)
  - [📚 Documentation](#-documentation)
  - [What is MCP?](#what-is-mcp)
  - [Why FastMCP?](#why-fastmcp)
  - [Installation](#installation)
  - [Core Concepts](#core-concepts)
    - [The `FastMCP` Server](#the-fastmcp-server)
    - [Tools](#tools)
    - [Resources \& Templates](#resources--templates)
    - [Prompts](#prompts)
    - [Context](#context)
    - [MCP Clients](#mcp-clients)
  - [Authentication](#authentication)
    - [Enterprise Authentication, Zero Configuration](#enterprise-authentication-zero-configuration)
  - [Deployment](#deployment)
    - [From Development to Production](#from-development-to-production)
  - [Advanced Features](#advanced-features)
    - [Proxy Servers](#proxy-servers)
    - [Composing MCP Servers](#composing-mcp-servers)
    - [OpenAPI \& FastAPI Generation](#openapi--fastapi-generation)
  - [Running Your Server](#running-your-server)
  - [Contributing](#contributing)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Unit Tests](#unit-tests)
    - [Static Checks](#static-checks)
    - [Pull Requests](#pull-requests)

---

## What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) lets you build servers that expose data and functionality to LLM applications in a secure, standardized way. It is often described as "the USB-C port for AI", providing a uniform way to connect LLMs to resources they can use. It may be easier to think of it as an API, but specifically designed for LLM interactions. MCP servers can:

- Expose data through **Resources** (think of these sort of like GET endpoints; they are used to load information into the LLM's context)
- Provide functionality through **Tools** (sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
- Define interaction patterns through **Prompts** (reusable templates for LLM interactions)
- And more!

FastMCP provides a high-level, Pythonic interface for building, managing, and interacting with these servers.

## Why FastMCP?

FastMCP handles all the complex protocol details so you can focus on building. In most cases, decorating a Python function is all you need — FastMCP handles the rest.

🚀 **Fast:** High-level interface means less code and faster development

🍀 **Simple:** Build MCP servers with minimal boilerplate

🐍 **Pythonic:** Feels natural to Python developers

🔍 **Complete:** Everything for production — enterprise auth (Google, GitHub, Azure, Auth0, WorkOS), deployment tools, testing frameworks, client libraries, and more

FastMCP provides the shortest path from idea to production. Deploy locally, to the cloud with [FastMCP Cloud](https://fastmcp.cloud), or to your own infrastructure.

## Installation

We recommend installing FastMCP with [uv](https://docs.astral.sh/uv/):

```bash
uv pip install fastmcp
```

For full installation instructions, including verification, upgrading from the official MCPSDK, and developer setup, see the [**Installation Guide**](https://gofastmcp.com/getting-started/installation).

## Core Concepts

These are the building blocks for creating MCP servers and clients with FastMCP.

### The `FastMCP` Server

The central object representing your MCP application. It holds your tools, resources, and prompts, manages connections, and can be configured with settings like authentication.

```python
from fastmcp import FastMCP

# Create a server instance
mcp = FastMCP(name="MyAssistantServer")
```

Learn more in the [**FastMCP Server Documentation**](https://gofastmcp.com/servers/fastmcp).

### Tools

Tools allow LLMs to perform actions by executing your Python functions (sync or async). Ideal for computations, API calls, or side effects (like `POST`/`PUT`). FastMCP handles schema generation from type hints and docstrings. Tools can return various types, including text, JSON-serializable objects, and even images or audio aided by the FastMCP media helper classes.

```python
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b
```

Learn more in the [**Tools Documentation**](https://gofastmcp.com/servers/tools).

### Resources & Templates

Resources expose read-only data sources (like `GET` requests). Use `@mcp.resource("your://uri")`. Use `{placeholders}` in the URI to create dynamic templates that accept parameters, allowing clients to request specific data subsets.

```python
# Static resource
@mcp.resource("config://version")
def get_version(): 
    return "2.0.1"

# Dynamic resource template
@mcp.resource("users://{user_id}/profile")
def get_profile(user_id: int):
    # Fetch profile for user_id...
    return {"name": f"User {user_id}", "status": "active"}
```

Learn more in the [**Resources & Templates Documentation**](https://gofastmcp.com/servers/resources).

### Prompts

Prompts define reusable message templates to guide LLM interactions. Decorate functions with `@mcp.prompt`. Return strings or `Message` objects.

```python
@mcp.prompt
def summarize_request(text: str) -> str:
    """Generate a prompt asking for a summary."""
    return f"Please summarize the following text:\n\n{text}"
```

Learn more in the [**Prompts Documentation**](https://gofastmcp.com/servers/prompts).

### Context

Access MCP session capabilities within your tools, resources, or prompts by adding a `ctx: Context` parameter. Context provides methods for:

- **Logging:** Log messages to MCP clients with `ctx.info()`, `ctx.error()`, etc.
- **LLM Sampling:** Use `ctx.sample()` to request completions from the client's LLM.
- **Resource Access:** Use `ctx.read_resource()` to access resources on the server
- **Progress Reporting:** Use `ctx.report_progress()` to report progress to the client.
- and more...

To access the context, add a parameter annotated as `Context` to any mcp-decorated function. FastMCP will automatically inject the correct context object when the function is called.

```python
from fastmcp import FastMCP, Context

mcp = FastMCP("My MCP Server")

@mcp.tool
async def process_data(uri: str, ctx: Context):
    # Log a message to the client
    await ctx.info(f"Processing {uri}...")

    # Read a resource from the server
    data = await ctx.read_resource(uri)

    # Ask client LLM to summarize the data
    summary = await ctx.sample(f"Summarize: {data.content[:500]}")

    # Return the summary
    return summary.text
```

Learn more in the [**Context Documentation**](https://gofastmcp.com/servers/context).

### MCP Clients

Interact with *any* MCP server programmatically using the `fastmcp.Client`. It supports various transports (Stdio, SSE, In-Memory) and often auto-detects the correct one. The client can also handle advanced patterns like server-initiated **LLM sampling requests** if you provide an appropriate handler.

Critically, the client allows for efficient **in-memory testing** of your servers by connecting directly to a `FastMCP` server instance via the `FastMCPTransport`, eliminating the need for process management or network calls during tests.

```python
from fastmcp import Client

async def main():
    # Connect via stdio to a local script
    async with Client("my_server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"Result: {result.content[0].text}")

    # Connect via SSE
    async with Client("http://localhost:8000/sse") as client:
        # ... use the client
        pass
```

To use clients to test servers, use the following pattern:

```python
from fastmcp import FastMCP, Client

mcp = FastMCP("My MCP Server")

async def main():
    # Connect via in-memory transport
    async with Client(mcp) as client:
        # ... use the client
```

FastMCP also supports connecting to multiple servers through a single unified client using the standard MCP configuration format:

```python
from fastmcp import Client

# Standard MCP configuration with multiple servers
config = {
    "mcpServers": {
        "weather": {"url": "https://weather-api.example.com/mcp"},
        "assistant": {"command": "python", "args": ["./assistant_server.py"]}
    }
}

# Create a client that connects to all servers
client = Client(config)

async def main():
    async with client:
        # Access tools and resources with server prefixes
        forecast = await client.call_tool("weather_get_forecast", {"city": "London"})
        answer = await client.call_tool("assistant_answer_question", {"query": "What is MCP?"})
```

Learn more in the [**Client Documentation**](https://gofastmcp.com/clients/client) and [**Transports Documentation**](https://gofastmcp.com/clients/transports).

## Authentication

### Enterprise Authentication, Zero Configuration

FastMCP provides comprehensive authentication support that sets it apart from basic MCP implementations. Secure your servers and authenticate your clients with the same enterprise-grade providers used by major corporations.

**Built-in OAuth Providers:**

- **Google**
- **GitHub**
- **Microsoft Azure**
- **Auth0**
- **WorkOS**
- **Descope**
- **JWT/Custom**
- **API Keys**

Protecting a server takes just two lines:

```python
from fastmcp.server.auth.providers.google import GoogleProvider

auth = GoogleProvider(client_id="...", client_secret="...", base_url="https://myserver.com")
mcp = FastMCP("Protected Server", auth=auth)
```

Connecting to protected servers is even simpler:

```python
async with Client("https://protected-server.com/mcp", auth="oauth") as client:
    # Automatic browser-based OAuth flow
    result = await client.call_tool("protected_tool")
```

**Why FastMCP Auth Matters:**

- **Production-Ready:** Persistent storage, token refresh, comprehensive error handling
- **Zero-Config OAuth:** Just pass `auth="oauth"` for automatic setup
- **Enterprise Integration:** WorkOS SSO, Azure Active Directory, Auth0 tenants
- **Developer Experience:** Automatic browser launch, local callback server, environment variable support
- **Advanced Architecture:** Full OIDC support, Dynamic Client Registration (DCR), and unique OAuth proxy pattern that enables DCR with any provider

*Authentication this comprehensive is unique to FastMCP 2.0.*

Learn more in the **Authentication Documentation** for [servers](https://gofastmcp.com/servers/auth) and [clients](https://gofastmcp.com/clients/auth).

## Deployment

### From Development to Production

FastMCP supports every deployment scenario from local development to global scale:

**Development:** Run locally with a single command

```bash
fastmcp run server.py
```

**Production:** Deploy to [**FastMCP Cloud**](https://fastmcp.cloud) — Remote MCP that just works

- Instant HTTPS endpoints
- Built-in authentication
- Zero configuration
- Free for personal servers

**Self-Hosted:** Use HTTP or SSE transports for your own infrastructure

```python
mcp.run(transport="http", host="0.0.0.0", port=8000)
```

Learn more in the [**Deployment Documentation**](https://gofastmcp.com/deployment).

## Advanced Features

FastMCP introduces powerful ways to structure and compose your MCP applications.

### Proxy Servers

Create a FastMCP server that acts as an intermediary for another local or remote MCP server using `FastMCP.as_proxy()`. This is especially useful for bridging transports (e.g., remote SSE to local Stdio) or adding a layer of logic to a server you don't control.

Learn more in the [**Proxying Documentation**](https://gofastmcp.com/patterns/proxy).

### Composing MCP Servers

Build modular applications by mounting multiple `FastMCP` instances onto a parent server using `mcp.mount()` (live link) or `mcp.import_server()` (static copy).

Learn more in the [**Composition Documentation**](https://gofastmcp.com/patterns/composition).

### OpenAPI & FastAPI Generation

Automatically generate FastMCP servers from existing OpenAPI specifications (`FastMCP.from_openapi()`) or FastAPI applications (`FastMCP.from_fastapi()`), instantly bringing your web APIs to the MCP ecosystem.

Learn more: [**OpenAPI Integration**](https://gofastmcp.com/integrations/openapi) | [**FastAPI Integration**](https://gofastmcp.com/integrations/fastapi).

## Running Your Server

The main way to run a FastMCP server is by calling the `run()` method on your server instance:

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()  # Default: uses STDIO transport
```

FastMCP supports three transport protocols:

**STDIO (Default)**: Best for local tools and command-line scripts.

```python
mcp.run(transport="stdio")  # Default, so transport argument is optional
```

**Streamable HTTP**: Recommended for web deployments.

```python
mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")
```

**SSE**: For compatibility with existing SSE clients.

```python
mcp.run(transport="sse", host="127.0.0.1", port=8000)
```

See the [**Running Server Documentation**](https://gofastmcp.com/deployment/running-server) for more details.

## Contributing

Contributions are the core of open source! We welcome improvements and features.

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (Recommended for environment management)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jlowin/fastmcp.git 
   cd fastmcp
   ```

2. Create and sync the environment:

   ```bash
   uv sync
   ```

   This installs all dependencies, including dev tools.

3. Activate the virtual environment (e.g., `source .venv/bin/activate` or via your IDE).

### Unit Tests

FastMCP has a comprehensive unit test suite. All PRs must introduce or update tests as appropriate and pass the full suite.

Run tests using pytest:

```bash
pytest
```

or if you want an overview of the code coverage

```bash
uv run pytest --cov=src --cov=examples --cov-report=html
```

### Static Checks

FastMCP uses `pre-commit` for code formatting, linting, and type-checking. All PRs must pass these checks (they run automatically in CI).

Install the hooks locally:

```bash
uv run pre-commit install
```

The hooks will now run automatically on `git commit`. You can also run them manually at any time:

```bash
pre-commit run --all-files
# or via uv
uv run pre-commit run --all-files
```

### Pull Requests

1. Fork the repository on GitHub.
2. Create a feature branch from `main`.
3. Make your changes, including tests and documentation updates.
4. Ensure tests and pre-commit hooks pass.
5. Commit your changes and push to your fork.
6. Open a pull request against the `main` branch of `jlowin/fastmcp`.

Please open an issue or discussion for questions or suggestions before starting significant work!



================================================
FILE: AGENTS.md
================================================
# FastMCP Development Guidelines

> **Audience**: LLM-driven engineering agents and human developers

FastMCP is a comprehensive Python framework (Python ≥3.10) for building Model Context Protocol (MCP) servers and clients. This is the actively maintained v2.0 providing a complete toolkit for the MCP ecosystem.

## Required Development Workflow

**CRITICAL**: Always run these commands in sequence before committing:

```bash
uv sync                              # Install dependencies
uv run pre-commit run --all-files    # Ruff + Prettier + ty
uv run pytest                        # Run full test suite
```

**All three must pass** - this is enforced by CI. Alternative: `just build && just typecheck && just test`

**Tests must pass and lint/typing must be clean before committing.**

## Repository Structure

| Path               | Purpose                                             |
| ------------------ | --------------------------------------------------- |
| `src/fastmcp/`     | Library source code (Python ≥ 3.10)                 |
| `├─server/`        | Server implementation, `FastMCP`, auth, networking  |
| `│  ├─auth/`       | Authentication providers (Google, GitHub, Azure, AWS, WorkOS, Auth0, JWT, and more) |
| `│  └─middleware/` | Error handling, logging, rate limiting              |
| `├─client/`        | High-level client SDK + transports                  |
| `│  └─auth/`       | Client authentication (Bearer, OAuth)               |
| `├─tools/`         | Tool implementations + `ToolManager`                |
| `├─resources/`     | Resources, templates + `ResourceManager`            |
| `├─prompts/`       | Prompt templates + `PromptManager`                  |
| `├─cli/`           | FastMCP CLI commands (`run`, `dev`, `install`)      |
| `├─contrib/`       | Community contributions (bulk caller, mixins)       |
| `├─experimental/`  | Experimental features (new OpenAPI parser)          |
| `└─utilities/`     | Shared utilities (logging, JSON schema, HTTP)       |
| `tests/`           | Comprehensive pytest suite with markers             |
| `docs/`            | Mintlify documentation (published to gofastmcp.com) |
| `examples/`        | Runnable demo servers (echo, smart_home, atproto)   |

## Core MCP Objects

When modifying MCP functionality, changes typically need to be applied across all object types:

- **Tools** (`src/tools/` + `ToolManager`)
- **Resources** (`src/resources/` + `ResourceManager`)
- **Resource Templates** (`src/resources/` + `ResourceManager`)
- **Prompts** (`src/prompts/` + `PromptManager`)

## Writing Style

- Be brief and to the point. Do not regurgitate information that can easily be gleaned from the code, except to guide the reader to where the code is located.
- **NEVER** use "This isn't..." or "not just..." constructions. State what something IS directly. Avoid defensive writing patterns like:
  - "This isn't X, it's Y" or "Not just X, but Y" → Just say "This is Y"
  - "Not just about X" → State the actual purpose
  - "We're not doing X, we're doing Y" → Just explain what you're doing
  - Any variation of explaining what something isn't before what it is

## Testing Best Practices

### Testing Standards

- Every test: atomic, self-contained, single functionality
- Use parameterization for multiple examples of same functionality
- Use separate tests for different functionality pieces
- **ALWAYS** Put imports at the top of the file, not in the test body
- **NEVER** add `@pytest.mark.asyncio` to tests - `asyncio_mode = "auto"` is set globally
- **ALWAYS** run pytest after significant changes

### Inline Snapshots

FastMCP uses `inline-snapshot` for testing complex data structures. On first run with empty `snapshot()`, pytest will auto-populate the expected value when running `pytest --inline-snapshot=create`. To update snapshots after intentional changes, run `pytest --inline-snapshot=fix`. This is particularly useful for testing JSON schemas and API responses.

### Always Use In-Memory Transport

Pass FastMCP servers directly to clients for testing:

```python
mcp = FastMCP("TestServer")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Direct connection - no network complexity
async with Client(mcp) as client:
    result = await client.call_tool("greet", {"name": "World"})
```

Only use HTTP transport when explicitly testing network features:

```python
# Network testing on

[... Content truncated due to length ...]

</details>

<details>
<summary>Repository analysis for https://github.com/modelcontextprotocol/modelcontextprotocol</summary>

# Repository analysis for https://github.com/modelcontextprotocol/modelcontextprotocol

## Summary
Repository: modelcontextprotocol/modelcontextprotocol
Files analyzed: 168

Estimated tokens: 556.8k

## File tree
```Directory structure:
└── modelcontextprotocol-modelcontextprotocol/
    ├── README.md
    ├── ANTITRUST.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── MAINTAINERS.md
    ├── package.json
    ├── SECURITY.md
    ├── tsconfig.json
    ├── typedoc.config.mjs
    ├── typedoc.plugin.mjs
    ├── .npmrc
    ├── .nvmrc
    ├── .prettierignore
    ├── blog/
    │   ├── go.mod
    │   ├── go.sum
    │   ├── hugo.toml
    │   ├── archetypes/
    │   │   └── default.md
    │   ├── assets/
    │   │   └── css/
    │   │       └── extended/
    │   │           └── custom.css
    │   ├── content/
    │   │   ├── _index.md
    │   │   └── posts/
    │   │       ├── 2025-07-29-prompts-for-automation.md
    │   │       ├── 2025-07-31-governance-for-mcp.md
    │   │       ├── 2025-09-05-php-sdk.md
    │   │       ├── 2025-09-08-mcp-registry-preview.md
    │   │       ├── 2025-09-26-mcp-next-version-update.md
    │   │       ├── welcome-to-mcp-blog.md
    │   │       └── client_registration/
    │   │           └── index.md
    │   ├── layouts/
    │   │   ├── baseof.html
    │   │   ├── _markup/
    │   │   │   └── render-codeblock-mermaid.html
    │   │   └── partials/
    │   │       └── google_analytics.html
    │   └── static/
    │       └── CNAME
    ├── docs/
    │   ├── clients.mdx
    │   ├── docs.json
    │   ├── examples.mdx
    │   ├── faqs.mdx
    │   ├── style.css
    │   ├── about/
    │   │   └── index.mdx
    │   ├── community/
    │   │   ├── antitrust.mdx
    │   │   ├── communication.mdx
    │   │   ├── governance.mdx
    │   │   ├── sep-guidelines.mdx
    │   │   └── working-interest-groups.mdx
    │   ├── development/
    │   │   └── roadmap.mdx
    │   ├── docs/
    │   │   ├── sdk.mdx
    │   │   ├── develop/
    │   │   │   ├── build-client.mdx
    │   │   │   ├── build-server.mdx
    │   │   │   ├── connect-local-servers.mdx
    │   │   │   └── connect-remote-servers.mdx
    │   │   ├── getting-started/
    │   │   │   └── intro.mdx
    │   │   ├── learn/
    │   │   │   ├── architecture.mdx
    │   │   │   ├── client-concepts.mdx
    │   │   │   └── server-concepts.mdx
    │   │   ├── reference/
    │   │   │   ├── client.mdx
    │   │   │   └── server.mdx
    │   │   ├── tools/
    │   │   │   └── inspector.mdx
    │   │   └── tutorials/
    │   │       ├── use-local-mcp-server.mdx
    │   │       └── security/
    │   │           └── authorization.mdx
    │   ├── images/
    │   │   └── java/
    │   │       └── class-diagrams.puml
    │   ├── legacy/
    │   │   ├── concepts/
    │   │   │   ├── architecture.mdx
    │   │   │   ├── elicitation.mdx
    │   │   │   ├── prompts.mdx
    │   │   │   ├── resources.mdx
    │   │   │   ├── roots.mdx
    │   │   │   ├── sampling.mdx
    │   │   │   ├── tools.mdx
    │   │   │   └── transports.mdx
    │   │   └── tools/
    │   │       └── debugging.mdx
    │   ├── sdk/
    │   │   └── java/
    │   │       ├── mcp-client.mdx
    │   │       ├── mcp-overview.mdx
    │   │       └── mcp-server.mdx
    │   ├── snippets/
    │   │   └── snippet-intro.mdx
    │   ├── specification/
    │   │   ├── versioning.mdx
    │   │   ├── 2024-11-05/
    │   │   │   ├── index.mdx
    │   │   │   ├── architecture/
    │   │   │   │   └── index.mdx
    │   │   │   ├── basic/
    │   │   │   │   ├── index.mdx
    │   │   │   │   ├── lifecycle.mdx
    │   │   │   │   ├── messages.mdx
    │   │   │   │   ├── transports.mdx
    │   │   │   │   └── utilities/
    │   │   │   │       ├── cancellation.mdx
    │   │   │   │       ├── ping.mdx
    │   │   │   │       └── progress.mdx
    │   │   │   ├── client/
    │   │   │   │   ├── roots.mdx
    │   │   │   │   └── sampling.mdx
    │   │   │   └── server/
    │   │   │       ├── index.mdx
    │   │   │       ├── prompts.mdx
    │   │   │       ├── resources.mdx
    │   │   │       ├── tools.mdx
    │   │   │       └── utilities/
    │   │   │           ├── completion.mdx
    │   │   │           ├── logging.mdx
    │   │   │           └── pagination.mdx
    │   │   ├── 2025-03-26/
    │   │   │   ├── changelog.mdx
    │   │   │   ├── index.mdx
    │   │   │   ├── architecture/
    │   │   │   │   └── index.mdx
    │   │   │   ├── basic/
    │   │   │   │   ├── authorization.mdx
    │   │   │   │   ├── index.mdx
    │   │   │   │   ├── lifecycle.mdx
    │   │   │   │   ├── transports.mdx
    │   │   │   │   └── utilities/
    │   │   │   │       ├── cancellation.mdx
    │   │   │   │       ├── ping.mdx
    │   │   │   │       └── progress.mdx
    │   │   │   ├── client/
    │   │   │   │   ├── roots.mdx
    │   │   │   │   └── sampling.mdx
    │   │   │   └── server/
    │   │   │       ├── index.mdx
    │   │   │       ├── prompts.mdx
    │   │   │       ├── resources.mdx
    │   │   │       ├── tools.mdx
    │   │   │       └── utilities/
    │   │   │           ├── completion.mdx
    │   │   │           ├── logging.mdx
    │   │   │           └── pagination.mdx
    │   │   ├── 2025-06-18/
    │   │   │   ├── changelog.mdx
    │   │   │   ├── index.mdx
    │   │   │   ├── schema.mdx
    │   │   │   ├── architecture/
    │   │   │   │   └── index.mdx
    │   │   │   ├── basic/
    │   │   │   │   ├── authorization.mdx
    │   │   │   │   ├── index.mdx
    │   │   │   │   ├── lifecycle.mdx
    │   │   │   │   ├── security_best_practices.mdx
    │   │   │   │   ├── transports.mdx
    │   │   │   │   └── utilities/
    │   │   │   │       ├── cancellation.mdx
    │   │   │   │       ├── ping.mdx
    │   │   │   │       └── progress.mdx
    │   │   │   ├── client/
    │   │   │   │   ├── elicitation.mdx
    │   │   │   │   ├── roots.mdx
    │   │   │   │   └── sampling.mdx
    │   │   │   └── server/
    │   │   │       ├── index.mdx
    │   │   │       ├── prompts.mdx
    │   │   │       ├── resources.mdx
    │   │   │       ├── tools.mdx
    │   │   │       └── utilities/
    │   │   │           ├── completion.mdx
    │   │   │           ├── logging.mdx
    │   │   │           └── pagination.mdx
    │   │   └── draft/
    │   │       ├── changelog.mdx
    │   │       ├── index.mdx
    │   │       ├── schema.mdx
    │   │       ├── architecture/
    │   │       │   └── index.mdx
    │   │       ├── basic/
    │   │       │   ├── authorization.mdx
    │   │       │   ├── index.mdx
    │   │       │   ├── lifecycle.mdx
    │   │       │   ├── security_best_practices.mdx
    │   │       │   ├── transports.mdx
    │   │       │   └── utilities/
    │   │       │       ├── cancellation.mdx
    │   │       │       ├── ping.mdx
    │   │       │       └── progress.mdx
    │   │       ├── client/
    │   │       │   ├── elicitation.mdx
    │   │       │   ├── roots.mdx
    │   │       │   └── sampling.mdx
    │   │       └── server/
    │   │           ├── index.mdx
    │   │           ├── prompts.mdx
    │   │           ├── resources.mdx
    │   │           ├── tools.mdx
    │   │           └── utilities/
    │   │               ├── completion.mdx
    │   │               ├── logging.mdx
    │   │               └── pagination.mdx
    │   ├── tutorials/
    │   │   ├── building-a-client-node.mdx
    │   │   └── building-mcp-with-llms.mdx
    │   └── .well-known/
    │       └── security.txt
    ├── schema/
    │   ├── 2024-11-05/
    │   │   ├── schema.json
    │   │   └── schema.ts
    │   ├── 2025-03-26/
    │   │   ├── schema.json
    │   │   └── schema.ts
    │   ├── 2025-06-18/
    │   │   ├── schema.json
    │   │   └── schema.ts
    │   └── draft/
    │       ├── schema.json
    │       └── schema.ts
    └── .github/
        ├── CODEOWNERS
        └── workflows/
            ├── deploy-blog.yml
            ├── main.yml
            └── markdown-format.yml

```

## Extracted content
================================================
FILE: README.md
================================================
# Model Context Protocol (MCP)

_Just heard of MCP and not sure where to start? See [the documentation website instead](https://modelcontextprotocol.io)._

This repo contains the:

- MCP specification
- MCP protocol schema
- Official MCP documentation

The schema is [defined in TypeScript](schema/2025-06-18/schema.ts) first, but
[made available as JSON Schema](schema/2025-06-18/schema.json) as well, for wider
compatibility.

The official MCP documentation is built using Mintlify and available at
[modelcontextprotocol.io](https://modelcontextprotocol.io).

## Authors

The Model Context Protocol was created by David Soria Parra ([@dsp](https://github.com/dsp)) and Justin Spahr-Summers ([@jspahrsummers](https://github.com/jspahrsummers)).

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).



================================================
FILE: ANTITRUST.md
================================================
**MCP Project Antitrust Policy**

**Antitrust Policy**

Effective: September 29, 2025

**Introduction**

The goal of the Model Context Protocol open source project (the “Project”) is to develop a universal standard for model-to-world interactions, including enabling LLMs and agents to seamlessly connect with and utilize external data sources and tools. The purpose of this Antitrust Policy (the “Policy”) is to avoid antitrust risks in carrying out this pro-competitive mission.

Participants in and contributors to the Project (collectively, “participants”) will use their best reasonable efforts to comply in all respects with all applicable state and federal antitrust and trade regulation laws, and applicable antitrust/competition laws of other countries (collectively, the “Antitrust Laws”).

The goal of Antitrust Laws is to encourage vigorous competition. Nothing in this Policy prohibits or limits the ability of participants to make, sell or use any product, or otherwise to compete in the marketplace. This Policy provides general guidance on compliance with Antitrust Law. Participants should contact their respective legal counsel to address specific questions.

This Policy is conservative and is intended to promote compliance with the Antitrust Laws, not to create duties or obligations beyond what the Antitrust Laws actually require. In the event of any inconsistency between this Policy and the Antitrust Laws, the Antitrust Laws preempt and control.

**Participation**

Technical participation in the Project shall be open to all, subject only to compliance with the provisions of the Project’s charter and other governance documents.

**Conduct of Meetings**

At meetings among actual or potential competitors, there is a risk that participants in those meetings may improperly disclose or discuss information in violation of the Antitrust Laws or otherwise act in an anti-competitive manner. To avoid this risk, participants must adhere to the following policies when participating in Project-related or sponsored meetings, conference calls, or other forums (collectively, “Project Meetings”).

Participants must not, in fact or appearance, discuss or exchange information regarding:

- An individual company’s current or projected prices, price changes, price differentials, markups, discounts, allowances, terms and conditions of sale, including credit terms, etc., or data that bear on prices, including profits, margins or cost.
- Industry-wide pricing policies, price levels, price changes, differentials, or the like.
- Actual or projected changes in industry production, capacity or inventories.
- Matters relating to bids or intentions to bid for particular products, procedures for responding to bid invitations or specific contractual arrangements.
- Plans of individual companies concerning the design, characteristics, production, distribution, marketing or introduction dates of particular products, including proposed territories or customers.
- Matters relating to actual or potential individual suppliers that might have the effect of excluding them from any market or of influencing the business conduct of firms toward such suppliers.
- Matters relating to actual or potential customers that might have the effect of influencing the business conduct of firms toward such customers.
- Individual company current or projected cost of procurement, development or manufacture of any product.
- Individual company market shares for any product or for all products.
- Confidential or otherwise sensitive business plans or strategy.

In connection with all Project Meetings, participants must do the following:

- Adhere to prepared agendas.
- Insist that meeting minutes be prepared and distributed to all participants, and that meeting minutes accurately reflect the matters that transpired.
- Consult with their respective counsel on all antitrust questions related to Project Meetings.
- Protest against any discussions that appear to violate these policies or the Antitrust Laws, leave any meeting in which such discussions continue, and either insist that such protest be noted in the minutes.

**Requirements/Standard Setting**

The Project may establish standards, technical requirements and/or specifications for use (collectively, “requirements”). Participants shall not enter into agreements that prohibit or restrict any participant from establishing or adopting any other requirements. Participants shall not undertake any efforts, directly or indirectly, to prevent any firm from manufacturing, selling, or supplying any product not conforming to a requirement.

The Project shall not promote standardization of commercial terms, such as terms for license and sale.

**Contact Information**

To contact the Project regarding matters addressed by this Antitrust Policy, please send an email to antitrust@modelcontextprotocol.io, and reference “Antitrust Policy” in the subject line.



================================================
FILE: CODE_OF_CONDUCT.md
================================================
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our community a
harassment-free experience for everyone, regardless of age, body size, visible or
invisible disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal appearance,
race, religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse,
inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our community
include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes, and
  learning from the experience
- Focusing on what is best not just for us as individuals, but for the overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email address, without
  their explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional
  setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in response to
any behavior that they deem inappropriate, threatening, offensive, or harmful.

Community leaders have the right and responsibility to remove, edit, or reject comments,
commits, code, wiki edits, issues, and other contributions that are not aligned to this
Code of Conduct, and will communicate reasons for moderation decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when an
individual is officially representing the community in public spaces. Examples of
representing our community include using an official e-mail address, posting via an
official social media account, or acting as an appointed representative at an online or
offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to
the community leaders responsible for enforcement at mcp-coc@anthropic.com. All
complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the reporter
of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining the
consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing clarity
around the nature of the violation and an explanation of why the behavior was
inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series of actions.

**Consequence**: A warning with consequences for continued behavior. No interaction with
the people involved, including unsolicited interaction with those enforcing the Code of
Conduct, for a specified period of time. This includes avoiding interactions in community
spaces as well as external channels like social media. Violating these terms may lead to
a temporary or permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including sustained
inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public communication
with the community for a specified period of time. No public or private interaction with
the people involved, including unsolicited interaction with those enforcing the Code of
Conduct, is allowed during this period. Violating these terms may lead to a permanent
ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community standards,
including sustained inappropriate behavior, harassment of an individual, or aggression
toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 2.0,
available at https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.



================================================
FILE: CONTRIBUTING.md
================================================
# Contributing to Model Context Protocol

Thank you for your interest in contributing to the Model Context Protocol specification, schemas, or docs!
This document outlines how to contribute to this project.

Also see the [overall MCP communication guidelines in our docs](https://modelcontextprotocol.io/community/communication), which explains how and where discussions about changes happen.

## General prerequisites

The following software is required to work on the spec:

- Node.js 20 or above
- TypeScript
- TypeScript JSON Schema (for generating JSON schema)
- [Mintlify](https://mintlify.com/) (optional, for docs)
- nvm (optional, for managing Node versions)

### Getting Started

1. [Fork the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

2. Clone your fork:

   ```bash
   git clone https://github.com/YOUR-USERNAME/modelcontextprotocol.git
   cd modelcontextprotocol
   ```

3. Install dependencies:

   ```bash
   nvm install  # install correct Node version
   npm install  # install dependencies
   ```

4. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

## Schema changes

Schema changes go in `schema/draft/schema.ts`. To validate your changes, run:

```bash
npm run check:schema:ts
```

`schema/draft/schema.json` and `docs/specification/draft/schema.mdx` are generated from `schema/draft/schema.ts`; do not edit them directly. To generate them, run:

```bash
npm run generate:schema
```

## Documentation changes

Documentation is written in MDX format and in the [`docs`](./docs) directory.

You can preview documentation changes locally by running:

```bash
npm run serve:docs
```

And lint them with:

```bash
npm run check:docs
npm run format
```

## Blog changes

The blog is built using [Hugo](https://gohugo.io/installation/) and located in the [`blog`](./blog) directory.

To preview blog changes locally:

```bash
npm run serve:blog
```

## Documentation Guidelines

When contributing to the documentation:

- Keep content clear, concise, and technically accurate
- Follow the existing file structure and naming conventions
- Include code examples where appropriate
- Use proper MDX formatting and components
- Test all links and code samples
  - You may run `npm run check:docs:links` to look for broken internal links.
- Use appropriate headings: "When to use", "Steps", and "Tips" for tutorials
- Place new pages in appropriate sections (concepts, tutorials, etc.)
- Update `docs.json` when adding new pages
- Follow existing file naming conventions (`kebab-case.mdx`)
- Include proper frontmatter in MDX files

## Specification Proposal Guidelines

### Principles of MCP

1. **Simple + Minimal**: It is much easier to add things to a specification than it is to
   remove them. To maintain simplicity, we keep a high bar for adding new concepts and
   primitives as each addition requires maintenance and compatibility consideration.
2. **Concrete**: Specification changes need to be based on specific implementation
   challenges and not on speculative ideas.

### Stages of a specification proposal

1. **Define**: Explore the problem space, validate that other MCP users face a similar
   issue, and then clearly define the problem.
2. **Prototype**: Build an example solution to the problem and demonstrate its practical
   application.
3. **Write**: Based on the prototype, write a specification proposal.

## Submitting Changes

1. Push your changes to your fork
2. Submit a pull request to the main repository
3. Follow the pull request template
4. Wait for review

## License

By contributing, you agree that your contributions will be licensed under the MIT
License.

## Security

Please review our [Security Policy](SECURITY.md) for reporting security issues.



================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2024–2025 Anthropic, PBC and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: MAINTAINERS.md
================================================
# MCP Maintainers

This document lists current maintainers in the Model Context Protocol project.

**Last updated:** October 15, 2025

## Lead Maintainers

- [David Soria Parra](https://github.com/dsp-ant)
- _[Justin Spahr-Summers](https://github.com/jspahrsummers) (currently inactive)_

## Core Maintainers

- [Inna Harper](https://github.com/ihrpr)
- [Basil Hosmer](https://github.com/bhosmer-ant)
- [Paul Carleton](https://github.com/pcarleton)
- [Nick Cooper](https://github.com/nicknotfun)
- [Nick Aldridge](https://github.com/000-000-000-000-000)
- Che Liu
- [Den Delimarsky](https://github.com/localden)

## SDK Maintainers

### Java SDK

- [Christian Tzolov](https://github.com/tzolov)
- [Dariusz Jędrzejczyk](https://github.com/chemicL)
- [Daniel Garnier-Moiroux](https://github.com/Kehrlann)

### Ruby SDK

- [Topher Bullock](https://github.com/topherbullock)
- [Koichi Ito](https://github.com/koic)
- [Ateş Göral](https://github.com/atesgoral)

### Swift SDK

- [Matt Zmuda](https://github.com/mattt)
- [Carl Peaslee](https://github.com/carlpeaslee)

### Go SDK

- [Rob Findley](https://github.com/findleyr)
- [Jonathan Amsterdam](https://github.com/jba)
- [Sam Thanawalla](https://github.com/samthanawalla)

### C# SDK

- [Stephan Halter](https://github.com/halter73)
- [Mike Kistler](https://github.com/mikekistler)

### Kotlin SDK

- [Leonid Stashevsky](https://github.com/e5l)
- [Sergey Ignatov](https://github.com/ignatov)

### Python SDK

- [Inna Harper](https://github.com/ihrpr)
- [Jerome Swannack](https://github.com/jerome3o)
- [Samuel Colvin](https://github.com/samuelcolvin)
- [Marcelo Trylesinski](https://github.com/Kludex)

### TypeScript SDK

- [Inna Harper](https://github.com/ihrpr)
- [Felix Weinberger](https://github.com/felixweinberger)
- [Olivier Chafik](https://github.com/ochafik)

### Rust SDK

- [Alex Hancock](https://github.com/alexhancock)

### PHP SDK

- [Kyrian Obikwelu](https://github.com/CodeWithKyrian)
- [Christopher Hertel](https://github.com/chr-hertel)

## Project Maintainers

### use-mcp

- [Glen Maddern](https://github.com/geelen)

### Inspector

- [Ola Hungerford](https://github.com/olaservo)
- [Cliff Hall](https://github.com/cliffhall)

### Registry

- [Toby Padilla](https://github.com/toby)
- [Tadas Antanavicius](https://github.com/tadasant)
- [Adam Jones](https://github.com/domdomegg)
- [Radoslav (Rado) Dimitrov](https://github.com/rdimitrov)

### Reference Servers

- [Ola Hungerford](https://github.com/olaservo)
- [Cliff Hall](https://github.com/cliffhall)
- [Tadas Antanavicius](https://github.com/tadasant)
- [Shaun Smith](https://github.com/evalstate)
- [Jonathan Hefner](https://github.com/jonathanhefner)

## Community Moderators

- [Ola Hungerford](https://github.com/olaservo)
- [Cliff Hall](https://github.com/cliffhall)
- [Shaun Smith](https://github.com/evalstate)
- [Jonathan Hefner](https://github.com/jonathanhefner)
- [Tadas Antanavicius](https://github.com/tadasant)

## Working Group & Interest Group Maintainers

[Working Groups and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups) are not required to have maintainers (they can be managed by informal facilitators), but maintainers may be appointed on an as-needed basis.

### Security Interest Group

- [Den Delimarsky](https://github.com/dend)
- [Paul Carleton](https://github.com/pcarleton)
- [Jenn Newton](https://github.com/jenn-newton)

### Authorization Interest Group

- [Aaron Parecki](https://github.com/aaronpk)
- [Darin McAdams](https://github.com/D-McAdams)
- [Paul Carleton](https://github.com/pcarleton)

### Client Implementor Interest Group

**Note:** These individuals serve as MCP protocol representatives for their respective clients. For client-specific issues, use the official support channels provided by each product.

- [Alex Hancock](https://github.com/alexhancock) - Goose
- [Ben Brandt](https://github.com/benbrandt) - Zed
- [Connor Peet](https://github.com/connor4312) - VS Code
- [Gabriel Peal](https://github.com/gpeal) - Codex
- [Jun Han](https://github.com/formulahendry) - GitHub Copilot for JetBrains
- [Tyler Leonhardt](https://github.com/TylerLeonhardt) - VS Code
- [Michael Feldstein](https://github.com/msfeldstein) - Cursor

### Financial Services Interest Group

- [Sambhav Kothari](https://github.com/sambhav)

### Transports Interest Group

- [Kurtis Van Gent](https://github.com/kurtisvg)
- [Jonathan Hefner](https://github.com/jonathanhefner)
- [Shaun Smith](https://github.com/evalstate)
- [Harvey Tuch](https://github.com/htuch)

### Server Identity Working Group

- [Nick Cooper](https://github.com/nicknotfun)

### Agents Working Group

- [Peter Alexander](https://github.com/pja-ant)
- [Luca Chang](https://github.com/LucaButBoring)
- [Inna Harper](https://github.com/ihrpr)

## About This Document

This document is updated by the MCP maintainers and reflects the current
governance structure. For more information about MCP governance, see our
[governance documentation](https://modelcontextprotocol.io/community/governance).



================================================
FILE: package.json
================================================
{
  "name": "@modelcontextprotocol/specification",
  "private": true,
  "version": "0.1.0",
  "description": "Model Context Protocol specification and protocol schema",
  "license": "MIT",
  "author": "Anthropic, PBC (https://anthropic.com)",
  "homepage": "https://modelcontextprotocol.io",
  "bugs": "https://github.com/modelcontextprotocol/specification/issues",
  "engines": {
    "node": ">=20"
  },
  "prettier": {
    "overrides": [
      {
        "files": "*.{md,mdx}",
        "options": {
          "proseWrap": "preserve"
        }
      }
    ]
  },
  "scripts": {
    "check": "npm run check:schema && npm run check:docs",
    "check:schema": "npm run check:schema:ts && npm run check:schema:json && npm run check:schema:md",
    "check:schema:ts": "tsc",
    "check:schema:json": "for f in schema/*/schema.ts; do typescript-json-schema --defaultNumberType integer --required --skipLibCheck \"$f\" \"*\" | cat | cmp \"${f%.ts}.json\" - || exit 1; done",
    "check:schema:md": "for f in docs/specification/*/schema.mdx; do typedoc --entryPoints \"schema/$(basename -- $(dirname -- \"$f\"))/schema.ts\" | cmp \"$f\" - || exit 1; done",
    "check:docs": "npm run check:docs:format && npm run check:docs:links",
    "check:docs:format": "prettier --check \"**/*.{md,mdx}\"",
    "check:docs:links": "cd docs && mintlify broken-links",
    "generate:schema": "npm run generate:schema:json && npm run generate:schema:md",
    "generate:schema:json": "for f in schema/*/schema.ts; do typescript-json-schema --defaultNumberType integer --required --skipLibCheck \"$f\" \"*\" -o \"${f%.ts}.json\"; done",
    "generate:schema:md": "for f in docs/specification/*/schema.mdx; do typedoc --entryPoints \"schema/$(basename -- $(dirname -- \"$f\"))/schema.ts\" > \"$f\"; done",
    "format": "prettier --write \"**/*.{md,mdx}\" --ignore \"docs/specification/*/schema.mdx\" ",
    "serve:docs": "cd docs && mintlify dev",
    "serve:blog": "cd blog && hugo serve"
  },
  "devDependencies": {
    "ajv": "^8.17.1",
    "ajv-formats": "^3.0.1",
    "glob": "^11.0.0",
    "mintlify": "^4.0",
    "prettier": "^3.6.2",
    "tsx": "^4.19.1",
    "typedoc": "^0.28.7",
    "typescript": "^5.6.2",
    "typescript-json-schema": "^0.65.1"
  },
  "resolutions": {
    "fast-json-patch": "^3.1.1"
  }
}



================================================
FILE: SECURITY.md
================================================
# Security Policy

Thank you for helping us keep the SDKs and systems they interact with secure.

## Reporting Security Issues

This SDK is maintained by [Anthropic](https://www.anthropic.com/) as part of the Model
Context Protocol project.

The security of our systems and user data is Anthropic’s top priority. We appreciate the
work of security researchers acting in good faith in identifying and reporting potential
vulnerabilities.

Our security program is managed on HackerOne and we ask that any validated vulnerability
in this functionality be reported through their
[submission form](https://hackerone.com/anthropic-vdp/reports/new?type=team&report_type=vulnerability).

## Vulnerability Disclosure Program

Our Vulnerability Program Guidelines are defined on our
[HackerOne program page](https://hackerone.com/anthropic-vdp).



================================================
FILE: tsconfig.json
================================================
{
  "compilerOptions": {
    "noEmit": true,
    "target": "es2016",
    "rootDir": "schema",
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true
  }
}



================================================
FILE: typedoc.config.mjs
================================================
// @ts-check

/** @type {Partial<import("typedoc").TypeDocOptions>} */
const config = {
  out: "tmp",
  excludeInternal: true,
  excludeTags: [
    "@format",
    "@maximum",
    "@minimum",
  ],
  disableSources: true,
  logLevel: "Error",
  plugin: ["./typedoc.plugin.mjs"],
};

export default config;



================================================
FILE: typedoc.plugin.mjs
================================================
// @ts-check
import * as typedoc from "typedoc";

/** @param {typedoc.Application} app */
export function load(app) {
  app.outputs.addOutput("schema-reference", async (outputDir, project) => {
    app.renderer.router = new SchemaReferenceRouter(app);
    app.renderer.theme = new typedoc.DefaultTheme(app.renderer);
    app.renderer.trigger(typedoc.RendererEvent.BEGIN, new typedoc.RendererEvent(outputDir, project, []));

    const pageEvents = buildPageEvents(project, app.renderer.router);
    const rendered = renderPageEvents(pageEvents, /** @type {typedoc.DefaultTheme} */ (app.renderer.theme));

    process.stdout.write(`---\n`);
    process.stdout.write(`title: Schema Reference\n`);
    process.stdout.write(`---\n\n`);
    process.stdout.write(`<div id="schema-reference" />\n\n`);
    process.stdout.write(rendered);

    // Wait for all output to be written before allowing the process to exit.
    await new Promise((resolve) => process.stdout.write("", () => resolve(undefined)));
  })

  app.outputs.setDefaultOutputName("schema-reference")
}

class SchemaReferenceRouter extends typedoc.StructureRouter {
  /**
   * @param {typedoc.RouterTarget} target
   * @returns {string}
   */
  getFullUrl(target) {
    return "#" + this.getAnchor(target);
  }

  /**
   * @param {typedoc.RouterTarget} target
   * @returns {string}
   */
  getAnchor(target) {
    if (target instanceof typedoc.DeclarationReflection &&
      target.kindOf(typedoc.ReflectionKind.Property) &&
      !hasComment(target)
    ) {
      return "";
    } else {
      // Must use `toLowerCase()` because Mintlify generates lower case IDs for Markdown headings.
      return super.getFullUrl(target).replace(".html", "").replaceAll(/[./#]/g, "-").toLowerCase();
    }
  }
}

/**
 * @param {typedoc.DeclarationReflection} member
 * @returns {boolean}
 */
function hasComment(member) {
  return member.hasComment() || (
    member.type instanceof typedoc.ReflectionType &&
    !!member.type.declaration.children?.some((child) => hasComment(child))
  );
}

/**
 * @param {typedoc.ProjectReflection} project
 * @param {typedoc.Router} router
 * @returns {typedoc.PageEvent[]}
 */
function buildPageEvents(project, router) {
  const events = [];

  for (const pageDefinition of router.buildPages(project)) {
    const event = new typedoc.PageEvent(pageDefinition.model)
    event.url = pageDefinition.url;
    event.filename = pageDefinition.url;
    event.pageKind = pageDefinition.kind;
    event.project = project;
    events.push(event)
  }

  return events;
}

/**
 * @param {typedoc.PageEvent[]} events
 * @param {typedoc.DefaultTheme} theme
 * @returns {string}
 */
function renderPageEvents(events, theme) {
  const declarationEvents = events.
    filter(isDeclarationReflectionEvent).
    sort((event1, event2) => event1.model.name.localeCompare(event2.model.name));

  /** @type {Map<string, string[]>} */
  const outputsByCategory = new Map();

  for (const event of declarationEvents) {
    const category = getReflectionCategory(event.model);
    const rendered = renderReflection(event.model, theme.getRenderContext(event));

    if (!outputsByCategory.has(category)) {
      outputsByCategory.set(category, [renderCategory(category)]);
    }
    outputsByCategory.get(category)?.push(rendered);
  }

  return [...outputsByCategory.keys()].
    sort().flatMap((category) => outputsByCategory.get(category)).join("\n");
}

/**
 * @param {typedoc.PageEvent} event
 * @returns {event is typedoc.PageEvent<typedoc.DeclarationReflection>}
 */
function isDeclarationReflectionEvent(event) {
  return event.model instanceof typedoc.DeclarationReflection;
}

/**
 * @param {typedoc.DeclarationReflection} reflection
 * @returns {string}
 */
function getReflectionCategory(reflection) {
  const categoryTag = reflection.comment?.getTag("@category");
  return categoryTag ? categoryTag.content.map((part) => part.text).join(" ") : "";
}

/**
 * @param {string} category
 * @returns {string}
 */
function renderCategory(category) {
  let heading = category || "Common Types";
  if (heading.match(/^[a-z]/)) heading = "`" + heading + "`";
  return `## ${heading}\n`;
}

/**
 * @param {typedoc.DeclarationReflection} reflection
 * @param {typedoc.DefaultThemeRenderContext} context
 * @returns {string}
 */
function renderReflection(reflection, context) {
  const name = reflection.getFriendlyFullName();
  const members = reflection.children?.filter(hasComment) ?? [];

  const codeBlock = context.reflectionPreview(reflection);

  let content = renderJsxElements(
    codeBlock ?
      [codeBlock, context.commentSummary(reflection)] :
      context.memberDeclaration(reflection),
    members.map(member => context.member(member)),
  );

  // Convert `<hN>` elements to `<div>`.
  content = content.
    replaceAll(/<h([1-6])/g, `<div data-typedoc-h="$1"`).
    replaceAll(/<\/h[1-6]>/g, `</div>`);

  // Reduce code block indent from 4 spaces to 2 spaces.
  content = content.replaceAll("\u00A0\u00A0", "\u00A0");

  // Accommodate Mintlify's broken Markdown parser.
  content = content.
    replaceAll("\u00A0", "&nbsp;"). // Encode valid UTF-8 character as HTML entity
    replaceAll(/\n+</g, " <"). // Newlines around tags are not significant
    replaceAll("[", "&#x5B;"). // `[` inside HTML tags != link
    replaceAll("_", "&#x5F;"). // `_` inside HTML tags != emphasis
    replaceAll("{", "&#x7B;"). // Plain *.md is not supported, so must escape JSX interpolation
    replaceAll("$", "&#x24;"); // `$` does not demarcate LaTeX(?)


  // Remove `@TJS-type` tags.  (Ideally, we would include this tag in
  // `excludeTags`, but a TypeDoc bug rejects tag names with dashes.)
  content = content.replaceAll(/<p>@TJS-type [^<]+<\/p>/g, "");

  return `### \`${name}\`\n\n${content}\n`;
}

/**
 * @param {typedoc.JSX.Children[]} elements
 */
function renderJsxElements(...elements) {
  return typedoc.JSX.renderElement(typedoc.JSX.createElement(typedoc.JSX.Fragment, null, elements));
}



================================================
FILE: .npmrc
================================================
registry = "https://registry.npmjs.org/"



================================================
FILE: .nvmrc
================================================
v20.16.0



================================================
FILE: .prettierignore
================================================
docs/specification/*/schema.md
docs/specification/*/schema.mdx



================================================
FILE: blog/go.mod
================================================
module github.com/modelcontextprotocol/modelcontextprotocol

go 1.24.4

require github.com/adityatelange/hugo-PaperMod v0.0.0-20250913173842-ff85b9cd6579 // indirect



================================================
FILE: blog/go.sum
================================================
github.com/adityatelange/hugo-PaperMod v0.0.0-20250524045829-5a4651783fa9 h1:vSOmKCogP6L4SV2eO7A2zgO7sdml4Ta7tZSd6ccOTmQ=
github.com/adityatelange/hugo-PaperMod v0.0.0-20250524045829-5a4651783fa9/go.mod h1:HCHxNMKYdGafUYjVV3ICiAqznZK2yH0iI53jqcDFDdQ=
github.com/adityatelange/hugo-PaperMod v0.0.0-20250913173842-ff85b9cd6579 h1:U8K/kaIYeEGkvINZFlgcskPdN8tmRS5neQK27GdU39k=
github.com/adityatelange/hugo-PaperMod v0.0.0-20250913173842-ff85b9cd6579/go.mod h1:HCHxNMKYdGafUYjVV3ICiAqznZK2yH0iI53jqcDFDdQ=



================================================
FILE: blog/hugo.toml
================================================
baseURL = 'https://blog.modelcontextprotocol.io/'
languageCode = 'en-us'
title = 'mcp blog'
theme = 'github.com/adityatelange/hugo-PaperMod'
[pagination]
  pagerSize = 5

[params]
  author = "The MCP project"
  description = "Updates from the Model Context Protocol project"

  # PaperMod specific settings
  # defaultTheme = "dark" # MCP uses a dark theme
  disableThemeToggle = false
  ShowShareButtons = false
  ShowReadingTime = true
  ShowPostNavLinks = true
  ShowBreadCrumbs = true
  ShowCodeCopyButtons = true
  ShowWordCount = false
  ShowRssButtonInSectionTermList = true
  UseHugoToc = false
  disableSpecial1stPost = true
  disableScrollToTop = false
  comments = false
  hidemeta = false
  hideSummary = false
  showtoc = false
  ShowFullTextinRSS = true

  # Custom copyright
  copyright = '© 2025 Model Context Protocol Project'

  [params.assets]
    favicon = "favicon.svg"

  [[params.socialIcons]]
    name = "github"
    url = "https://github.com/modelcontextprotocol"

# Menu configuration
[[menu.main]]
  identifier = "docs"
  name = "Documentation"
  url = "https://modelcontextprotocol.io/docs"
  weight = 10

[[menu.main]]
  identifier = "github"
  name = "GitHub"
  url = "https://github.com/modelcontextprotocol"
  weight = 20

# Markup configuration for syntax highlighting
[markup]
  [markup.highlight]
    guessSyntax = true
    style = "monokai"
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true

[module]
  [[module.imports]]
    path = 'github.com/adityatelange/hugo-PaperMod'



================================================
FILE: blog/archetypes/default.md
================================================
+++
date = '{{ .Date }}'
draft = true
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
+++



================================================
FILE: blog/assets/css/extended/custom.css
================================================
/* Override list page background to white in light mode */
.list {
    background: var(--theme);
}

/* Dark mode remains unchanged */
.dark.list {
    background: var(--theme);
}

/* Mermaid diagram styling for dark mode */
.dark .mermaid {
    filter: invert(0.85) hue-rotate(180deg);
}

/* Prevent awkward wrapping in post metadata. See https://github.com/adityatelange/hugo-PaperMod/issues/1789 */
.post-meta {
    display: block !important;
}



================================================
FILE: blog/content/_index.md
================================================
+++
title = 'blog'
+++



================================================
FILE: blog/content/posts/2025-07-29-prompts-for-automation.md
================================================
+++
date = '2025-08-04T18:00:00+01:00'
publishDate = '2025-08-04T18:00:00+01:00'
draft = false
title = 'MCP Prompts: Building Workflow Automation'
author = 'Inna Harper (Core Maintainer)'
tags = ['automation', 'mcp', 'prompts', 'tutorial']
+++

[MCP (Model Context Protocol)](https://modelcontextprotocol.io/specification/2025-06-18) prompts enable workflow automation by combining AI capabilities with structured data access. This post demonstrates how to build automations using MCP's [prompts](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts) and [resource templates](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#resource-templates) through a practical example.

This guide demonstrates how MCP prompts can automate repetitive workflows. Whether you're interested in the MCP ecosystem or simply want to leverage AI for workflow automation, you'll learn how to build practical automations through a concrete meal planning example. No prior MCP experience needed—we'll cover the fundamentals before diving into implementation.

## The Problem: Time-Consuming Repetitive Tasks

Everyone has a collection of repetitive tasks that eat away at their productive hours. Common examples include applying code review feedback, generating weekly reports, updating documentation, or creating boilerplate code. These tasks aren't complex—they follow predictable patterns—but they're cumbersome and time-consuming. [MCP prompts](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts) were designed to help automate this kind of work.

MCP prompts offer more than command shortcuts. They're a primitive for building workflow automation that combines the flexibility of scripting with the intelligence of modern AI systems. This post explores how to build automations using MCP's prompt system, resource templates, and modular servers. I'll demonstrate these concepts through a meal planning automation I built, but the patterns apply broadly to any structured, repetitive workflow.

## Example: Automating Weekly Meal Planning

I needed to solve a recurring problem: planning weekly meals by cuisine to manage ingredients efficiently. The manual process involved selecting a cuisine, choosing dishes, listing ingredients, shopping, and organizing recipes—repetitive steps that took significant time each week.

So I decided to use MCP! By automating these steps, I could reduce the entire workflow to selecting a cuisine and receiving a complete meal plan with shopping list. (Any client that supports MCP prompts should work!)

1. **Select a prompt**

   <img
   src="/posts/images/prompts-list.png"
   alt="MCP prompts list showing available automation commands"
   />

2. **Select a cuisine from a dropdown**
   <img
     src="/posts/images/prompts-suggestions.png"
     alt="Dropdown showing cuisine suggestions as user types"
   />
3. **Done!**
   The system generates a meal plan, shopping list, and even prints the shopping list and recipes.

<img
    src="/posts/images/prompts-final-result.png"
    alt="Final generated meal plan and shopping list output"
  />

Here we are focuses primarily on the Recipe Server with its prompts and resources. You can find the [printing server example here](https://github.com/ihrpr/mcp-server-tiny-print) (it works with a specific thermal printer model, but you could easily swap it for email, Notion, or any other output method). The beauty of separate servers is that you can mix and match different capabilities.

## Core Components

Let's dive into the three components that make this automation possible: [prompts](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts), [resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources), and [completions](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/completion). I'll show you how each works conceptually, then we'll implement them together.

### 1. Resource Templates

In MCP, [static resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#resource-types) represent specific pieces of content with unique URIs—like `file://recipes/italian.md` or `file://recipes/mexican.md`. While straightforward, this approach doesn't scale well. If you have recipes for 20 cuisines, you'd need to define 20 separate resources, each with its own URI and metadata.

[Resource templates](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#resource-templates) solve this through URI patterns with parameters, transforming static resource definitions into dynamic content providers.

For example, a template like `file://recipes/{cuisine}.md` might represent a set of resources like these:

- `file://recipes/italian.md` returns Italian recipes
- `file://recipes/mexican.md` returns Mexican recipes

This pattern extends beyond simple filtering. You can create templates for:

- Hierarchical data: `file://docs/{category}/{topic}`
- Git repository content: `git://repo/{branch}/path/{file}`
- Web resources: `https://api.example.com/users/{userId}/data`
- Query parameters: `https://example.com/{collection}?type={filter}`

For more details on URI schemes and resource templates, see the [MCP Resource specification](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#resource-templates).

### 2. Completions

Nobody remembers exact parameter values. Is it "italian" or "Italian" or "it"? [Completions](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/completion) bridge this gap by providing suggestions as users type, creating an interface that feels intuitive rather than restrictive.

Different MCP clients present completions differently:

- VS Code shows a filterable dropdown
- Command-line tools might use fuzzy matching
- Web interfaces could provide rich previews

But the underlying data comes from your server, maintaining consistency across all client

[... Content truncated due to length ...]

</details>


## YouTube Video Transcripts

<details>
<summary>Here is a detailed transcript of the video.</summary>

Here is a detailed transcript of the video.

### Introduction to MCP Servers and Agentic Coding

(Overhead shot of a person's hands over a laptop keyboard. The screen shows an abstract image of a person walking down a glowing corridor.)

**Speaker:** As you know, MCP servers let you build tools for everything. (Text overlays on the screen: "As you know,", "MCP servers", "TOOLS", "TOOLS FOR EVERYTHING") MCP servers are one of the three most important innovations for evolving your engineering from AI coding to agentic coding.

(An animated diagram appears on screen. A small yellow circle labeled "AI Coding" is enclosed by a larger green oval labeled "Agentic Coding".)

With new models like Claude 4, and the brand new DeepSeek-R1.1, we have more intelligence to build than EVER before.

(A browser window appears over the laptop, first showing an Anthropic blog post titled "Introducing Claude 3" (the speaker says "Claude 4"), then switching to the DeepSeek API documentation for "DeepSeek-R1 update".)

[00:30]
But the models are no longer the limiting factor for your engineering output. That forces us to ask, what's limiting us as engineers from creating more value faster than ever? (The abstract image returns with text overlays: "what's limiting", "us as engineers", "from creating", "more VALUE", "FASTER than ever", accompanied by a large question mark.) It's our abilities to create capabilities for our agentic coding tools like Claude Code.

(The view switches to a terminal window titled "Claude Code". The AI logo for Claude Code is displayed.)

That brings us full circle back to MCP servers.

(The view returns to the abstract image, then a browser window shows the GitHub page for the "Model Context Protocol".)

In this video, we're going to understand the most underutilized capability of MCP servers.

(The browser window now shows the "Core MCP Concepts" documentation, listing: 1. Resources, 2. Tools, 3. Prompts.)

Most engineers STOP at tools.

*The speaker introduces Model Context Protocol (MCP) servers as a key innovation for advancing from simple AI coding to more complex "agentic coding," arguing that the new bottleneck isn't the AI models, but the developer's ability to create powerful tools.*

### The Power of MCP Primitives: Prompts

[01:00]
(In the documentation view, the speaker highlights "Tools" with an orange box.)

But once you understand this one SIMPLE idea, you'll be able to craft rich MCP servers that dramatically INCREASE your engineering VELOCITY as well as your teams. Resources, tools, and prompts. In the tier list in reverse order of capability, we have resources, tools, and prompts.

(The abstract image returns with an "MCP Primitive Tier List" title. The text "??? > ??? > ???" changes to "??? > ??? > Resources", then "??? > Tools > Resources", and finally "Prompts > Tools > Resources".)

Most engineers SKIP resources. They go ALL IN on tools and completely MISS OUT on the HIGHEST leverage primitive of MCP servers, PROMPTS. (The words on the tier list are highlighted in sequence.) Tool calling is just the beginning of your MCP server. Let me show you how to MAXIMIZE the value of your MCP servers.

(A title card appears over a view of clouds from an airplane window.)

**On-screen text:** MCP MAXXING

*The speaker presents a hierarchy of MCP server capabilities—Resources, Tools, and Prompts—and asserts that Prompts are the most powerful and underutilized primitive that can dramatically increase engineering velocity.*

### Practical Demo: Using Tools for Data Analysis

[01:30]
(The view returns to the "Claude Code" terminal.)

If we type `/mcp`, you can see I have six MCP servers available. We're going to be operating in the quick-data MCP server. Quick-data gives your agent arbitrary data analysis capabilities on .json and .csv files. We all know how tools work, but let's run a few to understand the quick-data MCP server and showcase how limited tool calls really are. If we type `/model`, we're going to run the Sonnet 4 fast workhorse model for this.

So, right away we have a problem. I have no idea what I can do with this MCP server. I have to rely on some type of documentation.

(An application launcher opens, and "Cursor" is selected.)

Let's open up Cursor and break open the README.

(The Cursor code editor opens, showing a README file for the "Generic Data Analytics MCP Server".)

If we scroll down here, I have a complete documented set of all the tools, resources, and prompts available for this MCP server.

[02:00]
(The view scrolls through the README, showing sections for "Analytics Tools", "Data Loading & Management", "Core Analytics", and "Advanced Analytics".)

Let's just start with a couple simple ones. I'll run this: `load_dataset`. And now we need to pass in a .json or a .csv file. I'll go back to Cursor. If I search for ecommerce orders, you can see we have this simple JSON list. I'll copy the reference to this file with Command+Shift+R. Then I'll hop back to Claude Code, paste this in, and have it load.

(The speaker copies the relative path of `ecommerce_orders.json` and pastes it into the Claude Code terminal.)

All right, so as expected, we have this `load_dataset` MCP server tool. It has the file path and the dataset name `ecommerce_orders`. This looks great. We'll go ahead and accept this.

(A "Tool use" prompt appears, which the speaker accepts. A JSON response confirms the dataset is loaded, showing status, name, rows, and columns.)

[02:30]
And you can see our JSON response. If we hit Control+R, you can see the entire thing. Columns, rows, dataset name. Looks great. So let's go ahead and get a dataset breakdown. So I'll paste. This also accepts the dataset name. So I'll go ahead, copy and paste this back in, and now we're just going to get some basic information about this dataset. We'll of course accept this tool call. And you can see we have the shape and key information about this dataset.

So far, this looks great. Let's run a couple more tools and then we're going to up-level everything we're doing by looking at the most powerful capability you can add to your MCP server. Let's run `suggest_analysis`.

(The speaker scrolls back to the README in Cursor and finds the `suggest_analysis` tool.)

Paste. And then I'll just say `ecom...` This is going to be auto-completed for us based on the current context.

[03:00]
There it is, `suggest_analysis`. Let's see what we get. So we have a couple of ideas given to us based on that tool call. `run command #1`. Fire this off. We're now going to get a segment breakdown by this `product_category` column. So check this out. We have product category segmentation. We can see that electronics are producing a lot of value inside of this `ecommerce_orders.json` file. So looking at this data from a business strategy perspective, we could, if we wanted to, cut down on sports and home & garden product categories and go all in on electronics based on this insight.

Okay, so there's one more cool tool I want to share with you here. If we scroll down to the bottom, we can execute arbitrary code.

[03:30]
We can have Claude Code, running on Claude 4 Sonnet, execute arbitrary code for us. So, again, we can just come back in here, paste, we can say `ecom...`. And let's find out the... if we look at the dataset here, we have this `region` column, and we also have `order_value`. So let's find out the top order value by region. `find top 3 region by order_value`. Yep, let's go ahead and fire that off.

(The AI generates a Python code block inside the tool call to perform the requested analysis.)

There we go. So you can see here we have custom code getting written based on our prompt. We'll hit yes. And there is our executed code response. You can see here our top three regions by order value: we have East Coast, West Coast, and of course Midwest in last place. Pretty accurate training data set, right?

[04:00]
If we want to reuse that same MCP tool call, we can hit up and then I'll say, `then create a pie chart label by region with value and percent`. It's going to create a pie chart for us. Let's go ahead and run this.

(A new browser tab opens, displaying a pie chart titled "Order Value Distribution by Region" with slices for east_coast, west_coast, midwest, and south.)

And bam, check this out. You can see we have East Coast, we have West Coast, Midwest, and then the South. We have a great breakdown here. And this was all just quickly created and managed with our MCP server for quick data analytics against .json and .csv files.

*The speaker demonstrates how to interact with an MCP server through a command-line interface, using tools to load a dataset, get information about it, receive analysis suggestions, segment the data, and even execute custom Python code to generate insights and visualizations.*

### Unleashing Agentic Workflows with MCP Server Prompts

[04:30]
So tools are great. We all know about their capabilities. We can build out tools for anything and tools for everything. (Text "TOOLS FOR EVERYTHING" appears on screen.) But tools ONLY scratch the SURFACE of what you can do with your MCP server. To unlock the full capabilities of what you can do, we need to build MCP server prompts.

(A title card appears over a view of clouds at sunset.)

**On-screen text:** MCP SERVER PROMPTS

So, in order to showcase the capabilities here, we're going to reset this Claude Code instance and really start from scratch. So let's open up Claude again. We'll run the same setup. So you can see here `/mcp`, `/model`, same deal, Sonnet 4.

[05:00]
So now instead of looking through the documentation... (The speaker opens the Cursor editor showing the code files and the README.) ...right, we had this README that thankfully detailed all of our tools, resources, and prompts. Right, there's the code-based structure. We'll take a look at that in a second. Instead of doing any of this, instead of, you know, relying on code-based architecture, code-based structure, we can just use MCP server prompts to guide the entire discovery and use of the quick-data MCP server. Let me show you exactly what I mean.

To find all the prompts associated with this MCP server inside of Claude Code, we can type `/quick-data`. So this is the name of the MCP server. And here you can see a ton of auto-complete suggestions with prompts.

[05:30]
So these are prompts built out in the MCP server. Now, we're going to run something really cool, something very useful that I highly recommend you set up inside of all your MCP servers. We're going to list all available MCP server capabilities including prompts, tools, and resources. So this is a prompt that's going to give us a clear breakdown of what we can do with this tool. Okay.

(The speaker runs the `list_mcp_assets_prompt`. The AI responds with a detailed summary of the server's capabilities, including "Key Components" like interactive prompts, tools, and resources, and a "Quick Start Flow".)

Check this out. So Claude Code, our agentic coding tool, has now consumed everything that we can do with this tool. It's now loaded fresh in the context window.

[06:00]
And we have a quick start flow to get started. So now if we want to, we can just ask Claude Code what exactly these key components are. Okay, so I'm just going to say, `what prompts and tools do we have available? List as bullets`. All right, so check this out. So now we can just, you know, query our agent. Right here are the prompts, here are the tools. This is everything that we saw before. Let's go ahead and continue firing off these prompts to really understand what they can do for us. So if we type `/find`, you can see we have another prompt: `find_datasources_prompt`. This is going to discover available data files in the current directory and present them as load options. Now...

[06:30]
...see how much more helpful these prompts are than just having tools hidden somewhere? I'm going to hit tab. You can see here we have an argument, the directory path. I'll just hit dot for that and fire that off. So this is going to automatically discover all available .json and .csv files for our quick-data MCP server. So we added a prompt, also known as an agentic workflow, to do this work for us automatically. You can see we also have, take note of this, this is really important, "Ready to load with `load_dataset()` commands."

[07:00]
So with the previous prompt and this prompt, you can see every prompt we're running, we're getting a suggestion or a forward direction or a next step for what we can do with this MCP server. So what I'm going to do here is just type `load ecom`. So I have a really tight, information-dense keyword prompt, literally just two words, with the current context that we have set up, thanks to our prompts, and thanks to Claude Code running on Claude 4 Sonnet, I can be nearly 100% sure that this is going to run the right tool with the right information. Okay?

[07:30]
So I'll kick this off. And notice how I just, you know, ran through the big three of AI coding: Context, Model, Prompt. (A Venn diagram appears showing three overlapping ovals for CONTEXT, MODEL, and PROMPT.) These never go away. That's why they're a principle of AI coding. They're always there whether you realize it or not. The more you can look and think from your agent's perspective with the current available context, model, and prompt, the more you'll be able to hand off tons and tons of engineering work, which in the end results in your engineering velocity increase. So check this out. We have the file path here, using the full absolute path. Looks great. And then we have the dataset name. Okay?

[08:00]
With just typing slash, with just working through a few pre-existing prompts, we're moving a lot faster than if we were looking through, you know, the documentation, going back and forth and back and forth. And that is a really important thing to call out here, right? We haven't left the terminal. We haven't left Claude Code. We're focused, we're moving quickly, and we're operating inside of this MCP server with minimal information. Okay, so we have that dataset loaded. If we scroll back up, you'll remember here at the top that we were given a concrete workflow. You can see, uh, find dataset to discover data files, and then we can run `load_dataset`, and then explore data.

[08:30]
So let's go ahead and run that. I'm going to type `/first`. This is our first look MCP prompt. I'll hit tab, and you can see there the arguments are dataset name. I'll go ahead and just type `ecom...` and we should get auto-completion there. There it is. So this prompt, and we're going to take a look at the individual prompts in a second, is kicking off one or more tools. Okay? So we'll go ahead and fire that off.

(The prompt triggers a tool call to `resource_datasets_sample`. The speaker accepts it.)

And based on that prompt, right, and based on the information returned by this tool, we're getting a nice breakdown of a sample of this dataset. Size, columns, sample data, looks great. You can see there we actually did get a sample. If we hit Control+R, it broke down, you know, pieces of our data.

[09:00]
So that looks great. Thanks to the existing context window that all of these prompts have been giving our agent, we can just type something like this: `How can we further explore this data?` Okay, so check this out. From the existing context window, we have, you know, tons of ideas of how we can keep pushing this. And this is really useful for when you're operating outside of your MCP server. Obviously, if you're building your MCP server, you have access to the actual code, and you can just kind of, you know, have your agent run through this.

[09:30]
But when we're operating in this, when we're handing off our MCP servers to our team, to our engineering team, and when we're exposing our MCP servers to the public, we want it easy to use, we want it to be quickly consumable, and we want these guided workflows, okay? Prompts are really important because they can return entire sets of information to your agent, and they can provide next steps. You can keep pushing yourself, you can keep pushing engineers on your team, and pushing the agent in the right direction for your domain-specific problem set. Okay? So let's go ahead, let's run another prompt. So we can do `/quick-data` to see all of our prompts.

[10:00]
Let's go ahead and run the `correlation_investigation_prompt`. So this is going to find correlations inside of our dataset. We'll of course type `ecom...` And before we run this, let me show you exactly what these prompts look like inside of the MCP server. So I'll open up Cursor, and we're just going to search for that prompt. And notice how I just have a single method inside of this file. And since we're here, let's talk about code-based architecture. This is important. So I have the codebase embedded in its own directory here. And on top, you can see the three essential directories for agentic coding, and you can see our `trees` directory for multi-agent parallel AI coding.

[10:30]
(The speaker shows a file explorer view with folders: `claude`, `project`, `trees`, and `arch-modular-mcp`.)

Check out the previous video to see how we parallelize Claude Code into multiple trees to get work done at the same time. But if we click into `arch-modular-mcp` and we take a look at the architecture here, you can see we have our data there, and then we have `src`, `mcp_server`, and we have the primitives of the MCP server, right? Tools, resources, and prompts. If we open up prompts, we can see our `correlation_investigation_prompt.py` here inside of a single function. These are all single-function Python files to keep everything nice and isolated and easily testable. So if we hop up to this file, we can see something really cool. We're passing in the dataset name, and then we're just running arbitrary code, which is effectively our agentic workflow.

[11:00]
You can do anything you want here. The most important thing is to gather some type of prompt response and then return that back to your agent. Right, this is what's going to get passed right back into the agent. So you can see, we have lots of detail on the correlation investigation, a couple of branching of logic here, a loop, and you can see we're loading that schema out of our existing dataset. So let's go ahead, let's run this. This is going to run a really great analysis on our dataset. Okay? So we're going to close that. Let's run this. So this prompt is kicking off a tool call, and this is super important. Inside of your prompt, you can kick off one or more tool calls.

[11:30]
You can see here how the prompt allows you to compose sequences of tool calls very, very quickly using a custom slash command here. Okay? So quick commands to start, you can see that we're picking this up automatically. This is getting returned into the context window, and now Claude Code, running on Claude 4, wants to kick this off for us based on this prompt. Okay? So of course we'll hit yes. And you can see there we're getting some concrete feedback. We need at least two numerical columns for correlation analysis. Okay, so we're going to kick this off. This is going to re-expose information back into our agent.

[12:00]
So, `ecommerce_orders` cannot run this. So our tools are giving us feedback, all guided by our prompt. So let's go ahead and load some more data, right? We can very quickly thanks to our slash command just run `/find`. And let's go ahead and find those other data sources that we have. I'll specify the directory here, dot, and this is going to re-load all of our data sources. So you can see here, we can load these two additional data sources. Let's go ahead and load these. So I'm just going to say, `load all`. So now we're going to get those two prompts. There's our `employee_survey` dataset. And here's our `product_performance` dataset. We'll hit yes, yes.

[12:30]
"Now you have multiple numerical columns across datasets for correlation analysis!" Okay, so I'll just say `run analysis on employee, product`. Okay. So there it is. There's that find correlation lookup. And you can see here it's queued up several calls, several tool calls that we can now kick off. So this is one way to activate this workflow. That's great. I'm going to hit escape here and I'm going to reuse the slash command that we were we were going for. So I'm going to type `/correlation_investigation_prompt`. Looks great. And then I'll pass in... let's use our `employee_survey`.

[13:00]
So I'll paste that in, and let's run the investigation prompt here. This should kick off a similar workflow. There it is. So this prompt is exposing the potential columns that we can correlate. So there's a strong positive correlation between satisfaction score and tenure year. That means employees with higher satisfaction scores tend to have longer tenure. And so this reveals, you know, not to get too specific into the weeds of this MCP server, but this is important because it's going to immediately reveal to us that satisfaction and retention are closely linked. Satisfied employees stay longer. Not a mind-blowing revelation, but this could be anything inside of your dataset. Okay, I'm just, I'm just putting together a small concise example that we can, you know, discuss to showcase the power of these MCP server prompts.

[13:30]
Okay? "Do you want to visualize this with option 2?" I'll say go ahead. And we'll just continue walking through... `create_chart`. So let's go ahead and fire that off. We now have an additional chart setup here. We can open this up. So we can copy this file path here. If we go into HTML preview mode, we can see this chart generated. If you average these out over the satisfaction score, you can see we have a pretty strong correlation here between tenure and satisfaction score.

[14:00]
So, very powerful stuff. So what does this all mean, right? Why are prompts inside of your MCP server so important? Right away, by using this MCP server, we were able to move a lot faster. If we close Claude here, reopen it, and we type `/assets`, we can get our agent back up and running with this MCP server very quickly. Okay? So prompts allow you to quickly set up your agent with everything they need to know to operate your MCP server.

[14:30]
So this is just one simple way you can use MCP server prompts. Check this out. And we can look at this exact prompt. Right, this is the `list_mcp_assets` prompt. So check this out. Look how simple this is. This is quite literally just returning essential information about this MCP server in a custom way to our agent. This prompt primes both your memory and your agent's memory with everything it needs to know about your MCP server. Every MCP server I build out now has some type of prompt just like this. So now everything is exposed. We can quickly see and operate on things in a much faster way. We can always type `/quick-` and start understanding our datasets. Right?

[15:00]
So, you know, we then ran our `find`, and we passed in dot, and this is going to re-load all of our data sources. So you can see here, with this prompt we can load these two additional data sources. Let's go ahead and load these. So I'm just going to say, `load all datasets`. Okay, so there's three prompts instead of one. Right, we can move a lot faster thanks to the prompt. Okay? So we're going to load bam, bam, bam. Now we have all three datasets loaded. Fantastic. And now we can run, you know, our `dataset_first_look` if we wanted to. We can continue down the line of data exploration or running whatever other tools or prompts our MCP server exposes to us.

[15:30]
With prompts, you can build out high-quality MCP servers that do more than just call tools. Tool calling is just the beginning. Tools are the primitives of MCP servers, not the end state. You want to end up with prompts, right? Prompts represent end-to-end developer workflows that are truly agentic workflows, or as I like to call them, AI Developer Workflows, right? They're quite literally doing developer work that you would do, but it's powered, of course, by GenAI. You really want to be thinking about MCP servers as a way to solve a domain-specific problem in an automated fashion with repeat solutions embedded inside of the prompts.

[16:00]
The prompt is what the tools scale into. This codebase is linked in the description to give you a concrete example of how you can use prompts inside your MCP servers. Come in here, play with it, `cd` into this folder name. I'll probably change this by the time you see it, and you'll be able to quickly boot up Claude Code with this `.mcp.json` file here. If you made it to the end, like, comment to let the YouTube algorithm know you want more hands-on engineering information like this. You know where to find me every Monday. Stay focused and keep building.

</details>


## Additional Sources Scraped

<details>
<summary>connect-claude-code-to-tools-via-mcp-claude-docs</summary>

Claude Code can connect to hundreds of external tools and data sources through the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), an open-source standard for AI-tool integrations. MCP servers give Claude Code access to your tools, databases, and APIs.

## [​](https://docs.claude.com/en/docs/claude-code/mcp#what-you-can-do-with-mcp)What you can do with MCP

With MCP servers connected, you can ask Claude Code to:

- **Implement features from issue trackers**: “Add the feature described in JIRA issue ENG-4521 and create a PR on GitHub.”
- **Analyze monitoring data**: “Check Sentry and Statsig to check the usage of the feature described in ENG-4521.”
- **Query databases**: “Find emails of 10 random users who used feature ENG-4521, based on our Postgres database.”
- **Integrate designs**: “Update our standard email template based on the new Figma designs that were posted in Slack”
- **Automate workflows**: “Create Gmail drafts inviting these 10 users to a feedback session about the new feature.”

</details>

<details>
<summary>mcp-inspector-model-context-protocol</summary>

The [MCP Inspector](https://github.com/modelcontextprotocol/inspector) is an interactive developer tool for testing and debugging MCP servers. While the [Debugging Guide](https://modelcontextprotocol.io/legacy/tools/debugging) covers the Inspector as part of the overall debugging toolkit, this document provides a detailed exploration of the Inspector’s features and capabilities.

## [​](https://modelcontextprotocol.io/docs/tools/inspector\#getting-started)  Getting started

### [​](https://modelcontextprotocol.io/docs/tools/inspector\#installation-and-basic-usage)  Installation and basic usage

The Inspector runs directly through `npx` without requiring installation:

```
npx @modelcontextprotocol/inspector <command>

```

```
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>

```

#### [​](https://modelcontextprotocol.io/docs/tools/inspector\#inspecting-servers-from-npm-or-pypi)  Inspecting servers from npm or PyPI

A common way to start server packages from [npm](https://npmjs.com/) or [PyPI](https://pypi.org/).

- npm package

- PyPI package

```
npx -y @modelcontextprotocol/inspector npx <package-name> <args>
# For example
npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem /Users/username/Desktop

```

#### [​](https://modelcontextprotocol.io/docs/tools/inspector\#inspecting-locally-developed-servers)  Inspecting locally developed servers

To inspect servers locally developed or downloaded as a repository, the most common
way is:

- TypeScript

- Python

```
npx @modelcontextprotocol/inspector node path/to/server/index.js args...

```

Please carefully read any attached README for the most accurate instructions.

## [​](https://modelcontextprotocol.io/docs/tools/inspector\#feature-overview)  Feature overviewhttps://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/images/mcp-inspector.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=83b12e2a457c96ef4ad17c7357236290

The MCP Inspector interface

The Inspector provides several features for interacting with your MCP server:

### [​](https://modelcontextprotocol.io/docs/tools/inspector\#server-connection-pane)  Server connection pane

- Allows selecting the [transport](https://modelcontextprotocol.io/legacy/concepts/transports) for connecting to the server
- For local servers, supports customizing the command-line arguments and environment

### [​](https://modelcontextprotocol.io/docs/tools/inspector\#resources-tab)  Resources tab

- Lists all available resources
- Shows resource metadata (MIME types, descriptions)
- Allows resource content inspection
- Supports subscription testing

### [​](https://modelcontextprotocol.io/docs/tools/inspector\#prompts-tab)  Prompts tab

- Displays available prompt templates
- Shows prompt arguments and descriptions
- Enables prompt testing with custom arguments
- Previews generated messages

### [​](https://modelcontextprotocol.io/docs/tools/inspector\#tools-tab)  Tools tab

- Lists available tools
- Shows tool schemas and descriptions
- Enables tool testing with custom inputs
- Displays tool execution results

### [​](https://modelcontextprotocol.io/docs/tools/inspector\#notifications-pane)  Notifications pane

- Presents all logs recorded from the server
- Shows notifications received from the server

## [​](https://modelcontextprotocol.io/docs/tools/inspector\#best-practices)  Best practices

### [​](https://modelcontextprotocol.io/docs/tools/inspector\#development-workflow)  Development workflow

1. Start Development   - Launch Inspector with your server
   - Verify basic connectivity
   - Check capability negotiation
2. Iterative testing   - Make server changes
   - Rebuild the server
   - Reconnect the Inspector
   - Test affected features
   - Monitor messages
3. Test edge cases   - Invalid inputs
   - Missing prompt arguments
   - Concurrent operations
   - Verify error handling and error responses

## [​](https://modelcontextprotocol.io/docs/tools/inspector\#next-steps)  Next steps

[**Inspector Repository** \\
\\
Check out the MCP Inspector source code](https://github.com/modelcontextprotocol/inspector) [**Debugging Guide** \\
\\
Learn about broader debugging strategies](https://modelcontextprotocol.io/legacy/tools/debugging)

</details>

<details>
<summary>model-context-protocol-mcp-claude-docs</summary>

MCP is an open protocol that standardizes how applications provide context to LLMs.Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.

## [​](https://docs.claude.com/en/docs/mcp\#build-your-own-mcp-products)  Build your own MCP products

[**MCP Documentation** \\
\\
Learn more about the protocol, how to build servers and clients, and discover those made by others.](https://modelcontextprotocol.io/)

## [​](https://docs.claude.com/en/docs/mcp\#mcp-in-anthropic-products)  MCP in Anthropic products

[**MCP in the Messages API** \\
\\
Use the MCP connector in the Messages API to connect to MCP servers.](https://docs.claude.com/en/docs/agents-and-tools/mcp-connector) [**MCP in Claude Code** \\
\\
Add your MCP servers to Claude Code, or use Claude Code as a server.](https://docs.claude.com/en/docs/claude-code/mcp) [**MCP in Claude.ai** \\
\\
Enable MCP connectors for your team in Claude.ai.](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) [**MCP in Claude Desktop** \\
\\
Add MCP servers to Claude Desktop.](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)

</details>

<details>
<summary>model-context-protocol-mcp-cursor-docs</summary>

# Model Context Protocol (MCP)

## What is MCP?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) enables Cursor to connect to external tools and data sources.

### Why use MCP?

MCP connects Cursor to external systems and data. Instead of explaining your project structure repeatedly, integrate directly with your tools.

Write MCP servers in any language that can print to `stdout` or serve an HTTP endpoint - Python, JavaScript, Go, etc.

### How it works

MCP servers expose capabilities through the protocol, connecting Cursor to external tools or data sources.

Cursor supports three transport methods:

| Transport | Execution environment | Deployment | Users | Input | Auth |
| --- | --- | --- | --- | --- | --- |
| **`stdio`** | Local | Cursor manages | Single user | Shell command | Manual |
| **`SSE`** | Local/Remote | Deploy as server | Multiple users | URL to an SSE endpoint | OAuth |
| **`Streamable HTTP`** | Local/Remote | Deploy as server | Multiple users | URL to an HTTP endpoint | OAuth |

### Protocol support

Cursor supports these MCP protocol capabilities:

| Feature | Support | Description |
| --- | --- | --- |
| **Tools** | Supported | Functions for the AI model to execute |
| **Prompts** | Supported | Templated messages and workflows for users |
| **Resources** | Supported | Structured data sources that can be read and referenced |
| **Roots** | Supported | Server-initiated inquiries into URI or filesystem boundaries |
| **Elicitation** | Supported | Server-initiated requests for additional information from users |

## Installing MCP servers

### Using `mcp.json`

Configure custom MCP servers with a JSON file:

CLI Server - Node.js
```
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "mcp-server"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

CLI Server - Python
```
{
  "mcpServers": {
    "server-name": {
      "command": "python",
      "args": ["mcp-server.py"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

Remote Server
```
// MCP server using HTTP or SSE - runs on a server
{
  "mcpServers": {
    "server-name": {
      "url": "http://localhost:3000/mcp",
      "headers": {
        "API_KEY": "value"
      }
    }
  }
}
```

### STDIO server configuration

For STDIO servers (local command-line servers), configure these fields in your `mcp.json`:

| Field | Required | Description | Examples |
| --- | --- | --- | --- |
| **type** | Yes | Server connection type | `"stdio"` |
| **command** | Yes | Command to start the server executable. Must be available on your system path or contain its full path. | `"npx"`, `"node"`, `"python"`, `"docker"` |
| **args** | No | Array of arguments passed to the command | `["server.py", "--port", "3000"]` |
| **env** | No | Environment variables for the server | `{"API_KEY": "${env:api-key}"}` |
| **envFile** | No | Path to an environment file to load more variables | `".env"`, `"${workspaceFolder}/.env"` |

### Authentication

MCP servers use environment variables for authentication. Pass API keys and tokens through the config.

Cursor supports OAuth for servers that require it.

## Security considerations

When installing MCP servers, consider these security practices:

- **Verify the source**: Only install MCP servers from trusted developers and repositories
- **Review permissions**: Check what data and APIs the server will access
- **Limit API keys**: Use restricted API keys with minimal required permissions
- **Audit code**: For critical integrations, review the server's source code

Remember that MCP servers can access external services and execute code on your behalf. Always understand what a server does before installation.

</details>

<details>
<summary>prompts-model-context-protocol</summary>

**Protocol Revision**: 2025-06-18

The Model Context Protocol (MCP) provides a standardized way for servers to expose prompt
templates to clients. Prompts allow servers to provide structured messages and
instructions for interacting with language models. Clients can discover available
prompts, retrieve their contents, and provide arguments to customize them.

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#user-interaction-model)  User Interaction Model

Prompts are designed to be **user-controlled**, meaning they are exposed from servers to
clients with the intention of the user being able to explicitly select them for use.Typically, prompts would be triggered through user-initiated commands in the user
interface, which allows users to naturally discover and invoke available prompts.For example, as slash commands:https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/specification/2025-06-18/server/slash-command.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=7f003e36d881dd6f3e5b8cbdd85e5ca5However, implementors are free to expose prompts through any interface pattern that suits
their needs—the protocol itself does not mandate any specific user interaction
model.

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#capabilities)  Capabilities

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

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#protocol-messages)  Protocol Messages

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#listing-prompts)  Listing Prompts

To retrieve available prompts, clients send a `prompts/list` request. This operation
supports [pagination](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination).**Request:**

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

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#getting-a-prompt)  Getting a Prompt

To retrieve a specific prompt, clients send a `prompts/get` request. Arguments may be
auto-completed through [the completion API](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/completion).**Request:**

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

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#list-changed-notification)  List Changed Notification

When the list of available prompts changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:

```
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}

```

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#message-flow)  Message Flow

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#data-types)  Data Types

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#prompt)  Prompt

A prompt definition includes:

- `name`: Unique identifier for the prompt
- `title`: Optional human-readable name of the prompt for display purposes.
- `description`: Optional human-readable description
- `arguments`: Optional list of arguments for customization

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#promptmessage)  PromptMessage

Messages in a prompt can contain:

- `role`: Either “user” or “assistant” to indicate the speaker
- `content`: One of the following content types:

All content types in prompt messages support optional
[annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) for
metadata about audience, priority, and modification times.

#### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#text-content)  Text Content

Text content represents plain text messages:

```
{
  "type": "text",
  "text": "The text content of the message"
}

```

This is the most common content type used for natural language interactions.

#### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#image-content)  Image Content

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

#### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#audio-content)  Audio Content

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

#### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#embedded-resources)  Embedded Resources

Embedded resources allow referencing server-side resources directly in messages:

```
{
  "type": "resource",
  "resource": {
    "uri": "resource://example",
    "name": "example",
    "title": "My Example Resource",
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

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#error-handling)  Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

- Invalid prompt name: `-32602` (Invalid params)
- Missing required arguments: `-32602` (Invalid params)
- Internal errors: `-32603` (Internal error)

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#implementation-considerations)  Implementation Considerations

1. Servers **SHOULD** validate prompt arguments before processing
2. Clients **SHOULD** handle pagination for large prompt lists
3. Both parties **SHOULD** respect capability negotiation

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts\#security)  Security

Implementations **MUST** carefully validate all prompt inputs and outputs to prevent
injection attacks or unauthorized access to resources.

</details>

<details>
<summary>resources-model-context-protocol</summary>

**Protocol Revision**: 2025-06-18

The Model Context Protocol (MCP) provides a standardized way for servers to expose
resources to clients. Resources allow servers to share data that provides context to
language models, such as files, database schemas, or application-specific information.
Each resource is uniquely identified by a
[URI](https://datatracker.ietf.org/doc/html/rfc3986).

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#user-interaction-model)  User Interaction Model

Resources in MCP are designed to be **application-driven**, with host applications
determining how to incorporate context based on their needs.For example, applications could:

- Expose resources through UI elements for explicit selection, in a tree or list view
- Allow the user to search through and filter available resources
- Implement automatic context inclusion, based on heuristics or the AI model’s selectionhttps://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/specification/2025-06-18/server/resource-picker.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=133fa885ef6e9c2e20049da5c33f4386However, implementations are free to expose resources through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#capabilities)  Capabilities

Servers that support resources **MUST** declare the `resources` capability:

```
{
  "capabilities": {
    "resources": {
      "subscribe": true,
      "listChanged": true
    }
  }
}

```

The capability supports two optional features:

- `subscribe`: whether the client can subscribe to be notified of changes to individual
resources.
- `listChanged`: whether the server will emit notifications when the list of available
resources changes.

Both `subscribe` and `listChanged` are optional—servers can support neither,
either, or both:

```
{
  "capabilities": {
    "resources": {} // Neither feature supported
  }
}

```

```
{
  "capabilities": {
    "resources": {
      "subscribe": true // Only subscriptions supported
    }
  }
}

```

```
{
  "capabilities": {
    "resources": {
      "listChanged": true // Only list change notifications supported
    }
  }
}

```

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#protocol-messages)  Protocol Messages

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#listing-resources)  Listing Resources

To discover available resources, clients send a `resources/list` request. This operation
supports [pagination](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination).**Request:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "resources/list",
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
    "resources": [\
      {\
        "uri": "file:///project/src/main.rs",\
        "name": "main.rs",\
        "title": "Rust Software Application Main File",\
        "description": "Primary application entry point",\
        "mimeType": "text/x-rust"\
      }\
    ],
    "nextCursor": "next-page-cursor"
  }
}

```

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#reading-resources)  Reading Resources

To retrieve resource contents, clients send a `resources/read` request:**Request:**

```
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "resources/read",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}

```

**Response:**

```
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "contents": [\
      {\
        "uri": "file:///project/src/main.rs",\
        "name": "main.rs",\
        "title": "Rust Software Application Main File",\
        "mimeType": "text/x-rust",\
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"\
      }\
    ]
  }
}

```

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#resource-templates)  Resource Templates

Resource templates allow servers to expose parameterized resources using
[URI templates](https://datatracker.ietf.org/doc/html/rfc6570). Arguments may be
auto-completed through [the completion API](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/completion).**Request:**

```
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "resources/templates/list"
}

```

**Response:**

```
{
  "jsonrpc": "2.0",
  "id": 3,
  "result": {
    "resourceTemplates": [\
      {\
        "uriTemplate": "file:///{path}",\
        "name": "Project Files",\
        "title": "📁 Project Files",\
        "description": "Access files in the project directory",\
        "mimeType": "application/octet-stream"\
      }\
    ]
  }
}

```

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#list-changed-notification)  List Changed Notification

When the list of available resources changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:

```
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}

```

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#subscriptions)  Subscriptions

The protocol supports optional subscriptions to resource changes. Clients can subscribe
to specific resources and receive notifications when they change:**Subscribe Request:**

```
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///project/src/main.rs"
  }
}

```

**Update Notification:**

```
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///project/src/main.rs",
    "title": "Rust Software Application Main File"
  }
}

```

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#message-flow)  Message Flow

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#data-types)  Data Types

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#resource)  Resource

A resource definition includes:

- `uri`: Unique identifier for the resource
- `name`: The name of the resource.
- `title`: Optional human-readable name of the resource for display purposes.
- `description`: Optional description
- `mimeType`: Optional MIME type
- `size`: Optional size in bytes

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#resource-contents)  Resource Contents

Resources can contain either text or binary data:

#### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#text-content)  Text Content

```
{
  "uri": "file:///example.txt",
  "name": "example.txt",
  "title": "Example Text File",
  "mimeType": "text/plain",
  "text": "Resource content"
}

```

#### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#binary-content)  Binary Content

```
{
  "uri": "file:///example.png",
  "name": "example.png",
  "title": "Example Image",
  "mimeType": "image/png",
  "blob": "base64-encoded-data"
}

```

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#annotations)  Annotations

Resources, resource templates and content blocks support optional annotations that provide hints to clients about how to use or display the resource:

- **`audience`**: An array indicating the intended audience(s) for this resource. Valid values are `"user"` and `"assistant"`. For example, `["user", "assistant"]` indicates content useful for both.
- **`priority`**: A number from 0.0 to 1.0 indicating the importance of this resource. A value of 1 means “most important” (effectively required), while 0 means “least important” (entirely optional).
- **`lastModified`**: An ISO 8601 formatted timestamp indicating when the resource was last modified (e.g., `"2025-01-12T15:00:58Z"`).

Example resource with annotations:

```
{
  "uri": "file:///project/README.md",
  "name": "README.md",
  "title": "Project Documentation",
  "mimeType": "text/markdown",
  "annotations": {
    "audience": ["user"],
    "priority": 0.8,
    "lastModified": "2025-01-12T15:00:58Z"
  }
}

```

Clients can use these annotations to:

- Filter resources based on their intended audience
- Prioritize which resources to include in context
- Display modification times or sort by recency

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#common-uri-schemes)  Common URI Schemes

The protocol defines several standard URI schemes. This list not
exhaustive—implementations are always free to use additional, custom URI schemes.

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#https%3A%2F%2F)  https://

Used to represent a resource available on the web.Servers **SHOULD** use this scheme only when the client is able to fetch and load the
resource directly from the web on its own—that is, it doesn’t need to read the resource
via the MCP server.For other use cases, servers **SHOULD** prefer to use another URI scheme, or define a
custom one, even if the server will itself be downloading resource contents over the
internet.

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#file%3A%2F%2F)  file://

Used to identify resources that behave like a filesystem. However, the resources do not
need to map to an actual physical filesystem.MCP servers **MAY** identify file:// resources with an
[XDG MIME type](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14),
like `inode/directory`, to represent non-regular files (such as directories) that don’t
otherwise have a standard MIME type.

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#git%3A%2F%2F)  git://

Git version control integration.

### [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#custom-uri-schemes)  Custom URI Schemes

Custom URI schemes **MUST** be in accordance with [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986),
taking the above guidance in to account.

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#error-handling)  Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

- Resource not found: `-32002`
- Internal errors: `-32603`

Example error:

```
{
  "jsonrpc": "2.0",
  "id": 5,
  "error": {
    "code": -32002,
    "message": "Resource not found",
    "data": {
      "uri": "file:///nonexistent.txt"
    }
  }
}

```

## [​](https://modelcontextprotocol.io/specification/2025-06-18/server/resources\#security-considerations)  Security Considerations

1. Servers **MUST** validate all resource URIs
2. Access controls **SHOULD** be implemented for sensitive resources
3. Binary data **MUST** be properly encoded
4. Resource permissions **SHOULD** be checked before operations

</details>

<details>
<summary>scaling-your-ai-enterprise-architecture-with-mcp-systems</summary>

# Why MCP Breaks Old Enterprise AI Architectures

MCP is everywhere these days.

Scroll through any developer feed, and you’ll see tutorials on how to spin up an MCP server, plug it into your IDE, or connect it to Claude Desktop. It’s cool, it’s shiny, and it feels like the future.

But most tutorials stop at the basics. They show you how to connect one thing to another, but skip over why it’s worth your attention. The real beauty of MCP isn’t in the connection—it’s in **how it changes the way you design automations at scale**.

This piece isn’t another _“how to build a server”_ guide. It’s about why you might want MCP at the base of your systems. By the end, you’ll know what MCP _really_ brings to the table, and whether it’s worth starting with it on day one.

Most LLM projects start with a prompt or a hack. Ours starts with a use case and the solution architecture—and continues with a deep dive on how to implement it.

🔍 **The use case?** An assistant that reviews your pull requests before your teammates even get the chance. Fast, automated, and context-aware.

_Think of it as the code reviewer who never ghosts your PR, never nitpicks semicolons, and actually reads the diff._

In these series, we’re building **a production-ready PR reviewer assistant**—an LLM-powered system that listens for GitHub pull requests, analyzes them, and posts review summaries directly to Slack. It’s a real use case, with real integrations and real constraints.

[https://substackcdn.com/image/fetch/$s_!wGcX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb178a33-45df-45d5-99ae-2b8b6c5e2d46_1452x1348.png](https://substackcdn.com/image/fetch/$s_!wGcX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb178a33-45df-45d5-99ae-2b8b6c5e2d46_1452x1348.png) Figure 1: Architecting an Enterprise PR Reviewer with MCP

But what really matters is _how_ we’re building it—with **the Model Context Protocol (MCP)**, a standard that makes LLM systems modular, testable, and built to scale.

> 🧑‍💻 **This is a hands-on walkthrough, not just theory.** In this lesson, we break down the design decisions—and in the next, we dive into the code. _(If you're eager, you can [jump straight to the GitHub repo](https://github.com/your-org/your-pr-reviewer-assistant) and follow along as you read.)_

In this lesson, you’ll learn:

- What MCP is and the problem it solves in real-world AI systems

- How its core architecture of clients, hosts, and servers fits together

- How to build a PR reviewer assistant and put MCP into action

- When MCP is the right choice compared to traditional LLM setups

## 1\. What is MCP really? (and why should you care?)

AI systems start simple, but they get messy fast. Add a few tools, connect some APIs, and suddenly you're dealing with brittle integrations and custom glue code everywhere.

Every framework, SDK, or service seems to define its own tool format, its own way of handling inputs and outputs, its own undocumented conventions. One expects OpenAPI-style schemas, another wants function signatures embedded in JSON, a third relies on hardcoded Python decorators with custom parsing logic.

Even calling two different tools that “do the same thing” can require completely different invocation logic.

The result? **Nothing fits together.**

You end up writing adapters on top of wrappers on top of hacks. Tools can’t be reused. Workflows become tightly coupled to specific implementations. Testing becomes a nightmare. Scaling or swapping components feels like performing surgery on spaghetti.

This fragmentation isn't just annoying—it’s the core bottleneck for building maintainable, extensible LLM systems.

That’s **the problem** the **Model Context Protocol (MCP)** is designed to solve.

MCP is a **protocol** , a formal standard for building modular, message-driven LLM systems. It’s not just a library or framework. It’s a way to architect AI software that doesn’t collapse under its own weight.

It defines how clients, hosts, and servers communicate, with clear roles and structured messages, so your workflows stay composable, testable, and scalable by default.

**Think of it like HTTP:**

- The protocol defines how things should talk

- The implementation is just how you choose to use it

- Multiple systems can interact without writing custom integration code for each one

**MCP doesn’t bring any new features**.

What it brings is **structure**. It simply formalizes what we were already doing with tool-using agents in a form that scales like real software. It captures the patterns that emerged naturally as LLM systems matured and gives us a shared standard for building them.

So instead of reinventing that architecture for every project, MCP gives you a consistent, interoperable way to do it right, from day one.

If you want your AI workflows to scale, evolve, and stay sane, **you need to think in protocols — not just prompts.**

[https://substackcdn.com/image/fetch/$s_!srDy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F143a290b-afed-4ca8-9f70-c0b7fa8f1e5f_1396x1274.png](https://substackcdn.com/image/fetch/$s_!srDy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F143a290b-afed-4ca8-9f70-c0b7fa8f1e5f_1396x1274.png) Figure 2: Tool integration before and after MCP

## 2\. Traditional agent setups vs MCP-based architecture

Early agent builds are quick wins: wire in a few tools, get results, move on. But over time, those shortcuts turn into tangled code that’s hard to maintain or extend.

Think of it as inline, **monolithic agents versus MCP**, which enforces a **clean separation of concerns**. That difference in approach becomes clear when you look at how tools are integrated and managed.

**The old way:**

- Tools are hardcoded into the agent loop (e.g., a `summarize_diff()` call sitting inside the logic)

- No clear abstraction, so changes mean editing core code _( **hint**: yep, the Open/Closed Principle we all nodded to in class!)_

- Scaling is painful, and reusing tools across different frameworks is nearly impossible

**The MCP way:**

- Tools, resources and prompts sit on separate servers, decoupled from core logic

- A standard interface keeps agents open for extension but closed for modification, letting you plug in multiple servers

- The same interface makes tools reusable across frameworks, simplifying scaling and experimentation

This separation of concerns keeps your workflows clean, tools reusable, and systems easier to evolve as your needs change.

## 3\. How MCP Works

So how does MCP actually pull this off?

It starts with a simple idea: **every piece of the system has a clear job.**

At its core, MCP uses a role-based architecture. Every component in an MCP-powered app plays one of three roles:

- **Host** – the “agent brain.” It gathers context, decides which tools to use, and coordinates the workflow. Examples include a Python app, an IDE, or Claude Desktop.

- **Client** – initiates tasks and talks directly to servers, keeping 1:1 connection with each MCP Server.

- **Server** – exposes tools, resources, and prompts for the AI Applications to use.

Think of it like this: **clients ask, hosts decide, servers deliver.**

Now let’s zoom in on one of the most common things an MCP server does — tool calling — and see how these pieces interact together.

[https://substackcdn.com/image/fetch/$s_!sXci!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0a0f37e-1e0c-4c77-a21e-0ae6fcefe560_1222x1058.png](https://substackcdn.com/image/fetch/$s_!sXci!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0a0f37e-1e0c-4c77-a21e-0ae6fcefe560_1222x1058.png) Figure 3: How tool calling works with MCP

First, the MCP Client asks the MCP Server what tools are available.

Once the list comes back, the LLM Gateway (your agent logic) selects the right tool and fills in the arguments — for example, asking to run `summarize_diff`. The client then sends that request to the server.

The MCP Server executes the requested tool and sends the result back. The client passes it to the LLM, which uses it to continue the workflow and generate the final response.

Because MCP defines a common protocol, **every server speaks the same “language”.**

Your host and client don’t need to know how each server works internally. They simply send a request and get back a response in a standard format.

This means you can swap one server for another — maybe replace your PDF processor or change your GitHub integration — without touching the rest of your system.

You can also add new servers without rewriting your core logic, letting your system grow over time instead of getting stuck with one-off integrations.

To understand how this plays out in practice, let’s take a look at the full MCP architecture involving multiple servers:

[https://substackcdn.com/image/fetch/$s_!8lRP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf35c8d7-a897-423c-9333-9e18fde72c1c_1098x1002.png](https://substackcdn.com/image/fetch/$s_!8lRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbf35c8d7-a897-423c-9333-9e18fde72c1c_1098x1002.png) Figure 4: The MCP Architecture

This diagram shows the MCP architecture in practice, where a single Host is hooked to multiple Servers across the system.

When you’re working with multiple servers, the overall flow stays familiar — but with one important change: the Host now needs to route each request to the server that owns the right tool for the job.

The Host still drives the process. It uses an LLM to reason about the task, then passes the request through its connected MCP Client to the appropriate server. Since each server exposes different tools, selecting the right one matters.

As we covered earlier, servers handle real functionality. They offer tools like `summarize_diff`, `get_jira_issue`, or `extract_keywords`, which the Host can call through standard MCP messages.

But tool execution is just part of the story. Let’s explore what else servers can provide.

#### What can servers provide?

Most articles oversimplify MCP servers as “just tools.”

That’s not true. **Servers are much more than tool endpoints.**

They can expose three types of things:

- **Tools** – functions to call, like `send_slack_message`, `summarize_diff`, or `fetch_weather`

- **Resources** – data to retrieve, such as files from a local file system or an internal database

- **Prompts** – pre-defined templates or system messages that the client can fill and use for LLM calls

These servers act like modular building blocks, each focused on a single purpose but all speaking the same MCP “language.”

#### What protocol do they use?

MCP keeps things simple under the hood: **it’s all built on JSON‑RPC**.

This is a lightweight protocol commonly used in microservices for server-to-server communication, where everything is encoded as JSON and exchanged over a simple request-response format.

Check out a basic example of a JSON-RPC call to a tool named `summarize_code`:

```
{
  "jsonrpc": "2.0",
  "method": "summarize_code",
  "params": {
    "file_path": "src/utils/helpers.py"
  },
  "id": 1
}
```

This standard defines how clients and servers exchange messages, but it doesn’t lock you into a single transport. You can choose the one that best fits your environment:

- **stdio (great for development)**

  - The client spawns the server as a subprocess and communicates over `stdin/stdout`

  - Fast and synchronous

  - Perfect for running servers as Python modules or quick local testing
- **Streamed HTTP (production‑ready)**

  - Allows servers to respond with standard HTTP responses or streaming data on demand

  - Supports optional session IDs for state management and recovery

  - Flexible enough for anything from serverless functions to full-scale AI applications

  - Replaces the older HTTP + SSE approach with better reliability and session recovery

> 🔗 **Learn more about the protocol in the [MCP transport specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)**

#### How can we secure them?

Now that we know they provide the actual data … how do we secure them?

When you expose an MCP server to the outside world, you’re effectively opening a door into your system.

If someone gets unauthorized access, they could:

- Trigger tools they shouldn’t have access to (think deploying code or deleting files)

- Pull sensitive data from resources

- Abuse prompts for unintended automation

This isn’t theoretical — any open endpoint can be a target, and MCP servers are no different.

**The go‑to: OAuth 2.0**

The most common way to secure these servers is **OAuth 2.0**. Instead of handing out one static token that works for everyone (and everything), OAuth issues **scoped, time‑limited tokens** tied to specific users or systems.

That means:

- Each user or client authenticates and gets a unique token.

- Tokens can expire or be revoked, limiting long‑term risk.

- Access can be scoped so one user might only read data while another can run administrative tools.

This is why OAuth 2.0 is the standard for production MCP deployments — it’s battle‑tested, flexible, and integrates with many identity providers.

> 🔐 **Want to go deeper?** Check out [this guide on securing MCP servers with OAuth 2.0](https://www.infracloud.io/blogs/securing-mcp-servers/) for real-world tips and best practices.

To visualize how this works, here’s what a typical **OAuth 2.0 flow** looks like between an MCP Host and a remote MCP Server:

[https://substackcdn.com/image/fetch/$s_!Zgjo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd1bd4b0-8b99-4566-8f62-7332c1ca3087_1424x1240.png](https://substackcdn.com/image/fetch/$s_!Zgjo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdd1bd4b0-8b99-4566-8f62-7332c1ca3087_1424x1240.png) Figure 5: Using OAuth 2.0 with MCP

Let’s briefly go through each step in the diagram:

1. The **MCP Host** authenticates with the **Authorization Server** using its `client_id` and `client_secret`.

2. It receives a **scoped access token**—not a catch-all credential, but one limited to only what this host is allowed to do (e.g., call specific tools, not all tools).

3. The MCP Host sends a request to the **Remote MCP Server**, including the token in the `Authorization` header.

4. The MCP Server validates the token.

5. If valid and authorized, the server executes the requested tool and returns the result.

This setup ensures fine-grained access control and keeps your system secure.

## 4\. Designing The PR Reviewer Assistant with MCP

Now let’s break down a real use case to make the mental model stick.

Imagine you want an AI teammate that reviews pull requests the moment they’re opened — and delivers feedback to your team without you lifting a finger. No waiting on busy reviewers, no half-finished feedback, and no hunting through Asana tickets for missing context.

We’ve all been there — the reviewer staring at a thousand-line diff wondering where to start, while the reviewee refreshes the page like it’s a flight status update.

So, how would you actually design something like this?

The diagram below shows one way to wire it up using MCP:

[https://substackcdn.com/image/fetch/$s_!c4Up!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe135b8d-c18b-4bd2-963f-5c940b294e95_1440x1380.png](https://substackcdn.com/image/fetch/$s_!c4Up!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe135b8d-c18b-4bd2-963f-5c940b294e95_1440x1380.png) Figure 6: Data flow for the PR Reviewer Agent

In our use case, the **MCP Host** is a FastAPI app powered by a Gemini LLM, wired into your GitHub repo through a webhook. It’s the component that reacts the instant a PR appears and decides exactly what should happen next.

The host runs a single **MCP Client** connected to the **MCP Global Server**, which keeps every MCP server in one place. It organizes tools, prompts and resources, tags them, and makes it easy to find exactly what you need without going through scattered configs.

For this setup, four MCP servers handle the heavy lifting — each with a specific job:

- **GitHub MCP Server** – The primary source for PR context. It pulls metadata, file changes, and code diffs so the review has the full picture of what’s being proposed.

- **Asana MCP Server** – Provides the task-level context behind the PR. It surfaces linked tasks and requirements so you can tell whether the changes actually deliver what was promised.

- **Agent Scope MCP Server** – The starting point for the review logic. This is where the host retrieves the initial PR review prompt from, ensuring the LLM knows exactly how to frame and approach the evaluation.

- **Slack MCP Server** – Handles the final step of delivery. It posts the completed review into the right Slack channel, ensuring the feedback is instantly visible where the team already communicates.

**Now that we understand each component, let’s walk through the flow:**

1. A developer opens a pull request in GitHub.

2. GitHub fires a PR `opened` event to our FastAPI host with all the PR metadata.

3. The host asks the Agent Scope MCP Server (via the Global Server) for the right PR review prompt.

4. The host sends the PR data and prompt to Gemini, asking which tools to run.

5. Gemini returns a plan — e.g., fetch PR content, grab linked tasks.

6. The host calls the Global MCP Server to invoke the required tools and gather the needed data.

7. Each MCP server talks to its external API, executes the job, and sends the results back.

8. The host sends those results to Gemini to create the final review.

9. The review goes to the Slack MCP Server, which posts it directly to the team.

> _**Note**_: _In some cases, Gemini may request additional tool calls in a subsequent pass, meaning steps **5–9** can loop until all required data is gathered and the review is complete._

And just like that, your PR is reviewed, contextualized, and shared — before you’ve even switched tabs.

## 5\. Why This Scales (and Why You’ll Thank Yourself Later)

MCP isn’t just clean architecture — it’s a future-proof way to build AI systems that won’t collapse under their own complexity.

This scales because every component follows the same protocol. Adding a new capability doesn’t mean rewriting everything else — it’s simply a matter of plugging in another piece.

Instead of a single, heavy system that grows harder to maintain, you’re building small, independent units that fit together naturally.

Now picture this.

[https://substackcdn.com/image/fetch/$s_!zFEo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedccc09a-ac2b-42b9-a023-7d73c8d6c7cb_1420x1320.png](https://substackcdn.com/image/fetch/$s_!zFEo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fedccc09a-ac2b-42b9-a023-7d73c8d6c7cb_1420x1320.png) Figure 7: Enterprise DevEx system designed with MCP

Say your enterprise wants three developer-experience automations: a PR reviewer, an incident response bot, and a research summarizer. In most setups, each would need its own integrations with GitHub, Slack, Jira, and other services.

With MCP, they all connect to the same set of shared servers. If one service gets a lot of traffic — like Slack — you can simply spin up another server of the same type to handle the load. And the same GitHub or Jira server can be reused across all AI applications, no matter how many you add.

All of this means you get some very real perks.

**Reusability.** You can swap Claude for OpenAI or Gemini without touching the rest of your workflow. The same Slack server you built for one project? You can reuse it across ten others. Need to support multiple products? Just plug in a different map server for each one — no glue code, no duplication.

**Reliability.** Because everything runs through a standard interface, every step is traceable. You can see which server ran what tool, with what inputs and outputs. And since servers are stateless and mockable, writing tests becomes straightforward. No more faking end-to-end flows just to check if a tool works.

**Scalability.** And when you’re ready to scale — really scale — you’re not locked into one machine or repo. Servers can live on separate machines, in different teams, even across org boundaries. It’s distributed by design.

**Cost efficiency.** Shared servers mean you’re not rebuilding the same integrations repeatedly. You save on engineering time, reduce infrastructure costs, and can move workloads to cheaper environments without disruption.

> **MCP brings a microservices mindset to AI development**.

It turns your LLM workflows into composable infrastructure — not just clever wrappers around chat models.

## Conclusion

So we’ve gone from “MCP is a buzzword” to “I know how to architect my next AI system with MCP.”

Theory time is over — now it’s time to make it real.

</details>

<details>
<summary>stop-vibe-testing-your-mcp-server</summary>

In Part 2A of this course (Lessons 12-14), we laid out the system design for our research agent, Nova. We decided to split the research and writing tasks into two separate agents, keeping Nova’s orchestration thin and pushing the heavy lifting into a set of portable, reusable tools. To achieve this, we chose the Model Context Protocol (MCP) as our interoperability layer and FastMCP as our Python implementation.

This lesson marks the beginning of Part 2B, where we shift from design to hands-on implementation. We will turn our architectural diagrams into a running system. By the end of this lesson, you will run a complete MCP server and client, discover the capabilities they expose, and execute your first tool calls—all using the actual code from the `research_agent_part_2` project.

### MCP in Short: Primitives, Transports, and Why It Matters

Before we dive into the code, let’s have a quick recap of MCP’s core concepts. MCP is an open protocol designed to connect LLM applications to external tools, data, and services over a standardized JSON-RPC interface. It’s built on three main primitives:

*   **Tools**: These are actions that can have side effects, like writing a file, calling an API, or running a computation.
*   **Resources**: These provide read-only access to data, such as files, system information, or database records.
*   **Prompts**: These are reusable, server-hosted instruction blocks that can define entire workflows or recipes, ensuring any client can initiate the same process consistently.

Clients interact with an MCP server by first discovering its capabilities (e.g., `list_tools`, `list_resources`, `list_prompts`) and then calling them as needed.

Communication between the client and server happens over a **transport**. For our project, we will focus on the two transports that FastMCP supports out of the box and that our agent uses:

1.  **In-Memory**: The client and server run in the same process. This is extremely fast, has no network overhead, and is perfect for development, testing, and running in environments like Jupyter notebooks.
2.  **stdio**: The client spawns the server as a separate subprocess and communicates with it over standard input/output streams (`stdin`/`stdout`). This model mirrors how external applications, like IDEs (e.g., Cursor), integrate with MCP servers, providing a more production-like setup.

Using MCP gives our research agent loose coupling (tools can evolve independently of the agent), token efficiency (the agent’s LLM only needs to decide *what* to do, not how to do it), and portability (our tools are instantly available to any MCP-compliant client). For a deeper dive into these architectural decisions, you can refer back to Lessons 12-14.

### Quickstart in the Notebook (In-Memory)

Let's get our hands dirty. The quickest way to see our system in action is to run the client directly inside our course notebook. This setup uses the **in-memory** transport, where the MCP server is instantiated and run within the same Python kernel as the client.

Assuming you've set up your environment and configured your Gemini API key as described in the course administration guide, you can start the client. When it launches, you'll see a startup banner listing the available capabilities:

```
INFO:     MCP Server version 0.1.0
INFO:     - 11 tools available.
INFO:     - 2 resources available.
INFO:     - 1 prompt available.
INFO:     - Type '/quit' to exit.
INFO:     - Type '/tools', '/resources', or '/prompts' to list available capabilities.
INFO:     - Type '/model-thinking-switch' to toggle model thinking.
INFO:     - Type '/prompt/<prompt_name>' to load a prompt.
INFO:     - Type '/resource/<resource_uri>' to view a resource.
```

This banner is the result of the client performing **capability discovery**—it queries the server for all the tools, resources, and prompts it exposes.

Now, you can interact with the agent. Try typing the following commands one by one:

1.  `Hello! Who are you?`
    *   The agent will introduce itself as a research assistant.
2.  `/tools`
    *   This command lists all 11 tools registered on the server, along with their descriptions and parameters.
3.  `/resources`
    *   This lists the available resources. You should see `system://memory`.
4.  `/resource/system://memory`
    *   This command reads the `system://memory` resource and displays current memory usage statistics for the server process.
5.  `/quit`
    *   This will shut down the client.

You've just run a live MCP client, discovered its capabilities, and interacted with both the agent's LLM and a server-side resource.

### How the MCP Server is Organized

Now that you've seen the system run, let's look at how the server is structured. The server's code lives in the `src/mcp_server/` directory.

*   **`server.py`**: This is the main entry point. It creates a `FastMCP` app instance and registers the routers that expose our capabilities.
*   **`routers/`**: This directory contains `tools.py`, `resources.py`, and `prompts.py`. Each file is responsible for importing the actual implementations and registering them with the FastMCP app using decorators.
*   **`tools/`, `resources/`, `prompts/`**: These directories contain the business logic for each capability. For example, `tools/file_tools.py` contains the Python functions that perform file operations.
*   **`config/settings.py`**: This file uses `pydantic-settings` to manage configuration like the server's name, version, API keys, and model choices.

Let's examine how one of each primitive type is registered.

#### Tool Registration

In `src/mcp_server/routers/tools.py`, we register the `extract_guidelines_urls` tool, which is implemented in `src/mcp_server/tools/guidelines_tools.py`. The registration looks like this:

```python
from ..tools.guidelines_tools import extract_guidelines_urls_tool
# ... other imports

@mcp.tool(
    name="extract_guidelines_urls",
    description="Extracts URLs from research guidelines files.",
    # ... other parameters
)
async def extract_guidelines_urls(
    research_directory: str,
    # ... other parameters
) -> dict:
    """Extracts URLs from research guidelines files."""
    return await extract_guidelines_urls_tool(
        research_directory=research_directory,
        # ... other parameters
    )
```

The `@mcp.tool()` decorator exposes the function to any connected client. This specific tool reads guideline files from a specified directory and writes the extracted URLs to a new file at `.nova/guidelines_filenames.json`. This is a classic **Tool**—it performs an action with a side effect (writing a file).

#### Resource Registration

In `src/mcp_server/routers/resources.py`, we register the `system://memory` resource:

```python
from ..resources.system_resources import get_memory_resource
# ... other imports

@mcp.resource("system://memory")
async def system_memory() -> dict:
    """Returns memory usage statistics."""
    return await get_memory_resource()
```

The `@mcp.resource()` decorator makes the function's return value available at the specified URI. Unlike a tool, a resource is read-only and should not have side effects.

#### Prompt Registration

Finally, in `src/mcp_server/routers/prompts.py`, we register our main workflow prompt:

```python
from ..prompts.research_instructions_prompt import research_instructions_prompt
# ... other imports

@mcp.prompt("full_research_instructions_prompt")
def full_research_instructions_prompt() -> str:
    """The main prompt that drives the research agent's workflow."""
    return research_instructions_prompt
```

The `@mcp.prompt()` decorator exposes a string—in this case, the detailed, multi-step instructions for conducting research. By hosting the prompt on the server, we ensure that any MCP client, whether it's our command-line tool or a third-party application, can initiate the exact same research workflow simply by loading this prompt.

### The MCP Client: Transports, Discovery, and the Agent Loop

The client code, located in `src/client/`, is responsible for connecting to the server, parsing user input, and orchestrating the agent's logic.

#### Transports and Run Modes

The client in `client.py` supports two run modes, controlled by the `--transport` command-line argument:

1.  `--transport in-memory` (default): The client imports the `create_mcp_server` function from the server code and passes the server instance directly to the `fastmcp.Client`. This is what the notebook uses.
2.  `--transport stdio`: The client launches the server as a separate process (`uv run -m src.server --transport stdio`) and communicates with it over standard I/O. This is how you'll run it from the terminal for a more realistic setup.

#### Capability Discovery and Command Parsing

Upon startup, the client calls `get_capabilities_from_mcp_client()`, which uses the `client.list_tools()`, `client.list_resources()`, and `client.list_prompts()` methods to query the server. The results are then printed in the startup banner we saw earlier.

The `parse_user_input()` function then routes user input. If the input starts with a `/`, it's treated as a command (like `/tools` or `/quit`). If not, it's passed to the agent loop to be processed by the LLM.

#### The Agent Loop

The core of the client is the `handle_agent_loop()` function. This is where the ReAct-style reasoning occurs:

1.  It builds a configuration for the LLM, dynamically including the list of available MCP tools as function declarations.
2.  It sends the current conversation history to the LLM.
3.  If the LLM's response includes a request to call a function (a tool), the client verifies that it's a valid MCP tool.
4.  It executes the tool by calling `client.call_tool(name, args)` and appends the result to the conversation history. The loop then continues, sending the updated history back to the LLM.
5.  If the LLM responds without a function call, the client treats it as the final answer, prints it to the user, and the loop terminates for that turn.

This loop cleanly separates the LLM's role (deciding *what* to do) from the tools' role (doing the work).

### Try It in the Terminal: Two Run Modes

Now, let's run the full client-server application from your terminal.

First, run it using the **in-memory** transport. This is the default, so you don't need to specify the transport.

```bash
uv run -m src.client
```

You should see the same startup banner as in the notebook.

Next, run it using the **stdio** transport. This will launch a separate server process in the background.

```bash
uv run -m src.client --transport stdio
```

The behavior from your perspective will be identical, but you are now communicating between two separate processes, just as an external IDE would.

In either mode, try out the following commands:

*   `/tools`: See the full list of 11 tools available for research tasks.
*   `/resources`: See the two available resources.
*   `/prompts`: See the one available workflow prompt.
*   `/model-thinking-switch`: This toggles the agent's "thinking" traces on and off. As we discussed in Lesson 14, this is a practical application of managing reasoning budgets. Try asking a question with it on and off to see the difference.

### Conclusion

In this lesson, you successfully ran a complete MCP-based agent system. You stood up an MCP server that exposes tools, resources, and prompts, and you used an MCP client to connect to it using both in-memory and stdio transports. You learned how to discover capabilities, execute a resource call, and inspect the structure of both the server and client code.

This foundation is crucial for the upcoming lessons, where we will put this system to work.

*   In **Lesson 17**, we will load and use the `full_research_instructions_prompt` to kick off the full research workflow, implementing the tools for ingesting guidelines and processing URLs.
*   In **Lesson 18 and 19**, we will continue implementing the remaining tools, including those for web scraping, data curation, and handling human-in-the-loop decision points, culminating in the final `research.md` artifact.
*   Later, in **Part 3**, we will return to this system to add observability with Opik and discuss security hardening for production environments.

</details>

<details>
<summary>tools-model-context-protocol</summary>

**Protocol Revision**: 2025-06-18

The Model Context Protocol (MCP) allows servers to expose tools that can be invoked by
language models. Tools enable models to interact with external systems, such as querying
databases, calling APIs, or performing computations. Each tool is uniquely identified by
a name and includes metadata describing its schema.

## User Interaction Model

Tools in MCP are designed to be **model-controlled**, meaning that the language model can
discover and invoke tools automatically based on its contextual understanding and the
user’s prompts.However, implementations are free to expose tools through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.

For trust & safety and security, there **SHOULD** always
be a human in the loop with the ability to deny tool invocations.Applications **SHOULD**:

- Provide UI that makes clear which tools are being exposed to the AI model
- Insert clear visual indicators when tools are invoked
- Present confirmation prompts to the user for operations, to ensure a human is in the
loop

## Capabilities

Servers that support tools **MUST** declare the `tools` capability:

```
{
  "capabilities": {
    "tools": {
      "listChanged": true
    }
  }
}

```

`listChanged` indicates whether the server will emit notifications when the list of
available tools changes.

## Protocol Messages

### Listing Tools

To discover available tools, clients send a `tools/list` request. This operation supports
[pagination](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination).**Request:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
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
    "tools": [\
      {\
        "name": "get_weather",\
        "title": "Weather Information Provider",\
        "description": "Get current weather information for a location",\
        "inputSchema": {\
          "type": "object",\
          "properties": {\
            "location": {\
              "type": "string",\
              "description": "City name or zip code"\
            }\
          },\
          "required": ["location"]\
        }\
      }\
    ],
    "nextCursor": "next-page-cursor"
  }
}

```

### Calling Tools

To invoke a tool, clients send a `tools/call` request:**Request:**

```
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
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
    "content": [\
      {\
        "type": "text",\
        "text": "Current weather in New York:\nTemperature: 72°F\nConditions: Partly cloudy"\
      }\
    ],
    "isError": false
  }
}

```

### List Changed Notification

When the list of available tools changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:

```
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}

```

## Message Flow

## Data Types

### Tool

A tool definition includes:

- `name`: Unique identifier for the tool
- `title`: Optional human-readable name of the tool for display purposes.
- `description`: Human-readable description of functionality
- `inputSchema`: JSON Schema defining expected parameters
- `outputSchema`: Optional JSON Schema defining expected output structure
- `annotations`: optional properties describing tool behavior

For trust & safety and security, clients **MUST** consider
tool annotations to be untrusted unless they come from trusted servers.

### Tool Result

Tool results may contain [**structured**](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#structured-content) or **unstructured** content.**Unstructured** content is returned in the `content` field of a result, and can contain multiple content items of different types:

All content types (text, image, audio, resource links, and embedded resources)
support optional
[annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) that
provide metadata about audience, priority, and modification times. This is the
same annotation format used by resources and prompts.

#### Text Content

```
{
  "type": "text",
  "text": "Tool result text"
}

```

#### Image Content

```
{
  "type": "image",
  "data": "base64-encoded-data",
  "mimeType": "image/png"
  "annotations": {
    "audience": ["user"],
    "priority": 0.9
  }

}

```

This example demonstrates the use of an optional Annotation.

#### Audio Content

```
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}

```

#### Resource Links

A tool **MAY** return links to [Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources), to provide additional context
or data. In this case, the tool will return a URI that can be subscribed to or fetched by the client:

```
{
  "type": "resource_link",
  "uri": "file:///project/src/main.rs",
  "name": "main.rs",
  "description": "Primary application entry point",
  "mimeType": "text/x-rust",
  "annotations": {
    "audience": ["assistant"],
    "priority": 0.9
  }
}

```

Resource links support the same [Resource annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) as regular resources to help clients understand how to use them.

Resource links returned by tools are not guaranteed to appear in the results
of a `resources/list` request.

#### Embedded Resources

[Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources) **MAY** be embedded to provide additional context
or data using a suitable [URI scheme](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#common-uri-schemes). Servers that use embedded resources **SHOULD** implement the `resources` capability:

```
{
  "type": "resource",
  "resource": {
    "uri": "file:///project/src/main.rs",
    "title": "Project Rust Main File",
    "mimeType": "text/x-rust",
    "text": "fn main() {\n    println!(\"Hello world!\");\n}",
    "annotations": {
      "audience": ["user", "assistant"],
      "priority": 0.7,
      "lastModified": "2025-05-03T14:30:00Z"
    }
  }
}

```

Embedded resources support the same [Resource annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) as regular resources to help clients understand how to use them.

#### Structured Content

**Structured** content is returned as a JSON object in the `structuredContent` field of a result.For backwards compatibility, a tool that returns structured content SHOULD also return the serialized JSON in a TextContent block.

#### Output Schema

Tools may also provide an output schema for validation of structured results.
If an output schema is provided:

- Servers **MUST** provide structured results that conform to this schema.
- Clients **SHOULD** validate structured results against this schema.

Example tool with output schema:

```
{
  "name": "get_weather_data",
  "title": "Weather Data Retriever",
  "description": "Get current weather data for a location",
  "inputSchema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City name or zip code"
      }
    },
    "required": ["location"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "temperature": {
        "type": "number",
        "description": "Temperature in celsius"
      },
      "conditions": {
        "type": "string",
        "description": "Weather conditions description"
      },
      "humidity": {
        "type": "number",
        "description": "Humidity percentage"
      }
    },
    "required": ["temperature", "conditions", "humidity"]
  }
}

```

Example valid response for this tool:

```
{
  "jsonrpc": "2.0",
  "id": 5,
  "result": {
    "content": [\
      {\
        "type": "text",\
        "text": "{\"temperature\": 22.5, \"conditions\": \"Partly cloudy\", \"humidity\": 65}"\
      }\
    ],
    "structuredContent": {
      "temperature": 22.5,
      "conditions": "Partly cloudy",
      "humidity": 65
    }
  }
}

```

Providing an output schema helps clients and LLMs understand and properly handle structured tool outputs by:

- Enabling strict schema validation of responses
- Providing type information for better integration with programming languages
- Guiding clients and LLMs to properly parse and utilize the returned data
- Supporting better documentation and developer experience

## Error Handling

Tools use two error reporting mechanisms:

1. **Protocol Errors**: Standard JSON-RPC errors for issues like: - Unknown tools
   - Invalid arguments
   - Server errors
2. **Tool Execution Errors**: Reported in tool results with `isError: true`: - API failures
   - Invalid input data
   - Business logic errors

Example protocol error:

```
{
  "jsonrpc": "2.0",
  "id": 3,
  "error": {
    "code": -32602,
    "message": "Unknown tool: invalid_tool_name"
  }
}

```

Example tool execution error:

```
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [\
      {\
        "type": "text",\
        "text": "Failed to fetch weather data: API rate limit exceeded"\
      }\
    ],
    "isError": true
  }
}

```

## Security Considerations

1. Servers **MUST**: - Validate all tool inputs
   - Implement proper access controls
   - Rate limit tool invocations
   - Sanitize tool outputs
2. Clients **SHOULD**: - Prompt for user confirmation on sensitive operations
   - Show tool inputs to the user before calling the server, to avoid malicious or
     accidental data exfiltration
   - Validate tool results before passing to LLM
   - Implement timeouts for tool calls
   - Log tool usage for audit purposes

</details>

<details>
<summary>transports-model-context-protocol</summary>

**Protocol Revision**: 2025-06-18

MCP uses JSON-RPC to encode messages. JSON-RPC messages **MUST** be UTF-8 encoded.The protocol currently defines two standard transport mechanisms for client-server
communication:

1. [stdio](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#stdio), communication over standard in and standard out
2. [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http)

Clients **SHOULD** support stdio whenever possible.It is also possible for clients and servers to implement
[custom transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#custom-transports) in a pluggable fashion.

## stdio

In the **stdio** transport:

- The client launches the MCP server as a subprocess.
- The server reads JSON-RPC messages from its standard input ( `stdin`) and sends messages
to its standard output ( `stdout`).
- Messages are individual JSON-RPC requests, notifications, or responses.
- Messages are delimited by newlines, and **MUST NOT** contain embedded newlines.
- The server **MAY** write UTF-8 strings to its standard error ( `stderr`) for logging
purposes. Clients **MAY** capture, forward, or ignore this logging.
- The server **MUST NOT** write anything to its `stdout` that is not a valid MCP message.
- The client **MUST NOT** write anything to the server’s `stdin` that is not a valid MCP
message.

## Streamable HTTP

This replaces the [HTTP+SSE\\
transport](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports#http-with-sse) from
protocol version 2024-11-05. See the [backwards compatibility](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#backwards-compatibility)
guide below.

In the **Streamable HTTP** transport, the server operates as an independent process that
can handle multiple client connections. This transport uses HTTP POST and GET requests.
Server can optionally make use of
[Server-Sent Events](https://en.wikipedia.org/wiki/Server-sent_events) (SSE) to stream
multiple server messages. This permits basic MCP servers, as well as more feature-rich
servers supporting streaming and server-to-client notifications and requests.The server **MUST** provide a single HTTP endpoint path (hereafter referred to as the
**MCP endpoint**) that supports both POST and GET methods. For example, this could be a
URL like `https://example.com/mcp`.

#### Security Warning

When implementing Streamable HTTP transport:

1. Servers **MUST** validate the `Origin` header on all incoming connections to prevent DNS rebinding attacks
2. When running locally, servers **SHOULD** bind only to localhost (127.0.0.1) rather than all network interfaces (0.0.0.0)
3. Servers **SHOULD** implement proper authentication for all connections

Without these protections, attackers could use DNS rebinding to interact with local MCP servers from remote websites.

### Sending Messages to the Server

Every JSON-RPC message sent from the client **MUST** be a new HTTP POST request to the
MCP endpoint.

1. The client **MUST** use HTTP POST to send JSON-RPC messages to the MCP endpoint.
2. The client **MUST** include an `Accept` header, listing both `application/json` and
`text/event-stream` as supported content types.
3. The body of the POST request **MUST** be a single JSON-RPC _request_, _notification_, or _response_.
4. If the input is a JSON-RPC _response_ or _notification_:

   - If the server accepts the input, the server **MUST** return HTTP status code 202
     Accepted with no body.
   - If the server cannot accept the input, it **MUST** return an HTTP error status code
     (e.g., 400 Bad Request). The HTTP response body **MAY** comprise a JSON-RPC _error_
     _response_ that has no `id`.
5. If the input is a JSON-RPC _request_, the server **MUST** either
return `Content-Type: text/event-stream`, to initiate an SSE stream, or
`Content-Type: application/json`, to return one JSON object. The client **MUST**
support both these cases.
6. If the server initiates an SSE stream:
   - The SSE stream **SHOULD** eventually include JSON-RPC _response_ for the
     JSON-RPC _request_ sent in the POST body.
   - The server **MAY** send JSON-RPC _requests_ and _notifications_ before sending the
     JSON-RPC _response_. These messages **SHOULD** relate to the originating client
     _request_.
   - The server **SHOULD NOT** close the SSE stream before sending the JSON-RPC _response_
     for the received JSON-RPC _request_, unless the [session](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#session-management)
     expires.
   - After the JSON-RPC _response_ has been sent, the server **SHOULD** close the SSE
     stream.
   - Disconnection **MAY** occur at any time (e.g., due to network conditions).
     Therefore:

     - Disconnection **SHOULD NOT** be interpreted as the client cancelling its request.
     - To cancel, the client **SHOULD** explicitly send an MCP `CancelledNotification`.
     - To avoid message loss due to disconnection, the server **MAY** make the stream
       [resumable](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#resumability-and-redelivery).

### Listening for Messages from the Server

1. The client **MAY** issue an HTTP GET to the MCP endpoint. This can be used to open an
SSE stream, allowing the server to communicate to the client, without the client first
sending data via HTTP POST.
2. The client **MUST** include an `Accept` header, listing `text/event-stream` as a
supported content type.
3. The server **MUST** either return `Content-Type: text/event-stream` in response to
this HTTP GET, or else return HTTP 405 Method Not Allowed, indicating that the server
does not offer an SSE stream at this endpoint.
4. If the server initiates an SSE stream:
   - The server **MAY** send JSON-RPC _requests_ and _notifications_ on the stream.
   - These messages **SHOULD** be unrelated to any concurrently-running JSON-RPC
     _request_ from the client.
   - The server **MUST NOT** send a JSON-RPC _response_ on the stream **unless** [resuming](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#resumability-and-redelivery) a stream associated with a previous client
     request.
   - The server **MAY** close the SSE stream at any time.
   - The client **MAY** close the SSE stream at any time.

### Multiple Connections

1. The client **MAY** remain connected to multiple SSE streams simultaneously.
2. The server **MUST** send each of its JSON-RPC messages on only one of the connected
streams; that is, it **MUST NOT** broadcast the same message across multiple streams.

   - The risk of message loss **MAY** be mitigated by making the stream
     [resumable](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#resumability-and-redelivery).

### Resumability and Redelivery

To support resuming broken connections, and redelivering messages that might otherwise be
lost:

1. Servers **MAY** attach an `id` field to their SSE events, as described in the
[SSE standard](https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation).

   - If present, the ID **MUST** be globally unique across all streams within that
     [session](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#session-management)—or all streams with that specific client, if session
     management is not in use.
2. If the client wishes to resume after a broken connection, it **SHOULD** issue an HTTP
GET to the MCP endpoint, and include the
[`Last-Event-ID`](https://html.spec.whatwg.org/multipage/server-sent-events.html#the-last-event-id-header)
header to indicate the last event ID it received.

   - The server **MAY** use this header to replay messages that would have been sent
     after the last event ID, _on the stream that was disconnected_, and to resume the
     stream from that point.
   - The server **MUST NOT** replay messages that would have been delivered on a
     different stream.

In other words, these event IDs should be assigned by servers on a _per-stream_ basis, to
act as a cursor within that particular stream.

### Session Management

An MCP “session” consists of logically related interactions between a client and a
server, beginning with the [initialization phase](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle). To support
servers which want to establish stateful sessions:

1. A server using the Streamable HTTP transport **MAY** assign a session ID at
initialization time, by including it in an `Mcp-Session-Id` header on the HTTP
response containing the `InitializeResult`.

   - The session ID **SHOULD** be globally unique and cryptographically secure (e.g., a
     securely generated UUID, a JWT, or a cryptographic hash).
   - The session ID **MUST** only contain visible ASCII characters (ranging from 0x21 to
     0x7E).
2. If an `Mcp-Session-Id` is returned by the server during initialization, clients using
the Streamable HTTP transport **MUST** include it in the `Mcp-Session-Id` header on
all of their subsequent HTTP requests.

   - Servers that require a session ID **SHOULD** respond to requests without an
     `Mcp-Session-Id` header (other than initialization) with HTTP 400 Bad Request.
3. The server **MAY** terminate the session at any time, after which it **MUST** respond
to requests containing that session ID with HTTP 404 Not Found.
4. When a client receives HTTP 404 in response to a request containing an
`Mcp-Session-Id`, it **MUST** start a new session by sending a new `InitializeRequest`
without a session ID attached.
5. Clients that no longer need a particular session (e.g., because the user is leaving
the client application) **SHOULD** send an HTTP DELETE to the MCP endpoint with the
`Mcp-Session-Id` header, to explicitly terminate the session.

   - The server **MAY** respond to this request with HTTP 405 Method Not Allowed,
     indicating that the server does not allow clients to terminate sessions.

### Protocol Version Header

If using HTTP, the client **MUST** include the `MCP-Protocol-Version: <protocol-version>` HTTP header on all subsequent requests to the MCP
server, allowing the MCP server to respond based on the MCP protocol version.For example: `MCP-Protocol-Version: 2025-06-18`The protocol version sent by the client **SHOULD** be the one [negotiated during\\
initialization](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle#version-negotiation).For backwards compatibility, if the server does _not_ receive an `MCP-Protocol-Version`
header, and has no other way to identify the version - for example, by relying on the
protocol version negotiated during initialization - the server **SHOULD** assume protocol
version `2025-03-26`.If the server receives a request with an invalid or unsupported
`MCP-Protocol-Version`, it **MUST** respond with `400 Bad Request`.

### Backwards Compatibility

Clients and servers can maintain backwards compatibility with the deprecated [HTTP+SSE\\
transport](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports#http-with-sse) (from
protocol version 2024-11-05) as follows:**Servers** wanting to support older clients should:

- Continue to host both the SSE and POST endpoints of the old transport, alongside the
new “MCP endpoint” defined for the Streamable HTTP transport.
  - It is also possible to combine the old POST endpoint and the new MCP endpoint, but
    this may introduce unneeded complexity.

**Clients** wanting to support older servers should:

1. Accept an MCP server URL from the user, which may point to either a server using the
old transport or the new transport.
2. Attempt to POST an `InitializeRequest` to the server URL, with an `Accept` header as
defined above:

   - If it succeeds, the client can assume this is a server supporting the new Streamable
     HTTP transport.
   - If it fails with an HTTP 4xx status code (e.g., 405 Method Not Allowed or 404 Not
     Found):
     - Issue a GET request to the server URL, expecting that this will open an SSE stream
       and return an `endpoint` event as the first event.
     - When the `endpoint` event arrives, the client can assume this is a server running
       the old HTTP+SSE transport, and should use that transport for all subsequent
       communication.

## Custom Transports

Clients and servers **MAY** implement additional custom transport mechanisms to suit
their specific needs. The protocol is transport-agnostic and can be implemented over any
communication channel that supports bidirectional message exchange.Implementers who choose to support custom transports **MUST** ensure they preserve the
JSON-RPC message format and lifecycle requirements defined by MCP. Custom transports
**SHOULD** document their specific connection establishment and message exchange patterns
to aid interoperability.

</details>

<details>
<summary>welcome-to-fastmcp-2-0-fastmcp</summary>

**FastMCP is the standard framework for building MCP applications.** The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) provides a standardized way to connect LLMs to tools and data, and FastMCP makes it production-ready with clean, Pythonic code:

```
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## What is MCP?

The Model Context Protocol lets you build servers that expose data and functionality to LLM applications in a secure, standardized way. It is often described as “the USB-C port for AI”, providing a uniform way to connect LLMs to resources they can use. It may be easier to think of it as an API, but specifically designed for LLM interactions. MCP servers can:

- Expose data through `Resources` (think of these sort of like GET endpoints; they are used to load information into the LLM’s context)
- Provide functionality through `Tools` (sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
- Define interaction patterns through `Prompts` (reusable templates for LLM interactions)
- And more!

FastMCP provides a high-level, Pythonic interface for building, managing, and interacting with these servers.

## Why FastMCP?

FastMCP handles all the complex protocol details so you can focus on building. In most cases, decorating a Python function is all you need — FastMCP handles the rest.

🚀 **Fast**: High-level interface means less code and faster development
🍀 **Simple**: Build MCP servers with minimal boilerplate
🐍 **Pythonic**: Feels natural to Python developers
🔍 **Complete**: Everything for production — enterprise auth (Google, GitHub, Azure, Auth0, WorkOS), deployment tools, testing frameworks, client libraries, and more

FastMCP provides the shortest path from idea to production.

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
<summary>_Users_omar_Documents_ai_repos_course-ai-agents_lessons_16_fastmcp_notebook</summary>

# Lesson 16: FastMCP — MCP Server and Client Quickstart

In this lesson, you will run a Model Context Protocol (MCP) server and MCP client using the FastMCP library, then explore how our research agent exposes MCP tools, MCP resources, and MCP prompts. We’ll start with a quick demo that runs the MCP client with an in-memory MCP server directly from this notebook, so you can get to try its capabilities immediately. Then, we’ll examine the MCP server and MCP client code structure.

Learning Objectives:
- Learn how to create an MCP server using `fastmcp`
- Learn how to create an MCP client using `fastmcp`
- Learn how to use the `fastmcp` library to expose MCP tools, MCP resources, and MCP prompts
- Learn how to use the `fastmcp` library to interact with an MCP server

## 1. Setup

First, we define some standard Magic Python commands to autoreload Python packages whenever they change:

```python
%load_ext autoreload
%autoreload 2
```


### Set Up Python Environment

To set up your Python virtual environment using `uv` and load it into the Notebook, follow the step-by-step instructions from the `Course Admin` lesson from the beginning of the course.

**TL/DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.

### Configure Gemini API

To configure the Gemini API, follow the step-by-step instructions from the `Course Admin` lesson.

But here is a quick check on what you need to run this Notebook:

1.  Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  From the root of your project, run: `cp .env.example .env` 
3.  Within the `.env` file, fill in the `GOOGLE_API_KEY` variable:

Now, the code below will load the key from the `.env` file:

```python
from utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])
```


### Import Key Packages

```python
import nest_asyncio

nest_asyncio.apply()  # Allow nested async usage in notebooks
```


## 2. Try the agent (MCP client quickstart)

The research agent is made of an MCP server and an MCP client.

The MCP server is a `fastmcp` server that registers MCP tools, MCP resources, and MCP prompt via router modules. The MCP client is a `fastmcp` client that connects to the MCP server and allows you to interact with it, along with interacting with the LLM agent.

This quickstart runs the MCP client of the research agent inside the notebook kernel. It connects to the MCP server running in‑memory (same process), which is the only transport supported for running everything in the same notebook. So, we'll always run the MCP server in-memory in the notebooks.

Run the next code cell to start the MCP client. You will see some texts and can type commands directly in the input box that appears. The input box will be in different locations depending on where you are running the notebook from.

Once the client is running, you can type commands when prompted, such as:

- `/tools`: list all available MCP tools with names and descriptions.
- `/resources`: list all available MCP resources with their URIs.
- `/prompts`: list all available MCP prompts by name and description.
- `/prompt/full_research_instructions_prompt`: fetch the research workflow prompt and inject it into the conversation.
- `/resource/system://memory`: read and print the server memory stats (an example of running an MCP resource).
- `/model-thinking-switch`: toggle model “thinking” traces on/off. By default it is true, which means that you'll see the agent's thoughts in the conversation before each answer or tool call.
- Any other text: treated as a normal user message for the agent, which may use the MCP server tools for answering.
- `/quit`: terminate the client.

At first, try with the following commands and see what happens:
- `Hello! Who are you?`
- `/tools`
- `/resource/system://memory`
- `/quit`

```python
# Run the MCP client in-kernel
import sys

from research_agent_part_2.mcp_client.src.client import main as client_main


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


Whenever you want, you can run the previous cell again to try the client.

Now, let's see how the MCP server works.

## 3. MCP Server Overview

The purpose of this section is to show how the MCP server is created with `fastmcp` and how it wires MCP tools, MCP resources, and MCP prompts.

The MCP server is a `fastmcp` server that registers MCP tools (actions with side effects like scraping webpages, transcribing videos, etc.), MCP resources (read-only endpoints for information like system status or memory), and MCP prompts (reusable instruction blocks, such as our agent workflow) via router modules.

The MCP server follows a FastAPI‑like layout for clarity and scalability. It is structured as follows:

- `server.py`: Entry point exposing `create_mcp_server()` and a `__main__` runner.
- `routers/`: Functions that attach endpoints to the FastMCP instance.
  - `tools.py`: registers all MCP tools.
  - `resources.py`: registers all MCP resources.
  - `prompts.py`: registers all MCP prompts.
- `tools/`: MCP tools implementations.
- `resources/`: MCP resources implementations.
- `prompts/`: MCP prompts implementations (e.g. full workflow instructions for the agent).
- `app/`: Functions implementing business logic.
- `utils/`: Utility functions.
- `config/`: Pydantic settings (`settings.py`) for server name/version, logging, model choices, and API keys.

This separation keeps orchestration thin at the server boundary while allowing each capability (tool/resource/prompt) to evolve independently.

Let's see now how the MCP server is created.

Source:
_mcp_server/src/server.py_

```python
from fastmcp import FastMCP

from .config.settings import settings
from .routers.prompts import register_mcp_prompts
from .routers.resources import register_mcp_resources
from .routers.tools import register_mcp_tools


def create_mcp_server() -> FastMCP:
    """
    Create and configure the MCP server instance.

    This function can be imported to get a configured MCP server
    for use with in-memory transport in clients.

    Returns:
        FastMCP: Configured MCP server instance
    """
    # Create the FastMCP server instance
    mcp = FastMCP(
        name=settings.server_name,
        version=settings.version,
    )

    # Register all MCP endpoints
    register_mcp_tools(mcp)
    register_mcp_resources(mcp)
    register_mcp_prompts(mcp)

    return mcp
```

Notice how the `FastMCP` instance is created and how the `mcp` object is passed to the `register_mcp_tools`, `register_mcp_resources`, and `register_mcp_prompts` functions. It is pretty similar to how you would create a FastAPI app and attach endpoints to it!

### 3.1 Registering MCP Tools

Let's see now in particular how to register an MCP tool with `fastmcp`. This specific tool reads the article guidelines and extracts relevant references. Its implementation is in the `tools/extract_guidelines_urls_tool.py` file, along with other business logic functions in the `app/` folder. You can read the full file `mcp_server/src/routers/tools.py` to see all the 11 available MCP tools.

Source: _mcp_server/src/routers/tools.py_

```python
@mcp.tool()
async def extract_guidelines_urls(research_directory: str) -> Dict[str, Any]:
    """
    Extract URLs and local file references from article guidelines.

    Reads the ARTICLE_GUIDELINE_FILE file in the research directory and extracts:
    - GitHub URLs
    - Other HTTP/HTTPS URLs
    - Local file references (files mentioned in quotes with extensions)

    Results are saved to GUIDELINES_FILENAMES_FILE in the research directory.
    """
    result = extract_guidelines_urls_tool(research_directory)
    return result
```

This tool is the first step in the workflow. It reads the article guideline and writes a structured file containing URLs and local references. Notice how it requires a `research_directory` input, which is the path to the research directory containing a `article_guideline.md` file.


Let's test it with a sample article guideline. In the research agent folder, there's a `data/sample_research_folder` folder with an `article_guideline.md` file. Let's use it as input for the `extract_guidelines_urls` tool.

Here is how it is structured:

```md
## Global Context of the Lesson

...

## Lesson Outline

## Section 1: Introduction

...

## Section 2: Understanding why agents need tools

...

## Section N: Conclusion

...

## Article code

Links to code that will be used to support the article. Always prioritize this code over every other piece of code found in the sources: 

- [Notebook 1](https://github.com/path/to/notebook.ipynb)

## Sources

- [Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)
- [Function calling with OpenAI's API](https://platform.openai.com/docs/guides/function-calling)
- [Tool Calling Agent From Scratch](https://www.youtube.com/watch?v=ApoDzZP8_ck)
- [Efficient Tool Use with Chain-of-Abstraction Reasoning](https://arxiv.org/pdf/2401.17464v3)
- [Building AI Agents from scratch - Part 1: Tool use](https://www.newsletter.swirlai.com/p/building-ai-agents-from-scratch-part)
- [What is Tool Calling? Connecting LLMs to Your Data](https://www.youtube.com/watch?v=h8gMhXYAv1k)
- [ReAct vs Plan-and-Execute: A Practical Comparison of LLM Agent Patterns](https://dev.to/jamesli/react-vs-plan-and-execute-a-practical-comparison-of-llm-agent-patterns-4gh9)
- [Agentic Design Patterns Part 3, Tool Use](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/)
```

Normally, an `article_guideline.md` file would contain detailed information about the article to write, including the outline, the sections, the sources, and the code, as the research agent needs this information to look for the best content to include in the article. In this sample file, we have a simplified version of an article guideline.

Now, run the next code cell to run the research agent MCP client again, and give it the following command. Make sure to replace the folder path with your actual absolute folder path, otherwise the tool will not find the file.
- Command to give to the client: `Run the "extract_guidelines_urls" tool with the "data/sample_research_folder" directory as research folder and stop after the tool has finished running.`.

In case you provide the wrong path, notice how the tool will return an error and how the agent will ask you to provide a valid path and how to proceed.

*Important*: the agent will manage every message starting with the `/` as a command, so, if you want to provide the folder path in a message, you need to write something like this: `Here is the folder path: /absolute/path/to/the/folder`.

```python
# Run the MCP client in-kernel
import sys

from research_agent_part_2.mcp_client.src.client import main as client_main


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


Notice the agent's thoughts. If everything ran correctly, you'll see the text "Tool execution successful". If so, notice that there is a new folder named `.nova` in the research directory, with a file `guidelines_filenames.json` inside. This file contains the URLs and local references extracted from the article guideline.

Its content should be like this:

```json
{
  "github_urls": [
    "https://github.com/path/to/notebook.ipynb"
  ],
  "youtube_videos_urls": [
    "https://www.youtube.com/watch?v=ApoDzZP8_ck",
    "https://www.youtube.com/watch?v=h8gMhXYAv1k"
  ],
  "other_urls": [
    "https://ai.google.dev/gemini-api/docs/function-calling",
    "https://platform.openai.com/docs/guides/function-calling",
    "https://arxiv.org/pdf/2401.17464v3",
    "https://www.newsletter.swirlai.com/p/building-ai-agents-from-scratch-part",
    "https://dev.to/jamesli/react-vs-plan-and-execute-a-practical-comparison-of-llm-agent-patterns-4gh9",
    "https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/"
  ],
  "local_file_paths": []
}
```

So, the tool has extracted those URLs from the `article_guideline.md` file and categorized them into the groups you see above.

We can run the above tool also programmatically as follows. The output shows the result of running it from the local setup of the author of this notebook. To run it, update the path of the `research_folder` variable with your absolute path to the `sample_research_folder` folder.

```python
from research_agent_part_2.mcp_server.src.tools import extract_guidelines_urls_tool

research_folder = "/your/absolute/path/to/sample_research_folder"
extract_guidelines_urls_tool(research_folder=research_folder)
```


We'll comment the output of this tool in the next lesson. In the next lessons, we'll run each tool one by one like in the above code cell, so you can see the output of each tool and understand how the research agent works.

### 3.2 Registering MCP Resources

Let's see now how to register an MCP resource endpoint using `fastmcp`.

Source:
_lessons/research_agent_part_2/mcp_server/src/routers/resources.py_

```python
@mcp.resource("system://memory")
async def memory_usage() -> Dict[str, Any]:
    """Monitor memory usage of the server."""
    return await get_memory_usage_resource()
```

It's very similar to how tools are registered, except that the `@mcp.resource()` decorator is used instead of the `@mcp.tool()` decorator.

Let's now run the `get_memory_usage_resource` function to see the memory usage of the server.

```python
from research_agent_part_2.mcp_server.src.resources import get_memory_usage_resource

await get_memory_usage_resource()
```


This output is the same output that an MCP client would get if it uses this MCP resource.

*Important*: in the research agent MCP client, we have only implemented the use of tools by the agent LLM, but we could have implemented the use of resources as well. Most MCP clients do not support resources yet, but their support is increasing.

### 3.3 Registering MCP Prompts

This section shows how MCP prompts are implemented with `fastmcp`. This specific prompt defines the agentic workflow for the research agent.

Source:
_mcp_server/src/routers/prompts.py_

```python
@mcp.prompt()
async def full_research_instructions_prompt() -> str:
    """Complete Nova research agent workflow instructions."""
    return await _get_research_instructions()
```

The prompt content encodes the full workflow orchestration the agent should follow when started via a prompt.

In practice, MCP prompts are triggered by users from an MCP client, not by the agent LLM. When a user triggers an MCP prompt, the MCP client would retrieve that prompt and load it to instruct the LLM on how to run the available tools in sequence (and sometimes in parallel) according to the workflow described in it.

For reference, here is the full prompt content of the only MCP prompt implemented in the research agent, which is the `full_research_instructions_prompt` prompt.

```python
from research_agent_part_2.mcp_server.src.prompts import full_research_instructions_prompt

prompt = await full_research_instructions_prompt()
print(prompt)
```


This is the instruction block that defines the agentic workflow for the research agent. In the next lessons, we'll go through each step defined in the workflow, learn how it is implemented, and run it in isolation.

Let's now see how the MCP client works.

## 4. MCP Client Overview

Here is the MCP client's layout. It is structured as follows:

- `client.py`: CLI entry point. Parses `--transport`, creates the client (in‑memory or stdio), fetches capabilities, prints the startup banner, and runs the interactive loop.
- `settings.py`: Centralized Pydantic settings for API keys, model selection, logging, transport, and server paths.
- `utils/`: Helper modules used by `client.py`.

The MCP client can run with two transports:

- **in-memory**: The client imports the server factory (the `create_mcp_server` function from the `client.py` file) and instantiates the server inside the same Python process. This is fast, simple to debug, and is what we use in this notebook.
- **stdio**: The client launches the server as a separate process and communicates using the MCP stdio transport. This mirrors how external MCP clients (e.g., editors) connect to servers and provides process isolation.

Let's see how the code of the `client.py` file works.

Source: _mcp_client/src/client.py_

```python
if args.transport == "in-memory":
    ...
    from mcp_server.src.server import create_mcp_server
    mcp_server = create_mcp_server()
    mcp_client = Client(mcp_server)

elif args.transport == "stdio":
    config = {
        "mcpServers": {
            "research-agent": {
                "transport": "stdio",
                "command": "uv",
                "args": [
                    "--directory", str(settings.server_main_path),
                    "run", "-m", "src.server",
                    "--transport", "stdio",
                ],
            }
        }
    }
    mcp_client = Client(config)

# At startup
tools, resources, prompts = await get_capabilities_from_mcp_client(mcp_client)
print_startup_info(tools, resources, prompts)

async with mcp_client:
    while True:
        # Get user input
        user_input = input("👤 You: ").strip()
        ...

        # Parse input
        parsed_input = parse_user_input(user_input)
        ...

        # Dispatch handling
        await handle_user_message(parsed_input=parsed_input, ...)
        ...
```

It does the following:
1) Parse the `--transport` flag.
2) If in-memory, build a `Client` with the FastMCP server object. If stdio, pass a config that tells FastMCP how to exec the server via `uv`.
3) Query the MCP server for its capabilities (tools/resources/prompts) and print them.
4) Enter the interactive loop: read input, parse it, and dispatch handling.

The code above is run when the MCP client is started. If you remember from previous cells, when the MCP client is started, it prints the following information:

```
🛠️ Available tools: 11
📚 Available resources: 2
💬 Available prompts: 1

Available Commands: /tools, /resources, /prompts, /prompt/<name>, /resource/<uri>, /model-thinking-switch, /quit
```

But, how does the MCP client know how many tools, resources, and prompts are available? Let's see how the `get_capabilities_from_mcp_client` function works.

Source:
_mcp_client/src/utils/mcp_startup_utils.py_

```python
async def get_capabilities_from_mcp_client(client: Client) -> tuple[List, List, List]:
    """Get available capabilities."""
    async with client:
        tools = await client.list_tools()
        resources = await client.list_resources()
        prompts = await client.list_prompts()

    return tools, resources, prompts
```

As you can see, the MCP client object has a `list_tools`, `list_resources`, and `list_prompts` method that returns the list of tools, resources, and prompts respectively. These lists contain information about their names, descriptions, parameters, and so on.

We are now ready to learn how the MCP client parses the user input and how it handles the user messages.

### 4.1 Parsing Input and Commands

The client supports a small command language. Input can be either a command (starting with `/`) or a freeform user message.

Possible commands are:
- `/tools`, `/resources`, `/prompts`
- `/prompt/<name>` (e.g., `/prompt/full_research_instructions_prompt`)
- `/resource/<uri>` (e.g., `/resource/system://status`)
- `/model-thinking-switch`
- `/quit`

The `parse_user_input` function simply classifies the input (no side effects) and it returns a `ProcessedInput` with metadata. Here are some examples:

```python
from research_agent_part_2.mcp_client.src.utils.parse_message_utils import parse_user_input

processed_input = parse_user_input("/tools")
print(processed_input.input_type)

processed_input = parse_user_input("/resources")
print(processed_input.input_type)

processed_input = parse_user_input("/prompt/full_research_instructions_prompt")
print(processed_input.input_type, processed_input.prompt_name)

processed_input = parse_user_input("Hello, how are you?")
print(processed_input.input_type)
```


These processed inputs are then used to dispatch the correct handling.

The `handle_user_message` function orchestrates the conversation, calling the appropriate helper for the parsed command, or appending a normal message and running the agent loop.

Here are some examples. Let's first create the MCP server and client, and get the server capabilities (available tools, resources, and prompts).

```python
from fastmcp import Client
from research_agent_part_2.mcp_client.src.utils.handle_message_utils import handle_user_message
from research_agent_part_2.mcp_client.src.utils.mcp_startup_utils import get_capabilities_from_mcp_client
from research_agent_part_2.mcp_server.src.server import create_mcp_server

# Create the MCP server and client
mcp_server = create_mcp_server()
mcp_client = Client(mcp_server)

# Get the MCP server capabilities
tools, resources, prompts = await get_capabilities_from_mcp_client(mcp_client)
```


Now, let's parse the user input and handle the user message with the `handle_user_message` function. Here is an example with commands (i.e. messages starting with `/`):

```python
# Parse the user input
processed_input = parse_user_input("/resources")
conversation_history = []
response = await handle_user_message(
    processed_input, tools, resources, prompts, conversation_history, mcp_client, thinking_enabled=True
)
```


The `handle_user_message` function is basically a router that calls the appropriate helper for the parsed message. It is defined in the `handle_message_utils.py` file, you can read it to learn more about it.

As previously explained, the `tools` object contains the list of tools registered in the MCP server, retrieved by the `list_tools` method. If the input is of type `COMMAND_INFO_TOOLS`, the `handle_command` function is called.

Source:
_mcp_client/src/utils/command_utils.py_

```python
def handle_command(processed_input: ProcessedInput, tools: List, resources: List, prompts: List):
    """Handle informational commands.

    This function only handles informational commands (COMMAND_INFO_* types).
    """
    if processed_input.input_type == InputType.COMMAND_INFO_TOOLS:
        print_header("🛠️  Available Tools")
        for i, tool in enumerate(tools, 1):
            print_item(tool.name, tool.description, i, Color.BRIGHT_WHITE, Color.YELLOW)
    ...
```

This function retrieves, from each tool, the name and description, and prints them in a pretty format.

All the tools are managed in a similar way.

If the input message is of type `NORMAL_MESSAGE`, the `handle_agent_loop` function is called instead, which manages the agent loop for tool execution. Let's see how it works.

Source:
_mcp_client/src/utils/handle_agent_loop_utils.py_

```python
async def handle_agent_loop(
    conversation_history: List[types.Content],
    tools: List,
    client: Client,
    thinking_enabled: bool,
):
    """Handle the agent loop for tool execution."""
    # Initialize LLM client
    llm_config = build_llm_config_with_tools(tools, thinking_enabled)
    llm_client = LLMClient(settings.model_id, llm_config)

    while True:
        print()
        # Call LLM with current conversation history
        response = await llm_client.generate_content(conversation_history)

        # Extract and display thoughts as separate message (only if enabled)
        if thinking_enabled:
            thoughts = extract_thought_summary(response)
            ...

        # Check for function calls
        function_call_info = extract_first_function_call(response)
        if function_call_info:
            name, args = function_call_info

            # Check if this is a tool call
            is_tool = any(tool.name == name for tool in tools)

            if is_tool:
                ...

                # Execute the tool via MCP server
                tool_result = await execute_tool(name, args, client)
                # Add tool result to conversation history
                tool_response = f"Tool '{name}' executed successfully. Result: {tool_result}"
                conversation_history.append(types.Content(role="user", parts=[types.Part(text=tool_response)]))
                ...
        else:
            # Extract final text response - this ends the ReAct loop
            final_text = extract_final_answer(response)
            conversation_history.append(response.candidates[0].content)
            ...
            break  # Exit the agent loop
```

This function is the main loop that manages the agent loop for tool execution. It initializes the LLM client, builds the LLM configuration with the tools, and then enters the agent loop.

The loop is structured as follows:

1) Call the LLM with the current conversation history.
2) Extract and display thoughts as separate message (only if enabled).
3) Check for function calls.
4) If there is a function call, check if it is a tool call.
5) If it is a tool call, execute the tool via MCP server.
6) Add the tool result to the conversation history.

The `LLMClient` class is simply a wrapper class that allows to generate content (or a function call) with an LLM, independently from the specific LLM provider. Right now it only implements Google Gemini as model, but it can be easily extended to other models. It is defined in the `llm_utils.py` file.

The `build_llm_config_with_tools` function builds the LLM configuration with the tools, it only works with Gemini for now. It is defined in the `llm_utils.py` file as well. Here's its code.

```python
def build_llm_config_with_tools(mcp_tools: List, thinking_enabled: bool = True) -> types.GenerateContentConfig:
    """Build Gemini config with all MCP tools converted to Gemini format."""
    gemini_tools = []

    for tool in mcp_tools:
        gemini_tool = types.Tool(
            function_declarations=[
                types.FunctionDeclaration(
                    name=tool.name,
                    description=tool.description,
                    parameters=tool.inputSchema,
                )
            ]
        )
        gemini_tools.append(gemini_tool)

    # Create thinking config dynamically based on current state
    thinking_config = types.ThinkingConfig(
        include_thoughts=thinking_enabled,
        thinking_budget=settings.thinking_budget,
    )

    return types.GenerateContentConfig(
        tools=gemini_tools,
        thinking_config=thinking_config,
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
    )
```

The code above basically instructions the LLM to leverage thinking (if enabled) with the specificed thinking budget (i.e. the maximum number of tokens the LLM can use to think) and to use the available tools from the MCP server.

The other functions from the `handle_agent_loop` function, like `extract_thought_summary` and `extract_final_answer`, are used to extract the thoughts and the final answer from the LLM response. It's boilerplate code that works for Gemini and can be copypasted for other projects.

The `execute_tool` function is used to execute the tool via MCP server. It is defined in the `handle_agent_loop_utils.py` file. Here's its code.

```python
async def execute_tool(name: str, args: dict, client: Client):
    """Execute a tool and return the result."""
    ...
    tool_result = await client.call_tool(name, args)
    return tool_result
```

It uses the `call_tool` method of the `Client` object to execute the tool.

We can now test the MCP client with a user message that involves tool execution and see how the agent behaves.

```python
# Parse the user input
path_to_research_folder = (
    "/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder"
)
message = (
    f"Call the 'extract_guidelines_urls' tool with the '{path_to_research_folder}' directory as research folder, and stop after the tool has finished running."
    "Don't run any other tool after the 'extract_guidelines_urls' tool has finished running."
    "If the tool fails, explain to me the error message."
)
processed_input = parse_user_input(message)
conversation_history = []
async with mcp_client:
    response = await handle_user_message(
        processed_input, tools, resources, prompts, conversation_history, mcp_client, thinking_enabled=True
    )
```


We are good to go!

In the next lesson, we'll learn more about how the MCP prompt is used by the MCP client to orchestrate the agentic workflow.
Then, we'll go through each step of the research agent workflow, and we'll see how to run each tool in isolation.

</details>
