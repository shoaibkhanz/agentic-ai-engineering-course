# Research

## Research Results

<details>
<summary>What are the performance benchmarks and error analysis of traditional OCR on complex documents like financial reports and technical manuals?</summary>

### Source [1]: https://www.octaria.com/blog/what-are-advancements-in-ocr-technologies-in-q1-2025-using-llms

Query: What are the performance benchmarks and error analysis of traditional OCR on complex documents like financial reports and technical manuals?

Answer: **Traditional OCR** systems typically offer more than 95% accuracy for printed text and are known for their fast processing speeds, handling a page in 3–4 seconds. For handwritten text, accuracy rates drop into the 60–90% range, depending heavily on the clarity of the writing. Cost efficiency is a hallmark of traditional OCR, particularly with open-source solutions, and these systems preserve the original document layout well. However, challenges remain, especially with complex or degraded documents. Traditional OCR can struggle with poor-quality images, heavily formatted layouts, and non-standard text arrangements, which are common in financial reports and technical manuals. In such scenarios, error rates increase, and the extracted text may lose structural fidelity, affecting downstream usability. As of Q1 2025, newer LLM-augmented OCR systems are surpassing traditional OCR in accuracy for challenging documents, but traditional OCR still dominates where cost and speed are priorities.

-----

-----

-----

### Source [2]: https://www.dataunboxed.io/blog/ocr-vs-vlm-ocr-naive-benchmarking-accuracy-for-scanned-documents

Query: What are the performance benchmarks and error analysis of traditional OCR on complex documents like financial reports and technical manuals?

Answer: A benchmark comparing traditional OCR with Vision Language Models (VLMs) on the FUNSD dataset (comprised of noisy, scanned forms with complex layouts) found that **traditional OCR methods are significantly outperformed by VLMs** for accuracy, especially on documents with complex formatting and poor scan quality. The evaluation used metrics such as text similarity, word error rate, and character error rate. Traditional OCR exhibited higher error rates in scenarios where document structure was not straightforward or when image quality degraded. Processing time for traditional OCR was faster, but it came at the cost of accuracy in these challenging contexts. The study highlighted that while traditional OCR can be serviceable for simple documents, its error rates and loss of layout context limit its effectiveness on complex documents like financial reports and technical manuals.

-----

-----

-----

### Source [3]: https://www.mixedbread.com/blog/the-hidden-ceiling

Query: What are the performance benchmarks and error analysis of traditional OCR on complex documents like financial reports and technical manuals?

Answer: Testing with the **OHR (OCR hinders RAG) Benchmark v2**—which includes over 8,500 PDF pages from diverse domains (including finance and technical manuals) with complex layouts, tables, formulas, charts, diagrams, and non-standard reading orders—demonstrated that **all traditional OCR solutions underperformed compared to a ground truth benchmark using perfect text**. This "OCR ceiling" limits downstream tasks such as retrieval and question answering. Common errors include:
- Failure to capture non-standard reading orders.
- Inaccurate extraction of tables, formulas, and diagrams.
- Loss of semantic relationships in multi-column or highly formatted documents.

These systematic errors impact the reliability of information retrieval from OCR-extracted content in financial and technical settings. Even state-of-the-art OCR libraries and commercial solutions were unable to match human-verified, perfect extraction, highlighting persistent limitations in handling document complexity.

-----

-----

-----

### Source [4]: https://www.3rdaiautomation.com/blog/benchmarking-QA-on-complex-industrial-PDFs

Query: What are the performance benchmarks and error analysis of traditional OCR on complex documents like financial reports and technical manuals?

Answer: Traditional OCR benchmarking typically relies on **word and character accuracy metrics**, which do not reflect the true impact of OCR errors in real-world applications. For complex industrial and technical PDFs, a single OCR error (e.g., a misrecognized value in a spec sheet or a misplaced decimal in a financial statement) can have outsized negative effects. The limitations of traditional benchmarks become evident when evaluating downstream tasks such as question answering or data extraction. Traditional OCR often struggles with:
- Noisy backgrounds.
- Variable formatting.
- Embedded tables and figures.
- Multi-language or domain-specific terminology.

The article argues that end-to-end benchmarks that include downstream use cases provide a more realistic measure of OCR performance. In practice, traditional OCR’s word/character-level errors compound and can make accurate automated understanding of complex documents unreliable.

-----

-----

</details>

<details>
<summary>How do multimodal LLMs like LLaVA and Gemini process and integrate different data modalities like images and text at an architectural level?</summary>

### Source [6]: https://galileo.ai/blog/multimodal-llm-guide-evaluation

Query: How do multimodal LLMs like LLaVA and Gemini process and integrate different data modalities like images and text at an architectural level?

Answer: Multimodal LLMs like LLaVA and Gemini are constructed around several core architectural components:

- **Visual Encoders:** These are typically vision transformers (ViT) or models like CLIP, responsible for extracting features from images.
- **Language Model Backbone:** Based on transformer architectures (e.g., LLaMA or GPT), these models process textual information.
- **Alignment Modules:** Components such as Q-Former or linear projection layers bridge the gap between the visual and textual modalities by mapping visual features into a representation compatible with the language model.

Three key architectural patterns are commonly used:

- **Unified Embedding Decoder:** Visual and textual inputs are projected into a shared embedding space, allowing a single decoder to process them jointly.
- **Cross-Modality Attention:** Attention mechanisms directly connect visual and textual embeddings, allowing the model to attend to both simultaneously within the transformer layers.
- **Hybrid Approaches:** Modern multimodal LLMs like LLaVA use a hybrid approach, where a vision encoder is connected to a language model via adapter layers that project visual features into the language model's embedding space.

These designs enable the seamless integration and joint reasoning over multimodal inputs.

-----

-----

-----

### Source [7]: https://arxiv.org/html/2409.02889v1

Query: How do multimodal LLMs like LLaVA and Gemini process and integrate different data modalities like images and text at an architectural level?

Answer: A LLaVA-inspired multimodal architecture, as described in the LongLLaVA paper, comprises three main components: the **Vision Encoder**, the **Projector**, and the **LLM** (Large Language Model).

- **Vision Information Processing:** The model uses a vision encoder (such as CLIP-ViT) to extract high-level visual features from images. These features are then passed through a two-layer MLP projector, which maps them into the LLM's text embedding space. Before projection, bilinear pooling reduces the image token representation, which helps preserve essential spatial information while improving computational efficiency.
- **Hybrid LLM Architecture:** The architecture integrates transformer and Mamba layers in a 7:1 ratio and uses a Mixture of Experts (MoE) approach, where multiple expert layers are available, and the best are dynamically selected for each token. Additional design elements include grouped query attention, advanced normalization (RMSNorm), and activation functions such as SwiGLU. Notably, positional embeddings are omitted in this design.

This architecture allows the model to process visual information, align it with text representations, and jointly reason across both modalities using the LLM.

-----

-----

-----

### Source [8]: https://arxiv.org/html/2503.15621v1

Query: How do multimodal LLMs like LLaVA and Gemini process and integrate different data modalities like images and text at an architectural level?

Answer: According to the LLaVA-MORE study, the standard LLaVA multimodal architecture consists of three core components:

- **Large Language Model Backbone**: Handles user interaction and text generation.
- **Visual Encoder(s)**: Extract features from visual input, typically using pre-trained models like CLIP-based architectures. The visual encoder is usually kept frozen (i.e., not updated during multimodal training).
- **Vision-to-Language Adapter**: Bridges the visual and textual modalities by projecting visual features into the language model's embedding space.

The processing pipeline involves the visual encoder extracting image features, which are then passed through the vision-to-language adapter to align them with the language model's input tokens. The language model then receives both the encoded visual information and text tokens, allowing it to generate responses that integrate both types of data.

Recent extensions combine various LLMs with different visual backbones, but the core mechanism—feature extraction, modality alignment, and unified processing in the language model—remains consistent across LLaVA and similar multimodal LLMs.

-----

-----

</details>

<details>
<summary>What are the best practices for handling different image data formats (raw bytes, Base64, cloud storage URLs) when making API calls to multimodal models like Gemini?</summary>

### Source [9]: https://ai.google.dev/gemini-api/docs/image-understanding

Query: What are the best practices for handling different image data formats (raw bytes, Base64, cloud storage URLs) when making API calls to multimodal models like Gemini?

Answer: **Gemini models support several image data formats and have specific best practices and limitations for input handling:**

- **Supported formats:** Gemini accepts the following image MIME types: PNG (`image/png`), JPEG (`image/jpeg`), WEBP (`image/webp`), HEIC (`image/heic`), and HEIF (`image/heif`).
- **File limits:** For Gemini 2.5 Pro/Flash, 2.0 Flash, 1.5 Pro, and 1.5 Flash, a maximum of 3,600 image files can be sent per request.
- **Token calculation:** For Gemini 1.5 Flash and Pro, images with both dimensions ≤ 384 pixels count as 258 tokens; larger images are tiled and resized (min tile 256px, max 768px, resized to 768x768) with each tile costing 258 tokens. For Gemini 2.0 Flash and 2.5 Flash/Pro, larger images are tiled into 768x768 pixel tiles, each costing 258 tokens.
- **Capabilities:** All Gemini versions support multimodal tasks such as image captioning, visual question answering, image classification, object detection, and segmentation. Later versions provide enhanced accuracy for object detection and segmentation.
- **Best practice:** Ensure images are in a supported format and within size limits to avoid request errors or excessive token costs. For large images, be aware of tiling and its impact on token usage.

-----

-----

-----

### Source [10]: https://ai.google.dev/gemini-api/docs/image-generation

Query: What are the best practices for handling different image data formats (raw bytes, Base64, cloud storage URLs) when making API calls to multimodal models like Gemini?

Answer: **When sending image data to the Gemini API (and related models), the best practices for handling image formats are:**

- **Base64 encoding:** Images should be Base64 encoded when sending them inline with your API request. For example, when using cURL, convert your image file to Base64 and include it in the JSON payload under the `inline_data` field with the appropriate `mime_type` (e.g., `"image/jpeg"`).
- **Supported MIME types:** Use only the officially supported image MIME types (PNG, JPEG, WEBP, HEIC, HEIF).
- **Request structure:** The API expects the image data to be presented in a specific JSON structure, with `inline_data` containing both the Base64-encoded data and the MIME type.
- **Example:** 
    ```
    "inline_data": {
      "mime_type": "image/jpeg",
      "data": "<your_base64_encoded_data>"
    }
    ```
- **Watermarking:** All images generated by Gemini include a SynthID watermark.

**Best practice:** Encode your image to Base64, specify the correct MIME type, and closely follow the API's JSON schema to ensure compatibility and successful processing.

-----

-----

-----

### Source [11]: https://firebase.google.com/docs/ai-logic/analyze-images

Query: What are the best practices for handling different image data formats (raw bytes, Base64, cloud storage URLs) when making API calls to multimodal models like Gemini?

Answer: **Firebase AI Logic (using Gemini models) supports two main methods for image input:**

- **Inline (Base64-encoded):** You can provide images directly as Base64-encoded data in your API call. Each input must include the correct `mimeType` and the encoded file data.
- **Via URL:** Images can also be referenced by URL if supported by your API provider and project configuration.
- **Code example (Swift):** The `generateContent()` method can be used to pass both a text prompt and an image (e.g., a `UIImage` in Swift), allowing multimodal input for analysis.
- **Best practice:** Always provide the correct file format (as supported by Gemini) and the associated MIME type. When using Base64, ensure the encoding is correct and matches the declared MIME type.

**Recommendations:** 
- Use Base64 encoding for direct, inline image data.
- Use URLs for images stored in cloud storage, provided your API/project supports it and access permissions are correctly set.

-----

-----

-----

### Source [12]: https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/vision.ipynb

Query: What are the best practices for handling different image data formats (raw bytes, Base64, cloud storage URLs) when making API calls to multimodal models like Gemini?

Answer: **Gemini API's vision capabilities documentation reiterates key technical constraints:**

- **Supported MIME types:** Only PNG, JPEG, WEBP, HEIC, and HEIF formats are accepted.
- **Batch limits:** Up to 3,600 image files can be included in a single request.
- **Best practice:** Ensure all images comply with supported formats and quantity limits to avoid API errors.

-----

-----

-----

### Source [13]: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference

Query: What are the best practices for handling different image data formats (raw bytes, Base64, cloud storage URLs) when making API calls to multimodal models like Gemini?

Answer: **Vertex AI (using Gemini) recommends:**

- **Image input:** Images can be sent as part of the API request, typically inline as Base64-encoded data.
- **Request structure:** The API expects the image data in a field designated for image content, along with the correct MIME type.
- **Integration:** Example code demonstrates generating content using both text and image inputs, with images provided as raw bytes or Base64-encoded data.

**Best practice:** Always encode image data as Base64 when sending inline, specify the MIME type, and follow the API's expected request structure for multimodal input.

-----

-----

</details>

<details>
<summary>How does the ColPali architecture's "bag-of-embeddings" from image patches improve retrieval performance compared to single-vector embeddings from text chunks in RAG systems?</summary>

### Source [14]: https://learnopencv.com/multimodal-rag-with-colpali/

Query: How does the ColPali architecture's "bag-of-embeddings" from image patches improve retrieval performance compared to single-vector embeddings from text chunks in RAG systems?

Answer: ColPali redefines retrieval in RAG systems by treating each document page as an image and generating a **bag-of-embeddings**—one embedding per image patch—rather than a single vector per text chunk. This approach is inspired by ColBERT, which creates lightweight, multi-vector (bag-of-embeddings) representations. During querying, a "late interaction" mechanism computes the maximum similarity between each query embedding and the pre-indexed patch embeddings, enabling fine-grained matching. This is in contrast to traditional RAG systems, which typically generate a single embedding for each text chunk, potentially missing nuanced or localized information, especially from non-textual elements like tables or figures. ColPali’s method thus allows for more precise retrieval of relevant information from complex, visually rich documents and supports efficient, scalable indexing and querying by leveraging vector databases that natively support multi-vector embeddings.

-----

-----

-----

### Source [15]: https://arxiv.org/html/2407.01449v5

Query: How does the ColPali architecture's "bag-of-embeddings" from image patches improve retrieval performance compared to single-vector embeddings from text chunks in RAG systems?

Answer: ColPali’s **bag-of-embeddings** architecture requires storing a vector per image patch, resulting in a larger but more detailed representation compared to single-vector embeddings from text. This enables the model to capture localized visual information from each part of a document, which is especially beneficial for retrieving elements embedded in complex layouts. To manage memory and computational efficiency, ColPali applies token pooling, merging similar or redundant patch embeddings (like those from white backgrounds), thereby reducing storage with minimal performance loss. For example, pooling can reduce the number of vectors by two-thirds while retaining nearly 98% of the original retrieval performance. In contrast, single-vector text chunk embeddings lack this granularity and may overlook visual or spatial relationships crucial for accurate retrieval in visually dense documents.

-----

-----

-----

### Source [16]: https://arxiv.org/html/2407.01449v2

Query: How does the ColPali architecture's "bag-of-embeddings" from image patches improve retrieval performance compared to single-vector embeddings from text chunks in RAG systems?

Answer: Experimental results on the ViDoRe benchmark show that ColPali’s **multi-vector (patch-level) embeddings** outperform modern single-vector retrieval methods, both in accuracy and indexing speed, for visually rich documents. By creating one embedding per image patch, ColPali enables detailed, fine-grained retrieval, making it possible to match queries to very specific visual or textual content within a page. This is not feasible with single-vector text chunk approaches, which aggregate information and may miss localized or non-textual cues. The architecture also supports end-to-end training and fast corpus indexing, further enhancing retrieval performance and scalability for industrial applications.

-----

-----

-----

### Source [17]: https://blog.vespa.ai/scaling-colpali-to-billions/

Query: How does the ColPali architecture's "bag-of-embeddings" from image patches improve retrieval performance compared to single-vector embeddings from text chunks in RAG systems?

Answer: ColPali leverages **approximate nearest neighbor search** across multiple patch embeddings per page, rather than a single embedding per document or chunk. For a query, each token (or query vector) is matched against all image patch vectors, and the best matches are ranked using the MaxSim operation. This allows retrieval to be fine-tuned at the patch level, so queries can target specific regions or elements within a page. Such granularity is not possible with single-vector text chunk embeddings, which only enable document- or chunk-level retrieval and may overlook relevant subregions.

-----

-----

-----

### Source [18]: https://huggingface.co/blog/manu/colpali

Query: How does the ColPali architecture's "bag-of-embeddings" from image patches improve retrieval performance compared to single-vector embeddings from text chunks in RAG systems?

Answer: Traditional RAG pipelines use OCR, layout detection, and text chunking to generate a single embedding per text chunk, which can be slow, error-prone, and poor at capturing visual elements (like tables, figures, or fonts). ColPali’s approach skips these steps by embedding the whole page as an image and then generating a **bag-of-embeddings** from image patches. This method directly encodes both visual and textual information, enabling the retrieval pipeline to account for layout, structure, and non-textual features. The result is a retrieval system that is faster, more robust to errors in text extraction, and much better at handling documents where important content is visual rather than textual.
-----

-----

</details>

<details>
<summary>How can LangGraph be used to build a ReAct agent that utilizes a custom multimodal retrieval tool for a RAG task?</summary>

### Source [19]: https://langchain-ai.github.io/langgraph/how-tos/react-agent-from-scratch/

Query: How can LangGraph be used to build a ReAct agent that utilizes a custom multimodal retrieval tool for a RAG task?

Answer: LangGraph can be used to build a **ReAct agent** by defining a custom agent state, integrating tools (including multimodal retrieval tools), and orchestrating the interaction between the LLM and tool calls within a composable graph structure.

- **State Definition:** Begin by defining the agent's state as a Python TypedDict, typically including a sequence of messages. You can extend this to include any other state relevant for your RAG or multimodal task.
  
- **Tool Integration:** Tools are simply Python functions decorated with `@tool`. To utilize a custom multimodal retrieval tool, define it as a function (e.g., for image, video, or document retrieval) and decorate it appropriately. Add it to the tools list.
  
