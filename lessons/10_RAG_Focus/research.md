# Research

## Research Results

<details>
<summary>What are the latest production-ready architectures for agentic RAG systems using frameworks like LangGraph?</summary>

### Source [1]: https://qdrant.tech/documentation/agentic-rag-langgraph/

Query: What are the latest production-ready architectures for agentic RAG systems using frameworks like LangGraph?

Answer: This source presents a **production-ready architecture** for agentic Retrieval-Augmented Generation (RAG) systems using LangGraph, Qdrant, and supporting tools. The architecture consists of the following components:

- **AI Agent:** An agent orchestrated by LangGraph handles parsing queries, selecting tools, and integrating responses. OpenAI’s GPT-4o serves as the reasoning engine.
- **Embedding:** Queries are converted to embeddings using OpenAI’s `text-embedding-3-small` model.
- **Vector Database:** Qdrant serves as the vector store for embeddings, enabling efficient similarity searches.
- **LLM:** OpenAI’s GPT-4o is used for generating contextually grounded responses.
- **Search Tools:** The system enhances RAG by integrating real-time web search using the BraveSearchAPI, thereby enabling up-to-date information retrieval.
- **Workflow Management:** LangGraph orchestrates the entire process, managing workflow, tool selection, and execution sequences. This enables intelligent, flexible, and robust agentic workflows.

This stack enables efficient combination of retrieval, reasoning, and real-time search, managed through a graph-based workflow for flexible and robust agentic RAG systems.

-----

-----

-----

### Source [2]: https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/

Query: What are the latest production-ready architectures for agentic RAG systems using frameworks like LangGraph?

Answer: This source details the **key architectural features** for building advanced agentic RAG systems with LangGraph:

- **Custom Agent Architectures:** LangGraph allows highly customizable agent architectures beyond simple agent/router models.
- **Human-in-the-Loop:** Incorporates human feedback and approval steps for sensitive or high-stakes workflows, which can improve reliability.
- **Parallelization:** Supports concurrent processing of states and subtasks through the Send API, enabling map-reduce-like operations for efficiency in multi-agent or complex tasks.
- **Subgraphs:** Facilitates modularity and hierarchical design by letting developers define subgraphs for isolated agent teams, with controlled communication via overlapping state schema keys.
- **Reflection:** Integrates self-evaluation and iterative improvement mechanisms, allowing agents to evaluate their own outputs (e.g., task completion, correctness) and self-correct, leveraging both LLM-based and deterministic feedback.

By leveraging these features, developers can create sophisticated, production-ready agentic RAG systems tailored to complex, evolving requirements.

-----

-----

-----

### Source [3]: https://blog.lancedb.com/agentic-rag-using-langgraph-building-a-simple-customer-support-autonomous-agent/

Query: What are the latest production-ready architectures for agentic RAG systems using frameworks like LangGraph?

Answer: This source explains the **core mechanics** of building agentic RAG systems with LangGraph, highlighting the following elements:

- **Graph-Based Workflow:** The architecture is based on a graph where each node is a function that processes state, and edges define execution order.
- **State Management:** Uses Pydantic models or TypedDict to encapsulate variables and pass messages between nodes.
- **Tool Integration:** Tools are Python functions or models that the agent can call for retrieval, web search, calculations, or API calls.
- **Conditional Routing:** Supports dynamic workflows through conditional edges (routers), allowing decision-based transitions between nodes.
- **RAG Placement:** RAG can be implemented as either a tool or a dedicated node within the workflow. This enables more granular and conditional use of retrieval, depending on the context and requirements.

This approach allows for highly flexible and modular agentic RAG architectures where retrieval is deeply integrated into the agent’s reasoning and workflow.

-----

-----

-----

### Source [4]: https://www.youtube.com/watch?v=5TLQdNM5pHg

Query: What are the latest production-ready architectures for agentic RAG systems using frameworks like LangGraph?

Answer: In this presentation, Databricks showcases **advanced RAG agent architectures using LangGraph** for flow engineering:

- **Reliable Control Flows:** LangGraph enables the design of RAG agents that follow user-defined, deterministic control flows each time they are executed, enhancing reliability and reproducibility.
- **Debugging & Observability:** Integration with LangSmith allows detailed debugging and tracing of agent workflows, which is critical for production-readiness.
- **Composable Workflows:** The framework supports building RAG agents as composable graphs, where each step (retrieval, reasoning, tool invocation) is a node, and transitions are explicitly defined.
- **Production-Readiness:** Emphasizes the design of robust, traceable, and maintainable RAG systems suitable for enterprise deployment.

This approach ensures that agentic RAG systems are not only flexible and capable but also maintainable and auditable in production environments.

-----

-----

</details>

<details>
<summary>What are best practices for the ingestion pipeline in RAG, specifically regarding advanced chunking strategies and metadata enrichment?</summary>

### Source [6]: https://www.amazee.io/blog/post/data-pipelines-for-rag/

Query: What are best practices for the ingestion pipeline in RAG, specifically regarding advanced chunking strategies and metadata enrichment?

Answer: The ingestion stage in a RAG pipeline is critical for sourcing, preparing, and organizing external knowledge to feed into the system. Best practices include:
- **Data cleaning**: Remove extraneous elements such as headers, footers, code, and other non-informational content from raw data (webpages, documents, etc.). This ensures only necessary content is retained.
- Clean data improves the retrieval system and language model performance, resulting in more accurate and helpful information retrieval.
- The process should focus on including only the specific external data that supports the model, which provides helpful context and makes model responses more accurate and relevant.

These steps are foundational to building a reliable ingestion pipeline and should precede advanced chunking or metadata enrichment. Clean data maximizes the effectiveness of downstream chunking, retrieval, and generation processes.

-----

-----

-----

### Source [8]: https://lakefs.io/blog/what-is-rag-pipeline/

Query: What are best practices for the ingestion pipeline in RAG, specifically regarding advanced chunking strategies and metadata enrichment?

Answer: This source describes the ingestion pipeline as feeding raw, unstructured data from various sources (databases, documents, live feeds) into the system. Key best practices include:
- **Flexible document loading**: Use loaders (such as those in LangChain) to import and preprocess data from diverse formats (CSV, emails, Confluence, etc.).
- **Vector search index creation**: Transform and preprocess documents to build a trustworthy vector database filled with accurate and context-rich data.
- **Advanced optimization techniques** (though not chunking-specific): Improve retrieval by fine-tuning models, reformulating queries, and applying re-ranking algorithms to surface the most relevant context.

While advanced chunking strategies are not detailed, the emphasis is on robust preprocessing and transformation to maximize the relevance and accuracy of the resulting vector index.

-----

-----

-----

### Source [9]: https://aws.amazon.com/blogs/security/securing-the-rag-ingestion-pipeline-filtering-mechanisms/

Query: What are best practices for the ingestion pipeline in RAG, specifically regarding advanced chunking strategies and metadata enrichment?

Answer: Security considerations for the ingestion pipeline are crucial, particularly:
- **Content filtering**: Remove toxic language and personally identifiable information (PII) from ingest documents using tools like Amazon Comprehend.
- **Chunking for moderation**: Large documents may need to be split into smaller segments (chunks) to stay within API limits for toxicity and PII detection. This operationally enforces a chunking strategy where each chunk is appropriately sized for automated content moderation.
- **Responsible AI and security**: Apply both responsible AI principles and traditional security measures throughout the ingestion process to reduce the risk of harmful or inappropriate content entering the knowledge base.

This source highlights a practical chunking approach—splitting documents for moderation and compliance—which can be integrated into advanced chunking workflows alongside metadata enrichment.

-----

-----

</details>

<details>
<summary>How do query transformation techniques like multi-query, RAG-Fusion, and HyDE improve retrieval relevance in RAG systems?</summary>

### Source [10]: https://www.swiftorial.com/swiftlessons/rag/advanced-techniques/multi-query-rag

Query: How do query transformation techniques like multi-query, RAG-Fusion, and HyDE improve retrieval relevance in RAG systems?

Answer: **Multi-Query RAG** enhances retrieval relevance by leveraging multiple user queries or query variants to gather a broader and richer context for response generation. The process involves:
- **Query Acquisition:** Collecting multiple queries.
- **Information Retrieval:** Fetching relevant documents for each query.
- **Data Synthesis:** Synthesizing data from multiple retrievals into a coherent information set.
- **Output Generation:** Using a generative model to create responses based on the synthesized context.

This method increases the efficiency and contextual relevance of retrieved information because the system is not limited to a single query interpretation. By accessing multiple perspectives on the information need, it better covers ambiguities or gaps that a single query might miss. The main advantage is the provision of more accurate and meaningful responses, as the generative model has access to more comprehensive supporting data drawn from diverse angles.

Multi-Query RAG is model-agnostic and can be integrated with different generative models, provided those models can utilize external knowledge bases effectively. The technique ensures that the generative model outputs responses grounded in a wider selection of relevant information, which is particularly important for complex or nuanced queries.

-----

-----

-----

### Source [11]: https://docsbot.ai/article/advanced-rag-techniques-multiquery-and-rank-fusion

Query: How do query transformation techniques like multi-query, RAG-Fusion, and HyDE improve retrieval relevance in RAG systems?

Answer: **Multi-query retrieval** and **rank fusion** (often called RAG-Fusion) techniques directly address the challenge of retrieving highly relevant information for complex questions. Multi-query retrieval improves relevance by simultaneously searching with several query variants, increasing the likelihood of retrieving pertinent contexts, especially for nuanced or multifaceted questions.

**Rank fusion** further enhances relevance by amalgamating search results from different queries or sources (such as different databases or web searches). Techniques like **Reciprocal Rank Fusion** combine these retrieved results in a way that prioritizes the most consistently relevant documents across the different queries. This results in more precise and reliable information retrieval, as it integrates complementary evidence from multiple perspectives.

Together, these approaches create a more robust RAG system, better equipped to handle ambiguity and complexity in user queries, and yield more accurate, comprehensive, and contextually appropriate responses.

-----

-----

-----

### Source [12]: https://arxiv.org/html/2504.07104v1

Query: How do query transformation techniques like multi-query, RAG-Fusion, and HyDE improve retrieval relevance in RAG systems?

Answer: Traditional RAG systems focus on maximizing context relevance for retrieval, but **retrieving only the most "relevant" contexts can paradoxically degrade answer quality** by creating information bottlenecks. The paper introduces a method called **RErank BEyond reLevance (REBEL)**, which improves retrieval by introducing **multi-criteria optimization**—balancing both context relevance and answer quality.

REBEL leverages **Chain-of-Thought prompting** and, optionally, **Multi-Turn dialogue** at inference time. This enables the system to scale retrieval with available compute resources, allowing for a richer combination of candidate contexts that are not just topically relevant but also likely to improve the generated answer. The process thus provides a better trade-off between retrieval speed and downstream answer quality, ensuring that the retrieved context is both relevant and useful for generation.

The findings highlight that solely optimizing for retrieval relevance is insufficient for high-quality RAG outcomes; incorporating additional answer-centric criteria into the retrieval process leads to improved response performance.

-----

-----

-----

### Source [13]: https://openreview.net/forum?id=lz936bYmb3

Query: How do query transformation techniques like multi-query, RAG-Fusion, and HyDE improve retrieval relevance in RAG systems?

Answer: The **DMQR-RAG** (Diverse Multi-Query Rewriting RAG) method advances RAG systems by focusing on **diversity in query rewriting**. Unlike standard RAG, which uses a single query, DMQR-RAG generates multiple rewrites of the original query using different rewriting strategies. This diversity enables the retrieval of a broader set of relevant documents, thus improving both recall and the chance of finding information that strictly single-query-based retrieval might miss.

The retrieval phase in DMQR-RAG is executed in parallel for each rewritten query, maintaining retrieval efficiency. Retrieved documents are then reranked and synthesized for the generative model, just as in classic RAG, but with a more diverse and potentially more relevant context set. This method is particularly effective for queries where a single formulation might not capture the full breadth of the information need, ensuring more comprehensive and relevant retrieval for subsequent answer generation.

-----

-----

-----

### Source [61]: https://arxiv.org/html/2411.13154v1

Query: How do query transformation techniques like multi-query, RAG-Fusion, and HyDE improve retrieval relevance in RAG systems?

Answer: The DMQR-RAG framework introduces a **multi-query rewriting method** to improve both document retrieval and final answer quality in RAG systems. The core idea is that **rewriting a user's query in diverse forms allows retrieval of a wider and more relevant set of documents**. Unlike single-query retrieval, where only one formulation is used, multi-query approaches—such as RAG-Fusion—generate multiple query rewrites and retrieve documents for each. RAG-Fusion then applies the Reciprocal Rank Fusion (RRF) algorithm to rerank the combined results, increasing the chance of surfacing relevant documents that may not be found with a single query.

DMQR-RAG advances this by using information-theoretic diversity when generating rewrites, ensuring that different rewrites capture different aspects or interpretations of the user's intent. Each rewritten query can retrieve different, potentially complementary, documents. A cross-attention embedding model is used to rerank all retrieved documents, further improving relevance.

However, simply increasing the number of query rewrites can introduce noise. To balance diversity and precision, DMQR-RAG includes a **rewriting strategy selection method** that adaptively chooses which and how many rewriting strategies to use for a given query—improving retrieval and response performance while minimizing irrelevant results.

Extensive evaluation confirms that **multi-query rewriting, especially when informed by information diversity and adaptive selection, consistently outperforms single-query approaches and vanilla RAG-Fusion**, both in academic and real-world settings.

-----

-----

-----

### Source [62]: https://www.f22labs.com/blogs/what-is-multi-step-rag-a-complete-guide/

Query: How do query transformation techniques like multi-query, RAG-Fusion, and HyDE improve retrieval relevance in RAG systems?

Answer: **Multi-Step RAG** is an advanced query transformation technique that improves retrieval relevance by incorporating **iterative retrieval and reasoning cycles**. Instead of retrieving documents once based on the original query, Multi-Step RAG performs an initial retrieval, uses the results to refine or decompose the query, and then **executes additional retrieval rounds** with more context-aware or focused queries.

This process is particularly effective for **complex, multi-hop, or ambiguous questions**, as it allows the system to break down the original question into sub-tasks or clarify ambiguous elements. Each retrieval and reasoning step builds a deeper, more refined context, ultimately leading to more accurate, coherent, and contextually relevant responses.

Compared to traditional single-step RAG, Multi-Step RAG is:
- Better at handling complex queries that require chaining multiple pieces of information.
- Less prone to inaccuracies due to progressive refinement of the query and context.
- More capable of dealing with ambiguous or multi-part questions by iteratively clarifying and expanding upon the user's needs.

Overall, **iterative query transformation and retrieval cycles** enable Multi-Step RAG systems to assemble a more comprehensive and relevant set of documents for the generation stage, directly improving answer quality.

-----

-----

-----

### Source [63]: https://ai.gopubby.com/rag-fusion-redefining-search-using-multi-query-retrieval-and-reranking-88da68783d26

Query: How do query transformation techniques like multi-query, RAG-Fusion, and HyDE improve retrieval relevance in RAG systems?

Answer: **RAG-Fusion** enhances retrieval relevance by implementing **multi-query retrieval** combined with a **reranking mechanism**. In traditional RAG, a single query is used to retrieve relevant documents, typically ranked by vector similarity (e.g., cosine similarity). However, this approach may miss relevant documents due to limitations in how the query is formulated or how semantic similarity is measured.

RAG-Fusion addresses this by generating **multiple queries from different perspectives or phrasings** of the user's original question. Each query retrieves its own set of documents, potentially surfacing different relevant information. The results from all queries are then **combined and reranked using the Reciprocal Rank Fusion (RRF) algorithm**, which merges the ranked lists from each query in a way that rewards documents appearing near the top of multiple lists.

This multi-query, fusion-based approach improves both **recall** (by retrieving a broader set of relevant documents) and **precision** (by reranking to prioritize the most consistently relevant results). By considering multiple ways to interpret or express the user's intent, RAG-Fusion makes the retrieval component of RAG systems more robust and comprehensive, directly enhancing the final response quality.

-----

-----

</details>

<details>
<summary>What is the role of re-ranking models, like cross-encoders, in a post-retrieval RAG pipeline and how do they improve final answer quality?</summary>

### Source [14]: https://www.chitika.com/re-ranking-in-retrieval-augmented-generation-how-to-use-re-rankers-in-rag/

Query: What is the role of re-ranking models, like cross-encoders, in a post-retrieval RAG pipeline and how do they improve final answer quality?

Answer: Re-ranking models, such as **cross-encoders**, are integrated into Retrieval-Augmented Generation (RAG) pipelines to refine the initial set of retrieved documents by prioritizing those most relevant to the user’s query. The RAG process typically begins with a dense retrieval model (for example, DPR) to gather a candidate pool of documents. The re-ranker, often a cross-encoder like BERT, then re-scores and reorders these candidates to reflect their true relevance to the query.

Re-rankers can also filter for **trustworthiness**, downranking documents from less credible sources. In practice, this ability has led to substantial accuracy improvements: for example, introducing a re-ranker in healthcare applications increased response accuracy by 20%. In legal technology, domain-adapted re-rankers have reduced irrelevant results by 30%, streamlining research.

A key consideration is that cross-encoders are computationally intensive. To manage this, a hybrid approach is recommended: a fast retriever (such as BM25) quickly narrows down candidates, and then a cross-encoder provides precise ranking. This layered strategy ensures both efficiency and answer quality.

Furthermore, aligning the re-ranker’s scoring with the large language model’s (LLM) understanding helps prevent mismatches that lead to incoherent generative outputs. Data quality is also critical; noisy training data can degrade re-ranker performance, so ongoing data audits are advised. Re-ranking should be viewed as an adaptable process, evolving as user needs and domains shift.

-----

-----

-----

### Source [15]: https://adasci.org/how-to-select-the-best-re-ranking-model-in-rag/

Query: What is the role of re-ranking models, like cross-encoders, in a post-retrieval RAG pipeline and how do they improve final answer quality?

Answer: In a RAG pipeline, **re-ranking** is a post-retrieval step that critically determines the quality and relevance of information provided to a generative model. After the initial retrieval phase, which returns a set of candidate documents or passages, the re-ranking model performs a deeper, more nuanced analysis to assess each document’s relevance to the query or context.

Re-ranking models assign new, more accurate relevance scores, leading to a reordering of the documents. This process is crucial because the initial retrieval step may only provide a rough estimate of relevance, potentially including less useful or off-topic results. By refining the ranking, the re-ranker ensures that the most contextually appropriate and informative documents are prioritized for the generation phase. This directly improves the quality, factuality, and usefulness of the final generated answers.

-----

-----

-----

### Source [16]: https://zilliz.com/learn/optimize-rag-with-rerankers-the-role-and-tradeoffs

Query: What is the role of re-ranking models, like cross-encoders, in a post-retrieval RAG pipeline and how do they improve final answer quality?

Answer: Rerankers, including cross-encoders, provide a **two-stage retrieval system** in RAG pipelines. The initial stage involves a vector database conducting a fast search to identify Top-K candidate documents. In the second stage, the reranker analyzes and reprioritizes these candidates according to their query relevance, sending the best-scoring results to the LLM for answer generation. This process yields **more relevant and accurate answers**.

However, rerankers—especially cross-encoders—introduce substantial computational overhead. While vector searches are quick (milliseconds), reranking requires running a deep neural network on each candidate, which can take hundreds of milliseconds to several seconds depending on model and hardware. Therefore, the decision to use rerankers involves balancing improved answer quality against increased latency and computational costs.

-----

-----

-----

### Source [17]: https://adasci.org/a-hands-on-guide-to-enhance-rag-with-re-ranking/

Query: What is the role of re-ranking models, like cross-encoders, in a post-retrieval RAG pipeline and how do they improve final answer quality?

Answer: In RAG systems, re-ranking is used to **reduce hallucinations** and ensure reliable search results by providing a more contextually aware assessment of candidate documents. After the retriever model generates an initial, broadly relevant set, the re-ranking phase applies a more sophisticated model—such as a **cross-encoder** or BERT-based re-ranker—that evaluates both the query and document together for precise relevance scoring.

This process reorders the candidates, retaining only the top-ranked, contextually relevant passages for the generator. The use of cross-encoders and similar models is crucial for capturing deeper semantic and contextual relationships, which basic retrieval scoring may miss. The final answer quality is thus significantly improved, with higher factual accuracy and reduced irrelevant content.

-----

</details>

<details>
<summary>How does GraphRAG solve sensemaking queries over large datasets where traditional vector RAG fails?</summary>

### Source [18]: https://ragaboutit.com/graph-rag-vs-vector-rag-a-comprehensive-tutorial-with-code-examples/

Query: How does GraphRAG solve sensemaking queries over large datasets where traditional vector RAG fails?

Answer: GraphRAG solves sensemaking queries over large datasets by leveraging the structured nature of knowledge graphs, in contrast to traditional vector RAG, which relies on vectorized textual representations. GraphRAG excels when the relationships between entities and the overall structure of data are crucial for generating accurate and contextually relevant responses. By utilizing knowledge graphs, GraphRAG captures and utilizes the inherent semantics and hierarchies within the data, enabling sophisticated reasoning and inference beyond simple similarity matching.

This makes GraphRAG particularly suitable for domains with complex, interconnected data—such as healthcare, finance, and scientific research—where understanding multi-step relationships and domain-specific knowledge is essential. GraphRAG also enhances explainability, as traversing the graph and retrieving relevant subgraphs provides a transparent and interpretable trace of the reasoning process, thereby increasing trustworthiness and accountability. In contrast, vector RAG is efficient for large-scale similarity searches but lacks this level of explainability and depth of reasoning since it retrieves information based on semantic similarity rather than explicit inter-entity relationships.

-----

-----

-----

### Source [19]: https://www.chitika.com/graph-rag-vs-vector-rag/

Query: How does GraphRAG solve sensemaking queries over large datasets where traditional vector RAG fails?

Answer: Graph-Based RAG organizes information as knowledge graphs, explicitly mapping entities and their relationships, which mirrors real-world hierarchies. This structure enables GraphRAG to perform multi-hop reasoning, making it ideal for sensemaking queries that require understanding how entities are interconnected—such as drug interactions in healthcare or legal precedents in law. Vector-Based RAG, by contrast, retrieves data based on semantic similarity using dense embeddings, which is efficient for unstructured data but struggles with multi-step reasoning tasks needed for deep sensemaking.

GraphRAG's structured approach allows it to navigate complex relationships, providing answers that not only retrieve information but also explain the links between entities. However, maintaining knowledge graphs requires meticulous curation. Hybrid systems are emerging that combine graph reasoning with vector efficiency, aiming to balance explainability with scalability—critical for robust sensemaking in large datasets.

-----

-----

-----

### Source [20]: https://www.gitselect.com/post/demystifying-retrieval-augmented-generation-vector-rag-vs-graph-rag

Query: How does GraphRAG solve sensemaking queries over large datasets where traditional vector RAG fails?

Answer: GraphRAG addresses sensemaking queries by using knowledge graphs to represent entities and their relationships, allowing for context-rich exploration of data. When processing a query, GraphRAG navigates the knowledge graph to identify relevant entities and their connections, providing a deeper understanding of context and relationships than traditional vector RAG.

While vector RAG retrieves thematically relevant information (i.e., documents or passages similar in meaning to the query), GraphRAG retrieves entities and explains how they are related, supporting richer multi-step reasoning essential for sensemaking. For example, in a historical query, GraphRAG can show how one event influenced another, capturing causal and contextual links that vector RAG’s similarity search would miss. This entity- and relationship-centric retrieval gives GraphRAG a significant edge in answering complex, interconnected queries in large datasets.

-----

-----

</details>

<details>
<summary>What are the latest techniques and best practices for advanced RAG chunking, specifically focusing on semantic, layout-aware, and propositional strategies for complex, multi-modal documents?</summary>

### Source [21]: https://www.dailydoseofds.com/p/5-chunking-strategies-for-rag/

Query: What are the latest techniques and best practices for advanced RAG chunking, specifically focusing on semantic, layout-aware, and propositional strategies for complex, multi-modal documents?

Answer: This source outlines five key chunking strategies for RAG (Retrieval-Augmented Generation):

- **Fixed-size chunking**: The document is split into uniform segments based on a set number of characters, words, or tokens. Overlapping chunks are recommended to preserve context, but this method often disrupts semantic flow and can split sentences or ideas between chunks, potentially diluting critical information.

- **Semantic chunking**: Instead of size-based splitting, this method divides text based on semantic boundaries—meaningful units such as sentences or paragraphs. Embedding models or NLP tools are used to group together semantically related content, which helps maintain the integrity of ideas and improves retrieval accuracy for contextually relevant information.

- **Recursive chunking**: This approach uses a hierarchy of separators—such as paragraphs, sentences, and words—to recursively split the text until the desired chunk size is achieved. This method is more adaptive and preserves the logical structure of the document, which is crucial for complex texts.

- **Document structure-based chunking**: Leverages the inherent organization of a document (e.g., sections, headings, bullet points) for splitting. This layout-aware strategy is especially effective for structured documents, preserving context and improving downstream retrieval.

- **LLM-based chunking**: Uses large language models to determine optimal chunking points based on a deeper understanding of semantic and propositional boundaries. This method can dynamically adapt to both content and structural nuances, making it suitable for multi-modal and complex documents.

The source emphasizes that while simple methods like fixed-size chunking are easy to implement, advanced strategies—especially semantic and layout-aware—are preferred for information-dense or complex documents to optimize RAG workflows and retrieval quality[1].

-----

-----

-----

### Source [22]: https://airbyte.com/data-engineering-resources/chunk-text-for-rag

Query: What are the latest techniques and best practices for advanced RAG chunking, specifically focusing on semantic, layout-aware, and propositional strategies for complex, multi-modal documents?

Answer: This source details five chunking strategies for RAG with a focus on semantic and adaptive approaches:

- **Fixed-size chunking**: Splits text into equally sized segments, which can break context mid-sentence or mid-paragraph. Overlapping is recommended to retain semantic continuity.

- **Recursive chunking**: Uses a set of separators (e.g., paragraphs, sentences, words) and recursively splits the text until chunks are within a desired size range. Tools like LangChain’s RecursiveCharacterTextSplitter are cited for implementation. This approach better preserves semantic and structural integrity compared to fixed-size methods, though it can be computationally intensive.

- **Semantic chunking**: Advanced splitting based on content meaning rather than arbitrary size. Uses embeddings to group text by semantic similarity, resulting in context-aware and logical chunks. LlamaIndex’s SemanticSplitterNodeParse is mentioned as a practical tool, creating nodes where each contains semantically related sentences.

Semantic chunking is especially recommended for complex documents where maintaining context is critical for accurate retrieval. It enables the RAG system to extract and retrieve more coherent, meaningful information, improving both retrieval accuracy and user experience for multi-modal and contextually rich documents[2].

