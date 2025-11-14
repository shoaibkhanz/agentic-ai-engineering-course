# Research

## Research Results

<details>
<summary>What are best practices for implementing human-in-the-loop (HITL) checkpoints in autonomous AI agent workflows?</summary>

### Source [1]: https://www.tredence.com/blog/hitl-human-in-the-loop

Query: What are best practices for implementing human-in-the-loop (HITL) checkpoints in autonomous AI agent workflows?

Answer: Best practices for implementing human-in-the-loop (HITL) checkpoints in autonomous AI agent workflows include:

- **Define the HITL role:** Clearly specify what humans are responsible for within the workflow, such as reviewing outputs, annotating data, or validating decisions. This ensures efficient collaboration and higher accuracy.

- **Use active learning:** Integrate active learning so human intervention is triggered only when the model's confidence is low or uncertain. This focuses human effort on ambiguous or challenging cases, enhancing both training efficiency and model accuracy.

- **Train humans like models:** Provide comprehensive training to human contributors on annotation guidelines and review criteria. This ensures that human inputs are consistent, transparent, and reliable.

- **Feedback integration:** Establish a continuous feedback loop where human corrections and insights are systematically incorporated into model retraining. This helps the model adapt to new data and maintain high predictive accuracy over time.

- **Leverage MLOps frameworks:** Automate data annotation pipelines, track audit logs, manage all human feedback, and facilitate model retraining. MLOps practices help combine machine efficiency with human judgment for fair, accurate, and trustworthy AI systems.

-----

-----

### Source [2]: https://www.sogolytics.com/blog/human-in-the-loop-ai/

Query: What are best practices for implementing human-in-the-loop (HITL) checkpoints in autonomous AI agent workflows?

Answer: For effective human-in-the-loop (HITL) integration in AI workflows, several strategies are recommended:

- **Design for Transparency:** Ensure AI behaviors are explainable and well-documented, with ongoing monitoring for accountability. This includes making it clear how decisions are made and how humans can intervene or audit outcomes.

- **Judicious Hybrid Modeling:** Combine the contextual intelligence of humans with the pattern recognition abilities of AI, so that each focuses on what they do best.

- **Vigilant Feedback Loops:** Maintain ongoing user feedback mechanisms to detect unexpected AI behaviors and enable rapid refinements. This supports continuous improvement and adaptation of both the AI and the surrounding workflow.

-----

-----

### Source [3]: https://parseur.com/blog/human-in-the-loop-ai

Query: What are best practices for implementing human-in-the-loop (HITL) checkpoints in autonomous AI agent workflows?

Answer: Key best practices for HITL implementation in AI agent workflows:

- **Strategic Human Involvement:** Focus human intervention on edge cases, low-confidence predictions, or periodic audits. Use active learning to ensure humans review only the most critical or ambiguous outputs.

- **Mitigate Human Error and Bias:** Clearly define roles for human reviewers, provide consistent training, and use multiple reviewers for critical decisions. Regularly assess both AI and human accuracy to drive continuous improvement.

- **Scope the Loop Properly:** Not every decision needs human intervention; identify high-risk or high-impact areas where errors would be most costly. Automate routine, low-risk tasks to maximize efficiency.

- **Pilot and Iterate:** Start with a pilot project, measure outcomes such as accuracy and turnaround time, and refine the workflow based on results.

- **Scale and Monitor:** Once validated, expand HITL to other use cases and continually monitor performance, feedback, and compliance as models and risks evolve.

-----

-----

### Source [4]: https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo

Query: What are best practices for implementing human-in-the-loop (HITL) checkpoints in autonomous AI agent workflows?

Answer: Recommended HITL practices for agentic workflows:

- **Design for Decision Points:** Explicitly identify where human input is critical (e.g., approvals, configuration changes, destructive actions) and build checkpoints at these moments. Use mechanisms like `interrupt()` to enforce these pauses.

- **Keep Prompts Contextual and Lightweight:** When seeking human approval, make requests clear and concise, providing only the necessary context to avoid overwhelming reviewers.

- **Use Policy Engines:** Delegate approval logic to policy engines rather than hardcoding rules, enabling declarative, versioned, and enforceable policies across systems.

- **Comprehensive Logging:** Ensure every access request, approval, and denial is logged for transparency and auditability.

- **Asynchronous Review Channels:** Not all approvals need to be real-time. For lower-priority tasks, use asynchronous channels (like Slack or dashboards) for reviews.

HITL should be viewed as a permanent and foundational pattern for trustworthy agentic AI, ensuring safe operational boundaries and maintaining human control over autonomous workflows.

-----

-----

### Source [5]: https://www.tines.com/blog/humans-in-the-loop-of-ai/

Query: What are best practices for implementing human-in-the-loop (HITL) checkpoints in autonomous AI agent workflows?

Answer: Best practices for HITL in workflow automation:

- **Establish Clear Roles and Monitoring:** Define when and how humans should interact with AI, and implement strong monitoring and alerts for visibility and quick response to unexpected events.

- **Prioritize Training and Transparency:** Facilitate transparency and explainability in AI decisions. Provide continuous training and regular audits to ensure AI operates correctly and adheres to guidelines.

- **Ensure User Control:** Allow authorized users to overrule AI decisions easily, balancing efficiency with human creativity and critical thinking.

- **Prioritize End Users:** Focus on enhancing user experience and fostering collaboration between humans and AI, rather than simply automating or replacing human roles.

-----

-----

### Source [6]: https://www.wsiworld.com/blog/human-in-the-loop-keeping-up-to-date-with-the-ai-landscape

Query: What are best practices for implementing human-in-the-loop (HITL) checkpoints in autonomous AI agent workflows?

Answer: A key best practice for HITL is to:

- **Identify Key Decision Points for Human Intervention:** Not all processes require human input. Carefully map the AI workflow to pinpoint where human expertise adds the most value, such as regulatory compliance or ethical judgment. This targeted approach balances efficiency and risk mitigation.

-----

</details>

<details>
<summary>How does the Model Context Protocol (MCP) enable portability for AI agents across different clients like Cursor?</summary>

### Source [11]: https://en.wikipedia.org/wiki/Model_Context_Protocol

Query: How does the Model Context Protocol (MCP) enable portability for AI agents across different clients like Cursor?

Answer: The Model Context Protocol (MCP) is an open standard and open-source framework introduced by Anthropic in November 2024 to standardize the way AI systems, such as large language models (LLMs), integrate and share data with external tools, systems, and data sources. MCP provides a universal interface for reading files, executing functions, and handling contextual prompts. One of its main goals is to address the 'N×M' integration challenge, where developers previously needed custom connectors for every tool and data source combination. By introducing a standardized framework for data ingestion, transformation, metadata tagging, and interoperability, MCP makes it possible for AI assistants to connect with any MCP-compatible server or client seamlessly. Developers can expose their data using MCP servers or build MCP client applications, such as AI coding assistants like Cursor, that can access these servers. This architecture enables AI agents to be portable across different client applications, as any client or server implementing MCP can communicate without the need for custom integration work.

-----

-----

### Source [12]: https://www.solo.io/topics/ai-infrastructure/what-is-mcp

Query: How does the Model Context Protocol (MCP) enable portability for AI agents across different clients like Cursor?

Answer: Model Context Protocol (MCP) provides a universal, model-agnostic interface that allows AI agents to connect to various data sources, tools, and systems using a standardized protocol. MCP eliminates the need for fragmented, custom integrations by enabling secure, bi-directional context exchange between AI-powered clients and data repositories. Developers can either expose data via MCP servers or access data as MCP clients, facilitating dynamic and accurate AI experiences. For example, an AI agent embedded in the Cursor IDE can connect to any MCP-compliant data source, making the agent portable across environments that support MCP. Security is ensured through robust authentication and authorization mechanisms, with support for policy-driven access. MCP’s open-source SDKs, available in multiple programming languages, further enhance portability by enabling easy adoption and integration across platforms. This structure allows AI agents to maintain and transfer context across workflows and client applications without rewriting integration logic.

-----

-----

### Source [13]: https://www.descope.com/learn/post/mcp

Query: How does the Model Context Protocol (MCP) enable portability for AI agents across different clients like Cursor?

Answer: The Model Context Protocol (MCP) acts as a 'universal remote' for AI by providing a consistent and standardized way for large language models and AI agents to connect with external data sources and tools. MCP’s client-server architecture is partially inspired by the Language Server Protocol (LSP), enabling host applications (such as Cursor) to integrate MCP clients that connect to various MCP servers. When an MCP client starts, it discovers the capabilities of connected servers and registers them, making these resources accessible to the AI agent during user interaction. The protocol specifies a universal format for requests and responses, so any AI application that implements the MCP client can plug into any MCP-compliant server without the need for custom code. This plug-and-play approach enables portability, as AI agents can move between different host applications and environments (like Cursor, Claude Desktop, web chat interfaces) and instantly access tools and data provided by any available MCP server.

-----

-----

### Source [14]: https://openai.github.io/openai-agents-python/mcp/

Query: How does the Model Context Protocol (MCP) enable portability for AI agents across different clients like Cursor?

Answer: MCP is described as an open protocol that standardizes how applications provide context to language models, likened to a 'USB-C port for AI applications.' Just as USB-C allows for standardized connections between devices and peripherals, MCP provides a consistent way for AI models to access different data sources and tools. This standardization is key to portability: any AI agent or client that supports MCP can connect to any MCP-compliant tool or data source, allowing AI agents to be used across multiple client applications (such as Cursor) without the need for specialized integration work for each environment.

-----

-----

### Source [15]: https://www.anthropic.com/news/model-context-protocol

Query: How does the Model Context Protocol (MCP) enable portability for AI agents across different clients like Cursor?

Answer: The Model Context Protocol (MCP) is introduced as an open standard for connecting AI assistants to the systems where data resides, such as content repositories, business tools, and development environments. MCP is designed to overcome the challenge of information silos and legacy system integration by providing a universal protocol that enables secure, two-way connections between data sources and AI-powered tools. Developers can choose to either expose their data through MCP servers or create AI applications (MCP clients) that connect to these servers. This architecture allows AI agents to be portable across different client environments, as any MCP-compliant agent can access any MCP-exposed data source, making integration and migration between clients seamless.

-----

</details>

<details>
<summary>What are advanced techniques for cleaning and preparing scraped web content for LLM consumption?</summary>

### Source [16]: https://www.prompts.ai/en/blog/best-practices-for-preprocessing-text-data-for-llms

Query: What are advanced techniques for cleaning and preparing scraped web content for LLM consumption?

Answer: Advanced techniques for cleaning and preparing scraped web content for LLM consumption revolve around several core steps:

- **Noise Removal:** Remove irrelevant content such as typos, formatting artifacts, and inconsistent data, which can otherwise confuse LLMs. Efficient noise reduction leads to improved model precision and fewer hallucinations.

- **Standardization:** Ensure textual consistency by normalizing formats and structures, allowing LLMs to better recognize patterns and improve both retrieval and generative accuracy.

- **Semantic Text Segmentation:** Instead of basic fixed-size chunking, use semantic segmentation to divide text into meaningful chunks based on context and content. This is particularly valuable for RAG (Retrieval-Augmented Generation) systems, ensuring contextually coherent chunks that fit within LLM input limits.

- **Tokenization:** Employ advanced tokenization strategies that preserve context and meaning, optimizing both computational efficiency and content integrity.

- **Outlier Detection and Management:** Use AI-based methods like Isolation Forest, Local Outlier Factor (LOF), and One-Class SVM to identify and remove outliers that could introduce noise into the dataset.

- **Domain-Specific Methods:** Customize preprocessing for specific domains (medical, legal, technical) to address unique data quirks and requirements.

- **Automation:** Utilize platforms that automate standardization, error reduction, and scalability to efficiently maintain high-quality, consistent data at scale.

Overall, investing in comprehensive preprocessing—cleaning, standardization, noise reduction, chunking, and outlier management—substantially improves LLM accuracy and efficiency.

-----

-----

### Source [17]: https://wandb.ai/wandb_gen/llm-data-processing/reports/Processing-Data-for-Large-Language-Models--VmlldzozMDg4MTM2

Query: What are advanced techniques for cleaning and preparing scraped web content for LLM consumption?

Answer: The article discusses several advanced techniques for cleaning and preparing web-scraped content for LLMs:

- **Junk and Boilerplate Removal:** Use specialized tools (e.g., justext, trafilatura) to strip HTML and remove boilerplate, ensuring only valuable content is retained. Balancing precision (removing junk) and recall (retaining valid content) is key.

- **Metadata Filtering:** Apply heuristics based on metadata (e.g., only use links with certain engagement scores) to filter for higher-quality content, as seen in the creation of WebText for GPT-2.

- **Document Length Filtering:** Exclude very short documents (e.g., <100 tokens) to reduce noise and focus on contiguous, context-rich text that better models dependencies.

- **Chunking:** Preprocess large documents by breaking them into non-overlapping spans of desirable length suitable for transformer input requirements.

- **De-duplication:** Employ both exact and fuzzy de-duplication techniques (e.g., using deduplicate-text-datasets, datasketch) to eliminate redundant content, essential for large-scale web crawls.

- **Toxic Content Filtering:** Use tools like PerspectiveAPI or spamscanner to identify and remove toxic or harmful content, supporting ethical AI development and reducing downstream bias.

These techniques collectively ensure that training data is clean, relevant, and suitable for effective LLM training.

-----

-----

### Source [18]: https://developer.nvidia.com/blog/mastering-llm-techniques-data-preprocessing/

Query: What are advanced techniques for cleaning and preparing scraped web content for LLM consumption?

Answer: NVIDIA outlines a detailed pipeline for preparing data for LLMs, emphasizing:

- **Download and Extraction:** Gather data and extract it into structured formats such as JSONL for easier downstream processing.

- **Preliminary Text Cleaning:** Correct encoding issues (Unicode fixing), separate languages, and perform other initial cleanups to standardize the raw scraped text.

- **Heuristic Filtering:** Apply both standard and custom filters to the dataset based on specific quality criteria (e.g., remove low-quality or irrelevant content).

- **Deduplication:** Use techniques at multiple levels (exact, fuzzy, semantic) to identify and remove duplicate content, improving dataset diversity and reducing model bias.

- **Model-Based Quality Filtering:** Integrate advanced quality filters, including:
  - **PII Redaction:** Detect and remove personally identifiable information.
  - **Distributed Data Classification:** Use machine learning classifiers to rate or filter content based on quality or relevance.
  - **Task Decontamination:** Ensure training data doesn't leak test set information or unwanted content.

- **Blending and Shuffling:** Combine curated datasets from multiple sources and shuffle them to ensure model exposure to diverse contexts and minimize ordering artifacts.

This pipeline ensures data is not only clean and standardized but also balanced, non-redundant, and free from privacy or contamination risks—crucial for successful LLM training.

-----

-----

### Source [19]: https://www.turing.com/resources/understanding-data-processing-techniques-for-llms

Query: What are advanced techniques for cleaning and preparing scraped web content for LLM consumption?

Answer: Key advanced preprocessing techniques detailed include:

- **Normalization:** Standardizes textual data, enforcing uniformity (e.g., case folding, removing special characters, converting different date formats), which helps LLMs learn patterns more efficiently and reduces spurious variability.

- **Tokenization:** Breaks text into smaller units (words, subwords, or characters), facilitating vocabulary creation and embedding generation. This is foundational for language modeling and understanding.

- **Stemming and Lemmatization:** Reduces words to their base or root form. This minimizes vocabulary size, allowing the model to generalize better and focus on semantic content rather than surface variations.

- **Stop Word Removal:** Eliminates common but information-poor words (e.g., "the," "and") that may add noise and little value to the model's understanding.

- **Noise Removal:** Targets removal of irrelevant elements like HTML tags, special symbols, or formatting artifacts, which are prevalent in scraped web data.

Collectively, these methods ensure the LLM receives clean, standardized, and meaningful input, optimizing both training efficiency and downstream performance.

-----

</details>

<details>
<summary>How can LLMs be used as classifiers or filters for data quality assurance in AI pipelines?</summary>

### Source [20]: https://www.rapidcanvas.ai/blogs/building-better-data-pipelines-with-large-language-models

Query: How can LLMs be used as classifiers or filters for data quality assurance in AI pipelines?

Answer: LLMs can be used as classifiers and filters for data quality assurance by automating critical validation and transformation tasks in data pipelines. They generate data quality rules and tests, ensuring that incoming data meets predefined standards, such as checking for null values, validating data types, and identifying outliers. LLMs can also generate and run code for these checks, reducing manual effort and human error. In addition, they assist in generating and maintaining documentation, making it easier to track changes and collaborate on pipeline projects. For testing and validation, LLMs automatically create test cases and validate data transformations, which helps maintain high accuracy and reliability. Metadata management is another area where LLMs excel—they can generate metadata tags and descriptions, improving data discoverability and understanding. Platforms like RapidCanvas integrate LLMs into data engineering workflows, leveraging their capabilities to enhance code generation, enable natural language interactions with data pipelines, and facilitate best practice sharing among engineers. These features collectively help ensure data flowing through AI pipelines is accurate, consistent, and reliable.

-----

-----

### Source [21]: https://www.bitcot.com/ai-powered-data-pipelines/

Query: How can LLMs be used as classifiers or filters for data quality assurance in AI pipelines?

Answer: LLMs and AI models function as intelligent filters and classifiers in data pipelines by automating anomaly detection and correction at multiple stages. They identify unusual patterns, inconsistent formats, and values outside expected ranges, going beyond rigid rule-based checks. This behavior-based approach catches errors early and adapts dynamically as data evolves. LLMs automate repetitive tasks like categorizing text, extracting fields, normalizing labels, and matching records, reducing manual intervention and maintaining consistency. For validation and quality checks, they compare current data patterns to historical norms, detect subtle anomalies, and assess the plausibility of enriched outputs, providing dynamic quality control that evolves with the dataset. In transformation and normalization phases, LLMs match similar records, standardize labels, and correct inconsistencies by recognizing patterns and applying the most likely interpretations, even as upstream data sources change. Anomaly detection and historical comparison further monitor data health, alerting teams when deviations occur and preventing propagation of subtle issues. By defining data quality thresholds and leveraging these capabilities, AI-powered pipelines maintain reliable performance and resilience.

-----

-----

### Source [22]: https://www.getdbt.com/blog/ai-data-pipelines

Query: How can LLMs be used as classifiers or filters for data quality assurance in AI pipelines?

Answer: In AI pipelines, LLMs and associated automated validation tools are vital for maintaining data quality. These systems implement automated checks to detect anomalies such as missing values and inconsistencies before data reaches the AI models. Tools like dbt enable column-level lineage tracking, which improves auditability and reliability by showing how data is transformed and where it originates. Data transformation processes are automated, ensuring datasets are cleaned, structured, and optimized for downstream AI workflows. Built-in testing frameworks catch errors early, preserving high-quality datasets and preventing unreliable data from impacting model predictions. Continuous monitoring detects data drift, ensuring that changes in data distribution do not degrade model performance. Observability features support maintaining data quality and reliability at scale, enabling teams to trace transformations and document data sources for transparency and accountability. These mechanisms collectively position LLMs and automated tools as data classifiers and filters that protect and enhance data integrity in AI pipelines.

-----

-----

### Source [23]: https://www.telm.ai/blog/demystifying-data-qualitys-impact-on-large-language-models/

Query: How can LLMs be used as classifiers or filters for data quality assurance in AI pipelines?

Answer: LLMs' effectiveness in AI pipelines is highly dependent on the quality of data used for training and fine-tuning. Imbalances in training data, attribute mix-ups, and value truncations can significantly decrease prediction quality, as demonstrated by experiments showing drops in precision when noisy data is used. Data quality tools like Telmai utilize profiling and data monitoring features to detect such issues: identifying label imbalances, spotting attribute mix-ups through pattern analysis, and flagging anomalies in value lengths. These tools automate quality assurance by alerting users to unexpected drifts (row count changes, schema changes, value distribution shifts) without requiring code. Telmai provides visual indicators and anomaly ratings, helping teams quickly identify root causes of data discrepancies. By enabling swift and precise identification of data issues, these systems act as classifiers and filters, ensuring high-quality inputs for LLMs and enhancing the reliability and performance of AI applications, while reducing manual labor and project costs.

-----

-----

### Source [24]: https://www.stauffer.com/news/blog/the-impact-of-ai-and-large-language-models-in-quality-assurance

Query: How can LLMs be used as classifiers or filters for data quality assurance in AI pipelines?

Answer: LLMs and AI significantly enhance quality assurance processes by automating repetitive testing tasks and improving accuracy. These models analyze large codebases, generate test cases, identify bugs, and run regression tests at speeds far surpassing manual efforts. Their consistent and repeatable outputs minimize human errors, especially in complex environments. Machine learning models trained on historical data can predict areas most likely to contain bugs, allowing targeted QA efforts. LLMs further augment QA by enabling sophisticated test case generation and leveraging natural language processing to improve the scope and effectiveness of testing. This automation allows QA teams to focus on complex tasks, leading to better resource utilization and cost savings. The adoption of LLMs in QA results in robust, high-quality software releases, faster development cycles, and higher reliability—demonstrating their role as classifiers and filters for data quality in the broader AI pipeline context.

-----

</details>

<details>
<summary>What are best practices for creating a final, auditable research artifact from multiple data sources like web scrapes, API results, and document transcripts?</summary>

### Source [25]: https://github.com/ITI/releasing-research-artifacts

Query: What are best practices for creating a final, auditable research artifact from multiple data sources like web scrapes, API results, and document transcripts?

Answer: Best practices for creating a final, auditable research artifact from multiple data sources include:

- **Specification of dependencies**: Clearly list all software, libraries, tools, and platform requirements necessary to use or reproduce the artifact. This increases the likelihood of re-use by others, regardless of their technical background.

- **Artifact completeness**: Ensure all components required to validate the research are included. This encompasses data, scripts, configuration files, and documentation necessary for others to run analyses or reproduce results.

- **Clear, concise instructions**: Provide straightforward instructions for setup and use, ideally in a README file. Instructions should not assume prior familiarity with the artifact's technology stack.

- **Reproducibility support**: Whenever feasible, supply a fully reproducible version of the artifact, such as a Docker image and Dockerfile. This allows users to recreate the environment and results without manual configuration.

- **Standard formats**: Favor open, well-known data formats over proprietary ones to maximize accessibility and ease of integration with other research. If proprietary formats are needed, point to supporting tools or converters.

- **Public accessibility**: Host artifacts in widely used, accessible repositories (such as GitHub or DockerHub) to aid discovery, citation, and long-term preservation.

- **README template**: Use templates for documentation to ensure all critical information is included and consistently presented, improving discoverability and usability of the artifact.

-----

-----

### Source [26]: https://www.sigmobile.org/grav/about/artifact-guidelines

Query: What are best practices for creating a final, auditable research artifact from multiple data sources like web scrapes, API results, and document transcripts?

Answer: To ensure a research artifact is final and auditable, the ACM SIGMOBILE Artifact Evaluation Guidelines recommend:

- **Artifact availability**: Make the artifact (data, code, documentation) available to external parties for testing and validation.

- **Minimum working example**: Include a simple, self-contained example demonstrating basic functionality, so users or evaluators can quickly verify operation.

- **Detailed installation and usage instructions**: Provide an appendix or separate documentation with explicit steps to set up, install, and run the artifact, including hardware/software requirements and expected runtimes for key components.

- **Reusability and replicability**: While availability is the top priority, also aim for artifacts to be reusable and results to be replicable by others, recognizing that evaluation complexity may limit what is feasible.

- **Versioning and referencing**: Ensure the artifact matches the final version of the associated paper or research report, so evaluation is accurate and results are reproducible.

- **Public demonstration and review**: Support artifact demonstrations at conferences and/or through public testbeds, allowing independent verification and transparency.

- **Replication tolerance**: Define clearly what constitutes acceptable variance in reproducing results, to set expectations for auditors and users.

- **Appendices and documentation**: Augment publications with appendices providing artifact-use guidance, enhancing the reproducibility and auditability for the research community.

-----

-----

### Source [27]: https://www.interaction-design.org/literature/topics/artifact

Query: What are best practices for creating a final, auditable research artifact from multiple data sources like web scrapes, API results, and document transcripts?

Answer: Effective practices for research artifacts, particularly for UX and multi-source research, include:

- **Focus on actionable insights**: Rather than presenting raw data from scrapes, APIs, or transcripts, synthesize key findings into recommendations or conclusions that directly inform decisions or further research. This turns the artifact into a useful decision-making tool.

- **Triangulation and validation**: Validate findings by cross-referencing multiple sources (e.g., web scrapes, APIs, transcripts) to ensure reliability and confidence in the conclusions. This strengthens the artifact's credibility.

- **Anonymization and privacy**: When including direct quotes or examples, anonymize sensitive information to protect data privacy, especially if sources contain personal or protected information.

- **Design for diverse audiences**: Structure the artifact so it is understandable and actionable for different stakeholders, not just technical experts. This includes clear language, summaries, and visualizations where appropriate.

- **Documentation of process and sources**: Clearly document how data was collected, processed, and synthesized. This transparency is essential for auditability and for others to verify or build upon the research.

-----

-----

### Source [28]: https://www.absoluteproduct.com/article/the-importance-of-comprehensive-artifact-documentation-in-museums

Query: What are best practices for creating a final, auditable research artifact from multiple data sources like web scrapes, API results, and document transcripts?

Answer: Comprehensive documentation is crucial for auditable artifacts. Best practices highlighted for artifact records, which are transferable to research artifacts, include:

- **Detailed descriptions and cataloguing**: Record all relevant metadata—provenance, context, dimensions, and unique identifiers—for each data source or component, ensuring traceability and auditability.

- **Standardized cataloguing practices**: Use consistent, standardized formats and terminology for metadata, which facilitates organization, retrieval, and future audits.

- **Digital management systems**: Employ robust digital databases or management systems to store, track, and update artifact records. This ensures data integrity, ease of access, and security for multi-source artifacts.

