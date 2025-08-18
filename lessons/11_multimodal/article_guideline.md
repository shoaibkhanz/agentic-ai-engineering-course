## Global Context of the Lesson

### What We Are Planning to Share

A hands-on lesson presenting the fundamentals of working with multimodal data in the context of LLMs, LLM workflows and AI Agents. When building AI apps, in the real world, we rarely work only with text data. As human beings we work daily with all types of data: text, images, documents, audio. Thus, having them integrated into our AI systems is a must. This quickly translates to a business problem, where all enterprise grade AI apps use and require multimodal data (text, images, documents) when manipulating their private data from databases, warehouses and lakes. 

In the early days, most AI apps tried to normalize everything to text. For example, we used OCRs to parse documents and map them to text or tabular data. The plot twist behind this lesson is that instead of translating images or documents to text, when building AI and RAG systems, it's better and recommened to process them directly as native images or documents. Like this we can natively pass all the visual rich information to the model. To understand how to do that we have to cover a few theoretical aspects such as how multimodal LLMs, embedding models, and RAG systems work. Just enough theory for the reader to have an intuition on how these works. Then, we will implement a few hands-on use cases where we explain how to work with LLM with text, images, and documents combined. Then we will connect the reader to the bigger picture and show them, first, how to build a simple text-image RAG system, and then an agentic RAG app. We want to highlight that once you built an text-image system, as the documents are processed as images as well, mapping it to a text-images-document modality is a no brainer.

So this lesson will provide all the knowledge to built enterprise AI agents or LLM workflows that can process your personal or organization data. Side note: most of these techniques can be transalted to video or audio, but that won't be covered here.

### Why We Think It's Valuable

Often, we have to manipulate various types of multimodal data such as text, images, and documents within the same context window and tools. Most of the issues come when we start threating each image or document the same. We cannot do that. An extremely popular example is building AI agents that process various financial PDFs that sometimes contain only text and sometime tables, diagrams and graphs from various reports and research. If we try to translate the documents or images with complex layouts to text we loose a lot of information, resulting in suboptimal solutions. Thus, instead of using OCR-based systems that normalize everything to text, modern AI systems directly processs data input in their native format (documents, images, audio), preserving all the rich information made possible by their specific format. For example if we translate sketches or diagrams to text it's impossible to grasp all the details, such as the colors and geometrical relationships between the elements, in text. But directly processing the image, as a human would, it's easier to implement, faster, cheaper, more intutive and usually more performant. That's why AI apps MUST have native support for images and documents to easily process complex data formats and relationships that are natural for a human being to use in their daily workflow.

### Expected Length of the Lesson

**3250 words** (without the titles and references), where we assume that 200-250 words ≈ 1 minute of reading time.

### Theory / Practice Ratio

30% theory - 70% real-world examples

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 4 parts, each with multiple lessons. 

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in its journey. You will be careful to consider the following:
- The points of view
- To not reintroduce concepts already taught in the previous lesson.
- To be careful when talking about concepts introduced only in future lessons
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

This is lesson 11 (from part 3) of the course on working with multimodal data, such as text, images and documents.

### Point of View
The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

Examples of correct point of view:
- Instead of "Before we can choose between workflows and agents, we need a clear understanding of what they are." word it as "To choose between workflows and agents, you need a clear understanding of what they are."

### Who Is the Intended Audience

Aspiring AI engineers who are learning about working with multimodal data for the first time.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:

**Part 1:**

- **Lesson 1 - AI Engineering & Agent Landscape**: Understanding the role, the stack, and why agents matter now
- **Lesson 2 - Workflows vs. Agents**: Grasping the crucial difference between predefined logic and LLM-driven autonomy
- **Lesson 3 - Context Engineering**: The art of managing information flow to LLMs
- **Lesson 4 - Structured Outputs**: Ensuring reliable data extraction from LLM responses
- **Lesson 5 - Basic Workflow Ingredients**: Implementing chaining, routing, parallel and the orchestrator-worker patterns
- **Lesson 6 - Agent Tools & Function Calling**: Giving your LLM the ability to take action
- **Lesson 7 - Planning & Reasoning**: Understanding patterns like ReAct (Reason + Act)
- **Lesson 8 - Implementing ReAct**: Building a reasoning agent from scratch
- **Lesson 9 - Agent Memory & Knowledge**: Short-term vs. long-term memory (procedural, episodic, semantic)
- **Lesson 10 - RAG Deep Dive**: Advanced retrieval techniques for knowledge-augmented agents