-----

-----

-----

### Source [23]: https://www.ibm.com/think/tutorials/chunking-strategies-for-rag-with-langchain-watsonx-ai

Query: What are the latest techniques and best practices for advanced RAG chunking, specifically focusing on semantic, layout-aware, and propositional strategies for complex, multi-modal documents?

Answer: This IBM tutorial describes chunking as central to RAG, especially for handling large documents by breaking them into manageable, meaningful snippets:

- **Significance of chunking**: Essential for embedding documents into vector databases and optimizing retrieval efficiency in RAG pipelines. Smaller, semantically coherent chunks are generally preferred for models with limited context windows.

- **Strategy selection**: The tutorial highlights the importance of choosing a chunking method suited to the document type and use case. While not listing methods in detail, it reinforces that semantic and structure-aware chunking approaches are best for complex, multi-modal documents.

- **Semantic chunking**: Recommended for dividing documents based on meaning, ensuring each chunk is a logical unit of information. This helps preserve context, making semantic search and retrieval more precise.

- **Layout-awareness**: For documents with complex structures, chunking strategies that respect layout cues (such as sections, tables, or multi-modal content) are advised. This ensures that chunks align with the natural organization of the document, supporting more accurate information retrieval and downstream processing.

The tutorial underscores the need for advanced chunking—semantic and layout-aware—when dealing with complex, information-dense, or multi-format content in RAG workflows[3].

-----

-----

-----

### Source [24]: https://community.databricks.com/t5/technical-blog/the-ultimate-guide-to-chunking-strategies-for-rag-applications/ba-p/113089

Query: What are the latest techniques and best practices for advanced RAG chunking, specifically focusing on semantic, layout-aware, and propositional strategies for complex, multi-modal documents?

Answer: This Databricks guide presents a comprehensive set of chunking strategies for RAG, with practical insights for advanced document processing:

- **Fixed-size chunking**: Divides text into chunks of a predefined size, optionally with overlap to maintain context.

- **Semantic chunking**: Uses semantic similarity (often via embeddings) to ensure each chunk represents a coherent idea or topic. This is especially useful for unstructured or information-dense documents.

- **Recursive chunking**: Adapts to code or prose, splitting at logical boundaries (e.g., functions, paragraphs) and recursively refining chunks to the desired size.

- **Adaptive chunking**: Adjusts chunk sizes dynamically, based on content complexity, with user-defined minimum and maximum sizes. This strategy can use complexity measures to optimize chunk boundaries for varying document types.

- **Context-enriched chunking**: Expands each chunk with surrounding context (windowing), which can improve retrieval accuracy by providing more complete information per chunk.

- **AI-driven chunking**: Employs large language models to determine chunk boundaries based on a deep understanding of both content and structure. This approach can adapt chunking strategies to the specific layout, semantics, and even propositional boundaries of a document, making it highly suited to complex, multi-modal sources.

This source recommends combining semantic, adaptive, and AI-driven chunking for best results with complex, multi-modal documents. Layout-aware and propositional chunking are best achieved using AI-driven techniques, which can flexibly adapt to both content and structure[4].

-----

-----

</details>

<details>
<summary>How are hybrid search systems in RAG architected to effectively combine keyword-based (like BM25) and semantic vector search, including the role of rank fusion algorithms like Reciprocal Rank Fusion (RRF)?</summary>

### Source [25]: https://www.chitika.com/hybrid-retrieval-rag/

Query: How are hybrid search systems in RAG architected to effectively combine keyword-based (like BM25) and semantic vector search, including the role of rank fusion algorithms like Reciprocal Rank Fusion (RRF)?

Answer: Hybrid retrieval in RAG systems is designed to leverage the complementary strengths of **BM25** (a keyword-based search algorithm) and **FAISS** (a dense vector/semantic search library). BM25 excels at **exact term matching** and can be fine-tuned via parameters for domain-specific needs, making it suitable for scenarios where precision in keyword matching is critical. However, BM25 alone can miss semantically relevant results that use different terminology.

FAISS, on the other hand, identifies **deeper semantic connections** between queries and documents by using vector representations, capturing meaning beyond specific keywords but sometimes returning irrelevant results due to lack of lexical constraints.

**Hybrid retrieval systems architect these methods in a layered fashion:**
- **BM25 acts as an initial filter**, narrowing down the candidate set based on exact or near-exact keyword matches.
- **FAISS then applies semantic refinement** to this filtered set, promoting documents that are contextually relevant even if the exact keywords are not present.

This architecture enhances both **precision** (through BM25) and **contextual relevance** (through FAISS), and it also **reduces computational overhead** because FAISS only needs to operate on a smaller subset of documents pre-selected by BM25.

Such hybrid models are widely used in RAG for domains requiring both accuracy and semantic understanding, including legal research, healthcare, and technical documentation. The key to effectiveness in this architecture is the **integration and ordering of the retrieval steps**, ensuring that each method compensates for the other's limitations.

-----

-----

-----

### Source [26]: https://blog.vectorchord.ai/hybrid-search-with-postgres-native-bm25-and-vectorchord

Query: How are hybrid search systems in RAG architected to effectively combine keyword-based (like BM25) and semantic vector search, including the role of rank fusion algorithms like Reciprocal Rank Fusion (RRF)?

Answer: Hybrid search systems in RAG combine **BM25** (for keyword-based retrieval) and **vector-based semantic search** (such as VectorChord or FAISS) to deliver both precision and semantic understanding. BM25 is highly effective for structured, keyword-heavy content, providing **exact keyword matches and ranking documents based on term frequency**. However, it lacks capability for understanding synonyms or contextual nuances.

Vector-based retrieval captures **semantic meaning**, allowing for better generalization and retrieval of contextually relevant documents even when exact keywords do not match. However, it might miss precise keyword matches.

A typical hybrid search architecture involves:
- **Running both BM25 (keyword) and vector (semantic) queries in parallel** or sequence.
- **Combining results using a reranking step**, where the most relevant results from both retrievals are merged.

The combination can be implemented in databases like PostgreSQL using extensions (e.g., VectorChord for vectors and VectorChord-bm25 for BM25). After initial retrieval, a **reranking algorithm** (sometimes involving a third-party model or scoring function) is applied to produce a final, ranked set of results that blend the strengths of both retrieval methods.

This approach is suitable for applications such as recommendation engines, enterprise search, and document retrieval systems, where both exact matches and semantic relevance are important. The hybrid search system is flexible, allowing tuning on the relative importance of each retrieval method in the final ranking.

-----

-----

-----

### Source [27]: https://arxiv.org/html/2502.16767v1

Query: How are hybrid search systems in RAG architected to effectively combine keyword-based (like BM25) and semantic vector search, including the role of rank fusion algorithms like Reciprocal Rank Fusion (RRF)?

Answer: This research paper details an architecture that **integrates a fine-tuned sentence transformer model (for semantic retrieval) with the traditional BM25 algorithm (for lexical search)** to achieve both semantic precision and lexical accuracy in RAG systems.

The core step is **score normalization and weighted combination**:
- The system computes scores independently using both BM25 and the semantic model.
- These scores are normalized to ensure comparability. For instance, in this work, the authors set \(\alpha=0.65\) to give slightly higher weight to semantic matching, while preserving the influence of lexical search.
- The final relevance score for each document is a **weighted sum of normalized BM25 and semantic scores**, ensuring that neither approach dominates due to differences in score distributions.

Empirical results show that the **hybrid system outperforms both BM25-only and semantic-only systems on recall and mean average precision (MAP)**, confirming the hybrid approach’s effectiveness. The paper emphasizes that **careful calibration of score weighting and normalization** is crucial for optimal performance.

This architecture allows RAG systems to **balance exact phrase matching with semantic similarity**, providing robust retrieval in diverse information needs.

-----

-----

-----

### Source [28]: https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking

Query: How are hybrid search systems in RAG architected to effectively combine keyword-based (like BM25) and semantic vector search, including the role of rank fusion algorithms like Reciprocal Rank Fusion (RRF)?

Answer: Hybrid search in RAG is described as a combination of **keyword (sparse) search**—with BM25 as a primary algorithm—and **vector (dense) search**. The hybrid approach allows the system to **match on keywords in contextually relevant content**, thereby increasing both recall and the quality of outputs generated by large language models (LLMs).

A key architectural step is the inclusion of a **reranking stage**. After retrieving results using both BM25 and vector search, the retrieved documents are passed through a **reranker** (e.g., CohereRerank), which scores and reorders them based on contextual relevance to the query.

The process can be summarized as:
- **BM25 and vector search retrieve candidate documents** based on their respective strengths.
- **Candidates are then merged or concatenated into a single pool**.
- A **reranker model evaluates each candidate** in the context of the original query and assigns a new relevance score.
- The final ranked list is used for answer generation.

This reranking process can be further optimized with ensemble retrievers and contextual compression, ensuring only the most relevant information is used by the downstream LLM. The hybrid method’s superior recall rates increase the likelihood that the LLM will have access to all necessary context for generating accurate answers.

-----

-----

</details>

<details>
<summary>What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?</summary>

### Source [30]: https://github.com/ranguy9304/LangGraphRAG

Query: What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?

Answer: LangGraphRAG is a terminal-based RAG system implemented using LangGraph. The architecture is modular, consisting of distinct components for the flow of the RAG process, data storage and models, and core logic. The system routes queries through multiple stages—message history caching, query transformation, and vector database retrieval. LangGraph orchestrates the flow and interactions between these modules, supporting more flexible and dynamic control compared to a fixed linear pipeline. The modularity and explicit flow management are foundational for transitioning from a static, pre-determined process to a more dynamic, agentic system, as each module can be adapted, replaced, or extended within the LangGraph framework.

-----

-----

-----

### Source [31]: https://python.langchain.com/docs/tutorials/rag/

Query: What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?

Answer: A traditional, linear RAG pipeline comprises two main components: an offline indexing pipeline (loading, splitting, and storing documents in a vector store), and a retrieval and generation pipeline (retrieving relevant data at query time and generating a response using an LLM). In this standard architecture, the path from query to answer is fixed—input flows sequentially from retrieval to generation. Using LangGraph for orchestration enables the retrieval and generation steps to be implemented as configurable components. This flexibility is the starting point for a more dynamic, agentic RAG system, as LangGraph can support branching flows, conditional logic, and integration of more sophisticated agent behaviors within the pipeline.

-----

-----

-----

### Source [32]: https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/

Query: What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?

Answer: Moving to a dynamic, agentic RAG system requires architectural changes that allow for complex, flexible agent behaviors beyond simple linear routing. LangGraph provides features such as:
- **Human-in-the-loop**: Integrate human oversight or feedback at critical junctures, allowing for approval, correction, or guidance during the retrieval/generation process.
- **Parallelization**: Enable concurrent execution of multiple retrieval or reasoning tasks, supporting workflows like map-reduce or multi-agent collaboration.
- **Subgraphs**: Structure the system into modular, hierarchical sub-components (agents or agent teams) with isolated state management and controlled communication, enabling dynamic and context-sensitive routing.
- **Reflection**: Implement mechanisms for self-evaluation and iterative improvement, where the agent can assess its outputs, revise strategies, or self-correct.
In summary, the shift involves replacing a fixed, sequential pipeline with a graph-based, modular architecture in which agentic behaviors (e.g., parallel reasoning, human feedback, recursive improvement) can be orchestrated and controlled at runtime.

-----

-----

-----

### Source [33]: https://www.langchain.com/langgraph

Query: What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?

Answer: LangGraph provides a framework for designing highly controllable and expressive cognitive architectures. It supports diverse control flows: single agent, multi-agent, hierarchical, and sequential patterns. LangGraph emphasizes robust handling of realistic, complex scenarios, with features allowing for easy integration of moderation, quality control loops, and component configurability. For the architectural shift, this means moving away from a hardcoded, linear pipeline to a configurable, templatized system where tools, prompts, and models can be dynamically orchestrated and reconfigured. This enables RAG systems to support dynamic decision-making, agent hand-offs, and multiple modes of operation within a unified framework.

-----

-----

### Source [52]: https://github.com/ranguy9304/LangGraphRAG

Query: What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?

Answer: LangGraphRAG, a terminal-based Retrieval-Augmented Generation (RAG) system using LangGraph, organizes its architecture into clearly separated modules: **Architecture** (which defines the flow of the RAG system), **Data** (containing data files and models), and **Modules** (housing the core logic and functions). The system routes queries through various processes, including message history caching, query transformation, and document retrieval from a vector database. LangGraph is used to manage the flow and interactions between these modules, allowing for modular and flexible orchestration of the RAG pipeline. This design supports dynamic handling of queries and lays the groundwork for more agentic behaviors by decoupling the system into distinct, interactable components, as opposed to a strictly linear, pre-determined sequence.

-----

-----

-----

### Source [53]: https://python.langchain.com/docs/tutorials/rag/

Query: What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?

Answer: A typical linear RAG pipeline consists of two main components: **indexing** (loading, splitting, and storing data in a vector store) and **retrieval and generation** (retrieving relevant data for a query and generating an answer using an LLM). Traditionally, this flow is predetermined: data is indexed offline, and at runtime, a query triggers a fixed sequence—retrieve relevant chunks and generate a response. When integrating LangGraph, the orchestration of retrieval and generation steps becomes more modular and dynamic. LangGraph allows the definition of custom flows and branching logic, enabling the pipeline to adapt based on query context, retrieved evidence, or intermediate results. This shift from a linear pipeline to a more agentic system involves re-architecting the workflow so that steps are not strictly sequential but can involve conditional logic, iterative retrieval, or incorporation of additional tools and agents as needed.

-----

-----

-----

### Source [54]: https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/

Query: What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?

Answer: LangGraph empowers the transition from linear to agentic RAG architectures by supporting advanced agent behaviors and control flows far beyond simple routing. Key architectural features include:

- **Custom agent architectures:** Developers can design tailored systems for specific tasks, moving beyond fixed pipelines.
- **Human-in-the-loop:** Incorporation of human approvals and feedback enables dynamic decision-making and reliability, which is crucial for sensitive or complex queries.
- **Parallelization:** LangGraph’s Send API allows for concurrent processing, enabling agents to handle subtasks or multiple retrievals in parallel instead of sequentially.
- **Subgraphs:** These enable modular and hierarchical organization, allowing different agents (or agent teams) to work in isolation yet communicate and synchronize with the parent workflow.
- **Reflection:** Agents can evaluate their own task completion, correctness, and iteratively improve or self-correct, using feedback loops (potentially LLM-driven or deterministic).

These capabilities collectively facilitate the architectural shift to a dynamic, agentic RAG system, where decision points, workflow paths, and even the set of active agents can evolve at runtime based on the specific needs of each query or task.

-----

-----

-----

### Source [55]: https://www.langchain.com/langgraph

Query: What is the practical architectural shift required to move from a linear, pre-determined RAG pipeline to a dynamic, agentic RAG system using frameworks like LangGraph?

Answer: LangGraph provides a **flexible and controllable cognitive architecture** that supports diverse control flows, including single-agent, multi-agent, hierarchical, and sequential patterns. Unlike rigid, black-box pipelines, LangGraph enables developers to templatize and adapt their RAG architectures for complex, realistic scenarios. Features such as **easy-to-add moderation, quality loops, and configuration of tools, prompts, and models** allow for robust, dynamic systems that can prevent agents from veering off course. This means the practical architectural shift involves moving from a fixed, sequential data flow to a more expressive, modular, and configurable agentic framework where tasks, models, and logic can be dynamically orchestrated and adapted to real-world requirements.

-----

</details>

<details>
<summary>How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?</summary>

### Source [34]: https://wandb.ai/byyoung3/Generative-AI/reports/GraphRAG-Enhancing-LLMs-with-knowledge-graphs-for-superior-retrieval--VmlldzoxMDY0OTU0MA

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: GraphRAG addresses the limitations of traditional vector-based RAG by **transforming unstructured data into interconnected knowledge graphs**. While vector-based RAG systems retrieve isolated text chunks based on semantic similarity, they often miss the broader context and relationships necessary for answering complex, multi-hop reasoning queries. GraphRAG overcomes this by enabling LLMs to perceive and utilize the **connections between data points**, facilitating a more holistic understanding. Through the use of **hierarchical community detection**, GraphRAG identifies densely connected clusters within the knowledge graph. This process helps synthesize information across multiple nodes and relationships, allowing for **query-focused summarization and global sensemaking**. As a result, GraphRAG can provide richer, more insightful answers to queries that require drawing connections across large datasets, in contrast to the fragmented responses typical of standard RAG approaches.

-----

-----

-----

### Source [35]: https://weaviate.io/blog/graph-rag

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: MS GraphRAG distinguishes itself from naive RAG by employing **graph algorithms—specifically the Leiden algorithm—for community detection**. This approach identifies clusters of densely interconnected nodes (entities and their relationships), which often represent semantically or contextually related information. After constructing the knowledge graph, the system uses an LLM to **generate concise summaries for both individual entities/relationships and entire communities**. By consolidating redundant or duplicate information and summarizing at the community level, GraphRAG provides a **holistic overview** that synthesizes interconnected facts into a cohesive narrative. This capability enables the system to **answer complex, multi-hop queries** that span multiple entities and relationships—something traditional vector-based RAG struggles with due to its lack of relational awareness and context integration.

-----

-----

-----

### Source [36]: https://aiexpjourney.substack.com/p/graph-rag-an-approach-to-answering

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: GraphRAG applies **community detection to divide the knowledge graph into groups of related nodes, edges, and claims**. These communities can be summarized at both indexing and query time, allowing the LLM to generate **report-like, query-focused summaries** for each relevant cluster. Importantly, even if the LLM's entity extraction is imperfect, community detection can **link variants or synonyms of the same entity** (a form of entity disambiguation), ensuring connections aren't lost due to inconsistent labeling. By summarizing the information in each community—particularly using hierarchical methods such as the Leiden algorithm—GraphRAG delivers **comprehensive, multi-hop answers** that capture the global structure and semantics of the dataset. This process enables the system to handle queries that require synthesizing information across multiple documents and relationships, addressing a key limitation of vector-based RAG.

-----

-----

-----

### Source [37]: https://learnopencv.com/graphrag-explained-knowledge-graphs-medical/

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: GraphRAG **integrates structured knowledge graphs with semantic vector chunks**, enabling LLMs to reason over **multi-hop connections** necessary for complex queries. The framework distinguishes between **local (fine-grained) and global (aggregated) communities** within the knowledge graph: lower-level communities focus on detailed nodes and edges, while higher-level ones aggregate information from multiple sub-communities. This hierarchical strategy allows GraphRAG to **scale analysis across large datasets**, retaining key details at the node level but also synthesizing broader context for global queries. During the querying phase, **Query-Focused Summarization (QFS)** is used to identify and summarize relevant entities and relationships in response to user queries, leveraging the graph structure to follow multi-hop paths and uncover patterns that are lost in traditional RAG. As a result, GraphRAG produces **better responses to overarching, global queries** that require connecting disparate pieces of information, compared to standard source text or vector-based summarization.

-----

-----

-----

### Source [47]: https://www.machinelearningplus.com/gen-ai/graph-rag-explained-your-complete-guide-to-knowledge-graph-powered-rag/

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: GraphRAG advances retrieval-augmented generation by building **knowledge graphs** that explicitly capture **relationships among entities** from text, and then applies **community detection** to identify clusters of related concepts. The process starts with splitting documents into chunks and converting them to vector embeddings. These chunks are then connected if they are semantically similar above a certain threshold, forming a graph structure rather than a flat vector index.

The use of knowledge graphs allows GraphRAG to represent complex, multi-step relationships (multi-hop connections) between entities that traditional vector-based RAG—which treats each chunk as an isolated unit—cannot easily model. Community detection further groups related concepts, enabling the system to reason about and summarize information at the level of entire clusters, rather than just individual passages. This approach is critical for queries that require connecting insights across multiple documents or reasoning steps, as it enables the retrieval and synthesis of information spanning interconnected concepts, thus overcoming the limitations of standard vector search in multi-hop reasoning.

-----

-----

-----

### Source [48]: https://wandb.ai/byyoung3/Generative-AI/reports/GraphRAG-Enhancing-LLMs-with-knowledge-graphs-for-superior-retrieval--VmlldzoxMDY0OTU0MA

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: GraphRAG is designed specifically to address the **limitations of traditional RAG** in handling complex, overarching queries that require synthesizing information across an entire dataset. While standard RAG retrieves isolated passages based on semantic similarity, it often leaves users with "fragmented answers" and cannot reveal the relationships that connect disparate pieces of information.

GraphRAG overcomes this by transforming data into **interconnected knowledge graphs** that encode entity-to-entity relationships. The addition of **hierarchical community detection** allows the system to cluster related entities and concepts together, supporting **global sensemaking**—the ability to see overarching patterns and connections. This enables LLMs to generate **richer, more insightful answers** to complex, multi-hop queries, as they can "see beyond individual data points" and synthesize larger patterns and relationships that traditional RAG systems miss.

-----

-----

-----

### Source [49]: https://weaviate.io/blog/graph-rag

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: The distinguishing feature of MS GraphRAG is its use of **community detection algorithms** (such as the Leiden algorithm) to identify **clusters of densely interconnected nodes** (entities and their relationships) within the knowledge graph. Each node (entity) may have multiple relationships, potentially appearing in numerous contexts.

The process involves **summarizing nodes and relationships** using LLMs to consolidate information and resolve redundancy, resulting in comprehensive entity profiles. Once communities are detected, the system generates **high-level summaries for each community**, effectively synthesizing information from multiple related entities and their interactions into a **cohesive overview**. This enables the answering of complex queries that require reasoning across several entities and relationships, rather than retrieving isolated facts as in traditional vector-based RAG. The resulting summaries and community-level understanding provide a **holistic view**, which is essential for multi-hop and global reasoning.

-----

-----

-----

### Source [50]: https://aiexpjourney.substack.com/p/graph-rag-an-approach-to-answering

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: GraphRAG's pipeline uses LLM-driven prompts to **detect, extract, and summarize nodes (entities), edges (relations), and covariates (claims)** from the dataset. **Community detection** is then applied to group related elements within the knowledge graph, enabling the LLM to **summarize information at both the indexing and querying stages**.

For complex, multi-hop reasoning queries, GraphRAG generates a "global answer" by performing a final round of **query-focused summarization over all relevant community summaries**. Community detection also aids **entity disambiguation** by grouping variant forms of the same entity, even when extraction is inconsistent. This results in report-like, hierarchical summaries for each community, which help users understand the **global structure and semantics** of the entire corpus—capabilities that flat vector-based retrieval cannot offer.

-----

-----

-----

### Source [51]: https://learnopencv.com/graphrag-explained-knowledge-graphs-medical/

Query: How does GraphRAG's use of knowledge graphs and community detection solve complex, multi-hop reasoning queries that traditional vector-based RAG struggles with?

Answer: GraphRAG **integrates structured knowledge graphs (KGs) with semantic vector chunks**, allowing LLMs to **reason over multi-hop connections** for complex queries. This hybrid approach enables answers to global, high-level questions (e.g., "Who are the common people across the stories?") that require synthesizing information from different parts of the dataset.

Communities are organized hierarchically, with **lower-level (local) communities** focusing on significant nodes and relationships, while **higher-level (global) communities** aggregate multiple local communities. This structure supports **progressive summarization** and enables the model to traverse and summarize information across multiple hops and contexts, addressing the limitations of traditional vector-based RAG in handling queries that require complex, interconnected reasoning.

-----

-----

</details>

<details>
<summary>What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?</summary>

### Source [38]: https://www.patronus.ai/llm-testing/rag-evaluation-metrics

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: The article identifies **five key metrics** for evaluating the end-to-end performance of production RAG systems:

- **Context Relevance**: Measures how relevant the retrieved context is to the user query. High context relevance ensures the model is retrieving information that is closely aligned with the user's intent.
- **Context Sufficiency**: Evaluates whether the retrieved context contains enough information to answer the query. Insufficient context can lead to incomplete or inaccurate answers.
- **Answer Relevance**: Assesses how relevant the generated answer is to the user query. Even with correct context, the answer must directly address the user's needs.
- **Answer Correctness**: Determines whether the generated answer is factually correct based on the provided context. This is a critical metric for applications requiring high factual accuracy.
- **Answer Hallucination**: Tracks the frequency and severity of hallucinated information—answers that do not correspond to the retrieved context or contain fabricated facts.

The article emphasizes the importance of benchmarking these metrics against target values and tailoring them to specific use cases. It also notes that robust RAG evaluation practices are essential for maintaining the reliability of LLM applications, especially when handling unstructured data sources.

-----

-----

-----

### Source [39]: https://arxiv.org/html/2405.07437v2

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: This survey introduces the **A Unified Evaluation Process of RAG (Auepora)**, which structures RAG evaluation around three main questions:

- **What to Evaluate?** (Targets): Clearly define the performance aspects to be assessed, such as retrieval accuracy, generative quality, faithfulness, and relevance.
- **How to Evaluate?** (Datasets): Select or construct datasets that reflect real-world use cases and enable meaningful comparisons.
- **How to Measure?** (Metrics): Use metrics that align with the defined targets and the characteristics of the chosen datasets.

The Auepora methodology systematically covers all pairs of "Evaluable Outputs" (e.g., retrieved contexts, generated answers) and "Ground Truths" (e.g., reference documents, expected answers). The process aims to address the interplay between **retrieval accuracy** (e.g., context relevance, context sufficiency) and **generative quality** (e.g., answer relevance, faithfulness, correctness).

The survey highlights the need for targeted benchmarks and calls attention to current challenges in RAG evaluation, including the creation of standardized datasets, the calibration of metrics for both retrieval and generation, and the alignment with practical, user-facing outcomes.

-----

-----

-----

### Source [40]: https://cloud.google.com/blog/products/ai-machine-learning/optimizing-rag-retrieval

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: This Google Cloud blog outlines **common RAG evaluation frameworks** and their associated metrics:

- **Model-based metrics**: Use LLM "judge" models to evaluate RAG outputs. These can be:
    - **Pointwise**: Assign a numerical score (e.g., 0–5) to each output along criteria such as relevance, faithfulness, and correctness.
    - **Pairwise**: Compare outputs from two models and select the superior response, useful for benchmarking and A/B testing.
- **Computation-based metrics**: Rely on automated calculations such as **ROUGE** and **BLEU**, which compare generated responses to reference answers.
- **Golden question sets**: Collaborate with stakeholders to curate diverse, representative queries ("golden sets") that reflect key use cases, including simple, complex, and misspelled queries.
- **Vertex AI generative AI evaluation framework**: Provides built-in tools to automate the measurement of multiple metrics and streamline iterative RAG system improvement.