- **Model Binding:** Use a chat model (e.g., OpenAI's GPT-4o). The model is bound to the tools, so it can invoke them as needed. For example:
  ```python
  model = ChatOpenAI(model="gpt-4o-mini")
  model = model.bind_tools([your_custom_multimodal_tool])
  ```
  
- **Graph Composition:** Use LangGraph's graph primitives to control the ReAct reasoning flow, which typically alternates between LLM reasoning steps and tool invocations. The agent's state and outputs from each node (LLM or tool) are passed through the graph.
  
This modularity allows easy addition of any custom tool, including a multimodal retrieval component, within the ReAct agent's reasoning loop for RAG tasks. Each invocation step and message is tracked in the agent's state, supporting iterative reasoning and retrieval[1].

-----

-----

-----

### Source [20]: https://ai.google.dev/gemini-api/docs/langgraph-example

Query: How can LangGraph be used to build a ReAct agent that utilizes a custom multimodal retrieval tool for a RAG task?

Answer: To implement a **ReAct agent with LangGraph**, follow these steps:

- **StateGraph Setup:** Create a graph with your defined agent state (e.g., containing messages and any multimodal context).
  
- **Nodes:** Add nodes for each major function:
  - `"llm"`: Handles LLM reasoning steps (e.g., generating the next action or response).
  - `"tools"`: Handles tool calls, including your custom multimodal retrieval tool.
  
- **Workflow Logic:**
  - Set the entry point to the LLM node.
  - After each LLM step, use a conditional edge to determine whether to call a tool or end the process (using a function like `should_continue`).
  - After a tool is called, return to the LLM node, allowing for iterative reasoning and retrieval.
  
- **Graph Compilation:** Compile the workflow into a runnable LangGraph graph.
  ```python
  workflow = StateGraph(AgentState)
  workflow.add_node("llm", call_model)
  workflow.add_node("tools", call_tool)
  workflow.set_entry_point("llm")
  workflow.add_conditional_edges("llm", should_continue, {"continue": "tools", "end": END})
  workflow.add_edge("tools", "llm")
  graph = workflow.compile()
  ```
  
This design allows for *plug-and-play* tool integration, so a custom multimodal retrieval tool can be added to the `"tools"` node. The agent alternates between LLM reasoning and tool usage, ideal for RAG scenarios requiring complex retrieval[2].

-----

-----

-----

### Source [21]: https://github.com/langchain-ai/react-agent

Query: How can LangGraph be used to build a ReAct agent that utilizes a custom multimodal retrieval tool for a RAG task?

Answer: The official LangGraph ReAct agent template provides a structure that is easily customizable for integration with custom tools, including multimodal retrieval for RAG tasks.

- **Tool Customization:** You can add new tools by defining Python functions (in `tools.py`) that perform the desired retrieval or processing. For multimodal retrieval, implement a function that interfaces with your retrieval system and returns results to the agent.
  
- **Model Configuration:** The agent supports various chat models; you can select the most suitable one for your multimodal context (e.g., models supporting vision or document understanding).
  
- **Prompt and Reasoning Customization:** Adjust the system prompt or modify the agent's reasoning steps in `graph.py` to better suit your multimodal RAG scenario.
  
- **ReAct Loop:** The agent's decision-making process (when to reason, when to retrieve) can be customized by editing the ReAct loop, allowing sophisticated control over how and when the multimodal retrieval tool is invoked.
  
- **Development Workflow:** Hot reloading and state editing make it easy to iterate on your agent's logic and debug the integration of multimodal retrieval tools.
  
- **Studio and Tracing:** LangGraph Studio and LangSmith integration enable in-depth tracing and collaborative development, which is useful for complex, multimodal RAG workflows[3].

-----

-----

</details>

<details>
<summary>What are the architectural differences and use cases for image generation models like Stable Diffusion versus multimodal LLMs with image generation capabilities like GPT-4o?</summary>

### Source [23]: https://learnopencv.com/stable-diffusion-3/

Query: What are the architectural differences and use cases for image generation models like Stable Diffusion versus multimodal LLMs with image generation capabilities like GPT-4o?

Answer: **Stable Diffusion 3.5** is built on the **Diffusion Transformers** model, featuring an Encoder (VAE) that generates latent noise variables and a Decoder (VAE) for upscaling outputs. The architecture leverages the **MMDiT** structure, which employs three textual encoders: CLIP-G/14, CLIP-L/14, and T5 XXL (approx. 5 billion parameters). The use of multiple encoders enhances performance and allows flexibility during inference by enabling or removing the T5 XXL encoder to balance memory use and accuracy.

The text prompts are embedded using these encoders, and their outputs are concatenated with image patch encodings (created by flattening 2×2 image patches and adding positional encodings). This ensures alignment of text and image information in the same embedding space. The model operates by manipulating these embeddings and latent variables, making it efficient for high-quality image generation from text prompts.

This architecture is fundamentally different from large language models (LLMs) with image generation capabilities, which typically use a unified transformer-based model to jointly process and generate both text and images, rather than relying on specialized modules for encoding and decoding image and text information.

**Use cases for Stable Diffusion** include:
- High-quality, customizable text-to-image generation
- Scenarios where fine control over output style and resolution is needed
- Applications benefiting from modularity and inference-time resource management

-----

-----

-----

### Source [24]: https://jalammar.github.io/illustrated-stable-diffusion/

Query: What are the architectural differences and use cases for image generation models like Stable Diffusion versus multimodal LLMs with image generation capabilities like GPT-4o?

Answer: **Stable Diffusion** is not a monolithic model but a system of multiple components. The architecture includes a **text encoder** (typically from CLIP), which translates input text into embeddings, and an **image generator**, comprised of:

1. **Image information creator**: This is a UNet neural network operating in a compressed, latent space rather than pixel space, which contributes to both speed and efficiency. The image is iteratively refined in this latent space through multiple steps, with a scheduler determining the progression.
2. **Decoder**: After refinement in the latent space, a decoder reconstructs the final image in pixel space.

The use of a separate text encoder and image generator distinguishes Stable Diffusion from multimodal LLMs like GPT-4o. Multimodal LLMs generally use a single transformer backbone for both text and image processing, often interleaving modalities within the same sequence and generating outputs in either domain.

**Key architectural differences**:
- Stable Diffusion separates text and image processing modules.
- Multimodal LLMs unify these modalities within a single transformer architecture.

**Use cases**:
- Stable Diffusion: Focused text-to-image generation, efficient batch processing, artistic and creative content creation.
- Multimodal LLMs: General-purpose tasks involving both text and images, such as image captioning, visual question answering, and dialogue with visual context.

-----

-----

-----

### Source [25]: https://viso.ai/deep-learning/stable-diffusion/

Query: What are the architectural differences and use cases for image generation models like Stable Diffusion versus multimodal LLMs with image generation capabilities like GPT-4o?

Answer: **Stable Diffusion** utilizes a **latent diffusion architecture**, which significantly reduces memory and compute requirements by performing the diffusion process in a lower-dimensional latent space, rather than in high-resolution pixel space. The key architectural components are:

- **U-Net Backbone**: Handles the denoising process, enhanced with cross-attention layers for conditioning on inputs like text.
- **VAE (Variational Autoencoder)**: Encodes input images to latent representations for the U-Net and decodes the output back to the image.
- **Conditioning Mechanism**: Allows the model to be conditioned by different modalities, primarily text via a CLIP-ViT text encoder.

During inference, the model starts with a latent noise seed and a conditioning input (e.g., text embedding), and then iteratively denoises the latent representation to generate an image. This workflow emphasizes modularity, with clear separation of roles for encoding, denoising, and decoding.

**Differences from multimodal LLMs**:
- Stable Diffusion: Modular, with specialized networks for each function.
- Multimodal LLMs: Typically a single, large model trained to handle all modalities together, often at the cost of some specialization and efficiency.

**Use cases**:
- Stable Diffusion: Efficient, scalable text-to-image generation, especially suited for high-resolution creative outputs.
- Multimodal LLMs: Tasks requiring tight integration of text and vision, such as document understanding or multimodal dialogue.

-----

-----

-----

### Source [26]: https://stable-diffusion-art.com/how-stable-diffusion-work/

Query: What are the architectural differences and use cases for image generation models like Stable Diffusion versus multimodal LLMs with image generation capabilities like GPT-4o?

Answer: Stable Diffusion operates as a **latent diffusion model** for text-to-image generation. The process begins by generating a random latent tensor (controlled by a seed), which is initially all noise. The U-Net noise predictor, conditioned on a text prompt, predicts the noise component in the latent space. This predicted noise is subtracted from the latent image, and the process is repeated for a set number of steps, progressively denoising the image representation in the latent space.

The use of a **latent space** (as opposed to pixel space) is a defining architectural feature, making the model more efficient for high-resolution image synthesis. The architecture is modular, with dedicated components for text encoding, noise prediction, and decoding.

By contrast, **multimodal LLMs** integrate text and image processing within a unified model, allowing for joint reasoning and generation across modalities. These models are optimized for tasks involving both text and images, rather than focused, high-fidelity image synthesis.

**Use cases**:
- Stable Diffusion: High-quality image generation from text, with efficient resource usage and reproducible outputs via seeding.
- Multimodal LLMs: Cross-modal reasoning (e.g., describing images, answering questions about images, generating images in a conversational context).

-----

</details>

<details>
<summary>What are the performance and efficiency trade-offs of using cloud storage URLs versus Base64 encoding for image inputs in enterprise-level multimodal LLM applications?</summary>

### Source [27]: https://community.openai.com/t/why-docs-say-to-use-url-instead-of-base64/780453

Query: What are the performance and efficiency trade-offs of using cloud storage URLs versus Base64 encoding for image inputs in enterprise-level multimodal LLM applications?

Answer: The discussion emphasizes that **Base64 encoding should be avoided whenever possible** in favor of using **URLs for image inputs**. The main arguments are:
- **Base64 encoding increases payload size** by approximately 40% compared to the original image, leading to greater network usage and inefficiency.
- Using URLs is more network-efficient because only the reference to the image is transmitted, not the image data itself.
- Base64 has some situational uses (such as localhost or statically hosted web apps), but for most networked or scalable enterprise scenarios, URLs are preferable.
- The performance impact of Base64 is well-understood: the increased data size can become significant at scale, though for small applications the impact may be less pronounced.
- The only caveat is if introducing URLs requires significant architectural changes (like adding a server for hosting images), but purely in terms of network and encoding/decoding efficiency, **URLs outperform Base64**.

-----

-----

-----

### Source [28]: https://csswizardry.com/2017/02/base64-encoding-and-performance/

Query: What are the performance and efficiency trade-offs of using cloud storage URLs versus Base64 encoding for image inputs in enterprise-level multimodal LLM applications?

Answer: This source highlights that **Base64 encoding complicates caching strategies** in web applications:
- When images are embedded as Base64 within other assets (e.g., CSS or HTML), they are tightly coupled to those assets. Any change to the parent asset forces the browser or client to re-download all bundled resources, not just the modified part.
- **Independent caching is lost**: with URLs, images can be cached separately and updated independently, improving efficiency. With Base64, small changes in code can invalidate large amounts of cached data.
- The resource separation principle is violated with Base64; ideally, images, styles, and fonts should be cached and updated on their own schedules.
- The conclusion is clear: **avoid Base64 for performance and efficiency**, especially at scale.

-----

-----

-----

### Source [29]: https://langfuse.com/docs/tracing-features/multi-modality

Query: What are the performance and efficiency trade-offs of using cloud storage URLs versus Base64 encoding for image inputs in enterprise-level multimodal LLM applications?

Answer: Langfuse's documentation shows that both **Base64-encoded images and URLs are supported** for multimodal LLM applications, but with notable differences:
- **Base64**: When images are provided as Base64 data URIs, Langfuse SDKs automatically extract them, upload them as separate media objects, and reference them in traces. This extra processing step is needed because Base64 data is embedded in payloads, increasing payload size and complicating direct access.
- **URLs**: When images are supplied via external URLs, Langfuse renders them directly without handling or storing the content. This is more streamlined for display and tracing, and it avoids unnecessary data transfer and duplication.
- For enterprise applications, using URLs means **less payload overhead and more efficient trace management**, while Base64 requires additional extraction and storage steps.

-----

-----

-----

### Source [30]: https://cloud.google.com/vertex-ai/generative-ai/docs/image/base64-encode

Query: What are the performance and efficiency trade-offs of using cloud storage URLs versus Base64 encoding for image inputs in enterprise-level multimodal LLM applications?

Answer: This Google Cloud documentation provides practical guidance for **Base64 encoding and decoding images** for API calls:
- **Base64 is often used when embedding binary data directly into request payloads**, particularly in programmatic (API) environments where direct file transfer is not feasible.
- All major programming languages support Base64 encoding, and it is straightforward to implement.
- The documentation acknowledges that embedding binary data in text editors (e.g., for manual API requests) is impractical; Base64 is more suited to automated, client-driven use cases.
- There is **no mention of performance or payload efficiency**, but the implication is that Base64 is a standard workaround for including binary data in APIs that require text-based inputs.

-----

-----

-----

### Source [31]: https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding

Query: What are the performance and efficiency trade-offs of using cloud storage URLs versus Base64 encoding for image inputs in enterprise-level multimodal LLM applications?

Answer: This page describes how to **add images to Gemini multimodal LLM requests on Vertex AI**:
- The documentation provides examples for both uploading images (which could be via URLs or Base64) and using them as inputs for image understanding.
- There is **no explicit discussion of performance or efficiency trade-offs** between URLs and Base64.
- The focus is on usability and API compatibility, rather than network or computational efficiency.
-----

-----

</details>

<details>
<summary>What are the leading multimodal embedding models for video and audio retrieval, and how do their architectures extend beyond the text-image paradigm of CLIP?</summary>

### Source [32]: https://milvus.io/ai-quick-reference/how-are-audio-embeddings-integrated-into-multimodal-search-systems

Query: What are the leading multimodal embedding models for video and audio retrieval, and how do their architectures extend beyond the text-image paradigm of CLIP?

Answer: **Audio embeddings** are integrated into multimodal retrieval systems by **mapping raw audio into numerical vectors** that capture semantic and acoustic features. These embeddings are produced using neural networks such as CNNs or transformers—examples include models like **Wav2Vec**. The embeddings are then aligned with those from other modalities (e.g., text, images) by either:
- Training a **joint model** that ensures semantically similar content across modalities is close in the embedding space (e.g., the phrase “jazz piano” and an audio clip of jazz piano yield similar vectors).
- Using **late fusion**, where embeddings from different modalities are searched independently and then combined at ranking.

A key example is **CLAP (Contrastive Language-Audio Pretraining)**, which uses contrastive learning to align audio and text embeddings, enabling cross-modal retrieval tasks such as matching a user’s humming to relevant music tracks. These approaches extend CLIP’s text-image paradigm by:
- Incorporating **audio-specific encoders** and aligning their outputs with text/image embeddings.
- Supporting queries in one modality (e.g., audio) and retrieval in another (e.g., text or music).

This architecture enables flexible, multimodal search well beyond the original text-image pairing in CLIP.

-----

-----

-----

### Source [33]: https://arxiv.org/html/2504.04572v1

Query: What are the leading multimodal embedding models for video and audio retrieval, and how do their architectures extend beyond the text-image paradigm of CLIP?

Answer: A leading approach for **multimodal video retrieval** described here involves a **framework combining visual, aural (audio), and subtitle (text) information**. The architecture includes:
- **Visual matching stream**: Processes video frames using vision models.
- **Aural matching stream**: Processes the audio track independently, using specialized audio models.
- **Subtitles-based segmentation**: Uses subtitles to segment videos into semantically meaningful units for more precise retrieval.
- **Two-stage audio retrieval mechanism**: Enhances performance for long-duration videos by filtering and refining results using audio features.

This framework is tailored for **long-form, complex videos** and supports retrieval using correlations between all three modalities, extending beyond CLIP by:
- Integrating **audio processing pipelines** alongside vision and text.
- Applying **temporal localization** and **audio filtering** to address lengthy and noisy video content.
- Adapting retrieval evaluation to the challenges of multimodal, long-video search.

-----

-----

-----

### Source [34]: https://vcg.ece.ucr.edu/sites/default/files/2019-03/IJMIR_Camera_Ready.pdf

Query: What are the leading multimodal embedding models for video and audio retrieval, and how do their architectures extend beyond the text-image paradigm of CLIP?

Answer: This paper proposes a **joint embedding framework for video-text retrieval** using a **mixture of experts** approach:
- The model uses **multiple modalities from video**, such as visual features (from frames), audio cues, and possibly motion information.
- Each modality is encoded using dedicated neural networks, then combined via a mixture-of-experts mechanism to form a unified embedding.
- The embedding is trained with a **modified pairwise ranking loss** to improve cross-modal retrieval.

Compared to text-image models like CLIP, this architecture:
- Explicitly incorporates **audio and motion features** in addition to visual and textual inputs.
- Enables retrieval using richer, **multimodal video cues**, which are particularly important given the diversity and complexity of real-world video content.

Experiments on video-text retrieval show that integrating these multimodal cues yields **significant performance gains** over single-modality or naive fusion models.

-----

-----

-----

### Source [35]: https://www.twelvelabs.io/blog/multimodal-embeddings

Query: What are the leading multimodal embedding models for video and audio retrieval, and how do their architectures extend beyond the text-image paradigm of CLIP?

Answer: Video embedding models have evolved to use **multiple strategies**, including:
- **Image-based embeddings**: Extract visual features from frames using pre-trained image models (e.g., Inception-V3, ResNet).
- **Audio-based embeddings**: Convert audio signals from video into embeddings using spectrogram analysis or audio encoders.
- **Joint audio-visual embeddings**: Fuse visual and audio features within the model architecture to capture cross-modal correlations.
- **Temporal embeddings**: Encode motion and sequence information across video frames (e.g., using optical flow or motion vectors).
- **Spatial embeddings**: Capture the spatial relationships within video frames.

For **multimodal video retrieval**, these models extend beyond the text-image design of CLIP by:
- **Explicitly fusing audio and visual features** at various stages of the architecture.
- Incorporating **temporal and spatial context** to capture the dynamics and structure unique to video.
- Allowing retrieval or search based on **audio, visual, or combined cues**, rather than just text and image.

Such architectures are essential for tasks like **video captioning, video retrieval, and audio-visual synchronization**, highlighting the broader scope and technical complexity of modern multimodal embedding models.

-----

</details>

<details>
<summary>What are the most common challenges and error modes when implementing multimodal RAG systems in production environments?</summary>

### Source [36]: https://arxiv.org/html/2504.08748v1

Query: What are the most common challenges and error modes when implementing multimodal RAG systems in production environments?

Answer: The survey outlines several significant challenges and error modes encountered when implementing multimodal retrieval-augmented generation (MRAG) systems in production:
- **Cumbersome Document Parsing**: Converting multimodal data (e.g., images, audio) into textual representations (such as captions) adds considerable complexity, requiring separate models for each modality. This process often leads to **information loss**, as textual descriptions tend to capture only coarse-grained details, omitting fine-grained information essential for accurate retrieval and generation.
- **Retrieval Bottlenecks**: While text retrieval is mature, multimodal systems face challenges with **high recall accuracy**. Text chunking can fragment key concepts, making some content irretrievable. Transforming non-text modalities into text introduces additional information loss, collectively creating a bottleneck that limits the system’s ability to retrieve comprehensive and relevant information.
- **Challenges in Generation**: MRAG systems must organize and synthesize diverse data types (text, captions, etc.) into coherent prompts. This complexity increases the risk of **redundancy and irrelevant information** in outputs. The "Garbage In, Garbage Out" problem is exacerbated: information loss during parsing and retrieval raises the likelihood of incorporating irrelevant or misleading data, undermining the reliability and robustness of generated responses.
- **Performance Ceiling**: The reliance on text-based representations for multimodal data introduces a performance ceiling, as critical gaps remain in multimodal understanding, retrieval efficiency, and generation robustness. Addressing these limitations requires enhanced models, improved information retention, and better integration strategies for diverse data types.

-----

-----

-----

### Source [37]: https://denemlabs.blog/2025/04/16/multimodal-retrieval-augmented-generation-advances-and-remaining-challenges/

Query: What are the most common challenges and error modes when implementing multimodal RAG systems in production environments?

Answer: The blog identifies several core scientific and technological bottlenecks for multimodal RAG systems:
- **Fine-Grained Semantic Alignment**: Achieving precise alignment between visual and textual modalities remains challenging. For example, in healthcare, a retrieved decision tree may represent correct thresholds, but the model can struggle to accurately link each node to the appropriate clinical context or cues. In education, models often fail to connect graphical representations with their corresponding explanatory text, limiting the system’s utility for complex reasoning tasks.
- **Fragmented Retrieval Pipelines**: Many architectures use **separate retrievers** for each modality, resulting in **inconsistent downstream synthesis**. If the retrieval or ranking of images and text is not based on a shared semantic space, outputs can be incomplete or incoherent (e.g., missing crucial visual context in a clinical recommendation, or pedagogical gaps in educational applications).
- **Hallucination and Lack of Verification**: Multimodal hallucination—where the model fabricates or misinterprets details not present in the source material—is a major risk. This is especially problematic in sensitive contexts such as clinical advice, where incorrect interpretation of a chart or image can have significant consequences. Research into cross-modal verification is ongoing, but robust and scalable solutions to ensure factual consistency across modalities are not yet fully developed.

-----

-----

-----

### Source [38]: https://www.edge-ai-vision.com/2024/12/an-easy-introduction-to-multimodal-retrieval-augmented-generation/

Query: What are the most common challenges and error modes when implementing multimodal RAG systems in production environments?

Answer: This article highlights practical challenges when building and operating multimodal RAG pipelines:
- **Modality-Specific Challenges**: Each data modality (e.g., images, text, tables, charts) presents unique obstacles. For images, crucial challenges include ensuring that models capture both **general context and fine-grained details** (such as specific elements in a diagram or chart) rather than just broad features. Information-dense images require pipelines capable of extracting multiple relevant points, not just a single caption.
- **Cross-Modal Representation Alignment**: Effectively managing and integrating information across modalities is critical. For instance, a system must ensure that the **semantic embedding of a chart** aligns with the text that describes it, so that retrieval and generation steps produce coherent and unified responses. Failure to align representations can result in **disjointed or incomplete outputs**.
- **Handling Unstructured Enterprise Data**: In production, multimodal RAG systems often face unstructured and heterogeneous data (such as folders of images or mixed-content PDFs). Building robust pipelines that can parse, represent, and relate these diverse data types is a nontrivial engineering challenge.

-----

-----

</details>

<details>
<summary>What are some real-world examples of multimodal AI agents that use tools for tasks beyond simple retrieval, such as interacting with UIs or external APIs based on visual input?</summary>

### Source [40]: https://www.ema.co/additional-blogs/addition-blogs/understanding-multimodal-ai-agents

Query: What are some real-world examples of multimodal AI agents that use tools for tasks beyond simple retrieval, such as interacting with UIs or external APIs based on visual input?

Answer: Multimodal AI agents are deployed in various real-world scenarios requiring complex, context-rich decision-making by integrating text, vision, and speech. In **customer service and support**, these agents can simultaneously analyze spoken queries, interpret emotional tone, and reference past support history, enabling real-time escalation, smarter routing, and context-aware, personalized responses. For example, Walmart employs AI chatbots to autonomously process around 80% of customer inquiries, streamlining operations beyond simple retrieval.

In **healthcare and diagnostics**, multimodal AI can process visual scans, doctors’ notes, and sensor data from medical devices together, empowering faster and more accurate diagnoses and supporting early detection of health risks. A notable example includes a study by Google DeepMind and Moorfields Eye Hospital, where AI analyzed 3D eye scans to detect over 50 eye diseases with 94% accuracy. Google has advanced this further with **Multimodal AMIE**, a conversational diagnostic AI agent integrating voice, text, and visual understanding to provide real-time clinical decision support—acting as an interactive tool for clinicians rather than just a retrieval system.

These examples demonstrate how multimodal agents go beyond basic information retrieval to directly interact with digital environments and external systems, offering decision support, automation, and enhanced user experiences[1].

-----

-----

-----

### Source [41]: https://www.tekrevol.com/blogs/multimodal-ai-how-it-works-use-cases-examples/

Query: What are some real-world examples of multimodal AI agents that use tools for tasks beyond simple retrieval, such as interacting with UIs or external APIs based on visual input?

Answer: Multimodal AI is used across diverse real-world applications that require integrating visual, textual, and sensor data for complex tasks. In **healthcare diagnostics and imaging**, multimodal agents combine MRI and X-ray images, patient history, and live vitals. The AI models process these inputs simultaneously, matching patterns in imaging data with electronic health records (EHRs) for highly accurate diagnoses. These agents can also analyze doctor notes and scan results together, providing actionable insights for oncologists and radiologists.

In **financial fraud detection and risk management**, multimodal AI agents analyze transaction data, customer interactions, and behavioral patterns. They use real-time transaction logs and customer communications, including sentiment analysis, to identify suspicious or fraudulent activity, going beyond passive detection to support active investigation.

In the domain of **autonomous driving**, multimodal AI agents integrate camera feeds, LiDAR, radar, and GPS data. These real-time inputs are processed to control vehicle movement, recognize objects, and predict the actions of pedestrians and other vehicles. The agent’s capacity for integrating multiple sensory modalities enables advanced route planning and real-time decision-making, directly interacting with control systems for navigation and safety.

These applications illustrate multimodal AI agents performing complex, tool-using tasks such as interacting with UI elements (e.g., diagnostic workstations) or external APIs (e.g., financial systems, vehicle controllers) based on integrated visual and other sensory data[2].

-----

-----

-----

### Source [42]: https://www.xenonstack.com/blog/multimodal-ai-agents

Query: What are some real-world examples of multimodal AI agents that use tools for tasks beyond simple retrieval, such as interacting with UIs or external APIs based on visual input?

Answer: Existing virtual assistants like Siri and Alexa are primarily unimodal, but multimodal AI agents enhance these systems by adding visual processing capabilities. This enables the agents to handle queries involving images, face recognition, or gestures, leading to a more realistic and operational user interface.

For example, a multimodal AI application could respond to a voice command such as “What is it like outside?” and also identify objects in a picture sent by the user, producing visually integrated search results. This demonstrates the agent’s ability to interact with user-provided visual input and external data sources.

In **healthcare diagnostics**, multimodal AI agents can utilize medical images, patient records, and doctors’ notes to provide diagnostic support. An agent that examines X-ray films and reviews clinical text documents can assist medical personnel with diagnosis and treatment planning, effectively interacting with external medical systems and electronic health records based on both visual and textual data.

These capabilities show that multimodal agents can perform tasks that require tool use and UI interaction based on visual and multimodal inputs, moving well beyond simple information retrieval[3].

-----

-----

-----

### Source [43]: https://www.sparkouttech.com/multi-model-ai-agent/

Query: What are some real-world examples of multimodal AI agents that use tools for tasks beyond simple retrieval, such as interacting with UIs or external APIs based on visual input?

Answer: The future of multimodal AI agents involves increasingly sophisticated **autonomous agentic ecosystems**. These agents are evolving to interact not just with users but also with digital and physical environments, other agents, and external APIs. For example, robots and devices powered by multimodal agents will soon understand their surroundings through vision, sound, and physical movement, enabling complex navigation and real-time decision-making.

Multimodal AI integration with AR/VR platforms is also highlighted, where agents use multiple sensory cues to create smart, responsive virtual experiences. The rise of **Emotional AI** is enabling systems to detect emotions from facial expressions, language, and voice, further enhancing their ability to interact with humans and digital interfaces in nuanced ways.

With **unified foundation models** like GPT-4o, multimodal agents can reason across any input type and act accordingly—such as using visual input to interact with UI elements programmatically or making API calls based on combined sensory data. This allows agents to perform general-purpose tool use in real-world environments, such as navigating digital dashboards, triggering alerts, or executing workflows based on what they “see” and “hear.”

These trends underscore the real-world shift from passive multimodal processing to **active tool use and environment interaction**, driving the next generation of AI-powered automation and decision-making[4].

-----

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>AI has advanced significantly and **multimodal AI** is driving its evolution. Multimodal AI processes multiple data types simultaneously — such as text, images, video, and audio — making decision-making more accurate. This accuracy results in human-like interactions and improves systems’ context-aware performance.</summary>

AI has advanced significantly and **multimodal AI** is driving its evolution. Multimodal AI processes multiple data types simultaneously — such as text, images, video, and audio — making decision-making more accurate. This accuracy results in human-like interactions and improves systems’ context-aware performance.

It’s becoming a prominent tool in healthcare, finance, manufacturing, automotive, and many other sectors that use advanced data analysis and precise, actionable insights.

Multimodal AI’s impact on industries can be reflected in its growing market value. According to [Grand View Research](https://www.grandviewresearch.com/press-release/global-multimodal-artificial-intelligence-ai-market), the global multimodal AI market is expected to reach $10.89 billion by 2030. With exponential integration across diverse fields that demand AI models capable of interpreting and acting on multiple data types concurrently, multimodal AI is becoming integral.

## **What is Multimodal AI?**

Multimodal AI is a class of artificial intelligence systems designed to process and analyze multiple data types simultaneously.

Rather than relying on a single data source, such as text or images, multimodal AI integrates inputs like **natural language**, **visual content**, **audio signals**, and **sensor data** to produce precise and context-aware insights.

This capability allows AI systems to address complex scenarios by synthesizing data from different sources to provide actionable outcomes.

### **Technical Architecture**

Multimodal AI uses advanced deep learning frameworks such as **convolutional neural networks (CNNs)** for image recognition, **recurrent neural networks (RNNs)** for sequential data processing, and **transformer models** to handle complex text analysis.

These models use techniques like **attention mechanisms** to focus on key data points across modalities, and **tensor fusion** to align and process different types of data inputs in parallel. This alignment across modalities enables multimodal AI to process data cohesively for accurate, real-time predictions and decisions.

### **Functional Execution**

Multimodal AI boosts operational capabilities through integrated, context-driven responses.

For instance, in an **autonomous driving system**, multimodal AI processes input from **LIDAR sensors**, **radar**, **visual cameras**, and **audio signals** to assess traffic conditions, detect obstacles, and adjust driving actions instantly.

The system can interpret each modality in real-time and synchronize responses for safe navigation. The ability to simultaneously process this diverse range of inputs gives multimodal AI systems an edge in industries that rely on real-time, complex data streams.

### **Application in Real-World Use**

Multimodal AI applies in several industries with diverse data streams and a need for rapid response systems.

In **healthcare**, it integrates medical imaging, patient history, and biometric data for enhanced diagnostic capabilities. In **manufacturing**, it improves **predictive maintenance** by merging sensor readings, visual inspections, and historical machine performance data to detect and prevent equipment failure.

## **How Multimodal AI Works? – A Technical Overview**

Multimodal AI merges data from different modalities to provide a holistic view and make decisions based on a unified interpretation of that data. The technology’s core lies in its ability to process and synchronize different data types in real-time.

Here’s a step-by-step breakdown of how multimodal AI works:

- ### **Data Collection & Structuring**
Multimodal AI begins with collecting data from various sources: natural language input (text), image/video feeds, and audio signals. Each modality undergoes a preprocessing phase, where structured formats are applied to ensure data compatibility. For text, tokenization and embedding techniques such as **BERT** or **Word2Vec** are used, while images and videos undergo feature extraction using **CNNs** (Convolutional Neural Networks).

- ### **Data Alignment & Synchronization**
Aligning diverse data sources is essential for cohesive AI models. The system synchronizes inputs across modalities. For example, video frames and their accompanying audio are aligned with relevant text transcripts or metadata. **Tensor fusion** or **bilinear pooling** techniques align these different data points within a common semantic space.

- ### **Feature Extraction & Dimensionality Reduction**
Once synchronized, the AI extracts key features from each modality. For text data, **NLP** models extract semantic meaning, while images undergo object detection via CNNs. Audio signals are analyzed using **spectrograms** for sound pattern recognition. Techniques like **principal component analysis (PCA)** or **t-distributed stochastic neighbor embedding (t-SNE)** are used to reduce data dimensionality, ensuring efficient processing without loss of critical information.

- ### **Cross-Modal Fusion & Integration**
This is where the strength of multimodal AI lies. The system integrates features from various data sources through **deep multimodal fusion**. Fusion can occur at the early stages (combining raw data) or late stages (combining decision outcomes). A hybrid approach often delivers the best results, merging both raw data and model inferences. This enables the system to consider all inputs in a meaningful way to create a unified model output.

- ### **Deep Learning Model Training**
The AI system is then trained using **multimodal transformers**, **recurrent neural networks (RNNs)**, or **temporal convolutional networks (TCNs)**. Each modality contributes to the model’s learning process. Cross-modality attention mechanisms ensure that the model weighs each input appropriately, refining its predictions and enhancing the model’s ability to generalize across diverse scenarios.

- ### **Inference Generation & Decision-Making**
Once trained, multimodal AI models can analyze new data and deliver high-precision insights. This stage involves leveraging learned patterns to make informed decisions, drawing on each input type. For example, in healthcare, the model could analyze patient data, medical imagery, and doctor’s notes to provide diagnostic recommendations or potential treatments.

- ### **Continuous Learning & Adaptation**
Multimodal AI systems are continuously updated with new data to ensure they remain accurate and relevant. Reinforcement learning mechanisms allow the system to adapt, improving performance over time and applying new learning to improve future inferences.

## **12 Industry-Specific Use Cases Of Multimodal AI**

- ### **Healthcare Diagnostics & Imaging**
In healthcare, multimodal AI integrates MRI scan data with X-ray data, patient history, and live vitals. Diagnostic images are fed to AI models and patterns are extracted and matched with EHR to provide almost accurate diagnosis. Patients benefit from the improvement of an AI that incorporates notes and scans to make quick and accurate diagnoses, especially in oncology and radiology.

- ### **Financial Fraud Detection & Risk Management**
Multimodal AI also helps in the detection of fraud by analyzing the data of transactions, interacting with customers, and their behavioral patterns.

Combining real-time transaction logs and customer communication implies that AI systems can identify suspicious activities that may not be detected. Multimodal systems can also incorporate sentiment analysis in the support interactions aimed at identifying stress signals regarding fraudulent issues.

- ### **Autonomous Driving**
Multimodal AI is critically important for self-driving vehicles. These include camera feeds in adding to LiDAR, radar, and GPS data that allows for decisions that are made in real-time.

All of these inputs are fed into the driving models where they are processed at the same time to control movements on roads, object recognition, and future actions by pedestrians and other vehicles on the road. It helps AI systems to further improve route planning, and safety measures to prevent any possible collisions.

- ### **Retail & eCommerce Personalization**
In retail, multimodal AI utilizes the purchase history, images, comments, and live browsing patterns to identify products to offer. Multimodal AI employed by eCommerce platforms such as Amazon helps to capture customers’ preferences across such modalities.

Based on the analysis of the use of images of products and the reviews provided by the users, the AI provides more relevant results, which improves the conversion rates.

- ### **Manufacturing Process Optimization**
In smart factories, multimodal AI integrates data from IoT sensors, camera feeds, and production schedules to optimize workflow. The AI predicts machine failures by analyzing real-time sensor data and historical maintenance logs. Additionally, computer vision systems monitor product quality in real-time, identifying defects and alerting teams before issues escalate, which reduces downtime and operational inefficiencies.

- ### **Agriculture & Crop Management**
In agriculture, multimodal AI processes drone imagery, weather data, and soil conditions to provide actionable insights for farmers. For example, AI systems use satellite data and environmental sensor inputs to monitor crop health, assess irrigation needs, and predict yield outcomes. Precision agriculture is increasingly reliant on multimodal models to optimize resource usage and improve crop yields.

- ### **Energy Sector & Grid Management**
Energy companies employ multimodal AI for grid optimization by analyzing sensor data, environmental conditions, and historical energy consumption patterns.

AI systems predict peak demand times, optimize energy distribution, and detect anomalies that might indicate equipment failures or inefficiencies. AI helps improve operational efficiency and predictively maintain grid infrastructure to minimize outages.

- ### **Consumer Electronics & Virtual Assistants**
Devices like Amazon Alexa and Google Home rely on multimodal AI to process voice commands, detect contextual clues, and interact with users. These virtual assistants process real-time audio, text input, and user preferences to perform tasks such as setting reminders, playing music, or answering queries.

AI models trained on multimodal data help assistants understand nuanced voice commands, improving user interaction.

- ### **Education & Adaptive Learning Platforms**
Educational tools use multimodal AI to create adaptive learning experiences. These systems integrate video lectures, student performance data, and interaction logs to personalize learning paths.

AI can suggest supplementary resources for students struggling with specific topics or accelerate content delivery for advanced learners. These systems continuously refine the student’s learning experience through data from quizzes, essays, and real-time feedback.

- ### **Social Media Content Moderation**
Platforms like Facebook and Instagram use multimodal AI to moderate user-generated content. AI models detect harmful or inappropriate content in real time by analyzing text, images, and videos.

Social media platforms use multimodal systems to enhance user safety and optimize content recommendations by flagging inappropriate behaviors based on user preferences and interactions across multiple content types.

- ### **Supply Chain & Logistics**
Multimodal AI streamlines supply chain operations by processing GPS data, traffic patterns, and inventory levels. AI systems integrate this data to optimize delivery routes, predict supply shortages, and adjust logistics planning.

AI helps warehouse supervisors analyze inventory data, shipment schedules, and customer demand forecasts to optimize stock levels and reduce delivery times.

- ### **Telecommunications Network Optimization**
Multimodal AI helps optimize network performance in the telecom sector. It thoroughly analyzes signal strength data, real-time traffic patterns, and user device information to predict network congestion, optimize bandwidth allocation, and proactively resolve connectivity issues.

Using multimodal AI telecommunications providers can enhance call quality, reduce latency, and ensure consistent service across various geographical locations for better, consistent customer experience and operational efficiency. It also assists with predictive maintenance by identifying potential network failures before they impact users.

## **8 Benefits Of Multimodal AI**

- ### **Enhanced Decision-Making**
Multimodal AI combines two or more modalities such as vision, sound, and textual data, which permits better decision making. For this reason, multilingual AI systems are beneficial as they process various forms of data at once and generate solutions that single-modality models cannot offer. This capability makes it valuable especially for industries in which decisions depend on several forms of data, such as self-driving cars and diagnostics of illnesses.

- ### **Improved User Interaction**
Multimodal AI makes the user’s experience better because it takes into consideration voice, face, and hand gestures. This technology can assist in developing natural and intuitive user interfaces in voice-controlled services such as voice assistants, virtual reality applications, and customer support.

For instance, in smart home applications, it is possible to implement multimodal AI that can comprehend both spoken and gestural control at the same time which will allow it to perform more precise actions and provide better experience and feedback.

- ### **Real-Time Contextual Understanding**
This ultimately allows for a better understanding of the context within the use of sensor data, environmental information, and real-time signals. This benefit is especially important in areas such as self-driving vehicles and robotics.

It is all possible because robots with multimodal AI can not only see but also sense and decide all at once using data from cameras and sensors, as well as the GPS. This real-time processing benefits functions such as manufacturing, logistics, and self-driving cars.

- ### **Cost Efficiency in Operations**
Multimodal AI improves operational efficiency and saves costs across industries through process optimization. It can analyze the visual and sensor data in the manufacturing process to identify faulty instances in real time, thereby minimizing equipment breakdowns.

Likewise, in the healthcare sector, it becomes possible to combine patient documentation, MRI scans, and real-time data to diagnose a disease earlier, excluding the necessity to spend a great deal of money on further treatment. Multimodal systems enhance efficiency thus increasing ROI for businesses that adopt the technology.

- ### **Scalable Data Handling**
Multimodal AI has the advantage of being capable of working with more than one type of data, making it a much better option to deal with big data. Multimodal AI proves useful for companies dealing with vast volumes of various data, like retail analytics, where it is possible to analyze purchasing patterns, sales, and customer opinions concurrently. It also exhibits an impressive ability to scale with data volume, making it a good option for companies that require growth at a fast pace.

- ### **Predictive Accuracy**
The data fusion at the multimodal level enhances the accuracy of prediction. For example, in the process of financial forecasting, AI systems can input market patterns, news articles, and financial data to provide better stock estimates. With the help of this functionality, businesses can better understand the data provided and manage risks and opportunities effectively. This is useful in providing companies with a competitive advantage since it offers more accurate forecasts.

- ### **Automation of Complex Tasks**
Multimodal AI is suitable in cases where there is a need to automate a task involving the comprehension of various data inputs. In particular, AI can help in the diagnostic process by analyzing X-rays, CT scans, and patient information in medical imaging, which are actions that require time and effort from healthcare professionals.

It can be applied for instance in retail where AI enables automation of certain tasks within the business such as using visual and sensor data to check on the inventory and forecast when replenishment will be needed.

- ### **Enhanced Personalization**
Multimodal AI improves the effectiveness of recognizing and interacting with clients as compared to solely using keywords by identifying the voice, facial expressions, and behavior of the client. For instance, in e-commerce, it can correlate a user’s browser history with visual product preferences to offer recommendations. Engaging the client increases their satisfaction thus creating demand for products by recommending customized products based on multiple inputs.

## **9 Multimodal AI Apps & Products Examples**

- ### **Google Lens**
Google Lens is an example of a multimodal AI system that takes inputs in the form of images through the camera of a smartphone and maps the inputs to textual data obtained from the internet. By aiming the camera, users can identify plants, scan QR codes, and even translate text. Google Lens is a real-time computer vision and natural language processing (NLP) tool that can identify objects depending on the context.

- ### **OpenAI DALL·E**
DALL·E is an AI model for image generation created by OpenAI, which converts words into unique artwork. DALL·E achieves an understanding of natural language and generates images corresponding to the given description with a high level of detail. This ability to handle multiple modes of data makes it a useful tool in several fields, especially in arts and graphics where it can create a design, art, or marketing image.

- ### **Microsoft Azure Cognitive Services**
The intent behind Azure’s Cognitive Services is a set of multimodal AI solutions catering to speech, vision, text, and language. These services find applications in various business areas such as healthcare, finance, and customer relations services. Using multiple connected data inputs, Azure’s platform can execute advanced, performable tasks such as language translation and document scanning.

- ### **Amazon Rekognition**
Amazon Rekognition is a software service that uses artificial intelligence technology to recognize images and videos. It takes in video streams and integrates the data with user data to provide outputs like facial recognition, object identification, and activity monitoring. This multimodal system is employed in security, surveillance, and e-commerce to enhance products’ individualization and safety measures. It is also capable of detecting the feelings of users due to its capability to identify emotions displayed on faces in real time.

- ### **IBM Watson Visual Recognition**
IBM Watson offers visual recognition tools that integrate with Watson’s natural language processing engine. This multimodal AI system can process visual content like images and videos and combine them with textual descriptions to extract meaningful insights. In industrial applications, Watson Visual Recognition can identify product defects on assembly lines or track items in warehouses through real-time video feeds.

- ### **SoundHound**
SoundHound is an advanced voice AI platform that combines speech recognition with music identification. Users can speak or hum a song to receive information about it instantly. This system relies on audio processing and natural language understanding to deliver accurate results. It’s used widely in smart assistants, automotive voice systems, and entertainment to enhance user interaction through natural, voice-driven commands.

- ### **Flamingo**
Developed by DeepMind, Flamingo is a state-of-the-art multimodal model designed for image-text understanding. By combining text prompts with images, Flamingo can generate captions, answer questions about images, and interpret visual inputs in context. This technology is beneficial in content moderation, digital marketing, and customer support, where understanding both text and visuals is crucial for accurate content handling.

- ### **MUM (Multitask Unified Model)**
Introduced by Google, MUM can process and integrate multiple types of inputs such as text, images, and video to answer complex search queries. It is designed to understand and generate insights across 75 languages and handle cross-lingual tasks. This product is particularly effective for global e-commerce and international SEO, where understanding user intent across languages and media formats is critical.

- ### **Florence**
Florence is a multimodal AI model developed by Microsoft for advanced computer vision tasks. It is particularly adept at combining image recognition with natural language processing, enabling it to identify objects and describe them in natural language. Florence is highly valuable in fields like surveillance, retail inventory management, and industrial automation, where image understanding in context is required for efficient operation.

## Wrap Up

Multimodal AI is reshaping industries by integrating diverse data types to deliver more precise, efficient, and intelligent solutions. From optimizing decision-making to automating complex workflows, its applications are vast.

As businesses adopt multimodal AI, leveraging benefits like improved accuracy, real-time insights, and operational efficiency will drive growth and innovation.

Now is the time to embrace AI-driven solutions for the future.

## Frequently Asked Questions:

##### What is multimodal AI, and how does it work?

Multimodal AI combines data from multiple sources—such as text, images, audio, and sensor inputs—into a single system. This integration allows AI models to analyze diverse data types simultaneously, improving decision-making and automation accuracy.

##### What are the key use cases of multimodal AI?

Multimodal AI is used in healthcare for diagnostic imaging and patient data analysis, in retail for visual and text-based product recommendations, and autonomous vehicles for real-time sensor and image processing.

##### How does multimodal AI improve the accuracy of AI models?

By integrating diverse data types, multimodal AI models capture more context and complexity, reducing errors and enhancing the precision of outputs compared to single-mode models that rely on one data source.

##### What industries benefit most from multimodal AI applications?

Healthcare, retail, automotive, and customer service industries benefit significantly from multimodal AI, using it for tasks like automated diagnostics, personalized shopping experiences, real-time vehicle navigation, and chatbot interactions

##### What are the challenges in implementing multimodal AI systems?

Challenges include handling large datasets, synchronizing different data types, and ensuring interoperability between AI models. Advanced algorithms and robust data infrastructures are critical to overcoming these obstacles.

</details>

<details>
<summary>Retrieval-Augmented Generation (RAG) has become the default way to connect Large Language Models (LLMs) with enterprise data. However, there's a critical flaw in this approach that's rarely discussed: nearly all production RAG pipelines rely on Optical Character Recognition (OCR) to process PDFs, scans, presentations, and other documents, with the silent assumption that the extracted text is "good enough" for downstream AI tasks.</summary>

Retrieval-Augmented Generation (RAG) has become the default way to connect Large Language Models (LLMs) with enterprise data. However, there's a critical flaw in this approach that's rarely discussed: nearly all production RAG pipelines rely on Optical Character Recognition (OCR) to process PDFs, scans, presentations, and other documents, with the silent assumption that the extracted text is "good enough" for downstream AI tasks.

Our comprehensive analysis shows that this assumption is fundamentally flawed. OCR quality creates an invisible ceiling that limits the performance of even the most advanced RAG systems. The gap between what's possible with perfect text extraction and what's achieved with current OCR technology represents one of the most significant yet overlooked challenges in enterprise AI today.

## Why OCR is still critical for AI systems

Most enterprise knowledge is locked in unstructured formats like PDFs, scanned documents, invoices, presentations, images, and a plethora of other formats. Before a Large Language Model (LLM) can reason over this knowledge, it needs to be converted from its original visual or semi-structured format into plain text.

This text conversion step, typically handled by OCR engines, is crucial because it feeds two core components of a RAG system:

1.  **The Retrieval System:** Most retrieval systems depend on extracted text as their main search input. When OCR quality is poor, it produces inaccurate or "corrupted" text representations of your documents. This results in flawed text representations, making it difficult or impossible for the retrieval system to locate the relevant documents when a user asks a question. If the text doesn't accurately reflect the content, the search fails before it even begins.
2.  **The Generation Model (LLM):** LLMs generate answers based _only_ on the context they are given. If the retrieved document snippets contain OCR errors (missing words, jumbled tables, incorrect numbers), the LLM receives flawed information. This directly leads to incomplete, nonsensical, or factually incorrect answers, even if the retrieval system managed to find the _correct_ document pages.

In short, errors introduced by OCR don't just stay in the text; they cascade through the entire RAG pipeline, impacting both the ability to _find_ information and the ability to _generate accurate answers_ from it.

## Illustrative Examples: Where Standard OCR Falters

To make the impact of OCR limitations more concrete, let's examine a few specific scenarios from our benchmark data. These examples highlight common situations where traditional OCR-based systems can struggle and demonstrate how a multimodal approach to retrieval can lead to more accurate document interpretation.

### Example 1: The Challenge of Handwritten Data in Regulatory Filings

**The Scenario:** Regulatory filings, such as a telecommunications company's PUCO annual report, frequently combine structured typed content with critical handwritten financial figures. This mixture presents a significant **OCR challenge**, as traditional systems often fail to accurately recognize handwritten entries, leading to potential compliance and analysis issues.https://www.mixedbread.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fexample-1.8c2adea3.png&w=3840&q=75&dpl=dpl_CLymEScs1qG3zZWqP9TtAwxbHoFS

**Typical OCR Output & Its Limitations:**
When processed by a standard OCR engine, the crucial handwritten financial data is often missed entirely or garbled:

```
Annual Report of TSC Communications, Inc. Year Ended December 31, 2026

Instructions:
Schedule 2 is used for PUCO annual assessment purposes pursuant to Section 4905.10, RC...

STATEMENT OF INTRASTATE GROSS EARNINGS (REVENUE)
                                                       Amount
Line                                                   Ohio
No.        Item                                         Intrastate
1    Operating and Miscellaneous Revenue - Wholesale    [???????]
     Cellular Communications, Radio Common Carrier...
2    Other Revenue, Dividend and Interest Income...      [???????]
3    SUBTOTAL                  (1) + (2)                [???????]
4    Earnings or receipts from sales to other public    (          )
     utilities for resale
5    TOTAL                     (3) + (4)                [???????]

     [???????]
     [???????]
     [???????]
```

**Impact on RAG Systems:**
Consequently, if a query such as, _"What is the total revenue of TSC Communications?"_ is posed, a RAG system relying on this flawed OCR output would likely respond: _"Unable to determine revenue figures from the available document."_ This necessitates manual data review, delaying important reporting and analytical tasks.

### Example 2: Deciphering Visual Trends in Financial Charts

**The Scenario:** Quarterly investment reports often feature charts, like stacked area charts showing portfolio allocation, to convey critical trends. The **OCR challenge** here is that traditional OCR primarily extracts textual elements (titles, labels) but fails to capture the actual visual data representing the trends themselves.https://www.mixedbread.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fexample-2.14a5258e.png&w=3840&q=75&dpl=dpl_CLymEScs1qG3zZWqP9TtAwxbHoFS

**Typical OCR Output & Its Limitations:**
A standard OCR tool might only extract the labels and title, leaving out the core data:

```
Portfolio Allocation Trends (Q1 2023 - Q4 2024)
Percentage (%)
100
75
50
25
0
Q1 2023, Q2 2023, Q3 2023, Q4 2023, Q1 2024, Q2 2024, Q3 2024, Q4 2024
Cash, Commodities,Real Estate,Fixed Income, Equities
```

**Impact on RAG Systems:**
When a client asks, _"How has my equity exposure changed over the past year?"_, a RAG system using this limited OCR output might provide only generic information about portfolio components. It would completely miss the crucial visual trend, such as a 13 percentage point increase in equity exposure, which is essential for understanding investment risk.

### Example 3: Navigating Complex Financial Tables

**The Scenario:** Financial reports frequently contain multi-column tables detailing revenue breakdowns and operating expenses. The **OCR challenge** with such complex table structures lies in maintaining correct column and row alignment; failures here can lead to financial figures being associated with incorrect business units or categories.https://www.mixedbread.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fexample-3.5f1ccfef.png&w=3840&q=75&dpl=dpl_CLymEScs1qG3zZWqP9TtAwxbHoFS

**Typical OCR Output & Its Limitations:**
Even if text is extracted, subtle misalignments or parsing errors by the OCR can corrupt the table's structure:

```
Operating Expenses
                                          Year Ended
                          Jan 26, 2025     Jan 28, 2024        $           %
                                                              Change       Change
                                           ($ in millions)
Research and development expenses    $        12,914    $         8,675    $    4,239        49 %
% of net revenue                                9.9 %              14.2 %
Sales, general and administrative expenses      3,491              2,654         837         32 %
% of net revenue                                2.7 %               4.4 %
  Total operating expenses           $        16,405    $        11,329    $   5,076         45 %
% of net revenue                               12.6 %              18.6 %
```

**Impact on RAG Systems:**
If a financial analyst asks, _"What percentage of revenue did R&D represent in 2025 compared to 2024?"_, a RAG system relying on poorly structured OCR output might misinterpret the relationships between figures. An erroneous response could be: _"R&D was 49% of revenue in 2025 compared to 8,675% in 2024."_ Such nonsensical answers arise from the system's inability to correctly understand the visual and semantic structure of the table.

</details>

<details>
<summary>The provided markdown content is an article about "Stable Diffusion," an image generation model. The article guidelines, however, describe a lesson focused on using multimodal LLMs for understanding and processing data (like images and PDFs) to build RAG systems and AI agents.</summary>

The provided markdown content is an article about "Stable Diffusion," an image generation model. The article guidelines, however, describe a lesson focused on using multimodal LLMs for understanding and processing data (like images and PDFs) to build RAG systems and AI agents.

The guidelines explicitly state that diffusion models like Stable Diffusion are a different family of models and will *not* be covered in depth. The provided content is a detailed, in-depth explanation of Stable Diffusion. Therefore, the vast majority of the content is not pertinent to the requested article and has been removed.

No content from the provided markdown was relevant to the specific lesson outline.

</details>

<details>
<summary>Implementing deep learning models has become an increasingly important machine learning strategy for companies looking to build data-driven products. In order to build and power deep learning models, companies collect and feed hundreds of millions of terabytes of multimodal data into deep learning models. As a result, **embeddings** — deep learning models’ internal representations of their input data — are quickly becoming a critical component of building machine learning systems.</summary>

Implementing deep learning models has become an increasingly important machine learning strategy for companies looking to build data-driven products. In order to build and power deep learning models, companies collect and feed hundreds of millions of terabytes of multimodal data into deep learning models. As a result, **embeddings** — deep learning models’ internal representations of their input data — are quickly becoming a critical component of building machine learning systems.

For example, they make up a significant part of [Spotify’s item recommender systems](https://research.atspotify.com/2021/04/contextual-and-sequential-user-embeddings-for-music-recommendation/), [YouTube video recommendations of what to watch](https://research.google/pubs/pub45530/), and [Pinterest’s visual search](https://arxiv.org/abs/1505.07647). Even if not explicitly presented to the user through recommendation system UIs, embeddings are used internally at places like Netflix to make content decisions around which shows to develop based on user preference popularity.https://framerusercontent.com/images/HL4kazD6gvna6UIR2RTDNJvv4w.png

The usage of embeddings to generate compressed, context-specific representations of content exploded in popularity after the publication of [Google’s Word2Vec paper](https://arxiv.org/abs/1301.3781). Building and expanding on the concepts in Word2Vec, [the Transformer architecture](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html), with its self-attention mechanism, a much more specialized case of calculating context around a given word, has become the de-facto way to learn representations of growing multimodal vocabularies, and its rise in popularity both in academia and in the industry has caused embeddings to become a staple of deep learning workflows.

However, the concept of embeddings can be elusive because they are neither data flow inputs nor output results - they are intermediate elements that live within machine learning services to refine models. So it is helpful to define them explicitly from the beginning.

#### 1 - What Are Embeddings?

A dense embedding is a vector that distributes information related to a concept with multiple elements, indicating that elements can be tuned separately to allow more concepts to be encoded efficiently in a relatively low-dimensional space. Such representations can be compared to symbolic representations, such as **one-hot encoding**, which uses an element with a value of one to indicate the presence of a concept locally and values of zero for other elements.https://framerusercontent.com/images/7qK6al0BVgITZkCcWz1m119Q8U.png

In deep learning, the term “ **embedding**” often refers to a mapping from a one-hot vector representing a word or image category to a distributed representation of real-valued numbers. More specifically, the process of embedding includes three steps:

1. **Transforms** multimodal input into representations that are easier to perform intensive computation on in the form of **vectors**, tensors, or graphs.

2. **Compress** input information for an ML task, such as summarizing a blog post or performing a **semantic search** on a large video corpus. The process of compression changes variable feature dimensions into fixed inputs, allowing them to be passed efficiently into downstream components of machine learning systems.

3. **Creates an embedding space** that is specific to the data the embeddings were trained on but that, in the case of deep learning representations, can also generalize to other tasks and domains through **transfer learning.**

Creating an embedding for a word, image, or video to represent an artifact in multidimensional space offers us many possibilities. For instance, in tasks that concentrate on **content understanding in a video recommendation system**, we are often interested in comparing two given items to assess their similarity. We can perform this task with mathematical precision by transforming videos into vectors and comparing video frames in a shared embedding space.

#### 2 - Unimodal Embeddings

##### 2.1 - Language Representations

**Text embeddings** are a type of representation for text data that map words or phrases to real-valued vectors in a lower-dimensional space. These vectors capture the meaning and context of the text and enable a variety of natural language processing (NLP) tasks. They have many NLP applications, including search engines, product recommendations, social media content moderation, email spam filtering, and customer support chatbots.https://framerusercontent.com/images/Xx2RdWmMX2uOP65HCNaCZYMzCSM.png

Text embeddings can be generated using a neural network that extracts high-level features from the text and converts them into a fixed-size dimension vector (e.g., 1,500 dimensions). These embeddings can be used to compare and analyze text data, allowing for tasks such as text classification, text retrieval, and text summarization.

In the past, recurrent neural networks like [long short-term memory (LSTM)](https://ieeexplore.ieee.org/abstract/document/6795963/) or [gated recurrent unit (GRU)](https://arxiv.org/abs/1412.3555) language models incorporated information from all past words stored in a fixed-length recurrent vector when predicting a current word. Other commonly used methods for generating word embeddings include [the continuous bag-of-words model](https://arxiv.org/abs/1301.3781), [skip-grams](https://arxiv.org/abs/1310.4546), and [global vectors (GloVe)](https://aclanthology.org/D14-1162/).

**Since 2017, Transformers have been heavily used to learn text embeddings**. The [Vanilla Transformer](https://arxiv.org/abs/1706.03762) is a model originally proposed for NLP and uses a self-attention mechanism to achieve state-of-the-art results on various NLP tasks. Many derivative models have been proposed following the success of the Vanilla Transformer, such as [BERT](https://aclanthology.org/N19-1423.pdf), [BART](https://aclanthology.org/2020.acl-main.703/), [GPT](https://openai.com/research/language-unsupervised), [Longformer](https://github.com/allenai/longformer), [Transformer-XL](https://vimeo.com/384795188), and [XLNet](https://papers.nips.cc/paper_files/paper/2019/hash/dc6a7e655d7e5840e66733e9ee67cc69-Abstract.html). A pre-trained Transformer model can be a powerful text embedding generator.

##### 2.2 - Visual Representations

**Image embeddings** are a way to represent images as real-valued vectors in a lower-dimensional space. These vectors capture the visual content of the image, which can be used for various computer vision tasks, such as image search, object detection, facial recognition, and content-based image retrieval.https://framerusercontent.com/images/iBVhteX1sTnE2wPKFeKMhzljbbg.webp

We can obtain image embeddings using the output values from the final layers in image classification models (such as [AlexNet](https://dl.acm.org/doi/pdf/10.1145/3065386), [VGGNet](https://arxiv.org/abs/1409.1556), [GoogLeNet](https://arxiv.org/abs/1409.4842), and [ResNet](https://arxiv.org/abs/1512.03385)). These models won the [ImageNet Large Scale Visual Recognition Competition for image classification](https://arxiv.org/abs/1409.0575) in 2012, 2014, and 2015. Image embeddings can be used to compare and analyze image data, enabling tasks such as image classification, image retrieval, and image similarity search.

Alternatively, more direct features can be used as visual embeddings, such as convolutional features and associated class labels from selected regions identified by object detection models. Models using this approach include the [region-based CNN (R-CNN)](https://arxiv.org/abs/1311.2524), [Fast R-CNN](https://arxiv.org/abs/1504.08083), and [Faster R-CNN](https://arxiv.org/pdf/1506.01497.pdf).

**Transformers are currently the most popular tool for NLP, and researchers are now exploring how they can be used in other areas, such as visual domains**. One such area is the use of a [Vision Transformer](https://www.youtube.com/watch?v=TrdevFK_am4) (ViT), which applies the encoder of a Transformer to images. ViT and its variations have been successfully used for various computer vision tasks, including [low-level tasks](https://github.com/huawei-noah/Pretrained-IPT), [recognition](https://proceedings.mlr.press/v139/touvron21a.html), [detection](https://arxiv.org/abs/2012.09958), and [segmentation](https://github.com/microsoft/Swin-Transformer). They work well for both supervised and [self-supervised visual learning](https://www.youtube.com/watch?v=LHhu11kOA-Y). Recent studies have also provided further understanding of ViT, such as [its robustness in internal representation](https://github.com/sayakpaul/robustness-vit) and the continuous behavior of its latent representation propagation. A pre-trained ViT model can be a powerful image embedding generator.

##### 2.3 - Audio Representations

**Audio embeddings** are numerical representations of audio signals that capture the acoustic content of the audio in a compact and meaningful way. These vectors aim to capture the semantic and contextual information of audio signals. They have many applications in audio processing, especially for tasks such as audio classification, audio retrieval, speaker recognition, and music recommendation.https://framerusercontent.com/images/pzxcygnWyNHxX39daPs95jXs.png

We can use pre-trained models, such as [VGGish](https://github.com/tensorflow/models/tree/master/research/audioset/vggish) or [SoundNet](http://soundnet.csail.mit.edu/), which have been trained on large-scale audio datasets like [AudioSet](https://research.google.com/audioset/) or [UrbanSound](https://paperswithcode.com/dataset/urbansound8k-1), to generate these audio embeddings. These models can extract high-level features from the audio signals, such as spectrograms or mel-frequency cepstral coefficients (MFCCs), and encode them into embeddings.

**Similar to the language and visual domain, we can also leverage the Transformer architecture to generate these audio embeddings**. Some examples include [PaSST](https://github.com/kkoutini/PaSST), [Audio Transformer](https://arxiv.org/abs/2105.00335), [CTAL](https://github.com/tal-ai/CTAL_EMNLP2021), [SSAST](https://github.com/YuanGongND/ssast), and [Audio Spectrogram Transformer](https://github.com/YuanGongND/ast).

#### 3 - Multimodal Embeddings

Although significant advancements have been made in representing vision, language, or speech, it is theoretically insufficient to model a complete set of human concepts using only one modality. For instance, the idea of a "beautiful picture" is grounded in visual representation, making it hard to describe through natural language or other non-visual ways. That's why it's crucial to **learn joint embeddings that use multiple modalities** to represent such concepts better. Generally speaking, [the field of Multimodal AI](https://app.twelvelabs.io/blog/what-is-multimodal-ai) looks at building AI systems that can extract embeddings from multimodal data.

##### 3.1 - A Quick Note on Multimodal AIhttps://framerusercontent.com/images/toDkPQ5VaZtbVX909UCBveP38Pw.png

Multimodal AI has been a significant research area in recent decades. The world we live in is a multimodal environment, and both our observations and behaviors are multimodal. For example, [an AI navigation robot requires multimodal sensors to perceive the real-world environment](https://boschresearch.github.io/multimodalperception/). These sensors include a camera, LiDAR, radar, ultrasonic, GNSS, HD Map, and odometer. Additionally, **human behaviors, emotions, events, actions, and humor are also multimodal**. As a result, various human-centered Multimodal AI tasks are widely studied, including [multimodal emotion recognition](https://ieeexplore.ieee.org/document/9578811), [multimodal event representation](https://rowanzellers.com/merlot/), [understanding multimodal humor](https://ojs.aaai.org/index.php/AAAI/article/view/17534), [face-body-voice-based video person-clustering](https://www.youtube.com/watch?v=ho58dTFO9kg), and more.

Thanks to the advancements in internet technology and the proliferation of intelligent devices, an ever-growing volume of multimodal data is transmitted over the web. **This has given rise to a plethora of multimodal application scenarios**. In today's world, we can observe a broad range of such applications, including commercial services (like [e-commerce retrieval](https://lichengunc.github.io/images/kdd2022_commercemm_poster.pdf), [vision-language navigation](https://www.youtube.com/watch?v=m9HpHVuSn4A), and [audio-visual navigation](https://vision.cs.utexas.edu/projects/semantic_audio_visual_navigation/)), communication methods (such as [lip-reading](https://openaccess.thecvf.com/content/CVPR2021/html/Ren_Learning_From_the_Master_Distilling_Cross-Modal_Advanced_Knowledge_for_Lip_CVPR_2021_paper.html) and [sign language translation](https://www.robots.ox.ac.uk/~vgg/research/bslattend/)), [human-computer interaction](https://arxiv.org/abs/2001.02600), [healthcare AI](https://www.nature.com/articles/s41598-020-62922-y), and [surveillance AI](https://github.com/PengBoXiangShang/deepchange).

In the era of Deep Learning, Multimodal AI has made significant progress thanks to deep neural networks. Among the most competitive architectures are the [Transformers](https://arxiv.org/abs/1706.03762), which offer new challenges and opportunities to Multimodal AI. Recent successes with large language models and their multimodal derivatives, such as [Frozen](https://fh295.github.io/frozen.html), [VL-Adapter](https://github.com/ylsung/VL_adapter), [Flamingo](https://www.deepmind.com/blog/tackling-multiple-tasks-with-a-single-visual-language-model), [BEiT](https://github.com/microsoft/unilm/tree/master/beit3), and [PaLI](https://ai.googleblog.com/2022/09/pali-scaling-language-image-learning-in.html), show that **Transformers have great potential for creating foundation models for Multimodal AI**.

##### 3.2 - Multimodal Pre-Traininghttps://framerusercontent.com/images/L5mD3f8Kjc4V60RJahxrAX4dWA.png

In 2021, [CLIP](https://github.com/openai/CLIP) was proposed as a new milestone. It uses multimodal pre-training to convert classification into a retrieval task, which enables pre-trained models to tackle zero-shot recognition. Thus, CLIP is a successful practice that fully utilizes large-scale multimodal pre-training to enable zero-shot learning. This has become a main breakthrough for many multimodal tasks. Recently, the idea of CLIP has been further studied in other works, such as [CLIP pre-trained model-based zero-shot semantic segmentation](https://github.com/MendelXu/zsseg.baseline), [ALIGN](https://ai.googleblog.com/2021/05/align-scaling-up-visual-and-vision.html), [MAD](https://arxiv.org/abs/2204.10496), [ALBEF](https://github.com/salesforce/ALBEF), and [CoCa](https://github.com/lucidrains/CoCa-pytorch).

</details>

<details>
<summary>> For long running conversations, we suggest passing images via URL’s instead of base64</summary>

> For long running conversations, we suggest passing images via URL’s instead of base64
at [https://platform.openai.com/docs/guides/vision/managing-images](https://platform.openai.com/docs/guides/vision/managing-images)

Just why?

For long-running conversations, it may be that OpenAI caches the image request data, so a new download from the remote source is not needed when continuing to pass the URL in past chat, whereas if you sent the BASE64 every time (as you must do with chat completions), your re-sending the same data over and over would have more network delay.

I’m surprised they even support base64. That’s the worst way mankind has ever invented to handle images, unless it’s a tiny icon or something. The entire internet uses the URL way to access images, and that’s all that was needed.

EDIT: as mentioned below, despite horrible inefficiency of base64 it might be needed for sending from localhost.

Well, no.

If I have a local image I would prefer to send it over as b64 (as most email providers do) then upload it to a remote source

I should have said “most wasteful way” (of bandwidth), rather than “worst way” which is too vague, but you’re right I wasn’t considering cases when sending from localhost. I’ll edit that post. Thanks for pointing that out.

Fair. Yeah. Not as efficient as directly downloading the file.

Yeah you can take a compressed image, decompress it, then put it in a less efficient format (base64) and then recompress it again, and send that compressed output. I realize that’s sensible for sending data from localhost, but for most networked components it’s the worst way possible, when you can just use a URL. I stand by my original statement, but it needed more context.

Not just sending from localhost, any serverless app that just works classically on a device (or even web apps that are hosted statically) require this feature.

Sounds like we’re all in agreement that base64 should be avoided whenever possible, as it is a far less efficient approach than a URL.

I would say only if using URLs does not require a major change in your architecture (like introducing a server). Anyway, has someone measured the real performance impact?

We don’t need to conduct any experiments, when we know for sure base64 is 40% larger than the image. (on average). Some people will care. Some people will not care.

Only if network transmission or base64 encoding/decoding is the bottleneck. I would not be surprised if that was just a small share in comparison to the processing inside the model.

</details>


## Code Sources

<details>
<summary>Repository analysis for https://github.com/towardsai/course-ai-agents/blob/main/lessons/11_multimodal/notebook.ipynb</summary>

# Repository analysis for https://github.com/towardsai/course-ai-agents/blob/main/lessons/11_multimodal/notebook.ipynb

## Summary
Repository: towardsai/course-ai-agents
File: notebook.ipynb
Lines: 974

Estimated tokens: 7.9k

## File tree
```Directory structure:
└── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/11_multimodal/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 11: Multimodal

This notebook demonstrates how to build multimodal AI systems that can process and understand both text and visual content using Google's Gemini models. You'll learn to work with images and PDFs in various formats, implement multimodal RAG systems for semantic search, and create AI agents capable of visual reasoning.

We will use the `google-genai` library to interact with Google's Gemini models.

**Learning Objectives:**

1. **Process multimodal content**: Learn to handle images and PDFs in different formats (bytes, base64, URLs) with Gemini models
2. **Implement object detection**: Use multimodal LLMs for visual analysis and structured output generation
3. **Build multimodal RAG systems**: Create embeddings for images and text to enable semantic search across visual content
4. **Develop multimodal AI agents**: Construct ReAct agents that can search through and reason about visual information
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

import base64
import io
from pathlib import Path
from typing import Literal

from google import genai
from google.genai import types
from IPython.display import Image as IPythonImage
from PIL import Image as PILImage

from lessons.utils import pretty_print

"""
### Initialize the Gemini Client
"""

client = genai.Client()

"""
### Define Constants

We will use the `gemini-2.5-flash` model, which is fast, cost-effective, and supports advanced features like tool use.
"""

MODEL_ID = "gemini-2.5-flash"

"""
## 2. Applying multimodal LLMs to images, PDFs, and text

There are three core ways we can process images and PDFs with multimodal models:
1. As raw bytes
2. As base64 encoded strings
3. As URLs

First, let's examine a test image:

"""

def display_image(image_path: Path) -> None:
    """
    Display an image from a file path in the notebook.

    Args:
        image_path: Path to the image file to display

    Returns:
        None
    """

    image = IPythonImage(filename=image_path, width=400)
    display(image)


display_image(Path("images") / "image_1.jpeg")
# Output:
#   <IPython.core.display.Image object>

"""
### 2.1 As raw bytes
"""

def load_image_as_bytes(
    image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
) -> bytes | tuple[bytes, tuple[int, int]]:
    """
    Load an image from file path and convert it to bytes with optional resizing.

    Args:
        image_path: Path to the image file to load
        format: Output image format (WEBP, JPEG, or PNG). Defaults to "WEBP"
        max_width: Maximum width for resizing. If image width exceeds this, it will be resized proportionally. Defaults to 600
        return_size: If True, returns both bytes and image size tuple. Defaults to False

    Returns:
        bytes: Image data as bytes, or tuple of (bytes, (width, height)) if return_size is True
    """

    image = PILImage.open(image_path)
    if image.width > max_width:
        ratio = max_width / image.width
        new_size = (max_width, int(image.height * ratio))
        image = image.resize(new_size)

    byte_stream = io.BytesIO()
    image.save(byte_stream, format=format)

    if return_size:
        return byte_stream.getvalue(), image.size

    return byte_stream.getvalue()

image_bytes = load_image_as_bytes(image_path=Path("images") / "image_1.jpeg", format="WEBP")

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/webp",
        ),
        "Tell me what is in this image in one paragraph.",
    ],
)
pretty_print.wrapped(response.text, title="Image 1 Caption")

# Output:
#   [93m----------------------------------------- Image 1 Caption -----------------------------------------[0m

#     This image features a striking contrast between a large, imposing robot and a small, delicate kitten set within what appears to be an industrial or workshop environment. The robot, made of dark, metallic armor with intricate circuit-like patterns on its head, has intensely glowing red eyes, giving it a powerful and somewhat ominous presence. Perched playfully on the robot's large, detailed left arm, a small grey tabby kitten with curious eyes is depicted in mid-action, seemingly reaching out with a paw towards the robot's upper arm or shoulder. The scene is lit by soft light filtering in from a window or opening in the background, highlighting the metallic sheen of the robot and the soft fur of the kitten, creating a compelling juxtaposition of technology and nature.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Using the same approach, we can easily pass multiple images simultaneously:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=load_image_as_bytes(image_path=Path("images") / "image_1.jpeg", format="WEBP"),
            mime_type="image/webp",
        ),
        types.Part.from_bytes(
            data=load_image_as_bytes(image_path=Path("images") / "image_2.jpeg", format="WEBP"),
            mime_type="image/webp",
        ),
        "What's the difference between these two images? Describe it in one paragraph.",
    ],
)
pretty_print.wrapped(response.text, title="Differences between images")

# Output:
#   [93m------------------------------------ Differences between images ------------------------------------[0m

#     The two images present a stark contrast in the nature of the interaction between an animal and a robot, as well as their respective environments. The first image depicts a gentle and curious encounter, with a small, grey kitten affectionately standing on the arm of a large, metallic robot in what appears to be a clean, well-lit industrial setting, conveying a sense of harmony and innocence. In contrast, the second image portrays a tense and aggressive confrontation between a large, fluffy white dog and a sleek, black humanoid robot in a dirty, trash-strewn urban alleyway, with both subjects in an combative stance, evoking a feeling of conflict and danger.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
### 2.2 As base64 encoded strings

"""

from typing import cast


def load_image_as_base64(
    image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
) -> str:
    """
    Load an image and convert it to base64 encoded string.

    Args:
        image_path: Path to the image file to load
        format: Output image format (WEBP, JPEG, or PNG). Defaults to "WEBP"
        max_width: Maximum width for resizing. If image width exceeds this, it will be resized proportionally. Defaults to 600
        return_size: Parameter passed to load_image_as_bytes function. Defaults to False

    Returns:
        str: Base64 encoded string representation of the image
    """

    image_bytes = load_image_as_bytes(image_path=image_path, format=format, max_width=max_width, return_size=False)

    return base64.b64encode(cast(bytes, image_bytes)).decode("utf-8")

image_base64 = load_image_as_base64(image_path=Path("images") / "image_1.jpeg", format="WEBP")
pretty_print.wrapped(f"{image_base64[:100]}...", title="Image 1 Base64")
# Output:
#   [93m------------------------------------------ Image 1 Base64 ------------------------------------------[0m

#     UklGRmCtAABXRUJQVlA4IFStAABQ7AKdASpYAlgCPm0ylEekIqInJnQ7gOANiWdtk7FnEo2gDknjPixW9SNSb5P7IbBNhLn87Vtp...

#   [93m----------------------------------------------------------------------------------------------------[0m


response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image_base64, mime_type="image/webp"),
        "Tell me what is in this image in one paragraph.",
    ],
)
response.text

# Output:
#   "The image features a striking juxtaposition of a large, imposing humanoid robot and a small, fluffy grey tabby kitten. The robot, constructed from dark, metallic armor with intricate circuitry patterns on its head, stares forward with intense, glowing red eyes. Perched on its left arm, the curious kitten appears to be exploring or playfully interacting with the metallic giant, with one paw raised and gently touching the robot's shoulder armor. The scene is set in what looks like an industrial or workshop environment, with large metal structures visible in the background and a warm light source illuminating the subjects from the upper left."

"""
### 2.3 As URLs

At the time of writing this notebook, Gemini works well primarily with GCP Cloud Storage links, which are excellent for production use cases but complicate our simple demonstration.

The code would not change much and would look like this:
```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_uri(uri="gs://gemini-images/image_1.jpeg", mime_type="image/webp"),
        "Tell me what is in this image in one paragraph.",
    ],
)
```
"""

"""
### 2.4 Object detection with LLMs

As a more exciting example, let's do object detection with multimodal LLMs.
"""

from pydantic import BaseModel, Field


class BoundingBox(BaseModel):
    ymin: float
    xmin: float
    ymax: float
    xmax: float
    label: str = Field(default="The object found within the bounding box.")


class Detections(BaseModel):
    bounding_boxes: list[BoundingBox]


client = genai.Client()
prompt = """
Detect all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.
"""

image_bytes, image_size = load_image_as_bytes(
    image_path=Path("images") / "image_1.jpeg", format="WEBP", return_size=True
)

config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=Detections,
)

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/webp",
        ),
        prompt,
    ],
    config=config,
)

width, height = image_size
print("Image size: ", width, height)
detections = cast(Detections, response.parsed)

for bounding_box in detections.bounding_boxes:
    bounding_box.ymin = int(bounding_box.ymin / 1000 * height)
    bounding_box.xmin = int(bounding_box.xmin / 1000 * width)
    bounding_box.ymax = int(bounding_box.ymax / 1000 * height)
    bounding_box.xmax = int(bounding_box.xmax / 1000 * width)
    print(bounding_box)
# Output:
#   Image size:  600 600

#   ymin=163 xmin=21 ymax=473 xmax=321 label='The object found within the bounding box.'

#   ymin=0 xmin=223 ymax=598 xmax=600 label='The object found within the bounding box.'


"""
For fun, let's visualize the bounding boxes: 
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def visualize_detections(detections: Detections, image_path: Path) -> None:
    """
    Visualize detected bounding boxes on an image with red rectangles and labels.

    Args:
        detections: Detections object containing bounding boxes with pixel coordinates
        image_path: Path to the image file to visualize

    Returns:
        None: Displays the image with bounding boxes in the notebook
    """

    image = PILImage.open(image_path)
    image_array = np.array(image)

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.imshow(image_array)

    for bbox in detections.bounding_boxes:
        # Calculate box dimensions (matplotlib uses bottom-left corner + width/height)
        width = bbox.xmax - bbox.xmin
        height = bbox.ymax - bbox.ymin

        # Create rectangle patch (x, y is bottom-left corner)
        rect = patches.Rectangle((bbox.xmin, bbox.ymin), width, height, linewidth=3, edgecolor="red", facecolor="none")

        # Add rectangle to the plot
        ax.add_patch(rect)

        # Add label text (positioned at bottom-left of bounding box)
        ax.text(
            bbox.xmin,
            bbox.ymax + 5,  # Slightly below the box
            bbox.label,
            fontsize=12,
            color="red",
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
        )

    # Remove axis ticks and labels for cleaner display
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Object Detection Results: {image_path.name}", fontsize=14, fontweight="bold")

    plt.tight_layout()
    plt.show()

visualize_detections(detections, Path("images") / "image_1.jpeg")
# Output:
#   <Figure size 800x600 with 1 Axes>

"""
### 2.5 Working with PDFs

We can treat PDFs similarly to images. Therefore, we can pass PDFs as bytes:

"""

pdf_bytes = (Path("pdfs") / "decoding_ml_article.pdf").read_bytes()

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
        "What is this document about? Provide a brief summary of the main topics.",
    ],
)
pretty_print.wrapped(response.text, title="PDF Summary (as bytes)")
# Output:
#   [93m-------------------------------------- PDF Summary (as bytes) --------------------------------------[0m

#     This document is an article titled "5 Books to Ship AI Products in 2025" by Paul Iusztin.

#   

#   **Brief Summary:**

#   The article provides a curated list of five (plus one bonus) recommended books for individuals interested in AI Engineering, particularly focusing on building and deploying Large Language Model (LLM) and agentic systems in production environments.

#   

#   **Main Topics:**

#   

#   *   **Foundational Machine Learning System Design:** Concepts for building robust, production-grade ML systems and MLOps.

#   *   **Prompt Engineering for LLMs:** Techniques for designing effective and scalable prompts for large language models.

#   *   **AI Engineering Principles:** Broader concepts of AI Engineering, including RAG (Retrieval-Augmented Generation), agentic systems, and LLMOps (LLM Operations).

#   *   **Building LLMs for Production:** Practical, hands-on guidance on implementing LLM applications, including RAG techniques, fine-tuning, and integrating frameworks like LangChain and LlamaIndex.

#   *   **Deploying and Optimizing LLMs:** Strategies for shipping LLMs to production, including optimization tools, data engineering for LLMs, serving at scale, and infrastructure considerations.

#   *   **End-to-End LLM System Development:** The bonus book, co-authored by the writer, focuses on a comprehensive approach to architecting, building, and deploying complex LLM RAG applications.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Alternatively, as base64 encoded strings:
"""

def load_pdf_as_base64(pdf_path: Path) -> str:
    """
    Load a PDF file and convert it to base64 encoded string.

    Args:
        pdf_path: Path to the PDF file to load

    Returns:
        str: Base64 encoded string representation of the PDF
    """

    with open(pdf_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


pdf_base64 = load_pdf_as_base64(pdf_path=Path("pdfs") / "decoding_ml_article.pdf")

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        "What is this document about? Provide a brief summary of the main topics.",
        types.Part.from_bytes(data=pdf_base64, mime_type="application/pdf"),
    ],
)

pretty_print.wrapped(response.text, title="PDF Summary (as base64)")

# Output:
#   [93m------------------------------------- PDF Summary (as base64) -------------------------------------[0m

#     This document is a review and recommendation list of six books (five main plus one bonus) aimed at individuals looking to get into AI Engineering and ship AI products in 2025, with a strong focus on Large Language Models (LLMs) and agentic systems.

#   

#   **Main topics covered by the recommended books include:**

#   

#   *   **Foundational Machine Learning and AI Systems Design:** Concepts for building robust, production-grade ML and AI systems, including MLOps and infrastructure.

#   *   **Prompt Engineering for LLMs:** Strategies and best practices for effectively designing and manipulating prompts for large language models.

#   *   **AI Engineering Principles:** Understanding the differences between AI and ML engineering, and key aspects like RAG (Retrieval Augmented Generation), building agentic systems (guardrails, caches, memory), and LLMOps (observability, user feedback).

#   *   **Hands-on LLM Production & Deployment:** Practical implementation of LLM applications, covering techniques like RAG, fine-tuning, data engineering for LLM apps, optimization (e.g., ONNX, TensorRT), training, serving LLMs at scale, and deployment considerations.

#   *   **End-to-end LLM RAG Application Development:** Comprehensive steps for architecting, collecting data for, building pipelines for, fine-tuning, evaluating, deploying, and scaling LLM and RAG systems.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 3. Implementing multimodal RAG for images and text
"""

from io import BytesIO
from typing import Any

import numpy as np


def generate_image_description(image_bytes: bytes) -> str:
    """
    Generate a detailed description of an image using Gemini Vision model.

    Args:
        image_bytes: Image data as bytes

    Returns:
        str: Generated description of the image
    """

    try:
        # Convert bytes back to PIL Image for vision model
        img = PILImage.open(BytesIO(image_bytes))

        # Use Gemini Vision model to describe the image
        prompt = """
        Describe this image in detail for semantic search purposes. 
        Include objects, scenery, colors, composition, text, and any other visual elements that would help someone find 
        this image through text queries.
        """

        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[prompt, img],
        )

        if response and response.text:
            description = response.text.strip()

            return description
        else:
            print("❌ No description generated from vision model")

            return ""

    except Exception as e:
        print(f"❌ Failed to generate image description: {e}")

        return ""


def embed_text_with_gemini(content: str) -> np.ndarray | None:
    """
    Embed text content using Gemini's text embedding model.

    Args:
        content: Text string to embed

    Returns:
        np.ndarray | None: Embedding vector as numpy array or None if failed
    """

    try:
        result = client.models.embed_content(
            model="gemini-embedding-001",  # Gemini's text embedding model
            contents=[content],
        )
        if not result or not result.embeddings:
            print("❌ No embedding data found in response")
            return None

        return np.array(result.embeddings[0].values)

    except Exception as e:
        print(f"❌ Failed to embed text: {e}")
        return None

embed_text_with_gemini("This is a test")
# Output:
#   array([-0.02252334, -0.00076438,  0.00240217, ..., -0.00574729,

#          -0.00052345, -0.00213343], shape=(3072,))

from typing import cast


def create_multimodal_embeddings(image_paths: list[Path]) -> list[dict]:
    """
    Create embeddings for both images and text using proper Gemini approach.

    This function processes a list of image paths, generates descriptions for each image
    using Gemini Vision model, and creates embeddings for those descriptions.

    Args:
        image_paths: List of Path objects pointing to image files to process

    Returns:
        list[dict]: List of dictionaries containing image data, descriptions, and embeddings.
                   Each dict contains keys: 'content', 'type', 'filename', 'description', 'embedding'
    """

    docs = []
    for image_path in image_paths:
        image_bytes = cast(bytes, load_image_as_bytes(image_path, format="WEBP", return_size=False))

        image_description = generate_image_description(image_bytes)
        pretty_print.wrapped(f"`{image_description[:500]}...`", title="Generated image description:")

        # IMPORTANT NOTE: When working with multimodal embedding models, we can directly embed the
        # `image_bytes` instead of generating and embedding the description. Otherwise, everything
        # else remains the same within the whole RAG system.
        image_embedding = embed_text_with_gemini(image_description)

        docs.append(
            {
                "content": image_bytes,
                "type": "image",
                "filename": image_path,
                "description": image_description,
                "embedding": image_embedding,
            }
        )

    return docs


image_paths = list(Path("images").glob("*.jpeg"))
all_docs = create_multimodal_embeddings(image_paths)

if len(all_docs) == 0:
    pretty_print.wrapped("No embeddings were created successfully", title="❌")
else:
    pretty_print.wrapped(f"Successfully created {len(all_docs)} embeddings", title="✅")
# Output:
#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image depicts a striking juxtaposition of advanced technology and innocent nature, set within a grimy, futuristic industrial environment.

#   

#   **Objects:**

#   

#   *   **Robot:** The dominant figure is a large, humanoid robot, occupying the right side of the frame.

#       *   **Head/Face:** Its head is helmet-like, dark grey, and features intricate **circuit board patterns** or **motherboard textures** etched across its surface, giving it a sophisticated, high-tech appearance. The most prominent feature ...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image captures a dramatic and unusual confrontation between a large white dog and a sleek black humanoid robot in a gritty urban alleyway.

#   

#   **Objects & Figures:**

#   

#   1.  **The Dog:** A prominent, fluffy white dog, resembling a Samoyed or a large white spitz breed, is positioned on the left side of the frame. It is captured mid-action, lunging forward with its front paws raised off the ground, mouth wide open in an aggressive snarl, baring its teeth. Its pink tongue is visible. Its thick, whit...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image depicts a detailed close-up of an African American man intently working on the internal components of an open desktop computer tower. The scene is illuminated by the cool, bright blue and white glow of the PC's internal fans and components, contrasting with the generally darker ambient lighting of the workspace.

#   

#   **Objects:**

#   *   **Person:** An adult Black male with a salt-and-pepper beard and black-framed eyeglasses. He is wearing a dark, possibly teal or grey, t-shirt. His hands are...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image depicts a dynamic, high-impact scene of two humanoid robots engaged in a futuristic combat within a sleek, metallic arena.

#   

#   **Objects:**

#   *   **Robot 1 (Left):** A slender, agile-looking robot with highly reflective, polished silver or chrome armor. Its helmet features a bright, glowing electric blue visor/eye area. Blue energy lines also illuminate its chest and parts of its limbs, indicating power or internal systems. It is shown mid-punch, with its right arm extended, making contact...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------------ ✅ ------------------------------------------------[0m

#     Successfully created 4 embeddings

#   [93m----------------------------------------------------------------------------------------------------[0m


from sklearn.metrics.pairwise import cosine_similarity


def search_multimodal(query_text: str, docs: list[dict], top_k: int = 3) -> list[Any]:
    """
    Search for most similar documents to query using direct Gemini client.

    This function embeds the query text and compares it against pre-computed embeddings
    of document descriptions to find the most semantically similar matches.

    Args:
        query_text: Text query to search for
        docs: List of document dictionaries containing embeddings and metadata
        top_k: Number of top results to return. Defaults to 3

    Returns:
        list[Any]: List of document dictionaries with similarity scores, sorted by relevance
    """

    print(f"\n🔍 Embedding query: '{query_text}'")

    query_embedding = embed_text_with_gemini(query_text)

    if query_embedding is None:
        print("❌ Failed to embed query")
        return []
    else:
        print("✅ Query embedded successfully")

    # Calculate similarities using our custom function
    embeddings = [doc["embedding"] for doc in docs]
    similarities = cosine_similarity([query_embedding], embeddings).flatten()

    # Get top results
    top_indices = np.argsort(similarities)[::-1][:top_k]  # type: ignore

    results = []
    for idx in top_indices.tolist():
        results.append({**docs[idx], "similarity": similarities[idx]})

    return results


query = "two robots fighting"
results = search_multimodal(query, all_docs, top_k=1)

if not results:
    pretty_print.wrapped("❌ No results found", title="❌")
else:
    result = results[0]

    pretty_print.wrapped(
        [
            f"Similarity {result['similarity']:.3f}",
            f"Filename {result['filename']}",
            f"Description `{result['description'][:1000]}...`",
        ],
        title=f"Results for query = {query}",
    )
    display_image(Path(result["filename"]))
# Output:
#   

#   🔍 Embedding query: 'two robots fighting'

#   ✅ Query embedded successfully

#   [93m----------------------------- Results for query = two robots fighting -----------------------------[0m

#     Similarity 0.768

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Filename images/image_4.jpeg

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Description `This image depicts a dynamic, high-impact scene of two humanoid robots engaged in a futuristic combat within a sleek, metallic arena.

#   

#   **Objects:**

#   *   **Robot 1 (Left):** A slender, agile-looking robot with highly reflective, polished silver or chrome armor. Its helmet features a bright, glowing electric blue visor/eye area. Blue energy lines also illuminate its chest and parts of its limbs, indicating power or internal systems. It is shown mid-punch, with its right arm extended, making contact with the other robot. Its left arm is bent, seemingly ready for another strike, and its body is coiled in a powerful, lunging pose.

#   *   **Robot 2 (Right):** A bulkier, more heavily armored robot with a darker, charcoal or matte black finish. The back of its torso features two prominent, glowing red lights, possibly eyes, power indicators, or thrusters. It is recoiling from the impact, with its body angled back and its arms slightly splayed.

#   *   **Debris/Particles:** A significant amount of brig...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   <IPython.core.display.Image object>

query = "a kitten with a robot"
results = search_multimodal(query, all_docs, top_k=1)

if not results:
    pretty_print.wrapped("❌ No results found", title="❌")
else:
    result = results[0]

    pretty_print.wrapped(
        [
            f"Similarity {result['similarity']:.3f}",
            f"Filename {result['filename']}",
            f"Description `{result['description'][:1000]}...`",
        ],
        title=f"Results for query = {query}",
    )
    display_image(Path(result["filename"]))
# Output:
#   

#   🔍 Embedding query: 'a kitten with a robot'

#   ✅ Query embedded successfully

#   [93m---------------------------- Results for query = a kitten with a robot ----------------------------[0m

#     Similarity 0.808

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Filename images/image_1.jpeg

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Description `This image depicts a striking juxtaposition of advanced technology and innocent nature, set within a grimy, futuristic industrial environment.

#   

#   **Objects:**

#   

#   *   **Robot:** The dominant figure is a large, humanoid robot, occupying the right side of the frame.

#       *   **Head/Face:** Its head is helmet-like, dark grey, and features intricate **circuit board patterns** or **motherboard textures** etched across its surface, giving it a sophisticated, high-tech appearance. The most prominent feature is its **glowing red eyes** (or optical sensors), which emit a fierce, intense light, creating a strong contrast with its metallic body. It has a segmented, angular jawline and facial armor plating. There are no other visible facial features like a nose or mouth.

#       *   **Body/Arms:** The robot's body is robust and armored, primarily in shades of **gunmetal grey** and **dark silver**. Its shoulder is broadly curved, with visible bolts or rivets. The right arm is heavily detailed, appearing segm...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   <IPython.core.display.Image object>

"""
## 4. Building multimodal AI agents
"""

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent


@tool
def multimodal_search_tool(query: str) -> dict[str, Any]:
    """
    Search through a collection of images and their text descriptions to find relevant content.

    This tool searches through a pre-indexed collection of image-text pairs using the query
    and returns the most relevant match. The search uses multimodal embeddings to find
    semantic matches between the query and the content.

    Args:
        query: Text query describing what to search for (e.g., "cat", "kitten with robot")

    Returns:
        A formatted string containing the search result with description and similarity score
    """

    pretty_print.wrapped(query, title="🔍 Tool executing search for:")

    results = search_multimodal(query, all_docs, top_k=1)

    if not results:
        return {"role": "tool_result", "content": "No relevant content found for your query."}
    else:
        pretty_print.wrapped(str(results[0]["filename"]), title="🔍 Found results:")
    result = results[0]

    content = [
        {
            "type": "text",
            "text": f"Image description: {result['description']}",
        },
        types.Part.from_bytes(
            data=result["content"],
            mime_type="image/jpeg",
        ),
    ]

    return {
        "role": "tool_result",
        "content": content,
    }

def build_react_agent() -> Any:
    """
    Build a ReAct agent with multimodal search capabilities.

    This function creates a LangGraph ReAct agent that can search through images
    and text using the multimodal_search_tool. The agent uses Gemini 2.5 Pro
    for reasoning and tool execution.

    Returns:
        Any: A LangGraph ReAct agent instance configured with multimodal search tools
    """

    tools = [multimodal_search_tool]

    system_prompt = """You are a helpful AI assistant that can search through images and text to answer questions.
    
    When asked about visual content like animals, objects, or scenes:
    1. Use the multimodal_search_tool to find relevant images and descriptions
    2. Carefully analyze the image or image descriptions from the search results
    3. Look for specific details like colors, features, objects, or characteristics
    4. Provide a clear, direct answer based on the search results
    5. If you can't find the specific information requested, be honest about limitations
    
    Pay special attention to:
    - Colors and visual characteristics
    - Animal features and breeds
    - Objects and their properties
    - Scene descriptions and context
    
    Always search first using your tools before attempting to answer questions about specific images or visual content.
    """

    agent = create_react_agent(
        model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.1),
        tools=tools,
        prompt=system_prompt,
    )

    return agent


try:
    react_agent = build_react_agent()

    test_question = "what color is my kitten?"
    pretty_print.wrapped(test_question, title="🧪 Asking question:")

    response = react_agent.invoke(input={"messages": test_question})
    messages = response.get("messages", [])
    if messages:
        final_message = messages[-1].content
    else:
        final_message = "No response from the agent"
    pretty_print.wrapped(final_message, title="🤖 Agent response")
except Exception as e:
    print(f"❌ Error in ReAct agent: {e}")
# Output:
#   [93m---------------------------------------- 🧪 Asking question: ----------------------------------------[0m

#     what color is my kitten?

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- 🔍 Tool executing search for: -----------------------------------[0m

#     my kitten

#   [93m----------------------------------------------------------------------------------------------------[0m

#   

#   🔍 Embedding query: 'my kitten'

#   ✅ Query embedded successfully

#   [93m----------------------------------------- 🔍 Found results: -----------------------------------------[0m

#     images/image_1.jpeg

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------------- 🤖 Agent response -----------------------------------------[0m

#     Based on the image, your kitten is a grey tabby with light grey fur and faint darker stripes.

#   [93m----------------------------------------------------------------------------------------------------[0m

</details>


## YouTube Video Transcripts

<details>
<summary>API Error during transcription for https://www.youtube.com/watch?v=YOvxh_ma5qE: 500 INTERNAL. {'error': {'code': 500, 'message': 'An internal error has occurred. Please retry or report in https://developers.generativeai.google/guide/troubleshooting', 'status': 'INTERNAL'}}</summary>

API Error during transcription for https://www.youtube.com/watch?v=YOvxh_ma5qE: 500 INTERNAL. {'error': {'code': 500, 'message': 'An internal error has occurred. Please retry or report in https://developers.generativeai.google/guide/troubleshooting', 'status': 'INTERNAL'}}

</details>


## Additional Sources Scraped

<details>
<summary>arxiv-org</summary>

Documents are visually rich structures that convey information through text, but also figures, page layouts, tables, or even fonts. Since modern retrieval systems mainly rely on the textual information they extract from document pages to index documents -often through lengthy and brittle processes-, they struggle to exploit key visual cues efficiently. This limits their capabilities in many practical document retrieval applications such as Retrieval Augmented Generation (RAG). To benchmark current systems on visually rich document retrieval, we introduce the Visual Document Retrieval Benchmark ViDoRe, composed of various page-level retrieval tasks spanning multiple domains, languages, and practical settings. The inherent complexity and performance shortcomings of modern systems motivate a new concept; doing document retrieval by directly embedding the images of the document pages. We release ColPali, a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages. Combined with a late interaction matching mechanism, ColPali largely outperforms modern document retrieval pipelines while being drastically simpler, faster and end-to-end trainable. We release models, data, code and benchmarks under open licenses at [https://hf.co/vidore](https://hf.co/vidore).

# 1 INTRODUCTION

Document Retrieval consists of matching a user query to relevant documents in a given corpus. It is central to many widespread industrial applications, either as a standalone ranking system (search engines) or as part of more complex information extraction or Retrieval Augmented Generation (RAG) pipelines.

Over recent years, pretrained language models have enabled large improvements in text embedding models. In practical industrial settings, however, the primary performance bottleneck for efficient document retrieval stems not from embedding model performance but from the prior data ingestion pipeline. Indexing a standard PDF document involves several steps. First, PDF parsers or Optical Character Recognition (OCR) systems are used to extract words from the pages. Document layout detection models can then be run to segment paragraphs, titles, and other page objects such as tables, figures, and headers. A chunking strategy is then defined to group text passages with some semantical coherence, and modern retrieval setups may even integrate a captioning step to describe visually rich elements in a natural language form, more suitable for embedding models. In our experiments (Table 2), we typically find that optimizing the ingestion pipeline yields much better performance on visually rich document retrieval than optimizing the text embedding model.https://arxiv.org/pdf/images/391f32efa12ee5d8c95be1f641c318cd9e821711f7d2f28610e9c54a25d13db6.jpg

Figure 1: ColPali simplifies document retrieval w.r.t. standard retrieval methods while achieving stronger performances with better latencies. Latencies and results are detailed in section 5 and subsection B.4.

Contribution 2: ColPali. We propose a novel concept and model architecture based on Vision Language Models (VLMs) to efficiently index documents purely from their visual features, allowing for subsequent fast query matching with late interaction mechanisms (Khattab & Zaharia, 2020). Our method, ColPali, significantly outperforms all other retrieval systems on $V i D o R e$ while being fast and end-to-end trainable. These results demonstrate the potential and the many benefits of this novel Retrieval in Vision Space concept, which could significantly alter the way document retrieval is approached in the industry moving forward. We release all resources at [https://hf.co/vidore](https://hf.co/vidore).

# 4 LATE INTERACTION BASED VISION RETRIEVAL

# 4.1 ARCHITECTURE

Vision-Language Models. Encouraged by their strong document understanding capabilities, we propose adapting recent VLMs for retrieval. The key concept is to leverage the alignment between output embeddings of text and image tokens acquired during multi-modal fine-tuning. To this extent, we introduce ColPali, a Paligemma-3B extension that is capable of generating ColBERT-style multivector representations of text and images (Figure 1). PaliGemma-3B is a strong candidate due to its small size, the many released checkpoints fine-tuned for different image resolutions and tasks, and the promising performances on various document understanding benchmarks. We add a projection layer to map each of the language model’s output token embeddings (whether from text or image tokens) to a vector space of reduced dimension $D = 1 2 8$ as used in the ColBERT paper (Khattab & Zaharia, 2020) to keep lightweight bag-of-embedding representations.

Late Interaction. Given query $q$ and document $d$ , we denote as $\\mathbf { E \_ { q } } \\in \\mathbb { R } ^ { N \_ { q } \\times D }$ and $\\mathbf { E \_ { d } } \\in \\mathbb { R } ^ { N \_ { d } \\times D }$ their respective multi-vector representation in the common embedding space $\\mathbb { R } ^ { D }$ , where $N \_ { q }$ and $N \_ { d }$ are respectively the number of vectors in the query and in the document page embeddings. The late interaction operator, $\\operatorname { L I } \\left( q , d \\right)$ , is the sum over all query vectors $\\mathbf { E \_ { q } } ^ { ( j ) }$ , of its maximum dot product $\\langle \\cdot \| \\cdot \\rangle$ with each of the $N \_ { d }$ document embedding vectors $\\mathbf { E \_ { d \\left( 1 : N \_ { d } \\right) } }$ .

$$
\\mathbf { L } \\left( q , d \\right) = \\sum \_ { i \\in \\left\[ \\left\| 1 , N \_ { q } \\right\| \\right\] } \\operatorname\* { m a x } \_ { j \\in \\left\[ \\left\| 1 , N \_ { d } \\right\| \\right\] } \\langle \\mathbf { E \_ { q } } ^ { ( i ) } \| \\mathbf { E \_ { d } } ^ { ( j ) } \\rangle
$$

Contrastive Loss. The Late Interaction operation is fully differentiable, enabling backpropagation. Let a batch ${ q \_ { k } , d \_ { k } } \_ { k \\in \[ \| 1 , b \| \] }$ composed of $b$ query-page pairs, where for all $k \\in \[ \| \\bar { 1 , \\upsilon } \| \]$ , the document page $d \_ { k }$ is the document corresponding to query $q \_ { k }$ . Following Khattab & Zaharia (2020), we define our in-batch contrastive loss $\\mathcal { L }$ as the softmaxed cross-entropy of the positive scores $s \_ { k } ^ { + } = \\mathrm { L I } \\left( q \_ { k } , d \_ { k } \\right)$ w.r.t. to the maximal in-batch negative scores $s \_ { k } ^ { - } = \\operatorname\* { m a x } \_ { l , l \\neq k } \\quad \\mathrm { L I } ( q \_ { k } , d \_ { l } ) ^ { 6 }$ :

$$
\\mathcal { L } = - \\frac { 1 } { b } \\sum \_ { k = 1 } ^ { b } \\log \\left\[ \\frac { \\exp \\left( s \_ { k } ^ { + } \\right) } { \\exp \\left( s \_ { k } ^ { + } \\right) + \\exp \\left( s \_ { k } ^ { - } \\right) } \\right\] = \\frac { 1 } { b } \\sum \_ { k = 1 } ^ { b } \\log \\left( 1 + \\exp \\left( s \_ { k } ^ { - } - s \_ { k } ^ { + } \\right) \\right)
$$

# 5.1 PERFORMANCE (R1)

We show performance is achieved iteratively through the combination of three factors; (1) a carefully crafted task-specific dataset, (2) pairing a pretrained LLM to a vision model to better leverage text semantics from the image, and (3) using multi-vector embeddings rather than a single vector representation to better capture the vast amount of visual information present in a document.

Leveraging Multi-Vector Embeddings through Late Interaction: ColPali. One benefit of inputting image patch embeddings through a language model is that they are natively mapped to a latent space similar to the textual input (query). This enables leveraging the ColBERT strategy to construct one embedding per image patch token, and at inference compute all interactions between text tokens and image patches, resulting in a step-change improvement in performance compared to BiPali. Results in Table 2 show that our ColPali model also largely outperforms the strong baselines based on Unstructured and captioning, as well as all evaluated text-image embedding models. The difference is particularly stark on the more visually complex benchmark tasks, such as InfographicVQA, ArxivQA, and TabFQuAD, respectively representing infographics, figures, and tables. However, text-centric documents are also better retrieved by the ColPali models across all evaluated domains and languages, making our approach the overall best-performing document-retrieval model.

# 5.2 LATENCIES & MEMORY FOOTPRINT

Offline Indexing. (R3) Standard retrieval methods using bi-encoders represent each chunk as a single vector embedding, which is easy to store and fast to compute. However, processing a PDF to get the different chunks is the most time-consuming part (layout detection, OCR, chunking), and using captioning to handle multimodal data will only exacerbate this already lengthy process. On the other hand, ColPali directly encodes pages from their image representation. Although the model is larger than standard retrieval encoders, skipping the preprocessing allows large speedups at indexing13 (Figure 2). As pages are embedded end-to-end in single forward pass, the VRAM usage depends exclusively on the sequence length (number of patches per image) which is fixed as well, enabling efficient batching strategies to fully leverage hardware acceleration. ColPali also benefits from most LLM efficiency improvements introduced in the ecosystem such as Flash Attention (Dao, 2023).https://arxiv.org/pdf/images/9b42e697ca163d7e29300ce3893bfbb565058abb5496f1a4433ddbc0420c9cb1.jpg

Figure 2: Offline document indexing with ColPali is much simpler and faster compared to standard retrieval methods. The PDF Parser results are obtained following the Unstructured settings with BGE-M3 detailed in subsection 3.2. All indexing speeds are averaged per-page latencies. More details in subsection B.4

# 5.3 INTERPRETABILITY

By superimposing the late interaction heatmap on top of the original image, we can visualize the most salient image patches with respect to each term of the query, yielding interpretable insights into model focus zones. As epitomized in Figure 3 (right), we observe ColPali exhibits strong OCR capabilities as both the words “hourly” and “hours” present a high similarity score with the query token < hour>. We also note particular focus on other non-trivial image features such as the x-axis representing hours being salient. Other visualization examples are shown in Appendix D.https://arxiv.org/pdf/images/8293b990ecdbbef3709cfbff1889d6bbaef5395f6aee03741bd76b28b993209f.jpg

Figure 3: (Left: Token Pooling) Relative performance degradation when reducing the number of stored embeddings per document. (Right: Interpretability) For each term in a user query, ColPali identifies the most relevant document image patches (highlighted zones) and computes a query-topage matching score.

</details>

<details>
<summary>complex-document-recognition-ocr-doesn-t-work-and-here-s-how</summary>

In this article, I will dive into a complex world of complex document recognition using AI and OCR.

Document recognition nowadays is not a complex task.

Modern OCR solutions are able to detect both typed and written text in many languages. One can find dedicated solutions for the detection of specific documents like passports and driver’s licenses.

But where out-of-the-box [AI](https://hackernoon.com/c/ai?ref=hackernoon.com) tends to struggle is when a document includes special symbols or tilted text.

Technical drawings are among the ‘trouble children’ that cause ready-made OCR solutions to struggle: they are nothing but a collection of weird symbols and weirdly placed text.

Having worked on an AI solution for technical drawing recognition, I have insights into the world of modern OCR that I will share in this article.

## Why OCR is bad for OCR

The ‘digital first’ approach, at the forefront of many businesses, has motivated many to convert physical documents into a digital format. This process usually involves the implementation of OCR — optical character recognition — which converts physical documents into PDF files.

Morel OCR tools are capable of recognizing more than just text. In many cases, OCR tools can detect special symbols, written text, signatures, images, and more.

Many of these tools come ready to use: all you need to do is install the tool (or, if you are working on a custom solution, use an API) to scan the documents in question.

Despite all this, OCR tools have certain limitations. They don’t work well for irregular text, also called wild text, like low-quality scanned documents with no predefined structure, car license plates, text on advertisement billboards, etc.

### Low-quality scans

The quality of text recognition depends highly on the quality of the document itself. Warping, scratches, faded ink, and more have a detrimental effect on the recognition quality.

### Symbol mixups

Even the best OCR tools have trouble distinguishing between certain similar-looking letters and numbers, like ‘3’ and ‘8’ or ‘O’ and ‘D.’ The very challenges OCR is supposed to solve often become the stumbling block of document digitization.

### Special symbols

Documents that feature any special symbols, from letters specific to a certain language to symbols denominating certain objects, like symbols used in technical drawings, e.g., diameter ‘Ø,’ square ‘□.’

## AI to the rescue

Using artificial intelligence, OCR tools can be improved and augmented to better handle complex documents, and often even replaced by a custom [AI neural network](https://hackernoon.com/enhancing-neural-network-reasoning-the-promise-of-contrastive-decoding-for-llms?ref=hackernoon.com).

Model-based OCR, or intelligent OCR, is the result of using deep learning for text document recognition.

Neural networks can be trained to recognize text regular OCR tools have trouble with. Intelligent OCR provides superior text recognition results in document recognition applications by improving recognition speed and reducing errors.

## Recognition of complex documents

Despite the widespread digitization, some paperwork remains offline. This usually applies to complex documents that are impossible to digitize due to their complex layouts, the use of special symbols, and unconventional formatting.

Technical drawings are the perfect example of a complex document: their layouts change from one document to another; they include a bunch of symbols specific to technical drawings only, and the text is often formatted in odd ways. All of the above makes technical drawings the perfect candidate for model-based OCR.

While working on a similar project, I’ve developed an understanding of the best strategies to apply when working on digitizing technical drawings. I have had experience with working on an AI for floor plan detection, so that’s what I’ll be using as an example.

I’ve broken the process down into sections, as this is exactly how one should approach the development of AI-based OCR solutions for complex document recognition.

## Stage 1: Detection of text

Recognition of plain text is the most simple part of this entire ordeal. When it comes to technical drawings, plain text is used to specify the drawing type, dimensions, floor plan type, building type, etc. While the detection of plain text is a simple task, detecting text on a technical drawing is far more complex.

The text can come in a variety of fonts, sizes, and colors, can be rotated or upside down, and contains special symbols. Ready-made OCR software like iText and OCRSpace can detect simple text with high accuracy, but they fail spectacularly when it comes to technical drawings (or any other complex document, for that matter). For example, these tools struggle to detect rotated text.https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-v993xj8.jpeg?w=800

OCR tools often have trouble detecting rotated text \| Image by author

Most OCR tools can be fine-tuned to handle problematic text better. The best approach to recognizing complex text is to use multiple fine-tuned OCR tools along with a balancer that compares the results of each tool and chooses the one that produces the most accurate results.

Another benefit of using fine-tuned OCR software is the increase in recognition speed.https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-v9a3xhv.jpeg?w=800

Fine-tuning of OCR software leads to better results \| Image by author

By fine-tuning these tools alone, we’ve seen a 200 times decrease in document processing speed.If you add an OCR engine into the equation, like Tesseract, the text recognition quality can be increased up to 99.9%.

## Stage 2: Recognition of special symbols

Each technical drawing includes special symbols of some sort. In the case of floor plan technical drawings, the documents include symbols designating doors, windows, electrical outlets, etc.

These symbols, or labels, look like geometric figures with text inside. They can be difficult to distinguish from their surroundings due to their shape, which blends in perfectly with the rest of the drawing.

In addition, there can be multiple labels representing the same object due to inconsistencies in document design.https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-efb3xu6.jpeg?w=800

Similar looking objects are often detected as the same one \| Image by author

Pre-trained computer vision solutions, like OpenCV libraries for symbol detection, work best with photographs of real-life objects. Technical drawings are quite a bit different: they are almost always in black and white and mostly consist of geometric shapes.

We’ve tested multiple OpenCV libraries, each of which resulted in albeit different, yet insufficiently low recognition quality. Unless you develop your own neural network from scratch, any pre-trained computer vision model needs to be built upon to achieve decent recognition quality.

One of the main problems with using [pre-trained CV models](https://hackernoon.com/creating-computer-vision-apps-without-building-media-pipelines?ref=hackernoon.com) is the amount of false positive results they produce. Technical drawings consist of simple geometric shapes, but so do special symbols and labels, which results in CV models detecting random parts of the drawings as labels.

The best way of mitigating this issue is to implement deep learning to detect false positive results and remove them from the final detection results.https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-mjc3x1z.jpeg?w=800

Deep learning can be used to remove false positive results \| Image by author

## Stage 3: Spreadsheets

Technical drawings often include large spreadsheets with merged cells and complex structures stretching across multiple pages. While spreadsheets are generally easy to detect, the complex nature of these spreadsheets makes them difficult to crack.

Going a custom software route is the best way to achieve satisfactory results. Here’s how we’ve done it:

### Recognition of text in a spreadsheet

Solutions like Amazon Textract work very well and can extract text with very high accuracy as long as the document scan is of high quality. Documents with 300 DPI result in 100% recognition accuracy and 100 DPI results in ~90% accuracy.

### Recognition of spreadsheet structure

First, you need to detect the spreadsheet structure by detecting vertical and horizontal lines.

Using OpenCV, create a binary matrix by converting the document into black and white, defining its threshold in a way that results in all horizontal and vertical lines being one and the rest — a zero. The binary matrix will then contain the spreadsheet structure.

Using the extracted text and spreadsheet structure, the spreadsheet itself can be extracted in an editable format like Excel.

## Summing Up

Digitizing any complex document comes with its own set of problems. The best approach to solving them is to approach them one by one, researching the best tools for the job, testing them, and comparing results.

The approaches I’ve described work on any document type despite its type, as individual challenges can be similar despite the document type being completely different.

For example, I have experience in working on a passport detection solution where the text recognition challenges were very similar, and we’ve used some of the same techniques.

Knowing your OCR tools, being well-versed in coding neural networks and having decent experience in the field of custom AI development will help overcome any document digitization challenges.

</details>

<details>
<summary>image-understanding-gemini-api-google-ai-for-developers</summary>

Gemini models are built to be multimodal from the ground up, unlocking a wide range of image processing and computer vision tasks including but not limited to image captioning, classification, and visual question answering without having to train specialized ML models.

## Passing images to Gemini

You can provide images as input to Gemini using two methods:

- [Passing inline image data](https://ai.google.dev/gemini-api/docs/image-understanding#inline-image): Ideal for smaller files (total request
size less than 20MB, including prompts).
- [Uploading images using the File API](https://ai.google.dev/gemini-api/docs/image-understanding#upload-image): Recommended for larger files or for
reusing images across multiple requests.

### Passing inline image data

You can pass inline image data in the
request to `generateContent`. You can provide image data as Base64 encoded
strings or by reading local files directly (depending on the language).

The following example shows how to read an image from a local file and pass
it to `generateContent` API for processing.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)

```
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[\
      types.Part.from_bytes(\
        data=image_bytes,\
        mime_type='image/jpeg',\
      ),\
      'Caption this image.'\
    ]
  )

  print(response.text)

```

You can also fetch an image from a URL, convert it to bytes, and pass it to
`generateContent` as shown in the following examples.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)

```
from google import genai
from google.genai import types

import requests

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=["What is this image?", image],
)

print(response.text)

```

## Prompting with multiple images

You can provide multiple images in a single prompt by including multiple image
`Part` objects in the `contents` array. These can be a mix of inline data
(local files or URLs) and File API references.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)

```
from google import genai
from google.genai import types

client = genai.Client()

# Upload the first image
image1_path = "path/to/image1.jpg"
uploaded_file = client.files.upload(file=image1_path)

# Prepare the second image as inline data
image2_path = "path/to/image2.png"
with open(image2_path, 'rb') as f:
    img2_bytes = f.read()

# Create the prompt with text and multiple images
response = client.models.generate_content(

    model="gemini-2.5-flash",
    contents=[\
        "What is different between these two images?",\
        uploaded_file,  # Use the uploaded file reference\
        types.Part.from_bytes(\
            data=img2_bytes,\
            mime_type='image/png'\
        )\
    ]
)

print(response.text)

```

## Object detection

From Gemini 2.0 onwards, models are further trained to detect objects in an
image and get their bounding box coordinates. The coordinates, relative to image
dimensions, scale to \[0, 1000\]. You need to descale these coordinates based on
your original image size.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)

```
from google import genai
from google.genai import types
from PIL import Image
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

image = Image.open("/path/to/image.png")

config = types.GenerateContentConfig(
  response_mime_type="application/json"
  )

response = client.models.generate_content(model="gemini-2.5-flash",
                                          contents=[image, prompt],
                                          config=config
                                          )

width, height = image.size
bounding_boxes = json.loads(response.text)

converted_bounding_boxes = []
for bounding_box in bounding_boxes:
    abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
    abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
    abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
    abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
    converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

print("Image size: ", width, height)
print("Bounding boxes:", converted_bounding_boxes)

```

</details>

<details>
<summary>multi-modal-ml-with-openai-s-clip-pinecone</summary>

The multi-modal nature of CLIP is powered by two encoder models trained to “speak the same language”. Text inputs are passed to a text encoder, and image inputs to an image encoder [3]. These models then create a _vector representation_ of the respective input.

Both models “speak the same language” by encoding similar concepts in text and images into similar vectors. That means that the text “two dogs running across a frosty field” would output a vector similar to an _image_ of two dogs running across a frosty field.https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fa54a2f1fa0aeac03748c09df0fdfbb42aadc96b7-2430x1278.png&w=3840&q=75

Similar text and images will be encoded into a similar vector space. Dissimilar text and images do not share a similar vector space.

We can think of the language these models speak as the vector space in which they encode vectors. These two models can express nuanced information about text and images through this vector space. However, this “vector language” is far too abstract for us to directly understand.

Rather than directly reading this “language”, we can train other simple neural networks to understand it and make predictions that we can understand. Or we use vector search to identify similar concepts and patterns across text and image domains.

Now that we’ve seen what CLIP can do, let’s take a look at _how_ it can do this.

## CLIP

CLIP actually consists of two models trained in parallel. A 12-layer text transformer for building text embeddings and a ResNet or vision transformer (ViT) for building image embeddings [3].https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F539716ea1571e459908c1fdc5a898fea239d8243-2803x1672.png&w=3840&q=75

Architecture diagram of CLIP with the text encoder and ViT or ResNet as the image encoder.

The text encoder and image encoder (ResNet _or_ ViT) output single vector embeddings for each text/image record fed into the encoders. All vectors are 512 dimensional and can be represented in the same vector space, meaning similar images and text produce vectors that appear near each other.

### Contrastive Pretraining

Across both [**N** atural](https://www.pinecone.io/learn/series/nlp/) [**L** anguage](https://www.pinecone.io/learn/series/nlp/) [**P** rocessing (NLP)](https://www.pinecone.io/learn/series/nlp/) and computer vision (CV), large pretrained models dominate the SotA. The idea is that by giving a big model a lot of data, they can learn general patterns from the dataset.

For language models, that may be the general rules and patterns in the English language. For vision models, that may be the characteristics of different scenes or objects.

The problem with multi-modality is that these models are trained separately and, by default, have no understanding of one another. CLIP solves this thanks to image-text _contrastive pretraining_. With CLIP, text and image encoders are trained while considering the other modality and context. Meaning that the text and image encoders share an “indirect understanding” of patterns in both modalities; language and vision.

Contrastive pretraining works by taking a _(text, image)_ pair – where the text describes the image – and learning to encode the pairs as closely as possible in vector space.

For this to work well, we also need negative pairs to provide a contrastive comparison. We need positive pairs that should output similar vectors and negative pairs that should output dissimilar vectors.

This is the general idea behind contrastive learning, which can be found in the training functions of many models, particularly those that produce embedding vectors.

The negative pairs can be extracted directly from positive pairs. If we have positive pairs (T1,I1)(T\_1,I\_1)(T1​,I1​) and (T2,I2)(T\_2,I\_2)(T2​,I2​), we simply swap the components, giving us the negative pairs (T1,I2)(T\_1,I\_2)(T1​,I2​) and (T2,I1)(T\_2,I\_1)(T2​,I1​).

With this, we can apply a loss function that maximizes the similarity between (T1,I1)(T\_1,I\_1)(T1​,I1​) and (T2,I2)(T\_2,I\_2)(T2​,I2​), and minimizes the similarity between (T1,I2)(T\_1,I\_2)(T1​,I2​) and (T2,I1)(T\_2,I\_1)(T2​,I1​). Altogether, this looks like this:https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fd6868e6dae721512fed8f1287fc9ffe6b6a2cddd-2332x1342.png&w=3840&q=75

Contrastive pretraining with CLIP.

In this image, we can see a single pretraining step on a single batch. The loss function assumes pairs in the diagonal should have a maximized dot product score, and all other pairs should have a minimized dot product score. Both text and image encoder models are optimized for this.

A fundamental assumption is that there are no other positive pairs within a single batch. For example, we assume that “two dogs running across a frosty field” is only relevant to the image it is paired with. We assume there are no other texts or images with similar meanings.

This assumption is possible because the datasets used for pretraining are diverse and large enough that the likelihood of two similar pairs appearing in a single batch is negligible. Therefore, rare enough to have a little-to-no negative impact on pretraining performance.

</details>

<details>
<summary>multimodal-embeddings-an-introduction-towards-data-science</summary>

AI research is traditionally split into distinct fields: NLP, computer vision (CV), robotics, human-computer interface (HCI), etc. However, countless practical tasks require the **integration of these different research areas** e.g. autonomous vehicles (CV + robotics), AI agents (NLP + CV + HCI), personalized learning (NLP + HCI), etc.

Although these fields aim to solve different problems and work with different data types, they all share a fundamental process. Namely, **generating useful numerical representations of real-world phenomena**.

Historically, this was done by hand. This means that researchers and practitioners would use their (or other people’s) expertise to explicitly transform data into a more helpful form. Today, however, _these can be derived another way_.

## **Embeddings**

**Embeddings** are **(useful) numerical representations of data learned implicitly through model training**. For example, through learning how to predict text, BERT learned representations of text, which are helpful for many NLP tasks \[1\]. Another example is the Vision Transformer (ViT), trained for image classification on Image Net, which can be repurposed for other applications \[2\].

A key point here is that these learned embedding spaces will have some underlying structure so that **similar concepts are located close together**. As shown in the toy examples below.https://towardsdatascience.com/wp-content/uploads/2024/11/1jpmC6Kx7DxVeikEr15vooA.png

One **key limitation** of the previously mentioned models is they are restricted to a single data modality, e.g., text or images. Preventing cross-modal applications like image captioning, content moderation, image search, and more. _But what if we could merge these two representations?_

## **Multimodal Embeddings**

Although text and images may look very different to us, in a neural network, these are **represented via the same mathematical object**, i.e., a vector. Therefore, in principle, text, images, or any other data modality can processed by a single model.

This fact underlies **multimodal embeddings**, which **represent multiple data modalities in the same vector space** such that similar concepts are co-located (independent of their original representations).https://towardsdatascience.com/wp-content/uploads/2024/11/15d3HBNjNIXLy0oMIvJjxWw.png

For example, CLIP encodes text and images into a shared embedding space \[3\]. A key insight from CLIP is that by aligning text and image representations, the **model is capable of 0-shot image classification on an arbitrary set of target classes** since any input text can be treated as a class label (we will see a concrete example of this later).

However, this idea is not limited to text and images. Virtually any data modalities can be aligned in this way e.g., text-audio, audio-image, text-EEG, image-tabular, and text-video. Unlocking use cases such as video captioning, advanced OCR, audio transcription, video search, and EEG-to-text \[4\].

## **Contrastive Learning**

The standard approach to aligning disparate embedding spaces is **contrastive learning (CL)**. A key intuition of CL is to **represent different views of the same _information_ similarly** \[5\].

This consists of learning representations that **maximize the similarity between positive pairs** and **minimize the similarity of negative pairs**. In the case of an image-text model, a positive pair might be an image with an appropriate caption, while a negative pair would be an image with an irrelevant caption (as shown below).https://towardsdatascience.com/wp-content/uploads/2024/11/1AGHBVjzwjXapJSe4aUPrjg.png

**Two key aspects** **of CL** contribute to its effectiveness

1.  Since positive and negative pairs can be curated from the data’s inherent structure (e.g., metadata from web images), CL training data **do not require manual labeling**, which unlocks larger-scale training and more powerful representations \[3\].
2.  It simultaneously maximizes positive and minimizes negative pair similarity via a special loss function, as demonstrated by CLIP \[3\].![CLIP's contrastive loss for text-image representation alignment [3]. Image by author.](https://towardsdatascience.com/wp-content/uploads/2024/11/12X1aT8fzFsgbqn23zXmmAA.png)

</details>

<details>
<summary>multimodal-rag-with-colpali-milvus-and-vlms</summary>

In this post, we will see how to doIn this post, we will see how to do multimodal RAG with [colpali](https://arxiv.org/abs/2407.01449), [milvus](https://milvus.io/) and a visual language model (gemini/gpt-4o).

We will build an application to upload a PDF and then do Q&A queries on it. Q&A can be done on both text and visual elements of the PDF. We will not extract text from the PDF; instead, we will treat it as an image and use colpali to get embeddings for the PDF pages. These embeddings will be indexed to Milvus, and then we will use a VLM to do Q&A queries on the PDF pages.

## Problem

Let's say a company wants to build a Q&A/search interface for its internal documents, which include PDFs, word files, wikis, images, and text files. The traditional approach involves extracting text and media, detecting layout for structure, and indexing the information in a vector store for semantic search. However, this method often falls short for complex documents containing images, tables, and graphs. Let's look at an example below:

We have a [PDF with stats on covid](https://saumitra.me/2024/covid-slides.pdf) in the form of charts and tables. We want to answer the queries below:

```markdown
1. What is the correlation between the samples tested and the positivity rate?
2. When and what was the highest number of cases and TPR?
3. Which country had the highest omicron cases?

```

These queries can be answered by using data from following 3 pages:

**Page 4: A chart showing stats on samples and positivity rate**

[https://saumitra.me/2024/covid-page-4.png](https://saumitra.me/2024/covid-page-4.png)

**Page 8: A table showing cases and TPR**

[https://saumitra.me/2024/covid-page-8.png](https://saumitra.me/2024/covid-page-8.png)

**Page 9: A table showing cases by country**

[https://saumitra.me/2024/covid-page-9.png](https://saumitra.me/2024/covid-page-9.png)

It would be difficult to extract data from these pages as text in a manner which can be used for querying.
We want to show user the answer and source page(s) from the PDF which contains the answer, like below:

[https://saumitra.me/2024/rag-demo-screenshot.png](https://saumitra.me/2024/rag-demo-screenshot.png)

Let's understand how colpali can help us here.

## Why colpali?

Document retrieval has always been a key component of systems like search engines and information retrieval. Traditional document retrieval methods rely heavily on text-based methods (like OCR and text segmentation), often missing crucial visual cues like layouts, images, and tables.

Colpali addresses this by using Vision-Language Models (VLMs) to understand and retrieve visually rich documents, capturing both textual and visual information. Colpali's architecture allows direct encoding of document images into a common embedding space, eliminating the need for time-consuming text extraction and segmentation.

## Understanding how colpali works

Colpali works in the following steps:

### Step 1: Treating the Document as an Image

Imagine we have a PDF document. Normally, we would extract text from the document using OCR (Optical Character Recognition), segment it into different sections, and then use these segments for searching. colpali simplifies this process by treating the entire document page as an image, bypassing the need for complex text extraction, layout detection, or OCR.

### Step 2: Splitting the Image into Patches

Once colpali has this "image" of the document, it divides the page into small, uniform pieces called patches. Each patch captures a tiny portion of the page. It might contain a few words, a piece of a graph, or part of an image. This division helps the model focus on the document's small, detailed parts rather than trying to understand the whole page at once.

At first glance, it might seem like dividing an image into patches is similar to breaking text into chunks. However, these two methods have several key differences, especially in how they handle and preserve context. Let’s dive deeper into these differences to understand why patch-based processing in colpali is more effective for document retrieval compared to traditional text chunking.

#### Understanding Context Loss in Text Chunking

In traditional text chunking, text is split into smaller chunks based on certain tokens since many models limit the number of tokens they can process at once.

Problem with Context Loss:

- Chunking can split sentences or paragraphs midway, causing crucial context to be lost. It can also result in incomplete information in one chunk and missing context in another.
Chunking doesn't preserve visual or structural information, such as the relationship between headings and their corresponding content or the placement of text in tables or figures.

For example, If you have a document with a heading followed by a table, text chunking might separate the heading and the table, losing the context that the table belongs to that heading.

#### Patch-Based Image Processing in colpali

Colpali divides the document image into patches, much like dividing a photo into small squares. Each patch is a fixed-size portion of the image, like a mini-snapshot of that part of the page.

Patches are more effective due to the following reasons:

- **No Loss of Structure:** The patches retain the document's visual structure, preserving its spatial layout. For instance, if a page has two columns of text or a table with rows and columns, each patch maintains its relative position, ensuring that the model understands the overall arrangement of the elements.
- **Multi-Modal Context:** Patches capture both textual and visual information. This includes both visual features (e.g., font styles, colors, boldness) and non-text elements (e.g., figures and graphs).
- **Positional Awareness:** Each patch has a positional embedding that tells the model where it is located on the page, helping the model understand the overall layout.

### Step 3: Embedding Creation and **Aligning Visual and Textual Information**

Each patch is then passed through a Vision Transformer (ViT), which converts them into unique embeddings. Next, colpali aligns these visual embeddings with the text of the query by transforming the query into its own set of embeddings. colpali uses a process called `alignment` that aligns image path embeddings and text embeddings in the same vector space. Only then can we compare the similarity between query and document embeddings.

### Step 4: Scoring the Relevance - Late Interaction Mechanism

At this point, colpali has embeddings for both the query and the document. The next challenge is to identify the relevant parts of the document. colpali uses a process called the `Late Interaction Mechanism`, where each piece of the query is finely matched against every part of the document, scoring and ranking their relevance.

Colpali highlights the most relevant pieces of the document, focusing on the patches that best match the query. This approach enables colpali to efficiently retrieve relevant information from visually rich documents, capturing both visual and textual data without losing context.

* * *

## Code

Full code at [https://github.com/saumitras/colpali-milvus-rag/](https://github.com/saumitras/colpali-milvus-rag/)

### 1\. Add colpali processor

```python
model_name = "vidore/colpali-v1.2"
device = get_torch_device("cuda")

model = colpali.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map=device,
).eval()

processor = cast(colpaliProcessor, colpaliProcessor.from_pretrained(model_name))

```

### 2\. Use colpali to get embeddings for image (pdf pages)

```python
def process_images(self, image_paths:list[str], batch_size=5):

    print(f"Processing {len(image_paths)} image_paths")

    images = self.get_images(image_paths)

    dataloader = DataLoader(
        dataset=ListDataset[str](images),
        batch_size=batch_size,
        shuffle=False,
        collate_fn=lambda x: processor.process_images(x),
    )

    ds: List[torch.Tensor] = []
    for batch_doc in tqdm(dataloader):
        with torch.no_grad():
            batch_doc = {k: v.to(model.device) for k, v in batch_doc.items()}
            embeddings_doc = model(**batch_doc)
        ds.extend(list(torch.unbind(embeddings_doc.to(device))))

    ds_np = [d.float().cpu().numpy() for d in ds]

    return ds_np

```

### 3\. Use colpali to get embeddings for text (user query)

```python
def process_text(self, texts: list[str]):
    print(f"Processing {len(texts)} texts")

    dataloader = DataLoader(
        dataset=ListDataset[str](texts),
        batch_size=1,
        shuffle=False,
        collate_fn=lambda x: processor.process_queries(x),
    )

    qs: List[torch.Tensor] = []
    for batch_query in dataloader:
        with torch.no_grad():
            batch_query = {k: v.to(model.device) for k, v in batch_query.items()}
            embeddings_query = model(**batch_query)

        qs.extend(list(torch.unbind(embeddings_query.to(device))))

    qs_np = [q.float().cpu().numpy() for q in qs]

    return qs_np

```

### 4\. Code to create collection, index and query in milvus

```python
class MilvusManager:
    def __init__(self, milvus_uri, collection_name, create_collection, dim=128):
        self.client = MilvusClient(uri=milvus_uri)
        self.collection_name = collection_name
        if self.client.has_collection(collection_name=self.collection_name):
            self.client.load_collection(collection_name)
        self.dim = dim

        if create_collection:
            self.create_collection()
            self.create_index()

    def create_collection(self):
        if self.client.has_collection(collection_name=self.collection_name):
            self.client.drop_collection(collection_name=self.collection_name)
        schema = self.client.create_schema(
            auto_id=True,
            enable_dynamic_fields=True,
        )
        schema.add_field(field_name="pk", datatype=DataType.INT64, is_primary=True)
        schema.add_field(
            field_name="vector", datatype=DataType.FLOAT_VECTOR, dim=self.dim
        )
        schema.add_field(field_name="seq_id", datatype=DataType.INT16)
        schema.add_field(field_name="doc_id", datatype=DataType.INT64)
        schema.add_field(field_name="doc", datatype=DataType.VARCHAR, max_length=65535)

        self.client.create_collection(
            collection_name=self.collection_name, schema=schema
        )

    def create_index(self):
        self.client.release_collection(collection_name=self.collection_name)
        self.client.drop_index(
            collection_name=self.collection_name, index_name="vector"
        )
        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="vector",
            index_name="vector_index",
            index_type="HNSW",
            metric_type="IP",
            params={
                "M": 16,
                "efConstruction": 500,
            },
        )

        self.client.create_index(
            collection_name=self.collection_name, index_params=index_params, sync=True
        )

    def create_scalar_index(self):
        self.client.release_collection(collection_name=self.collection_name)

        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="doc_id",
            index_name="int32_index",
            index_type="INVERTED",
        )

        self.client.create_index(
            collection_name=self.collection_name, index_params=index_params, sync=True
        )

    def search(self, data, topk):
        search_params = {"metric_type": "IP", "params": {}}
        results = self.client.search(
            self.collection_name,
            data,
            limit=int(50),
            output_fields=["vector", "seq_id", "doc_id"],
            search_params=search_params,
        )
        doc_ids = set()
        for r_id in range(len(results)):
            for r in range(len(results[r_id])):
                doc_ids.add(results[r_id][r]["entity"]["doc_id"])

        scores = []

        def rerank_single_doc(doc_id, data, client, collection_name):
            doc_colbert_vecs = client.query(
                collection_name=collection_name,
                filter=f"doc_id in [{doc_id}, {doc_id + 1}]",
                output_fields=["seq_id", "vector", "doc"],
                limit=1000,
            )
            doc_vecs = np.vstack(
                [doc_colbert_vecs[i]["vector"] for i in range(len(doc_colbert_vecs))]
            )
            score = np.dot(data, doc_vecs.T).max(1).sum()
            return (score, doc_id)

        with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
            futures = {
                executor.submit(
                    rerank_single_doc, doc_id, data, self.client, self.collection_name
                ): doc_id
                for doc_id in doc_ids
            }
            for future in concurrent.futures.as_completed(futures):
                score, doc_id = future.result()
                scores.append((score, doc_id))

        scores.sort(key=lambda x: x[0], reverse=True)
        if len(scores) >= topk:
            return scores[:topk]
        else:
            return scores

    def insert(self, data):
        colbert_vecs = [vec for vec in data["colbert_vecs"]]
        seq_length = len(colbert_vecs)
        doc_ids = [data["doc_id"] for i in range(seq_length)]
        seq_ids = list(range(seq_length))
        docs = [""] * seq_length
        docs[0] = data["filepath"]

        self.client.insert(
            self.collection_name,
            [\
                {\
                    "vector": colbert_vecs[i],\
                    "seq_id": seq_ids[i],\
                    "doc_id": doc_ids[i],\
                    "doc": docs[i],\
                }\
                for i in range(seq_length)\
            ],
        )

    def get_images_as_doc(self, images_with_vectors:list):

        images_data = []

        for i in range(len(images_with_vectors)):
            data = {
                "colbert_vecs": images_with_vectors[i]["colbert_vecs"],
                "doc_id": i,
                "filepath": images_with_vectors[i]["filepath"],
            }
            images_data.append(data)

        return images_data

    def insert_images_data(self, image_data):
        data = self.get_images_as_doc(image_data)

        for i in range(len(data)):
            self.insert(data[i])

```

### 5\. Save pdf as individual images

```python
class PdfManager:
    def __init__(self):
        pass

    def clear_and_recreate_dir(self, output_folder):
        print(f"Clearing output folder {output_folder}")

        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)

        os.makedirs(output_folder)

    def save_images(self, id, pdf_path, max_pages, pages: list[int] = None) -> list[str]:
        output_folder = f"pages/{id}/"
        images = convert_from_path(pdf_path)

        print(f"Saving images from {pdf_path} to {output_folder}. Max pages: {max_pages}")

        self.clear_and_recreate_dir(output_folder)

        num_page_processed = 0

        for i, image in enumerate(images):
            if max_pages and num_page_processed >= max_pages:
                break

            if pages and i not in pages:
                continue

            full_save_path = f"{output_folder}/page_{i + 1}.png"

            image.save(full_save_path, "PNG")

            num_page_processed += 1

        return [f"{output_folder}/page_{i + 1}.png" for i in range(num_page_processed)]

```

### 6\. Middleware to index and search Milvus for embeddings generated from colpali

```python
class Middleware:
    def __init__(self, id:str, create_collection=True):
        hashed_id = hashlib.md5(id.encode()).hexdigest()[:8]
        milvus_db_name = f"milvus_{hashed_id}.db"
        self.milvus_manager = MilvusManager(milvus_db_name, "colpali", create_collection)

    def index(self, pdf_path: str, id:str, max_pages: int, pages: list[int] = None):

        print(f"Indexing {pdf_path}, id: {id}, max_pages: {max_pages}")

        image_paths = pdf_manager.save_images(id, pdf_path, max_pages)

        print(f"Saved {len(image_paths)} images")

        colbert_vecs = colpali_manager.process_images(image_paths)

        images_data = [{\
            "colbert_vecs": colbert_vecs[i],\
            "filepath": image_paths[i]\
        } for i in range(len(image_paths))]

        print(f"Inserting {len(images_data)} images data to Milvus")

        self.milvus_manager.insert_images_data(images_data)

        print("Indexing completed")

        return image_paths


    def search(self, search_queries: list[str]):
        print(f"Searching for {len(search_queries)} queries")

        final_res = []

        for query in search_queries:
            print(f"Searching for query: {query}")
            query_vec = colpali_manager.process_text([query])[0]
            search_res = self.milvus_manager.search(query_vec, topk=1)
            print(f"Search result: {search_res} for query: {query}")
            final_res.append(search_res)

        return final_res

```

### 7\. Use Gemini or gpt-4o to do Q&A on pdf page(s) matching user query

```python
class Rag:

    def get_answer_from_gemini(self, query, imagePaths):

        print(f"Querying Gemini for query={query}, imagePaths={imagePaths}")

        try:
            genai.configure(api_key=os.environ['GEMINI_API_KEY'])
            model = genai.GenerativeModel('gemini-1.5-flash')

            images = [Image.open(path) for path in imagePaths]

            chat = model.start_chat()

            response = chat.send_message([*images, query])

            answer = response.text

            print(answer)

            return answer

        except Exception as e:
            print(f"An error occurred while querying Gemini: {e}")
            return f"Error: {str(e)}"


    def get_answer_from_openai(self, query, imagesPaths):
        print(f"Querying OpenAI for query={query}, imagesPaths={imagesPaths}")

        try:
            payload = self.__get_openai_api_payload(query, imagesPaths)

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
            }

            response = requests.post(
                url="https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            )
            response.raise_for_status()  # Raise an HTTPError for bad responses

            answer = response.json()["choices"][0]["message"]["content"]

            print(answer)

            return answer

        except Exception as e:
            print(f"An error occurred while querying OpenAI: {e}")
            return None

    def __get_openai_api_payload(self, query:str, imagesPaths:List[str]):
        image_payload = []

        for imagePath in imagesPaths:
            base64_image = encode_image(imagePath)
            image_payload.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })

        payload = {
            "model": "gpt-4o",
            "messages": [\
                {\
                    "role": "user",\
                    "content": [\
                        {\
                            "type": "text",\
                            "text": query\
                        },\
                        *image_payload\
                    ]\
                }\
            ],
            "max_tokens": 1024
        }

        return payload


```

In the next post, we will understand the limitations of colpali and a workaround for them.

## References

1. [https://milvus.io/docs/use\_colpali\_with\_milvus.md](https://milvus.io/docs/use_colpali_with_milvus.md)
2. [https://arxiv.org/abs/2407.01449](https://arxiv.org/abs/2407.01449)

</details>

<details>
<summary>scraping-failed</summary>

⚠️ Error scraping https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/: Request Timeout: Failed to scrape URL as the request timed out. Request timed out - No additional error details provided.

</details>

<details>
<summary>start-with-a-prebuilt-agent</summary>

This guide shows you how to set up and use LangGraph's **prebuilt**, **reusable** components, which are designed to help you construct agentic systems quickly and reliably.

## Prerequisites

Before you start this tutorial, ensure you have the following:

- An [Anthropic](https://console.anthropic.com/settings/keys) API key

## 1\. Install dependencies

If you haven't already, install LangGraph and LangChain:

```md-code__content
pip install -U langgraph "langchain[anthropic]"

```

Info

LangChain is installed so the agent can call the [model](https://python.langchain.com/docs/integrations/chat/).

## 2\. Create an agent

To create an agent, use [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.chat_agent_executor.create_react_agent "<code class=\"doc-symbol doc-symbol-heading doc-symbol-function\"></code>            <span class=\"doc doc-object-name doc-function-name\">create_react_agent</span>"):

_API Reference: [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)_

```md-code__content
from langgraph.prebuilt import create_react_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    prompt="You are a helpful assistant"
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

```

## 3\. Configure an LLM

To configure an LLM with specific parameters, such as temperature, use [init\_chat\_model](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html):

_API Reference: [init\_chat\_model](https://python.langchain.com/api_reference/langchain/chat_models/langchain.chat_models.base.init_chat_model.html) \| [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)_

```md-code__content
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent

model = init_chat_model(
    "anthropic:claude-3-7-sonnet-latest",
    temperature=0
)

agent = create_react_agent(
    model=model,
    tools=[get_weather],
)

```

For more information on how to configure LLMs, see [Models](https://langchain-ai.github.io/langgraph/agents/models/).

## 4\. Add a custom prompt

Prompts instruct the LLM how to behave. Add one of the following types of prompts:

- **Static**: A string is interpreted as a **system message**.
- **Dynamic**: A list of messages generated at **runtime**, based on input or configuration.

[Static prompt](https://langchain-ai.github.io/langgraph/agents/agents/#__tabbed_1_1)[Dynamic prompt](https://langchain-ai.github.io/langgraph/agents/agents/#__tabbed_1_2)

Define a fixed prompt string or list of messages:

```md-code__content
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    # A static prompt that never changes
    prompt="Never answer questions about the weather."
)

agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

```

Define a function that returns a message list based on the agent's state and configuration:

```md-code__content
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt.chat_agent_executor import AgentState
from langgraph.prebuilt import create_react_agent

def prompt(state: AgentState, config: RunnableConfig) -> list[AnyMessage]:
    user_name = config["configurable"].get("user_name")
    system_msg = f"You are a helpful assistant. Address the user as {user_name}."
    return [{"role": "system", "content": system_msg}] + state["messages"]

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    prompt=prompt
)

agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    config={"configurable": {"user_name": "John Smith"}}
)

```

For more information, see [Context](https://langchain-ai.github.io/langgraph/agents/context/).

## 5\. Add memory

To allow multi-turn conversations with an agent, you need to enable [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) by providing a `checkpointer` when creating an agent. At runtime, you need to provide a config containing `thread_id` — a unique identifier for the conversation (session):

_API Reference: [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) \| [InMemorySaver](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver)_

```md-code__content
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    checkpointer=checkpointer
)

# Run the agent
config = {"configurable": {"thread_id": "1"}}
sf_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    config
)
ny_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what about new york?"}]},
    config
)

```

When you enable the checkpointer, it stores agent state at every step in the provided checkpointer database (or in memory, if using `InMemorySaver`).

Note that in the above example, when the agent is invoked the second time with the same `thread_id`, the original message history from the first conversation is automatically included, together with the new user input.

For more information, see [Memory](https://langchain-ai.github.io/langgraph/how-tos/memory/add-memory/).

## 6\. Configure structured output

To produce structured responses conforming to a schema, use the `response_format` parameter. The schema can be defined with a `Pydantic` model or `TypedDict`. The result will be accessible via the `structured_response` field.

_API Reference: [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)_

```md-code__content
from pydantic import BaseModel
from langgraph.prebuilt import create_react_agent

class WeatherResponse(BaseModel):
    conditions: str

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather],
    response_format=WeatherResponse
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