As this is only the last lesson of the first part of the course, we introduced most of the required concepts for people to work with LLM workflows and AI agents, except the last piece of the puzzle: multimodal data.

### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:

**Part 1:**

DONE - except the current lesson on multimodal data

**Part 2:**

In this section, you'll move from theory to practice by starting your work on the course's central project: an interconnected research and writing agent system. After a deep dive into agentic design patterns and a comparative look at modern frameworks, we'll focus on LangGraph. You will implement the research agent, equipping it with tools for web scraping and analysis. Then, you'll construct the writing workflow to convert research into polished content. Finally, you'll integrate these components, working on the orchestration of a complete, multi-agent pipeline from start to finish.

Other concepts from Part 2:
- MCP

**Part 3:**

With the agent system built, this section focuses on the engineering practices required for production. You will learn to design and implement robust evaluation frameworks to measure and guarantee agent reliability, moving far beyond simple demos. We will cover AI observability, using specialized tools to trace, debug, and understand complex agent behaviors. Finally, you’ll explore optimization techniques for cost and performance and learn the fundamentals of deploying your agent system, ensuring it is scalable and ready for real-world use.

**Part 4:**

In this final part of the course, you will build and submit your own advanced LLM agent, applying what you've learned throughout the previous sections. We provide a complete project template repository, enabling you to either extend our agent pipeline or build your own novel solution. Your project will be reviewed to ensure functionality, relevance, and adherence to course guidelines for the awarding of your course certification.

### Anchoring the Reader in the Educational Journey

Within the course we are teaching the reader multiple topics and concepts. Thus, understanding where the reader is in their educational journey is critical for this piece. You have to use only previously introduced concepts, while being reluctant about using concepts that haven't been introduced yet.

When discussing the **concepts introduced in previous lessons** listed in the `Concepts Introduced in Previous Lessons` section, avoid reintroducing them to the reader. Especially don't reintroduce the acronyms. Use them as if the reader already knows what they are. 

Avoid using all the **concepts that haven't been introduced in previous lessons** listed in the `Concepts That Will Be Introduced in Future Lessons` subsection. Whenever another concept requires references to these banned concepts, instead of directly using them, use intuitive analogies or explanations that are more general and easier to understand, as you would explain them to a 7-year-old. For example:
- If the "tools" concept wasn't introduced yet and you have to talk about agents, refer to them as "actions".
- If the "routing" concept wasn't introduced yet and you have to talk about it, refer to it as "guiding the workflow between multiple decisions".
You can use the concepts that haven't been introduced in previous lessons listed in the `Concepts That Will Be Introduced in Future Lessons` subsection only if we explicitly specify them. Still, even in that case, as the reader doesn't know how that concept works, you are only allowed to use the term, while keeping the explanation extremely high-level and intuitive, as if you were explaining it to a 7-year-old.
Whenever you use a concept from the `Concepts That Will Be Introduced in Future Lessons` subsection, explicitly specify in what lesson it will be explained in more detail, leveraging the particulars from the subsection. If not explicitly specified in the subsection, simply state that we will cover it in future lessons without providing a concrete lesson number. 

In all use cases avoid using acronyms that aren't explicitly stated in the guidelines. Rather use other more accessible synonyms or descriptions that are easier to understand by non-experts.

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we learning to solve? Why is it essential to solve it?
    - Start with a personal story where we encountered the problem
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger field of AI Engineering. Add course next steps.

## Lesson Outline 

1. Section 1 - Introduction: The need for multimodal AI
2. Section 2: Limitations of traditional document processing
3. Section 3: Foundations of multimodal LLMs
4. Section 4: Applying multimodal LLMs to images and PDFs
5. Section 5: Foundations of multimodal RAG (ColPali architecture)
6. Section 6: Implementing multimodal RAG for images and text
7. Section 7: Building multimodal AI agents
8. Section 8: Conclusion


