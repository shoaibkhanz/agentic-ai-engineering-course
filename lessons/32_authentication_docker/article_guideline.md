# Authentication and Docker Guidelines

## Global Context of the Lesson

### What We Are Planning to Share

In this lesson, we prepare our research agent for production deployment by addressing two critical infrastructure requirements:

1. **Authentication with Descope:** Implementing OAuth 2.0 authentication using Descope and FastMCP's `DescopeProvider`, enabling secure API access and per-user data isolation.
2. **Docker containerization:** Creating a multi-stage Dockerfile and Docker Compose configuration for local development with PostgreSQL.

We also introduce the architectural shift from stateful (file-based) to stateless (database-backed) design, which is essential for cloud deployment. This lesson focuses on the "how" of authentication and containerization, while the next lesson covers database schema and file handling in depth.

### Why We Think It's Valuable

Moving from prototype to production is where most AI agent projects fail. The jump from "works on my laptop" to "runs reliably in the cloud" requires specific infrastructure knowledge:

- **Security:** Without authentication, anyone with your server URL can execute tools and run expensive LLM calls.
- **Data isolation:** Multiple users need their own research sessions without data leakage.
- **Portability:** Docker containers ensure the same code runs identically in development and production.
- **Scalability:** Stateless architecture enables horizontal scaling on serverless platforms like Cloud Run.

This lesson bridges the gap between local development and cloud-ready infrastructure.

### Expected Length of the Lesson

**4,500–5,500 words** (without the titles and references), where we assume that 200-250 words ≈ 1 minute of reading time.

### Theory / Practice Ratio

40% theory - 60% real-world examples and configuration walkthroughs

---

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 4 parts, each with multiple lessons.

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in their journey. You will be careful to consider the following:
- The points of view
- To not reintroduce concepts already taught in previous lessons.
- To be careful when talking about concepts introduced only in future lessons
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

This is **Lesson 32** (from **Part 3**) of the course on AI agents.

### Point of View

The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

### Who Is the Intended Audience

Aspiring AI engineers who have built AI agent systems and are now learning to deploy them to production.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:

**Part 1:**
- AI Engineering fundamentals, workflows vs. agents, context engineering
- Structured outputs, basic workflow patterns, tools & function calling
- Planning & reasoning, ReAct implementation, agent memory & knowledge
- RAG deep dive, multimodal processing

**Part 2:**
- Agentic design patterns and framework comparisons
- LangGraph implementation for the research agent (Nova)
- MCP (Model Context Protocol) for tool integration
- The writing workflow agent (Brown)
- Multi-agent orchestration

**Part 3 (preceding lessons):**
- Agent observability with Opik (Lesson 27)
- Evaluation dataset creation (Lesson 28)
- Evaluation-driven development (Lesson 29)
- AI evaluations and quality metrics (Lesson 30)
- Continuous Integration for AI agents (Lesson 31)

At this point, the reader has built functional agent systems and understands CI pipelines. They are ready to learn production deployment infrastructure.

### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:

**Part 3 (remaining lessons):**
- **Lesson 33 - Database and File Handling:** PostgreSQL schema design, Alembic migrations, file uploads/downloads for MCP servers, user usage tracking.
- **Lesson 34 - Cloud Deployment:** Deploying to Google Cloud Run, Cloud SQL configuration, production environment setup.

**Part 4:**
- Final project building and submission, applying all course concepts to create a novel agent solution.

### Anchoring the Reader in the Educational Journey

Within the course we are teaching the reader multiple topics and concepts. Understanding where the reader is in their educational journey is critical for this piece. You have to use only previously introduced concepts, while being reluctant about using concepts that haven't been introduced yet.

The reader has built the research agent (Nova) and writing agent (Brown) in previous lessons. They understand MCP, tools, and agent workflows. In Lesson 31, they learned CI practices. This lesson builds directly on that foundation by addressing what happens after CI passes: deployment.

When referencing database concepts, keep explanations high-level since Lesson 33 covers them in depth. Focus on the "why" of stateless architecture rather than the "how" of database schema.

---

## Narrative Flow of the Lesson