- **Training and standardization**: Ensure that everyone contributing to the artifact follows the same documentation protocols. Consistency is key to maintaining accuracy and reducing errors or ambiguities across the research artifact.

-----

</details>

<details>
<summary>How can prompt engineering be used to implement flexible human-in-the-loop (HITL) checkpoints in an AI agent's workflow without changing the underlying code?</summary>

### Source [29]: https://aws.amazon.com/blogs/machine-learning/building-generative-ai-prompt-chaining-workflows-with-human-in-the-loop/

Query: How can prompt engineering be used to implement flexible human-in-the-loop (HITL) checkpoints in an AI agent's workflow without changing the underlying code?

Answer: Prompt engineering can be used to integrate flexible human-in-the-loop (HITL) checkpoints into an AI agent’s workflow by structuring tasks as a series of prompts (prompt chaining) and leveraging workflow orchestration tools (such as AWS Step Functions) that support human review without modifying the underlying code of the AI model. Prompt chaining breaks down complex tasks into smaller, manageable subtasks, each represented by a focused prompt. This modular approach allows checkpoints to be inserted between subtasks, where human judgment can be invoked for validation or approval.

A practical implementation involves designing the workflow to pause at certain steps by using mechanisms like "Wait for a Callback with Task Token." At these checkpoints, the workflow sends relevant information (generated by the AI in response to a prompt) to a human reviewer (for example, via email or a dashboard). The reviewer then approves or rejects the content. Their decision is returned to the workflow, which then resumes execution based on the outcome. This architecture means HITL can be introduced or adjusted by modifying the workflow logic and prompt structures rather than changing the underlying AI agent code. For example, you can add, remove, or reconfigure human review steps in the workflow, making the system highly flexible for different scenarios, all while keeping the core AI logic unchanged.

-----

-----

### Source [30]: https://humanloop.com/blog/prompt-engineering-101

Query: How can prompt engineering be used to implement flexible human-in-the-loop (HITL) checkpoints in an AI agent's workflow without changing the underlying code?

Answer: Prompt engineering allows for flexible control over the behavior of large language models (LLMs) by specifying clear, direct instructions and desired outcomes directly in the prompt. You can define desired checkpoints or review stages by including explicit instructions within the prompt, such as requesting confirmation or review from a human before proceeding. Additionally, prompts can be structured to request the AI to flag uncertain or high-risk outputs for human review, effectively embedding HITL checkpoints at the instruction level without code changes.

For example, the prompt could contain: "If you are not confident in your answer, respond with: 'Needs human review.'" This approach leverages the model's ability to follow natural language instructions, so humans can dynamically step in when needed based on the prompt's logic. As the workflow is dictated by the prompt structure and instructions, inserting or modifying HITL checkpoints is a matter of updating the prompt rather than changing the application code.

-----

-----

### Source [31]: https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo

Query: How can prompt engineering be used to implement flexible human-in-the-loop (HITL) checkpoints in an AI agent's workflow without changing the underlying code?

Answer: A common pattern for implementing HITL checkpoints with prompt engineering involves designing the workflow around explicit decision points where human input is required. The agent processes a prompt, proposes an action, and then pauses execution to route the request to a human reviewer using an explicit interrupt (such as an `interrupt()` function or similar mechanism in the workflow engine). The human receives contextualized information, reviews the proposed action, and either approves or rejects it. The agent then resumes operation based on the human's decision.

Prompts play a key role in this process by clearly communicating to the human reviewer what decision is required, summarizing the relevant context, and explaining why approval or input is needed. This approach keeps prompts lightweight and focused, ensuring the HITL checkpoints are understandable and actionable without modifying the underlying AI code. By designing workflows where prompts and interruptions are used to define review points, you can flexibly insert or remove HITL steps as business needs evolve.

-----

</details>

<details>
<summary>What are the most effective strategies for an LLM to automatically evaluate and filter web search results for authority, relevance, and trustworthiness?</summary>

### Source [32]: https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full

Query: What are the most effective strategies for an LLM to automatically evaluate and filter web search results for authority, relevance, and trustworthiness?

Answer: This source proposes a framework where LLMs evaluate web search results using three main methodologies: Pointwise, Pairwise, and Pass/Fail assessments. The evaluation process begins with a structured parsing of the user query, converting it into JSON format with key attributes (such as category, filters, location, and keywords). For each parsed result, a tailored evaluation prompt is constructed, which includes the user query, parsed output, domain-specific evaluation criteria (like category accuracy, filter accuracy, location accuracy, keyword accuracy, synonym accuracy, completeness), rating rubrics for the evaluation method, and few-shot examples to anchor the LLM’s reasoning. The LLM then evaluates the result by assigning scores (Pointwise), selecting preferred options (Pairwise), or providing a binary judgment (Pass/Fail), each with an explanation. The framework also introduces 'Contextual Evaluation Prompt Routing,' which dynamically selects domain-specific prompts based on query categories, enhancing contextual relevance and reducing hallucinations. Experiments show that this strategy achieves over 90% agreement with human judgments, validating it as a scalable and interpretable method for automated evaluation of authority, relevance, and trustworthiness in search systems.

-----

-----

### Source [33]: https://arxiv.org/html/2504.14401v1

Query: What are the most effective strategies for an LLM to automatically evaluate and filter web search results for authority, relevance, and trustworthiness?

Answer: This study refines LLM-based evaluation by focusing on 'usefulness' in addition to traditional relevance, recognizing that authority and trustworthiness are closely tied to user goal achievement. The methodology aggregates user behavior metrics (such as click-through rate, dwell time, satisfaction scores) and document features to form structured prompts for the LLM. The LLM is instructed to act as a 'search quality rater' using detailed session histories and Google’s evaluator guidelines. Evaluation rubrics (TRUE) guide the LLM through a step-by-step Chain-of-Thought reasoning process, decomposing the task into smaller judgments based on predefined metrics. Fine-tuned LLMs, given structured session context, show improved ability to differentiate relevance from usefulness, and experiments demonstrate that rubric-based prompts yield usefulness scores that align closely with human judgments. The ablation study highlights that well-defined criteria and detailed context are crucial for consistent, reliable evaluation, especially at scale.

-----

-----

### Source [34]: https://www.evidentlyai.com/llm-guide/llm-as-a-judge

Query: What are the most effective strategies for an LLM to automatically evaluate and filter web search results for authority, relevance, and trustworthiness?

Answer: This guide describes how LLMs can be used to evaluate the quality of search results by employing ranking metrics such as NDCG (Normalized Discounted Cumulative Gain) and precision at K. These metrics measure how well the system ranks documents according to their relevance and usefulness to the user's query. Evaluations are typically performed offline, iterating over different search strategies and parameter settings to optimize for authority and relevance. LLMs act as judges by evaluating the ranked lists and scoring the results, providing a practical alternative to manual human evaluations. The approach is especially useful for large-scale or iterative system development, where human-based assessments would be too costly.

-----

-----

### Source [35]: https://mirascope.com/docs/mirascope/guides/evals/evaluating-web-search-agent

Query: What are the most effective strategies for an LLM to automatically evaluate and filter web search results for authority, relevance, and trustworthiness?

Answer: This source outlines strategies for monitoring and evaluating LLM-powered web search agents. Functional monitoring tracks metrics such as response time, token usage, error rates, and costs to ensure reliability. Prompt monitoring involves checking user inputs and LLM prompts for toxic content, embedding distance (measuring semantic relevance), and identifying malicious prompt injections. Response monitoring analyzes outputs for hallucinations (false information), topic divergence (staying on topic), and tone/sentiment. These monitoring practices help filter results for trustworthiness and relevance by systematically identifying and addressing issues that affect output quality and user experience.

-----

-----

### Source [36]: https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches

Query: What are the most effective strategies for an LLM to automatically evaluate and filter web search results for authority, relevance, and trustworthiness?

Answer: This source reviews four main approaches for evaluating LLM outputs, focusing on answer-choice accuracy using multiple-choice benchmarks such as MMLU (Massive Multitask Language Understanding). These benchmarks assess how accurately an LLM can select correct answers from a set of choices, serving as a proxy for authority and factual correctness. The use of standardized datasets enables consistent measurement and comparison, ensuring that LLMs meet predefined accuracy standards. While this approach primarily evaluates correctness, it indirectly supports filtering for authority and trustworthiness by aligning LLM outputs with established knowledge and benchmarks.

-----

</details>

<details>
<summary>What are the trade-offs between snippet-based research from search APIs versus full-content scraping of selected URLs for AI-driven article writing?</summary>

### Source [37]: https://www.scrapingdog.com/blog/web-scraping-vs-api/

Query: What are the trade-offs between snippet-based research from search APIs versus full-content scraping of selected URLs for AI-driven article writing?

Answer: Web scraping offers significant flexibility and the ability to extract a wide range of data from virtually any publicly accessible web page. This makes it ideal for scenarios where APIs are unavailable, or when the goal is to collect data from multiple diverse sources. Scrapers can be customized to collect specific data and scheduled for regular updates, ensuring freshness. However, web scraping poses challenges such as legal risks, maintenance burdens due to site changes, and the need to manage anti-scraping defenses like CAPTCHAs. Infrastructure costs and the requirement for intense data cleaning are also notable drawbacks.

APIs, on the other hand, provide clean, fast, and structured access to data, typically in machine-readable formats like JSON or XML. They are generally more reliable, scalable, and easier to integrate, with the added benefit of bypassing issues like JavaScript rendering and CAPTCHAs. However, APIs often have rate limits, may expose only a limited subset of data, and are subject to the provider’s control and potential costs. Full-content access is typically restricted compared to scraping. In summary, the trade-off is between the flexibility and breadth of web scraping versus the efficiency, reliability, and structure of API-based snippet retrieval.

-----

-----

### Source [38]: https://brightdata.com/blog/web-data/web-scraping-vs-api

Query: What are the trade-offs between snippet-based research from search APIs versus full-content scraping of selected URLs for AI-driven article writing?

Answer: Web scraping is a customizable method to retrieve data directly from any public website by parsing HTML and extracting desired content. The process requires site-specific logic and can be applied to static or dynamic sites. Its main advantage is the ability to scrape data from any website, regardless of whether an official API exists. However, the approach is highly dependent on the target site's structure, which can change and break scraping logic, affecting stability and scalability.

APIs, in contrast, are official interfaces provided by websites or data providers. They guarantee stability, scalability, and performance, as these factors are managed by the API provider. The downside is that only a limited number of sites offer APIs, and the available data is restricted to what the API exposes. For AI-driven article writing, this means snippet-based research via APIs is more stable and easier to automate but may lack depth and coverage, while full-content scraping can offer more comprehensive data at the cost of higher technical overhead and maintenance.

-----

-----

### Source [39]: https://www.seoclarity.net/blog/scraping-vs.-api

Query: What are the trade-offs between snippet-based research from search APIs versus full-content scraping of selected URLs for AI-driven article writing?

Answer: UI (full-content) scraping captures the entire user-facing output, including all formatting, citations, brand mentions, and contextual phrasing, mirroring the actual experience of end users. This method is essential when a complete and accurate representation of what users see is required, particularly as the UI may include additional logic, browsing content, or dynamic presentation elements not available via the API. The trade-off is greater technical effort, as scraping requires simulating real user sessions and handling dynamic web elements.

API-based snippet research provides structured, text-only responses, which are consistent and easy to process. However, APIs typically offer only a simplified, developer-focused version of the content, lacking the formatting, branding, shopping integrations, and dynamic enhancements present in the UI. For AI-driven article writing, API access is efficient but may miss critical context and nuances present in full-content scraping.

-----

-----

### Source [40]: https://oxylabs.io/blog/api-vs-web-scraping

Query: What are the trade-offs between snippet-based research from search APIs versus full-content scraping of selected URLs for AI-driven article writing?

Answer: Web scraping provides complete control and customization for data extraction from any web page, making it possible to handle complex scenarios and dynamic content. It incurs no additional costs beyond infrastructure and labor but requires ongoing maintenance, as changes in website structures can break scrapers. Anti-scraping measures and IP blocking must be managed, increasing technical complexity and operational overhead.

APIs return structured content in formats like JSON, offering greater stability and efficiency. They are easier to use and maintain, but often come with restrictions on data availability, usage quotas, and possible costs. For AI-driven article writing, snippet-based research via APIs is more sustainable and less resource-intensive, but full-content scraping allows for more comprehensive data collection at the expense of higher development and maintenance demands.

-----

</details>

<details>
<summary>What are the benefits of a "file-first" design pattern in multi-step AI agent workflows for ensuring auditability and simplifying debugging?</summary>

### Source [41]: https://valanor.co/design-patterns-for-ai-agents/

Query: What are the benefits of a "file-first" design pattern in multi-step AI agent workflows for ensuring auditability and simplifying debugging?

Answer: A file-first (or modular) design pattern in multi-step AI agent workflows offers several benefits for auditability and debugging:

- **Modular design** breaks workflows into explicit, isolated stages. Each stage handles a specific part of the workflow, making it easier to pinpoint issues when debugging. If a problem arises, teams can trace it to a specific component rather than searching through a large, monolithic process.

- **Transparency and auditability** are improved because workflows remain interpretable. Each step’s inputs and outputs are clearly defined and often logged, producing a transparent record of the agent's decision-making process. This is essential for compliance and post-mortem analysis.

- Tools such as **LangGraph** structure complex agent workflows into explicit stages, which further enhances the ability to audit and debug by making the workflow stages visible and trackable.

- Overall, this approach simplifies maintenance and updates: since each stage is modular, changes or improvements can be made in isolation without risking unintended side effects elsewhere in the workflow.

-----

-----

### Source [42]: https://machinelearningmastery.com/7-must-know-agentic-ai-design-patterns/

Query: What are the benefits of a "file-first" design pattern in multi-step AI agent workflows for ensuring auditability and simplifying debugging?

Answer: The sequential (file-first) design pattern in AI agent workflows provides predictability and clarity because each step is handled by a specific agent in a fixed order. This structure offers the following benefits for auditability and simplifying debugging:

- **Predictable behavior:** The fixed sequence of steps ensures that the process is easy to follow and understand, making it straightforward to identify where issues occur.

- **Simplified debugging:** Knowing which agent or stage is responsible for each part of the workflow makes troubleshooting direct and efficient. If an error occurs, you can quickly narrow it down to a particular step or file.

- **Clear role separation:** Each agent or module is responsible for a distinct task, reducing ambiguity and making it easier to audit the workflow by retracing the flow and examining logs at each stage.

- This pattern is best suited for workflows that are structured and rarely change, further enhancing stability and reliability in audit and debugging processes.

-----

-----

### Source [43]: https://techcommunity.microsoft.com/blog/azurearchitectureblog/building-ai-agents-workflow-first-vs-code-first-vs-hybrid/4466788

Query: What are the benefits of a "file-first" design pattern in multi-step AI agent workflows for ensuring auditability and simplifying debugging?

Answer: Workflow-first (which aligns closely with file-first) platforms enable auditability and ease of debugging by abstracting orchestration logic into declarative, visual models rather than imperative code. The main advantages include:

- **Governance and observability baked in:** These platforms have built-in monitoring and observability tools, making it easy to track and audit agent actions across each step of the workflow.

- **Visual representation of workflows:** The visual or declarative modeling of workflows means each step is explicit, making it easier to identify where issues occur and to understand the flow for audit purposes.

- **Durable and compliant workflows:** Such frameworks enable pause/resume functionality, human-in-the-loop approvals, and integration with observability standards like OpenTelemetry, all of which contribute to traceability and auditability.

- **Rapid prototyping and controlled customization:** Developers can quickly iterate on workflows and debug visually, while still having the flexibility to dive into code for more advanced scenarios, ensuring that both business users and engineers can trace and audit the process at the right level of abstraction.

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>The provided markdown content is about general AI agent design patterns and does not align with the specific "Lesson 19 Guideline" which focuses on completing a research agent using MCP tools, quality control, and compilation steps. Therefore, the entire content is irrelevant to the specified article guidelines.</summary>

The provided markdown content is about general AI agent design patterns and does not align with the specific "Lesson 19 Guideline" which focuses on completing a research agent using MCP tools, quality control, and compilation steps. Therefore, the entire content is irrelevant to the specified article guidelines.

</details>

<details>
<summary>LLM-as-a-Judge: automated evaluation of search query parsing using large language models</summary>

# LLM-as-a-Judge: automated evaluation of search query parsing using large language models

**Introduction:** The adoption of Large Language Models (LLMs) in search systems necessitates new evaluation methodologies beyond traditional rule-based or manual approaches.

**Methods:** We propose a general framework for evaluating structured outputs using LLMs, focusing on search query parsing within an online classified platform. Our approach leverages LLMs' contextual reasoning capabilities through three evaluation methodologies: Pointwise, Pairwise, and Pass/Fail assessments. Additionally, we introduce a Contextual Evaluation Prompt Routing strategy to improve reliability and reduce hallucinations.

**Results:** Experiments conducted on both small- and large-scale datasets demonstrate that LLM-based evaluation achieves approximately 90% agreement with human judgments.

**Discussion:** These results validate LLM-driven evaluation as a scalable, interpretable, and effective alternative to traditional evaluation methods, providing robust query parsing for real-world search systems.

## 1 Introduction

The adoption of large language models (LLMs) in search systems is fundamentally reshaping how these systems function, driving the emergence of generative search beyond traditional retrieval methods. This shift introduces new challenges in the evaluation of search system performance, especially in real-world applications such as online classified ads platforms, where accurately interpreting user search queries is essential to improve the retrieval and ranking quality ( [Luo et al., 2023](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B13)).

shows the parsing of an example search query in an online ads platform and a sketch of the evaluation process proposed in this work. The search system extracts structured information from the user query given in natural language, including query category, search filters, location, explicit and implicit keywords, synonyms, and other relevant attributes. The extracted elements are represented in a structured form which is used as the basis for evaluation. Unlike traditional syntactic parsing, search systems parse based not only on the textual features of the query but also on its semantics and contexts. This implies that the system infers implicit intentions, resolves ambiguities, and maps the query to a structured representation that aligns with its underlying meaning rather than just its surface form.

Traditional evaluation methods for search query parsing such as exact match, precision, recall, and rule-based heuristics like the number of search results returned often struggle to fully reflect the query understanding capability of the systems used in complex applications ( [Lee et al., 2021](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B9)). Additionally, these approaches may not effectively capture the semantic nuances of the parsed user queries, leading to limited generalizability. Task-specific evaluation methods, such as checking whether a query retrieves the correct results or measuring how users interact with search results, can provide better assessments. However, these methods are highly dependent on domain specific rules and are difficult to apply across different search systems, making them less flexible ( [Jiang and Cai, 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B7)). Moreover, manual evaluation methods, which involve human annotators assessing query parsing results, are both time-consuming and expensive, making them impractical for large-scale, real-time systems. Due to the ambiguity inherent in natural language, there is often no single correct output for a given query, as multiple valid structured representations may exist depending on subtle differences in context and user intent. Traditional evaluation methods rely on rigid comparisons against predefined reference outputs and thus cannot handle cases where multiple outputs are equally valid or where errors are subtle yet impactful. Consequently, a more context-aware and flexible evaluation approach is necessary to assess the effectiveness of the search system in understanding and structuring user queries.

The challenge is particularly evident in high-traffic environments such as e-commerce platforms, where the ability to accurately parse user queries into structured representations is crucial for delivering relevant search results. In these scenarios, traditional evaluation methods face difficulties in scaling to the vast number of user queries, ensuring real-time adaptability, and mitigating inconsistencies in human-labeled reference datasets. Beyond these commonly-used methods, other automated evaluation techniques, such as BLEU ( [Papineni et al., 2002](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B15)) for n-gram overlap or Smatch ( [Cai and Knight, 2013](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B1)) for Abstract Meaning Representation (AMR), have shown promise but cannot fully address the complexity of evaluating structured outputs like search query parsing results.

The LLM-as-a-Judge framework initially emerged as a promising approach for evaluating various natural language processing (NLP) tasks, providing an automated and scalable alternative to human assessments. Over time, its application has expanded to include the evaluation of structured outputs of various systems. While still an evolving method, it offers the potential for more scalable and consistent assessments compared to traditional techniques. Recent research ( [Schneider et al., 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B17)) has demonstrated that LLMs can effectively evaluate semantic parsing tasks by leveraging their ability to understand natural language nuances and assess the correctness of structured outputs beyond surface-level lexical matching.

In this work, we employ automated LLM-based evaluation methods for assessing search query parsing systems, which leverage the reasoning and contextual understanding capabilities of LLMs. Unlike rule-based or heuristic evaluation methods, which may fail to generalize across different query formulations, LLMs offer a more nuanced and adaptable evaluation framework. These methods enable the system to be assessed not just on surface-level correctness but also on semantic fidelity, intent alignment, and contextual appropriateness. By integrating LLM-as-a-Judge methods, we ensure a more robust and scalable evaluation of search query parsing in large-scale, real-world search systems, where accuracy and efficiency are critical. However, integrating LLMs into evaluation pipelines introduces new complexities, necessitating careful design to ensure reliability, efficiency, and alignment with human judgment. In this work, we explore strategies to mitigate these challenges, refining LLM-based evaluations to enhance consistency and reduce hallucinations, ultimately making them a viable alternative to both costly and labor-intensive human evaluations and evaluations made by traditional syntax-based/word-based metrics.

We explore three distinct LLM-as-a-Judge methodologies: _Pointwise Evaluation, Pairwise Evaluation_, and _Pass/Fail Evaluation_. Our approach builds upon existing research in semantic parsing evaluation, incorporating elements from both traditional metrics like Smatch and newer LLM-based assessment techniques. We conduct extensive experiments using various LLMs, prompting strategies, and evaluation techniques, and demonstrate that our LLM-as-a-Judge framework achieves over 90% alignment with human judgments across evaluation types. Furthermore, we introduce a _Contextual Evaluation Prompt Routing_ strategy within LLM evaluation to enhance the efficiency of the evaluation and mitigate LLM hallucinations. Our findings validate the effectiveness of LLM-driven automated evaluation for search query parsing in large-scale, real-world search systems, offering a scalable and adaptable evaluation pipeline that minimizes manual effort. Beyond structured output evaluation, we also examine the reliability of our LLM evaluator framework using statistical agreement metrics to ensure the robustness of LLM-based assessments.

The contributions in this work are as follows:

• We propose an evaluation framework that leverages large language models for context-aware, interpretable, and scalable evaluation of structured outputs.

• We apply the proposed evaluation framework to search query parsing by adapting the Pointwise, Pairwise, and Pass/Fail evaluation strategies to address various assessment requirements.

• We introduce the Contextual Evaluation Prompt Routing strategy as a domain-specific solution for dynamically adjusting evaluation prompts based on query categories, enabling more accurate and context-aware assessment of structured search query parsing outputs.

• We show that the proposed framework, particularly the Contextual Evaluation Prompt Routing strategy, substantially improves the evaluation accuracy and reliability compared to baseline methods.

## 2 Related work

The evaluation of search query parsing and semantic parsing systems has been a longstanding challenge in NLP and information retrieval (IR). Various methods ranging from rule-based systems to neural models have been proposed to improve parsing accuracy and assessment. Recently, LLM-as-a-Judge has emerged as a promising approach for evaluating structured outputs, offering scalability and adaptability across different domains. In this section, we review traditional evaluation methods for search query parsing, discuss general LLM-as-a-Judge techniques, and explore domain-specific applications of LLM-as-a-Judge, particularly in search and semantic parsing systems.

### 2.1 Traditional evaluation methods

Traditional evaluation methods for search query parsing and semantic parsing rely on exact match accuracy, precision-recall metrics, and rule-based heuristics. While these approaches measure the correctness by comparing system outputs to reference query outputs, they often fail to capture semantic equivalence, penalizing valid variations in structured outputs ( [Lee et al., 2021](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B9)). Early methods assessed correctness through query execution accuracy, where system-generated queries are executed against a database and the returned results determine the accuracy ( [Jiang and Cai, 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B7)). While this approach is applicable in search query parsing, evaluating the correctness of the results still requires manual judgments. [Luo et al. (2023)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B13) introduced precision and coverage metrics to evaluate attribute extraction, but these methods require manual judgments, making them less scalable.

With the rise of neural semantic parsers, evaluation techniques increasingly incorporated denotation-based methods while retaining other approaches. Denotation-based evaluation, which compares execution results rather than output structures, was already used in non-neural settings and gained further prominence with neural models. Additionally, though initially designed for machine translation, statistical metrics like BLEU ( [Papineni et al., 2002](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B15)) continued to be used for assessing semantic parsing outputs. However, these approaches face some challenges:

• Spurious matches—Incorrect queries may produce correct results by chance.

• Over-penalization—Semantically correct but syntactically different outputs are unfairly penalized.

• Lack of semantic awareness—BLEU and similar metrics fail to capture deep semantic understanding.

Graph-based evaluation metrics like Smatch ( [Cai and Knight, 2013](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B1)) attempt to address these issues by measuring semantic structure similarity rather than strict string matching. While effective, these methods are computationally expensive and not widely used in search query parsing.

Overall, traditional evaluation methods struggle with generalization, adaptability, and deeper semantic reasoning. This highlights the need for more semantically oriented evaluators, which can assess semantic correctness beyond surface-level comparisons. Our work builds on these findings by employing LLM-as-a-Judge to evaluate structured search query parsing, ensuring alignment with user intent and domain-specific accuracy.

### 2.2 LLM-as-a-Judge for automated evaluation

LLM-as-a-Judge has gained traction as a scalable alternative to human evaluations across various NLP tasks, including text summarization, dialogue evaluation, and semantic parsing. The concept leverages the reasoning capabilities of large language models to assess system outputs, reducing reliance on costly human annotations while maintaining evaluation consistency and scalability.