response["structured_response"]

```

LLM post-processing

Structured output requires an additional call to the LLM to format the response according to the schema.

</details>

<details>
<summary>the-8-best-ai-image-generators-in-2025-zapier</summary>

Most AI image generators work in a pretty similar way. [Millions or billions](https://laion.ai/blog/laion-5b/) of image-text pairs are used to train a neural network (basically, a very fancy computer algorithm [modeled loosely on the human brain](https://news.mit.edu/2017/explained-neural-networks-deep-learning-0414)) on _what things are_. By allowing it to process near-countless images, it learns what dogs, the color red, Vermeers, and everything else are. Once this is done, you have an AI that can interpret almost any prompt—though [there is a skill in setting things up](https://zapier.com/blog/ai-art-prompts/) so it can do so accurately.

The next step is to actually render the AI-generated image. The latest generation of AI image generators typically uses a [process called diffusion](https://www.assemblyai.com/blog/diffusion-models-for-machine-learning-introduction/)—though OpenAI's latest foray into image generation uses a slightly different [process called autoregression](https://arxiv.org/abs/2404.02905). In essence, the image generators start with a random field of noise and then edit it in a series of steps to match their interpretation of the prompt. It's kind of like looking up at a cloudy sky, finding a cloud that looks kind of like a dog, and then being able to snap your fingers to keep making it more and more dog-like.

</details>

<details>
<summary>understanding-multimodal-llms-by-sebastian-raschka-phd</summary>

As hinted at in the introduction, multimodal LLMs are large language models capable of processing multiple types of inputs, where each "modality" refers to a specific type of data—such as text (like in traditional LLMs), sound, images, videos, and more. For simplicity, we will primarily focus on the image modality alongside text inputs.

A classic and intuitive application of multimodal LLMs is image captioning: you provide an input image, and the model generates a description of the image, as shown in the figure below.

[https://substackcdn.com/image/fetch/$s_!8kaL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93884822-79f1-498d-a33a-8a367ba57134_1500x1222.png](https://substackcdn.com/image/fetch/$s_!8kaL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93884822-79f1-498d-a33a-8a367ba57134_1500x1222.png) _Example use of a multimodal LLM explaining [a meme](https://x.com/PainSci/status/1309570607458086914)._

Of course, there are many other use cases. For example, one of my favorites is extracting information from a PDF table and converting it into LaTeX or Markdown.

# 2. Common approaches to building multimodal LLMs

There are two main approaches to building multimodal LLMs:

- Method A: Unified Embedding Decoder Architecture approach;

- Method B: Cross-modality Attention Architecture approach.

[https://substackcdn.com/image/fetch/$s_!8miE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53956ae8-9cd8-474e-8c10-ef6bddb88164_1600x938.png](https://substackcdn.com/image/fetch/$s_!8miE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53956ae8-9cd8-474e-8c10-ef6bddb88164_1600x938.png) _The two main approaches to developing multimodal LLM architectures._

As shown in the figure above, the _**Unified Embedding-Decoder Architecture**_ utilizes a single decoder model, much like an unmodified LLM architecture such as GPT-2 or Llama 3.2. In this approach, images are converted into tokens with the same embedding size as the original text tokens, allowing the LLM to process both text and image input tokens together after concatenation.

The _**Cross-Modality Attention Architecture**_ employs a cross-attention mechanism to integrate image and text embeddings directly within the attention layer.

In the following sections, we will explore how these methods work on a conceptual level. Then, we will look at recent research papers on multimodal LLMs to see how they are applied in practice.

## **2.1 Method A: Unified Embedding Decoder Architecture**

Let’s begin with the unified embedding decoder architecture, illustrated again in the figure below.

[https://substackcdn.com/image/fetch/$s_!Ws6n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91955021-7da5-4bc4-840e-87d080152b18_1166x1400.png](https://substackcdn.com/image/fetch/$s_!Ws6n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91955021-7da5-4bc4-840e-87d080152b18_1166x1400.png) _Illustration of the unified embedding decoder architecture, which is an unmodified decoder-style LLM (like GPT-2, Phi-3, Gemma, or Llama 3.2) that receives inputs consisting of image token and text token embeddings._

In the unified embedding-decoder architecture, an image is converted into embedding vectors, similar to how input text is converted into embeddings in a standard text-only LLM.

For a typical text-only LLM that processes text, the text input is usually tokenized (e.g., using Byte-Pair Encoding) and then passed through an embedding layer, as shown in the figure below.

[https://substackcdn.com/image/fetch/$s_!dOba!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97009dd-cee6-455f-87fe-64c33a868e9f_986x858.png](https://substackcdn.com/image/fetch/$s_!dOba!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97009dd-cee6-455f-87fe-64c33a868e9f_986x858.png) _Illustration of the standard process for tokenizing text and converting it into token embedding vectors, which are subsequently passed to an LLM during training and inference._

### **2.1.1 Understanding Image encoders**

Analogous to the tokenization and embedding of text, image embeddings are generated using an image encoder module (instead of a tokenizer), as shown in the figure below.

[https://substackcdn.com/image/fetch/$s_!PlBh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15e9cc2f-95de-4723-9de5-9f2af7573aaa_790x750.png](https://substackcdn.com/image/fetch/$s_!PlBh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15e9cc2f-95de-4723-9de5-9f2af7573aaa_790x750.png) _Illustration of the process for encoding an image into image patch embeddings._

What happens inside the image encoder shown above? To process an image, we first divide it into smaller patches, much like breaking words into subwords during tokenization. These patches are then encoded by a pretrained vision transformer (ViT), as shown in the figure below.

[https://substackcdn.com/image/fetch/$s_!_DNf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffef5f8cb-c76c-4c97-9771-7fdb87d7d8cd_1600x1135.png](https://substackcdn.com/image/fetch/$s_!_DNf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffef5f8cb-c76c-4c97-9771-7fdb87d7d8cd_1600x1135.png) _Illustration of a classic vision transformer (ViT) setup, similar to the model proposed in [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) (2020)._

Note that ViTs are often used for classification tasks, so I included the classification head in the figure above. However, in this case, we only need the image encoder part.

### **2.1.2 The role of the linear projection module**

The "linear projection" shown in the previous figure consists of a single linear layer (i.e., a fully connected layer). The purpose of this layer is to project the image patches, which are flattened into a vector, into an embedding size compatible with the transformer encoder. This linear projection is illustrated in the figure below. An image patch, flattened into a 256-dimensional vector, is up-projected to a 768-dimensional vector.

[https://substackcdn.com/image/fetch/$s_!i9i4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee32d720-92d7-48c2-b39d-adf61a870075_1600x681.png](https://substackcdn.com/image/fetch/$s_!i9i4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee32d720-92d7-48c2-b39d-adf61a870075_1600x681.png) _Illustration of a linear projection layer that projects flattened image patches from a 256-dimensional into a 768-dimensional embedding space._

### **2.1.3 Image vs text tokenization**

Now that we briefly discussed the purpose of the image encoder (and the linear projection that is part of the encoder), let's return to the text tokenization analogy from earlier and look at text and image tokenization and embedding side by side, as depicted in the figure below.

[https://substackcdn.com/image/fetch/$s_!zjmg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d56ea06-d202-4eb7-9e01-9aac492ee309_1522x1206.png](https://substackcdn.com/image/fetch/$s_!zjmg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d56ea06-d202-4eb7-9e01-9aac492ee309_1522x1206.png) _Image tokenization and embedding (left) and text tokenization and embedding (right) side by side._

As you can see in the figure above, I included an additional _**projector**_ module that follows the image encoder. This _projector_ is usually just another _**linear projection**_ layer that is similar to the one explained earlier. The purpose is to project the image encoder outputs into a dimension that matches the dimensions of the embedded text tokens, as illustrated in the figure below. (As we will see later, the projector is sometimes also called adapter, adaptor, or connector.)

[https://substackcdn.com/image/fetch/$s_!TaTW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0be64c-da90-4193-86db-804f6a8a0abb_1542x1242.png](https://substackcdn.com/image/fetch/$s_!TaTW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0be64c-da90-4193-86db-804f6a8a0abb_1542x1242.png) _Another side-by-side comparison between image tokenization and text tokenization, where the role of the projector is to match the text token embedding dimensions._

Now that the image patch embeddings have the same embedding dimension as the text token embeddings, we can simply concatenate them as input to the LLM, as shown in the figure at the beginning of this section. Below is the same figure again for easier reference.

[https://substackcdn.com/image/fetch/$s_!FTft!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa219f185-211b-4569-9398-2e080e2c5619_1166x1400.png](https://substackcdn.com/image/fetch/$s_!FTft!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa219f185-211b-4569-9398-2e080e2c5619_1166x1400.png) _After projecting the image patch tokens into the same dimension as the text token embeddings, we can simply concatenate them as input to a standard LLM._

By the way, the image encoder we discussed in this section is usually a pretrained vision transformer. A popular choice is [CLIP](https://github.com/openai/CLIP) or [OpenCLIP](https://github.com/mlfoundations/open_clip).

However, there are also versions of Method A that operate directly on patches, such as [Fuyu](https://www.adept.ai/blog/fuyu-8b), which is shown in the figure below.

[https://substackcdn.com/image/fetch/$s_!LB1L!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28269d0d-b806-4ae7-bf96-b282affd7e93_1600x645.png](https://substackcdn.com/image/fetch/$s_!LB1L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28269d0d-b806-4ae7-bf96-b282affd7e93_1600x645.png) _Annotated figure of the Fuyu multimodal LLM that operates directly on the image patches without image encoder. (Annotated figure from [https://www.adept.ai/blog/fuyu-8b](https://www.adept.ai/blog/fuyu-8b).)_

As illustrated in the figure above, Fuyu passes the input patches directly into a linear projection (or embedding layer) to learn its own image patch embeddings rather than relying on an additional pretrained image encoder like other models and methods do. This greatly simplifies the architecture and training setup.

## **2.2 Method B: Cross-Modality Attention Architecture**

Now that we have discussed the unified embedding decoder architecture approach to building multimodal LLMs and understand the basic concept behind image encoding, let's talk about an alternative way of implementing multimodal LLMs via cross-attention, as summarized in the figure below.

[https://substackcdn.com/image/fetch/$s_!7Xvv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9c06055-b959-45d1-87b2-1f4e90ceaf2d_1296x1338.png](https://substackcdn.com/image/fetch/$s_!7Xvv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9c06055-b959-45d1-87b2-1f4e90ceaf2d_1296x1338.png) _An illustration of the Cross-Modality Attention Architecture approach to building multimodal LLMs._

In the Cross-Modality Attention Architecture method depicted in the figure above, we still use the same image encoder setup we discussed previously. However, instead of encoding the patches as input to the LLM, we connect the input patches in the multi-head attention layer via a cross-attention mechanism.

The idea is related and goes back to the original transformer architecture from the 2017 [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper, highlighted in the figure below.

[https://substackcdn.com/image/fetch/$s_!JYyE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d028b95-7965-43e0-b8fc-350609a69377_1370x1582.png](https://substackcdn.com/image/fetch/$s_!JYyE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d028b95-7965-43e0-b8fc-350609a69377_1370x1582.png) _High-level illustration of the cross-attention mechanism used in the original transformer architecture. (Annotated figure from the "Attention Is All You Need" paper: https://arxiv.org/abs/1706.03762.)_

Note that the original "Attention Is All You Need" transformer depicted in the figure above was originally developed for language translation. So, it consists of a text **en** coder (left part of the figure) that takes the sentence to be translated and generates the translation via a text **de** coder (right part of the figure). In the context of multimodal LLM, the encoder is an image encoder instead of a text encoder, but the same idea applies.

How does cross-attention work? Let's have a look at a conceptual drawing of what happens inside the regular self-attention mechanism.

[https://substackcdn.com/image/fetch/$s_!HqoQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff763532b-1eed-4f7d-ae2c-7783d4f4fc46_1440x1194.png](https://substackcdn.com/image/fetch/$s_!HqoQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff763532b-1eed-4f7d-ae2c-7783d4f4fc46_1440x1194.png) _Outline of the regular self-attention mechanism. (This flow depicts one of the heads in a regular multi-head attention module.)_

In the figure above, x is the input, and _Wq_ is a weight matrix used to generate the queries ( _Q_). Similarly, _K_ stands for keys, and _V_ stands for values. A represents the attention scores matrix, and _Z_ are the inputs (x) transformed into the output context vectors.

In cross-attention, in contrast to self-attention, we have two different input sources, as illustrated in the following figure.

[https://substackcdn.com/image/fetch/$s_!3PZD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe4cc6f4-ca9a-431b-b572-95a1fda373a7_1508x1120.png](https://substackcdn.com/image/fetch/$s_!3PZD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe4cc6f4-ca9a-431b-b572-95a1fda373a7_1508x1120.png) _Illustration of cross attention, where there can be two different inputs x1 and x2_

As illustrated in the previous two figures, in self-attention, we work with the same input sequence. In cross-attention, we mix or combine two different input sequences.

In the case of the original transformer architecture in the _Attention Is All You Need_ paper, the two inputs _x1_ and _x2_ correspond to the sequence returned by the encoder module on the left ( _x2_) and the input sequence being processed by the decoder part on the right ( _x1_). In the context of a multimodal LLM, _x2_ is the output of an image encoder. (Note that the queries usually come from the decoder, and the keys and values typically come from the encoder.)

Note that in cross-attention, the two input sequences _x1_ and _x2_ can have different numbers of elements. However, their embedding dimensions must match. If we set _x1 = x2_, this is equivalent to self-attention.

# 3. Unified decoder and cross-attention model training

Now that we have talked a bit about the two major multimodal design choices, let's briefly talk about how we deal with the three major components during model training, which are summarized in the figure below.

[https://substackcdn.com/image/fetch/$s_!e2P-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24a12032-d32e-41f6-b390-4e321e1ea29f_1600x770.png](https://substackcdn.com/image/fetch/$s_!e2P-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24a12032-d32e-41f6-b390-4e321e1ea29f_1600x770.png) _An overview of the different components in a multimodal LLM. The components numbered 1-3 can be frozen or unfrozen during the multimodal training process._

Similar to the development of traditional text-only LLMs, the training of multimodal LLMs also involves two phases: pretraining and instruction finetuning. However, unlike starting from scratch, multimodal LLM training typically begins with a pretrained, instruction-finetuned text-only LLM as the base model.

For the image encoder, CLIP is commonly used and often remains unchanged during the entire training process, though there are exceptions, as we will explore later. Keeping the LLM part frozen during the pretraining phase is also usual, focusing only on training the projector—a linear layer or a small multi-layer perceptron. Given the projector's limited learning capacity, usually comprising just one or two layers, the LLM is often unfrozen during multimodal instruction finetuning (stage 2) to allow for more comprehensive updates. However, note that in the cross-attention-based models (Method B), the cross-attention layers are unfrozen throughout the entire training process.

After introducing the two primary approaches (Method A: Unified Embedding Decoder Architecture and Method B: Cross-modality Attention Architecture), you might be wondering which is more effective. The answer depends on specific trade-offs.

The Unified Embedding Decoder Architecture (Method A) is typically easier to implement since it doesn't require any modifications to the LLM architecture itself.

The Cross-modality Attention Architecture (Method B) is often considered more computationally efficient because it doesn't overload the input context with additional image tokens, introducing them later in the cross-attention layers instead. Additionally, this approach maintains the text-only performance of the original LLM if the LLM parameters are kept frozen during training.

</details>

<details>
<summary>what-are-some-real-world-applications-of-multimodal-ai</summary>

# What are some real-world applications of multimodal AI?

Multimodal AI, which processes and combines different data types like text, images, audio, and sensor inputs, has practical applications across industries. By integrating multiple data sources, these systems improve accuracy and functionality in tasks that require contextual understanding. Below are three key areas where multimodal AI is being applied effectively today.

In healthcare, multimodal AI enhances diagnostics and patient care by merging medical imaging, electronic health records (EHRs), and sensor data. For example, a system might analyze a chest X-ray (image), a patient’s symptom descriptions (text), and vital signs from wearables (sensor data) to detect pneumonia. Models like Google’s **Med-PaLM 2** combine vision and language processing to interpret radiology images alongside clinical notes, reducing misdiagnosis risks. Another use case is monitoring postoperative recovery: wearable devices track movement and heart rate, while speech analysis detects pain or fatigue in a patient’s voice, enabling proactive interventions.

Autonomous vehicles rely heavily on multimodal AI to fuse data from cameras, LiDAR, radar, and GPS. A self-driving car processes road signs (visual data), pedestrian movements (video), and proximity sensor readings to navigate safely. Tesla’s Autopilot, for instance, uses neural networks to combine camera feeds with ultrasonic sensors, improving object detection in varied lighting or weather. Similarly, companies like Waymo train models to correlate map data with real-time sensor inputs, ensuring precise localization and path planning. This redundancy across modalities helps address limitations of single-sensor systems, such as camera failures in low light.

Customer service and content moderation also benefit from multimodal approaches. Virtual assistants like Amazon’s Alexa process voice commands while analyzing user history (text) to personalize responses. In moderation, platforms like YouTube use AI to flag harmful content by scanning video frames (images), audio for hate speech, and user comments (text) simultaneously. For example, a post containing violent imagery and threatening text would be detected faster than if each modality were analyzed separately. Tools like **OpenAI’s CLIP** enable cross-modal matching, such as linking inappropriate images to their descriptive captions, improving accuracy in filtering violations. These systems reduce reliance on manual review while scaling to handle large data volumes.

</details>

<details>
<summary>what-are-vision-language-models-nvidia-glossary</summary>

# Vision Language Models

Vision language models (VLMs) are multimodal, generative AI models capable of understanding and processing video, image, and text.

## What Are Vision Language Models?

Vision language models are multimodal AI systems built by combining a large language model (LLM) with a vision encoder, giving the LLM the ability to “see.”

With this ability, VLMs can process and provide advanced understanding of video, image, and text inputs supplied in the prompt to generate text responses.https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy/nv_image.coreimg.100.1290.png/1736201901571/metropolis-iva-diagram-vlm-glossary-ces25-3576177-r1--1-.png

Figure 1: Use cases for vision language models

Unlike traditional [computer vision](https://www.nvidia.com/en-us/glossary/computer-vision/) models, VLMs are not bound by a fixed set of classes or a specific task like classification or detection. Retrained on a vast corpus of text and image/video-caption pairs, VLMs can be instructed in natural language and used to handle many classic vision tasks plus new generative AI-powered tasks such as summarization and visual Q&A.

## Why Are Vision Language Models Important?

To understand the importance of VLMs, it’s helpful to know how past computer vision (CV) models work. Traditional convolutional neural network ( [CNN](https://www.nvidia.com/en-us/glossary/convolutional-neural-network/))-based CV models are trained for a specific task on a bounded set of classes. For example:

- A classification model that identifies whether an image contains a cat or a dog
- An optical character detection and recognition CV model that reads text in an image but doesn’t interpret the format or any visual data within a document

Previous CV models were trained for a specific purpose and did not have the ability to go beyond the task or set of classes they were developed for and trained on. If the use case changed at all or required a new class to be added to the model, a developer would have to collect and label a large number of images and retrain the model. This is an expensive, time-consuming process. Additionally, CV models don't have any natural language understanding.

VLMs bring a new class of capabilities by combining the power of foundation models, like [CLIP](https://github.com/openai/CLIP), and LLMs to have both vision and language capabilities. Out of the box, VLMs have strong zero-shot performance on a variety of vision tasks, like visual question-answering, classification, and optical character recognition. They are also extremely flexible and can be used not just on a fixed set of classes but for nearly any use case by simply changing a text prompt.

Using a VLM is very similar to interacting with an LLM. The user supplies text prompts that can be interleaved with images. The inputs are then used to generate text output. The input prompts are open-ended, allowing the user to instruct the VLM to answer questions, summarize, explain the content, or reason with the image. Users can chat back and forth with the VLM, with the ability to add images into the context of the conversation. VLMs can also be integrated into visual agents to autonomously perform vision tasks.

## How Do Vision Language Models Work?

Most VLMs follow an architecture with three parts:

- A vision encoder
- A projector
- An LLM

The vision encoder is typically a CLIP-based model with a transformer architecture that has been trained on millions of image-text pairs, giving it the ability to associate images and text. The projector is a set of layers that translates the output of the vision encoder into a form the LLM can understand, often interpreted as image tokens. This projector can be a simple line layer like LLaVA and VILA, or something more complex like the cross-attention layers used in Llama 3.2 Vision.

Any off-the-shelf LLM can be used to build a VLM. There are hundreds of VLM variants that combine various LLMs with vision encoders.https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy_co_300503066/nv_image.coreimg.svg/1736168815674/vlm-architecture-diagram.svg

Figure 2: A common three-part architecture for vision language models

## How Are Vision Language Models Trained?

VLMs are trained in several stages that include pretraining, followed by supervised fine-tuning. Optionally, parameter efficient fine-tuning (PEFT) can be applied as a final stage to create a domain-specific VLM on custom data.

The pretraining stage aligns the vision encoder, projector, and LLM to essentially speak the same language when interpreting the text and image input. This is done using large corpora of text and images with image-caption pairs and interleaved image-text data. Once the three components have been aligned through pretraining, the VLM goes through a supervised fine-tuning stage to help it understand how to respond to user prompts.

The data used in this stage are a blend of example prompts with text and/or image input and the expected response of the model. For example, this data could be prompts telling the model to describe the image or to count all the objects in the frame with the expected correct response. After this round of training, the VLM will understand how to best interpret images and respond to user prompts.https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy_co_1755415045/nv_image.coreimg.svg/1736168816034/vlm-training-process-diagram.svg

Figure 3: Training for VLMs is often done in several stages to target certain parts of the model

Once the VLM is trained, it can be used in the same way as an LLM by providing prompts that can also include images interleaved in text. The VLM will then generate a text response based on the inputs. VLMs are typically deployed with an OpenAI style REST API interface to make it easy to interact with the model.

More advanced techniques are currently being researched to enhance vision capabilities:

- Ensembling vision encoders to process image inputs
- Breaking apart high-resolution image inputs into smaller tiles for processing
- Increasing context length to improve long video understanding

All of these advancements are progressing the capabilities of VLMs from only understanding single-image input to being highly capable models that can compare and contrast images, accurately read text, understand long videos, and have strong spatial understanding.

## How Are Vision Language Models Benchmarked?

Several common benchmarks, such [MMMU](https://mmmu-benchmark.github.io/), [Video-MME](https://video-mme.github.io/home_page.html), [MathVista](https://mathvista.github.io/), [ChartQA](https://github.com/vis-nlp/ChartQA) , and [DocVQA](https://www.docvqa.org/), exist to determine how well vision-language models perform on a variety of tasks, such as:

- Visual question-answering
- Logic and reasoning
- Document understanding
- Multi-image comparisons
- Video understanding

Most benchmarks consist of a set of images with several associated questions, often posed as multiple-choice questions. The multiple-choice format is the easiest way to consistently benchmark and compare VLMs. These questions test the VLMs perception, knowledge, and reasoning capabilities. When running these benchmarks, the VLM is provided with the image, question, and several multiple-choice answers it must choose from.https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy_co_42410027/nv_image.coreimg.100.1290.jpeg/1736168816436/vlm-mmmu-ari.jpeg

Figure 4: Example multiple-choice questions for VLMs used in the MMMU benchmark

Source ( [MMMU](https://mmmu-benchmark.github.io/))

The accuracy of the VLM is the number of correct choices over the set of multiple-choice questions. Some benchmarks also include numerical questions where the VLM must perform a specific calculation and be within a certain percentage of the answer to be considered correct. Often these questions and images come from academic sources, such as college-level textbooks.

## How Are Vision Language Models Used?

VLMs are quickly becoming the go-to tool for all types of vision-related tasks due to their flexibility and natural language understanding. VLMs can be easily instructed to perform a wide variety of tasks through natural language:

1. Visual questions-answering
2. Image and video summarization
3. Parsing text and handwritten documents

Previous applications that would have required a large ensemble of specially trained models can now be accomplished with just a single VLM.

VLMs are especially good at summarizing the contents of images and can be prompted to perform specific tasks based on the contents. Take for example, an education use case—a VLM could be given an image of a handwritten math problem, and it could use its optical character recognition and reasoning capabilities to interpret the problem and produce a step-by-step guide on how to solve it. VLMs can not only understand the content of the image but also reason and perform specific tasks.https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy_co_531349501/nv_image.coreimg.svg/1736168816834/vlm-real-world-diagram.svg

Figure 5: video analytics AI agents transform video and image data into real-world insights

With vast amounts of video being produced every day, it's infeasible to review and extract insights from this volume of video that is produced by all industries. VLMs can be integrated into a larger system to build video analytics AI agents capable of detecting specific events when prompted. These systems could be used to detect malfunctioning robots in a warehouse or generate out-of-stock alerts when shelves are empty. Their general understanding goes beyond simple detection and could be used to generate automated reports. For example, an intelligent traffic system could detect, analyze, and produce reports of traffic hazards, such as fallen trees, stalled vehicles, or collisions.

VLMs can be used with technologies like graph databases to understand long videos. This helps them capture the complexity of objects and events in a video. Such systems could be used to summarize operations in a warehouse to find bottlenecks and inefficiencies or produce sports commentary for football, basketball, or soccer games.

## What Are the Challenges of Vision Language Models?

Vision language models are maturing quickly, but they still have some limitations, particularly around spatial understanding and long-context video understanding.

Most VLMs use CLIP-based models as the vision encoder, which are limited to 224x224 or 336x336 image input size. This relatively small input image makes it difficult for small objects and details to be detected. For example, an HD 1080x1920 frame from a video must be downsized or cropped to a much smaller input resolution, making it difficult to retain details for small objects or fine details. To fix this, VLMs are starting to use tiling methods that allow a big image to be broken into smaller pieces and then fed into the model. There's also ongoing research to explore the use of higher-resolution image encoders.

VLMs also have difficulty providing precise locations for objects. The training data for CLIP-based vision encoders consists mostly of short text descriptions of images, like captions. These descriptions don't include detailed, fine-grained object locations, and this limitation impacts CLIP’s spatial understanding. This is inherited by VLMs that use it as a vision encoder. New approaches are exploring the use of ensembling several vision encoders to address these limitations [2408.15998 (arxiv.org)](https://arxiv.org/pdf/2408.15998).

Long video understanding is a challenge due to the need to take into account visual information across potential hours of video to properly analyze or answer questions. Like LLMs, VLMs have limited context length meaning—only a certain number of frames from a video can be included to answer questions. Approaches to increase context length and train VLMs on more video-based data are being researched, such as LongVILA [2408.10188 (arxiv.org)](https://www.arxiv.org/pdf/2408.10188).

VLMs may not have seen enough data for very specific use cases, such as finding manufacturing defects in a specific product line. This limitation can be overcome by fine-tuning the VLM on domain-specific data or using multi-image VLMs with in-context learning to provide examples that can teach the model new information without explicitly training the model. Training the model on domain-specific data with PEFT is another technique that can be used to improve a VLM’s accuracy on custom data.

</details>

<details>
<summary>what-is-optical-character-recognition-ocr-explained</summary>

Have you ever wondered how a computer can understand the words on a photo, just like you do?  That's where Optical Character Recognition, or [OCR](https://roboflow.com/ocr?ref=blog.roboflow.com), steps in. OCR takes the text you see in images – be it from a book, a receipt, or an old letter – and turns it into something your computer can read, edit, and search.

OCR finds widespread applications in tasks such as automated data entry, document digitization, text extraction from images, invoice processing, form recognition, and enhancing accessibility for visually impaired individuals.

Let's explore the fundamentals of OCR, understanding its workings, the challenges it addresses, and why it remains a crucial component of present and future technology.

## What Is Optical Character Recognition?

Optical Character Recognition (OCR) involves converting both handwritten and typed text from various sources, including images, videos, and scanned documents like PDFs, into a digitally editable format.

The output from OCR can be used by a computer to make decisions. Common use cases of OCR include:

Using OCR to read product identifiers on an assembly line. When each identifier is read, a piece of software can update an inventory tracking system to note the package with the given identifier has arrived.

Using OCR for scanned document recognition. This involves scanning printed documents, after which OCR software converts them into searchable and editable text. This method is widely employed to automate the handling of legal documents, extract data from bank statements and invoices, and streamline tasks like invoice processing and financial record-keeping.

Using OCR for “scene text recognition”, wherein an OCR system recognizes text from natural scenes, such as street signs, storefronts, or license plates.

Using OCR for alphanumeric, printed text, such as text that was written on a typewriter, or text that was printed out. But, you can also use OCR on handwriting. This usually involves using a separate system due to the differences in handwriting compared to printed text.https://blog.roboflow.com/content/images/2024/04/image-733.webp_Application of OCR on the text of a book._ [_Source_](https://www.edenai.co/post/optical-character-recognition-ocr-which-solution-to-choose?ref=blog.roboflow.com).

## How Optical Character Recognition Works

Let's discuss the typical steps modern OCR software uses to read text:

1. **Image pre-processing**: After an image has been collected, the image undergoes pre-processing to enhance image quality, improving recognition. Pre-processing may involve resizing, contrast enhancement, binarization, noise reduction, and other techniques.
2. **Text Detection**: Using a specialized deep-learning model trained on large datasets of images and text, the computer vision model detects regions in the input image that likely contain text. This process is usually a crucial step.
3. **Layout Analysis**: After detecting text regions, the computer vision model conducts layout analysis to determine the structure and order of the text in the image. This step ensures the preservation of context and organizes the output for readability, but is not run by all OCR systems.
4. **Text Recognition**: Detected text regions pass through a deep learning-based text recognition model, utilizing a combination of convolutional neural networks (CNNs) and recurrent neural networks (RNNs). This model recognizes individual characters and words in the input image, converting them into machine-readable text.
5. **Language Model**: The final output undergoes post-processing to remove noise, correct spelling mistakes, and enhance overall accuracy. The predicted sequence of characters may contain errors, especially for long or uncommon words. Language models, acting as word processors, refine the output by predicting the probability of a sequence of words based on the input image. Statistical models and advanced methods, including deep learning, may be employed for this purpose.https://blog.roboflow.com/content/images/2024/04/image-738.webp_An example OCR system pipeline._

Having acquired an understanding of how OCR operates, let's examine its algorithms and investigate their operational mechanisms, covering the old and the new.

## Traditional Approaches to OCR

The first OCR algorithms rooted in image processing were typically rule-based systems. One well-known OCR that uses this approach is [Tesseract](https://github.com/tesseract-ocr/tesseract?ref=blog.roboflow.com). These systems relied on manually crafted features and heuristic rules to identify characters within images. The approach involved segmenting characters into individual units and applying a set of rules for character classification.

However, the accuracy and performance of these algorithms were often constrained due to the intricate process of developing and fine-tuning the necessary handcrafted features and rules for effective recognition.

### Tesseract

Tesseract, an open-source optical character recognition engine, originated at Hewlett-Packard Laboratories in the 1980s and subsequently became open-source in 2005.

Initially designed to recognize English text exclusively, Tesseract has evolved into a versatile OCR engine. Working from traditional image processing principles, which involves manual logic unlike the deep learning processes in modern systems, Tesseract analyzes images to identify patterns for character recognition.

First, Tesseract preprocesses the image to enhance input quality, a step which encompasses tasks like contrast improvement and noise removal. Following this, Tesseract employs feature extraction techniques, including edge detection and pattern recognition, to identify and recognize characters.https://blog.roboflow.com/content/images/2024/04/image-741.webp_Tesseract OCR engine pipeline._ [_Source_](https://www.researchgate.net/figure/Tesseract-OCR-engine-architecture_fig4_265087843?ref=blog.roboflow.com).

## Deep Learning Approaches to Optical Character Recognition

With the rise of deep learning, the integration of neural networks into OCR systems has gained substantial popularity. In particular, deep learning methodologies like [Convolutional Neural Networks](https://blog.roboflow.com/what-is-a-convolutional-neural-network/) and Long Short-Term Memory networks are leveraged, for precise text recognition. Neural networks regularly achieve better performance than traditional OCR techniques.

In recent years, there has also been a surge in novel approaches that leverage pre-trained image and text [Transformers](https://blog.roboflow.com/what-is-a-transformer/), a deep learning architecture. Transformers are ushering in a new era of end-to-end optical word recognition.

### PaddleOCR

[Paddle OCR](https://arxiv.org/abs/2009.09941?ref=blog.roboflow.com) is an open-source engine developed by Baidu's PaddlePaddle team. Leveraging deep learning techniques, including CNNs and recurrent neural networks, Paddle OCR excels in accurate text recognition. It comprises two key components: the detector and the extractor. The detector is tasked with pinpointing text within an image or document. It employs various algorithms, such as [EAST (Efficient and Accurate Scene Text)](https://paperswithcode.com/paper/east-an-efficient-and-accurate-scene-text?ref=blog.roboflow.com) or [DB (Differentiable Binarization)](https://arxiv.org/abs/1911.08947?ref=blog.roboflow.com) detectors, to identify text regions.https://blog.roboflow.com/content/images/2024/04/image-745.webp_DB (Differentiable Binarization) architecture._ [_Source_](https://arxiv.org/pdf/2009.09941.pdf?ref=blog.roboflow.com).

After the detector locates the text, the extractor comes into play, retrieving the text from the image. It employs a blend of Convolutional Neural Networks and Recurrent Neural Networks for precise text recognition. CNNs are utilized to extract features from the text, while RNNs play a crucial role in recognizing the sequence of characters.https://blog.roboflow.com/content/images/2024/04/image-748.webp_CRNN Extractor architecture._ [_Source_](https://arxiv.org/pdf/1507.05717.pdf?ref=blog.roboflow.com).

Paddle OCR stands out for its remarkable speed, making it among the swiftest OCR engines. Its efficiency is attributed to the utilization of parallel computing and GPU acceleration. This feature renders it particularly suitable for extensive OCR tasks, including document scanning and image recognition. Moreover, its adaptability shines through as it can be tailored and fine-tuned for specific tasks and datasets, enhancing its versatility and robustness in various OCR applications.

### TrOCR

[Transformer-based Optical Character Recognition (TrOCR)](https://arxiv.org/abs/2109.10282?ref=blog.roboflow.com) is one of many transformer-based [OCR models](https://blog.roboflow.com/best-ocr-models-text-recognition/). In contrast to traditional OCR systems, TrOCR adopts a methodology where both input image processing and the generation of corresponding text output occur within a single model.

The encoder segment of TrOCR employs a transformer-based architecture to handle the input image, segmenting it into a grid of patches and extracting visual features from each patch. Simultaneously, the decoder component utilizes a transformer-based model to produce the relevant text output, incorporating the visual features extracted from the image.https://blog.roboflow.com/content/images/2024/04/image-752.webp_TrOCR Architecture._ [_Source_](https://arxiv.org/pdf/2109.10282.pdf?ref=blog.roboflow.com).

This comprehensive and transformer-based methodology empowers TrOCR to attain strong performance across diverse OCR benchmarks, establishing the model as a highly dependable and effective tool for text recognition tasks.

## Advantages of Modern OCR Techniques

One of the primary advantages of OCR is its ability to automate the data entry process. Traditional manual data entry is not only time-consuming but also prone to errors. OCR technology streamlines this process by automatically extracting text from images or scanned documents, eliminating the need for human input. This automation significantly reduces the time required for tasks such as transcribing printed or handwritten text into digital formats.

In addition, OCR facilitates the digitization of documents, leading to improved efficiency in document management. By converting physical documents into digital formats, OCR enables easy storage, retrieval, and organization of information.

Digital documents are more accessible and can be quickly searched, eliminating the need for manual sorting through paper files. This advantage is particularly crucial in business settings where quick access to relevant information is essential.

## Limitations of Modern OCR Techniques

OCR systems, while proficient in recognizing printed text, often face challenges when it comes to accurately interpreting handwritten text. Handwriting is inherently diverse, varying in styles, shapes, and legibility. Unlike printed text, which follows standardized fonts and structures, handwritten text can exhibit significant variability, making it difficult for OCR algorithms to consistently and accurately recognize every nuance.

This limitation is particularly pronounced in scenarios where the handwriting is cursive, unconventional, or poorly formed. Overcoming this challenge requires more advanced techniques, such as integrating machine learning [models](https://blog.roboflow.com/best-ocr-models-text-recognition/) specifically trained on diverse handwritten datasets.

Furthermore,OCR systems can be sensitive to the quality of the input image and may struggle with images that have poor resolution, low contrast, or significant noise. Additionally, documents with complex layouts, multiple columns, or irregular text arrangements pose challenges for traditional OCR methods.

The image preprocessing steps performed by OCR engines, such as Tesseract, are crucial for improving recognition accuracy, but they may not always suffice for images with inherent complexities. Complex layouts can disrupt the OCR's ability to accurately segment text regions and extract meaningful content, leading to errors in character recognition.

To mitigate these issues, additional preprocessing techniques or more advanced OCR methods may be necessary, adding complexity to the implementation process.

</details>