Follow this story arc:

1. **Problem:** "Our research agent works locally but breaks when we try to run it in the cloud. Files disappear, users overwrite each other's data, and anyone can access our API."
2. **The stateless constraint:** Cloud platforms like Cloud Run require stateless applications. We must rethink how we store data.
3. **Authentication solution:** Descope provides OAuth 2.0 authentication that integrates with FastMCP.
4. **Containerization solution:** Docker packages our agent with all dependencies for consistent execution anywhere.
5. **Practical workflow:** How to run the containerized agent locally with Docker Compose.

---

## Lesson Outline

1. **Section 1 - Introduction: Preparing for Production**
2. **Section 2 - From Stateful to Stateless Architecture**
3. **Section 3 - Authentication with Descope**
4. **Section 4 - Docker for AI Agents**
5. **Section 5 - Running the Agent Locally**
6. **Section 6 - Conclusion**

---

## Section 1 — Introduction: Preparing for Production

**Source reference:** Reference the introduction paragraphs and "Introduction: Preparing for Production" section in `source.md`, including the subsections on Cloud Run features and "Alternatives to Cloud Run."

### Writing Instructions

- **Opening hook:** Start by recalling what we built in Part 2—the research agent using MCP that reads and writes files locally. Acknowledge that this approach worked well for development but creates problems in production.

- **Quick reference to previous lessons:** Briefly mention Lesson 31 (CI) as the foundation we're building on. CI ensures code quality; now we address deployment infrastructure.

- **Transition to this lesson:** Explain that production deployment introduces new constraints: multiple users, ephemeral instances, and security requirements.

- **Introduce Cloud Run:** Explain what Google Cloud Run is and why we chose it (automatic scaling, health checks, load balancing, zero infrastructure management). Reference the "Alternatives to Cloud Run" subsection to mention AWS App Runner, Fargate, and Azure Container Apps—the concepts apply across platforms.

- **The stateless constraint:** Introduce the fundamental constraint early. Cloud Run instances are ephemeral. Local file storage breaks completely.

- **Roadmap of changes:** List the four key changes needed from `source.md`:
  1. Stateless data storage (database)
  2. User authentication (Descope)
  3. File upload/download (custom HTTP endpoints)
  4. Containerization (Docker)

- **Scope clarification:** State that this lesson covers authentication and Docker. Database configuration and file handling are covered in Lesson 33.

- **Section length:** ~500 words

### Transition to Section 2

After explaining what Cloud Run requires, transition to the architectural shift needed to meet those requirements. Use a phrase like: "Before diving into authentication and Docker, let's understand the fundamental architectural change required for cloud deployment: moving from stateful to stateless design."

---

## Section 2 — From Stateful to Stateless Architecture

**Source reference:** Reference the "From Stateful to Stateless Architecture" section in `source.md`, including "The Problem with Local File Storage" and "The Database Solution" subsections.

### Writing Instructions

- **Show the problem:** Describe how the original `research_agent_part_2` stored data in a `.nova/` directory. List the specific files from `source.md` (guidelines_filenames.json, perplexity_results.md, etc.).

- **Explain why this breaks:** Walk through the three failure modes:
  1. Multiple users overwrite each other's files
  2. Files are lost when instances scale
  3. No way to associate research with specific users

- **Introduce the database solution:** Explain that `research_agent_part_3` replaces file storage with PostgreSQL. Every model includes a `user_id` field.

- **List the benefits:** Data isolation, horizontal scaling, persistence, usage tracking.

- **Scope boundary:** Explicitly state that the database schema and configuration details are covered in Lesson 33. This section focuses on understanding *why* the change is necessary.

- **Section length:** ~400 words

### Transition to Section 3

With the stateless architecture established, transition to authentication. Use a phrase like: "With data now stored per-user in the database, we need a way to identify those users. This is where authentication comes in."

---

## Section 3 — Authentication with Descope

**Source reference:** Reference the "Authentication with Descope" section in `source.md`, including all subsections: "Why Authentication for AI Agents," "Descope Overview," "Setting Up Descope," "Code Implementation," and "Environment Variables."