## Section 1 - Introduction: The need for multimodal AI
(What problem are we learning to solve? Why is it essential to solve it?)

- **Quick reference to what we've learned in previous lessons:** Take the core ideas of what we've learned in previous lessons from the `Concepts Introduced in Previous Lessons` subsection of the `Anchoring the Lesson in the Course` section.
- **Transition to what we'll learn in this lesson:** After presenting what we learned in the past, make a transition to what we will learn in this lesson. Take the core ideas of the lesson from the `What We Are Planning to Share` subsection and highlight the importance and existence of the lesson from the `Why We Think It's Valuable` subsection of the `Global Context of the Lesson` section.

- On top of the general WHAT and WHY give some industry real-world use cases and limitations of text-only approaches. At the moment you can keep them more general, just to anchor the reader in the real-world:
    - Use cases:
        - Object detection and classification in images
        - Image captioning
    - Limitations:
        - Financial reports with complex charts
        - Research assistants processing charts and diagrams
        - Medical documents with diagnostics
        - Technical documents with diagrams
        - Building sketches 

-  **Section length:** 100 words

## Section 2: Limitations of traditional document processing
(What problem are we learning to solve? Why is it essential to solve it?)

- To sediment the problem, dig deeper into the limitations of traditional document processing. The problem can be translated to other data types such as images or audio. The core and real idea is that previous approaches tried to normalize everything to text before passing it into an AI model, which has many flaws, as during the translation we loose a ton of information. For example, when encountering diagrams, charts or sketches into a document, it's impossible to fully reproduce them in text. 
- Make our point, by digging deeper into the problem of processing documents as text using OCR-based systems
- Give a high-level overview of traditional document processing workflows done with Layout detection + OCR. Use processing a PDF mixed with text, diagrams and tables, as an example:
    1. Load the document
    2. Document preprocessing (e.g., noise removal)
    3. Layout detection for different regions with the document
    3. Use OCR models to process text regions and other specialzed models for each expected data structure such as images, tables, charts, etc.
    4. Output the text + other metadata as JSON or other structured data formats (images, tables, charts, etc.)
    (Figure 1: Create a marmaid diagram of this flow.)
- Challenges. Too many moving pieces within the flow - layout detection, OCR models, and different models for each data structures. This makes the system:
    1. rigid to new data structures (e.g., if a document contains charts and we don't have a model for it, it will fail)
    2. slow and costly as we have to call too many models
    3. fragile as we have to keep in check all these models
    4. Performance challenges:
        - The multi-step nature of traditional document processing creates a cascade effect where errors compound at each stage. 
        - Advanced OCR engines struggle with handwritten text, poor scans, stylized fonts, or more complex layouts such as nested tables, complex multi-column layouts, building sketches, X-rays, noisy handwritten documents. *[Note: Add some report numbers on this.]*
    (Figure 2: Add an image with a building sketche showing how hard this is for classic OCR-systems)

- This might work for extremely specialized applications, but it's obvious that it has tons of problems and it doesn't scale for a world of AI agents that have to flexible and fast.
- Transition: That's why modern AI solutions use multimodal LLMs, such as Gemini, that can directly interpret text, images or even PDFs as native input, completely bypassing the OCR-workflow from Figure 1. Thus, let's understand how multimodal LLMs work.
-  **Section length**: 400 words (don't count the mermaid diagrams or image links)

## Section 3: Foundations of multimodal LLMs

@TODO: Give a double-check on the structure of this section, relation to Sebastian's article: https://magazine.sebastianraschka.com/p/understanding-multimodal-llms

- Before showing you the code on how to use LLMs with images and documents, you have to understand how multimodal LLMs works. We won't cover all the details, as you don't have to understand them as an AI Engineer. That's the job of a AI researcher. But you need an intuition on how they work to know how to use, deploy and monitor them.
- High level overview of the common approaches to building multimodal LLMs using text-image models as an example:
    1. Unified Embedding Decoder Architecture approach;
    2. Cross-modality Attention Architecture approach.
    (Figure 3: Image from Sebastian's Raschka magazine showing the two approaches)
- Dig deeper into the `Unified Embedding Decoder Architecture approach` approach. Explain how the image information is passed to the text-LLM through the image encoder as input tokens along the text tokens.
(Figure 4: Image from Sebastian's Raschka magazine showing the method)
- Dig deeper into the `Cross-modality Attention Architecture approach` approach. Explain how the image information is passed to the text-LLM decoder through the attention mechanism
(Figure 5: Image from Sebastian's Raschka magazine showing the method)
- Quick walkthrough over image encoders:
    1. Make parallel between text tokenization (e.g., using Byte-Pair Encoding) and patching images
    (Figure 6: Image from Sebastian's Raschka magazine showing image tokenization and embedding (left) and text tokenization and embedding (right) side by side.)
    2. Explain how creating image embeddings through patching works
    (Figure 7: Image from Sebastian's Raschka magazine showing the ViT setup)
    3. Highlight how the output has the same structure and dimensions, as embeddings, that's why we can input image embeddings along text embeddings with no issues
    4. Even if the image and text embeddings have the same dimensions, in the vector space, they have to be aligned. Thus, explain how we do this throug the linear projection module
    5. Examples of image encoder models: CLIP or OpenCLIP. Explain that most image encoders that have the embeddings in the same vector space as the text embeddings are leveraging the core CLIP architecture.
    6. Explain that these are also used as embedding models for multimodal RAG to find semantic similarities between images and text data points. In other words you can run similarity metrics between text/image/document/audio vectors 
    (Figure 8: Image showing text/image embeddings within the same vector space)
- Trade-offs between the two methods:
    1. `Unified Embedding Decoder Architecture approach`: higher accuracy in OCR-related tasks (what we talked about in section 2)
    2. `Cross-modality Attention Architecture approach`: superior computational efficiency for high-resolution images as we don't have to pass all the tokens as input
    3. `Hybrid Approaches`: best of both worlds
- In 2025, most LLMs are actually multimodal. For example:
    - in the open-source world we have Llama 4, Gemma 2, Qwen3 and DeepSeek R1/V3
    - in the closed-source world we have GPT-5, Gemini 2.5 and Claude
    (most probably their version will increase constantly, but these are the most popular family of models)
- A paragraph on how it can be expanded to other modalities, such as PDFs, audio or video, on hooking different encoders for each modality
- Include a paragraph on multimodal LLMs vs. diffusion generation models, such as Midjourney or Stable Diffusion:
    - Comparison between diffusion image generation models and multimodal LLMs that support generating images (e.g., GPT-4o)
    - Explain that diffusion models are a different family of models than LLMs, which we will not cover in this course, as they are used only to generate images or videos, not to build AI agents
    - Still, in the context of LLM workflows and agents, these models can easily be integrated as tools.
- Conclude with the idea that innovations in multimodal LLM architectures are happening often. This section scope was not to be exhaustive, but to give you an intuition on how multimodal LLMs work and why they are superior to older multi-step OCR approaches.
- Now that we understand how LLMs can directly input images or documents, let's see how this works in pratice.
-  **Section length**: 800 words (don't count the images or mermaid diagrams)

## Section 4: Applying multimodal LLMs to images and PDFs

- To better understand how multimodal LLMs work, let's write a few examples in Gemini to show you some best practices when working with images and PDFs.
- First, let's quickly look at the three core ways to process images with LLMs: as raw bytes, Base64, and URLs:
    1. **Raw bytes:** The easiest way to work with LLMs. Work well for one-off API calls. However, the biggest con of this method is that when storing the item in a database, it can easily get corrupted. Explain why it can get corrupted.
    2. **Base64:** As a way to encode raw bytes as strings. This method is often used to embed images directly into a website, but in our use case the biggest advance is that it allows us to store images in a database (e.g., PostgreSQL, MongoDB) without getting corrupted. Therefore, we often use this format when storing images directly in a database and want to avoid data lakes such as AWS S3. It's biggest downside is that because we store it as strings, it's size is usually 33% bigger.
    3. **URLS:** Useful in two core scenarios: public images from the internet or images stored in a company's data lake, such as AWS S3 or GCP GCS. In most enterprise scenarios, which require scale, the data will be stored in some sort of data lake. Using this method, the LLM can directly download the media from the bucket instead of passing it around the network, making this the most efficient option since I/O is usually of the most common bottleneck of AI apps
    (Figure 9: Mermaid diagram comparing method 2 based on Base64 + databases and method based on URLs + data lakes)
- Conclude, theoretical section by highlighting each methods advantages and when to use them when building AI apps:
    1. **Raw bytes:** one-off LLM calls without storage
    2. **Base64:** storing data directly in the database avoiding data corruption
    3. **URLS:** storing data in data lakes avoiding data corruption and easily distributing the images or documents across the organization

- Now, let's dig into the code. Using the code examples from the provided Notebook within the <research> tag, use all the code from the <notebook_section_title>`2. Applying multimodal LLMs to images, PDFs, and text`</notebook_section_title> section to explain how to 
<what_we_are_implementing>work with LLMs with images and PDFs in multiple formats such as bytes, base64 and URLs</what_we_are_implementing>
- We will show case these scenarios by extracting image captions and PDFs descriptions using Gemini
- Here is how you should use and format the code from the <notebook_section_title>`2. Applying multimodal LLMs to images, PDFs, and text`</notebook_section_title> section of the provided Notebook along with other notes:
    <define_how_the_code_should_be_explained_step_by_step>
    1. Display sample image
    2. Process image as raw bytes:
        - Define `load_image_as_bytes` function
        - Load sample image as raw bytes. Explain that we load it as `WEBP` because it's the most efficient format.
        - Show the image looks like as bytes and it's size
        - Call the LLM
        - Show the output image caption
        - Scale the method by calling the LLM with multiple images asking for the difference between the two
        - Show the LLM response printing the differences between the images
    3. Process the image as base64 encoded strings:
        - Define `load_image_as_base64` function
        - Load the image as base64
        - Show how the base64 image looks like
        - Show concrete example on how base64 images are 33% larger than bytes ones
        - Call the LLM
        - Show the output image caption
    4. Process the image as URLs:
        - Explain that at the time of writing this lesson, Gemini works well only with GCS images, not public URLs. Thus, for simplicity, we will provide only pseudocode.
        - Show mocked code as an example
    5. Show a more complex use case of working with multimodal LLMs and images, which is object detection with LLMs:
        - Define the output Pydantic models 
        - Define the prompt and input image as bytes
        - Call the LLM
        - Show the bounding boxes LLM response as text
        - Visualize the bounding boxes LLM response on the rendered image
    6. Process PDFs as raw bytes:
        - Begin by explaining that because we use exactly the Gemini model and interface, the process is almost identical with what we did for the images
        - load the `decoding_ml_article.pdf` as bytes
        - Call the LLM 
        - Show the LLM response explaining the content of the document
    7.  Process PDFs as base64 encoded strings:
        - Define `load_pdf_as_base64` function
        - Load the PDF as base64
        - Show how the base64 image looks like
        - Call the LLM
        - Show the LLM response explaining the content of the document
    </define_how_the_code_should_be_explained_step_by_step>

-  **Section length**: 600 words (Don't count the code, images or mermaid diagrams)


## Section 5: Foundations of multimodal RAG (ColPali architecture)

@TODO: Start with a generic paragraphs, then move to ColPali
- Explanation of how this relates to RAG:
    - How it can be used to query information: text query → return images/text, or image query → return images/text.
    - *[Generate a mermaid diagram showing how this relates to RAG]*

- Brief introduction to ColPali, explaining that this is the modern architecture for multimodal RAG when working with PDF documents
- ColPali architecture and innovations:
    - The problem it solves
    - The innovation lies in bypassing the entire OCR pipeline that typically involves text extraction, layout detection, chunking, and embedding. Instead, ColPali processes document images directly using vision-language models to understand both textual and visual content simultaneously.
    - Why layout matters for document comprehension. ColPali works great for documents with tables, figures, and other complex visual layouts.
    - Architecture: Used models, offline indexing and online query logic
    - Chunking text vs. Patching images
    - Outputting "bag-of-embeddings"
    - Using ColPali as a reranking system
- Use an image from the research showing the architecture of ColPali
- Paradigm shift comparison:
    - Standard retrieval: OCR, layout detection, chunking, indexing using a text embedding model
    - ColPali: patching and indexing documents as images using a multimodal multi-vector embedding model, where each image outputs a "bag-of-embedding" representation
    - Performance advantages over traditional methods
    - Scalability of ColPali as a reranker
- Real-world example scenarios, mostly related to RAG, where we have to interpret and retrieve complex PDF documents:
    - Financial document analysis with charts, tables, and spatial relationships
    - Technical documentation with diagrams, flowcharts, and complex visuals
    - Research files with images, videos, and diagrams
-  **Section length**: 500 words (don't count the images or mermaid diagrams)

## Section 6: Implementing multimodal RAG for images and text

@TODO: Add PDFs as images in the dataset as well to align better with ColPali

- Connect all the dots with a more complex coding example where we combine what we have learned in this lesson and Lesson 10 on RAG into a multimodal RAG exercise.
- Explain mini-project: A simple multimodal RAG example where we populate an in-memory vector database with multiple images from the `images` folder and further query it with text questions. 
- Figure 10: Generate a mermaid diagram of our multimodal RAG example

- Now, let's dig into the code. Using the code examples from the provided Notebook within the <research> tag, use all the code from the <notebook_section_title>`3. Implementing multimodal RAG for images and text`</notebook_section_title> section to explain how to 
<what_we_are_implementing>build a multimodal RAG system</what_we_are_implementing>.
- Here is how you should use and format the code from the <notebook_section_title>`3. Implementing multimodal RAG for images and text`</notebook_section_title> section of the provided Notebook along with other notes:
    <define_how_the_code_should_be_explained_step_by_step>
    1. Display the images that we will embed and load into our mocked vector index
    2. Define and explain the `create_multimodal_embeddings` function. 
        - As we have only a few images, we will mock the vector index as a simple list. Explain that in the real-world you use a vector database that has dedicated vector indexes that scale using algorithms such as HNSW.
        - As we preached that doing image -> text translations is a bad idea explain in more depth why we did this here through the `generate_image_description` function:
            - The Gemini Dev API doesn't support image embeddings. To keep it simple and avoid integrating another API or running open-source models on a GPU, we will create a description of each image using Gemini and embed that using the text embedding model. As we kept highlighting throughout the lesson, this is usually not recommend. But the good news is that one you have a multimodal embedding model avaiable, you can just skip creating the image description and embed the image directly. Everything else from the RAG system, conceptually remains the same as the image and text embeddings are within the same vector space, which means you can run similarity metrics between the two.
            - Here is a list of popular multimodal embedding models that you can easily integrate in this example: Voyage, Cohere, Google Embeddings on Vertex AI (not Gemini Dev), OpenAI CLIP (available on Hugging Face).
            - Mocked Python code that explains how this would look like:
            ```python
            image_bytes = ...
            # SKIPPED !
            # image_description = generate_image_description(image_bytes)
            image_embeddings = embed_with_multimodal(image_bytes)
            ```
    3. Define and explain the `generate_image_description` function
    4. Define and explain the `embed_text_with_gemini` function
    5. Define the `search_multimodal` function. Explain that it's used to find top `k` images based on a text query
    6. Call the `search_multimodal` function using the `"two robots fighting"` query
    7. Show the results
    8. Another example with the `query = "a kitten with a robot"` and show the results.
    </define_how_the_code_should_be_explained_step_by_step>

- @TODO: ColPali ...: - Also highlight that this is not a complete ColPali implementation, as we do not patch the image before embedding or use the ColBERT reranker. Since running `colpali` requires a GPU, we wanted to keep the example lightweight by leveraging Gemini and focusing on how multimodal works in general.
- Specify that the official `colpali` implementation can be found on GitHub at `illuin-tech/colpali` (we can load the model from Hugging Face).

-  **Section length**: 400 words (don't count the code, images or mermaid diagrams)

## Section 7: Building multimodal AI agents

- Now take this example even further and integrate the `search_multimodal` RAG functionality into a ReAct agent as a tool consolidating most of the skills learnt in part 1.
- First, shortly explain how multimodal techniques can be added to AI Agents by:
    1. Adding multimodal inputs or outputs to the reasoning LLM behind the agent.
    2. Leveraging multimodal retrieval tools, such as in the RAG example, which can be adapted to other modalities.
    3. Leveraging other multimodal tools such as deep research or MCP servers that return or act on external resources: company PDF files, screenshots from your computer, audio files from Spotify, or videos from Zoom.
- Quick walkthough over the exercise: In this example we will show case how to implement techniques 1 and 2, while 3 will be touched in part 2 and 3, when building the larger project. In this example, we will create a ReAct Agent leveraging LangGraph's `create_react_agent()` and connect the RAG retrieval function `search_multimodal` from the previous section as a tool for the agent, which returns the top-k images based on semantic similarity between the images and a text query generated by the agent. As an example, we will ask the agent about the color of our kitten. 
- Figure 11: Generate a mermaid diagram of our multimodal ReAct + RAG example

- Now, let's dig into the code. Using the code examples from the provided Notebook within the <research> tag, use all the code from the <notebook_section_title>`4. Building multimodal AI agents`</notebook_section_title> section to explain how to 
<what_we_are_implementing>implement multimodal AI agents, more exactly multimodal RAG AI agents that can query images from a vector database and process them</what_we_are_implementing>.
- Here is how you should use and format the code from the <notebook_section_title>`4. Building multimodal AI agents`</notebook_section_title> section of the provided Notebook along with other notes:
    <define_how_the_code_should_be_explained_step_by_step>
    1. Define the `multimodal_search_tool` multimodal RAG tool
    2. Define the `build_react_agent` function that creates ReAct agents using LangGraph. Emphasize the `system_prompt`.
    3. Built the `react_agent`
    4. Call the ReAct agent using the `"what color is my kitten?"` `test_question`
    5. Show all the intermediate steps of the ReAct agent
    6. Show the final answer of the ReAct agent along with the kitten image from the Notebook
    </define_how_the_code_should_be_explained_step_by_step>
-  **Section length**: 350 words (don't count the code, images or mermaid diagrams)

## Section 8: Conclusion
(Connect our solution to the bigger field of AI Engineering. Add course next steps.)

- Wrap-up the lesson by explaining that we will use multimodal techniques in our capstone project to pass images and PDFs from our research agent to the writer agent, avoiding any text translation issues and benefit of the complete visual information from them research
- To transition from this lesson to the next, specify that this was the last lesson from part 1, on the fundamentals of AI Engeering. 
- Next specify what we will learn in future lessons. Mention what we will learn in the next part of the course, which is Part 2. Leverage the concepts listed in subsection `Concepts That Will Be Introduced in Future Lessons` to provide a short summary of what we will do in Part 2.
-  **Section length**: 100 words

## Article Code

Links to code that will be used to support the article. Always prioritize this code over any other code found in the sources: 

1. [Notebook 1](https://github.com/towardsai/course-ai-agents/blob/main/lessons/11_multimodal/notebook.ipynb)

## Golden Sources

1. [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)
2. [Vision Language Models](https://www.nvidia.com/en-us/glossary/vision-language-models/)
3. [Multimodal Embeddings: An Introduction](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/)
3. [Multimodal Embeddings: An Introduction](https://www.youtube.com/watch?v=YOvxh_ma5qE)
4. [Multi-modal ML with OpenAI's CLIP](https://www.pinecone.io/learn/series/image-search/clip/)
5. [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/pdf/2407.01449v6)

## Other Sources

1. [Image understanding with Gemini](https://ai.google.dev/gemini-api/docs/image-understanding)
2. [Multimodal RAG with Colpali, Milvus and VLMs](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag)
3. [Google Generative AI Embeddings (AI Studio & Gemini API)](https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/)
4. [LangGraph quickstart](https://langchain-ai.github.io/langgraph/agents/agents/)
5. [Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it)
6. [What are some real-world applications of multimodal AI?](https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai)
7. [What Is Optical Character Recognition (OCR)?](https://blog.roboflow.com/what-is-optical-character-recognition-ocr/)
8. [The 8 best AI image generators in 2025](https://zapier.com/blog/best-ai-image-generator/)