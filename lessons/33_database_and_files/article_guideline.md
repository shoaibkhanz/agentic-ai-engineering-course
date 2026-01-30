# Database and File Handling Guidelines

## Global Context of the Lesson

### What We Are Planning to Share

In this lesson, we complete the transformation of our research agent from a local prototype to a production-ready application. Building on Lesson 32's authentication and containerization work, we:

- **Migrate from filesystem to PostgreSQL** for all state management, ensuring data persists beyond container lifetimes and each user's data is isolated.
- **Design a database schema** centered on the Article model, with supporting tables for scraped content, GitHub ingests, YouTube transcripts, and tool usage tracking.
- **Refactor MCP tools** to read from and write to database columns instead of filesystem paths.
- **Set up local development** with Docker Compose, running PostgreSQL alongside our MCP server.
- **Configure Cloud SQL** for production, using environment-based settings to switch between local and cloud databases.
- **Implement Alembic migrations** for version-controlled schema evolution.
- **Add rate limiting** to protect API budgets by tracking tool calls per user per month.
- **Work around MCP's file transfer limitations** with custom HTTP endpoints for uploading article guidelines and downloading research results.

### Why We Think It's Valuable

The transition from file-based to database-backed storage is more than a technical upgrade; it is a fundamental shift in how an agent manages state. Without this change:

- Data disappears when containers restart (ephemeral storage problem).
- Multiple users would overwrite each other's data.
- Features like rate limiting and analytics become impossible.

This lesson teaches the infrastructure patterns every production AI agent needs: persistent storage, user isolation, usage tracking, and file handling workarounds for protocol limitations.

### Expected Length of the Lesson

**6,000–7,000 words** (without the titles and references), where we assume that 200-250 words ≈ 1 minute of reading time.

### Theory / Practice Ratio

30% theory - 70% real-world examples (code-heavy lesson with schema designs, tool refactoring, and configuration walkthroughs)

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 4 parts, each with multiple lessons.

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in its journey. You will be careful to consider the following:
- The points of view
- To not reintroduce concepts already taught in the previous lesson.
- To be careful when talking about concepts introduced only in future lessons
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

This is Lesson 33 (from Part 3) of the course on AI agents. It is the second lesson in the "deployment" mini-series (Lessons 32-34).

### Point of View

The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

### Who Is the Intended Audience

Aspiring AI engineers who have built the research agent (Nova) through the course and are now learning production deployment patterns.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:

**Part 1:**
- AI Engineering fundamentals, workflows vs. agents, context engineering
- Structured outputs, workflow patterns, tools and function calling
- Planning and reasoning, ReAct implementation, agent memory

**Part 2:**
- MCP (Model Context Protocol) and MCP servers
- Nova research agent implementation with tools for web scraping, GitHub ingestion, YouTube transcription, and Perplexity research
- Brown writing workflow for article generation

**Part 3:**
- Observability with Opik (Lesson 27)
- Evaluation datasets and AI-as-judge patterns (Lessons 28-29)
- Evaluation-driven development (Lesson 30)
- Continuous Integration for AI agents (Lesson 31)
- **Lesson 32: OAuth authentication with Descope, Docker containerization, and the four-part plan for production readiness**

### Concepts That Will Be Introduced in Future Lessons

**Lesson 34:** Google Cloud Run deployment, Cloud SQL instance creation, continuous deployment with GitHub Actions, production monitoring and logging.

### Anchoring the Reader in the Educational Journey

At this point, the reader has:
- Built the complete Nova research agent with MCP tools
- Set up authentication with Descope (Lesson 32)
- Containerized the application with Docker (Lesson 32)
- Understands the four changes needed for production: (1) database storage, (2) authentication, (3) file handling, (4) containerization

This lesson completes items 1 and 3 from that list. The reader should be comfortable with:
- Python async/await patterns
- Basic Docker concepts
- The MCP tool structure from Part 2
- OAuth concepts from Lesson 32

---

## Narrative Flow of the Lesson

Follow this story arc:

1. **Recap the problem:** Lesson 32 identified four production requirements. Authentication and Docker are done. What remains: replacing the filesystem with a database and handling file uploads/downloads.
2. **Why PostgreSQL:** Evaluate database options and justify the choice.
3. **Schema design:** Map the `.nova/` folder structure to database tables.
4. **Tool refactoring:** Show the transformation pattern from file-based to database-backed tools.
5. **Local development:** Docker Compose for running PostgreSQL alongside the MCP server.
6. **Cloud SQL:** Environment-based configuration for production.
7. **Migrations:** Alembic for schema version control.
8. **Rate limiting:** A bonus feature enabled by the database.
9. **File workarounds:** Custom HTTP endpoints for upload and download.
10. **Analytics preview:** What the database enables.
11. **Conclusion and forward look:** Set up Lesson 34's deployment.

---

## Lesson Outline

1. **Section 1 - Introduction: From Files to Database**
2. **Section 2 - Choosing a Database**
3. **Section 3 - Database Schema Design**
4. **Section 4 - Refactoring Tools: From Files to Database**
5. **Section 5 - Local Development with Docker Compose**
6. **Section 6 - Cloud SQL for Production**
7. **Section 7 - Database Migrations with Alembic**
8. **Section 8 - Rate Limiting for MCP Tools**
9. **Section 9 - File Handling: Upload and Download Workarounds**
10. **Section 10 - Analytics and Monitoring**
11. **Section 11 - Conclusion**

---

## Section 1 — Introduction: From Files to Database

**Source reference:** Use the opening paragraphs and introductory content from `source.md` (lines 1-6).

**Transition from Lesson 32:**
- Begin by recapping Lesson 32: we implemented OAuth 2.0 with Descope and containerized the research agent with Docker.
- Remind the reader of the four-part production plan: (1) stateless storage, (2) authentication ✓, (3) file handling, (4) containerization ✓.
- This lesson tackles the remaining pieces: replacing the local filesystem with PostgreSQL and implementing file transfer workarounds.

**Key points to cover:**
- The `.nova/` folder approach from `research_agent_part_2` works for single-user development but fails in production.
- Serverless platforms like Cloud Run have ephemeral containers—files disappear on restart.
- Multiple users sharing a container would overwrite each other's data.
- The database provides three critical capabilities: persistence, user isolation, and query power.

**Introduce the bonus feature:** Rate limiting for MCP tools, enabled by the database.

**Section length:** 400-500 words

---

## Section 2 — Choosing a Database

**Source reference:** Use the "Choosing a Database" section from `source.md` (lines 7-22).

**Transition:** Now that you understand why file-based storage fails in production, let's evaluate database options and justify our choice.

**Subsections to cover:**

### Why We Need a Database
- Ephemeral containers (cite Cloud Run docs)
- Multi-user isolation requirements
- Query capabilities for features like rate limiting

### Why PostgreSQL
Walk through the alternatives evaluated:
- **SQLite:** Unsuitable for multi-container deployments
- **MySQL/MariaDB:** Limited JSON support
- **MongoDB:** Less appropriate for relational data
- **Firebase/Firestore:** Vendor lock-in, limited queries

Highlight PostgreSQL's advantages:
- ACID transactions
- Native JSON/JSONB columns
- High-performance async with `asyncpg`
- Cloud SQL integration
- Rich Python ecosystem (SQLAlchemy, Alembic)

**Section length:** 400-500 words

---

## Section 3 — Database Schema Design

**Source reference:** Use the "Database Schema Design" section from `source.md` (lines 23-238).

**Transition:** With PostgreSQL selected, let's design a schema that captures everything the research agent needs to persist while supporting multi-user access.

### The Article Model
- Show the complete `Article` model from `source.md` (lines 31-116)
- Explain key design decisions:
  - UUID primary key (client-side generation, no information leakage)
  - User ID index for fast lookups
  - JSON column for `extracted_urls` (structured data without extra tables)
  - Status enum for workflow tracking