### Writing Instructions

- **Why authentication matters:** Start with the four reasons from `source.md`: security, data isolation, usage limits, audit trail. Emphasize that authentication is not optional for production AI agents.

- **Introduce Descope:** Explain what Descope is—an authentication platform with OAuth 2.0 support. Highlight the key features: multiple auth methods, Dynamic Client Registration, user management dashboard, free tier.

- **Setup walkthrough:** Walk through the four setup steps from `source.md`:
  1. Create a Descope account
  2. Create a project (get the Project ID)
  3. Enable Dynamic Client Registration (DCR)
  4. Configure authentication methods

- **Code implementation:** Show the code from `source.md` that creates the `DescopeProvider` in `server.py`. Explain the three parameters (`project_id`, `descope_base_url`, `base_url`) and what each does.

- **Environment variables:** Show the environment variables needed (DESCOPE_PROJECT_ID, DESCOPE_BASE_URL, SERVER_URL) and the corresponding settings in `settings.py`.

- **Important note:** Emphasize that authentication only works with HTTP transport mode, not stdio transport.

- **Foreshadow the experience:** Mention that later in the lesson (after Docker setup), the reader will experience the authentication flow when connecting from Cursor.

- **Section length:** ~800 words

### Transition to Section 4

With authentication configured, transition to containerization. Use a phrase like: "With authentication in place, we need to package our agent for deployment. Docker provides containerization, which ensures your application runs identically in development and production."

---

## Section 4 — Docker for AI Agents

**Source reference:** Reference the "Docker for AI Agents" section in `source.md`, including all subsections: "What is Docker," "The Dockerfile," "Docker Compose," "The Entrypoint Script," and "Local Development vs Cloud Deployment."

### Writing Instructions

This is the longest and most technical section. Structure it clearly with subsections.

#### 4.1 What is Docker

- Briefly explain Docker and containers (1-2 paragraphs)
- List the benefits for AI agents from `source.md`: consistency, isolation, reproducibility, cloud-native

#### 4.2 The Dockerfile (Multi-stage Build)

Walk through the Dockerfile in detail, following the structure in `source.md`:

- **Stage 1: Builder**
  - Explain slim Python base image
  - Explain `uv` installation for fast dependency management
  - Explain layer caching (copy dependency files first)
  - Explain `uv sync --frozen --no-dev`

- **Stage 2: Runtime**
  - Explain installing only runtime dependencies (libpq5, git)
  - Explain creating non-root user `nova` for security
  - Explain Git configuration for non-interactive environment
  - Explain copying virtual environment from builder
  - Explain copying application code, Alembic files, entrypoint script
  - Explain environment variables (PATH, PYTHONUNBUFFERED, GIT_TERMINAL_PROMPT)
  - Explain health check configuration

#### 4.3 Docker Compose

Walk through `docker-compose.yml` from `source.md`:

- **PostgreSQL service:** Alpine image, environment variables with defaults, volume for persistence, health check
- **MCP server service:** Build context, `depends_on` with health condition, DATABASE_URL using Docker network hostname, API key pass-through, volume mount for development

- **Volumes:** Explain named volume for database persistence

#### 4.4 The Entrypoint Script

- Show the `docker-entrypoint.sh` script from `source.md`
- Explain the three steps: run migrations, start server, use `exec` for signal handling

#### 4.5 Local Development vs Cloud Deployment

- Explain how the same code works in both environments through environment-based configuration
- **Local:** Docker Compose, PostgreSQL container, localhost access
- **Cloud:** Cloud Run, Cloud SQL, configured via environment variables
- Mention `Dockerfile.cloudrun` and `docker-entrypoint-cloudrun.sh` exist for cloud deployment
- Show the `is_cloud_sql` property from `settings.py`

- **Section length:** ~1,500 words

### Transition to Section 5

With the Docker configuration explained, transition to running the agent. Use a phrase like: "With Docker configured, let's run the research agent on your local machine and experience the full authentication flow."

---

## Section 5 — Running the Agent Locally