A comprehensive survey by [Gu et al. (2025)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B6) explores how LLM-as-a-Judge can enhance evaluation reliability by addressing challenges such as bias mitigation, prompt engineering, and standardization of evaluation methodologies. The study highlights that LLMs offer more nuanced assessments compared to rule-based or heuristic metrics, particularly in tasks requiring semantic alignment rather than syntactic matching. Similarly, [Li H. et al. (2024)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B11) provide a structured framework for constructing LLM-based evaluation pipelines, addressing how LLMs can be utilized effectively, where they perform best and how they should be assessed.

Another critical aspect is the evaluation process itself. [Chiang and Lee (2023)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B2) analyze different strategies, revealing that forcing LLMs to output only a single numeric rating is suboptimal, while prompting LLMs to explain their ratings significantly improves alignment with human judgments. These findings emphasize the importance of prompt engineering and structured evaluation prompts to enhance the reliability of LLM-generated assessments.

Despite their advantages, LLM-based evaluators are prone to stochastic variability, position bias, verbosity bias, and self-enhancement bias. [Zheng et al. (2023)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B21) highlight these limitations in their study on MT-Bench and Chatbot Arena, demonstrating that while LLM judges such as GPT-4 align with human preferences over 80% of the time, they still require bias mitigation techniques to ensure fair assessments. To address reliability concerns, researchers have explored adaptive evaluation techniques. [Shankar et al. (2024)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B19) introduce EvalGen, a system that refines evaluation prompts through human-in-the-loop feedback. They identify criteria drift, where evaluation criteria evolve as human reviewers assess more outputs. This aligns with our prompt engineering with iterative refinement approach, which systematically optimizes evaluation prompts to enhance consistency and reduce hallucinations. In our experiments, since we use evaluators from the same model family we do not consider self-enhancement bias a significant threat. However, position bias and stochastic variability remain critical challenges in our context. This study explicitly addresses these two sources of evaluation instability through experimental controls such as randomized response ordering and repeated runs with majority voting or averaging to enhance robustness.

A major challenge in LLM-based evaluation is result consistency across multiple replications. [Schroeder and Wood-Doughty (2024)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B18) introduce McDonald's omega as a measure of evaluation reliability, assessing how sensitive LLM evaluators are to small variations in input conditions. Their study emphasizes that single-shot evaluations may introduce inconsistencies, reinforcing the need for multiple evaluation iterations and statistical reliability measures, which is an approach we integrate into our study.

While these studies focus on LLM-based evaluation across general NLP tasks, their insights inform our approach to evaluating structured outputs in search query parsing. Our study extends this paradigm by adapting LLM-as-a-Judge to structured JSON-like evaluations, ensuring that search query parsing accuracy is assessed through semantic correctness, intent alignment, and contextual appropriateness rather than surface-level comparisons.

### 2.3 Domain-specific LLM-as-a-Judge and its application in search query parsing

While LLM-as-a-Judge has been widely explored in general text generation and evaluation tasks, its application in domain-specific structured evaluation, such as search query parsing and semantic parsing, presents additional challenges. Unlike free-text evaluation, query parsing evaluation requires assessing structured outputs, including logical forms, database queries, or graph representations. Recent research has focused on adapting LLM-based evaluation frameworks to domain-specific tasks, ensuring that evaluations align with business needs, structured information retrieval, and reasoning-intensive applications.

A key challenge in domain-specific LLM-based evaluation is the need for custom evaluation criteria. [Zhang et al. (2024)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B20) introduce TALEC, a model-based evaluation method that enables users to flexibly define their own evaluation criteria based on domain requirements. Their approach leverages zero-shot and few-shot in-context learning (ICL) to teach LLMs in-house evaluation rules, improving adaptability across different business scenarios. By combining prompt engineering with iterative refinement, TALEC achieves over 80% correlation with human judgments, demonstrating that LLM-as-a-Judge can accurately reflect domain-specific quality standards. Our work builds upon these findings by applying the Contextual Evaluation Prompt Routing strategy to search query parsing evaluation, where domain-specific prompts are dynamically selected based on query categories, ensuring that evaluation criteria remain contextually relevant.

Another critical aspect of LLM-based evaluation in domain-specific applications is the construction of specialized evaluation datasets. [Raju et al. (2024)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B16) propose a data pipeline for curating domain-specific evaluation sets, addressing the limitations of general-purpose benchmarks like AlpacaEval 2.0 LC ( [Dubois et al., 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B4)) and Arena-Hard v0.1 ( [Li T. et al., 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B12)). Their method integrates manual curation, semi-supervised clustering, and stratified sampling to create balanced evaluation datasets covering diverse domains such as law, medicine, and multilingual contexts. This approach significantly improves benchmark separability (84%) and agreement with human preferences (84%), demonstrating the importance of tailored evaluation datasets for LLM-as-a-Judge frameworks. Our study aligns with this research by constructing manually labeled validation sets for search query parsing evaluation, ensuring that assessments align with human preferences and domain-specific accuracy requirements.

Beyond domain-specific benchmarks, LLM-as-a-Judge has also been explored in reasoning-intensive retrieval tasks. JudgeRank ( [Niu et al., 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B14)) introduces a three-step agentic reranking approach, where query analysis, document summarization, and relevance judgment are performed sequentially to improve retrieval accuracy in retrieval-augmented generation (RAG) systems. Their method outperforms dense retrieval baselines on reasoning-intensive tasks, highlighting the potential of LLMs in structured evaluation. While JudgeRank focuses on ranking search results, its stepwise reasoning approach informs our multi-step query parsing evaluation framework, where LLMs assess query understanding based on extracted structured attributes rather than document rankings.

Finally, evaluating semantic parsing for knowledge-based conversational question answering has revealed important insights into LLM performance on structured outputs. [Schneider et al. (2024)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B17) evaluate LLMs in generating structured graph queries from natural language, demonstrating that few-shot prompting and fine-tuning techniques improve performance on structured parsing tasks. Their findings suggest that zero-shot performance is often inadequate for complex structured outputs, reinforcing our decision to incorporate few-shot prompting and iterative refinements in LLM-based search query parsing evaluation.

Overall, these studies highlight the importance of domain-specific criteria, specialized benchmarks, reasoning-driven evaluation strategies, and structured query assessment in adapting LLM-as-a-Judge to search query parsing and semantic parsing applications. Our work extends these efforts by introducing a scalable, structured evaluation pipeline, leveraging LLM-as-a-Judge for assessing query parsing outputs in real-world search systems.

## 3 Methodology

In this section, we propose a general framework for evaluating structured outputs using the LLM-as-a-Judge approach. Structured outputs, such as those in semantic and search query parsing, require both semantic understanding and structural consistency, making their evaluation more complex than rule-based assessments. We demonstrate our framework through the evaluation of search query parsing in an online advertisement platform. However, the proposed approach is not limited to this task. Instead, it provides a scalable and adaptable evaluation methodology for assessing structured outputs across various domains. To ensure reliable and interpretable evaluations, our framework incorporates structured evaluation prompts. Additionally, we introduce a Contextual Evaluation Prompt Routing strategy to improve evaluation efficiency and mitigate hallucinations in LLM-based assessments.

The LLM-as-a-Judge framework proposed in this work is depicted in . The framework follows a structured approach to assess the quality of the results of the parsed search query. The process begins with a user query that is given to the search query parser. The search query parser converts the query into a structured format, capturing attributes such as category, filters, location, and keywords by making use of information about categories (vehicle, real estate, etc.) and filters (vehicle condition, room size, etc.) encoded in trees. This parsed output is then evaluated through three distinct methods: pointwise evaluation, pairwise evaluation, and pass/fail evaluation. To perform evaluations, an evaluation prompt is given to the LLM-as-a-Judge as input. This evaluation prompt consists of domain-specific evaluation criteria, rating rubrics customized for each evaluation method, enough few-shot examples so that the LLM can learn how to evaluate from context, and the search query parsing system prompt to understand the category and filter information. Each evaluation method ensures transparency by providing a justification for its evaluation, reducing the reliance on human intervention while maintaining high reliability. By leveraging these techniques, the LLM-as-a-Judge framework offers a robust and scalable solution for evaluating structured outputs across diverse applications.

### 3.1 Search query parsing system

In this study, we evaluate a search query parsing system designed for an online classified advertisement platform. The parsing system plays a crucial role in understanding user queries and transforming them into a structured representation that enhances search accuracy and filtering capabilities. In this section, we describe briefly the query parsing system used in this work to understand the evaluation process clearly.

#### 3.1.1 Query types and user intent

The platform handles a diverse set of user search queries, ranging from simple keyword-based searches to more complex, multi-faceted queries that include specific filters and conditions. The queries typically fall into the following categories:

• Generic queries: broad search terms without specific filters (e.g., “cars for sale,” “rental apartments”).

• Feature-specific queries: queries that include attributes such as price range, brand, or room count (e.g., “red BMW under 500,000 TL,” “2 + 1 apartments for rent in Beşiktaş”).

• Location-based queries: queries that explicitly mention cities, districts, or neighborhoods (e.g., “houses for sale in Kadıköy,” “office space for rent in Levent”).

• Implicit intent queries: queries where certain attributes (e.g., price expectations such as “bargain price,” conditions like “urgent sale”) are implied rather than explicitly stated.

To ensure an optimal search experience, the search query parsing system must effectively interpret these queries, extract meaningful attributes, and represent them in a structured format.

#### 3.1.2 Structured output representation

The parsing system converts each query into a structured JSON output, ensuring that the search criteria in the query are properly categorized and formatted for the retrieval engine. All categories and filters used to extract structured output in this system are specific to the online classified platform domain. This structured output consists of the following key components:

• The search query parsing system classifies each query into a multi-level category hierarchy, ensuring that the search intent is accurately captured and aligned with the platform's structured taxonomy. At the highest level, category\_level\_1 represents the broad category, such as real estate. This is further refined into category\_level\_2, which indicates the general classification within the broader category, such as apartments or commercial properties. category\_level\_3 provides a more specific classification, identifying distinctions like for sale or for rent. In some cases, an additional level, category\_level\_4, is included for further refinements. Accurately determining the category of a query is essential, as it ensures that relevant filters and retrieval mechanisms are applied correctly, improving the precision of search results.

• The system also performs filter extraction, identifying both explicit and implicit filters within the query. Filters capture essential attributes that refine the search results and enhance user experience. These include numerical filters such as price ranges, mileage, and room counts (e.g., “houses under 5 million TL”); boolean filters which indicate conditions (e.g., “furnished” or “new”); and enumerated filters which define specific values such as brand names, fuel types, or transmission types. For reliable query interpretation, the extracted filters must be mapped accurately to the predefined system filters, ensuring structured and meaningful retrieval.

• The system also extracts location information, if present in the query. Location data is mapped to structured fields such as city (e.g., “Istanbul”) and district (e.g., “Kadıköy”). If the query lacks explicit location details, the system may infer relevant location attributes based on user behavior, default preferences, or additional context. Proper location extraction ensures that the results are relevant to the user's intent and geographical constraints.

• Keyword and synonym recognition plays a crucial role in enhancing search coverage and query understanding. The system identifies explicit keywords that appear in the user query, while also generating synonyms to improve search recall (e.g., “flat” for “apartment,” “auto” for “car”). However, if a keyword is already categorized under the category or filter fields, it is not duplicated as an explicit keyword to avoid redundancy. This structured approach to keyword and synonym recognition helps refine search accuracy while maintaining query clarity.

By converting unstructured natural language queries into structured data, the search query parsing system enhances the efficiency of the search engine. However, ensuring the accuracy of these parsed outputs requires a robust evaluation framework. This is where the LLM-as-a-Judge evaluation methodology is applied, assessing the correctness of structured outputs using various evaluation techniques described in the following section.

### 3.2 Evaluation methods

To systematically assess the quality of structured search query parsing outputs, we employ the LLM-as-a-Judge framework with three distinct evaluation methods: Pointwise, Pairwise, and Pass/Fail evaluation. Each of these methods leverages predefined evaluation criteria and structured rating rubrics to ensure consistency, transparency, and alignment with human assessments.

For all evaluation methods, we use the evaluation criteria outlined in which ensure that the key aspects—category accuracy, filter accuracy, location accuracy, keyword accuracy, synonym accuracy, and completeness—are systematically assessed. Furthermore, each evaluation prompt incorporates few-shot examples to provide the LLM with contextual understanding and enable it to generate well-grounded assessments.

The general evaluation pipeline is as follows:

1\. Query parsing: a user query is parsed into a structured JSON format as explained in Section 3.1.2.

2\. Evaluation prompt construction: an evaluation prompt is generated, incorporating the user query, the parsed output, the evaluation criteria, the rating rubrics, and few-shot examples.

3\. LLM-based assessment: the LLM-as-a-Judge evaluates the parsed output using the selected evaluation method. The LLM assigns a score (for Pointwise Evaluation), selects a preferred response (for Pairwise Evaluation), or classifies the response as pass/fail (for Pass/Fail Evaluation), accompanied by an explanation.

4\. Consistency: each evaluation is repeated multiple times with different runs. The average value for Pointwise Evaluation and the majority voting value for the other two evaluation methods is used to obtain reliable assessments.

#### 3.2.1 Use of few-shot examples in evaluation prompts

To enhance the reliability and reasoning capabilities of the LLM-as-a-Judge framework, we iteratively constructed and incorporated few-shot examples into the evaluation prompts. These few-shot examples are entirely independent of the validation dataset and were manually crafted to reflect a diverse range of user queries and parsing scenarios.

Each few-shot example consists of a user query, a corresponding structured output (either fully correct, partially correct, or incorrect), a detailed evaluation of that output based on the established evaluation criteria, and a final judgment (score, preference, or pass/fail decision) with justification. This structure provides the LLM with contextual grounding and helps calibrate its evaluation behavior across diverse parsing outcomes.

Experiments were conducted using both zero-shot and few-shot versions of the evaluation prompts. Initially, evaluation was performed using zero-shot prompts to identify common failure patterns. These insights were then used to iteratively design targeted few-shot examples that address specific weaknesses observed in the model's judgments. This adaptive refinement continued across multiple iterations, with new few-shot cases added in response to the evaluator errors, particularly focusing on challenging or ambiguous cases. Separate sets of few-shot examples were maintained and updated for each evaluation method (Pointwise, Pairwise, and Pass/Fail), ensuring that the prompting remained method-specific and aligned with the underlying rating rubrics.

The number of few-shot examples varied by evaluation type and category but generally started with around five examples per prompt. As iterations progressed and the evaluator's weaknesses became better understood, the number of few-shot examples increased, culminating in ~30 examples in the final prompt configurations. This iterative augmentation process significantly improved evaluator consistency and performance, as evidenced by the quantitative results reported in Section 4.4.

#### 3.2.2 Pointwise evaluation