The blog emphasizes best practices such as combining subjective (human or model-judged) and objective (computed) metrics, and ensuring that test sets are comprehensive and aligned with production requirements.

-----

-----

-----

### Source [41]: https://www.pinecone.io/learn/series/vector-databases-in-production-for-busy-engineers/rag-evaluation/

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: This guide presents a table of **evaluation frameworks and metrics** mapped to different RAG use cases:

- **RAGAS**: Suitable for initial evaluations with limited reference data. Metrics include **Average Precision (AP)** and **Faithfulness**, focusing on precision and context alignment.
- **ARES**: Designed for continuous, dynamic deployments. Uses **Mean Reciprocal Rank (MRR)** and **Normalized Discounted Cumulative Gain (NDCG)** to assess response relevance and ranking, often leveraging synthetic data and LLM judges.
- **TraceLoop**: Tracks full system traces, including vector storage. Metrics include **Information Gain**, **Factual Consistency**, and **Citation Accuracy**—useful for applications requiring detailed information provenance.
- **Arize**: Focused on real-time monitoring. Uses **Precision**, **Recall**, and **F1** metrics for immediate feedback on performance.
- **Galileo**: Tailored for enterprise applications needing advanced metrics integration. Measures include **Custom metrics** and **Context Adherence**.
- **TruLens**: Optimized for domain-specific applications. Assesses **Domain-specific accuracy** and **Precision**.

The source recommends choosing frameworks and metrics based on the system’s deployment context and organizational needs, highlighting the importance of both retrieval and generation quality for robust RAG evaluation.

-----

-----

-----

### Source [56]: https://www.patronus.ai/llm-testing/rag-evaluation-metrics

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: This source outlines that **RAG evaluation metrics** focus on measuring the effectiveness of both the **context retrieval** and the **generated response**. The five key metrics highlighted for RAG system evaluation are:

- **Context relevance:** Measures how relevant the retrieved context is to the user's query.
- **Context sufficiency:** Assesses whether the retrieved context contains enough information to answer the question.
- **Answer relevance:** Evaluates how well the generated answer addresses the query.
- **Answer correctness:** Checks the factual accuracy of the generated response.
- **Answer hallucination:** Identifies when the model generates information not supported by the retrieved context.

The evaluation process is described as essential for benchmarking RAG systems before moving to production. The article also notes the architecture of RAG (vector database for retrieval, prompt composition, and LLM generation) and emphasizes the importance of metrics that separately target retrieval and generation components for a comprehensive assessment.

-----

-----

-----

### Source [57]: https://arxiv.org/html/2405.07437v2

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: This arXiv survey introduces the **Auepora Unified Evaluation Process**, a systematic methodology for assessing RAG systems. The framework is structured around three core questions:

- **What to Evaluate?** (Target): Defines the evaluation direction, such as relevance or faithfulness.
- **How to Evaluate?** (Dataset): Focuses on the construction and selection of datasets used for benchmarking.
- **How to Measure?** (Metric): Details the specific metrics that correspond to the evaluation targets and datasets.

Auepora emphasizes systematically covering all possible pairs between **Evaluable Outputs (EOs)** and **Ground Truths (GTs)**, aiming for a holistic approach. The process is designed to provide clarity and accessibility when comparing RAG benchmarks, focusing on quantifiable metrics for both the retrieval and generation components, such as **relevance, accuracy, and faithfulness**.

-----

-----

-----

### Source [58]: https://cloud.google.com/blog/products/ai-machine-learning/optimizing-rag-retrieval

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: Google Cloud describes an evaluation framework that supports both **model-based** and **computation-based** metrics:

- **Model-based metrics** involve using an evaluator model to score RAG outputs on criteria such as relevance and faithfulness. These are divided into:
  - **Pointwise metrics:** Assign numerical scores to single outputs.
  - **Pairwise metrics:** Compare two outputs to determine which is superior.

- **Computation-based metrics** use mathematical comparisons between the RAG output and reference answers, such as **ROUGE** and **BLEU** scores.

The framework also recommends creating a "golden" set of queries that reflect key use cases, including a variety of query types. The **Vertex AI generative AI evaluation framework** is highlighted for rapidly implementing and testing multiple metrics, supporting a fast feedback loop for iterative improvement.

-----

-----

-----

### Source [59]: https://docs.llamaindex.ai/en/stable/examples/evaluation/RAGChecker/

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: **RAGChecker** is presented as a **fine-grained evaluation framework** for RAG systems, offering metrics for both retrieval and generation:

- **Overall Metrics:**
  - **Precision:** Proportion of correct claims in the generated response.
  - **Recall:** Proportion of ground truth claims covered by the response.
  - **F1 Score:** Harmonic mean of precision and recall.

- **Retriever Metrics:**
  - **Claim Recall:** Fraction of ground truth claims present in the retrieved context.
  - **Context Precision:** Fraction of retrieved context that is actually relevant.

- **Generator Metrics:** (details not fully listed in the snippet, but implied to focus on accuracy and relevance)

RAGChecker emphasizes claim-level entailment checking, providing actionable insights into both retrieval effectiveness and generation accuracy, making it suitable for diagnosing and improving end-to-end RAG performance.

-----

-----

-----

### Source [60]: https://www.pinecone.io/learn/series/vector-databases-in-production-for-busy-engineers/rag-evaluation/

Query: What are the most effective evaluation frameworks and key metrics (e.g., faithfulness, context relevance, answer relevance) for assessing the end-to-end performance of a production RAG system?

Answer: This source recommends frameworks and metrics based on the RAG use case:

- For **initial RAG evaluations**, **RAGAS** is suggested, focusing on:
  - **Average Precision (AP):** Assesses the precision of the retrieval phase.
  - **Faithfulness:** Measures how accurately the generated response aligns with the retrieved context.

RAGAS is particularly useful when reference data is scarce and prioritizes how well the system's responses are grounded in the provided context. The emphasis is on early-stage evaluation, especially for environments where comprehensive ground truth annotations are not available.

-----

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>5 Chunking Strategies For RAG</summary>

# 5 Chunking Strategies For RAG

...explained in a single frame.

### 5 Chunking Strategies For RAG

Here’s the typical workflow of a RAG application:https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6878b8fa-5e74-45a1-9a89-5aab92889126_2366x990.gifRAG: Store additional information as vectors, match the incoming query to those vectors, and feed the most similar info to the LLM along with the query.

Since the additional document(s) can be pretty large, step 1 also involves chunking, wherein a large document is divided into smaller/manageable pieces.https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdeab4ef3-d3ec-4459-8004-ceffe81652ca_1829x392.png

This step is crucial since it ensures the text fits the input size of the embedding model.