- Map each column to its file equivalent in `research_agent_part_2`:
  - `guideline_text` ← `article_guideline.md`
  - `extracted_urls` ← `.nova/guidelines_filenames.json`
  - `perplexity_results` ← `.nova/perplexity_results.md`
  - etc.

### Supporting Tables
- Explain the pattern: UUID primary key, user_id, article_guideline_id foreign key, content columns, timestamp
- List the supporting tables:
  - `LocalFile`: User-uploaded reference files
  - `ScrapedUrl`: Web content from guideline URLs
  - `GitHubIngest`: Processed GitHub repositories
  - `YouTubeTranscript`: Video transcriptions
  - `ScrapedResearchUrl`: URLs discovered during Perplexity research
- Show the `ScrapedUrl` example from `source.md` (lines 140-156)

### Schema Diagram
- Include the Mermaid ER diagram from `source.md` (lines 162-236)
- Explain the relationships: Article is central, all supporting tables reference it via foreign keys
- Note that `ToolCallUsage` stands alone for rate limiting

**Section length:** 700-800 words

---

## Section 4 — Refactoring Tools: From Files to Database

**Source reference:** Use the "Refactoring Tools: From Files to Database" section from `source.md` (lines 240-341).

**Transition:** Now that you understand the schema, let's see how MCP tools transform from file-based to database-backed implementations.

### The Transformation Pattern
State the consistent pattern across all tools:
- **Before:** `research_folder: str` parameter, read from files, write to `.nova/` directory
- **After:** `article_guideline_id: str` (UUID), query database, update columns or insert rows

### Example: extract_guidelines_urls_tool
- Show the Part 2 (file-based) implementation from `source.md` (lines 257-291)
- Show the Part 3 (database-based) implementation from `source.md` (lines 295-332)
- Highlight the four key differences:
  1. Input parameter: folder path → UUID
  2. Data source: file read → database column
  3. Data destination: file write → database update
  4. Async: function becomes `async` for non-blocking DB operations

**Emphasize:** The business logic (URL extraction, categorization) remains unchanged. Only the storage layer is different.

**Section length:** 500-600 words

---

## Section 5 — Local Development with Docker Compose

**Source reference:** Use the "Local Development with Docker Compose" section from `source.md` (lines 343-429).

**Transition:** With our tools refactored for database access, you need a way to run PostgreSQL during development. Docker Compose provides an elegant solution.

### The Two-Service Architecture
- Show the `docker-compose.yml` from `source.md` (lines 351-401)
- Explain the PostgreSQL service:
  - Alpine image for smaller size
  - Environment variables with defaults
  - Named volume for data persistence
  - Health check with `pg_isready`

### Key Configuration Elements
Explain each important aspect:
- **Docker network hostname:** `postgres` resolves to the container's IP
- **Named volume:** Data survives `docker compose down`, only removed with `-v`
- **Health check:** MCP server waits for healthy database before starting
- **Source mount:** `./src:/app/src:ro` allows code changes without rebuilding (`:ro` is read-only)

### Development Commands
Show the common commands:
```bash
docker compose up -d
docker compose logs -f mcp-server
docker compose down
docker compose down -v
```

**Section length:** 500-600 words

---

## Section 6 — Cloud SQL for Production

**Source reference:** Use the "Cloud SQL for Production" section from `source.md` (lines 431-539).

**Transition:** Docker Compose works for local development, but production requires a managed database service. Cloud SQL provides fully managed PostgreSQL with automatic backups and IAM authentication.

### What is Cloud SQL
- Define Cloud SQL briefly
- List advantages: automatic backups, high availability, security patches, private connectivity, IAM authentication

### Environment-Based Configuration
- Show the `settings.py` configuration from `source.md` (lines 452-476)
- Explain the `is_cloud_sql` property: if `CLOUD_SQL_INSTANCE` is set, use Cloud SQL; otherwise, use local `DATABASE_URL`

### The Cloud SQL Python Connector
- Show the `_init_database()` function from `source.md` (lines 484-531)
- Explain both code paths: local (direct DATABASE_URL) and Cloud SQL (connector)
- Highlight connector benefits:
  - IAM authentication using service account identity
  - Automatic SSL certificate handling
  - Connection pooling
  - `refresh_strategy="lazy"` optimized for Cloud Run

