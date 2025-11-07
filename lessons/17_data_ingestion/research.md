# Research

## Research Results

<details>
<summary>Best practices for designing fault-tolerant data ingestion pipelines for AI agents, specifically handling critical vs. non-critical failures.</summary>

### Source [1]: https://www.shaped.ai/blog/10-best-practices-in-data-ingestion

Query: Best practices for designing fault-tolerant data ingestion pipelines for AI agents, specifically handling critical vs. non-critical failures.

Answer: Best practices for designing **fault-tolerant data ingestion pipelines** include:

- **Instrument Robust Error Handling and Dead Letter Queues (DLQs):** Always expect and prepare for bad data (malformed payloads, missing fields, unexpected schema changes). Use DLQs to route failed events, preserving them with metadata (timestamp, source, error type) for later inspection and reprocessing. Tag records with failure codes, set retry thresholds, and escalate persistent failures to the DLQ. Separate transient errors (e.g., network failures, which can be retried) from structural errors (e.g., schema mismatches, which may require intervention).
- **Monitor DLQ Volumes:** Use the size and growth of DLQs as a health signal for upstream systems and overall pipeline quality.
- **Graceful Failure:** Ensure the system fails gracefully, not catastrophically, maintaining the main data flow’s integrity.
- **Design for Backpressure and Throughput Variability:** Use message brokers (Kafka, RabbitMQ, SQS) to buffer and decouple producers from consumers. Implement autoscaling and rate limiting to handle burst loads. Partition loads for parallelism and resiliency.
- **Schema Enforcement and Timestamps:** Enforce schema early to catch format issues. Normalize all timestamps at ingestion to maintain consistency across distributed systems.

For **critical failures** (e.g., systemic schema changes, total data source loss), immediate alerting and escalation to operators is necessary. For **non-critical failures** (e.g., occasional malformed record), use DLQs and automated retries to minimize disruption to the main pipeline.

-----

-----

-----

### Source [2]: https://airbyte.com/data-engineering-resources/data-ingestion-pipeline-best-practices-for-modern-organizations

Query: Best practices for designing fault-tolerant data ingestion pipelines for AI agents, specifically handling critical vs. non-critical failures.

Answer: Key practices for **fault tolerance in data ingestion pipelines** include:

- **Graceful Failure Handling:** Pipelines should employ **automatic retry logic** for transient errors, **dead-letter queues** for persistent failures, and **comprehensive monitoring** for early detection of issues.
- **Automated Alerts:** Set up alerts to notify administrators when source systems are unavailable or data formats change, ensuring quick intervention for critical issues.
- **Continuity of Operation:** Design pipelines to maintain operation even during failures, isolating problematic data/events to prevent them from impacting the main data flow.
- **Elastic Scaling:** Use auto-scaling to handle unpredictable data volumes, preventing overload and dropped records.
- **Quality Monitoring:** Implement AI-driven or automated checks at the data source to flag inconsistencies early, ensuring downstream reliability.

For **critical failures** (e.g., prolonged source outages, widespread data corruption), the pipeline should escalate to human intervention and possibly pause affected data flows. **Non-critical failures** (e.g., occasional schema mismatches) should be handled automatically, with problematic records diverted and the pipeline continuing uninterrupted.

-----

-----

-----

### Source [3]: https://www.integrate.io/blog/data-engineering-best-practices/

Query: Best practices for designing fault-tolerant data ingestion pipelines for AI agents, specifically handling critical vs. non-critical failures.

Answer: Best practices for ensuring **fault tolerance** in data pipelines include:

- **Idempotent Design:** Ensure operations can be safely retried without data duplication or integrity loss, which is crucial for automated recovery from transient issues.
- **Retry Mechanisms with Exponential Backoff:** Implement retries for transient errors, spacing retries to avoid overwhelming systems during temporary outages.
- **Message Queues for Asynchronous Processing:** Use tools like Kafka or RabbitMQ to buffer data, decouple pipeline stages, and facilitate recovery from downstream failures.
- **Checkpointing:** Regularly save pipeline state to enable resuming from the last successful point after a failure, minimizing data loss or reprocessing.
- **Automated Monitoring:** Continuously track pipeline health and alert on anomalies or failures, enabling rapid response to both critical and non-critical issues.

For **critical failures** (persistent system or network failures), checkpointing and alerting allow rapid recovery and minimal data loss. **Non-critical failures** (intermittent errors) are mitigated by idempotency, retries, and queuing, keeping the pipeline robust without operator intervention.

-----

-----

-----

### Source [4]: https://docs.databricks.com/aws/en/lakehouse-architecture/reliability/best-practices

Query: Best practices for designing fault-tolerant data ingestion pipelines for AI agents, specifically handling critical vs. non-critical failures.

Answer: Databricks recommends the following for **reliable and fault-tolerant data ingestion**:

- **Rescue Invalid or Nonconforming Data:** Filter out or quarantine data that does not conform to the expected schema at ingestion. Use a "rescued data" column to capture and store unparsed or invalid data for later analysis, ensuring no data is lost.
- **Auto Loader and Declarative Pipelines:** Use tools like Auto Loader to automatically handle and rescue invalid JSON or CSV records, and Lakeflow Declarative Pipelines to specify quality constraints.
- **Quarantine Invalid Records:** Define expectation rules that store invalid records in a separate quarantine table, allowing the main pipeline to continue processing conforming data.
- **Modes for Handling Invalid Data:** Choose between retaining, dropping, or failing on invalid records, depending on criticality. For non-critical failures, retain or quarantine. For critical failures, fail the pipeline and trigger alerts.

**Critical failures** (e.g., schema-breaking changes or massive influx of invalid records) should trigger pipeline failures and immediate alerts. **Non-critical failures** (e.g., sporadic invalid records) should be quarantined, allowing the pipeline to maintain overall throughput and reliability.

-----

-----

</details>

<details>
<summary>How to implement a token-efficient 'LLM clean pass' for scraped web content without summarizing?</summary>

### Source [5]: https://arxiv.org/html/2502.01968v1

Query: How to implement a token-efficient 'LLM clean pass' for scraped web content without summarizing?

Answer: Token Cleaning presents a fine-grained data selection approach specifically designed for LLM supervised fine-tuning that operates at the token level rather than the sample level. The framework addresses a critical problem: even in high-quality samples, many tokens can be redundant or uninformative. Common tokens and patterns that occur frequently across samples can overshadow task-specific words crucial for model performance during training. This token-level noise dilutes essential signals even in well-curated datasets.

The token cleaning pipeline works by first assessing token quality using an influence-guided scoring mechanism, then applying threshold-based separation to filter out uninformative tokens while retaining those with meaningful task-specific information. The influence of model updates on each token is calculated by measuring the loss disparity between a base model and a reference model.

Two implementation strategies are provided: Fix-Model Cleaning applies one-shot token cleaning to the entire dataset with both base and reference models remaining fixed, after which the base model is fine-tuned on the cleaned tokens. Self-Evolving Cleaning keeps the base model fixed while iteratively updating the reference model, dividing data into multiple parts where each iteration cleans one part and updates the reference model sequentially using cleaned results.

For scraped web content, this approach is particularly valuable because web data typically contains substantial amounts of boilerplate text, navigation elements, and other non-task-related patterns. By identifying and removing these uninformative tokens at a granular level, the method helps the model prioritize important content without requiring summarization. The framework enables models to concentrate on the most pertinent tokens while maintaining the original content structure, achieving consistent performance improvements across multiple downstream tasks.

-----

-----

### Source [6]: https://arxiv.org/html/2502.00340v1

Query: How to implement a token-efficient 'LLM clean pass' for scraped web content without summarizing?

Answer: Collider represents a system that enhances the efficiency of token filtering in LLM training by unlocking computational benefits while maintaining utility improvements. The system addresses the challenge that while token filtering is effective for improving model utility, its potential to improve computational efficiency in training remains largely unexplored. Standard implementations combining token filtering with existing LLM training systems demonstrate only modest speedup (1.2%) even when 40% of tokens are eliminated.

Collider implements backward token filtering, which maintains standard forward computation while performing selective token training in the output layer. The methodology uses a reference model to assess the importance of each token by comparing the loss of a target model against a reference model trained on high-quality data. Tokens with high excessive loss (the difference between target model loss and reference model loss) are considered important and retained, while those with lower excessive loss are filtered out during the backward pass.

For implementing token-efficient processing of scraped web content, Collider's approach features two main design points: First, it filters activations in the backward computation to retain sufficient sparsity in the gradient calculations. Second, it transforms sparse general matrix multiplication (GEMM) operations into dimension-reduced dense GEMM through automatically updating the backward computation graph to achieve maximum performance with existing hardware.

This system is particularly relevant for web content because it can systematically discard less significant tokens early in the training process while maintaining computational efficiency. By reducing the number of tokens processed in the computational pipeline, the approach decreases computational demands and expedites training without requiring content summarization, allowing models to concentrate on the most pertinent tokens from web sources.

-----

</details>

<details>
<summary>What are the best practices for converting Jupyter Notebooks (.ipynb) to LLM-friendly markdown for RAG pipelines?</summary>

### Source [7]: https://dev.to/coderatul/converting-jupyter-notebooks-to-markdown-made-easy-with-nbconvert-8dl

Query: What are the best practices for converting Jupyter Notebooks (.ipynb) to LLM-friendly markdown for RAG pipelines?

Answer: **nbconvert** is an official Jupyter tool that provides robust functionality for converting Jupyter Notebooks (.ipynb) to Markdown, making it valuable for documentation and integration into broader text workflows such as RAG (Retrieval-Augmented Generation) pipelines. 

Key best practices highlighted include:
- **Comprehensive Conversion:** nbconvert supports converting notebooks to various formats (Markdown, HTML, PDF, LaTeX, etc.), allowing for customization of the output through templates and syntax highlighting.
- **Simple Command-Line Usage:** The basic conversion can be performed via command line with `jupyter nbconvert --to markdown notebook.ipynb`. To ensure code cells are included, add the `--show-input` flag.
- **Extensibility and Customization:** Users can define custom templates or processing hooks to tailor the Markdown output to specific requirements, which is useful for preparing LLM-friendly documents or aligning the output with branding/documentation standards.
- **Workflow Integration:** The command-line and Python API make nbconvert easy to integrate into automated pipelines, ensuring reproducibility and consistency in documentation workflows.
- **Preservation of Narrative Flow:** The converted Markdown retains the narrative, code, and visualizations from the notebook, making the resulting .md file well-suited for downstream processing in RAG systems.

The article emphasizes that nbconvert is reliable, versatile, and feature-rich for converting Jupyter Notebooks into Markdown for sharing, documentation, and further automated processing[1].

-----

-----

-----

### Source [8]: https://jupyterbook.org/file-types/myst-notebooks.html

Query: What are the best practices for converting Jupyter Notebooks (.ipynb) to LLM-friendly markdown for RAG pipelines?

Answer: **Jupytext** and **MyST Markdown** offer advanced workflows for converting .ipynb notebooks to Markdown in a way that is fully compatible with Jupyter Book and other modern documentation systems—beneficial for LLM and RAG use cases.

Best practices from this source include:
- **MyST Markdown Format:** MyST (Markedly Structured Text) Markdown allows Jupyter notebooks to be stored and versioned as plain text Markdown files, supporting executable content and metadata.
- **Conversion with Jupytext:** Use Jupytext to convert between .ipynb and MyST Markdown with the command `jupytext mynotebook.ipynb --to myst`, producing a `.md` file that preserves code, outputs, and notebook structure.
- **Synchronization:** Jupytext can automatically synchronize .ipynb and Markdown files, ensuring that updates in one are reflected in the other, which is important for maintaining consistency in collaborative or automated environments.
- **Kernel Metadata:** When initializing a MyST Markdown file, use `jupyter-book myst init mymarkdownfile.md --kernel kernelname` to specify the execution kernel, ensuring downstream tools can execute code blocks correctly.

These practices facilitate storing notebooks in a form that is easy for version control and subsequent parsing or ingestion by LLMs in RAG pipelines, while retaining all executable and narrative content[2].

-----

-----

-----

### Source [9]: https://coderpad.io/blog/data-science/mastering-jupyter-notebooks-best-practices-for-data-science/

Query: What are the best practices for converting Jupyter Notebooks (.ipynb) to LLM-friendly markdown for RAG pipelines?

Answer: This source emphasizes the importance of **structured Markdown usage within Jupyter Notebooks** to enhance readability and flow, which translates directly to LLM-friendly Markdown for RAG pipelines:

- **Structured Organization:** Use headers, lists, images, links, and equations in Markdown cells to create a clear, logical structure. This helps LLMs to parse and extract relevant information efficiently.
- **Narrative and Context:** Maintain a strong narrative with Markdown text that explains the rationale behind code, the steps taken, and the significance of results. This contextual information is crucial for RAG pipelines to understand not just the code, but the reasoning and outcomes.
- **Audience Awareness:** Tailor the amount and type of Markdown narrative to the intended audience, which can help downstream LLMs better match retrieved information to user queries.
- **Cell Execution Order:** Ensure code cells are executed in logical sequence to avoid confusion and maintain consistency in outputs, as this order will be reflected in the Markdown conversion.

Focusing on these Markdown best practices ensures that the converted documents are not just machine-readable but also rich in context, which improves retrieval and answer quality in LLM applications[3].

-----

-----

</details>

<details>
<summary>How does the Model Context Protocol (MCP) concept of 'server-hosted prompts' compare to traditional agent tool-use orchestration?</summary>

### Source [10]: https://modelcontextprotocol.io/specification/2025-06-18/server/prompts

Query: How does the Model Context Protocol (MCP) concept of 'server-hosted prompts' compare to traditional agent tool-use orchestration?

Answer: The Model Context Protocol (MCP) concept of **server-hosted prompts** provides a standardized way for servers to expose prompt templates to clients. These prompts are intended to be **user-controlled**—meaning they are exposed by servers but selected and triggered by users, typically through user interface commands (such as slash commands). The protocol does not enforce a specific interaction model, allowing implementors flexibility in how prompts are presented and invoked. Servers supporting prompts must declare the `prompts` capability during initialization and can notify clients if the list of available prompts changes. This model centers on user discovery and explicit invocation of prompts, rather than automated orchestration by the agent or system.

-----

-----

-----

### Source [11]: https://modelcontextprotocol.info/docs/concepts/prompts/

Query: How does the Model Context Protocol (MCP) concept of 'server-hosted prompts' compare to traditional agent tool-use orchestration?

Answer: According to the MCP documentation, **prompts in MCP are reusable, user-controlled templates** that servers define to standardize workflows and interactions with large language models (LLMs). Prompts can accept dynamic arguments from the client, allowing customization for specific tasks (e.g., generating a Git commit message or explaining code). The server exposes an interface where clients can list available prompts and request the details of a specific prompt, including any required arguments. This approach emphasizes **server-defined, discoverable, and parameterizable workflows**, contrasting with traditional agent orchestration where the agent might select and chain tools autonomously based on intent and context.

-----

-----

-----

### Source [12]: https://openai.github.io/openai-agents-python/mcp/

Query: How does the Model Context Protocol (MCP) concept of 'server-hosted prompts' compare to traditional agent tool-use orchestration?

Answer: The OpenAI Agents SDK documentation explains that **MCP servers can provide prompts that dynamically generate agent instructions**. The server exposes two main methods: `list_prompts()` to enumerate available templates and `get_prompt(name, arguments)` to fetch a specific prompt (optionally parameterized). These prompts can then be used to generate the instructions for an agent, which subsequently runs with those instructions. By contrast, **traditional agent tool-use orchestration** involves agents autonomously discovering, selecting, and invoking tools (via `list_tools()` and related methods), often chaining tool executions based on intermediate results and reasoning. MCP's prompt mechanism allows for a standardized, server-driven way to inject structured instructions into agent workflows, but the control remains more transparent and user-facing compared to black-box agent orchestration.

-----

-----

-----

### Source [13]: https://www.legitsecurity.com/aspm-knowledge-base/whats-an-mcp-server-model-context-protocol-explained

Query: How does the Model Context Protocol (MCP) concept of 'server-hosted prompts' compare to traditional agent tool-use orchestration?

Answer: This overview of MCP servers highlights the protocol's **context-aware, session-based approach**. The MCP server processes client requests by considering session context and permissions, then builds appropriate backend calls (potentially involving data transformation and security checks). While the source details the general workflow of MCP—including backend data access and response merging—it does not specifically contrast **server-hosted prompts** with traditional agent orchestration. However, it notes that MCP servers can **orchestrate tasks together**, passing outputs between servers for more complex automations, which is conceptually similar to some forms of agent tool-use orchestration but typically involves more explicit, structured server-side workflow definitions rather than autonomous agent-driven tool chaining.

-----

-----

-----

### Source [14]: https://www.descope.com/learn/post/mcp

Query: How does the Model Context Protocol (MCP) concept of 'server-hosted prompts' compare to traditional agent tool-use orchestration?

Answer: This source describes the **MCP architecture** as providing a standardized client-server interface for LLMs to access external data and tools. The protocol is inspired by the Language Server Protocol (LSP), focusing on exposing specific server-side functions and integrations to clients in a way that is discoverable and interoperable. While it emphasizes the **standardization and universality** of the protocol for tool and data access, it does not detail the implementation or comparative philosophy of server-hosted prompts versus traditional agent orchestration. The focus is on clear, structured exposure of server capabilities, suggesting a more transparent and controlled approach compared to autonomous agent orchestration.

-----

-----

</details>

<details>
<summary>What are the latest techniques for adding auditability and traceability metadata to ingested data for AI research agents?</summary>

### Source [15]: https://marutitech.com/ai-auditability/

Query: What are the latest techniques for adding auditability and traceability metadata to ingested data for AI research agents?

Answer: **Auditability in AI systems** is defined as the process of tracking, analyzing, and understanding how AI systems function, which includes their decision-making processes, the data they use, and how outputs are generated. To support auditability and traceability, organizations are recommended to:

- **Establish clear audit criteria** with measurable, documented standards for data quality, algorithmic fairness, interpretability, consistency, and compliance.
- **Maintain comprehensive logs, documentation, and transparent mechanisms** for tracking the flow and transformation of data throughout the AI lifecycle.
- **Apply structured audit frameworks** that define the audit scope, collect essential input and output data, verify data quality (accuracy, completeness, bias), and evaluate both algorithms and governance structures.
- **Detect and address bias or anomalies** by analyzing decision-making outcomes and comparing them to expected results.
- **Ensure compliance with regulations** (e.g., GDPR, CCPA, ISO 42001, EU AI Act) by keeping verifiable records of data processing and AI decision-making.
- **Engage human auditors** to validate data quality, relevance, and the effectiveness of AI oversight mechanisms.

Audit trails are crucial for accountability, especially in regulated sectors. By following these steps, organizations both foster trust and demonstrate their commitment to transparency and ethics in AI development and deployment.

-----

-----

-----

### Source [16]: https://sparkco.ai/blog/ai-driven-data-insights-trends-and-techniques-for-2025

Query: What are the latest techniques for adding auditability and traceability metadata to ingested data for AI research agents?

Answer: Key trends for adding auditability and traceability metadata in AI research agents include:

- **Agentic AI systems**: These systems autonomously analyze data, identifying patterns and anomalies. Their automated processes can generate detailed, machine-generated logs that record every analytical step, supporting traceability.
- **AI-driven data preparation**: Automation of data cleansing, normalization, and classification helps ensure that metadata about data transformations is consistently and reliably recorded, which is essential for audit trails.
- **Synthetic data**: The use of AI-generated synthetic datasets allows for the tracking of data lineage without exposing real user data, aiding both privacy compliance and traceability.
- **Decentralized data governance frameworks**: These frameworks provide robust mechanisms for controlling and recording data access, movement, and transformation, making it easier to attach auditable metadata at every step.
- Integration of these technologies and methodologies allows organizations to both meet regulatory requirements and maintain high levels of data integrity and traceability, ensuring that all data ingested and processed by AI agents can be traced back to its source and every transformation step is auditable.

-----

-----

-----

### Source [17]: https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2025/no-looking-back-transforming-audit-with-artificial-intelligence

Query: What are the latest techniques for adding auditability and traceability metadata to ingested data for AI research agents?

Answer: AI-driven auditing is transforming the field with several techniques that enhance auditability and traceability:

- **Full data analysis**: Rather than relying on samples, AI can analyze entire datasets, creating comprehensive logs of what was reviewed, when, and by what algorithms, dramatically increasing traceability.
- **Continuous monitoring and real-time auditing**: AI systems now enable real-time analysis and monitoring. Every transaction or data point processed can be logged instantly, providing a complete, timestamped audit trail for each action or decision.
- **Visualization and reporting tools**: Modern audit tools powered by AI (such as ACL Robotics, KNIME, Arbutus, IDEA) provide visualizations and structured reports, which help document and communicate audit trails and findings.
- These developments mean that auditability is no longer a retrospective process but can be integrated into continuous, proactive oversight, with audit and traceability metadata embedded throughout the data lifecycle.

-----

-----

-----

### Source [18]: https://www.cpapracticeadvisor.com/2025/09/11/pwc-launches-new-ai-enabled-tools-to-help-enhance-audit-quality-and-simplify-data-preparation/168837/

Query: What are the latest techniques for adding auditability and traceability metadata to ingested data for AI research agents?

Answer: PwC's latest AI-enabled auditing tools illustrate advanced techniques for auditability and traceability:

- **Advanced analytics and machine learning models**: These tools automatically analyze datasets to detect unusual patterns and surface risks early. Every analytical operation is logged, creating detailed, machine-generated metadata for traceability.
- **Simplified data preparation**: AI automates data cleaning and structuring, with all steps documented, ensuring traceable data lineage from ingestion to audit conclusion.
- **Continuous risk identification**: Real-time monitoring tools provide ongoing auditing capabilities, logging every transaction or event as it occurs, which builds comprehensive, immutable audit trails.
- The integration of these AI tools means that organizations can produce audit logs and metadata in real time, greatly enhancing both auditability and traceability for all data ingested and processed by AI research agents.

-----

-----

</details>

<details>
<summary>What are the best practices for preparing GitHub repository content for LLM analysis, comparing specialized tools like gitingest versus simple file concatenation?</summary>

### Source [19]: https://arxiv.org/html/2406.01422v1

Query: What are the best practices for preparing GitHub repository content for LLM analysis, comparing specialized tools like gitingest versus simple file concatenation?

Answer: Best practices for preparing GitHub repository content for LLM analysis emphasize a **structured, hierarchical, and context-aware approach** rather than simple file concatenation. The paper introduces RepoUnderstander, an LLM-based agent that first organizes the repository into a **hierarchical structure tree** and constructs a **repository knowledge graph** to condense complex information. This allows comprehensive understanding of the repository’s functional modules, dependencies, and code relationships.

The recommended workflow includes:
- **Top-down analysis:** Organize the repository into a hierarchical structure for clear context and scope.
- **Expand to reference graphs:** Capture function call relationships to facilitate dependency and interaction analysis.
- **Guided exploration:** Use strategies like Monte Carlo Tree Search (MCTS) to help agents efficiently collect and learn repository-level knowledge, focusing on relevant areas.
- **Global summarization and planning:** Agents summarize, analyze, and plan repository information according to specific software engineering tasks.
- **Dynamic tool interaction:** Agents manipulate API tools to acquire additional local information as needed.

This structured approach is shown to outperform simple concatenation or naive ingestion, leading to more precise fault localization and informed patch generation. The paper demonstrates that understanding the global repository structure and leveraging repository-level knowledge is crucial for effective LLM-based software engineering tasks, particularly on benchmarks like SWE-bench Lite.

-----

-----

-----

### Source [21]: https://github.com/ghimiresunil/LLM-PowerHouse-A-Curated-Guide-for-Large-Language-Models-with-Custom-Training-and-Inferencing

Query: What are the best practices for preparing GitHub repository content for LLM analysis, comparing specialized tools like gitingest versus simple file concatenation?

Answer: This curated guide covers **Retrieval Augmented Generation (RAG)**, a common best practice for enabling LLMs to analyze large repositories. RAG involves connecting LLMs to databases or document stores, which allows the model to retrieve relevant documents or code segments at inference time, rather than relying solely on concatenated files or static context.

Key practices highlighted include:
- **Orchestrators** (e.g., LangChain, LlamaIndex): Frameworks to connect LLMs with external tools, databases, and memory systems, enabling sophisticated analysis of repository content.
- **Retrievers:** Using advanced techniques to optimize retrieval instructions, such as multi-query retrievers and hypothetical document expansion (HyDE).
- **Memory and summarization:** Maintaining a history of prior context and answers, with improvements via summarization or vector stores.
- **Evaluation:** Measuring retrieval (precision/recall) and generation (faithfulness and relevancy) with dedicated tools (e.g., Ragas, DeepEval).

This approach is more robust than simple file concatenation, as it enables **context-aware and scalable analysis** by allowing the LLM to dynamically access and process relevant repository fragments. Frameworks like LangChain and LlamaIndex are especially recommended for building these pipelines.

-----

-----

-----

### Source [46]: https://arxiv.org/html/2406.01422v1

Query: What are the best practices for preparing GitHub repository content for LLM analysis, comparing specialized tools like gitingest versus simple file concatenation?

Answer: This paper introduces **RepoUnderstander**, a method for preparing and analyzing GitHub repositories for LLM-based software engineering tasks. Instead of simple file concatenation, RepoUnderstander emphasizes a **structured, hierarchical approach**:
- The repository is organized into a **hierarchical structure tree**, which clarifies the context and scope of code modules.
- A **repository knowledge graph** is constructed, capturing dependencies and function call relationships to provide a comprehensive overview.
- An **MCTS-based exploration strategy** is used to efficiently collect and summarize task-relevant knowledge from the repository.
- Agents are guided to **summarize, analyze, and plan** based on global repository information, then use API tools to dynamically acquire more details as needed.

The paper finds that this structured, top-down method leads to superior performance on benchmarks compared to unstructured approaches (such as simple file concatenation), enabling more precise fault localization and patch generation. It highlights the importance of **global repository experience**, effective summarization, and planning mechanisms for LLMs working with large codebases. The study demonstrates that integrating these practices—rather than relying on raw, unstructured data—significantly enhances LLM understanding and task performance.

Best practices include:
- Building a **repository-level knowledge graph** for context.
- Organizing code and documentation into a **hierarchical structure**.
- Enabling **targeted exploration** with strategies like MCTS.
- Providing **summaries and analyses** to guide LLM reasoning.
Simple file concatenation is not recommended because it fails to provide structure or context, limiting the LLM’s ability to understand dependencies and relationships within the codebase.

-----

-----

-----

### Source [48]: https://github.com/ghimiresunil/LLM-PowerHouse-A-Curated-Guide-for-Large-Language-Models-with-Custom-Training-and-Inferencing

Query: What are the best practices for preparing GitHub repository content for LLM analysis, comparing specialized tools like gitingest versus simple file concatenation?

Answer: This guide highlights **Retrieval Augmented Generation (RAG)** as a best practice for enabling LLMs to analyze large document or code repositories:
- **Orchestrators** (e.g., LangChain, LlamaIndex) are recommended to connect LLMs with tools, databases, and memory mechanisms, facilitating complex repository analysis.
- **Retrievers** are used to optimize the retrieval of relevant code and documentation, rather than naively concatenating files.
- **Memory** strategies (context buffering, summarization, vector stores) help LLMs manage repository context efficiently.
- **Evaluation** tools (e.g., Ragas, DeepEval) are suggested to assess both retrieval quality and generation faithfulness.

The resource suggests that using frameworks like LlamaIndex or LangChain allows for structured ingestion of repository content, supporting functions such as:
- Creating hierarchical indexes of code files and documentation.
- Embedding and storing code/document chunks for efficient retrieval.
- Summarizing or chunking content to fit within LLM context windows.

Simple concatenation of files is not recommended, as it does not provide retrieval mechanisms or context management, which are essential for scalable and accurate LLM analysis of large or complex repositories.

-----

-----

</details>

<details>
<summary>How to implement a token-efficient LLM clean-pass to remove boilerplate (headers, ads, navigation) from scraped markdown content without summarizing the core information?</summary>

### Source [24]: https://www.tigerdata.com/blog/document-loading-parsing-and-cleaning-in-ai-applications

Query: How to implement a token-efficient LLM clean-pass to remove boilerplate (headers, ads, navigation) from scraped markdown content without summarizing the core information?

Answer: Document cleaning is a critical preprocessing step for LLM applications. Raw text extracted from websites or documents is often messy and contains content not relevant to the main text, including ads, navigation menus, footers, tracking scripts, or leftover HTML/CSS markup. Removing this noise is crucial to avoid feeding irrelevant text to your AI model, reduce input token size to lower costs, and increase retrieval accuracy.

Specific elements to clean include `<script>`, `<style>`, `<nav>`, `<footer>`, and similar boilerplate components. Tools like Firecrawl and Jina AI's Reader API already handle webpage data cleaning and return only the main text content automatically.

For more specific requirements, you can use web automation frameworks like Playwright or BeautifulSoup to get the raw DOM, then use traditional DOM traversal or regex patterns to clean the data. This approach gives you fine-grained control over what gets removed.

When dealing with documents that have undergone OCR processing (like those run through Mistral OCR), you'll still have repeated content like page numbers, headers/footers, and repetitive line breaks. A growing technique is using an LLM like Gemini Flash 2.0, which has a two-million-token context window and reasonable costs to automate cleaning. You can use natural language instructions to tell the LLM what to clean: removing repeated titles, sources, footnotes, and other boilerplate elements.

This LLM-based approach is particularly useful because it can understand context and distinguish between boilerplate repetition and legitimate content, ensuring that core information is preserved while noise is removed.

-----

-----

### Source [25]: https://arxiv.org/html/2502.01968v1

Query: How to implement a token-efficient LLM clean-pass to remove boilerplate (headers, ads, navigation) from scraped markdown content without summarizing the core information?

Answer: Token cleaning represents a fine-grained data selection approach for LLM supervised fine-tuning that goes beyond traditional sample-level data cleaning. The framework addresses the reality that even in high-quality samples, patterns or phrases that are not task-related can be redundant or uninformative. Continuing to fine-tune on these patterns may offer limited benefit and even degrade downstream task performance.

The token cleaning pipeline works by first evaluating token quality through an influence-guided scoring mechanism, then applying threshold-based separation to filter out uninformative tokens while preserving those carrying key task-specific information. The method measures token influence by examining the disparity between a base model and a reference model.

Two implementation strategies are supported: Fix-Model Cleaning, where both models remain fixed and one-shot token cleaning is applied to the entire dataset, and Self-Evolving Cleaning, where the base model remains fixed while the reference model is updated iteratively across multiple data parts.

The framework is particularly relevant for markdown content because each sample typically contains hundreds of tokens, some of which occur frequently regardless of the sample's quality. Common tokens and patterns can overshadow task-specific words that are crucial for model performance during training. By removing or down-weighting uninformative tokens, the model can prioritize important content and improve downstream results, effectively reducing token bloat from boilerplate while maintaining semantic value.

-----

</details>

<details>
<summary>What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?</summary>

### Source [26]: https://www.shaped.ai/blog/10-best-practices-in-data-ingestion

Query: What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?

Answer: Efficient management of concurrency and rate limiting in parallel data ingestion pipelines begins with **choosing the appropriate ingestion pattern** (batch, streaming, or hybrid) to suit latency and reliability needs. For real-time or high-concurrency scenarios, a streaming approach (using tools like Kafka or Kinesis) is preferred due to its low latency and event-driven support.

**Idempotency and deduplication** are critical: ensure your ingestion system can process the same event multiple times without adverse effects. Use unique event IDs, window-based deduplication for streaming, and hash-based methods when necessary, all to prevent duplicate records and maintain data integrity under concurrent loads.

**Observability and error handling** should be built in from the start. Monitor ingestion performance, detect bottlenecks, and ensure retries and failures are handled gracefully. This is especially crucial when dealing with third-party APIs, where rate limits or intermittent failures can otherwise disrupt the ingestion process.

The pipeline should be **scalable, fault-tolerant, and capable of handling operational surges or downstream slowdowns** without data loss or corruption. Enforcing these practices is key for reliable, concurrent ingestion from multiple external APIs.

-----

-----

-----

### Source [27]: https://learn.microsoft.com/en-us/answers/questions/1283307/azure-data-factory-best-practices

Query: What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?

Answer: For parallel data ingestion pipelines, **parallel execution** is recommended to boost throughput—this can be achieved by configuring activities (such as "ForEach" in Azure Data Factory) to process tasks in parallel rather than sequentially. 

**Batch size optimization** is important: adjusting the number of records or calls in each batch can help balance performance gains against potential rate limit violations from third-party APIs. Experiment with batch sizes to determine the optimal value that maximizes throughput without exceeding API rate limits.

**Incremental loading** (processing only new or changed data) minimizes redundant API calls and reduces the likelihood of hitting rate limits. This is especially useful when working with APIs that provide mechanisms for incremental data retrieval.

Regularly **monitor performance** and adjust pipeline configuration as needed to maintain efficient, reliable ingestion while respecting concurrency and rate limits imposed by external APIs.

-----

-----

-----

### Source [28]: https://xenoss.io/blog/data-pipeline-best-practices

Query: What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?

Answer: **Parallel processing** is a cornerstone practice: break ingestion jobs into smaller, independently executable workflows to maximize concurrency and processing capacity. Use platforms such as Kafka Streams, AWS Glue, and Hadoop MapReduce for scalable parallelism.

**Modularizing pipelines** by splitting monolithic processes into discrete ETL (Extract, Transform, Load) tasks allows for finer-grained parallel execution and easier identification and resolution of bottlenecks.

**In-memory processing** (using tools like Redis or PySpark) can further accelerate ingestion by reducing disk I/O, supporting high-concurrency operations typical of parallel API calls.

When integrating with third-party APIs, **rate limiting** should be enforced at the workflow or task level to ensure compliance with external service constraints. This can be implemented via token buckets, leaky buckets, or similar algorithms within the ingestion framework.

-----

-----

-----

### Source [29]: https://www.statsig.com/perspectives/designing-scalable-data-ingestion-pipelines

Query: What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?

Answer: Scalable data ingestion pipelines rely on **distributed, real-time collection tools** (like Apache Kafka) and **processing frameworks** (such as Apache Spark) to manage high concurrency and large data volumes efficiently.

**Data quality monitoring** and **real-time observability** (using tools like Datadog or Prometheus) are essential to track pipeline health and performance, detect anomalies, and respond quickly to rate limit or concurrency issues.

The selection of **appropriate storage solutions** (Amazon S3, Azure Data Lake, etc.) ensures that data can be ingested and processed at scale without downstream bottlenecks that might otherwise exacerbate concurrency or rate limit challenges.

Combining these approaches allows pipelines to handle multiple concurrent third-party API calls, maintain stability under varying workloads, and quickly surface issues related to rate limiting or throughput.

-----

-----

-----

### Source [51]: https://www.shaped.ai/blog/10-best-practices-in-data-ingestion

Query: What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?

Answer: Best practices for managing concurrency and rate limiting in parallel data ingestion pipelines include **choosing the right ingestion pattern**, implementing **idempotency and deduplication**, and ensuring **robust observability and error handling**. For concurrency, it's essential to decide between batch, streaming, or hybrid approaches based on latency, volume, and reliability requirements. Streaming ingestion, suited for real-time APIs, requires careful management of ordering, retries, and backpressure to prevent overload and ensure data consistency. Idempotency is crucial in distributed systems as duplicate events are inevitable; deduplication should occur early using unique event IDs, window-based deduplication for streams, or hash-based methods. These techniques ensure the pipeline can handle repeated or delayed calls to third-party APIs without data corruption. Observability tools and error-handling logic are vital for tracking failures and bottlenecks, helping quickly identify issues with third-party API calls, including rate limit exceedances. Together, these practices enhance reliability, scalability, and fault tolerance in modern data ingestion systems that interact with multiple third-party APIs.

-----

-----

-----

### Source [52]: https://learn.microsoft.com/en-us/answers/questions/1283307/azure-data-factory-best-practices

Query: What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?

Answer: To optimize concurrency and rate limiting in parallel data ingestion pipelines, **parallel execution** is recommended: process multiple tasks simultaneously to boost performance, using mechanisms like the "ForEach" activity in Azure Data Factory. This approach allows each API call or data source to be ingested in parallel, increasing throughput. However, it's important to **monitor and optimize batch size**—adjust batch sizes to balance throughput and avoid overwhelming third-party APIs that may enforce rate limits. Regular performance monitoring using built-in tools is also critical; these help detect bottlenecks and rate limit issues, enabling dynamic adjustment of concurrency settings. Additionally, **incremental loading techniques**—such as only fetching new or changed data—reduce the load on APIs, minimizing the risk of hitting rate limits while improving processing efficiency.

-----

-----

-----

### Source [53]: https://estuary.dev/blog/data-ingestion-pipeline/

Query: What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?

Answer: Hybrid data ingestion pipelines combine batch and real-time ingestion to efficiently manage concurrency and rate limiting. By segregating data that requires real-time processing from batch workloads, the system can prioritize urgent API calls and schedule less critical ones in batches, thus reducing peak load and avoiding rate limit violations. Real-time components handle immediate, low-latency ingestion, while batch components manage periodic, larger-volume tasks. Storage strategies are also split: real-time data may be stored in fast-access systems, while batch data resides in traditional warehouses. Scheduling mechanisms and triggers can be configured to start batch processes when API rate limits reset, and real-time processes can include logic to throttle requests dynamically if limits are approached. This architectural approach offers flexibility in managing both concurrency and rate limiting across multiple third-party APIs.

-----

-----

-----

### Source [54]: https://xenoss.io/blog/data-pipeline-best-practices

Query: What are best practices for managing concurrency and rate limiting in a parallel data ingestion pipeline that calls multiple third-party APIs like Firecrawl and Gemini?

Answer: Improving pipeline performance when calling third-party APIs relies on **parallel processing**, where data jobs are split into smaller workflows that run concurrently. This ramps up processing capacity but must be balanced with rate limiting constraints of external APIs. Tools such as Kafka Streams, AWS Glue, and Hadoop MapReduce offer built-in parallelization features. It's beneficial to **split monolithic pipelines into a series of ETL tasks**, allowing more granular control over how and when API calls are made and enabling easier identification and mitigation of bottlenecks caused by rate limiting. **In-memory processing** can reduce the time required for data transformation and loading, which is particularly valuable when waiting for API responses. However, pipelines must include logic to monitor and respect third-party rate limits, potentially queuing or delaying requests to avoid service interruptions or throttling.

-----

-----

</details>

<details>
<summary>What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?</summary>

### Source [30]: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/best-practices/metadata-best-practices

Query: What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?

Answer: Adobe emphasizes the importance of **consistency, accuracy, and completeness** when implementing metadata strategies for digital assets, which can be directly applied to embedding auditability metadata in markdown files. The recommended practices include:

- **Defining a metadata schema:** Clearly outline required metadata fields such as source URL, capture timestamp, and tool version to ensure all files contain the necessary auditability information.
- **Custom metadata fields:** Add dedicated fields for auditability data, ensuring these fields are consistently used across all markdown files. For example, you might include fields like `source_url`, `capture_timestamp`, and `tool_version`.
- **Controlled vocabularies:** Use standardized terms (e.g., consistent field names) to prevent ambiguity and facilitate automated extraction.
- **Metadata validation:** Implement checks to ensure metadata entries are accurate and complete, reducing the risk of missing or inconsistent audit information.
- **Bulk metadata application:** When managing multiple files, apply metadata in bulk to maintain consistency.
- **Assess and improve searchability:** Organize metadata to boost search and retrieval, which is vital in RAG pipelines for traceability and auditing.

While not markdown-specific, these principles strongly support a robust, systematic approach for metadata management, ensuring auditability and reliability in downstream processes.

-----

-----

-----

### Source [31]: https://www.tomarkdown.org/guides/markdown-best-practice

Query: What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?

Answer: This source provides general best practices for Markdown files but does not specifically address embedding auditability metadata. Relevant recommendations include:

- **Consistent document structure:** Use clear heading hierarchies and logical section organization, which can help keep metadata isolated and easy to locate.
- **Valid link formats and URLs:** When including source URLs as part of metadata, ensure they use proper Markdown link syntax for clarity and machine readability.
- **Code blocks for clarity:** Use triple backticks and specify the language for any embedded metadata or configuration information that may be programmatically parsed.
- **UTF-8 encoding and formatting standards:** Adhere to standard character encoding and formatting practices to prevent data corruption, which is crucial for audit trails.

While not specific to auditability, these practices facilitate the clear presentation and reliable extraction of metadata from Markdown files in automated pipelines.

-----

-----

-----

### Source [32]: https://www.ssw.com.au/rules/best-practices-for-frontmatter-in-markdown/

Query: What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?

Answer: This source focuses on the **use of Frontmatter** for embedding metadata into Markdown files, which is considered the most effective method for auditability metadata in RAG pipelines.

- **Frontmatter format:** Place a block at the top of the Markdown file, enclosed within triple dashes (`---`). Common formats include YAML, TOML, or JSON, with YAML being the most widely supported.
- **Key-value pairs:** Use descriptive keys such as `source_url`, `capture_timestamp`, and `tool_version`, each assigned its respective value.
- **Data types:** Values can be strings, numbers, dates, or arrays as appropriate for the metadata.
- **Standardized structure:** Avoid mixing data types or using non-standard formats, which can lead to parsing errors and disrupt downstream processing.
- **Example:**
  ```yaml
  ---
  source_url: "https://example.com/page"
  capture_timestamp: "2025-11-07T01:11:42Z"
  tool_version: "v1.4.2"
  ---
  ```
- **Machine and human readability:** Frontmatter is both easy for people to read and for Markdown processors and RAG pipelines to extract, ensuring reliable auditability.
- **Avoid inline HTML:** Keep metadata in plain text for maximum compatibility.

By following these guidelines, Markdown files can reliably carry auditability metadata, making them suitable for automated ingestion and traceability in RAG systems.

-----

-----

-----

### Source [33]: https://www.appsilon.com/post/r-markdown-reporting-best-practices

Query: What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?

Answer: This source addresses best practices in R Markdown reporting, emphasizing the importance of understanding documentation and leveraging templates for proper metadata inclusion.

- **Consult official documentation:** Refer to the official documentation for tools used (such as R Markdown or other processors) to understand supported metadata schemas and options.
- **Use templates:** RStudio and related packages often provide templates that include standard metadata fields; these can be customized to add auditability data such as source URLs, timestamps, and tool versions.
- **UI support:** Some environments, like RStudio, offer UI-based metadata entry, reducing manual errors and improving consistency.
- **Flexible metadata:** R Markdown allows for custom fields in its document header (YAML frontmatter), which can be adapted for auditability metadata.

While this source is specific to R Markdown, the principle of using the document header (YAML frontmatter) for metadata is widely applicable and aligns with best practices for embedding auditability information.

-----

-----

-----

### Source [55]: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/best-practices/metadata-best-practices

Query: What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?

Answer: Adobe Experience Manager's metadata best practices emphasize the importance of **consistent, accurate, and complete metadata** management for digital assets. While not specific to markdown, these principles are directly applicable when embedding auditability metadata for RAG pipelines:

- **Be consistent with your metadata strategy:** Use standardized and descriptive naming conventions for metadata attributes (e.g., `source_url`, `capture_timestamp`, `tool_version`) to avoid ambiguity and duplication.
- **Use controlled vocabularies:** Employ standardized terms and formats for metadata values to ensure searchability and interoperability. For example, always use ISO 8601 format for timestamps and well-defined URLs.
- **Maintain accuracy and completeness:** Auditability metadata should always be accurate, complete, and aligned across sources. For instance, double-check that URLs are valid and timestamps correctly represent the capture moment.
- **Custom metadata fields:** Add custom fields to store auditability data. In markdown, this typically means defining these fields in a consistent structure (such as frontmatter).
- **Metadata validation:** Use validation checks (manual or automated) to ensure that metadata entries conform to expected formats and do not introduce ambiguity.
- **Usage tracking:** Periodically assess which metadata properties are most useful for auditing and optimize your schema accordingly.

These practices collectively ensure that auditability metadata embedded in markdown files is reliable, discoverable, and interoperable for RAG workflows.

-----

-----

-----

### Source [56]: https://www.tomarkdown.org/guides/markdown-best-practice

Query: What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?

Answer: This guide on Markdown best practices focuses on **document structure, syntax, and formatting standards**, which are foundational for embedding metadata:

- **Heading hierarchy and content organization:** Place metadata in a clearly demarcated section at the beginning of the document, such as a frontmatter block or a dedicated metadata table.
- **Formatting standards:** Use plain text formats (preferably YAML, TOML, or JSON) for metadata, ensuring UTF-8 encoding and proper line breaks. Avoid mixing formatting styles that could hinder parsing.
- **Code blocks and valid URLs:** When embedding source URLs or tool versions, ensure they use valid link formats (`[text](URL)`) and are placed inside appropriate code blocks for clarity if necessary.
- **Whitespace and visual distinction:** Ensure that the metadata section is visually distinct from the rest of the document, using blank lines or horizontal rules if needed.
- **Moderation and clarity:** Avoid cluttering the metadata section with unnecessary information; only include auditability fields essential for traceability (e.g., `source_url`, `capture_timestamp`, `tool_version`).

These recommendations help maintain **clarity, consistency, and machine-readability** of auditability metadata in markdown files designed for RAG ingestion.

-----

-----

-----

### Source [57]: https://www.ssw.com.au/rules/best-practices-for-frontmatter-in-markdown/

Query: What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?

Answer: Frontmatter, typically formatted as **YAML**, is the recommended method for embedding metadata in markdown files. Best practices include:

- **Use key-value pairs:** Structure metadata as simple, descriptive key-value pairs at the top of the markdown file, enclosed by triple dashes (`---`). For auditability, use keys such as `source_url`, `capture_timestamp`, and `tool_version`.
- **Consistent data types:** Each key should have a value of the appropriate type (string for URLs and tool versions, ISO date string for timestamps).
- **Avoid non-standard practices:** Do not mix data types, use inline HTML, or introduce unnecessary complexity—these can cause parsing errors and reduce portability.
- **Portability and simplicity:** Using YAML frontmatter ensures that both humans and machines (including RAG pipelines) can reliably extract and utilize auditability metadata.
- **Example:**
  ```yaml
  ---
  source_url: "https://example.com/article"
  capture_timestamp: "2025-11-07T01:12:23Z"
  tool_version: "v2.3.1"
  ---
  ```
- **Place frontmatter at the very top:** This placement ensures that markdown processors and downstream systems recognize and extract metadata before processing the content.

Following these practices ensures **maximum interoperability, reliability, and clarity** for embedding auditability metadata in markdown for RAG pipelines.

-----

-----

-----

### Source [58]: https://www.appsilon.com/post/r-markdown-reporting-best-practices

Query: What is the most effective way to embed auditability metadata, such as source URL, capture timestamp, and tool version, into markdown files intended for RAG pipelines?

Answer: Appsilon recommends starting with **official documentation** and leveraging built-in templates for metadata management in R Markdown. Relevant points:

- **Read official documentation:** Always consult the maintainer’s documentation for supported metadata fields, formats, and best practices.
- **Use templates:** RStudio (and similar tools) offer markdown templates that include standardized metadata fields in frontmatter, which can be easily extended to include auditability fields.
- **Custom templates:** Create or extend templates to add fields like `source_url`, `capture_timestamp`, and `tool_version` in the YAML frontmatter.
- **Leverage UI tools:** Use graphical user interfaces (e.g., RStudio) to ensure metadata is formatted correctly and adheres to standards.

While focused on R Markdown, these recommendations are applicable for general markdown workflows: **use official tools and documentation to maintain consistency and minimize errors when embedding auditability metadata.**

-----

-----

</details>

<details>
<summary>How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?</summary>

### Source [34]: modelcontextprotocol.info/docs/concepts/prompts/

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: MCP’s server-hosted prompt concept enables discoverable and reusable agent workflows by allowing servers to define and manage prompt templates and workflows centrally, which can then be surfaced to clients and LLMs as needed. This centralization means prompts are not hard-coded into every client or agent, but are instead maintained, versioned, and updated on the server. Clients can dynamically discover available prompts via the list_prompts() method, which returns a catalog of prompt templates, each with metadata such as name, description, and required arguments. For example, a “git-commit” prompt template might require a “changes” argument, while an “explain-code” template might take “code” and optionally “language” arguments. When a client needs a specific prompt, it calls get_prompt(name, arguments), and the server dynamically generates the appropriate prompt messages based on the provided arguments. This allows for consistent, reusable prompt logic across different clients and agents, and makes it easy to update or extend prompts without requiring changes to client code. The example shows that the server can return structured prompt messages (e.g., a user message with templated content), which agents can then use directly. This architecture contrasts with client-side orchestration, where each client must implement and maintain its own prompt logic, leading to duplication, inconsistency, and more complex updates. By hosting prompts on the server, MCP enables a single source of truth for prompt definitions, fostering discoverability through standardized APIs and reusability through shared templates.

-----

-----

### Source [35]: openai.github.io/openai-agents-python/mcp/

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: The MCP protocol’s server-hosted prompt mechanism allows clients to enumerate available prompt templates via list_prompts() and to fetch concrete, parameterized prompts using get_prompt(name, arguments). This enables dynamic discovery of workflows and instructions that agents can use. For instance, a client can request a code review prompt focused on “security vulnerabilities” in “Python,” and the server returns the appropriate instructions, which the client’s agent then uses. This approach decouples the definition and maintenance of agent workflows from the client, centralizing them on the server. Clients and agents remain lightweight, as they do not need to hard-code or manage complex prompt logic. Instead, they rely on the server to provide up-to-date, context-aware prompts. The protocol also supports caching of prompt lists to reduce latency, but clients can invalidate the cache if they suspect prompts have changed. Tracing is built in, so all MCP activity—including prompt discovery and usage—is automatically captured for observability. This architecture makes agent workflows more discoverable (since available prompts are explicitly listed) and more reusable (since the same prompts can be used by multiple agents and clients). In contrast, client-side orchestration would require each client to implement, update, and maintain its own prompt logic, leading to fragmentation and increased maintenance overhead.

-----

-----

### Source [36]: legitsecurity.com/aspm-knowledge-base/whats-an-mcp-server-model-context-protocol-explained

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: MCP servers act as centralized hosts for prompts and workflows, which clients (such as AI assistants) can discover and invoke. When a client sends a request, the MCP server recognizes the session context, checks permissions, and determines which backend or logic to use—including which prompt template to apply. The server then retrieves, merges, and transforms data as needed, and returns a structured response. This allows for sophisticated, context-aware workflows that can be reused across different clients and sessions. By hosting prompts and workflows on the server, MCP ensures that updates and improvements are propagated to all clients automatically, without requiring changes to each client’s code. This is a key advantage over client-side orchestration, where each client must implement and maintain its own logic, leading to inconsistency and increased complexity when updating workflows. The server-hosted model also enables complex orchestration, where one server’s output can feed into another’s input, creating multi-step automation pipelines. This level of integration and reuse is difficult to achieve with client-side orchestration, where workflows are siloed within individual clients. Overall, MCP’s server-hosted approach makes agent workflows more discoverable (through centralized APIs), more reusable (through shared, versioned templates), and more maintainable (through centralized updates).

-----

-----

### Source [37]: descope.com/learn/post/mcp

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: MCP uses a client-server architecture, with the server acting as a central hub for exposing specific functions—including prompts and workflows—to AI applications. The host application (e.g., an IDE or LLM chat interface) contains an MCP client that communicates with MCP servers over a standardized transport layer (STDIO or HTTP+SSE), using JSON-RPC 2.0 for message formatting. Servers are standalone components focused on particular integrations (e.g., GitHub, databases), and can expose discoverable prompts and workflows through the protocol. This architecture allows AI applications to dynamically discover and invoke server-hosted prompts, ensuring that workflow logic is maintained and versioned on the server rather than duplicated across clients. The result is greater consistency, easier updates, and improved reusability of agent workflows. In contrast, client-side orchestration would require each application to implement and maintain its own prompt and workflow logic, leading to fragmentation and increased maintenance burden. MCP’s server-hosted model is inspired by the Language Server Protocol (LSP), which similarly standardizes interactions between development tools and languages, but MCP extends this concept to the broader domain of AI and LLM integrations.

-----

-----

### Source [38]: code.visualstudio.com/docs/copilot/customization/mcp-servers

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: MCP defines a standardized message format for communication between clients and servers, including the discovery, invocation, and response handling of tools and prompts. This means that clients can dynamically discover which prompts and workflows are available from a server, and invoke them in a consistent way. By hosting prompts on the server, MCP enables centralized management and versioning of workflow logic, making it easier to maintain and update prompts across all clients. This is a significant improvement over client-side orchestration, where each client must implement and update its own prompt logic independently. The protocol’s standardization ensures that prompts and workflows are discoverable and reusable across different AI applications and platforms.

-----

-----

### Source [42]: https://modelcontextprotocol.info/docs/concepts/prompts/

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: The **server-hosted prompt** concept in MCP allows servers to define, host, and expose reusable prompt templates that standardize LLM interactions and enable workflow discoverability. These prompts are server-side resources, described with metadata (name, description, arguments), and are accessible to clients through standardized requests such as `list_prompts` and `get_prompt`. By hosting prompt templates on the server:
- **Prompts become discoverable**: Clients can dynamically enumerate available workflows by calling `list_prompts`, allowing any compatible client to explore the server's capabilities without prior knowledge or hardcoding of prompt logic.
- **Prompts are reusable**: The same prompt template, once defined on the server, can be invoked by different clients or workflows and parameterized with user input, ensuring consistency and reducing duplication.
- **Centralized updates**: Changes to prompt templates propagate instantly to all clients, as the logic and content are managed server-side rather than being distributed to clients.
- **Workflow standardization**: By centralizing prompt logic, servers can enforce consistent workflows and best practices across all clients.
In contrast, with client-side orchestration, prompts and workflow logic are hardcoded or managed individually by each client, making workflows less discoverable, harder to update across clients, and less reusable.

Example implementations show how servers define prompt templates (e.g., "git-commit" or "explain-code") and allow clients to list and fetch them with arguments, returning structured prompt messages ready for LLM use.

-----

-----

-----

### Source [43]: https://openai.github.io/openai-agents-python/mcp/

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: MCP servers with **server-hosted prompts** expose methods for prompt discovery and retrieval: `list_prompts()` enumerates available prompt templates, and `get_prompt(name, arguments)` returns a concrete, parameterized prompt. This enables:
- **Dynamic agent workflow construction**: Clients can list available prompts and fetch instructions dynamically from the server, allowing agents to be configured or reconfigured on the fly based on the server's current capabilities.
- **Prompt reuse and sharing**: Because prompts are hosted and managed centrally, the same prompt logic is accessible to different clients and agent instances, promoting reuse and easy sharing of workflows.
- **Simplified agent setup**: Clients do not need to embed prompt logic; instead, they fetch it from the server, reducing maintenance and supporting easier updates.
- **Discoverability**: By listing prompts, clients can automatically present users with available workflows, making it straightforward to discover new or updated agent capabilities without manual configuration.
In contrast, **client-side orchestration** requires clients to manage, update, and distribute prompt logic independently, which fragments workflows and reduces discoverability.

-----

-----

-----

### Source [44]: https://www.legitsecurity.com/aspm-knowledge-base/whats-an-mcp-server-model-context-protocol-explained

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: An MCP server, by hosting prompts and workflows, enables **discoverable and reusable integrations** by acting as a central point for workflow definition and orchestration. When a client requests a workflow (like a specific prompt), the server handles session context, permissions, and backend orchestration, allowing:
- **Centralized workflow management**: Workflows (including prompts) are defined and updated on the server. Clients can discover available workflows by querying the server, rather than relying on pre-defined client-side logic.
- **Composable and chainable workflows**: Multiple MCP servers can participate in a larger workflow, with outputs from one feeding into another, supporting complex, reusable automation pipelines.
- **Rapid workflow evolution**: As workflows are managed server-side, updates and improvements are immediately available to all clients, supporting continuous enhancement and versioning.
Client-side orchestration lacks these benefits, as each client must independently manage workflow logic and updates, making workflow discovery, reuse, and evolution more difficult.

-----

-----

-----

### Source [45]: https://www.descope.com/learn/post/mcp

Query: How does the Model Context Protocol's (MCP) 'server-hosted prompt' concept enable discoverable and reusable agent workflows compared to client-side orchestration?

Answer: MCP’s **client-server architecture** is designed to standardize and centralize how LLMs access prompts, tools, and workflows. The **MCP server** exposes specific capabilities—including prompts—to client applications. By using server-hosted prompts:
- **Clients can query the server for available prompts**, making workflows **discoverable** at runtime rather than statically defined within the client.
- **Standardization of workflows**: Server-hosted prompts ensure that all clients accessing the server use consistent, up-to-date workflow definitions.
- **Separation of concerns**: The client focuses on user interaction and presentation, while the server handles workflow logic, prompt construction, and integration with external systems.
In contrast, **client-side orchestration** embeds workflow definitions in each client, leading to fragmentation (as each client may implement logic differently), difficulty in updating workflows, and limited discoverability for new workflows as they are introduced.

-----

-----

</details>

<details>
<summary>What are the best practices for designing a token-efficient 'LLM clean pass' for scraped web content that removes boilerplate without summarizing?</summary>

### Source [39]: https://arxiv.org/html/2502.00340v1

Query: What are the best practices for designing a token-efficient 'LLM clean pass' for scraped web content that removes boilerplate without summarizing?

Answer: Backward token filtering is highlighted as an effective approach for improving the token efficiency of LLM training by selectively removing inconsequential tokens, allowing the model to focus on the most relevant content. The process involves using a reference model trained on high-quality, domain-specific data (e.g., clean mathematical instructions) to evaluate token importance. During training, the loss of the target model on each token is compared to the loss from the reference model. Tokens with high "excessive loss" (i.e., where the target model performs worse than the reference model) are kept, as they represent more valuable training opportunities, while those with low excessive loss are filtered out. This technique ensures that training resources are concentrated on tokens most beneficial for model learning.

The paper also notes that effective token filtering should extend beyond simply dropping tokens in the output layer; to unlock maximal computational efficiency, the sparsity from token filtering must be preserved throughout the entire backpropagation process. However, this is technically challenging due to limitations in current sparse tensor implementations and the dynamic nature of computation graphs in transformer models. The authors suggest transforming sparse matrix operations into dimension-reduced dense operations to address these challenges, but acknowledge that existing frameworks like PyTorch do not fully support this for LLM training workloads.

Best practices drawn from this source for a token-efficient "LLM clean pass" include:
- Using a high-quality reference model to guide token selection.
- Filtering tokens based on excessive loss to prioritize learning from challenging or informative content.
- Extending filtering to impact the entire computational pipeline, not just the output layer, for optimal efficiency.
- Addressing technical hurdles in sparse computation and dynamic graph handling to realize the full computational savings from token filtering.

The methodology is intended to preserve important content while removing boilerplate or low-value tokens, without summarizing or altering the core information structure.

-----

-----

-----

### Source [40]: https://www.prompts.ai/en/blog/best-practices-for-preprocessing-text-data-for-llms

Query: What are the best practices for designing a token-efficient 'LLM clean pass' for scraped web content that removes boilerplate without summarizing?

Answer: This source emphasizes that systematic cleaning and quality filtering are essential for preparing web-scraped content for LLMs. The recommended best practices for preprocessing include:
- **Cleaning the text**: Remove irrelevant information, boilerplate, and noise (e.g., HTML tags, navigation bars, ads, and repetitive headers/footers) to ensure the remaining content is meaningful for the model.
- **Quality filtering**: Retain only text that is relevant and well-structured, discarding fragments or poorly formatted sections that do not contribute to the intended learning objectives.
- **De-duplication**: Identify and eliminate duplicate or near-duplicate content, as redundant text wastes tokens and skews model learning.
- **Standardization**: Ensure consistency in text formatting, encoding, and language usage, which helps the model process content more efficiently and reduces confusion caused by inconsistent data presentation.
- **Ongoing monitoring**: Continuously review and refine preprocessing workflows to adapt to evolving web content structures and maintain high data quality.

The source also notes that investing effort in thorough preprocessing directly enhances model accuracy and token efficiency, as the model can learn from higher-quality, less noisy data. Automation of these steps using modern tools is encouraged to improve scalability and reduce manual intervention, ensuring that token-efficient clean passes are consistent and maintainable over time.

-----

-----

-----

### Source [41]: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompt-best-practices

Query: What are the best practices for designing a token-efficient 'LLM clean pass' for scraped web content that removes boilerplate without summarizing?

Answer: According to this documentation, minimizing token count is a best practice for optimizing LLM efficiency—both for latency and for overall resource usage. To create a token-efficient "clean pass" for web content:
- **Craft concise inputs**: Strip unnecessary details, boilerplate, and redundancy from the text to reduce the number of tokens processed by the model.
- **Clear intent**: Ensure the remaining content is clear and directly related to the desired task or output, which helps the model process information without confusion or wasted computation.
- **Output control**: Although primarily focused on prompt engineering, the principles apply to content cleaning as well: limiting input size and focusing on essential details leads to faster and more efficient model performance.
- **Systematic removal of boilerplate**: The explicit recommendation is to remove non-essential or repetitive content (like navigation menus or disclaimers) to avoid wasting tokens on irrelevant information.

While this guidance is oriented toward prompt design, the underlying principle is directly applicable to a "clean pass" preprocessing step: by minimizing token count and maximizing relevance, you achieve both efficiency and model clarity, which is especially important when working with large-scale, web-scraped datasets. This approach is essential for reducing LLM computational costs and latency while preserving all critical content.

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>10 Best Practices in Data Ingestion: A Scalable Framework for Real-Time, Reliable Pipelines</summary>

# 10 Best Practices in Data Ingestion: A Scalable Framework for Real-Time, Reliable Pipelines

This post outlines 10 best practices for designing robust, scalable data ingestion pipelines that support real-time analytics, personalization, and machine learning. It covers essential topics like choosing the right ingestion pattern, enforcing data contracts, handling duplicates, implementing observability, and securing data at the edge. With practical guidance for teams building modern data platforms, the post emphasizes reliability, adaptability, and long-term maintainability, plus how tools like Shaped can simplify ingestion for personalization use cases.

June 11, 2025

\|

9

min read

by

Tullie Murrell

Every real-time dashboard, machine learning model, and personalized user experience depends on one foundational layer: data ingestion. It’s the first step in any modern data pipeline, responsible for collecting, validating, and delivering data from source systems into downstream platforms where it can be analyzed, modeled, or acted upon.

Despite its importance, ingestion is often where data quality, reliability, and scalability problems begin. Delayed records, schema mismatches, dropped events, and brittle connectors can quietly break entire analytics stacks, especially as systems grow more complex and distributed.

Whether you're building a real-time recommendation engine or syncing data across microservices, getting ingestion right is critical.

We’ll walk through ten best practices to help you design ingestion systems that are fast, fault-tolerant, and ready to scale. From schema enforcement to error handling and observability, these principles are designed to reduce operational pain and future-proof your data infrastructure.

## 1\. Choose the Right Ingestion Pattern for Your Use Case

Not all ingestion pipelines are built the same, nor should they be. The first decision you’ll need to make is whether to use batch, streaming, or a hybrid approach, depending on the latency, volume, and reliability requirements of your system.

### Batch Ingestion

Ideal for use cases where data can be collected and delivered at scheduled intervals. Think of nightly ETL jobs that pull records from SaaS tools or legacy databases into a warehouse.

- **Common tools:** Airflow, dbt, Snowflake (with Snowpipe), Fivetran
- **Pros:** Simple to manage, easier to debug, lower compute costs for large datasets
- **Cons:** Limited in time-sensitive scenarios; slower to reflect new data

### Streaming Ingestion

Best suited for real-time applications that require immediate access to fresh data—like personalization engines, alerting systems, or fraud detection.

- **Common tools:** Apache Kafka, Apache Pulsar, AWS Kinesis, Apache Flink
- **Pros:** Low latency, continuous processing, event-driven architecture support
- **Cons:** More operational complexity, requires careful handling of ordering, retries, and backpressure

### Hybrid Approach

Most modern data architectures use a mix of both. For example, product events might flow in via Kafka while nightly CRM updates arrive in batches.

Start by understanding the nature of your data and its downstream dependencies. Then choose an ingestion pattern that aligns with how fast you need data to flow and how often it changes.

## 2\. Define and Enforce Data Contracts Early

One of the most common causes of broken pipelines is schema drift, when upstream producers change the shape of data without warning, breaking downstream consumers. The fix? Treat your data interfaces like APIs and formalize them with data contracts.

A data contract defines the expected structure, types, and semantics of ingested data. It can include:

- Required and optional fields
- Data types (e.g. string, integer, timestamp)
- Validation rules (e.g. non-null constraints, enum values)
- Expectations for units, formats, and identifiers

To enforce contracts:

- Use schema definitions (like Avro, Protobuf, or JSON Schema) to validate incoming data at the point of ingestion
- Apply automatic validation checks within streaming pipelines or ingestion gateways
- Break builds or alert when incompatible schema changes are introduced

This practice shifts ingestion from “best-effort parsing” to “explicitly defined expectations,” reducing the risk of downstream failure and improving confidence across data teams.

**Bonus:** Strong contracts make it easier to onboard new producers and automate schema evolution with tools like Confluent Schema Registry, Dataplex, or custom schema validation layers.

## 3\. Prioritize Idempotency and Deduplication

In distributed systems, duplicate events are inevitable. Network retries, service restarts, and inconsistent producer behavior can all result in the same data being ingested multiple times. If your ingestion pipeline isn’t designed to handle this, you risk skewed metrics, double-counted transactions, and corrupted downstream models.

To prevent this, your ingestion system should be idempotent; processing the same event more than once without changing the final outcome. That requires implementing robust deduplication logic as early in the pipeline as possible.

Here are a few proven strategies:

- **Use unique event IDs:** Every ingested event should include a globally unique identifier (UUID or ULID). Deduplication can then be handled via keyed storage, caches, or lookup tables that discard previously seen IDs.
- **Implement window-based deduplication for streams:** In streaming pipelines (e.g. Kafka + Flink), use event-time windows and watermarking to group and deduplicate near-duplicate events. This is especially useful for handling late-arriving data.
- **Hash-based deduplication:** Generate a hash of the event payload and use it to check for duplicates in memory or temporary storage. While less precise than ID-based methods, it’s helpful when upstream systems don’t assign event IDs.

Idempotency ensures your ingestion logic is repeatable, resilient, and accurate, even under failure conditions or scale surges.

## 4\. Instrument Robust Error Handling and Dead Letter Queues

No matter how well you design your pipeline, bad data will eventually show up. Whether it’s a malformed payload, a missing field, or an unexpected schema change, your ingestion system should fail gracefully, not silently or catastrophically.

To make that possible, implement structured error handling and dead letter queues (DLQs).

### Dead Letter Queues

A DLQ is a secondary destination where failed events are routed for later inspection and reprocessing. Rather than discarding problematic records, you preserve them along with metadata such as:

- Timestamp of failure
- Source system or partition
- Error type or parsing stack trace

This makes it easier to triage issues, recover lost data, and debug anomalies without interrupting the main data flow.

Best practices for error handling:

- Tag records with failure codes or validation statuses
- Set thresholds for retries, then escalate to the DLQ
- Separate transient errors (e.g., network failures) from structural ones (e.g., missing fields)
- Monitor DLQ volumes as a signal of upstream quality or system health

Well-instrumented pipelines expose when and why things go wrong. This visibility helps teams move faster, resolve issues proactively, and build more resilient ingestion architectures.

## 5\. Normalize Timestamps and Time Zones at Ingestion

Inconsistent timestamps are one of the most common sources of confusion in data pipelines, especially when data flows in from multiple sources, devices, or regions.

To avoid downstream ambiguity, normalize all time-related fields as early as possible in the ingestion process.

Best practices:

- Store all timestamps in UTC to maintain a single source of temporal truth.
- Capture both event time and ingestion time, especially for streaming pipelines. This allows you to measure processing delays and support event-time windowing in tools like Apache Flink or Kafka Streams.
- Use a consistent format, such as ISO 8601, to simplify parsing and debugging.
- If source data includes ambiguous local time, enrich it with explicit time zone context before normalization.

Proper timestamp handling ensures that downstream systems can safely aggregate, join, and replay data without inconsistencies. It’s a small upfront cost that saves hours of troubleshooting later.

## 6\. Design for Backpressure and Throughput Variability

Ingestion systems need to handle more than steady-state workloads; they must survive bursts, traffic spikes, and upstream anomalies without dropping data or degrading performance.

This requires designing for backpressure, the condition where your system temporarily can’t process incoming data as fast as it’s arriving.

#### How to handle it:

- **Buffer with queues:** Use durable message brokers like Kafka, RabbitMQ, or SQS to decouple producers from consumers.
- **Enable autoscaling:** Use container orchestration tools (like Kubernetes) to scale ingestion workers based on queue depth or throughput metrics.
- **Partition for parallelism:** Distribute load across partitions or shards to improve concurrency and reduce latency.
- **Apply rate limiting and retries:** Control input rates from upstream systems and avoid overloading downstream dependencies.

Monitoring throughput trends and failure modes under pressure is just as important as measuring baseline performance. A well-architected ingestion layer should absorb volatility rather than amplify it.

## 7\. Implement Observability Across the Ingestion Pipeline

You can’t fix what you can’t see. Observability is essential for maintaining data quality, performance, and reliability in complex ingestion systems. Without clear visibility into how data is flowing (or failing), teams are flying blind.

#### What to monitor:

- **Ingestion throughput:** Events per second, per source or topic
- **Lag and latency:** Time between event occurrence and availability downstream
- **Error rates:** Percentage of failed records, categorized by type (schema mismatch, missing fields, etc.)
- **Dropped or retried events:** Volume and cause of retries, dead letters, or discarded records

#### Tooling and instrumentation:

- Use logging frameworks (e.g., structured logs via Fluent Bit or Logstash) to track event-level details
- Apply distributed tracing (e.g., OpenTelemetry) to trace data flow across microservices
- Monitor with Prometheus, Grafana, or vendor-specific dashboards (e.g., Datadog, New Relic)
- Set alerts on abnormal drops, delays, or backlog growth

Observability transforms ingestion from a black box into a transparent, measurable system. It shortens time to resolution, prevents silent failures, and builds confidence across data, engineering, and product teams.

## 8\. Plan for Schema Evolution and Versioning

Data is never static. Fields get added, formats change, and new use cases emerge. If your ingestion pipeline isn’t designed to accommodate evolving schemas, even small changes can cause major disruptions downstream.

#### Why schema evolution matters:

- Producers may update fields, change data types, or restructure payloads
- Consumers may expect different versions of the same dataset
- Backward and forward compatibility is essential for replayability, audits, and historical analysis

#### Best practices:

- **Use versioned schemas** with tools like Avro, Protobuf, or JSON Schema, and store them in a central registry (e.g., Confluent Schema Registry or Apicurio)
- **Support compatibility modes:** Prefer backward-compatible changes (e.g., adding optional fields) over breaking changes (e.g., removing required fields)
- **Validate at ingestion:** Apply schema validation before data reaches your core systems to prevent bad records from propagating
- **Track schema versions in metadata:** Attach a version identifier to each ingested record so downstream systems can parse appropriately

Schema evolution is inevitable. Planning for it upfront allows your ingestion system to grow and adapt without creating instability for consumers.

## 9\. Secure Data at the Edge and In Transit

Data ingestion is often the first point where sensitive information enters your system. Without proper controls in place, this stage can become a major vulnerability, from exposed personally identifiable information (PII) to insecure transport channels.

#### **Key security practices:**

- **Encrypt data in transit:** Use TLS for all inbound connections, whether ingesting from APIs, message brokers, or event streams. Never send raw payloads over unsecured channels.
- **Apply access controls and authentication:** Limit who or what can publish to ingestion endpoints. Use API keys, OAuth tokens, IAM roles, or signed messages to verify trusted sources.
- **Mask or tokenize PII at the edge:** If user data includes names, emails, or identifiers, apply redaction, hashing, or tokenization before storing or processing further downstream.
- **Implement audit logging:** Record who sent what data and when. Include metadata for traceability, especially in regulated environments like finance, healthcare, or education.
- **Restrict scope of access:** Producers should only publish to specific topics, streams, or endpoints. Isolate ingestion components from broader data systems where possible.

Security at the ingestion layer is about establishing trust, preventing leaks, and minimizing the blast radius of failures or misconfigurations.

## 10\. Test with Realistic Loads and Edge Cases

Production data rarely behaves like your staging environment. Late events, malformed payloads, duplicate records, and unexpected spikes are common—and if your ingestion pipeline can’t handle them, it will break when you least expect it.

#### How to test effectively:

- **Replay production traffic (anonymized)** to simulate real-world load, event structure, and timing irregularities
- **Inject failure scenarios**, such as:
  - Events missing required fields
  - Out-of-order or delayed messages
  - Payloads exceeding size limits
  - Unrecognized schema versions
- **Stress test ingestion throughput** with synthetic load generators to evaluate autoscaling, latency, and backpressure handling
- **Establish validation pipelines** to compare input vs. output records and ensure completeness and fidelity
- **Automate ingestion testing in CI** to catch regressions early. Include schema validations, format checks, and deduplication tests as part of every build.

Testing ingestion is about variability. The more edge cases you handle upfront, the more stable and predictable your system will be in production.

## Build Ingestion Systems That Scale With Confidence

Data ingestion sits at the foundation of every modern data pipeline. Whether you're supporting real-time personalization, analytics, or machine learning, ingestion is where reliability, consistency, and trust begin.

Thoughtful ingestion design makes it easier to evolve your data systems without sacrificing quality or velocity.

The strongest data platforms aren’t just fast; they’re built to adapt, recover, and scale under pressure.

</details>

<details>
<summary>Do you know the best practices for Frontmatter in markdown?</summary>

# Do you know the best practices for Frontmatter in markdown?

Frontmatter is a critical component in Markdown files, especially when generating static sites or handling content management. It allows authors and developers to embed metadata directly at the beginning of a Markdown document. This metadata can include information about the document's title, author, date, and other attributes. A well-structured Frontmatter ensures that the Markdown processor can quickly extract the necessary metadata and use it for various purposes, like generating page titles or categorizing posts.

However, when not structured properly, it can lead to parsing errors, inconsistencies, and even disrupt the rendering of the entire page. To avoid these pitfalls and ensure a seamless integration of your Markdown files, it's essential to follow best practices when defining Frontmatter.

### Use Key-Value Pair Organization

Frontmatter is metadata serialized into a plain text format primarily yaml but can also be toml, or json. In Frontmatter, each key represents an attribute, like the title or the author, and the value associated with it provides specific information related to that attribute.

- **Keys** are always strings and should be descriptive enough to indicate the type of data they hold
- **Values** can be strings, numbers, dates, or even arrays, depending on the data you're representing

Using key-value pairs ensures a standardized format, which in turn makes it easier for both humans and machines to read and interpret the data. Moreover, this structured approach ensures that Markdown processors can reliably extract and utilize the metadata, whether it's for rendering a webpage title, categorizing posts, or any other function.
However, avoid non-standard practices like mixing data types or adding unnecessary complexity:

```
–––
title+author: My Article by John
2023-10-31
–––
```

Figure: Bad example - Non-standard practices can lead to parsing errors and inconsistencies

```
–––
title: My Article
author: Bob Northwind
date: 2023-10-31
–––
```

Figure: Good example - Clear key-value pairs make it easy to understand and extract the metadata

### Use Arrays for Complex Data

Arrays in Frontmatter are particularly useful when you have to represent multiple values for a single attribute. In Markdown, an array is essentially a list of values that are associated with a common key.

- **Why Use Arrays?** Sometimes, a single key might have multiple associated values. Instead of creating multiple keys, or stringing values together, arrays provide a clean and organized method to capture this complex data
- **Accessibility:** Arrays make it straightforward for Markdown processors to loop through multiple values, making tasks like generating a list of tags or authors on a webpage much simpler
- **Flexibility:** Arrays can hold strings, numbers, or even other objects, giving you a versatile tool to represent complex structures

However, avoid the common mistake of listing values in a continuous string. This format is harder to parse, and you lose the distinct advantage of the array's structure:

```
–––
authors: John Doe, Jane Smith, Bob Johnson
–––
```

Figure: Bad example - Listing values in a string reduces clarity and makes data extraction challenging

Here's how you can effectively use arrays:

```
–––
authors:
  - Bob Northwind
  - Jane Smith
  - Bob Johnson
–––
```

Figure: Good example - Using arrays helps in listing multiple values under a single key efficiently

### Use Meaningful Keys

The keys you choose for your Frontmatter should be meaningful and descriptive. They act as identifiers for the associated values, so it's essential that they clearly convey the data they represent.

- **Descriptive Names:** Instead of using `desc`, use `description`. Instead of `auth`, use `author`
- **Consistency:** Stick to a consistent naming convention, whether it's camelCase, snake\_case, or kebab-case

Avoid non-descriptive keys:

```
–––
t: My Article
auth: Bob Northwind
–––
```

Figure: Bad example - Shortened or unclear keys can lead to confusion

Use clear, meaningful keys:

```
–––
title: My Article
author: Bob Northwind
–––
```

Figure: Good example - Descriptive keys make Frontmatter easy to understand and work with

### Use Explicit Datatypes

It's crucial to be explicit about datatypes in Frontmatter. This clarity helps Markdown processors understand how to handle the provided metadata correctly.

- **Strings vs. Numbers:** If you're representing a year, use a number, e.g., `2023`. If you're mentioning a title or name, use a string, e.g., `"My Article"`
- **Booleans:** For binary choices, like true or false, use booleans. For example, `published: true`

Avoid ambiguous datatypes:

```
–––
year: '2023'
published: "yes"
–––
```

Figure: Bad example - Ambiguous datatypes can lead to parsing errors

Be explicit with your datatypes:

```
–––
year: 2023
published: true
–––
```

Figure: Good example - Explicit datatypes ensure accurate data representation and extraction

### Avoid Inline HTML

While Markdown allows the integration of inline HTML, it's recommended to avoid using it within Frontmatter. Using HTML can lead to rendering issues, especially when the Markdown is processed by static site generators or other tools.

- **Simplicity:** Sticking to Markdown syntax within Frontmatter keeps the metadata clean and straightforward
- **Portability:** By avoiding HTML, you ensure that the Frontmatter remains compatible with various Markdown processors and platforms

However, some might try to use HTML for additional formatting or structure:

```
–––
title: <em>My</em> Article
author: <strong>Bob Northwind</strong>
–––
```

Figure: Bad example - Using inline HTML can cause unexpected rendering or parsing issues

Stick to plain Markdown:

```
–––
title: "My Article"
author:
  - name: "Bob Northwind"
    role: "Writer"
published: true
year: 2023
tags:
  - Technology
  - Writing
  - Markdown
metadata:
  created_at: "2023-10-30"
  modified_at: "2023-11-06"
–––
```

Figure: Good example - Keeping Frontmatter free of HTML ensures consistent rendering

</details>

<details>
<summary>Enhancing Token Filtering Efficiency in Large Language Model Training with Collider</summary>

# Enhancing Token Filtering Efficiency in Large Language Model Training with Collider

Di Chai1, Pengbo Li1, Feiyuan Zhang1, Yilun Jin1, Han Tian2, Junxue Zhang1, Kai Chen1†

1Hong Kong University of Science and Technology

2University of Science and Technology of ChinaJunxue Zhang and Kai Chen are the corresponding authors.

###### Abstract

Token filtering has been proposed to enhance utility of large language models (LLMs) by eliminating inconsequential tokens during training. While using fewer tokens should reduce computational workloads, existing studies have not succeeded in achieving higher efficiency. This is primarily due to the insufficient sparsity caused by filtering tokens only in the output layers, as well as inefficient sparse GEMM (General Matrix Multiplication), even when having sufficient sparsity.

This paper presents Collider 111A collider is a modern system in physics used for accelerating and colliding particles to uncover deeper insights into the fundamental nature of matter., a system unleashing the full efficiency of token filtering in LLM training. At its core, Collider filters activations of inconsequential tokens across all layers to maintain sparsity. Additionally, it features an automatic workflow that transforms sparse GEMM into dimension-reduced dense GEMM for optimized efficiency. Evaluations on three LLMs—TinyLlama-1.1B Zhang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib38 "")), Qwen2.5-1.5B Yang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib34 "")), and Phi1.5-1.4B Li et al. ( [2023b](https://arxiv.org/html/2502.00340v1#bib.bib17 ""))—demonstrate that Collider reduces backpropagation time by up to 35.1% and end-to-end training time by up to 22.0% when filtering 40% of tokens. Utility assessments of training TinyLlama on 15B tokens indicate that Collider sustains the utility advancements of token filtering by relatively improving model utility by 16.3% comparing to
regular training, and reduces training time from 4.7 days to 3.5 days using 8 GPUs. Collider is designed for easy integration into existing LLM training frameworks, allowing systems already using token filtering to accelerate training with just one line of code.

## 1 Introduction

Training high-quality large language models (LLMs) is notably resource-intensive, requiring substantial investments in both data and computational power. For example, the training of foundational models such as LLaMA 3-70B necessitates approximately 7 million GPU hours and over 15 trillion high-quality tokens Dubey et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib9 "")). _Token filtering_ represents an emerging paradigm aimed at enhancing the cost-efficiency of LLM training by systematically discarding less significant tokens early in the training process222This paper primarily focuses on backward filtering, as it demonstrates superior performance in enhancing the capabilities of LLMs. Further details can be found in § [2.1](https://arxiv.org/html/2502.00340v1#S2.SS1 "2.1 LLM Training & Token Filtering ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"). This methodology enables the model to concentrate on the most pertinent tokens, resulting in up to 30% absolute improvement in model utility across various tasks Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")).

While the effectiveness of token filtering in enhancing model utility is well recognized within the AI community333Rho-1 Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) received the Best Paper Runner-up Award at NeurIPS 2024., its potential to improve computational efficiency in training remains largely unexplored. In principle, by significantly reducing the number of tokens processed in the computational pipeline, token filtering should decrease computational demands and expedite training. However, our experiments, which combine token filtering with existing LLM training systems, demonstrate only a modest 1.2% speedup in training time, even when 40% of the tokens are eliminated (§ [2.2](https://arxiv.org/html/2502.00340v1#S2.SS2 "2.2 Existing Token Filtering Fails to Improve Efficiency ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")). This limited enhancement in training efficiency constrains the broader advantages of token filtering for large-scale LLM training. Therefore, we pose the question: _Can we fully unlock the efficiency of token filtering while simultaneously achieving greater utility than conventional training?_

To address this question, we first investigate the key factors limiting the efficiency gains of existing token filtering system: (1) Insufficient sparsity after token filtering: Existing approaches fail to create true sparsity following token filtering Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")). These methods drop tokens only at the first stage of backpropagation—the loss computation layer—along with their corresponding loss values, without modifying the generated gradients. As a result, in subsequent backpropagation steps, the hidden states of the dropped tokens are still updated because they contribute to the computed gradients (via attention). This leads to dense matrix computations, undermining the efficiency of token filtering. (2) Inefficiency of sparse matrix implementations: Even when sparse matrices are employed, existing sparse GEMM (General Matrix Multiplication) implementations fail to fully exploit the sparsity introduced by token filtering. Current implementations are effective only when sparsity exceeds 95%percent9595\\%95 % (§ [2.2](https://arxiv.org/html/2502.00340v1#S2.SS2 "2.2 Existing Token Filtering Fails to Improve Efficiency ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")), whereas the sparsity achieved through backward token filtering typically ranges between 30%percent3030\\%30 % and 40%percent4040\\%40 %Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")). Our experiments demonstrate that directly applying existing GEMM implementations to backward token filtering even significantly increase the training time (§ [2.2](https://arxiv.org/html/2502.00340v1#S2.SS2 "2.2 Existing Token Filtering Fails to Improve Efficiency ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")).

To tackle the two aforementioned challenges and fully unlock the training efficiency enabled by token filtering, we propose Collider. To the best of our knowledge, Collider is the first system designed to unleash the performance potential of token filtering. At its core, Collider integrates two key ideas:

- 1.

Collider carefully analyzes the backward computation graph and proposes further filtering activations of inconsequential tokens during backpropagation to retain sufficient sparsity. Collider sustains the utility advancements of existing token filtering method Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) and increases the opportunity for efficiency improvement.

- 2.

Collider leverages the characteristics of token filtering—specifically, the sparsity of matrices in either columns or rows—to transform sparse GEMM into dimension-reduced dense GEMM, maximizing performance on existing hardware. However, PyTorch’s dynamic graph nature complicates global updates to dimensions and variables, as graph variability and node differences prevent static rules for correctness. To overcome this, we design an automatic workflow leveraging the runtime stability ( _i.e_., the graph remains stable during the training) to dynamically identify and update the necessary dimensions and variables before backpropagation.

We implement Collider as a PyTorch C++ extension that can be easily integrated into existing training pipelines with minimal code changes. Systems already using backward token filtering only need to add one line of code to achieve efficiency improvement. We leverage Torchgen444Torchgen is a tool used to autogenerate wrappers for the torch package. In particular, the node processing codes in autograd graph are generate using gen\_autograd.py in Torchgen. to automatically generate graph updating code for different models, ensuring compatibility with a wide range of LLM architectures. Our system is compatible with widely-used efficient attention implementations ( _e.g_., FlashAttention) and can also work with parallelism strategies like tensor parallelism to further reduce communication costs (dicsussed in § [4.2](https://arxiv.org/html/2502.00340v1#S4.SS2 "4.2 Collider Reduces Communication Overheads in Distributed Training ‣ 4 Discussion ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")).

We evaluate Collider comprehensively regarding utility and efficiency using three tiny but mighty models: TinyLlama Zhang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib38 "")), Qwen2.5-1.5B Yang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib34 "")), and Phi-1.5 Li et al. ( [2023b](https://arxiv.org/html/2502.00340v1#bib.bib17 "")).
Using the same parameter settings from previous work Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 ""))
, utility assessments of training TinyLlama on open-web-math with 15 billion tokens show that the Collider improves model utility by an average of 16.3% across nine tasks comparing to regular training and reduces training duration from 4.5 to 3.7 days using eight NVIDIA 3090 GPUs.
While Collider offers significant efficiency improvements over existing backward filtering Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")), it shows slightly decreased model utility as it necessitates different optimal parameter settings and more details are discussed in § [4.1](https://arxiv.org/html/2502.00340v1#S4.SS1 "4.1 Filtering Activations Necessitates Different Training Parameters ‣ 4 Discussion ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider").

Efficiency evaluation on three LLMs indicate that the Collider can reduce the backward computation by up to 35.1% and lower overall training time up to 22% when filtering 40% of tokens. The efficiency improvements of Collider is more pronounced with longer contexts and higher filtering ratios.

## 2 Background and Motivation

### 2.1 LLM Training & Token Filteringhttps://arxiv.org/html/2502.00340v1/x1.pngFigure 1: An overview of LLM training.

Training LLMs is a computationally intensive process that that demands substantial computational resources. Figure [1](https://arxiv.org/html/2502.00340v1#S2.F1 "Figure 1 ‣ 2.1 LLM Training & Token Filtering ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") shows an overview of the LLM training process. The training data is first tokenized and fed into the LLM, which consists of multiple transformer layers. The model processes the input data and generates predictions, which are compared to the ground truth labels ( _i.e_., next tokens) to compute the loss. Finally, gradients are computed based on the loss to update the model parameters.
Two primary factors significantly influence the computational cost: the size of the model ( _e.g_., the number of layers) and the number of training tokens. For instance, training foundation models like LLaMA3-70B requires approximately 7 million GPU hours and involves processing more than 15 trillion tokens. Additionally, LLM-based applications necessitate extensive domain knowledge to fine-tune the model, which can also be computationally expensive—particularly for applications that require frequent updates ( _e.g_., LLM-based recommender systems Lin et al. ( [2024a](https://arxiv.org/html/2502.00340v1#bib.bib19 ""))).
Accelerating LLM training is crucial to enable faster application development, reducing costs, and minimizing the environmental impact of training LLMs.

Existing studies have explored various techniques to accelerate LLM training. However, many of them either leave limited room for further improvement or adversely affect model utility. Specifically, distributed training systems Narayanan et al. ( [2021](https://arxiv.org/html/2502.00340v1#bib.bib26 "")); Jiang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib13 "")) have been proposed to effectively leverage computational resources in parallel and reduce idle time in the computation pipeline by overlapping communication and data input/output (I/O) with computations. State-of-the-art LLM training systems Jiang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib13 "")) have achieved 55.2% model FLOPs utilization (MFU) while training on more than 10,000 GPUs. Further enhancing the utilization rate of hardware remains a challenging task with limited room for improvement.
Techniques such as layer freezing Li et al. ( [2023a](https://arxiv.org/html/2502.00340v1#bib.bib16 "")); Wang et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib33 "")), model pruning Ma et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib22 "")); Sun et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib31 "")), and low-rank fine-tuning Hu et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib12 "")) have been explored to reduce the number of trainable model parameters and improve training efficiency. However, decreasing the number of trainable parameters may negatively impact the model’s utility and generalization ability Ding et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib8 "")).

Token filtering is a recently proposed technology that has been well recognized by the AI community. The core idea is to identify and filter out tokens that are either noisy or unlikely to contribute meaningfully to the training process, which implicitly improves the quality of training data to benefit the model utility. Moreover, by reducing the total number of tokens to be trained, token filtering also brings opportunity for efficiency improvement.

Existing token filtering works can be categorized into two types: _forward token filtering_ and _backward token filtering_. As illustrated in [Figure2](https://arxiv.org/html/2502.00340v1#S2.F2 "In 2.1 LLM Training & Token Filtering ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"), forward token filtering techniques remove training tokens during the forward pass, whereas backward token filtering methods eliminate tokens exclusively during the backward pass.https://arxiv.org/html/2502.00340v1/x2.pngFigure 2: An overview of existing token filter studies. Forward token filtering methods (a) filter hidden states during forward process, while backward token filtering methods (b) filter training loss during the backward process.

Forward token filtering methods have been extensively studied in previous works Hou et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib11 "")); Zhong et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib40 "")); Yao et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib35 "")); Ataiefard et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib4 "")). However, they typically underperform compared to backward filtering methods due to semantic losses Zhong et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib40 "")); Yao et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib35 "")); Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")). As shown in [Figure2](https://arxiv.org/html/2502.00340v1#S2.F2 "In 2.1 LLM Training & Token Filtering ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"), forward token filtering methods filter tokens at each layer of the forward computation, such that each layer of the model only processes partial context. However, this approach has been shown to cause semantic loss and potential harm model utility Zhong et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib40 "")); Yao et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib35 "")). Evaluations in existing forward filtering studies Hou et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib11 "")); Zhong et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib40 "")); Yao et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib35 "")); Ataiefard et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib4 "")) report only similar or lower model utilities and fail to achieve the improvements in utility seen with backward filtering methods Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")).

Backward token filtering is an effective solution for enhancing model utility and is widely accepted within the AI community. Existing work Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) has demonstrated that backward filtering methods can not only reduce the number of training tokens processed during the backward pass but also improve model utility by eliminating inconsequential tokens. As illustrated in [Figure2](https://arxiv.org/html/2502.00340v1#S2.F2 "In 2.1 LLM Training & Token Filtering ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"), the backward filtering method maintains standard forward computation while performing selective token training in the output layer.
Existing studies leverage a reference model to assess the importance of each token. For instance, when training a target model to enhance mathematical reasoning, the reference model is trained on a small but high-quality mathematical corpus ( _e.g_., clean datasets with clear instructions and derivations). During the training process, the loss of the target model ( _i.e_., the model being trained) is compared to the loss of the reference model. Tokens with high excessive loss ( _i.e_., the loss of the target model minus the loss of the reference model) are considered important, while those with lower excessive loss are filtered out during the backward pass.
Empirically, tokens with high excessive loss have larger room to be trained, and lower loss in the reference model also indicates that the tokens match the distribution of high-quality data. Mathematically, backward token filtering can be formulated as follows Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")):

| | | | |
| --- | --- | --- | --- |
| | ℒf⁢i⁢l⁢t⁢e⁢r=−1N×k%⁢∑i=1NIk%⁢(𝐱i)⁢log⁡Pθ⁢(𝐱i\|𝐱<i;θ)subscriptℒ𝑓𝑖𝑙𝑡𝑒𝑟1𝑁percent𝑘subscriptsuperscript𝑁𝑖1subscript𝐼percent𝑘subscript𝐱𝑖subscript𝑃𝜃conditionalsubscript𝐱𝑖subscript𝐱absent𝑖𝜃\\mathcal{L}\_{filter}=-\\frac{1}{N\\times k\\%}\\sum^{N}\_{i=1}I\_{k\\%}(\\mathbf{x}\_{i%<br>})\\log P\_{\\theta}(\\mathbf{x}\_{i}\|\\mathbf{x}\_{<i};\\theta)caligraphic\_L start\_POSTSUBSCRIPT italic\_f italic\_i italic\_l italic\_t italic\_e italic\_r end\_POSTSUBSCRIPT = - divide start\_ARG 1 end\_ARG start\_ARG italic\_N × italic\_k % end\_ARG ∑ start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT italic\_I start\_POSTSUBSCRIPT italic\_k % end\_POSTSUBSCRIPT ( bold\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) roman\_log italic\_P start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT ( bold\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT \| bold\_x start\_POSTSUBSCRIPT < italic\_i end\_POSTSUBSCRIPT ; italic\_θ ) | | (1) |

| | | | |
| --- | --- | --- | --- |
| | Ik%(𝐱i)={1,i⁢f⁢𝐱i∈t⁢o⁢p⁢k%⁢o⁢f⁢(ℒθ⁢(𝐱i)−ℒr⁢e⁢f⁢(𝐱i))0,otherwiseI\_{k\\%}(\\mathbf{x}\_{i})=\\left\\{\\begin{aligned} 1,&\ if\ \\mathbf{x}\_{i}\ \\in\ %<br>top\ k\\%\ of\ (\\mathcal{L}\_{\\theta}(\\mathbf{x}\_{i})-\\mathcal{L}\_{ref}(\\mathbf{%<br>x}\_{i}))\\\<br>0,&\ \\text{otherwise}\\end{aligned}\\right.italic\_I start\_POSTSUBSCRIPT italic\_k % end\_POSTSUBSCRIPT ( bold\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) = { start\_ROW start\_CELL 1 , end\_CELL start\_CELL italic\_i italic\_f bold\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ∈ italic\_t italic\_o italic\_p italic\_k % italic\_o italic\_f ( caligraphic\_L start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT ( bold\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) - caligraphic\_L start\_POSTSUBSCRIPT italic\_r italic\_e italic\_f end\_POSTSUBSCRIPT ( bold\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) ) end\_CELL end\_ROW start\_ROW start\_CELL 0 , end\_CELL start\_CELL otherwise end\_CELL end\_ROW | | (2) |

where ℒθsubscriptℒ𝜃\\mathcal{L}\_{\\theta}caligraphic\_L start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT is the loss of the target model, ℒr⁢e⁢fsubscriptℒ𝑟𝑒𝑓\\mathcal{L}\_{ref}caligraphic\_L start\_POSTSUBSCRIPT italic\_r italic\_e italic\_f end\_POSTSUBSCRIPT is the loss of the reference model, and ℒf⁢i⁢l⁢t⁢e⁢rsubscriptℒ𝑓𝑖𝑙𝑡𝑒𝑟\\mathcal{L}\_{filter}caligraphic\_L start\_POSTSUBSCRIPT italic\_f italic\_i italic\_l italic\_t italic\_e italic\_r end\_POSTSUBSCRIPT is the actual loss to train the target model while keeping k%percent𝑘k\\%italic\_k % of tokens.

In this paper, we mainly focus on backward token filtering due to its aforementioned advantages.

### 2.2 Existing Token Filtering Fails to Improve Efficiency

Although backward token filtering has shown promising results in improving model utility, its potential of improving training efficiency remains unexplored. In principle, reducing the number of training tokens should bring significant efficiency improvement due to the reduced computation workload. However, existing studies fail to improve training efficiency due to the following two reasons: (1) insufficient sparsity after token filtering; and (2) inefficiency of sparse GEMM implementations.

Insufficient sparsity after token filtering.
The potential for efficiency improvements in token filtering methods arises from the sparsity achieved by filtering out unimportant tokens. The gradients of the filtered tokens become zero, allowing for a reduction in computational costs during the backward process. Essentially, backpropagation involves computations between gradients and activations, which are intermediate results specifically stored for the backward pass.
Current methods filter the loss of unimportant tokens at the output layer, resulting in sparse gradients. However, they leave all dense activations unchanged. Consequently, after being multiplied by these dense activations, the gradients are no longer sparse once they pass through the final attention block. Therefore, existing backward filtering methods Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) exhibit insufficient sparsity, even after filtering the loss at the output layer.

[Equation3](https://arxiv.org/html/2502.00340v1#S2.E3 "In 2.2 Existing Token Filtering Fails to Improve Efficiency ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") shows the forward computation of the attention block in the transformer model, where s⁢o⁢f⁢t⁢m⁢a⁢x⁢(𝐐𝐊T/d)𝑠𝑜𝑓𝑡𝑚𝑎𝑥superscript𝐐𝐊𝑇𝑑softmax(\\mathbf{Q}\\mathbf{K}^{T}/\\sqrt{d})italic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x ( bold\_QK start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT / square-root start\_ARG italic\_d end\_ARG ) is stored as activation555Eager implementation of attention block in PyTorch stores the softmax as intermediate results. The FlashAttention recomputes the the softmax matrix during backward, which is mathematically equalivent to storing the matrix..

| | | | |
| --- | --- | --- | --- |
| | 𝐗=s⁢o⁢f⁢t⁢m⁢a⁢x⁢(𝐐𝐊Td)×𝐕𝐗𝑠𝑜𝑓𝑡𝑚𝑎𝑥superscript𝐐𝐊𝑇𝑑𝐕\\mathbf{X}=softmax(\\frac{\\mathbf{Q}\\mathbf{K}^{T}}{\\sqrt{d}})\\times\\mathbf{V}bold\_X = italic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x ( divide start\_ARG bold\_QK start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT end\_ARG start\_ARG square-root start\_ARG italic\_d end\_ARG end\_ARG ) × bold\_V | | (3) |https://arxiv.org/html/2502.00340v1/x3.pngFigure 3: Leaving the activation ( _i.e_., s⁢o⁢f⁢t⁢m⁢a⁢x𝑠𝑜𝑓𝑡𝑚𝑎𝑥softmaxitalic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x) of filtered tokens unchanged makes the 𝐕𝐕\\mathbf{V}bold\_V’s gradients computed by the attention block not sparse anymore after the backpropagation. The dense gradients 𝐆Vsubscript𝐆𝑉\\mathbf{G}\_{V}bold\_G start\_POSTSUBSCRIPT italic\_V end\_POSTSUBSCRIPT will be passed to the front layers, undermining sparsity in all the rest computations .

[Figure3](https://arxiv.org/html/2502.00340v1#S2.F3 "In 2.2 Existing Token Filtering Fails to Improve Efficiency ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") illustrates the process of computing gradients for 𝐕𝐕\\mathbf{V}bold\_V ( _i.e_., 𝐆𝐕subscript𝐆𝐕\\mathbf{G\_{V}}bold\_G start\_POSTSUBSCRIPT bold\_V end\_POSTSUBSCRIPT) using sparse gradients while maintaining unchanged activations ( _i.e_., activations of all tokens are retained). After filtering the tokens based on loss, the gradients of the corresponding tokens become zero, as depicted in [Figure3](https://arxiv.org/html/2502.00340v1#S2.F3 "In 2.2 Existing Token Filtering Fails to Improve Efficiency ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"). However, because the activations of the filtered tokens remain unchanged, the gradients of 𝐕𝐕\\mathbf{V}bold\_V are no longer sparse. Consequently, the backward computation following the first attention block lacks sparsity, limiting efficiency improvements solely within the output layer.

Following the setting in existing work Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")), we can estimate the upper bound of efficiency improvement with existing token filtering schemes. Taking TinyLlama, a model with 22 layers and 1.1B parameters, as an example. Filtering 40% tokens will only linearly improve the efficiency on backward propagation of the last layer, while no front layers can be improved. Thus, the overall backward efficiency can only be improved by 1.8%. Given that backpropagation consumes 66% of the whole training Narayanan et al. ( [2021](https://arxiv.org/html/2502.00340v1#bib.bib26 "")), the end-to-end efficiency improvement is only 1.2%.

To unlock the full efficiency of token filtering, we propose to further filter the activations to retain the sparsity in the whole backpropagation, as we illustrate in § [3.1](https://arxiv.org/html/2502.00340v1#S3.SS1 "3.1 Activations or Loss? ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider").

Inefficient sparse GEMM. Existing sparse GEMM implementations are not well-suited for token filtering training. Although sparse GEMM is a hot research topic and PyTorch has provided a sparse tensor implementation ( _i.e_., torch.sparse), the efficiency of existing sparse GEMM is only improved when the data has very high sparsity ( _e.g_., 95%). Furthermore, torch.sparse does not fully support model training. For instance, the commonly used Compressed Sparse Row (CSR) format only accommodates 2D tensors, whereas the data in transformer models is typically represented as 3D or 4D tensors.https://arxiv.org/html/2502.00340v1/x4.pngFigure 4: PyTorch sparse GEMM outperforms regular GEMM only when filtering more than 95% tokens and cannot improve efficiency of token filtering training which typically drops 30% ∼similar-to\\sim∼ 40% tokens Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")).

To demonstrate the problem, we perform experiments on our testbed (details in § [6.1](https://arxiv.org/html/2502.00340v1#S6.SS1 "6.1 Experimental Setup ‣ 6 Evaluation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")).
We compare the efficiency of sparse GEMM in PyTorch and regular GEMM in the scenario of token filtering, _i.e_., the matrix is sparse by row or columns. [Figure4](https://arxiv.org/html/2502.00340v1#S2.F4 "In 2.2 Existing Token Filtering Fails to Improve Efficiency ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") shows the comparison results under different ratios of token filtering and batch sizes. The sparse GEMM is more efficient only when over 95% of all tokens are filtered, which is unrealistic for token filtering. Under the typical filtering rate of 40%, sparse GEMM is even 10×\\times× slower than regular GEMM.

## 3 Collider

To solve this problem, we propose Collider, a system that unleashes the full efficiency of token filtering. Collider features two main design points: 1) Collider filters the activations in the backward computation to retain sufficient sparsity (§ [3.1](https://arxiv.org/html/2502.00340v1#S3.SS1 "3.1 Activations or Loss? ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")); 2) Collider transforms the sparse GEMM to dimension-reduced dense GEMM through automatically updating the backward computation graph to achieve maximum performance with existing hardware (§ [3.2](https://arxiv.org/html/2502.00340v1#S3.SS2 "3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")).

### 3.1 Activations or Loss?

Although existing method Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) filters loss of inconsequential tokens at the output layer, they leave activations of filtered tokens unchanged which will subsequently participate in the backward computation and cause dense gradients. The backward computation starts at the last layer and propagates to the first layer. Essentially, the gradients passed from the i𝑖iitalic\_i-th layer to the i−1𝑖1i-1italic\_i - 1-th layer are computed based on the input gradients and activations of the i𝑖iitalic\_i-th layer. Existing works leave the activations unchanged, _i.e_., the dense activation of the filtered tokens are still stored in the memory and used for computing the gradients. Thus, even though the input gradients of the i𝑖iitalic\_i-th layer are sparse, the activations are dense and the gradients passed to the i−1𝑖1i-1italic\_i - 1-th layer are also dense, leading to limited optimization opportunities. To solve this problem, Collider further filters the activations in the backward computation to retain suffcient sparsity.

To understand how the activations impact the gradient computation, we first analyze the forward and backward computations of the attention block. [Equation4](https://arxiv.org/html/2502.00340v1#S3.E4 "In 3.1 Activations or Loss? ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") shows the forward computation of the self-attention, where 𝐗𝐗\\mathbf{X}bold\_X is the input, 𝐖Q,𝐖Ksubscript𝐖𝑄subscript𝐖𝐾\\mathbf{W}\_{Q},\\mathbf{W}\_{K}bold\_W start\_POSTSUBSCRIPT italic\_Q end\_POSTSUBSCRIPT , bold\_W start\_POSTSUBSCRIPT italic\_K end\_POSTSUBSCRIPT are the model parameters, and 𝐐,𝐊,𝐕𝐐𝐊𝐕\\mathbf{Q,K,V}bold\_Q , bold\_K , bold\_V are the query, key, and value matrices, and 𝐗′superscript𝐗′\\mathbf{X^{\\prime}}bold\_X start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT is the output. [Equation5](https://arxiv.org/html/2502.00340v1#S3.E5 "In 3.1 Activations or Loss? ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") shows the backward computation of the attention block, where the underlined terms are the activations saved during the forward computation. We make the following observations:

- ∙∙\\bullet∙

The activation of s⁢o⁢f⁢t⁢m⁢a⁢x𝑠𝑜𝑓𝑡𝑚𝑎𝑥softmaxitalic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x determines the sparsity of 𝐕𝐕\\mathbf{V}bold\_V’s gradient. It also implicitly impacts the gradients of 𝐐𝐐\\mathbf{Q}bold\_Q and 𝐊𝐊\\mathbf{K}bold\_K through 𝐆Asubscript𝐆𝐴\\mathbf{G}\_{A}bold\_G start\_POSTSUBSCRIPT italic\_A end\_POSTSUBSCRIPT ( _i.e_., 𝐆Asubscript𝐆𝐴\\mathbf{G}\_{A}bold\_G start\_POSTSUBSCRIPT italic\_A end\_POSTSUBSCRIPT is also computed based on s⁢o⁢f⁢t⁢m⁢a⁢x𝑠𝑜𝑓𝑡𝑚𝑎𝑥softmaxitalic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_xDao et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib7 ""))). Thus, the activation of s⁢o⁢f⁢t⁢m⁢a⁢x𝑠𝑜𝑓𝑡𝑚𝑎𝑥softmaxitalic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x needs to be filtered to retain the sparsity. Specifically, we remove the data corresponding to the filtered tokens.

- ∙∙\\bullet∙

The activations of linear transformation ( _e.g_., 𝐖Qsubscript𝐖𝑄\\mathbf{W}\_{Q}bold\_W start\_POSTSUBSCRIPT italic\_Q end\_POSTSUBSCRIPT) only work on the hidden dimensions and do not impact the sequence dimension, thus having no impact on the sparsity of the gradients ( _i.e_., filtering tokens will only bring sparsity in the sequence dimension). Similarly, the activations in the feedforward network (FFN) do not need to be filtered.

| | | | |
| --- | --- | --- | --- |
| | {𝐐=𝐗×𝐖Q,𝐊=𝐗×𝐖K,𝐕=𝐗×𝐖V𝐀=𝐐×𝐊T/d𝐗′=s⁢o⁢f⁢t⁢m⁢a⁢x⁢(𝐀)×𝐕\\left\\{\\begin{aligned} \\mathbf{Q}&=\\mathbf{X}\\times\\mathbf{W}\_{Q},\ \\mathbf{K}%<br>=\\mathbf{X}\\times\\mathbf{W}\_{K},\ \\mathbf{V}=\\mathbf{X}\\times\\mathbf{W}\_{V}\\\<br>\\mathbf{A}&=\\mathbf{Q}\\times\\mathbf{K}^{T}/\\sqrt{d}\\\<br>\\mathbf{X^{\\prime}}&=softmax(\\mathbf{A})\\times\\mathbf{V}\\\<br>\\end{aligned}\\right.{ start\_ROW start\_CELL bold\_Q end\_CELL start\_CELL = bold\_X × bold\_W start\_POSTSUBSCRIPT italic\_Q end\_POSTSUBSCRIPT , bold\_K = bold\_X × bold\_W start\_POSTSUBSCRIPT italic\_K end\_POSTSUBSCRIPT , bold\_V = bold\_X × bold\_W start\_POSTSUBSCRIPT italic\_V end\_POSTSUBSCRIPT end\_CELL end\_ROW start\_ROW start\_CELL bold\_A end\_CELL start\_CELL = bold\_Q × bold\_K start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT / square-root start\_ARG italic\_d end\_ARG end\_CELL end\_ROW start\_ROW start\_CELL bold\_X start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT end\_CELL start\_CELL = italic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x ( bold\_A ) × bold\_V end\_CELL end\_ROW | | (4) |

| | | | |
| --- | --- | --- | --- |
| | {𝐆V=s⁢o⁢f⁢t⁢m⁢a⁢xT¯×𝐆X′𝐆Q=𝐆A×𝐊¯×d𝐆K=𝐆AT×𝐐¯×d𝐆X=𝐆Q×𝐖QT¯⁢\|𝐆K×𝐖KT¯\|⁢𝐆V×𝐖VT¯\\left\\{\\begin{aligned} \\mathbf{G}\_{V}&=\\underline{softmax^{T}}\\times\\mathbf{G}%<br>\_{X^{\\prime}}\\\<br>\\mathbf{G}\_{Q}&=\\mathbf{G}\_{A}\\times\\underline{\\mathbf{K}}\\times\\sqrt{d}\\\<br>\\mathbf{G}\_{K}&=\\mathbf{G}\_{A}^{T}\\times\\underline{\\mathbf{Q}}\\times\\sqrt{d}\\\<br>\\mathbf{G}\_{X}&=\\mathbf{G}\_{Q}\\times\\underline{\\mathbf{W}\_{Q}^{T}}\ \|\ \\mathbf%<br>{G}\_{K}\\times\\underline{\\mathbf{W}\_{K}^{T}}\ \|\ \\mathbf{G}\_{V}\\times\\underline%<br>{\\mathbf{W}\_{V}^{T}}\\\<br>\\end{aligned}\\right.{ start\_ROW start\_CELL bold\_G start\_POSTSUBSCRIPT italic\_V end\_POSTSUBSCRIPT end\_CELL start\_CELL = under¯ start\_ARG italic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT end\_ARG × bold\_G start\_POSTSUBSCRIPT italic\_X start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT end\_CELL end\_ROW start\_ROW start\_CELL bold\_G start\_POSTSUBSCRIPT italic\_Q end\_POSTSUBSCRIPT end\_CELL start\_CELL = bold\_G start\_POSTSUBSCRIPT italic\_A end\_POSTSUBSCRIPT × under¯ start\_ARG bold\_K end\_ARG × square-root start\_ARG italic\_d end\_ARG end\_CELL end\_ROW start\_ROW start\_CELL bold\_G start\_POSTSUBSCRIPT italic\_K end\_POSTSUBSCRIPT end\_CELL start\_CELL = bold\_G start\_POSTSUBSCRIPT italic\_A end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT × under¯ start\_ARG bold\_Q end\_ARG × square-root start\_ARG italic\_d end\_ARG end\_CELL end\_ROW start\_ROW start\_CELL bold\_G start\_POSTSUBSCRIPT italic\_X end\_POSTSUBSCRIPT end\_CELL start\_CELL = bold\_G start\_POSTSUBSCRIPT italic\_Q end\_POSTSUBSCRIPT × under¯ start\_ARG bold\_W start\_POSTSUBSCRIPT italic\_Q end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT end\_ARG \| bold\_G start\_POSTSUBSCRIPT italic\_K end\_POSTSUBSCRIPT × under¯ start\_ARG bold\_W start\_POSTSUBSCRIPT italic\_K end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT end\_ARG \| bold\_G start\_POSTSUBSCRIPT italic\_V end\_POSTSUBSCRIPT × under¯ start\_ARG bold\_W start\_POSTSUBSCRIPT italic\_V end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT end\_ARG end\_CELL end\_ROW | | (5) |https://arxiv.org/html/2502.00340v1/x5.pngFigure 5: By filtering the activations in the backward of attention block, we maintain the efficiency advantages of backward token filtering. Other activations ( _e.g_., for backward on 𝐐𝐐\\mathbf{Q}bold\_Q and 𝐊𝐊\\mathbf{K}bold\_K) are also filtered simultaneously.

[Figure5](https://arxiv.org/html/2502.00340v1#S3.F5 "In 3.1 Activations or Loss? ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") illustrates filtering the s⁢o⁢f⁢t⁢m⁢a⁢x𝑠𝑜𝑓𝑡𝑚𝑎𝑥softmaxitalic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x activation when computing the gradients of 𝐕𝐕\\mathbf{V}bold\_V with the corresponding rows of s⁢o⁢f⁢t⁢m⁢a⁢xT𝑠𝑜𝑓𝑡𝑚𝑎superscript𝑥𝑇softmax^{T}italic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT set to zero. By filtering the activations, the gradients of 𝐕,𝐐,𝐊𝐕𝐐𝐊\\mathbf{V,Q,K}bold\_V , bold\_Q , bold\_K and the gradients back-propagated to the front layers will still be sparse, which retains the sparsity and the opportunity to accelerate the end-to-end training efficiency. For implementations that do not explicitly store s⁢o⁢f⁢t⁢m⁢a⁢x𝑠𝑜𝑓𝑡𝑚𝑎𝑥softmaxitalic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x activation ( _e.g_., FlashAttention Dao et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib7 ""))), we can alternatively filter the 𝐐𝐐\\mathbf{Q}bold\_Q and 𝐊𝐊\\mathbf{K}bold\_K which are used to compute the s⁢o⁢f⁢t⁢m⁢a⁢x𝑠𝑜𝑓𝑡𝑚𝑎𝑥softmaxitalic\_s italic\_o italic\_f italic\_t italic\_m italic\_a italic\_x.

Analyzing the correlation between filtering loss and activations.
In causal language modeling, the hidden states of each token are constructed based on all preceding tokens. Although the loss associated with unimportant tokens is filtered, the loss of the remaining tokens still incorporates information from all prior tokens, including those that have been filtered. Consequently, gradients are propagated from the remaining tokens to the hidden states of the filtered tokens. We propose to filter the activations primarily by modifying the softmax function, which thus implicitly cuts off the connections from the remaining tokens to the filtered tokens. This approach effectively eliminates the gradients of the filtered tokens during the backward computation, thereby retaining sparsity.

### 3.2 Dimension-reduced Dense GEMM

Filtering the activations in the backward computation retains sufficient sparsity to improve training performance. However, existing sparse GEMM implementations cannot effectively support token filtering. Our experiments show that existing sparse GEMM is effective only when the data is highly sparse ( _e.g_., filtering 95% tokens) (§ [2.2](https://arxiv.org/html/2502.00340v1#S2.SS2 "2.2 Existing Token Filtering Fails to Improve Efficiency ‣ 2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")). However, the typical token filtering ratio is 30% ∼similar-to\\sim∼ 40% under which existing sparse GEMM implementations even have worse performance than dense GEMM.

To address this problem, we propose transforming sparse GEMM into dimension-reduced dense GEMM by leveraging the characteristics of sparsity in token filtering scenarios (§ [3.2.1](https://arxiv.org/html/2502.00340v1#S3.SS2.SSS1 "3.2.1 Transforming Sparse GEMM to Dimension-reduced Dense GEMM ‣ 3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")). However, performing dimension reduction is challenging due to the dynamics of the computation graph, making static updating rules impractical (§ [3.2.2](https://arxiv.org/html/2502.00340v1#S3.SS2.SSS2 "3.2.2 Dynamic Graph Complicates the Transformation ‣ 3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")). To this end, we introduce an automatic workflow that utilizes runtime stability to determine the graph nodes and employs special markers to finalize the node updating logic (§ [3.2.3](https://arxiv.org/html/2502.00340v1#S3.SS2.SSS3 "3.2.3 Automatic Graph Updating Workflow ‣ 3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")).

#### 3.2.1 Transforming Sparse GEMM to Dimension-reduced Dense GEMM

To understand and optimize the computation after filtering, we first carefully analyze the characteristics of sparsed computation in the backward process. [Figure6](https://arxiv.org/html/2502.00340v1#S3.F6 "In 3.2.1 Transforming Sparse GEMM to Dimension-reduced Dense GEMM ‣ 3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") shows the generalized backward process in the computation graph of existing machine learning libraries ( _e.g_., PyTorch), where 𝐆∈ℝb⁢s⁢z∗s⁢e⁢q×d1𝐆superscriptℝ𝑏𝑠𝑧𝑠𝑒𝑞subscript𝑑1\\mathbf{G}\\in\\mathbb{R}^{bsz\*seq\\times d\_{1}}bold\_G ∈ blackboard\_R start\_POSTSUPERSCRIPT italic\_b italic\_s italic\_z ∗ italic\_s italic\_e italic\_q × italic\_d start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT is the gradients matrix, b⁢s⁢z𝑏𝑠𝑧bszitalic\_b italic\_s italic\_z is the batch size, s⁢e⁢q𝑠𝑒𝑞seqitalic\_s italic\_e italic\_q is the sequence length, d1subscript𝑑1d\_{1}italic\_d start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT is the hidden size, 𝐖∈ℝd1×d2𝐖superscriptℝsubscript𝑑1subscript𝑑2\\mathbf{W}\\in\\mathbb{R}^{d\_{1}\\times d\_{2}}bold\_W ∈ blackboard\_R start\_POSTSUPERSCRIPT italic\_d start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT × italic\_d start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT is the parameter matrix, and 𝐗∈ℝb⁢s⁢z∗s⁢e⁢q×d2𝐗superscriptℝ𝑏𝑠𝑧𝑠𝑒𝑞subscript𝑑2\\mathbf{X}\\in\\mathbb{R}^{bsz\*seq\\times d\_{2}}bold\_X ∈ blackboard\_R start\_POSTSUPERSCRIPT italic\_b italic\_s italic\_z ∗ italic\_s italic\_e italic\_q × italic\_d start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT is the input matrix. The gradients of the filtered tokens are set to zero ( _i.e_., 𝐆𝐆\\mathbf{G}bold\_G is row-wise sparse).https://arxiv.org/html/2502.00340v1/x6.pngFigure 6: The generalized backward computation in existing machine learning libraries ( _e.g_., PyTorch). Each node in the computation graph necessarily has the input gradients and output for the next nodes. The model weights and saved variables could be optional and vary in different nodes ( _e.g_., transpose and slicing have no model weights).

We can categorize the sparse GEMM into two types: 1) Gradients for previous nodes: 𝐆s⁢p⁢a⁢r⁢s⁢e⋅𝐖⋅subscript𝐆𝑠𝑝𝑎𝑟𝑠𝑒𝐖\\mathbf{G}\_{sparse}\\cdot\\mathbf{W}bold\_G start\_POSTSUBSCRIPT italic\_s italic\_p italic\_a italic\_r italic\_s italic\_e end\_POSTSUBSCRIPT ⋅ bold\_W, 𝐆s⁢p⁢a⁢r⁢s⁢e⊙𝐠direct-productsubscript𝐆𝑠𝑝𝑎𝑟𝑠𝑒𝐠\\mathbf{G}\_{sparse}\\odot\\mathbf{g}bold\_G start\_POSTSUBSCRIPT italic\_s italic\_p italic\_a italic\_r italic\_s italic\_e end\_POSTSUBSCRIPT ⊙ bold\_g, which are sparse and passed to the next nodes. 𝐠𝐠\\mathbf{g}bold\_g is a scaler or vector that performs element-wise computation on the gradients; 2) And the gradients of model parameters: 𝐆s⁢p⁢a⁢s⁢eT⋅𝐗⋅subscriptsuperscript𝐆𝑇𝑠𝑝𝑎𝑠𝑒𝐗\\mathbf{G}^{T}\_{spase}\\cdot\\mathbf{X}bold\_G start\_POSTSUPERSCRIPT italic\_T end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_s italic\_p italic\_a italic\_s italic\_e end\_POSTSUBSCRIPT ⋅ bold\_X, which will be dense and updated to the model weights. Based on these analyses, we have the following observations:

- ∙∙\\bullet∙

The gradients passed to the next nodes inherit the sparsity of the input gradients and the sparsity follows the same pattern as the input gradients ( _i.e_., the gradients of filtered tokens are zeros). Thus if we shrink the sequence dimension at the initial gradients ( _i.e_., removing the zeros), all the afterward gradients will be automatically reduced.

- ∙∙\\bullet∙

The sequence dimension vanishes in the gradients of model parameters, which is reasonable since the parameters are independent of the sequence length, and we can directly shrink the sequence dimension to reduce the computational cost.

Instead of directly optimizing the sparse matrix computations, we leverage the above observations and propose to globally reduce the sequence dimension of the gradients and the saved variable in the backward computation graph to accelerate the computation. [Figure7](https://arxiv.org/html/2502.00340v1#S3.F7 "In 3.2.1 Transforming Sparse GEMM to Dimension-reduced Dense GEMM ‣ 3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") illustrates the computation before and after reducing the sequence dimension. By shrinking the sequence dimension, we can transform the sparse GEMM to dimension-reduced dense computations with optimized performance. Compared with directly optimizing the sparse GEMM, transforming to dense GEMM is more effective since the dense GEMM has been well optimized on existing hardware.https://arxiv.org/html/2502.00340v1/x7.pngFigure 7: Computations before and after reducing the sequence dimension. Instead of directly optimizing the sparse matrix computations, we leverage the characteristics of token filtering and globally reduce the sequence dimension.

#### 3.2.2 Dynamic Graph Complicates the Transformation

Based on observations from backward computations, sparse matrix operations can be reformulated into dimension-reduced dense computations. To implement this proposed approach, it is crucial to first understand the functionality of existing automatic differentiation (autograd) libraries. For example, PyTorch, one of the most widely used frameworks, employs a dynamic computational graph that is constructed incrementally as operations are executed.
Other machine learning libraries ( _e.g_., TensorFlow Abadi et al. ( [2016](https://arxiv.org/html/2502.00340v1#bib.bib1 ""))) and systems ( _e.g_., MegatronLM Narayanan et al. ( [2021](https://arxiv.org/html/2502.00340v1#bib.bib26 "")) and DeepSpeed Rasley et al. ( [2020](https://arxiv.org/html/2502.00340v1#bib.bib29 ""))) also use a similar graph-based approach or are mostly built on PyTorch.
The backward graph is built during forward propagation and is utilized only once to compute gradients ( _i.e_., discarded after the backward pass in each iteration).

Backward token filtering occurs after the forward computation, at which point the computation graph has already been constructed. Therefore, we need to update the computation graph node by node ( _e.g_., updating the sizes and variables) prior to performing the backward computation. However, modifying the computational graph poses significant challenges due to the following reasons:

- ∙∙\\bullet∙

Dynamic graph structure. The computational graph is dynamically built. Different implementations of the same algorithm can have significantly different backward computation graph. Even the input and output can impact the graph, _e.g_., FlashAttention Dao et al. ( [2022](https://arxiv.org/html/2502.00340v1#bib.bib7 "")) only accept model weights in 16-bits and naive attention implementation is the only choice if we need to explicitly output the attention values. The dynamic graph structure makes it impractical to design static updating rules based on the model ( _e.g_., designing static rules for updating self-attention and FFN layers).

- ∙∙\\bullet∙

Dynamic usage of the graph nodes. The same type of node can have different inputs and outputs in different models or even in the same model. For example, the same multiplication node has different outputs when multiplying with scalar, vector, or matrix. The dynamic usage of the graph nodes makes it impractical to use static updating rules based on the node types.

- ∙∙\\bullet∙

Numerous types of nodes. Different models typically have different computations and thus use different type of nodes. Different nodes require different updating logic. PyTorch, for instance, has over 300 node types, significantly increasing the complexity of system implementation.

In summary, effectively accelerating the token filtering requires us to transform the sparse GEMM to dimension-reduced dense GEMM that requires updating the computation graph, which is challenging due to the dynamic of graph structure, the dynamic usage of nodes, and the numerous types of nodes.

#### 3.2.3 Automatic Graph Updating Workflow

To address this issue, we propose an automatic workflow to amend the computational graph. The key insight is that, even though the graph is highly dynamic, it still can be deterministic when using the same implementation and inputs. Particularly, the model implementation and inputs remain the same during the whole training ( _i.e_., runtime stability). Thus, we can mimic the input and traverse the graph using the same implementation to dynamically determine the node information.
The automatic workflow contains two steps: 1) generating the skeleton code for processing each type of nodes and their attributes; 2) leveraging special markers to generate detailed node processing rules.

Specifically, we first perform a coarse-grained graph traversing using synthetic data ( _i.e_., mimicing the actual inputs) to collect all the node types and find the target attributes ( _e.g_., sizes and variables) that need to be updated. [Table1](https://arxiv.org/html/2502.00340v1#S3.T1 "In 3.2.3 Automatic Graph Updating Workflow ‣ 3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") shows examples of the node attributes that need to be amended. We select the list of target attributes and corresponding data types based on Torchgen, which could be easily updated if more attributes needs to be processed.
We generate skeleton codes for processing attributes of all the nodes and the implementation detail is presented in § [5.1](https://arxiv.org/html/2502.00340v1#S5.SS1 "5.1 Offline Generating Model-customized Operator ‣ 5 Implementation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider").

| | |
| --- | --- |
| Node Attributes | | | |
| --- | --- |
| Data Type | | | |
| --- | --- |
| Operations | |
| --- | --- | --- |
| InputMetadata | | |
| --- | --- |
| Int Array | | | |
| --- | --- |
| Update size | |
| SavedVariables | | |
| --- | --- |
| Tensor | | | |
| --- | --- |
| Reduce Dimensions | |
| Matrix Sizes | | |
| --- | --- |
| Int Array | | | |
| --- | --- |
| Update size | |
| Matrix # of elements | | |
| --- | --- |
| Int | | | |
| --- | --- |
| Update value | |

Table 1: Examples of the nodes’ attributes that need to be updated during amending the graph.

After obtaining the skeleton code for updating the node attributes, we still need to determine the updating logic. Specifically, we need to determine which dimensions should be reduced and the sizes after the reduction. We only focus on the sequence dimension since we need to filter out unimportant tokens. However, the index of the sequence dimension varies among different nodes and may also be mixed with the batch size. Moreover, the same type of node can have different dimensions at different positions in the same graph, making it impractical to use static updating logic. To address this issue, we design a simple-but-effective method by marking the batch size and sequence length with special numbers to precisely find the shrinking dimensions of various nodes in the computational graph. [Figure8](https://arxiv.org/html/2502.00340v1#S3.F8 "In 3.2.3 Automatic Graph Updating Workflow ‣ 3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") shows an example of marking the batch size and sequence length with prime numbers.
In the skeleton code, we use a greedy algorithm to find the batch size and sequence dimension. Directly using the greedy algorithm can produce wrong results as the batch size or sequence length may be identified with other dimensions ( _e.g_., the sequence length and hidden dimension could be both 2048). The special markers avoid the ambiguity of the dimension and enable the greedy algorithm to precisely find the shrinking dimensions and determine the size after the reduction. The system will cache the output of greedy algorithm for online training (§ [5.1](https://arxiv.org/html/2502.00340v1#S5.SS1 "5.1 Offline Generating Model-customized Operator ‣ 5 Implementation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")).https://arxiv.org/html/2502.00340v1/x8.pngFigure 8: An example of marking batch size and sequence length with prime numbers. Leveraging the special marks is a simple-but-effective way to precisely find the shrinking dimensions of various nodes in the computational graph.

## 4 Discussion

Apart from the existing designs in Collider, we would also like to discuss the following aspects of potential improvements brought by Collider ( _e.g_., communication efficiency) and future directions of enhancing the performance of token fitlering systems.

### 4.1 Filtering Activations Necessitates Different Training Parameters

To retain sparsity and achieve efficiency improvements, Collider further filters the activations of inconsequential tokens across all layers during the backward computation. From the perspective of the chain rule in gradient propagation, the gradients of the remaining tokens ( _i.e_., tokens that are not filtered out) are backpropagated to the front layers through all previous tokens ( _i.e_., based on causal language modeling), including the filtered tokens.
Filtering the activations of inconsequential tokens implicitly eliminates the gradients transferred from the remaining tokens to filtered ones, resulting in a reduced amount of gradients backpropagated to the front layers. Given the same inputs, Collider passes a smaller amount of gradients to update the models compared to methods that only filter the loss ( _i.e_., Rho Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 ""))). Therefore, Collider ( _i.e_., after filtering the activations) necessitates different training parameters from existing work Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) to achieve optimal performance. For example, Collider is more likely to require a larger batch size to increase stability, and layer-wise learning rate adjustments Singh et al. ( [2015](https://arxiv.org/html/2502.00340v1#bib.bib30 "")); Zheng et al. ( [2020](https://arxiv.org/html/2502.00340v1#bib.bib39 "")) could also be beneficial in inproving model utility in Collider.

### 4.2 Collider Reduces Communication Overheads in Distributed Training

Collider optimizes computational efficiency in backward token filtering by transforming sparse GEMM into dense GEMM, which significantly reduces communication overheads in distributed LLM training. Specifically, Collider updates the entire computation graph, where the gradients and activations are reduced along the sequence dimension. Existing parallelism strategies that enable LLM training on distributed systems typically transfer gradients between different nodes or GPUs during backward computation. Therefore, reducing the sequence dimension of gradients can linearly decrease communication overheads in distributed training. We discuss the advantages of Collider across different parallelism strategies as follows.

- ∙∙\\bullet∙

Tensor Parallel (TP) Narayanan et al. ( [2021](https://arxiv.org/html/2502.00340v1#bib.bib26 "")). In TP, the transformer models are typically partitioned along the multiple heads and hidden dimensions. All-reduce of gradients on inputs are required twice ( _i.e_., inputs of FFN and attention block) in each layer’s backward computation. Collider can linearly reduce the amount of data transferred in each all-reduce operation.

- ∙∙\\bullet∙

Sequence Parallel (SP) Korthikanti et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib15 "")). SP is designed to be combined with TP to further reduce the memory usage caused by the redundant activations of dropout and layer normalization. In SP, the sequence dimension is partitioned on multiple devices through all-gather during computing dropout and layer normalization and recovered to partition on hidden dimensions through reduce-scatter. Collider can reduce the communication overhead in the corresponding all-gather and reduce-scatter operations.

- ∙∙\\bullet∙

Pipeline Parallel (PP) Narayanan et al. ( [2021](https://arxiv.org/html/2502.00340v1#bib.bib26 "")). The advantages of using Collider in PP is straightforward as PP sequentially transfers the gradients in the graph which are linearly reduced by Collider.

- ∙∙\\bullet∙

Mixture-of-Experts (MoE). The integration of Collider in MoE helps in optimizing communication between experts during the backward passes, thereby minimizing the data transferred across devices and enhancing throughput. Specifically, Collider ensures that only gradients of important tokens are routed to the corresponding experts.

Apart from reducing communication costs in various parallelism strategies, Collider is also beneficial for activation offloading methods, such as ZeRO-R Rasley et al. ( [2020](https://arxiv.org/html/2502.00340v1#bib.bib29 "")), by minimizing input/output (I/O) costs.

### 4.3 Reducing Overhead of Reference Model

Existing studies Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) select filtered tokens based on a reference model, which may introduce additional computational overhead. The reference model uses the same architecture as the target training model and is fine-tuned on a manually curated, high-quality dataset Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")). Intuitively, the reference model helps filter out tokens that do not conform to the distribution of the high-quality dataset, which implicitly represents the domain on which we expect the target model to be trained. Although the approach to use a reference model has been proven effective, it has two significant drawbacks: 1) Training the reference model incurs additional costs, and it is computationally inefficient to update the knowledge within the reference model ( _e.g_., updating the manually curated high-quality dataset requires retraining the model); 2) While inference results from the reference model can be prepared offline to reduce overhead during training, the inference process still consumes significant resources since the model has the same architecture as the target model ( _i.e_., the same number of parameters).

Thus, it is necessary to reduce the overhead of the reference model to improve the practicality of token filtering systems. The key insight is that the reference model is used for filtering tokens and should therefore be loss-tolerant in the system ( _e.g_., some deviation in output loss may yield the same filtering results). Here, we discuss two potential directions to reduce the overhead of the reference model.

Model compression. We can employ model compression techniques to reduce the inference overhead of the reference model. For example, we can distill knowledge into a smaller model or directly prune the model to decrease the number of parameters. Other techniques, such as quantizing the reference model to low-bit precision, can also be utilized to further reduce inference overhead.

Combining with n-gram models. We can also combine the reference model with n-gram models to reduce overhead. The n-gram approach is an early and quintessential method in statistical linguistics, based on the central assumption that the current word is influenced solely by the previous n−1𝑛1n-1italic\_n - 1 words. For a given sentence w1,w2,…,wmsubscript𝑤1subscript𝑤2…subscript𝑤𝑚w\_{1},w\_{2},...,w\_{m}italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , … , italic\_w start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT, the n-gram model calculates its probability by:

| | | | |
| --- | --- | --- | --- |
| | P⁢(w1,w2,…,wm)≈∏i=1mP⁢(wi∣wi−1,…,wi−n+1).𝑃subscript𝑤1subscript𝑤2…subscript𝑤𝑚superscriptsubscriptproduct𝑖1𝑚𝑃conditionalsubscript𝑤𝑖subscript𝑤𝑖1…subscript𝑤𝑖𝑛1\\vspace{-1mm}P(w\_{1},w\_{2},\\dots,w\_{m})\\approx\\prod\_{i=1}^{m}P(w\_{i}\\mid w\_{i-%<br>1},\\dots,w\_{i-n+1}).\\vspace{-1mm}italic\_P ( italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , … , italic\_w start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT ) ≈ ∏ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_m end\_POSTSUPERSCRIPT italic\_P ( italic\_w start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ∣ italic\_w start\_POSTSUBSCRIPT italic\_i - 1 end\_POSTSUBSCRIPT , … , italic\_w start\_POSTSUBSCRIPT italic\_i - italic\_n + 1 end\_POSTSUBSCRIPT ) . | | (6) |

It is worth noting that the mathematical principle of n-gram models is similar to the concept of causal language modeling in LLMs, allowing n-gram models to serve as a substitute. In particular, n-gram models generally require much less time for training and inference, which is negligible compared to transformer-based models. Thus, we can quickly update the knowledge in the n-gram model.
We have also conducted prior experiments to validate the performance of n-gram models. We measured the Pearson correlation between the loss of n-gram and transformer-based models trained on the same dataset, with the results presented in [Figure9(a)](https://arxiv.org/html/2502.00340v1#S4.F9.sf1 "In Figure 9 ‣ 4.3 Reducing Overhead of Reference Model ‣ 4 Discussion ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"). Additionally, we assessed the common ratio of filtered tokens between n-gram and transformer-based models, with the results shown in [Figure9(b)](https://arxiv.org/html/2502.00340v1#S4.F9.sf2 "In Figure 9 ‣ 4.3 Reducing Overhead of Reference Model ‣ 4 Discussion ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"). The findings indicate that the n-gram model exhibits high similarity to the transformer-based model in terms of token filtering, which supports the viability of using n-gram models to reduce the overhead of the reference model.https://arxiv.org/html/2502.00340v1/x9.png(a)Distribution of pearson correlation between the loss of n-gram and transformer-based models.https://arxiv.org/html/2502.00340v1/x10.png(b)Distribution of common ratio of filtered tokens between n-gram and transformer-based models.

Figure 9: The n-gram model shows high similarity with the transformer-based model in terms of token filtering.

In our system, we assume that the reference model is already trained and that the inference results are prepared offline. We leave the exploration of reducing the overhead of the reference model for future work.

## 5 Implementationhttps://arxiv.org/html/2502.00340v1/x11.pngFigure 10: Implementation and usage of Collider.

We implement Collider in PyTorch, one of the most widely used frameworks, and use its C++ extension666C++ extensions in PyTorch allow users to create custom operators outside the PyTorch backend, providing flexibility and reducing boilerplate code. Once defined, these extensions can be organized into native PyTorch functions for upstream contributions. to create the backward filtering operator. Collider improves the efficiency of token filtering through two designs: filtering the activations and transforming sparse GEMM to dense GEMM. We implement these two designs in a single operator by directly reducing the sequence dimension, as the filtered activations ( _i.e_., those set to zero) will be subsequently removed in the transformation from sparse GEMM to dense GEMM. Thus, we can directly remove the activations instead of setting them to zero in advance.
To address the challenges posed by the dynamic computation graph and to support various LLM architectures, we implement Collider in two phases: the offline and online stages, as illustrated in [Figure10](https://arxiv.org/html/2502.00340v1#S5.F10 "In 5 Implementation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"). In the offline stage, Collider employs an automatic workflow to generate a model-customized operator for updating the graph. In the online training (§ [5.1](https://arxiv.org/html/2502.00340v1#S5.SS1 "5.1 Offline Generating Model-customized Operator ‣ 5 Implementation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")), the operator filters the activations and transforms the sparse GEMM into dimension-reduced dense GEMM to accelerate the training process (§ [5.2](https://arxiv.org/html/2502.00340v1#S5.SS2 "5.2 Online Training using Collider ‣ 5 Implementation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")).
Collider can also be implemented in other frameworks, such as TensorFlow Abadi et al. ( [2016](https://arxiv.org/html/2502.00340v1#bib.bib1 "")), by following similar procedures to update the computation graph during backpropagation.

### 5.1 Offline Generating Model-customized Operator

Given the model, we run forward and backward computations using synthetic data ( _i.e_., simulating the training samples) to obtain all the node types. Due to runtime stability ( _i.e_., the graph remains stable during training), the node information from synthetic data is identical to that during training. We then parse the node attributes from Torchgen and generate the operator’s skeleton code for processing each node. LABEL:code:offline shows examples of the generated skeleton code for processing GEMM and FlashAttention nodes.
The generated code is a skeleton and cannot be used directly because the operator employs a greedy algorithm to determine the batch size and sequence dimension based on the inputs. However, the actual batch size and sequence length might be the same as other dimensions ( _e.g_., hidden states of 2048), which can mislead the operator into reducing the wrong dimensions.

[⬇](data:text/plain;base64,LyogJCQgc3RhcnQgb2YgY29kZSBnZW5lcmF0aW9uICQkICovCmlmKGZuLT5uYW1lKCkgPT0gIk1tQmFja3dhcmQwIikgewogIE1tQmFja3dhcmQwKiBvcF9mbiA9IGR5bmFtaWNfY2FzdDxNbUJhY2t3YXJkMCo+KGZuKTsKICBhdXRvIHVucGFja2VkX3NlbGYgPSBvcF9mbi0+c2VsZl8udW5wYWNrKCk7CiAgaWYodW5wYWNrZWRfc2VsZi5kZWZpbmVkKCkpCiAgb3BfZm4tPnNlbGZfID0gZ3JhcGhfZmlsdGVyLT5wcm9jZXNzX3ZhcmlhYmxlKHVucGFja2VkX3NlbGYsIGZhbHNlKTsKICBhdXRvIHVucGFja2VkX21hdDIgPSBvcF9mbi0+bWF0Ml8udW5wYWNrKCk7CiAgaWYodW5wYWNrZWRfbWF0Mi5kZWZpbmVkKCkpCiAgb3BfZm4tPm1hdDJfID0gZ3JhcGhfZmlsdGVyLT5wcm9jZXNzX3ZhcmlhYmxlKHVucGFja2VkX21hdDIsIGZhbHNlKTsKICBncmFwaF9maWx0ZXItPnByb2Nlc3Nfc2l6ZXMob3BfZm4tPm1hdDJfc3ltX3NpemVzKTsKICBncmFwaF9maWx0ZXItPnByb2Nlc3Nfc2l6ZXMob3BfZm4tPnNlbGZfc3ltX3NpemVzKTsKfQppZihmbi0+bmFtZSgpID09ICJTY2FsZWREb3RQcm9kdWN0Rmxhc2hBdHRlbnRpb25CYWNrd2FyZDAiKSB7CiAgU2NhbGVkRG90UHJvZHVjdEZsYXNoQXR0ZW50aW9uQmFja3dhcmQwKiBvcF9mbiA9CiAgICBkeW5hbWljX2Nhc3Q8U2NhbGVkRG90UHJvZHVjdEZsYXNoQXR0ZW50aW9uQmFja3dhcmQwKj4oZm4pOwogIGF1dG8gdW5wYWNrZWRfcXVlcnkgPSBvcF9mbi0+cXVlcnlfLnVucGFjaygpOwogIGlmKHVucGFja2VkX3F1ZXJ5LmRlZmluZWQoKSkKICBvcF9mbi0+cXVlcnlfID0gZ3JhcGhfZmlsdGVyLT5wcm9jZXNzX3ZhcmlhYmxlKHVucGFja2VkX3F1ZXJ5LCBmYWxzZSk7CiAgYXV0byB1bnBhY2tlZF9rZXkgPSBvcF9mbi0+a2V5Xy51bnBhY2soKTsKICBpZih1bnBhY2tlZF9rZXkuZGVmaW5lZCgpKQogIG9wX2ZuLT5rZXlfID0gZ3JhcGhfZmlsdGVyLT5wcm9jZXNzX3ZhcmlhYmxlKHVucGFja2VkX2tleSwgZmFsc2UpOwogIGF1dG8gdW5wYWNrZWRfdmFsdWUgPSBvcF9mbi0+dmFsdWVfLnVucGFjaygpOwogIGlmKHVucGFja2VkX3ZhbHVlLmRlZmluZWQoKSkKICBvcF9mbi0+dmFsdWVfID0gZ3JhcGhfZmlsdGVyLT5wcm9jZXNzX3ZhcmlhYmxlKHVucGFja2VkX3ZhbHVlLCBmYWxzZSk7CiAgYXV0byB1bnBhY2tlZF9vdXRwdXQgPSBvcF9mbi0+b3V0cHV0Xy51bnBhY2sob3BfZm4tPmdldHB0cigpKTsKICBpZih1bnBhY2tlZF9vdXRwdXQuZGVmaW5lZCgpKQogIG9wX2ZuLT5vdXRwdXRfID0gZ3JhcGhfZmlsdGVyLT5wcm9jZXNzX3ZhcmlhYmxlKHVucGFja2VkX291dHB1dCwgdHJ1ZSk7CiAgLy8gLi4uIG1vcmUgYXR0cmlidXRlcyBvbWl0dGVkCiAgZ3JhcGhfZmlsdGVyLT5wcm9jZXNzX3NpemVzKG9wX2ZuLT5tYXhfcSk7CiAgZ3JhcGhfZmlsdGVyLT5wcm9jZXNzX3NpemVzKG9wX2ZuLT5tYXhfayk7Cn0KLy8gLi4uIG1vcmUgbm9kZXMKLyogJCQgZW5kIG9mIGNvZGUgZ2VuZXJhdGlvbiAkJCAqLw==)

/\*$$startofcodegeneration$$\*/

if(fn->name()=="MmBackward0"){

MmBackward0\*op\_fn=dynamic\_cast<MmBackward0\*>(fn);

autounpacked\_self=op\_fn->self\_.unpack();

if(unpacked\_self.defined())

op\_fn->self\_=graph\_filter->process\_variable(unpacked\_self,false);

autounpacked\_mat2=op\_fn->mat2\_.unpack();

if(unpacked\_mat2.defined())

op\_fn->mat2\_=graph\_filter->process\_variable(unpacked\_mat2,false);

graph\_filter->process\_sizes(op\_fn->mat2\_sym\_sizes);

graph\_filter->process\_sizes(op\_fn->self\_sym\_sizes);

}

if(fn->name()=="ScaledDotProductFlashAttentionBackward0"){

ScaledDotProductFlashAttentionBackward0\*op\_fn=

dynamic\_cast<ScaledDotProductFlashAttentionBackward0\*>(fn);

autounpacked\_query=op\_fn->query\_.unpack();

if(unpacked\_query.defined())

op\_fn->query\_=graph\_filter->process\_variable(unpacked\_query,false);

autounpacked\_key=op\_fn->key\_.unpack();

if(unpacked\_key.defined())

op\_fn->key\_=graph\_filter->process\_variable(unpacked\_key,false);

autounpacked\_value=op\_fn->value\_.unpack();

if(unpacked\_value.defined())

op\_fn->value\_=graph\_filter->process\_variable(unpacked\_value,false);

autounpacked\_output=op\_fn->output\_.unpack(op\_fn->getptr());

if(unpacked\_output.defined())

op\_fn->output\_=graph\_filter->process\_variable(unpacked\_output,true);

//...moreattributesomitted

graph\_filter->process\_sizes(op\_fn->max\_q);

graph\_filter->process\_sizes(op\_fn->max\_k);

}

//...morenodes

/\*$$endofcodegeneration$$\*/

Code 1: Generated skeleton code for processing GEMM and FlashAttention nodes. The automatic code generation enables Collider to support various nodes with low implementation costs ( _e.g_., PyTorch has more than 300 types of nodes).

To solve this issue, as demonstrated in § [3.2.3](https://arxiv.org/html/2502.00340v1#S3.SS2.SSS3 "3.2.3 Automatic Graph Updating Workflow ‣ 3.2 Dimension-reduced Dense GEMM ‣ 3 Collider ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"), we compile the generated skeleton code and run the operator using inputs with special markers for both batch size and sequence length. These special markers ( _i.e_., unique from other dimensions) enable the greedy algorithm to precisely identify the correct dimensions for reduction. The operator will save the output of the greedy algorithm and load it during online training, which is guaranteed to be correct due to runtime stability.

After executing the above workflow, we obtain a model-customized operator that contains all the node information and corresponding dimension updating logic for a specific model. We have prepared scripts that allow users to easily execute the workflow and generate operators for their own models. The reset system implementation includes updating the node attributes, _e.g_., changing the InputMetadata to pass verification and update the saved variables, which is quite straightforward as long as the attributes and reducing dimensions are correctly identified.

### 5.2 Online Training using Collider

[⬇](data:text/plain;base64,CWltcG9ydCAoKkBcc29sdXRpb25AKikKCS4uLgoJZm9yIHN0ZXAsIGJhdGNoIGluIGVudW1lcmF0ZSh0b2tlbml6ZWRfZGF0YXNldCk6CgkJbG9naXRzID0gc2VsZi5tb2RlbChiYXRjaFsiaW5wdXRfaWRzIl0pLmxvZ2l0cwooKkBcdGV4dGJme1x0ZXh0Y29sb3J7cmVkfXstfX1AKikgICAoKkBcdGV4dGJme1x0ZXh0Y29sb3J7cmVkfXtsb3NzID0gY2F1c2FsXF9sb3NzKGJhdGNoWyJpbnB1dFxfaWRzIl0sIGxvZ2l0cyl9fUAqKQooKkBcdGV4dGJme1x0ZXh0Y29sb3J7ZGtncmVlbn17K319QCopICAgKCpAXHRleHRiZntcdGV4dGNvbG9ye2RrZ3JlZW59e2xvc3MsIGZpbHRlclxfbWFzayA9IHRva2VuXF9maWx0ZXJcX2xvc3MofX1AKikKKCpAXHRleHRiZntcdGV4dGNvbG9ye2RrZ3JlZW59eyt9fUAqKSAgICgqQFx0ZXh0YmZ7XHRleHRjb2xvcntka2dyZWVufXtcIFwgXCBcIGJhdGNoWyJpbnB1dFxfaWRzIl0sIGxvZ2l0cyx9fUAqKQooKkBcdGV4dGJme1x0ZXh0Y29sb3J7ZGtncmVlbn17K319QCopICAgKCpAXHRleHRiZntcdGV4dGNvbG9ye2RrZ3JlZW59e1wgXCBcIFwgcmVmXF9sb3NzPWJhdGNoWyJyZWZcX2xvc3MiXSwgZHJvcFxfcmF0ZT0wLjQsfX1AKikKKCpAXHRleHRiZntcdGV4dGNvbG9ye2RrZ3JlZW59eyt9fUAqKSAgICgqQFx0ZXh0YmZ7XHRleHRjb2xvcntka2dyZWVufXspfX1AKikKKCpAXHRleHRiZntcdGV4dGNvbG9ye2RrZ3JlZW59eyt9fUAqKSAgICgqQFx0ZXh0YmZ7XHRleHRjb2xvcntka2dyZWVufXtcc29sdXRpb24ub3BzLmJhY2t3YXJkXF9maWx0ZXIobG9zcywgZmlsdGVyXF9tYXNrKX19QCopCgkJbG9zcy5iYWNrd2FyZCgpCgkJb3B0aW1pemVyLnN0ZXAoKQoJCW9wdGltaXplci56ZXJvX2dyYWQoKQoJLi4u)

importCollider

...

forstep,batchinenumerate(tokenized\_dataset):

logits=self.model(batch\["input\_ids"\]).logits

-loss = causal\_loss(batch\["input\_ids"\], logits)

+loss, filter\_mask = token\_filter\_loss(

+    batch\["input\_ids"\], logits,

+    ref\_loss=batch\["ref\_loss"\], drop\_rate=0.4,

+)

+Collider.ops.backward\_filter(loss, filter\_mask)

loss.backward()

optimizer.step()

optimizer.zero\_grad()

...

Code 2: Using Collider in the online training.

Using the operator only requires adding a few lines ( _i.e_., five lines) of code. LABEL:code:online shows an example of using Collider in online training. Starting from regular training, we first need to change the loss computation to a token-filtered loss, _i.e_., only considering the loss on selected tokens. Then, we call the Collider operator using the loss and filter mask to update the graph. The filter mask is a tensor consisting of zeros and ones to indicate which tokens are filtered. For systems that already utilize token filtering, only one line of code Collider.ops.backward\_filter(loss, filter\_mask) is needed to get the full efficiency of token filtering.

## 6 Evaluation

In this section, we comprehensively evaluate Collider with the following key results:

- ∙∙\\bullet∙

Utility evaluations of training TinyLlama Zhang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib38 "")) on open-web-math with 15B tokens Paster et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib27 "")) show that Collider not only improves the model utility by 16.3% (averaged relative improvements on nine tasks)
and also reduces the end-to-end training time from 4.5 days to 3.7 days compared with regular training. Compared with Rho filtering Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")), Collider shows significant efficiency improvements but slightly decreases in model utility, due to requiring different optimal parameter settings
.

- ∙∙\\bullet∙

Efficiency evaluations on three LLMs show that Collider can reduce the backward computation up to 35.1% and reduce end-to-end training cost by up to 22% when filtering 40% tokens. The speedup of Collider becomes more pronounced as the context length increases and the filtering ratio increases. The cost of the Collider operator does not increase with the filtering ratio is negligible compared with the time saved in the backward stage.

| | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Method | FinetuningDataset | Evaluation tasks | Time(days) |
| | |
| --- | --- |
| GSM8K | | | |
| --- | --- |
| MATH | | | |
| --- | --- |
| SVAMP | | ASDiv | MAWPS | TAB | MQA | MMLU | SAT | Average |
| TinyLlama | NA | 2.3 | 2.4 | 9.9 | 18.1 | 20.2 | 8.8 | 22.1 | 17.9 | 21.9 | 13.7 | NA |
| TinyLlama | | |
| --- | --- |
| OWM |
| (Full) | | 3.6 | 4.2 | 19.1 | 31.5 | 36.2 | 14.7 | 10.3 | 21.7 | 18.8 | 17.8 | ∼similar-to\\sim∼4.5 |
| RHO | | |
| --- | --- |
| OWM |
| (Filter 40%) | | 11.7 | 8 | 35.9 | 48.1 | 63.2 | 19 | 16 | 15.5 | 6.2 | 24.8 | ∼similar-to\\sim∼4.5 |
| | |
| --- | --- |
| Collider |
| (Ours) | | | |
| --- | --- |
| OWM |
| (Filter 40%) | | 6.7 | 5.8 | 28.0 | 37.4 | 46.7 | 14.9 | 10.2 | 14.5 | 21.9 | 20.7 | ∼similar-to\\sim∼3.7 |

Table 2: Utility evaluation on different tasks. Compared with regular training, Collider improves the model utility and significantly reduces the end-to-end training time. Compared with Rho filtering, Collider shows significant efficiency improvements but has some decrease of model utiltiy, which potentially could be solved by tuning the training parameters (§ [6.2](https://arxiv.org/html/2502.00340v1#S6.SS2 "6.2 Utility Evaluation ‣ 6 Evaluation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider")).

| | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Model | TrainingMethod | Detailed Time Consumption (seconds) |
| | |
| --- | --- |
| Forward | | | |
| --- | --- |
| Computing Loss | | | |
| --- | --- |
| Collider Operator | | | |
| --- | --- |
| Backward | | Total |
| TinyLlama(1.1B, 4K) | | |
| --- | --- |
| Regular Training | | 13.43 | 0.023 | NA | 29.36 | 42.82 |
| | |
| --- | --- |
| Rho Filtering | | 13.41 | 0.094 | NA | 29.21 | 42.73 |
| | |
| --- | --- |
| Collider (Ours) | | 13.44 | 0.099 | 0.87 | | |
| --- | --- |
| 18.96 (↓↓\\downarrow↓ 35.1%) | | | |
| --- | --- |
| 33.37(↓↓\\downarrow↓ 22.0%) | |
| Qwen2.5(1.5B, 3K) | | |
| --- | --- |
| Regular Training | | 12.93 | 0.039 | NA | 31.31 | 44.27 |
| | |
| --- | --- |
| Rho Filtering | | 12.90 | 0.321 | NA | 31.22 | 44.48 |
| | |
| --- | --- |
| Collider (Ours) | | 12.90 | 0.317 | 1.14 | | |
| --- | --- |
| 23.27 (↓↓\\downarrow↓ 25.7%) | | | |
| --- | --- |
| 37.65(↓↓\\downarrow↓ 15.0%) | |
| Phi1.5(1.4B, 3K) | | |
| --- | --- |
| Regular Training | | 12.68 | 0.027 | NA | 26.97 | 39.32 |
| | |
| --- | --- |
| Rho Filtering | | 12.77 | 0.126 | NA | 26.90 | 39.38 |
| | |
| --- | --- |
| Collider (Ours) | | 12.75 | 0.129 | 0.794 | | |
| --- | --- |
| 18.68 (↓↓\\downarrow↓ 30.5%) | | | |
| --- | --- |
| 32.03(↓↓\\downarrow↓ 18.7%) | |

Table 3: The detailed time consumption of one iteration ( _i.e_., 512 samples) in three models using 8 GPUs.

### 6.1 Experimental Setup

Testbed setup. We evaluate Collider on Ubuntu servers, each equipped with 8 NVIDIA RTX 3090 GPUs (24GB), 40 CPU cores, and 256GB of memory. We use PyTorch 2.5.0 and CUDA 12.6 for implementation. Following previous studies Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")), we utilize small but powerful LLMs in our experiments ( _e.g_., TinyLlama Zhang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib38 "")) with 1.1B parameters). To maximize training efficiency, we perform single-node multi-GPU training using ZeRO-1 in DeepSpeed Rasley et al. ( [2020](https://arxiv.org/html/2502.00340v1#bib.bib29 "")). We implement gradient accumulation to facilitate large batch training and use mixed precision with BF16 to reduce memory consumption and accelerate training.

Datasets, models, and tasks. Our experiments focus on fine-tuning pre-trained foundation models for downstream tasks. We utilize two small but powerful LLMs in the experiments: TinyLlama Zhang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib38 "")), Qwen2.5-1.5B Yang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib34 "")), and Phi1.5 Li et al. ( [2023b](https://arxiv.org/html/2502.00340v1#bib.bib17 "")). Following previous work Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")), we first train a reference model on small yet high-quality datasets, and then use the loss from the reference model to filter tokens during the training of the target model.
We focus on mathematical reasoning as the main task, employing a blend of synthetic and manually curated math-related tokens Yu et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib36 "")); Yue et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib37 "")); Mitra et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib25 "")); Amini et al. ( [2019a](https://arxiv.org/html/2502.00340v1#bib.bib2 "")); Wang et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib32 "")) as high-quality data to train the reference model. For large-scale datasets to train the target model, we use open-web-math (OWM) Paster et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib27 "")). We follow Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) and use the same architecture for both the reference and target models.
To evaluate the utility of the models, we use the following tasks: GSM8K Cobbe et al. ( [2021](https://arxiv.org/html/2502.00340v1#bib.bib6 "")), MATH Lightman et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib18 "")), SVAMP Patel et al. ( [2021](https://arxiv.org/html/2502.00340v1#bib.bib28 "")), ASDiv Miao et al. ( [2020](https://arxiv.org/html/2502.00340v1#bib.bib24 "")), MAWPS Koncel-Kedziorski et al. ( [2016](https://arxiv.org/html/2502.00340v1#bib.bib14 "")), TabMWP Lu et al. ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib21 "")), MathQA Amini et al. ( [2019b](https://arxiv.org/html/2502.00340v1#bib.bib3 "")), SATMath McAleer ( [2023](https://arxiv.org/html/2502.00340v1#bib.bib23 "")), and MMLU Hendrycks et al. ( [2021](https://arxiv.org/html/2502.00340v1#bib.bib10 "")).

Baselines and hyperparameters. We compare Collider with the following baselines: (1) regular training, which involves training the model without token filtering; and (2) Rho filtering Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")), an existing method of backward filtering that does not significantly enhance efficiency.
For the utility evaluation, we largely adhere to the hyperparameters outlined in Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")). Specifically, we aggregate different samples into a context length of 2048, set the batch size to one million tokens, and utilize a learning rate of 5×10−55superscript1055\\times 10^{-5}5 × 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT with cosine decay. We train all models for 1 epoch during the utility evaluation.
For the efficiency evaluation, we report throughput or time consumption per iteration, averaged over 10 iterations. Due to limited resources, we only report the utility evaluation on the TinyLlama, while the efficiency evaluation encompasses all three models—TinyLlama, Qwen2.5-1.5B, and Phi1.5.

### 6.2 Utility Evaluation

In the utility evaluation, we compare Collider with regular training and Rho filtering Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) on the TinyLlama model. We filter 40% of the tokens during the training of Collider and Rho filtering, while regular training utilizes all the tokens. [Table2](https://arxiv.org/html/2502.00340v1#S6.T2 "In 6 Evaluation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") displays the models’ performance on different tasks.
Compared to regular training, Collider not only improves model utility by 16.3% ( _i.e_., relative accuracy improvement) but also reduces the end-to-end training time from 4.5 to 3.7 days. For single tasks, the model utility of Collider surpasses that of regular training by up to 10.5% ( _e.g_., absolute accuracy improvements in MAWPS). In comparison to Rho filtering, Collider demonstrates significant efficiency improvements, though it exhibits a slight decrease in model utility. We analyze the utility decrease as follows.

Analyzing the utility decrease of Collider compared with Rho.
It is worth noting that the utility assessments are based on a direct comparison to provide readers with an intuitive impression: both Rho Lin et al. ( [2024b](https://arxiv.org/html/2502.00340v1#bib.bib20 "")) and Collider use the same training parameter settings. However, as discussed in § [4.1](https://arxiv.org/html/2502.00340v1#S4.SS1 "4.1 Filtering Activations Necessitates Different Training Parameters ‣ 4 Discussion ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"), Collider further filters the activations to improve efficiency and passes a smaller amount of gradients during backpropagation given the same inputs. Thus, it requires different parameters to achieve optimal performance. We believe that with more optimal parameter settings, the drop in model utility would be minimal.https://arxiv.org/html/2502.00340v1/x12.pngFigure 11: Throughput of regular training, Rho filtering, and Collider on TinyLlama model with different context lengths. Collider shows superior performance, with its efficiency advantage growing at longer contexts.https://arxiv.org/html/2502.00340v1/x13.pngFigure 12: The end-to-end speedup of Collider compared with Rho filtering on three models with different filtering ratios. The speedup of Collider linearly increases with the filtering ratio.https://arxiv.org/html/2502.00340v1/x14.pngFigure 13: The cost of Collider operator ( _i.e_., updating the graph) under different filtering ratios. The cost does not increase with the filtering ratio and is negligible compared with the time saved in the backward stage.

### 6.3 Efficiency Evaluation

We compare the training efficiency of Collider with regular training and Rho filtering on three models: TinyLlama, Qwen2.5-1.5B, and Phi1.5. We divide the training process into four stages: forward, computing loss, Collider operator ( _i.e_., updating the graph), and backward. [Table3](https://arxiv.org/html/2502.00340v1#S6.T3 "In 6 Evaluation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") presents a detailed time comparison for these four stages across the three models.
When filtering 40% of the tokens, Collider reduces end-to-end time consumption by 22.0%, 15.0%, and 18.7% compared to regular training and Rho filtering for the three models, respectively. In particular, Collider decreases the backward time consumption by 35.1%, 25.7%, and 30.5%, respectively. The additional cost of updating the graph ( _i.e_., the Collider operator) is relatively small compared to the time saved during the backward stage, resulting in a significant overall improvement in efficiency.
While the time consumption for loss computation is increased in token filtering methods compared to regular training—due to the additional process of selecting filtered tokens—the increased time is negligible and does not impact overall efficiency.

Impact of the context length.
The context length is a critical factor influencing the training efficiency of LLMs, as the training complexity increases quadratically with the context length. We evaluate the efficiency of Collider using different context lengths on the TinyLlama model. [Figure11](https://arxiv.org/html/2502.00340v1#S6.F11 "In 6.2 Utility Evaluation ‣ 6 Evaluation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider") illustrates the throughput of regular training, Rho filtering, and Collider across various context lengths ranging from 1K to 4K.
The throughput of Collider consistently exceeds that of both regular training and Rho filtering, with the efficiency improvement becoming more pronounced as the context length increases. At a context length of 4K, Collider achieves a 1.28×\\times× higher throughput than that of the other methods. These results demonstrate that Collider can effectively enhance efficiency in computationally intensive scenarios, such as long-context training.

Impact of the filtering ratio.
To further investigate the efficiency improvement of Collider, we evaluate the end-to-end speedup compared to Rho filtering under different filtering ratios, with the results shown in [Figure12](https://arxiv.org/html/2502.00340v1#S6.F12 "In 6.2 Utility Evaluation ‣ 6 Evaluation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"). The speedup of Collider increases linearly with the filtering ratio, demonstrating the effectiveness of Collider’s system design and indicating potential performance gains in scenarios with higher filtering ratios ( _e.g_., long-context training).
Additionally, the cost associated with the Collider operator ( _i.e_., updating the graph) at different filtering ratios is illustrated in [Figure13](https://arxiv.org/html/2502.00340v1#S6.F13 "In 6.2 Utility Evaluation ‣ 6 Evaluation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"). Notably, this cost does not increase with the filtering ratio and remains negligible when compared to the time saved during the backward stage. These results demonstrate that Collider can effectively enhance the training efficiency of LLMs through token filtering across varying filtering ratios.

## 7 Related Work

Apart from the studies introduced in § [2](https://arxiv.org/html/2502.00340v1#S2 "2 Background and Motivation ‣ Enhancing Token Filtering Efficiency in Large Language Model Training with Collider"), the following research topic is also closely related to our work.

Data Selection. Data selection is a pre-processing technique ( _i.e_., applied before training) aimed at improving data quality. Typically, it involves selecting diverse and high-quality training samples Bai et al. ( [2024](https://arxiv.org/html/2502.00340v1#bib.bib5 "")). Data selection occurs at the sample level prior to training, while our work focuses on token-level filtering during the training process. Theoretically, Collider functions as a fine-grained data selection method during training, selecting important tokens.

## 8 Conclusion

In this paper, we propose Collider, a system that unlocks the full efficiency of token filtering in LLM training. Collider maintains sparsity by further filtering the activations and transforms sparse GEMM into dense GEMM to optimize efficiency on existing hardware. Extensive evaluations demonstrate that Collider effectively achieves its design targets.

## References

- Abadi et al. \[2016\]↑
Martín Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo, Zhifeng Chen,
Craig Citro, Gregory S. Corrado, Andy Davis, Jeffrey Dean, Matthieu Devin,
Sanjay Ghemawat, Ian J. Goodfellow, Andrew Harp, Geoffrey Irving, Michael
Isard, Yangqing Jia, Rafal Józefowicz, Lukasz Kaiser, Manjunath Kudlur,
Josh Levenberg, Dan Mané, Rajat Monga, Sherry Moore, Derek Gordon
Murray, Chris Olah, Mike Schuster, Jonathon Shlens, Benoit Steiner, Ilya
Sutskever, Kunal Talwar, Paul A. Tucker, Vincent Vanhoucke, Vijay Vasudevan,
Fernanda B. Viégas, Oriol Vinyals, Pete Warden, Martin Wattenberg,
Martin Wicke, Yuan Yu, and Xiaoqiang Zheng.

Tensorflow: Large-scale machine learning on heterogeneous distributed
systems.

_CoRR_, abs/1603.04467, 2016.

- Amini et al. \[2019a\]↑
Aida Amini, Saadia Gabriel, Shanchuan Lin, Rik Koncel-Kedziorski, Yejin Choi,
and Hannaneh Hajishirzi.

Mathqa: Towards interpretable math word problem solving with
operation-based formalisms.

In _NAACL-HLT (1)_, pages 2357–2367. Association for
Computational Linguistics, 2019a.

- Amini et al. \[2019b\]↑
Aida Amini, Saadia Gabriel, Shanchuan Lin, Rik Koncel-Kedziorski, Yejin Choi,
and Hannaneh Hajishirzi.

Mathqa: Towards interpretable math word problem solving with
operation-based formalisms.

In _NAACL-HLT (1)_, pages 2357–2367. Association for
Computational Linguistics, 2019b.

- Ataiefard et al. \[2024\]↑
Foozhan Ataiefard, Walid Ahmed, Habib Hajimolahoseini, Saina Asani, Farnoosh
Javadi, Mohammad Hassanpour, Omar Mohamed Awad, Austin Wen, Kangling Liu, and
Yang Liu.

Skipvit: Speeding up vision transformers with a token-level skip
connection.

_CoRR_, abs/2401.15293, 2024.

- Bai et al. \[2024\]↑
Tianyi Bai, Ling Yang, Zhen Hao Wong, Jiahui Peng, Xinlin Zhuang, Chi Zhang,
Lijun Wu, Jiantao Qiu, Wentao Zhang, Binhang Yuan, and Conghui He.

Multi-agent collaborative data selection for efficient LLM
pretraining.

_CoRR_, abs/2410.08102, 2024.

- Cobbe et al. \[2021\]↑
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz
Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano,
Christopher Hesse, and John Schulman.

Training verifiers to solve math word problems.

_CoRR_, abs/2110.14168, 2021.

- Dao et al. \[2022\]↑
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré.

Flashattention: Fast and memory-efficient exact attention with
io-awareness.

In _NeurIPS_, 2022.

- Ding et al. \[2023\]↑
Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su,
Shengding Hu, Yulin Chen, Chi-Min Chan, Weize Chen, Jing Yi, Weilin Zhao,
Xiaozhi Wang, Zhiyuan Liu, Hai-Tao Zheng, Jianfei Chen, Yang Liu, Jie Tang,
Juanzi Li, and Maosong Sun.

Parameter-efficient fine-tuning of large-scale pre-trained language
models.

_Nat. Mac. Intell._, 5(3):220–235, 2023.

- Dubey et al. \[2024\]↑
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad
Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan,
et al.

The llama 3 herd of models.

_arXiv preprint arXiv:2407.21783_, 2024.

- Hendrycks et al. \[2021\]↑
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn
Song, and Jacob Steinhardt.

Measuring massive multitask language understanding.

In _ICLR_. OpenReview.net, 2021.

- Hou et al. \[2022\]↑
Le Hou, Richard Yuanzhe Pang, Tianyi Zhou, Yuexin Wu, Xinying Song, Xiaodan
Song, and Denny Zhou.

Token dropping for efficient BERT pretraining.

In _ACL (1)_, pages 3774–3784. Association for
Computational Linguistics, 2022.

- Hu et al. \[2022\]↑
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li,
Shean Wang, Lu Wang, and Weizhu Chen.

Lora: Low-rank adaptation of large language models.

In _ICLR_. OpenReview.net, 2022.

- Jiang et al. \[2024\]↑
Ziheng Jiang, Haibin Lin, Yinmin Zhong, Qi Huang, Yangrui Chen, Zhi Zhang,
Yanghua Peng, Xiang Li, Cong Xie, Shibiao Nong, Yulu Jia, Sun He, Hongmin
Chen, Zhihao Bai, Qi Hou, Shipeng Yan, Ding Zhou, Yiyao Sheng, Zhuo Jiang,
Haohan Xu, Haoran Wei, Zhang Zhang, Pengfei Nie, Leqi Zou, Sida Zhao, Liang
Xiang, Zherui Liu, Zhe Li, Xiaoying Jia, Jianxi Ye, Xin Jin, and Xin Liu.

Megascale: Scaling large language model training to more than 10, 000
gpus.

In _NSDI_, pages 745–760. USENIX Association, 2024.

- Koncel-Kedziorski et al. \[2016\]↑
Rik Koncel-Kedziorski, Subhro Roy, Aida Amini, Nate Kushman, and Hannaneh
Hajishirzi.

MAWPS: A math word problem repository.

In _HLT-NAACL_, pages 1152–1157. The Association for
Computational Linguistics, 2016.

- Korthikanti et al. \[2023\]↑
Vijay Anand Korthikanti, Jared Casper, Sangkug Lym, Lawrence McAfee, Michael
Andersch, Mohammad Shoeybi, and Bryan Catanzaro.

Reducing activation recomputation in large transformer models.

In _MLSys_. mlsys.org, 2023.

- Li et al. \[2023a\]↑
Sheng Li, Geng Yuan, Yue Dai, Youtao Zhang, Yanzhi Wang, and Xulong Tang.

Smartfrz: An efficient training framework using attention-based layer
freezing.

In _ICLR_. OpenReview.net, 2023a.

- Li et al. \[2023b\]↑
Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie Del Giorno, Suriya
Gunasekar, and Yin Tat Lee.

Textbooks are all you need II: phi-1.5 technical report.

_CoRR_, abs/2309.05463, 2023b.

- Lightman et al. \[2024\]↑
Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker,
Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe.

Let’s verify step by step.

In _ICLR_. OpenReview.net, 2024.

- Lin et al. \[2024a\]↑
Xinyu Lin, Wenjie Wang, Yongqi Li, Shuo Yang, Fuli Feng, Yinwei Wei, and
Tat-Seng Chua.

Data-efficient fine-tuning for llm-based recommendation.

In _SIGIR_, pages 365–374. ACM, 2024a.

- Lin et al. \[2024b\]↑
Zhenghao Lin, Zhibin Gou, Yeyun Gong, Xiao Liu, Ruochen Xu, Chen Lin, Yujiu
Yang, Jian Jiao, Nan Duan, Weizhu Chen, et al.

Not all tokens are what you need for pretraining.

In _The Thirty-eighth Annual Conference on Neural Information_
_Processing Systems_, 2024b.

- Lu et al. \[2023\]↑
Pan Lu, Liang Qiu, Kai-Wei Chang, Ying Nian Wu, Song-Chun Zhu, Tanmay
Rajpurohit, Peter Clark, and Ashwin Kalyan.

Dynamic prompt learning via policy gradient for semi-structured
mathematical reasoning.

In _ICLR_. OpenReview.net, 2023.

- Ma et al. \[2023\]↑
Xinyin Ma, Gongfan Fang, and Xinchao Wang.

Llm-pruner: On the structural pruning of large language models.

In _NeurIPS_, 2023.

- McAleer \[2023\]↑
Stephen McAleer.

Sat multiple choice math may 23.

[https://huggingface.co/datasets/mcaleste/sat\_multiple\_choice\_math\_may\_23](https://huggingface.co/datasets/mcaleste/sat_multiple_choice_math_may_23 ""),
2023.

- Miao et al. \[2020\]↑
Shen-Yun Miao, Chao-Chun Liang, and Keh-Yih Su.

A diverse corpus for evaluating and developing english math word
problem solvers.

In _ACL_, pages 975–984. Association for Computational
Linguistics, 2020.

- Mitra et al. \[2024\]↑
Arindam Mitra, Hamed Khanpour, Corby Rosset, and Ahmed Awadallah.

Orca-math: Unlocking the potential of slms in grade school math.

_CoRR_, abs/2402.14830, 2024.

- Narayanan et al. \[2021\]↑
Deepak Narayanan, Mohammad Shoeybi, Jared Casper, Patrick LeGresley, Mostofa
Patwary, Vijay Korthikanti, Dmitri Vainbrand, Prethvi Kashinkunti, Julie
Bernauer, Bryan Catanzaro, Amar Phanishayee, and Matei Zaharia.

Efficient large-scale language model training on GPU clusters using
megatron-lm.

In _SC_, page 58. ACM, 2021.

- Paster et al. \[2024\]↑
Keiran Paster, Marco Dos Santos, Zhangir Azerbayev, and Jimmy Ba.

Openwebmath: An open dataset of high-quality mathematical web text.

In _ICLR_. OpenReview.net, 2024.

- Patel et al. \[2021\]↑
Arkil Patel, Satwik Bhattamishra, and Navin Goyal.

Are NLP models really able to solve simple math word problems?

In _NAACL-HLT_, pages 2080–2094. Association for
Computational Linguistics, 2021.

- Rasley et al. \[2020\]↑
Jeff Rasley, Samyam Rajbhandari, Olatunji Ruwase, and Yuxiong He.

Deepspeed: System optimizations enable training deep learning models
with over 100 billion parameters.

In _KDD_, pages 3505–3506. ACM, 2020.

- Singh et al. \[2015\]↑
Bharat Singh, Soham De, Yangmuzi Zhang, Thomas A. Goldstein, and Gavin Taylor.

Layer-specific adaptive learning rates for deep networks.

In _ICMLA_, pages 364–368. IEEE, 2015.

- Sun et al. \[2024\]↑
Mingjie Sun, Zhuang Liu, Anna Bair, and J. Zico Kolter.

A simple and effective pruning approach for large language models.

In _ICLR_. OpenReview.net, 2024.

- Wang et al. \[2024\]↑
Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen,
Yu Wu, and Zhifang Sui.

Math-shepherd: Verify and reinforce llms step-by-step without human
annotations.

In _ACL (1)_, pages 9426–9439. Association for
Computational Linguistics, 2024.

- Wang et al. \[2023\]↑
Yiding Wang, Decang Sun, Kai Chen, Fan Lai, and Mosharaf Chowdhury.

Egeria: Efficient DNN training with knowledge-guided layer
freezing.

In _EuroSys_, pages 851–866. ACM, 2023.

- Yang et al. \[2024\]↑
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng
Li, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan
Lin, Jialong Tang, Jialin Wang, Jian Yang, Jianhong Tu, Jianwei Zhang,
Jianxin Ma, Jin Xu, Jingren Zhou, Jinze Bai, Jinzheng He, Junyang Lin, Kai
Dang, Keming Lu, Keqin Chen, Kexin Yang, Mei Li, Mingfeng Xue, Na Ni, Pei
Zhang, Peng Wang, Ru Peng, Rui Men, Ruize Gao, Runji Lin, Shijie Wang, Shuai
Bai, Sinan Tan, Tianhang Zhu, Tianhao Li, Tianyu Liu, Wenbin Ge, Xiaodong
Deng, Xiaohuan Zhou, Xingzhang Ren, Xinyu Zhang, Xipin Wei, Xuancheng Ren,
Yang Fan, Yang Yao, Yichang Zhang, Yu Wan, Yunfei Chu, Yuqiong Liu, Zeyu Cui,
Zhenru Zhang, and Zhihao Fan.

Qwen2 technical report.

_arXiv preprint arXiv:2407.10671_, 2024.

- Yao et al. \[2022\]↑
Zhewei Yao, Xiaoxia Wu, Conglong Li, Connor Holmes, Minjia Zhang, Cheng Li, and
Yuxiong He.

Random-ltd: Random and layerwise token dropping brings efficient
training for large-scale transformers.

_CoRR_, abs/2211.11586, 2022.

- Yu et al. \[2024\]↑
Longhui Yu, Weisen Jiang, Han Shi, Jincheng Yu, Zhengying Liu, Yu Zhang,
James T. Kwok, Zhenguo Li, Adrian Weller, and Weiyang Liu.

Metamath: Bootstrap your own mathematical questions for large
language models.

In _ICLR_. OpenReview.net, 2024.

- Yue et al. \[2024\]↑
Xiang Yue, Xingwei Qu, Ge Zhang, Yao Fu, Wenhao Huang, Huan Sun, Yu Su, and
Wenhu Chen.

Mammoth: Building math generalist models through hybrid instruction
tuning.

In _ICLR_. OpenReview.net, 2024.

- Zhang et al. \[2024\]↑
Peiyuan Zhang, Guangtao Zeng, Tianduo Wang, and Wei Lu.

Tinyllama: An open-source small language model, 2024.

- Zheng et al. \[2020\]↑
Shuai Zheng, Haibin Lin, Sheng Zha, and Mu Li.

Accelerated large batch optimization of BERT pretraining in 54
minutes.

_CoRR_, abs/2006.13484, 2020.

- Zhong et al. \[2023\]↑
Qihuang Zhong, Liang Ding, Juhua Liu, Xuebo Liu, Min Zhang, Bo Du, and Dacheng
Tao.

Revisiting token dropping strategy in efficient BERT pretraining.

In _ACL (1)_, pages 10391–10405. Association for
Computational Linguistics, 2023.

</details>

<details>
<summary>How to Understand Whole Software Repository?</summary>

# How to Understand Whole Software Repository?

Yingwei Ma, Qingping Yang, Rongyu Cao, Binhua Li, Fei Huang, Yongbin Li
[mayingwei.myw, yangqingping.yqp, caorongyu.cry, binhua.lbh, f.huang, shuide.lyb@alibaba-inc.com](mailto:mayingwei.myw,%20yangqingping.yqp,%20caorongyu.cry,%20binhua.lbh,%20f.huang,%20shuide.lyb@alibaba-inc.com)Alibaba Group

###### Abstract.

Recently, Large Language Model (LLM) based agents have advanced the significant development of Automatic Software Engineering (ASE). Although verified effectiveness, the designs of the existing methods mainly focus on the local information of codes, e.g., issues, classes, and functions, leading to limitations in capturing the global context and interdependencies within the software system. From the practical experiences of the human SE developers, we argue that an excellent understanding of the whole repository will be the critical path to ASE. However, understanding the whole repository raises various challenges, e.g., the extremely long code input, the noisy code information, the complex dependency relationships, etc. To this end, we develop a novel ASE method named RepoUnderstander by guiding agents to comprehensively understand the whole repositories. Specifically, we first condense the critical information of the whole repository into the repository knowledge graph in a top-to-down mode to decrease the complexity of repository. Subsequently, we empower the agents the ability of understanding whole repository by proposing a Monte Carlo tree search based repository exploration strategy. In addition, to better utilize the repository-level knowledge, we guide the agents to summarize, analyze, and plan. Then, they can manipulate the tools to dynamically acquire information and generate the patches to solve the real-world GitHub issues. Extensive experiments demonstrate the superiority and effectiveness of the proposed RepoUnderstander. It achieved 18.5% relative improvement on the SWE-bench Lite benchmark compared to SWE-agent.

Automatic Software Engineering (ASE), Agents, Large Language Models (LLMs), Fault Localization, Program Repair, Monte Carlo Tree Search (MCTS)

## 1\. Introduction

Automating Software Engineering (ASE), which aims to automatically accomplish the Software Engineering (SE) tasks, is a promising and challenging research direction. Recent years, in the ASE domain, Large Language Models (LLMs), especially LLM-based agents, have demonstrated their strong general abilities, e.g., the environment awareness ability (Hong et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib16 ""); Wang et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib38 ""); Kong et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib22 "")), planning & reasoning ability (Cognition, [2023](https://arxiv.org/html/2406.01422v1#bib.bib7 ""); OpenDevin, [2023](https://arxiv.org/html/2406.01422v1#bib.bib33 ""); Luo et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib30 ""); Wang et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib38 "")), tool construction (Zhang et al., [2024a](https://arxiv.org/html/2406.01422v1#bib.bib49 "")) ability, etc.

More recently, an exemplary milestone termed Devin (Cognition, [2023](https://arxiv.org/html/2406.01422v1#bib.bib7 "")) explores an end-to-end LLM-based agent system for complex real-world SE tasks (i.e., fix real-world Github issues). Specifically, it plans user requirements, utilizes editor, terminal, and search engine tools for independent decision-making and reasoning, and eventually generates code patches to meet the needs. This innovative approach has garnered considerable attention from the AI and SE communities, notably sparking interest in ASE (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 ""); Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 "")). For instance, SWE-agent (Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 "")) strategically designs an Agent Computer Interface (ACI) to empower SE agents in creating & editing code files, navigating repositories, and executing programs. Additionally, AutoCodeRover (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")) extracts abstract syntax trees in programs, iteratively searches for useful information based on requirements, and generates program patches.

Although the pioneers highlighted the road to advanced ASE and achieved promising performance, their designs, focusing on local information, failed to grasp the global context and intricate interdependencies among functions and classes.
For example, SWE-agent (Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 "")) maintains a context window within a code file that allows the agent to scroll up and down. AutoCodeRover (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")) searches functions or classes within the whole repository.
Typically, the code comprising a full logic chain for a specific functionality is not arranged sequentially within a single file; rather, it is logically scattered across multiple folders and files.
It is difficult to retrieve all relevant code files among maybe thousands of files in a repository, especially starting only from the text in user requirements.
This paper argues that a comprehensive understanding of the whole repository becomes the most critical path to ASE.

Undoubtedly, it is challenging to utilize the vast information of an entire repository within LLM.
Firstly, a GitHub repository may contain thousands of code files, making it impractical to include them all in the context windows of LLM. Even if it could, an LLM would struggle to accurately capture the code relevant to the objective within such an extensive context.
Secondly, since user requirements are often described in natural language, identifying the relevant code within a repository presents a significant challenge.
Thirdly, the intrinsic logic of how the code execution is distinctly different from the sequence of the code text in a file. For instance, the location where a bug triggers an error message and the actual place that requires modification may not be in the same file, yet they are certainly logically connected.

To solve this problem, we propose a novel ASE method named RepoUnderstander by guiding the LLM-based agents to comprehensively understand the whole repository and take advantage of the learned the repository-level knowledge. Imaging the human software engineers are solving project-level issues, they will first overview the repository to ensure a full understanding of the functional modules and dependencies that may be involved. Motivated by this practical insight, we first condense the complex repository-level information by constructing the repository knowledge graph in a top-down manner. Concretely, the repository is organized into a hierarchical structure tree, enabling a clear understanding of the code’s context and scope. Besides, to facilitate comprehensive dependency and interaction analysis, the tree structure is further expanded into a reference graph that captures function call relationships.

Subsequently, we propose a Monte Carlo Tree Search (MCTS) based repository exploration strategy to empower the LLM-based agents the ability of collecting and learning repository-level knowledge. Specifically, the agents first collect the critical information regarding to the SE task on the repository knowledge graph by the explore-and-exploit strategy. Then, by simulating multiple trajectories and evaluating their reward score, our method iteratively narrows down the search space and guide the agents to focus on the most relevant areas. In addition, to better utilize the repository-level knowledge, we guide the agents to summarize, analyze, and plan for the repository information regarding to the SE targets. By these designs, it enables the agents to effectively and efficiently collect and learn task-relevant repository-level knowledge, therefore facilitating the precise fault localization and the informed patch generation. Finally, the agents are instructed to manipulate the API tools to dynamically acquire local information, and fix the real-world issues by generating patches. We demonstrate the superiority and effectiveness of RepoUnderstander via extensive experiments and comprehensive analyses. Besides, through carefully analyses during the experiments, we identify an important problem of the SWE-bench dataset, i.e., missing the necessary interface specification for new feature issues. We propose to fix it and achieve more reliable and effective evaluation for our method and the baseline. The main contributions of this paper are summarized as follows.

- •

We highlight the whole repository understanding as the crucial path to ASE and propose a novel agent-based method named RepoUnderstander to solve the challenges.

- •

We propose to condense the extensive codes and complex relations of the repository into the knowledge graph in a top-to-down mode, improving performance and efficiency.

- •

We design a Monte Carlo tree search based repository exploration strategy to assist the comprehensive understanding of the whole repository for the issue-solving agents.

- •

Extensive experiments and analyses demonstrate the superiority and effectiveness of RepoUnderstander 111 [https://github.com/RepoUnderstander/RepoUnderstander](https://github.com/RepoUnderstander/RepoUnderstander "").

## 2\. Related Work

### 2.1. LLM-based Software Engineering Agents

In recent years, Large Language Model (LLM) based AI agents have advanced the development of automatic software engineering. AI agents improve the capabilities of project-level software engineering (SE) tasks through running environment awareness (Hong et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib16 ""); Wang et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib38 ""); Kong et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib22 "")), planning & reasoning (Wang et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib38 ""); Cognition, [2023](https://arxiv.org/html/2406.01422v1#bib.bib7 ""); OpenDevin, [2023](https://arxiv.org/html/2406.01422v1#bib.bib33 ""); Luo et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib30 "")), and tool construction (Zhang et al., [2024a](https://arxiv.org/html/2406.01422v1#bib.bib49 ""); Lee et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib24 "")). Surprisingly, Devin (Cognition, [2023](https://arxiv.org/html/2406.01422v1#bib.bib7 "")) is a milestone that explores an end-to-end LLM-based agent system to handle complex SE tasks. Concretely, it first plans the requirements of users, then adopts the editor, terminal and search engine tools to make independent decisions and reasoning, and finally generates codes to satisfy the needs of users in an end-to-end manner. Its promising designs and performance swiftly ignited unprecedented attention from the AI community and SE community to Automatic Software Engineering (ASE) (Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 ""); Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")). For example, SWE-agent (Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 "")) carefully designs an Agent Computer Interface (ACI) to empower the SE agents capabilities of creating & editing code files, navigating repositories, and executing programs. Besides, AutoCodeRover (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")) extracts the abstract syntax trees in programs, then iteratively searches the useful information according to requirements, and eventually generates program patches. Their designs mainly focus on the local information in the repository, e.g., code files, classes, or functions themselves. Although achieving promising performance, from the insights of the human SE developers, the excellent understanding of the whole repository is a critical path to ASE.

### 2.2. Evaluation of LLM-based Software Engineering Agents

Benefiting from the strong general capability of LLMs, LLM-based software engineering agents can handle many important SE tasks, e.g., repository navigation (Zhang et al., [2024a](https://arxiv.org/html/2406.01422v1#bib.bib49 ""); Wang et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib38 "")), code generation (Hong et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib16 ""); Ding et al., [2024a](https://arxiv.org/html/2406.01422v1#bib.bib9 ""); Ishibashi and Nishimura, [2024](https://arxiv.org/html/2406.01422v1#bib.bib19 ""); Tang et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib37 ""); Rasheed et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib35 "")), debugging (Hong et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib16 ""); Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 ""); Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")), program repair (Qin et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib34 ""); Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 ""); Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 "")). The existing methods usually regard code generation as a core ability and mainly conduct evaluations on it. Precisely, the code generation test set (Chen et al., [2021](https://arxiv.org/html/2406.01422v1#bib.bib6 ""); Austin et al., [2021](https://arxiv.org/html/2406.01422v1#bib.bib3 ""); Liu et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib26 ""); Zheng et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib51 ""); Lu et al., [2021](https://arxiv.org/html/2406.01422v1#bib.bib29 "")) consists of the short problem description, the solution, and the corresponding unit test data. However, with the fast development of LLMs and agents, these datasets are no longer able to comprehensively evaluate their capabilities in the real-world SE tasks. To this end, the repository-level code completion and generation tasks (Liu et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib27 ""); Ding et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib10 ""); Du et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib13 "")) are presented to evaluate the repository understanding and generation capabilities of LLMs and agents. More recently, SWE team(Jimenez et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib20 ""); Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 "")) develop a unified dataset named SWE-bench to evaluate the capability of the agent system to solve real-world GitHub issues automatically. Specifically, it collects the task instances from real-world GitHub issues from twelve repositories. Consistent with previous evaluation methods, SWE-bench is based on the automatic execution of the unit tests. Differently, the presented test set is challenging and requires the agents to have multiple capabilities, including repository navigation, fault locating, debugging, code generation and program repairing. Besides, SWE-bench Lite (Carlos E. Jimenez, John Yang, Jiayi Geng, [2024](https://arxiv.org/html/2406.01422v1#bib.bib5 "")) is a subset of SWE-bench, and it has a similar diversity and distribution of repositories as the original version. Due to the smaller test cost and more detailed filtering, SWE-bench Lite is officially recommended as the benchmark of LLM-based SE agents. Therefore, consistent with previous methods (Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 ""); Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 ""); OpenDevin, [2023](https://arxiv.org/html/2406.01422v1#bib.bib33 "")), we report our performance on SWE-bench Lite.

### 2.3. Repository-level Code Intelligence

With the development of AI technology, the field of code intelligence has gradually transitioned from solving single function-level or code snippet-level problems to real-world software development at the repository level. In the repository-level code intelligence task, there are many works (Liang et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib25 ""); Ding et al., [2022](https://arxiv.org/html/2406.01422v1#bib.bib11 ""); Zhang et al., [2023b](https://arxiv.org/html/2406.01422v1#bib.bib48 ""); Lozhkov et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib28 ""); Guo et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib14 ""); Zan et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib46 ""); Shrivastava et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib36 ""); Bairi et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib4 "")) that aim to leverage the large amount of code available in current repositories to help code models generate better, more accurate code.
Among them, StarCoder2 (Lozhkov et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib28 "")) and Deepseek-Coder (Guo et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib14 "")) model repository knowledge in the pre-training stage, sort repository files according to reference dependencies, and guide the model to learn the global dependencies of repository information. RepoCoder (Zhang et al., [2023b](https://arxiv.org/html/2406.01422v1#bib.bib48 "")) continuously retrieves relevant content by iterating RAG, while methods such as CoCoMIC (Ding et al., [2022](https://arxiv.org/html/2406.01422v1#bib.bib11 "")) and RepoFuse (Liang et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib25 "")) jointly use the RAG module and the current file’s dependency relationship module to introduce it into the context of LLM. Although the above methods enhance the model’s understanding of the repository context to a certain extent, the repository-level code often contains complex contextual call relationships, and the RAG method alone may not be able to recall all semantically relevant content. In addition, there may be a large amount of complex irrelevant information in the RAG results, which interferes with the model’s accurate fault location. Therefore, starting from the practical experience of software engineering, we simulated people’s global experience in understanding the repository and experience-guided exploration and location to achieve more effective repository understanding.

## 3\. Methodology

### 3.1. Overview

We first describe the overall operating process of RepoUnderstander, and introduce the stages in detail in the subsequent parts of this section. Given a workspace, RepoUnderstander can automatically solve real-world GitHub issues. Among them, RepoUnderstander involves three key steps, repository knowledge graph construction stage, MCTS-enhanced repository understanding stage, information utilization & patch generation stage. The overall workflow is shown in Figure [1](https://arxiv.org/html/2406.01422v1#S3.F1 "Figure 1 ‣ 3.1. Overview ‣ 3. Methodology ‣ How to Understand Whole Software Repository?").https://arxiv.org/html/2406.01422v1/x1.pngFigure 1. The overview of our proposed RepoUnderstander. Firstly, we construct the repository knowledge graph is constructed to efficiently represent the code and the dependency in the repository. Subsequently, we empower the agents with the ability of repository understanding by designing the Monte Carlo tree search based repository explore strategy. In addition, we guide the agents to summarize, analyze, and plan to better utilize the repository-level knowledge. Then, they can manipulate the tools to dynamically acquire issue-relevant code information and generate the patches to solve the real-world GitHub issues
In Repository Knowledge Graph Construction phase, RepoUnderstander first builds a repository knowledge graph to represent the entire repository and describe the relationships between entities. This is achieved by parsing the software structure and analyzing it in a top-down manner. The repository is first organized into a hierarchical tree that allows a clear understanding of the context and scope of the code. To facilitate comprehensive dependency and interaction analysis, the tree structure is further extended into a reference graph that captures function call relationships.

Due to the large scale and information complexity of the repository knowledge graph, during the MCTS-Enhanced Repository Understanding phase, RepoUnderstander uses the Monte Carlo tree search algorithm to dynamically explore the entire graph. This method focus on discovering key information (i.e., repository functionality and dependency structure) that has a significant impact on issue solving. Through correlation expansion and reference expansion, MCTS simulates multiple trajectories and evaluates their importance, dynamically narrowing the search space and allocating computing resources to the most relevant regions. This targeted navigation enables the model to efficiently access and process important information in the repository, thereby facilitating precise fault localization and informed patch generation.

Inspired by the actual development experience of human programmers, it is necessary to have certain global prior knowledge of the repository before solving specific tasks. Therefore, in Information Utilization & Patch Generation phase, RepoUnderstander first summarizes the important information collected in the repository understanding phase to form an experience of the entire repository. Then, in order for RepoUnderstander to use the global experience to obtain dynamic information during the problem solving process, we follow AutoCodeRover(Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 ""))’s information retrieval method and use API tools to extract information in the repository knowledge graph. This includes specific classes and functions and code snippets, etc., to maintain local dynamic knowledge during the task. After collecting enough context, RepoUnderstander uses global experience to summarize the currently acquired information to locate faults, generate modified code and return patches that try to resolve the issue.

### 3.2. Repository Knowledge Graph Construction

For human programmers, when solving project-level issues, developers first need to carefully review and understand the project’s software repository to ensure that they have a full understanding of the functional modules and dependencies that may be involved. This includes building the hierarchical tree structure and call graph of the software repository. Through the hierarchical tree structure, developers can clearly see the overall architecture of the project and the relationship between each module; through the call graph, developers can understand the calling relationships and dependency paths between functions to identify the root causes of problems and the potential impact of changes.

Therefore, in order to learn from the practices of human programmers in understanding and maintaining code, we represent the entire repository as a repository knowledge graph and describe the relationships between entities by parsing the software structure  (see Repo. Knowledge Graph Construction in Figure [1](https://arxiv.org/html/2406.01422v1#S3.F1 "Figure 1 ‣ 3.1. Overview ‣ 3. Methodology ‣ How to Understand Whole Software Repository?")). First, we top-down analyze the structure of the software repository, organizing the repository into a hierarchical structure tree (including files, classes, and functions) to clearly understand the context and scope of the code. We then extend the tree structure into a reference graph containing function call relationships, allowing the model to perform comprehensive dependency and interaction analysis. Different from existing methods(Luo et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib30 ""); Ding et al., [2022](https://arxiv.org/html/2406.01422v1#bib.bib11 "")), our reference relationship only involves functions, because functions are the basic unit of program execution, and the calling relationship between functions directly affects the behavior and execution logic of the program. Excessive reference relationships may increase the complexity of the graph structure and affect the analysis efficiency and accuracy of the model. This structured repository knowledge graph not only improves the efficiency of the model in retrieving relevant information, but also ensures the consistency and reliability of the automated process.

Specifically, we recursively traverse each code file in the repository, use abstract syntax trees to parse the corresponding files respectively, and obtain basic units such as classes and functions, including their names, code snippets, paths, and locations in the files. We then add these elements to the structure tree from top to bottom. Finally, we analyze the calling relationship between functions and add corresponding directed edges to the graph. This in-depth understanding provides LLM agents with the necessary background knowledge and contextual information, allowing them to more accurately locate the problem and come up with effective solutions.

### 3.3. MCTS-Enhanced Repository Understanding

After building a repository knowledge graph, a comprehensive understanding of the information in the graph is critical to effectively solving problems. However, given the complexity and size of modern software systems, often containing hundreds of files and thousands of functions. The vast magnitude of the search space in large software repositories makes exhaustive analysis impractical. Furthermore, context length limitations of language models limit the amount of information that can be efficiently processed at given conversation. Therefore, without targeted methods to identify highly relevant nodes and edges in graphs, models may struggle to perform accurate and efficient analysis, hampering their ability to solve real-world software engineering problems.

To address these challenges, we propose an repository exploration approach that leverages Monte Carlo Tree Search (MCTS) to enhance LLM and agents’ understanding of software repositories (see MCTS-Enhanced Repo. Understanding in Figure [1](https://arxiv.org/html/2406.01422v1#S3.F1 "Figure 1 ‣ 3.1. Overview ‣ 3. Methodology ‣ How to Understand Whole Software Repository?")). This method systematically explores the repository knowledge graph and prioritizes the discovery of critical information such as repository functions and dependency structures that have a greater impact on resolving issues. By simulating multiple trajectories and evaluating their importance, MCTS dynamically narrows the search space and focuses computational resources on the most relevant areas. This targeted navigation enables models to access and process important information more efficiently, thus facilitating precise fault localization and informed patch generation. The MCTS process begins from a root node, representing the repository node, and unfolds in four iterative stages: selection, correlation expansion, simulation&evaluation and backpropagation&reference expansion. Below we describe each stage in further detail.

Selection. The selection phase aims to balance exploration and exploitation problems in the node selection process. The main challenge in this phase is to maintain a balance between in-depth analysis of highly relevant content in the repository and a broad search for potentially important information throughout the repository. Delving excessively into high-correlation modules can cause the model within a local optimal solution, ignoring that other critical paths or dependencies may exist. Extensive search may lead to the dispersion of computing resources and the processing of a large amount of irrelevant information, which increases the burden on the model and reduces search efficiency. To balance the needs of the above two aspects, we use the UCT algorithm (Kocsis and Szepesvári, [2006](https://arxiv.org/html/2406.01422v1#bib.bib21 "")) for node selection, following the formula: U⁢C⁢T=wini+c⁢2⁢ln⁡npni𝑈𝐶𝑇subscript𝑤𝑖subscript𝑛𝑖𝑐2subscript𝑛𝑝subscript𝑛𝑖UCT=\\frac{w\_{i}}{n\_{i}}+c\\sqrt{\\frac{2\\ln n\_{p}}{n\_{i}}}italic\_U italic\_C italic\_T = divide start\_ARG italic\_w start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG start\_ARG italic\_n start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG + italic\_c square-root start\_ARG divide start\_ARG 2 roman\_ln italic\_n start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT end\_ARG start\_ARG italic\_n start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG end\_ARG, where wisubscript𝑤𝑖w\_{i}italic\_w start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT is the total reward of child node i𝑖iitalic\_i. The calculation of specific rewards will be introduced in detail in Simulation & Evaluation section. nisubscript𝑛𝑖n\_{i}italic\_n start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT is the number of visits to child node i𝑖iitalic\_i and npsubscript𝑛𝑝n\_{p}italic\_n start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT is the number of visits to the parent node. c𝑐citalic\_c is the exploration parameter used to adjust the balance between exploration and exploitation. In this work, we set c𝑐citalic\_c to 2/222\\sqrt{2}/2square-root start\_ARG 2 end\_ARG / 2.

Correlation Expansion. During the expansion process, leaf nodes are expanded to incorporate new nodes. If the current leaf node has a child node in the repository knowledge graph, the most likely child node is selected instead of random expansion. In this stage, we designed two methods: Correlation expansion and Reference relationship expansion. In this section, we mainly introduce correlation expansion, and reference relationship expansion will be introduced in the Backpropagation & Reference Expansion section. Similar code is most likely to be code related to user requirements. User requirements or issues usually contain some keywords that may add new or modified functions. Therefore, we use the bm25 score to calculate the relevance (Ding et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib10 ""); Husain et al., [2019](https://arxiv.org/html/2406.01422v1#bib.bib18 ""); Xie et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib43 "")), and give priority to codes with higher relevance for expansion. Correlation expansion can effectively match user requirements with relevant nodes in the software knowledge graph, thereby improving the accuracy and efficiency of node expansion.

Simulation & Evaluation. After completing the expansion, we enter the simulation process. During the simulation, we start from the newly expanded node and simulate along possible paths to evaluate the effectiveness of these paths in solving the current issue. Consistent with the correlation expansion method, we continuously and recursively select the child nodes with the highest correlation scores in the software knowledge graph until leaf nodes, and then reward the nodes.

In the evaluation phase, we need to evaluate the relevance of the selected leaf nodes to the issue, including classes, top-level functions, class methods or sub-functions, etc. However, traditional evaluation methods usually rely on keyword matching and semantic matching algorithms, which perform poorly when dealing with complex software systems and diverse problem descriptions.https://arxiv.org/html/2406.01422v1/x2.pngFigure 2. Reward agent’s input prompt template and output results, with some details omitted.
Inspired by the success of large language models in in-context learning (ICL) (Dong et al., [2022](https://arxiv.org/html/2406.01422v1#bib.bib12 ""); Work, [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib41 "")) and Chain-of-Thought (CoT) (Wei et al., [2022](https://arxiv.org/html/2406.01422v1#bib.bib39 "")) methods, we propose a reward method based on ICL and CoT, aiming to provide a more accurate and reliable solution for relevance evaluation in software repository. Our approach leverages the advanced ability of large language models to learn and optimize reward functions from limited examples of programming practice to accurately assess the correlation between leaf nodes and problem descriptions. Specifically, we first use ICL to let the language model learn to understand the core functions and operating modes of the reward function in a given context. Then, the CoT is used to enable the model to conduct in-depth reasoning based on the specific information in the question and code snippets to evaluate the correlation of leaf nodes. The reward function prompt template we designed (see Figure [2](https://arxiv.org/html/2406.01422v1#S3.F2 "Figure 2 ‣ 3.3. MCTS-Enhanced Repository Understanding ‣ 3. Methodology ‣ How to Understand Whole Software Repository?")) starts with a guided system prompt that clearly points out the goals and responsibilities of the reward function. Then, through a series of example combinations of ¡issue description, code snippets, thinking process, results¿, the input, output and reasoning chain in the scoring process are demonstrated. Finally, the prompt ends with a new set of issue descriptions and code snippets, at which point the model is expected to learn the intermediate reasoning steps from the given examples and output corresponding reward scores. Finally, we only keep the nodes with a reward score of no less than 6 and return their content and structural dependencies.

Compared with traditional methods, our method reduces the dependence on large amounts of labeled data. This is critical to cope with diverse and evolving situations in software repository, as traditional approaches may suffer from the limitations of labeled data. Therefore, our method has better adaptability and accuracy when resolving real-world software development environments.

Backpropagation & Reference Expansion.
After the evaluation ends, we perform a bottom-up update from the terminal node back to the root node. During this process, we update the visit count n𝑛nitalic\_n and the reward value w𝑤witalic\_w. In addition, we also introduced reference relationship expansion in the backpropagation phase. Different from the conventional expansion method, we not only expand when we encounter leaf nodes, but also when we encounter those nodes with higher reward scores (set the threshold to a reward score of not less than 6 here), we will expand their reference modules and objects based on the repository knowledge graph. And then integrate them into new nodes. The insight is that in actual development, the node called by the current node is often the key node for function implementation, and the called node is usually the use of the current node and depends on the implementation and changes of the current node. Therefore, if a node has a higher reward score, the nodes with calling relationships may also be relevant. By expanding these calling relationship nodes, code snippets related to the current issue can be captured more comprehensively.

### 3.4. Information Utilization & Patch Generation

At this stage, RepoUnderstander first summarizes the whole repository experience, then obtains code snippet information dynamicly on this basis, and finally generates patches that try to solve the problem. The three steps are detailed below.

Repository Summary. To more effectively utilize the global repository information collected during the repository understanding phase, we introduce a summary agent. The agent aims to systematically analyze and summarize the code snippets collected in the repository knowledge graph and submitted issues , and then plan how to solve the problem, thereby forming an experience of the entire repository. Specifically, the summary agent takes the issue and the collected relevant code fragments as input, and then outputs a summary of the relevant fragments in sequence and plans a solution. The specific prompt template is shown in Figure [3](https://arxiv.org/html/2406.01422v1#S3.F3 "Figure 3 ‣ 3.4. Information Utilization & Patch Generation ‣ 3. Methodology ‣ How to Understand Whole Software Repository?"). Since the collected global repository information may be complex and contain a large number of code fragments and annotation descriptions, we only use the location description of the relevant code fragments (i.e., structural dependencies in the repository) and the output of the Summary Agent (i.e., summary and planning) as RepoUnderstander’s experience to guide subsequent actions. This experience does not include specific function implementation, but only focuses on overall repository experience guidance. The location description is formalized as ¡file¿a.py¡/file¿¡class¿Class A¡/class¿¡func¿func a¡/func¿, and the summary agent output is as shown in Figure [3](https://arxiv.org/html/2406.01422v1#S3.F3 "Figure 3 ‣ 3.4. Information Utilization & Patch Generation ‣ 3. Methodology ‣ How to Understand Whole Software Repository?").https://arxiv.org/html/2406.01422v1/Figure 3. Summary agent’s input prompt template and output results, with some details omitted.
Dynamic information acquisition. Global experience information is RepoUnderstander’s experience summary of relevant information in the current workspace, which can help the language model understand issues and find solutions more quickly. In the process of solving problems, in order to make full use of this global experience information, RepoUnderstander futher needs to dynamically extract local information from the current repository, including specific classes, functions and code snippets in the repository.

The ReAct (Yao et al., [2022](https://arxiv.org/html/2406.01422v1#bib.bib45 "")) framework (i.e., Reson then Act) guides the model to generate inference trajectories and task-specific actions in a staggered manner, allowing the model to interact with the code repository and collect information. Specifically, the ReAct framework first generates reasoning paths through the Chain-of-Thought (Wei et al., [2022](https://arxiv.org/html/2406.01422v1#bib.bib39 "")), and then outputs actual actions based on the reasoning results. Therefore, by using ReAct method, RepoUnderstander can call the corresponding search API according to task requirements and dynamically extract local information from the current repository to collect relevant context. We follow AutoCodeRover’s search API method (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")), using the three-layer search method of search\_class, search\_method, and search\_code. Specifically, RepoUnderstander first independently determines the API that needs to be called. Then the retrieval API will search for classes, methods and code snippets in the repository knowledge graph, and finally return the results to the agent.

Patch Generation. In the patch generation step, RepoUnderstander first locates faults based on the summary of global experience and dynamic information, extracts the context of code snippets that may need to be modified, and then generates modified code snippets. Finally, a diff is generated based on the code snippet before modification and the code snippet after modification, and is returned as the final result. If a diff is incorrect due to syntax, we will retry until an applicable patch with correct syntax is generated. We follow AutoCodeRover (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")) and set the maximum number of retries to 3 to ensure that the generated patch can be applied as much as possible.

## 4\. Experiment

To validate the performance of RepoUnderstander, we conduct experiments and compare it with other LLMs and agents to demonstrate its superiority (§ [4.2](https://arxiv.org/html/2406.01422v1#S4.SS2 "4.2. Comparison Experiment ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"), § [4.4](https://arxiv.org/html/2406.01422v1#S4.SS4 "4.4. Ablation Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?")). In addition, we found that there is an information asymmetry problem in SWE-bench (Jimenez et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib20 "")) caused by new added function names and variable names in the test patch (§ [4.3](https://arxiv.org/html/2406.01422v1#S4.SS3 "4.3. Dataset Analysis & Fix ‣ 4. Experiment ‣ How to Understand Whole Software Repository?")). We proposed issue patches to new feature types issues to solve this problem and test agents on the new FIX version test set. Finally, we systematically analyzed the problem-solving capabilities of RepoUnderstander at different stages (§ [4.5](https://arxiv.org/html/2406.01422v1#S4.SS5 "4.5. Case Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?")).

### 4.1. Experimental Setup

Datasets. We evaluate on the SWE-bench Lite dataset (Jimenez et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib20 "")) which are constructed due to the high cost of evaluating in the complete SWE-bench. SWE-bench Lite includes 300 task instances sampled from SWE-bench, following a similar repository distribution. SWE-bench team recommend future systems evaluating on SWE-bench to report numbers on SWE-bench Lite in lieu of the full SWE-bench set if necessary. SWE-bench Lite aims to provide a diverse set of code base issues that can be verified using in-repository unit tests. It requires LLM systems to generate corresponding patches based on the actual issues in the repository, and then pass the tests.

Baselines.
We compare RepoUnderstander with two types of baselines. The first category is the RAG baselines (Jimenez et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib20 "")). This type of baseline uses the BM25 method to retrieve code base files related to the issue and inputs them into LLM to directly generate patch files that solve the problem. The second type of baseline is the agents baseline (i.e., AutoCodeRover (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")) and SWE-agent (Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 ""))), which locates the problem through complex multiple rounds of interaction and execution feedback, and finally generates a patch to solve the problem through iterative verification.

Metrics.
Following the SWE-bench (Jimenez et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib20 "")), We evaluate the effectiveness of RepoUnderstander, using the percentage of resolved instances and the patch application rate. Among them, the patch application rate refers to the proportion of instances where code changes are successfully generated and can be applied to existing code bases using Git tools. Resolved ratio represents the overall effectiveness of solving actual GitHub issues, and application ratio reflects the intermediate results of patch availability.

Configurations.
All results, ablations, and result analyzes of RepoUnderstander use the GPT4-Turbo model (i.e., gpt-4-1106-preview (Achiam et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib2 "")), the same model with SWE-agent (Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 ""))). We use ast222https://docs.python.org/3/library/ast.html and Jedi333https://github.com/davidhalter/jedi library to parse repository and obtain syntax structures and dependencies of repository. In MCTS-Enhanced Repository Understanding stage, we set the number of search iterations to 600 and maximum search time to 300 seconds. In information Utilization & Patch Generation stage, we set the maximun number of summary code snippets to 10. SWE-bench has a relatively complex environment configuration. Thanks to the development of the open source community, we use the well-build open source docker of the AutoCodeRover (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")) team for experiments.

### 4.2. Comparison Experiment

| Method | Resolved | Apply |
| --- | --- | --- |
| RAG-based | | |
| SWE-Llama 7B | 1.33% (4) | 38.00% |
| SWE-Llama 13B | 1.00% (3) | 38.00% |
| ChatGPT-3.5 | 0.33% (1) | 10.33% |
| GPT-4 | 2.67% (8) | 29.67% |
| Claude-2 | 3.00% (9) | 33.00% |
| Claude-3 Opus | 4.33% (13) | 51.67% |
| Agent-based | | |
| AutoCodeRover | 16.11% (48) | 83.00% |
| SWE-agent | 18.00% (54) | 93.00% |
| RepoUnderstander | 21.33% (64) | 85.67% |

Table 1. Main results for RepoUnderstander performance on the SWE-bench-lite test set. The numbers in brackets indicate the number of issues solved.
We first evaluate the effectiveness of RepoUnderstander in SWE-bench Lite (300 instances). The performance comparison analysis between RepoUnderstander and other methods is shown in Table [1](https://arxiv.org/html/2406.01422v1#S4.T1 "Table 1 ‣ 4.2. Comparison Experiment ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"). In each instance, we provide a natural language description from a real-world software engineering problem and a local code repository of corresponding versions, asking the model to solve the problem and generate patches that can pass local automated testing. Resolved reflects the end-to-end ability of the current RAG LLM system and Agent system to solve software engineering problems. The results show that RepoUnderstander is significantly better than other RAG and Agent systems, achieving SOTA performance on the test set. Compared with the RAG system, our method improves performance by nearly 5 times. Compared with the state-of-the-art Agent system, we improve the accuracy of SWE-agent by 18.5%. These excellent performances demonstrate the advancement of our approach. In addition, the Apply application rate indicates the availability of generated patches. We found that Agent-based systems all achieved high availability, while RAG-based systems have lower availability, which proves that agent systems may be an important means to automatically solve software engineering tasks. SWE-agent has the highest Apply application rate due to the introduction of its running feedback capability, which shows that running feedback is an effective way. This paper focuses more on the understanding of the entire repository information. We will integrate running feedback in future work.

In addition, we also compared the issue-solving distribution diagrams of three Agent-based methods, and the results are shown in Figure [4](https://arxiv.org/html/2406.01422v1#S4.F4 "Figure 4 ‣ 4.2. Comparison Experiment ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"). We found that our method is very complementary to the SWE-agent method. The two methods jointly solved 80 examples, achieving a task resolved rate of 26.67% (see Table [2](https://arxiv.org/html/2406.01422v1#S4.T2 "Table 2 ‣ 4.2. Comparison Experiment ‣ 4. Experiment ‣ How to Understand Whole Software Repository?")), which further illustrates the complementarity of our method and the execution feedback method. We will provide a detail discussion and combination of the two methods in future work.https://arxiv.org/html/2406.01422v1/x4.pngFigure 4. Venn diagrams of resolved cases of RepoUnderstander, SWE-agent and AutoCodeRover.
| Method | Resolved | Apply |
| --- | --- | --- |
| ACR & SWE-agent | 24.33% (73) | 98.00% |
| RepoU & ACR | 25.33% (76) | 94.67% |
| RepoU & SWE-agent | 26.67% (80) | 99.67% |

Table 2. Venn diagram analysis of our method and baselines.
### 4.3. Dataset Analysis & Fix

User issues usually include bug reports, feature requests, and enhancements, etc (Moran Altarac, [2024](https://arxiv.org/html/2406.01422v1#bib.bib32 ""); Merten et al., [2016](https://arxiv.org/html/2406.01422v1#bib.bib31 ""); Krishna et al., [2018](https://arxiv.org/html/2406.01422v1#bib.bib23 ""); wiki koha, [2024](https://arxiv.org/html/2406.01422v1#bib.bib40 "")). In SWE-bench dataset (Jimenez et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib20 "")), we found that there is information asymmetry for issues of the feature request type, such as adding functions or adding parameter definitions. Specifically, since the test patch contains the signature information of the new features, and the LLM Agents input lacks this interface specification information, the agent model may not be able to correctly understand the full context of the problem. Even if the logic of the generated patch is correct, errors may occur during testing. This information asymmetry may affect the performance evaluation and practical application of the LLM agents. From the perspective of software engineering practice, new features are usually defined and specified in the system design document. In actual development, the information of these new features should be specified rather than inferred by the agent model. Therefore, merging the new feature interface specification in the test patch into the problem description can enable the agent model to better understand the problem and reduce the impact of information asymmetry.

We made a fix for the SWE-bench Lite dataset and proposed a FIX version. Specifically, we integrated the new feature interface specifications in the test patch into the problem description through manual analysis, and guided the agent model to generate patches based on the complete problem description. In total, we fixed 45/300 instances in SWE-bench Lite. This method can better reflect the reality in practice, reduce the problems caused by information asymmetry, and thus improve the credibility and effectiveness of automatic software engineering technology in practical applications.
As shown in Table [3](https://arxiv.org/html/2406.01422v1#S4.T3 "Table 3 ‣ 4.3. Dataset Analysis & Fix ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"), our experimental results show that on the FIX version test set, the methods RepoUnderstander and AutoCodeRover (Zhang et al., [2024b](https://arxiv.org/html/2406.01422v1#bib.bib50 "")) have all improved, among which RepoUnderstander performs best, further demonstrating the superior performance of RepoUnderstander.
We look forward to subsequent agent system work reporting their performance on the FIX version.

| Method | Resolved | Apply |
| --- | --- | --- |
| SWE-bench-Lite | | |
| AutoCodeRover | 16.11% (48) | 83.00% |
| RepoUnderstander | 21.33% (64) | 85.67% |
| SWE-bench-Lite-FIX | | |
| AutoCodeRover | 18.00% (54) | 84.00% |
| RepoUnderstander | 23.00% (69) | 88.00% |

Table 3. Results for RepoUnderstander performance on the SWE-bench-Lite-FIX test set.
### 4.4. Ablation Study

#### 4.4.1. Module Analysis

This ablation experiment aims to study the effectiveness of RepoUnderstander’s global repository understanding component. (1) Remove MCTS & summary modules: RepoUnderstander has no prior knowledge of the repository structure and functions, that is, it lacks empirical information about the whole repository and can only locate relevant code snippets by searching through limited information in the issue. (2) Remove only the summary module: Only the signature and dependency structure of relevant information in the repository obtained by MCTS are used as global experience, and the summary and planning of information are removed. This experiment aims to verify the effectiveness of the summary agent, i.e., the importance of comprehensive summary of repository information. (3) Add a review agent module: After RepoUnderstander generates a patch that can be applied, in order to simulate the code review process in the development process, a static review of the patch by the review agent is added to discover possible defects in the newly generated code. If there is a defect, the patch is regenerated according to the review reason until a patch that passes the review is generated. This process is repeated up to three times.

Our experimental results demonstrate the importance of global experience and the effectiveness of the summary agent. As shown in Table [4](https://arxiv.org/html/2406.01422v1#S4.T4 "Table 4 ‣ 4.4.1. Module Analysis ‣ 4.4. Ablation Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"), removing these modules all resulted in a drop in the performance of RepoUnderstander, especially after removing the MCTS & summary agent; the number of problem instances solved decreased from 64 to 48, which highlights the importance of global experience for automatically solving repository-level issues. In addition, we found that after adding the review agent, the performance of RepoUnderstander dropped, suggesting the limitations of static review. We speculate that the LLM-based static review may only rely on the surface grammatical information of the code and cannot fully understand the semantic meaning of the code. Therefore, the static review may ignore some hidden logical errors or illogical situations in the code. Therefore, we suggest that subsequent work can combine dynamic program analysis (Zhang et al., [2023a](https://arxiv.org/html/2406.01422v1#bib.bib47 ""); Deng et al., [2023](https://arxiv.org/html/2406.01422v1#bib.bib8 ""); Xia et al., [2024](https://arxiv.org/html/2406.01422v1#bib.bib42 "")) such as program instrumentation (Hollingsworth et al., [1994](https://arxiv.org/html/2406.01422v1#bib.bib15 ""); Huang, [1978](https://arxiv.org/html/2406.01422v1#bib.bib17 "")) to improve the reliability of the LLM Agent.

| Method | Resolved | Apply |
| --- | --- | --- |
| RepoUnderstander | 21.33% (64) | 85.67% |
| \- w/o. summary | 17.67% (53) | 85.33% |
| \- w/o. mcts & summary | 16.00% (48) | 80.33% |
| \- w. review | 18.33% (55) | 87.67% |

Table 4. Ablation results of RepoUnderstander.
#### 4.4.2. Hyper Parameter Analysis

We further analyzed the impact of the iterations number in MCTS. We set the maximum number of iterations to 50, 200, and 600, and limited the maximum iteration time to 300 seconds. The results are shown in Table [5](https://arxiv.org/html/2406.01422v1#S4.T5 "Table 5 ‣ 4.4.2. Hyper Parameter Analysis ‣ 4.4. Ablation Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"). We found that: (1) As the number of iterations increases, RepoUnderstander solves more actual issues. This shows that as the number of iterations rounds increases, agents will collect more repository information, i.e., they will have more experience with the repository, resulting in a higher problem solving rate; (2) As the number of iterations increases, we found that the relative improvement in problem solving gradually decreases. Specifically, the improvement of 50 iterations is significant compared to no iterations, but the relative improvement of the subsequent 200 and 600 iterations decreases. This may be because in the early stage, agents can quickly search and summarize relevant experience, but as the number of iterations increases, the convergence speed of the model gradually slows down, and the contribution of new information to performance improvement becomes smaller; (3) We observed that as the number of iterations increases from 200 to 600, the apply rate decreases. This phenomenon indicates that as the number of iterations increases, the model may be affected by some interference information when generating results, resulting in a decrease in the quality of the generated results. Therefore, when selecting the number of iterations, it is necessary to consider avoiding the influence of excessive interference information.

| Iters | Resolved | Apply |
| --- | --- | --- |
| 0 | 16.00% (48) | 80.33% |
| 50 | 19.67% (59) | 86.67% |
| 200 | 20.67% (62) | 88.00% |
| 600 | 21.33% (64) | 85.67% |

Table 5. Hyperparameter results of RepoUnderstander.https://arxiv.org/html/2406.01422v1/x5.pngFigure 5. Distribution of results in SWE-bench Lite.
### 4.5. Case Study

#### 4.5.1. Wrong Reason

Although RepoUnderstander achieved better results than other methods in the ASE task, the task is still challenging (even when RepoUnderstander and SWE-agent worked together, only 80/300 instances were fully automatically solved). To guide the optimization of subsequent work, we analyzed the specific reasons for the unsolved issues and divided the failure types into three categories: wrong location, apply patch failed, and wrong patch. Wrong location means that the agent did not locate the root cause of the problem and mistakenly modified the code in other correct locations. Apply patch failed means that the agent did not generate a syntactically correct patch and could not be directly applied to the existing version of the repository. Wrong patch means that when the bug location and patch syntax are correct, the repaired code cannot completely solve the problem, i.e., the test case does not pass completely.

We compared the results of RepoUnderstander and the current SOTA agent SWE-agent on SWE-bench Lite, as shown in the figure. The results show that: (1) In terms of bug location, our method generated patches in the wrong location in 45.0% of the tasks, while SWE-agent generated patches in 62.0%. This shows that our method performs better in correctly locating bugs, and the global experience at the repository level plays a key role in fault location. (2) In terms of patch applicability, our method did not generate patches in 13.7% of the tasks, while SWE-agent generated 5.0%. (3) In terms of patch correctness, our method generated incorrect patches in 20.0% of the tasks, while SWE-agent generated 15.0%. These indicators show that our method is more accurate in locating bug locations, but has certain weaknesses in generating correct patches and ensuring patch applicability. This may be because the execution feedback module of SWE-agent allows the agent to iteratively generate and verify the correctness of patches. This also shows the importance of execution feedback for solving practical problems. Therefore, by combining the global experience at the repository level and an effective execution feedback mechanism, we can further optimize the effect of automated software repair.

#### 4.5.2. Resolved Tasks Studyhttps://arxiv.org/html/2406.01422v1/x6.pngFigure 6. Case of django-15498. (Partial wrokflow of RepoUnderstander and SWE-agent)https://arxiv.org/html/2406.01422v1/x7.pngFigure 7. Case of matplotlib-26011. (Partial wrokflow of RepoUnderstander and SWE-agent)
To further analyze the performance of RepoUnderstander in real-world problems, we selected two examples from SWE-bench (as shown in Figures [6](https://arxiv.org/html/2406.01422v1#S4.F6 "Figure 6 ‣ 4.5.2. Resolved Tasks Study ‣ 4.5. Case Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?") and [7](https://arxiv.org/html/2406.01422v1#S4.F7 "Figure 7 ‣ 4.5.2. Resolved Tasks Study ‣ 4.5. Case Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?")) and compared them with the SOTA solution, SWE-agent. By analyzing the oracle patch, we determined the actual fault location that needs to be modified. Among them, the green highlight indicates that the agents correctly tracked the target that needs to be modified, and the yellow highlight indicates that the agents incorrectly identified the target that is not to be modified.

As shown in Figure [6](https://arxiv.org/html/2406.01422v1#S4.F6 "Figure 6 ‣ 4.5.2. Resolved Tasks Study ‣ 4.5. Case Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"), RepoUnderstander correctly explored the issue-related function to be modified was\_modified\_since in the MCTS-based Repository Exploration stage; in the subsequent summary stage, it clearly pointed out that the function needed to be updated; finally, under the guidance of global experience, the agents accurately searched and located the was\_modified\_since function in the dynamic information acquisition stage and the patch generation stage, and successfully implemented the correct modification. In contrast, in SWE-agent, agents can search for files and view file contents in a fixed window size through computer interface operations. However, due to the lack of guidance from repositroy experience knowledge, SWE-agent mistakenly located the function get\_conditional\_response in the local search. Although this function has a certain relevance to solving the issue, it is not directly related. Therefore, modifying the wrong place resulted in the failure to solve the task.

In Figure [7](https://arxiv.org/html/2406.01422v1#S4.F7 "Figure 7 ‣ 4.5.2. Resolved Tasks Study ‣ 4.5. Case Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"), we analyzed and found that solving the matplotlib-26011 task can be achieved by modifying the \_set\_lim or set\_xlim function. Both RepoUnderstander and SWE-agent correctly located the position to be modified. However, due to the running feedback and iteration capabilities of SWE-agent, the agents finally generated the correct patch through feedback information. This shows the importance of execution feedback for solving practical problems. Since RepoUnderstander and SWE-agent have certain complementarity, in the future we will combine global experience and effective execution feedback mechanism to further optimize the effect of automated software repair.

## 5\. Limitation

### 5.1. Resource Overhead.

Although RepoUnderstander aims to guide large language models to fully understand the whole software repository to effectively solve the challenges in automatic software engineering (ASE), the Monte Carlo Tree Search (MCTS) process does require a certain amount of resource consumption. Specifically, we set the maximum number of iterations to 600 and the maximum search time to 300 seconds to ensure that the model can fully explore the search space and accurately evaluate the rewards of different paths. However, such settings are controllable and adjustable to adapt to different application scenarios and resource constraints. Through reasonable parameter adjustment, the best balance between resource consumption and result accuracy can be found. In addition, as shown in Table [5](https://arxiv.org/html/2406.01422v1#S4.T5 "Table 5 ‣ 4.4.2. Hyper Parameter Analysis ‣ 4.4. Ablation Study ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"), only 50 iterations can also achieve results that are superior to other agents. Further research may discover more efficient strategies to reduce resource requirements while maintaining or improving agents performance.

### 5.2. Runtime feedback.

RepoUnderstander aims to study how to understand the entire software repository, and has emerged effective ASE capabilities through modules such as software knowledge graph construction and MCTS-enhanced repository understanding, especially in tasks such as fault location that rely on effective understanding of the entire repository knowledge. SWE-agent (Yang et al., [\[n. d.\]](https://arxiv.org/html/2406.01422v1#bib.bib44 "")) uses information such as execution feedback to assist in verifying the correctness of generated patches, and iteratively repairs patches to pass tests, which has a certain effect on improving the correctness of patch generation. In Table [2](https://arxiv.org/html/2406.01422v1#S4.T2 "Table 2 ‣ 4.2. Comparison Experiment ‣ 4. Experiment ‣ How to Understand Whole Software Repository?"), we analyze the distribution of problem solving by RepoUnderstander and SWE-agent, and find that the two methods have a certain complementarity, jointly solving 26.67% of the problems on SWE-bench Lite. Inspired by this, in the future, further combining RepoUnderstander with runtime feedback is an effective way to enhance ASE capabilities.

## 6\. Conclusion

This paper highlights the significance of understanding the whole software repository as a critical path to achieving automatic software engineering (ASE). To this end, we present a novel LLM-based agent method named RepoUnderstander, which guides agents to comprehensively understand entire repositories. Concretely, RepoUnderstander first constructs a repository knowledge graph to condense extensive and complex repository-level information into a hierarchical structure. Subsequently, we enhance the agents’ repository understanding through a Monte Carlo Tree Search (MCTS) enhanced repository exploration strategy. Finally, we guide the agents to summarize, analyze, and plan according to global experiences. Then, they can manipulate the tools to dynamically acquire information and generate patches to solve real-world GitHub issues.

We demonstrate the superior performance of RepoUnderstander through extensive experiments and comprehensive analyses. Our method achieves state-of-the-art performance on the SWE-bench Lite benchmark, outperforming existing RAG-based and agent-based systems. Furthermore, we address the issue of information asymmetry in the SWE-bench Lite dataset by proposing a FIX version that integrates new feature interface specifications into the problem description. Additionally, we conduct ablation studies to analyze the effectiveness of various components of RepoUnderstander and identify areas for further improvement. Our findings emphasize the importance of global repository experiences and the potential benefits of integrating runtime feedback mechanisms. Future work will focus on combining global experiences with runtime feedback mechanisms to further enhance the capabilities of LLM-based agents in solving complex software engineering tasks.

###### Acknowledgements.
To Robert, for the bagels and explaining CMYK and color spaces.

## References

- (1)↑
- Achiam et al. (2023)↑
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. 2023.

Gpt-4 technical report.

_arXiv preprint arXiv:2303.08774_ (2023).

- Austin et al. (2021)↑
Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, et al. 2021.

Program synthesis with large language models.

_arXiv preprint arXiv:2108.07732_ (2021).

- Bairi et al. (2023)↑
Ramakrishna Bairi, Atharv Sonwane, Aditya Kanade, Arun Iyer, Suresh Parthasarathy, Sriram Rajamani, B Ashok, Shashank Shet, et al. 2023.

Codeplan: Repository-level coding using llms and planning.

_arXiv preprint arXiv:2309.12499_ (2023).

- Carlos E. Jimenez, John Yang, Jiayi Geng (2024)↑
Carlos E. Jimenez, John Yang, Jiayi Geng. 2024.

_Introducing SWE-bench Lite_.

[https://www.swebench.com/lite.html](https://www.swebench.com/lite.html "")
- Chen et al. (2021)↑
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis,
Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. 2021.

Evaluating Large Language Models Trained on Code.

(2021).

arXiv:2107.03374 \[cs.LG\]

- Cognition (2023)↑
Cognition. 2023.

_Introducing Devin_.

[https://www.cognition.ai/introducing-devin](https://www.cognition.ai/introducing-devin "")
- Deng et al. (2023)↑
Yinlin Deng, Chunqiu Steven Xia, Haoran Peng, Chenyuan Yang, and Lingming Zhang. 2023.

Large language models are zero-shot fuzzers: Fuzzing deep-learning libraries via large language models. In _Proceedings of the 32nd ACM SIGSOFT international symposium on software testing and analysis_. 423–435.

- Ding et al. (2024a)↑
Yangruibo Ding, Marcus J Min, Gail Kaiser, and Baishakhi Ray. 2024a.

CYCLE: Learning to Self-Refine the Code Generation.

_Proceedings of the ACM on Programming Languages_ 8, OOPSLA1 (2024), 392–418.

- Ding et al. (2024b)↑
Yangruibo Ding, Zijian Wang, Wasi Ahmad, Hantian Ding, Ming Tan, Nihal Jain, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, et al. 2024b.

Crosscodeeval: A diverse and multilingual benchmark for cross-file code completion.

_Advances in Neural Information Processing Systems_ 36 (2024).

- Ding et al. (2022)↑
Yangruibo Ding, Zijian Wang, Wasi Uddin Ahmad, Murali Krishna Ramanathan, Ramesh Nallapati, Parminder Bhatia, Dan Roth, and Bing Xiang. 2022.

Cocomic: Code completion by jointly modeling in-file and cross-file context.

_arXiv preprint arXiv:2212.10007_ (2022).

- Dong et al. (2022)↑
Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong Wu, Baobao Chang, Xu Sun, Jingjing Xu, and Zhifang Sui. 2022.

A survey on in-context learning.

_arXiv preprint arXiv:2301.00234_ (2022).

- Du et al. (2024)↑
Xueying Du, Mingwei Liu, Kaixin Wang, Hanlin Wang, Junwei Liu, Yixuan Chen, Jiayi Feng, Chaofeng Sha, Xin Peng, and Yiling Lou. 2024.

Evaluating large language models in class-level code generation. In _Proceedings of the IEEE/ACM 46th International Conference on Software Engineering_. 1–13.

- Guo et al. (2024)↑
Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Y Wu, YK Li, et al. 2024.

DeepSeek-Coder: When the Large Language Model Meets Programming–The Rise of Code Intelligence.

_arXiv preprint arXiv:2401.14196_ (2024).

- Hollingsworth et al. (1994)↑
Jeffrey K Hollingsworth, Barton Paul Miller, and Jon Cargille. 1994.

Dynamic program instrumentation for scalable performance tools. In _Proceedings of IEEE Scalable High Performance Computing Conference_. IEEE, 841–850.

- Hong et al. (2023)↑
Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. 2023.

Metagpt: Meta programming for multi-agent collaborative framework.

_arXiv preprint arXiv:2308.00352_ (2023).

- Huang (1978)↑
JC Huang. 1978.

Program instrumentation and software testing.

_Computer_ 11, 4 (1978), 25–32.

- Husain et al. (2019)↑
Hamel Husain, Ho-Hsiang Wu, Tiferet Gazit, Miltiadis Allamanis, and Marc Brockschmidt. 2019.

Codesearchnet challenge: Evaluating the state of semantic code search.

_arXiv preprint arXiv:1909.09436_ (2019).

- Ishibashi and Nishimura (2024)↑
Yoichi Ishibashi and Yoshimasa Nishimura. 2024.

Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization.

_arXiv preprint arXiv:2404.02183_ (2024).

- Jimenez et al. (2024)↑
Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik R Narasimhan. 2024.

SWE-bench: Can Language Models Resolve Real-world Github Issues?. In _The Twelfth International Conference on Learning Representations_.

[https://openreview.net/forum?id=VTF8yNQM66](https://openreview.net/forum?id=VTF8yNQM66 "")
- Kocsis and Szepesvári (2006)↑
Levente Kocsis and Csaba Szepesvári. 2006.

Bandit based monte-carlo planning. In _European conference on machine learning_. Springer, 282–293.

- Kong et al. (2024)↑
Jiaolong Kong, Mingfei Cheng, Xiaofei Xie, Shangqing Liu, Xiaoning Du, and Qi Guo. 2024.

ContrastRepair: Enhancing Conversation-Based Automated Program Repair via Contrastive Test Case Pairs.

_arXiv preprint arXiv:2403.01971_ (2024).

- Krishna et al. (2018)↑
Rahul Krishna, Amritanshu Agrawal, Akond Rahman, Alexander Sobran, and Tim Menzies. 2018.

What is the connection between issues, bugs, and enhancements? Lessons learned from 800+ software projects. In _Proceedings of the 40th international conference on software engineering: Software engineering in practice_. 306–315.

- Lee et al. (2024)↑
Cheryl Lee, Chunqiu Steven Xia, Jen-tse Huang, Zhouruixin Zhu, Lingming Zhang, and Michael R Lyu. 2024.

A Unified Debugging Approach via LLM-Based Multi-Agent Synergy.

_arXiv preprint arXiv:2404.17153_ (2024).

- Liang et al. (2024)↑
Ming Liang, Xiaoheng Xie, Gehao Zhang, Xunjin Zheng, Peng Di, Hongwei Chen, Chengpeng Wang, Gang Fan, et al. 2024.

REPOFUSE: Repository-Level Code Completion with Fused Dual Context.

_arXiv preprint arXiv:2402.14323_ (2024).

- Liu et al. (2024)↑
Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, and Lingming Zhang. 2024.

Is your code generated by chatgpt really correct? rigorous evaluation of large language models for code generation.

_Advances in Neural Information Processing Systems_ 36 (2024).

- Liu et al. (2023)↑
Tianyang Liu, Canwen Xu, and Julian McAuley. 2023.

Repobench: Benchmarking repository-level code auto-completion systems.

_arXiv preprint arXiv:2306.03091_ (2023).

- Lozhkov et al. (2024)↑
Anton Lozhkov, Raymond Li, Loubna Ben Allal, Federico Cassano, Joel Lamy-Poirier, Nouamane Tazi, Ao Tang, Dmytro Pykhtar, Jiawei Liu, Yuxiang Wei, et al. 2024.

StarCoder 2 and The Stack v2: The Next Generation.

_arXiv preprint arXiv:2402.19173_ (2024).

- Lu et al. (2021)↑
Shuai Lu, Daya Guo, Shuo Ren, Junjie Huang, Alexey Svyatkovskiy, Ambrosio Blanco, Colin Clement, Dawn Drain, Daxin Jiang, Duyu Tang, et al. 2021.

Codexglue: A machine learning benchmark dataset for code understanding and generation.

_arXiv preprint arXiv:2102.04664_ (2021).

- Luo et al. (2024)↑
Qinyu Luo, Yining Ye, Shihao Liang, Zhong Zhang, Yujia Qin, Yaxi Lu, Yesai Wu, Xin Cong, Yankai Lin, Yingli Zhang, et al. 2024.

RepoAgent: An LLM-Powered Open-Source Framework for Repository-level Code Documentation Generation.

_arXiv preprint arXiv:2402.16667_ (2024).

- Merten et al. (2016)↑
Thorsten Merten, Matúš Falis, Paul Hübner, Thomas Quirchmayr, Simone Bürsner, and Barbara Paech. 2016.

Software feature request detection in issue tracking systems. In _2016 IEEE 24th international requirements engineering conference (RE)_. IEEE, 166–175.

- Moran Altarac (2024)↑
Moran Altarac. 2024.

_Mastering Bug Reporting and Feedback Collection: A Comprehensive Guide_.

[https://www.guidde.com/blog/mastering-bug-reporting-and-feedback-collection-a-comprehensive-guide](https://www.guidde.com/blog/mastering-bug-reporting-and-feedback-collection-a-comprehensive-guide "")
- OpenDevin (2023)↑
OpenDevin. 2023.

_OpenDevin_.

[https://github.com/OpenDevin/OpenDevin](https://github.com/OpenDevin/OpenDevin "")
- Qin et al. (2024)↑
Yihao Qin, Shangwen Wang, Yiling Lou, Jinhao Dong, Kaixin Wang, Xiaoling Li, and Xiaoguang Mao. 2024.

AgentFL: Scaling LLM-based Fault Localization to Project-Level Context.

_arXiv preprint arXiv:2403.16362_ (2024).

- Rasheed et al. (2024)↑
Zeeshan Rasheed, Muhammad Waseem, Mika Saari, Kari Systä, and Pekka Abrahamsson. 2024.

Codepori: Large scale model for autonomous software development by using multi-agents.

_arXiv preprint arXiv:2402.01411_ (2024).

- Shrivastava et al. (2023)↑
Disha Shrivastava, Hugo Larochelle, and Daniel Tarlow. 2023.

Repository-level prompt generation for large language models of code. In _International Conference on Machine Learning_. PMLR, 31693–31715.

- Tang et al. (2024)↑
Daniel Tang, Zhenghan Chen, Kisub Kim, Yewei Song, Haoye Tian, Saad Ezzini, Yongfeng Huang, and Jacques Klein Tegawende F Bissyande. 2024.

Collaborative agents for software engineering.

_arXiv preprint arXiv:2402.02172_ (2024).

- Wang et al. (2024)↑
Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji. 2024.

Executable Code Actions Elicit Better LLM Agents.

arXiv:2402.01030 \[cs.CL\]

- Wei et al. (2022)↑
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022.

Chain-of-thought prompting elicits reasoning in large language models.

_Advances in neural information processing systems_ 35 (2022), 24824–24837.

- wiki koha (2024)↑
wiki koha. 2024.

_Bug Reporting Guidelines_.

[https://wiki.koha-community.org/wiki/Bug\_Reporting\_Guidelines](https://wiki.koha-community.org/wiki/Bug_Reporting_Guidelines "")
- Work (\[n. d.\])↑
What Makes In-Context Learning Work. \[n. d.\].

Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?

(\[n. d.\]).

- Xia et al. (2024)↑
Chunqiu Steven Xia, Matteo Paltenghi, Jia Le Tian, Michael Pradel, and Lingming Zhang. 2024.

Fuzz4all: Universal fuzzing with large language models. In _Proceedings of the IEEE/ACM 46th International Conference on Software Engineering_. 1–13.

- Xie et al. (2023)↑
Yutao Xie, Jiayi Lin, Hande Dong, Lei Zhang, and Zhonghai Wu. 2023.

Survey of code search based on deep learning.

_ACM Transactions on Software Engineering and Methodology_ 33, 2 (2023), 1–42.

- Yang et al. (\[n. d.\])↑
John Yang, Carlos E Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. \[n. d.\].

SWE-AGENT: AGENT-COMPUTER INTERFACES ENABLE AUTOMATED SOFTWARE ENGINEERING.

(\[n. d.\]).

- Yao et al. (2022)↑
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2022.

React: Synergizing reasoning and acting in language models.

_arXiv preprint arXiv:2210.03629_ (2022).

- Zan et al. (2023)↑
Daoguang Zan, Bei Chen, Yongshun Gong, Junzhi Cao, Fengji Zhang, Bingchao Wu, Bei Guan, Yilong Yin, and Yongji Wang. 2023.

Private-library-oriented code generation with large language models.

_arXiv preprint arXiv:2307.15370_ (2023).

- Zhang et al. (2023a)↑
Cen Zhang, Mingqiang Bai, Yaowen Zheng, Yeting Li, Xiaofei Xie, Yuekang Li, Wei Ma, Limin Sun, and Yang Liu. 2023a.

Understanding large language model based fuzz driver generation.

_arXiv preprint arXiv:2307.12469_ (2023).

- Zhang et al. (2023b)↑
Fengji Zhang, Bei Chen, Yue Zhang, Jacky Keung, Jin Liu, Daoguang Zan, Yi Mao, Jian-Guang Lou, and Weizhu Chen. 2023b.

Repocoder: Repository-level code completion through iterative retrieval and generation.

_arXiv preprint arXiv:2303.12570_ (2023).

- Zhang et al. (2024a)↑
Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. 2024a.

CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges.

_arXiv preprint arXiv:2401.07339_ (2024).

- Zhang et al. (2024b)↑
Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, and Abhik Roychoudhury. 2024b.

AutoCodeRover: Autonomous Program Improvement.

_arXiv preprint arXiv:2404.05427_ (2024).

- Zheng et al. (2023)↑
Qinkai Zheng, Xiao Xia, Xu Zou, Yuxiao Dong, Shan Wang, Yufei Xue, Lei Shen, Zihan Wang, Andi Wang, Yang Li, et al. 2023.

Codegeex: A pre-trained model for code generation with multilingual benchmarking on humaneval-x. In _Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_. 5673–5684.

</details>

<details>
<summary>Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning</summary>

# Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning

Recent studies show that in supervised fine-tuning (SFT) of large language models (LLMs), data quality matters more than quantity.
While most data cleaning methods concentrate on filtering entire samples, the quality of individual tokens within a sample can vary significantly. After pre-training, even in high-quality samples, patterns or phrases that are not task-related can be redundant or uninformative. Continuing to fine-tune on these patterns may offer limited benefit and even degrade downstream task performance.
In this paper, we investigate token quality from a noisy-label perspective and propose a generic _token cleaning_ pipeline for SFT tasks. Our method filters out uninformative tokens while preserving those carrying key task-specific information. Specifically, we first evaluate token quality by examining the influence of model updates on each token, then apply a threshold-based separation. The token influence can be measured in a single pass with a fixed reference model or iteratively with self-evolving reference models. The benefits and limitations of both methods are analyzed theoretically by error upper bounds. Extensive experiments show that our framework consistently improves performance across multiple downstream tasks.

## 1 Introduction

Supervised fine-tuning (SFT) has served as a widely adopted approach and a fundamental step in aligning large language models (LLMs) with human expectations. This process ensures that LLMs can accurately understand human instructions and produce relevant responses. In practice, SFT involves fine-tuning pre-trained models using annotated instructional data (Touvron et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib1 "")). Following general data scaling laws (Zhang et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib2 "")), significant efforts have been dedicated to collecting large-scale instructional data containing millions of examples (Wang et al., [2022](https://arxiv.org/html/2502.01968v1#bib.bib3 ""); Chung et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib4 ""); Longpre et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib5 "")).

Recent studies on the SFT have widely agreed that data quality matters far more than quantity (Zhou et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib6 ""); Chen et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib7 ""); Pang et al., [2024a](https://arxiv.org/html/2502.01968v1#bib.bib8 ""); Liu et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib9 "")). That is, a small, well-curated dataset can often deliver effective or even superior performance on downstream tasks, highlighting the critical role of data cleaning or selection.
Existing data cleaning approaches primarily emphasize identifying high-quality samples in large dataset pools via some metrics, including perplexity (Cao et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib10 "")), completion length (Zhao et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib11 "")), confidence scores (Chen and Mueller, [2024](https://arxiv.org/html/2502.01968v1#bib.bib12 ""))), LLM-generated quality ratings (Chen et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib7 ""); Pang et al., [2024a](https://arxiv.org/html/2502.01968v1#bib.bib8 ""); Liu et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib9 "")) or even costly human annotations (Zhou et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib6 "")).
Although these methods have proven effective, focusing solely on sample-level cleaning may overlook complexities within each sample.

In practice, each sample typically contains hundreds of tokens, some of which occur frequently regardless of the sample’s quality. These common tokens/patterns can overshadow task-specific words that are crucial for model performance during training. Moreover, during interference, if the model continually outputs these frequent tokens, it may neglect more informative ones, producing outputs that appear correct yet fail to address specific tasks. Thus, even well-curated samples can contain token-level noise that dilutes essential signals. Addressing these token-level issues by removing or down-weighting uninformative tokens can help the model prioritize important content and improve downstream results.

In this paper, we go beyond traditional sample-level data cleaning by proposing a generic _token cleaning_ pipeline and an analytical framework for LLM SFT tasks. Specifically, we filter out uninformative tokens while retaining those with meaningful task-specific information.
This is achieved by first assessing token quality using an influence-guided scoring mechanism, followed by threshold-based separation.https://arxiv.org/html/2502.01968v1/x1.pngFigure 1: Token cleaning pipelines. Fixed-Model Cleaning applies a one-shot cleaning process to the entire dataset D~~𝐷\\widetilde{D}over~ start\_ARG italic\_D end\_ARG. In contrast, Self-Evolving Cleaning follows an iterative approach. It begins with a warm-up phase, where a model is fine-tuned on the full tokens of split-00, denoted as D~0subscript~𝐷0\\widetilde{D}\_{0}over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, and then used to clean the next data split, transforming D~1subscript~𝐷1\\widetilde{D}\_{1}over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT into D^1subscript^𝐷1\\widehat{D}\_{1}over^ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT. The reference model is subsequently updated by fine-tuning the warm-up model (i.e., the first reference model) on D^1subscript^𝐷1\\widehat{D}\_{1}over^ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT. This iterative process continues, progressively refining the reference model with each newly cleaned data split.

Figure [1](https://arxiv.org/html/2502.01968v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") illustrates two scoring strategies supported by our token cleaning pipeline. The high-level idea is to evaluate the influence of model updates on each token, which can be calculated by the loss disparity between a base model and a reference model. We introduce two implementations:

- ∙∙\\bullet∙

Fix-Model Cleaning.
In this strategy, both the base model and the reference model remain fixed, and a one-shot token cleaning is applied to the entire SFT dataset. The base model is then fine-tuned on the cleaned tokens, producing the final model output. This strategy is similar to the latest token selection method for pre-trained data Lin et al. ( [2024](https://arxiv.org/html/2502.01968v1#bib.bib13 "")). We defer detailed comparisons to Section [4.3.1](https://arxiv.org/html/2502.01968v1#S4.SS3.SSS1 "4.3.1 Fixed-Model Cleaning ‣ 4.3 Selection of 𝜃 and 𝜃' ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") (analytical) and Section [6](https://arxiv.org/html/2502.01968v1#S6 "6 Experiments ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") (experimental).

- ∙∙\\bullet∙

Self-Evolving Cleaning.
In this strategy, the base model remains fixed while the reference model is updated iteratively. The data is divided into multiple parts, with each iteration cleaning one part. The reference model is then updated sequentially using the cleaned results from each part. Unlike the fix-model cleaning, the final model output is the reference model obtained in the last iteration.

Our main contributions can be summarized as follows.

- ∙∙\\bullet∙

Generic Token Cleaning Pipeline. We formulate the problem from the perspective of noisy labels and present a novel influence-guided token cleaning pipeline that scores and filters out uninformative tokens, enhancing downstream task performance by focusing model training on the most relevant tokens. The pipeline not only encompasses existing approaches but also inspires new implementations.

- ∙∙\\bullet∙

Self-Envolving Cleaning.
Beyond merely calculating the influence scores with a pair of fixed models, we propose to update the reference model iteratively, which could progressively enhance the quality of supervision signals, leading to better downstream performance.

- ∙∙\\bullet∙

Analytical Framework. We provide rigorous analyses to demonstrate when and why SFT with the cleaned token outperforms the full tokens. Specifically, we establish an upper bound on the error incurred when learning with full tokens (Theorem [5.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1 "Theorem 5.1 (Error of learning with full tokens). ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning")), offering theoretical insights into the trade-offs of different cleaning strategies. Our analysis explains why fix-model cleaning yields stable but limited improvements, while self-evolving cleaning shows greater potential but requires careful implementation.

- ∙∙\\bullet∙

Comprehensive Experiments. We conduct extensive experiments across multiple tasks, demonstrating that our token cleaning pipeline consistently boosts performance over baselines and validates the practical merits of our work.

## 2 Related Work

##### LLM Data Selection

In the LLM SFT phase, various metrics have been introduced to assess data quality including completion length (Zhao et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib11 "")), perplexity (Cao et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib10 "")), reward scores (Gou and Nguyen, [2024](https://arxiv.org/html/2502.01968v1#bib.bib14 "")), discrete confidence scores (Chen and Mueller, [2024](https://arxiv.org/html/2502.01968v1#bib.bib12 "")), the loss disparities when certain examples are included or excluded (Li et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib15 "")), gradient matching (Zhou et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib16 "")) and influence function scores (Xia et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib17 "")).
Another line of work uses advanced LLMs directly to filter out low-quality samples according to different metrics, such as quality-based rating scores  (Chen et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib7 ""); Liu et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib9 ""); Pang et al., [2024a](https://arxiv.org/html/2502.01968v1#bib.bib8 "")) and fine-grained tags (Lu et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib18 "")). Diversity-aware scoring has also been integrated into the overall quality assessment, highlighting its importance.
Although extensive data selection methods have shown promise, fine-grained token-level selection remains underexplored. Recent studies (Lin et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib13 "")) have highlighted the significant benefits of token selection during the pre-training phase, yet its application in the SFT phase has received limited attention.

##### Noisy Data Cleaning

The learning with noisy labels has been extensively studied (Vahdat, [2017](https://arxiv.org/html/2502.01968v1#bib.bib19 ""); Veit et al., [2017](https://arxiv.org/html/2502.01968v1#bib.bib20 ""); Li et al., [2017](https://arxiv.org/html/2502.01968v1#bib.bib21 ""); Liu and Wang, [2021](https://arxiv.org/html/2502.01968v1#bib.bib22 ""); Yuan et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib23 "")). Various approaches have been proposed to mitigate label errors, including developing noise-tolerant loss functions (Natarajan et al., [2013](https://arxiv.org/html/2502.01968v1#bib.bib24 ""); Reed et al., [2014](https://arxiv.org/html/2502.01968v1#bib.bib25 ""); Zhu et al., [2021](https://arxiv.org/html/2502.01968v1#bib.bib26 "")) and identifying clean samples while re-labeling corrupted ones (Northcutt et al., [2021](https://arxiv.org/html/2502.01968v1#bib.bib27 ""), [2017](https://arxiv.org/html/2502.01968v1#bib.bib28 ""); Cheng et al., [2021](https://arxiv.org/html/2502.01968v1#bib.bib29 ""); Zhu et al., [2022](https://arxiv.org/html/2502.01968v1#bib.bib30 "")).
Recently, the issue of noisy labels in LLM alignment has gained increasing attention, driven by the observation that data quality is far more critical than quantity (Zhou et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib6 "")). Recent work (Chong et al., [2022](https://arxiv.org/html/2502.01968v1#bib.bib31 "")) investigated the effectiveness of leveraging pre-trained models to identify inherent label errors in natural language datasets. Additionally, efforts have been made to mitigate label errors in LLM alignment datasets (Zhu et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib32 "")), particularly in the context of binary harmlessness classification. Furthermore, Pang et al. ( [2024a](https://arxiv.org/html/2502.01968v1#bib.bib8 "")) systematically analyzed error patterns in LLM-generated quality rating scores to reduce score errors. Another line of research has focused on developing noise-tolerant DPO-based loss functions, including cDPO ( [Mitchell,](https://arxiv.org/html/2502.01968v1#bib.bib33 "")), robust-DPO (Chowdhury et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib34 "")), and PerpCorrect ( [Kong et al.,](https://arxiv.org/html/2502.01968v1#bib.bib35 "")).
The above studies primarily focus on noisy labels at the sample level. In contrast, our work explores fine-grained, token-level noisy labels to identify and filter out uninformative tokens, thereby boosting downstream task performance.

## 3 Preliminary

### 3.1 Next-Token Prediction

Consider a data pool comprising N𝑁Nitalic\_N samples, denoted as {𝒙i}i=1Nsuperscriptsubscriptsubscript𝒙𝑖𝑖1𝑁\\{\\bm{x}\_{i}\\}\_{i=1}^{N}{ bold\_italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT } start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT. Each sample 𝒙isubscript𝒙𝑖\\bm{x}\_{i}bold\_italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT represents a sequence of tokens (including the prompt and the response) defined as 𝒙i:={xi,j}j=1Liassignsubscript𝒙𝑖superscriptsubscriptsubscript𝑥𝑖𝑗𝑗1subscript𝐿𝑖\\bm{x}\_{i}:=\\{x\_{i,j}\\}\_{j=1}^{L\_{i}}bold\_italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT := { italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT } start\_POSTSUBSCRIPT italic\_j = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_L start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT, where Lisubscript𝐿𝑖L\_{i}italic\_L start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT denotes the token length for the i𝑖iitalic\_i-th sample.
The training of LLMs can be framed as minimizing the negative log-likelihood of the observed tokens in the dataset. The model predicts the conditional probability ℙ⁢(xi,j\|𝒙i,:j;θ)ℙconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃\\mathbb{P}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta)blackboard\_P ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ ) for each token xi,jsubscript𝑥𝑖𝑗x\_{i,j}italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT given its preceding context, where θ𝜃\\thetaitalic\_θ represents the model parameters, and 𝒙i,:jsubscript𝒙𝑖:absent𝑗\\bm{x}\_{i,:j}bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT denotes the first j−1𝑗1j-1italic\_j - 1 tokens, i.e., {xi,1,⋯,xi,j−1}subscript𝑥𝑖1⋯subscript𝑥𝑖𝑗1\\{x\_{i,1},\\cdots,x\_{i,j-1}\\}{ italic\_x start\_POSTSUBSCRIPT italic\_i , 1 end\_POSTSUBSCRIPT , ⋯ , italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j - 1 end\_POSTSUBSCRIPT }.
Denote by

|     |     |     |
| --- | --- | --- |
|  | D:={(xi,j,𝒙i,:j,yi,j),∀(i,j)∈S},assign𝐷subscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗subscript𝑦𝑖𝑗for-all𝑖𝑗𝑆D:=\\{(x\_{i,j},\\bm{x}\_{i,:j},y\_{i,j}),\\forall(i,j)\\in S\\},italic\_D := { ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT , bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT , italic\_y start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT ) , ∀ ( italic\_i , italic\_j ) ∈ italic\_S } , |  |

where

|     |     |     |
| --- | --- | --- |
|  | S:={(i,j)\|i∈\[N\],j∈\[Li\]},\[N\]:={1,2,⋯,N}.formulae-sequenceassign𝑆conditional-set𝑖𝑗formulae-sequence𝑖delimited-\[\]𝑁𝑗delimited-\[\]subscript𝐿𝑖assigndelimited-\[\]𝑁12⋯𝑁S:=\\{(i,j)\|i\\in\[N\],j\\in\[L\_{i}\]\\},\[N\]:=\\{1,2,\\cdots,N\\}.italic\_S := { ( italic\_i , italic\_j ) \| italic\_i ∈ \[ italic\_N \] , italic\_j ∈ \[ italic\_L start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT \] } , \[ italic\_N \] := { 1 , 2 , ⋯ , italic\_N } . |  |

The loss function for the dataset can be expressed as:

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒ^D⁢(θ)=1∑(i,j)∈Syi,j⁢∑(i,j)∈Syi,j⁢ℓ⁢(xi,j\|𝒙i,:j;θ),subscript^ℒ𝐷𝜃1subscript𝑖𝑗𝑆subscript𝑦𝑖𝑗subscript𝑖𝑗𝑆subscript𝑦𝑖𝑗ℓconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃\\widehat{\\mathcal{L}}\_{D}(\\theta)=\\frac{1}{\\sum\_{(i,j)\\in S}y\_{i,j}}\\sum\_{(i,j%<br>)\\in S}y\_{i,j}\\ell(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta),over^ start\_ARG caligraphic\_L end\_ARG start\_POSTSUBSCRIPT italic\_D end\_POSTSUBSCRIPT ( italic\_θ ) = divide start\_ARG 1 end\_ARG start\_ARG ∑ start\_POSTSUBSCRIPT ( italic\_i , italic\_j ) ∈ italic\_S end\_POSTSUBSCRIPT italic\_y start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT end\_ARG ∑ start\_POSTSUBSCRIPT ( italic\_i , italic\_j ) ∈ italic\_S end\_POSTSUBSCRIPT italic\_y start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT roman\_ℓ ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ ) , |  | (1) |

where ℓ⁢(xi,j\|𝒙i,:j;θ):=−log⁡ℙ⁢(xi,j\|𝒙i,:j;θ)assignℓconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃ℙconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃\\ell(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta):=-\\log\\mathbb{P}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta)roman\_ℓ ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ ) := - roman\_log blackboard\_P ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ ), and yi,j∈{0,1}subscript𝑦𝑖𝑗01y\_{i,j}\\in\\{0,1\\}italic\_y start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT ∈ { 0 , 1 } is a binary (ground-truth) label indicating whether the token xi,jsubscript𝑥𝑖𝑗x\_{i,j}italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT is a valid target or not.
By iteratively updating θ𝜃\\thetaitalic\_θ, the model learns to assign higher probabilities to the correct tokens while disregarding irrelevant ones.

### 3.2 Token-Level Labels

Token-level labels yi,j∈{0,1}subscript𝑦𝑖𝑗01y\_{i,j}\\in\\{0,1\\}italic\_y start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT ∈ { 0 , 1 } play a crucial role in determining which tokens contribute to the loss calculation. However, its ground-truth value is often unknown. Denote y~i,jsubscript~𝑦𝑖𝑗\\tilde{y}\_{i,j}over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT by the (noisy) token label that we use in practice, which may or may not be identical to yi,jsubscript𝑦𝑖𝑗y\_{i,j}italic\_y start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT. During different training phases, the criteria for setting y~i,jsubscript~𝑦𝑖𝑗\\tilde{y}\_{i,j}over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT may vary:

- •

Model Pretraining: When training on general text data without explicit distinction between prompts and responses, all tokens are typically considered valid targets (y~i,j=1subscript~𝑦𝑖𝑗1\\tilde{y}\_{i,j}=1over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT = 1), unless specific tokens are identified as irrelevant or redundant (Lin et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib13 "")).

- •

Supervised Fine-tuning (SFT): In this phase, the tokens corresponding to the prompt part are ignored, as they do not represent the model’s predictions. Therefore, for prompt tokens, y~i,j=0subscript~𝑦𝑖𝑗0\\tilde{y}\_{i,j}=0over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT = 0, and for response tokens, y~i,j=1subscript~𝑦𝑖𝑗1\\tilde{y}\_{i,j}=1over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT = 1.

## 4 Token Cleaning: A Noisy Label Perspective

### 4.1 Intuition

In the phase of SFT, some tokens are deemed uninformative or redundant since most of the knowledge has been obtained in the pretraining phase, e.g., common patterns and structures, high-frequency phrases. In practice, the SFT phase assigns a label of 1111 to every token in the response, resulting in noisy token labels, where irrelevant tokens are incorrectly labeled as important (y~i,j=1subscript~𝑦𝑖𝑗1\\tilde{y}\_{i,j}=1over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT = 1). Such noise can hinder the model’s optimization process by introducing misleading gradients, reducing the signal-to-noise ratio by hiding informative tokens, and potentially leading to suboptimal performance.

To address this issue, it is essential to perform fine-grained token label cleaning. This involves identifying and filtering out uninformative tokens while preserving the tokens that carry valuable task-specific information. As suggested by the noisy label literature Zhu et al. ( [2022](https://arxiv.org/html/2502.01968v1#bib.bib30 ""), [2024](https://arxiv.org/html/2502.01968v1#bib.bib32 "")), the cleaning process typically involves two key components: a scoring function to assess the quality of each token and a threshold to distinguish between informative and uninformative tokens, which will be detailed in the next subsection.

### 4.2 Token Cleaning Pipeline

In this section, we will introduce the main components of the token-cleaning pipeline, including the scoring function and a simple yet effective threshold.

#### 4.2.1 Score Functions: An Influence-Guided Approach

We deliver our intuition when designing score functions using the following example.
Suppose that the model is improved from θ𝜃\\thetaitalic\_θ to θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT by fine-tuning it on some data.
According to Koh and Liang ( [2017](https://arxiv.org/html/2502.01968v1#bib.bib36 "")); Pang et al. ( [2024b](https://arxiv.org/html/2502.01968v1#bib.bib37 "")), the model update influences the prediction accuracy of each token, which can be written as

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  |  | Infl⁢(xi,j\|𝒙i,:j;θ,θ′):=ℓ⁢(xi,j\|𝒙i,:j;θ′)−ℓ⁢(xi,j\|𝒙i,:j;θ).assignsubscriptInflconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃superscript𝜃′ℓconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗superscript𝜃′ℓconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃\\displaystyle\\textsf{Infl}\_{\\textsf{\ }}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta,\\theta^{%<br>\\prime}):=\\ell(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta^{\\prime})-\\ell(x\_{i,j}\|\\bm{x}\_{i,:%<br>j};\\theta).Infl start\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ , italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) := roman\_ℓ ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) - roman\_ℓ ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ ) . |  | (2) |

Intuitively, a more negative Infl⁢(xi,j\|𝒙i,:j;θ,θ′)subscriptInflconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃superscript𝜃′\\textsf{Infl}\_{\\textsf{\ }}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta,\\theta^{\\prime})Infl start\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ , italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) indicates a higher confidence improvement on predicting xi,jsubscript𝑥𝑖𝑗x\_{i,j}italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT given 𝒙i,:jsubscript𝒙𝑖:absent𝑗\\bm{x}\_{i,:j}bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT. The equation can be explained from two perspectives:

- •

Assume Token Quality: As demonstrated by Pang et al. ( [2024b](https://arxiv.org/html/2502.01968v1#bib.bib37 "")), if we believe that token xi,jsubscript𝑥𝑖𝑗x\_{i,j}italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT is the best choice given context xi,:jsubscript𝑥𝑖:absent𝑗x\_{i,:j}italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT, the above influence can be used to evaluate the quality of data that brings the model from θ𝜃\\thetaitalic\_θ to θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT on this specific task, i.e, a more negative Infl⁢(xi,j\|𝒙i,:j;θ,θ′)subscriptInflconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃superscript𝜃′\\textsf{Infl}\_{\\textsf{\ }}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta,\\theta^{\\prime})Infl start\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ , italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) indicates a higher data quality.

- •

Assume Model Quality: From another perspective, if we believe the model θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT performs better on θ𝜃\\thetaitalic\_θ on this specific task, the above influence can be used to evaluate the quality of token xi,jsubscript𝑥𝑖𝑗x\_{i,j}italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT since a good and underfitted choice of xi,jsubscript𝑥𝑖𝑗x\_{i,j}italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT tends to have a negative Infl⁢(xi,j\|𝒙i,:j;θ,θ′)subscriptInflconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃superscript𝜃′\\textsf{Infl}\_{\\textsf{\ }}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta,\\theta^{\\prime})Infl start\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ , italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ).

In this paper, we assume the model quality and use the negative of the influence defined in Eq. ( [2](https://arxiv.org/html/2502.01968v1#S4.E2 "In 4.2.1 Score Functions: An Influence-Guided Approach ‣ 4.2 Token Cleaning Pipeline ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning")) to evaluate the quality of tokens, i.e.,

|     |     |     |     |
| --- | --- | --- | --- |
|  | Score⁢(xi,j\|𝒙i,:j;θ,θ′)=−Infl⁢(xi,j\|𝒙i,:j;θ,θ′),Scoreconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃superscript𝜃′subscriptInflconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃superscript𝜃′\\textsf{Score}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta,\\theta^{\\prime})=-\\textsf{Infl}\_{%<br>\\textsf{\ }}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta,\\theta^{\\prime}),Score ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ , italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) = - Infl start\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ , italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) , |  | (3) |

where a higher score indicates a higher token quality.

Extending from the current use of influences Koh and Liang ( [2017](https://arxiv.org/html/2502.01968v1#bib.bib36 "")); Pang et al. ( [2024b](https://arxiv.org/html/2502.01968v1#bib.bib37 "")), we notice that θ𝜃\\thetaitalic\_θ and θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT are not necessarily to be the same model structure, as long as they share the same tokenizer. We will discuss potential choices of θ𝜃\\thetaitalic\_θ and θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT in Section [4.3](https://arxiv.org/html/2502.01968v1#S4.SS3 "4.3 Selection of 𝜃 and 𝜃' ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning").

#### 4.2.2 Threshold

After computing token scores, a threshold is applied to filter out corrupted or uninformative tokens. The threshold separates the tokens that significantly improve the model performance from those that do not. An ideal approach is to use algorithms to estimate the ratio of the corrupted and then select the informative tokens according to the ratio. However, although there are lots of trials in the literature on noisy labels, most works focus on cleaning the image labels Lad and Mueller ( [2023](https://arxiv.org/html/2502.01968v1#bib.bib38 "")) or sample-level text labels Zhu et al. ( [2024](https://arxiv.org/html/2502.01968v1#bib.bib32 "")); Pang et al. ( [2024a](https://arxiv.org/html/2502.01968v1#bib.bib8 "")). To the best of our knowledge, a feasible algorithm for estimating the noise ratio of token labels is unclear, which is beyond the scope of our paper and left for future explorations. In this paper, we use a fixed ratio (i.e., selected token proportion) k%percent𝑘k\\%italic\_k % to separate between information and uninformative tokens. Denote by y^i,jsubscript^𝑦𝑖𝑗\\hat{y}\_{i,j}over^ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT the token label after cleaning. We have

|     |     |     |     |
| --- | --- | --- | --- |
|  | y^i,j={1if Score⁢(xi,j\|𝒙i,:j;θ,θ′)⁢ ranks top ⁢k%,∀i,j;0otherwise.subscript^𝑦𝑖𝑗cases1if Scoreconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗𝜃superscript𝜃′ ranks top percent𝑘for-all𝑖𝑗0otherwise\\displaystyle\\hat{y}\_{i,j}=\\begin{cases}1&\\text{if }\\textsf{Score}(x\_{i,j}\|\\bm%<br>{x}\_{i,:j};\\theta,\\theta^{\\prime})\\text{ ranks top }k\\%,\\forall i,j;\\\<br>0&\\text{otherwise}.\\vspace{-10pt}\\end{cases}over^ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT = { start\_ROW start\_CELL 1 end\_CELL start\_CELL if sansserif\_Score ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ , italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) ranks top italic\_k % , ∀ italic\_i , italic\_j ; end\_CELL end\_ROW start\_ROW start\_CELL 0 end\_CELL start\_CELL otherwise . end\_CELL end\_ROW |  | (4) |

### 4.3 Selection of θ𝜃\\thetaitalic\_θ and θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT

We discuss two feasible strategies for selecting θ𝜃\\thetaitalic\_θ and θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT.

#### 4.3.1 Fixed-Model Cleaning

Following the analyses in Section [4.2.1](https://arxiv.org/html/2502.01968v1#S4.SS2.SSS1 "4.2.1 Score Functions: An Influence-Guided Approach ‣ 4.2 Token Cleaning Pipeline ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"), we can assume the access to a model θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT that outperforms θ𝜃\\thetaitalic\_θ. For example, a moderately performing Llama model can be considered as θ𝜃\\thetaitalic\_θ, while a well-performing Llama model can be considered as θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPTMindermann et al. ( [2022](https://arxiv.org/html/2502.01968v1#bib.bib39 "")); Lin et al. ( [2024](https://arxiv.org/html/2502.01968v1#bib.bib13 "")).
Specifically, given the warm-up model θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT and the base model θ𝜃\\thetaitalic\_θ, we compute the token scores for the entire dataset D~~𝐷\\widetilde{D}over~ start\_ARG italic\_D end\_ARG according to Eq. ( [3](https://arxiv.org/html/2502.01968v1#S4.E3 "In 4.2.1 Score Functions: An Influence-Guided Approach ‣ 4.2 Token Cleaning Pipeline ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning")) and use a fixed threshold kfixedsubscript𝑘fixedk\_{\\text{fixed}}italic\_k start\_POSTSUBSCRIPT fixed end\_POSTSUBSCRIPT to assign token labels y~i,jsubscript~𝑦𝑖𝑗\\tilde{y}\_{i,j}over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT according to Eq. ( [4](https://arxiv.org/html/2502.01968v1#S4.E4 "In 4.2.2 Threshold ‣ 4.2 Token Cleaning Pipeline ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning")).
Note that token cleaning is performed globally, meaning that some samples may be entirely removed if they contain no positive tokens. This differs from Lin et al. ( [2024](https://arxiv.org/html/2502.01968v1#bib.bib13 "")), where each sample retains a fixed proportion of positive tokens.
The benefits and limitations of this strategy will be discussed theoretically in Section [5.2](https://arxiv.org/html/2502.01968v1#S5.SS2 "5.2 Fixed-Model Cleaning: Stable But Limited Improvement ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning").

#### 4.3.2 Self-Evolving Cleaning

Inspired by the success of semi-supervised learning (SSL), we propose to do token cleaning iteratively. Specifically, in the t𝑡titalic\_t-th iteration, we fix the base model θ𝜃\\thetaitalic\_θ and adopt θ′=θtsuperscript𝜃′subscript𝜃𝑡\\theta^{\\prime}=\\theta\_{t}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT = italic\_θ start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT, then fine-tune θtsubscript𝜃𝑡\\theta\_{t}italic\_θ start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT with the selected tokens after cleaning.
See Algorithm [1](https://arxiv.org/html/2502.01968v1#alg1 "Algorithm 1 ‣ 4.3.2 Self-Evolving Cleaning ‣ 4.3 Selection of 𝜃 and 𝜃' ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") for more details.

Algorithm 1 Token Cleaning Pipeline

1:Input: Entire dataset D~~𝐷\\widetilde{D}over~ start\_ARG italic\_D end\_ARG, base model θ0subscript𝜃0\\theta\_{0}italic\_θ start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, threshold kself-evol.subscript𝑘self-evolk\_{\\text{self-evol}}.italic\_k start\_POSTSUBSCRIPT self-evol end\_POSTSUBSCRIPT .

2:  Split dataset D~~𝐷\\widetilde{D}over~ start\_ARG italic\_D end\_ARG into a series of subset {D~0,⋯,D~T}subscript~𝐷0⋯subscript~𝐷𝑇\\{\\widetilde{D}\_{0},\\cdots,\\widetilde{D}\_{T}\\}{ over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT , ⋯ , over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT italic\_T end\_POSTSUBSCRIPT }. Denote their indices by {S0,⋯,ST}subscript𝑆0⋯subscript𝑆𝑇\\{S\_{0},\\cdots,S\_{T}\\}{ italic\_S start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT , ⋯ , italic\_S start\_POSTSUBSCRIPT italic\_T end\_POSTSUBSCRIPT }.

3:Warmup Modelθ1subscript𝜃1\\theta\_{1}italic\_θ start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT: Finetune from base model θ0subscript𝜃0\\theta\_{0}italic\_θ start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT on D~0subscript~𝐷0\\widetilde{D}\_{0}over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT subset with all tokens.

4:fort𝑡titalic\_tin{1,2,⋯,T}12⋯𝑇\\{1,2,\\cdots,T\\}{ 1 , 2 , ⋯ , italic\_T }do

5:     Compute scores for subset D~tsubscript~𝐷𝑡\\widetilde{D}\_{t}over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT’s tokens via Score⁢(xi,j\|𝒙i,:j;θt−1,θt),∀xi,j∈D~tScoreconditionalsubscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗subscript𝜃𝑡1subscript𝜃𝑡for-allsubscript𝑥𝑖𝑗subscript~𝐷𝑡\\textsf{Score}(x\_{i,j}\|\\bm{x}\_{i,:j};\\theta\_{t-1},\\theta\_{t}),\\forall x\_{i,j}%
\\in\\widetilde{D}\_{t}Score ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT \| bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ; italic\_θ start\_POSTSUBSCRIPT italic\_t - 1 end\_POSTSUBSCRIPT , italic\_θ start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT ) , ∀ italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT ∈ over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT.

6:     Assign token labels y^i,jsubscript^𝑦𝑖𝑗\\hat{y}\_{i,j}over^ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT with a threshold kself-evolsubscript𝑘self-evolk\_{\\text{self-evol}}italic\_k start\_POSTSUBSCRIPT self-evol end\_POSTSUBSCRIPT.

7:     Obtain θt+1subscript𝜃𝑡1\\theta\_{t+1}italic\_θ start\_POSTSUBSCRIPT italic\_t + 1 end\_POSTSUBSCRIPT by finetuning θtsubscript𝜃𝑡\\theta\_{t}italic\_θ start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT on cleaned subset D^t={(xi,j,𝒙i,:j,y^i,j),∀(i,j)∈St}subscript^𝐷𝑡subscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗subscript^𝑦𝑖𝑗for-all𝑖𝑗subscript𝑆𝑡\\widehat{D}\_{t}=\\{(x\_{i,j},\\bm{x}\_{i,:j},\\hat{y}\_{i,j}),\\forall(i,j)\\in S\_{t}\\}over^ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT = { ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT , bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT , over^ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT ) , ∀ ( italic\_i , italic\_j ) ∈ italic\_S start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT }.

8:endfor

9:Output:θT+1subscript𝜃𝑇1\\theta\_{T+1}italic\_θ start\_POSTSUBSCRIPT italic\_T + 1 end\_POSTSUBSCRIPT

##### Algorithm Details

The overall procedure is outlined in Algorithm [1](https://arxiv.org/html/2502.01968v1#alg1 "Algorithm 1 ‣ 4.3.2 Self-Evolving Cleaning ‣ 4.3 Selection of 𝜃 and 𝜃' ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning").
First, we evenly partition the dataset D~~𝐷\\widetilde{D}over~ start\_ARG italic\_D end\_ARG into a series of subsets, denoted as {D~0,D~1,…,D~T}subscript~𝐷0subscript~𝐷1…subscript~𝐷𝑇\\{\\widetilde{D}\_{0},\\widetilde{D}\_{1},\\dots,\\widetilde{D}\_{T}\\}{ over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT , over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , … , over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT italic\_T end\_POSTSUBSCRIPT }.
Next, the base model θ𝜃\\thetaitalic\_θ is fine-tuned on the initial subset D~0subscript~𝐷0\\widetilde{D}\_{0}over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT to produce a warm-up model θ0subscript𝜃0\\theta\_{0}italic\_θ start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, which serves as the initial reference model.
Rather than relying solely on θ0subscript𝜃0\\theta\_{0}italic\_θ start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT as a fixed reference model, a self-evolving mechanism is introduced in Lines 4-8.
Specifically, for each subsequent subset D~tsubscript~𝐷𝑡\\widetilde{D}\_{t}over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT, we keep the base model fixed and utilize the latest updated model as the reference model, i.e., θ=θ0𝜃subscript𝜃0\\theta=\\theta\_{0}italic\_θ = italic\_θ start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT and θ′=θtsuperscript𝜃′subscript𝜃𝑡\\theta^{\\prime}=\\theta\_{t}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT = italic\_θ start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT, to compute token scores.
By applying a threshold kself-evolsubscript𝑘self-evolk\_{\\text{self-evol}}italic\_k start\_POSTSUBSCRIPT self-evol end\_POSTSUBSCRIPT to these scores, we obtain the cleaned labels y^i,jsubscript^𝑦𝑖𝑗\\hat{y}\_{i,j}over^ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT.
The updated model θtsubscript𝜃𝑡\\theta\_{t}italic\_θ start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT is then fine-tuned on the cleaned subset D^tsubscript^𝐷𝑡\\widehat{D}\_{t}over^ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT, producing the reference model for the next iteration.
This process continues iteratively, and the final reference model is used as the output of the algorithm.

## 5 Theoretical Analyses

Let 𝟙⁢{⋅}1⋅\\mathds{1}\\{\\cdot\\}blackboard\_1 { ⋅ } be the indicator function taking value 1111 when the specified condition is satisfied and 00 otherwise. Define the _0-1 loss_ as
𝟙⁢(θ⁢(𝑿prev),Xnext):=𝟙⁢{θ⁢(𝑿prev)≠Xnext}assign1𝜃subscript𝑿prevsubscript𝑋next1𝜃subscript𝑿prevsubscript𝑋next\\mathds{1}{(\\theta(\\bm{X}\_{\\text{prev}}),X\_{\\text{next}})}:=\\mathds{1}\\{\\theta%
(\\bm{X}\_{\\text{prev}})\\neq X\_{\\text{next}}\\}blackboard\_1 ( italic\_θ ( bold\_italic\_X start\_POSTSUBSCRIPT prev end\_POSTSUBSCRIPT ) , italic\_X start\_POSTSUBSCRIPT next end\_POSTSUBSCRIPT ) := blackboard\_1 { italic\_θ ( bold\_italic\_X start\_POSTSUBSCRIPT prev end\_POSTSUBSCRIPT ) ≠ italic\_X start\_POSTSUBSCRIPT next end\_POSTSUBSCRIPT }, where Xnextsubscript𝑋nextX\_{\\text{next}}italic\_X start\_POSTSUBSCRIPT next end\_POSTSUBSCRIPT is the random variable for the next token, Xprevsubscript𝑋prevX\_{\\text{prev}}italic\_X start\_POSTSUBSCRIPT prev end\_POSTSUBSCRIPT is the random variable for tokens before the next token, and θ⁢(𝑿prev)𝜃subscript𝑿prev\\theta(\\bm{X}\_{\\text{prev}})italic\_θ ( bold\_italic\_X start\_POSTSUBSCRIPT prev end\_POSTSUBSCRIPT ) stands for the prediction of next token for model θ𝜃\\thetaitalic\_θ given 𝑿prevsubscript𝑿prev\\bm{X}\_{\\text{prev}}bold\_italic\_X start\_POSTSUBSCRIPT prev end\_POSTSUBSCRIPT as input.
Without loss of generality, we consider the ideal case where all the training instances for next-token prediction are _i.i.d._ and minimize 0-1 loss in the following analyses. The loss can be generalized to bounded loss ℓ⁢(⋅)ℓ⋅\\ell(\\cdot)roman\_ℓ ( ⋅ ) and finite function space ℱℱ\\mathcal{F}caligraphic\_F following the generalization bounds that can be introduced using Rademacher complexity (Bartlett and Mendelson, [2002](https://arxiv.org/html/2502.01968v1#bib.bib40 "")).

### 5.1 Exceed the Performance of Full Tokens

Denote by D~:={(xi,j,𝒙i,:j,y~i,j),∀i,j}assign~𝐷subscript𝑥𝑖𝑗subscript𝒙𝑖:absent𝑗subscript~𝑦𝑖𝑗for-all𝑖𝑗\\widetilde{D}:=\\{(x\_{i,j},\\bm{x}\_{i,:j},\\tilde{y}\_{i,j}),\\forall i,j\\}over~ start\_ARG italic\_D end\_ARG := { ( italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT , bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT , over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT ) , ∀ italic\_i , italic\_j } the full-token dataset.
By minimizing the noisy loss

|     |     |     |
| --- | --- | --- |
|  | ℒ^D~⁢(θ)=1N⁢∑i=1N1∑j=1Liy~i,j⁢∑j=1Liy~i,j⁢𝟙⁢(θ⁢(𝒙i,:j),xi,j)subscript^ℒ~𝐷𝜃1𝑁superscriptsubscript𝑖1𝑁1superscriptsubscript𝑗1subscript𝐿𝑖subscript~𝑦𝑖𝑗superscriptsubscript𝑗1subscript𝐿𝑖subscript~𝑦𝑖𝑗1𝜃subscript𝒙𝑖:absent𝑗subscript𝑥𝑖𝑗\\widehat{\\mathcal{L}}\_{\\widetilde{D}}(\\theta)=\\frac{1}{N}\\sum\_{i=1}^{N}\\frac{1%<br>}{\\sum\_{j=1}^{L\_{i}}\\tilde{y}\_{i,j}}\\sum\_{j=1}^{L\_{i}}\\tilde{y}\_{i,j}\\mathds{1%<br>}(\\theta(\\bm{x}\_{i,:j}),x\_{i,j})over^ start\_ARG caligraphic\_L end\_ARG start\_POSTSUBSCRIPT over~ start\_ARG italic\_D end\_ARG end\_POSTSUBSCRIPT ( italic\_θ ) = divide start\_ARG 1 end\_ARG start\_ARG italic\_N end\_ARG ∑ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT divide start\_ARG 1 end\_ARG start\_ARG ∑ start\_POSTSUBSCRIPT italic\_j = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_L start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT end\_ARG ∑ start\_POSTSUBSCRIPT italic\_j = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_L start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT blackboard\_1 ( italic\_θ ( bold\_italic\_x start\_POSTSUBSCRIPT italic\_i , : italic\_j end\_POSTSUBSCRIPT ) , italic\_x start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT ) |  |

we can get model θ^D~:=arg⁢minθ⁡ℒ^D~⁢(θ)assignsubscript^𝜃~𝐷subscriptargmin𝜃subscript^ℒ~𝐷𝜃\\hat{\\theta}\_{\\widetilde{D}}:=\\operatorname\*{arg\\,min}\_{\\theta}~{}\\widehat{%
\\mathcal{L}}\_{\\widetilde{D}}(\\theta)over^ start\_ARG italic\_θ end\_ARG start\_POSTSUBSCRIPT over~ start\_ARG italic\_D end\_ARG end\_POSTSUBSCRIPT := start\_OPERATOR roman\_arg roman\_min end\_OPERATOR start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT over^ start\_ARG caligraphic\_L end\_ARG start\_POSTSUBSCRIPT over~ start\_ARG italic\_D end\_ARG end\_POSTSUBSCRIPT ( italic\_θ ).
Denote by Y~~𝑌\\widetilde{Y}over~ start\_ARG italic\_Y end\_ARG, Y𝑌Yitalic\_Y the random variables for y~i,jsubscript~𝑦𝑖𝑗\\tilde{y}\_{i,j}over~ start\_ARG italic\_y end\_ARG start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT and the corresponding ground-truth label yi,jsubscript𝑦𝑖𝑗y\_{i,j}italic\_y start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT.
The expected loss of training with full tokens can be denoted by

|     |     |     |
| --- | --- | --- |
|  | ℒ𝒟~⁢(θ)=𝔼⁢\[Y~⋅𝟙⁢(θ⁢(𝑿prev),Xnext)\],subscriptℒ~𝒟𝜃𝔼delimited-\[\]⋅~𝑌1𝜃subscript𝑿prevsubscript𝑋next{\\mathcal{L}}\_{\\widetilde{\\mathcal{D}}}(\\theta)=\\mathbb{E}\\left\[\\widetilde{Y}%<br>\\cdot\\mathds{1}{(\\theta(\\bm{X}\_{\\text{prev}}),X\_{\\text{next}})}\\right\],caligraphic\_L start\_POSTSUBSCRIPT over~ start\_ARG caligraphic\_D end\_ARG end\_POSTSUBSCRIPT ( italic\_θ ) = blackboard\_E \[ over~ start\_ARG italic\_Y end\_ARG ⋅ blackboard\_1 ( italic\_θ ( bold\_italic\_X start\_POSTSUBSCRIPT prev end\_POSTSUBSCRIPT ) , italic\_X start\_POSTSUBSCRIPT next end\_POSTSUBSCRIPT ) \] , |  |

where 𝒟~~𝒟\\widetilde{\\mathcal{D}}over~ start\_ARG caligraphic\_D end\_ARG is the distribution of D~~𝐷\\widetilde{D}over~ start\_ARG italic\_D end\_ARG.
Denote by

|     |     |     |
| --- | --- | --- |
|  | η⁢(D~):=ℙ⁢(Y~≠Y)assign𝜂~𝐷ℙ~𝑌𝑌\\eta(\\widetilde{D}):=\\mathbb{P}(\\widetilde{Y}\\neq Y)italic\_η ( over~ start\_ARG italic\_D end\_ARG ) := blackboard\_P ( over~ start\_ARG italic\_Y end\_ARG ≠ italic\_Y ) |  |

the noise rate of full tokens. Theorem [5.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1 "Theorem 5.1 (Error of learning with full tokens). ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") shows the error upper bound of learning with full tokens. See Appendix [9](https://arxiv.org/html/2502.01968v1#S9 "9 Proof for Theorem 5.1 ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") for the proof.

###### Theorem 5.1(Error of learning with full tokens).

With probability at least 1−δ1𝛿1-\\delta1 - italic\_δ, the generalization error of learning with full tokens is upper-bounded by

|     |     |     |     |
| --- | --- | --- | --- |
|  | ℒ𝒟⁢(θ^D~)≤η⁢(D~)⏟Data quality+2⁢log⁡(4/δ)M⏟Data quantity,subscriptℒ𝒟subscript^𝜃~𝐷subscript⏟𝜂~𝐷Data qualitysubscript⏟24𝛿𝑀Data quantity{\\mathcal{L}}\_{{\\mathcal{D}}}(\\hat{\\theta}\_{\\widetilde{D}})\\leq\\underbrace{%<br>\\eta(\\widetilde{D})}\_{\\text{Data quality}}+\\underbrace{\\sqrt{\\frac{2\\log({4}/%<br>\\delta)}{M}}}\_{\\text{Data quantity}},caligraphic\_L start\_POSTSUBSCRIPT caligraphic\_D end\_POSTSUBSCRIPT ( over^ start\_ARG italic\_θ end\_ARG start\_POSTSUBSCRIPT over~ start\_ARG italic\_D end\_ARG end\_POSTSUBSCRIPT ) ≤ under⏟ start\_ARG italic\_η ( over~ start\_ARG italic\_D end\_ARG ) end\_ARG start\_POSTSUBSCRIPT Data quality end\_POSTSUBSCRIPT + under⏟ start\_ARG square-root start\_ARG divide start\_ARG 2 roman\_log ( 4 / italic\_δ ) end\_ARG start\_ARG italic\_M end\_ARG end\_ARG end\_ARG start\_POSTSUBSCRIPT Data quantity end\_POSTSUBSCRIPT , |  | (5) |

where M:=∑i=1NLiassign𝑀superscriptsubscript𝑖1𝑁subscript𝐿𝑖M:=\\sum\_{i=1}^{N}L\_{i}italic\_M := ∑ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT italic\_L start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT denotes the number of tokens.

Theorem [5.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1 "Theorem 5.1 (Error of learning with full tokens). ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") shows that the error of learning with full tokens depends on two factors:

- ∙∙\\bullet∙

Data Quality: η⁢(D~)𝜂~𝐷\\eta(\\widetilde{D})italic\_η ( over~ start\_ARG italic\_D end\_ARG ) denotes the noise rates of learning with full tokens, where a higher noise rate leads to a larger error, i.e., a worse performance. The negative impact of wrong token labels may not be canceled by increasing the number of tokens.

- ∙∙\\bullet∙

Data Quantity: When the number of tokens M𝑀Mitalic\_M increases, the generalization could be smaller, showing that the token cleaning result cannot merely return a small set of high-quality tokens, i.e., the precision and recall of the token cleaning algorithm are both important.

Denote by Y^^𝑌\\widehat{Y}over^ start\_ARG italic\_Y end\_ARG the random variable of token labels after cleaning.
We show the superiority of token cleaning compared to the full-token case in the following corollary.

###### Corollary 5.1.1.

With probability as least 1−2⁢δ12𝛿1-2\\delta1 - 2 italic\_δ, token cleaning performs better than full-tokens in terms of the error upper bound when

|     |     |     |     |
| --- | --- | --- | --- |
|  | η⁢(D~)−η^≥2⁢log⁡(4/δ)⋅1M⋅(1r^−1),𝜂~𝐷^𝜂⋅24𝛿1𝑀1^𝑟1\\eta(\\widetilde{D})-\\hat{\\eta}\\geq\\sqrt{2\\log(4/\\delta)}\\cdot\\sqrt{\\frac{1}{M}%<br>}\\cdot\\left(\\sqrt{\\frac{1}{\\hat{r}}}-1\\right),italic\_η ( over~ start\_ARG italic\_D end\_ARG ) - over^ start\_ARG italic\_η end\_ARG ≥ square-root start\_ARG 2 roman\_log ( 4 / italic\_δ ) end\_ARG ⋅ square-root start\_ARG divide start\_ARG 1 end\_ARG start\_ARG italic\_M end\_ARG end\_ARG ⋅ ( square-root start\_ARG divide start\_ARG 1 end\_ARG start\_ARG over^ start\_ARG italic\_r end\_ARG end\_ARG end\_ARG - 1 ) , |  | (6) |

where η^:=ℙ⁢(Y^≠Y)assign^𝜂ℙ^𝑌𝑌\\hat{\\eta}:=\\mathbb{P}(\\widehat{Y}\\neq Y)over^ start\_ARG italic\_η end\_ARG := blackboard\_P ( over^ start\_ARG italic\_Y end\_ARG ≠ italic\_Y ) denotes the noise rates of cleaned labels and r^:=ℙ⁢(Y^=1)assign^𝑟ℙ^𝑌1\\hat{r}:=\\mathbb{P}(\\widehat{Y}=1)over^ start\_ARG italic\_r end\_ARG := blackboard\_P ( over^ start\_ARG italic\_Y end\_ARG = 1 ) denotes the ratio of positive tokens after token cleaning.

Corollary [5.1.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1.Thmcorollary1 "Corollary 5.1.1. ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") shows token cleaning is preferred when the positive impact of reducing noise rate outweighs the negative impact of reducing the number of feasible tokens. For example, when M𝑀Mitalic\_M is larger (a larger dataset), the inequality in Corollary [5.1.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1.Thmcorollary1 "Corollary 5.1.1. ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") is more likely to hold since the right-hand side is smaller.

### 5.2 Fixed-Model Cleaning: Stable But Limited Improvement

We now analyze the benefits and limitations based on Theorem [5.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1 "Theorem 5.1 (Error of learning with full tokens). ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") and Corollary [5.1.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1.Thmcorollary1 "Corollary 5.1.1. ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning").
By selecting an appropriate model θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT, we can take a one-shot token cleaning on all the tokens in the candidate data pool. In this case:

- ∙∙\\bullet∙

Data Quality: The noise rate of cleaned tokens is fixed, i.e., the data quality term in Eq. ( [5](https://arxiv.org/html/2502.01968v1#S5.E5 "In Theorem 5.1 (Error of learning with full tokens). ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning")) is fixed. By carefully selecting the threshold kfixedsubscript𝑘fixedk\_{\\text{fixed}}italic\_k start\_POSTSUBSCRIPT fixed end\_POSTSUBSCRIPT, there exists a token cleaning result whose noise rate η^^𝜂\\hat{\\eta}over^ start\_ARG italic\_η end\_ARG is less than η⁢(D~)𝜂~𝐷\\eta(\\widetilde{D})italic\_η ( over~ start\_ARG italic\_D end\_ARG ).

- ∙∙\\bullet∙

Data Quantity: With more tokens being cleaned, M𝑀Mitalic\_M is increasing. Then the total generalization error can be consistently reduced.

Therefore, under this strategy, as long as the reference model θ′superscript𝜃′\\theta^{\\prime}italic\_θ start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT is sufficiently good to reduce the noise rate from η⁢(D~)𝜂~𝐷\\eta(\\widetilde{D})italic\_η ( over~ start\_ARG italic\_D end\_ARG ) to a lower rate η^^𝜂\\hat{\\eta}over^ start\_ARG italic\_η end\_ARG, the model’s performance can be improved by fine-tuning with additional i.i.d. cleaned tokens, demonstrating the advantage on stability. However, even as M→∞→𝑀M\\rightarrow\\inftyitalic\_M → ∞, the total error does not go to zero due to imperfect data quality, showing the limitations on final performance.

### 5.3 Self-Evolving Cleaning: Potential Matthew Effect

For ease of presentation, we divide the data into three groups according to their task difficulty and number of i.i.d. clean tokens in the training dataset:

- ∙∙\\bullet∙

G1subscript𝐺1G\_{1}italic\_G start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT (Rich Group): Characterized by lower noise rates after token cleaning and a higher proportion of effective tokens. This group typically experiences significant performance gains during warmup (Line 3, Algorithm [1](https://arxiv.org/html/2502.01968v1#alg1 "Algorithm 1 ‣ 4.3.2 Self-Evolving Cleaning ‣ 4.3 Selection of 𝜃 and 𝜃' ‣ 4 Token Cleaning: A Noisy Label Perspective ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning")) and has a great number of relevant tokens.

- ∙∙\\bullet∙

G2subscript𝐺2G\_{2}italic\_G start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT (Poor Group): Marked by higher noise rates after token cleaning and fewer effective tokens. This group often exhibits limited or even degraded performance during warmup and has a scarce number of relevant tokens.

- ∙∙\\bullet∙

G3subscript𝐺3G\_{3}italic\_G start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT (Intermediate Group): Falling between the rich and poor groups in terms of data quality and quantity. While it generally sees reasonable performance improvement during warmup, its convergence tends to be unstable due to a limited number of effective tokens.

Note that the definition of groups only applies to the theoretical analyses, which does not mean we need to explicitly know the group attribute of each data. In fact, it is challenging to know this information.
Theoretically, there are three observations during SFT.

- ∙∙\\bullet∙

Observation 1: The rich get richer (G1subscript𝐺1G\_{1}italic\_G start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT). When η^<η⁢(D~)^𝜂𝜂~𝐷\\hat{\\eta}<\\eta({\\widetilde{D}})over^ start\_ARG italic\_η end\_ARG < italic\_η ( over~ start\_ARG italic\_D end\_ARG ) and r^⋅M⋅^𝑟𝑀\\hat{r}\\cdot Mover^ start\_ARG italic\_r end\_ARG ⋅ italic\_M is sufficiently large, according to Corollary [5.1.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1.Thmcorollary1 "Corollary 5.1.1. ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"), fine-tuning on D^1subscript^𝐷1\\widehat{D}\_{1}over^ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT benefits from lower token noise rates and a higher number of effective tokens, thereby reducing the error upper bound and resulting in a better model θ2subscript𝜃2\\theta\_{2}italic\_θ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT. With a better reference model and a similar number of effective tokens, the model in the next iteration can be further improved, i.e., the rich get richer.

- ∙∙\\bullet∙

Observation 2: The poor get poorer (G2subscript𝐺2G\_{2}italic\_G start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT).
When the model θ1subscript𝜃1\\theta\_{1}italic\_θ start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT underperforms compared to θ0subscript𝜃0\\theta\_{0}italic\_θ start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT, η1subscript𝜂1\\eta\_{1}italic\_η start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT increases significantly and may even exceed 0.50.50.50.5. According to Corollary [5.1.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1.Thmcorollary1 "Corollary 5.1.1. ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"), continued fine-tuning on tokens with such high noise rates can further degrade performance, exemplifying a “the poor get poorer" effect.

- ∙∙\\bullet∙

Observation 3: Unstable convergence (G3subscript𝐺3G\_{3}italic\_G start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT).
If η^^𝜂\\hat{\\eta}over^ start\_ARG italic\_η end\_ARG is comparable to η⁢(D~)𝜂~𝐷\\eta({\\widetilde{D}})italic\_η ( over~ start\_ARG italic\_D end\_ARG ) and r^⋅M⋅^𝑟𝑀\\hat{r}\\cdot Mover^ start\_ARG italic\_r end\_ARG ⋅ italic\_M is only marginally sufficient, fine-tuning on D^3subscript^𝐷3\\widehat{D}\_{3}over^ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 3 end\_POSTSUBSCRIPT may yield moderate improvements but suffers from instability due to the limited number of effective tokens.
According to Corollary [5.1.1](https://arxiv.org/html/2502.01968v1#S5.Thmtheorem1.Thmcorollary1 "Corollary 5.1.1. ‣ 5.1 Exceed the Performance of Full Tokens ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"), the model’s error upper bound may not decrease consistently, leading to unstable convergence.

From the above analyses, we know that self-evolving models are more adaptive and aggressive compared to fixed models. The theoretical insights further highlight strategies for achieving better performance.

## 6 Experiments

### 6.1 Experiments Setup

##### Data Pool

We utilize a high-quality data pool with 50k sample size from five popular SFT datasets (300k in total): Flan\_v2 (Longpre et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib5 "")), Open Assistant 1 (Köpf et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib41 "")), Stanford Alpaca (Taori et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib42 "")), Dolly (Databricks, [2023](https://arxiv.org/html/2502.01968v1#bib.bib43 "")), and WizardLM (Xu et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib44 "")). The data pool is constructed based on a new powerful data curation pipeline proposed by (Pang et al., [2024a](https://arxiv.org/html/2502.01968v1#bib.bib8 "")), which involves selecting data samples using quality rating scores generated by LLMs.
More dataset statistical information including token length can be found in Appendix [10.1](https://arxiv.org/html/2502.01968v1#S10.SS1 "10.1 Data Pool ‣ 10 Experimental Details ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"). For the self-evolving cleaning strategy, we heuristically divide the data pool into five equally sized subsets (10k samples).

Table 1: Performance (original score ×\\times×100) comparison of different baselines on various benchmarks. We highlight the best result in boldface and the second-best with underline. By default, the selected token proportion (i.e., threshold) is 0.6.

| Model | TruthfulQA | TydiQA | LoqiQA | MMLU | HellaSwag | ARC-C | BoolQ | AVG |
| Base model: LLaMA-3.2-3B |
| Base | 39.39 | 21.10 | 22.17 | 56.29 | 55.24 | 42.20 | 72.95 | 44.19 |
| DS2 (10k) | 43.35 | 41.20 | 24.96 | 56.93 | 55.64 | 44.62 | 74.80 | 48.79 |
| Full Tokens (50k) | 43.32 | 49.60 | 24.34 | 56.87 | 55.57 | 44.44 | 74.98 | 49.87 |
| Uniform Random (50k×\\times×0.6) | 43.79 | 47.00 | 23.41 | 56.96 | 55.37 | 44.44 | 75.05 | 49.43 |
| Rho | 45.57 | 53.60 | 26.05 | 57.10 | 55.16 | 45.39 | 77.36 | 51.46 |
| Fixed-Model Cleaning | 48.96 | 52.60 | 25.89 | 57.09 | 56.43 | 45.39 | 77.52 | 51.98 |
| Self-Evolving Cleaning | 51.07 | 56.38 | 28.22 | 56.18 | 55.81 | 45.99 | 77.33 | 53.00 |
| Base model: LLaMA-3.1-8B |
| Base | 45.10 | 22.80 | 26.51 | 65.29 | 59.92 | 50.82 | 82.18 | 50.37 |
| DS2 (10k) | 49.57 | 45.80 | 27.44 | 65.77 | 60.37 | 53.49 | 83.26 | 55.10 |
| Full Tokens (50k) | 47.51 | 58.10 | 28.53 | 65.78 | 60.42 | 54.01 | 82.49 | 56.70 |
| Uniform Random (50k×\\times×0.6) | 48.68 | 56.60 | 27.29 | 65.81 | 60.40 | 54.09 | 83.11 | 56.57 |
| Rho | 54.63 | 61.90 | 28.99 | 65.74 | 62.14 | 54.78 | 81.66 | 58.55 |
| Fixed-Model Cleaning | 56.02 | 62.38 | 28.22 | 65.71 | 61.92 | 55.12 | 82.67 | 58.90 |
| Self-Evolving Cleaning | 59.58 | 63.58 | 26.05 | 65.07 | 62.67 | 54.87 | 82.49 | 59.20 |
| Base model: Mistral-7B-v0.3 |
| Base | 42.56 | 54.70 | 25.74 | 62.41 | 60.77 | 48.92 | 82.30 | 52.88 |
| DS2 (10k) | 44.24 | 55.70 | 25.27 | 62.50 | 61.10 | 50.39 | 83.45 | 53.85 |
| Full Tokens (50k) | 43.67 | 55.60 | 25.27 | 62.41 | 61.14 | 50.56 | 83.85 | 54.12 |
| Uniform Random (50k×\\times×0.6) | 43.82 | 55.70 | 24.81 | 62.47 | 61.20 | 50.04 | 83.76 | 53.64 |
| Rho | 43.92 | 54.50 | 25.43 | 62.12 | 61.35 | 51.08 | 83.29 | 53.60 |
| Fixed-Model Cleaning | 44.52 | 59.03 | 26.05 | 61.45 | 61.47 | 51.68 | 82.03 | 55.20 |
| Self-Evolving Cleaning | 45.41 | 56.17 | 27.44 | 62.30 | 61.40 | 50.65 | 81.28 | 55.00 |

##### Base Models

In this paper, we select three popular open-source LLMs as our base models, including LLaMA-3.2-3B, LLaMA-3.1-8B (Dubey et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib45 "")) and Mistral-7B-v0.3 (Jiang et al., [2023](https://arxiv.org/html/2502.01968v1#bib.bib46 "")). These base models will be fine-tuned using samples from our data pool.

##### Baselines

There are several baselines for performance comparisons: 1) Base denotes the used base model; 2) DS2Pang et al. ( [2024a](https://arxiv.org/html/2502.01968v1#bib.bib8 "")) fine-tunes base model on 10k selected high-quality samples (with full tokens) from the entire data pool (50k); 3) Full Tokens utilizes all tokens to fine-tune the base model; 4) Uniform Random randomly selects k%percent𝑘k\\%italic\_k % tokens from the 50k data pool without replacement; 5) Rho(Mindermann et al., [2022](https://arxiv.org/html/2502.01968v1#bib.bib39 ""); Lin et al., [2024](https://arxiv.org/html/2502.01968v1#bib.bib13 "")) directly computes the excess loss for all tokens between the base and reference model and then selects top-k%percent𝑘k\\%italic\_k % tokens. Recall that k𝑘kitalic\_k is the pre-defined threshold for token cleaning.

##### Warmup

We warmup by fine-tuning the base model on subset D~0subscript~𝐷0\\widetilde{D}\_{0}over~ start\_ARG italic\_D end\_ARG start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT with full tokens, and make it the (initial) reference model for Rho, our Fixed-Model Cleaning, and Self-Evolving Cleaning. The warmup model is equivalent to the DS2 baseline (Pang et al., [2024a](https://arxiv.org/html/2502.01968v1#bib.bib8 "")).

Table 2: Performance results of self-evolving cleaning strategy over iterations (checkpoints) on seven benchmarks. Base model: LLaMA-3.2-3B. These performance results align with three observations arising from the Matthew effect.

| Model | TruthfulQA | TydiQA | LoqiQA | MMLU | HellaSwag | ARC-C | BoolQ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reference-1 | 45.46 | 50.05 | 27.44 | 57.31 | 56.10 | 45.91 | 76.87 |
| Reference-2 | 46.67 | 53.18 | 27.44 | 56.89 | 56.25 | 46.51 | 77.15 |
| Reference-3 | 48.91 | 54.36 | 28.22 | 56.43 | 56.13 | 46.43 | 77.36 |
| Reference-4 | 51.07 | 56.38 | 28.22 | 56.18 | 55.81 | 45.99 | 77.33 |

##### Evaluation

To comprehensively evaluate the efficacy of token cleaning methods, we adopt seven OpenLLM Leaderboard tasks, including MMLU (Hendrycks et al., [2020](https://arxiv.org/html/2502.01968v1#bib.bib47 "")), TruthfulQA (Lin et al., [2021](https://arxiv.org/html/2502.01968v1#bib.bib48 "")), TydiQA (Clark et al., [2020](https://arxiv.org/html/2502.01968v1#bib.bib49 "")), HellaSwag (Zellers et al., [2019](https://arxiv.org/html/2502.01968v1#bib.bib50 "")), ARC-Challenge (Clark et al., [2018](https://arxiv.org/html/2502.01968v1#bib.bib51 "")), BoolQ (Clark et al., [2019](https://arxiv.org/html/2502.01968v1#bib.bib52 "")) and LogiQA (Liu et al., [2020](https://arxiv.org/html/2502.01968v1#bib.bib53 "")). These datasets are sufficiently diverse to thoroughly assess the fine-tuned model across various aspects, including factual accuracy, reasoning, and multilingual capability.
The task performances are evaluated on the lm-eval-hareness111 [https://github.com/EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness "") repository. More evaluation and training details can be found in Appendix [10.2](https://arxiv.org/html/2502.01968v1#S10.SS2 "10.2 Evaluation Benchmarks ‣ 10 Experimental Details ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning").

### 6.2 Main Empirical Results

As shown in Table [1](https://arxiv.org/html/2502.01968v1#S6.T1 "Table 1 ‣ Data Pool ‣ 6.1 Experiments Setup ‣ 6 Experiments ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"), our proposed strategies consistently outperform baselines across three base models on seven evaluation benchmarks. Notably, compared to using full tokens, our self-evolving cleaning has achieved the average performance improvement of 6.3% on the 3B model and 2.0%/4.4% on the 7B/8B models.

##### Local Ranking vs. Global Ranking

Compared to RHO, which ranks token scores locally within individual samples and removes the same proportion of tokens per sample, our fixed-model cleaning method globally ranks token scores across the entire dataset. As shown in Table [1](https://arxiv.org/html/2502.01968v1#S6.T1 "Table 1 ‣ Data Pool ‣ 6.1 Experiments Setup ‣ 6 Experiments ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"), the local-ranking method (Rho) yields lower average performance than the global-ranking method (Fixed-Model Cleaning), e.g., 51.4651.4651.4651.46 vs. 51.9851.9851.9851.98 for LLaMA-3.2-3B and 53.6053.6053.6053.60 vs. 55.2055.2055.2055.20 for Mistral-7B-v0.3, demonstrating that global ranking leads to more stable performance improvements.
One possible explanation is that local ranking is constrained by the quality of individual samples. For example, in SFT, a low-quality sample may not contain any useful tokens, while almost all tokens in a high-quality sample may be useful. Since local ranking removes the same proportion of tokens from both samples, it inevitably retains uninformative tokens from low-quality samples while discarding informative ones from high-quality samples.
This limitation can be mitigated through global token ranking, as employed in our fixed-model cleaning approach.

##### Self-Evolving Cleaning Follows the Matthew Effect

Table [2](https://arxiv.org/html/2502.01968v1#S6.T2 "Table 2 ‣ Warmup ‣ 6.1 Experiments Setup ‣ 6 Experiments ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") presents the model’s performance across different training iterations (checkpoints), illustrating three phenomena arising from the Matthew effect, as discussed in Section [5.3](https://arxiv.org/html/2502.01968v1#S5.SS3 "5.3 Self-Evolving Cleaning: Potential Matthew Effect ‣ 5 Theoretical Analyses ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning").
Specifically, performance on TruthfulQA, TydiQA, and LogiQA steadily improves over iterations, representing Observation 1: the rich get richer. In contrast, MMLU which focuses on factual knowledge, exhibits a slight performance decline, illustrating Observation 2: the poor get poorer. Meanwhile, for the remaining tasks (HellaSwag, ARC-C, and BoolQ), performance improvements are observed but exhibit fluctuations, aligning with Observation 3: unstable convergence.https://arxiv.org/html/2502.01968v1/extracted/6176326/figs/token_ratio_impact.pngFigure 2: Average performance results of self-evolving cleaning pipeline under different token proportions. The base model is LLaMA-3.2-3B.

### 6.3 Ablation Study

##### Impact of Selected Token Proportion.

Here, we investigate the impact of selected token proportion for our pipeline using a series of token proportion values including {0.3,0.4,⋯,0.9}0.30.4⋯0.9\\{0.3,0.4,\\cdots,0.9\\}{ 0.3 , 0.4 , ⋯ , 0.9 }. As presented in Figure [2](https://arxiv.org/html/2502.01968v1#S6.F2 "Figure 2 ‣ Self-Evolving Cleaning Follows the Matthew Effect ‣ 6.2 Main Empirical Results ‣ 6 Experiments ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"), the best results are achieved when the selected token proportion is approximately 50% to 70%. Beyond this range, the overall performance declines, which may be attributed to uninformative tokens. One valuable empirical finding is that the performance gains in SFT tasks largely rely on a small number of highly informative tokens. This observation supports the prevailing view that data quality is more crucial than mere volume.
Full results can be referred to in Appendix [11](https://arxiv.org/html/2502.01968v1#S11 "11 Additional Experimental Results ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning") (Table [7](https://arxiv.org/html/2502.01968v1#S11.T7 "Table 7 ‣ 11.2 Impact of Selected Token Proportion ‣ 11 Additional Experimental Results ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning")).

Table 3: Performance comparison with a new reference model: LLaMA-3.1-8B-Instruct.
Blue: A better reference model brings a higher performance improvement. Red: The counterpart.

| Models | MMLU | BoolQ | TydiQA | ARC-C |
| --- | --- | --- | --- | --- |
| Reference: LLaMA-8b-Inst | 68.18 | 84.03 | 21.63 | 51.77 |
| Rho | 57.04 | 75.94 | 39.37 | 46.08 |
| Fixed-Model Cleaning | 56.96 | 76.37 | 39.17 | 46.08 |
| Reference: Warmup | 56.93 | 74.80 | 41.20 | 44.62 |
| Rho | 57.10 | 77.36 | 53.60 | 45.39 |
| Fixed-Model Cleaning | 57.09 | 77.52 | 52.60 | 45.39 |

##### Impact of Reference Model.

To assess the impact of the reference model on performance, we run Rho and our fixed-model cleaning approach using LLaMA-3.1-8B-Instruct as the new reference model and compare the results with our previous reference model (DS2 as the warmup). As shown in Table [3](https://arxiv.org/html/2502.01968v1#S6.T3 "Table 3 ‣ Impact of Selected Token Proportion. ‣ 6.3 Ablation Study ‣ 6 Experiments ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning"), a more powerful reference model generally leads to greater performance improvements in datasets such as TydiQA and ARC-C. However, some counterintuitive results emerge: in MMLU and BoolQ, despite the 8B reference model significantly outperforming the warmup model, it fails to yield further improvements through token cleaning.
A possible explanation for this phenomenon is the distribution shift. If we divide the evaluation task distribution into two parts: an in-distribution segment aligned with our data pool and an out-of-distribution segment, LLaMA-3.1-8B-Instruct, while achieving high overall performance, may not necessarily surpass the warmup model in the in-distribution subset. Investigating this hypothesis and validating this assumption are promising directions for future research.
More detailed results can be found in Appendix [11](https://arxiv.org/html/2502.01968v1#S11 "11 Additional Experimental Results ‣ Token Cleaning: Fine-Grained Data Selection for LLM Supervised Fine-Tuning").

## 7 Conclusion

This work has demonstrated the effectiveness and importance of token cleaning, introducing a generic token cleaning pipeline that removes uninformative tokens while preserving task-relevant information.
Our theoretical analysis has revealed the strengths and limitations of two scoring strategies: _fixed-model cleaning_, which provides stability but limited improvements, and _self-evolving cleaning_, which has shown the potential for greater performance gains but requires more careful implementation.
Empirically, we have found that filtering out approximately 30%–40% of tokens consistently enhances performance across both strategies, achieving an average 6.3% improvement over the full-token baseline at the 3B model scale.

</details>


## Code Sources

_No code sources found._


## YouTube Video Transcripts

_No YouTube video transcripts found._


## Additional Sources Scraped

<details>
<summary>anthropic-launches-tool-to-connect-ai-systems-directly-to-da</summary>

# Anthropic launches tool to connect AI systems directly to datasets

The Model Context Protocol connects an AI system to multiple data sources, which Anthropic says can eliminate the need to create custom code for each one.

byEmma Roth

Nov 25, 2024, 3:38 PM ESThttps://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/25469776/STK269_ANTHROPIC_C.jpg?quality=90&strip=all&crop=0%2C0%2C100%2C100&w=2400

Image: The Verge

Anthropic has released a new open-source tool to connect AI assistants directly to the information they need to inform their responses or carry out tasks. [The new Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) (MCP) provides a universal connection to all sorts of data sources, which Anthropic says will improve performance.

Earlier this month, OpenAI started testing a new “Work with Apps” feature that [lets the Mac version of ChatGPT directly connect](https://www.theverge.com/2024/11/14/24296745/chatgpts-mac-app-will-be-able-to-read-your-code#:~:text=%2D%20The%20Verge&text=Emma%20Roth-,ChatGPT%E2%80%99s%20Mac%20app%20will%20be%20able%20to%20read%20your%20code,paste%20it%20into%20the%20app.) to certain coding apps. Anthropic’s tool, on the other hand, aims to work across all AI systems and data sources.

[As noted by Alex Albert](https://x.com/alexalbert__/status/1861079886619918644), Anthropic’s head of Claude relations, developers currently have to create custom code for each dataset they want their AI model to draw from. With Anthropic’s MCP, Albert says developers can integrate it with their AI tool once and then “connect to data sources anywhere” thanks to a “standard protocol for sharing resources, tools, and prompts.”

Anthropic says coding software like Replit, Codeium, and Souregraph have already started using MCP to build out their AI agents, which can complete tasks on behalf of users. This tool will likely make it easier for other companies and developers to connect an AI system with multiple data sources — something that could become especially helpful as the [industry leans into agentic AI](https://www.theverge.com/2024/10/10/24266333/ai-agents-assistants-openai-google-deepmind-bots).

“Instead of maintaining separate connectors for each data source, developers can now build against a standard protocol,” Anthropic’s announcement says. “As the ecosystem matures, AI systems will maintain context as they move between different tools and datasets, replacing today’s fragmented integrations with a more sustainable architecture.”

</details>

<details>
<summary>firecrawl-the-web-data-api-for-ai</summary>

# Turn websites into   LLM-ready data

Power your AI apps with clean web data

from any website.

```json
1[\
2  {\
3    "url": "!tap-:0/=*Zz*aA9-0-",\
4    "markdown": "# 0ZAtZ-- 9!!-teA.=Z",\
5    "json": { "title": "-a0?e", "docs": "..." },\
6    "screenshot": "h0zps?z?-Zaz9ze?!Am/?-ro.png"\
7  }\
8]
```

## Startscraping   today

Enhance your apps with industry leading web scraping and crawling capabilities.

Scrape

Get llm-ready data from websites. Markdown, JSON, screenshot, etc.

Search
New

Search the web and get full content from results.

Crawl

Crawl all the pages on a website and get data for each page.

Python

Node.js

Curl

```python
1# pip install firecrawl-py
2from firecrawl import Firecrawl
3
4app = Firecrawl(api_key="fc-YOUR_API_KEY")
5
6# Scrape a website:
7app.scrape('firecrawl.dev')
8
9
10
```

```markdown
1# Firecrawl
2
3Firecrawl is a powerful web scraping
4library that makes it easy to extract
5data from websites.
6
7## Installation
8
9To install Firecrawl, run:
10
11
```

### Use well-known tools

Already fully integrated with the greatest existing tools and workflows.

### Code you can trust

Developed transparently and collaboratively. Join our community of contributors.

## Core principles,    provenperformance

Built from the ground up to outperform traditional scrapers.

No proxy headaches

Reliable.Covers 96% of the web,

including JS-heavy and protected pages. No proxies, no puppets, just clean data.

Firecrawl

51%

Puppeteer

47%

cURL

46%

Speed that feels invisible

Blazingly fast.Delivers results in less than 1 second, fast for real-time agents

and dynamic apps.

URL

Crawl

Scrape

firecrawl.dev/changelog

0ms

0ms

firecrawl.dev/playground

50ms

49ms

firecrawl.dev/login

49ms

51ms

firecrawl.dev/docs

49ms

51ms

firecrawl.dev/faq

49ms

50ms

firecrawl.dev/blog

50ms

51ms

firecrawl.dev/partners

51ms

49ms

## We handle the hard stuff

Rotating proxies, orchestration, rate limits, js-blocked content and more.

Docs to data

Media parsing.Firecrawl can parse and output content from web hosted pdfs, docx, and more.

https://example.com/docs/report.pdf

https://example.com/files/brief.docx

https://example.com/docs/guide.html

Knows the moment

Smart wait.Firecrawl intelligently waits for content to load, making scraping faster and more reliable.

https://example-spa.com

Scrapes the real thing

Cached, when you need it.Selective caching, you choose your caching patterns, growing web index.

Invisible access

Stealth mode.Crawls the web without

being blocked, mimics real users to access protected or dynamic content.

Interactive scraping

Actions.Click, scroll, write, wait, press and more before extracting content.

https://example.com

## Transform    web data into  AI-powered solutions

Discover how Firecrawl customers are getting the most out of our API.

Chat with context

Smarter AI chats

Power your AI assistants with real-time, accurate web content.

Know your leads

Lead enrichment

Enhance your sales data with

web information.

MCPs

Add powerful scraping to your

code editors.

Build with context

AI platforms

Let your customers build AI apps

with web data.

Extracting text

No insight missed

Deep research

Extract comprehensive information for

in-depth research.

## Frequently    askedquestions

Everything you need to know about Firecrawl.

General

What is Firecrawl?

What sites work?

Who can benefit from using Firecrawl?

Is Firecrawl open-source?

What is the difference between Firecrawl and other web scrapers?

What is the difference between the open-source version and the hosted version?

Scraping & Crawling

How does Firecrawl handle dynamic content on websites?

Why is it not crawling all the pages?

Can Firecrawl crawl websites without a sitemap?

What formats can Firecrawl convert web data into?

How does Firecrawl ensure the cleanliness of the data?

Is Firecrawl suitable for large-scale data scraping projects?

Does it respect robots.txt?

What measures does Firecrawl take to handle web scraping challenges like rate limits and caching?

Does Firecrawl handle captcha or authentication?

API Related

Where can I find my API key?

Billing

Is Firecrawl free?

Is there a pay-per-use plan instead of monthly?

Do credits roll over to the next month?

How many credits do scraping and crawling cost?

Do you charge for failed requests?

What payment methods do you accept?

</details>

<details>
<summary>gitingest-1</summary>

# Prompt-friendly codebase
Turn any Git repository into a simple text digest of its codebase.
This is useful for feeding a codebase into any LLM.
- PAT is never stored in the backend
- Used once for cloning, then discarded from memory
- No browser caching
- Cloned repos are deleted after processing
You can also replace 'hub' with 'ingest' in any GitHub URL.

</details>

<details>
<summary>gitingest</summary>

# Prompt-friendly codebase

Turn any Git repository into a simple text digest of its codebase.

This is useful for feeding a codebase into any LLM.

- PAT is never stored in the backend
- Used once for cloning, then discarded from memory
- No browser caching
- Cloned repos are deleted after processing

You can also replace 'hub' with 'ingest' in any GitHub URL.

</details>

<details>
<summary>model-context-protocol-mcp-openai-agents-sdk</summary>

# Model context protocol (MCP)

The [Model context protocol](https://modelcontextprotocol.io/introduction) (MCP) standardises how applications expose tools and
context to language models. From the official documentation:

> MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI
> applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP
> provides a standardized way to connect AI models to different data sources and tools.

The Agents Python SDK understands multiple MCP transports. This lets you reuse existing MCP servers or build your own to expose
filesystem, HTTP, or connector backed tools to an agent.

## Choosing an MCP integration

Before wiring an MCP server into an agent decide where the tool calls should execute and which transports you can reach. The
matrix below summarises the options that the Python SDK supports.

| What you need | Recommended option |
| --- | --- |
| Let OpenAI's Responses API call a publicly reachable MCP server on the model's behalf | **Hosted MCP server tools** via [`HostedMCPTool`](https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.HostedMCPTool "HostedMCPTool            dataclass   ") |
| Connect to Streamable HTTP servers that you run locally or remotely | **Streamable HTTP MCP servers** via [`MCPServerStreamableHttp`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStreamableHttp "MCPServerStreamableHttp") |
| Talk to servers that implement HTTP with Server-Sent Events | **HTTP with SSE MCP servers** via [`MCPServerSse`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerSse "MCPServerSse") |
| Launch a local process and communicate over stdin/stdout | **stdio MCP servers** via [`MCPServerStdio`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStdio "MCPServerStdio") |

The sections below walk through each option, how to configure it, and when to prefer one transport over another.

## 1\. Hosted MCP server tools

Hosted tools push the entire tool round-trip into OpenAI's infrastructure. Instead of your code listing and calling tools, the
[`HostedMCPTool`](https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.HostedMCPTool "HostedMCPTool            dataclass   ") forwards a server label (and optional connector metadata) to the Responses API. The
model lists the remote server's tools and invokes them without an extra callback to your Python process. Hosted tools currently
work with OpenAI models that support the Responses API's hosted MCP integration.

### Basic hosted MCP tool

Create a hosted tool by adding a [`HostedMCPTool`](https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.HostedMCPTool "HostedMCPTool            dataclass   ") to the agent's `tools` list. The `tool_config`
dict mirrors the JSON you would send to the REST API:

```
import asyncio

from agents import Agent, HostedMCPTool, Runner

async def main() -> None:
    agent = Agent(
        name="Assistant",
        tools=[\
            HostedMCPTool(\
                tool_config={\
                    "type": "mcp",\
                    "server_label": "gitmcp",\
                    "server_url": "https://gitmcp.io/openai/codex",\
                    "require_approval": "never",\
                }\
            )\
        ],
    )

    result = await Runner.run(agent, "Which language is this repository written in?")
    print(result.final_output)

asyncio.run(main())
```

The hosted server exposes its tools automatically; you do not add it to `mcp_servers`.

### Streaming hosted MCP results

Hosted tools support streaming results in exactly the same way as function tools. Pass `stream=True` to `Runner.run_streamed` to
consume incremental MCP output while the model is still working:

```
result = Runner.run_streamed(agent, "Summarise this repository's top languages")
async for event in result.stream_events():
    if event.type == "run_item_stream_event":
        print(f"Received: {event.item}")
print(result.final_output)
```

### Optional approval flows

If a server can perform sensitive operations you can require human or programmatic approval before each tool execution. Configure
`require_approval` in the `tool_config` with either a single policy (`"always"`, `"never"`) or a dict mapping tool names to
policies. To make the decision inside Python, provide an `on_approval_request` callback.

```
from agents import MCPToolApprovalFunctionResult, MCPToolApprovalRequest

SAFE_TOOLS = {"read_project_metadata"}

def approve_tool(request: MCPToolApprovalRequest) -> MCPToolApprovalFunctionResult:
    if request.data.name in SAFE_TOOLS:
        return {"approve": True}
    return {"approve": False, "reason": "Escalate to a human reviewer"}

agent = Agent(
    name="Assistant",
    tools=[\
        HostedMCPTool(\
            tool_config={\
                "type": "mcp",\
                "server_label": "gitmcp",\
                "server_url": "https://gitmcp.io/openai/codex",\
                "require_approval": "always",\
            },\
            on_approval_request=approve_tool,\
        )\
    ],
)
```

The callback can be synchronous or asynchronous and is invoked whenever the model needs approval data to keep running.

### Connector-backed hosted servers

Hosted MCP also supports OpenAI connectors. Instead of specifying a `server_url`, supply a `connector_id` and an access token. The
Responses API handles authentication and the hosted server exposes the connector's tools.

```
import os

HostedMCPTool(
    tool_config={
        "type": "mcp",
        "server_label": "google_calendar",
        "connector_id": "connector_googlecalendar",
        "authorization": os.environ["GOOGLE_CALENDAR_AUTHORIZATION"],
        "require_approval": "never",
    }
)
```

Fully working hosted tool samples—including streaming, approvals, and connectors—live in
[`examples/hosted_mcp`](https://github.com/openai/openai-agents-python/tree/main/examples/hosted_mcp).

## 2\. Streamable HTTP MCP servers

When you want to manage the network connection yourself, use
[`MCPServerStreamableHttp`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStreamableHttp "MCPServerStreamableHttp"). Streamable HTTP servers are ideal when you control the
transport or want to run the server inside your own infrastructure while keeping latency low.

```
import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp
from agents.model_settings import ModelSettings

async def main() -> None:
    token = os.environ["MCP_SERVER_TOKEN"]
    async with MCPServerStreamableHttp(
        name="Streamable HTTP Python Server",
        params={
            "url": "http://localhost:8000/mcp",
            "headers": {"Authorization": f"Bearer {token}"},
            "timeout": 10,
        },
        cache_tools_list=True,
        max_retry_attempts=3,
    ) as server:
        agent = Agent(
            name="Assistant",
            instructions="Use the MCP tools to answer the questions.",
            mcp_servers=[server],
            model_settings=ModelSettings(tool_choice="required"),
        )

        result = await Runner.run(agent, "Add 7 and 22.")
        print(result.final_output)

asyncio.run(main())
```

The constructor accepts additional options:

- `client_session_timeout_seconds` controls HTTP read timeouts.
- `use_structured_content` toggles whether `tool_result.structured_content` is preferred over textual output.
- `max_retry_attempts` and `retry_backoff_seconds_base` add automatic retries for `list_tools()` and `call_tool()`.
- `tool_filter` lets you expose only a subset of tools (see [Tool filtering](https://openai.github.io/openai-agents-python/mcp/#tool-filtering)).

## 3\. HTTP with SSE MCP servers

If the MCP server implements the HTTP with SSE transport, instantiate
[`MCPServerSse`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerSse "MCPServerSse"). Apart from the transport, the API is identical to the Streamable HTTP server.

```
from agents import Agent, Runner
from agents.model_settings import ModelSettings
from agents.mcp import MCPServerSse

workspace_id = "demo-workspace"

async with MCPServerSse(
    name="SSE Python Server",
    params={
        "url": "http://localhost:8000/sse",
        "headers": {"X-Workspace": workspace_id},
    },
    cache_tools_list=True,
) as server:
    agent = Agent(
        name="Assistant",
        mcp_servers=[server],
        model_settings=ModelSettings(tool_choice="required"),
    )
    result = await Runner.run(agent, "What's the weather in Tokyo?")
    print(result.final_output)
```

## 4\. stdio MCP servers

For MCP servers that run as local subprocesses, use [`MCPServerStdio`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStdio "MCPServerStdio"). The SDK spawns the
process, keeps the pipes open, and closes them automatically when the context manager exits. This option is helpful for quick
proofs of concept or when the server only exposes a command line entry point.

```
from pathlib import Path
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

current_dir = Path(__file__).parent
samples_dir = current_dir / "sample_files"

async with MCPServerStdio(
    name="Filesystem Server via npx",
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", str(samples_dir)],
    },
) as server:
    agent = Agent(
        name="Assistant",
        instructions="Use the files in the sample directory to answer questions.",
        mcp_servers=[server],
    )
    result = await Runner.run(agent, "List the files available to you.")
    print(result.final_output)
```

## Tool filtering

Each MCP server supports tool filters so that you can expose only the functions that your agent needs. Filtering can happen at
construction time or dynamically per run.

### Static tool filtering

Use [`create_static_tool_filter`](https://openai.github.io/openai-agents-python/ref/mcp/util/#agents.mcp.util.create_static_tool_filter "create_static_tool_filter") to configure simple allow/block lists:

```
from pathlib import Path

from agents.mcp import MCPServerStdio, create_static_tool_filter

samples_dir = Path("/path/to/files")

filesystem_server = MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", str(samples_dir)],
    },
    tool_filter=create_static_tool_filter(allowed_tool_names=["read_file", "write_file"]),
)
```

When both `allowed_tool_names` and `blocked_tool_names` are supplied the SDK applies the allow-list first and then removes any
blocked tools from the remaining set.

### Dynamic tool filtering

For more elaborate logic pass a callable that receives a [`ToolFilterContext`](https://openai.github.io/openai-agents-python/ref/mcp/util/#agents.mcp.util.ToolFilterContext "ToolFilterContext            dataclass   "). The callable can be
synchronous or asynchronous and returns `True` when the tool should be exposed.

```
from pathlib import Path

from agents.mcp import MCPServerStdio, ToolFilterContext

samples_dir = Path("/path/to/files")

async def context_aware_filter(context: ToolFilterContext, tool) -> bool:
    if context.agent.name == "Code Reviewer" and tool.name.startswith("danger_"):
        return False
    return True

async with MCPServerStdio(
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", str(samples_dir)],
    },
    tool_filter=context_aware_filter,
) as server:
    ...
```

The filter context exposes the active `run_context`, the `agent` requesting the tools, and the `server_name`.

## Prompts

MCP servers can also provide prompts that dynamically generate agent instructions. Servers that support prompts expose two
methods:

- `list_prompts()` enumerates the available prompt templates.
- `get_prompt(name, arguments)` fetches a concrete prompt, optionally with parameters.

```
from agents import Agent

prompt_result = await server.get_prompt(
    "generate_code_review_instructions",
    {"focus": "security vulnerabilities", "language": "python"},
)
instructions = prompt_result.messages[0].content.text

agent = Agent(
    name="Code Reviewer",
    instructions=instructions,
    mcp_servers=[server],
)
```

## Caching

Every agent run calls `list_tools()` on each MCP server. Remote servers can introduce noticeable latency, so all of the MCP
server classes expose a `cache_tools_list` option. Set it to `True` only if you are confident that the tool definitions do not
change frequently. To force a fresh list later, call `invalidate_tools_cache()` on the server instance.

## Tracing

[Tracing](https://openai.github.io/openai-agents-python/tracing/) automatically captures MCP activity, including:

1. Calls to the MCP server to list tools.
2. MCP-related information on tool calls.

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

ServerClientServerClientDiscoveryUsageChangesopt\[listChanged\]prompts/listList of promptsprompts/getPrompt contentprompts/list\_changedprompts/listUpdated prompts

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

## User Interaction Model

Resources in MCP are designed to be **application-driven**, with host applications
determining how to incorporate context based on their needs.For example, applications could:

- Expose resources through UI elements for explicit selection, in a tree or list view
- Allow the user to search through and filter available resources
- Implement automatic context inclusion, based on heuristics or the AI model’s selectionhttps://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/specification/2025-06-18/server/resource-picker.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=133fa885ef6e9c2e20049da5c33f4386However, implementations are free to expose resources through any interface pattern that
suits their needs—the protocol itself does not mandate any specific user
interaction model.

## Capabilities

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

## Protocol Messages

### Listing Resources

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

### Reading Resources

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
        "mimeType": "text/x-rust",\
        "text": "fn main() {\n    println!(\"Hello world!\");\n}"\
      }\
    ]
  }
}
```

### Resource Templates

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

### List Changed Notification

When the list of available resources changes, servers that declared the `listChanged`
capability **SHOULD** send a notification:

```
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}
```

### Subscriptions

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
    "uri": "file:///project/src/main.rs"
  }
}
```

## Message Flow

ServerClientServerClientResource DiscoveryResource AccessSubscriptionsUpdatesresources/listList of resourcesresources/readResource contentsresources/subscribeSubscription confirmednotifications/resources/updatedresources/readUpdated contents

## Data Types

### Resource

A resource definition includes:

- `uri`: Unique identifier for the resource
- `name`: The name of the resource.
- `title`: Optional human-readable name of the resource for display purposes.
- `description`: Optional description
- `mimeType`: Optional MIME type
- `size`: Optional size in bytes

### Resource Contents

Resources can contain either text or binary data:

#### Text Content

```
{
  "uri": "file:///example.txt",
  "mimeType": "text/plain",
  "text": "Resource content"
}
```

#### Binary Content

```
{
  "uri": "file:///example.png",
  "mimeType": "image/png",
  "blob": "base64-encoded-data"
}
```

### Annotations

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

## Common URI Schemes

The protocol defines several standard URI schemes. This list not
exhaustive—implementations are always free to use additional, custom URI schemes.

### https://

Used to represent a resource available on the web.Servers **SHOULD** use this scheme only when the client is able to fetch and load the
resource directly from the web on its own—that is, it doesn’t need to read the resource
via the MCP server.For other use cases, servers **SHOULD** prefer to use another URI scheme, or define a
custom one, even if the server will itself be downloading resource contents over the
internet.

### file://

Used to identify resources that behave like a filesystem. However, the resources do not
need to map to an actual physical filesystem.MCP servers **MAY** identify file:// resources with an
[XDG MIME type](https://specifications.freedesktop.org/shared-mime-info-spec/0.14/ar01s02.html#id-1.3.14),
like `inode/directory`, to represent non-regular files (such as directories) that don’t
otherwise have a standard MIME type.

### git://

Git version control integration.

### Custom URI Schemes

Custom URI schemes **MUST** be in accordance with [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986),
taking the above guidance in to account.

## Error Handling

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

## Security Considerations

1. Servers **MUST** validate all resource URIs
2. Access controls **SHOULD** be implemented for sensitive resources
3. Binary data **MUST** be properly encoded
4. Resource permissions **SHOULD** be checked before operations

</details>

<details>
<summary>scrape-firecrawl</summary>

Firecrawl converts web pages into markdown, ideal for LLM applications.

- It manages complexities: proxies, caching, rate limits, js-blocked content
- Handles dynamic content: dynamic websites, js-rendered sites, PDFs, images
- Outputs clean markdown, structured data, screenshots or html.

For details, see the [Scrape Endpoint API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Scraping a URL with Firecrawl

### /scrape endpoint

Used to scrape a URL and get its content.

### Installation

Python

Node

```
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
```

### Usage

Python

Node

cURL

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

# Scrape a website:
doc = firecrawl.scrape("https://firecrawl.dev", formats=["markdown", "html"])
print(doc)
```

For more details about the parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

### Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

```
{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",\
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",\
    "metadata": {\
      "title": "Home - Firecrawl",\
      "description": "Firecrawl crawls and converts any website into clean markdown.",\
      "language": "en",\
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",\
      "robots": "follow, index",\
      "ogTitle": "Firecrawl",\
      "ogDescription": "Turn any website into LLM-ready data.",\
      "ogUrl": "https://www.firecrawl.dev/",\
      "ogImage": "https://www.firecrawl.dev/og.png?123",\
      "ogLocaleAlternate": [],\
      "ogSiteName": "Firecrawl",\
      "sourceURL": "https://firecrawl.dev",\
      "statusCode": 200\
    }\
  }\
}\
```

## Scrape Formats

You can now choose what formats you want your output in. You can specify multiple output formats. Supported formats are:

- Markdown (`markdown`)
- Summary (`summary`)
- HTML (`html`)
- Raw HTML (`rawHtml`) (with no modifications)
- Screenshot (`screenshot`, with options like `fullPage`, `quality`, `viewport`)
- Links (`links`)
- JSON (`json`) - structured output
- Images (`images`) - extract all image URLs from the page
- Branding (`branding`) - extract brand identity and design system

Output keys will match the format you choose.

## Extract brand identity

### /scrape (with branding) endpoint

The branding format extracts comprehensive brand identity information from a webpage, including colors, fonts, typography, spacing, UI components, and more. This is useful for design system analysis, brand monitoring, or building tools that need to understand a website’s visual identity.

Python

Node

cURL

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

result = firecrawl.scrape(\
    url='https://firecrawl.dev',\
    formats=['branding']\
)

print(result['branding'])
```

### Response

The branding format returns a comprehensive `BrandingProfile` object with the following structure:

Output

```
{
  "success": true,
  "data": {
    "branding": {
      "colorScheme": "dark",
      "logo": "https://firecrawl.dev/logo.svg",
      "colors": {
        "primary": "#FF6B35",
        "secondary": "#004E89",
        "accent": "#F77F00",
        "background": "#1A1A1A",
        "textPrimary": "#FFFFFF",
        "textSecondary": "#B0B0B0"
      },
      "fonts": [
        {
          "family": "Inter"
        },
        {
          "family": "Roboto Mono"
        }
      ],
      "typography": {
        "fontFamilies": {
          "primary": "Inter",
          "heading": "Inter",
          "code": "Roboto Mono"
        },
        "fontSizes": {
          "h1": "48px",
          "h2": "36px",
          "h3": "24px",
          "body": "16px"
        },
        "fontWeights": {
          "regular": 400,
          "medium": 500,
          "bold": 700
        }
      },
      "spacing": {
        "baseUnit": 8,
        "borderRadius": "8px"
      },
      "components": {
        "buttonPrimary": {
          "background": "#FF6B35",
          "textColor": "#FFFFFF",
          "borderRadius": "8px"
        },
        "buttonSecondary": {
          "background": "transparent",
          "textColor": "#FF6B35",
          "borderColor": "#FF6B35",
          "borderRadius": "8px"
        }
      },
      "images": {
        "logo": "https://firecrawl.dev/logo.svg",
        "favicon": "https://firecrawl.dev/favicon.ico",
        "ogImage": "https://firecrawl.dev/og-image.png"
      }
    }
  }
}
```

### Branding Profile Structure

The `branding` object contains the following properties:

- `colorScheme`: The detected color scheme (`"light"` or `"dark"`)
- `logo`: URL of the primary logo
- `colors`: Object containing brand colors:
  - `primary`, `secondary`, `accent`: Main brand colors
  - `background`, `textPrimary`, `textSecondary`: UI colors
  - `link`, `success`, `warning`, `error`: Semantic colors
- `fonts`: Array of font families used on the page
- `typography`: Detailed typography information:
  - `fontFamilies`: Primary, heading, and code font families
  - `fontSizes`: Size definitions for headings and body text
  - `fontWeights`: Weight definitions (light, regular, medium, bold)
  - `lineHeights`: Line height values for different text types
- `spacing`: Spacing and layout information:
  - `baseUnit`: Base spacing unit in pixels
  - `borderRadius`: Default border radius
  - `padding`, `margins`: Spacing values
- `components`: UI component styles:
  - `buttonPrimary`, `buttonSecondary`: Button styles
  - `input`: Input field styles
- `icons`: Icon style information
- `images`: Brand images (logo, favicon, og:image)
- `animations`: Animation and transition settings
- `layout`: Layout configuration (grid, header/footer heights)
- `personality`: Brand personality traits (tone, energy, target audience)

### Combining with other formats

You can combine the branding format with other formats to get comprehensive page data:

Python

Node

cURL

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

result = firecrawl.scrape(\
    url='https://firecrawl.dev',\
    formats=['markdown', 'branding', 'screenshot']\
)

print(result['markdown'])
print(result['branding'])
print(result['screenshot'])
```

## Extract structured data

### /scrape (with json) endpoint

Used to extract structured data from scraped pages.

Python

Node

cURL

```
from firecrawl import Firecrawl
from pydantic import BaseModel

app = Firecrawl(api_key="fc-YOUR-API-KEY")

class CompanyInfo(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

result = app.scrape(\
    'https://firecrawl.dev',\
    formats=[{\
      "type": "json",\
      "schema": CompanyInfo.model_json_schema()\
    }],\
    only_main_content=False,\
    timeout=120000\
)

print(result)
```

Output:

JSON

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
        "supports_sso": true,
        "is_open_source": true,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### Extracting without schema

You can now extract without a schema by just passing a `prompt` to the endpoint. The llm chooses the structure of the data.

Python

Node

cURL

```
from firecrawl import Firecrawl

app = Firecrawl(api_key="fc-YOUR-API-KEY")

result = app.scrape(\
    'https://firecrawl.dev',\
    formats=[{\
      "type": "json",\
      "prompt": "Extract the company mission from the page."\
    }],\
    only_main_content=False,\
    timeout=120000\
)

print(result)
```

Output:

JSON

```
{
    "success": true,
    "data": {
      "json": {
        "company_mission": "AI-powered web scraping and data extraction",
      },
      "metadata": {
        "title": "Firecrawl",
        "description": "AI-powered web scraping and data extraction",
        "robots": "follow, index",
        "ogTitle": "Firecrawl",
        "ogDescription": "AI-powered web scraping and data extraction",
        "ogUrl": "https://firecrawl.dev/",
        "ogImage": "https://firecrawl.dev/og.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Firecrawl",
        "sourceURL": "https://firecrawl.dev/"
      },
    }
}
```

### JSON format options

When using the `json` format, pass an object inside `formats` with the following parameters:

- `schema`: JSON Schema for the structured output.
- `prompt`: Optional prompt to help guide extraction when a schema is present or when you prefer light guidance.

## Interacting with the page with Actions

Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.It is important to almost always use the `wait` action before/after executing other actions to give enough time for the page to load.

### Example

Python

Node

cURL

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

doc = firecrawl.scrape(\
    url="https://example.com/login",\
    formats=["markdown"],\
    actions=[\
        {"type": "write", "text": "john@example.com"},\
        {"type": "press", "key": "Tab"},\
        {"type": "write", "text": "secret"},\
        {"type": "click", "selector": 'button[type="submit"]'},\
        {"type": "wait", "milliseconds": 1500},\
        {"type": "screenshot", "fullPage": True},\
    ],\
)

print(doc.markdown, doc.screenshot)
```

### Output

JSON

```
{
  "success": true,
  "data": {
    "markdown": "Our first Launch Week is over! [See the recap 🚀](blog/firecrawl-launch-week-1-recap)...",
    "actions": {
      "screenshots": [
        "https://alttmdsdujxrfnakrkyi.supabase.co/storage/v1/object/public/media/screenshot-75ef2d87-31e0-4349-a478-fb432a29e241.png"
      ],
      "scrapes": [
        {
          "url": "https://www.firecrawl.dev/",
          "html": "<html><body><h1>Firecrawl</h1></body></html>"
        }
      ]
    },
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "http://google.com",
      "statusCode": 200
    }
  }
}
```

For more details about the actions parameters, refer to the [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/scrape).

## Location and Language

Specify country and preferred languages to get relevant content based on your target location and language preferences.

### How it works

When you specify the location settings, Firecrawl will use an appropriate proxy if available and emulate the corresponding language and timezone settings. By default, the location is set to ‘US’ if not specified.

### Usage

To use the location and language settings, include the `location` object in your request body with the following properties:

- `country`: ISO 3166-1 alpha-2 country code (e.g., ‘US’, ‘AU’, ‘DE’, ‘JP’). Defaults to ‘US’.
- `languages`: An array of preferred languages and locales for the request in order of priority. Defaults to the language of the specified location.

Python

Node

cURL

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

doc = firecrawl.scrape('https://example.com',\
    formats=['markdown'],\
    location={\
        'country': 'US',\
        'languages': ['en']\
    }\
)

print(doc)
```

For more details about supported locations, refer to the [Proxies documentation](https://docs.firecrawl.dev/features/proxies).

## Caching and maxAge

To make requests faster, Firecrawl serves results from cache by default when a recent copy is available.

- **Default freshness window**: `maxAge = 172800000` ms (2 days). If a cached page is newer than this, it’s returned instantly; otherwise, the page is scraped and then cached.
- **Performance**: This can speed up scrapes by up to 5x when data doesn’t need to be ultra-fresh.
- **Always fetch fresh**: Set `maxAge` to `0`.
- **Avoid storing**: Set `storeInCache` to `false` if you don’t want Firecrawl to cache/store results for this request.

Example (force fresh content):

Python

Node

cURL

```
from firecrawl import Firecrawl
firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

doc = firecrawl.scrape(url='https://example.com', maxAge=0, formats=['markdown'])
print(doc)
```

Example (use a 10-minute cache window):

Python

Node

cURL

```
from firecrawl import Firecrawl
firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

doc = firecrawl.scrape(url='https://example.com', maxAge=600000, formats=['markdown', 'html'])
print(doc)
```

## Batch scraping multiple URLs

You can now batch scrape multiple URLs at the same time. It takes the starting URLs and optional parameters as arguments. The params argument allows you to specify additional options for the batch scrape job, such as the output formats.

### How it works

It is very similar to how the `/crawl` endpoint works. It submits a batch scrape job and returns a job ID to check the status of the batch scrape.The sdk provides 2 methods, synchronous and asynchronous. The synchronous method will return the results of the batch scrape job, while the asynchronous method will return a job ID that you can use to check the status of the batch scrape.

### Usage

Python

Node

cURL

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

job = firecrawl.batch_scrape([\
    "https://firecrawl.dev",\
    "https://docs.firecrawl.dev",\
], formats=["markdown"], poll_interval=2, wait_timeout=120)

print(job)
```

### Response

If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.

#### Synchronous

Completed

```
{
  "status": "completed",
  "total": 36,
  "completed": 36,
  "creditsUsed": 36,
  "expiresAt": "2024-00-00T00:00:00.000Z",
  "next": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789?skip=26",
  "data": [
    {
      "markdown": "[Firecrawl Docs home pagehttps://mintlify.s3-us-west-1.amazonaws.com/firecrawl/logo/light.svg!...",
      "html": "<!DOCTYPE html><html lang=\"en\" class=\"js-focus-visible lg:[--scroll-mt:9.5rem]\" data-js-focus-visible=\"\">...",
      "metadata": {
        "title": "Build a 'Chat with website' using Groq Llama 3 | Firecrawl",
        "language": "en",
        "sourceURL": "https://docs.firecrawl.dev/learn/rag-llama3",
        "description": "Learn how to use Firecrawl, Groq Llama 3, and Langchain to build a 'Chat with your website' bot.",
        "ogLocaleAlternate": [],
        "statusCode": 200
      }
    },
    ...
  ]
}
```

#### Asynchronous

You can then use the job ID to check the status of the batch scrape by calling the `/batch/scrape/{id}` endpoint. This endpoint is meant to be used while the job is still running or right after it has completed **as batch scrape jobs expire after 24 hours**.

```
{
  "success": true,
  "id": "123-456-789",
  "url": "https://api.firecrawl.dev/v2/batch/scrape/123-456-789"
}
```

## Stealth Mode

For websites with advanced anti-bot protection, Firecrawl offers a stealth proxy mode that provides better success rates at scraping challenging sites.Learn more about [Stealth Mode](https://docs.firecrawl.dev/features/stealth-mode).

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

ServerClientLLMServerClientLLMDiscoveryTool SelectionInvocationUpdatestools/listList of toolsSelect tool to usetools/callTool resultProcess resulttools/list\_changedtools/listUpdated tools

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

1. **Protocol Errors**: Standard JSON-RPC errors for issues like:   - Unknown tools
   - Invalid arguments
   - Server errors
2. **Tool Execution Errors**: Reported in tool results with `isError: true`:   - API failures
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

1. Servers **MUST**:   - Validate all tool inputs
   - Implement proper access controls
   - Rate limit tool invocations
   - Sanitize tool outputs
2. Clients **SHOULD**:   - Prompt for user confirmation on sensitive operations
   - Show tool inputs to the user before calling the server, to avoid malicious or
     accidental data exfiltration
   - Validate tool results before passing to LLM
   - Implement timeouts for tool calls
   - Log tool usage for audit purposes

</details>

<details>
<summary>video-understanding-gemini-api-google-ai-for-developers</summary>

# Video understanding

Gemini models can process videos, enabling many frontier developer use cases
that would have historically required domain specific models.
Some of Gemini's vision capabilities include the ability to:

- Describe, segment, and extract information from videos
- Answer questions about video content
- Refer to specific timestamps within a video

Gemini was built to be multimodal from the ground up and we continue to push the
frontier of what is possible. This guide shows how to use the Gemini API to
generate text responses based on video inputs.

## Video input

You can provide videos as input to Gemini in the following ways:

- [Upload a video file](https://ai.google.dev/gemini-api/docs/video-understanding#upload-video) using the File API before making a
request to `generateContent`. Use this method for files larger than 20MB, videos
longer than approximately 1 minute, or when you want to reuse the file across
multiple requests.
- [Pass inline video data](https://ai.google.dev/gemini-api/docs/video-understanding#inline-video) with the request to `generateContent`. Use this method for smaller files (<20MB) and shorter durations.
- [Pass YouTube URLs](https://ai.google.dev/gemini-api/docs/video-understanding#youtube) as part of your `generateContent` request.

### Upload a video file

You can use the [Files API](https://ai.google.dev/gemini-api/docs/files) to upload a video file.
Always use the Files API when the total request size (including the file, text
prompt, system instructions, etc.) is larger than 20 MB, the video duration is
significant, or if you intend to use the same video in multiple prompts.
The File API accepts video file formats directly.

The following code downloads the sample video, uploads it using the File API,
waits for it to be processed, and then uses the file reference in
a `generateContent` request.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)More

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.mp4",
    config: { mimeType: "video/mp4" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: createUserContent([\
      createPartFromUri(myfile.uri, myfile.mimeType),\
      "Summarize this video. Then create a quiz with an answer key based on the information in this video.",\
    ]),
  });
  console.log(response.text);
}

await main();
```

```
uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.mp4", nil)

parts := []*genai.Part{
    genai.NewPartFromText("Summarize this video. Then create a quiz with an answer key based on the information in this video."),
    genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-2.5-flash",
    contents,
    nil,
)

fmt.Println(result.Text())
```

```
VIDEO_PATH="path/to/sample.mp4"
MIME_TYPE=$(file -b --mime-type "${VIDEO_PATH}")
NUM_BYTES=$(wc -c < "${VIDEO_PATH}")
DISPLAY_NAME=VIDEO

tmp_header_file=upload-header.tmp

echo "Starting file upload..."
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D ${tmp_header_file} \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

echo "Uploading video data..."
curl "${upload_url}" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${VIDEO_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

echo "File uploaded successfully. File URI: ${file_uri}"

# --- 3. Generate content using the uploaded video file ---
echo "Generating content from video..."
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},\
          {"text": "Summarize this video. Then create a quiz with an answer key based on the information in this video."}]\
        }]
      }' 2> /dev/null > response.json

jq -r ".candidates[].content.parts[].text" response.json
```

To learn more about working with media files, see
[Files API](https://ai.google.dev/gemini-api/docs/files).

### Pass video data inline

Instead of uploading a video file using the File API, you can pass smaller
videos directly in the request to `generateContent`. This is suitable for
shorter videos under 20MB total request size.

Here's an example of providing inline video data:

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)More

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-2.5-flash',
    contents=types.Content(
        parts=[\
            types.Part(\
                inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
```

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64VideoFile = fs.readFileSync("path/to/small-sample.mp4", {
  encoding: "base64",
});

const contents = [\
  {\
    inlineData: {\
      mimeType: "video/mp4",\
      data: base64VideoFile,\
    },\
  },\
  { text: "Please summarize the video in 3 sentences." }\
];

const response = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: contents,
});
console.log(response.text);
```

```
VIDEO_PATH=/path/to/your/video.mp4

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
            {\
              "inline_data": {\
                "mime_type":"video/mp4",\
                "data": "'$(base64 $B64FLAGS $VIDEO_PATH)'"\
              }\
            },\
            {"text": "Please summarize the video in 3 sentences."}\
        ]\
      }]
    }' 2> /dev/null
```

### Pass YouTube URLs

You can pass YouTube URLs directly to Gemini API as part of your `generateContent`request as follows:

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)More

```
response = client.models.generate_content(
    model='models/gemini-2.5-flash',
    contents=types.Content(
        parts=[\
            types.Part(\
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=9hE5-98ZeCg')\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
```

```
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GOOGLE_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });
const result = await model.generateContent([\
  "Please summarize the video in 3 sentences.",\
  {\
    fileData: {\
      fileUri: "https://www.youtube.com/watch?v=9hE5-98ZeCg",\
    },\
  },\
]);
console.log(result.response.text());
```

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  parts := []*genai.Part{
      genai.NewPartFromText("Please summarize the video in 3 sentences."),
      genai.NewPartFromURI("https://www.youtube.com/watch?v=9hE5-98ZeCg","video/mp4"),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-2.5-flash",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
            {"text": "Please summarize the video in 3 sentences."},\
            {\
              "file_data": {\
                "file_uri": "https://www.youtube.com/watch?v=9hE5-98ZeCg"\
              }\
            }\
        ]\
      }]
    }' 2> /dev/null
```

**Limitations:**

- For the free tier, you can't upload more than 8 hours of YouTube video per day.
- For the paid tier, there is no limit based on video length.
- For models prior to Gemini 2.5, you can upload only 1 video per request. For Gemini 2.5 and later models, you can upload a maximum of 10 videos per request.
- You can only upload public videos (not private or unlisted videos).

## Refer to timestamps in the content

You can ask questions about specific points in time within the video using
timestamps of the form `MM:SS`.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)More

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

```
const prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?";
```

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
         // Adjusted timestamps for the NASA video
        genai.NewPartFromText("What are the examples given at 00:05 and " +
            "00:10 supposed to show us?"),
    }
```

```
PROMPT="What are the examples given at 00:05 and 00:10 supposed to show us?"
```

## Extract detailed insights from video

Gemini models offer powerful capabilities for understanding video content by
processing information from both the audio and visual streams. This lets you
extract a rich set of details, including generating descriptions of what is
happening in a video and answering questions about its content. For visual
descriptions, the model samples the video at a rate of **1 frame per second**.
This sampling rate may affect the level of detail in the descriptions,
particularly for videos with rapidly changing visuals.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding#rest)More

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

```
const prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments.";
```

```
    prompt := []*genai.Part{
        genai.NewPartFromURI(currentVideoFile.URI, currentVideoFile.MIMEType),
        genai.NewPartFromText("Describe the key events in this video, providing both audio and visual details. " +
      "Include timestamps for salient moments."),
    }
```

```
PROMPT="Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Customize video processing

You can customize video processing in the Gemini API by setting clipping
intervals or providing custom frame rate sampling.

### Set clipping intervals

You can clip video by specifying `videoMetadata` with start and end offsets.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding#javascript)More

```
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-2.5-flash',
    contents=types.Content(
        parts=[\
            types.Part(\
                file_data=types.FileData(file_uri='https://www.youtube.com/watch?v=XEzRZ35urlk'),\
                video_metadata=types.VideoMetadata(\
                    start_offset='1250s',\
                    end_offset='1570s'\
                )\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
```

```
import { GoogleGenAI } from '@google/genai';
const ai = new GoogleGenAI({});
const model = 'gemini-2.5-flash';

async function main() {
const contents = [\
  {\
    role: 'user',\
    parts: [\
      {\
        fileData: {\
          fileUri: 'https://www.youtube.com/watch?v=9hE5-98ZeCg',\
          mimeType: 'video/*',\
        },\
        videoMetadata: {\
          startOffset: '40s',\
          endOffset: '80s',\
        }\
      },\
      {\
        text: 'Please summarize the video in 3 sentences.',\
      },\
    ],\
  },\
];

const response = await ai.models.generateContent({
  model,
  contents,
});

console.log(response.text)

}

await main();
```

### Set a custom frame rate

You can set custom frame rate sampling by passing an `fps` argument to
`videoMetadata`.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding#python)More

```
from google import genai
from google.genai import types

# Only for videos of size <20Mb
video_file_name = "/path/to/your/video.mp4"
video_bytes = open(video_file_name, 'rb').read()

client = genai.Client()
response = client.models.generate_content(
    model='models/gemini-2.5-flash',
    contents=types.Content(
        parts=[\
            types.Part(\
                inline_data=types.Blob(\
                    data=video_bytes,\
                    mime_type='video/mp4'),\
                video_metadata=types.VideoMetadata(fps=5)\
            ),\
            types.Part(text='Please summarize the video in 3 sentences.')\
        ]
    )
)
```

By default 1 frame per second (FPS) is sampled from the video. You might want to
set low FPS (< 1) for long videos. This is especially useful for mostly static
videos (e.g. lectures). If you want to capture more details in rapidly changing
visuals, consider setting a higher FPS value.

## Supported video formats

Gemini supports the following video format MIME types:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/avi`
- `video/x-flv`
- `video/mpg`
- `video/webm`
- `video/wmv`
- `video/3gpp`

## Technical details about videos

- **Supported models & context**: All Gemini 2.0 and 2.5 models can process video data.

  - Models with a 2M context window can process videos up to 2 hours long at
    default media resolution or 6 hours long at low media resolution, while
    models with a 1M context window can process videos up to 1 hour long at
    default media resolution or 3 hours long at low media resolution.
- **File API processing**: When using the File API, videos are stored at 1
frame per second (FPS) and audio is processed at 1Kbps (single channel).
Timestamps are added every second.

  - These rates are subject to change in the future for improvements in inference.
  - You can override the 1 FPS sampling rate by [setting a custom frame rate](https://ai.google.dev/gemini-api/docs/video-understanding#custom-frame-rate).
- **Token calculation**: Each second of video is tokenized as follows:

  - Individual frames (sampled at 1 FPS):
    - If [`mediaResolution`](https://ai.google.dev/api/generate-content#MediaResolution) is set
      to low, frames are tokenized at 66 tokens per frame.
    - Otherwise, frames are tokenized at 258 tokens per frame.
  - Audio: 32 tokens per second.
  - Metadata is also included.
  - Total: Approximately 300 tokens per second of video at default media resolution, or 100 tokens per second of video at low media resolution.
- **Timestamp format**: When referring to specific moments in a video within your prompt, use the `MM:SS` format (e.g., `01:15` for 1 minute and 15 seconds).
- **Best practices**:

  - Use only one video per prompt request for optimal results.
  - If combining text and a single video, place the text prompt _after_ the video part in the `contents` array.
  - Be aware that fast action sequences might lose detail due to the 1 FPS sampling rate. Consider slowing down such clips if necessary.

## What's next

This guide shows how to upload video files and generate text outputs from video
inputs. To learn more, see the following resources:

- [System instructions](https://ai.google.dev/gemini-api/docs/text-generation#system-instructions):
System instructions let you steer the behavior of the model based on your
specific needs and use cases.
- [Files API](https://ai.google.dev/gemini-api/docs/files): Learn more about uploading and managing
files for use with Gemini.
- [File prompting strategies](https://ai.google.dev/gemini-api/docs/files#prompt-guide): The
Gemini API supports prompting with text, image, audio, and video data, also
known as multimodal prompting.
- [Safety guidance](https://ai.google.dev/gemini-api/docs/safety-guidance): Sometimes generative
AI models produce unexpected outputs, such as outputs that are inaccurate,
biased, or offensive. Post-processing and human evaluation are essential to
limit the risk of harm from such outputs.

</details>

<details>
<summary>video-understanding-generative-ai-on-vertex-ai-google-cloud</summary>

# Video understanding

You can add videos to Gemini requests to perform tasks that involve
understanding the contents of the included videos. This page
shows you how to add videos to your requests to Gemini in
Vertex AI by using the Google Cloud console and the Vertex AI API.

## Supported models

The following table lists the models that support video understanding:

| **Model** | **Media details** | **MIME types** |
| --- | --- | --- |
| [Gemini 2.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash)<br> <br> (Preview) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| [Gemini 2.5 Flash-Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite)<br> <br> (Preview) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| [Gemini 2.5 Flash-Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-lite) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| [Gemini 2.5 Flash with Live API native audio](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-live-api)<br> <br> (Preview) | - Standard resolution:<br>   768 x 768 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| [Gemini 2.0 Flash with Live API](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash#live-api)<br> <br> (Preview) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10<br>   <br>- Maximum tokens per minute (TPM):<br>   <br>    - <br>       High/Medium/Default media resolution:<br>       <br>          - <br>             US/Asia:<br>             37.9 M<br>             <br>             <br>          - <br>             EU:<br>             9.5 M<br>    - <br>       Low media resolution:<br>       <br>          - <br>             US/Asia:<br>             1 G<br>             <br>             <br>          - <br>             EU:<br>             2.5 M | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| [Gemini 2.0 Flash with image generation](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash)<br> <br> (Preview) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10<br>   <br>- Maximum tokens per minute (TPM):<br>   <br>    - <br>       High/Medium/Default media resolution:<br>       <br>          - <br>             US/Asia:<br>             37.9 M<br>             <br>             <br>          - <br>             EU:<br>             9.5 M<br>    - <br>       Low media resolution:<br>       <br>          - <br>             US/Asia:<br>             1 G<br>             <br>             <br>          - <br>             EU:<br>             2.5 M |  |
| [Gemini 2.5 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-pro) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| [Gemini 2.5 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10 | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| [Gemini 2.0 Flash](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10<br>   <br>- Maximum tokens per minute (TPM):<br>   <br>    - <br>       High/Medium/Default media resolution:<br>       <br>          - <br>             US/Asia:<br>             38 M<br>             <br>             <br>          - <br>             EU:<br>             10 M<br>    - <br>       Low media resolution:<br>       <br>          - <br>             US/Asia:<br>             10 M<br>             <br>             <br>          - <br>             EU:<br>             2.5 M | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |
| [Gemini 2.0 Flash-Lite](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-0-flash-lite) | - Maximum video length (with audio):<br>   Approximately 45 minutes<br>   <br>- Maximum video length (without audio):<br>   Approximately 1 hour<br>   <br>- Maximum number of videos per prompt:<br>   10<br>   <br>- Maximum tokens per minute (TPM):<br>   <br>    - <br>       High/Medium/Default media resolution:<br>       <br>          - <br>             US/Asia:<br>             6.3 M<br>             <br>             <br>          - <br>             EU:<br>             3.2 M<br>    - <br>       Low media resolution:<br>       <br>          - <br>             US/Asia:<br>             3.2 M<br>             <br>             <br>          - <br>             EU:<br>             3.2 M | - `video/x-flv`<br>- `video/quicktime`<br>- `video/mpeg`<br>- `video/mpegs`<br>- `video/mpg`<br>- `video/mp4`<br>- `video/webm`<br>- `video/wmv`<br>- `video/3gpp` |

The quota metric is
`generate_content_video_input_per_base_model_id_and_resolution`.

For a list of languages supported by Gemini models, see model information
[Google models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models). To learn
more about how to design multimodal prompts, see
[Design multimodal prompts](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/design-multimodal-prompts).
If you're looking for a way to use Gemini directly from your mobile and
web apps, see the
[Firebase AI Logic client SDKs](https://firebase.google.com/docs/ai-logic) for
Swift, Android, Web, Flutter, and Unity apps.

## Add videos to a request

You can add a single video or multiple videos in your request to Gemini and the
video can include audio.

### Single video

The sample code in each of the following tabs shows a different way to identify
what's in a video. This sample works with all Gemini multimodal models.

[Console](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#console)[Python](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#python-gen-ai-sdk)[Go](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#go-gen-ai-sdk)[Java](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#java-gen-ai-sdk)[Node.js](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#node.js-gen-ai-sdk)[REST](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#rest)

To send a multimodal prompt by using the Google Cloud console, do the
following:

01. In the Vertex AI section of the Google Cloud console, go to
     the **Vertex AI Studio** page.

02. Click **Create prompt**.

03. Optional: Configure the model and parameters:

    - **Model**: Select a model.
04. Optional: To configure advanced parameters, click **Advanced** and
     configure as follows:

- **Top-K**: Use the slider or textbox to enter a value for top-K.

Top-K changes how the model selects tokens for output. A top-K of
`1` means the next selected token is the most probable among all
tokens in the model's vocabulary (also called greedy decoding), while a top-K of
`3` means that the next token is selected from among the three most
probable tokens by using temperature.

For each token selection step, the top-K tokens with the highest
probabilities are sampled. Then tokens are further filtered based on top-P with
the final token selected using temperature sampling.

Specify a lower value for less random responses and a higher value for more
random responses.

- **Top-P**: Use the slider or textbox to enter a value for top-P.
Tokens are selected from most probable to the least until the sum of their
probabilities equals the value of top-P. For the least variable results,
set top-P to `0`.
- **Max responses**: Use the slider or textbox to enter a value for
the number of responses to generate.
- **Streaming responses**: Enable to print responses as they're
generated.
- **Safety filter threshold**: Select the threshold of how likely you
are to see responses that could be harmful.
- **Enable Grounding**: Grounding isn't supported for multimodal
prompts.
- **Region**: Select the region that you want to use.
- **Temperature**: Use the slider or textbox to enter a value for
temperature.

```

The temperature is used for sampling during response generation, which occurs when topP
and topK are applied. Temperature controls the degree of randomness in token selection.
Lower temperatures are good for prompts that require a less open-ended or creative response, while
higher temperatures can lead to more diverse or creative results. A temperature of 0
means that the highest probability tokens are always selected. In this case, responses for a given
prompt are mostly deterministic, but a small amount of variation is still possible.

If the model returns a response that's too generic, too short, or the model gives a fallback
response, try increasing the temperature. If the model enters infinite generation, increasing the
temperature to at least 0.1 may lead to improved results.
1.0 is the
recommended starting value for temperature.

    <li>**Output token limit**: Use the slider or textbox to enter a value for
      the max output limit.


Maximum number of tokens that can be generated in the response. A token is
approximately four characters. 100 tokens correspond to roughly 60-80 words.

Specify a lower value for shorter responses and a higher value for potentially longer
responses.


    <li>**Add stop sequence**: Optional. Enter a stop sequence, which is a
      series of characters that includes spaces. If the model encounters a
      stop sequence, the response generation stops. The stop sequence isn't
      included in the response, and you can add up to five stop sequences.
</ul>
```

05. Click **Insert Media**, and select a source for your file.

    [Upload](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#upload)[By URL](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#by-url)[YouTube](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#youtube)[Cloud Storage](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#cloud-storage)[Google Drive](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#google-drive)

    Select the file that you want to upload and click **Open**.

    Enter the URL of the file that you want to use and click **Insert**.

    Enter the URL of the YouTube video that you want to use and click
    **Insert**.

    You can use any public video or a video that's owned by the account that
    you used to sign in to the Google Cloud console.

    Select the bucket and then the file from the bucket that
    you want to import and click **Select**.

1. Choose an account and give consent to
Vertex AI Studio to access your account the first
time you select this option. You can upload multiple files that
have a total size of up to 10 MB. A single file can't exceed
7 MB.
2. Click the file that you want to add.
3. Click **Select**.

The file thumbnail displays in the **Prompt** pane. The total
number of tokens also displays. If your prompt data exceeds the
[token limit](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-models), the
tokens are truncated and aren't included in processing your data.

06. Enter your text prompt in the **Prompt** pane.

07. Optional: To view the **Token ID to text** and **Token IDs**, click the
     **tokens count** in the **Prompt** pane.

08. Click **Submit**.

09. Optional: To save your prompt to **My prompts**, click save\_alt **Save**.

10. Optional: To get the Python code or a curl command for your prompt, click
     code **Build with code > Get code**.

#### Install

```
pip install --upgrade google-genai
```

To learn more, see the
[SDK reference documentation](https://googleapis.github.io/python-genai/).

Set environment variables to use the Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_VERTEXAI=True
```

```
from google import genai
from google.genai.types import HttpOptions, Part

client = genai.Client(http_options=HttpOptions(api_version="v1"))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[\
        Part.from_uri(\
            file_uri="gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",\
            mime_type="video/mp4",\
        ),\
        "What is in the video?",\
    ],
)
print(response.text)
# Example response:
# The video shows several people surfing in an ocean with a coastline in the background. The camera ...
```

Learn how to install or update the [Go](https://cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview).

To learn more, see the
[SDK reference documentation](https://pkg.go.dev/google.golang.org/genai).

Set environment variables to use the Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_VERTEXAI=True
```

```
import (
	"context"
	"fmt"
	"io"

	genai "google.golang.org/genai"
)

// generateWithMuteVideo shows how to generate text using a video with no sound as the input.
func generateWithMuteVideo(w io.Writer) error {
	ctx := context.Background()

	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		HTTPOptions: genai.HTTPOptions{APIVersion: "v1"},
	})
	if err != nil {
		return fmt.Errorf("failed to create genai client: %w", err)
	}

	modelName := "gemini-2.5-flash"
	contents := []*genai.Content{
		{Parts: []*genai.Part{
			{Text: "What is in the video?"},
			{FileData: &genai.FileData{
				FileURI:  "gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",
				MIMEType: "video/mp4",
			}},
		},
			Role: "user"},
	}

	resp, err := client.Models.GenerateContent(ctx, modelName, contents, nil)
	if err != nil {
		return fmt.Errorf("failed to generate content: %w", err)
	}

	respText := resp.Text()

	fmt.Fprintln(w, respText)

	// Example response:
	// The video shows several surfers riding waves in an ocean setting. The waves are ...

	return nil
}
```

Learn how to install or update the [Java](https://cloud.google.com/vertex-ai/generative-ai/docs/sdks/overview).

To learn more, see the
[SDK reference documentation](https://central.sonatype.com/artifact/com.google.genai/google-genai).

Set environment variables to use the Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_VERTEXAI=True
```

```

import com.google.genai.Client;
import com.google.genai.types.Content;
import com.google.genai.types.GenerateContentResponse;
import com.google.genai.types.HttpOptions;
import com.google.genai.types.Part;

public class TextGenerationWithMuteVideo {

  public static void main(String[] args) {
    // TODO(developer): Replace these variables before running the sample.
    String modelId = "gemini-2.5-flash";
    generateContent(modelId);
  }

  // Generates text with mute video input
  public static String generateContent(String modelId) {
    // Initialize client that will be used to send requests. This client only needs to be created
    // once, and can be reused for multiple requests.
    try (Client client =
        Client.builder()
            .location("global")
            .vertexAI(true)
            .httpOptions(HttpOptions.builder().apiVersion("v1").build())
            .build()) {

      GenerateContentResponse response =
          client.models.generateContent(
              modelId,
              Content.fromParts(
                  Part.fromUri(
                      "gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",
                      "video/mp4"),
                  Part.fromText("What is in this video?")),
              null);

      System.out.print(response.text());
      // Example response:
      // This video features **surfers in the ocean**.
      //
      // The main focus is on **one individual who catches and rides a wave**, executing various
      // turns and maneuvers as the wave breaks and dissipates into whitewater...
      return response.text();
    }
  }
}
```

#### Install

```
npm install @google/genai
```

To learn more, see the
[SDK reference documentation](https://googleapis.github.io/js-genai/).

Set environment variables to use the Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_VERTEXAI=True
```

```
const {GoogleGenAI} = require('@google/genai');

const GOOGLE_CLOUD_PROJECT = process.env.GOOGLE_CLOUD_PROJECT;
const GOOGLE_CLOUD_LOCATION = process.env.GOOGLE_CLOUD_LOCATION || 'global';

async function generateText(
  projectId = GOOGLE_CLOUD_PROJECT,
  location = GOOGLE_CLOUD_LOCATION
) {
  const client = new GoogleGenAI({
    vertexai: true,
    project: projectId,
    location: location,
  });

  const response = await client.models.generateContent({
    model: 'gemini-2.5-flash',
    contents: [\
      {\
        role: 'user',\
        parts: [\
          {\
            fileData: {\
              mimeType: 'video/mp4',\
              fileUri:\
                'gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4',\
            },\
          },\
          {\
            text: 'What is in the video?',\
          },\
        ],\
      },\
    ],
  });

  console.log(response.text);

  // Example response:
  // The video shows several people surfing in an ocean with a coastline in the background. The camera ...

  return response.text;
}
```

After you
[set up your environment](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal#gemini-setup-environment-drest),
you can use REST to test a text prompt. The following sample sends a request to the publisher
model endpoint.

Before using any of the request data,
make the following replacements:

- `PROJECT_ID`: Your [project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
- `FILE_URI`:
The URI or URL of the file to include in the prompt. Acceptable values include the following:

  - **Cloud Storage bucket URI:** The object must either be publicly readable or reside in
     the same Google Cloud project that's sending the request. For `gemini-2.0-flash`
     and `gemini-2.0-flash-lite`, the size limit is 2 GB.
  - **HTTP URL:** The file URL must be publicly readable. You can specify one video file, one
     audio file, and up to 10 image files per request. Audio files, video files, and documents can't
     exceed 15 MB.
  - **YouTube video URL:** The YouTube video must be either owned by the account that you used
     to sign in to the Google Cloud console or is public. Only one YouTube video URL is supported per
     request.

When specifying a `fileURI`, you must also specify the media type
(`mimeType`) of the file. If VPC Service Controls is enabled, specifying a media file
URL for `fileURI` is not supported.

If you don't have a video file in Cloud Storage, then you can use the following
publicly available file:
`gs://cloud-samples-data/video/animals.mp4` with a mime type of
`video/mp4`. To view this video,
[open the sample MP4](https://storage.googleapis.com/cloud-samples-data/video/animals.mp4)
file.

- `MIME_TYPE`:
The media type of the file specified in the `data` or `fileUri`
fields. Acceptable values include the following:

- `application/pdf`
- `audio/mpeg`
- `audio/mp3`
- `audio/wav`
- `image/png`
- `image/jpeg`
- `image/webp`
- `text/plain`
- `video/mov`
- `video/mpeg`
- `video/mp4`
- `video/mpg`
- `video/avi`
- `video/wmv`
- `video/mpegps`
- `video/flv`

- `TEXT`:
The text instructions to include in the prompt.
For example,
`What is in the video?`

To send your request, choose one of these options:

[curl](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#curl)[PowerShell](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#powershell)

Save the request body in a file named `request.json`.
Run the following command in the terminal to create or overwrite
this file in the current directory:

```
cat > request.json << 'EOF'
{
  "contents": {
    "role": "USER",
    "parts": [\
      {\
        "fileData": {\
          "fileUri": "FILE_URI",\
          "mimeType": "MIME_TYPE"\
        }\
      },\
      {\
        "text": "TEXT"\
      }\
    ]
  }
}
EOF
```

Then execute the following command to send your REST request:

```
curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d @request.json \
     "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-2.5-flash:generateContent"
```

Save the request body in a file named `request.json`.
Run the following command in the terminal to create or overwrite
this file in the current directory:

```
@'
{
  "contents": {
    "role": "USER",
    "parts": [\
      {\
        "fileData": {\
          "fileUri": "FILE_URI",\
          "mimeType": "MIME_TYPE"\
        }\
      },\
      {\
        "text": "TEXT"\
      }\
    ]
  }
}
'@  | Out-File -FilePath request.json -Encoding utf8
```

Then execute the following command to send your REST request:

```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
    -Method POST `
    -Headers $headers `
    -ContentType: "application/json; charset=utf-8" `
    -InFile request.json `
    -Uri "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-2.5-flash:generateContent" | Select-Object -Expand Content
```

You should receive a JSON response similar to the following.

**Response**

```
{
  "candidates": [\
    {\
      "content": {\
        "role": "model",\
        "parts": [\
          {\
            "text": "This video is a commercial for Google Photos, featuring animals taking selfies\
              with the Google Photos app. The commercial plays on the popularity of media in which\
              animals act like humans, especially their use of technology. The commercial also\
              highlights the app's ability to automatically back up photos."\
          }\
        ]\
      },\
      "finishReason": "STOP",\
      "safetyRatings": [\
        {\
          "category": "HARM_CATEGORY_HATE_SPEECH",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.053601142,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.053799648\
        },\
        {\
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.06278921,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.07850098\
        },\
        {\
          "category": "HARM_CATEGORY_HARASSMENT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.090253234,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.058453236\
        },\
        {\
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.1647851,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.09285216\
        }\
      ]\
    }\
  ],
  "usageMetadata": {
    "promptTokenCount": 28916,
    "candidatesTokenCount": 61,
    "totalTokenCount": 28977
  }
}
```

Note the following in the URL for this sample:

- Use the
[`generateContent`](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.publishers.models/generateContent)
method to request that the response is returned after it's fully generated.
To reduce the perception of latency to a human audience, stream the response as it's being
generated by using the
[`streamGenerateContent`](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.publishers.models/streamGenerateContent)
method.

- The multimodal model ID is located at the end of the URL before the method
(for example, `gemini-2.0-flash`). This sample might support other
models as well.

### Video with audio

The following shows you how to summarize a video file with audio and return
chapters with timestamps. This sample works with Gemini 2.0.

[Python](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#python-gen-ai-sdk)[REST](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#rest)[Console](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#console)

#### Install

```
pip install --upgrade google-genai
```

To learn more, see the
[SDK reference documentation](https://googleapis.github.io/python-genai/).

Set environment variables to use the Gen AI SDK with Vertex AI:

```
# Replace the `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION` values
# with appropriate values for your project.
export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_VERTEXAI=True
```

```
from google import genai
from google.genai.types import HttpOptions, Part

client = genai.Client(http_options=HttpOptions(api_version="v1"))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[\
        Part.from_uri(\
            file_uri="gs://cloud-samples-data/generative-ai/video/ad_copy_from_video.mp4",\
            mime_type="video/mp4",\
        ),\
        "What is in the video?",\
    ],
)
print(response.text)
# Example response:
# The video shows several people surfing in an ocean with a coastline in the background. The camera ...
```

After you
[set up your environment](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal#gemini-setup-environment-drest),
you can use REST to test a text prompt. The following sample sends a request to the publisher
model endpoint.

Before using any of the request data,
make the following replacements:

- `PROJECT_ID`: .
- `FILE_URI`:
The URI or URL of the file to include in the prompt. Acceptable values include the following:

  - **Cloud Storage bucket URI:** The object must either be publicly readable or reside in
     the same Google Cloud project that's sending the request. For `gemini-2.0-flash`
     and `gemini-2.0-flash-lite`, the size limit is 2 GB.
  - **HTTP URL:** The file URL must be publicly readable. You can specify one video file, one
     audio file, and up to 10 image files per request. Audio files, video files, and documents can't
     exceed 15 MB.
  - **YouTube video URL:** The YouTube video must be either owned by the account that you used
     to sign in to the Google Cloud console or is public. Only one YouTube video URL is supported per
     request.

When specifying a `fileURI`, you must also specify the media type
(`mimeType`) of the file. If VPC Service Controls is enabled, specifying a media file
URL for `fileURI` is not supported.

If you don't have a video file in Cloud Storage, then you can use the following
publicly available file:
`gs://cloud-samples-data/generative-ai/video/pixel8.mp4` with a mime type of
`video/mp4`. To view this video,
[open the sample MP4](https://storage.googleapis.com/cloud-samples-data/generative-ai/video/pixel8.mp4)
file.

- `MIME_TYPE`:
The media type of the file specified in the `data` or `fileUri`
fields. Acceptable values include the following:

- `application/pdf`
- `audio/mpeg`
- `audio/mp3`
- `audio/wav`
- `image/png`
- `image/jpeg`
- `image/webp`
- `text/plain`
- `video/mov`
- `video/mpeg`
- `video/mp4`
- `video/mpg`
- `video/avi`
- `video/wmv`
- `video/mpegps`
- `video/flv`

```
TEXT
```

The text instructions to include in the prompt.
For example,
`Provide a description of the video. The description should also contain anything
        important which people say in the video.`

To send your request, choose one of these options:

[curl](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#curl)[PowerShell](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#powershell)

Save the request body in a file named `request.json`.
Run the following command in the terminal to create or overwrite
this file in the current directory:

```
cat > request.json << 'EOF'
{
  "contents": {
    "role": "USER",
    "parts": [\
      {\
        "fileData": {\
          "fileUri": "FILE_URI",\
          "mimeType": "MIME_TYPE"\
        }\
      },\
      {\
        "text": "TEXT"\
      }\
    ]
  }
}
EOF
```

Then execute the following command to send your REST request:

```
curl -X POST \
     -H "Authorization: Bearer $(gcloud auth print-access-token)" \
     -H "Content-Type: application/json; charset=utf-8" \
     -d @request.json \
     "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-2.5-flash:generateContent"
```

Save the request body in a file named `request.json`.
Run the following command in the terminal to create or overwrite
this file in the current directory:

```
@'
{
  "contents": {
    "role": "USER",
    "parts": [\
      {\
        "fileData": {\
          "fileUri": "FILE_URI",\
          "mimeType": "MIME_TYPE"\
        }\
      },\
      {\
        "text": "TEXT"\
      }\
    ]
  }
}
'@  | Out-File -FilePath request.json -Encoding utf8
```

Then execute the following command to send your REST request:

```
$cred = gcloud auth print-access-token
$headers = @{ "Authorization" = "Bearer $cred" }

Invoke-WebRequest `
    -Method POST `
    -Headers $headers `
    -ContentType: "application/json; charset=utf-8" `
    -InFile request.json `
    -Uri "https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-2.5-flash:generateContent" | Select-Object -Expand Content
```

You should receive a JSON response similar to the following.

**Response**

```
{
  "candidates": [\
    {\
      "content": {\
        "role": "model",\
        "parts": [\
          {\
            "text": "The video opens with a shot of a train traveling over a bridge in the night. \n\
              \nThe scene changes to a woman walking in the streets of Tokyo. She says "My name is\
              Saeko. I am a photographer in Tokyo. Tokyo has many faces. The city at night\
              is totally different from what you see during the day. The new Pixel has a feature\
              called "Video Boost". In low light, it activates "Night Sight" to make the quality\
              even better." \n\nShe then uses her phone to take several photos of different parts of\
              the city including a street with a lot of shops, a small alleyway, and a small\
              restaurant. She says "Sancha is where I used to live when I first moved to Tokyo. I\
              have a lot of great memories here. Oh, I like this." \n\nShe smiles and says\
              "Beautiful".\n\nThe video ends with the woman standing in a different part of the\
              city. She says "Next, I came to Shibuya." The scene shows the famous Shibuya crossing\
              in the night. \n\nThe video features a woman showcasing the camera features of the\
              Google Pixel phone while walking around the streets of Tokyo. She mentions "Night\
              Sight" and "Video Boost" features. \n"\
          }\
        ]\
      },\
      "finishReason": "STOP",\
      "safetyRatings": [\
        {\
          "category": "HARM_CATEGORY_HATE_SPEECH",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.053601142,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.053799648\
        },\
        {\
          "category": "HARM_CATEGORY_DANGEROUS_CONTENT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.06278921,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.07850098\
        },\
        {\
          "category": "HARM_CATEGORY_HARASSMENT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.090253234,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.058453236\
        },\
        {\
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",\
          "probability": "NEGLIGIBLE",\
          "probabilityScore": 0.1647851,\
          "severity": "HARM_SEVERITY_NEGLIGIBLE",\
          "severityScore": 0.09285216\
        }\
      ]\
    }\
  ],
  "usageMetadata": {
    "promptTokenCount": 28916,
    "candidatesTokenCount": 61,
    "totalTokenCount": 28977
  }
}
```

Note the following in the URL for this sample:

- Use the
[`generateContent`](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.publishers.models/generateContent)
method to request that the response is returned after it's fully generated.
To reduce the perception of latency to a human audience, stream the response as it's being
generated by using the
[`streamGenerateContent`](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.publishers.models/streamGenerateContent)
method.

- The multimodal model ID is located at the end of the URL before the method
(for example, `gemini-2.0-flash`). This sample might support other
models as well.

To send a multimodal prompt by using the Google Cloud console, do the
following:

01. In the Vertex AI section of the Google Cloud console, go to
     the **Vertex AI Studio** page.

02. Click **Create prompt**.

03. Optional: Configure the model and parameters:

    - **Model**: Select a model.
04. Optional: To configure advanced parameters, click **Advanced** and
     configure as follows:

- **Top-K**: Use the slider or textbox to enter a value for top-K.

Top-K changes how the model selects tokens for output. A top-K of
`1` means the next selected token is the most probable among all
tokens in the model's vocabulary (also called greedy decoding), while a top-K of
`3` means that the next token is selected from among the three most
probable tokens by using temperature.

For each token selection step, the top-K tokens with the highest
probabilities are sampled. Then tokens are further filtered based on top-P with
the final token selected using temperature sampling.

Specify a lower value for less random responses and a higher value for more
random responses.

- **Top-P**: Use the slider or textbox to enter a value for top-P.
Tokens are selected from most probable to the least until the sum of their
probabilities equals the value of top-P. For the least variable results,
set top-P to `0`.
- **Max responses**: Use the slider or textbox to enter a value for
the number of responses to generate.
- **Streaming responses**: Enable to print responses as they're
generated.
- **Safety filter threshold**: Select the threshold of how likely you
are to see responses that could be harmful.
- **Enable Grounding**: Grounding isn't supported for multimodal
prompts.
- **Region**: Select the region that you want to use.
- **Temperature**: Use the slider or textbox to enter a value for
temperature.

```

The temperature is used for sampling during response generation, which occurs when topP
and topK are applied. Temperature controls the degree of randomness in token selection.
Lower temperatures are good for prompts that require a less open-ended or creative response, while
higher temperatures can lead to more diverse or creative results. A temperature of 0
means that the highest probability tokens are always selected. In this case, responses for a given
prompt are mostly deterministic, but a small amount of variation is still possible.

If the model returns a response that's too generic, too short, or the model gives a fallback
response, try increasing the temperature. If the model enters infinite generation, increasing the
temperature to at least 0.1 may lead to improved results.
1.0 is the
recommended starting value for temperature.

    <li>**Output token limit**: Use the slider or textbox to enter a value for
      the max output limit.


Maximum number of tokens that can be generated in the response. A token is
approximately four characters. 100 tokens correspond to roughly 60-80 words.

Specify a lower value for shorter responses and a higher value for potentially longer
responses.


    <li>**Add stop sequence**: Optional. Enter a stop sequence, which is a
      series of characters that includes spaces. If the model encounters a
      stop sequence, the response generation stops. The stop sequence isn't
      included in the response, and you can add up to five stop sequences.
</ul>
```

05. Click **Insert Media**, and select a source for your file.

    [Upload](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#upload)[By URL](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#by-url)[YouTube](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#youtube)[Cloud Storage](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#cloud-storage)[Google Drive](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding#google-drive)

    Select the file that you want to upload and click **Open**.

    Enter the URL of the file that you want to use and click **Insert**.

    Enter the URL of the YouTube video that you want to use and click
    **Insert**.

    You can use any public video or a video that's owned by the account that
    you used to sign in to the Google Cloud console.

    Select the bucket and then the file from the bucket that
    you want to import and click **Select**.

1. Choose an account and give consent to
Vertex AI Studio to access your account the first
time you select this option. You can upload multiple files that
have a total size of up to 10 MB. A single file can't exceed
7 MB.
2. Click the file that you want to add.
3. Click **Select**.

The file thumbnail displays in the **Prompt** pane. The total
number of tokens also displays. If your prompt data exceeds the
[token limit](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-models), the
tokens are truncated and aren't included in processing your data.

06. Enter your text prompt in the **Prompt** pane.

07. Optional: To view the **Token ID to text** and **Token IDs**, click the
     **tokens count** in the **Prompt** pane.

08. Click **Submit**.

09. Optional: To save your prompt to **My prompts**, click save\_alt **Save**.

10. Optional: To get the Python code or a curl command for your prompt, click
     code **Build with code > Get code**.

## Customize video processing

You can customize video processing in the Gemini for Google Cloud API by setting
clipping intervals or providing custom frame rate sampling.

### Set clipping intervals

You can clip videos by specifying
[`videoMetadata`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/Content#VideoMetadata)
with start and end offsets.

### Set a custom frame rate

You can set custom frame rate sampling by passing an `fps` argument to
`videoMetadata`.

By default 1 frame per second (FPS) is sampled from the video. You might want to
set low FPS (< 1) for long videos. This is especially useful for mostly static
videos (e.g. lectures). If you want to capture more details in rapidly changing
visuals, consider setting a higher FPS value.

## Adjust media resolution

You can adjust
[`MediaResolution`](https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.evaluationRuns#MediaResolution) to process your videos with fewer tokens.

## Set optional model parameters

Each model has a set of optional parameters that you can set. For more
information, see [Content generation parameters](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters).

## Video tokenization

Here's how tokens are calculated for video:

- The audio track is encoded with video frames. The audio track is also
broken down into 1-second trunks that each accounts for
32 tokens. The video frame and audio tokens are interleaved together with
their timestamps. The timestamps are represented as 5 tokens.

- For videos that are sampled at or below 1 frame per second (fps),
the timestamps for the first hour of video are represented as 5 tokens per
video frame. The remaining timestamps are represented as 7 tokens per
video frame.

- For videos that are sampled above 1 frame per second (fps),
the timestamps for the first hour of video are represented as 9 tokens per
video frame. The remaining timestamps are represented as 11 tokens per
video frame.

## Best practices

When using video, use the following best practices and information for the
best results:

- If your prompt contains a single video, place the video before the text
prompt.

- If you require timestamp localization in a video with audio, ask the model
to generate timestamps that follow the format as described in "Timestamp
format".

## Limitations

While Gemini multimodal models are powerful in many multimodal use
cases, it's important to understand the limitations of the models:

- **Content moderation**: The models refuse to provide answers
on videos that violate our safety policies.

- **Non-speech sound recognition**: The models that support
audio might make mistakes recognizing sound that's not speech.

## Technical details about videos

- **Supported models & context**: All Gemini 2.0 and 2.5 models can
process video data.

  - Models with a 2M context window can process videos up to 2 hours long at
    default media resolution or 6 hours long at low media resolution, while
    models with a 1M context window can process videos up to 1 hour long at
    default media resolution or 3 hours long at low media resolution.
- **File API processing**: When using the File API, videos are sampled at 1
frame per second (FPS) and audio is processed at 1Kbps (single channel).
Timestamps are added every second.

  - These rates are subject to change in the future for improvements in
    inference.
- **Token calculation**: Each second of video is tokenized as follows:

  - Individual frames (sampled at 1 FPS):

    - If [`mediaResolution`](https://cloud.google.com/api/generate-content#MediaResolution) is set
      to low, frames are tokenized at 66 tokens per frame, plus timestamp tokens.

    - Otherwise, frames are tokenized at 258 tokens per frame, plus timestamp tokens.
  - Audio: 25 tokens per second, plus timestamp tokens.

  - Metadata is also included.

  - Total: Approximately 300 tokens per second of video at default media
    resolution, or 100 tokens per second of video at low media resolution.
- **Timestamp format**: When referring to specific moments in a video within
your prompt, the timestamp format depends on your video's frame per second
(FPS) sampling rate:

  - **For sampling rates at 1 FPS or below**: Use the `MM:SS` format, where
    the first two digits represent minutes and the last two digits represent
    seconds. If you have offsets that are greater than 1 hour, use the
    `H:MM:SS` format.

  - **For sampling rates above 1 FPS**: Use the `MM:SS.sss` format, or, if
    you have offsets that are greater than 1 hour, use the
    `H:MM:SS.sss` format, described as follows:

    - The first digit represents the hour.
    - The second two digits two digits represent minutes.
    - The third two digits represent seconds.
    - The final three digits represent subseconds.
- **Best practices**:

  - Use only one video per prompt request for optimal results.

  - If combining text and a single video, place the text prompt _after_ the
    video part in the `contents` array.

  - Be aware that fast action sequences might lose detail due to the 1 FPS
    sampling rate. Consider slowing down such clips if necessary.

</details>


## Local Files

<details>
<summary>_Users_omar_Documents_ai_repos_agentic-ai-engineering-course_lessons_14_agent_system_design_nova_system_design_notes</summary>

## Nova Research Agent — System Design

### Purpose
- **What**: A research automation agent built on the Model Context Protocol (MCP), split into an MCP server that exposes research tools/resources/prompts and an MCP client that orchestrates an LLM-driven ReAct loop to call those tools.
- **Where**: Server in `src/nova/mcp_server`, client in `src/nova/mcp_client`.
- **Why**: To execute the research workflow described in `mcp_server/src/prompts/research_instructions_prompt.py` and produce a comprehensive `research.md` from guidelines and web sources.

---

## High-level architecture

### Components
- **MCP Server** (`mcp_server`)
  - Entry point: `src/nova/mcp_server/src/server.py`
    - Builds a `FastMCP` instance and registers:
      - Tools: `src/nova/mcp_server/src/routers/tools.py`
      - Resources: `src/nova/mcp_server/src/routers/resources.py`
      - Prompts: `src/nova/mcp_server/src/routers/prompts.py`
  - Tool implementations in `src/nova/mcp_server/src/tools/` call application handlers in `src/nova/mcp_server/src/app/` and use helpers in `src/nova/mcp_server/src/utils/`.
  - Configuration and constants in `src/nova/mcp_server/src/config/`.

- **MCP Client** (`mcp_client`)
  - Entry point: `src/nova/mcp_client/src/client.py`
    - Transport options:
      - In-memory: imports the server and runs it in-process
      - Stdio: spawns `uv run -m src.server --transport stdio` under the server directory
    - On startup, lists server tools/resources/prompts and prints them.
    - Interactive loop: accepts user input and orchestrates an LLM ReAct loop to decide which MCP tools to call.
  - Message/agent helpers in `src/nova/mcp_client/src/utils/`:
    - `handle_message_utils.py`: routes user commands and normal messages
    - `handle_agent_loop_utils.py`: runs the LLM/tool ReAct loop and executes tools via `client.call_tool`
    - `llm_utils.py`: prepares Gemini tool schemas from MCP tools and parses LLM responses

### Communication
- The client queries server capabilities (`list_tools`, `list_resources`, `list_prompts`) and executes tools by name (`call_tool("toolName", {args...})`).
- The client maps MCP tool metadata to Gemini function declarations so the LLM can propose function calls. Automatic function calling is disabled; the client explicitly inspects the LLM response and executes tools accordingly.

---

## How the client and server work together

1. The client starts and establishes an MCP connection (in-memory or stdio).
2. The client fetches and prints available tools/resources/prompts.
3. The user can load the workflow prompt via `/prompt/full_research_instructions_prompt`, which inserts the instructions into the conversation history.
4. The user asks for a task (e.g., “Run the full research workflow for directory X”).
5. The client starts the ReAct loop:
   - Converts MCP tools into Gemini tool schemas.
   - Calls the LLM with conversation history.
   - If the LLM proposes a function call matching an MCP tool, the client executes it via `client.call_tool` and appends the tool result to the conversation.
   - Repeats until the LLM emits a final answer instead of a function call.

Notes:
- The research prompt encourages parallelism for certain steps; the current client loop executes tools sequentially (one function call at a time). Several server tools internally run concurrent workloads (e.g., web/YT scraping), so you still get parallelism inside tool execution.

---

### Prompts
- `full_research_instructions_prompt` → returns the workflow instructions from `prompts/research_instructions_prompt.py`.

---

## Workflow mapping (from research_instructions_prompt.py)
Below, each step from the prompt is mapped to the exact tool(s) on the server with precise inputs/outputs as implemented.

### Step 1 — Setup
- User loads the instructions (optional but recommended) via `/prompt/full_research_instructions_prompt`.
- All subsequent tools require a `research_directory` that contains:
  - `article_guideline.md` (the prompt references this as `ARTICLE_GUIDELINE_FILE`)
  - A hidden `.nova/` folder that tools will create/populate as needed

### Step 1.3 — Extract URLs from guidelines
- MCP Tool: `extract_guidelines_urls(research_directory: str)`
  - Implementation: `tools/extract_guidelines_urls_tool.py`
  - Reads: `article_guideline.md`
  - Writes: `.nova/guidelines_filenames.json`
  - Output (dict):
    - `status`: "success"
    - `github_sources_count`: int
    - `youtube_sources_count`: int
    - `web_sources_count`: int
    - `local_files_count`: int
    - `output_path`: absolute path to `.nova/guidelines_filenames.json`
    - `message`: human-readable summary
  - File schema written to `.nova/guidelines_filenames.json` (keys):
    - `github_urls`: list[str]
    - `youtube_videos_urls`: list[str]
    - `other_urls`: list[str]
    - `local_file_paths`: list[str]
  - Important: Downstream tools expect different key names for local files (see callouts below).

---

## Step 2 — Process extracted resources (tools can be run independently)

### 2.1 Local files
- MCP Tool: `process_local_files(research_directory: str)`
  - Implementation: `tools/process_local_files_tool.py`
  - Reads: `.nova/guidelines_filenames.json`
  - Writes: `.nova/local_files_from_research/` copies or converted notebooks
  - Output (dict):
    - `status`: "success" or "warning" (if 0 files processed)
    - `files_processed`: int
    - `files_total`: int
    - `processed_files`: list[str] (filenames saved inside destination)
    - `warnings`: list[str]
    - `errors`: list[str]
    - `output_directory`: absolute path to `.nova/local_files_from_research/`
    - `message`: summary string
  - Expected JSON keys: The implementation uses `data.get("local_files", [])`. However, the extractor writes `local_file_paths`. If you run this step as-is, no files will be processed unless `.nova/guidelines_filenames.json` contains `local_files`. Adjustments may be required (see “Notable implementation notes”).

### 2.2 Other HTTP/HTTPS URLs (non-GitHub, non-YouTube)
- MCP Tool: `scrape_and_clean_other_urls(research_directory: str, concurrency_limit: int = 4)`
  - Implementation: `tools/scrape_and_clean_other_urls_tool.py`
  - Reads: `.nova/guidelines_filenames.json` → `other_urls`, `article_guideline.md`
  - Internals: Concurrent scraping with Firecrawl; LLM-based markdown cleaning; filenames generated safely
  - Writes: `.nova/urls_from_guidelines/*.md`
  - Output (dict):
    - `status`: "success" or "warning" (if 0 successful scrapes)
    - `urls_processed`: int (successful scrapes)
    - `urls_total`: int (attempted)
    - `files_saved`: int
    - `output_directory`: absolute path to `.nova/urls_from_guidelines/`
    - `saved_files`: list[str]
    - `message`: summary string

### 2.3 GitHub URLs
- MCP Tool: `process_github_urls(research_directory: str)`
  - Implementation: `tools/process_github_urls_tool.py`
  - Reads: `.nova/guidelines_filenames.json` → `github_urls`
  - Internals: Uses `gitingest.ingest_async` to summarize repo, tree, and content; truncates and strips base64 images; sequential by URL
  - Writes: `.nova/urls_from_guidelines_code/*.md`
  - Output (dict):
    - `status`: "success" or "warning"
    - `urls_processed`: int
    - `urls_total`: int
    - `files_saved`: int
    - `output_directory`: absolute path to `.nova/urls_from_guidelines_code/`
    - `message`: summary

### 2.4 YouTube URLs
- MCP Tool: `transcribe_youtube_urls(research_directory: str)`
  - Implementation: `tools/transcribe_youtube_videos_tool.py`
  - Reads: `.nova/guidelines_filenames.json` → `youtube_videos_urls`
  - Internals: Gemini-based transcription with retries, limited concurrency
  - Writes: `.nova/urls_from_guidelines_youtube_videos/*.md`
  - Output (dict):
    - `status`: "success"
    - `videos_processed`: int
    - `videos_total`: int
    - `output_directory`: absolute path to `.nova/urls_from_guidelines_youtube_videos/`
    - `message`: summary

---

## Step 3 — Research loop (repeatable)

### 3.1 Generate next queries
- MCP Tool: `generate_next_queries(research_directory: str, n_queries: int = 5)`
  - Implementation: `tools/generate_next_queries_tool.py`
  - Reads: `article_guideline.md`, `.nova/perplexity_results.md` (if exists), `.nova/urls_from_guidelines/*.md`
  - Writes: `.nova/next_queries.md` (overwrites)
  - Output (dict):
    - `status`: "success"
    - `queries_count`: int
    - `queries`: list[tuple[str, str]] → [(query, reason), ...]
    - `output_path`: absolute path to `.nova/next_queries.md`
    - `message`: summary + formatted query list

### 3.2 Run Perplexity research for those queries
- MCP Tool: `run_perplexity_research(research_directory: str, queries: list[str])`
  - Implementation: `tools/run_perplexity_research_tool.py`
  - Reads: None mandatory; creates/updates results file
  - Internals: Structured Perplexity call, appends normalized “Source [id]” sections
  - Writes: `.nova/perplexity_results.md` (appends)
  - Output (dict):
    - `status`: "success"
    - `queries_processed`: int
    - `sources_added`: int (number of source blocks appended)
    - `output_path`: absolute path to `.nova/perplexity_results.md`
    - `message`: summary

---

## Step 4 — Filter Perplexity results by quality

### 4.1 Select sources to keep
- MCP Tool: `select_research_sources_to_keep(research_directory: str)`
  - Implementation: `tools/select_research_sources_to_keep_tool.py`
  - Reads: `article_guideline.md`, `.nova/perplexity_results.md`
  - Writes:
    - `.nova/perplexity_sources_selected.md`: comma-separated IDs
    - `.nova/perplexity_results_selected.md`: filtered markdown containing only selected source blocks
  - Output (dict):
    - `status`: "success"
    - `sources_selected_count`: int
    - `selected_source_ids`: list[int]
    - `sources_selected_path`: absolute path to IDs file
    - `results_selected_path`: absolute path to filtered results file
    - `message`: summary

---

## Step 5 — Identify accepted sources to scrape fully

### 5.1 Select research sources to scrape
- MCP Tool: `select_research_sources_to_scrape(research_directory: str, max_sources: int = 5)`
  - Implementation: `tools/select_research_sources_to_scrape_tool.py`
  - Reads: `article_guideline.md`, `.nova/perplexity_results_selected.md`, content from `.nova/urls_from_guidelines/*.md`
  - Writes: `.nova/urls_to_scrape_from_research.md` (one URL per line)
  - Output (dict):
    - `status`: "success"
    - `urls_selected_count`: int
    - `selected_urls`: list[str]
    - `selection_reasoning`: str
    - `urls_output_path`: absolute path to `.nova/urls_to_scrape_from_research.md`
    - `message`: summary

### 5.2 Scrape selected research URLs (full content)
- MCP Tool: `scrape_research_urls(research_directory: str, concurrency_limit: int = 4)`
  - Implementation: `tools/scrape_research_urls_tool.py`
  - Reads: `.nova/urls_to_scrape_from_research.md`; optionally deduplicates against `.nova/guidelines_filenames.json` (`other_urls` + `github_urls`)
  - Categorizes: YouTube vs other URLs; transcribes YouTube; scrapes/cleans other URLs concurrently
  - Writes: `.nova/urls_from_research/*.md`
  - Output (dict):
    - `status`: "success" or "warning"
    - `urls_processed`: int (successful scrapes for non-YouTube; YouTube transcriptions are not counted in `urls_processed` but appear in the report message)
    - `urls_total`: int (new URLs after deduplication, both categories)
    - `original_urls_count`: int (before deduplication)
    - `deduplicated_count`: int
    - `files_saved`: int
    - `output_directory`: absolute path to `.nova/urls_from_research/`
    - `saved_files`: list[str]
    - `message`: summary

---

## Step 6 — Generate final research file

### 6.1 Create `research.md`
- MCP Tool: `create_research_file(research_directory: str)`
  - Implementation: `tools/create_research_file_tool.py`
  - Reads (if present):
    - Preferred: `.nova/perplexity_results_selected.md`
    - Fallback: `.nova/perplexity_results.md`
    - Plus sections from:
      - `.nova/urls_from_research/*.md`
      - `.nova/urls_from_guidelines_code/*.md`
      - `.nova/urls_from_guidelines_youtube_videos/*.md`
      - `.nova/urls_from_guidelines/*.md`
  - Writes: `research.md` at the root of `research_directory`
  - Output (dict):
    - `status`: "success"
    - `markdown_file`: absolute path to `research.md`
    - `research_results_count`: int (number of grouped query sections)
    - `scraped_sources_count`: int (from `urls_from_research`)
    - `code_sources_count`: int (from `urls_from_guidelines_code`)
    - `youtube_transcripts_count`: int (from `urls_from_guidelines_youtube_videos`)
    - `additional_sources_count`: int (from `urls_from_guidelines`)
    - `message`: summary

---

## Files, folders, and constants
Key constants from `mcp_server/src/config/constants.py`:
- Files written under `.nova/`:
  - `guidelines_filenames.json`
  - `perplexity_results.md`
  - `perplexity_results_selected.md`
  - `perplexity_sources_selected.md`
  - `next_queries.md`
  - `urls_to_scrape_from_research.md`
  - Folders: `urls_from_guidelines/`, `urls_from_guidelines_code/`, `urls_from_guidelines_youtube_videos/`, `local_files_from_research/`, `urls_from_research/`
- Root files:
  - `article_guideline.md` (input)
  - `research.md` (final output)

---

## Notable implementation notes and edge cases
- **Local files key mismatch**:
  - Extractor writes `local_file_paths` in `.nova/guidelines_filenames.json`.
  - `process_local_files_tool` reads `local_files`.
  - If unchanged, no local files will be processed by step 2.1. Resolve by aligning the key (either update the extractor to write `local_files` or adjust the processing tool to read `local_file_paths`).
- **Parallelism**:
  - The server tools implement async concurrency internally (web/YT scraping and transcription). The client’s ReAct loop executes tools one at a time; true cross-tool parallelism would require client-side orchestration changes.
- **Perplexity result format**:
  - Results are appended as normalized blocks: `### Source [id]: <url>`, plus `Query:` and `Answer:` sections, separated by `-----`. Several downstream parsers depend on this format.
- **YouTube transcription**:
  - Concurrency limited via `YOUTUBE_TRANSCRIPTION_MAX_CONCURRENT_REQUESTS`; retried on server errors, timeouts are handled with messages written to files.
- **GitHub processing**:
  - `gitingest` output is sanitized to remove base64 image payloads and truncated if too long.
- **Scraping**:
  - Uses Firecrawl with a 1-week cache for speed; content cleaned via LLM prompt constrained to removal of non-content elements.

---

## End-to-end flow summary
1. Load instructions prompt (optional).
2. Run `extract_guidelines_urls` to seed `.nova/guidelines_filenames.json`.
3. Process extracted resources:
   - `process_local_files` (requires `local_files` key) → copies/exports referenced files
   - `scrape_and_clean_other_urls` → `.nova/urls_from_guidelines/`
   - `process_github_urls` → `.nova/urls_from_guidelines_code/`
   - `transcribe_youtube_urls` → `.nova/urls_from_guidelines_youtube_videos/`
4. Repeat research loop:
   - `generate_next_queries` → `.nova/next_queries.md`
   - `run_perplexity_research` → append to `.nova/perplexity_results.md`
5. Curate results:
   - `select_research_sources_to_keep` → filter IDs and selected results
   - `select_research_sources_to_scrape` → write `.nova/urls_to_scrape_from_research.md`
6. Scrape full sources: `scrape_research_urls` → `.nova/urls_from_research/`
7. Compile final output: `create_research_file` → `research.md`.

</details>

<details>
<summary>_Users_omar_Documents_ai_repos_agentic-ai-engineering-course_lessons_17_data_ingestion_notebook</summary>

# Lesson 17: Initial Data Ingestion and Tooling

In this lesson, we focus on building the first set of essential MCP tools for data gathering in our research agent. We'll implement tools that read article guideline files, extract web URLs programmatically, and scrape their content in parallel. This lesson demonstrates how file-based approaches can save tokens for the orchestrating agent, which only needs to process simple success or failure messages rather than large content blocks.

Learning Objectives:
- Learn how to build MCP tools that extract URLs and references from text files
- Understand the benefits of file-based tool outputs for token efficiency
- Implement robust web scraping tools using external services
- Handle error cases gracefully thanks to appropriate policies in the MCP prompt instructions

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

To run this lesson, you'll need several API keys configured:

1. **Gemini API Key**, `GOOGLE_API_KEY` variable: Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. **Firecrawl API Key**, `FIRECRAWL_API_KEY` variable: Get your key from [Firecrawl](https://firecrawl.dev/). They have a free tier that allows you to scrape 500 pages, which is enough for testing the agent for free.
3. **GitHub token (optional)**, `GITHUB_TOKEN` variable: If you want to process private GitHub repositories, you'll need a GitHub token with access to them. In case you want to test this functionality, you can get a token from [here](https://github.com/settings/personal-access-tokens). However, this is not required for the lesson, as we can easily use public repositories for explaining the functionalities.

```python
from utils import env

env.load(required_env_vars=["GOOGLE_API_KEY", "FIRECRAWL_API_KEY", "GITHUB_TOKEN"])
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


## 2. Understanding the Research Agent Workflow

As we saw in the previous lesson, the research agent follows a systematic workflow for data ingestion. The MCP prompt defines a clear two-phase approach regarding the data ingestion:

- **Step 1**: Extract URLs and file references from the article guidelines.
- **Step 2**: Process all the extracted resources in parallel (local files, web URLs, GitHub repos, YouTube videos).

Here's a snapshot of the MCP prompt that defines the first two steps of the workflow:
```markdown
1. Setup:

    1.1. Explain to the user the numbered steps of the workflow. Be concise. Keep them numbered so that the user
    can easily refer to them later.
    
    1.2. Ask the user for the research directory, if not provided. Ask the user if any modification is needed for the
    workflow (e.g. running from a specific step, or adding user feedback to specific steps).

    1.3 Extract the URLs from the ARTICLE_GUIDELINE_FILE with the "extract_guidelines_urls" tool. This tool reads the
    ARTICLE_GUIDELINE_FILE and extracts three groups of references from the guidelines:
    • "github_urls" - all GitHub links;
    • "youtube_videos_urls" - all YouTube video links;
    • "other_urls" - all remaining HTTP/HTTPS links;
    • "local_files" - relative paths to local files mentioned in the guidelines (e.g. "code.py", "src/main.py").
    Only extensions allowed are: ".py", ".ipynb", and ".md".
    The extracted data is saved to the GUIDELINES_FILENAMES_FILE within the NOVA_FOLDER directory.

2. Process the extracted resources in parallel:

    You can run the following sub-steps (2.1 to 2.4) in parallel. In a single turn, you can call all the
    necessary tools for these steps.

    2.1 Local files - run the "process_local_files" tool to read every file path listed under "local_files" in the
    GUIDELINES_FILENAMES_FILE and copy its content into the LOCAL_FILES_FROM_RESEARCH_FOLDER subfolder within
    NOVA_FOLDER, giving each copy an appropriate filename (path separators are replaced with underscores).

    2.2 Other URL links - run the "scrape_and_clean_other_urls" tool to read the `other_urls` list from the
    GUIDELINES_FILENAMES_FILE and scrape/clean them. The tool writes the cleaned markdown files inside the
    URLS_FROM_GUIDELINES_FOLDER subfolder within NOVA_FOLDER.

    2.3 GitHub URLs - run the "process_github_urls" tool to process the `github_urls` list from the
    GUIDELINES_FILENAMES_FILE with gitingest and save a Markdown summary for each URL inside the
    URLS_FROM_GUIDELINES_CODE_FOLDER subfolder within NOVA_FOLDER.

    2.4 YouTube URLs - run the "transcribe_youtube_urls" tool to process the `youtube_videos_urls` list from the
    GUIDELINES_FILENAMES_FILE, transcribe each video, and save the transcript as a Markdown file inside the
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER subfolder within NOVA_FOLDER.
        Note: Please be aware that video transcription can be a time-consuming process. For reference,
        transcribing a 39-minute video can take approximately 4.5 minutes.
```

Let's examine the MCP tools involved in these first two steps of the workflow. As we saw in the previous lesson, the MCP tool endpoints are defined in the `src/routers/tools.py` file.

Source: _research_agent_part_2/mcp_server/src/routers/tools.py_

```python
def register_mcp_tools(mcp: FastMCP) -> None:
    """Register all MCP tools with the server instance."""
    
    # Step 1: Extract URLs and file references from guidelines
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

    # Step 2.1: Process local files
    @mcp.tool()
    async def process_local_files(research_directory: str) -> Dict[str, Any]:
        """Process local files referenced in the article guidelines."""
        result = process_local_files_tool(research_directory)
        return result
        
    # Step 2.2: Scrape web URLs
    @mcp.tool() 
    async def scrape_and_clean_other_urls(research_directory: str, concurrency_limit: int = 4) -> Dict[str, Any]:
        """Scrape and clean other URLs from GUIDELINES_FILENAMES_FILE."""
        result = await scrape_and_clean_other_urls_tool(research_directory, concurrency_limit)
        return result

    # Step 2.3: Process GitHub repositories
    @mcp.tool()
    async def process_github_urls(research_directory: str) -> Dict[str, Any]:
        """
        Process GitHub URLs from GUIDELINES_FILENAMES_FILE using gitingest.
        
        Reads the GUIDELINES_FILENAMES_FILE file and processes each URL listed
        under 'github_urls' using gitingest to extract repository summaries, file trees,
        and content. The results are saved as markdown files in the
        URLS_FROM_GUIDELINES_CODE_FOLDER subfolder.
        """
        result = await process_github_urls_tool(research_directory)
        return result
        
    # Step 2.4: Transcribe YouTube videos
    @mcp.tool()
    async def transcribe_youtube_urls(research_directory: str) -> Dict[str, Any]:
        """
        Transcribe YouTube video URLs from GUIDELINES_FILENAMES_FILE using Gemini 2.5 Pro.
        
        Reads the GUIDELINES_FILENAMES_FILE file and processes each URL listed
        under 'youtube_videos_urls'. Each video is transcribed, and the results are
        saved as markdown files in the URLS_FROM_GUIDELINES_YOUTUBE_FOLDER subfolder.
        """
        result = await transcribe_youtube_videos_tool(research_directory)
        return result
```

Notice how this tool returns a concise summary rather than the full extracted content. We'll see the exact outputs in the next sections. This design choice has several advantages:

1. **Token Efficiency**: The agent receives only essential information (counts, status, file path) rather than large content blocks.
2. **Context Management**: Keeps the agent's context window manageable for complex workflows.
3. **Selective Reading**: The agent can choose to read the output file only if needed for decision-making. However, the ability to read files must be implemented as a tool (or another MCP server) for the MCP client. To do this, it would be possible to add a separate MCP server to the MCP client, or to use an MCP client that has already this capability (e.g. Cursor).
4. **Error Handling**: Clear status messages help the agent understand what succeeded or failed, and how to proceed.

Let's now see how each of these MCP tools is implemented.

## 3. Extracting URLs from Guidelines

The first tool in our data ingestion pipeline reads an article guideline file and programmatically extracts all URLs and file references it contains.

Here's its implementation:

Source: _research_agent_part_2/mcp_server/src/tools/extract_guidelines_urls_tool.py_

```python
def extract_guidelines_urls_tool(research_folder: str) -> Dict[str, Any]:
    """
    Extract URLs and local file references from the article guidelines in the research folder.
    
    Reads the ARTICLE_GUIDELINE_FILE file and extracts:
    - GitHub URLs
    - YouTube video URLs  
    - Other HTTP/HTTPS URLs
    - Local file references
    
    Results are saved to GUIDELINES_FILENAMES_FILE in the research folder.
    """
    ...

    # Convert to Path object
    research_path = Path(research_folder)
    nova_path = research_path / NOVA_FOLDER
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    ...
    
    # Read guidelines content
    guidelines_content = read_file_safe(guidelines_path)
    
    # Extract URLs
    urls = extract_urls(guidelines_content)
    github_source_urls = [u for u in all_urls if "github.com" in u]
    youtube_source_urls = [u for u in all_urls if "youtube.com" in u]
    web_source_urls = [u for u in all_urls if "github.com" not in u and "youtube.com" not in u]

    # Extract local file paths
    local_paths = extract_local_paths(guidelines_content)
    
    # Prepare the extracted data structure
    extracted_data = {
        "github_urls": urls["github_urls"],
        "youtube_videos_urls": urls["youtube_videos_urls"], 
        "other_urls": urls["other_urls"],
        "local_file_paths": local_paths,
    }
    
    # Save to JSON file
    output_path = nova_path / GUIDELINES_FILENAMES_FILE
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=2, ensure_ascii=False)
    
    return {
        "status": "success",
        "github_sources_count": len(urls["github_urls"]),
        "youtube_sources_count": len(urls["youtube_videos_urls"]),
        "web_sources_count": len(urls["other_urls"]),
        "local_files_count": len(local_paths),
        "output_path": str(output_path),
        "message": f"Successfully extracted URLs from article guidelines in '{research_folder}'. "
                  f"Found {len(urls['github_urls'])} GitHub URLs, {len(urls['youtube_videos_urls'])} YouTube videos URLs, "
                  f"{len(urls['other_urls'])} other URLs, and {len(local_paths)} local file references. "
                  f"Results saved to: {output_path}"
    }
```

The code:
1. Identifies the location of the article guidelines file,
2. Uses the `extract_urls` function to extract the URLs from the guidelines content,
3. Extracts local file paths with the `extract_local_paths` function,
4. Saves the extracted data to a JSON file, and
5. Returns a summary of the results.

Let's now see how the URLs are extracted from the guidelines content.

### 3.1 URLs Extraction

The `extract_urls` function from the guideline extractions handler finds all HTTP/HTTPS URLs:

Source: _research_agent_part_2/mcp_server/src/app/guideline_extractions_handler.py_

```python
def extract_urls(text: str) -> list[str]:
    """Extract all HTTP/HTTPS URLs from the given text."""
    url_pattern = re.compile(r"https?://[^\s)>\"',]+")
    return url_pattern.findall(text)
```

This regular expression pattern:
- `https?://` - Matches both HTTP and HTTPS protocols
- `[^\s)>\"',]+` - Matches any characters except whitespace, closing parentheses, greater-than signs, quotes, or commas
- This ensures URLs are extracted cleanly from markdown links, plain text, and various formatting contexts

After extraction, the URLs are categorized by domain to enable specialized processing for each type of content source.

### 3.2 Local File Path Extraction

The `extract_local_paths` function is used to extract local file paths from the guidelines content, and it is defined in the `app/guideline_extractions_handler.py` file.

We won't show its code here as it's not interesting for teaching how AI agents work. You can check how it works in the code if you're curious. You only need to know the following:
- It only looks for specific file extensions (`.py`, `.ipynb`, `.md`)
- It excludes anything that looks like a URL

### 3.3 Running the Tool

Let's test this tool programmatically to get an idea of its output:

```python
from research_agent_part_2.mcp_server.src.tools import extract_guidelines_urls_tool

# Update this path to your actual sample research folder
research_folder = "/path/to/research_folder"
result = extract_guidelines_urls_tool(research_folder=research_folder)
print(result)
```

**Output:**
```
{'status': 'success', 'github_sources_count': 1, 'youtube_sources_count': 1, 'web_sources_count': 2, 'local_files_count': 0, 'output_path': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/guidelines_filenames.json', 'message': "Successfully extracted URLs from article guidelines in '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder'. Found 1 GitHub URLs, 1 YouTube videos URLs, 2 other URLs, and 0 local file references. Results saved to: /Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/guidelines_filenames.json"}
```


The output will show a structured summary like:

```json
{
  "status": "success",
  "github_sources_count": 1,
  "youtube_sources_count": 2, 
  "web_sources_count": 6,
  "local_files_count": 0,
  "output_path": "/path/to/research_folder/.nova/guidelines_filenames.json",
  "message": "Successfully extracted URLs from article guidelines in '/path/to/research_folder'. Found 1 GitHub URLs, 2 YouTube videos URLs, 6 other URLs, and 0 local file references. Results saved to: /path/to/research_folder/.nova/guidelines_filenames.json"
}
```

With this summary, the agent can understand if everything worked fine or not, and how to proceed in case of errors (e.g. by asking the user for help).

## 4. Processing Local Files

The `process_local_files_tool` tool handles local file references found in the guidelines. It copies referenced files to an organized folder structure and formats them for LLM consumption.

Source: _research_agent_part_2/mcp_server/src/tools/process_local_files_tool.py_

```python
def process_local_files_tool(research_directory: str) -> Dict[str, Any]:
    """
    Process local files referenced in the article guidelines.

    Reads the guidelines JSON file and copies each referenced local file
    to the local files subfolder. Path separators in filenames are
    replaced with underscores to avoid creating nested folders.

    Args:
        research_directory: Path to the research directory containing the guidelines JSON file

    Returns:
        Dict with status, processing results, and file paths
    """
    ...

    # Convert to Path object
    research_path = Path(research_directory)
    nova_path = research_path / NOVA_FOLDER

    # Look for GUIDELINES_FILENAMES_FILE
    metadata_path = nova_path / GUIDELINES_FILENAMES_FILE

    ...

    # Load JSON metadata
    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    local_files = data.get("local_files", [])

    if not local_files:
        return {
            "status": "success",
            "message": f"No local files to process in research folder '{research_directory}'.",
            "files_processed": 0,
            "files_total": 0,
            "warnings": [],
            "errors": [],
        }

    # Create destination folder if it doesn't exist
    dest_folder = nova_path / LOCAL_FILES_FROM_RESEARCH_FOLDER
    dest_folder.mkdir(parents=True, exist_ok=True)

    processed = 0
    warnings = []
    errors = []
    processed_files = []

    # Initialize notebook converter for .ipynb files
    notebook_converter = NotebookToMarkdownConverter(include_outputs=True, include_metadata=False)

    for rel_path in local_files:
        # Local files are relative to the research folder
        src_path = research_path / rel_path
        ...

        # Sanitize destination filename (replace path separators with underscores)
        dest_name = rel_path.replace("/", "_").replace("\\", "_")

        try:
            # Handle .ipynb files specially by converting to markdown
            if src_path.suffix.lower() == ".ipynb":
                # Convert .ipynb to .md extension for destination
                dest_name = dest_name.rsplit(".ipynb", 1)[0] + ".md"
                dest_path = dest_folder / dest_name

                # Convert notebook to markdown string
                markdown_content = notebook_converter.convert_notebook_to_string(src_path)

                # Write markdown content to destination
                dest_path.write_text(markdown_content, encoding="utf-8")
            else:
                # For other file types, copy as before
                dest_path = dest_folder / dest_name
                shutil.copy2(src_path, dest_path)

            processed += 1
            processed_files.append(dest_name)
        except Exception as e:
            errors.append(f"Failed to process {rel_path}: {str(e)}")

    # Build result message using the dedicated function
    result_message = build_result_message(research_directory, processed, local_files, dest_folder, warnings, errors)

    return {
        "status": "success" if processed > 0 else "warning",
        "files_processed": processed,
        "files_total": len(local_files),
        "processed_files": processed_files,
        "warnings": warnings,
        "errors": errors,
        "output_directory": str(dest_folder.resolve()),
        "message": result_message,
    }
```

This local file processing tool looks for the local files extracted by the `extract_guidelines_urls_tool` tool and copies them to an organized folder structure. It distinguishes between different file types (where it copy its content as is) and notebooks (where it converts the content to markdown).

The `NotebookToMarkdownConverter` class can be found in the `app/notebook_handler.py` file. We won't show its code here as it's not interesting for teaching how AI agents work. You can check how it works in the code if you're curious. You only need to know that it keeps both markdown cells and code cells, and it also keeps the outputs of the executed cells truncated to a maximum amount of characters.

## 5. Web Scraping with Firecrawl and LLM Cleaning

This is the most complex tool in our data ingestion pipeline. It scrapes web URLs and cleans the content using both external services and LLM processing. Here's its implementation:

Source: _research_agent_part_2/mcp_server/src/tools/scrape_and_clean_other_urls_tool.py_

```python
async def scrape_and_clean_other_urls_tool(research_directory: str, concurrency_limit: int = 4) -> Dict[str, Any]:
    """
    Scrape and clean other URLs from guidelines file in the research folder.
    
    Reads the guidelines file and scrapes/cleans each URL listed
    under 'other_urls'. The cleaned markdown content is saved to the
    URLS_FROM_GUIDELINES_FOLDER subfolder with appropriate filenames.
    """    
    # Convert to Path object
    research_path = Path(research_directory)
    nova_path = research_path / NOVA_FOLDER
    
    # Look for GUIDELINES_FILENAMES_FILE file
    guidelines_file_path = nova_path / GUIDELINES_FILENAMES_FILE
    
    # Read the guidelines filenames file
    guidelines_data = json.loads(read_file_safe(guidelines_file_path))
    urls_to_scrape = guidelines_data.get("other_urls", [])
    
    if not urls_to_scrape:
        return {
            "status": "success",
            "urls_processed": [],
            "urls_failed": [],
            "total_urls": 0,
            "successful_urls_count": 0,
            "failed_urls_count": 0,
            "output_directory": str(nova_path / URLS_FROM_GUIDELINES_FOLDER),
            "message": "No other URLs found to scrape in the guidelines filenames file."
        }
    
    # Read article guidelines for context
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    guidelines_content = read_file_safe(guidelines_path)
    
    # Scrape URLs concurrently
    completed_results = await scrape_urls_concurrently(
        urls_to_scrape, 
        concurrency_limit, 
        guidelines_content
    )
    
    # Write results to files
    output_dir = nova_path / URLS_FROM_GUIDELINES_FOLDER
    saved_files, successful_scrapes = write_scraped_results_to_files(completed_results, output_dir)
    
    # Calculate statistics
    failed_urls = [res["url"] for res in completed_results if not res.get("success", False)]
    successful_urls = [res["url"] for res in completed_results if res.get("success", False)]
    
    return {
        "status": "success",
        "urls_processed": successful_urls,
        "urls_failed": failed_urls,
        "total_urls": len(urls_to_scrape),
        "successful_urls_count": successful_scrapes,
        "failed_urls_count": len(failed_urls),
        "output_directory": str(output_dir),
        "message": f"Successfully processed {successful_scrapes}/{len(urls_to_scrape)} URLs. "
                  f"Results saved to: {output_dir}"
    }
```

Here's how it works:
1. It looks for the URLs to scrape in the guidelines filenames file.
2. It uses the `scrape_urls_concurrently` function to scrape the URLs concurrently using Firecrawl and clean the content using an LLM.
3. It saves the cleaned content to the `URLS_FROM_GUIDELINES_FOLDER` folder.
4. It returns a summary of the results.

Let's see in more detail how the `scrape_urls_concurrently` function works.

### 5.1 The Two-Stage Cleaning Process

The scraping process uses a two-stage approach:

1. **Firecrawl for Initial Scraping**: Firecrawl is a specialized service that handles the complexity of modern web scraping, including:
   - JavaScript rendering
   - Dynamic content loading  
   - Anti-bot protection
   - Clean markdown extraction

2. **LLM for Content Refinement**: After Firecrawl extracts the raw content, an LLM (Gemini 2.5 Flash) further cleans and structures the content by:
   - Removing irrelevant sections (ads, navigation, footers)
   - Focusing on content relevant to the article guidelines
   - Maintaining proper markdown formatting
   - Preserving important links and references

This Firecrawl scraping function handles the complexity of modern web scraping:

```python
async def scrape_url(url: str, firecrawl_app: AsyncFirecrawl) -> dict:
    """
    Scrape a URL using Firecrawl with retries and return a dict with url, title, markdown.

    Uses maxAge=1 week for 500% faster scraping by leveraging cached data when available.
    This optimization significantly improves performance for documentation, articles, and
    relatively static content while maintaining freshness within acceptable limits.
    """
    max_retries = 3
    base_delay = 5  # seconds
    timeout_seconds = 120000  # 2 minutes timeout per request

    for attempt in range(max_retries):
        try:
            # Add timeout to individual Firecrawl request
            # Use maxAge=1 week for 500% faster scraping with cached data
            res = await firecrawl_app.scrape(
                url, formats=["markdown"], maxAge=MAX_AGE_ONE_WEEK, timeout=timeout_seconds
            )
            title = res.metadata.title if res and res.metadata and res.metadata.title else "N/A"
            markdown_content = res.markdown if res and res.markdown else ""
            return {"url": url, "title": title, "markdown": markdown_content, "success": True}
        except asyncio.TimeoutError:
            # Manage retries
            ...
        except Exception as e:
            # Manage retries
            ...
    
    return {
        "url": url,
        "title": "Scraping Failed",
        "markdown": f"⚠️ Error scraping {url} after {max_retries} attempts.",
        "success": False,
    }
```

The core of it is the `firecrawl_app.scrape` function that scrapes the URL and returns the markdown content.

The LLM cleaning process is handled by the `clean_markdown` function:

Source: _research_agent_part_2/mcp_server/src/app/scraping_handler.py_

```python
async def clean_markdown(
    markdown_content: str, article_guidelines: str, url_for_log: str, chat_model: BaseChatModel
) -> str:
    """Clean markdown content via LLM and convert image syntax to URLs."""
    if not markdown_content.strip():
        return markdown_content

    prompt_text = PROMPT_CLEAN_MARKDOWN.format(article_guidelines=article_guidelines, markdown_content=markdown_content)
    timeout_seconds = 180  # 3 minutes timeout for LLM call

    try:
        # Add timeout to LLM API call
        response = await asyncio.wait_for(chat_model.ainvoke(prompt_text), timeout=timeout_seconds)
        cleaned_content = response.content if hasattr(response, "content") else str(response)

        if isinstance(cleaned_content, list):
            cleaned_content = "".join(str(part) for part in cleaned_content)

        # Post-process: convert markdown images to just URLs
        cleaned_content = convert_markdown_images_to_urls(cleaned_content)

        return cleaned_content
    except asyncio.TimeoutError:
        logger.error(f"LLM API call timed out after {timeout_seconds}s for {url_for_log}. Using original content.")
        return markdown_content
    except Exception as e:
        logger.error(f"Error cleaning markdown for {url_for_log}: {e}. Using original content.", exc_info=True)
        return markdown_content
```

The `clean_markdown` function simply uses Gemini 2.5 Flash to clean the markdown content using an appropriate prompt.
Here's the prompt used (`PROMPT_CLEAN_MARKDOWN`) to clean the markdown content:

```markdown
Your task is to clean markdown content scraped from a webpage by *only removing* all irrelevant sections such as
headers, footers, navigation bars, advertisements, sidebars, self-promotion, call-to-actions, etc.
Focus on keeping only the core textual content (and code content if there are code sections) that is pertinent to
the article guidelines provided below.
Return *only* the cleaned markdown.
Do not summarize or rewrite the original content. This task is only about *removing* irrelevant content.
Good content should be kept as is, do not touch it.

Here are the article guidelines:
<article_guidelines>
{article_guidelines}
</article_guidelines>

Here is the markdown content to clean:
<markdown_content>
{markdown_content}
</markdown_content>
```

The cleaning process significantly reduces token count while preserving the most relevant information for research purposes.

### 5.2 Why Use External Scraping Services?

Web scraping is notoriously complex due to:

- **Dynamic Content**: Modern websites heavily use JavaScript
- **Anti-Bot Measures**: CAPTCHAs, rate limiting, IP blocking
- **Varied Formats**: Inconsistent HTML structures across sites
- **Performance Issues**: Slow loading, timeouts, redirects

Rather than building a robust scraper from scratch (which would require significant effort and still fall short), using a specialized service like Firecrawl allows us to:

- Focus on our core research logic
- Get reliable results across diverse websites  
- Benefit from ongoing improvements to the scraping infrastructure
- Handle edge cases that would be time-consuming to solve ourselves

Let's now test the scraping tool to see what is its output:

```python
from research_agent_part_2.mcp_server.src.tools import scrape_and_clean_other_urls_tool

# Test the scraping tool
result = await scrape_and_clean_other_urls_tool(research_directory=research_folder, concurrency_limit=2)
print(result)
```

**Output:**
```
/Users/fabio/Desktop/course-ai-agents/.venv/lib/python3.12/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
  from .autonotebook import tqdm as notebook_tqdm
```

**Output:**
```
{'status': 'success', 'urls_processed': 2, 'urls_total': 2, 'files_saved': 2, 'output_directory': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/urls_from_guidelines', 'saved_files': ['function-calling-with-the-gemini-api-google-ai-for-developer.md', 'openai-platform.md'], 'message': "Scraped and cleaned 2/2 other URLs from guidelines_filenames.json in '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder'.\nSaved 2 files to urls_from_guidelines folder: function-calling-with-the-gemini-api-google-ai-for-developer.md, openai-platform.md"}
```


The output lists the number of URLs processed, the number of URLs that failed, and the output directory where the cleaned content is saved. You can now open the output directory (in the `.nova/urls_from_guidelines` folder) to see the cleaned content.

Now, let's see how GitHub URLs are processed.

## 6. Processing GitHub URLs

For GitHub repositories, we use a different approach optimized for code analysis. The `process_github_urls_tool` function (from `mcp_server/src/tools/process_github_urls_tool.py`) leverages the `gitingest` library to extract comprehensive information from GitHub repositories, making code and documentation available for research purposes.

We won't show the code here as it's not interesting for teaching how AI agents work. You can check how it works in the code if you're curious. You only need to know that it uses the `gitingest` library to extract the information from the GitHub repositories.

Let's test the GitHub processing tool here. The GitHub URL from the sample article guideline refer to a prompting guide for GPT-5 and is available in a [public repository](https://github.com/openai/openai-cookbook/blob/main/examples/gpt-5/gpt-5_prompting_guide.ipynb), so you don't need to provide a GitHub token for it.

```python
from research_agent_part_2.mcp_server.src.tools import process_github_urls_tool

# Test GitHub URL processing
result = await process_github_urls_tool(research_directory=research_folder)
print(result)
```

**Output:**
```
{'status': 'success', 'urls_processed': 1, 'urls_total': 1, 'files_saved': 1, 'output_directory': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/urls_from_guidelines_code', 'message': "Processed 1/1 GitHub URLs from guidelines_filenames.json in '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder'. Saved markdown summaries to urls_from_guidelines_code folder."}
```


From its result, you can see that the tool has extracted the information from the GitHub repository and saved it in the `.nova/github_urls_from_guidelines_code` folder. You can now open the output directory to see the extracted information.

## 7. YouTube Video Transcription

The `transcribe_youtube_videos_tool` (from the `mcp_server/src/tools/transcribe_youtube_videos_tool.py` file) leverages Gemini's multimodal capabilities to process video content directly and generate structured transcripts for research purposes.

The core of it is the `transcribe_youtube` function, which is the one that actually transcribes the YouTube video. Here's its implementation:

Source: _research_agent_part_2/mcp_server/src/app/youtube_handler.py_

```python
async def transcribe_youtube(
    url: str,
    output_path: Path,
    timestamp: int = 30,
) -> None:
    """
    Transcribes a public YouTube video using a Gemini model and saves the
    result to a file.

    Args:
        url: The public URL of the YouTube video.
        output_path: The path to save the transcription markdown file.
        timestamp: The interval in seconds for inserting timestamps in the
                   transcription.
    """
    # Create client internally using settings and track with Opik if configured
    base_client = genai.Client(api_key=settings.google_api_key.get_secret_value())
    client = track_genai_client(base_client)
    model_name = settings.youtube_transcription_model

    prompt = PROMPT_YOUTUBE_TRANSCRIPTION.format(timestamp=timestamp)

    parts: list[types.Part] = [
        types.Part(
            file_data=types.FileData(file_uri=url)  # YouTube URL - no download needed
        ),
        types.Part(text=prompt),
    ]

    ...
    response: types.GenerateContentResponse = await client.aio.models.generate_content(
        model=model_name,
        contents=types.Content(parts=parts),
    )
    ...

    output_path.write_text(response.text, encoding="utf-8")
```

The Gemini API can [transcribe YouTube videos](https://ai.google.dev/gemini-api/docs/video-understanding#transcribe-video) by adding the video URL as a `types.Part` to the request, as shown above. Visit the provided link to learn more about the Gemini API's video understanding capabilities.

You can run the following code to test the YouTube transcription tool.

```python
from research_agent_part_2.mcp_server.src.tools import transcribe_youtube_videos_tool

# Test YouTube transcription (note: this can be time-consuming)
result = await transcribe_youtube_videos_tool(research_directory=research_folder)
print(result)
```

**Output:**
```
{'status': 'success', 'videos_processed': 1, 'videos_total': 1, 'output_directory': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/urls_from_guidelines_youtube_videos', 'message': "Processed 1 YouTube URLs from guidelines_filenames.json in '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder'. Saved transcriptions to urls_from_guidelines_youtube_videos folder."}
```


The output lists the number of videos processed, the number of videos that failed, and the output directory where the transcription is saved. You can now open the output directory to see the transcription.

**Note**: Video transcription is time-intensive. A 39-minute video typically takes about 4.5 minutes to process. The tool processes videos concurrently but with controlled concurrency to respect API limits and avoid overwhelming the service.

## 8. Running the Full Agent with MCP Prompt

We're now ready to run the MCP client and see how these tools work together! Run the following code cell to start the client.

Once the client is running, you can:

1. **Start the workflow**: Type `/prompt/full_research_instructions_prompt` to load the complete research workflow. It will load the MCP prompt with all the instructions and feed it to the LLM, which will in turn write a message to the user asking for the research directory path and whether the workflow should be run with modifications.
2. **Answer the agent**: Give the path to your sample research folder, and tell the agent to run only the first two steps of the workflow, and to stop after that.
3. **Watch the agent work**: Observe how it runs the tools in sequence
4. **Examine outputs**: Check the `.nova` folder for generated files

Try these commands in sequence:
- `/prompt/full_research_instructions_prompt`
- `The research folder is /path/to/research_folder. Run only the first two steps of the workflow and stop after that, and ask me how to proceed.` Replace the `/path/to/research_folder` with the path to your sample research folder.
- `/quit` after the agent has finished running the tools and asked you how to proceed.

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
[35m**Understanding the Research Task**

Okay, so the user wants me to run a research workflow. My first step is clear: I need to concisely explain the entire process to them, breaking it down into manageable chunks. Numbered steps will be the most straightforward approach here. Once I've laid out the plan, I'll need to gather some crucial information: the location where the research will be saved (`research_directory`) and whether they want to customize the workflow at all. This is important – I want to make sure I'm aligned with their expectations before diving in. Then, and only then, can I actually begin running the research workflow.[0m

[37m💬 LLM Response: [0mHello! I will help you with the research workflow. Here are the steps:

1.  **Setup:** Extract URLs and local file references from your article guidelines.
2.  **Process Extracted Resources:** In parallel, I will process local files, scrape other web URLs, process GitHub repository links, and transcribe YouTube video URLs found in your guidelines.
3.  **Research Loop:** I will run a research loop for 3 rounds. In each round, I'll generate new search queries based on existing data and execute them using Perplexity to gather more information.
4.  **Filter Perplexity Results:** I will evaluate the Perplexity research results and select only the high-quality, relevant sources.
5.  **Scrape Selected Research Sources:** I will identify the most valuable sources from the filtered Perplexity results and scrape their full content.
6.  **Write Final Research File:** Finally, I will compile all the gathered and processed information into a comprehensive `research.md` file.

To begin, please provide the path to your research directory. Also, let me know if you need any modifications to this workflow, such as starting from a specific step or adding user feedback points.


[1m[95m🤔 LLM's Thoughts:[0m
[35m**Executing the Next Phase of the Workflow**

Okay, so I'm ready to move forward. My focus right now is definitely on steps 1 and 2 of this workflow. I remember step 1.3 is all about pulling those guidelines URLs, which is straightforward enough. But step 2, that's where the real action is. It's calling for some serious parallel processing! I've got four distinct sub-steps within step 2 that need to run concurrently: `process_local_files`, `scrape_and_clean_other_urls`, `process_github_urls`, and `transcribe_youtube_urls`.  

All of these tools, the core tools for these steps and sub-steps, need to be executed while taking into account the `research_directory`.  I'll manage the inputs and outputs, and make sure everything is coordinated.  Time to get these functions moving![0m


[1m[36m🔧 Function Call (Tool):[0m
[36m  Tool: [0m[1m[36mextract_guidelines_urls[0m
[36...
```


Now, read the above output and notice the following:
- Since there isn't any local file to extract, the agent skipped the `process_local_files_tool` tool.
- Read the agent thoughts to understand the reasoning behind the choices it made. They usually refer to the previous tool outputs.
- Read the final message from the agent.

## 9. Exploring Generated Files

After running the tools, examine the organized file structure in your research directory:

```
research_directory/
├── article_guideline.md                     # Input guidelines
├── .nova/                                   # Hidden folder with all data
│   ├── guidelines_filenames.json           # Extracted URLs and files
│   ├── local_files_from_research/          # Copied local files  
│   ├── urls_from_guidelines/               # Scraped web content
│   ├── urls_from_guidelines_code/          # GitHub repo summaries
│   └── urls_from_guidelines_youtube/       # Video transcripts
```

Each folder contains processed content ready for the next stages of the research workflow. The file-based approach ensures that:

- **Content is persistent** across agent sessions
- **Large content blocks** don't overwhelm the agent's context
- **Selective access** allows the agent to read only relevant files
- **Human inspection** is possible for debugging and verification

In a production setting, these files can be replaced with a database to enable more efficient querying and retrieval.

</details>