_Editor’s note: This post is part of the [AI On](https://blogs.nvidia.com/blog/tag/ai-on/) blog series, which explores the latest techniques and real-world applications of agentic AI, chatbots and copilots. The series also highlights the NVIDIA software and hardware powering advanced AI agents, which form the foundation of AI query engines that gather insights and perform tasks to transform everyday experiences and reshape industries._

[AI agents](https://www.nvidia.com/en-us/glossary/ai-agents/) powered by large language models ([LLMs](https://www.nvidia.com/en-us/glossary/large-language-models/)) have grown past their FAQ chatbot beginnings to become true digital teammates capable of planning, reasoning and taking action — and taking in corrective feedback along the way.

Thanks to reasoning AI models, agents can learn how to think critically and tackle complex tasks. This new class of “reasoning agents” can break down complicated problems, weigh options and make informed decisions — while using only as much compute and as many [tokens](https://blogs.nvidia.com/blog/ai-tokens-explained/) as needed.

Reasoning agents are making a splash in industries where decisions rely on multiple factors. Such industries range from customer service and healthcare to manufacturing and financial services.

## **Reasoning On vs. Reasoning Off**

Modern AI agents can toggle reasoning on and off, allowing them to efficiently use compute and tokens.

A full [chain‑of‑thought](https://www.nvidia.com/en-us/glossary/cot-prompting/) pass performed during reasoning can take up to 100x more compute and tokens than a quick, single‑shot reply — so it should only be used when needed. Think of it like turning on headlights — switching on high beams only when it’s dark and turning them back to low when it’s bright enough out.

Single-shot responses are great for simple queries — like checking an order number, resetting a password or answering a quick FAQ. Reasoning might be needed for complex, multistep tasks such as reconciling tax depreciation schedules or orchestrating the seating at a 120‑guest wedding.

New [NVIDIA Llama Nemotron models](https://developer.nvidia.com/blog/build-enterprise-ai-agents-with-advanced-open-nvidia-llama-nemotron-reasoning-models/), featuring advanced reasoning capabilities, expose a simple system‑prompt flag to enable or disable reasoning, so developers can programmatically decide per query. This allows agents to perform reasoning only when the stakes demand it — saving users wait times and minimizing costs.

## **Reasoning AI Agents in Action**

Reasoning AI agents are already being used for complex problem-solving across industries, including:

- **Healthcare:** Enhancing diagnostics and treatment planning.
- **Customer Service**: Automating and personalizing complex customer interactions, from resolving billing disputes to recommending tailored products.
- **Finance:** Autonomously analyzing market data and providing investment strategies.
- **Logistics and Supply Chain:** Optimizing delivery routes, rerouting shipments in response to disruptions and simulating possible scenarios to anticipate and mitigate risks.
- **Robotics**: Powering warehouse robots and autonomous vehicles, enabling them to plan, adapt and safely navigate dynamic environments.

Many customers are already experiencing enhanced workflows and benefits using reasoning agents.

Amdocs uses reasoning-powered AI agents to transform customer engagement for telecom operators. Its amAIz GenAI platform, enhanced with advanced reasoning models such as NVIDIA Llama Nemotron and amAIz Telco verticalization, enables agents to autonomously handle complex, multistep customer journeys — spanning customer sales, billing and care.

EY is using reasoning agents to significantly improve the quality of responses to tax-related queries. The company compared generic models to tax-specific reasoning models, which revealed up to an 86% improvement in response quality for tax questions when using a reasoning approach.

SAP’s Joule agents — which will be equipped with reasoning capabilities from Llama Nemotron –– can interpret complex user requests, surface relevant insights from enterprise data and execute cross-functional business processes autonomously.

## **Designing an AI Reasoning Agent**

A few key components are required to build an AI agent, including tools, memory and planning modules. Each of these components augments the agent’s ability to interact with the outside world, create and execute detailed plans, and otherwise act semi- or fully autonomously.

Reasoning capabilities can be added to AI agents at various places in the development process. The most natural way to do so is by augmenting planning modules with a large reasoning model, like [Llama Nemotron Ultra](https://build.nvidia.com/nvidia/llama-3_1-nemotron-ultra-253b-v1) or [DeepSeek-R1](https://build.nvidia.com/deepseek-ai/deepseek-r1). This allows more time and reasoning effort to be used during the initial planning phase of the agentic workflow, which has a direct impact on the overall outcomes of systems.

The [AI-Q NVIDIA AI Blueprint](https://build.nvidia.com/nvidia/aiq) and the [NVIDIA Agent Intelligence toolkit](https://developer.nvidia.com/agent-intelligence-toolkit) can help enterprises break down silos, streamline complex workflows and optimize agentic AI performance at scale.

The AI-Q blueprint provides a reference workflow for building advanced agentic AI systems, making it easy to connect to NVIDIA accelerated computing, storage and tools for high-accuracy, high-speed digital workforces. AI-Q integrates fast multimodal data extraction and retrieval using [NVIDIA NeMo Retriever](https://developer.nvidia.com/nemo-retriever), [NIM microservices](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/) and AI agents.

In addition, the open-source NVIDIA Agent Intelligence toolkit enables seamless connectivity between agents, tools and data. Available on [GitHub](https://github.com/NVIDIA/AIQToolkit), this toolkit lets users connect, profile and optimize teams of AI agents, with full system traceability and performance profiling to identify inefficiencies and improve outcomes. It’s framework-agnostic, simple to onboard and can be integrated into existing multi-agent systems as needed.

## **Build and Test Reasoning Agents With Llama Nemotron**

Learn more about [Llama Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/llama-nemotron/), which recently was at the top of industry benchmark [leaderboards](https://developer.nvidia.com/blog/nvidia-llama-nemotron-ultra-open-model-delivers-groundbreaking-reasoning-accuracy/) for advanced science, coding and math tasks. [Join the community](https://forums.developer.nvidia.com/t/introducing-llama-nemotron-ultra-peak-accuracy-meets-unmatched-efficiency/329685) shaping the future of agentic, reasoning-powered AI.

Plus, explore and fine-tune using the open Llama Nemotron post-training [dataset](https://huggingface.co/datasets/nvidia/Llama-Nemotron-Post-Training-Dataset) to build custom reasoning agents. Experiment with toggling reasoning on and off to optimize for cost and performance.

And test NIM-powered agentic workflows, including [retrieval-augmented generation](https://build.nvidia.com/nvidia/build-an-enterprise-rag-pipeline) and the [NVIDIA AI Blueprint for video search and summarization](https://build.nvidia.com/nvidia/video-search-and-summarization), to quickly prototype and deploy advanced AI solutions.