**Section length:** 500-600 words

---

## Section 7 — Database Migrations with Alembic

**Source reference:** Use the "Database Migrations with Alembic" section from `source.md` (lines 541-735).

**Transition:** Whether running locally or in the cloud, you need a way to evolve the database schema over time. Alembic provides version-controlled migrations.

### What is Alembic
- Define Alembic and its purpose
- Explain core concepts: revision IDs, upgrade/downgrade functions, autogeneration, environment support

### Alembic Configuration
- Show `alembic.ini` configuration from `source.md` (lines 558-566)
- Explain `env.py` handling both local and Cloud SQL (lines 571-607)

### Migration Examples

**Example 1: Creating the Articles Table**
- Show migration from `source.md` (lines 618-659)
- Highlight patterns: idempotent enum creation, server defaults, comments

**Example 2: Adding the Rate Limiting Table**
- Show migration from `source.md` (lines 672-697)
- Explain the composite index for efficient rate limiting queries

### Running Migrations
- Show development commands: `alembic upgrade head`, `alembic downgrade -1`, etc.
- Show the Docker entrypoint script that runs migrations on startup (lines 723-733)

**Section length:** 600-700 words

---

## Section 8 — Rate Limiting for MCP Tools

**Source reference:** Use the "Rate Limiting for MCP Tools" section from `source.md` (lines 737-876).

**Transition:** With the database infrastructure in place, you can implement features that require persistent storage. Rate limiting is a perfect example—it needs to track usage across requests and container restarts.

### Why Rate Limiting Matters
- Each tool call can trigger expensive API requests (LLM, Firecrawl, etc.)
- Without limits, a single user or malfunctioning agent loop could exhaust your budget
- Enables future tiered pricing models

### The ToolCallUsage Model
- Show the model from `source.md` (lines 757-774)
- Explain the `year_month` denormalization for efficient queries

### The @rate_limited Decorator
- Show the complete implementation from `source.md` (lines 780-851)
- Walk through the decorator logic:
  1. Extract user_id from OAuth token
  2. Query current month's usage
  3. Raise `RateLimitExceededError` if limit reached (includes reset date)
  4. Record the new tool call
  5. Execute the original tool

### Applying Rate Limiting
- Show how tools are decorated (lines 864-875)
- Explain decorator order: `@mcp.tool()` → `@opik.track()` → `@rate_limited`

**Section length:** 500-600 words

---

## Section 9 — File Handling: Upload and Download Workarounds

**Source reference:** Use the "File Upload: Working Around MCP Limitations" and "File Download: Delivering Research Results" sections from `source.md` (lines 877-1130).

**Transition:** The database handles state, and rate limiting protects your budget. But there's another challenge the MCP specification doesn't address: file transfers. Let's implement workarounds using custom HTTP endpoints.

### The MCP Protocol Gap
- Explain the limitation: MCP has no message type for file upload/download
- Local `stdio` transport can access the filesystem; HTTP transport cannot
- The MCP specification is evolving and may address this in future versions

### Our Solution: Custom HTTP Endpoints
- FastMCP allows adding custom routes with `@mcp.custom_route()`
- These exist outside the MCP protocol as regular HTTP endpoints

### The Upload Flow
- Include the sequence diagram from `source.md` (lines 901-918)
- Explain the flow: agent provides URL with user_id → user opens in browser → uploads .md file → receives UUID → provides UUID to agent
- Show the implementation from `source.md` (lines 926-1003)

### The Download Flow
- Include the sequence diagram from `source.md` (lines 1029-1051)
- Explain: tool compiles research → saves to database → returns download URL → user opens in browser → receives file
- Show the implementation from `source.md` (lines 1059-1130)

**Section length:** 700-800 words

---

## Section 10 — Analytics and Monitoring

**Source reference:** Use the "Analytics and Monitoring" section from `source.md` (lines 1132-1192).

**Transition:** All this usage data—tool calls, articles created, research completed—lives in the database. This opens powerful analytics possibilities that were impossible with file-based storage.

