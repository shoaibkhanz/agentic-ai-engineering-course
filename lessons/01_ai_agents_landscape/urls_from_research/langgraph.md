## Controllable cognitive architecture for any task

LangGraph's flexible framework supports diverse control flows – single agent, multi-agent, hierarchical, sequential – and robustly handles realistic, complex scenarios.

Ensure reliability with easy-to-add moderation and quality loops that prevent agents from veering off course.

Use LangGraph Platform to templatize your cognitive architecture so that tools, prompts, and models are easily configurable with LangGraph Platform Assistants.

[See the docs](https://langchain-ai.github.io/langgraph/)

## Designed for human-agent collaboration

With built-in statefulness, LangGraph agents seamlessly collaborate with humans by writing drafts for review and awaiting approval before acting. Easily inspect the agent’s actions and "time-travel" to roll back and take a different action to correct course.

[Read a conceptual guide](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#human-in-the-loop)

## How does LangGraph help?

## Guide, moderate, and control your agent with human-in-the-loop.

Prevent agents from veering off course with easy-to-add moderation and quality controls. Add human-in-the-loop checks to steer and approve agent actions.

[Learn how to add human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)

## Build expressive, customizable agent workflows.

LangGraph’s low-level primitives provide the flexibility needed to create fully customizable agents. Design diverse control flows — single, multi-agent, hierarchical — all using one framework.

[See different agent architectures](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)

## Persist context for long-term interactions.

LangGraph’s built-in memory stores conversation histories and maintains context over time, enabling rich, personalized interactions across sessions.

[Learn about agent memory](https://langchain-ai.github.io/langgraph/concepts/memory/)

## First-class streaming for better UX design.

Bridge user expectations and agent capabilities with native token-by-token streaming, showing agent reasoning and actions in real time.

[See how to use streaming](https://langchain-ai.github.io/langgraph/how-tos/streaming/)

## First class streaming support for better UX design

Bridge user expectations and agent capabilities with native token-by-token streaming and streaming of intermediate steps, helpful for showing agent reasoning and actions back to the user as they happen. Use LangGraph Platform's API to deliver dynamic and interactive user experiences.

[Learn more](https://langchain-ai.github.io/langgraph/how-tos/streaming-tokens/)

## Deploy agents at scale, monitor carefully, iterate boldly

Design agent-driven user experiences with LangGraph Platform's APIs. Quickly deploy and scale your application with infrastructure built for agents. Choose from multiple deployment options.

### Fault-tolerant scalability

Handle large workloads gracefully with horizontally-scaling servers, task queues, and built-in persistence. Enhance resilience with intelligent caching and automated retries.

### Dynamic APIs for designing agent experience

Craft personalized user experiences with APIs featuring long-term memory to recall information across conversation sessions. Track, update, and rewind your app's state for easy human steering and interaction. Kick off long-running background jobs for research-style or multi-step work.

### Integrated developer experience

Simplify prototyping, debugging, and sharing of agents in our visual LangGraph Studio. Deploy your application with 1-click deploy with our SaaS offering or within your own VPC. Then, monitor app performance with LangSmith.

### Without LangGraph Platform

Write your own API endpoints for human-in-the-loop, background jobs, and more. Manage state and checkpointing.  Handle horizontal scaling and engineer fault tolerance. Continual maintenance and on-call.

### With LangGraph Platform

Focus on the app logic, not the infrastructure. Full batteries included — APIs, scalability, streaming, built in.

## LangGraph FAQs

How is LangGraph different from other agent frameworks?

Other agentic frameworks can work for simple, generic tasks but fall short for complex tasks bespoke to a company’s needs. LangGraph provides a more expressive framework to handle companies’ unique tasks without restricting users to a single black-box cognitive architecture.

Does LangGraph impact the performance of my app?

LangGraph will not add any overhead to your code and is specifically designed with streaming workflows in mind.

Is LangGraph open source? Is it free?

Yes. LangGraph is an MIT-licensed open-source library and is free to use.

How are LangGraph and LangGraph Platform different?

LangGraph is a stateful, orchestration framework that brings added control to agent workflows. LangGraph Platform is a service for deploying and scaling LangGraph applications, with an opinionated API for building agent UXs, plus an integrated developer studio.

LangGraph (open source)

LangGraph Platform

Features

Stateful orchestration framework for agentic applications

Scalable infrastructure for deploying LangGraph applications

Python and JavaScript

Python and JavaScript

None

Yes - useful for retrieving & updating state or long-term memory, or creating a configurable assistant

Basic

Dedicated mode for token-by-token messages

Community contributed

Supported out-of-the-box

Self-managed

Managed Postgres with efficient storage

Self-managed

\- Cloud

\- Hybrid

\- Full self-hosted

Self-managed

Auto-scaling of task queues and servers

Self-managed

Automated retries

Simple threading

Supports double-texting

None

Cron scheduling

Opt-in LangSmith integration for observability

Integrated with LangSmith for observability

LangGraph Studio for Desktop

LangGraph Studio for Desktop & Cloud

What are my deployment options for LangGraph Platform?

We currently have the following deployment options for LangGraph applications:

‍

**Cloud SaaS:** Fully managed and hosted as part of LangSmith (our unified observability & evals platform). Deploy quickly, with automatic updates and zero maintenance.

‍

**Hybrid** (SaaS control plane, self-hosted data plane). No data leaves your VPC. Provisioning and scaling is managed as a service.

‍

**Fully** **Self-Hosted:** Deploy LangGraph entirely on your own infrastructure.

‍

If you want to try out a basic version of our LangGraph server in your environment, you can also self-host on our Developer plan and get up to 100k nodes executed per month for free. Great for running hobbyist projects, with fewer features are available than in paid plans.

‍

Is LangGraph Platform open source?

No. LangGraph Platform is proprietary software.

‍

There is a free, self-hosted version of LangGraph Platform with access to basic features. The Cloud SaaS deployment option is free while in beta, but will eventually be a paid service. We will always give ample notice before charging for a service and reward our early adopters with preferential pricing. The Bring Your Own Cloud (BYOC) and Self-Hosted Enterprise options are also paid services. [Contact our sales team](https://www.langchain.com/contact-sales) to learn more.

‍

For more information, see our [LangGraph Platform pricing page](https://www.langchain.com/pricing-langgraph-platform).