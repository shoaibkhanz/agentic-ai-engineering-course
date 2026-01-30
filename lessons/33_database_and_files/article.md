# Lesson 33: From Filesystem to Cloud SQL: Production-Ready Data for AI Agents

In Lesson 32, we took the first major steps toward production readiness by implementing OAuth 2.0 authentication with Descope and containerizing our research agent with Docker. We identified a four-part plan to transform our local prototype into a cloud-native application: (1) adopting stateless data storage, (2) implementing user authentication, (3) handling file uploads and downloads, and (4) containerizing the application. With authentication and Docker now complete, this lesson tackles the remaining pieces: replacing the local filesystem with a PostgreSQL database and implementing workarounds for file transfers that the MCP specification does not yet support.

The transition from file-based to database-backed storage represents a fundamental shift in how our agent manages state. In `research_agent_part_2`, every piece of data lived in a `.nova/` folder on the local filesystem. This approach worked for single-user development but fails catastrophically in production.

In a serverless environment like Cloud Run, container instances are ephemeral; they can be replaced at any moment, and any data written to the local filesystem is lost. Furthermore, with multiple users accessing the agent simultaneously, their data would intermingle and become corrupted without a proper isolation mechanism.

By moving all state to a PostgreSQL database, we achieve three essential goals. First, data persists beyond the lifetime of any single container. Second, each user's data is strictly isolated from others. Finally, we gain powerful query capabilities that unlock new features. This lesson also introduces a bonus feature enabled by our database: rate limiting for MCP tools. Since each tool call can trigger expensive LLM API requests, we need a way to track and limit usage per user. The database makes this straightforward by recording every tool invocation and checking usage counts before allowing new calls.

## Section 1 — Choosing a Database

Now that you understand why file-based storage fails in production, let's evaluate database options and justify our choice. The first major decision when moving from file-based to database-backed storage is choosing the right database technology. Before committing to a specific solution, it is worth considering the alternatives and understanding why PostgreSQL emerged as the best choice for our use case.

### Why We Need a Database

Serverless platforms like Cloud Run impose constraints that make local file storage impractical:

*   **Ephemeral Containers:** Container instances can be created, destroyed, or replaced at any time. Any data written to the local filesystem is lost when this happens.
*   **Multi-User Isolation:** Multiple users will access our agent simultaneously. Without a database, their data would intermingle in the same files, causing overwrites and corruption.
*   **Query Capabilities:** Features like rate limiting require counting records efficiently. A database provides indexing and query optimization that file-based storage cannot match [[6]](https://docs.cloud.google.com/run/docs/container-contract), [[15]](https://github.com/ahmetb/cloud-run-faq/blob/master/README.md), [[16]](https://www.crunchydata.com/blog/designing-your-postgres-database-for-multi-tenancy), [[17]](https://www.postgresql.org/docs/current/using-explain.html).

### Why PostgreSQL

After evaluating several alternatives, PostgreSQL emerged as the ideal choice. SQLite is excellent for embedded or single-user applications but is not designed for multi-container deployments where multiple processes access the same database over a network, leading to locking issues and data corruption. MySQL and MariaDB are solid relational databases, but their JSON support, while improved, is less powerful than PostgreSQL's JSONB type, which offers advanced indexing and a richer set of operators for querying semi-structured data. Document databases like MongoDB are great for unstructured data but less suited for the relational aspects of our schema. Finally, managed services like Firebase/Firestore can lead to vendor lock-in and have more limited query capabilities [[7]](https://www.sqlite.org/whentouse.html), [[18]](https://sqlite.org/faq.html), [[19]](https://dev.to/harry_do/part-3-mysql-vs-postgresql-features-capabilities-comparison-13gj).

PostgreSQL provides ACID transactions for data integrity, native JSON/JSONB columns perfect for storing structured data like extracted URLs, and high-performance asynchronous support through the `asyncpg` driver. It also offers excellent integration with Google Cloud SQL and has a rich Python ecosystem with powerful tools like SQLAlchemy for object-relational mapping (ORM) and Alembic for database migrations [[1]](https://www.postgresql.org/docs/current/datatype-json.html), [[2]](https://www.sqlalchemy.org/), [[3]](https://alembic.sqlalchemy.org/), [[5]](https://cloud.google.com/sql/docs/postgres), [[11]](https://magicstack.github.io/asyncpg/current/).

## Section 2 — Database Schema Design

With PostgreSQL selected, let's design a schema that captures all the data our research agent needs to persist. The schema must replace every file that `research_agent_part_2` stored in the `.nova/` folder while also supporting multi-user access through user ID associations.

### The Article Model

The `Article` model is the central entity in our schema, replacing the research folder and its `.nova/` subdirectory. Every piece of data that was previously a file now becomes a column on this table.

1.  We start by defining the class, table name, and primary key. We use a UUID for the `id` to allow for client-side generation and prevent information leakage.

    ```python
    # research_agent_part_3/src/db/models.py
    
    class Article(Base):
        """
        Main research article entity.
    
        Stores the article guideline and all intermediate outputs from the research workflow.
        Each article belongs to a user (identified by user_id from Descope).
        """
    
        __tablename__ = "articles"
    
        # Primary key - article ID
        id: Mapped[uuid.UUID] = mapped_column(
            UUID(as_uuid=True),
            primary_key=True,
            default=uuid.uuid4,
            comment="Unique article identifier",
        )
    ```

2.  Next, we add columns for user association and the core content: the guideline text and the workflow status. The `user_id` is indexed for fast lookups.

    ```python
    # research_agent_part_3/src/db/models.py
    
        # User association (from Descope authentication)
        user_id: Mapped[str] = mapped_column(
            Text,
            nullable=False,
            index=True,
            comment="User ID from Descope authentication",
        )
    
        # Article guideline content (the uploaded article_guideline.md)
        guideline_text: Mapped[str] = mapped_column(
            Text,
            nullable=False,
            comment="Full content of the article guideline markdown file",
        )
    
        # Workflow status
        status: Mapped[ArticleStatus] = mapped_column(
            Enum(ArticleStatus, name="article_status", create_type=False),
            default=ArticleStatus.CREATED,
            nullable=False,
            comment="Current status of the research workflow",
        )
    ```

3.  We then define columns that replace the files previously stored in the `.nova/` directory. A native JSON column holds the extracted URLs, while `Text` columns store the various markdown outputs.

    ```python
    # research_agent_part_3/src/db/models.py
    
        # Replaces: .nova/guidelines_filenames.json
        extracted_urls: Mapped[dict | None] = mapped_column(
            JSON,
            nullable=True,
            comment="Extracted URLs from guidelines (JSON): github_urls, youtube_videos_urls, other_urls",
        )
    
        # Replaces: .nova/perplexity_results.md
        perplexity_results: Mapped[str | None] = mapped_column(
            Text,
            nullable=True,
            comment="Raw Perplexity research results (markdown format)",
        )
    
        # Replaces: .nova/perplexity_results_selected.md
        perplexity_results_selected: Mapped[str | None] = mapped_column(
            Text,
            nullable=True,
            comment="Filtered Perplexity results (markdown format)",
        )
    
        # Replaces: research.md
        research: Mapped[str | None] = mapped_column(
            Text,
            nullable=True,
            comment="Final comprehensive research markdown content",
        )
    ```

4.  Finally, we add automatic timestamps to track when records are created and updated.

    ```python
    # research_agent_part_3/src/db/models.py
    
        # Timestamps
        created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False,
        )
    
        updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )
    ```

The key design decisions in this model are:

*   **UUID Primary Key:** Using UUIDs instead of auto-incrementing integers allows us to generate IDs client-side and prevents information leakage about how many articles exist. While UUIDs take up more space (16 bytes vs. 8 for a bigint), the performance penalty in PostgreSQL is minimal for the security and sharding benefits they provide.
*   **User ID Index:** The `user_id` column is indexed for fast lookups when querying a user's articles.
*   **JSON Column:** The `extracted_urls` field uses PostgreSQL's native JSON type to store structured data that would otherwise require multiple tables.
*   **Status Enum:** A PostgreSQL enum tracks the workflow state, enabling queries like "show me all failed articles" [[20]](https://www.cybertec-postgresql.com/en/int4-vs-int8-vs-uuid-vs-numeric-performance-on-bigger-joins/), [[19]](https://dev.to/harry_do/part-3-mysql-vs-postgresql-features-capabilities-comparison-13gj).

### Supporting Tables

The research workflow generates several types of content that warrant their own tables, each linked to an article through a foreign key:

*   **LocalFile:** Stores user-uploaded reference files that accompany the article guideline.
*   **ScrapedUrl:** Contains web content scraped from URLs found in the article guideline.
*   **GitHubIngest:** Holds the results of processing GitHub repositories with GitIngest.
*   **YouTubeTranscript:** Stores transcriptions of YouTube videos referenced in the guideline.
*   **ScrapedResearchUrl:** Contains content from URLs discovered during Perplexity research.

Each supporting table follows the same pattern: a UUID primary key, a `user_id` for ownership, an `article_guideline_id` foreign key linking to the parent article, content-specific columns, and a creation timestamp.

```python
# research_agent_part_3/src/db/models.py

class ScrapedUrl(Base):
    """Scraped and cleaned URLs from article guidelines."""

    __tablename__ = "scraped_urls"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    article_guideline_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("articles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    url: Mapped[str] = mapped_column(Text, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
```

### Schema Diagram

The following diagram illustrates the relationships between our database tables. The `Article` table sits at the center, with all supporting tables referencing it through foreign keys. The `ToolCallUsage` table stands alone, tracking tool invocations for rate limiting.

```mermaid
erDiagram
    Article {
        uuid id PK
        string user_id
        string guideline_text
        enum status
        json extracted_urls
        string perplexity_results
        string perplexity_results_selected
        string urls_to_scrape_from_research
        string research
        datetime created_at
        datetime updated_at
    }

    LocalFile {
        uuid id PK
        string user_id
        uuid article_guideline_id FK
        string filename
        string content
        datetime created_at
    }

    ScrapedUrl {
        uuid id PK
        string user_id
        uuid article_guideline_id FK
        string url
        string content
        datetime created_at
    }

    GitHubIngest {
        uuid id PK
        string user_id
        uuid article_guideline_id FK
        string github_url
        string gitingest_result
        datetime created_at
    }

    YouTubeTranscript {
        uuid id PK
        string user_id
        uuid article_guideline_id FK
        string youtube_url
        string transcription
        datetime created_at
    }

    ScrapedResearchUrl {
        uuid id PK
        string user_id
        uuid article_guideline_id FK
        string url
        string content
        datetime created_at
    }

    ToolCallUsage {
        uuid id PK
        string user_id
        string tool_name
        string year_month
        datetime created_at
    }

    Article ||--o{ LocalFile : "has"
    Article ||--o{ ScrapedUrl : "has"
    Article ||--o{ GitHubIngest : "has"
    Article ||--o{ YouTubeTranscript : "has"
    Article ||--o{ ScrapedResearchUrl : "has"
```

Image 1: Entity-relationship diagram showing the database schema. The Article table is the central entity, with supporting tables linked via foreign keys. The ToolCallUsage table tracks tool invocations independently for rate limiting.

## Section 3 — Refactoring Tools: From Files to Database

Now that you understand the schema, let's see how MCP tools transform from file-based to database-backed implementations. Every tool follows the same transformation pattern: what was once a file path parameter becomes a UUID, file reads become database queries, and file writes become database updates.

### The Transformation Pattern

The refactoring pattern is consistent across all tools:

*   **Before (Part 2):** Tools accept a `research_folder` path, read from files like `article_guideline.md`, and write to files in the `.nova/` subdirectory.
*   **After (Part 3):** Tools accept an `article_guideline_id` UUID, query the `Article` table for data, and update columns or insert rows in related tables.

### Example: extract_guidelines_urls_tool

Let's examine the `extract_guidelines_urls_tool` to see this pattern in action. This tool extracts URLs from the article guideline and categorizes them into GitHub URLs, YouTube URLs, and other web URLs.

**Part 2 (File-Based Implementation):**

```python
# research_agent_part_2/mcp_server/src/tools/extract_guidelines_urls_tool.py

def extract_guidelines_urls_tool(research_folder: str) -> Dict[str, Any]:
    """Extract URLs from the article guidelines in the research folder."""
    
    # Convert to Path object
    research_path = Path(research_folder)
    nova_path = research_path / NOVA_FOLDER
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE

    # Create NOVA_FOLDER directory if it doesn't exist
    nova_path.mkdir(parents=True, exist_ok=True)

    # Read the guidelines file from filesystem
    text = guidelines_path.read_text(encoding="utf-8")

    # Extract and categorize URLs
    all_urls = extract_urls(text)
    github_source_urls = [u for u in all_urls if "github.com" in u]
    youtube_source_urls = [u for u in all_urls if "youtube.com" in u]
    web_source_urls = [u for u in all_urls if "github.com" not in u and "youtube.com" not in u]

    data = {
        "github_urls": github_source_urls,
        "youtube_videos_urls": youtube_source_urls,
        "other_urls": web_source_urls,
    }

    # Write results to JSON file
    output_path = nova_path / GUIDELINES_FILENAMES_FILE
    output_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    return {"status": "success", "output_path": str(output_path)}
```

**Part 3 (Database-Based Implementation):**

```python
# research_agent_part_3/src/tools/extract_guidelines_urls_tool.py

async def extract_guidelines_urls_tool(article_guideline_id: str) -> Dict[str, Any]:
    """Extract URLs from the article guidelines in the database."""

    # Convert string to UUID
    article_uuid = uuid.UUID(article_guideline_id)

    # Query database for article
    session_factory = await get_async_session_factory()
    async with session_factory() as session:
        article = await session.get(Article, article_uuid)

        if not article:
            raise ValueError(f"Article with ID '{article_guideline_id}' not found")

        # Read the guidelines text from the database column
        text = article.guideline_text

        # Extract and categorize URLs (same logic as before)
        all_urls = extract_urls(text)
        github_source_urls = [u for u in all_urls if "github.com" in u]
        youtube_source_urls = [u for u in all_urls if "youtube.com" in u]
        web_source_urls = [u for u in all_urls if "github.com" not in u and "youtube.com" not in u]

        data = {
            "github_urls": github_source_urls,
            "youtube_videos_urls": youtube_source_urls,
            "other_urls": web_source_urls,
        }

        # Save to database column instead of file
        article.extracted_urls = data
        await session.commit()

    return {"status": "success", "message": "Results saved to database"}
```

The key differences are:

1.  **Input Parameter:** `research_folder: str` becomes `article_guideline_id: str` (a UUID).
2.  **Data Source:** `guidelines_path.read_text()` becomes `article.guideline_text`.
3.  **Data Destination:** `output_path.write_text(json.dumps(data))` becomes `article.extracted_urls = data`.
4.  **Async:** The function becomes `async` to support non-blocking database operations.

This same pattern applies to all other tools in the research workflow. The business logic remains unchanged; only the storage layer is different.

## Section 4 — Local Development with Docker Compose

With our tools refactored for database access, you need a way to run PostgreSQL during development. Docker Compose is a good way to manage this by defining our multi-container application in a single YAML file. With one command, we can spin up both the PostgreSQL database and our MCP server.

### The Two-Service Architecture

Our `docker-compose.yml` defines two services that work together.

1.  First, we define the `postgres` service. We use the lightweight `postgres:16-alpine` image, configure it with environment variables, and map the container's port 5432 to the host. A named volume ensures data persistence, and a health check verifies the database is ready before other services start.

    ```yaml
    # research_agent_part_3/docker-compose.yml
    
    services:
      # PostgreSQL Database
      postgres:
        image: postgres:16-alpine
        container_name: nova-postgres
        environment:
          POSTGRES_USER: ${POSTGRES_USER:-nova}
          POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-nova_dev_password}
          POSTGRES_DB: ${POSTGRES_DB:-nova_research}
        ports:
          - "${POSTGRES_PORT:-5432}:5432"
        volumes:
          - postgres_data:/var/lib/postgresql/data
        healthcheck:
          test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-nova} -d ${POSTGRES_DB:-nova_research}"]
          interval: 5s
          timeout: 5s
          retries: 5
        restart: unless-stopped
    ```

2.  Next, we define the `mcp-server` service. It builds from our local `Dockerfile` and depends on the `postgres` service being healthy. The `DATABASE_URL` uses the service name `postgres` as the hostname, which Docker's internal networking resolves. We also mount the source code as a read-only volume to enable hot-reloading during development.

    ```yaml
    # research_agent_part_3/docker-compose.yml
    
      # Nova MCP Server
      mcp-server:
        build:
          context: .
          dockerfile: Dockerfile
        container_name: nova-mcp-server
        depends_on:
          postgres:
            condition: service_healthy
        environment:
          DATABASE_URL: postgresql+asyncpg://${POSTGRES_USER:-nova}:${POSTGRES_PASSWORD:-nova_dev_password}@postgres:5432/${POSTGRES_DB:-nova_research}
          SERVER_HOST: 0.0.0.0
          SERVER_PORT: 8000
          # API Keys passed through from host .env
          GOOGLE_API_KEY: ${GOOGLE_API_KEY}
          OPENAI_API_KEY: ${OPENAI_API_KEY}
          PPLX_API_KEY: ${PPLX_API_KEY}
          # ... other environment variables
        ports:
          - "${SERVER_PORT:-8000}:8000"
        volumes:
          - ./src:/app/src:ro
        restart: unless-stopped
    ```

3.  Finally, we declare the named volume for PostgreSQL data.

    ```yaml
    # research_agent_part_3/docker-compose.yml
    
    volumes:
      postgres_data:
        driver: local
    ```

### Key Configuration Elements

Several aspects of this configuration deserve explanation:

*   **Docker Network Hostname:** The `DATABASE_URL` uses `postgres` as the hostname, which Docker's internal networking resolves to the PostgreSQL container's IP address. This works because both containers share the same Docker network by default.

*   **Named Volume:** The `postgres_data` volume persists database files outside the container. When you run `docker compose down`, the data survives. Only `docker compose down -v` removes the volume.

*   **Health Check:** The `pg_isready` command verifies PostgreSQL is accepting connections. The MCP server's `depends_on: condition: service_healthy` ensures it waits for a healthy database before starting.

*   **Source Mount:** Mounting `./src:/app/src:ro` allows code changes during development without rebuilding the container, while `:ro` (read-only) prevents the container from modifying host files [[8]](https://docs.docker.com/compose/how-tos/networking/), [[9]](https://docs.docker.com/engine/storage/volumes/), [[10]](https://docs.docker.com/reference/compose-file/services/#healthcheck).

### Development Commands

Show the common commands:

```bash
# Build and start both services in detached mode
docker compose up -d

# View logs for the MCP server
docker compose logs -f mcp-server

# Stop services but preserve the data volume
docker compose down

# Stop services and remove the data volume
docker compose down -v
```

## Section 5 — Cloud SQL for Production

Docker Compose works for local development, but production requires a managed database service. Cloud SQL provides fully managed PostgreSQL with automatic backups and IAM authentication.

### What is Cloud SQL

Cloud SQL is Google Cloud's fully managed relational database service supporting PostgreSQL, MySQL, and SQL Server. For production deployments, it offers several advantages over self-managed databases:

*   **Automatic Backups:** Daily backups with point-in-time recovery and configurable retention periods.
*   **High Availability:** Optional regional instances with automatic failover.
*   **Security Patches:** Google applies security updates without downtime.
*   **Private Connectivity:** Cloud Run can connect to Cloud SQL over a private IP, never exposing the database to the public internet.
*   **IAM Authentication:** Instead of managing passwords, Cloud Run can authenticate using its service account [[5]](https://cloud.google.com/sql/docs/postgres), [[13]](https://cloud.google.com/sql/docs/postgres/connect-run), [[14]](https://cloud.google.com/sql/docs/postgres/iam-authentication).

### Environment-Based Configuration

Our application must work in two environments: local development with Docker Compose and production with Cloud SQL. We achieve this through environment-based configuration in `settings.py`:

```python
# research_agent_part_3/src/config/settings.py

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Database settings (local PostgreSQL)
    database_url: str = Field(
        default="postgresql+asyncpg://nova:nova_dev_password@localhost:5432/nova_research",
        alias="DATABASE_URL",
        description="PostgreSQL connection URL - used for local development",
    )

    # Cloud SQL settings (GCP deployment)
    cloud_sql_instance: str | None = Field(
        default=None,
        alias="CLOUD_SQL_INSTANCE",
        description="Cloud SQL instance connection name (e.g., project:region:instance)",
    )
    db_user: str = Field(default="nova", alias="DB_USER")
    db_pass: SecretStr | None = Field(default=None, alias="DB_PASS")
    db_name: str = Field(default="nova_research", alias="DB_NAME")

    @property
    def is_cloud_sql(self) -> bool:
        """Check if running with Cloud SQL configuration."""
        return self.cloud_sql_instance is not None
```

The `is_cloud_sql` property provides a simple check: if the `CLOUD_SQL_INSTANCE` environment variable is set, we are running in production; otherwise, we use the local `DATABASE_URL`.

### The Cloud SQL Python Connector

The database session management in `session.py` handles both environments transparently. The key is the `_init_database()` function, which creates the appropriate SQLAlchemy engine based on the environment:

```python
# research_agent_part_3/src/db/session.py

async def _init_database() -> tuple[AsyncEngine, async_sessionmaker]:
    """Initialize database connection for the current event loop."""
    
    connector = None
    if settings.is_cloud_sql:
        # Cloud SQL mode: use the Cloud SQL Python Connector
        from google.cloud.sql.connector import create_async_connector

        # create_async_connector() binds to the current event loop
        # refresh_strategy="lazy" is recommended for Cloud Run
        connector = await create_async_connector(refresh_strategy="lazy")

        async def get_cloud_sql_conn():
            """Create an asyncpg connection to Cloud SQL."""
            return await connector.connect_async(
                settings.cloud_sql_instance,
                "asyncpg",
                user=settings.db_user,
                password=settings.db_pass.get_secret_value() if settings.db_pass else "",
                db=settings.db_name,
            )

        engine = create_async_engine(
            "postgresql+asyncpg://",
            async_creator=get_cloud_sql_conn,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10,
        )
    else:
        # Local development mode: use DATABASE_URL directly
        engine = create_async_engine(
            settings.database_url,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10,
        )

    session_factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    return engine, session_factory
```

The Cloud SQL Python Connector provides several benefits over direct connection strings:

*   **IAM Authentication:** Connects using the Cloud Run service account's identity instead of passwords.
*   **Automatic Certificate Handling:** Manages SSL certificates transparently.
*   **Connection Pooling:** Efficiently manages database connections.
*   **Lazy Refresh:** The `refresh_strategy="lazy"` option is optimized for serverless environments like Cloud Run, where CPU may be throttled between requests. This strategy retrieves connection info only when needed, rather than in a periodic background thread [[4]](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector), [[21]](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/google/cloud/sql/connector/connector.py).

## Section 6 — Database Migrations with Alembic

Whether running locally or in the cloud, you need a way to evolve the database schema over time. Adding a new column, creating a new table, or modifying an index requires careful coordination between code changes and database changes. Alembic provides database migrations for SQLAlchemy, acting as version control for your database schema.

### What is Alembic

Alembic is a database migration tool created by the author of SQLAlchemy. It addresses a fundamental challenge: your SQLAlchemy models define what the schema *should* be, but the database might have an older schema. Alembic bridges this gap by:

*   **Version Control:** Each migration has a unique revision ID, creating a linear history of schema changes.
*   **Upgrade/Downgrade:** Migrations define both `upgrade()` (apply changes) and `downgrade()` (rollback) functions.
*   **Autogeneration:** Alembic can compare your models to the database and generate migration scripts automatically.
*   **Environment Support:** The same migrations run in development, staging, and production [[3]](https://alembic.sqlalchemy.org/), [[22]](https://testdriven.io/blog/alembic-database-migrations/), [[23]](https://alembic.sqlalchemy.org/en/latest/autogenerate.html).

### Alembic Configuration

Our Alembic setup consists of two key files: `alembic.ini` for configuration and `env.py` for runtime behavior.

```ini
# research_agent_part_3/alembic.ini

[alembic]
script_location = alembic
file_template = %%(year)d%%(month).2d%%(day).2d_%%(hour).2d%%(minute).2d%%(second).2d_%%(rev)s_%%(slug)s

# The SQLAlchemy URL is loaded from environment/settings in env.py
# sqlalchemy.url is intentionally NOT set here for security
```

The `env.py` file handles async database connections and supports both local PostgreSQL and Cloud SQL:

```python
# research_agent_part_3/alembic/env.py

async def run_async_migrations() -> None:
    """Run migrations with async engine, supporting both local and Cloud SQL."""
    
    if settings.is_cloud_sql:
        # Cloud SQL mode: use the Cloud SQL Python Connector
        from google.cloud.sql.connector import create_async_connector

        connector = await create_async_connector(refresh_strategy="lazy")

        async def get_cloud_sql_conn():
            return await connector.connect_async(
                settings.cloud_sql_instance, "asyncpg",
                user=settings.db_user,
                password=settings.db_pass.get_secret_value() if settings.db_pass else "",
                db=settings.db_name,
            )

        connectable = create_async_engine(
            "postgresql+asyncpg://",
            async_creator=get_cloud_sql_conn,
            poolclass=pool.NullPool,
        )
    else:
        # Local development: use DATABASE_URL
        connectable = async_engine_from_config(
            config.get_section(config.config_ini_section, {}),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()
```

### Migration Examples

Let's examine two migrations from our project to understand Alembic's capabilities.

**Example 1: Creating the Articles Table**

The first migration creates the main `articles` table with its enum type and all columns:

```python
# research_agent_part_3/alembic/versions/20241211_000000_001_create_articles_table.py

revision: str = "001"
down_revision: Union[str, None] = None  # First migration

def upgrade() -> None:
    """Create the articles table."""
    
    # Create the article_status enum type with idempotent SQL
    op.execute("""
        DO $$ BEGIN
            CREATE TYPE article_status AS ENUM (
                'created', 'extracting_urls', 'processing_sources',
                'researching', 'selecting_sources', 'scraping_research',
                'finalizing', 'completed', 'failed'
            );
        EXCEPTION
            WHEN duplicate_object THEN null;
        END $$;
    """)

    # Create the articles table
    op.create_table(
        "articles",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text("gen_random_uuid()")),
        sa.Column("user_id", sa.Text(), nullable=False, index=True),
        # ... more columns
    )

def downgrade() -> None:
    """Drop the articles table."""
    op.drop_table("articles")
    op.execute("DROP TYPE IF EXISTS article_status")
```

**Example 2: Adding the Rate Limiting Table**

A later migration adds the `tool_call_usage` table for rate limiting:

```python
# research_agent_part_3/alembic/versions/20241216_000000_008_create_tool_call_usage_table.py

revision: str = "008"
down_revision: Union[str, None] = "007"  # Depends on previous migration

def upgrade() -> None:
    """Create the tool_call_usage table."""
    op.create_table(
        "tool_call_usage",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text("gen_random_uuid()")),
        sa.Column("user_id", sa.Text(), nullable=False),
        sa.Column("tool_name", sa.Text(), nullable=False),
        sa.Column("year_month", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )

    # Composite index for efficient user+month queries
    op.create_index("ix_tool_call_usage_user_month", "tool_call_usage", ["user_id", "year_month"])
    op.create_index("ix_tool_call_usage_user_id", "tool_call_usage", ["user_id"])

def downgrade() -> None:
    """Drop the tool_call_usage table."""
    op.drop_index("ix_tool_call_usage_user_id", table_name="tool_call_usage")
    op.drop_index("ix_tool_call_usage_user_month", table_name="tool_call_usage")
    op.drop_table("tool_call_usage")
```

### Running Migrations

In development, run migrations manually:

```bash
# Apply all pending migrations to the latest version
alembic upgrade head

# Rollback one migration from the current state
alembic downgrade -1

# View the current database revision
alembic current
```

In production, the Docker entrypoint script runs migrations automatically on container startup, ensuring the database schema is always up-to-date before the application starts accepting requests.

```bash
# research_agent_part_3/docker-entrypoint.sh

#!/bin/bash
set -e

echo "Running database migrations..."
alembic upgrade head

echo "Starting MCP server..."
exec uvicorn src.server:mcp --host 0.0.0.0 --port 8000
```
[[24]](https://www.youtube.com/watch?v=91j6zOoIP4g)
## Section 7 — Rate Limiting for MCP Tools

With the database infrastructure in place, we can now implement features that require persistent storage. Rate limiting is a perfect example: it needs to track usage across requests and even container restarts. Without a database, we would have no way to know how many tool calls a user has made this month.

### Why Rate Limiting Matters

MCP tools are not free to operate. Each tool call can trigger expensive API requests:

*   **LLM Calls:** Perplexity research, source selection, and query generation all invoke paid LLM APIs.
*   **Web Scraping:** Firecrawl charges per page scraped.
*   **YouTube Transcription:** Processing videos consumes compute resources.

Without rate limiting, a single user could exhaust your API budget in minutes. Rate limiting also enables future business models: in the current implementation, all users share the same monthly limit, but the system could be extended to support premium users with higher limits.

### The ToolCallUsage Model

The `ToolCallUsage` model records every tool invocation:

```python
# research_agent_part_3/src/db/models.py

class ToolCallUsage(Base):
    """Track MCP tool calls per user for rate limiting."""

    __tablename__ = "tool_call_usage"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[str] = mapped_column(Text, nullable=False)
    tool_name: Mapped[str] = mapped_column(Text, nullable=False)
    year_month: Mapped[str] = mapped_column(Text, nullable=False)  # e.g., "2026-01"
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("ix_tool_call_usage_user_month", "user_id", "year_month"),
        Index("ix_tool_call_usage_user_id", "user_id"),
    )
```

The `year_month` column is a deliberate denormalization. We could extract the month from `created_at`, but storing it explicitly enables a simple, indexed query: `SELECT COUNT(*) WHERE user_id = ? AND year_month = ?`. This is a common pattern for optimizing analytics queries [[25]](https://neon.com/guides/rate-limiting).

### The @rate_limited Decorator

The rate limiting logic is encapsulated in a decorator that wraps MCP tools:

```python
# research_agent_part_3/src/utils/rate_limit_utils.py

class RateLimitExceededError(Exception):
    """Raised when a user exceeds their monthly tool call limit."""
    # ... implementation ...

async def check_and_record_tool_call(user_id: str, tool_name: str) -> int:
    """Check if user has remaining quota and record the tool call."""
    
    if settings.monthly_tool_call_limit == 0:
        return 0  # Unlimited

    year_month = datetime.now(UTC).strftime("%Y-%m")

    session_factory = await get_async_session_factory()
    async with session_factory() as session:
        # Count existing calls this month
        stmt = select(func.count()).select_from(ToolCallUsage).where(
            ToolCallUsage.user_id == user_id,
            ToolCallUsage.year_month == year_month,
        )
        result = await session.execute(stmt)
        current_count = result.scalar() or 0

        # Check if limit exceeded
        if current_count >= settings.monthly_tool_call_limit:
            raise RateLimitExceededError(user_id, current_count, settings.monthly_tool_call_limit)

        # Record this tool call
        usage = ToolCallUsage(user_id=user_id, tool_name=tool_name, year_month=year_month)
        session.add(usage)
        await session.commit()

        return current_count + 1


def rate_limited(func):
    """Decorator to enforce rate limiting on MCP tools."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Get user ID from access token
        token = get_access_token()
        user_id = token.claims["sub"]

        # Check rate limit and record the call
        await check_and_record_tool_call(user_id, func.__name__)

        # Execute the actual tool
        return await func(*args, **kwargs)

    return wrapper
```

### Applying Rate Limiting to Tools

Every tool in `tools.py` is decorated with `@rate_limited`:

```python
# research_agent_part_3/src/routers/tools.py

@mcp.tool()
@opik.track(type="tool")
@rate_limited
async def extract_guidelines_urls(article_guideline_id: str) -> Dict[str, Any]:
    """Extract URLs from article guidelines."""
    # ... implementation
```

## Section 8 — File Handling: Upload and Download Workarounds

The database handles state, and rate limiting protects your budget. But there's another challenge the MCP specification doesn't address: file transfers. Let's implement workarounds using custom HTTP endpoints.

### The MCP Protocol Gap

When running locally with `stdio` transport, file handling is straightforward: the agent can read files from the user's filesystem. But HTTP transport is different. The MCP client (Cursor) and MCP server may be on different machines, and there's no MCP message type for "upload this file" or "download this file." Users need to upload article guidelines before research can begin.

The MCP specification is actively evolving and may address file handling in future versions. For now, we implement a workaround using custom HTTP endpoints [[12]](https://modelcontextprotocol.io/specification).

### Our Solution: Custom HTTP Endpoints

FastMCP allows adding custom HTTP routes alongside MCP endpoints using the `@mcp.custom_route()` decorator. These routes are regular FastAPI endpoints that exist outside the MCP protocol [[26]](https://blog.jcharistech.com/2022/12/11/create-an-upload-and-download-files-api-endpoint-with-fastapi/).

### The Upload Flow

The upload flow involves coordination between the user, the AI agent, and the MCP server:

```mermaid
sequenceDiagram
    participant User
    participant "AI Agent (Cursor)" as Agent
    participant Browser
    participant "MCP Server" as MCPServer
    participant Database

    User->>Agent: "Initiate research"
    Agent->>Agent: "Retrieve user_id from auth token"
    Agent-->>User: "Provide URL for guideline upload"
    User->>Browser: "Open URL"
    Browser->>MCPServer: "Request upload form"
    MCPServer-->>Browser: "Serve HTML upload form"
    User->>Browser: "Upload markdown file"
    Browser->>MCPServer: "Send markdown file"
    MCPServer->>Database: "Create 'Article' record"
    Database-->>MCPServer: "Return article UUID"
    MCPServer-->>User: "Display article UUID"
    User->>Agent: "Provide article UUID"
    Agent->>MCPServer: "Call tools with article_guideline_id"
```

Image 2: Sequence diagram for user uploading an article guideline.

The implementation in `upload_ui.py` handles the POST request, parses the multipart form data, and creates a new `Article` record in the database.

### The Download Flow

At the end of the research workflow, we need a way for users to download the final research document. The same custom route approach applies.

```mermaid
sequenceDiagram
    participant "AI Agent (Cursor)" as AIC
    participant "MCP Server" as MCPS
    participant "Database" as DB
    participant "User"

    AIC->>MCPS: "Call create_research_file(article_id)"
    MCPS->>DB: "Query for relevant research data"
    DB-->>MCPS: "Return scraped content, transcripts, etc."
    MCPS->>MCPS: "Compile comprehensive markdown document"
    MCPS->>DB: "Save to Article.research column"
    DB-->>MCPS: "Confirmation"
    MCPS-->>AIC: "Return download URL"
    AIC->>User: "Provide download URL"
    User->>MCPS: "Open URL in browser"
    MCPS->>DB: "Query Article.research column"
    DB-->>MCPS: "Return markdown content"
    MCPS-->>User: "Return file with Content-Disposition: attachment"
    User->>User: "Download research.md"
```

Image 3: Sequence diagram illustrating the process of a user downloading the final research document.

The download route, defined in `downloads.py`, queries the database for the completed research content and returns it as a downloadable markdown file.

## Section 9 — Analytics and Monitoring

All this usage data, including tool calls, articles created, and research completed, lives in our database. This opens up powerful analytics possibilities that were impossible with file-based storage.

### What the Database Captures

Our schema provides rich data for analysis:

*   **Tool Usage:** Every tool call is recorded in `tool_call_usage` with user, tool name, and timestamp.
*   **Article Lifecycle:** The `articles` table tracks status transitions from `created` through `completed` or `failed`.
*   **Research Artifacts:** All intermediate data is preserved for debugging.

### Example Analytics Queries

Here are some queries you might run to understand your agent's usage:

```sql
-- Monthly tool calls per user
SELECT user_id, year_month, COUNT(*) as calls
FROM tool_call_usage
GROUP BY user_id, year_month
ORDER BY year_month DESC, calls DESC;

-- Most popular tools
SELECT tool_name, COUNT(*) as usage
FROM tool_call_usage
GROUP BY tool_name
ORDER BY usage DESC;

-- Research completion rate
SELECT status, COUNT(*) as count
FROM articles
GROUP BY status;

-- Users approaching rate limit
SELECT user_id, COUNT(*) as calls
FROM tool_call_usage
WHERE year_month = to_char(now(), 'YYYY-MM')
GROUP BY user_id
HAVING COUNT(*) > 80 -- Assuming a limit of 100
ORDER BY calls DESC;
```
[[27]](https://www.tigerdata.com/learn/guide-to-data-analysis-on-postgresql), [[28]](https://www.postgresql.org/docs/current/monitoring-stats.html)
### Preview: Querying Cloud SQL

Once deployed, you can run these queries directly in Google Cloud Console's Cloud SQL Studio, or connect via the `gcloud` CLI:

```bash
# Connect to Cloud SQL instance
gcloud sql connect nova-db --user=nova --database=nova_research
```

We will cover Cloud SQL querying in detail in Lesson 34 after deploying the application.

## Section 10 — Conclusion

This lesson addressed the core infrastructure challenges of preparing an AI agent for production deployment. We transformed our research agent from a file-based prototype into a database-backed, rate-limited, cloud-ready application.

### Summary of Changes

*   **Database Integration:** Replaced the ephemeral `.nova/` folder with persistent PostgreSQL storage, ensuring data survives container restarts and can be queried efficiently.
*   **Schema Design:** Created an article-centric data model with supporting tables for research artifacts, each linked to users through authentication.
*   **Tool Refactoring:** Updated all MCP tools to read from and write to database columns instead of filesystem paths.
*   **Environment Flexibility:** Designed the application to use Docker Compose with local PostgreSQL for development and Cloud SQL for production.
*   **Schema Evolution:** Implemented Alembic migrations to version-control database changes, with automatic migration on container startup.
*   **Rate Limiting:** Added usage tracking and monthly limits to protect API budgets and enable future tiered pricing models.
*   **File Handling:** Worked around MCP's lack of file transfer support by implementing custom HTTP endpoints for upload and download.

### What's Next in Lesson 34

With our agent fully prepared for production, the next lesson covers the actual deployment:

*   **Google Cloud Run Deployment:** Pushing our container to Artifact Registry and deploying to Cloud Run.
*   **Cloud SQL Setup:** Creating and configuring the production database instance.
*   **Continuous Deployment:** Setting up GitHub Actions to automatically deploy on push to main.
*   **Monitoring and Logging:** Using Cloud Logging and Cloud Monitoring to observe our agent in production.

## References

1. PostgreSQL Global Development Group. (n.d.). *JSON types*. PostgreSQL Documentation. https://www.postgresql.org/docs/current/datatype-json.html
2. SQLAlchemy. (n.d.). *SQLAlchemy documentation*. https://www.sqlalchemy.org/
3. Alembic. (n.d.). *Alembic documentation*. https://alembic.sqlalchemy.org/
4. Google. (n.d.). *Cloud SQL Python Connector*. GitHub. https://github.com/GoogleCloudPlatform/cloud-sql-python-connector
5. Google. (n.d.). *Cloud SQL for PostgreSQL documentation*. Google Cloud. https://cloud.google.com/sql/docs/postgres
6. Google. (n.d.). *Container runtime contract*. Google Cloud. https://cloud.google.com/run/docs/configuring/services/containers
7. SQLite. (n.d.). *Appropriate uses for SQLite*. https://www.sqlite.org/whentouse.html
8. Docker. (n.d.). *Networking in Compose*. https://docs.docker.com/compose/how-tos/networking/
9. Docker. (n.d.). *Use volumes*. https://docs.docker.com/engine/storage/volumes/
10. Docker. (n.d.). *Compose file reference: healthcheck*. https://docs.docker.com/reference/compose-file/services/#healthcheck
11. MagicStack. (n.d.). *asyncpg documentation*. https://magicstack.github.io/asyncpg/current/
12. Model Context Protocol. (n.d.). *MCP specification*. https://modelcontextprotocol.io/specification
13. Google. (n.d.). *Connect from Cloud Run*. Google Cloud. https://cloud.google.com/sql/docs/postgres/connect-run
14. Google. (n.d.). *IAM database authentication*. Google Cloud. https://cloud.google.com/sql/docs/postgres/iam-authentication
15. AhmetB. (n.d.). *Cloud Run FAQ*. GitHub. https://github.com/ahmetb/cloud-run-faq/blob/master/README.md
16. Crunchy Data. (n.d.). *Designing your Postgres database for multi-tenancy*. https://www.crunchydata.com/blog/designing-your-postgres-database-for-multi-tenancy
17. PostgreSQL Global Development Group. (n.d.). *Using EXPLAIN*. PostgreSQL Documentation. https://www.postgresql.org/docs/current/using-explain.html
18. SQLite. (n.d.). *Frequently asked questions*. https://sqlite.org/faq.html
19. Do, H. (n.d.). *MySQL vs PostgreSQL: Features & capabilities comparison*. DEV Community. https://dev.to/harry_do/part-3-mysql-vs-postgresql-features-capabilities-comparison-13gj
20. Cybertec. (n.d.). *INT4 vs INT8 vs UUID vs NUMERIC performance on bigger JOINs*. https://www.cybertec-postgresql.com/en/int4-vs-int8-vs-uuid-vs-numeric-performance-on-bigger-joins/
21. Google. (n.d.). *cloud-sql-python-connector/connector.py*. GitHub. https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/google/cloud/sql/connector/connector.py
22. testdriven.io. (n.d.). *Alembic database migrations*. https://testdriven.io/blog/alembic-database-migrations/
23. Alembic. (n.d.). *Auto-generating migrations*. https://alembic.sqlalchemy.org/en/latest/autogenerate.html
24. The Full Stack. (2023, May 25). *Production-ready FastAPI with background tasks and database migrations* [Video]. YouTube. https://www.youtube.com/watch?v=91j6zOoIP4g
25. Neon. (n.d.). *Rate limiting in Postgres*. https://neon.com/guides/rate-limiting
26. JCharisTech. (2022, December 11). *Create an upload and download files API endpoint with FastAPI*. https://blog.jcharistech.com/2022/12/11/create-an-upload-and-download-files-api-endpoint-with-fastapi/
27. Tiger Data. (n.d.). *A guide to data analysis on PostgreSQL*. https://www.tigerdata.com/learn/guide-to-data-analysis-on-postgresql
28. PostgreSQL Global Development Group. (n.d.). *Viewing statistics*. PostgreSQL Documentation. https://www.postgresql.org/docs/current/monitoring-stats.html