Pointwise evaluation assesses the parsed query outputs by assigning a numerical score based on the predefined evaluation criteria and rating rubrics. The rating rubric we used for this method is shown in . The LLM evaluates the correctness of the parsed query with respect to the user query, assigns a score on a Likert scale (0–4), and also provides a textual justification for its rating. A running example of the pointwise evaluation process is illustrated in . An example evaluation prompt used in the pointwise evaluation can be found in [Supplementary material](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#h13).

#### 3.2.3 Pairwise evaluation

Pairwise evaluation compares two different parsed outputs for the same query, enabling a direct comparison between different search query parsing models. This method may be particularly useful for assessing performance improvements between traditional rule-based systems and LLM-based systems. The LLM determines which output better meets the evaluation criteria or declares them equivalent if both are equally valid or unsatisfactory. The rating rubric used for pairwise evaluation is given in . shows an example that compares the outputs of two parsing systems for the same query. An example evaluation prompt used in pairwise evaluation can be found in [Supplementary material](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#h13).

#### 3.2.4 Pass/fail evaluation

The Pass/Fail evaluation simplifies the assessment by converting the evaluation process into a binary classification task. Instead of assigning scores or making comparative judgments, the LLM assesses whether the parsed output meets the evaluation criteria and classifies it as either “PASS” or “FAIL.” The rating rubric is given in . presents a sample Pass/Fail evaluation scenario. An example evaluation prompt used in Pass/Fail evaluation can be found in [Supplementary material](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#h13).

### 3.3 Contextual evaluation prompt routing

We propose a method called Contextual Evaluation Prompt Routing to improve both the reliability and efficiency of LLM-based evaluation in structured output tasks. This approach dynamically routes evaluation prompts based on the category of the user query, enabling the use of tailored evaluation criteria, category-specific rating rubrics, and customized few-shot examples aligned with domain-specific parsing expectations.

Prior to this approach, we used a single unified evaluation prompt for all query categories as detailed in Section 3.2. The prompt included a comprehensive set of evaluation rubrics, criteria, and few-shot examples covering all categories. However, experimental analysis revealed that this one-size-fits-all design introduces several key limitations:

• First, criteria that are important in one domain (e.g., Location Accuracy in real estate category) are not that much important in other domains, leading the LLM evaluator to misinterpret irrelevant or inapplicable instructions.

• Second, the inclusion of few-shot examples from unrelated domains increases hallucination risk, as the model might align the evaluation with incorrect reference structures.

• Third, as we expand the number of few-shot examples to improve performance, the token length of the prompts exceeds practical limits (up to 100k tokens), resulting in degraded performance and higher computational cost.

To mitigate these issues, the Contextual Evaluation Prompt Routing strategy segments the evaluation process into two stages. First, the structured output's category\_level\_1 value is used to determine the main category of the query. Then, a category-specific evaluation prompt is constructed with

• Only the relevant evaluation criteria and rating rubric,

• Tailored few-shot examples that reflect the annotation standards of that specific category, and

• A more compact and focused prompt length, improving LLM interpretability.

This strategy offers several advantages. By eliminating irrelevant instructions and examples, it reduces hallucinations and improves evaluation accuracy through domain-specific guidance. The modular nature of the prompts also significantly lowers the inference time and computational costs due to shorter input lengths. Moreover, isolating category-specific configurations allows for the inclusion of a larger number of relevant few-shot examples, further enhancing the evaluation performance. The overview of the routing mechanism is depicted in , and a sample routed prompt is provided in [Supplementary material](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#h13).

The proposed method is conceptually inspired by advances in task decomposition and prompt specialization. For instance, Multi-Trait Specialization (MTS) ( [Lee et al., 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B10)) applies trait-specific prompts to improve zero-shot performance in essay scoring. While MTS addresses unstructured generation tasks, our Contextual Evaluation Prompt Routing strategy adapts the underlying principles to the structured output domain of semantic search query parsing. [Khot et al. (2023)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B8) introduce decomposed prompting that modularizes complex tasks into simpler, interpretable components. [Dun et al. (2025)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B5) propose the Mixture of Prompts (MoPs) framework, which dynamically selects specialized prompt modules based on input characteristics, improving adaptability across heterogeneous tasks. Building on these insights, our routing method offers a scalable, interpretable, and efficient alternative to monolithic prompts for evaluation in multi-domain structured output settings.

While related to prior prompt specialization approaches, the proposed method is uniquely designed for structured evaluation scenarios that require strict rubric alignment, interpretability, and category consistency. Thus, Contextual Evaluation Prompt Routing is not just a heuristic routing solution, it also serves as a foundational mechanism for scalable and reliable deployment of LLM-as-a-Judge systems in real-world, multi-domain search applications.

To validate its effectiveness, we constructed category-specific evaluation subsets, each annotated by domain experts. These controlled benchmarks revealed that category-specialized routing improves both alignment with human judgments and consistency across repeated assessments. Importantly, the strategy generalizes well to unseen inputs without requiring model fine-tuning, supporting its modularity and adaptability to diverse semantic parsing domains. Furthermore, we applied a range of statistical methods, including agreement metrics and error analysis, to quantify the reliability and stability of our evaluation framework. The results indicate that using category-specialized prompts not only improves alignment with human assessments but also enhances evaluation robustness without introducing the cost overhead associated with full-scale model fine-tuning.

Through the methodology explained in Sections 3.2 and 3.3, the proposed LLM-as-a-Judge framework offers a modular, scalable, and semantically accurate evaluation solution for structured search query parsing. By integrating multiple evaluation strategies and enhancing them with domain-aware prompt routing, our approach achieves high interpretability and consistency while significantly reducing the need for human evaluation in critical systems.

## 4 Experiments and results

In this section, we present the datasets, the evaluation metrics, and the experimental setup used for assessing the effectiveness of the LLM-as-a-Judge framework in evaluating search query parsing systems. Our goal is to systematically compare different evaluation methods (Pointwise, Pairwise, and Pass/Fail) and evaluation techniques (in-context learning, prompt engineering with iterative refinement, human-in-the-loop evaluation, etc.) and validate their reliability in capturing the accuracy and completeness of structured query parsing outputs. In addition, we investigate the impact of the Contextual Evaluation Prompt Routing strategy on the consistency and efficiency of the evaluation. The results are presented accompanied with ablation studies. We also conduct an error analysis and discuss the limitations of the proposed approach.

### 4.1 Datasets

In this work, we compiled two datasets and conducted the experiments on these datasets.

#### 4.1.1 Small-scale evaluation dataset

The first dataset consists of 66 queries covering various search scenarios. These queries were manually created by domain experts and designed to represent different category levels, filtering attributes, and query complexities commonly encountered in search systems. Each query was processed by two different search query parsers:

• Rule-based parser: a traditional query parsing system that relies on predefined rules and heuristics to extract structured information.

• LLM-assisted parser: a more flexible, context-based parser that leverages a large language model to interpret and generate structured query representations.

For each query, the structured outputs generated by both parsers are manually evaluated and labeled by a human annotator with domain knowledge and background in computer science. The annotator assigns scores to the search query parser outputs for Pointwise evaluations, makes pass/fail decisions for Pass/Fail evaluations, and determines which of the two parsing outputs better captures the search intent for Pairwise evaluations. To address the known position bias issues in Pairwise evaluation, in half of the cases the first parser output and in the other half of the cases the second parser output are presented first to the LLM evaluator. The annotations are then reviewed by five domain experts who provide feedback and additional notes to ensure accuracy and consistency. Based on this expert feedback, the annotator revisits and refines the labels, ensuring that the final annotations align with domain-specific expectations and serve as reliable ground-truth references.

#### 4.1.2 Large-scale evaluation dataset

To further analyze the performance of the LLM-as-a-Judge framework at scale, we constructed a more extensive dataset consisting of 600 queries spanning multiple domain-specific categories. These queries were selected according to search frequency after removing duplicate and highly similar queries among the most frequently searched queries on the online classified platform. These categories align with the main categories used in the routing strategy and include “Real Estate,” “Vehicles,” “Used & Brand New Items,” “Vehicle Parts, Accessories & Tuning,” “Other Categories,” and “No Category” (Uncategorized Queries) categories.

One hundred queries were collected for each category, ensuring a balanced representation of search intents and parsing challenges. Given the high annotation cost of the large-scale dataset and based on the experimental findings in the small-scale dataset that show that Pass/Fail evaluation yields more consistent results, the large-scale dataset was only annotated for the outputs of the LLM-based parser for Pass/Fail evaluation. The annotation process followed a similar labeling procedure as the small-scale dataset. However, to accelerate the manual annotation process, a preliminary annotation was first conducted using the best-performing techniques identified in the small-scale dataset. The outputs were then manually reviewed and refined by human annotators to ensure high-quality ground truth labels.

This larger dataset enabled a more comprehensive assessment of the Contextual Evaluation Prompt Routing strategy, allowing us to evaluate how well domain-specific prompts improve the accuracy and reliability of search query parsing evaluations across different query characteristics, such as query length, complexity, and category-specific constraints.

### 4.2 Evaluation metrics

To assess the effectiveness of the LLM-as-a-Judge framework, we employed a range of evaluation metrics that measure the alignment between LLM-based evaluations and human judgments. We selected a number of proper metrics for each evaluation method. The metrics were used to quantify both the agreement with human evaluations and the reliability of the LLM-based assessment process.

#### 4.2.1 Agreement metrics

We utilized different agreement metrics depending on the evaluation methodology.

##### 4.2.1.1 Pointwise evaluation

Since Pointwise evaluation involves assigning numerical scores to structured query parsing outputs, we used correlation metrics below to measure the alignment between LLM-generated scores and human ratings:

• _Spearman's rank correlation (_ ρ _)_ was used to assess the monotonic relationship between the rankings of human and LLM evaluations. This metric evaluates whether higher scores assigned by humans correspond to higher scores assigned by the LLM.

• _Standard deviation across runs_ reflects the average variability of scores assigned by the LLM across evaluation runs per query, indicating the consistency of the LLM-as-a-Judge system for a given setup.

##### 4.2.1.2 Pairwise and pass/fail evaluation

Since these evaluation methods involve categorical decisions rather than numerical scores, we used classification-based agreement metrics:

• _Exact match accuracy_ was used to measure the percentage of instances where the LLM's decision matched the human annotated label. This metric is a simple but effective way to calculate the agreement of categorical evaluations.

• _Cohen's Kappa (_ κ _)_ was utilized to account for agreement beyond chance, measuring the level of consistency between human and LLM evaluations while considering the possibility of random agreement. This metric is particularly useful for categorical classification.

#### 4.2.2 Reliability metrics

In addition to aligning with human annotations, we assessed the internal reliability of the LLM evaluator using statistical measures that quantify the consistency of its evaluations across different subsets. Unlike conventional inter-rater agreement metrics, which evaluate the consensus among different raters, our approach measures the variability of LLM judgments using standard deviation, coefficient of variation, and mean absolute deviation. These metrics provide a robust assessment of how consistently the LLM applies its evaluation criteria across diverse query distributions.

The standard deviation (SD) measures how much the agreement scores deviate from their mean. A lower standard deviation indicates that the evaluations are consistent and stable, while a higher value suggests fluctuations in agreement scores, pointing to inconsistencies in LLM assessments. This metric is useful for understanding the overall dispersion of scores across different evaluation runs.

The coefficient of variation (CV) normalizes the standard deviation by expressing it as a percentage of the mean, making it useful for comparing variability across different datasets. A lower CV percentage suggests more stable evaluations, while a higher percentage indicates greater variability. Since CV accounts for differences in scale, it helps in making meaningful comparisons between categories with varying levels of agreement scores.

The mean absolute deviation (MAD) measures the average absolute difference between the agreement scores and their mean. Unlike standard deviation, MAD is less sensitive to extreme outliers, making it a robust alternative for measuring variability. A lower MAD value suggests that evaluations remain closely distributed around the mean, while a higher value indicates larger fluctuations and potential inconsistency in LLM-based judgments.

This combination of agreement and reliability metrics provides a comprehensive assessment of the LLM-as-a-Judge framework, ensuring that the evaluation process is both aligned with human judgments and reliable.

### 4.3 Experimental setup

In the experiments, we evaluated the LLM-as-a-Judge framework using a range of Gemini models: gemini-1.5-flash-001, gemini-1.5-flash-002, gemini-1.5-pro-001, and gemini-1.5-pro-002. The flash models are optimized for efficiency, being smaller and faster than the pro models. Specifically, gemini-1.5-flash-002 represents an update over 001. We initially began with Pointwise evaluation, which is relatively more complex than the other evaluation methods. For this task, we primarily employed the pro models due to their higher capacity, and ran each prompt setup multiple times to ensure the stability of the results. Given the high computational cost of the pro models, we continued with the more cost-efficient flash models in the later stages. Additionally, as new Gemini models were released during the study, we updated the models used in our experiments accordingly. As a result, we used the most suitable models in different stages of the experiments based on the complexity of the evaluation and the cost considerations. By comparing these models, we aimed to understand the impact of model size, optimization strategies, and generational advancements on the framework's performance.

We configure the temperature and seed parameters during inference to ensure controlled and reproducible evaluations. The temperature is set to 0.7, allowing for a balanced degree of randomness in token selection while maintaining response consistency. The seed parameter is specified to enforce deterministic outputs. However, due to the probabilistic nature of LLMs, setting a fixed seed does not entirely eliminate the variance in responses across multiple runs.

Although LLM evaluation is inherently a deterministic task, variability in token selection may lead to slight inconsistencies in the generated evaluations. We perform multiple evaluation iterations for each experimental setup to mitigate this issue. By running multiple iterations, we ensure the stability of LLM evaluations and reduce the impact of randomness on the assessment metrics. This iterative approach helps quantify the robustness of the LLM evaluators across different evaluation methodologies.

### 4.4 Results

This section presents the results of the experiments for the LLM evaluation of search query parsing outputs. We analyze the impact of various evaluation methods, prompt designs, evaluator models, and reference values on alignment with human judgments and evaluation consistency.

As stated in Section 4.1, the queries in the small-scale dataset were parsed by both the rule-based parser and the LLM-based parser, and the results of both parsers were manually annotated. We thus evaluate the outputs of both parsers using the LLM-as-a-Judge framework for the small-scale dataset and compute the agreement scores with the human labels. For Pointwise and Pass/Fail evaluations the parsed outputs of the two parsers are assessed separately, while for Pairwise evaluation the two parsers are compared in the same experiment. Since the Contextual Evaluation Prompt Routing strategy was tested across all three evaluation methodologies (Pointwise, Pairwise, and Pass/Fail), the experiments leveraging this strategy were conducted using the small-scale validation dataset where both parsers' outputs were annotated. Due to the annotation cost, the large-scale dataset was only used to evaluate the effectiveness of the strategy in the Pass/Fail setting, where only the LLM-based parser's outputs were labeled.

#### 4.4.1 Pointwise evaluation results

, show the evaluation results of the parsed queries for the two parsers. In all the tables in this section, we include the results only for the gemini-1.5-flash-002 and gemini-1.5-pro-002 models which are newer versions of the flash and pro models in order not to clutter the tables. The complete results for all the models and configurations are provided in [Supplementary material](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#h13). The LLM evaluation for each query and setting is repeated 10 times and averaged to increase the reliability of the scores. The Spearman's correlation column is the correlation between the human scores and the LLM scores (averaged). In addition to Spearman's correlation, Pearson and Kendall's Tau correlation metrics were also computed. However, as their results were consistent with the Spearman correlation values and did not provide additional insights, we do not include them in the tables. shows the interpretation of the Spearman's correlation values. The standard deviation column is the standard deviation of the 10 runs. Having multiple runs helps account for the variability in the LLM outputs, ensuring that our evaluation captures consistency across different test cases.

_Basic prompt_ denotes the prompt in its basic form and is shown in [Supplementary material](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#h13). _Few-shot_ shows the effect of including query examples in the prompt (Section 3.2.1) to guide the LLM evaluation. While evaluating a parser output, the LLM gives a score which is followed by an explanation. _Explain first_ shows the results when the LLM is guided to explain the score before presenting the score, which was observed to increase the evaluation performance in some works. _Separate system prompt_ refers to a prompt design in which the search query parser's original system prompt and the user query are presented in separate sections, rather than being concatenated and given as a single input. This aims to make the evaluation criteria clearer by structurally distinguishing between system behavior and user input. In order to apply the separate system prompt, the user query should be removed from the Search Query Parser Prompt section in the evaluation prompt and written under a separate heading. _Reference values_ indicates whether the gold (human-annotated) reference parsing output is provided within the evaluation prompt. When reference values are included, the LLM-as-a-Judge can see what the correct structured output should look like, allowing it to make more informed and accurate evaluations.

It is important to note that there is a significant score gap between the evaluation of the rule-based and LLM-based parser outputs. This discrepancy primarily stems from the nature of the rule-based parser, which either parses a query very well or very poorly due to extensive manual mappings and highly domain-specific rules. As a result, the LLM evaluator often assigns either the highest or lowest score, which simplifies its decision-making and leads to higher agreement with human ratings. In contrast, the LLM-based parser tends to produce more nuanced outputs with partial correctness. In these borderline cases, the LLM evaluator may either overlook minor errors and assign a high score or interpret them as critical issues and give a low score, both of which hinder alignment with human judgment.

##### 4.4.1.1 Impact of adding few-shot examples

, reveal different impacts of few-shot prompting across the two types of parser. For the LLM-based parser, adding few-shot examples does not improve alignment with human scores; in fact, a slight drop is observed. For example, in gemini-1.5-flash-002, Spearman's correlation decreases from 0.381 to 0.364, and in gemini-1.5-pro-002 from 0.490 to 0.445. This decline can be attributed to the fact that the LLM-based parser already produces semantically nuanced outputs. Introducing few-shot examples may have led the LLM evaluator to overfit to specific reference patterns in the prompt, resulting in misalignment for more ambiguous or borderline cases.

In contrast, for the rule-based parser, few-shot prompting yields substantial improvements. Correlation increases from 0.564 to 0.793 in gemini-1.5-flash-002 and from 0.677 to 0.853 in gemini-1.5-pro-002, representing a clear boost in evaluation accuracy. This effect is likely due to the more rigid and deterministic nature of rule-based outputs, which align better with the explicit decision templates presented in few-shot examples. The examples provide clear guidance that helps the LLM evaluator assess structured, rule-derived outputs more effectively.

##### 4.4.1.2 Impact of contextual evaluation prompt routing

The addition of Contextual Evaluation Prompt Routing yields different effects depending on the parser type. For the LLM-based parser, routing alone results in a modest improvement or similar performance over the basic prompt (0.402 and 0.481 Spearman correlation for flash-002 and pro-002, respectively). When combined with category-specific few-shot examples, the alignment further improves to 0.664 and 0.671 for the two models, respectively. This reflects a transition from moderate to strong correlation ( ), suggesting that contextual prompt routing helps the LLM evaluator better understand structured outputs through more targeted domain-specific guidance.

For the rule-based parser, however, the effect is more nuanced. In the flash-002 model, routing alone or with few-shot examples does not improve performance and in fact leads to a decline (0.371 and 0.309 vs. 0.564 with the basic prompt). This may be due to the simpler and highly rigid outputs of the rule-based system, which align better with generic evaluation instructions rather than segmented category-specific ones. However, in the pro-002 model, prompt routing continues to be beneficial, achieving 0.802 correlation without few-shot and 0.815 with category-specific few-shot examples, both signaling improvement over the basic prompt (0.677). These results suggest that routing is more effective when combined with stronger evaluator models that can make use of nuanced prompt variations.

Overall, the findings indicate that Contextual Evaluation Prompt Routing, especially when paired with few-shot examples, is a promising approach for increasingrere alignment in LLM-based evaluations, particularly for LLM-based parser outputs.

##### 4.4.1.3 Impact of evaluator model

The choice of the evaluator model significantly affects the reliability and quality of LLM-based evaluations. Across our experiments, we observed that different sizes of the Gemini family models (flash-002 and pro-002) demonstrate varying levels of correlation with human judgments and stability across runs, even under identical prompting conditions.

Interestingly, the smaller model gemini-1.5-flash-002 achieves the highest Spearman correlation among all configurations for LLM-based parser outputs when reference values are provided (0.898), outperforming the larger pro-002 model (0.858). Similarly, in the rule-based parser evaluation, flash-002 reaches a peak correlation of 0.870, slightly higher than pro-002 (0.832). These results suggest that smaller models can be more effective than larger ones in alignment with human ratings when given strong reference cues.

However, flash-002 also shows more pronounced variability across different prompting strategies. For example, in the LLM-based parser, Spearman correlation drops to 0.350 with the Explain First prompt, compared to 0.565 with Separate System Prompt, indicating greater sensitivity to prompt format. On the other hand, pro-002 tends to offer more stable performance across configurations, with smaller fluctuations in correlation values between prompt types.

Standard deviation results further support this observation. Under basic prompt conditions, pro-002 exhibits low variability (0.061 and 0.062 for LLM-based and rule-based parsers), whereas flash-002 shows very low variability only in its simplest configurations (0.023) but higher variance in others (e.g., 0.184 in Explain First). This implies that while both models can reach strong alignment with humans under optimal prompting, the pro-002 model tends to produce more consistent evaluations across prompt types.

One notable and consistent observation is that individual evaluator models behave similarly when scoring both the LLM-based and rule-based parser outputs. That is, if a model performs well in evaluating the rule-based system, it tends to also perform well in the LLM-based system, under the same prompt configuration. This suggests that model behavior is influenced more by the evaluator's internal alignment mechanisms than by the type of the parser being evaluated.

Prompt length is another critical factor. Adding more few-shot examples or reference values generally increases prompt complexity, which can in turn lead to higher output variance. For instance, standard deviation reaches 0.464 with few-shot prompts in pro-002 (LLM-based parser), suggesting that model outputs become less stable when overwhelmed with too much contextual information.

Notably, prompt routing appears effective in reducing this variance. In the LLM-based parser evaluations, using prompt routing combined with few-shot examples yields standard deviations of 0.081 (flash-002) and 0.151 (pro-002), substantially lower than in their respective monolithic few-shot setups. These findings validate our hypothesis that modular, category-specific routing mitigates prompt overload and improves evaluation stability, especially when tailored few-shot examples are supplied for each domain.

Overall, these results highlight that while larger models like pro-002 may offer more predictable performance across settings, smaller models like flash-002 can deliver superior alignment when supported by strong reference guidance. Ultimately, careful balancing of model size, prompt strategy, and task-specific routing is key to achieving both accurate and consistent LLM-as-a-Judge evaluations.

##### 4.4.1.4 Impact of reference values

Providing reference values within the prompt mostly enhances alignment with human evaluations. In the LLM-assisted parser evaluations, the correlation improved from 0.445 to 0.858, moving from a strong relationship to a very strong relationship ( ), highlighting the importance of reference values in guiding the evaluation. Additionally, standard deviation values decreased from 0.464 to 0.209, reinforcing that reference values contribute to more stable evaluations.

##### 4.4.1.5 Impact of scoring first vs. explaining first

When the LLM is requested to provide a justification for the score before giving the score, the correlation with the human score increases. shows that correlation increases from 0.445 to 0.461 for the stronger gemini-1.5-pro-002 model. The increase in correlation suggests that allowing the LLM to rationalize its decisions before scoring leads to more thoughtful and accurate evaluations. However, the variability in the evaluation runs does not follow a particular pattern.

After observing that the explain-first strategy yielded consistently better results than the score-first prompting for the LLM-based parser, all subsequent evaluations in this study were conducted using the explain-first strategy.

##### 4.4.1.6 Impact of providing system prompt separately

We observe that separating the system prompt from the user query, i.e. making the evaluation criteria distinct from the user input, results in lower Spearman correlation scores compared to other setups but yields more stable evaluations. This suggests that integrating the system prompt with the evaluation prompt provides additional context that aids assessment and keeping them separate improves consistency across multiple runs.

In particular, for rule-based parser outputs evaluated with gemini-1.5-pro-002, using the separated system prompt along with few-shot examples yielded a Spearman correlation of 0.711. This is lower than other configurations except the basic prompt, indicating that structurally separating prompt sections negatively impacts accurate evaluations.

#### 4.4.2 Pairwise evaluation results

shows the evaluation results for Pairwise evaluation where we compare the outputs of the two parsers. As stated in Section 4.1.1, the dataset is randomly shuffled such that the output of the rule-based parser appears in the first position in half of the examples and the output of the LLM-based parser appears in the first position in the other half. The LLM evaluation for each query and setting is repeated 5 times and majority voting is applied. In _Few-Shot (Initial)_, we include 3 examples in the prompt. After the initial experiment with few-shot examples, we iteratively refine the prompt by analyzing the decisions of the LLM and adding new examples to the prompt according to the results of the analysis (Section 3.2.1). _Few-Shot (Final)_ denotes the final form of the prompt in which 24 examples are used. We used the exact match and Cohen's Kappa to measure the alignment between human evaluations and LLM evaluations. Full evaluation results including experiments with gemini-1.5-pro-001 and gemini-1.5-flash-001 are provided in [Supplementary material](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#h13) for completeness and reference.

##### 4.4.2.1 Impact of few-shot prompting

shows that, for the gemini-1.5-flash-002 model, using the basic prompt yields an exact match accuracy of 0.773 and a Cohen's Kappa of 0.635. While these results seem reasonable, they indicate room for improvement for the LLM evaluator in capturing nuanced differences between the system outputs. When a large number of examples is included in the prompt, the exact match accuracy is increased to 0.879 and the Cohen's Kappa to 0.807, demonstrating the effectiveness of few-shot learning in refining LLM-based evaluation. When switching from the gemini-1.5-flash-002 model to the more advanced gemini-1.5-pro-002 model using the same refined prompt, Cohen's Kappa increased slightly from 0.807 to 0.816, suggesting better agreement between the human and the LLM compared to random agreement.

These results confirm that adding more diverse few-shot examples enhances the evaluation accuracy, allowing the model to better differentiate between subtle variations in query parsing performance.

##### 4.4.2.2 Impact of contextual evaluation prompt routing

In addition to standard few-shot prompting, we evaluated the impact of Contextual Evaluation Prompt Routing in the pairwise setting. This strategy routes evaluation prompts based on the category of the search query to reduce prompt length and improve semantic relevance (see Section 3.3).

As shown in , prompt routing without few-shot examples results in lower performance than the basic prompt in both flash-002 and pro-002 models. For instance, exact match accuracy drops from 0.773 to 0.697 in flash-002, and Cohen's Kappa decreases from 0.635 to 0.508. This suggests that routing alone, without adequate in-context examples, may reduce the LLM's ability to generalize comparisons across domains.

However, when routing is combined with even a small number of few-shot examples \[prompt routing + few shot (initial)\], performance may improve substantially. For example, in pro-002, exact match accuracy increases to 0.803 and Cohen's Kappa to 0.687, outperforming the basic prompt setup. This confirms that routing and few-shot prompting are complementary in the sense that routing helps delivering category-relevant context while examples help guiding fine-grained decision boundaries in the pairwise comparison task.

These findings align with earlier trends observed in pointwise evaluations; routing by itself reduces prompt cluttering and improves stability, but gains are best realized when domain-specific few-shot guidance is also provided.

##### 4.4.2.3 Impact of position bias

Position bias is a well-known issue in pairwise evaluation, where models tend to favor responses in a particular position (first position or second position). To analyze the effect of position bias, we conducted an additional experiment using an unshuffled dataset. The output of one of the parsers always appears in the first position and the LLM is asked to select the better one among the two outputs. We used the gemini-1.5-flash-002 model and the refined prompt with large number of few-shot examples. shows the results. Compared to the original setting where the order of the pairs are shuffled, the exact match accuracy decreased from 0.879 to 0.833 and Cohen's Kappa dropped from 0.807 to 0.639.

This significant drop in inter-rater agreement highlights the importance of randomizing the response order in pairwise evaluation setups to prevent systematic biases. Without shuffling, the model may develop an unintended preference for responses in a specific position, leading to skewed evaluation results.

#### 4.4.3 Pass/fail evaluation results

, show the evaluation results for Pass/Fail evaluation for the outputs of the two parsers. The LLM evaluation for each query and setting is repeated 5 times and majority voting is applied. Similar to Pointwise evaluation, we started with a basic prompt without few shot examples and then used 15 examples in the initial few-shot setting. By analyzing the evaluations of the LLM, we refined the prompt to include more examples and used 30 examples in the final few-shot setting (Section 3.2.1). Full evaluation results including experiments with gemini-1.5-pro-001 and gemini-1.5-flash-001 are provided in [Supplementary material](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#h13) for completeness and reference.

##### 4.4.3.1 Impact of few-shot prompting

, show that using a basic prompt without few-shot examples yields low agreement with human labels. When few-shot examples are included in the prompt, the agreement scores increase significantly for both parsers. Refining the prompt and adding more targeted examples further improves alignment with human decisions. We also tested whether increasing the number of examples beyond 30 leads to higher scores, but observed that prompt length issues began to reduce effectiveness. This aligns with prior findings indicating that overly long prompts may introduce confusion and hallucination in LLM-based evaluators ( [Zhang et al., 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B20)).

##### 4.4.3.2 Impact of fine-tuning the LLM evaluator

To address the prompt length and inference overhead challenges in few-shot prompting setups, we explored fine-tuning as an alternative strategy for enhancing the reliability of LLM-based evaluations in an additional experiment. Instead of incorporating few-shot examples directly into the prompt which may lead to prompt length constraints, we constructed a supervised dataset containing 57 manually curated examples, aggregated from the few-shot samples used in earlier prompting experiments. These examples span a range of query parsing outputs across multiple categories and were used to fine-tune the gemini-1.5-flash-002 model.

Although the fine-tuned models achieved improvements over the basic prompt setting by raising the exact match accuracy from 0.742 to 0.794 for the LLM-based parser and from 0.485 to 0.755 for the rule-based parser, they could not outperform the few-shot prompting configuration. , show that the final few-shot prompt setup achieved Exact Match Accuracy scores of 0.848 for the LLM-based parser and 0.803 for the rule-based parser in the gemini-1.5-flash-002 model, surpassing the fine-tuned model performance. This indicates that while fine-tuning provides a stable baseline improvement over naive prompting, few-shot prompting remains a more effective method, especially when sufficient in-context examples can be supplied.

To further explore this, we conducted additional experiments by combining the fine-tuned models with 30 new few-shot examples (excluded from the fine-tuning set) during evaluation. This hybrid approach offered marginal improvements, suggesting that prompt-based guidance can still help the fine-tuned models contextualize and refine their judgments. However, the overall findings reinforce that direct few-shot prompting outperforms fine-tuning in terms of evaluation accuracy, especially when computational resources allow for longer prompt lengths.

##### 4.4.3.3 Impact of contextual evaluation prompt routing

Given that few-shot prompting gives rise to long prompts and fine-tuning requires training large models on task-specific data, we experimented also with prompt routing which is a more scalable approach. shows that even without few-shot examples, routing the prompts based on context improved the exact match accuracy from 0.742 to 0.894 for the LLM-based parser and from 0.485 to 0.909 for the rule-based parser for gemini-1.5-flash-002. When few-shot examples are included in the prompt, the accuracy further improved to 0.939 for both LLM-based parser and rule-based parser. This confirms that prompt routing is a highly effective approach for structured query parsing evaluation, even when applied to traditional rule-based parsing outputs.

These results suggest that prompt routing helps maintain prompt clarity while avoiding hallucination issues associated with long few-shot prompts.

##### 4.4.3.4 Scaling prompt routing to a larger dataset

Since Contextual Evaluation Prompt Routing yielded promising results, we evaluated its performance on a larger dataset that covers multiple search query categories. Up to this point, all the experiments had been conducted on the small-scale dataset consisting of 66 manually crafted queries. This small dataset was used to observe the effect of iterative improvements of the prompt on a controlled set of complex, long-form queries containing explicit filters and implicit keywords. By focusing on a small but diverse dataset, we were able to systematically determine the most effective evaluation approach for the problem. However, given the limited sample size, we need to validate the findings on a larger and more representative test set, ensuring the method's robustness across real-world search queries.

presents the results on the large-scale dataset which consists of six categories with 100 queries in each category. The column labeled “Initial Few-Shot Prompt” gives the results using the refined prompt obtained in the small-scale dataset experiments. These results show how well the prompt optimized for a smaller manually curated dataset generalizes to a broader set of search queries.

The small-scale dataset contains long and complex queries designed to test the system's ability to extract structured attributes effectively. However, the larger dataset was constructed from the most frequently searched queries on the online classified ads platform and thus the queries are mostly shorter and more ambiguous, creating a slight distributional shift between the two datasets. Due to this shift, evaluations on the large dataset using the original prompt revealed discrepancies in performance, highlighting the need for further refinements.

To address this, the prompt routing strategy was adjusted to better align with the characteristics of the larger dataset. The column labeled “Improved Few-Shot Prompt” represents the results obtained after modifying the prompts to accommodate for shorter and more ambiguous queries. These adjustments involved refining the category-specific few-shot examples and optimizing the evaluation instructions to account for real-world search behavior.

The largest performance improvement was observed in the _Vehicle Parts, Accessories & Tuning_ category, where the accuracy increased from 0.40 to 0.94. Similarly, _Real Estate_ queries saw a notable improvement from 0.66 to 0.91, indicating that category-specific prompt refinements significantly enhance the evaluation quality. However, _No Category_ queries remained the most challenging with accuracy peaking at 0.87. This suggests that implicit category assignments are inherently harder to evaluate, as they rely more heavily on contextual inference rather than explicit query signals.

Overall, these findings confirm that prompt routing, particularly when combined with category-specific few-shot examples, provides a robust and scalable evaluation approach. The ability to adapt the prompts to different query distributions ensures that the LLM-as-a-Judge framework remains effective across diverse search environments.

##### 4.4.3.5 Reliability measuring

We conducted an experiment on the large-scale dataset to assess the reliability of the LLM-as-a-Judge system. For each category, we randomly selected five different subsets, each containing 20 samples. Agreement metrics were calculated across these subsets to capture the variability in LLM evaluations. Using these agreement scores, we computed the standard deviation (SD), coefficient of variation (CV), and mean absolute deviation (MAD) metrics.

presents the variability in the LLM-based agreement scores across different categories. Lower values indicate more consistent evaluations across the subsets, while higher values suggest greater variability.

The results reveal that the _Real Estate_ and _No Category_ categories exhibit the lowest variability, implying that LLM evaluations in these domains are relatively stable. This is likely due to well-structured queries in the real estate sector and limited complexity in non-categoric queries, queries without any category assignment, such as “urgent.” In such queries, it is usually sufficient to extract only the explicit keyword, which simplifies the problem. Conversely, the _Other Categories_ category demonstrates the highest variability, indicating significant inconsistencies in LLM evaluations across the subsets. This can be expected as the category aggregates diverse and sparsely represented queries, making structured evaluation more challenging.

### 4.5 Comparisons with related works

In the proposed approach, a search query is parsed into a structured form (search query parser output) that is used to retrieve the search results from a database. The quality of the structured output cannot be evaluated by executing it and counting the number of returned items, as a large set of results does not necessarily signal relevancy. For instance, omitting parsing altogether and performing a simple keyword search may yield a broad set of results, but many of them would not reflect the user's actual intent. In such a setup, the only reliable way to assess the quality of a parsed output is through human evaluation, examining whether the structured output accurately represents the user's semantic intent. However, manual evaluation of thousands of structured outputs is prohibitively time-consuming and costly. Therefore, we adopt the LLM-as-a-Judge framework as an efficient and semantically robust alternative. In assessing the performance of the proposed evaluation framework, we use correlation with human judgments as the evaluation metric. Traditional automated metrics (e.g., BLEU) or heuristic-based baselines are not directly applicable in our setting due to the nature of the search pipeline and the sparsity of ground truth labels at scale.

While our primary comparison is against expert human annotation on a small-scale validation set, we acknowledge the need to contextualize our results within the broader literature. Several recent studies have validated the effectiveness of LLM-based evaluation methods against human preferences and established their superiority over traditional baselines:

• [Raju et al. (2024)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B16) introduce a domain-specific benchmark to evaluate LLMs as judges, achieving a Spearman correlation of 0.915 with human judgments, substantially outperforming existing baselines such as AlpacaEval 2.0 LC (0.297). Their study also reports 84% agreement with Chatbot Arena results, demonstrating that well-designed evaluation prompts tailored to the task domain can lead to highly reliable assessments.

• TALEC ( [Zhang et al., 2024](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B20)) proposes a framework for training LLM evaluators with task-specific criteria, reporting Spearman correlations of 0.96–0.97 for tasks such as sentiment analysis and title generation. The study also highlights that average correlation with human judgment exceeds 0.80, often surpassing inter-human agreement in subjective tasks.

• [Zheng et al. (2023)](https://www.frontiersin.org/journals/big-data/articles/10.3389/fdata.2025.1611389/full#B21), use the LLM-as-a-Judge strategy with MT-Bench and Chatbot Arena and report that GPT-4 achieves 85% agreement with human experts, which is higher than the 81% agreement among human annotators themselves. This reinforces the reliability of advanced LLMs like GPT-4 as scalable surrogates for human judgment in evaluation pipelines.

In our study, we similarly observe around 90% agreement between the LLM-based evaluations and human annotations using different prompt configurations. These results are in line with the findings in the literature and confirm that LLM-as-a-Judge can serve as a reliable and scalable alternative to manual evaluation for structured output tasks in search systems.

Finally, we emphasize that while real-time A/B testing metrics such as click-through rate (CTR) and exit rate will eventually serve as automated feedback signals in production, these signals are not currently accessible during the offline development phase. As such, traditional automated baselines cannot be employed to evaluate the effectiveness of query parsing outputs at scale prior to deployment. In this setting, LLM-as-a-Judge serves as an indispensable evaluation mechanism, offering a scalable and semantically grounded alternative to manual annotation.

### 4.6 Error analysis

In this section, we briefly mention some error cases and limitations of the proposed framework. One issue is the tendency of the search query parser to generate hallucinated outputs. The parser may assign categories that do not exist in the predefined category taxonomy or it may fail to make category assignments at the appropriate hierarchical level and assigns categories at a more granular level than required. Although LLM-as-a-Judge is generally effective in assessing the accuracy of the structured outputs, it exhibits improper evaluations in cases where such hallucinations occur. The main reason for these errors is that LLM-as-a-Judge lacks reference ground truth values, relying solely on the instructions provided in the system prompt of the search query parser. When the prompt does not contain sufficiently detailed explanations, the evaluation process becomes susceptible to errors as the model has no alternative means of verifying correctness.

Another limitation of the framework involves domain-specific search requirements. In cases of incorrect category matching, the model for instance may misclassify a term such as “golf” under sports rather than identifying it as a car model (Volkswagen Golf). In such cases, LLM-as-a-Judge struggles to detect misclassifications, leading to erroneous evaluations. Furthermore, the model exhibits difficulty in recognizing implicit information within the search queries. For example, the word “paint-free” implies that a vehicle is undamaged and the filters should be extracted according to this. However, the search query parser fails to infer this meaning and LLM-as-a-Judge does not correctly flag the response as erroneous.

These findings suggest that enhancing the system prompt with more detailed explanations and incorporating domain-specific knowledge 5improve the reliability of LLM-as-a-Judge in evaluating search query parser outputs.

## 5 Conclusion

In this paper, we introduced LLM-as-a-Judge, a general framework for evaluating structured outputs, with a specific focus on search query parsing in an online classifieds platform. Unlike traditional evaluation methods, the proposed approach leverages LLMs' reasoning abilities to assess structured outputs more effectively, ensuring context-aware, interpretable, and scalable evaluations. We proposed three evaluation methodologies, Pointwise, Pairwise, and Pass/Fail, to cover different assessment needs, and we further enhanced reliability and efficiency with the Contextual Evaluation Prompt Routing strategy which dynamically adjusts evaluation prompts based on query categories. To validate the framework, we conducted experiments on two datasets which are a small, manually curated dataset and a large, real-world dataset. The small dataset enabled us to iteratively refine our evaluation prompts and methodologies, while the large dataset allowed us to test the scalability of the prompt routing approach. The findings confirmed that routing the prompts based on context of the query significantly improves the evaluation accuracy, particularly in category-specific few-shot prompting. Also, the reliability analysis showed that this approach is highly effective for well-defined, high-traffic categories, while more ambiguous queries require further optimization to achieve consistent evaluations.

The experimental results highlighted key insights into the performance of different evaluation techniques, some of which are outlined below:

• Pointwise evaluation: across both LLM-based and rule-based parser outputs, few-shot prompting generally improved alignment with human scores, as reflected by increased Spearman's correlation. For example, in the rule-based parser, correlation rose from 0.564 to 0.793 (flash-002) and from 0.677 to 0.853 (pro-002). Incorporating reference values further boosted alignment, achieving correlation scores of up to 0.898 for the LLM-based parser and 0.870 for the rule-based parser.

• Pairwise evaluation: by adding few shot examples to the prompt we improved the alignment from 0.773/0.758 to 0.879 for both models. Also, we mitigated position bias by randomizing the order of the outputs of the two parsers, improving exact match accuracy from 0.833 to 0.879.

• Pass/fail evaluation: the prompt routing method achieved 0.939 exact match accuracy and 0.861 Cohen's Kappa (flash-002) on the small-scale dataset and 0.87–0.97 exact match accuracy on the large-scale real world dataset for the LLM-based parser, demonstrating its effectiveness in binary classification tasks.

As future work, we aim at improving the reliability of the evaluation of ambiguous queries, specifically those without a clear category and those outside the four main categories. This will involve expanding the prompt diversity by incorporating a broader range of query formulations and optimizing prompt routing strategies for these underrepresented categories. Additionally, we plan to explore alternative LLM architectures and fine-tune the models with domain-specific evaluation data to further enhance alignment with human judgments. Another key direction is automating the refinement process by iteratively identifying failure cases and adapting the evaluation prompts dynamically. Also, we will investigate cross-domain generalization, applying the LLM-as-a-Judge framework to other structured output evaluation tasks beyond search query parsing. Lastly, once the system is live in the future, we plan to use live A/B testing metrics as a post-deployment baseline to measure the practical effectiveness of the LLM-as-a-Judge evaluations. These real-world metrics will allow us to retrospectively validate and calibrate the judgments made by our LLM-based evaluation framework, providing a closed-loop mechanism that combines human-aligned semantic assessment with behavioral user signals from production.

</details>

<details>
<summary>Human-in-the-Loop (HITL) in AI/ML: Smarter Intelligence in the AI or Human Era</summary>

# Human-in-the-Loop (HITL) in AI/ML: Smarter Intelligence in the AI or Human Era

Learn how HITL AI enhances decision-making, reduces bias, and builds trust in GenAI and large language models across enterprise use cases.

Will AI replace humans? That question is already outdated.

It’s no longer AI or humans as the real story lies in how the two can work together to create smarter and reliable AI systems. Central to this is none other than Human-in-the-Loop (HITL), a groundbreaking methodology that seamlessly integrates machine intelligence with human oversight to make AI decisions fair, transparent, and accurate.

This is transforming multiple industries like healthcare, finance, and retail by combining the strengths of AI’s speed and data-processing power with human creativity and oversight. In this blog, we will explore how this concept enables that, along with its diverse use cases, best practices, and emerging future trends.

## What is Human-in-the-Loop (HITL)?

AI/ML system lifecycles greatly benefit from collaborative approaches, integrating human input and nuanced expertise within complex frameworks. Humans train AI models and provide crucial guidance, thereby enhancing adaptability, reliability, and accuracy of models. HITL leverages humans and machines' aggregated capabilities, facilitating rather accurate decisions with ethical insights in place. It is widely used in AI content moderation, image classification, speech recognition, etc.

Humans can interact with AI and ML processes in the following ways:

- Data labeling - Your AI model is only as good as the quality of data you feed it. But in complex domains like medical diagnostics, AI/ML models will struggle with unstructured data. This is where humans label complex or ambiguous data points to guide the model.
- Model feedback - After deploying an AI model, human experts step in to rectify any incorrect outputs. When a model's prediction is incorrect, humans can give feedback and tweak outputs accordingly with precision. Iterative feedback loops facilitate incremental model refinement over time, minimizing errors significantly with each successive cycle of refinement.
- Active learning - This involves model solicitation of human input on data points that are difficult to comprehend. Human experts label the most informative samples, and the models also flag data points that they’re least confident about, saving time from having to label every single data point.

Human-in-the-loop systems come in various types as well:

- Interactive - Humans interact directly with AI algorithms to provide guidance and feedback.
- Semi-automated - Combines automated processes and human input to optimize the performance of AI models.
- Real-time - Humans monitor these systems continuously and address dynamic changes in data or outputs.

Clearly, this collaborative process between AI and humans is no longer optional. Understanding the critical roles humans play in the decision-making process of AI/ML systems sheds light on how this approach ensures adaptability and ethical standards in complex, real-world situations.

## Why Human-in-the-Loop Matters in AI & ML

AI and ML can accomplish much in the tech space, but even they have limitations when it comes to making accurate and fair decisions. This is where humans step in, offering critical context and problem-solving skills, thereby filling gaps in AI's decision-making processes.

Here’s a deep dive on why HITL matters:

### 1\. Enhancing Accuracy in Complex or Edge Cases

AI models occasionally stutter in obscure scenarios known as Edge cases, which impact the accuracy and reliability of delivered outputs. Human experts validate and refine AI outputs, thereby enhancing the scope for greater accuracy.

For instance, AI in dermatology may struggle to fully distinguish diverse skin tones and various conditions. Dermatologists review AI assessments of patients and train models on subtle distinctions, thereby improving precision with each new iteration.

### 2\. Bringing Ethical Oversight and Reducing Bias

AI systems trained on skewed datasets often amplify unfair outcomes or perpetuate discriminatory results in many cases. Human-in-the-loop review is crucial here for mitigating biases by optimizing decision criteria and tweaking training data continuously. Human ethical supervision ensures outputs stay fair and align with societal norms, something autonomous systems often disregard or overlook.

### 3\. Boosting Trust and Transparency in AI Systems

Many AI models operate as “black boxes,” making decisions that are difficult to comprehend. HITL introduces human judgments at critical points, making AI decisions more explainable. Circling back to an example in medical diagnostics, radiologists can review and confirm if AI highlights in medical images are accurate and relevant, making explanations medically sound. This boosts trust and transparency, which are needed in high-stakes sectors like finance and healthcare.

### 4\. Improving Model Learning Through Human Feedback

The concept of human-in-the-loop emphasizes making human values clear while working and coexisting with AI/ML systems ( [Source](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/keeping-artificial-intelligence-real)). And human feedback plays a critical role in improving coexistence through continuous model learning and refinement. HITL fosters a continuous feedback loop where humans provide labeled data, score outputs, and rectify errors, allowing AI models to learn, adapt, and ensure predictive accuracy over time.

### 5\. Making AI Safer for High-Stakes Applications

Timing and accuracy matter the most in critical domains like healthcare, finance, legal services, and autonomous driving. While AI makes swift decisions, humans review those decisions before deployment, catching any errors that the system may have overlooked. Human oversight here enhances safety and reliability, preventing severe consequences that may arise from errors.

From the points listed above, the importance of human involvement in AI’s decision-making cannot be overstated. However, some organizations might still leave all core decisions and processes to autonomous systems. While it does have some perks, it still falls short of the collaborative power of humans and AI in data-driven and ethical outputs delivered.

## Human-in-the-Loop vs. Fully Automated Systems

Here’s a comprehensive distinction between the collaborative HITL approach and the independent nature of fully automated systems:

| | | |
| --- | --- | --- |
| **Basis** | **HITL systems** | **Fully automated systems** |
| Operation | Involves humans at specific stages of the process to provide feedback, make decisions, and guide automation | Designed to operate autonomously, making decisions and taking action without human intervention |
| Speed and efficiency | Slower due to human involvement and coordination | Can process information and complete tasks at a faster rate than human-operated systems. |
| Scalability | [AI scalability can be a challenge](https://www.tredence.com/blog/ai-scalability) due to human resource constraints | Highly scalable |
| Cost | Higher operational costs due to human labor and slower throughput | Initial investments are higher, but have lower ongoing labor costs |
| Risk management | Superior risk mitigation where humans are involved in critical areas | Poses higher risk of unmitigated errors in critical situations due to lack of human oversight |
| Error handling | Includes exceptional management | Automation may fail silently |

## Top HITL Use Cases

The applications of Human-in-the-loop automation can be seen in multiple fields like healthcare, finance, and retail. AI is used extensively to streamline critical processes and decision-making, which humans oversee and review to enhance accuracy, reliability, and trust in various applications. Here are some examples of HITL’s real-world use cases:

- Content moderation and annotation - Human experts moderate user-generated content on digital platforms to ensure compliance with legal regulations.
- Customer support automation - AI-powered chatbots handle routine queries, but escalate complex or unclear issues to human agents for personalized assistance, boosting customer satisfaction.
- Fraud detection in BFSI - While AI flags suspicious transactions, humans validate alerts to reduce false flags and review fraud patterns effectively.
- Retail and Supply Chain Forecasting - Human experts oversee and refine [AI-powered supply chain](https://www.tredence.com/blog/remove-silos-and-orchestrate-your-network-with-an-aipowered-supply-chain) forecasting models that analyze real-time data. They help optimize inventory levels, reduce waste, and improve demand forecasting.
- Healthcare diagnostics - Integration of HITL systems in medical imaging or diagnostics enables clinicians to assess and validate diagnostic outcomes.
- Generative AI safety - Active usage of GenAI has been estimated to be between 115-180 million in 2025 ( [Source](https://www.technollama.co.uk/a-gemini-report-how-many-people-are-using-generative-ai-on-a-daily-basis-a-gemini-report)). Rapid adoption also raises several safety concerns, which humans address by monitoring its outputs to prevent biased or inaccurate content.

There are plenty of other ways human-in-the-loop can be used to drive the best outcomes. However, nothing is without its unique challenges.

## Challenges of HITL Systems

On the surface level, implementing Human-in-the-loop in AI systems may seem like a winning strategy that’s not only efficient but risk-free as well. However, there are still challenges that make this system quite complex. Here are some common challenges and potential solutions to tackle them:

1\] Scalability issues: As data volume grows, human involvement may create bottlenecks as manual reviews are expensive and time-consuming.

Potential Solutions

- Tiered evaluation - Initial evaluations are broader, followed by detailed reviews for higher accuracy.
- AI-powered pre-filtering - AI pre-filters data, highlighting potential issues and automating routine tasks.
- Human-in-the-loop reinforcement learning - Humans train AI systems to learn from their mistakes, improving performance over time.

2\] Latency: Human feedback introduces delays, which is a problem for applications requiring instant, real-time responses.

Potential Solutions

- Edge computing - Processes data closer to the source, minimizing the distance data needs to travel to a central cloud, enabling faster response times.
- Hybrid systems - AI handles immediate tasks while humans are involved asynchronously to handle complex tasks.

3\] Bias risks - Human experts may intentionally/unintentionally introduce or reinforce biases based on their personal experiences or perspectives, compromising accuracy and fairness in deployment outcomes.

### Potential Solutions

- Bias detection tools - They identify and quantify potential [biases in AI models](https://www.tredence.com/blog/ai-bias) and data, allowing human reviewers to focus on areas where AI is most likely to be unfair. D-BIAS, IBM AI Fairness 360, and Microsoft Fairlearn are popular bias detection tools that can be used.
- Diverse group of annotators - Diverse teams bring in different perspectives, catching nuances that can block individual biases.
- Continuous auditing - This process ensures outputs are continuously monitored to identify and correct biased patterns.

4\] Training & Consistency - Variabilities in skill and judgment among human experts are also major challenges that deter the quality and standards of the inputs given.

### Potential Solutions

- Training programs - Human contributors will be equipped with the necessary skills and knowledge needed to effectively guide AI systems.
- Quality control mechanisms - Structured annotator programs for targeted training, review cycles, and consensus pipelines can resolve discrepancies and improve consistency in human inputs.

## Best Practices to Implement HITL in AI/ML Projects

To successfully implement Human-in-the-loop in artificial intelligence and machine learning projects and solve the surrounding challenges, follow these best practices:

Define the HITL role - Clearly define specific human roles for efficient collaboration with AI/ML systems. For example, you can assign reviewers to verify model outputs, labelers to annotate training data, and validators to confirm model decisions, ensuring proper workflow and higher accuracy.

Use active learning - Incorporate active learning only when the model’s confidence level is low or uncertain. This way, human efforts are well-optimized and more focused on the most ambiguous cases, improving training efficiency and model accuracy.

Train humans like models - Just like how AI/ML models are trained on data, human contributors should also be trained on annotation guidelines, review criteria so they can give high-quality inputs for the models. This ensures transparency and higher accuracy, adding reliability as well.

Feedback integration - Establish a continuous feedback loop where human insights are systematically fed into the model’s training practices. This practice closes the loop, allowing the model to learn from human inputs, improve, and adapt to new data.

Leverage MLOps frameworks - Implement [MLOps best practices](https://www.tredence.com/blog/mlops-a-set-of-essential-practices-for-scaling-ml-powered-applications) like automating data annotation pipelines, tracking audit logs, managing human feedback, and model retraining. They seamlessly combine machine efficiency with human judgment, creating AI systems that are fair, accurate, and trustworthy.

## Future of Human-in-the-Loop AI

While AI keeps advancing, the concept of HITL highlights the indispensable role of human oversight in developing and refining AI models. And as we look ahead, understanding the evolving nature of this collaboration can make a difference in building trustworthy autonomous systems. Let’s take a look at some up-and-coming trends:

### Agentic AI

Human-in-the-loop systems and [agentic AI](https://www.tredence.com/blog/agentic-ai) are poised to have a symbiotic relationship, where AI agents handle routine tasks and human experts intervene when necessary. It is also predicted that by 2028, 15% of daily work decisions will be made autonomously by agentic AI ( [Source](https://www.gartner.com/en/articles/intelligent-agent-in-ai)). In such a case, this calls for a balance between both systems, where humans effectively train AI agents to make accurate and fair decisions autonomously.

### Augmented intelligence

There is a common misconception that AI will completely replace humans in almost all sectors. But [augmented intelligence](https://www.tredence.com/blog/forrester-augmented-intelligence-unlocks-the-intelligence-in-ai) says otherwise - AI doesn’t replace humans, but enhances human capabilities even further. As AI models become more sophisticated, their combination will push the boundaries of human-machine collaboration, improving decision-making and user experiences across multiple fields.

For example, in finance, augmented intelligence systems will assist analysts in detecting fraud by tracking transaction patterns. And human experts will review these alerts to confirm fraud and decide on appropriate actions.

### LLMs

LLMs like GPT-4 and Gemini are powerful natural language processors that generate human-like text, but require human inputs for added quality, creativity, and ethical use. HITL will be integral here to fine-tune LLMs through techniques like reinforcement learning, prompt engineering, and continuous evaluation. This ensures LLMs always align with human values.

## Final Thoughts

The smartest AI doesn’t keep humans on the sidelines. Instead, it collaborates with them, which is the primary goal human-in-the-loop achieves. This concept is the bridge between cutting-edge AI capabilities and ethical, trustworthy deployment, ensuring outputs are both powerful and principled.

It’s no longer human vs AI - it’s the synergy of human and AI working together to unlock smarter, more responsible AI solutions.

## FAQs

### 1\] What is Human-in-the-Loop (HITL) AI?

HITL AI is an approach that integrates human intelligence and judgment with AI systems and ML processes, combining their strengths to improve accuracy, reliability, and ethical decision-making.

### 2\] Why is HITL important for enterprise AI/ML?

HITL holds significant importance in enterprise AI and machine learning initiatives because of its ability to validate model accuracy thoroughly. It leverages human expertise to refine AI models and subsequently mitigate considerable bias. Fairness is ensured during development and deployment with ethical considerations addressed amidst complex scenarios.

### 3\] What are real-world HITL use cases in industries?

A few real-world, industry-wide use cases of HITL include:

- Healthcare: Analyzing medical images and flagging potential abnormalities, with human clinicians validating these findings to ensure accurate diagnoses.
- Retail: Assists in inventory management, product recommendations, and customer service with human judgment involved to refine predictions and improve shopping experiences.
- Finance: Used in areas like creditworthiness, fraud detection, investment portfolio management, price adjustments, and regulatory compliance.

### 4\] What challenges come with scaling HITL systems?

Some of the common challenges of scaling these systems include high investment costs, security risks, maintaining the quality of human feedback, and logistical constraints.

### 5\] Can HITL work with GenAI and LLMs?

Yes, it can work effectively alongside GenAI and LLMs by leveraging human judgment to refine AI-generated content. GenAI outputs remain reliable and trustworthy across various applications, owing largely to collaboration between humans and advanced AI systems.

### 6\] How can enterprises measure HITL success?

Enterprises can measure HITL success by tracking metrics relevant to both the AI model’s performance and human contributions. AI model metrics to track include error rate, accuracy, and speed, while human metrics include feedback quality, human efforts, and satisfaction over the process.

</details>

<details>
<summary>The provided markdown content is a complete article on "Human-in-the-Loop for AI Agents," which is a topic related to, but not the core focus of, Lesson 19.</summary>

The provided markdown content is a complete article on "Human-in-the-Loop for AI Agents," which is a topic related to, but not the core focus of, Lesson 19.

The article guidelines for Lesson 19 explicitly state its purpose is to **finish the research agent** by adding quality-control and compilation steps, introducing specific MCP tools (`select_research_sources_to_keep_tool.py`, `select_research_sources_to_scrape_tool.py`, `scrape_research_urls_tool.py`, `create_research_file_tool.py`), running the full agent, and showing Cursor integration.

While Lesson 19's Section 7 is dedicated to "Human-in-the-Loop (HITL) Controls via MCP," this section is specifically about how HITL applies to the *research agent's* quality gates (e.g., approving kept/scraped sources via prompt-level controls). It is not a general overview of HITL concepts, frameworks, or use cases as presented in the scraped content.

Therefore, the entire scraped markdown content is considered irrelevant to the specific scope of Lesson 19 as defined by the article guidelines. The task is to keep *only* the core textual content pertinent to the *article guidelines provided*. Since the content does not align with the lesson's primary focus on the research agent's completion and specific tools, it should all be removed.

</details>

<details>
<summary>Scraping vs. API: Best Method to Track AI Search Visibility</summary>

# Scraping vs. API: Best Method to Track AI Search Visibility

By [Rebecca Brosnan](https://www.seoclarity.net/blog/author/rebecca-brosnan), August 26, 2025
, in

[AI / Machine Learning](https://www.seoclarity.net/blog/topic/ai-machine-learning) and

[API](https://www.seoclarity.net/blog/topic/api)

As AI search engines become increasingly popular for retrieving information, they have the potential to significantly influence user perception, guide purchasing decisions, and shape overall brand visibility

As such, it’s essential for SEOs, marketers, and brand managers to understand not only how their brand appears within AI-generated answers, but also search intent and how users are engaging.

There are two primary methods for tracking AI search visibility: **UI scraping** and **API-based data collection**. The method used can significantly impact the accuracy, completeness, and usefulness of the insights you receive.

In this post, we’ll break down the key differences between UI scraping and API-based data collection to help you cut through the noise and choose the approach that best supports accurate AI search visibility tracking.

Table of Contents:

- [Key Differences Between UI Scraping and API-Based Monitoring](https://www.seoclarity.net/blog/scraping-vs.-api#key-differences)
- [API-Based Data Collection for AI Search: How It Works](https://www.seoclarity.net/blog/scraping-vs.-api#how-api-works)
- [The Downside of API-Based Monitoring](https://www.seoclarity.net/blog/scraping-vs.-api#downside-api)
- [UI Scraping for AI Search Data: How It Works](https://www.seoclarity.net/blog/scraping-vs.-api#how-ui-scraping-works)
- [The Advantages of UI Scraping](https://www.seoclarity.net/blog/scraping-vs.-api#advantages-ui-scraping)
- [Side-By-Side Comparison: API vs UI Scraping](https://www.seoclarity.net/blog/scraping-vs.-api#side-by-side)
- [Why This Matters for Enterprise AI Search Optimization](https://www.seoclarity.net/blog/scraping-vs.-api#why-this-matters)
- [The Bottom Line](https://www.seoclarity.net/blog/scraping-vs.-api#bottom-line)

## Key Differences Between UI Scraping and API-Based Monitoring

| | **UI Scraping** | **API-Based Monitoring** |
| --- | --- | --- |
| **What it captures** | Full user-facing output <br>(citations, shopping results, plugins, formatting) | Raw model text only |
| **Accuracy** | Mirrors what real users see | Simplified, developer-facing version |
| **Data source** | Rendered interface output from a logged-in session | Structured responses returned by the API |
| **Context** | Shows brand mentions, citations, and presentation | Provides text without user experience context |
| **Difficulty** | Requires more technical effort | Easy and fast way to gather data that is open to anyone |

### API-Based Data Collection for AI Search: How It Works

AI search platforms offer API access. This is designed for developers to build applications and interact with the language model, focusing often on text-based tasks rather than product discovery or [shopping-related features](https://help.openai.com/en/articles/11128490-improved-shopping-results-from-chatgpt-search).

For example, using OpenAI’s API, you define parameters (like model version or prompt) and receive a raw output from the model without any influence from the ChatGPT interface.

### The Downside of API-Based Monitoring

API access is, no doubt, the easiest way to gather AI search visibility data. It’s clean, fast, and **open to anyone**. Many new players entering the AI search tracking space are taking this route precisely for these reasons.

But here's the problem: **APIs do not show what real users actually see**.

Take ChatGPT, for example. The interface users interact with applies its own proprietary logic, adding features like:

- Shopping results with clickable product links
- Plugins and browsing enhancements
- Specific model behaviors tied to UI settings

None of that is accessible via the API. The API returns plain text that is detached from the nuanced logic of the ChatGPT experience. It’s not a mirror of reality. It’s a simplified version for developers.

This leads to the fundamental flaw: **you can’t fully understand how a brand is showing up in AI search if you’re only seeing what the API allows.**

## UI Scraping for AI Search Data: How It Works

UI scraping simulates a logged-in user interacting directly with an AI tool like ChatGPT. It **captures the full response as displayed in the interface**—including model selection, live web browsing content, citations, shopping results, and formatting.

UI scraping is typically used when the goal is to mirror what end users see during real interactions with the platform.

The process typically involves:

- Logging into the platform programmatically
- Issuing queries as a real user would
- Capturing rendered output, citations, and any interactive elements
- Digitizing the rendered output into useful data, metrics and insights

### The Advantages of UI Scraping

When it comes to fully understanding what the end user sees, UI scraping is the more effective approach.

Scraping from a logged-in perspective allows you to replicate the true user experience by:

- Capturing actual results as users see them
- Retrieving all citations, brand mentions, and contextual phrasing
- Reflecting the influence of model choice, browsing behavior, and plugins

This method is more challenging from a technical perspective, but it delivers a more **complete and accurate view**.

As previously stated, the ChatGPT UI includes additional logic and response handling not reflected in the API. Further, many of the underlying parameters used in the UI are not publicly disclosed, making it impossible to fully replicate the same output through the API alone.

Ultimately, **scraping the UI is the only way to capture the full picture of brand visibility in AI search**.

## Side-By-Side Comparison: API vs UI Scraping

Still unsure which method provides the most accurate results? See for yourself!

Here’s a side-by-side comparison of responses to the same query **“top 3 running shoes for low arches,”** run through both the ChatGPT UI and the API, using the same GPT-5 model with web browsing enabled.

#### API Response With Web Search Enabled:

#### https://lh7-rt.googleusercontent.com/docsz/AD_4nXeoxHTBOLqf2CIUCR4CWbp8VbkVQZYeQEXS-67blsQ9gmpsktWhs14w9-VcWJAqtlsb5FZlIAteLnUfdk0XemUf-PjBdneBYj5LY7koNCCCyQ8YTaT_QFeyzy1jN7LO1KPbf21S?key=88SeSoJavKNKwFLIis9r6Q

- Text-only output
- Includes citations from relevant sources
- No formatting or structure typical of user-facing platforms
- No shopping or product-specific enhancements
- Generic summary without brand emphasis

#### UI Output For the Same Prompt:

https://lh7-rt.googleusercontent.com/docsz/AD_4nXeK2ISgWj0pzTzg1XIxEsDHNs1NSBRleOwTyAy208lXVpWx_BRz-_ce89TKjPecXKUL0xTeS4ztw6I5SmzFhCb9S1NrKzDvjaNoiKyY9m2NLteC44slSXdurYbhXfJsu79FVA_PVg?key=88SeSoJavKNKwFLIis9r6Q

- Conversational tone with natural language formatting
- Includes clickable shopping results (when available)
- Highlights specific products with context and user-focused recommendations
- Dynamic interface logic (e.g., model settings, browsing behavior) influences output
- Mirrors the real experience end users see

While the API does return a response with cited web sources, the experience is noticeably different. The UI version includes a more curated, conversational result, often with richer formatting, product highlights, and additional context that mirrors how users engage with the platform.

Despite using the same model and enabling browsing, the **output between the two is far from identical**, reinforcing the fact that the UI introduces its own logic, presentation, and enhancements that the API doesn’t replicate.

### Why This Matters for Enterprise AI Search Optimization

Brands don’t just want to know what a model is _capable_ of generating. They want to know:

- Where their brand appears in generative answers
- How competitors are being mentioned
- How product recommendations are made

These are questions about _experience_, not just data. And that experience can only be captured by emulating the user’s interaction with AI search tools.

### The Bottom Line

API-based solutions provide a clean and consistent dataset, but it’s a simplified view. They show _a version_ of the truth, not necessarily what end users experience.

Scraping from the UI, on the other hand, captures the full context: citations, phrasing, shopping results, and everything else that shapes how your brand appears in AI search.

We built [AI search visibility tracking](https://www.seoclarity.net/ai-seo/ai-search-engine-visibility) in Clarity ArcAI to help marketers optimize for real-world impact.

https://www.seoclarity.net/hs-fs/hubfs/Rebecca%20Profile%20Photo-1.jpg?width=140&name=Rebecca%20Profile%20Photo-1.jpg

[Rebecca Brosnan](https://www.seoclarity.net/blog/author/rebecca-brosnan)

Rebecca is a seasoned SEO content writer at seoClarity, bringing over 6 years of experience in crafting compelling and optimized online content for clients in a diverse range of industries. Her passion for SEO content writing stems from her love of educating readers as well as seeing the rewarding results of her work in the form of increased organic traffic and engagement.

</details>


## Local Files From Research

<details>
<summary>Lesson 19: Final Outputs and Agent Completion</summary>

# Lesson 19: Final Outputs and Agent Completion

In our final lesson about the research agent implementation, we will complete the research agent's workflow by implementing the remaining tools that filter research results, scrape additional sources, and compile everything into a final research file. We'll test the complete end-to-end agent and analyze its output.

Learning Objectives:
- Learn how to filter and validate research sources for quality and trustworthiness
- Understand how to select the most valuable sources for full content scraping
- Implement the final research compilation tool that creates structured outputs
- Test the complete agent workflow and analyze output quality

## 1. Setup

First, we define some standard Magic Python commands to autoreload Python packages whenever they change:

```python
%load_ext autoreload
%autoreload 2
```


### Set Up Python Environment

To set up your Python virtual environment using `uv` and load it into the Notebook, follow the step-by-step instructions from the `Course Admin` lesson from the beginning of the course.

**TL/DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.

### Configure Required APIs

To run this lesson, you'll need several API keys configured:

1. **Gemini API Key**, `GOOGLE_API_KEY` variable: Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2. **Firecrawl API Key**, `FIRECRAWL_API_KEY` variable: Get your key from [Firecrawl](https://firecrawl.dev/). They have a free tier that allows you to scrape 500 pages.

```python
from utils import env

env.load(required_env_vars=["GOOGLE_API_KEY", "FIRECRAWL_API_KEY"])
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


## 2. Completing the Research Workflow

As we've seen in previous lessons, our research agent follows a systematic workflow. We've covered the initial data ingestion (lesson 16) and the research loop with query generation (lesson 17). Now we need to implement the final steps that ensure quality and compile the results.

The complete workflow includes these final steps:

```markdown
4. Filter Perplexity results by quality:
    4.1 Run the "select_research_sources_to_keep" tool to automatically evaluate each source 
    for trustworthiness, authority and relevance.

5. Identify which of the accepted sources deserve a full scrape:
    5.1 Run the "select_research_sources_to_scrape" tool to choose up to 5 diverse, 
    authoritative sources whose full content will add most value.
    5.2 Run the "scrape_research_urls" tool to scrape/clean each selected URL's full content.

6. Write final research file:
    6.1 Run the "create_research_file" tool to combine all research data into a 
    comprehensive research.md file.
```

Let's examine each of these final tools and understand their purpose in the workflow.

## 3. Filtering Research Sources for Quality

The `select_research_sources_to_keep` tool addresses a critical problem we discovered during development: Perplexity results often include sources from untrustworthy blogs, SEO spam, or low-quality content that would pollute our research.

### 3.1 Understanding the Tool Implementation

This tool takes a research directory as input and automatically filters Perplexity results for quality. It reads the article guidelines and raw Perplexity results, then uses an LLM to evaluate each source based on trustworthiness, authority, and relevance criteria. The tool outputs two files: a list of selected source IDs and a filtered markdown file containing only the approved sources. This automated filtering saves time while ensuring research quality.

Source: _mcp_server/src/tools/select_research_sources_to_keep_tool.py_

```python
async def select_research_sources_to_keep_tool(research_directory: str) -> Dict[str, Any]:
    """
    Automatically select high-quality sources from Perplexity results.

    Uses an LLM to evaluate each source in perplexity_results.md for trustworthiness,
    authority, and relevance based on the article guidelines. Writes the comma-separated
    IDs of accepted sources to perplexity_sources_selected.md and saves a filtered
    markdown file perplexity_results_selected.md containing only the accepted sources.

    Args:
        research_directory: Path to the research directory containing article guidelines and research data

    Returns:
        Dict with status, selection results, and file paths
    """
    # Convert to Path object
    research_path = Path(research_directory)
    nova_path = research_path / NOVA_FOLDER
    
    # Gather context from the research folder
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    results_path = nova_path / PERPLEXITY_RESULTS_FILE
    
    article_guidelines = read_file_safe(guidelines_path)
    perplexity_results = read_file_safe(results_path)
    
    # Use LLM to select sources
    selected_ids = await select_sources(
        article_guidelines, perplexity_results, settings.source_selection_model
    )
    
    # Write selected source IDs to file
    sources_selected_path = nova_path / PERPLEXITY_SOURCES_SELECTED_FILE
    sources_selected_path.write_text(",".join(map(str, selected_ids)), encoding="utf-8")
    
    # Extract and save filtered content
    filtered_content = extract_selected_blocks_content(selected_ids, perplexity_results)
    results_selected_path = nova_path / PERPLEXITY_RESULTS_SELECTED_FILE
    results_selected_path.write_text(filtered_content, encoding="utf-8")
    
    return {
        "status": "success",
        "sources_selected_count": len(selected_ids),
        "selected_source_ids": selected_ids,
        "sources_selected_path": str(sources_selected_path.resolve()),
        "results_selected_path": str(results_selected_path.resolve()),
        "message": f"Successfully selected {len(selected_ids)} high-quality sources..."
    }
```

The core of this tool is the `select_sources` function, which uses the `PROMPT_SELECT_SOURCES` prompt to evaluate each source and select the most relevant ones.

### 3.2 The Source Evaluation Prompt

Here's the prompt used to evaluate the sources:

Source: _mcp_server/src/config/prompts.py_

```python
PROMPT_SELECT_SOURCES = """
You are a research quality evaluator. Your task is to evaluate web sources for an upcoming article
and select only the high-quality, trustworthy sources that are relevant to the article guidelines.

<article_guidelines>
{article_guidelines}
</article_guidelines>

Here are the sources to evaluate:
<sources_to_evaluate>
{sources_data}
</sources_to_evaluate>

**Selection Criteria:**
- ACCEPT sources from trustworthy domains (e.g., .edu, .gov, established news sites,
official documentation, reputable organizations)
- ACCEPT sources with high-quality, relevant content that directly supports the article guidelines
- REJECT sources from obscure, untrustworthy, or potentially biased websites
- REJECT sources with low-quality, irrelevant, or superficial content
- REJECT sources that seem to be marketing materials, advertisements, or self-promotional content

Return your decision as a structured output with:
1. selection_type: "none" if no sources meet the quality standards, "all" if all sources are acceptable,
or "specific" for specific source IDs
2. source_ids: List of selected source IDs
""".strip()
```

This prompt serves as a quality gatekeeper, automatically filtering out unreliable sources that could compromise research quality. The key aspect is the structured selection criteria that balance domain reputation, content quality, and relevance. The prompt explicitly targets common quality issues like SEO spam, marketing content, and biased sources that often pollute web search results, ensuring only authoritative sources proceed to the next stage.

### 3.3 Testing the Source Selection Tool

Let's test the source filtering tool to see how it evaluates and selects high-quality sources from our Perplexity results. The tool will analyze each source and provide feedback on which ones meet our quality standards.

```python
from research_agent_part_2.mcp_server.src.tools import select_research_sources_to_keep_tool

# Test the source selection tool
research_folder = "/path/to/research_folder"
result = await select_research_sources_to_keep_tool(research_directory=research_folder)
print(result)
```

**Output:**
```
/Users/fabio/Desktop/course-ai-agents/.venv/lib/python3.12/site-packages/pydantic/_internal/_fields.py:198: UserWarning: Field name "schema" in "FewShotExampleStructuredOutputCompliance" shadows an attribute in parent "BaseModel"
  warnings.warn(
/Users/fabio/Desktop/course-ai-agents/.venv/lib/python3.12/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
  from .autonotebook import tqdm as notebook_tqdm
[32m2025-09-24 13:58:58.185[0m | [1mINFO    [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | 👍 All sources accepted.
```

**Output:**
```
{'status': 'success', 'sources_selected_count': 12, 'selected_source_ids': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 'sources_selected_path': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/perplexity_sources_selected.md', 'results_selected_path': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/perplexity_results_selected.md', 'message': '✅ Selected 12 source(s). IDs written to /Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/perplexity_sources_selected.md. Filtered results written to /Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/perplexity_results_selected.md.'}
```

**Output:**
```
[32m2025-09-24 13:59:32.995[0m | [1mINFO    [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | 👍 3 sources selected to scrape.
[32m2025-09-24 13:59:37.915[0m | [1mINFO    [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | HTTP Request: POST https://api.firecrawl.dev/v2/scrape "HTTP/1.1 200 OK"
[32m2025-09-24 13:59:39.887[0m | [1mINFO    [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | HTTP Request: POST https://api.firecrawl.dev/v2/scrape "HTTP/1.1 200 OK"
[32m2025-09-24 13:59:41.921[0m | [1mINFO    [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | HTTP Request: POST https://api.firecrawl.dev/v2/scrape "HTTP/1.1 200 OK"
[32m2025-09-24 14:02:38.124[0m | [31m[1mERROR   [0m | [36mlogging[0m:[36mcallHandlers[0m:[36m1762[0m | LLM API call timed out after 180s for https://arxiv.org/html/2412.01130v2. Using original content.
```


The tool provides feedback on which sources were selected, allowing users to review the decisions if needed.

## 4. Selecting Sources for Full Content Scraping

After filtering for quality, we need to identify which sources deserve a full scrape. While Perplexity provides summaries and excerpts, some high-quality sources contain much more valuable content in their full form. The `select_research_sources_to_scrape` tool analyzes the filtered results and strategically chooses the most valuable sources for comprehensive content extraction. This full content will provide the writing agent with richer context, detailed examples, and comprehensive coverage that brief excerpts cannot capture.

### 4.1 Understanding the Selection Logic

This tool takes filtered Perplexity results and selects the most valuable sources for full scraping. It analyzes the article guidelines, accepted sources, and already-scraped guideline content to avoid duplication. The tool uses an LLM to evaluate sources based on relevance, authority, quality, and uniqueness, then outputs a prioritized list of URLs. The default limit of 5 sources balances comprehensive coverage with processing efficiency and API costs.

Source: _mcp_server/src/tools/select_research_sources_to_scrape_tool.py_

```python
async def select_research_sources_to_scrape_tool(research_directory: str, max_sources: int = 5) -> Dict[str, Any]:
    """
    Select up to max_sources priority research sources to scrape in full.
    
    Analyzes the filtered Perplexity results together with the article guidelines and
    the material already scraped from guideline URLs, then chooses up to max_sources diverse,
    authoritative sources whose full content will add most value. The chosen URLs are
    written (one per line) to urls_to_scrape_from_research.md.
    """
    # Gather context from the research folder
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    results_selected_path = nova_path / PERPLEXITY_RESULTS_SELECTED_FILE
    
    article_guidelines = read_file_safe(guidelines_path)
    accepted_sources_data = read_file_safe(results_selected_path)
    scraped_guideline_ctx = load_scraped_guideline_context(nova_path)
    
    # Use LLM to select top sources for scraping
    selected_urls, reasoning = await select_top_sources(
        article_guidelines, accepted_sources_data, scraped_guideline_ctx, max_sources
    )
    
    # Write selected URLs to file
    urls_out_path = nova_path / URLS_TO_SCRAPE_FROM_RESEARCH_FILE
    urls_out_path.write_text("\n".join(selected_urls) + "\n", encoding="utf-8")
    
    return {
        "status": "success",
        "sources_selected": selected_urls,
        "sources_selected_count": len(selected_urls),
        "output_path": str(urls_out_path.resolve()),
        "reasoning": reasoning,
        "message": f"Successfully selected {len(selected_urls)} sources for full scraping..."
    }
```

The core of this tool is the `select_top_sources` function, which uses the `PROMPT_SELECT_TOP_SOURCES` prompt to evaluate each source and select the best ones to scrape.

### 4.2 The Source Selection Prompt

The tool uses a prompt to choose the most valuable sources:

```python
PROMPT_SELECT_TOP_SOURCES = """
You are assisting with research for an upcoming article.

Your task is to select the most relevant and trustworthy sources from the web search results.
You should consider:
1. **Relevance**: How well each source addresses the article guidelines
2. **Authority**: The credibility and reputation of the source
3. **Quality**: The depth and accuracy of the information provided
4. **Uniqueness**: Sources that provide unique insights not covered by the scraped guideline URLs

Please select the top {top_n} sources that would be most valuable for the article research.

Return your selection with the following structure:
- **selected_urls**: A list of the most valuable URLs to scrape in full, ordered by priority
- **reasoning**: A short explanation summarizing why these specific URLs were chosen
""".strip()
```

This prompt optimizes resource allocation by strategically selecting sources for expensive full-content scraping. The four-dimensional evaluation framework (relevance, authority, quality, uniqueness) ensures maximum research value while avoiding duplication with already-scraped guideline content. The uniqueness criterion is particularly important as it prevents redundant scraping of similar information. The reasoning requirement provides transparency for human oversight and helps identify potential gaps in the selection logic, making the process auditable and improvable.

### 4.3 Testing the Source Selection Tool

Now let's test the source selection tool to see which URLs it chooses for full content scraping. The tool will analyze our filtered sources and select the most valuable ones based on their potential contribution to the final research.

```python
from research_agent_part_2.mcp_server.src.tools import select_research_sources_to_scrape_tool

# Test selecting sources to scrape
result = await select_research_sources_to_scrape_tool(research_directory=research_folder, max_sources=3)
print("Selected sources:")
print(result)
```

**Output:**
```
Selected sources:
{'status': 'success', 'urls_selected_count': 3, 'selected_urls': ['https://www.elastic.co/what-is/large-language-models', 'https://arxiv.org/html/2412.01130v2', 'https://www.legitsecurity.com/aspm-knowledge-base/llm-security-risks'], 'selection_reasoning': "These sources were chosen for their direct relevance to the article's themes of understanding why agents need tools, the development of autonomous AI agents, and crucial security considerations. The Elastic.co source provides a comprehensive overview of LLM limitations that tool use addresses. The ArXiv paper offers authoritative insights into the role of function calling in autonomous agent development and action models. The Legit Security source details critical security risks and mitigation strategies associated with external tool-calling, which is a vital aspect not covered in the existing guideline URLs.", 'urls_output_path': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/urls_to_scrape_from_research.md', 'message': "✅ Saved 3 URL(s) to scrape to /Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/urls_to_scrape_from_research.md.\nReasoning: These sources were chosen for their direct relevance to the article's themes of understanding why agents need tools, the development of autonomous AI agents, and crucial security considerations. The Elastic.co source provides a comprehensive overview of LLM limitations that tool use addresses. The ArXiv paper offers authoritative insights into the role of function calling in autonomous agent development and action models. The Legit Security source details critical security risks and mitigation strategies associated with external tool-calling, which is a vital aspect not covered in the existing guideline URLs."}
```


## 5. Scraping Selected Research URLs

The `scrape_research_urls_tool` handles the full content extraction from our selected sources. It works very similarly to the guideline URL scraping tool we saw in lesson 16, using Firecrawl for robust web scraping and an LLM for content cleaning. For this reason, we won't go into the details of the scraping process here, and we only provide the code for testing the tool.

```python
from research_agent_part_2.mcp_server.src.tools import scrape_research_urls_tool

# Test scraping the selected research URLs
result = await scrape_research_urls_tool(research_directory=research_folder, concurrency_limit=3)
print("Scraping results:")
print(result)
```

**Output:**
```
Scraping results:
{'status': 'success', 'urls_processed': 3, 'urls_total': 3, 'original_urls_count': 3, 'deduplicated_count': 0, 'files_saved': 3, 'output_directory': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/.nova/urls_from_research', 'saved_files': ['understanding-large-language-models-a-comprehensive-guide-el.md', 'enhancing-function-calling-capabilities-in-llms-strategies-f.md', 'large-language-model-llm-security-risks-and-best-practices.md'], 'message': "Processed 3 new URLs from urls_to_scrape_from_research.md in '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder'. Scraped 3/3 web pages."}
```


## 6. Creating the Final Research File

The `create_research_file_tool` is the final step of our entire workflow. It takes all the accumulated research data and formats it into a comprehensive, well-organized markdown file that serves as input for the writing agent we'll build in the next part of the course.

### 6.1 Understanding the Compilation Process

This tool serves as the final orchestrator, combining all research data into a comprehensive markdown file. It takes the research directory as input and collects content from multiple sources: filtered Perplexity results, scraped guideline sources, code repositories, YouTube transcripts, and additional research sources. The tool organizes everything into collapsible sections and outputs a structured `research.md` file with detailed statistics about the compilation process.

Source: _mcp_server/src/tools/create_research_file_tool.py_

```python
def create_research_file_tool(research_directory: str) -> Dict[str, Any]:
    """
    Generate comprehensive research.md file from all research data.
    
    Combines all research data including filtered Perplexity results, scraped guideline
    sources, and full research sources into a comprehensive research.md file. The file
    is organized into sections with collapsible blocks for easy navigation.
    """
    # Convert to Path object
    article_dir = Path(research_directory)
    nova_dir = article_dir / NOVA_FOLDER
    
    # Collect all research data
    perplexity_results = read_file_safe(nova_dir / PERPLEXITY_RESULTS_SELECTED_FILE)
    
    # Collect scraped sources from guidelines
    scraped_sources = collect_directory_markdowns_with_titles(nova_dir / URLS_FROM_GUIDELINES_FOLDER)
    code_sources = collect_directory_markdowns_with_titles(nova_dir / URLS_FROM_GUIDELINES_CODE_FOLDER)
    youtube_transcripts = collect_directory_markdowns_with_titles(nova_dir / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER)
    
    # Collect full research sources
    additional_sources = collect_directory_markdowns_with_titles(nova_dir / URLS_FROM_RESEARCH_FOLDER)
    
    # Build comprehensive research sections
    research_results_section = build_research_results_section(perplexity_results)
    scraped_sources_section = build_sources_section("Scraped Sources from Guidelines", scraped_sources)
    code_sources_section = build_sources_section("Code Sources from Guidelines", code_sources)
    youtube_section = build_sources_section("YouTube Transcripts from Guidelines", youtube_transcripts)
    additional_section = build_sources_section("Additional Research Sources", additional_sources)
    
    # Combine all sections into final research file
    research_content = combine_research_sections([
        research_results_section,
        scraped_sources_section,
        code_sources_section,
        youtube_section,
        additional_section
    ])
    
    # Write final research file
    research_file_path = article_dir / RESEARCH_MD_FILE
    research_file_path.write_text(research_content, encoding="utf-8")
    
    return {
        "status": "success",
        "markdown_file": str(research_file_path.resolve()),
        "research_results_count": len(extract_perplexity_chunks(perplexity_results)),
        "scraped_sources_count": len(scraped_sources),
        "code_sources_count": len(code_sources),
        "youtube_transcripts_count": len(youtube_transcripts),
        "additional_sources_count": len(additional_sources),
        "message": f"Successfully created comprehensive research file: {research_file_path.name}"
    }
```

No need to go into the details of the code here, as it's standard Python code for file I/O and string manipulation. We'll simply test the tool and see the final output to better understand what the input of the writing agent will be.

### 6.2 The Research File Structure

The final research file `research.md` is organized into collapsible sections for easy navigation. It will look like the following:

```markdown
# Research Results

## Research Results from Web Search
<details>
<summary>Query: [Original Query]</summary>

### Source [1]: [URL]
[Content from source]

### Source [2]: [URL]
[Content from source]
</details>

## Scraped Sources from Guidelines
<details>
<summary>Source: [Filename]</summary>
[Full scraped content]
</details>

## Code Sources from Guidelines
<details>
<summary>Repository: [Repository Name]</summary>
[Repository analysis and code content]
</details>

## YouTube Transcripts from Guidelines
<details>
<summary>Video: [Video Title]</summary>
[Full video transcript]
</details>

## Additional Research Sources
<details>
<summary>Source: [URL]</summary>
[Full scraped research content]
</details>
```

This structure provides comprehensive coverage while remaining navigable for both humans and AI writing agents.

### 6.3 Testing the Research File Creation

Now let's test the final compilation tool to see how it brings together all our research data into a comprehensive, well-structured file. This represents the final step of our entire research workflow.

```python
from research_agent_part_2.mcp_server.src.tools import create_research_file_tool

# Test creating the final research file
result = create_research_file_tool(research_directory=research_folder)
print("Research file creation results:")
print(result)

# Read and display a sample of the generated research file
with open(result["markdown_file"], "r") as f:
    content = f.read()
    print("\nFirst 1000 characters of the research file:")
    print(content[:1000] + "...")
```

**Output:**
```
Research file creation results:
{'status': 'success', 'markdown_file': '/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_research_folder/research.md', 'research_results_count': 3, 'scraped_sources_count': 6, 'code_sources_count': 2, 'youtube_transcripts_count': 1, 'additional_sources_count': 2, 'message': '✅ Generated research markdown file:\n  - research.md'}

First 1000 characters of the research file:
# Research

## Research Results

<details>
<summary>What are the fundamental limitations of large language models that tool use and function calling aim to solve?</summary>

### Source [1]: https://hatchworks.com/blog/gen-ai/large-language-models-guide/

Query: What are the fundamental limitations of large language models that tool use and function calling aim to solve?

Answer: Large Language Models (LLMs) have several fundamental technical limitations that tool use and function calling aim to solve:

- **Domain Mismatch**: LLMs trained on general datasets struggle with providing accurate or detailed responses in specialized or niche domains, leading to generic or incorrect outputs when specific expertise is required.

- **Word Prediction Issues**: LLMs often fail with less common words or phrases, affecting their ability to generate or translate technical or domain-specific content accurately.

- **Hallucinations**: LLMs sometimes produce highly original but fabricated information. F...
```


## 7. Human-in-the-Loop Feedback Integration

As we saw in the previous lesson, it's possible to integrate human feedback into the research agent workflow by simply providing instructions after invoking the MCP prompt. For example, when running the workflow, users can instruct the agent to:

- Show the source IDs selected by `select_research_sources_to_keep` and ask for approval before proceeding.
- Display the URLs chosen by `select_research_sources_to_scrape` and allow modifications.
- Pause after any step for human review and guidance.

This flexibility allows users to maintain control over the research quality while benefiting from the agent's analytical capabilities. Notice that this is possible because of how the MCP prompt is designed and how the inputs/outputs of the MCP tools are structured!

The next section will show you how to run the complete workflow from the MCP client. If you want, you could run it and provide some of the workflow modifications above to the agent and see how it performs!

## 8. Testing the Complete Agent Workflow

Now let's test the complete end-to-end research agent workflow. We'll use the MCP client to run the full workflow and examine the results.

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
[35m**Let's Get This Research Started!**

Okay, so I'm ready to roll. My first step is to lay out this research workflow – gotta make sure we're on the same page and, critically, that I have the right starting point. I need to explain the steps, and then I'll politely ask for that all-important `research_directory`. I'm also going to check if there are any tweaks or modifications you'd like to make to the process.

Once that's clear, I'll kick things off by calling `extract_guidelines_urls` to grab the URLs and local files listed in `ARTICLE_GUIDELINE_FILE`. That gives me a solid initial pool to work with.

Then, the heavy lifting begins. I'll launch several parallel processes to handle different types of resources efficiently. I'll call `process_local_files` for local content, `scrape_and_clean_other_urls` for general web pages, `process_github_urls` for those GitHub repositories (always a good source!), and `transcribe_youtube_urls` for any relevant YouTube videos. Parallel processing is key here for speed.

Next comes the core research loop. We'll run this three times, each time generating new search queries with `generate_next_queries`. Those queries will then be fed into `run_perplexity_research` to pull in the initial research results.

Now, we filter. I'll use `select_research_sources_to_keep` to identify and keep only the highest-quality sources from the Perplexity results. This is where expertise comes into play – I need to make sure we're focusing on the good stuff.

Once the good stuff is identified, I'll identify sources for a complete scrape using `select_research_sources_to_scrape`. Then I'll call `scrape_research_urls` to scrape the selected sources.

Finally, I'll synthesize everything. I'll call `create_research_file` to compile all the research, cleaned content, scraped pages, and initial sources into a comprehensive `research.md` file.

Now, a critical point: I need to be prepared for potential hiccups. If *any* of the tools run into trouble and successfully process zero items, I'm going to halt the entire process. I'll state which tool failed and the associated error message, and then I'll ask for your guidance on how to proceed. Better safe than sorry – a failed start could compromise the integrity of the entire process![0m

[37m💬 LLM Response: [0mHello! I will help you execute the Nova research agent workflow. Here are the steps involved:

1.  **Setup**: I will begin by extracting URLs and local file references from your `ARTICLE_GUIDELINE_FILE`.
2.  **Process Extracted Resources**: I will then process these extracted resources in parallel:
    *   Copying referenced local files to a dedicated folder.
    *   Scraping and cleaning content from other web URLs.
    *   Processing GitHub URLs using gitinge...
```

**Output:**
```
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1758624909.196635 3235692 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
```

**Output:**
```
[1m[95m🤔 LLM's Thoughts:[0m
[35m**Ready to Process Extracted Resources**

Okay, so the user has given me the research directory and wants to execute the full workflow. Good, Step 1.3 (`extract_guidelines_urls`) has already finished without a hitch! Now, I need to move on to Step 2, which involves processing the resources I just extracted – and it needs to be done in parallel.

According to the workflow instructions, I've got to run `process_local_files`, `scrape_and_clean_other_urls`, `process_github_urls`, and `transcribe_youtube_urls` simultaneously.

I've got the output from `extract_guidelines_urls`, which tells me a few key things: there's 1 GitHub source, no YouTube sources, 9 web sources, and no local files. And the `scrape_and_clean_other_urls` step has already completed successfully, processing 7 out of those 9 web sources.

Since there are no local files and no YouTube sources, I can skip `process_local_files` and `transcribe_youtube_urls`. That simplifies things. It looks like the only thing left to do in parallel is to call `process_github_urls`. That seems like a reasonable and efficient execution plan. The research directory I'm working with is `/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_context_engineering`. Time to get started![0m


[1m[36m🔧 Function Call (Tool):[0m
[36m  Tool: [0m[1m[36mprocess_github_urls[0m
[36m  Arguments: [0m[36m{
  "research_directory": "/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_context_engineering"
}[0m

[36m⚡ Executing tool 'process_github_urls' via MCP server...[0m
[36m✅ Tool execution successful![0m

[1m[95m🤔 LLM's Thoughts:[0m
[35m**Moving to the Core Research Loop**

Okay, so the user's ready for the full workflow run. I've already handled the preliminary steps: extracting the guideline URLs and getting started on scraping and processing the web resources. Based on the outputs, I've got one GitHub URL done, seven out of nine "other" URLs processed.

My immediate focus now is completing step 2: fully processing those extracted resources. Luckily, it looks pretty straightforward. The `extract_guidelines_urls` tool confirmed no local files or YouTube URLs, so I can skip `process_local_files` and `transcribe_youtube_urls` entirely.

That means I'm free to wrap up step 2 and then kick off step 3: the critical research loop. Three rounds of `generate_next_queries` and `run_perplexity_research` are up next. It's time to dig into the main insights. Let's make this happen![0m


[1m[36m🔧 Function Call (Tool):[0m
[36m  Tool: [0m[1m[36mgenerate_next_queries[0m
[36m  Arguments: [0m[36m{
  "research_directory": "/Users/fabio/Desktop/course-ai-agents/lessons/research_agent_part_2/data/sample_context_engineering"
}[0m

[36m⚡ Executing tool 'generate_next_queries' via MCP server...[0m
[36m✅ Tool execution successful![0m

[1m[95m🤔 LLM's Thoughts:[0m
[35m**Next Steps in the Research Workflow**

Okay...
```


Once the client is running, you can:

1. **Start the complete workflow**: Type `/prompt/full_research_instructions_prompt` to load the complete research workflow.
2. **Provide the research directory**: Write something like `The research folder is /path/to/research_folder. Run the complete workflow from start to finish.` Remember to replace the path with the actual absolute path to your research folder.
3. **Examine the final output**: Check the generated `research.md` file.
4. **Terminate the client**: Type `/quit` after the agent completes all steps.

## 9. Using Cursor with the MCP Server

Our research agent can also be used directly within Cursor IDE through the MCP protocol. The `mcp_server` folder contains a `.mcp.json.sample` file that shows how to configure Cursor to use our research agent.

Here's the content of the `.mcp.json.sample` file:

```json
{
  "mcpServers": {
    "research-agent": {
      "transport": "stdio",
      "command": "uv",
      "args": [
        "--directory",
        "/Users/fabio/Desktop/course-agents-writing/src/nova/mcp_server",
        "run",
        "-m",
        "src.server",
        "--transport",
        "stdio"
      ]
    }
  }
}
```

To set this up:
1. In Cursor, click on "Cursor" in the top bar, then "Settings", then "Cursor Settings", then "MCP", and finally on "New MCP Server". Cursor will open a `mcp.json` file.
2. Update the `mcp.json` file as shown above. `"research-agent"` is the name of our MCP server that you are connecting Cursor to. You could also have other MCP servers defined in the same file.
3. Save the `mcp.json` file and restart Cursor. Then, make sure that in the "Cursor Settings" page you see the new "research-agent" MCP server and that it's active. If everything is working fine, it should show the amount of MCP tools, prompts and resources available.
4. Now, you can use the research agent directly within Cursor! Open a new chat in the AI Pane and write `/research-agent` to see the available MCP prompts. You can write `/research-agent/full_research_instructions_prompt` and send it in the chat to start the complete research workflow.

This integration allows you to conduct research directly within your development environment, making it easy to incorporate findings into your coding projects.

</details>


## Code Sources

_No code sources found._


## YouTube Video Transcripts

_No YouTube video transcripts found._


## Additional Sources Scraped

<details>
<summary>advanced-scraping-guide-firecrawl</summary>

This guide will walk you through the different endpoints of Firecrawl and how to use them fully with all its parameters.

## Basic scraping with Firecrawl

To scrape a single page and get clean markdown content, you can use the `/scrape` endpoint.

```
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

doc = firecrawl.scrape("https://firecrawl.dev")

print(doc.markdown)
```

## Scraping PDFs

Firecrawl supports PDFs. Use the `parsers` option (e.g., `parsers: ["pdf"]`) when you want to ensure PDF parsing.

## Scrape options

When using the `/scrape` endpoint, you can customize scraping with the options below.

### Formats (`formats`)

- **Type**: `array`
- **Strings**: `["markdown", "links", "html", "rawHtml", "summary", "images"]`
- **Object formats**:
  - JSON: `{ type: "json", prompt, schema }`
  - Screenshot: `{ type: "screenshot", fullPage?, quality?, viewport? }`
  - Change tracking: `{ type: "changeTracking", modes?, prompt?, schema?, tag? }` (requires `markdown`)
- **Default**: `["markdown"]`

### Full page content vs main content (`onlyMainContent`)

- **Type**: `boolean`
- **Description**: By default the scraper returns only the main content. Set to `false` to return full page content.
- **Default**: `true`

### Include tags (`includeTags`)

- **Type**: `array`
- **Description**: HTML tags/classes/ids to include in the scrape.

### Exclude tags (`excludeTags`)

- **Type**: `array`
- **Description**: HTML tags/classes/ids to exclude from the scrape.

### Wait for page readiness (`waitFor`)

- **Type**: `integer`
- **Description**: Milliseconds to wait before scraping (use sparingly).
- **Default**: `0`

### Freshness and cache (`maxAge`)

- **Type**: `integer` (milliseconds)
- **Description**: If a cached version of the page is newer than `maxAge`, Firecrawl returns it instantly; otherwise it scrapes fresh and updates the cache. Set `0` to always fetch fresh.
- **Default**: `172800000` (2 days)

### Request timeout (`timeout`)

- **Type**: `integer`
- **Description**: Max duration in milliseconds before aborting.
- **Default**: `30000` (30 seconds)

### PDF parsing (`parsers`)

- **Type**: `array`
- **Description**: Control parsing behavior. To parse PDFs, set `parsers: ["pdf"]`.

### Actions (`actions`)

When using the /scrape endpoint, Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.

- **Type**: `array`
- **Description**: Sequence of browser steps to run before scraping.
- **Supported actions**:
  - `wait``{ milliseconds }`
  - `click``{ selector }`
  - `write``{ selector, text }`
  - `press``{ key }`
  - `scroll``{ direction: "up" | "down" }`
  - `scrape``{ selector }` (scrape a sub-element)
  - `executeJavascript``{ script }`
  - `pdf` (trigger PDF render in some flows)

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key='fc-YOUR-API-KEY')

doc = firecrawl.scrape('https://example.com', {
  actions: [\
    { type: 'wait', milliseconds: 1000 },\
    { type: 'click', selector: '#accept' },\
    { type: 'scroll', direction: 'down' },\
    { type: 'write', selector: '#q', text: 'firecrawl' },\
    { type: 'press', key: 'Enter' }\
  ],
  formats: ['markdown']
})

print(doc.markdown)
```

### Example Usage

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
    -H '
    Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "formats": [\
        "markdown",\
        "links",\
        "html",\
        "rawHtml",\
        { "type": "screenshot", "fullPage": true, "quality": 80 }\
      ],
      "includeTags": ["h1", "p", "a", ".main-content"],
      "excludeTags": ["#ad", "#footer"],
      "onlyMainContent": false,
      "waitFor": 1000,
      "timeout": 15000,
      "parsers": ["pdf"]
    }'
```

In this example, the scraper will:

- Return the full page content as markdown.
- Include the markdown, raw HTML, HTML, links, and a screenshot in the response.
- Include only the HTML tags `<h1>`, `<p>`, `<a>`, and elements with the class `.main-content`, while excluding any elements with the IDs `#ad` and `#footer`.
- Wait for 1000 milliseconds (1 second) before scraping to allow the page to load.
- Set the maximum duration of the scrape request to 15000 milliseconds (15 seconds).
- Parse PDFs explicitly via `parsers: ["pdf"]`.

Here is the API Reference: [Scrape Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)

## JSON extraction via formats

Use the JSON format object in `formats` to extract structured data in one pass:

```
curl -X POST https://api.firecrawl.dev/v2/scrape \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://firecrawl.dev",
    "formats": [{\
      "type": "json",\
      "prompt": "Extract the features of the product",\
      "schema": {"type": "object", "properties": {"features": {"type": "object"}}, "required": ["features"]}\
    }]
  }'
```

## Extract endpoint

Use the dedicated extract job API when you want asynchronous extraction with status polling.

```
import Firecrawl from '@mendable/firecrawl-js';

const firecrawl = new Firecrawl({ apiKey: 'fc-YOUR-API-KEY' });

// Start extract job
const started = await firecrawl.startExtract({
  urls: ['https://docs.firecrawl.dev'],
  prompt: 'Extract title',
  schema: { type: 'object', properties: { title: 'string' }, required: ['title'] }
});

// Poll status
const status = await firecrawl.getExtractStatus(started.id);
console.log(status.status, status.data);
```

## Crawling multiple pages

To crawl multiple pages, use the `/v2/crawl` endpoint.

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

Returns an id

```
{ "id": "1234-5678-9101" }
```

### Check Crawl Job

Used to check the status of a crawl job and get its result.

```
curl -X GET https://api.firecrawl.dev/v2/crawl/1234-5678-9101 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY'
```

#### Pagination/Next URL

If the content is larger than 10MB or if the crawl job is still running, the response may include a `next` parameter, a URL to the next page of results.

### Crawl prompt and params preview

You can provide a natural-language `prompt` to let Firecrawl derive crawl settings. Preview them first:

```
curl -X POST https://api.firecrawl.dev/v2/crawl/params-preview \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer fc-YOUR-API-KEY' \
  -d '{
    "url": "https://docs.firecrawl.dev",
    "prompt": "Extract docs and blog"
  }'
```

### Crawler options

When using the `/v2/crawl` endpoint, you can customize the crawling behavior with:

#### includePaths

- **Type**: `array`
- **Description**: Regex patterns to include.
- **Example**: `["^/blog/.*$", "^/docs/.*$"]`

#### excludePaths

- **Type**: `array`
- **Description**: Regex patterns to exclude.
- **Example**: `["^/admin/.*$", "^/private/.*$"]`

#### maxDiscoveryDepth

- **Type**: `integer`
- **Description**: Max discovery depth for finding new URLs.

#### limit

- **Type**: `integer`
- **Description**: Max number of pages to crawl.
- **Default**: `10000`

#### crawlEntireDomain

- **Type**: `boolean`
- **Description**: Explore across siblings/parents to cover the entire domain.
- **Default**: `false`

#### allowExternalLinks

- **Type**: `boolean`
- **Description**: Follow links to external domains.
- **Default**: `false`

#### allowSubdomains

- **Type**: `boolean`
- **Description**: Follow subdomains of the main domain.
- **Default**: `false`

#### delay

- **Type**: `number`
- **Description**: Delay in seconds between scrapes.
- **Default**: `undefined`

#### scrapeOptions

- **Type**: `object`
- **Description**: Options for the scraper (see Formats above).
- **Example**: `{ "formats": ["markdown", "links", {"type": "screenshot", "fullPage": true}], "includeTags": ["h1", "p", "a", ".main-content"], "excludeTags": ["#ad", "#footer"], "onlyMainContent": false, "waitFor": 1000, "timeout": 15000}`
- **Defaults**: `formats: ["markdown"]`, caching enabled by default (maxAge ~ 2 days)

### Example Usage

```
curl -X POST https://api.firecrawl.dev/v2/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "includePaths": ["^/blog/.*$", "^/docs/.*$"],
      "excludePaths": ["^/admin/.*$", "^/private/.*$"],
      "maxDiscoveryDepth": 2,
      "limit": 1000
    }'
```

## Mapping website links

The `/v2/map` endpoint identifies URLs related to a given website.

### Usage

```
curl -X POST https://api.firecrawl.dev/v2/map \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer fc-YOUR-API-KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev"
    }'
```

### Map Options

#### search

- **Type**: `string`
- **Description**: Filter links containing text.

#### limit

- **Type**: `integer`
- **Description**: Maximum number of links to return.
- **Default**: `100`

#### sitemap

- **Type**: `"only" | "include" | "skip"`
- **Description**: Control sitemap usage during mapping.
- **Default**: `"include"`

#### includeSubdomains

- **Type**: `boolean`
- **Description**: Include subdomains of the website.
- **Default**: `true`

Here is the API Reference for it: [Map Endpoint Documentation](https://docs.firecrawl.dev/api-reference/endpoint/map)

</details>

<details>
<summary>gitingest</summary>

The provided markdown content is an advertisement/self-promotion for "gitingest," a tool for turning Git repositories into text digests for LLMs. This content is entirely irrelevant to the core subject of Lesson 19, which focuses on completing a research agent with quality control, compilation, and specific MCP tools. Therefore, all of the content should be removed.

</details>

<details>
<summary>mcp-json-configuration-fastmcp-fastmcp</summary>

## MCP JSON Configuration Standard

The MCP JSON configuration format is an **emergent standard** that has developed across the MCP ecosystem. This format defines how MCP clients should configure and launch MCP servers, providing a consistent way to specify server commands, arguments, and environment variables.

### Configuration Structure

The standard uses a `mcpServers` object where each key represents a server name and the value contains the server’s configuration:

```
{
  "mcpServers": {
    "server-name": {
      "command": "executable",
      "args": ["arg1", "arg2"],
      "env": {
        "VAR": "value"
      }
    }
  }
}
```

### Server Configuration Fields

#### `command` (required)

The executable command to run the MCP server. This should be an absolute path or a command available in the system PATH.

```
{
  "command": "python"
}
```

#### `args` (optional)

An array of command-line arguments passed to the server executable. Arguments are passed in order.

```
{
  "args": ["server.py", "--verbose", "--port", "8080"]
}
```

#### `env` (optional)

An object containing environment variables to set when launching the server. All values must be strings.

```
{
  "env": {
    "API_KEY": "secret-key",
    "DEBUG": "true",
    "PORT": "8080"
  }
}
```

### Client Adoption

This format is widely adopted across the MCP ecosystem:

- **Claude Desktop**: Uses `~/.claude/claude_desktop_config.json`
- **Cursor**: Uses `~/.cursor/mcp.json`
- **VS Code**: Uses workspace `.vscode/mcp.json`
- **Other clients**: Many MCP-compatible applications follow this standard

## Overview

**For the best experience, use FastMCP’s first-class integrations:** [`fastmcp install claude-code`](https://gofastmcp.com/integrations/claude-code), [`fastmcp install claude-desktop`](https://gofastmcp.com/integrations/claude-desktop), or [`fastmcp install cursor`](https://gofastmcp.com/integrations/cursor). Use MCP JSON generation for advanced use cases and unsupported clients.

The `fastmcp install mcp-json` command generates configuration in the standard `mcpServers` format used across the MCP ecosystem. This is useful when:

- **Working with unsupported clients** - Any MCP client not directly integrated with FastMCP
- **CI/CD environments** - Automated configuration generation for deployments
- **Configuration sharing** - Easy distribution of server setups to team members
- **Custom tooling** - Integration with your own MCP management tools
- **Manual setup** - When you prefer to manually configure your MCP client

## Basic Usage

Generate configuration and output to stdout (useful for piping):

```
fastmcp install mcp-json server.py
```

This outputs the server configuration JSON with the server name as the root key:

```
{
  "My Server": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "fastmcp",
      "run",
      "/absolute/path/to/server.py"
    ]
  }
}
```

To use this in a client configuration file, add it to the `mcpServers` object in your client’s configuration:

```
{
  "mcpServers": {
    "My Server": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "/absolute/path/to/server.py"
      ]
    }
  }
}
```

When using `--python`, `--project`, or `--with-requirements`, the generated configuration will include these options in the `uv run` command, ensuring your server runs with the correct Python version and dependencies.

Different MCP clients may have specific configuration requirements or formatting needs. Always consult your client’s documentation to ensure proper integration.

## Configuration Options

### Server Naming

```
# Use server's built-in name (from FastMCP constructor)
fastmcp install mcp-json server.py

# Override with custom name
fastmcp install mcp-json server.py --name "Custom Server Name"
```

### Dependencies

Add Python packages your server needs:

```
# Single package
fastmcp install mcp-json server.py --with pandas

# Multiple packages
fastmcp install mcp-json server.py --with pandas --with requests --with httpx

# Editable local package
fastmcp install mcp-json server.py --with-editable ./my-package

# From requirements file
fastmcp install mcp-json server.py --with-requirements requirements.txt
```

You can also use a `fastmcp.json` configuration file (recommended):

fastmcp.json

```
{
  "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
  "source": {
    "path": "server.py",
    "entrypoint": "mcp"
  },
  "environment": {
    "dependencies": ["pandas", "matplotlib", "seaborn"]
  }
}
```

Then simply install with:

```
fastmcp install mcp-json fastmcp.json
```

### Environment Variables

```
# Individual environment variables
fastmcp install mcp-json server.py \
  --env API_KEY=your-secret-key \
  --env DEBUG=true

# Load from .env file
fastmcp install mcp-json server.py --env-file .env
```

### Python Version and Project Directory

Specify Python version or run within a specific project:

```
# Use specific Python version
fastmcp install mcp-json server.py --python 3.11

# Run within a project directory
fastmcp install mcp-json server.py --project /path/to/project
```

### Server Object Selection

Use the same `file.py:object` notation as other FastMCP commands:

```
# Auto-detects server object (looks for 'mcp', 'server', or 'app')
fastmcp install mcp-json server.py

# Explicit server object
fastmcp install mcp-json server.py:my_custom_server
```

## Clipboard Integration

Copy configuration directly to your clipboard for easy pasting:

```
fastmcp install mcp-json server.py --copy
```

The `--copy` flag requires the `pyperclip` Python package. If not installed, you’ll see an error message with installation instructions.

## Usage Examples

### Basic Server

```
fastmcp install mcp-json dice_server.py
```

Output:

```
{
  "Dice Server": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "fastmcp",
      "run",
      "/home/user/dice_server.py"
    ]
  }
}
```

### Production Server with Dependencies

```
fastmcp install mcp-json api_server.py \
  --name "Production API Server" \
  --with requests \
  --with python-dotenv \
  --env API_BASE_URL=https://api.example.com \
  --env TIMEOUT=30
```

### Advanced Configuration

```
fastmcp install mcp-json ml_server.py \
  --name "ML Analysis Server" \
  --python 3.11 \
  --with-requirements requirements.txt \
  --project /home/user/ml-project \
  --env GPU_DEVICE=0
```

Output:

```
{
  "Production API Server": {
    "command": "uv",
    "args": [
      "run",
      "--with",
      "fastmcp",
      "--with",
      "python-dotenv",
      "--with",
      "requests",
      "fastmcp",
      "run",
      "/home/user/api_server.py"
    ],
    "env": {
      "API_BASE_URL": "https://api.example.com",
      "TIMEOUT": "30"
    }
  }
}
```

The advanced configuration example generates:

```
{
  "ML Analysis Server": {
    "command": "uv",
    "args": [
      "run",
      "--python",
      "3.11",
      "--project",
      "/home/user/ml-project",
      "--with",
      "fastmcp",
      "--with-requirements",
      "requirements.txt",
      "fastmcp",
      "run",
      "/home/user/ml_server.py"
    ],
    "env": {
      "GPU_DEVICE": "0"
    }
  }
}
```

### Pipeline Usage

Save configuration to file:

```
fastmcp install mcp-json server.py > mcp-config.json
```

Use in shell scripts:

```
#!/bin/bash
CONFIG=$(fastmcp install mcp-json server.py --name "CI Server")
echo "$CONFIG" | jq '."CI Server".command'
# Output: "uv"
```

## Integration with MCP Clients

The generated configuration works with any MCP-compatible application:

### Claude Desktop

**Prefer [`fastmcp install claude-desktop`](https://gofastmcp.com/integrations/claude-desktop)** for automatic installation. Use MCP JSON for advanced configuration needs.

Copy the `mcpServers` object into `~/.claude/claude_desktop_config.json`

### Cursor

**Prefer [`fastmcp install cursor`](https://gofastmcp.com/integrations/cursor)** for automatic installation. Use MCP JSON for advanced configuration needs.

Add to `~/.cursor/mcp.json`

### VS Code

Add to your workspace’s `.vscode/mcp.json` file

### Custom Applications

Use the JSON configuration with any application that supports the MCP protocol

## Configuration Format

The generated configuration outputs a server object with the server name as the root key:

```
{
  "<server-name>": {
    "command": "<executable>",
    "args": ["<arg1>", "<arg2>", "..."],
    "env": {
      "<ENV_VAR>": "<value>"
    }
  }
}
```

To use this in an MCP client, add it to the client’s `mcpServers` configuration object.**Fields:**

- `command`: The executable to run (always `uv` for FastMCP servers)
- `args`: Command-line arguments including dependencies and server path
- `env`: Environment variables (only included if specified)

**All file paths in the generated configuration are absolute paths**. This ensures the configuration works regardless of the working directory when the MCP client starts the server.

## Requirements

- **uv**: Must be installed and available in your system PATH
- **pyperclip** (optional): Required only for `--copy` functionality

Install uv if not already available:

```
# macOS
brew install uv

# Linux/Windows
curl -LsSf https://astral.sh/uv/install.sh | sh
```

</details>

<details>
<summary>model-context-protocol-mcp-cursor-docs</summary>

# Model Context Protocol (MCP)

## What is MCP?

Model Context Protocol (MCP) enables Cursor to connect to external tools and data sources.

## Servers

Browse available MCP servers. Click "Add to Cursor" to install them directly.

Filters

| Name | Install | Description |
| --- | --- | --- |
| Notion | [Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=Notion&config=eyJ1cmwiOiJodHRwczovL21jcC5ub3Rpb24uY29tL21jcCJ9) | All-in-one workspace for notes, docs, and project management. |
| Figma | [Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=Figma&config=eyJ1cmwiOiJodHRwczovL21jcC5maWdtYS5jb20vbWNwIn0%3D) | Design and collaboration platform for teams. |
| Linear | [Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=Linear&config=eyJ1cmwiOiJodHRwczovL21jcC5saW5lYXIuYXBwL3NzZSJ9) | Issue tracking and project management for development teams. |
| Playwright | [Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=Playwright&config=eyJjb21tYW5kIjoibnB4IC15IEBwbGF5d3JpZ2h0L21jcEBsYXRlc3QifQ%3D%3D) | End-to-end browser testing. |
| Sentry | [Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=Sentry&config=eyJ1cmwiOiJodHRwczovL21jcC5zZW50cnkuZGV2L21jcCJ9) | Error tracking and performance monitoring. |

Show more servers

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

### One-click installation

Install MCP servers from our collection and authenticate with OAuth.

[Browse MCP Tools
Browse available MCP servers](https://cursor.com/docs/context/mcp/directory) [Add to Cursor Button
Create an "Add to Cursor" button](https://cursor.com/docs/context/mcp/install-links)

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

### Using the Extension API

For programmatic MCP server registration, Cursor provides an extension API that allows dynamic configuration without modifying `mcp.json` files. This is particularly useful for enterprise environments and automated setup workflows.

[MCP Extension API Reference
Learn how to register MCP servers programmatically using
`vscode.cursor.mcp.registerServer()`](https://cursor.com/docs/context/mcp-extension-api)

### Configuration locations

Project Configuration

Create `.cursor/mcp.json` in your project for project-specific tools.

Global Configuration

Create `~/.cursor/mcp.json` in your home directory for tools available everywhere.

### Config interpolation

Use variables in `mcp.json` values. Cursor resolves variables in these fields: `command`, `args`, `env`, `url`, and `headers`.

Supported syntax:

- `${env:NAME}` environment variables
- `${userHome}` path to your home folder
- `${workspaceFolder}` project root (the folder that contains `.cursor/mcp.json`)
- `${workspaceFolderBasename}` name of the project root
- `${pathSeparator}` and `${/}` OS path separator

Examples

```
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": ["${workspaceFolder}/tools/mcp_server.py"],
      "env": {
        "API_KEY": "${env:API_KEY}"
      }
    }
  }
}
```

```
{
  "mcpServers": {
    "remote-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:MY_SERVICE_TOKEN}"
      }
    }
  }
}
```

### Authentication

MCP servers use environment variables for authentication. Pass API keys and tokens through the config.

Cursor supports OAuth for servers that require it.

## Using MCP in chat

The Composer Agent automatically uses MCP tools listed under `Available Tools` when relevant. Ask for a specific tool by name or describe what you need. Enable or disable tools from settings.

### Toggling tools

Enable or disable MCP tools directly from the chat interface. Click a tool name in the tools list to toggle it. Disabled tools won't be loaded into context or available to Agent.

### Tool approval

Agent asks for approval before using MCP tools by default. Click the arrow next to the tool name to see arguments.

https://cursor.com/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fcontext%2Fmcp%2Ftool-confirm.png&w=1920&q=75

#### Auto-run

Enable auto-run for Agent to use MCP tools without asking. Works like terminal commands. Read more about Auto-run settings [here](https://cursor.com/docs/agent/tools#auto-run).

### Tool response

Cursor shows the response in chat with expandable views of arguments and responses:

https://cursor.com/docs-static/_next/image?url=%2Fdocs-static%2Fimages%2Fcontext%2Fmcp%2Ftool-call.png&w=1920&q=75

### Images as context

MCP servers can return images - screenshots, diagrams, etc. Return them as base64 encoded strings:

```
const RED_CIRCLE_BASE64 = "/9j/4AAQSkZJRgABAgEASABIAAD/2w...";
// ^ full base64 clipped for readability

server.tool("generate_image", async (params) => {
  return {
    content: [\
      {\
        type: "image",\
        data: RED_CIRCLE_BASE64,\
        mimeType: "image/jpeg",\
      },\
    ],
  };
});
```

See this [example server](https://github.com/msfeldstein/mcp-test-servers/blob/main/src/image-server.js) for implementation details. Cursor attaches returned images to the chat. If the model supports images, it analyzes them.

## Security considerations

When installing MCP servers, consider these security practices:

- **Verify the source**: Only install MCP servers from trusted developers and repositories
- **Review permissions**: Check what data and APIs the server will access
- **Limit API keys**: Use restricted API keys with minimal required permissions
- **Audit code**: For critical integrations, review the server's source code

Remember that MCP servers can access external services and execute code on your behalf. Always understand what a server does before installation.

## Real-world examples

For practical examples of MCP in action, see our [Web Development guide](https://cursor.com/docs/cookbook/web-development) which demonstrates integrating Linear, Figma, and browser tools into your development workflow.

## FAQ

### What's the point of MCP servers?

### How do I debug MCP server issues?

### Can I temporarily disable an MCP server?

### What happens if an MCP server crashes or times out?

### How do I update an MCP server?

### Can I use MCP servers with sensitive data?

</details>

<details>
<summary>model-context-protocol-mcp-openai-agents-sdk</summary>

```markdown
# Model context protocol (MCP)

The [Model context protocol](https://modelcontextprotocol.io/introduction) (MCP) standardises how applications expose tools and context to language models. From the official documentation:

> MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.

The Agents Python SDK understands multiple MCP transports. This lets you reuse existing MCP servers or build your own to expose filesystem, HTTP, or connector backed tools to an agent.

## Choosing an MCP integration

Before wiring an MCP server into an agent decide where the tool calls should execute and which transports you can reach. The matrix below summarises the options that the Python SDK supports.

| What you need | Recommended option |
| --- | --- |
| Let OpenAI's Responses API call a publicly reachable MCP server on the model's behalf | **Hosted MCP server tools** via [`HostedMCPTool`](https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.HostedMCPTool "HostedMCPTool            dataclass   ") |
| Connect to Streamable HTTP servers that you run locally or remotely | **Streamable HTTP MCP servers** via [`MCPServerStreamableHttp`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStreamableHttp "MCPServerStreamableHttp") |
| Talk to servers that implement HTTP with Server-Sent Events | **HTTP with SSE MCP servers** via [`MCPServerSse`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerSse "MCPServerSse") |
| Launch a local process and communicate over stdin/stdout | **stdio MCP servers** via [`MCPServerStdio`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStdio "MCPServerStdio") |

The sections below walk through each option, how to configure it, and when to prefer one transport over another.

## 1\. Hosted MCP server tools

Hosted tools push the entire tool round-trip into OpenAI's infrastructure. Instead of your code listing and calling tools, the [`HostedMCPTool`](https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.HostedMCPTool "HostedMCPTool            dataclass   ") forwards a server label (and optional connector metadata) to the Responses API. The model lists the remote server's tools and invokes them without an extra callback to your Python process. Hosted tools currently work with OpenAI models that support the Responses API's hosted MCP integration.

### Basic hosted MCP tool

Create a hosted tool by adding a [`HostedMCPTool`](https://openai.github.io/openai-agents-python/ref/tool/#agents.tool.HostedMCPTool "HostedMCPTool            dataclass   ") to the agent's `tools` list. The `tool_config` dict mirrors the JSON you would send to the REST API:

```python
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

Hosted tools support streaming results in exactly the same way as function tools. Pass `stream=True` to `Runner.run_streamed` to consume incremental MCP output while the model is still working:

```python
result = Runner.run_streamed(agent, "Summarise this repository's top languages")
async for event in result.stream_events():
    if event.type == "run_item_stream_event":
        print(f"Received: {event.item}")
print(result.final_output)
```

### Optional approval flows

If a server can perform sensitive operations you can require human or programmatic approval before each tool execution. Configure `require_approval` in the `tool_config` with either a single policy (`"always"`, `"never"`) or a dict mapping tool names to policies. To make the decision inside Python, provide an `on_approval_request` callback.

```python
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

Hosted MCP also supports OpenAI connectors. Instead of specifying a `server_url`, supply a `connector_id` and an access token. The Responses API handles authentication and the hosted server exposes the connector's tools.

```python
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

Fully working hosted tool samples—including streaming, approvals, and connectors—live in [`examples/hosted_mcp`](https://github.com/openai/openai-agents-python/tree/main/examples/hosted_mcp).

## 2\. Streamable HTTP MCP servers

When you want to manage the network connection yourself, use [`MCPServerStreamableHttp`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStreamableHttp "MCPServerStreamableHttp"). Streamable HTTP servers are ideal when you control the transport or want to run the server inside your own infrastructure while keeping latency low.

```python
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

If the MCP server implements the HTTP with SSE transport, instantiate [`MCPServerSse`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerSse "MCPServerSse"). Apart from the transport, the API is identical to the Streamable HTTP server.

```python
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

For MCP servers that run as local subprocesses, use [`MCPServerStdio`](https://openai.github.io/openai-agents-python/ref/mcp/server/#agents.mcp.server.MCPServerStdio "MCPServerStdio"). The SDK spawns the process, keeps the pipes open, and closes them automatically when the context manager exits. This option is helpful for quick proofs of concept or when the server only exposes a command line entry point.

```python
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

Each MCP server supports tool filters so that you can expose only the functions that your agent needs. Filtering can happen at construction time or dynamically per run.

### Static tool filtering

Use [`create_static_tool_filter`](https://openai.github.io/openai-agents-python/ref/mcp/util/#agents.mcp.util.create_static_tool_filter "create_static_tool_filter") to configure simple allow/block lists:

```python
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

When both `allowed_tool_names` and `blocked_tool_names` are supplied the SDK applies the allow-list first and then removes any blocked tools from the remaining set.

### Dynamic tool filtering

For more elaborate logic pass a callable that receives a [`ToolFilterContext`](https://openai.github.io/openai-agents-python/ref/mcp/util/#agents.mcp.util.ToolFilterContext "ToolFilterContext            dataclass   "). The callable can be synchronous or asynchronous and returns `True` when the tool should be exposed.

```python
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

MCP servers can also provide prompts that dynamically generate agent instructions. Servers that support prompts expose two methods:

- `list_prompts()` enumerates the available prompt templates.
- `get_prompt(name, arguments)` fetches a concrete prompt, optionally with parameters.

```python
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

Every agent run calls `list_tools()` on each MCP server. Remote servers can introduce noticeable latency, so all of the MCP server classes expose a `cache_tools_list` option. Set it to `True` only if you are confident that the tool definitions do not change frequently. To force a fresh list later, call `invalidate_tools_cache()` on the server instance.
```

</details>

<details>
<summary>prompts-model-context-protocol</summary>

The Model Context Protocol (MCP) provides a standardized way for servers to expose prompt templates to clients. Prompts allow servers to provide structured messages and instructions for interacting with language models. Clients can discover available prompts, retrieve their contents, and provide arguments to customize them.

## User Interaction Model

Prompts are designed to be **user-controlled**, meaning they are exposed from servers to clients with the intention of the user being able to explicitly select them for use. Typically, prompts would be triggered through user-initiated commands in the user interface, which allows users to naturally discover and invoke available prompts.

For example, as slash commands:
https://mintcdn.com/mcp/4ZXF1PrDkEaJvXpn/specification/2025-06-18/server/slash-command.png?fit=max&auto=format&n=4ZXF1PrDkEaJvXpn&q=85&s=7f003e36d881dd6f3e5b8cbdd85e5ca5

However, implementors are free to expose prompts through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.

## Capabilities

Servers that support prompts **MUST** declare the `prompts` capability during initialization:

```
{
  "capabilities": {
    "prompts": {
      "listChanged": true
    }
  }
}
```

`listChanged` indicates whether the server will emit notifications when the list of available prompts changes.

## Protocol Messages

### Listing Prompts

To retrieve available prompts, clients send a `prompts/list` request. This operation supports pagination.

**Request:**

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

### Getting a Prompt

To retrieve a specific prompt, clients send a `prompts/get` request. Arguments may be auto-completed through the completion API.

**Request:**

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

### List Changed Notification

When the list of available prompts changes, servers that declared the `listChanged` capability **SHOULD** send a notification:

```
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

## Message Flow

ServerClientServerClientDiscoveryUsageChangesopt\[listChanged\]prompts/listList of promptsprompts/getPrompt contentprompts/list\_changedprompts/listUpdated prompts

## Data Types

### Prompt

A prompt definition includes:

- `name`: Unique identifier for the prompt
- `title`: Optional human-readable name of the prompt for display purposes.
- `description`: Optional human-readable description
- `arguments`: Optional list of arguments for customization

### PromptMessage

Messages in a prompt can contain:

- `role`: Either “user” or “assistant” to indicate the speaker
- `content`: One of the following content types:

All content types in prompt messages support optional annotations for metadata about audience, priority, and modification times.

#### Text Content

Text content represents plain text messages:

```
{
  "type": "text",
  "text": "The text content of the message"
}
```

This is the most common content type used for natural language interactions.

#### Image Content

Image content allows including visual information in messages:

```
{
  "type": "image",
  "data": "base64-encoded-image-data",
  "mimeType": "image/png"
}
```

The image data **MUST** be base64-encoded and include a valid MIME type. This enables multi-modal interactions where visual context is important.

#### Audio Content

Audio content allows including audio information in messages:

```
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}
```

The audio data MUST be base64-encoded and include a valid MIME type. This enables multi-modal interactions where audio context is important.

#### Embedded Resources

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

Embedded resources enable prompts to seamlessly incorporate server-managed content like documentation, code samples, or other reference materials directly into the conversation flow.

## Error Handling

Servers **SHOULD** return standard JSON-RPC errors for common failure cases:

- Invalid prompt name: `-32602` (Invalid params)
- Missing required arguments: `-32602` (Invalid params)
- Internal errors: `-32603` (Internal error)

## Implementation Considerations

1. Servers **SHOULD** validate prompt arguments before processing
2. Clients **SHOULD** handle pagination for large prompt lists
3. Both parties **SHOULD** respect capability negotiation

## Security

Implementations **MUST** carefully validate all prompt inputs and outputs to prevent injection attacks or unauthorized access to resources.

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

```
# pip install firecrawl-py

from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")
```

### Usage

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
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}
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

## Interacting with the page with Actions

Firecrawl allows you to perform various actions on a web page before scraping its content. This is particularly useful for interacting with dynamic content, navigating through pages, or accessing content that requires user interaction.Here is an example of how to use actions to navigate to google.com, search for Firecrawl, click on the first result, and take a screenshot.It is important to almost always use the `wait` action before/after executing other actions to give enough time for the page to load.

### Example

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

doc = firecrawl.scrape(
    url="https://example.com/login",
    formats=["markdown"],
    actions=[
        {"type": "write", "text": "john@example.com"},
        {"type": "press", "key": "Tab"},
        {"type": "write", "text": "secret"},
        {"type": "click", "selector": 'button[type="submit"]'},
        {"type": "wait", "milliseconds": 1500},
        {"type": "screenshot", "fullPage": True},
    ],
)

print(doc.markdown, doc.screenshot)
```

### Output

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

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

doc = firecrawl.scrape('https://example.com',
    formats=['markdown'],
    location={
        'country': 'US',
        'languages': ['en']
    }
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

```
from firecrawl import Firecrawl
firecrawl = Firecrawl(api_key='fc-YOUR_API_KEY')

doc = firecrawl.scrape(url='https://example.com', maxAge=0, formats=['markdown'])
print(doc)
```

Example (use a 10-minute cache window):

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

```
from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")

job = firecrawl.batch_scrape([
    "https://firecrawl.dev",
    "https://docs.firecrawl.dev",
], formats=["markdown"], poll_interval=2, wait_timeout=120)

print(job)
```

### Response

If you’re using the sync methods from the SDKs, it will return the results of the batch scrape job. Otherwise, it will return a job ID that you can use to check the status of the batch scrape.

#### Synchronous

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
<summary>structured-outputs-guide-perplexity</summary>

## Overview

Structured outputs enable you to enforce specific response formats from Perplexity’s models, ensuring consistent, machine-readable data that can be directly integrated into your applications without manual parsing.We currently support two types of structured outputs: **JSON Schema** and **Regex**. LLM responses will work to match the specified format, except for the following cases:

- The output exceeds `max_tokens`

Enabling the structured outputs can be done by adding a `response_format` field in the request:**JSON Schema**

- `response_format: { type: "json_schema", json_schema: {"schema": object} }` .
- The schema should be a valid JSON schema object.

**Regex** (only available for `sonar` right now)

- `response_format: { type: "regex", regex: {"regex": str} }` .
- The regex is a regular expression string.

**Improve Schema Compliance**: Give the LLM some hints about the output format in your prompts to improve adherence to the structured format.For example, include phrases like “Please return the data as a JSON object with the following structure…” or “Extract the information and format it as specified in the schema.”

The first request with a new JSON Schema or Regex expects to incur delay on the first token. Typically, it takes 10 to 30 seconds to prepare the new schema, and may result in timeout errors. Once the schema has been prepared, the subsequent requests will not see such delay.

## Examples

### 1\. Financial Analysis with JSON Schema

Python

TypeScript

cURL

Copy

Ask AI

```
from perplexity import Perplexity
from typing import List, Optional
from pydantic import BaseModel

class FinancialMetrics(BaseModel):
    company: str
    quarter: str
    revenue: float
    net_income: float
    eps: float
    revenue_growth_yoy: Optional[float] = None
    key_highlights: Optional[List[str]] = None

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar-pro",
    messages=[\
        {\
            "role": "user",\
            "content": "Analyze the latest quarterly earnings report for Apple Inc. Extract key financial metrics."\
        }\
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "schema": FinancialMetrics.model_json_schema()
        }
    }
)

metrics = FinancialMetrics.model_validate_json(completion.choices[0].message.content)
print(f"Revenue: ${metrics.revenue}B")
```

### 2\. Extract Contact Information with Regex

Python

TypeScript

cURL

Copy

Ask AI

```
from perplexity import Perplexity

client = Perplexity()

completion = client.chat.completions.create(
    model="sonar",
    messages=[\
        {\
            "role": "user",\
            "content": "Find the direct email address for the investor relations contact at Tesla Inc."\
        }\
    ],
    response_format={
        "type": "regex",
        "regex": {
            "regex": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        }
    }
)

email = completion.choices[0].message.content
print(f"Investor Relations Email: {email}")
```

## Best Practices

### Generating responses in a JSON Format

For Python users, we recommend using the Pydantic library to [generate JSON schema](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema).**Unsupported JSON Schemas**Recursive JSON schema is not supported. As a result of that, unconstrained objects are not supported either. Here’s a few example of unsupported schemas:

Copy

Ask AI

```
# UNSUPPORTED!

from typing import Any

class UnconstrainedDict(BaseModel):
   unconstrained: dict[str, Any]

class RecursiveJson(BaseModel):
   value: str
   child: list["RecursiveJson"]
```

**Links in JSON Responses**: Requesting links as part of a JSON response may not always work reliably and can result in hallucinations or broken links. Models may generate invalid URLs when forced to include links directly in structured outputs.To ensure all links are valid, use the links returned in the `citations` or `search_results` fields from the API response. Never count on the model to return valid links directly as part of the JSON response content.

### Generating responses using a regex

**Supported Regex**

- Characters: `\d`, `\w`, `\s` , `.`
- Character classes: `[0-9A-Fa-f]` , `[^x]`
- Quantifiers: `*`, `?` , `+`, `{3}`, `{2,4}` , `{3,}`
- Alternation: `|`
- Group: `( ... )`
- Non-capturing group: `(?: ... )`

**Unsupported Regex**

- Contents of group: `\1`
- Anchors: `^`, `$`, `\b`
- Positive lookahead: `(?= ... )`
- Negative lookahead: `(?! ... )`
- Positive look-behind: `(?<= ... )`
- Negative look-behind: `(?<! ... )`
- Recursion: `(?R)`

## Perplexity’s JSON Schema Implementation

Perplexity’s structured outputs implementation has several key differences compared to other providers:

### Simplified Schema Definition

- **Optional naming**: Unlike other providers that require explicit schema names, Perplexity automatically handles schema naming with sensible defaults
- **Flexible strictness**: Schema validation is handled automatically without requiring manual strictness configuration
- **Streamlined syntax**: You only need to provide the core schema object without additional wrapper fields

**Other Providers:**

Copy

Ask AI

```
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "financial_data",
      "strict": true,
      "schema": { /* your schema */ }
    }
  }
}
```

**Perplexity:**

Copy

Ask AI

```
{
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "schema": { /* your schema */ }
    }
  }
}
```

### Enhanced Error Handling

- **Clear error messages**: When schemas fail validation, you’ll receive specific, actionable error messages
- **Recursion protection**: Built-in safeguards prevent infinite recursion in complex nested schemas
- **Constraint validation**: Automatic detection and clear messaging for unsupported features like unconstrained objects

### Schema Compatibility

While Perplexity supports standard JSON Schema syntax, some advanced features may not be available:

- Recursive schemas are not supported for performance and reliability reasons
- Unconstrained objects (like `dict[str, Any]`) are automatically detected and rejected
- Complex reference patterns may require simplification

This approach prioritizes reliability and performance while maintaining compatibility with most common JSON Schema use cases.

## Structured Outputs for Reasoning Models

When using structured outputs with reasoning models like `sonar-reasoning-pro`, the response will include a `<think>` section containing reasoning tokens, immediately followed by the structured output. The `response_format` parameter does not remove these reasoning tokens from the output, so the final response will need to be parsed manually.**Sample Response:**

Copy

Ask AI

```
<think>
I need to provide information about France in a structured JSON format with specific fields: country, capital, population, official_language.

For France:
- Country: France
- Capital: Paris
- Population: About 67 million (as of 2023)
- Official Language: French

Let me format this information as required.
</think>
{"country":"France","capital":"Paris","population":67750000,"official_language":"French"}
```

For a reusable implementation to extract JSON from reasoning model outputs, see our [example utility on GitHub](https://github.com/ppl-ai/api-discussion/blob/main/utils/extract_json_reasoning_models.py).

</details>

<details>
<summary>tools-model-context-protocol</summary>

The provided markdown content appears to be a technical specification document for the Model Context Protocol (MCP) regarding its tool features. While Lesson 19 uses and discusses MCP tools and server-hosted prompts, the lesson guidelines indicate a focus on *building and finishing a research agent* and *critiquing its outputs*. The lesson is about implementing specific MCP tools for research, running a workflow, and integrating HITL, not a deep dive into the *protocol specification* of how MCP tools work under the hood (e.g., JSON-RPC messages, data types for image/audio content, detailed error handling mechanisms of the protocol itself).

The guidelines state: "To not reintroduce concepts already taught in the previous lessons" and "To be careful when talking about concepts introduced only in future lessons". Lesson 16 covered "MCP foundations: server/client; **tools/resources/prompts**; server-hosted prompts; discovery; thin orchestration over heavy tools." This implies that the basic understanding of what tools are within MCP has already been established. The current content is a detailed *specification* of the `tools` capability within MCP, which is too granular and theoretical for a lesson focused on *finishing and hardening a research agent* (30% theory – 70% hands‑on). The lesson is about *using* the MCP framework, not documenting its internal protocol.

Therefore, this entire content is considered irrelevant as it delves into the low-level specification of the MCP protocol rather than the application of MCP tools within the research agent workflow.

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

- [Upload a video file](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#upload-video) using the File API before making a
request to `generateContent`. Use this method for files larger than 20MB, videos
longer than approximately 1 minute, or when you want to reuse the file across
multiple requests.
- [Pass inline video data](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#inline-video) with the request to `generateContent`. Use this method for smaller files (<20MB) and shorter durations.
- [Pass YouTube URLs](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#youtube) as part of your `generateContent` request.

### Upload a video file

You can use the [Files API](https://ai.google.dev/gemini-api/docs/files) to upload a video file.
Always use the Files API when the total request size (including the file, text
prompt, system instructions, etc.) is larger than 20 MB, the video duration is
significant, or if you intend to use the same video in multiple prompts.
The File API accepts video file formats directly.

The following code downloads the sample video, uploads it using the File API,
waits for it to be processed, and then uses the file reference in
a `generateContent` request.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#rest)More

```
from google import genai

client = genai.Client()

myfile = client.files.upload(file="path/to/sample.mp4")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=[myfile, "Summarize this video. Then create a quiz with an answer key based on the information in this video."]
)

print(response.text)
```

To learn more about working with media files, see
[Files API](https://ai.google.dev/gemini-api/docs/files).

### Pass video data inline

Instead of uploading a video file using the File API, you can pass smaller
videos directly in the request to `generateContent`. This is suitable for
shorter videos under 20MB total request size.

Here's an example of providing inline video data:

[Python](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#javascript)[REST](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#rest)More

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

### Pass YouTube URLs

You can pass YouTube URLs directly to Gemini API as part of your `generateContent`request as follows:

[Python](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#rest)More

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

**Limitations:**

- For the free tier, you can't upload more than 8 hours of YouTube video per day.
- For the paid tier, there is no limit based on video length.
- For models prior to Gemini 2.5, you can upload only 1 video per request. For Gemini 2.5 and later models, you can upload a maximum of 10 videos per request.
- You can only upload public videos (not private or unlisted videos).

## Refer to timestamps in the content

You can ask questions about specific points in time within the video using
timestamps of the form `MM:SS`.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#rest)More

```
prompt = "What are the examples given at 00:05 and 00:10 supposed to show us?" # Adjusted timestamps for the NASA video
```

## Extract detailed insights from video

Gemini models offer powerful capabilities for understanding video content by
processing information from both the audio and visual streams. This lets you
extract a rich set of details, including generating descriptions of what is
happening in a video and answering questions about its content. For visual
descriptions, the model samples the video at a rate of **1 frame per second**.
This sampling rate may affect the level of detail in the descriptions,
particularly for videos with rapidly changing visuals.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#javascript)[Go](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#go)[REST](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#rest)More

```
prompt = "Describe the key events in this video, providing both audio and visual details. Include timestamps for salient moments."
```

## Customize video processing

You can customize video processing in the Gemini API by setting clipping
intervals or providing custom frame rate sampling.

### Set clipping intervals

You can clip video by specifying `videoMetadata` with start and end offsets.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#python)[JavaScript](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#javascript)More

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

### Set a custom frame rate

You can set custom frame rate sampling by passing an `fps` argument to
`videoMetadata`.

[Python](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#python)More

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
  - You can override the 1 FPS sampling rate by [setting a custom frame rate](https://ai.google.dev/gemini-api/docs/video-understanding?utm_source=chatgpt.com#custom-frame-rate).
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