**Source reference:** Reference the "Running the Agent Locally" section in `source.md`, including all subsections: "Prerequisites," "Starting the Services," "Connecting from Cursor," "Stopping the Services," and "Useful Commands."

### Writing Instructions

This section is a hands-on walkthrough. Use numbered steps and code blocks.

#### 5.1 Prerequisites

List the three prerequisites from `source.md`:
1. Install Docker Desktop
2. Create the `.env` file (show the template from `source.md`)
3. Generate the lock file if needed

#### 5.2 Starting the Services

Walk through the commands:
- `docker compose build`
- `docker compose up -d`
- `docker compose ps` to verify
- `docker compose logs -f mcp-server` to check logs

Show expected output from `source.md`.

#### 5.3 Connecting from Cursor

This is the payoff for the authentication setup:

- Show the MCP configuration JSON for Cursor
- **Without authentication:** Tools appear immediately
- **With authentication:** Walk through the OAuth flow:
  1. Click Connect button
  2. Browser opens to Descope
  3. Log in
  4. Redirected back, Cursor receives token
  5. Tools become available

Mention that the token is cached.

#### 5.4 Stopping the Services

Show the three stop commands from `source.md`:
- `docker compose stop` (keep data)
- `docker compose down` (remove containers, keep volume)
- `docker compose down -v` (remove everything)

#### 5.5 Useful Commands

Include the quick reference commands from `source.md` (logs, psql access, rebuild, status).

- **Section length:** ~700 words

### Transition to Section 6

After the hands-on section, transition to the conclusion. Use a phrase like: "You now have a containerized research agent running locally with authentication. Let's recap what we covered and look ahead to the next lesson."

---

## Section 6 — Conclusion

**Source reference:** Reference the "Conclusion" section in `source.md`.

### Writing Instructions

- **Summarize the four key topics:** Use the bullet points from `source.md`:
  1. Stateless architecture (file-based → PostgreSQL)
  2. Authentication with Descope (OAuth 2.0, `DescopeProvider`)
  3. Docker containerization (multi-stage Dockerfile, Docker Compose)
  4. Environment-based configuration (same code for local and cloud)

- **Emphasize the achievement:** The research agent is now containerized and ready for deployment. The reader can run it locally, authenticate with Descope, and use it from Cursor.

- **Forward reference to Lesson 33:** State that the next lesson covers database schema and configuration in depth, file uploads and downloads for MCP servers (since standard MCP tools can't handle file transfers over HTTP), and user usage tracking.

- **Forward reference to Lesson 34:** Briefly mention that Lesson 34 covers the actual Cloud Run deployment.

- **Section length:** ~300 words

---

## Article Code

Links to code that will be used to support the article. Always prioritize this code over every other piece of code found in the sources:

1. `source.md` - The comprehensive source document covering all lesson topics
2. `research_agent_part_3/` - The updated research agent implementation with authentication and Docker support

Key files to reference:
- `research_agent_part_3/src/server.py` - Server creation with DescopeProvider
- `research_agent_part_3/src/config/settings.py` - Settings including Descope and Cloud SQL configuration
- `research_agent_part_3/Dockerfile` - Multi-stage Docker build
- `research_agent_part_3/docker-compose.yml` - Local development orchestration
- `research_agent_part_3/docker-entrypoint.sh` - Container startup script

---

## Sources

1. [Descope Documentation - Dynamic Client Registration](https://docs.descope.com/identity-federation/inbound-apps/creating-inbound-apps#method-2-dynamic-client-registration-dcr)
2. [FastMCP - Descope Integration](https://gofastmcp.com/integrations/descope)
3. [Docker Documentation](https://docs.docker.com/)
4. [Docker Compose Documentation](https://docs.docker.com/compose/)
5. [Google Cloud Run Documentation](https://cloud.google.com/run/docs)

---

## Other Sources

1. [Descope FastMCP Server Example (GitHub)](https://github.com/descope/ai/tree/main/examples/fastmcp-server)
2. [Google Cloud SQL Documentation](https://cloud.google.com/sql/docs)
3. [uv Documentation - Docker Integration](https://docs.astral.sh/uv/guides/integration/docker/)