Moreover, it enhances the efficiency and accuracy of the retrieval step, which directly impacts the quality of generated responses ( [we discussed this yesterday](https://www.dailydoseofds.com/bi-encoders-and-cross-encoders-for-sentence-pair-similarity-scoring-part-1/)).

Here are five chunking strategies for RAG:https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F92c70184-ba0f-4877-9a55-e4add0e311ad_870x1116.gif

Let’s understand them today!

> _Note: Yesterday, we discussed techniques to build robust NLP systems that rely on pairwise content similarity (RAG is one of them). Read here in case you missed it:_ [**_Bi-encoders and Cross-encoders for Sentence Pair Similarity Scoring – Part 1_**](https://www.dailydoseofds.com/bi-encoders-and-cross-encoders-for-sentence-pair-similarity-scoring-part-1/) _._

* * *

#### 1) Fixed-size chunking

The most intuitive and straightforward way to generate chunks is by splitting the text into uniform segments based on a pre-defined number of characters, words, or tokens.https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98c422a0-f0e2-457c-a256-4476a56a601f_943x232.png

Since a direct split can disrupt the semantic flow, it is recommended to maintain some overlap between two consecutive chunks (the blue part above).

This is simple to implement. Also, since all chunks are of equal size, it simplifies batch processing.

But there is a big problem. This usually breaks sentences (or ideas) in between. Thus, important information will likely get distributed between chunks.

* * *

#### 2) Semantic chunking

The idea is simple.https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6ad83a6-2879-4c77-9e49-393f16577aef_1066x288.gif

- Segment the document based on meaningful units like sentences, paragraphs, or thematic sections.
- Next, create embeddings for each segment.
- Let’s say I start with the first segment and its embedding.
  - If the first segment’s embedding has a high cosine similarity with that of the second segment, both segments form a chunk.
  - This continues until cosine similarity drops significantly.
  - The moment it does, we start a new chunk and repeat.

Here’s what the output could look like:https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74037e11-362d-4ea2-8ee2-ee85ab013523_963x231.png

Unlike fixed-size chunks, this maintains the natural flow of language and preserves complete ideas.

Since each chunk is richer, it improves the retrieval accuracy, which, in turn, produces more coherent and relevant responses by the LLM.

A minor problem is that it depends on a threshold to determine if cosine similarity has dropped significantly, which can vary from document to document.

* * *

#### 3) Recursive chunking

This is also simple.https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4009caa-34fc-48d6-8102-3d0f6f2c1386_1066x316.gif

First, chunk based on inherent separators like paragraphs, or sections.

Next, split each chunk into smaller chunks if the size exceeds a pre-defined chunk size limit. If, however, the chunk fits the chunk-size limit, no further splitting is done.

Here’s what the output could look like:https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0e40cc1-996f-48f4-9306-781b112536e4_984x428.png

As shown above:

- First, we define two chunks (the two paragraphs in purple).
- Next, paragraph 1 is further split into smaller chunks.

Unlike fixed-size chunks, this approach also maintains the natural flow of language and preserves complete ideas.

However, there is some extra overhead in terms of implementation and computational complexity.

* * *

#### 4) Document structure-based chunking

This is another intuitive approach.https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe8febecd-ee68-42ff-ab06-41a0a3a43cd3_1102x306.gif

It utilizes the inherent structure of documents, like headings, sections, or paragraphs, to define chunk boundaries.

This way, it maintains structural integrity by aligning with the document’s logical sections.

Here’s what the output could look like:https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40bdaf3b-601d-4357-bc7f-89b47f812097_1025x663.png

That said, this approach assumes that the document has a clear structure, which may not be true.

Also, chunks may vary in length, possibly exceeding model token limits. You can try merging it with recursive splitting.

* * *

#### 5) LLM-based chunkinghttps://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d1b6d60-8956-4030-8525-d899ee61a9d5_1140x198.gif

Since every approach has upsides and downsides, why not use the LLM to create chunks?

The LLM can be prompted to generate semantically isolated and meaningful chunks.

Quite evidently, this method will ensure high semantic accuracy since the LLM can understand context and meaning beyond simple heuristics (used in the above four approaches).

The only problem is that it is the most computationally demanding chunking technique of all five techniques discussed here.

Also, since LLMs typically have a limited context window, that is something to be taken care of.

* * *

Each technique has its own advantages and trade-offs.

I have observed that semantic chunking works pretty well in many cases, but again, you need to test.

The choice will heavily depend on the nature of your content, the capabilities of the embedding model, computational resources, etc.

We shall be doing a hands-on demo of these strategies pretty soon.

In the meantime, in case you missed it, yesterday, we discussed techniques to build robust NLP systems that rely on pairwise content similarity (RAG is one of them).

Read here: [**Bi-encoders and Cross-encoders for Sentence Pair Similarity Scoring – Part 1**](https://www.dailydoseofds.com/bi-encoders-and-cross-encoders-for-sentence-pair-similarity-scoring-part-1/).

👉 Over to you: What other chunking strategies do you know?

</details>

<details>
<summary>Many LLM applications implement a particular control flow of steps before and / or after LLM calls. As an example, [RAG](https://github.com/langchain-ai/rag-from-scratch) performs retrieval of documents relevant to a user question, and passes those documents to an LLM in order to ground the model's response in the provided document context.</summary>

Many LLM applications implement a particular control flow of steps before and / or after LLM calls. As an example, [RAG](https://github.com/langchain-ai/rag-from-scratch) performs retrieval of documents relevant to a user question, and passes those documents to an LLM in order to ground the model's response in the provided document context.

Instead of hard-coding a fixed control flow, we sometimes want LLM systems that can pick their own control flow to solve more complex problems! This is one definition of an [agent](https://blog.langchain.dev/what-is-an-agent/): _an agent is a system that uses an LLM to decide the control flow of an application._ There are many ways that an LLM can control application:

- An LLM can route between two potential paths
- An LLM can decide which of many tools to call
- An LLM can decide whether the generated answer is sufficient or more work is needed

As a result, there are many different types of [agent architectures](https://blog.langchain.dev/what-is-a-cognitive-architecture/), which give an LLM varying levels of control.https://langchain-ai.github.io/langgraph/concepts/img/agent_types.png

## Router

A router allows an LLM to select a single step from a specified set of options. This is an agent architecture that exhibits a relatively limited level of control because the LLM usually focuses on making a single decision and produces a specific output from a limited set of pre-defined options. Routers typically employ a few different concepts to achieve this.

### Structured Output

Structured outputs with LLMs work by providing a specific format or schema that the LLM should follow in its response. This is similar to tool calling, but more general. While tool calling typically involves selecting and using predefined functions, structured outputs can be used for any type of formatted response. Common methods to achieve structured outputs include:

1. Prompt engineering: Instructing the LLM to respond in a specific format via the system prompt.
2. Output parsers: Using post-processing to extract structured data from LLM responses.
3. Tool calling: Leveraging built-in tool calling capabilities of some LLMs to generate structured outputs.

Structured outputs are crucial for routing as they ensure the LLM's decision can be reliably interpreted and acted upon by the system. Learn more about [structured outputs in this how-to guide](https://python.langchain.com/docs/how_to/structured_output/).

## Tool-calling agent

While a router allows an LLM to make a single decision, more complex agent architectures expand the LLM's control in two key ways:

1. Multi-step decision making: The LLM can make a series of decisions, one after another, instead of just one.
2. Tool access: The LLM can choose from and use a variety of tools to accomplish tasks.

[ReAct](https://arxiv.org/abs/2210.03629) is a popular general purpose agent architecture that combines these expansions, integrating three core concepts.

1. [Tool calling](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling): Allowing the LLM to select and use various tools as needed.
2. [Memory](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#memory): Enabling the agent to retain and use information from previous steps.
3. [Planning](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#planning): Empowering the LLM to create and follow multi-step plans to achieve goals.

This architecture allows for more complex and flexible agent behaviors, going beyond simple routing to enable dynamic problem-solving with multiple steps. Unlike the original [paper](https://arxiv.org/abs/2210.03629), today's agents rely on LLMs' [tool calling](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling) capabilities and operate on a list of [messages](https://langchain-ai.github.io/langgraph/concepts/low_level/#why-use-messages).

In LangGraph, you can use the prebuilt [agent](https://langchain-ai.github.io/langgraph/agents/agents/#2-create-an-agent) to get started with tool-calling agents.

### Tool calling

Tools are useful whenever you want an agent to interact with external systems. External systems (e.g., APIs) often require a particular input schema or payload, rather than natural language. When we bind an API, for example, as a tool, we give the model awareness of the required input schema. The model will choose to call a tool based upon the natural language input from the user and it will return an output that adheres to the tool's required schema.

[Many LLM providers support tool calling](https://python.langchain.com/docs/integrations/chat/) and [tool calling interface](https://blog.langchain.dev/improving-core-tool-interfaces-and-docs-in-langchain/) in LangChain is simple: you can simply pass any Python `function` into `ChatModel.bind_tools(function)`.https://langchain-ai.github.io/langgraph/concepts/img/tool_call.png

### Memory

[Memory](https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/) is crucial for agents, enabling them to retain and utilize information across multiple steps of problem-solving. It operates on different scales:

1. [Short-term memory](https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/#add-short-term-memory): Allows the agent to access information acquired during earlier steps in a sequence.
2. [Long-term memory](https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/#add-long-term-memory): Enables the agent to recall information from previous interactions, such as past messages in a conversation.

LangGraph provides full control over memory implementation:

- [`State`](https://langchain-ai.github.io/langgraph/concepts/low_level/#state): User-defined schema specifying the exact structure of memory to retain.
- [`Checkpointer`](https://langchain-ai.github.io/langgraph/concepts/persistence/#checkpoints): Mechanism to store state at every step across different interactions within a session.
- [`Store`](https://langchain-ai.github.io/langgraph/concepts/persistence/#memory-store): Mechanism to store user-specific or application-level data across sessions.

This flexible approach allows you to tailor the memory system to your specific agent architecture needs. Effective memory management enhances an agent's ability to maintain context, learn from past experiences, and make more informed decisions over time. For a practical guide on adding and managing memory, see [Memory](https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/).

### Planning

In a tool-calling [agent](https://langchain-ai.github.io/langgraph/agents/overview/#what-is-an-agent), an LLM is called repeatedly in a while-loop. At each step the agent decides which tools to call, and what the inputs to those tools should be. Those tools are then executed, and the outputs are fed back into the LLM as observations. The while-loop terminates when the agent decides it has enough information to solve the user request and it is not worth calling any more tools.

## Custom agent architectures

While routers and tool-calling agents (like ReAct) are common, [customizing agent architectures](https://blog.langchain.dev/why-you-should-outsource-your-agentic-infrastructure-but-own-your-cognitive-architecture/) often leads to better performance for specific tasks. LangGraph offers several powerful features for building tailored agent systems:

### Human-in-the-loop

Human involvement can significantly enhance agent reliability, especially for sensitive tasks. This can involve:

- Approving specific actions
- Providing feedback to update the agent's state
- Offering guidance in complex decision-making processes

Human-in-the-loop patterns are crucial when full automation isn't feasible or desirable. Learn more in our [human-in-the-loop guide](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/).

### Parallelization

Parallel processing is vital for efficient multi-agent systems and complex tasks. LangGraph supports parallelization through its [Send](https://langchain-ai.github.io/langgraph/concepts/low_level/#send) API, enabling:

- Concurrent processing of multiple states
- Implementation of map-reduce-like operations
- Efficient handling of independent subtasks

For practical implementation, see our [map-reduce tutorial](https://langchain-ai.github.io/langgraph/how-tos/graph-api/#map-reduce-and-the-send-api)

### Subgraphs

[Subgraphs](https://langchain-ai.github.io/langgraph/concepts/subgraphs/) are essential for managing complex agent architectures, particularly in [multi-agent systems](https://langchain-ai.github.io/langgraph/concepts/multi_agent/). They allow:

- Isolated state management for individual agents
- Hierarchical organization of agent teams
- Controlled communication between agents and the main system

Subgraphs communicate with the parent graph through overlapping keys in the state schema. This enables flexible, modular agent design. For implementation details, refer to our [subgraph how-to guide](https://langchain-ai.github.io/langgraph/how-tos/subgraph/).

### Reflection

Reflection mechanisms can significantly improve agent reliability by:

1. Evaluating task completion and correctness
2. Providing feedback for iterative improvement
3. Enabling self-correction and learning

While often LLM-based, reflection can also use deterministic methods. For instance, in coding tasks, compilation errors can serve as feedback. This approach is demonstrated in [this video using LangGraph for self-corrective code generation](https://www.youtube.com/watch?v=MvNdgmM7uyc).

By leveraging these features, LangGraph enables the creation of sophisticated, task-specific agent architectures that can handle complex workflows, collaborate effectively, and continuously improve their performance.

</details>

<details>
<summary>In the current world where everything is running with and for AI, retrieval-augmented generation (RAG) systems have become essential for handling simple queries and generating contextually relevant responses. However, as ever evolving human we are, the need for complex, autonomous problem-solving has emerged. Here I present, behold the mighty: **AI Agents** — autonomous entities that redefine how we interact with technology. In simple terms, it's a sophisticated Graph and even simpler, complex and advanced `for` loops which use LLMs as the core of working.</summary>

In the current world where everything is running with and for AI, retrieval-augmented generation (RAG) systems have become essential for handling simple queries and generating contextually relevant responses. However, as ever evolving human we are, the need for complex, autonomous problem-solving has emerged. Here I present, behold the mighty: **AI Agents** — autonomous entities that redefine how we interact with technology. In simple terms, it's a sophisticated Graph and even simpler, complex and advanced `for` loops which use LLMs as the core of working.

#### What good are these then?

- **Autonomous Problem-Solving**: AI Agents operate independently, driven by goals rather than specific inputs, and adapt dynamically to new information and environments.
- **Multi-Step Task Execution**: They perform complex, multi-step tasks, maintain state across interactions, and utilize tools like machine learning and rule-based systems to achieve optimal outcomes.
- **Versatile Capabilities**: From browsing the internet and managing apps to conducting financial transactions and controlling devices, AI Agents are reshaping intelligent automation.

#### What's LangGraph?

There are many tools available in the market to build agents and among the famous ones are [LangGraph](https://www.langchain.com/langgraph?ref=blog.lancedb.com), [AutoGen](https://github.com/microsoft/autogen?ref=blog.lancedb.com), [Swarm](https://github.com/openai/swarm?ref=blog.lancedb.com), [CrewAI](https://github.com/crewAIInc/crewAI?ref=blog.lancedb.com) etc etc. You can choose any but we chose this one for granular control and Open Source. It basically create a Graph for your workflow and inside your Graph are:

1. `State` : `Pydantic Models` or `Typed Dict` to hold your variables and used for message passing
2. `Node` : It is just a function that does some work. It accepts a `State` object and modifies that State
3. `Tools` : There are pure Python functions or `Pydantic` models which your agents can call. You use the tools to do some Retrieval, Web Search, Calculator, Cal some APIs etc etc. You just have to write the definition of what it does and model will understand which tool **CAN** be used at any point of time.
4. `Edge` : You have pre-defined flows which tell you the execution order of functions (Nodes) in our case
5. `Conditional Edges` or `Routers`: Instead of fixing in previous point, we make it conditional. So If you are at `Node-N`, you decide based on a condition where you want to go to out of Nodes `N_i....N_x`

**Where does the RAG Come in?**

You remember our `tools` and `Nodes` above? So we can use RAG either as a tool OR a Node. You'll see most of the tutorials using RAG as a tool however I want to show how can you use it as a `Node` and that too conditional.

### Lets build a use case: Email Agent

What is does is:

1. Fetch the unread emails from your inbox
2. Look at the type of email
3. If it is a Policy related email, it'll use RAG to refer to policies to Draft the Email otherwise just create a normal draft. If it's a SPAM or something else, just discard it..
4. Proofread the Draft. If it's good to send, send it else send it to redraft again. Ideally, you'd let the proof reader node know what are the criteria and then you'd send the reasoning why it was rejected so that Drafting model improves it. That would be out of scope of this blog (wait for next one 😄)
5. Once you get Okay from proof reader, send a reply. Ideally, you want an `interrupt` so that the human in the loop can review and THEN you send it but again, it's too much to cover here.
6. For sending, we just `print` for now

**_And Yes, All of it is Autonomous_**

Let's get some policies and build our RAG on top of that

```python
pip install -U colorama langgraph langchain-community langchain-openai langchain-anthropic tavily-python pandas openai lancedb sentence-transformers

```

```python
from langchain_core.messages import ToolMessage, SystemMessage, AIMessage, HumanMessage
from langchain_core.runnables import RunnableLambda
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import Runnable, RunnableConfig
from typing import TypedDict, Annotated
from langgraph.graph.message import AnyMessage, add_messages
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import tools_condition
import torch

# ------------ Vector Search ----------------

import lancedb, re, requests
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
import numpy as np
from langchain_core.tools import tool

# ------- Vecot DB using Lance DB ------------
model = get_registry().get("sentence-transformers").create(name="BAAI/bge-small-en-v1.5", device="cuda" if torch.cuda.is_available() else "cpu")

class Policy(LanceModel):
    text: str = model.SourceField()
    vector: Vector(model.ndims()) = model.VectorField()

response = requests.get(
    "https://storage.googleapis.com/benchmarks-artifacts/travel-db/swiss_faq.md"
)
response.raise_for_status()
faq_text = response.text

class VectorStoreRetriever:
    def __init__(self, db_path:str, table_name:str, model, docs: list, schema, ):
        self.db = lancedb.connect(db_path)
        self.table = self.db.create_table(table_name, schema = schema)
        self.table.add([{"text": txt} for txt in re.split(r"(?=\n##)", faq_text)])

    def query(self, query: str, k: int = 5) -> list[dict]:
        result = self.table.search(query).limit(k).to_list()
        return [{"page_content": item["text"], "similarity": 1- item["_distance"]} for item in result]

retriever = VectorStoreRetriever("./lancedb", "company_policy", model, faq_text, Policy)
```

Now that we have our documents, ready, let's build some helpers including a Dummy Function to fetch your email. In real world, you replace it with your logic and APIs

```python
from typing import Optional, List
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langgraph.graph import END, StateGraph, START
import os
from dotenv import load_dotenv
import random
from typing import Annotated
from langgraph.graph.message import AnyMessage, add_messages
from typing_extensions import TypedDict
from langchain_core.messages import ToolMessage, SystemMessage, AIMessage, HumanMessage
from langchain_core.runnables import RunnableLambda
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import Runnable, RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import tools_condition
import lancedb, re, requests
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
import numpy as np
from langchain_core.tools import tool
from google.colab import userdata # use os.environ.get()
import os
from colorama import Fore, Style

memory = MemorySaver() # it'll save the all the states and history corresponding to a `thread_id`. We can get previous conversations if we use memory

# llm = ChatOpenAI(model="gpt-3.5-turbo") # use any
def setup_llm():
    return AzureChatOpenAI(
        api_key=userdata.get("AZURE_OPENAI_API_KEY"),
        api_version=userdata.get("AZURE_OPENAI_API_MODEL_VERSION"),
        azure_endpoint=userdata.get("AZURE_OPENAI_API_ENDPOINT"),
        azure_deployment=userdata.get("AZURE_OPENAI_API_DEPLOYMENT_NAME"),
        temperature=0.7
    )

def create_dummy_random_emails():
    items = [\
        {\
            "subject": "Invoice Request for Recent Flight Booking",\
            "body": "Dear SWISS Team, I recently booked a flight with SWISS (Booking Reference: LX123456) and would like to request an invoice for my records. Could you please guide me on how to obtain it? Thank you, Anna Müller"\
        },\
        {\
            "subject": "Rebooking Inquiry for Upcoming Flight",\
            "body": "Hello, I need to change the travel dates for my flight (Booking Reference: LX789012). Can you confirm if this is possible and what fees might apply? Best regards, John Smith"\
        },\
        {\
            "subject": "Cancellation of Flight LX345678",\
            "body": "Hi SWISS Customer Service, I need to cancel my flight (Booking Reference: LX345678) due to unforeseen circumstances. Could you please explain the cancellation process and any associated fees? Sincerely, Maria Gonzalez"\
        },\
        {\
            "subject": "Request for Special Invoice for Italy",\
            "body": "Dear SWISS, I booked a flight originating in Italy and require a special invoice for tax purposes. Can you assist me with this request? Kind regards, Luca Rossi"\
        },\
        {\
            "subject": "Payment Issue with Credit Card",\
            "body": "Hello, I tried to pay for my booking using my Visa card, but the payment failed. Can you confirm if the issue is with my card or the payment system? Thanks, Emily Brown"\
        },\
        {\
            "subject": "Refund Status for Cancelled Flight",\
            "body": "Dear SWISS, I cancelled my flight (Booking Reference: LX456789) two weeks ago and was told I would receive a refund. Could you provide an update on the status? Best, David Johnson"\
        },\
        {\
            "subject": "Seat Reservation Inquiry",\
            "body": "Hi, I have a booking (Reference: LX567890) and would like to confirm if my seat reservation will be retained after a rebooking. Please advise. Regards, Sophie Lee"\
        },\
        {\
            "subject": "Upgrade Request for Economy Flex Fare",\
            "body": "Dear SWISS, I booked an Economy Flex fare and would like to upgrade to Business Class. Can you guide me on how to proceed? Thank you, Michael Chen"\
        },\
        {\
            "subject": "Group Booking Inquiry",\
            "body": "Hello, I am planning to book flights for a group of 12 passengers. Can you provide details on group booking options and any discounts? Best, Sarah Wilson"\
        },\
        {\
            "subject": "Issue with Online Booking Platform",\
            "body": "Hi SWISS, I am unable to see my recent booking in my profile on the SWISS website. Can you help resolve this issue? Regards, Thomas Anderson"\
        }\
    ]
    chosen_items = [random.choice(items) for _ in range(random.randint(0,2))]
    return [Email(id=str(i), sender="some_user@example.mail", subject=item["subject"], body=item["body"]) for i, item in enumerate(chosen_items)]

```

**Let's setup our Email Agent:**

First one is our `Email` object which basically tells us what an Email is. The second one is the `State` which will be used inside the graph

```python
class Email(BaseModel):
    id: str
    sender: str
    subject: str
    body: str
    final_reply: str = ""
    status: str = "pending"  # pending, sent, failed, skipped
    failure_reason: str = ""

class EmailState(BaseModel):
    emails: List[Email] = [] # List of the Unread above Email class
    processed_emails: List[Email] = [] # Final emails with the replies and denial reason
    current_email: Optional[Email] = None # Pop one everytime from the above list
    policy_context: Optional[str] = "" # Rag context for CURRENT email
    draft: str = "" # Current Draft of the Current Email
    trials: int = 0 # Trails done for Draft <-> Proof Read for current email
    allowed_trials: int = 3 # do Drft <-> Proof Read a max of 3 times
    sendable: bool = False # send the current email if True
    exit:bool = False # There are no unread emails left
```

Let's setup our Agent Classes and simple functions. Names and Prompts are self explanatory. Out **LanceDB** RAG is used in the function `lookup_policy` to fetch policies if the query requires searching the internal policies.

```python
class EmailAgent:
    def __init__(self):
        self.llm = setup_llm() # Replace with your LLM you want

    def fetch_unread_emails(self) -> List[Email]:
      """
      Replace this with your Email LOGIC
      """
      return create_dummy_random_emails()

    def lookup_policy(self, subject: str, body:str) -> str:
        """Always Consult the company policies to answer the queries.
        Use this for drafting the emails"""
        prompt = PromptTemplate(template="Identify whether the given email is policy related or not. Identify if the email requires info which might be in the policy documents.\n\nSubject: {subject}\n\nBody:\n{body}\n\n. Do not output any reasoning etc. Strictly reply with Yes/No", input_variables=["email"])
        chain = prompt | self.llm
        response = chain.invoke({"subject": subject, "body": body})
        policy_related = response.content.strip().lower() == "yes"
        if policy_related:
          docs = retriever.query(f"Email Subject: {subject}\n\nEmail Body:\n{body}", k=2)
          return "\nPolicy Context:" + "\n\n".join([doc["page_content"] for doc in docs])
        return ""

    def draft_email(self, email_subject:str, email_body: str, email_context:str = "") -> str:
        if not email_context:
          prompt = PromptTemplate(template="You are a specialised chat agent named Saleem Shady' working for SWISS Airline. Write a well professional response to this user email:\n\nEmail Subject: {email_subject}\n\nEmail Body:\n{email_body}\n\nResponse:", input_variables=["email"])
        else:
          prompt = PromptTemplate(template="You are a specialised chat agent named Saleem Shady' working for SWISS Airline. Write a well professional response to this user email given the Context (which may or may not be required in answering)\n\n{email_context}\n\nEmail Subject: {email_subject}\n\nEmail Body:\n{email_body}\n\nResponse:", input_variables=["email"])

        chain = prompt | self.llm
        response = chain.invoke({"email_subject":email_subject,"email_body": email_body, "email_context": email_context})
        return response.content

    def validate_draft(self, initial_email: str, draft_email: str) -> bool:
        prompt = PromptTemplate(template="You are a Email Proofreader. Review this response:\n\nOriginal Email:\n{initial_email}\n\nDraft Response:\n{draft_email}\n\nIs this mail ready to send? Do not give your reasoning or views. Reply only with (Yes/No):", input_variables=["initial_email", "draft_email"])
        chain = prompt | self.llm
        response = chain.invoke({"initial_email": initial_email, "draft_email": draft_email})
        return response.content.strip().lower() == "yes"

```

Now let's setup our main `Workflow` which is why you came here. The below functions are Either `Nodes` or `Routers` . Which we'll get to know when we build the nodes and define edges

```python

    agent = EmailAgent()

    def fetch_emails(state: EmailState) -> EmailState:
        emails = agent.fetch_unread_emails()
        state.emails = emails
        return state

    def process_next_email(state: EmailState) -> EmailState:
      if state.emails:
          state.current_email = state.emails.pop(0)
          state.policy_context = agent.lookup_policy(state.current_email.subject, state.current_email.body)
      else:
          state.exit = True
      return state

    def draft_email(state: EmailState) -> EmailState:
        if state.current_email:
            state.draft = agent.draft_email(state.current_email.subject, state.current_email.body, state.policy_context)
            state.trials += 1
        return state

    def validate_draft(state: EmailState) -> EmailState:
        if state.current_email and state.draft:
            state.sendable = agent.validate_draft(state.current_email.body, state.draft)
        return state

    def decide_next_step(state: EmailState) -> str:
        if state.sendable:
            print("\n\n-----------------------Sending Email ---------------\n\n")
            return "send"
        elif state.trials >= state.allowed_trials:
            state.current_email.status = "failed"
            state.current_email.failure_reason = "Failed after 3 attempts"
            print("\n\n*********************** Draft Failed after Max Tries ******************** \n\n")
            return "stop"
        else:
            return "rewrite"

    def send_or_skip_email(state: EmailState) -> EmailState:
        if state.current_email.status != "failed":
            print(f"\n\nSending email: {state.draft}")
            state.current_email.final_reply = state.draft
            state.current_email.status = "sent"
            state.processed_emails.append(state.current_email)

        # Reset state for the next email
        state.current_email = None
        state.draft = ""
        state.trials = 0
        state.policy_context = ""
        return state
```

Let's Define the `Nodes` and `Edges / Conditional Edges`

```python
    workflow.add_node("fetch_emails", fetch_emails)
    workflow.add_node("process_next_email", process_next_email)
    workflow.add_node("draft_email", draft_email)
    workflow.add_node("validate_draft", validate_draft)
    workflow.add_node("send_or_skip_email", send_or_skip_email)

    workflow.add_edge(START, "fetch_emails")
    workflow.add_edge("fetch_emails", "process_next_email")

    workflow.add_conditional_edges(
        "process_next_email",
        lambda state: END if state.exit else "draft_email" ,
        {"draft_email": "draft_email", END: END}
        )

    workflow.add_edge("draft_email", "validate_draft")

    workflow.add_conditional_edges(
        "validate_draft",
        decide_next_step,
        {"send": "send_or_skip_email", "rewrite": "draft_email", "stop": "send_or_skip_email"}
    )

    workflow.add_edge("send_or_skip_email", "process_next_email")

    compiled_email_subgraph = workflow.compile()
```

Want to see how our graph looks?

```python
initial_state = EmailState()

from IPython.display import Image, display
try:
    display(Image(compiled_email_subgraph.get_graph(xray=True).draw_mermaid_png()))
except Exception:
    pass
```https://blog.lancedb.com/content/images/2025/01/download.png

You can match the graph working with what we discussed the in the workflow. Let's put it to work. (Uncomment if you want to see the `State` at each point)

```python
print(Fore.GREEN + "Starting workflow..." + Style.RESET_ALL)
for output in compiled_email_subgraph.stream(initial_state):
    for key, value in output.items():
        print(Fore.CYAN + f"Finished running: {key}" + Style.RESET_ALL)
        # print(Fore.YELLOW + f"State after {key}:" + Style.RESET_ALL)
        # print(value)
```https://blog.lancedb.com/content/images/2025/01/Screenshot-from-2025-01-19-13-42-50.png

You see, one failed after 3 times and one got sent successfulAgentic RAG using LangGraph: Build autonomous Customer support agently. Which means that you need to tweak your prompts, add the validator reasoning and guidance etc according to the data and use case

</details>

<details>
<summary>Agentic RAG With LangGraph and Qdrant</summary>

# Agentic RAG With LangGraph and Qdrant

Traditional Retrieval-Augmented Generation (RAG) systems follow a straightforward path: query → retrieve → generate. Sure, this works well for many scenarios. But let’s face it—this linear approach often struggles when you’re dealing with complex queries that demand multiple steps or pulling together diverse types of information.

[Agentic RAG](https://qdrant.tech/articles/agentic-rag/) takes things up a notch by introducing AI agents that can orchestrate multiple retrieval steps and smartly decide how to gather and use the information you need. Think of it this way: in an Agentic RAG workflow, RAG becomes just one powerful tool in a much bigger and more versatile toolkit.

By combining LangGraph’s robust state management with Qdrant’s cutting-edge vector search, we’ll build a system that doesn’t just answer questions—it tackles complex, multi-step information retrieval tasks with finesse.

## What We’ll Build

We’re building an AI agent to answer questions about Hugging Face and Transformers documentation using LangGraph. At the heart of our AI agent lies LangGraph, which acts like a conductor in an orchestra. It directs the flow between various components—deciding when to retrieve information, when to perform a web search, and when to generate responses.

The components are: two Qdrant vector stores and the Brave web search engine. However, our agent doesn’t just blindly follow one path. Instead, it evaluates each query and decides whether to tap into the first vector store, the second one, or search the web.

This selective approach gives your system the flexibility to choose the best data source for the job, rather than being locked into the same retrieval process every time, like traditional RAG. While we won’t dive into query refinement in this tutorial, the concepts you’ll learn here are a solid foundation for adding that functionality down the line.

## Workflowhttps://qdrant.tech/documentation/examples/agentic-rag-langgraph/image1.png

| **Step** | **Description** |
| --- | --- |
| **1\. User Input** | You start by entering a query or request through an interface, like a chatbot or a web form. This query is sent straight to the AI Agent, the brain of the operation. |
| **2\. AI Agent Processes the Query** | The AI Agent analyzes your query, figuring out what you’re asking and which tools or data sources will best answer your question. |
| **3\. Tool Selection** | Based on its analysis, the AI Agent picks the right tool for the job. Your data is spread across two vector databases, and depending on the query, it chooses the appropriate one. For queries needing real-time or external web data, the agent taps into a web search tool powered by BraveSearchAPI. |
| **4\. Query Execution** | The AI Agent then puts its chosen tool to work:<br>\- **RAG Tool 1** queries Vector Database 1.<br>\- **RAG Tool 2** queries Vector Database 2.<br>\- **Web Search Tool** dives into the internet using the search API. |
| **5\. Data Retrieval** | The results roll in:<br>\- Vector Database 1 and 2 return the most relevant documents for your query.<br>\- The Web Search Tool provides up-to-date or external information. |
| **6\. Response Generation** | Using a text generation model (like GPT), the AI Agent crafts a detailed and accurate response tailored to your query. |
| **7\. User Response** | The polished response is sent back to you through the interface, ready to use. |

## The Stack

The architecture taps into cutting-edge tools to power efficient Agentic RAG workflows. Here’s a quick overview of its components and the technologies you’ll need:

- **AI Agent:** The mastermind of the system, this agent parses your queries, picks the right tools, and integrates the responses. We’ll use OpenAI’s _gpt-4o_ as the reasoning engine, managed seamlessly by LangGraph.
- **Embedding:** Queries are transformed into vector embeddings using OpenAI’s _text-embedding-3-small_ model.
- **Vector Database:** Embeddings are stored and used for similarity searches, with Qdrant stepping in as our database of choice.
- **LLM:** Responses are generated using OpenAI’s _gpt-4o_, ensuring answers are accurate and contextually grounded.
- **Search Tools:** To extend RAG’s capabilities, we’ve added a web search component powered by BraveSearchAPI, perfect for real-time and external data retrieval.
- **Workflow Management:** The entire orchestration and decision-making flow is built with LangGraph, providing the flexibility and intelligence needed to handle complex workflows.

Ready to start building this system from the ground up? Let’s get to it!

## Implementation

Before we dive into building our agent, let’s get everything set up.

### Imports

Here’s a list of key imports required:

```python
import os
import json
from typing import Annotated, TypedDict
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langgraph import StateGraph, tool, ToolNode, ToolMessage
from langchain.document_loaders import HuggingFaceDatasetLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import ChatOpenAI
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams
from brave_search import BraveSearch

```

### Qdrant Vector Database Setup

We’ll use **Qdrant Cloud** as our vector store for document embeddings. Here’s how to set it up:

| **Step** | **Description** |
| --- | --- |
| **1\. Create an Account** | If you don’t already have one, head to Qdrant Cloud and sign up. |
| **2\. Set Up a Cluster** | Log in to your account and find the **Create New Cluster** button on the dashboard. Follow the prompts to configure:<br>\- Select your **preferred region**.<br>\- Choose the **free tier** for testing. |
| **3\. Secure Your Details** | Once your cluster is ready, note these details:<br>\- **Cluster URL** (e.g., [https://xxx-xxx-xxx.aws.cloud.qdrant.io](https://xxx-xxx-xxx.aws.cloud.qdrant.io/))<br>\- **API Key** |

Save these securely for future use!

### OpenAI API Configuration

Your OpenAI API key will power both embedding generation and language model interactions. Visit [OpenAI’s platform](https://platform.openai.com/) and sign up for an account. In the API section of your dashboard, create a new API key. We’ll use the text-embedding-3-small model for embeddings and GPT-4 as the language model.

### Brave Search

To enhance search capabilities, we’ll integrate Brave Search. Visit the [Brave API](https://api.search.brave.com/) and complete their API access request process to obtain an API key. This key will enable web search functionality for our agent.

For added security, store all API keys in a .env file.

```json
OPENAI_API_KEY = <your-openai-api-key>
QDRANT_KEY = <your-qdrant-api-key>
QDRANT_URL = <your-qdrant-url>
BRAVE_API_KEY = <your-brave-api-key>

```

Then load the environment variables:

```python
load_dotenv()
qdrant_key = os.getenv("QDRANT_KEY")
qdrant_url = os.getenv("QDRANT_URL")
brave_key = os.getenv("BRAVE_API_KEY")

```

### Document Processing

Before we can create our agent, we need to process and store the documentation. We’ll be working with two datasets from Hugging Face: their general documentation and Transformers-specific documentation.

Here’s our document preprocessing function:

```python
def preprocess_dataset(docs_list):
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=700,
        chunk_overlap=50,
        disallowed_special=()
    )
    doc_splits = text_splitter.split_documents(docs_list)
    return doc_splits

```

This function processes our documents by splitting them into manageable chunks, ensuring important context is preserved at the chunk boundaries through overlap. We’ll use the HuggingFaceDatasetLoader to load the datasets into Hugging Face documents.

```python
hugging_face_doc = HuggingFaceDatasetLoader("m-ric/huggingface_doc","text")
transformers_doc = HuggingFaceDatasetLoader("m-ric/transformers_documentation_en","text")

```

In this demo, we are selecting the first 50 documents from the dataset and passing them to the processing function.

```python
hf_splits = preprocess_dataset(hugging_face_doc.load()[:number_of_docs])
transformer_splits = preprocess_dataset(transformers_doc.load()[:number_of_docs])

```

Our splits are ready. Let’s create a collection in Qdrant to store them.

### Defining the State

In LangGraph, a **state** refers to the data or information stored and maintained at a specific point during the execution of a process or a series of operations. States capture the intermediate or final results that the system needs to keep track of to manage and control the flow of tasks,

LangGraph works with a state-based system. We define our state like this:

```python
class State(TypedDict):
    messages: Annotated[list, add_messages]

```

Let’s build our tools.

### Building the Tools

Our agent is equipped with three powerful tools:

1. **Hugging Face Documentation Retriever**
2. **Transformers Documentation Retriever**
3. **Web Search Tool**

Let’s start by defining a retriever that takes documents and a collection name, then returns a retriever. The query is transformed into vectors using **OpenAIEmbeddings**.

```python
def create_retriever(collection_name, doc_splits):
    vectorstore = QdrantVectorStore.from_documents(
        doc_splits,
        OpenAIEmbeddings(model="text-embedding-3-small"),
        url=qdrant_url,
        api_key=qdrant_key,
        collection_name=collection_name,
    )
    return vectorstore.as_retriever()

```

Both the Hugging Face documentation retriever and the Transformers documentation retriever use this same function. With this setup, it’s incredibly simple to create separate tools for each.

```python
hf_retriever_tool = create_retriever_tool(
    hf_retriever,
    "retriever_hugging_face_documentation",
    "Search and return information about hugging face documentation, it includes the guide and Python code.",
)

transformer_retriever_tool = create_retriever_tool(
    transformer_retriever,
    "retriever_transformer",
    "Search and return information specifically about transformers library",
)

```

For web search, we create a simple yet effective tool using Brave Search:

```python
@tool("web_search_tool")
def search_tool(query):
    search = BraveSearch.from_api_key(api_key=brave_key, search_kwargs={"count": 3})
    return search.run(query)

```

The search\_tool function leverages the BraveSearch API to perform a search. It takes a query, retrieves the top 3 search results using the API key, and returns the results.

Next, we’ll set up and integrate our tools with a language model:

```python
tools = [hf_retriever_tool, transformer_retriever_tool, search_tool]

tool_node = ToolNode(tools=tools)

llm = ChatOpenAI(model="gpt-4o", temperature=0)

llm_with_tools = llm.bind_tools(tools)

```

Here, the ToolNode class handles and orchestrates our tools:

```python
class ToolNode:
    def __init__(self, tools: list) -> None:
        self.tools_by_name = {tool.name: tool for tool in tools}

    def __call__(self, inputs: dict):
        if messages := inputs.get("messages", []):
            message = messages[-1]
        else:
            raise ValueError("No message found in input")

        outputs = []
        for tool_call in message.tool_calls:
            tool_result = self.tools_by_name[tool_call["name"]].invoke(
                tool_call["args"]
            )
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )

        return {"messages": outputs}

```

The ToolNode class handles tool execution by initializing a list of tools and mapping tool names to their corresponding functions. It processes input dictionaries, extracts the last message, and checks for tool\_calls from LLM tool-calling capability providers such as Anthropic, OpenAI, and others.

### Routing and Decision Making

Our agent needs to determine when to use tools and when to end the cycle. This decision is managed by the routing function:

```python
def route(state: State):
    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get("messages", []):
        ai_message = messages[-1]
    else:
        raise ValueError(f"No messages found in input state to tool_edge: {state}")

    if hasattr(ai_message, "tool_calls") and len(ai_message.tool_calls) > 0:
        return "tools"

    return END

```

## Putting It All Together: The Graph

Finally, we’ll construct the graph that ties everything together:

```python
graph_builder = StateGraph(State)

graph_builder.add_node("agent", agent)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "agent",
    route,
    {"tools": "tools", END: END},
)

graph_builder.add_edge("tools", "agent")
graph_builder.add_edge(START, "agent")

```

This is what the graph looks like:https://qdrant.tech/documentation/examples/agentic-rag-langgraph/image2.jpg

Fig. 3: Agentic RAG with LangGraph

### Running the Agent

With everything set up, we can run our agent using a simple function:

```python
def run_agent(user_input: str):
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

```

Now, you’re ready to ask questions about Hugging Face and Transformers! Our agent will intelligently combine information from the documentation with web search results when needed.

For example, you can ask:

```txt
In the Transformers library, are there any multilingual models?

```

The agent will dive into the Transformers documentation, extract relevant details about multilingual models, and deliver a clear, comprehensive answer.

Here’s what the response might look like:

```txt
Yes, the Transformers library includes several multilingual models. Here are some examples:

BERT Multilingual:
Models like `bert-base-multilingual-uncased` can be used just like monolingual models.

XLM (Cross-lingual Language Model):
Models like `xlm-mlm-ende-1024` (English-German), `xlm-mlm-enfr-1024` (English-French), and others use language embeddings to specify the language used at inference.

M2M100:
Models like `facebook/m2m100_418M` and `facebook/m2m100_1.2B` are used for multilingual translation.

MBart:
Models like `facebook/mbart-large-50-one-to-many-mmt` and `facebook/mbart-large-50-many-to-many-mmt` are used for multilingual machine translation across 50 languages.

These models are designed to handle multiple languages and can be used for tasks like translation, classification, and more.

```

## Conclusion

We’ve successfully implemented Agentic RAG. But this is just the beginning—there’s plenty more you can explore to take your system to the next level.

Agentic RAG is transforming how businesses connect data sources with AI, enabling smarter and more dynamic interactions. In this tutorial, you’ve learned how to build an Agentic RAG system that combines the power of LangGraph, Qdrant, and web search into one seamless workflow.

This system doesn’t just stop at retrieving relevant information from Hugging Face and Transformers documentation. It also smartly falls back to web search when needed, ensuring no query goes unanswered. With Qdrant as the vector database backbone, you get fast, scalable semantic search that excels at retrieving precise information—even from massive datasets.

To truly grasp the potential of this approach, why not apply these concepts to your own projects? Customize the template we’ve shared to fit your unique use case, and unlock the full potential of Agentic RAG for your business needs. The possibilities are endless.

</details>

<details>
<summary>⚠️ Error scraping https://www.youtube.com/watch?v=5TLQdNM5pHg: None</summary>

⚠️ Error scraping https://www.youtube.com/watch?v=5TLQdNM5pHg: None

</details>


## Code Sources

_No code sources found._


## YouTube Video Transcripts

_No YouTube video transcripts found._


## Additional Sources Scraped

<details>
<summary>a-complete-guide-to-rag-towards-ai</summary>

If you haven’t heard about RAG from your refrigerator yet, you surely will very soon, so popular this technique has become. Surprisingly, there is a lack of complete guides that consider all the nuances (like relevance assessment, combating hallucinations, etc.), instead of just fragmented pieces. Based on our experience, I have compiled a guide that covers this topic thoroughly.

<Base64-Image-Removed>Image by DALL-E 3

**So, why do we need RAG?**

You could use [LLM](https://academy.towardsai.net/courses/beginner-to-advanced-llm-dev "LLM Dev") models like ChatGPT to create horoscopes (which it does quite successfully), or for something more practical (like work). However, there is a problem: companies typically have a multitude of documents, rules, regulations, etc., about which ChatGPT knows nothing, of course.

**What can be done?**

There are two options: retrain the model with your data or use RAG.

Retraining is long, expensive, and most likely **will not succeed** (don’t worry, it’s not because you’re a bad parent; it’s just that few people can and know how to do it).

The second option is **Retrieval-Augmented Generation** (also known as RAG). Essentially, the idea is simple: take a good existing model (like OpenAI’s), and attach a company information search to it. The model still knows little about your company, but now it has somewhere to look. While not as effective as if it knew everything, it’s sufficient for most tasks.

Here is a basic overview of the RAG structure:

https://miro.medium.com/v2/resize:fit:700/0*4FnEj61Crx9YA-dhRAG structure, image by the author

**The Retriever** is part of the system that searches for information relevant to your query (similarly to how you would search in your own wiki, company documents, or on Google). Typically, a vector database like Qdrant, where all the company’s indexed documents are stored, is used for this purpose, but essentially anything can be used.

**The Generator** receives the data found by the Retriever and uses it (combines, condenses, and extracts only the important information) to provide an answer to the user. This part is usually done using an [LLM](https://academy.towardsai.net/courses/beginner-to-advanced-llm-dev "LLM Dev") like OpenAI. It simply takes all (or part) of the found information and asks to make sense of it and provide an answer.

Here is an example of the simplest implementation of RAG in Python and LangChain.

```
import os
import wget
from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
from langchain import OpenAI
from langchain_community.document_loaders import BSHTMLLoader
from langchain.chains import RetrievalQA

#download War and Peace by Tolstoy
wget.download("http://az.lib.ru/t/tolstoj_lew_nikolaewich/text_0073.shtml")

#load text from html
loader = BSHTMLLoader("text_0073.shtml", open_encoding='ISO-8859-1')
war_and_peace = loader.load()

#init Vector DB
embeddings = OpenAIEmbeddings()

doc_store = Qdrant.from_documents(
 war_and_peace,
 embeddings,
 location=":memory:",
 collection_name="docs",
)

llm = OpenAI()
# ask questions

while True:
 question = input('Your question: ')
 qa = RetrievalQA.from_chain_type(
 llm=llm,
 chain_type="stuff",
 retriever=doc_store.as_retriever(),
 return_source_documents=False,
 )

 result = qa(question)
 print(f"Answer: {result}")
```

It sounds simple, but there’s a **nuance**:

Since the knowledge isn’t hardcoded into the model, the quality of the answers depends heavily on what the Retriever finds and in what form. It’s not a trivial task, as in the typical chaos of company documents, even people usually have a hard time understanding them. Documents and knowledge are generally stored in poorly structured forms, in different places, sometimes as images, charts, handwritten notes, etc. Often, information in one place contradicts information in another, and one has to make sense of all this mess.

Part of the information simply makes no sense without context, such as abbreviations, acronyms adopted by the company, and names and surnames.

What to do?

This is where various search optimizations (aka hacks) come into play. They are applied at different stages of the search. Broadly, the search can be divided into:

- Initial processing and cleaning of the user’s question
- Data searching in repositories
- Ranking of the results obtained from the repositories
- Processing and combining results into an answer
- Evaluating the response
- Applying formatting, stylistic, and tone

Let’s take a detailed look at each stage:

Initial processing of the user’s question

You wouldn’t believe what users write as questions. You can’t count on them being reasonable — the question could be phrased as a demand, statement, complaint, threat, just a single letter, or AN ENTIRE essay the size of “War and Peace.” For example:

https://miro.medium.com/v2/resize:fit:700/0*_zzJBaDyWGgpPL0gImage by the author

What “and”?

or

https://miro.medium.com/v2/resize:fit:700/0*__thyuBVknlrDrpBOnly some enraged Medium readers with their comments might match this. Image by the author

The input needs to be processed, turning it into a query that can be used to search for information. To solve this problem, we need a translator from the user language to the human language. Who could do this? Of course, an **LLM**. Basically, it might look like this:

https://miro.medium.com/v2/resize:fit:700/0*zrXahDMAXECjFNbgGood guess 😂 Image by the author

The simplest option — ask the LLM to reformulate the user’s request. But, depending on your audience, this might not be enough!!!!!1111

Then a slightly more complex technique comes into play — **RAG Fusion**.

**RAG Fusion**

The idea is to ask the LLM to provide several versions of the user’s question, conduct a search based on them, and then combine the results, having ranked them beforehand using some clever algorithm, such as a **Cross-Encoder**. Cross Encoder works quite slowly, but it provides more relevant results, so it’s not practical to use it for information retrieval — however, for ranking a list of found results, it’s quite suitable.

**Remarks about Cross and Bi Encoders**

Vector databases use **Bi-encoder** models to compute the similarity of two concepts in vector space. These models are trained to represent data in vector form and, accordingly, during a search, the user’s query is also turned into a vector, and vectors closest to the query are returned. However, this proximity does not guarantee that it is the best answer.

https://miro.medium.com/v2/resize:fit:700/0*N_wng9uYMv5zi3ge\* BERT stands for Bidirectional Encoder Representations from Transformers, a model based on transformers that encodes text into a vector (embedding). Image by the author

**Cross-Encoder** works differently. It takes two objects (texts, images, etc.) and returns their relevance (similarity) relative to each other. Its accuracy is usually [better](https://arxiv.org/abs/1908.10084) than that of a Bi-Encoder. Typically, more results than necessary are returned from the vector database (just in case, say 30) and then they are ranked using a Cross-Encoder or similar techniques, with the top 3 being returned.

https://miro.medium.com/v2/resize:fit:700/0*h98JJPZ-YSiOWwR1Cross-Encoder, image by the author

User request preprocessing also includes its classification. For example, requests can be subdivided into questions, complaints, requests, etc. Requests can further be classified as urgent, non-urgent, spam, or fraud. They can be classified by departments (e.g., accounting, production, HR), etc. All this helps narrow down the search for information and, consequently, increases the speed and quality of the response.

For classification, an LLM model or a specially trained neural network classifier can be used again.

**Data Search in Repositories**

The so-called **retriever**(the first letter in RAG) is responsible for the search.

Usually, a vector database serves as the repository where company data from various sources (document storage, databases, wikis, CRM, etc.) are indexed. However, it’s not mandatory and anything can be used, such as Elasticsearch or even Google search.

I will not discuss non-vector base searches here, as the principle is the same everywhere.

**Digression about Vector Databases**

A vector database (or vector storage. I use these terms interchangeably, although technically they are not the same) is a type of data storage optimized for storing and processing vectors (which are essentially arrays of numbers). These vectors are used to represent complex objects, such as images, texts, or sounds, as vectors in vector spaces for [machine learning](https://towardsai.net/ai/machine-learning "machine learning") and data analysis tasks. In a vector database (or, more precisely, in vector space), concepts that are semantically similar are located close to each other, regardless of their representation. For example, the words “dog” and “bulldog” will be close, whereas the words “lock” (as in a door lock) and “lock” (as in a castle) will be far apart. Therefore, vector databases are well suited for semantic data search.

Most Popular Vector Databases (as of now):

- **QDrant**— open-source database
- **Pinecone**— cloud-native (i.e., they will charge you a lot) database
- **Chroma**— another open-source database (Apache-2.0 license)
- **Weaviate**— open under BSD-3-Clause license
- **Milvus**— open under Apache-2.0 license
- **FAISS**— a separate beast, not a database but a framework from Meta

Also, some popular non-vector databases have started offering vector capabilities:

- **Pgvector** for PostgreSQL
- **Atlas** for Mongo

To improve results, several main techniques are used:

**Ensemble of retrievers and/or data sources —** a simple but effective idea, which involves asking several experts the same question and then somehow aggregating their answers (even just averaging) — the result on average turns out better. In some sense, this is analogous to “Ask the Crowd.”

As an example — the use of multiple types of retrievers from [Langchain](https://python.langchain.com/docs/modules/data_connection/retrievers/). Ensembling is particularly useful when combining sparse retrievers (like [BM25](https://python.langchain.com/docs/integrations/retrievers/bm25)) and dense retrievers (working based on embedding similarities, such as the same [vector](https://python.langchain.com/docs/modules/data_connection/retrievers/vectorstore) databases) because they complement each other well.

**Dense Retriever** — typically uses transformers, such as BERT, to encode both queries and documents into vectors in a multidimensional space. The similarity between a query and a document is measured by the proximity of their vectors in this space, often using cosine similarity to assess their closeness. This is the basis on which vector databases are built. Such a model better understands the semantic (meaningful) value of queries and documents, leading to more accurate and relevant results, especially for complex queries. Because the model operates at the level of meaning (semantics), it handles paraphrasing and semantic similarities well.

**Sparse Retriever** — uses traditional information retrieval methods, such as [TF-IDF](https://towardsai.net/p/nlp/natural-language-processing-nlp-with-python-tutorial-for-beginners-1f54e610a1a0 "natural language processing") (Term Frequency) or BM25. These methods create sparse vectors, where each dimension corresponds to a specific term from a predefined dictionary. The relevance of a document to a user’s query is calculated based on the presence and frequency of the terms (or words, let’s say) of the query in the document. It is effective for keyword-based queries and when the terms of the query are expected to be directly present in the relevant documents. They don’t always work as accurately as dense retrievers, but are faster and require fewer resources for searching and training.

The [EnsembleRetriever](https://python.langchain.com/docs/modules/data_connection/retrievers/ensemble) then ranks and combines results using, for example, [Reciprocal Rank Fusion](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf):

_Example of an ensemble:_

```
!pip install rank_bm25
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from langchain.vectorstores import Chroma

embedding = OpenAIEmbeddings()
documents = "/all_tolstoy_novels.txt"
bm25_retriever = BM25Retriever.from_texts(doc_list)
bm25_retriever.k = 2

vectorstore = Chroma.from_texts(doc_list, embedding)
vectorstore_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# initialize the ensemble retriever
ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, vectorstore_retriever ], weights=[0.4, 0.6])
docs = ensemble_retriever.get_relevant_documents("War and Peace")
```

How to choose the right strategy from all this zoo? Experiment. Or use a framework, for example, [https://github.com/Marker-Inc-Korea/AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG).

By the way, it’s also possible to ensemble several LLMs, which also improves the result. See “ [More agents is all you need](https://arxiv.org/abs/2402.05120).”

**RELP**

This is another method for data retrieval, Retrieval Augmented Language Model based Prediction. The distinction here is in the search step — after we find information in the vector storage, including using the techniques mentioned above, we use it not to generate an answer using an LLM but to generate example answers (via [few-shot prompting](https://en.wikipedia.org/wiki/Few-shot_learning)) for the LLM. Based on these examples, the LLM effectively learns and responds based on this mini-training to the posed question. This technique is a form of dynamic learning, which is much less costly than re-training the model using standard methods.

https://miro.medium.com/v2/resize:fit:451/0*0fpWX48eZ6Lw7nJRRELP flow, image by the author

**Remarks about few-shot (learning) prompting**

There are two similar LLM prompting techniques: zero-shot and few-shot. Zero-shot is when you ask your LLM a question without providing any examples. For instance:

https://miro.medium.com/v2/resize:fit:700/0*AlG7hPApACw63e2-Image by the author

**Few-shot** is when you first give the LLM several examples on which it trains. This significantly increases the likelihood of getting a relevant answer in the relevant form. For example:

https://miro.medium.com/v2/resize:fit:700/0*hyKm2xkJEW17gXDMImage by the author

As you can see, not everything is always obvious, and examples help to understand.

**Ranking, Combining, and Evaluating the Obtained Results**

We have already partially touched on this topic as part of RAG Fusion and the ensembling of retrievers. When we extract results from a (vector) storage, before sending this data to an LLM for answer generation, we need to rank the results, and possibly discard the irrelevant ones. The order in which you present the search results to the LLM for answer formulation matters. What the LLM sees first will have a stronger influence on the final outcome (more details here).

Different approaches are used for ranking. The most common include:

1. Using a **Cross-Encoder** (described above) for re-ranking the obtained results and discarding the least relevant (for example, pulling the top 30 results from a vector database (top k), ranking them with a Cross-Encoder, and taking the first 10).

There are already ready-made solutions for these purposes, for example from [Cohere](https://cohere.com/rerankhttps:/cohere.com/rerank).

[2\. Reciprocal Rank Fusion.](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) The main idea of RRF is to give greater importance to elements occupying higher positions in each set of search results. In RRF, the score of each element is calculated based on its position in the individual search results. This is usually done using the formula 1/(k + rank), where “rank” is the position of the element in a particular set of search results, and “k” is a constant (often set around 60). This formula provides a higher score for elements with a higher rank.

Scores for each element in different sets of results are then summed to obtain a final score. Elements are sorted by these final scores to form a combined list of results.

RRF is particularly useful because it does not depend on the absolute scores assigned by individual search systems, which can vary significantly in their scale and distribution. RRF effectively combines results from different systems in a way that highlights the most consistently highly ranked elements.

3\. LLM-based ranking and evaluation: you can relax and simply ask an LLM to rank and evaluate the result 🙂. The latest versions of OpenAI handle this quite well. However, using them for this purpose is costly.

**Evaluation of search results in the Vector Store:**

Suppose you have made reranking or other changes — how do you determine whether it was beneficial? Did the relevance increase or not? And in general, how well does the system work? This is a quality metric for the information found. It is used to understand how relevant the information your system finds is and to make decisions about further refinement.

You can assess how relevant the results are to the query using the following metrics: P@K, MAP@K, NDCG@K (and similar). These usually return a number from 0 to 1, where 1 is the highest accuracy. They are similar in meaning, with differences in details:

**P@K** means precision at K, i.e., accuracy for K elements. Suppose for a query about rabbits, the system found 4 documents:

_\[“Wild Rabbits”, “Task Rabbit: modern [jobs](https://jobs.towardsai.net/ "AI Jobs") platform”, “Treatise on Carrots”, “My Bunny: Memoirs by Walter Issac”\]_

Since Walter Issac's biography or jobs platforms have nothing to do with rabbits, these positions would be rated 0, and the overall accuracy would be calculated like this:

https://miro.medium.com/v2/resize:fit:700/0*fkdMKuqKYbn5odPjImage by the author

P@K at K=4, or P@4 = 2 relevant / (2 relevant + 2 irrelevant) = ½ = 0.5.

However, this does not take into account the order. What if the returned list looks like this:

_\[“Task Rabbit: modern jobs platform”, “My Bunny: Memoirs by Walter Issac”, “Wild Rabbits”, “Treatise on Carrots”\]_

P@K is still 0.5, but as we know, the order of relevant and irrelevant results matters! (both for people and for the LLM that will use them).

Therefore, we use **AP@K** or average precision at K. The idea is simple: we need to modify the formula so that the order is taken into account and relevant results at the end of the list do not increase the overall score less than those at the beginning of the list:

https://miro.medium.com/v2/resize:fit:700/0*kQLsLwQqidjxR6sAImage by the author

Or for our example above:

AP@4 = (0 \* 0 + 0 \*½ + 1 \* ⅓ + 1 + 1 \* 2/4) .2 = (⅓ + 2/4) / 2 = 0.41

Here are a few questions that arise: how did we assess the relevance of individual elements to calculate these metrics? This is a detective question, a very good one indeed.

In the context of RAG, we often ask an LLM or another model to make an assessment. That is, we query the LLM about each element — this document we found in the vector storage — is it relevant to this query at all?

Now, the second question: is it sufficient to ask just this way? The answer is no. We need more specific questions for the LLM that ask it to assess relevance according to certain parameters. For example, for the sample above, the questions might be:

Does this document relate to the animal type “rabbit”?

Is the rabbit in this document real or metaphorical?

Etc. There can be many questions (from two to hundreds), and they depend on how you assess relevance. This needs to be aggregated, and that’s where:

MAP@K (Mean Average Precision at K) comes in — it’s the average of the sum of AP@K for all questions.

NDCG@K stands for normalized discounted cumulative gain at K, and I won’t even translate that 🙂. Look it up online yourself.

**Evaluating the results of the LLM response**

Not everyone knows this, but you can ask an LLM (including Llama and OpenAI) not just to return tokens (text) but logits. That is, you can actually ask it to return a distribution of tokens with their probabilities, and see — how confident is the model really in what it has concocted (calculating token-level uncertainty)? If the probabilities in the distribution are low (what is considered low depends on the task), then most likely, the model has started to fabricate (hallucinate) and is not at all confident in its response. This can be used to evaluate the response and to return an honest “I don’t know” to the user.

**Using formatting, style, and tone**

The easiest item 🙂. Just ask the LLM to format the answer in a certain way and use a specific tone. It’s better to give the model an example, as it then follows instructions better. For instance, you could set the tone like this:

https://miro.medium.com/v2/resize:fit:700/0*lsnHytCsXujPJZrvImage by the author

Formatting and stylistics can be programmatically set in the last step of RAG — requesting the LLM to generate the final answer, for example:

```
question = input('Your question: ')
style = 'Users have become very very impudent lately. Answer as a gangster from a ghetto'
qa = RetrievalQA.from_chain_type(
 llm=llm,
 chain_type="stuff",
 retriever=doc_store.as_retriever()
)

result = qa(style + " user question: " + question)
print(f"Answer: {result}")
```

## Fine-tuning models

Sometimes you might indeed need further training. Yes, initially I said that most likely you won’t succeed, but there are cases when it is justified. If your company uses acronyms, names/surnames, and terms that the model does not and cannot know about, RAG may perform poorly. For example, it might struggle with searching data by Russian surnames, especially their declensions. Here, a light fine-tuning of the model using [LORA](https://arxiv.org/abs/2106.09685) can help, to train the model to understand such specific cases. You can use frameworks like [https://github.com/bclavie/RAGatouille](https://github.com/bclavie/RAGatouille).

Such fine-tuning is beyond the scope of this article, but if there is interest, I will describe it separately.

**Systems based on RAG**

There are several more advanced options based on RAG. In fact, new variants are emerging almost every day, and their creators claim that they have become increasingly better…

Nevertheless, one variation stands out — [FLARE](https://arxiv.org/abs/2305.06983)(Forward Looking Active REtrieval Augmented Generation).

It’s a very interesting idea based on the principle that RAG should not be used haphazardly but only when the LLM itself wants to. If the LLM confidently answers without RAG, then please proceed. However, if it starts to doubt, that’s when more contextual data needs to be searched for. This should not be done just once but as many times as necessary. When, during the response process, the LLM feels it needs more data, it performs a RAG search.

In some ways, this is similar to how people operate. We often do not know what we do not know and realize it only during the search process itself.

I will not go into details here; that is a topic for another article.

## Summary

In this article, I’ve provided a comprehensive guide to Retrieval-Augmented Generation (RAG). Here’s a quick recap of our journey:

**Need and Advantages:** I started by discussing why RAG is needed and its benefits over retraining models with custom data.

**RAG Structure:** Then, I explained the basic structure of RAG, highlighting the roles of the Retriever and Generator components.

**Implementation:** I walked through an example implementation using Python and LangСhain.

**User Query Processing:** I delved into processing user queries, including RAG Fusion and Cross-Encoders.

**Data Search Techniques:** Next, I explored various data search techniques, such as vector databases and ensembling retrievers.

**Ranking and Evaluating:** I covered the importance of ranking, combining, and evaluating retrieved results to improve response quality.

**Advanced Methods:** Finally, I discussed optimizations and advanced methods like RELP and FLARE, as well as considerations for fine-tuning models and maintaining response formatting, style, and tone.

</details>

<details>
<summary>advanced-rag-blueprint-optimize-llm-retrieval-systems</summary>

# Your RAG is wrong: Here's how to fix it

### The blueprint to advanced RAG (Retrieval-Augmented Generation)

The vanilla RAG framework doesn’t address many fundamental aspects that impact the quality of the retrieval and answer generation, such as:

- Are the retrieved documents relevant to the user’s question?

- Is the retrieved context enough to answer the user’s question?

- Is there any redundant information that only adds noise to the augmented prompt?

- Does the latency of the retrieval step match our requirements?

- What do we do if we can’t generate a valid answer using the retrieved information?

From the questions above, we can draw two conclusions.

**The first one** is that we need a robust evaluation module for our RAG system that can quantify and measure the quality of the retrieved data and generate answers relative to the user’s question.

**The second conclusion** is that we must improve our RAG framework to address the retrieval limitations directly in the algorithm. These improvements are known as advanced RAG.

This article will focus on the second conclusion, answering the question: _“How can I optimize an RAG system?”_.

[https://substackcdn.com/image/fetch/$s_!yOzH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19d2780b-7e3f-48aa-8e67-c4107ef8f0c7_792x792.png](https://substackcdn.com/image/fetch/$s_!yOzH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19d2780b-7e3f-48aa-8e67-c4107ef8f0c7_792x792.png)
Figure 1: The three stages of advanced RAG

The vanilla RAG design can be **optimized** **at** **three different stages**:

1. **Pre-retrieval:** This stage focuses on structuring and preprocessing your data for data indexing and query optimizations.

2. **Retrieval:** This stage revolves around improving the embedding models and metadata filtering to improve the vector search step.

3. **Post-retrieval:** This stage mainly targets different ways to filter out noise from the retrieved documents and compress the prompt before feeding it to an LLM for answer generation.

* * *

## 1\. Pre-retrieval

The pre-retrieval steps are performed in two different ways:

- **Data indexing:** It is part of the RAG ingestion pipeline. It is mainly implemented within the cleaning or chunking modules to preprocess the data for better indexing.

- **Query optimization:** The algorithm is performed directly on the user’s query before embedding it and retrieving the chunks from the vector DB.

As we index our data using embeddings that semantically represent the content of a chunked document, most of the data indexing techniques focus on better preprocessing and structuring the data to improve retrieval efficiency.

Here are a few popular methods for **optimizing data indexing**.

#### 1\. Sliding window

The sliding window technique introduces overlap between text chunks, ensuring that important context near chunk boundaries is retained, which enhances retrieval accuracy.

This is particularly beneficial in domains like legal documents, scientific papers, customer support logs, and medical records, where critical information often spans multiple sections.

The embedding is computed on the chunk along with the overlapping portion. Hence, the sliding window improves the system’s ability to retrieve relevant and coherent information by maintaining context across boundaries.

#### 2\. Enhancing data granularity

This involves data cleaning techniques like removing irrelevant details, verifying factual accuracy, and updating outdated information. A clean and accurate dataset allows for sharper retrieval.

#### 3\. Metadata

Adding metadata tags like dates, URLs, external IDs, or chapter markers helps filter results efficiently during retrieval.

#### 4\. Optimizing index structures

It is based on different data index methods, such as various chunk sizes and multi-indexing strategies.

#### 5\. Small-to-big

The algorithm decouples the chunks used for retrieval and the context used in the prompt for the final answer generation.

The algorithm uses a small sequence of text to compute the embedding while preserving the sequence itself and a wider window around it in the metadata. Thus, using smaller chunks enhances the retrieval’s accuracy, while the larger context adds more contextual information to the LLM.

The intuition behind this is that if we use the whole text for computing the embedding, we might introduce too much noise, or the text could contain multiple topics, which results in a poor overall semantic representation of the embedding.

**On the** **query optimization side**, we can leverage techniques such as query routing, query rewriting, and query expansion to refine the retrieved information for the LLM further.

#### 1\. Query routing

Based on the user’s input, we might have to interact with different categories of data and query each category differently.

Query rooting is used to decide what action to take based on the user’s input, similar to if/else statements. Still, the decisions are made solely using natural language instead of logical statements.

As illustrated in Figure 2, let’s assume that, based on the user’s input, to do RAG, we can retrieve additional context from a vector DB using vector search queries, a standard SQL DB by translating the user query to an SQL command, or the internet by leveraging REST API calls.

The query router can also detect whether a context is required, helping us avoid making redundant calls to external data storage. Also, a query router can pick the best prompt template for a given input.

The routing usually uses an LLM to decide what route to take or embeddings by picking the path with the most similar vectors.

To summarize, query routing is identical to an if/else statement but much more versatile as it works directly with natural language.

[https://substackcdn.com/image/fetch/$s_!SdZP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab3d3265-49a9-4bd6-a61a-7a3bf019ef25_792x792.png](https://substackcdn.com/image/fetch/$s_!SdZP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab3d3265-49a9-4bd6-a61a-7a3bf019ef25_792x792.png)
Figure 2: Query routing

#### 2\. Query rewriting

Sometimes, the user’s initial query might not perfectly align with how your data is structured. Query rewriting tackles this by reformulating the question to match the indexed information better.

This can involve techniques like:

- **Paraphrasing:** Rephrasing the user’s query while preserving its meaning (e.g., “What are the causes of climate change?” could be rewritten as “Factors contributing to global warming”).

- **Synonym substitution:** Replacing less common words with synonyms to broaden the search scope (e.g., “ joyful” could be rewritten as “happy”).

- **Sub-queries:** For longer queries, we can break them down into multiple shorter and more focused sub-queries. This can help the retrieval stage identify relevant documents more precisely.

#### 3\. Hypothetical document embeddings (HyDE)

This technique involves having an LLM create a hypothetical response to the query. Then, both the original query and the LLM’s response are fed into the retrieval stage.

#### 4\. Query expansion

This approach aims to enrich the user’s question by adding additional terms or concepts, resulting in different perspectives of the same initial question. For example, when searching for “disease,” you can leverage synonyms and related terms associated with the original query words and also include “illnesses” or “ailments.”

#### 5\. Self-query

The core idea is to map unstructured queries into structured ones. An LLM identifies key entities, events, and relationships within the input text. These identities are used as filtering parameters to reduce the vector search space (e.g., identify cities within the query, for example, “Paris,” and add it to your filter to reduce your vector search space).

Both data indexing and query optimization pre-retrieval optimization techniques depend highly on your data type, structure, and source. Thus, as with any data processing pipeline, no method always works, as every use case has its own particularities and gotchas.

Optimizing your pre-retrieval RAG layer is experimental. Thus, what is essential is to try multiple methods (such as the ones enumerated in this section), reiterate, and observe what works best.

## 2\. Retrieval

The retrieval step can be optimized in two fundamental ways:

- Improving the embedding models used in the RAG ingestion pipeline to encode the chunked documents and, at inference time, transform the user’s input.

- Leveraging the DB’s filter and search features. This step will be used solely at inference time when you have to retrieve the most similar chunks based on user input.

Both strategies are aligned with our ultimate goal: to enhance the vector search step by leveraging the semantic similarity between the query and the indexed data.

When improving the **embedding models**, you usually have to fine-tune the pre-trained embedding models to tailor them to specific jargon and nuances of your domain, especially for areas with evolving terminology or rare terms.

Instead of fine-tuning the embedding model, you can leverage instructor models, such as **[instructor-xl](https://huggingface.co/hkunlp/instructor-xl)**, to guide the embedding generation process with an instruction/prompt aimed at your domain. Tailoring your embedding network to your data using such a model can be a good option, as fine-tuning a model consumes more computing and human resources.

In the code snippet below, you can see an example of an Instructor model that embeds article titles about AI:

```
from InstructorEmbedding import INSTRUCTOR

model = INSTRUCTOR(“hkunlp/instructor-base”)

sentence = “RAG Fundamentals First”

instruction = “Represent the title of an article about AI:”

embeddings = model.encode([[instruction, sentence]])

print(embeddings.shape) # noqa

# Output: (1, 768)
```

On the other side of the spectrum, here is how you can **improve your retrieval** by leveraging classic filter and search DB features.

#### **Hybrid search**

This is a vector and keyword-based search blend.

Keyword-based search excels at identifying documents containing specific keywords. When your task demands pinpoint accuracy, and the retrieved information must include exact keyword matches, hybrid search shines. Vector search, while powerful, can sometimes struggle with finding exact matches, but it excels at finding more general semantic similarities.

You leverage both keyword matching and semantic similarities by combining the two methods. You have a parameter, usually called alpha, that controls the weight between the two methods. The algorithm has two independent searches, which are later normalized and unified.

#### Filtered vector search

This type of search leverages the metadata index to filter for specific keywords within the metadata. It differs from a hybrid search in that you retrieve the data once using only the vector index and perform the filtering step before or after the vector search to reduce your search space.

In practice, you usually start with filtered vector or hybrid search on the retrieval side, as they are fairly quick to implement. This approach gives you the flexibility to adjust your strategy based on performance.

If the results are unexpected, you can always fine-tune your embedding model.

## 3\. Post-retrieval

The post-retrieval optimizations are solely performed on the retrieved data to ensure that the LLM’s performance is not compromised by issues such as limited context windows or noisy data.

This is because the retrieved context can sometimes be too large or contain irrelevant information, both of which can distract the LLM.

Two popular methods performed at the post-retrieval step are the following.

#### **Prompt compression**

Eliminate unnecessary details while keeping the essence of the data.

#### Re-ranking

Use a cross-encoder ML model to give a matching score between the user’s input and every retrieved chunk.

[https://substackcdn.com/image/fetch/$s_!RjK7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff797810-7274-4a51-b487-ee06e881efe6_792x792.png](https://substackcdn.com/image/fetch/$s_!RjK7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff797810-7274-4a51-b487-ee06e881efe6_792x792.png)
Figure 3: Bi-encoder (the standard embedding model) versus cross-encoder

The retrieved items are sorted based on this score. Only the top N results are kept as the most relevant. As you can see in Figure 3, this works because the re-ranking model can find more complex relationships between the user input and some content than a simple similarity search.

However, we can’t apply this model at the initial retrieval step because it is costly. That is why a popular strategy is to retrieve the data using a similarity distance between the embeddings and refine the retrieved information using a re-raking model, as illustrated in Figure 4.

[https://substackcdn.com/image/fetch/$s_!2OdZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33ab6874-b3ea-4cd4-9a66-9665afe27de5_792x792.png](https://substackcdn.com/image/fetch/$s_!2OdZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F33ab6874-b3ea-4cd4-9a66-9665afe27de5_792x792.png)
Figure 4: The re-ranking algorithm

* * *

## Conclusion

The abovementioned techniques are far from an exhaustive list of all potential solutions. We used them as examples to get an intuition on what you can (and should) optimize at each step in your RAG workflow.

The truth is that these techniques can vary tremendously by the type of data you work with. For example, if you work with multi-modal data such as text and images, most of the techniques from earlier won’t work as they are designed for text only.

To summarize, the primary goal of these optimizations is to enhance the RAG algorithm at three key stages: pre-retrieval, retrieval, and post-retrieval.

This involves preprocessing data for improved vector indexing, adjusting user queries for more accurate searches, enhancing the embedding model, utilizing classic filtering DB operations, and removing noisy data.

By keeping these goals in mind, you can optimize your RAG workflow for data processing and retrieval.

</details>

<details>
<summary>from-local-to-global-a-graphrag-approach-to-query-focused-su</summary>

The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs) to answer questions over private and/or previously unseen document collections.
However, RAG fails on global questions directed at an entire text corpus, such as “What are the main themes in the dataset?”, since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task.
Prior QFS methods, meanwhile, do not scale to the quantities of text indexed by typical RAG systems.
To combine the strengths of these contrasting methods, we propose GraphRAG, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text.
Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities.
Given a question, each community summary is used to generate a partial response, before all partial responses are again summarized in a final response to the user.
For a class of global sensemaking questions over datasets in the 1 million token range, we show that GraphRAG leads to substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity of generated answers.

## 1 Introduction

Retrieval augmented generation (RAG) (Lewis et al.,, [2020](https://arxiv.org/html/2404.16130v2#bib.bib32 "")) is an established approach to using LLMs to answer queries based on data that is too large to contain in a language model’s _context window_, meaning the maximum number of _tokens_ (units of text) that can be processed by the LLM at once  (Liu et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib33 ""); Kuratov et al.,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib29 "")).
In the canonical RAG setup, the system has access to a large external corpus of text records and retrieves a subset of records that are individually relevant to the query and collectively small enough to fit into the context window of the LLM. The LLM then generates a response based on both the query and the retrieved records (Dang,, [2006](https://arxiv.org/html/2404.16130v2#bib.bib12 ""); Yao et al.,, [2017](https://arxiv.org/html/2404.16130v2#bib.bib71 ""); Baumel et al.,, [2018](https://arxiv.org/html/2404.16130v2#bib.bib6 ""); Laskar et al.,, [2020](https://arxiv.org/html/2404.16130v2#bib.bib31 "")).
This conventional approach, which we collectively call _vector RAG_, works well for queries that can be answered with information localized within a small set of records.
However, vector RAG approaches do not support sensemaking queries, meaning queries that require global understanding of the entire dataset, such as ” _What are the key trends in how scientific discoveries are influenced by interdisciplinary research over the past decade?_”

Sensemaking tasks require reasoning over “ _connections_
_(which can be among people, places, and events) in order to anticipate their trajectories and act effectively_” (Klein et al.,, [2006](https://arxiv.org/html/2404.16130v2#bib.bib27 "")).
LLMs such as GPT (Brown et al.,, [2020](https://arxiv.org/html/2404.16130v2#bib.bib8 ""); Achiam et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib1 "")), Llama (Touvron et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib61 "")), and Gemini (Anil et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib2 "")) excel at sensemaking in complex domains like scientific discovery (Microsoft,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib41 "")) and intelligence analysis (Ranade and Joshi,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib51 "")).
Given a sensemaking query and a text with an implicit and interconnected set of concepts, an LLM can generate a summary that answers the query.
The challenge, however, arises when the volume of data requires a RAG approach, since vector RAG approaches are unable to support sensemaking over an entire corpus.

In this paper, we present GraphRAG – a graph-based RAG approach that enables sensemaking over the entirety of a large text corpus.
GraphRAG first uses an LLM to construct a knowledge graph, where nodes correspond to key entities in the corpus and edges represent relationships between those entities.
Next, it partitions the graph into a hierarchy of communities of closely related entities, before using an LLM to generate community-level summaries. These summaries are generated in a bottom-up manner following the hierarchical structure of extracted communities, with summaries at higher levels of the hierarchy recursively incorporating lower-level summaries.
Together, these community summaries provide global descriptions and insights over the corpus.
Finally, GraphRAG answers queries through map-reduce processing of community summaries; in the map step, the summaries are used to provide partial answers to the query independently and in parallel, then in the reduce step, the partial answers are combined and used to generate a final global answer.

The GraphRAG method and its ability to perform global sensemaking over an entire corpus form the main contribution of this work. To demonstrate this ability, we developed a novel application of the LLM-as-a-judge technique  (Zheng et al.,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib78 "")) suitable for questions targeting broad issues and themes where there is no ground-truth answer.
This approach first uses one LLM to generate a diverse set of global sensemaking questions based on corpus-specific use cases, before using a second LLM to judge the answers of two different RAG systems using predefined criteria (defined in [Section 3.3](https://arxiv.org/html/2404.16130v2#S3.SS3 "3.3 Criteria for Evaluating Global Sensemaking ‣ 3 Methods ‣ From Local to Global: A GraphRAG Approach to Query-Focused Summarization")).
We use this approach to compare GraphRAG to vector RAG on two representative real-world text datasets.
Results show GraphRAG strongly outperforms vector RAG when using GPT-4 as the LLM.

GraphRAG is available as open-source software at [https://github.com/microsoft/graphrag](https://github.com/microsoft/graphrag "").
In addition, versions of the GraphRAG approach are also available as extensions to multiple open-source libraries, including LangChain (LangChain,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib30 "")), LlamaIndex (LlamaIndex,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib34 "")), NebulaGraph (NebulaGraph,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib43 "")), and Neo4J (Neo4J,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib44 "")).

## 2 Background

### 2.1 RAG Approaches and Systems

RAG generally refers to any system where a user query is used to retrieve relevant information from external data sources, whereupon this information is incorporated into the generation of a response to the query by an LLM (or other generative AI model, such as a multi-media model).
The query and retrieved records populate a prompt template, which is then passed to the LLM (Ram et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib50 "")).
RAG is ideal when the total number of records in a data source is too large to include in a single prompt to the LLM, i.e. the amount of text in the data source exceeds the LLM’s context window.

In canonical RAG approaches, the retrieval process returns a set number of records that are semantically similar to the query and the generated answer uses only the information in those retrieved records.
A common approach to conventional RAG is to use text embeddings, retrieving records closest to the query in vector space where closeness corresponds to semantic similarity (Gao et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib18 "")).
While some RAG approaches may use alternative retrieval mechanisms, we collectively refer to the family of conventional approaches as _vector RAG_.
GraphRAG contrasts with vector RAG in its ability to answer queries that require global sensemaking over the entire data corpus.

GraphRAG builds upon prior work on advanced RAG strategies.
GraphRAG leverages summaries over large sections of the data source as a form of ”self-memory” (described in Cheng et al., [2024](https://arxiv.org/html/2404.16130v2#bib.bib9 "")), which are later used to answer queries as in Mao et al., [2020](https://arxiv.org/html/2404.16130v2#bib.bib37 "")). These summaries are generated in parallel and iteratively aggregated into global summaries, similar to prior techniques (Shao et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib55 ""); Wang et al.,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib66 ""); Su et al.,, [2020](https://arxiv.org/html/2404.16130v2#bib.bib58 ""); Feng et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib16 ""); Trivedi et al.,, [2022](https://arxiv.org/html/2404.16130v2#bib.bib64 ""); Khattab et al.,, [2022](https://arxiv.org/html/2404.16130v2#bib.bib24 ""); Gao et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib18 "")).
In particular, GraphRAG is similar to other approaches that use hierarchical indexing to create summaries (similar to Kim et al., [2023](https://arxiv.org/html/2404.16130v2#bib.bib26 ""); Sarthi et al., [2024](https://arxiv.org/html/2404.16130v2#bib.bib53 "")).
GraphRAG contrasts with these approaches by generating a graph index from the source data, then applying graph-based community detection to create a thematic partitioning of the data.

### 2.2 Using Knowledge Graphs with LLMs and RAG

Approaches to knowledge graph extraction from natural language text corpora include rule-matching, statistical pattern recognition, clustering, and embeddings (Yates et al.,, [2007](https://arxiv.org/html/2404.16130v2#bib.bib73 ""); Mooney and Bunescu,, [2005](https://arxiv.org/html/2404.16130v2#bib.bib42 ""); Kim et al.,, [2016](https://arxiv.org/html/2404.16130v2#bib.bib25 ""); Etzioni et al.,, [2004](https://arxiv.org/html/2404.16130v2#bib.bib15 "")).
GraphRAG falls into a more recent body of research that use of LLMs for knowledge graph extraction (Melnyk et al.,, [2022](https://arxiv.org/html/2404.16130v2#bib.bib39 ""); Tan et al.,, [2017](https://arxiv.org/html/2404.16130v2#bib.bib59 ""); OpenAI,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib47 ""); Ban et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib4 ""); [Zhang et al., 2024a,](https://arxiv.org/html/2404.16130v2#bib.bib76 ""); Trajanoska et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib63 ""); Yao et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib72 ""); Yates et al.,, [2007](https://arxiv.org/html/2404.16130v2#bib.bib73 "")).
It also adds to a growing body of RAG approaches that use a knowledge graph as an index (Gao et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib18 "")).
Some techniques use subgraphs, elements of the graph, or properties of the graph structure directly in the prompt  (Baek et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib3 ""); He et al.,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib19 ""); Zhang,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib75 "")) or as factual grounding for generated outputs (Kang et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib23 ""); Ranade and Joshi,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib51 "")).
Other techniques ( [Wang et al., 2023b,](https://arxiv.org/html/2404.16130v2#bib.bib68 "")) use the knowledge graph to enhance retrieval, where at query time an LLM-based agent dynamically traverses a graph with nodes representing document elements (e.g., passages, tables) and edges encoding lexical and semantical similarity or structural relationships.
GraphRAG contrasts with these approaches by focusing on a previously unexplored quality of graphs in this context: their inherent _modularity_(Newman,, [2006](https://arxiv.org/html/2404.16130v2#bib.bib45 "")) and the ability to partition graphs into nested modular communities of closely related nodes (e.g., Louvain, Blondel et al., [2008](https://arxiv.org/html/2404.16130v2#bib.bib7 ""); Leiden, Traag et al., [2019](https://arxiv.org/html/2404.16130v2#bib.bib62 "")).
Specifically, GraphRAG recursively creates increasingly global summaries by using the LLM to create summaries spanning this community hierarchy.

## 3 Methods

### 3.1 GraphRAG Workflow

[Figure 1](https://arxiv.org/html/2404.16130v2#S3.F1 "Figure 1 ‣ 3.1 GraphRAG Workflow ‣ 3 Methods ‣ From Local to Global: A GraphRAG Approach to Query-Focused Summarization") illustrates the high-level data flow of the GraphRAG approach and pipeline.
In this section, we describe the key design parameters, techniques, and implementation details for each step.

Source DocumentsText Chunkstext extraction and chunkingEntities & Relationshipsdomain-tailored summarizationKnowledge Graphdomain-tailored summarizationGraph Communitiescommunity detectionCommunity Summariesdomain-tailored summarizationCommunity Answersquery-focused summarizationGlobal Answerquery-focused summarizationIndexing TimeQuery TimePipeline StageFigure 1:
Graph RAG pipeline using an LLM-derived graph index of source document text.
This graph index spans nodes (e.g., entities), edges (e.g., relationships), and covariates (e.g., claims) that have been detected, extracted, and summarized by LLM prompts tailored to the domain of the dataset.
Community detection (e.g., Leiden, [Traag et al.,](https://arxiv.org/html/2404.16130v2#bib.bib62 ""), [2019](https://arxiv.org/html/2404.16130v2#bib.bib62 "")) is used to partition the graph index into groups of elements (nodes, edges, covariates) that the LLM can summarize in parallel at both indexing time and query time.
The “global answer” to a given query is produced using a final round of query-focused summarization over all community summaries reporting relevance to that query.

#### 3.1.1 Source Documents →→\\rightarrow→ Text Chunks

To start, the documents in the corpus are split into text chunks.
The LLM extracts information from each chunk for downstream processing.
Selecting the size of the chunk is a fundamental design decision; longer text chunks require fewer LLM calls for such extraction (which reduces cost) but suffer from degraded recall of information that appears early in the chunk (Liu et al.,, [2023](https://arxiv.org/html/2404.16130v2#bib.bib33 ""); Kuratov et al.,, [2024](https://arxiv.org/html/2404.16130v2#bib.bib29 "")).
See [Section A.1](https://arxiv.org/html/2404.16130v2#A1.SS1 "A.1 Entity Extraction ‣ Appendix A Entity and Relationship Extraction Approach ‣ From Local to Global: A GraphRAG Approach to Query-Focused Summarization") for prompts and examples of the recall-precision trade-offs.

#### 3.1.2 Text Chunks →→\\rightarrow→ Entities & Relationships

In this step, the LLM is prompted to extract instances of important _entities_ and the _relationships_ between the entities from a given chunk.
Additionally, the LLM generates short descriptions for the entities and relationships. To illustrate, suppose a chunk contained the following text:

> NeoChip’s (NC) shares surged in their first week of trading on the NewTech Exchange.
> However, market analysts caution that the chipmaker’s public debut may not reflect trends for other technology IPOs.
> NeoChip, previously a private entity, was acquired by Quantum Systems in 2016.
> The innovative semiconductor firm specializes in low-power processors for wearables and IoT devices.
>

The LLM is prompted such that it extracts the following:

- •

The entity NeoChip, with description “NeoChip is a publicly traded company specializing in low-power processors for wearables and IoT devices.”

- •

The entity Quantum Systems, with description “Quantum Systems is a firm that previously owned NeoChip.”

- •

A relationship between NeoChip and Quantum Systems, with description “Quantum Systems owned NeoChip from 2016 until NeoChip became publicly traded.”

These prompts can be tailored to the domain of the document corpus by choosing domain appropriate few-shot exemplars for in-context learning (Brown et al.,, [2020](https://arxiv.org/html/2404.16130v2#bib.bib8 "")).
For example, while our default prompt extracts the broad class of “named entities” like people, places, and organizations and is generally applicable, domains with specialized knowledge (e.g., science, medicine, law) will benefit from few-shot exemplars specialized to those domains.

The LLM can also be prompted to extract _claims_ about detected entities.
_Claims_ are important factual statements about entities, such as dates, events, and interactions with other entities.
As with entities and relationships, in-context learning exemplars can provide domain-specific guidance. Claim descriptions extracted from the example tetx chunk are as follows:

- •

NeoChip’s shares surged during their first week of trading on the NewTech Exchange.

- •

NeoChip debuted as a publicly listed company on the NewTech Exchange.

- •

Quantum Systems acquired NeoChip in 2016 and held ownership until NeoChip went public.

See [Appendix A](https://arxiv.org/html/2404.16130v2#A1 "Appendix A Entity and Relationship Extraction Approach ‣ From Local to Global: A GraphRAG Approach to Query-Focused Summarization") for prompts and details on our implementation of entity and claim extraction.

#### 3.1.3 Entities & Relationships →→\\rightarrow→ Knowledge Graph

The use of an LLM to extract entities, relationships, and claims is a form of abstractive summarization – these are meaningful summaries of concepts that, in the case of relationships and claims, may not be explicitly stated in the text.
The entity/relationship/claim extraction processes creates multiple instances of a single element because an element is typically detected and extracted multiple times across documents.

In the final step of the knowledge graph extraction process, these instances of entities and relationships become individual nodes and edges in the graph.
Entity descriptions are aggregated and summarized for each node and edge.
Relationships are aggregated into graph edges, where the number of duplicates for a given relationship becomes edge weights.
Claims are aggregated similarly.

In this manuscript, our analysis uses exact string matching for _entity matching_ – the task of reconciling different extracted names for the same entity (Barlaug and Gulla,, [2021](https://arxiv.org/html/2404.16130v2#bib.bib5 ""); Christen and Christen,, [2012](https://arxiv.org/html/2404.16130v2#bib.bib10 ""); Elmagarmid et al.,, [2006](https://arxiv.org/html/2404.16130v2#bib.bib13 "")).
However, softer matching approaches can be used with minor adjustments to prompts or code.
Furthermore, GraphRAG is generally resilient to duplicate entities since duplicates are typically clustered together for summarization in subsequent steps.

#### 3.1.4 Knowledge Graph →→\\rightarrow→ Graph Communities

Given the graph index created in the previous step, a variety of community detection algorithms may be used to partition the graph into communities of strongly connected nodes (e.g., see the surveys by Fortunato, ( [2010](https://arxiv.org/html/2404.16130v2#bib.bib17 "")) and Jin et al., ( [2021](https://arxiv.org/html/2404.16130v2#bib.bib22 ""))).
In our pipeline, we use Leiden community detection (Traag et al.,, [2019](https://arxiv.org/html/2404.16130v2#bib.bib62 "")) in a hierarchical manner, recursively detecting sub-communities within each detected community until reaching leaf communities that can no longer be partitioned.

Each level of this hierarchy provides a community partition that covers the nodes of the graph in a mutually exclusive, collectively exhaustive way, enabling divide-and-conquer global summarization.
An illustration of such hierarchical partitioning on an example dataset can be found in [Appendix B](https://arxiv.org/html/2404.16130v2#A2 "Appendix B Example Community Detection ‣ From Local to Global: A GraphRAG Approach to Query-Focused Summarization").

#### 3.1.5 Graph Communities →→\\rightarrow→ Community Summaries

The next step creates report-like summaries of each community in the community hierarchy, using a method designed to scale to very large datasets.
These summaries are independently useful as a way to understand the global structure and semantics of the dataset, and may themselves be used to make sense of a corpus in the absence of a specific query.
For example, a user may scan through community summaries at one level looking for general themes of interest, then read linked reports at a lower level that provide additional details for each subtopic.
Here, however, we focus on their utility as part of a graph-based index used for answering global queries.

GraphRAG generates community summaries by adding various element summaries (for nodes, edges, and related claims) to a community summary template.
Community summaries from lower-level communities are used to generate summaries for higher-level communities as follows:

- •

_Leaf-level communities_. The element summaries of a leaf-level community are prioritized and then iteratively added to the LLM context window until the token limit is reached.
The prioritization is as follows: for each community edge in decreasing order of combined source and target node degree (i.e., overall prominence), add descriptions of the source node, target node, the edge itself, and related claims.

- •

_Higher-level communities_. If all element summaries fit within the token limit of the context window, proceed as for leaf-level communities and summarize all element summaries within the community.
Otherwise, rank sub-communities in decreasing order of element summary tokens and iteratively substitute sub-community summaries (shorter) for their associated element summaries (longer) until they fit within the context window.

#### 3.1.6 Community Summaries →→\\rightarrow→ Community Answers →→\\rightarrow→ Global Answer

Given a user query, the community summaries generated in the previous step can be used to generate a final answer in a multi-stage process.
The hierarchical nature of the community structure also means that questions can be answered using the community summaries from different levels, raising the question of whether a particular level in the hierarchical community structure offers the best balance of summary detail and scope for general sensemaking questions (evaluated in [section 4](https://arxiv.org/html/2404.16130v2#S4 "4 Analysis ‣ From Local to Global: A GraphRAG Approach to Query-Focused Summarization")).

For a given community level, the global answer to any user query is generated as follows:

- •

_Prepare community summaries_. Community summaries are randomly shuffled and divided into chunks of pre-specified token size. This ensures relevant information is distributed across chunks, rather than concentrated (and potentially lost) in a single context window.

- •

_Map community answers_. Intermediate answers are generated in parallel. The LLM is also asked to generate a score between 0-100 indicating how helpful the generated answer is in answering the target question. Answers with score 0 are filtered out.

- •

_Reduce to global answer_. Intermediate community answers are sorted in descending order of helpfulness score and iteratively added into a new context window until the token limit is reached. This final context is used to generate the global answer returned to the user.

## 7 Conclusion

We have presented GraphRAG, a RAG approach that combines knowledge graph generation and query-focused summarization (QFS) to support human sensemaking over entire text corpora.
Initial evaluations show substantial improvements over a vector RAG baseline for both the comprehensiveness and diversity of answers, as well as favorable comparisons to a global but graph-free approach using map-reduce source text summarization.
For situations requiring many global queries over the same dataset, summaries of root-level communities in the entity-based graph index provide a data index that is both superior to vector RAG and achieves competitive performance to other global methods at a fraction of the token cost.

</details>

<details>
<summary>introducing-contextual-retrieval-anthropic</summary>

For an AI model to be useful in specific contexts, it often needs access to background knowledge. For example, customer support chatbots need knowledge about the specific business they're being used for, and legal analyst bots need to know about a vast array of past cases.

Developers typically enhance an AI model's knowledge using Retrieval-Augmented Generation (RAG). RAG is a method that retrieves relevant information from a knowledge base and appends it to the user's prompt, significantly enhancing the model's response. The problem is that traditional RAG solutions remove context when encoding information, which often results in the system failing to retrieve the relevant information from the knowledge base.

In this post, we outline a method that dramatically improves the retrieval step in RAG. The method is called “Contextual Retrieval” and uses two sub-techniques: Contextual Embeddings and Contextual BM25. This method can reduce the number of failed retrievals by 49% and, when combined with reranking, by 67%. These represent significant improvements in retrieval accuracy, which directly translates to better performance in downstream tasks.

### A note on simply using a longer prompt

Sometimes the simplest solution is the best. If your knowledge base is smaller than 200,000 tokens (about 500 pages of material), you can just include the entire knowledge base in the prompt that you give the model, with no need for RAG or similar methods.

However, as your knowledge base grows, you'll need a more scalable solution. That’s where Contextual Retrieval comes in.

## A primer on RAG: scaling to larger knowledge bases

For larger knowledge bases that don't fit within the context window, RAG is the typical solution. RAG works by preprocessing a knowledge base using the following steps:

1. Break down the knowledge base (the “corpus” of documents) into smaller chunks of text, usually no more than a few hundred tokens;
2. Use an embedding model to convert these chunks into vector embeddings that encode meaning;
3. Store these embeddings in a vector database that allows for searching by semantic similarity.

At runtime, when a user inputs a query to the model, the vector database is used to find the most relevant chunks based on semantic similarity to the query. Then, the most relevant chunks are added to the prompt sent to the generative model.

While embedding models excel at capturing semantic relationships, they can miss crucial exact matches. Fortunately, there’s an older technique that can assist in these situations. BM25 (Best Matching 25) is a ranking function that uses lexical matching to find precise word or phrase matches. It's particularly effective for queries that include unique identifiers or technical terms.

BM25 works by building upon the TF-IDF (Term Frequency-Inverse Document Frequency) concept. TF-IDF measures how important a word is to a document in a collection. BM25 refines this by considering document length and applying a saturation function to term frequency, which helps prevent common words from dominating the results.

Here’s how BM25 can succeed where semantic embeddings fail: Suppose a user queries "Error code TS-999" in a technical support database. An embedding model might find content about error codes in general, but could miss the exact "TS-999" match. BM25 looks for this specific text string to identify the relevant documentation.

RAG solutions can more accurately retrieve the most applicable chunks by combining the embeddings and BM25 techniques using the following steps:

1. Break down the knowledge base (the "corpus" of documents) into smaller chunks of text, usually no more than a few hundred tokens;
2. Create TF-IDF encodings and semantic embeddings for these chunks;
3. Use BM25 to find top chunks based on exact matches;
4. Use embeddings to find top chunks based on semantic similarity;
5. Combine and deduplicate results from (3) and (4) using rank fusion techniques;
6. Add the top-K chunks to the prompt to generate the response.

By leveraging both BM25 and embedding models, traditional RAG systems can provide more comprehensive and accurate results, balancing precise term matching with broader semantic understanding.https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F45603646e979c62349ce27744a940abf30200d57-3840x2160.png&w=3840&q=75A Standard Retrieval-Augmented Generation (RAG) system that uses both embeddings and Best Match 25 (BM25) to retrieve information. TF-IDF (term frequency-inverse document frequency) measures word importance and forms the basis for BM25.

This approach allows you to cost-effectively scale to enormous knowledge bases, far beyond what could fit in a single prompt. But these traditional RAG systems have a significant limitation: they often destroy context.

### The context conundrum in traditional RAG

In traditional RAG, documents are typically split into smaller chunks for efficient retrieval. While this approach works well for many applications, it can lead to problems when individual chunks lack sufficient context.

For example, imagine you had a collection of financial information (say, U.S. SEC filings) embedded in your knowledge base, and you received the following question: _"What was the revenue growth for ACME Corp in Q2 2023?"_

A relevant chunk might contain the text: _"The company's revenue grew by 3% over the previous quarter."_ However, this chunk on its own doesn't specify which company it's referring to or the relevant time period, making it difficult to retrieve the right information or use the information effectively.

## Introducing Contextual Retrieval

Contextual Retrieval solves this problem by prepending chunk-specific explanatory context to each chunk before embedding (“Contextual Embeddings”) and creating the BM25 index (“Contextual BM25”).

Let’s return to our SEC filings collection example. Here's an example of how a chunk might be transformed:

```plaintext
original_chunk = "The company's revenue grew by 3% over the previous quarter."

contextualized_chunk = "This chunk is from an SEC filing on ACME corp's performance in Q2 2023; the previous quarter's revenue was $314 million. The company's revenue grew by 3% over the previous quarter."
```

It is worth noting that other approaches to using context to improve retrieval have been proposed in the past. Other proposals include: [adding generic document summaries to chunks](https://aclanthology.org/W02-0405.pdf) (we experimented and saw very limited gains), [hypothetical document embedding](https://arxiv.org/abs/2212.10496), and [summary-based indexing](https://www.llamaindex.ai/blog/a-new-document-summary-index-for-llm-powered-qa-systems-9a32ece2f9ec) (we evaluated and saw low performance). These methods differ from what is proposed in this post.

### Implementing Contextual Retrieval

Of course, it would be far too much work to manually annotate the thousands or even millions of chunks in a knowledge base. To implement Contextual Retrieval, we turn to Claude. We’ve written a prompt that instructs the model to provide concise, chunk-specific context that explains the chunk using the context of the overall document. We used the following Claude 3 Haiku prompt to generate context for each chunk:

```plaintext
<document>
{{WHOLE_DOCUMENT}}
</document>
Here is the chunk we want to situate within the whole document
<chunk>
{{CHUNK_CONTENT}}
</chunk>
Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk. Answer only with the succinct context and nothing else.
```

The resulting contextual text, usually 50-100 tokens, is prepended to the chunk before embedding it and before creating the BM25 index.

Here’s what the preprocessing flow looks like in practice:https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2496e7c6fedd7ffaa043895c23a4089638b0c21b-3840x2160.png&w=3840&q=75_Contextual Retrieval is a preprocessing technique that improves retrieval accuracy._

### Using Prompt Caching to reduce the costs of Contextual Retrieval

#### Methodology

We experimented across various knowledge domains (codebases, fiction, ArXiv papers, Science Papers), embedding models, retrieval strategies, and evaluation metrics.

The graphs below show the average performance across all knowledge domains with the top-performing embedding configuration (Gemini Text 004) and retrieving the top-20-chunks. We use 1 minus recall@20 as our evaluation metric, which measures the percentage of relevant documents that fail to be retrieved within the top 20 chunks. You can see the full results in the appendix - contextualizing improves performance in every embedding-source combination we evaluated.

#### Performance improvements

Our experiments showed that:

- **Contextual Embeddings reduced the top-20-chunk retrieval failure rate by 35%** (5.7% → 3.7%).
- **Combining Contextual Embeddings and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 49%** (5.7% → 2.9%).https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7f8d739e491fe6b3ba0e6a9c74e4083d760b88c9-3840x2160.png&w=3840&q=75_Combining Contextual Embedding and Contextual BM25 reduce the top-20-chunk retrieval failure rate by 49%._

#### Implementation considerations

When implementing Contextual Retrieval, there are a few considerations to keep in mind:

1. **Chunk boundaries:** Consider how you split your documents into chunks. The choice of chunk size, chunk boundary, and chunk overlap can affect retrieval performance1.
2. **Embedding model:** Whereas Contextual Retrieval improves performance across all embedding models we tested, some models may benefit more than others.
3. **Custom contextualizer prompts:** While the generic prompt we provided works well, you may be able to achieve even better results with prompts tailored to your specific domain or use case (for example, including a glossary of key terms that might only be defined in other documents in the knowledge base).
4. **Number of chunks:** Adding more chunks into the context window increases the chances that you include the relevant information. However, more information can be distracting for models so there's a limit to this. We tried delivering 5, 10, and 20 chunks, and found using 20 to be the most performant of these options (see appendix for comparisons) but it’s worth experimenting on your use case.

**Always run evals:** Response generation may be improved by passing it the contextualized chunk and distinguishing between what is context and what is the chunk.

## Further boosting performance with Reranking

In a final step, we can combine Contextual Retrieval with another technique to give even more performance improvements. In traditional RAG, the AI system searches its knowledge base to find the potentially relevant information chunks. With large knowledge bases, this initial retrieval often returns a lot of chunks—sometimes hundreds—of varying relevance and importance.

Reranking is a commonly used filtering technique to ensure that only the most relevant chunks are passed to the model. Reranking provides better responses and reduces cost and latency because the model is processing less information. The key steps are:

1. Perform initial retrieval to get the top potentially relevant chunks (we used the top 150);
2. Pass the top-N chunks, along with the user's query, through the reranking model;
3. Using a reranking model, give each chunk a score based on its relevance and importance to the prompt, then select the top-K chunks (we used the top 20);
4. Pass the top-K chunks into the model as context to generate the final result.https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8f82c6175a64442ceff4334b54fac2ab3436a1d1-3840x2160.png&w=3840&q=75_Combine Contextual Retrieva and Reranking to maximize retrieval accuracy._

### Performance improvements

There are several reranking models on the market. Our experiments showed that, across various domains, adding a reranking step further optimizes retrieval.

Specifically, we found that Reranked Contextual Embedding and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 67% (5.7% → 1.9%).https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F93a70cfbb7cca35bb8d86ea0a23bdeeb699e8e58-3840x2160.png&w=3840&q=75_Reranked Contextual Embedding and Contextual BM25 reduces the top-20-chunk retrieval failure rate by 67%._

#### Cost and latency considerations

One important consideration with reranking is the impact on latency and cost, especially when reranking a large number of chunks. Because reranking adds an extra step at runtime, it inevitably adds a small amount of latency, even though the reranker scores all the chunks in parallel. There is an inherent trade-off between reranking more chunks for better performance vs. reranking fewer for lower latency and cost. We recommend experimenting with different settings on your specific use case to find the right balance.

## Conclusion

We ran a large number of tests, comparing different combinations of all the techniques described above (embedding model, use of BM25, use of contextual retrieval, use of a reranker, and total # of top-K results retrieved), all across a variety of different dataset types. Here’s a summary of what we found:

1. Embeddings+BM25 is better than embeddings on their own;
2. Voyage and Gemini have the best embeddings of the ones we tested;
3. Passing the top-20 chunks to the model is more effective than just the top-10 or top-5;
4. Adding context to chunks improves retrieval accuracy a lot;
5. Reranking is better than no reranking;
6. **All these benefits stack**: to maximize performance improvements, we can combine contextual embeddings (from Voyage or Gemini) with contextual BM25, plus a reranking step, and adding the 20 chunks to the prompt.

## Appendix I

Below is a breakdown of results across datasets, embedding providers, use of BM25 in addition to embeddings, use of contextual retrieval, and use of reranking for Retrievals @ 20.https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F646a894ec4e6120cade9951a362f685cd2ec89b2-2458x2983.png&w=3840&q=75_1 minus recall @ 20 results across data sets and embedding providers._

#### Footnotes

1\. For additional reading on chunking strategies, check out [this link](https://www.pinecone.io/learn/chunking-strategies/) and [this link](https://research.trychroma.com/evaluating-chunking).

</details>

<details>
<summary>rag-fundamentals-first-by-paul-iusztin-decoding-ml</summary>

# Retrieval-Augmented Generation (RAG) Fundamentals First

### Mastering the basics of RAG still beats advanced techniques

To build successful and complex RAG applications, you must first deeply understand the fundamentals behind them. _In this article, we will learn why we use RAG and how to design the architecture of your RAG layer._

Retrieval-augmented generation (RAG) enhances the accuracy and reliability of generative AI models with information fetched from external sources. It is a technique complementary to the internal knowledge of the LLMs. Before going into the details, let’s understand what RAG stands for:

- **Retrieval:** search for relevant data;

- **Augmented:** add the data as context to the prompt;

- **Generation:** use the augmented prompt with an LLM for generation.


Any LLM is bound to understand the data it was trained on, sometimes called parameterized knowledge. Thus, even if the LLM can perfectly answer what happened in the past, it won’t have access to the newest data or any other external sources on which it wasn’t trained.

Let’s take the most powerful model from OpenAI as an example, which in the summer of 2024 is GPT-4o. The model is trained on data up to Oct 2023. Thus, if we ask what happened during the 2020 pandemic, it can be answered perfectly due to its parametrized knowledge. However, it will not know the answer if we ask about the 2024 soccer EURO cup results due to its bounded parametrized knowledge. Another scenario is that it will start confidently hallucinating and provide a faulty answer.

RAG overcomes these two limitations of LLMs. It provides access to external or latest data and prevents hallucinations, enhancing generative AI models’ accuracy and reliability.

* * *

## **Why use RAG?**

We briefly explained the importance of using RAG in generative AI applications above. Now, we will dig deeper into the “why”. Next, we will focus on what a naïve RAG framework looks like.

For now, to get an intuition about RAG, you have to know that when using RAG, we inject the necessary information into the prompt to answer the initial user question. After, we pass the augmented prompt to the LLM for the final answer. Now the LLM will use the additional context to answer the user question.

There are two fundamental problems that RAG solves:

1\. Hallucinations

2\. Old or private information

### **Hallucinations**

If a chatbot without RAG is asked a question about something it wasn’t trained on, there are big changes that will give you a confident answer about something that isn’t true. Let’s take the 2024 soccer EURO Cup as an example. If the model is trained up to Oct 2023 and we ask something about the tournament, it will most likely come up with some random answer that is hard to differentiate from reality.

Even if the LLM doesn’t hallucinate all the time, it raises the concern of trust in its answers. Thus, we have to ask ourselves: “When can we trust the LLM’s answers?” and “How can we evaluate if the answers are correct?”

By introducing RAG, we will enforce the LLM to always answer solely based on the introduced context. The LLM will act as the reasoning engine, while the additional information added through RAG will act as the single source of truth for the generated answer.

By doing so, we can quickly evaluate if the LLM’s answer is based on the external data or not.

### **Old information**

Any LLM is trained or fine-tuned on a subset of the total world knowledge dataset. This is due to three main issues:

- **Private data:** You cannot train your model on data you don’t own or have the right to use.

- **New data**: New data is generated every second. Thus, you would have to constantly train your LLM to keep up.

- **Costs:** Training or fine-tuning an LLM is an extremely costly operation. Hence, it is not feasible to do it on an hourly or daily basis.


RAG solved these issues, as you no longer have to constantly fine-tune your LLM on new data (or even private data). Directly injecting the necessary data to respond to user questions into the prompts that are fed to the LLM is enough to generate correct and valuable answers.

## **The vanilla RAG framework**

Every RAG system is similar at its roots. We will first focus on understanding RAG in its simplest form. Later, we will gradually introduce more advanced RAG techniques to improve the system’s accuracy.

A RAG system is composed of three main modules independent of each other:

1. **Ingestion pipeline:** A batch or streaming pipeline used to populate the vector DB.

2. **Retrieval pipeline:** A module that queries the vector DB and retrieves relevant entries to the user’s input.

3. **Generation pipeline:** The layer that uses the retrieved data to augment the prompt and an LLM to generate answers.


As these three components are classes or services of their own, we will dig into each separately.

_But how are these three modules connected?_ Here is a very simplistic overview:

1. On the backend side, the ingestion pipeline runs on a schedule or constantly to populate the vector DB with external data.

2. On the client side, the user asks a question.

3. The question is passed to the retrieval module, which pre-processes the user’s input and queries the vector DB.

4. The generation pipelines use a prompt template, user input, and retrieved context to create the prompt.

5. The prompt is passed to an LLM to generate the answer.

6. The answer is shown to the user.


[https://substackcdn.com/image/fetch/$s_!nn9L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a6bf20-e217-4a8c-8df4-f00caa5c51ca_933x933.png](https://substackcdn.com/image/fetch/$s_!nn9L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77a6bf20-e217-4a8c-8df4-f00caa5c51ca_933x933.png)
Vanilla RAG architecture

### **Ingestion pipeline**

The RAG ingestion pipeline extracts raw documents from various data sources (e.g., data warehouse, data lake, web pages, etc.). Then, it cleans, chunks and embeds the documents. Ultimately, it loads the embedded chunks to a vector DB (or other similar vector storage).

Thus, the RAG ingestion pipeline is split again into the following:

- The **data extraction module** gathers all necessary data from various sources such as databases, APIs, or web pages. This module is highly dependent on your data. It can be as easy as querying your data warehouse or something more complex, such as crawling Wikipedia.

- A **cleaning layer** that standardizes and removes unwanted characters from the extracted data.

- The **chunking module** splits the cleaned documents into smaller ones. As we want to pass the document’s content to an embedding model, this is necessary to ensure it doesn’t exceed the model’s input maximum size. Also, chunking is required to separate specific regions that are semantically related. For example, when chunking a book chapter, the most optimal way is to group similar paragraphs into the same chunk. By doing so, at the retrieval time, you will add only the essential data to the prompt.

- The **embedding component** usesanembedding model to take the chunk’s content (text, images, audio, etc.) and project it into a dense vector packed with semantic value — more on embeddings in the Embeddings models section below.


The **loading module** takes the embedded chunks along with a metadata document. The metadata will contain essential information such as the embedded content, the URL to the source of the chunk, when the content was published on the web, etc. The embedding is used as an index to query similar chunks, while the metadata is used to access the information added to augment the prompt.

At this point, we have an RAG ingestion pipeline that takes raw documents as input, processes them, and populates a vector DB. The next step is to retrieve relevant data from the vector store correctly.

### **Retrieval pipeline**

The retrieval components take the user’s input (text, image, audio, etc.), embed it, and query the vector DB for similar vectors to the user’s input.

The primary function of the retrieval step is to project the user’s input into the same vector space as the embeddings used as an index in the vector DB. This allows us to find the top K’s most similar entries by comparing the embeddings from the vector storage with the user’s input vector. These entries then serve as content to augment the prompt that is passed to the LLM to generate the answer.

You must use a distance metric to compare two vectors, such as the Euclidean or Manhattan distance. But the most popular one is the [cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) \[1\], which is equal to 1 minus the cosine of the angle between two vectors as follows:

[https://substackcdn.com/image/fetch/$s_!LkC-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6d16dbc-de3b-4b57-9f31-07f06799ba57_397x46.jpeg](https://substackcdn.com/image/fetch/$s_!LkC-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6d16dbc-de3b-4b57-9f31-07f06799ba57_397x46.jpeg)
Cosine distance formula

It ranges from -1 to 1, with a value of -1 when vectors A and B are in opposite directions, 0 if they are orthogonal and 1 if they point in the same direction.

Most of the time, the cosine distance works well in non-linear complex vector spaces. However, it is essential to notice that choosing the proper distance between two vectors depends on your data and the embedding model you use.

One critical factor to highlight is that the user’s input and embeddings must be in the same vector space. Otherwise, you cannot compute the distance between them. To do so, it is essential to pre-process the user input in the same way you processed the raw documents in the RAG ingestion pipeline. It means you must clean, chunk (if necessary), and embed the user’s input using the same functions, models, and hyperparameters. Similar to how you have to pre-process the data into features in the same way between training and inference, otherwise the inference will yield inaccurate results — a phenomenon also known as the training-serving skew.

### **Generation pipeline**

The last step of the RAG system is to take the user’s input and the retrieved data, pass them to an LLM of your choice and generate the answer.

The final prompt results from a prompt template populated with the user’s query and retrieved context. You might have a single or multiple prompt templates depending on your application. Usually, all the prompt engineering is done at the prompt template level.

Each prompt template and LLM should be tracked and versioned using MLOps best practices. Thus, you always know that a given answer was generated by a specific version of the LLM and prompt template(s).

* * *

## **Conclusion**

In this article, we have looked over the fundamentals of RAG.

First, we understood why RAG is so powerful and why many AI applications implement it, as it overcomes challenges such as hallucinations and outdated data.

Secondly, we examined the architecture of a naive RAG system, which consists of an ingestion, retrieval and generation pipeline.

</details>

<details>
<summary>rag-is-dead-long-live-agentic-retrieval-llamaindex-build-kno</summary>

RAG has come a long way since the days of naive chunk retrieval; now agentic strategies are table stakes.

Nowadays, an AI engineer has to be aware of a plethora of techniques and terminology that encompass the data-retrieval aspects of agentic systems: hybrid search, CRAG, Self-RAG, HyDE, deep research, reranking, multi-modal embeddings, and RAPTOR just to name a few.

As we’ve built the Retrieval services in LlamaCloud, we’ve chosen to abstract a few of these techniques into our API, only exposing a few top-level hyper-parameters for controlling these algorithms. In this blog post, we will showcase these various techniques, explaining how and when to use them. We will build upon these techniques one by one and end with a fully agentic retrieval system that can intelligently query multiple knowledge bases at once.

## Starting with the basics

You can’t talk about RAG without talking about “naive top-k retrieval”. In this basic approach, document chunks are stored in a vector database, and query embeddings are matched with the `k` most similar chunk embeddings.https://www.llamaindex.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F7m9jw85w%2Fproduction%2F188534199027c3232c2c49248b0099295ddce603-576x1210.png%3Ffit%3Dmax%26auto%3Dformat&w=640&q=75Naive top-k RAG

Here’s a basic code snippet to index a simple folder of PDFs:

```
import os
from llama_index.indices.managed.llama_cloud import LlamaCloudIndex
# ^ pip install llama-index-indices-managed-llama-cloud

financial_index = LlamaCloudIndex.from_documents(
    documents=[],  # leave documents empty since we will be uploading the raw files
    name="Financial Reports",
    project_name=project_name,
)

financial_reports_directory = "./data/financial_reports"
for file_name in os.listdir(financial_reports_directory):
    file_path = os.path.join(financial_reports_directory, file_name)
    # Add each file to the slides index
    financial_index.upload_file(file_path, wait_for_ingestion=False)

financial_index.wait_for_completion()
```

Once this is indexing is completed, you can start retrieving these chunks with one more line:

```
query = "Where is Microsoft headquartered?"
nodes = financial_index.as_retriever().retrieve(query)
# or, if you've set up the Settings object, generate the full response here
response = financial_index.as_query_engine().query(query)
```

Going slightly beyond this naive `chunk` retrieval mode, there are also two more modes if you want to retrieve the entire contents of relevant files:

- `files_via_metadata` \- use this mode when you want to handle queries where a specific filename or pathname is mentioned e.g. “What does the 2024\_MSFT\_10K.pdf file say about the financial outlook of MSFT?”.
- `files_via_content` \- use this mode when you want to handle queries that are asking general questions about a topic but not a particular set of files e.g. “What is the financial outlook of MSFT?”.https://www.llamaindex.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F7m9jw85w%2Fproduction%2F3e6e040367e14d6b7133820e26531396fa8c1fdd-1072x624.png%3Ffit%3Dmax%26auto%3Dformat&w=1080&q=75Multiple retrieval modes

While `chunk` retrieval is the default mode, you can use one of the other retrieval modes via the `retrieval_mode` kwarg:

```
files_via_metadata_nodes = financial_index.as_retriever(retrieval_mode="files_via_metadata").retrieve(query)
files_via_content_nodes = financial_index.as_retriever(retrieval_mode="files_via_content").retrieve(query)
```

## Level up: Auto Mode

Now that we have an understanding how and when to use each of our retrieval modes, you’re now equipped with the power to answer any and all of types of questions about your knowledge base!

However, many applications will not know which type of question is being asked beforehand. Most of the time, these questions are being asked by your end user. You will need a way to know which retrieval mode would be most appropriate for the given query.

Enter the 4th retrieval mode - `auto_routed` mode! As the name suggests, this mode uses a lightweight agent to determine which of the other 3 retrieval modes to use for a given query.https://www.llamaindex.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F7m9jw85w%2Fproduction%2Fc2d0bd793627f4d38e93491cfe51ba0f8bad09a5-1316x1050.png%3Ffit%3Dmax%26auto%3Dformat&w=1920&q=75Agentically auto-routed retrieval

Using this mode is just as simple as using any of the other modes:

```
nodes = financial_index.as_retriever(retrieval_mode="auto_routed").retrieve("Where is Microsoft headquartered?")
# you can check which mode the query was routed to via the retrieval_mode metadata value
# this will print "chunks" since the input query is asking about specific information
print(nodes[0].metadata["retrieval_mode"])
```

## Expanding Beyond a single knowledge base

With the use of `auto_routed` mode, we have a lightweight agentic system that is capable of competently answering a variety of questions. However, this system is somewhat restricted in terms of its search space - it is only able to retrieve data that has been ingested in a single index.

If all of your documents are of the same format (e.g. they’re all just SEC 10K filings), it may be actually be appropriate for you to just ingest all your documents through a single index. The parsing and chunking configurations on that single index can be highly optimized to fit the formatting of this homogenous set of documents. However, your overall knowledge base will surely encompass a wide variety of file formats - SEC Filings, Meeting notes, Customer Service requests, etc. These other formats will necessitate the setup of separate indices whose parsing & chunking settings are optimized to each subset of documents.

Let’s say you have your SEC filings in the `financial_index` from the prior code snippets, and additionally have created a `slides_index` that has ingested `.ppt` PowerPoint files from a folder of slide shows.

```
import os
from llama_index.indices.managed.llama_cloud import LlamaCloudIndex
# ^ pip install llama-index-indices-managed-llama-cloud

slides_index = LlamaCloudIndex.from_documents(
    documents=[],  # leave documents empty since we will be uploading the raw files
    name="Slides",
    project_name=project_name,
)

# Add your slide files to the index
slides_directory = "./data/slides"
for file_name in os.listdir(slides_directory):
    file_path = os.path.join(slides_directory, file_name)
    # Add each file to the slides index
    slides_index.upload_file(file_path, wait_for_ingestion=False)
```

Your application may now have users asking questions about the SEC Filings you’ve ingested in `financial_index` & the meeting slide shows you’ve ingested in `slides_index`.

This is where our Composite Retrieval APIs shine! They provide a single Retrieval API to retrieve relevant content from many indices - not just one. The Composite Retrieval API exposes a lightweight agent layer to clients to allow them to specify a name & description for each sub-index. These parameters can help you control how the agent decides to route a question between the various indices you’ve added to your composite retriever.

```
from llama_cloud import CompositeRetrievalMode
from llama_index.indices.managed.llama_cloud import LlamaCloudCompositeRetriever

composite_retriever = LlamaCloudCompositeRetriever(
    name="My App Retriever",
    project_name=project_name,
    # If a Retriever named "My App Retriever" doesn't already exist, one will be created
    create_if_not_exists=True,
    # CompositeRetrievalMode.ROUTED will query route the query to a subset of indices
    mode=CompositeRetrievalMode.ROUTED,
    # return the top 5 results from all queried indices
    rerank_top_n=5,
)

# Add the above indices to the composite retriever
# Carefully craft the description as this is used internally to route a query to an attached sub-index when CompositeRetrievalMode.ROUTING is used
composite_retriever.add_index(
    slides_index,
    description="Information source for slide shows presented during team meetings",
)
composite_retriever.add_index(
    financial_index,
    description="Information source for company financial reports",
)

# Start querying across both of these indices at once
nodes = retriever.retrieve("What was the key feature of the highest revenue product in 2024 Q4?")
```

## Piecing Together a Knowledge Agent

Now that we know how to use agents for both individual and multi-index level, we can put together a single system that does agentic retrieval at every step of retrieval! Doing so will enable the use of an LLM to optimize every layer of our search path.

The system works like this:

1. At the top layer, the composite retriever uses LLM-based classification to decide which sub-index (or indices) are relevant for the given query.
2. At the sub-index level, the `auto_routed` retrieval mode determines the most appropriate retrieval method (e.g., `chunk`, `files_via_metadata`, or `files_via_content`) for the query.https://www.llamaindex.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F7m9jw85w%2Fproduction%2F9fdb15bafdf8c0921f36c6cd8cdac43c8ca87e27-2232x1562.png%3Ffit%3Dmax%26auto%3Dformat&w=3840&q=75Retrieval routed agentically across multiple auto-routed indexes

Here’s the code implementation:

```
from llama_cloud import CompositeRetrievalMode
from llama_index.indices.managed.llama_cloud import LlamaCloudCompositeRetriever

# Create a composite retriever
composite_retriever = LlamaCloudCompositeRetriever(
    name="Knowledge Agent",
    project_name=project_name,
    create_if_not_exists=True,
    mode=CompositeRetrievalMode.ROUTED,  # Use routed mode for intelligent index selection
    rerank_top_n=5,  # Rerank and return the top 5 results
)

# Add sub-indices with detailed descriptions
composite_retriever.add_index(
    financial_index,
    description="Detailed financial reports, including SEC filings and revenue analysis",
)
composite_retriever.add_index(
    slides_index,
    description="Slide shows from team meetings, covering product updates and project insights",
)

# Query the composite retriever
query = "What does the Q4 2024 financial report say about revenue growth?"
nodes = composite_retriever.retrieve(query)

# Print the retrieval mode used for the query and the results
for node in nodes:
    print(f"Retrieved from: {node.metadata['retrieval_mode']} - {node.text}")

```

This setup ensures that retrieval decisions are intelligently routed at each layer, using LLM-based classification to handle complex queries across multiple indices and retrieval modes. The result is a fully agentic retrieval system capable of adapting dynamically to diverse user queries.

### Naive RAG is dead, agentic retrieval is the future

Agents have become an essential part of modern applications. For these agents to operate effectively and autonomously, they need precise and relevant context at their fingertips. This is why sophisticated data retrieval is crucial for any agent-based system. LlamaCloud serves as the backbone for these intelligent systems, providing reliable, accurate context when and where agents need it most.

</details>

<details>
<summary>scraping-failed</summary>

⚠️ Error scraping https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation:

</details>

<details>
<summary>what-is-agentic-rag-ibm</summary>

Agentic RAG is the use of [AI agents](https://www.ibm.com/think/topics/ai-agents) to facilitate [retrieval augmented generation (RAG)](https://www.ibm.com/think/topics/retrieval-augmented-generation). Agentic RAG systems add AI agents to the RAG pipeline to increase adaptability and accuracy. Compared to traditional RAG systems, agentic RAG allows [large language models (LLMs)](https://www.ibm.com/think/topics/large-language-models) to conduct [information retrieval](https://www.ibm.com/think/topics/information-retrieval) from multiple sources and handle more complex [workflows](https://www.ibm.com/think/topics/workflow).

### What is RAG?

Retrieval augmented generation is an [artificial intelligence (AI)](https://www.ibm.com/think/topics/artificial-intelligence) application that connects a [generative AI](https://www.ibm.com/think/topics/generative-ai) model with an external knowledge base. The data in the knowledge base augments user queries with more context so the LLM can generate more accurate responses. RAG enables LLMs to be more accurate in domain-specific contexts without needing [fine-tuning](https://www.ibm.com/think/topics/fine-tuning).

Rather than rely solely on training data, RAG-enabled [AI models](https://www.ibm.com/think/topics/ai-model) can access current data in real time through [APIs](https://www.ibm.com/think/topics/api) and other connections to data sources. A standard RAG pipeline comprises two AI models:

- The information retrieval component, typically an [embedding](https://www.ibm.com/think/topics/embedding) model paired with a [vector database](https://www.ibm.com/think/topics/vector-database) containing the data to be retrieved.

- The [generative AI](https://www.ibm.com/think/topics/generative-ai) component, usually an LLM.

In response to [natural language](https://www.ibm.com/think/topics/natural-language-processing) user queries, the embedding model converts the query to a vector embedding, then retrieves similar data from the knowledge base. The AI system combines the retrieved data with the user query for context-aware response generation.

### What is agentic AI?

Agentic AI is a type of AI that can determine and carry out a course of action by itself. Most agents available at the time of publishing are LLMs with function-calling capabilities, meaning that they can call tools to perform tasks. In theory, AI agents are LLMs with three significant characteristics:

- They have **memory**, both short and long term, which enables them to plan and execute complex tasks. Memory also allows agents to refer to previous tasks and use that data to inform future workflows. Agentic RAG systems use semantic caching to store and refer to previous sets of queries, context and results.

- They are capable of query **routing**, step-by-step **planning** and decision-making. Agents use their memory capabilities to retain information and plot an appropriate course of action in response to complex queries and prompts.

- They can perform **tool calling** through APIs. More capable agents can choose which tools to use for the workflow they generate in response to user interactions.

Agentic workflows can consist of either one AI agent or multiagent systems that combine several agents together.

## Agentic RAG vs. traditional RAG systems

Agentic RAG brings several significant improvements over traditional RAG implementation:

- **Flexibility:** Agentic RAG applications pull data from multiple external knowledge bases and allow for external tool use. Standard RAG pipelines connect an LLM to a single external dataset. For example, many enterprise RAG systems pair a [chatbot](https://www.ibm.com/think/topics/chatbots) with a knowledge base containing proprietary organization data.

- **Adaptability:** Traditional RAG systems are reactive data retrieval tools that find relevant information in response to specific queries. There is no ability for the RAG system to adapt to changing contexts or access other data. Optimal results often require extensive [prompt engineering](https://www.ibm.com/think/topics/prompt-engineering).

Meanwhile, agentic RAG is a transition from static rule-based querying to adaptive, intelligent problem-solving. Multiagent systems encourage multiple AI models to collaborate and check each other’s work.

- **Accuracy:** Traditional RAG systems do not validate or optimize their own results. People must discern whether the system is performing at an acceptable standard. The system itself has no way of knowing whether it is finding the right data or successfully incorporating it to facilitate context-aware generation. However, AI agents can iterate on previous processes to optimize results over time.

- **Scalability:** With networks of RAG agents working together, tapping into multiple external data sources and using tool-calling and planning capabilities, agentic RAG has greater scalability. Developers can construct flexible and scalable RAG systems that can handle a wide range of user queries.

- **Multimodality:** Agentic RAG systems benefit from recent advancements in multimodal LLMs to work with a greater range of data types, such as images and audio files. Multimodal models process multiple types of [structured, semistructured and unstructured data](https://www.ibm.com/think/topics/structured-vs-unstructured-data). For example, several recent [GPT](https://www.ibm.com/think/topics/gpt) models can generate visual and audio content in addition to standard text generation.

Consider several employees working in an office. A traditional RAG system is the employee who performs well when given specific tasks and told how to accomplish them. They are reluctant to take initiative and feel uncomfortable going outside explicit instructions.

In comparison, an agentic RAG system is a proactive and creative team. They are also good at following directions but love to take initiative and solve challenges on their own. They are unafraid to come up with their own solutions to complex tasks that might stump or intimidate their coworkers.

### Is agentic RAG better than traditional RAG?

While agentic RAG optimizes results with function calling, multistep reasoning and multiagent systems, it isn’t always the better choice. More agents at work mean greater expenses, and an agentic RAG system usually require paying for more tokens. While agentic RAG can increase speed over traditional RAG, LLMs also introduce latency because it can take more time for the model to generate its outputs.

Lastly, agents are not always reliable. They might struggle and even fail to complete tasks, depending on the complexity and the agents used. Agents do not always collaborate smoothly and can compete over resources. The more agents in a system, the more complex the collaboration becomes, with a higher chance for complications. And even the most airtight RAG system cannot eliminate the potential for hallucinations entirely.

## How does agentic RAG work?

Agentic RAG works by incorporating one or more types of AI agents into RAG systems. For example, an agentic RAG system might combine multiple information retrieval agents, each specialized in a certain domain or type of data source. One agent queries external databases while another can comb through emails and web results.

[Agentic AI frameworks](https://www.ibm.com/think/insights/top-ai-agent-frameworks), such as [LangChain](https://www.ibm.com/think/topics/langchain) and [LlamaIndex](https://www.ibm.com/think/topics/llamaindex), and the orchestration framework [LangGraph](https://www.ibm.com/think/topics/langgraph) can be found on GitHub. With them, it is possible to experiment with [agentic architectures](https://www.ibm.com/think/topics/agentic-architecture) for RAG at minimal costs. If using [open source](https://www.ibm.com/think/topics/open-source) models such as [Granite](https://www.ibm.com/granite) ™ or Llama-3, RAG system designers can also mitigate the fees demanded by other providers such as OpenAI while enjoying greater [observability](https://www.ibm.com/think/topics/observability).

Agentic RAG systems can contain one or more types of AI agents, such as:

- Routing agents

- Query planning agents

- ReAct agents

- Plan-and-execute agents

### Routing agents

Routing agents determine which external knowledge sources and tools are used to address a user query. They process user prompts and identify the RAG pipeline most likely to result in optimal response generation. In a single-agent RAG system, a routing agent chooses which data source to query.

### Query planning agents

Query planning agents are the task managers of the RAG pipeline. They process complex user queries to break them down into step-by-step processes. They submit the resulting subqueries to the other agents in the RAG system, then combine the responses for a cohesive overall response. The process of using one agent to manage other AI models is a type of [AI orchestration](https://www.ibm.com/think/topics/ai-orchestration).

### ReAct agents

ReAct (reasoning and action) is an agent framework that creates [multiagent systems](https://www.ibm.com/think/topics/multiagent-system) that can create and then act on step-by-step solutions. They can also identify appropriate tools that can help. Based on the results of each step, ReAct agents can dynamically adjust subsequent stages of the generated workflow.

### Plan-and-execute agents

Plan-and-execute agent frameworks are a progression from ReAct agents. They can execute multistep workflows without calling back to the primary agent, reducing costs and increasing efficiency. And because the planning agent must reason through all the steps needed for a task, completion rates and quality tend to be higher.

## Agentic RAG use cases

While agentic RAG can suit any traditional RAG application, the greater compute demands make it more appropriate for situations that require querying multiple data sources. Agentic RAG applications include:

- **Real-time question-answering:** Enterprises can deploy RAG-powered chatbots and FAQs to provide employees and customers with current, accurate information.

- **Automated support:** Businesses wanting to streamline customer support services can use automated RAG systems to handle simpler customer inquiries. The agentic RAG system can escalate more demanding support requests to human personnel.

- **Data management:** RAG systems make it easier to find information within proprietary data stores. Employees can quickly get the data they need without having to sort through databases themselves.

</details>

<details>
<summary>what-is-agentic-rag-weaviate</summary>

While Retrieval-Augmented Generation (RAG) dominated 2023, [agentic workflows are driving massive progress in 2024](https://x.com/AndrewYNg/status/1770897666702233815?lang=en). The usage of AI agents opens up new possibilities for building more powerful, robust, and versatile Large Language Model(LLM)-powered applications. One possibility is enhancing RAG pipelines with AI agents in agentic RAG pipelines.

This article introduces you to the concept of agentic RAG, its implementation, and its benefits and limitations.

## Fundamentals of Agentic RAG

Agentic RAG describes an AI agent-based implementation of RAG. Before we go any further, let’s quickly recap the fundamental concepts of RAG and AI agents.

### What is Retrieval-Augmented Generation (RAG)

[Retrieval-Augmented Generation (RAG)](https://weaviate.io/blog/introduction-to-rag) is a technique for building LLM-powered applications. It leverages an external knowledge source to provide the LLM with relevant context and reduce hallucinations.

A naive RAG pipeline consists of a retrieval component (typically composed of an embedding model and a vector database) and a generative component (an LLM). At inference time, the user query is used to run a similarity search over the indexed documents to retrieve the most similar documents to the query and provide the LLM with additional context.https://weaviate.io/assets/images/Vanilla_RAG-697535e2d5b9ae64ccfd6415a79965c7.png

Typical RAG applications have two considerable limitations:

1. The naive RAG pipeline only considers one external knowledge source. However, some solutions might require two external knowledge sources, and some solutions might require external tools and APIs, such as web searches.
2. They are a one-shot solution, which means that context is retrieved once. There is no reasoning or validation over the quality of the retrieved context.

### What are Agents in AI Systems

With the popularity of LLMs, new paradigms of AI agents and multi-agent systems have emerged. AI agents are LLMs with a role and task that have access to memory and external tools. The reasoning capabilities of LLMs help the agent plan the required steps and take action to complete the task at hand.

Thus, the core components of an AI agent are:

- LLM (with a role and a task)
- Memory (short-term and long-term)
- Planning (e.g., reflection, self-critics, query routing, etc.)
- Tools (e.g., calculator, web search, etc.)https://weaviate.io/assets/images/Components_of_an_AI_agent-2f1846374720471d6b11169203ccb865.png

One popular framework is the [ReAct framework](https://arxiv.org/abs/2210.03629). A ReAct agent can handle sequential multi-part queries while maintaining state (in memory) by combining routing, query planning, and tool use into a single entity.

> ReAct = Reason + Act (with LLMs)

The process involves the following steps:

1. Thought: Upon receiving the user query, the agent reasons about the next action to take

2. Action: the agent decides on an action and executes it (e.g., tool use)

3. Observation: the agent observes the feedback from the action

4. This process iterates until the agent completes the task and responds to the user.https://weaviate.io/assets/images/ReAct-6d7ea59cdc1c7f882f860e7015228302.png


## What is Agentic RAG?

Agentic RAG describes an AI agent-based implementation of RAG. Specifically, it incorporates AI agents into the RAG pipeline to orchestrate its components and perform additional actions beyond simple information retrieval and generation to overcome the limitations of the non-agentic pipeline.

> Agentic RAG describes an AI agent-based implementation of RAG.

### How does Agentic RAG work?

Although agents can be incorporated in different stages of the RAG pipeline, agentic RAG most commonly refers to the use of agents in the retrieval component.

Specifically, the retrieval component becomes agentic through the use of retrieval agents with access to different retriever tools, such as:

- Vector search engine (also called a query engine) that performs vector search over a vector index (like in typical RAG pipelines)
- Web search
- Calculator
- Any API to access software programmatically, such as email or chat programs
- and many more.

The RAG agent can then reason and act over the following example retrieval scenarios:

1. Decide whether to retrieve information or not
2. Decide which tool to use to retrieve relevant information
3. Formulate the query itself
4. Evaluate the retrieved context and decide whether it needs to re-retrieve.

### Agentic RAG Architecture

In contrast to the sequential naive RAG architecture, the core of the agentic RAG architecture is the agent. Agentic RAG architectures can have various levels of complexity. In the simplest form, a single-agent RAG architecture is a simple router. However, you can also add multiple agents into a multi-agent RAG architecture. This section discusses the two fundamental RAG architectures.

**Single-Agent RAG (Router)**

In its simplest form, agentic RAG is a router. This means you have at least two external knowledge sources, and the agent decides which one to retrieve additional context from. However, the external knowledge sources don't have to be limited to (vector) databases. You can retrieve further information from tools as well. For example, you can conduct a web search, or you could use an API to retrieve additional information from Slack channels or your email accounts.https://weaviate.io/assets/images/Single_Agent_RAG_System_(Router-ae2ec18616941504070d6b2a7210a358.png)

**Multi-agent RAG Systems**

As you can guess, the single-agent system also has its limitations because it's limited to only one agent with reasoning, retrieval, and answer generation in one. Therefore, it is beneficial to chain multiple agents into a multi-agent RAG application.

For example, you can have one master agent who coordinates information retrieval among multiple specialized retrieval agents. For instance, one agent could retrieve information from proprietary internal data sources. Another agent could specialize in retrieving information from your personal accounts, such as email or chat. Another agent could also specialize in retrieving public information from web searches.https://weaviate.io/assets/images/Multi_Agent_RAG_System-73e480f62a52e172a78a0ac344dcdcb5.png

### Beyond Retrieval Agents

The above example shows the usage of different retrieval agents. However, you could also use agents for purposes other than retrieval. The possibilities of agents in the RAG system are manifold.

## Agentic RAG vs. (Vanilla) RAG

While the fundamental concept of RAG (sending a query, retrieving information, and generating a response) remains the same, **tool use generalizes it,** making it more flexible and powerful.

Think of it this way: Common (vanilla) RAG is like being at the library (before smartphones existed) to answer a specific question. Agentic RAG, on the other hand, is like having a smartphone in your hand with a web browser, a calculator, your emails, etc.

|  | Vanilla RAG | Agentic RAG |
| --- | --- | --- |
| Access to external tools | No | Yes |
| Query pre-processing | No | Yes |
| Multi-step retrieval | No | Yes |
| Validation of retrieved information | No | Yes |

## Implementing Agentic RAG

As outlined earlier, agents are comprised of multiple components. To build an agentic RAG pipeline, there are two options: a language model with function calling or an agent framework. Both implementations get to the same result, it will just depend on the control and flexibility you want.

### Language Models with Function Calling

Language models are the main component of agentic RAG systems. The other component is tools, which enable the language model access to external services. Language models with function calling offer a way to build an agentic system by allowing the model to interact with predefined tools. Language model providers have added this feature to their clients.

In June 2023, [OpenAI released function calling](https://platform.openai.com/docs/assistants/tools/function-calling) for `gpt-3.5-turbo` and `gpt-4`. It enabled these models to reliably connect GPT’s capabilities with external tools and APIs. Developers quickly started building applications that plugged `gpt-4` into code executors, databases, calculators, and more.

[Cohere](https://docs.cohere.com/v2/docs/tool-use) further launched their connectors API to add tools to the Command-R suite of models. Additionally, [Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) and [Google](https://ai.google.dev/gemini-api/docs/function-calling) launched function calling for Claude and Gemini. By powering these models with external services, it can access and cite web resources, execute code and more.

Function calling isn’t only for proprietary models. Ollama introduced tool support for popular open-source models like `Llama3.2`, `nemotron-mini`, and [others](https://ollama.com/search?c=tools).

To build a tool, you first need to define the function. In this snippet, we’re writing a function that is using Weaviate’s [hybrid search](https://docs.weaviate.io/weaviate/search/hybrid) to retrieve objects from the database:

```codeBlockLines_e6Vv
def get_search_results(query: str) -> str:
    """Sends a query to Weaviate's Hybrid Search. Parses the response into a {k}:{v} string."""

    response = blogs.query.hybrid(query, limit=5)

    stringified_response = ""
    for idx, o in enumerate(response.objects):
        stringified_response += f"Search Result: {idx+1}:\n"
        for prop in o.properties:
            stringified_response += f"{prop}:{o.properties[prop]}"
        stringified_response += "\n"

    return stringified_response

```

We will then pass the function to the language model via a `tools_schema`. The schema is then used in the prompt to the language model:

```codeBlockLines_e6Vv
tools_schema=[{\
    'type': 'function',\
    'function': {\
        'name': 'get_search_results',\
        'description': 'Get search results for a provided query.',\
        'parameters': {\
          'type': 'object',\
          'properties': {\
            'query': {\
              'type': 'string',\
              'description': 'The search query.',\
            },\
          },\
          'required': ['query'],\
        },\
    },\
}]

```

Since you’re connecting to the language model API directly, you’ll need to write a loop that routes between the language model and tools:

```codeBlockLines_e6Vv
def ollama_generation_with_tools(user_message: str,
                                 tools_schema: List, tool_mapping: Dict,
                                 model_name: str = "llama3.1") -> str:
    messages=[{\
        "role": "user",\
        "content": user_message\
    }]
    response = ollama.chat(
        model=model_name,
        messages=messages,
        tools=tools_schema
    )
    if not response["message"].get("tool_calls"):
        return response["message"]["content"]
    else:
        for tool in response["message"]["tool_calls"]:
            function_to_call = tool_mapping[tool["function"]["name"]]
            print(f"Calling function {function_to_call}...")
            function_response = function_to_call(tool["function"]["arguments"]["query"])
            messages.append({
                "role": "tool",
                "content": function_response,
            })

    final_response = ollama.chat(model=model_name, messages=messages)
    return final_response["message"]["content"]

```

Your query will then look like this:

```codeBlockLines_e6Vv
ollama_generation_with_tools("How is HNSW different from DiskANN?",
                            tools_schema=tools_schema, tool_mapping=tool_mapping)

```

You can follow along [this recipe](https://github.com/weaviate/recipes/blob/main/integrations/llm-agent-frameworks/function-calling/ollama/ollama-weaviate-agents.ipynb) to recreate the above.

### Agent Frameworks

Agent Frameworks such as DSPy, LangChain, CrewAI, LlamaIndex, and Letta have emerged to facilitate building applications with language models. These frameworks simplify building agentic RAG systems by plugging pre-built templates together.

- DSPy supports [ReAct](https://dspy-docs.vercel.app/deep-dive/modules/react/) agents and [Avatar](https://github.com/stanfordnlp/dspy/blob/main/examples/agents/avatar_langchain_tools.ipynb) optimization. Avatar optimization describes the use of automated prompt engineering for the descriptions of each tool.
- [LangChain](https://www.langchain.com/) provides many services for working with tools. LangChain’s [LCEL](https://python.langchain.com/v0.1/docs/expression_language/) and [LangGraph](https://www.langchain.com/langgraph) frameworks further offer built-in tools.
- [LlamaIndex](https://www.llamaindex.ai/) further introduces the QueryEngineTool, a collection of templates for retrieval tools.
- [CrewAI](https://www.crewai.com/) is one of the leading frameworks for developing multi-agent systems. One of the key concepts utilized for tool use is sharing tools amongst agents.
- [Swarm](https://github.com/openai/swarm) is a framework built by OpenAI for multi-agent orchestration. Swarm similarly focuses on how tools are shared amongst agents.
- [Letta](https://docs.letta.com/introduction) interfaces reflecting and refining an internal world model as functions. This entails potentially using search results to update the agent’s memory of the chatbot user, in addition to responding to the question.

## Why are Enterprises Adopting Agentic RAG

Enterprises are moving on from vanilla RAG to building agentic RAG applications. [Replit released an agent](https://docs.replit.com/replitai/agent) that helps developers build and debug software. Additionally, [Microsoft announced copilots](https://blogs.microsoft.com/blog/2024/10/21/new-autonomous-agents-scale-your-team-like-never-before/) that work alongside users to provide suggestions in completing tasks. These are only a few examples of agents in production and the possibilities are endless.

### Benefits of Agentic RAG

The shift from vanilla RAG to agentic RAG allows these systems to produce more accurate responses, perform tasks autonomously, and better collaborate with humans.

The benefit of agentic RAG lies primarily in the improved quality of retrieved additional information. By adding agents with access to tool use, the retrieval agent can route queries to specialized knowledge sources. Furthermore, the reasoning capabilities of the agent enable a layer of validation of the retrieved context before it is used for further processing. As a result, agentic RAG pipelines can lead to more robust and accurate responses.

### Limitations of Agentic RAG

However, there are always two sides to every coin. Using an AI agent a for subtask means incorporating an LLM to do a task. This comes with the limitations of using LLMs in any application, such as added latency and unreliability. Depending on the reasoning capabilities of the LLM, an agent may fail to complete a task sufficiently (or even at all). It is important to incorporate proper failure modes to help an AI agent get unstuck when they are unable to complete a task.

## Summary

This blog discussed the concept of agentic RAG, which involves incorporating agents into the RAG pipeline. Although agents can be used for many different purposes in a RAG pipeline, agentic RAG most often involves using retrieval agents with access to tools to generalize retrieval.

This article discussed agentic RAG architectures using single-agent and multi-agent systems and their differences from vanilla RAG pipelines.

With the rise and popularity of AI agent systems, many different frameworks are evolving for implementing agentic RAG, such as LlamaIndex, LangGraph, or CrewAI.

Finally, this article discussed the benefits and limitations of agentic RAG pipelines.

</details>

<details>
<summary>what-is-retrieval-augmented-generation-aka-rag-nvidia-blogs</summary>

To understand the latest advancements in [generative AI](https://www.nvidia.com/en-us/glossary/data-science/generative-ai/), imagine a courtroom.

Judges hear and decide cases based on their general understanding of the law. Sometimes a case — like a malpractice suit or a labor dispute — requires special expertise, so judges send court clerks to a law library, looking for precedents and specific cases they can cite.

Like a good judge, large language models ( [LLMs](https://www.nvidia.com/en-us/glossary/data-science/large-language-models/)) can respond to a wide variety of human queries. But to deliver authoritative answers — grounded in specific court proceedings or similar ones  — the model needs to be provided that information.

The court clerk of AI is a process called [retrieval-augmented generation](https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/), or RAG for short.

## **So, What Is Retrieval-Augmented Generation (RAG)?**

[Retrieval-augmented generation](https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/) is a technique for enhancing the accuracy and reliability of generative AI models with information fetched from specific and relevant data sources.

In other words, it fills a gap in how LLMs work. Under the hood, LLMs are neural networks, typically measured by how many parameters they contain. An LLM’s parameters essentially represent the general patterns of how humans use words to form sentences.

That deep understanding, sometimes called parameterized knowledge, makes LLMs useful in responding to general prompts. However, it doesn’t serve users who want a deeper dive into a specific type of information.

## **Combining Internal, External Resources**

Lewis and colleagues developed retrieval-augmented generation to link generative AI services to external resources, especially ones rich in the latest technical details.

The paper, with coauthors from the former Facebook AI Research (now Meta AI), University College London and New York University, called RAG “a general-purpose fine-tuning recipe” because it can be used by nearly any LLM to connect with practically any external resource.

## **Building User Trust**

Retrieval-augmented generation gives models sources they can cite, like footnotes in a research paper, so users can check any claims. That builds trust.

What’s more, the technique can help models clear up ambiguity in a user query. It also reduces the possibility that a model will give a very plausible but incorrect answer, a phenomenon called hallucination.

Another great advantage of RAG is it’s relatively easy. A [blog](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/) by Lewis and three of the paper’s coauthors said developers can implement the process with as few as [five lines of code](https://huggingface.co/facebook/rag-token-nq).

That makes the method faster and less expensive than retraining a model with additional datasets. And it lets users hot-swap new sources on the fly.

## **How People Are Using RAG**

With retrieval-augmented generation, users can essentially have conversations with data repositories, opening up new kinds of experiences. This means the applications for RAG could be multiple times the number of available datasets.

For example, a generative AI model supplemented with a medical index could be a great assistant for a doctor or nurse. Financial analysts would benefit from an assistant linked to market data.

In fact, almost any business can turn its technical or policy manuals, videos or logs into resources called knowledge bases that can enhance LLMs. These sources can enable use cases such as customer or field support, employee training and developer productivity.

The broad potential is why companies including [AWS](https://aws.amazon.com/blogs/machine-learning/simplify-access-to-internal-information-using-retrieval-augmented-generation-and-langchain-agents/), [IBM](https://research.ibm.com/blog/retrieval-augmented-generation-RAG), [Glean](https://www.glean.com/resources/guides/what-is-retrieval-augmented-generation-rag), [Google](https://cloud.google.com/use-cases/retrieval-augmented-generation?hl=en), [Microsoft](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), NVIDIA, [Oracle](https://www.oracle.com/artificial-intelligence/generative-ai/retrieval-augmented-generation-rag/) and [Pinecone](https://www.pinecone.io/learn/retrieval-augmented-generation/) are adopting RAG.

## **The History of RAG**

The roots of the technique go back at least to the early 1970s. That’s when researchers in information retrieval prototyped what they called question-answering systems, apps that use natural language processing ( [NLP](https://www.nvidia.com/en-us/glossary/natural-language-processing/)) to access text, initially in narrow topics such as baseball.

The concepts behind this kind of text mining have remained fairly constant over the years. But the machine learning engines driving them have grown significantly, increasing their usefulness and popularity.

In the mid-1990s, the Ask Jeeves service, now Ask.com, popularized question answering with its mascot of a well-dressed valet. IBM’s Watson became a TV celebrity in 2011 when it handily beat two human champions on the _Jeopardy!_ game show.

[https://blogs.nvidia.com/wp-content/uploads/2023/11/Ask-Jeeves-2.jpg](https://blogs.nvidia.com/wp-content/uploads/2023/11/Ask-Jeeves-2.jpg)

Today, LLMs are taking question-answering systems to a whole new level.

## **Insights From a London Lab**

The seminal 2020 paper arrived as Lewis was pursuing a doctorate in NLP at University College London and working for Meta at a new London AI lab. The team was searching for ways to pack more knowledge into an LLM’s parameters and using a benchmark it developed to measure its progress.

Building on earlier methods and inspired by [a paper](https://arxiv.org/pdf/2002.08909.pdf) from Google researchers, the group “had this compelling vision of a trained system that had a retrieval index in the middle of it, so it could learn and generate any text output you wanted,” Lewis recalled.

[https://blogs.nvidia.com/wp-content/uploads/2023/11/IBM-Watson-wins-Jeopardy-YT.jpg](https://blogs.nvidia.com/wp-content/uploads/2023/11/IBM-Watson-wins-Jeopardy-YT.jpg) The IBM Watson question-answering system became a celebrity when it won big on the TV game show Jeopardy!

When Lewis plugged into the work in progress a promising retrieval system from another Meta team, the first results were unexpectedly impressive.

“I showed my supervisor and he said, ‘Whoa, take the win. This sort of thing doesn’t happen very often,’ because these workflows can be hard to set up correctly the first time,” he said.

Lewis also credits major contributions from team members Ethan Perez and Douwe Kiela, then of New York University and Facebook AI Research, respectively.

When complete, the work, which ran on a cluster of NVIDIA GPUs, showed how to make generative AI models more authoritative and [trustworthy](https://blogs.nvidia.com/blog/what-is-trustworthy-ai/). It’s since been cited by hundreds of papers that amplified and extended the concepts in what continues to be an active area of research.

## **How Retrieval-Augmented Generation Works**

At a high level, here’s [how retrieval-augmented generation works](https://developer.nvidia.com/topics/ai/retrieval-augmented-generation).

When users ask an LLM a question, the AI model sends the query to another model that converts it into a numeric format so machines can read it. The numeric version of the query is sometimes called an embedding or a vector.https://blogs.nvidia.com/wp-content/uploads/2024/11/ragexplainer131-960x1143.pngIn retrieval-augmented generation, LLMs are enhanced with embedding and reranking models, storing knowledge in a vector database for precise query retrieval.

The embedding model then compares these numeric values to vectors in a machine-readable index of an available knowledge base. When it finds a match or multiple matches, it retrieves the related data, converts it to human-readable words and passes it back to the LLM.

Finally, the LLM combines the retrieved words and its own response to the query into a final answer it presents to the user, potentially citing sources the embedding model found.

## **Keeping Sources Current**

In the background, the embedding model continuously creates and updates machine-readable indices, sometimes called vector databases, for new and updated knowledge bases as they become available.

[https://blogs.nvidia.com/wp-content/uploads/2023/11/LangChain-2-LLM-with-a-retriveal-process-672x268.jpg](https://blogs.nvidia.com/wp-content/uploads/2023/11/LangChain-2-LLM-with-a-retriveal-process.jpg) Retrieval-augmented generation combines LLMs with embedding models and vector databases.

Many developers find LangChain, an open-source library, can be particularly useful in chaining together LLMs, embedding models and knowledge bases. NVIDIA uses LangChain in its reference architecture for retrieval-augmented generation.

The LangChain community provides its own [description of a RAG process](https://blog.langchain.dev/tutorial-chatgpt-over-your-data/).

The future of generative AI lies in [agentic AI](https://blogs.nvidia.com/blog/what-is-agentic-ai/) — where LLMs and knowledge bases are dynamically orchestrated to create autonomous assistants. These AI-driven agents can enhance decision-making, adapt to complex tasks and deliver authoritative, verifiable results for users.

</details>