### What the Database Captures
- Tool usage in `tool_call_usage`
- Article lifecycle in `articles` (status transitions)
- All research artifacts preserved for debugging

### Example Analytics Queries
- Show the SQL queries from `source.md` (lines 1148-1180):
  - Monthly tool calls per user
  - Most popular tools
  - Research completion rate
  - Users approaching rate limit

### Preview: Querying Cloud SQL
- Mention Cloud SQL Studio in Google Cloud Console
- Show the `gcloud sql connect` command
- Note: detailed coverage in Lesson 34

**Section length:** 300-400 words

---

## Section 11 — Conclusion

**Source reference:** Use the "Conclusion" section from `source.md` (lines 1194-1220).

**Transition:** You have transformed the research agent from a file-based prototype into a database-backed, rate-limited, cloud-ready application.

### Summary of Changes
Recap the key transformations:
- Database integration (ephemeral → persistent)
- Schema design (article-centric with supporting tables)
- Tool refactoring (files → database columns)
- Environment flexibility (Docker Compose ↔ Cloud SQL)
- Schema evolution (Alembic migrations)
- Rate limiting (usage tracking)
- File handling (custom HTTP endpoints)

### What's Next in Lesson 34
Set up the final deployment lesson:
- Google Cloud Run deployment
- Cloud SQL instance creation
- Continuous deployment with GitHub Actions
- Monitoring and logging

**Section length:** 300-400 words

---

## Article Code

Links to code that will be used to support the article:

1. [research_agent_part_3/src/db/models.py](../research_agent_part_3/src/db/models.py) - Database models
2. [research_agent_part_3/src/db/session.py](../research_agent_part_3/src/db/session.py) - Session management with Cloud SQL support
3. [research_agent_part_3/src/config/settings.py](../research_agent_part_3/src/config/settings.py) - Environment-based configuration
4. [research_agent_part_3/src/tools/extract_guidelines_urls_tool.py](../research_agent_part_3/src/tools/extract_guidelines_urls_tool.py) - Refactored tool example
5. [research_agent_part_3/src/utils/rate_limit_utils.py](../research_agent_part_3/src/utils/rate_limit_utils.py) - Rate limiting implementation
6. [research_agent_part_3/src/routers/tools.py](../research_agent_part_3/src/routers/tools.py) - Tool registration with decorators
7. [research_agent_part_3/src/ui/upload_ui.py](../research_agent_part_3/src/ui/upload_ui.py) - Upload endpoint implementation
8. [research_agent_part_3/src/routers/downloads.py](../research_agent_part_3/src/routers/downloads.py) - Download endpoint implementation
9. [research_agent_part_3/docker-compose.yml](../research_agent_part_3/docker-compose.yml) - Local development setup
10. [research_agent_part_3/alembic/](../research_agent_part_3/alembic/) - Migration files

## Sources

1. [PostgreSQL Documentation - JSON Types](https://www.postgresql.org/docs/current/datatype-json.html)
2. [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
3. [Alembic Documentation](https://alembic.sqlalchemy.org/)
4. [Cloud SQL Python Connector](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector)
5. [Google Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres)
6. [Cloud Run Container Runtime Contract](https://cloud.google.com/run/docs/configuring/services/containers)
7. [SQLite - Appropriate Uses](https://www.sqlite.org/whentouse.html)
8. [Docker Compose Networking](https://docs.docker.com/compose/how-tos/networking/)
9. [Docker Volumes](https://docs.docker.com/engine/storage/volumes/)
10. [Docker Compose Healthcheck](https://docs.docker.com/reference/compose-file/services/#healthcheck)
11. [asyncpg Documentation](https://magicstack.github.io/asyncpg/current/)
12. [MCP Specification](https://modelcontextprotocol.io/specification)
13. [Cloud SQL - Connect from Cloud Run](https://cloud.google.com/sql/docs/postgres/connect-run)
14. [Cloud SQL - IAM Authentication](https://cloud.google.com/sql/docs/postgres/iam-authentication)
