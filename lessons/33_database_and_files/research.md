# Research

## Research Results

<details>
<summary>What are the performance and security trade-offs when using UUIDs versus serial integer primary keys in a multi-user web application with PostgreSQL?</summary>

### Source [1]: https://chat2db.ai/resources/blog/uuid-auto-increment-integer

Query: What are the performance and security trade-offs when using UUIDs versus serial integer primary keys in a multi-user web application with PostgreSQL?

Answer: Choosing between an Auto Increment Integer/Serial or a UUID as primary key considers database performance, data replication and other factors. Auto Increment Integers are more readable, such as 'issue-123' versus a UUID like 'issue-b1e92c3b-a44a-4856-9fe3-925444ac4c23'. They use less space: UUID occupies 16 bytes, while Long format integer takes 8 bytes, noticeable in tables with few columns. In databases like MySQL and Oracle with clustered primary keys, UUIDv1 or UUIDv4 hurt insertion performance due to row reordering in the clustered index. PostgreSQL uses a heap instead of clustered primary key, so it is not affected this way.

-----

-----

### Source [2]: https://www.cybertec-postgresql.com/en/int4-vs-int8-vs-uuid-vs-numeric-performance-on-bigger-joins/

Query: What are the performance and security trade-offs when using UUIDs versus serial integer primary keys in a multi-user web application with PostgreSQL?

Answer: UUIDs should generally be avoided for performance reasons as they take 16 bytes versus 4/8 bytes for normal integers, making them slower. Benchmarks on bigger joins show: int4 (2.72s), int8 (2.95s, +8%), numeric (3.65s, +34%), uuid (3.07s, +13% time, +40% index size at 150MB). The penalty is small enough to dismiss for benefits like sharding and security against guessing. Index size for UUID depends on type: random UUIDv4 has larger index (195-196MB) versus time-based UUIDv1 (150MB, ~20% smaller). UUIDv4 causes more page splits due to randomness.

-----

-----

### Source [3]: https://pganalyze.com/blog/5mins-postgres-uuid-vs-serial-primary-keys

Query: What are the performance and security trade-offs when using UUIDs versus serial integer primary keys in a multi-user web application with PostgreSQL?

Answer: UUIDs are 128 bits versus bigint 64 bits. Key question is random vs sequential keys. Sequential keys interact better with B-tree indexes, common in Postgres; random keys cause index bloat. Randomness leads to performance tanking on larger datasets due to index bloat and larger WAL from page splits updating more of the index. 128-bit UUIDs add memory overhead on 64-bit systems versus 64-bit datums. Hybrid approach: reserve 16 bits for sequence in 128-bit UUID for randomness benefits (prevent enumeration attacks) with low index overhead.

-----

-----

### Source [4]: https://supabase.com/blog/choosing-a-postgres-primary-key

Query: What are the performance and security trade-offs when using UUIDs versus serial integer primary keys in a multi-user web application with PostgreSQL?

Answer: Postgres catches collisions on PRIMARY KEY or UNIQUE INDEX. UUIDv1 contains time but not lexicographically sortable, sorts terribly relative to integer or timestamp, less random than v4, potential collisions at large scale. UUIDv4 good for collision avoidance but indexes poorly. Tests cover generation speed, table/index size. Best time-based ID is xid for performance and sort friendliness; UUID v6/v7 more standards-oriented. Weigh options and test for use-case.

-----

-----

### Source [5]: https://www.youtube.com/watch?v=DHtf_46OxY8

Query: What are the performance and security trade-offs when using UUIDs versus serial integer primary keys in a multi-user web application with PostgreSQL?

Answer: Comparison of auto-incrementing integer vs UUID primary keys. Sorted IDs (integers) use index efficiently, less storage (8 bytes for large integer). UUIDs take more storage, longer comparison time in queries depending on database. UUIDv4 random, scalable, generatable anywhere, easy database merges, hard to guess. UID V7 (likely ULID-like) includes time for sorting/index improvement over v4, but more storage than integers.

-----

-----

### Source [6]: https://brandur.org/nanoglyphs/026-ids

Query: What are the performance and security trade-offs when using UUIDs versus serial integer primary keys in a multi-user web application with PostgreSQL?

Answer: Integer sequences occupy 64 bits vs UUID 128 bits, slight storage saving. Performance issues with UUIDs solved by sequential approaches like time-ordered: new inserts map to same new pages, fewer pages in memory, fewer cache misses, good throughput, less WAL amplification. ULIDs (Universally Unique Lexicographically Sortable Identifiers) generalize this: 128-bit compatible with UUID storage.

-----

</details>

<details>
<summary>What are the trade-offs of using JSONB in PostgreSQL versus native JSON support in modern MySQL for application development?</summary>

### Source [7]: https://dev.to/harry_do/part-3-mysql-vs-postgresql-features-capabilities-comparison-13gj

Query: What are the trade-offs of using JSONB in PostgreSQL versus native JSON support in modern MySQL for application development?

Answer: PostgreSQL's JSONB support is a critical differentiator for applications with unstructured or semi-structured data, eliminating the need for separate document databases. Key advantages of PostgreSQL JSONB include native binary storage in a decomposed format for efficient querying without parsing overhead, GIN indexing for fast lookups on properties and containment, rich operators for querying and manipulation, type safety with schema-less flexibility, and superior query performance by avoiding synchronization with relational stores. This allows handling both relational and document data in one system, reducing complexity. MySQL 8.4 offers good JSON support with binary storage and functional path-specific indexes, adequate for basic storage and retrieval, but lacks comprehensive indexing and rich operators, making it less suitable for heavy JSON querying. Comparison table highlights PostgreSQL's superior JSONB with GIN indexes versus MySQL's functional path-specific indexes, and advanced JSON indexing on entire documents versus functional. Random inserts are slower in MySQL due to clustered hotspots, while PostgreSQL is consistent without clustering overhead.

-----

-----

### Source [8]: https://www.bytebase.com/blog/postgres-vs-mysql-json-support/

Query: What are the trade-offs of using JSONB in PostgreSQL versus native JSON support in modern MySQL for application development?

Answer: PostgreSQL 17 offers broader JSON functionality than MySQL 8, especially for heavy JSON workloads with advanced querying via jsonb and GIN indexes. PostgreSQL has jsonb (preferred, binary format, slower input but faster processing, supports indexing) and json (text copy, preserves whitespace/order, requires reparsing). MySQL has a single JSON type like jsonb, with optimized binary storage for quick access, automatic validation in both. MySQL features JSON_TABLE() for JSON-to-relational conversion, JSON Schema validation, multi-valued indexes on arrays since 8.0.17. Path expressions differ: PostgreSQL uses dots/brackets with enhanced SQL/JSON in 17; MySQL uses JS-like notation. Indexing: PostgreSQL jsonb supports GIN for containment/existence and functional indexes; MySQL uses generated columns or multi-valued indexes, no direct JSON column indexing. Performance: PostgreSQL jsonb has insertion conversion overhead but efficient GIN querying, partial updates; MySQL offers quick element access, partial in-place updates, compact binary logs. Table shows PostgreSQL advantages in data types (jsonb/json vs single JSON), containment operators (@> etc. vs functions), while MySQL has JSON_PRETTY(). PostgreSQL better for advanced JSON querying.

-----

-----

### Source [9]: https://www.dbvis.com/thetable/json-vs-jsonb-in-postgresql-a-complete-comparison/

Query: What are the trade-offs of using JSONB in PostgreSQL versus native JSON support in modern MySQL for application development?

Answer: This source focuses solely on JSON vs JSONB in PostgreSQL, not comparing to MySQL, so it provides no direct trade-offs for the query. It notes jsonb (added in 9.4, 'b' for better) stores in compressed binary format, efficient for querying/indexing; json stores exact text, preserves formatting but slower due to reparsing. jsonb slower on INSERT due to conversion but faster overall, supports more functions/operators and indexing. jsonb better for most cases unless preserving exact formatting needed. Performance: jsonb wins with binary storage and indexing vs json's text reparsing.

-----

-----

### Source [10]: https://news.ycombinator.com/item?id=36945115

Query: What are the trade-offs of using JSONB in PostgreSQL versus native JSON support in modern MySQL for application development?

Answer: MySQL indexes JSON via computed/generated columns extracting scalars or serializing to varchar for broad search, but not as direct. PostgreSQL uses GIN indices on JSONB. Tradeoff in complexity: MySQL via DDL (generated columns), PostgreSQL via DML/DQL with GIN on JSONB.

-----

-----

### Source [11]: https://skemato.com/blog/postgresql-vs-mysql-2025-deep-dive

Query: What are the trade-offs of using JSONB in PostgreSQL versus native JSON support in modern MySQL for application development?

Answer: PostgreSQL wins for JSON support: JSONB is more powerful and indexable than MySQL's JSON. In 2025 performance, both similar for simple read-heavy queries.

-----

</details>

<details>
<summary>What are best practices for managing Alembic database migrations in a production CI/CD pipeline with Docker, specifically regarding automated execution on startup?</summary>

### Source [12]: https://testdriven.io/blog/alembic-database-migrations/

Query: What are best practices for managing Alembic database migrations in a production CI/CD pipeline with Docker, specifically regarding automated execution on startup?

Answer: Alembic manages database migrations with SQLAlchemy by version controlling the database schema using revision files stored in a 'versions' directory, identified by hash strings similar to Git commit hashes. Each discrete migration file is called a revision, enabling upgrades and downgrades. Common workflows include autogenerating migrations after modifying database models by running `alembic revision --autogenerate -m "message"`, which creates a new .py file in alembic/versions/ with upgrade() and downgrade() logic. To apply migrations locally after changes or `git pull`, use `alembic upgrade head`. This applies the latest revisions in sequence, akin to `git pull`. The article emphasizes Alembic's Git-like model for handling branches, merges, and conflicts, but does not specifically address Docker, CI/CD pipelines, or automated execution on startup in production. It focuses on development workflows like pulling/applying migrations, rolling back with `alembic downgrade`, and resolving merge conflicts.

-----

-----

### Source [13]: https://www.youtube.com/watch?v=91j6zOoIP4g

Query: What are best practices for managing Alembic database migrations in a production CI/CD pipeline with Docker, specifically regarding automated execution on startup?

Answer: For production usage with Alembic database migrations in Docker, create a `docker-entrypoint.sh` file for the service container. This entrypoint script ensures prerequisites like database migrations run before starting the application. Specifically, it executes `alembic upgrade head` to migrate the database with all revisions before launching the main service. Make sure the database and service containers are up and running. The script handles multiple commands sequentially: first apply all Alembic revisions to the database, then start the container's primary process. This approach automates migrations on container startup in production CI/CD pipelines. Additional tips include using .env files for environment tags (e.g., test or prod) and overriding with shell ENV variables like `export TAG=local`. The video demonstrates setting up Alembic in a virtual environment and creating revisions inside containers before applying changes.

-----

-----

### Source [14]: https://alembic.sqlalchemy.org/en/latest/autogenerate.html

Query: What are best practices for managing Alembic database migrations in a production CI/CD pipeline with Docker, specifically regarding automated execution on startup?

Answer: Alembic's official documentation covers autogenerating migrations using `alembic revision --autogenerate`, which detects model changes and places candidate migrations into new revision files, but requires manual review and `alembic upgrade` to apply them. Post-write hooks in alembic.ini or pyproject.toml automate formatting (e.g., black) or linting on generated files. The `alembic check` command verifies if autogenerate would produce empty migrations, returning success if no changes needed, suitable for CI systems and on-commit schemes to ensure consistency without unnecessary runs. Configure hooks like:

[post_write_hooks]
hooks=black
black.type = console_scripts
black.entrypoint = black
black.options = -l 79 REVISION_SCRIPT_FILENAME

However, no direct guidance on Docker, production CI/CD pipelines, or automated execution on startup. Focus is on development and CI integration for migration generation and validation.

-----

-----

### Source [15]: https://hackernoon.com/solving-the-fastapi-alembic-docker-problem

Query: What are best practices for managing Alembic database migrations in a production CI/CD pipeline with Docker, specifically regarding automated execution on startup?

Answer: For managing Alembic migrations with FastAPI in Docker, create a 'migrations' directory with a 'versions' subdirectory, then run `alembic init .` to set up. This structure supports production setups. The article addresses solving integration issues in Docker environments but lacks specifics on CI/CD pipelines or automated execution on startup. Emphasizes proper initialization for containerized deployments.

-----

</details>

<details>
<summary>How does the Google Cloud SQL Python Connector use IAM and refresh strategies to securely manage database connections in a serverless environment like Cloud Run?</summary>

### Source [18]: https://github.com/GoogleCloudPlatform/cloud-sql-python-connector

Query: How does the Google Cloud SQL Python Connector use IAM and refresh strategies to securely manage database connections in a serverless environment like Cloud Run?

Answer: The Google Cloud SQL Python Connector uses IAM permissions via the Cloud SQL Client role assigned to the IAM principal (user or service account) for credentials to control access to Cloud SQL instances. It provides improved security with TLS 1.3 encryption and identity verification between client and server-side proxy. It supports optional Automatic IAM Database Authentication for Postgres and MySQL, where you configure the Cloud SQL instance to allow IAM auth and add an IAM database user. In connections, set enable_iam_auth=True and use the IAM principal as the user (e.g., email for users, service account email without .gserviceaccount.com suffix for Postgres). The Connector can be customized with parameters like ip_type (public/private/psc), enable_iam_auth, timeout, credentials, and refresh_strategy ('lazy' or 'background'). Refresh strategies manage credential and connection refreshes: 'lazy' refreshes on demand, 'background' proactively. This is ideal for serverless like Cloud Run as it integrates directly without managing proxies, firewalls, or SSL certs. Examples show connector.connect() with IAM auth for secure passwordless connections.

-----

-----

### Source [19]: https://cloud.google.com/blog/topics/developers-practitioners/how-connect-cloud-sql-using-python-easy-way

Query: How does the Google Cloud SQL Python Connector use IAM and refresh strategies to securely manage database connections in a serverless environment like Cloud Run?

Answer: The Cloud SQL Python Connector uses IAM Authorization to control who/what can connect to Cloud SQL instances via IAM permissions. It enhances security with TLS 1.3 encryption and identity verification independent of database protocol. Convenience comes from no need for SSL certificates, firewall management, or IP addresses. It supports optional IAM Database Authentication for passwordless access using IAM user or service account. This setup is secure and convenient for Python apps connecting to Cloud SQL, leveraging connectors for automatic handling.

-----

-----

### Source [20]: https://docs.cloud.google.com/sql/docs/mysql/iam-authentication

Query: How does the Google Cloud SQL Python Connector use IAM and refresh strategies to securely manage database connections in a serverless environment like Cloud Run?

Answer: Automatic IAM database authentication with the Cloud SQL Python Connector hands off access token requesting and management to the connector. Users pass only the IAM database username in the connection request; the connector submits the access token as the password on behalf of the client. This is supported for MySQL and requires a Cloud SQL connector like the Python one. IAM authentication uses SSL connections and OAuth 2.0 tokens with Cloud SQL Admin API scope. Manual IAM requires explicit token passing, but automatic simplifies it for connectors.

-----

-----

### Source [21]: https://www.revolgy.com/insights/blog/how-connect-to-google-cloud-sql-service-account-in-python

Query: How does the Google Cloud SQL Python Connector use IAM and refresh strategies to securely manage database connections in a serverless environment like Cloud Run?

Answer: To securely connect using IAM in serverless environments, create a service account in IAM & Admin, grant it the Cloud SQL Client role, and download JSON key for credentials (set GOOGLE_APPLICATION_CREDENTIALS). The Python Connector integrates secure tunnel functionality directly into code, eliminating separate proxy processes. Initialize Connector, then use connector.connect() with instance connection string (project:region:instance), driver (e.g., pymysql), user, password, db. This handles secure tunnel establishment and returns database connection, using service account IAM for authorization. Ideal for serverless as it's embedded.

-----

-----

### Source [22]: https://cloud.google.com/blog/products/databases/connect-your-application-to-cloud-sql

Query: How does the Google Cloud SQL Python Connector use IAM and refresh strategies to securely manage database connections in a serverless environment like Cloud Run?

Answer: The connector provides IAM-based connection authorization to control access via roles/permissions. Automatic IAM database authentication enables passwordless connections, avoiding credential issues. IAM conditions limit to specific instances, and connector enforcement ensures only official connectors connect. This setup is secure for serverless environments like Cloud Run.

-----

-----

### Source [23]: https://docs.cloud.google.com/sql/docs/mysql/connect-connectors

Query: How does the Google Cloud SQL Python Connector use IAM and refresh strategies to securely manage database connections in a serverless environment like Cloud Run?

Answer: Cloud SQL Language Connectors, including Python, provide encryption and IAM-based authorization for connections to Cloud SQL. They manage secure access without exposing IPs or managing certs, suitable for serverless.

-----

</details>

<details>
<summary>What are common database schema patterns for implementing API rate limiting, such as token bucket or sliding window counters?</summary>

### Source [25]: https://www.systemsdesign.cloud/SystemDesign/RateLimiter

Query: What are common database schema patterns for implementing API rate limiting, such as token bucket or sliding window counters?

Answer: Rate limiting controls API access speed to prevent resource exhaustion and attacks. Fixed window counter uses INCR and EXPIRE in Redis: increment counter for requests; if below limit, allow and decrement; reset if window (e.g., 60s) elapsed. Problem: burst at window edges allows double requests (e.g., 10 in <1 min despite 5/min limit). Sliding window counter uses Redis sorted set: add timestamp to set per request; fetch ZRange(0,-1) to count recent timestamps against limit; reject if exceeded. Update TTL atomically with MULTI. Avoid duplicates by timestamp granularity. Token bucket and leaky bucket implied. Types: Hard Throttling (strict limit), Soft Throttling (e.g., 10% exceed, 110/100 min). Use in-memory cache like Redis, avoid databases for speed.

-----

-----

### Source [26]: https://www.gravitee.io/blog/rate-limiting-apis-scale-patterns-strategies

Query: What are common database schema patterns for implementing API rate limiting, such as token bucket or sliding window counters?

Answer: Rate limiting tracks requests by API keys, user IDs, or IPs. At scale, use centralized stores like Redis/Redis Cell, consistent hashing, clock-tolerant algorithms: **sliding window counter**, **token bucket**, **leaky bucket**. Combine global, tenant, user, endpoint limits. State management is key problem; sliding window counters and token/leaky buckets handle distribution.

-----

-----

### Source [27]: https://dev.to/ahmedjaad/designing-and-implementing-an-api-rate-limiter-1f9m

Query: What are common database schema patterns for implementing API rate limiting, such as token bucket or sliding window counters?

Answer: API rate limiting restricts client requests per time period for fair usage and stability. Components: Rate Limiter intercepts requests, decides allow/throttle based on rules; Request Processor handles valid requests. Use Redis as distributed cache for rate limit states across instances. Rules Engine defines policies (requests per window, actions on exceed), typically from database but hardcoded in prototype. Implementation with Spring and Redis.

-----

-----

### Source [28]: https://api7.ai/learning-center/api-101/rate-limiting-strategies-for-api-management

Query: What are common database schema patterns for implementing API rate limiting, such as token bucket or sliding window counters?

Answer: Rate limiting controls requests per timeframe. Common algorithms: **Fixed Window**, **Sliding Window**, **Leaky Bucket**, **Token Bucket**. Implement at API gateway (e.g., API7 Enterprise) with policies per route/user/IP/API key, limits per second/minute/hour/day. Scalable with plugins.

-----

</details>

<details>
<summary>What are best practices for implementing file upload and download functionality in a Python web framework like FastAPI when the primary communication protocol, like MCP, lacks native file transfer capabilities?</summary>

### Source [33]: https://blog.jcharistech.com/2022/12/11/create-an-upload-and-download-files-api-endpoint-with-fastapi/

Query: What are best practices for implementing file upload and download functionality in a Python web framework like FastAPI when the primary communication protocol, like MCP, lacks native file transfer capabilities?

Answer: FastAPI supports file upload and download endpoints using UploadFile and FileResponse. Install python-multipart for handling uploads. For upload, define @app.post('/file/upload') with UploadFile parameter, validate content_type (e.g., 'application/json'), read file with file.file.read(), parse JSON, and return data and filename. Example: if file.content_type != 'application/json': raise HTTPException(400, 'Invalid document type'); data = json.loads(file.file.read()); return {'content': data, 'filename': file.filename}. For download after upload, use @app.post('/file/uploadndownload'), process uploaded JSON (e.g., convert to YAML), save to directory like UPLOAD_DIR with timestamped filename (e.g., '{basename}_{timestr}.yaml'), then return FileResponse(path=SAVE_FILE_PATH, media_type='application/octet-stream', filename=new_filename). Create UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads'). Full code includes imports: FastAPI, UploadFile, HTTPException, FileResponse, json, os, yaml, time; uvicorn server on 127.0.0.1:8000. Use media_type 'application/octet-stream' for multiple file types. Useful for services like JSON to YAML conversion.

-----

-----

### Source [34]: https://fastapi.tiangolo.com/tutorial/request-files/

Query: What are best practices for implementing file upload and download functionality in a Python web framework like FastAPI when the primary communication protocol, like MCP, lacks native file transfer capabilities?

Answer: FastAPI handles file uploads using File, bytes, and UploadFile for form data. Import from fastapi: File, UploadFile. For bytes: @app.post('/files/') async def create_file(file: Annotated[bytes, File()]): return {'file_size': len(file)}. For UploadFile: @app.post('/uploadfile/') async def create_upload_file(file: UploadFile): return {'filename': file.filename}. Use UploadFile to receive files from requests as form data. Install python-multipart is required for form data handling.

-----

-----

### Source [35]: https://fastapi.tiangolo.com/reference/uploadfile/

Query: What are best practices for implementing file upload and download functionality in a Python web framework like FastAPI when the primary communication protocol, like MCP, lacks native file transfer capabilities?

Answer: UploadFile class from fastapi receives files in path operation functions. Import: from fastapi import UploadFile. Attributes include content_type (from headers). Methods: read(size=-1) reads bytes asynchronously in threadpool; write(data) writes to file; close() closes the file. Define parameters as UploadFile to handle uploaded files.

-----

-----

### Source [36]: https://fastapi.tiangolo.com/tutorial/request-forms-and-files/

Query: What are best practices for implementing file upload and download functionality in a Python web framework like FastAPI when the primary communication protocol, like MCP, lacks native file transfer capabilities?

Answer: To receive uploaded files and form data, install python-multipart in a virtual environment. Use with File and UploadFile for handling forms and files.

-----

-----

### Source [37]: https://www.geeksforgeeks.org/python/save-uploadfile-in-fastapi/

Query: What are best practices for implementing file upload and download functionality in a Python web framework like FastAPI when the primary communication protocol, like MCP, lacks native file transfer capabilities?

Answer: UploadFile class handles files in FastAPI endpoints. Install python-multipart. Define @app.post('/upload/') async def uploadfile(file: UploadFile): save file by file_path = f'path/{file.filename}'; with open(file_path, 'wb') as f: f.write(file.file.read()); return {'message': 'File saved successfully'}. For multiple files: async def uploadfile(files: list[UploadFile]): loop over files, save each similarly. Methods: write(data), read(size), close(). Use HTML form for text, PDF, JPG files submitting to endpoint.

-----

-----

### Source [38]: https://betterstack.com/community/guides/scaling-python/uploading-files-using-fastapi/

Query: What are best practices for implementing file upload and download functionality in a Python web framework like FastAPI when the primary communication protocol, like MCP, lacks native file transfer capabilities?

Answer: Build production file upload with validation. Example: @app.post('/upload/single') async def upload_single_file(file: UploadFile = File(...)). Includes results tracking like successful/failed uploads and upload_time.

-----

-----

### Source [39]: https://python.plainenglish.io/streaming-file-uploads-and-downloads-with-fastapi-a-practical-guide-ee5be38fdd66

Query: What are best practices for implementing file upload and download functionality in a Python web framework like FastAPI when the primary communication protocol, like MCP, lacks native file transfer capabilities?

Answer: Streaming file uploads and downloads with FastAPI enable scalable, memory-efficient APIs for large files without blocking.

-----

</details>

<details>
<summary>How can you implement a robust API rate-limiting system using only PostgreSQL and Python, and what are the trade-offs compared to using an in-memory solution like Redis?</summary>

### Source [40]: https://neon.com/guides/rate-limiting

Query: How can you implement a robust API rate-limiting system using only PostgreSQL and Python, and what are the trade-offs compared to using an in-memory solution like Redis?

Answer: Rate limiting limits requests in a time window, like 5 per minute. Implement directly in Postgres using advisory locks and counters. Use advisory locks to synchronize access: SELECT pg_advisory_xact_lock(hashtext('user_123_rate_limit')); this ensures one transaction modifies the counter at a time without row locking. Create rate_limits table for tracking: columns key, count, window_start. Use UPSERT: INSERT INTO rate_limits (key, count, window_start) VALUES (rate_limit_key, 1, now) ON CONFLICT (key) DO UPDATE SET count = CASE WHEN rate_limits.window_start + window_length <= now THEN 1 ELSE rate_limits.count + 1 END, window_start = CASE WHEN rate_limits.window_start + window_length <= now THEN now ELSE rate_limits.window_start END. Wrap in PL/pgSQL DO block or function: CREATE OR REPLACE FUNCTION check_rate_limit(rate_key TEXT, max_requests INTEGER, window_seconds INTEGER) RETURNS VOID AS $$ ... PERFORM pg_advisory_xact_lock(hashtext(rate_key)); INSERT... SELECT count INTO current_count; IF current_count > max_requests THEN RAISE EXCEPTION 'Rate limit exceeded'; END IF; $$ LANGUAGE plpgsql; Call as SELECT check_rate_limit('user_123', 5, 60); This handles race conditions via locks and provides atomic updates.

-----

-----

### Source [41]: https://www.freecodecamp.org/news/build-a-rate-limiter-with-redis-and-python/

Query: How can you implement a robust API rate-limiting system using only PostgreSQL and Python, and what are the trade-offs compared to using an in-memory solution like Redis?

Answer: Build distributed rate limiter with Redis and Python using sliding window log algorithm. Use Redis sorted set (ZADD) to add timestamp of each request with unique score. Count recent requests with ZCARD on set for last 60 seconds (ZRANGEBYSCORE). Set EXPIRE on key for cleanup. Bundle in pipeline: pipe = redis.pipeline(); pipe.zadd(...); pipe.zremrangebyscore(...); pipe.expire(...); pipe.execute(); Check count > RATE_LIMIT_COUNT to return 429. This is fast, efficient, all in Redis optimized for operations. Handles distribution across multiple instances. Automatic expiration prevents memory buildup.

-----

-----

### Source [42]: https://dev.to/yugabyte/rate-limiting-with-postgresql-yugabytedb-token-buckets-function-5dh8

Query: How can you implement a robust API rate-limiting system using only PostgreSQL and Python, and what are the trade-offs compared to using an in-memory solution like Redis?

Answer: Implement token bucket rate limiting in PostgreSQL using counters per user. Store tokens, decrement on each call. Handles race conditions with SERIALIZABLE isolation and PRIMARY KEY constraint: concurrent calls serialize via pessimistic locking, wait or fail consistently. Scales on single server: tested 8 sessions getting token every ms with set default_transaction_isolation=serializable; select rate_limiting_request('user1',1000,3600); Works identically on YugabyteDB for distributed scaling. Monolithic DB limits writes to one node; distributed DB like Yugabyte maintains ACID across nodes without failover delays.

-----

-----

### Source [43]: https://pyratelimiter.readthedocs.io

Query: How can you implement a robust API rate-limiting system using only PostgreSQL and Python, and what are the trade-offs compared to using an in-memory solution like Redis?

Answer: pyrate-limiter supports PostgreSQL via PostgresBucket. Use with psycopg_pool.ConnectionPool('postgresql://...'). Create PostgresClock(connection_pool) for time. Define rates: rates = [Rate(3, 1000), Rate(4, 1500)]; bucket = PostgresBucket(connection_pool, "my-bucket-table", rates); limiter = Limiter(bucket). Supports unlimited rates, custom intervals, separate limits per service/resource. Manages breaches configurably. Python library for robust rate limiting using only Postgres storage.

-----

-----

### Source [44]: https://liambx.com/blog/building-rest-apis-postgresql-practical-guide

Query: How can you implement a robust API rate-limiting system using only PostgreSQL and Python, and what are the trade-offs compared to using an in-memory solution like Redis?

Answer: PostgreSQL-backed APIs implement rate limiting via API Gateways like Kong or AWS API Gateway with built-in per-user/IP limits. Or custom middleware in API code (e.g., Flask with Flask-Limiter) tracking counts in caching layer like Redis, rejecting excess requests. Example: limit 100 requests/hour per user to prevent overload from spikes or abuse, useful for third-party integrations.

-----

-----

### Source [45]: https://www.girmantech.com/blog/api-rate-limiting-with-redis-and-postgresql

Query: How can you implement a robust API rate-limiting system using only PostgreSQL and Python, and what are the trade-offs compared to using an in-memory solution like Redis?

Answer: Implement fixed-window rate limiting using Redis for real-time request tracking and PostgreSQL for configuration management.

-----

</details>

<details>
<summary>What is a step-by-step guide for setting up a local development environment using Docker Compose for a Python application with a PostgreSQL database and Alembic for migrations?</summary>

### Source [46]: https://dev.to/r_elena_mendez_escobar/simplify-database-migrations-using-python-with-alembic-4bhd

Query: What is a step-by-step guide for setting up a local development environment using Docker Compose for a Python application with a PostgreSQL database and Alembic for migrations?

Answer: To set up a local PostgreSQL database using Docker Compose for Alembic migrations:

1. Create a `docker-compose.yml` file:
```
version: "3.7"
services:
  db:
    image: postgres:13.3-alpine
    volumes:
      - ./db_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
    ports:
      - "5433:5432"
volumes:
  db_data:
```

2. Start the database: `docker-compose -f docker-compose.yml up --build`

3. Verify it's running: `docker ps`

This sets up PostgreSQL on port 5433 with persistent data in `./db_data`. Connect using `postgresql://postgres:postgres@localhost:5433/postgres`. The article focuses on Alembic migrations with this Dockerized PostgreSQL setup for Python applications.

-----

-----

### Source [47]: https://www.youtube.com/watch?v=JWQEostzy60

Query: What is a step-by-step guide for setting up a local development environment using Docker Compose for a Python application with a PostgreSQL database and Alembic for migrations?

Answer: Video tutorial on setting up a FastAPI dev environment with PostgreSQL, SQLAlchemy 2.0 async, Alembic, and Docker Compose:

- Create project structure and Dockerfile for FastAPI.
- Set up PostgreSQL with persistent volumes (15:05).
- Run services: `docker compose up` (18:43).
- Install SQLAlchemy, asyncpg, pydantic-settings (20:03).
- Manage environment variables for PostgreSQL connection (20:55, 26:06).
- Connect to PostgreSQL using service name 'db' as host (26:06-36:26).
- Create sample DB table (36:26).
- Use Docker Compose Watch for hot-reloading (42:36-46:22).
- Initialize Alembic (49:30), configure it (54:41), create initial revision (59:58).

Docker Compose includes services block with app and postgres services running together. Environment uses postgres user/password, host as service name 'database'.

-----

-----

### Source [48]: https://berkkaraal.com/blog/2024/09/19/setup-fastapi-project-with-async-sqlalchemy-2-alembic-postgresql-and-docker/

Query: What is a step-by-step guide for setting up a local development environment using Docker Compose for a Python application with a PostgreSQL database and Alembic for migrations?

Answer: To start PostgreSQL with Docker Compose for FastAPI + Alembic project:

Create `docker-compose.yaml` at project root:
```
services:
  postgres:
    image: postgres:16-alpine
    volumes:
      - ./var/db:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=db
```

- `./var/db` for data persistence.
- Expose port 5432.
- Set env vars.

Start: `docker compose up -d`. Stop with same command.

Add FastAPI server as `backend` service, override `PG_HOST=postgres` to connect to service (not localhost). Start both: `docker compose up -d`. Watch logs: `docker compose logs -f backend`.

-----

-----

### Source [49]: https://testdriven.io/blog/fastapi-sqlmodel/

Query: What is a step-by-step guide for setting up a local development environment using Docker Compose for a Python application with a PostgreSQL database and Alembic for migrations?

Answer: Docker Compose setup for FastAPI with Async SQLAlchemy, SQLModel, Alembic, PostgreSQL:

Run: `$ docker-compose up -d --build`

Test: http://localhost:8004/ping returns {"ping": "pong!"}

Check DB: `$ docker-compose exec db psql --username=postgres --dbname=foo`

Alembic config in `project/alembic.ini`:
```
sqlalchemy.url = postgresql+asyncpg://postgres:postgres@db:5432/foo
```

Generate first migration: `$ docker-compose exec web alembic revision --autogenerate -m "init"`

Creates migration file in `project/migrations/versions`. Uses PostgreSQL service named 'db', database 'foo'. Supports asyncpg driver for async SQLAlchemy.

-----

-----

### Source [50]: https://anagraph.io/en/articles/alembic_in_2021/

Query: What is a step-by-step guide for setting up a local development environment using Docker Compose for a Python application with a PostgreSQL database and Alembic for migrations?

Answer: Basic PostgreSQL Docker Compose setup for Alembic:

Start service: `docker-compose up -d`

Update `alembic.ini` with credentials from docker-compose:
```
sqlalchemy.url = postgresql://postgres:mypassword@localhost:5598/postgres
```

Focuses on managing PostgreSQL database with Alembic migrations in Python applications using containerized DB.

-----

</details>

<details>
<summary>What are the key architectural and security considerations when designing a multi-tenant database schema in PostgreSQL for a web application where each user's data must be strictly isolated?</summary>

### Source [51]: https://www.crunchydata.com/blog/designing-your-postgres-database-for-multi-tenancy

Query: What are the key architectural and security considerations when designing a multi-tenant database schema in PostgreSQL for a web application where each user's data must be strictly isolated?

Answer: Three main approaches to multi-tenant database design in PostgreSQL are: one database per customer, schema per customer, and tenant discriminator in shared tables. One database per customer provides maximum isolation, allowing separate encryption keys, independent scaling, upgrades, and app versions per tenant. Schema per customer offers isolation similar to separate databases but enables easy cross-tenant joins for analytics; pros include full schema isolation and cross-customer analytics, cons include management overhead. With Citus, schemas can be sharded across nodes, querying tenant locations via pg_dist_placement and pg_dist_node, and moving or isolating tenants using functions like isolate_tenant_to_new_shard('table_name', tenant_id). Citus 12 supports schema-based sharding with PgBouncer for connection management, suitable for up to several thousand tenants; for millions, tenant discriminator is recommended. Security benefits from isolation in databases or schemas prevent data intermingling.

-----

-----

### Source [52]: https://streamkap.com/resources-and-guides/postgresql-cdc-multi-tenant

Query: What are the key architectural and security considerations when designing a multi-tenant database schema in PostgreSQL for a web application where each user's data must be strictly isolated?

Answer: For multi-tenant PostgreSQL, every table with tenant-specific data must include a tenant_id column as the core of the strategy. All queries require a WHERE tenant_id = 'current_tenant' clause to prevent data leakage, serving as the first security defense. For massive tables, use declarative partitioning by tenant_id (list or hash) to physically group data, improving query performance, tenant-specific backups, and archival. In schema-per-tenant model, name schemas like tenant_<tenant_id> for automatic CDC capture via regex like tenant_.*\.orders, excluding noisy schemas like information_schema or pg_catalog. Shared schema with tenant-prefixed tables (e.g., t1_users, t2_users) uses regex t[0-9]+_.* to capture tenant tables while ignoring shared ones like plans or features. This ensures scalable, secure data isolation and simplifies operations.

-----

-----

### Source [53]: https://blog.logto.io/implement-multi-tenancy

Query: What are the key architectural and security considerations when designing a multi-tenant database schema in PostgreSQL for a web application where each user's data must be strictly isolated?

Answer: Implement multi-tenancy in PostgreSQL using Row-Level Security (RLS) and database roles for strict data isolation in a shared schema. Add a tenant identifier (tenant_id) to all resource tables like customers to associate data with tenants. Create a base role with shared permissions, then assign inherited tenant-specific roles upon tenant creation, stored in a tenants table with db_user and db_user_password for each. Use separate database connections per tenant for permission management. RLS policies enforce access control based on current tenant role, ensuring users only see their tenant's data. Triggers reduce developer burden by automatically managing tenant context. This shared resource approach with database-level isolation via RLS and roles provides security and scalability for CRM-like systems.

-----

-----

### Source [54]: https://www.tigerdata.com/blog/building-multi-tenant-rag-applications-with-postgresql-choosing-the-right-approach

Query: What are the key architectural and security considerations when designing a multi-tenant database schema in PostgreSQL for a web application where each user's data must be strictly isolated?

Answer: PostgreSQL supports four multi-tenancy levels: table (shared tables with tenant_id), schema (separate schema per tenant), logical database (separate database per tenant), and database service (fully isolated services). Each offers trade-offs in shared resources, data separation, customization, scalability, and costs. Table level uses shared schema with row-level security or discriminators for isolation but risks higher integrity violations. Schema level provides better isolation within one database, enabling cross-tenant analytics. Logical database per tenant maximizes isolation like separate DBs. Choose based on requirements: shared for cost-efficiency, isolated for security. Comparative analysis helps balance security, performance, and operations.

-----

-----

### Source [55]: https://neon.com/blog/multi-tenancy-and-database-per-user-design-in-postgres

Query: What are the key architectural and security considerations when designing a multi-tenant database schema in PostgreSQL for a web application where each user's data must be strictly isolated?

Answer: Multi-tenancy approaches in Postgres include shared schema, schema-per-user, and database-per-user. Shared schema stores all tenant data side-by-side using foreign keys and row-level security (RLS) for isolation; it's cheaper and easier to administer but has higher integrity violation risks and complex compliance as tenants grow. Schema-per-user offers better separation within one database. Database-per-user provides strongest isolation, encouraged by Neon's serverless projects, branches, and databases for instant scaling. Security considerations emphasize RLS in shared setups to enforce access restrictions, with risks increasing in shared models where breaches impact all tenants.

-----

-----

### Source [56]: https://www.youtube.com/watch?v=A8_FLPHc4KU

Query: What are the key architectural and security considerations when designing a multi-tenant database schema in PostgreSQL for a web application where each user's data must be strictly isolated?

Answer: Key considerations for scalable multi-tenant PostgreSQL architectures include tenant isolation, resource sharing, security, and performance. Avoid single shared tables for all tenants to prevent data leakage; instead, use bridge model isolating customers into individual schemas or individual databases within the same instance. This provides strict data separation while sharing resources efficiently.

-----

</details>

<details>
<summary>How does the Cloud SQL Python Connector's 'lazy' refresh strategy optimize database connections for serverless environments like Cloud Run, and how does it differ from the default background refresh?</summary>

### Source [57]: https://github.com/GoogleCloudPlatform/cloud-sql-python-connector

Query: How does the Cloud SQL Python Connector's 'lazy' refresh strategy optimize database connections for serverless environments like Cloud Run, and how does it differ from the default background refresh?

Answer: The Connector's refresh_strategy argument can be set to "lazy" to configure the Python Connector to retrieve connection info lazily and as-needed. Otherwise, a background refresh cycle runs to retrieve the connection info periodically. This setting is useful in environments where the CPU may be throttled outside of a request context, such as Cloud Run and Cloud Functions. To set the refresh strategy, initialize a Connector with refresh_strategy="lazy": connector = Connector(refresh_strategy="lazy"). For serverless environments like Cloud Functions and Cloud Run, it is beneficial to initialize the Connector with the lazy refresh strategy. The connector will automatically close all existing connections when switching strategies, forcing connection pools to establish new connections, which may cause in-progress database queries to fail. The connector polls for changes to the DNS name every 30 seconds by default, configurable via the failover_period argument (e.g., Connector(failover_period=60)). Setting failover_period to 0 disables polling and checks the DNS record only when creating a new connection. In lazy mode, the connector uses LazyRefreshCache, which refreshes only when needed, unlike the default background refresh using RefreshAheadCache that periodically retrieves ephemeral certificates and instance metadata.

-----

-----

### Source [58]: https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/google/cloud/sql/connector/connector.py

Query: How does the Cloud SQL Python Connector's 'lazy' refresh strategy optimize database connections for serverless environments like Cloud Run, and how does it differ from the default background refresh?

Answer: The Connector's refresh_strategy parameter defaults to RefreshStrategy.BACKGROUND and can be set to RefreshStrategy.LAZY ("lazy"). In lazy refresh mode (RefreshStrategy.LAZY), keys are lazily initialized (_keys = None), whereas in background mode, keys are pre-initialized using asyncio.run_coroutine_threadsafe(generate_keys(), self._loop). When connecting, if refresh_strategy == RefreshStrategy.LAZY, it creates a LazyRefreshCache for the instance connection name, client, keys, and IAM auth status. Otherwise, it uses RefreshAheadCache, which schedules periodic refreshes to retrieve up-to-date ephemeral certificates and instance metadata. LazyRefreshCache is used specifically for lazy refresh strategy, refreshing connection info only as needed during connection creation. Background refresh uses RefreshAheadCache for proactive periodic updates. Both are wrapped in MonitoredCache. On exceptions during connection, it calls monitored_cache.force_refresh(). The create_async_connector helper also supports refresh_strategy, defaulting to BACKGROUND.

-----

</details>

<details>
<summary>What is the container runtime contract for Google Cloud Run regarding filesystem persistence and data durability?</summary>

### Source [59]: https://docs.cloud.google.com/run/docs/container-contract

Query: What is the container runtime contract for Google Cloud Run regarding filesystem persistence and data durability?

Answer: The Cloud Run container runtime contract does not explicitly detail filesystem persistence or data durability in the provided documentation excerpt. Key behaviors include: Instances are not kept idle longer than 15 minutes unless required by minimum instances setting, after which Cloud Run sends a SIGTERM signal to all containers, followed by a 10-second grace period before SIGKILL, during which CPU is allocated and billed. This implies short-lived instances without guaranteed persistence. CPU allocation varies by billing: request-based (default) allocates CPU only during requests; instance-based always. Startup requires listening within 4 minutes, with CPU allocated. No alterations to system time or certain system calls are supported, and basic security profiles restrict root privileges and kernel features. Process restrictions may limit filesystem access requiring elevated privileges. Multi-container instances have configurable startup order and health checks. No mention of persistent volumes, emptyDir, or durable storage; data in container filesystem is ephemeral due to instance lifecycle.

-----

-----

### Source [60]: https://github.com/ahmetb/cloud-run-faq/blob/master/README.md

Query: What is the container runtime contract for Google Cloud Run regarding filesystem persistence and data durability?

Answer: Cloud Run is designed for running stateless HTTP containers. It explicitly states that Cloud Run is for server apps (HTTP/gRPC etc.) and not for run-to-completion tasks or one-time container execution. This underscores the expectation of statelessness, implying no guarantees for filesystem persistence or data durability across invocations, as containers are meant to be stateless without persistent local storage.

-----

-----

### Source [61]: https://cloud.google.com/blog/topics/developers-practitioners/improve-responsiveness-session-affinity-cloud-run/

Query: What is the container runtime contract for Google Cloud Run regarding filesystem persistence and data durability?

Answer: Container lifetime is not guaranteed for the duration of a session, even with session affinity cookies lasting 30 days. Cloud Run can restart or remove container instances at any time. While serving requests, instances remain active, but Cloud Run stops forwarding requests, sends SIGTERM, and shuts down after a 10-second grace period. Connections like WebSockets are kept open while active but subject to maximum request duration timeouts. This reinforces that filesystem data is not durable, as instances can be terminated unpredictably.

-----

-----

### Source [62]: https://docs.cloud.google.com/run/docs

Query: What is the container runtime contract for Google Cloud Run regarding filesystem persistence and data durability?

Answer: The Cloud Run documentation links to the container runtime contract but provides no specific details on filesystem persistence or data durability in the excerpt. It covers general topics like deploying images and contracts, implying users should refer to the contract for requirements, but no explicit persistence guarantees are noted.

-----

</details>

<details>
<summary>What are the failure modes and data corruption risks of using SQLite on a shared network volume (e.g., NFS) accessed by multiple containers?</summary>

### Source [63]: https://github.com/Sonarr/Sonarr/issues/1886

Query: What are the failure modes and data corruption risks of using SQLite on a shared network volume (e.g., NFS) accessed by multiple containers?

Answer: Sonarr uses WAL mode for SQLite journals, but WAL mode cannot safely be used over non-local filesystems like NFS, SMB/CIFS, leading to SQLite locking or corruption errors, especially in Docker for Windows or virtualization systems with host shared paths. Docker and virtualization often fail with these errors when the SQLite file is on shared paths. Recommendations include disabling WAL mode (e.g., via PRAGMA journal_mode=DELETE after stopping Sonarr to clear WAL files), detecting network/cloud drives and refusing to start or forcing non-WAL mode, or using block-level storage like iSCSI or CephFS instead of NFS to avoid file locks. NFS yields locks, but iSCSI on same hardware/NAS/network runs smoothly. CephFS with Ceph Fuse in Docker Swarm works without lock issues. Avoid mounting Windows host shares in Docker; use data volumes or MobyLinux mounts.

-----

-----

### Source [64]: https://discuss.hashicorp.com/t/intermittent-i-o-errors-while-using-nfs-csi-plugin/62704

Query: What are the failure modes and data corruption risks of using SQLite on a shared network volume (e.g., NFS) accessed by multiple containers?

Answer: Using NFS CSI plugin as storage backend for Nomad cluster (no local volumes) causes intermittent I/O errors in jobs, such as 'IOError: SQLitePCL.pretty.SQLiteException: disk I/O error'. Errors appear related to NFS CSI and resolve temporarily upon restarting the allocation.

-----

-----

### Source [65]: https://www.sqlite.org/howtocorrupt.html

Query: What are the failure modes and data corruption risks of using SQLite on a shared network volume (e.g., NFS) accessed by multiple containers?

Answer: SQLite databases can corrupt due to failed sync operations, especially on unreliable filesystems; WAL mode reduces risk as sync failures during COMMIT cause loss of durability but not corruption, unlike other modes—checkpoint infrequently. Use default synchronous= FULL for maximum reliability. Corruption risks from disk/flash failures flipping bits, flash wear-leveling damaging files during power loss (even unopened DBs), QNX mmap() issues in WAL mode (fixed 2011), switching WAL modes with VACUUM causing stale caches in other processes (fixed 2011), I/O errors on WAL shared memory locks failing cache reset leading to corruption on subsequent writes (theoretical, not observed).

-----

-----

### Source [66]: https://sqlite.org/forum/info/02c1a784a2830a3d

Query: What are the failure modes and data corruption risks of using SQLite on a shared network volume (e.g., NFS) accessed by multiple containers?

Answer: Multiple hosts accessing shared SQLite DB over NFS is problematic; issues persist even with cachefilesd due to caching of random vs sequential access. NFSv4+ implementations may deviate from specs, causing problems beyond filesystem specification. Shared block storage recommended over NFS, but volume issues still possible.

-----

-----

### Source [67]: https://news.ycombinator.com/item?id=43089346

Query: What are the failure modes and data corruption risks of using SQLite on a shared network volume (e.g., NFS) accessed by multiple containers?

Answer: Avoid WAL mode when accessing SQLite over NFS. WAL is preferred otherwise but not for network filesystems.

-----

-----

### Source [68]: https://sqlite.org/faq.html

Query: What are the failure modes and data corruption risks of using SQLite on a shared network volume (e.g., NFS) accessed by multiple containers?

Answer: Avoid putting SQLite database files on NFS if multiple processes might access simultaneously, as it causes problems. On Windows, network file locking is buggy and undependable, potentially causing unexpected issues when sharing between machines.

-----

</details>

<details>
<summary>What are best practices for converting a Python application from filesystem-based state management to an async, database-backed approach using an ORM like SQLAlchemy?</summary>

### Source [70]: https://dev.to/devsnorte/setting-up-a-standalone-sqlalchemy-20-orm-application-298c

Query: What are best practices for converting a Python application from filesystem-based state management to an async, database-backed approach using an ORM like SQLAlchemy?

Answer: To set up a standalone SQLAlchemy 2.0 ORM application, use the ORM built on Core for domain object models mapped to database schemas, enabling object-oriented operations on tables and columns. Create a single engine with create_engine() function, passing a database URL (e.g., sqlite+pysqlite:///:memory:, sqlite+pysqlite:///dbname.db, or remote ports) and configuration options like echo=True for SQL logging. Use context managers for connections: with engine.connect() as conn: to execute queries like text('SELECT ...'), handling opening/closing automatically. Transactions are not auto-committed; explicitly call conn.commit() to persist changes, as seen in examples with BEGIN, query, COMMIT, or ROLLBACK. For ORM, define a Base class inheriting from DeclarativeBase, then subclass for each table to acquire mappings. Example engine setup in engine.py: import os; from sqlalchemy import create_engine; current_path = os.path.dirname(os.path.realpath(__file__)); database_url = f'sqlite+pysqlite:///{current_path}/database.db'; engine = create_engine(database_url, echo=True). Include functions like reset_database() to drop/recreate tables for testing. For migrations, use tools like Alembic: separate schema and data migrations, review auto-generated scripts, create focused migrations per feature (e.g., 'payments', 'tours'). Alembic supports schema migrations primarily, with data migrations implemented manually.

-----

-----

### Source [71]: https://atlasgo.io/guides/orms/sqlalchemy

Query: What are best practices for converting a Python application from filesystem-based state management to an async, database-backed approach using an ORM like SQLAlchemy?

Answer: For SQLAlchemy migrations as an alternative to Alembic, use Atlas for automatic, advanced schema management while defining schema via SQLAlchemy models. Atlas integrates seamlessly, supporting features beyond SQLAlchemy/Alembic like views, functions, procedures, triggers, sequences, row-level security. Use declarative workflow: schema as code synced to Atlas Cloud, auto-generating migration plans without a migration directory. CI/CD support via GitHub Actions, GitLab, CircleCI for detecting issues, testing migrations, data/functions. Quick start: Load SQLAlchemy models into Atlas in standalone mode (single module) or Python script mode. Manage advanced objects: define tables/columns/indexes with classes/decorators; extend to composite types, domains, triggers. Implement row-level security (RLS) policies in models for data access control. Automate actions with triggers in models. Use composite schemas for extensions. This enables powerful, automated migrations from filesystem state to database-backed, maintaining SQLAlchemy ORM usage.

-----

-----

### Source [72]: https://www.youtube.com/watch?v=TajZVh4heaM

Query: What are best practices for converting a Python application from filesystem-based state management to an async, database-backed approach using an ORM like SQLAlchemy?

Answer: To perform database migrations using Alembic with SQLAlchemy, install Alembic and SQLAlchemy via pip in a virtual environment (e.g., from requirements.txt). Configure Alembic's env.py: set sqlalchemy.url to your database, import models (e.g., UserBase), provide [Base.metadata] in target_metadata list for all models. Initialize Alembic with alembic init, generating versions/ directory with upgrade/downgrade files. Run alembic revision --autogenerate -m 'message' to create migration scripts based on model changes. Apply changes with alembic upgrade head to push to database. This manages table creation/updates, transitioning from filesystem to database state via SQLAlchemy ORM.

-----

-----

### Source [73]: http://sqlalchemy-migrate.readthedocs.org/en/latest/

Query: What are best practices for converting a Python application from filesystem-based state management to an async, database-backed approach using an ORM like SQLAlchemy?

Answer: SQLAlchemy Migrate handles schema change management, split into versioning (migrate.versioning) for database schema versioning and changeset (migrate.changeset) for migration management. Use for transitioning schema changes in SQLAlchemy applications to persistent database state.

-----

</details>

<details>
<summary>Why do modern application protocols like gRPC or GraphQL often lack native support for large file transfers, and what are the recommended architectural patterns for handling them?</summary>

### Source [74]: https://discuss.dgraph.io/t/grpc-message-limit-for-a-single-transaction/1947

Query: Why do modern application protocols like gRPC or GraphQL often lack native support for large file transfers, and what are the recommended architectural patterns for handling them?

Answer: gRPC imposes a message length limit of 4MB for a single transaction. Attempting to ingest a large number of quads (e.g., 100k quads in a sample program or over 10 million in application code) in one transaction builds up client-side and hits this limit upon commit, causing errors. Short-term workarounds include increasing the gRPC server message limit or splitting ingest into multiple smaller transactions (e.g., 50k quads each), though the latter defeats the purpose of transactions for atomicity.

-----

-----

### Source [75]: https://stackoverflow.blog/2022/11/28/when-to-use-grpc-vs-graphql/

Query: Why do modern application protocols like gRPC or GraphQL often lack native support for large file transfers, and what are the recommended architectural patterns for handling them?

Answer: gRPC uses Protocol Buffers (protobufs) in a binary format that includes only values, resulting in smaller messages compared to GraphQL's text-based JSON, which includes field names. Smaller messages transfer faster over networks. gRPC lacks default values in messages (unlike GraphQL for some cases), further reducing size but affecting developer experience as unset fields and defaults are indistinguishable. gRPC supports client and bidirectional streaming via HTTP/2. Limitations include inability to use most API proxies and needing proxies like Connect for browser use. GraphQL weaknesses include complex rate limiting due to flexible queries allowing arbitrary nesting in single requests, inefficient text transport, and no default HTTP GET caching.

-----

-----

### Source [76]: https://wundergraph.com/blog/is-grpc-really-better-for-microservices-than-graphql

Query: Why do modern application protocols like gRPC or GraphQL often lack native support for large file transfers, and what are the recommended architectural patterns for handling them?

Answer: gRPC's compact binary format reduces transmitted data size, beneficial for large datasets like machine learning pipelines or high-throughput messaging, outperforming GraphQL's text-based JSON overhead. However, gRPC enforces predefined contracts leading to over-fetching (e.g., requesting a name returns full profile) and lacks built-in multi-service data aggregation. Limited browser support due to no native HTTP/2 low-level streaming APIs, despite networking support. gRPC supports native bidirectional streaming over HTTP/2 with Protocol Buffers, more efficient for high-throughput real-time updates than GraphQL subscriptions via WebSockets or SSE.

-----

-----

### Source [77]: https://www.redhat.com/en/blog/apis-soap-rest-graphql-grpc

Query: Why do modern application protocols like gRPC or GraphQL often lack native support for large file transfers, and what are the recommended architectural patterns for handling them?

Answer: gRPC uses Protocol Buffers binary data format for fast data movement, contrasting bulky text-based protocols like SOAP XML. Challenges include both client and server needing identical Protocol Buffers specs, complicating version control—adding fields risks breaking code unlike REST/GraphQL. Developers may avoid deserializing binary data, working at bit level for efficiency, leading to dependency on speed gains.

-----

</details>

<details>
<summary>What are practical SQL query patterns for generating application analytics, such as user engagement and resource usage, directly from a PostgreSQL production database?</summary>

### Source [78]: https://www.postgresql.org/docs/current/using-explain.html

Query: What are practical SQL query patterns for generating application analytics, such as user engagement and resource usage, directly from a PostgreSQL production database?

Answer: The EXPLAIN command displays the query plan that PostgreSQL's planner creates for any query, which is critical for performance optimization in analytics queries. The planner chooses plans based on query structure and data properties. Query plans include scan nodes for accessing base tables (e.g., Seq Scan, Index Scan) and upper nodes for joins, aggregations, sorting needed in analytics like user engagement summaries. Examples show plans for queries with subplans, filters, and NOT IN conditions useful for exclusion in usage metrics: EXPLAIN SELECT * FROM tenk1 t WHERE t.unique1 NOT IN (SELECT o.unique1 FROM onek o); reveals Seq Scan with hashed SubPlan using Index Only Scan. EXPLAIN ANALYZE provides execution details like actual time, rows, loops, buffers: EXPLAIN ANALYZE SELECT * FROM polygon_tbl WHERE f1 @> polygon '(0.5,2.0)'; shows Seq Scan costs, actual rows=0, planning/execution times. Use EXPLAIN ANALYZE on production analytics queries (e.g., engagement counts, resource usage aggregates) to identify slow scans or joins, optimize indexes, and ensure efficient plans without full execution impact in planning mode.

-----

-----

### Source [79]: https://www.postgresql.org/docs/current/monitoring-stats.html

Query: What are practical SQL query patterns for generating application analytics, such as user engagement and resource usage, directly from a PostgreSQL production database?

Answer: PostgreSQL's cumulative statistics system in pg_stat views collects server activity data ideal for application analytics like user engagement and resource usage directly from production databases. Key views include pg_stat_user_tables for table accesses (seq_tup_read, seq_tup_hot_updated, n_tup_ins/upd/del), idx_scan/blks_hit/miss for index usage efficiency, last_vacuum/analyze times. pg_stat_user_indexes tracks index scans, tuples read/fetched. pg_stat_bgwriter for checkpoint stats, buffers stats. pg_stat_database for database-wide metrics: tup_returned/fetched, conflicts, temp_blks, xact_commit/rollback, blks_read/hit. pg_stat_activity shows current queries, states, wait events for real-time usage. pg_stat_statements (with extension) aggregates normalized query stats: calls, total_time, rows, shared_blks_hit/read/dirtied. For engagement: query pg_stat_user_tables joined with application logs/tables for active users/pages. Resource usage: sum blks_read across databases/tables, query durations from pg_stat_statements. Regularly query these for trends, e.g., SELECT schemaname, seq_scan, seq_tup_read FROM pg_stat_user_tables ORDER BY seq_tup_read DESC; to find high-read tables.

-----

-----

### Source [80]: https://www.postgresql.org/docs/current/sql-analyze.html

Query: What are practical SQL query patterns for generating application analytics, such as user engagement and resource usage, directly from a PostgreSQL production database?

Answer: ANALYZE collects statistics on table contents, storing in pg_statistic for accurate query planner estimates essential for efficient analytics queries on production data. For application analytics like user engagement (GROUP BY user_id aggregates) or resource usage (JOINs on logs), up-to-date statistics prevent poor plans with full table scans. Run ANALYZE after bulk loads/updates common in analytics pipelines. Syntax: ANALYZE [VERBOSE] [table/partition]; VERBOSE shows progress. Target specific columns: ANALYZE table (column); Use AUTOANALYZE (enabled by default) for auto-sampling on writes exceeding autovacuum_analyze_scale_factor. Increase statistics via ALTER TABLE table ALTER COLUMN col SET STATISTICS value; (0-10000, default 100) for better histograms/MCVs in skewed engagement data. For production: schedule manual ANALYZE on analytics-heavy tables, monitor pg_stat_user_tables.last_analyze. This ensures planner chooses optimal indexes/joins for queries like daily active users: SELECT user_id, COUNT(*) FROM events WHERE date_trunc('day', timestamp) = CURRENT_DATE GROUP BY user_id;

-----

-----

### Source [81]: https://www.postgresql.org/docs/current/runtime-config-query.html

Query: What are practical SQL query patterns for generating application analytics, such as user engagement and resource usage, directly from a PostgreSQL production database?

Answer: Query planning parameters optimize analytics workloads. default_statistics_target (default 100) sets column stats target; increase to 500+ for better estimates in engagement aggregates with skewed data, but raises ANALYZE time. GEQO (geqo_threshold=12) uses heuristics for complex JOIN-heavy analytics queries (many tables), reducing planning time vs exhaustive search. constraint_exclusion=on leverages CHECK constraints to skip tables in partitioned analytics schemas, e.g., date-partitioned user events: SELECT * FROM events WHERE date='2026-01-22'; skips irrelevant partitions. cursor_tuple_fraction (0.1) biases fast-start plans for paginated analytics result sets. plan_cache_mode=auto chooses custom/generic plans for prepared analytics statements; force_generic_plan reuses across params. recursive_worktable_factor=10.0 tunes recursive CTEs for graph analytics like user referral chains. jit_above_cost=500000 enables JIT for compute-heavy GROUP BYs in resource usage reports. Tune for production: higher default_statistics_target, geqo_threshold based on join count in multi-table engagement queries.

-----

-----

### Source [82]: https://www.tigerdata.com/learn/guide-to-data-analysis-on-postgresql

Query: What are practical SQL query patterns for generating application analytics, such as user engagement and resource usage, directly from a PostgreSQL production database?

Answer: The guide covers implementing common data analysis use cases on PostgreSQL, including analytics patterns scalable for growing data. Key patterns: Aggregation for metrics like user engagement (daily active users: SELECT DATE_TRUNC('day', created_at) as day, COUNT(DISTINCT user_id) FROM events GROUP BY 1;), resource usage (AVG(duration) GROUP BY resource_id). Window functions for rankings, running totals: ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY session_start), LAG/LEAD for session analysis. Cohort analysis: user retention with first_login date. Time-series: GENERATE_SERIES for missing dates in usage reports. Sampling: TABLESAMPLE for large-table previews. Materialized views for pre-aggregated dashboards: CREATE MATERIALIZED VIEW daily_engagement AS SELECT date, COUNT(*) FROM events GROUP BY date; REFRESH daily. Indexing: BRIN for time-series, GIN for JSON logs. Partitioning by range (dates) for engagement tables. EXPLAIN ANALYZE all queries. Scaling: Parallel queries (max_parallel_workers), extensions like TimescaleDB for hypertables.

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>https://dev.to/harry_do/part-3-mysql-vs-postgresql-features-capabilities-comparison-13gj</summary>

```markdown
Alright, let's get into the nitty-gritty differences between MySQL and PostgreSQL. It's time to see how their core philosophies and features actually play out in the real world.

## 1. Philosophy & Design Principles: The Core DNA

💡 **Key Insight:** Understanding the fundamental design philosophies helps predict how each database will behave in different scenarios. Think of it as getting to know someone's personality before you start working together.

Here's the thing: MySQL and PostgreSQL were born with different goals in mind, and you can see it in every decision they make.

### 1.1 MySQL: The "Keep It Simple, Keep It Fast" Approach

**Core Principle:** "Speed, Simplicity, and Reliability"

MySQL is like that friend who always shows up on time, doesn't complicate things, and just gets the job done. It's engineered to be fast and straightforward, making it the go-to choice for web applications where you're mostly reading data and want things to just _work_.

**What MySQL Really Cares About:**

- ⚡ **Performance First:** It's optimized for speed and quick response times—MySQL wants to be the fastest kid on the block
- 🎯 **Simplicity:** Easy to set up, configure, and maintain—no PhD required

- 🔒 **Reliability:** Stable and dependable for production workloads—it won't randomly flake out on you
- 📚 **Ease of Use:** Minimal learning curve—you can be productive in an afternoon

### 1.2 PostgreSQL: The "Power User's Swiss Army Knife" Approach

**Core Principle:** "Extensibility, Standards Compliance, and Data Integrity"

PostgreSQL is like that overachieving friend who's prepared for _everything_. It's designed to be the most feature-rich, standards-compliant, and robust system possible. If MySQL is a reliable Honda Civic, PostgreSQL is a fully-loaded Tesla with every bell and whistle you can imagine.

**What PostgreSQL Really Cares About:**

- 🔧 **Extensibility:** Highly customizable and extensible architecture—you can make it do almost anything
- 📏 **Standards Compliance:** Strict adherence to SQL standards—it's the teacher's pet of databases
- 🛡️ **Data Integrity:** Robust ACID compliance and transaction support—your data is _safe_
- ⭐ **Advanced Features:** Rich set of advanced database features—it's like getting 10 databases in one

## 2. Standards Compliance: SQL Standard Adherence

PostgreSQL has consistently maintained strong adherence to SQL standards, while MySQL has historically taken a more pragmatic approach, prioritizing practicality over strict compliance. However, recent MySQL versions have significantly improved in this area.

**MySQL 8.4: Improved SQL Compliance**

MySQL 8.4 has made substantial progress in SQL standards compliance. Key improvements include:

- Window functions for advanced analytical queries
- Common Table Expressions (CTEs) for more readable and maintainable queries
- Comprehensive JSON functions and operators
- Atomic DDL operations and improved error handling for safer schema changes

However, some advanced SQL features remain limited or unavailable compared to PostgreSQL, including partial indexes, fully recursive CTEs, and certain SQL:2011+ constructs.

**PostgreSQL 17: Comprehensive Standards Support**

PostgreSQL maintains the highest level of SQL standards compliance among open-source databases:

- Full support for window functions and CTEs, including recursive queries
- Partial and expression-based indexes for optimized query performance
- Advanced full-text search capabilities
- Extensive JSON/JSONB operators and indexing support
- Strict adherence to ANSI SQL standards with early adoption of new features

## 3. Data Types & Flexibility

PostgreSQL and MySQL take fundamentally different approaches to data type support. MySQL focuses on standard SQL types with broad compatibility, while PostgreSQL provides an extensive type system designed for specialized use cases.

| Data Type Category | MySQL 8.4 | PostgreSQL 17 |
| --- | --- | --- |
| **JSON Support** | 🟡 **Good** \- Binary storage, functional indexes | 🟢 **Superior** \- JSONB, GIN indexes, JSON\_TABLE() |
| **Array Support** | 🔴 **None** \- JSON arrays or normalized tables | 🟢 **Native** \- True arrays with rich operators |
| **Custom Types** | 🔴 **Limited** \- Basic ENUM only | 🟢 **Extensive** \- Composite, enum, domain types |
| **Range/Interval** | 🔴 **Manual** \- Separate start/end columns | 🟢 **Native** \- TSRANGE, DATERANGE with operators |
| **Geospatial** | 🟡 **Basic** \- Simple geometry functions | 🟢 **Advanced** \- PostGIS extension, full GIS |
| **Network Types** | 🔴 **None** \- Store as VARCHAR | 🟢 **Native** \- INET, CIDR with validation |
| **UUID Support** | 🟡 **Manual** \- CHAR(36) or BINARY(16) | 🟢 **Native** \- Dedicated type with functions |
| **Learning Curve** | 🟢 **Simple** \- Familiar SQL types | 🔴 **Complex** \- Many specialized options |

### JSONB: A Game-Changer for Unstructured Data

**PostgreSQL's JSONB support stands out as a critical differentiator**, particularly for applications dealing with unstructured or semi-structured data. This capability can eliminate the need for maintaining a separate document database for many use cases with moderate complexity.

**Key Advantages of PostgreSQL JSONB:**

- **Native Binary Storage:** JSONB stores data in a decomposed binary format, enabling efficient querying and indexing without parsing overhead
- **GIN Indexing:** Generalized Inverted Index (GIN) support allows fast lookups on JSON properties and containment operations
- **Rich Operators:** Comprehensive set of operators for querying, filtering, and manipulating JSON data directly in SQL
- **Type Safety:** Validates JSON structure while maintaining flexibility for schema-less data
- **Query Performance:** Eliminates the overhead of maintaining synchronization between a relational database and a separate document store

**Practical Implications:**

When your application requires both structured relational data and flexible document-like storage, PostgreSQL's JSONB allows you to handle both within a single database system. This reduces architectural complexity, eliminates data synchronization issues, and simplifies your infrastructure.

For simple to moderate unstructured data requirements, PostgreSQL can effectively replace a dedicated document database like MongoDB, providing the benefits of both relational and document-oriented approaches in one system.

**MySQL's JSON Support:**

MySQL 8.4 provides functional JSON support with binary storage and path-specific indexing, which is adequate for basic JSON storage and retrieval. However, it lacks the comprehensive indexing capabilities and rich operator set that PostgreSQL offers, making it less suitable for heavy JSON querying workloads.

## 4. Indexing Capabilities: Different Strategies for Different Needs

This is where things get really interesting. MySQL and PostgreSQL have fundamentally different indexing philosophies, and understanding these differences will save you a lot of headaches.

| Indexing Aspect | MySQL 8.4 | PostgreSQL 17 |
| --- | --- | --- |
| **Index Architecture** | 🔵 **Clustered** \- Data stored in PK order | 🟡 **Heap** \- Data stored separately from indexes |
| **Index Types** | 🔴 **Limited** \- Primarily B-tree + JSON functional | 🟢 **Extensive** \- B-tree, GIN, GiST, BRIN, partial, expression |
| **Primary Key Access** | 🟢 **Exceptional** \- Direct clustered access | 🟡 **Good** \- Index + heap lookup |
| **Complex Queries** | 🟡 **Limited** \- B-tree optimization only | 🟢 **Excellent** \- Specialized indexes for any pattern |
| **Configuration** | 🟢 **Simple** \- Automatic optimization | 🔴 **Complex** \- Requires index type selection |
| **Random Inserts** | 🔴 **Slower** \- Clustered hotspots | 🟢 **Consistent** \- No clustering overhead |
| **JSON Indexing** | 🟡 **Functional** \- Path-specific indexes | 🟢 **Advanced** \- GIN indexes on entire documents |
| **Partial Indexes** | 🔴 **None** \- Must index entire column | 🟢 **Native** \- Index only matching conditions |
| **Expression Indexes** | 🟢 **Full Support** \- Functional indexes on any expression (8.0.13+) | 🟢 **Full support** \- Any computed expression |

💡 **For deeper understanding:** To fully grasp how index scans work and why these differences matter, refer to [Part 2 - Data Storage](https://part%202%20-%20mysql%20vs%20postgresql:%202.%20data%20storage.md/) where we explore the underlying storage architectures (clustered vs heap-based storage) that drive these indexing behaviors.

## 5. Index Scan Types: How They Actually Find Your Data

Here's where the rubber meets the road. Both databases can scan indexes, but they do it in their own special ways.

| Scan Type | MySQL 8.4 | PostgreSQL 17 |
| --- | --- | --- |
| **Index Scan** | 🟢 **Standard** \- B-tree traversal to find rows | 🟢 **Standard** \- B-tree traversal to find rows |
| **Index Only Scan** | 🟡 **Covering Index** \- Secondary index with INCLUDE-like behavior | 🟢 **Native** \- Index-only scan without heap access |
| **Bitmap Scan** | 🔴 **None** \- Uses range or index merge | 🟢 **Advanced** \- Bitmap heap scan for multiple conditions |
| **Sequential Scan** | 🟢 **Full Table** \- Reads all table pages | 🟢 **Full Table** \- Reads all table pages |
| **Index Range Scan** | 🟢 **Efficient** \- Range queries on clustered/secondary indexes | 🟢 **Efficient** \- Range queries with heap lookups |
| **Parallel Scans** | 🟡 **Basic** \- Parallel query execution (8.0+) | 🟢 **Advanced** \- Parallel index, bitmap, and sequential scans |

### The Bitmap Scan Deep Dive

**Bitmap Scan (PostgreSQL's Secret Weapon)**

PostgreSQL's bitmap scan is one of those features that makes database nerds weep with joy. It's a sophisticated strategy for handling complex WHERE clauses with multiple conditions, and it's something MySQL simply doesn't have.

**How Bitmap Scan Actually Works:**

Let's say you have this query:

```
-- Query with multiple conditions
SELECT * FROM orders
WHERE customer_id = 123
AND order_date >= '2024-01-01'
AND status = 'pending';

-- PostgreSQL execution plan:
-- 1. Bitmap Index Scan on idx_customer (customer_id = 123)
-- 2. Bitmap Index Scan on idx_date (order_date >= '2024-01-01')
-- 3. Bitmap Index Scan on idx_status (status = 'pending')
-- 4. BitmapAnd: Combine all bitmaps using AND operation
-- 5. Bitmap Heap Scan: Access heap pages only for matching rows
```

**Why Bitmap Scans Are So Cool:**

- **Multiple Index Combination:** Efficiently combines multiple indexes using bitmap operations—it's like magic
- **Reduced Heap Access:** Only accesses heap pages that contain matching rows—no wasted I/O
- **Memory Efficient:** Bitmap representation is compact compared to storing all row pointers
- **Complex Conditions:** Handles OR, AND combinations of multiple indexes seamlessly—handles whatever you throw at it

**What MySQL Does Instead:**

```
-- MySQL uses index intersection or chooses best single index
-- Option 1: Index intersection (limited support)
SELECT * FROM orders
WHERE customer_id = 123 AND order_date >= '2024-01-01';

-- Option 2: Query optimizer chooses single best index
-- Typically uses idx_customer, then filters remaining conditions
```

## 6. Views Support: Real-Time vs Pre-Computed

| View Feature | MySQL 8.4 | PostgreSQL 17 |
| --- | --- | --- |
| **Standard Views** | 🟢 **Full Support** \- Dynamic query execution | 🟢 **Full Support** \- Dynamic query execution |
| **Materialized Views** | 🔴 **None** \- Must use tables + triggers | 🟢 **Native** \- Pre-computed and stored results |
| **View Updates** | 🟡 **Limited** \- Simple views only | 🟢 **Advanced** \- Complex views with rules |
| **Refresh Options** | 🔴 **Manual** \- Application-level logic | 🟢 **Flexible** \- Manual, automatic, incremental |
| **Performance** | 🔴 **Query-dependent** \- No caching mechanism | 🟢 **Optimized** \- Materialized views cache results |
| **Storage Overhead** | 🟢 **Minimal** \- Views are just queries | 🔴 **Higher** \- Materialized views require storage |

### Why Materialized Views Matter

**Materialized Views are a game-changer for analytical workloads and complex reporting.** PostgreSQL's native support for materialized views provides a significant advantage over MySQL in scenarios where you need to optimize expensive, frequently-accessed queries.

**What Makes Materialized Views Special:**

1.  **Pre-computed Results:** Instead of executing a complex query every time, the results are computed once and stored physically on disk
2.  **Indexable:** You can create indexes on materialized views, making them as fast as regular tables for subsequent queries
3.  **Flexible Refresh:** Choose when to refresh—manually on-demand, scheduled via cron, or automatically with triggers
4.  **Perfect for Analytics:** Dashboards, reports, and analytical queries that aggregate millions of rows can return instantly instead of taking seconds or minutes

**Real-World Impact:**

Imagine a dashboard that shows sales analytics by aggregating millions of transactions. With standard views in MySQL, this query runs every time someone loads the dashboard. With PostgreSQL's materialized views, you compute it once (say, every hour), and all dashboard accesses are instant—just reading pre-computed data.

**MySQL's Workaround:**

Without native materialized views, MySQL users must manually create summary tables, write triggers or scheduled jobs to keep them updated, and implement their own refresh logic. This is error-prone, harder to maintain, and requires significant application-level code.

## 7. Security Features: Locking Down Your Data

| Security Feature | MySQL 8.4 | PostgreSQL 17 |
| --- | --- | --- |
| **Authentication Methods** | 🟡 **Multiple** \- Native, LDAP, PAM plugins | 🟢 **Extensive** \- Native, LDAP, Kerberos, RADIUS, etc. |
| **Row-Level Security** | 🔴 **None** \- Application-level implementation required | 🟢 **Native** \- Built-in row-level security policies |
| **Column Encryption** | 🟡 **Basic** \- Transparent data encryption (TDE) | 🟢 **Advanced** \- Column-level encryption with pgcrypto |
| **SSL/TLS Support** | 🟢 **Full** \- Complete SSL/TLS implementation | 🟢 **Full** \- Complete SSL/TLS implementation |
| **Audit Logging** | 🟡 **Enterprise** \- Available in commercial version | 🟢 **Open Source** \- pg\_audit extension available |
| **User Management** | 🟢 **Standard** \- Role-based access control | 🟢 **Advanced** \- Sophisticated role hierarchy |
| **Data Masking** | 🟡 **Enterprise** \- Commercial feature | 🟢 **Community** \- Available through extensions |
| **Compliance Features** | 🟡 **Enterprise-focused** \- Commercial compliance tools | 🟢 **Built-in** \- Strong compliance capabilities |

**PostgreSQL's Row-Level Security: A Nice Addition**

PostgreSQL offers native row-level security (RLS), allowing you to define security policies directly in the database that automatically filter rows based on the user. MySQL requires implementing this in application code if needed.

**The Trade-off:** Both databases provide solid security fundamentals. PostgreSQL includes more advanced security features in the open-source edition, while MySQL reserves some advanced features for the commercial Enterprise Edition.

## Wrapping Up

### Design Philosophy Summary

| Priority | MySQL 8.4 | PostgreSQL 17 |
| --- | --- | --- |
| **Primary Focus** | Performance & Simplicity | Features & Standards Compliance |
| **Target Use Case** | Web applications, read-heavy workloads | Complex applications, analytics, data integrity |
| **Philosophy** | Pragmatic, get it done fast | Academic, do it right by the standard |
| **Learning Curve** | Low - productive quickly | Moderate - more to learn |
| **Configuration** | Minimal - sensible defaults | Flexible - tuning options available |

Both are excellent databases. Choose based on your workload characteristics and team expertise, not on what's "better" in the abstract.
```

</details>

<details>
<summary>https://fastapi.tiangolo.com/tutorial/request-files/</summary>

The provided markdown content is a generic tutorial on handling file uploads in FastAPI. The article guidelines for Lesson 33 specify a focus on database migration, schema design, tool refactoring, local/cloud database setup, migrations, rate limiting, and custom HTTP endpoints *specifically for file transfer workarounds related to the MCP agent (uploading article guidelines, downloading research results)*.

The generic FastAPI tutorial content is not pertinent to the specific implementation details or the problem context of the AI agent lesson described in the guidelines. Therefore, this content is considered irrelevant to the core article.

```markdown
```

</details>

<details>
<summary>https://neon.com/guides/rate-limiting</summary>

The provided markdown content on "Rate Limiting in Postgres" is a general guide on implementing rate limiting using SQL advisory locks and counters. However, the `article_guidelines` for Section 8, "Rate Limiting for MCP Tools," explicitly refers to a `source.md` file and specific line numbers within that file for the `ToolCallUsage` model and `@rate_limited` decorator implementation. The guidelines describe the implementation in the context of Python, MCP tools, and a specific course's codebase, which is different from the generic SQL-based rate limiting approach presented in the scraped markdown.

Therefore, the provided markdown content is not pertinent to the specific requirements of Section 8 as detailed in the `article_guidelines`. It would introduce a different implementation and context than what the lesson is designed to teach.

Consequently, all content from the provided markdown is considered irrelevant to the *specific guidelines* for Section 8. Returning only the cleaned markdown means returning an empty string in this case, as no part of the provided text aligns with the detailed requirements for this specific section of the course.

</details>

<details>
<summary>https://www.cybertec-postgresql.com/en/int4-vs-int8-vs-uuid-vs-numeric-performance-on-bigger-joins/</summary>



</details>


## Code Sources

<details>
<summary>https://github.com/GoogleCloudPlatform/cloud-sql-python-connector</summary>

# Repository analysis for https://github.com/GoogleCloudPlatform/cloud-sql-python-connector

## Summary
Repository: googlecloudplatform/cloud-sql-python-connector
Commit: 820715822944e67a7a2a83d9962835ad43a7b2e4
Files analyzed: 94

Estimated tokens: 112.4k

## File tree
```Directory structure:
└── googlecloudplatform-cloud-sql-python-connector/
    ├── README.md
    ├── build.sh
    ├── CHANGELOG.md
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── noxfile.py
    ├── pyproject.toml
    ├── requirements-test.txt
    ├── requirements.txt
    ├── SECURITY.md
    ├── .flake8
    ├── google/
    │   └── cloud/
    │       └── sql/
    │           └── connector/
    │               ├── __init__.py
    │               ├── asyncpg.py
    │               ├── client.py
    │               ├── connection_info.py
    │               ├── connection_name.py
    │               ├── connector.py
    │               ├── enums.py
    │               ├── exceptions.py
    │               ├── instance.py
    │               ├── lazy.py
    │               ├── monitored_cache.py
    │               ├── pg8000.py
    │               ├── py.typed
    │               ├── pymysql.py
    │               ├── pytds.py
    │               ├── rate_limiter.py
    │               ├── refresh_utils.py
    │               ├── resolver.py
    │               ├── utils.py
    │               └── version.py
    ├── samples/
    │   ├── cloudrun/
    │   │   ├── README.md
    │   │   ├── mysql/
    │   │   │   ├── Dockerfile
    │   │   │   ├── main.py
    │   │   │   └── requirements.txt
    │   │   ├── postgres/
    │   │   │   ├── Dockerfile
    │   │   │   ├── main.py
    │   │   │   └── requirements.txt
    │   │   └── sqlserver/
    │   │       ├── Dockerfile
    │   │       ├── main.py
    │   │       └── requirements.txt
    │   └── notebooks/
    │       ├── mysql_python_connector.ipynb
    │       ├── postgres_python_connector.ipynb
    │       └── sqlserver_python_connector.ipynb
    ├── tests/
    │   ├── conftest.py
    │   ├── system/
    │   │   ├── test_asyncpg_connection.py
    │   │   ├── test_asyncpg_iam_auth.py
    │   │   ├── test_connector_object.py
    │   │   ├── test_ip_types.py
    │   │   ├── test_pg8000_connection.py
    │   │   ├── test_pg8000_iam_auth.py
    │   │   ├── test_pymysql_connection.py
    │   │   ├── test_pymysql_iam_auth.py
    │   │   └── test_pytds_connection.py
    │   └── unit/
    │       ├── mocks.py
    │       ├── test_asyncpg.py
    │       ├── test_client.py
    │       ├── test_connection_name.py
    │       ├── test_connector.py
    │       ├── test_instance.py
    │       ├── test_lazy.py
    │       ├── test_monitored_cache.py
    │       ├── test_packaging.py
    │       ├── test_pg8000.py
    │       ├── test_pymysql.py
    │       ├── test_pytds.py
    │       ├── test_rate_limiter.py
    │       ├── test_refresh_utils.py
    │       ├── test_resolver.py
    │       └── test_utils.py
    ├── .ci/
    │   └── cloudbuild.yaml
    └── .github/
        ├── auto-label.yaml
        ├── blunderbuss.yml
        ├── CODEOWNERS
        ├── flakybot.yaml
        ├── header-checker-lint.yml
        ├── labels.yml
        ├── release-please.yml
        ├── release-trigger.yml
        ├── renovate.json5
        ├── trusted-contribution.yml
        ├── ISSUE_TEMPLATE/
        │   ├── bug_report.yaml
        │   ├── documentation_issue.yaml
        │   ├── feature_request.yaml
        │   └── question.yaml
        └── workflows/
            ├── cloud_build_failure_reporter.yml
            ├── codeql.yml
            ├── coverage.yml
            ├── labels.yaml
            ├── lint.yml
            ├── schedule_reporter.yml
            ├── scorecard.yml
            └── tests.yml

```

## Extracted content
================================================
FILE: README.md
================================================
<p align="center">
    <a href="https://cloud.google.com/blog/topics/developers-practitioners/how-connect-cloud-sql-using-python-easy-way">
        <img src="https://raw.githubusercontent.com/GoogleCloudPlatform/cloud-sql-python-connector/main/docs/images/cloud-sql-python-connector.png" alt="cloud-sql-python-connector image">
    </a>
</p>

<h1 align="center">Cloud SQL Python Connector</h1>

[![Open In Colab][colab-badge]][colab-notebook]
[![CI][ci-badge]][ci-build]
[![pypi][pypi-badge]][pypi-docs]
[![PyPI download month][pypi-downloads]][pypi-docs]
[![python][python-versions]][pypi-docs]

[colab-badge]: https://colab.research.google.com/assets/colab-badge.svg
[colab-notebook]: https://colab.research.google.com/github/GoogleCloudPlatform/cloud-sql-python-connector/blob/main/samples/notebooks/postgres_python_connector.ipynb
[ci-badge]: https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/actions/workflows/tests.yml/badge.svg?event=push
[ci-build]: https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/actions/workflows/tests.yml?query=event%3Apush+branch%3Amain
[pypi-badge]: https://img.shields.io/pypi/v/cloud-sql-python-connector
[pypi-docs]: https://pypi.org/project/cloud-sql-python-connector
[pypi-downloads]: https://img.shields.io/pypi/dm/cloud-sql-python-connector.svg
[python-versions]: https://img.shields.io/pypi/pyversions/cloud-sql-python-connector

The _Cloud SQL Python Connector_ is a Cloud SQL connector designed for use with the
Python language. Using a Cloud SQL connector provides a native alternative to the
[Cloud SQL Auth Proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy) while
providing the following benefits:

* **IAM Authorization:** uses IAM permissions to control who/what can connect to
  your Cloud SQL instances
* **Improved Security:** uses robust, updated TLS 1.3 encryption and
  identity verification between the client connector and the server-side proxy,
  independent of the database protocol.
* **Convenience:** removes the requirement to use and distribute SSL
  certificates, as well as manage firewalls or source/destination IP addresses.
* (optionally) **IAM DB Authentication:** provides support for
  [Cloud SQL’s automatic IAM DB AuthN][iam-db-authn] feature.

[iam-db-authn]: https://cloud.google.com/sql/docs/postgres/authentication

The Cloud SQL Python Connector is a package to be used alongside a database driver.
Currently supported drivers are:
 - [`pymysql`](https://github.com/PyMySQL/PyMySQL) (MySQL)
 - [`pg8000`](https://github.com/tlocke/pg8000) (PostgreSQL)
 - [`asyncpg`](https://github.com/MagicStack/asyncpg) (PostgreSQL)
 - [`pytds`](https://github.com/denisenkom/pytds) (SQL Server)


## Installation

You can install this library with `pip install`, specifying the driver
based on your database dialect.

### MySQL
```
pip install "cloud-sql-python-connector[pymysql]"
```
### Postgres
There are two different database drivers that are supported for the Postgres dialect:

#### pg8000
```
pip install "cloud-sql-python-connector[pg8000]"
```
#### asyncpg
```
pip install "cloud-sql-python-connector[asyncpg]"
```
### SQL Server
```
pip install "cloud-sql-python-connector[pytds]"
```

### APIs and Services

This package requires the following to successfully make Cloud SQL Connections:

- IAM principal (user, service account, etc.) with the
[Cloud SQL Client][client-role] role. This IAM principal will be used for
[credentials](#credentials).
- The [Cloud SQL Admin API][admin-api] to be enabled within your Google Cloud
Project. By default, the API will be called in the project associated with
the IAM principal.

[admin-api]: https://console.cloud.google.com/apis/api/sqladmin.googleapis.com
[client-role]: https://cloud.google.com/sql/docs/mysql/roles-and-permissions

### Credentials

This library uses the [Application Default Credentials (ADC)][adc] strategy for
resolving credentials. Please see [these instructions for how to set your ADC][set-adc]
(Google Cloud Application vs Local Development, IAM user vs service account credentials),
or consult the [google.auth][google-auth] package.

To explicitly set a specific source for the credentials, see
[Configuring the Connector](#configuring-the-connector) below.

[adc]: https://cloud.google.com/docs/authentication#adc
[set-adc]: https://cloud.google.com/docs/authentication/provide-credentials-adc
[google-auth]: https://google-auth.readthedocs.io/en/master/reference/google.auth.html

## Usage

This package provides several functions for authorizing and encrypting
connections. These functions are used with your database driver to connect to
your Cloud SQL instance.

The instance connection name for your Cloud SQL instance is always in the
format "project:region:instance".

### How to use this Connector

To connect to Cloud SQL using the connector, inititalize a `Connector`
object and call its `connect` method with the proper input parameters.

The `Connector` itself creates connection objects by calling its `connect` method but does not manage database connection pooling. For this reason, it is recommended to use the connector alongside a library that can create connection pools, such as [SQLAlchemy](https://www.sqlalchemy.org/). This will allow for connections to remain open and be reused, reducing connection overhead and the number of connections needed.

In the Connector's `connect` method below, input your connection string as the first positional argument and the name of the database driver for the second positional argument. Insert the rest of your connection keyword arguments like user, password and database. You can also set the optional `timeout` or `ip_type` keyword arguments.

To use this connector with SQLAlchemy, use the `creator` argument for `sqlalchemy.create_engine`:

```python
from google.cloud.sql.connector import Connector
import sqlalchemy

# initialize Connector object
connector = Connector()

# initialize SQLAlchemy connection pool with Connector
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=lambda: connector.connect(
        "project:region:instance",
        "pymysql",
        user="my-user",
        password="my-password",
        db="my-db-name"
    ),
)
```

The returned connection pool engine can then be used to query and modify the database.

```python
# insert statement
insert_stmt = sqlalchemy.text(
    "INSERT INTO my_table (id, title) VALUES (:id, :title)",
)

with pool.connect() as db_conn:
    # insert into database
    db_conn.execute(insert_stmt, parameters={"id": "book1", "title": "Book One"})

    # query database
    result = db_conn.execute(sqlalchemy.text("SELECT * from my_table")).fetchall()

    # commit transaction (SQLAlchemy v2.X.X is commit as you go)
    db_conn.commit()

    # Do something with the results
    for row in result:
        print(row)
```

To close the `Connector` object's background resources, call its `close()` method as follows:

```python
connector.close()
```

> [!NOTE]
>
> For more examples of using SQLAlchemy to manage connection pooling with the connector,
> please see [Cloud SQL SQLAlchemy Samples](https://cloud.google.com/sql/docs/postgres/connect-connectors#python_1).

### Configuring the Connector

If you need to customize something about the connector, or want to specify
defaults for each connection to make, you can initialize a
`Connector` object as follows:

```python
from google.cloud.sql.connector import Connector

# Note: all parameters below are optional
connector = Connector(
    ip_type="public",  # can also be "private" or "psc"
    enable_iam_auth=False,
    timeout=30,
    credentials=custom_creds, # google.auth.credentials.Credentials
    refresh_strategy="lazy",  # can be "lazy" or "background"
)
```

### Using Connector as a Context Manager

The `Connector` object can also be used as a context manager in order to
automatically close and cleanup resources, removing the need for explicit
calls to `connector.close()`.

Connector as a context manager:

```python
from google.cloud.sql.connector import Connector
import sqlalchemy

# initialize Cloud SQL Python Connector as context manager
with Connector() as connector:
    # initialize SQLAlchemy connection pool with Connector
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=lambda: connector.connect(
            "project:region:instance",
            "pymysql",
            user="my-user",
            password="my-password",
            db="my-db-name"
        ),
    )
    # insert statement
    insert_stmt = sqlalchemy.text(
        "INSERT INTO my_table (id, title) VALUES (:id, :title)",
    )

    # interact with Cloud SQL database using connection pool
    with pool.connect() as db_conn:
        # insert into database
        db_conn.execute(insert_stmt, parameters={"id": "book1", "title": "Book One"})

        # commit transaction (SQLAlchemy v2.X.X is commit as you go)
        db_conn.commit()

        # query database
        result = db_conn.execute(sqlalchemy.text("SELECT * from my_table")).fetchall()

        # Do something with the results
        for row in result:
            print(row)
```

### Configuring a Lazy Refresh (Cloud Run, Cloud Functions etc.)

The Connector's `refresh_strategy` argument can be set to `"lazy"` to configure
the Python Connector to retrieve connection info lazily and as-needed.
Otherwise, a background refresh cycle runs to retrive the connection info
periodically. This setting is useful in environments where the CPU may be
throttled outside of a request context, e.g., Cloud Run, Cloud Functions, etc.

To set the refresh strategy, set the `refresh_strategy` keyword argument when
initializing a `Connector`:

```python
connector = Connector(refresh_strategy="lazy")
```

### Specifying IP Address Type

The Cloud SQL Python Connector can be used to connect to Cloud SQL instances
using both public and private IP addresses, as well as
[Private Service Connect][psc] (PSC). To specify which IP address type to connect
with, set the `ip_type` keyword argument when initializing a `Connector()` or when
calling `connector.connect()`.

Possible values for `ip_type` are `"public"` (default value),
`"private"`, and `"psc"`.

Example:

```python
conn = connector.connect(
    "project:region:instance",
    "pymysql",
    ip_type="private"  # use private IP
... insert other kwargs ...
)
```

> [!IMPORTANT]
>
> If specifying Private IP or Private Service Connect (PSC), your application must be
> attached to the proper VPC network to connect to your Cloud SQL instance. For most
> applications this will require the use of a [VPC Connector][vpc-connector].

[psc]: https://cloud.google.com/vpc/docs/private-service-connect
[vpc-connector]: https://cloud.google.com/vpc/docs/configure-serverless-vpc-access#create-connector

### Automatic IAM Database Authentication

Connections using [Automatic IAM database authentication](https://cloud.google.com/sql/docs/postgres/authentication#automatic) are supported when using Postgres or MySQL drivers.
First, make sure to [configure your Cloud SQL Instance to allow IAM authentication](https://cloud.google.com/sql/docs/postgres/create-edit-iam-instances#configure-iam-db-instance)
and [add an IAM database user](https://cloud.google.com/sql/docs/postgres/create-manage-iam-users#creating-a-database-user).

Now, you can connect using user or service account credentials instead of a password.
In the call to connect, set the `enable_iam_auth` keyword argument to true and the `user` argument to the appropriately formatted IAM principal.
> Postgres: For an IAM user account, this is the user's email address. For a service account, it is the service account's email without the `.gserviceaccount.com` domain suffix.

> MySQL: For an IAM user account, this is the user's email address, without the @ or domain name. For example, for `test-user@gmail.com`, set the `user` argument to `test-user`. For a service account, this is the service account's email address without the `@project-id.iam.gserviceaccount.com` suffix.

Example:

```python
conn = connector.connect(
     "project:region:instance",
     "pg8000",
     user="postgres-iam-user@gmail.com",
     db="my-db-name",
     enable_iam_auth=True,
 )
```

### SQL Server (MSSQL)

> [!IMPORTANT]
>
> If your SQL Server instance is set to [enforce SSL connections](https://cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#enforcing-ssl),
> you need to download the CA certificate for your instance and include `cafile={path to downloaded certificate}`
> and `validate_host=False`. This is a workaround for a [known issue](https://issuetracker.google.com/184867147).

#### Active Directory Authentication

Active Directory authentication for SQL Server instances is currently only supported on Windows.
First, make sure to follow [these steps](https://cloud.google.com/blog/topics/developers-practitioners/creating-sql-server-instance-integrated-active-directory-using-google-cloud-sql)
to set up a Managed AD domain and join your Cloud SQL instance to the domain.
[See here for more info on Cloud SQL Active Directory integration](https://cloud.google.com/sql/docs/sqlserver/ad).

Once you have followed the steps linked above, you can run the following code to return a connection object:

```python
conn = connector.connect(
    "project:region:instance",
    "pytds",
    db="my-db-name",
    active_directory_auth=True,
    server_name="public.[instance].[location].[project].cloudsql.[domain]",
)
```

Or, if using Private IP:

```python
conn = connector.connect(
    "project:region:instance",
    "pytds",
    db="my-db-name",
    active_directory_auth=True,
    server_name="private.[instance].[location].[project].cloudsql.[domain]",
    ip_type="private"
)
```

### Using Advanced Disaster Recovery and DNS domain names to identify instances

The connector can be configured to use DNS to look up an instance. 
Use a DNS name managed by Cloud SQL [Advanced Disaster Recovery](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery), 
or a domain name that you manage.

#### Using Advanced Recovery Write Endpoint DNS Name

[Advanced Disaster Recovery](https://docs.cloud.google.com/sql/docs/mysql/use-advanced-disaster-recovery)
creates geographically distributed replicas of your Cloud SQL database instance. When you perform 
switchover or failover on the database instance, the connector will gracefully disconnect from the
old primary instance and reconnect to the new primary instance. 

Follow the instructions in [Connect using Write Endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint)
to get the write endpoint DNS name for your primary instance. Then, use this write endpoint DNS
name to configure the connector.

#### Configure your DNS Records

The connector may be configured to use DNS that you define as well.

Add a DNS TXT record for the Cloud SQL instance to a **private** DNS server
or a private Google Cloud DNS Zone used by your application.

> [!NOTE]
>
> You are strongly discouraged from adding DNS records for your
> Cloud SQL instances to a public DNS server. This would allow anyone on the
> internet to discover the Cloud SQL instance name.

For example: suppose you wanted to use the domain name
`prod-db.mycompany.example.com` to connect to your database instance
`my-project:region:my-instance`. You would create the following DNS record:

* Record type: `TXT`
* Name: `prod-db.mycompany.example.com` – This is the domain name used by the application
* Value: `my-project:my-region:my-instance` – This is the Cloud SQL instance connection name

#### Configure the connector

Configure the connector to resolve DNS names by initializing it with
`resolver=DnsResolver` and replacing the instance connection name with the DNS
name in `connector.connect`:

```python
from google.cloud.sql.connector import Connector, DnsResolver
import pymysql
import sqlalchemy

# initialize Cloud SQL Python Connector with `resolver=DnsResolver`
with Connector(resolver=DnsResolver) as connector:
    # initialize SQLAlchemy connection pool with Connector
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=lambda: connector.connect(
            "prod-db.mycompany.example.com",  # using DNS name
            "pymysql",
            user="my-user",
            password="my-password",
            db="my-db-name"
        ),
    )
    # ... use SQLAlchemy engine normally
```

### Automatic failover using DNS domain names

> [!NOTE]
>
> Usage of the `asyncpg` driver does not currently support automatic failover.

When the connector is configured using a domain name, the connector will
periodically check if the DNS record for an instance changes. When the connector
detects that the domain name refers to a different instance, the connector will
close all open connections to the old instance. Subsequent connection attempts
will be directed to the new instance.

For example: suppose application is configured to connect using the
domain name `prod-db.mycompany.example.com`. Initially the private DNS
zone has a TXT record with the value `my-project:region:my-instance`. The
application establishes connections to the `my-project:region:my-instance`
Cloud SQL instance.

Then, to reconfigure the application to use a different database
instance, change the value of the `prod-db.mycompany.example.com` DNS record
from `my-project:region:my-instance` to `my-project:other-region:my-instance-2`

The connector inside the application detects the change to this
DNS record. Now, when the application connects to its database using the
domain name `prod-db.mycompany.example.com`, it will connect to the
`my-project:other-region:my-instance-2` Cloud SQL instance.

The connector will automatically close all existing connections to
`my-project:region:my-instance`. This will force the connection pools to
establish new connections. Also, it may cause database queries in progress
to fail.

The connector will poll for changes to the DNS name every 30 seconds by default.
You may configure the frequency of the connections using the Connector's
`failover_period` argument (i.e. `Connector(failover_period=60`). When this is
set to 0, the connector will disable polling and only check if the DNS record
changed when it is creating a new connection.

### Using the Python Connector with Python Web Frameworks

The Python Connector can be used alongside popular Python web frameworks such
as Flask, FastAPI, etc, to integrate Cloud SQL databases within your
web applications.

> [!NOTE]
>
> For serverless environments such as Cloud Functions, Cloud Run, etc, it may be
> beneficial to initialize the `Connector` with the lazy refresh strategy.
> i.e. `Connector(refresh_strategy="lazy")`
>
> See [Configuring a Lazy Refresh](#configuring-a-lazy-refresh-cloud-run-cloud-functions-etc)

#### Flask-SQLAlchemy

[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
is an extension for [Flask](https://flask.palletsprojects.com/en/2.2.x/)
that adds support for [SQLAlchemy](https://www.sqlalchemy.org/) to your
application. It aims to simplify using SQLAlchemy with Flask by providing
useful defaults and extra helpers that make it easier to accomplish
common tasks.

You can configure Flask-SQLAlchemy to connect to a Cloud SQL database from
your web application through the following:

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from google.cloud.sql.connector import Connector


# initialize Python Connector object
connector = Connector()

app = Flask(__name__)

# configure Flask-SQLAlchemy to use Python Connector
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+pg8000://"
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "creator": lambda: conn = connector.connect(
        "project:region:instance-name", # Cloud SQL Instance Connection Name
        "pg8000",
        user="my-user",
        password="my-password",
        db="my-database",
        ip_type="public"  # "private" for private IP
    )
}

# initialize the app with the extension
db = SQLAlchemy()
db.init_app(app)
```

For more details on how to use Flask-SQLAlchemy, check out the
[Flask-SQLAlchemy Quickstarts](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/)

#### FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance),
web framework for building APIs with Python based on standard Python type hints.

You can configure FastAPI to connect to a Cloud SQL database from
your web application using [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/14/orm/)
through the following:

```python
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector


# initialize Cloud SQL Python Connector
connector = Connector()

# create connection pool engine
engine = sqlalchemy.create_engine(
    "postgresql+pg8000://",
    creator=lambda: connector.connect(
        "project:region:instance-name", # Cloud SQL Instance Connection Name
        "pg8000",
        user="my-user",
        password="my-password",
        db="my-database",
        ip_type="public"  # "private" for private IP
    ),
)

# create SQLAlchemy ORM session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

To learn more about integrating a database into your FastAPI application,
follow along the [FastAPI SQL Database guide](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-models).

### Async Driver Usage

The Cloud SQL Connector is compatible with
[asyncio](https://docs.python.org/3/library/asyncio.html) to improve the speed
and efficiency of database connections through concurrency. You can use all
non-asyncio drivers through the `Connector.connect_async` function, in addition
to the following asyncio database drivers:
- [asyncpg](https://magicstack.github.io/asyncpg) (Postgres)

The Cloud SQL Connector has a helper `create_async_connector` function that is
recommended for asyncio database connections. It returns a `Connector`
object that uses the current thread's running event loop. This is different
than `Connector()` which by default initializes a new event loop in a
background thread.

The `create_async_connector` allows all the same input arguments as the
[Connector](#configuring-the-connector) object.

Once a `Connector` object is returned by `create_async_connector` you can call
its `connect_async` method, just as you would the `connect` method:

#### Asyncpg Connection Pool

```python
import asyncpg
from google.cloud.sql.connector import Connector, create_async_connector

async def main():
    # initialize Connector object for connections to Cloud SQL
    connector = await create_async_connector()

    # creation function to generate asyncpg connections as the 'connect' arg
    async def getconn(instance_connection_name, **kwargs) -> asyncpg.Connection:
        return await connector.connect_async(
            instance_connection_name,
            "asyncpg",
            user="my-user",
            password="my-password",
            db="my-db",
            **kwargs, # ... additional asyncpg args
        )

    # initialize connection pool
    pool = await asyncpg.create_pool(
        "my-project:my-region:my-instance", connect=getconn
    )

    # acquire connection and query Cloud SQL database
    async with pool.acquire() as conn:
        res = await conn.fetch("SELECT NOW()")
    
    # close Connector
    await connector.close_async()
```

#### SQLAlchemy Async Engine

```python
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from google.cloud.sql.connector import Connector, create_async_connector


async def main():
    # initialize Connector object for connections to Cloud SQL
    connector = await create_async_connector()

    # The Cloud SQL Python Connector can be used along with SQLAlchemy using the
    # 'async_creator' argument to 'create_async_engine'
    pool = create_async_engine(
        "postgresql+asyncpg://",
        async_creator=lambda: connector.connect_async(
            "project:region:instance",  # Cloud SQL instance connection name
            "asyncpg",
            user="my-user",
            password="my-password",
            db="my-db-name"
            # ... additional database driver args
        ),
    )

    # example query
    async with pool.connect() as conn:
        await conn.execute(sqlalchemy.text("SELECT NOW()"))

    # close Connector
    await connector.close_async()

    # dispose of connection pool
    await pool.dispose()
```

For more details on additional database arguments with an `asyncpg.Connection`
, please visit the
[official documentation](https://magicstack.github.io/asyncpg/current/api/index.html).

### Async Context Manager

An alternative to using the `create_async_connector` function is initializing
a `Connector` as an async context manager, removing the need for explicit
calls to `connector.close_async()` to cleanup resources.

> [!NOTE]
>
> This alternative requires that the running event loop be
> passed in as the `loop` argument to `Connector()`.

#### Asyncpg Connection Pool

```python
import asyncpg
from google.cloud.sql.connector import Connector, create_async_connector

async def main():
    # initialize Connector object for connections to Cloud SQL
    loop = asyncio.get_running_loop()
    async with Connector(loop=loop) as connector:

        # creation function to generate asyncpg connections as the 'connect' arg
        async def getconn(instance_connection_name, **kwargs) -> asyncpg.Connection:
            return await connector.connect_async(
                instance_connection_name,
                "asyncpg",
                user="my-user",
                password="my-password",
                db="my-db",
                **kwargs, # ... additional asyncpg args
            )

        # create connection pool
        pool = await asyncpg.create_pool(
            "my-project:my-region:my-instance", connect=getconn
        )

        # acquire connection and query Cloud SQL database
        async with pool.acquire() as conn:
            res = await conn.fetch("SELECT NOW()")
```

#### SQLAlchemy Async Engine

```python
import asyncio
import asyncpg

import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from google.cloud.sql.connector import Connector


async def main():
    # initialize Connector object for connections to Cloud SQL
    loop = asyncio.get_running_loop()
    async with Connector(loop=loop) as connector:
        # The Cloud SQL Python Connector can be used along with SQLAlchemy using the
        # 'async_creator' argument to 'create_async_engine'
        pool = create_async_engine(
            "postgresql+asyncpg://",
            async_creator=lambda: connector.connect_async(
                "project:region:instance",  # Cloud SQL instance connection name
                "asyncpg",
                user="my-user",
                password="my-password",
                db="my-db-name"
                # ... additional database driver args
            ),
        )

        # example query
        async with pool.connect() as conn:
            await conn.execute(sqlalchemy.text("SELECT NOW()"))

        # dispose of connection pool
        await pool.dispose()
```

### Debug Logging

The Cloud SQL Python Connector uses the standard [Python logging module][python-logging]
for debug logging support.

Add the below code to your application to enable debug logging with the Cloud SQL
Python Connector:

```python
import logging

logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger(name="google.cloud.sql.connector")
logger.setLevel(logging.DEBUG)
```

For more details on configuring logging, please refer to the
[Python logging docs][configure-logging].

[python-logging]: https://docs.python.org/3/library/logging.html
[configure-logging]: https://docs.python.org/3/howto/logging.html#configuring-logging

## Support policy

### Major version lifecycle

This project uses [semantic versioning](https://semver.org/), and uses the
following lifecycle regarding support for a major version:

**Active** - Active versions get all new features and security fixes (that
wouldn’t otherwise introduce a breaking change). New major versions are
guaranteed to be "active" for a minimum of 1 year.
**Deprecated** - Deprecated versions continue to receive security and critical
bug fixes, but do not receive new features. Deprecated versions will be publicly
supported for 1 year.
**Unsupported** - Any major version that has been deprecated for >=1 year is
considered publicly unsupported.

### Supported Python Versions

We follow the [Python Version Support Policy][pyver] used by Google Cloud
Libraries for Python. Changes in supported Python versions will be
considered a minor change, and will be listed in the release notes.

[pyver]: https://cloud.google.com/python/docs/supported-python-versions

### Release cadence
This project aims for a minimum monthly release cadence. If no new
features or fixes have been added, a new PATCH version with the latest
dependencies is released.

### Contributing

We welcome outside contributions. Please see our
[Contributing Guide](CONTRIBUTING.md) for details on how best to contribute.



================================================
FILE: build.sh
================================================
#!/usr/bin/env bash

# Copyright 2025 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http=//www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Set SCRIPT_DIR to the current directory of this file.
SCRIPT_DIR=$(cd -P "$(dirname "$0")" >/dev/null 2>&1 && pwd)
SCRIPT_FILE="${SCRIPT_DIR}/$(basename "$0")"

##
## Local Development
##
## These functions should be used to run the local development process
##

if [[ ! -d venv ]] ; then
  echo "./venv not found. Setting up venv"
  python3 -m venv "$PWD/venv"
fi

source "$PWD/venv/bin/activate"

if which pip3 ; then
  PIP_CMD=pip3
elif which pip ; then
  PIP_CMD=pip
else
  echo "pip not found. Please add pip to your path."
  exit 1
fi
if ! which nox ; then
  python3 -m pip install nox
fi



## clean - Cleans the build output
function clean() {
  if [[ -d '.tools' ]] ; then
    rm -rf .tools
  fi
}

## build - Builds the project without running tests.
function build() {
  nox --sessions build
}

## test - Runs local unit tests.
function test() {
  nox --sessions unit --python=3.13
}

## e2e - Runs end-to-end integration tests.
function e2e() {
  if [[ ! -f .envrc ]] ; then
    write_e2e_env .envrc
  fi
  source .envrc
  nox --sessions system  --python=3.13
}

## fix - Fixes code format.
function fix() {
  nox --sessions format
}

## lint - runs the linters
function lint() {
  # Check the commit includes a go.mod that is fully
  # up to date.
  nox --sessions lint
}

## deps - updates project dependencies to latest
function deps() {
  if ! which pip-review ; then 
    python3 -m pip install pip-review
  fi
  pip-review --auto -r requirements.txt
  pip-review --auto -r requirements-test.txt
  echo "Dependencies updated successfully."
}

# write_e2e_env - Loads secrets from the gcloud project and writes
#     them to target/e2e.env to run e2e tests.
function write_e2e_env(){
  # All secrets used by the e2e tests in the form <env_name>=<secret_name>
  secret_vars=(
    MYSQL_CONNECTION_NAME=MYSQL_CONNECTION_NAME
    MYSQL_USER=MYSQL_USER
    MYSQL_USER_IAM=MYSQL_USER_IAM_GO
    MYSQL_PASS=MYSQL_PASS
    MYSQL_DB=MYSQL_DB
    MYSQL_MCP_CONNECTION_NAME=MYSQL_MCP_CONNECTION_NAME
    MYSQL_MCP_PASS=MYSQL_MCP_PASS
    POSTGRES_CONNECTION_NAME=POSTGRES_CONNECTION_NAME
    POSTGRES_USER=POSTGRES_USER
    POSTGRES_USER_IAM=POSTGRES_USER_IAM_GO
    POSTGRES_PASS=POSTGRES_PASS
    POSTGRES_DB=POSTGRES_DB
    POSTGRES_CAS_CONNECTION_NAME=POSTGRES_CAS_CONNECTION_NAME
    POSTGRES_CAS_PASS=POSTGRES_CAS_PASS
    POSTGRES_CUSTOMER_CAS_CONNECTION_NAME=POSTGRES_CUSTOMER_CAS_CONNECTION_NAME
    POSTGRES_CUSTOMER_CAS_PASS=POSTGRES_CUSTOMER_CAS_PASS
    POSTGRES_CUSTOMER_CAS_DOMAIN_NAME=POSTGRES_CUSTOMER_CAS_DOMAIN_NAME
    POSTGRES_CUSTOMER_CAS_INVALID_DOMAIN_NAME=POSTGRES_CUSTOMER_CAS_INVALID_DOMAIN_NAME
    POSTGRES_MCP_CONNECTION_NAME=POSTGRES_MCP_CONNECTION_NAME
    POSTGRES_MCP_PASS=POSTGRES_MCP_PASS
    SQLSERVER_CONNECTION_NAME=SQLSERVER_CONNECTION_NAME
    SQLSERVER_USER=SQLSERVER_USER
    SQLSERVER_PASS=SQLSERVER_PASS
    SQLSERVER_DB=SQLSERVER_DB
    QUOTA_PROJECT=QUOTA_PROJECT
  )

  if [[ -z "$TEST_PROJECT" ]] ; then
    echo "Set TEST_PROJECT environment variable to the project containing"
    echo "the e2e test suite secrets."
    exit 1
  fi

  echo "Getting test secrets from $TEST_PROJECT into $1"
  {
  for env_name in "${secret_vars[@]}" ; do
    env_var_name="${env_name%%=*}"
    secret_name="${env_name##*=}"
    set -x
    val=$(gcloud secrets versions access latest --project "$TEST_PROJECT" --secret="$secret_name")
    echo "export $env_var_name='$val'"
  done
  # Aliases for python e2e tests
  echo "export POSTGRES_CUSTOMER_CAS_PASS_VALID_DOMAIN_NAME=\"\$POSTGRES_CUSTOMER_CAS_DOMAIN_NAME\""
  echo "export POSTGRES_IAM_USER=\"\$POSTGRES_USER_IAM\""
  echo "export MYSQL_IAM_USER=\"\$MYSQL_USER_IAM\""
  } > "$1"

}

## help - prints the help details
##
function help() {
   # This will print the comments beginning with ## above each function
   # in this file.

   echo "build.sh <command> <arguments>"
   echo
   echo "Commands to assist with local development and CI builds."
   echo
   echo "Commands:"
   echo
   grep -e '^##' "$SCRIPT_FILE" | sed -e 's/##/ /'
}

set -euo pipefail

# Check CLI Arguments
if [[ "$#" -lt 1 ]] ; then
  help
  exit 1
fi

cd "$SCRIPT_DIR"

"$@"




================================================
FILE: CHANGELOG.md
================================================
# Changelog

## [1.20.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.19.0...v1.20.0) (2026-01-13)


### Features

* Use configured DNS name to lookup instance IP address ([#1363](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1363)) ([18eddc4](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/18eddc49c905f3caf02b9682c3594b5939b3f9f3)), closes [#1362](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1362)


### Dependencies

* Update project dependencies to latest ([#1369](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1369)) ([8cb6745](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/8cb674531a9dd23520824ac136e4dce7e8ce39b4))

## [1.19.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.18.5...v1.19.0) (2025-12-09)


### Features

* Add python 3.14 and remove python 3.9 support  ([#1339](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1339)) ([a2e8c4d](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/a2e8c4d30deeeb73475caf3367acadc58193228f))


### Documentation

* Add sample Cloud Run example application ([#1335](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1335)) ([adc25f6](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/adc25f683059a3f0fe3865d648374dce087cdaaa))
* Update documentation to describe how to use Advanced DR write endpoint. ([#1332](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1332)) ([2e1ed21](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/2e1ed211cad6dd63a76fa8c80df6c1d09d112778))

## [1.18.5](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.18.4...v1.18.5) (2025-10-09)


### Bug Fixes

* error on connect_async() event loop mismatch ([#1113](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1113)) ([3030b82](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/3030b824c899c56861832c0254df3c87585d3fcb))

## [1.18.4](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.18.3...v1.18.4) (2025-08-12)


### Bug Fixes

* bump dependencies to latest ([#1317](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1317)) ([6ebfac6](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/6ebfac67199b44ab517af7ab57027c64c784f1a1))

## [1.18.3](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.18.2...v1.18.3) (2025-07-11)


### Bug Fixes

* suppress lint check for _scopes property ([#1308](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1308)) ([821245c](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/821245c1911fb970e3409b3e249698937a8b7867))

## [1.18.2](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.18.1...v1.18.2) (2025-05-20)


### Bug Fixes

* bump dependencies to latest ([#1295](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1295)) ([dc907ef](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/dc907ef18905959b5116032f66fff78b9cddc13d))

## [1.18.1](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.18.0...v1.18.1) (2025-04-16)


### Bug Fixes

* bump dependencies to latest ([#1283](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1283)) ([f29b639](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/f29b6396f8eb4bed9070b3a67711fe6698ed0d51))


### Documentation

* use lambda over getconn func ([#1251](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1251)) ([6ecf894](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/6ecf894759bd44c729a5a53f34f3f161923d1e33))

## [1.18.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.17.0...v1.18.0) (2025-03-21)


### Features

* add domain name validation ([#1246](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1246)) ([15934bd](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/15934bd18ab426edd19af67be799876b52895a48))
* reset connection when the DNS record changes ([#1241](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1241)) ([1405f56](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/1405f564019f6a30a15535ed2e0d1dc108f38195))

## [1.17.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.16.0...v1.17.0) (2025-02-12)


### Features

* add support for `GOOGLE_CLOUD_QUOTA_PROJECT` env var ([#1231](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1231)) ([5232055](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/523205583b89a7260cf427bbce90a7782abf443c))


### Bug Fixes

* update create_async_connector args ([#1232](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1232)) ([b4f8f52](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/b4f8f520b00b43d3c04fc27e297afaab4100d499))

## [1.16.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.15.0...v1.16.0) (2025-01-13)


### Features

* add support for `GOOGLE_CLOUD_UNIVERSE_DOMAIN` env var ([#1221](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1221)) ([ac77932](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/ac77932e7f6c592c73abc75a153b61571ba6c7ff))

## [1.15.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.14.0...v1.15.0) (2024-12-10)


### Features

* add support for DNS names with Connector ([#1204](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1204)) ([1a8f274](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/1a8f2743c661806528c54110fd2a08384398816c))
* improve aiohttp client error messages ([#1201](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1201)) ([11f9fe9](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/11f9fe93617cd9a161c69d527d3e7592fcbe56af))

## [1.14.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.13.0...v1.14.0) (2024-11-20)


### Features

* support native asyncpg connection pools ([#1182](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1182)) ([eb95a9d](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/eb95a9da35553387408e425721449660cc83196d))

## [1.13.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.12.1...v1.13.0) (2024-10-22)


### Features

* add support for Python 3.13 ([#1177](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1177)) ([6e6a1c8](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/6e6a1c8532b044729f54cdd6508d1afa5c7df749))
* drop support for Python 3.8 ([#1176](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1176)) ([10c9172](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/10c9172c93bfc8b2f3a2ab0a990f5a5369961199))
* improve key for connector cache ([#1172](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1172)) ([066c14e](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/066c14efb92af292cd795fb920d7fe5f736a9b0d))


### Bug Fixes

* remove `ConnectorLoopError` from connector.connect ([#1170](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1170)) ([a348659](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/a3486591d6f4f911b964fd2254ccf9a5ff80da20))

## [1.12.1](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.12.0...v1.12.1) (2024-09-17)


### Bug Fixes

* set PSC ip type based on `pscEnabled` ([#1158](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1158)) ([53e40c7](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/53e40c7dbec8f27e2e3e6e344bf87e08cf15c3e9))

## [1.12.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.11.0...v1.12.0) (2024-08-13)


### Features

* use non-blocking disk read/writes ([#1142](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1142)) ([d2fd465](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/d2fd46523fae041ec8b4e907e4d0eeb204f0aa8f))


### Dependencies

* update python non-major dependencies ([#1149](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1149)) ([2e27c05](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/2e27c05acb2d579127b892a7ed5860a9404c9f53))

## [1.11.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.10.0...v1.11.0) (2024-07-10)


### Features

* invalidate cache on bad connection info and IP lookup ([#1118](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1118)) ([672dc4e](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/672dc4e8b853e5b2ac1b44da889466b6693381da))


### Bug Fixes

* let DNS resolve outside connector ([#1120](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1120)) ([d321f79](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/d321f79dffebb7c630ba4f4c14dd36aa1a532798))
* retry 50x errors with exponential backoff ([#1125](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1125)) ([2da9128](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/2da9128cb1e46e713fe79094f1903f79e5a4cb64))

## [1.10.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.9.2...v1.10.0) (2024-06-11)


### Features

* add support for lazy refresh strategy ([#1093](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1093)) ([b9526bb](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/b9526bbd31304754c9099be17b5178f9ba43b92c))
* validate driver with database engine ([#1108](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1108)) ([a7c7861](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/a7c7861884fd95b28ec52d22cd6824f4d86db392))

## [1.9.2](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.9.1...v1.9.2) (2024-05-14)


### Dependencies

* update dependency cryptography to v42.0.7 ([#1076](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1076)) ([a4aec7e](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/a4aec7ee406cd3e4480833479d394d67c80e9352))

## [1.9.1](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.9.0...v1.9.1) (2024-04-17)


### Bug Fixes

* add minimum version for google-auth dep ([#1065](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1065)) ([b13d172](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/b13d1723f721a4a19751d4c2550f92656fff0ce4))


### Dependencies

* update dependency aiohttp to v3.9.5 ([#1063](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1063)) ([bd6c323](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/bd6c3239dad0c95ab5e5648a1950b241c4e1ed5b))

## [1.9.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.8.0...v1.9.0) (2024-04-16)


### Features

* add universe domain support to Connector (TPC) ([#1045](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1045)) ([b1e9dee](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/b1e9deee216c57e6831162f6aded79511c5e38e3))


### Dependencies

* update dependency aiohttp to v3.9.4 ([#1060](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1060)) ([78b3671](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/78b36715bd2d3a1ca4c4f72295c36b95e360abf1))
* Update dependency google-auth to v2.29.0 ([#1043](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1043)) ([2ac2fd1](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/2ac2fd1ab99ee1c0d3a12cd9da7f6820eb0237cc))
* Update dependency pg8000 to v1.31.1 ([#1053](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1053)) ([eaa371d](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/eaa371d95509f97b8951d80046a5a273bece489a))

## [1.8.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.7.0...v1.8.0) (2024-03-12)


### Features

* support `ip_type` as str ([#1029](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1029)) ([e087704](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/e08770422f05c96b1349d1505aab511b15ed1885))


### Bug Fixes

* update create_async_connector args ([#1016](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1016)) ([c3f51a2](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/c3f51a24f0fa055fc3459c9170557c6ff15424f5))


### Dependencies

* Update dependency cryptography to v42.0.5 ([#1015](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1015)) ([b47dfef](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/b47dfef36e11edd17def5a3b61714256d534ac62))
* Update dependency google-auth to v2.28.2 ([#1034](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1034)) ([bf20bbc](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/bf20bbc3694066e6905b77771ca044421fc3c92f))
* Update dependency pg8000 to v1.30.5 ([#1026](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/1026)) ([e66f4e3](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/e66f4e36235bf09d2a7de20f1a4c1e7158f97a40))

## [1.7.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.6.0...v1.7.0) (2024-02-13)


### Features

* add support for a custom user agent ([#986](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/986)) ([82da410](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/82da41050992de2eddfeae5a81a434192e88d134))
* add support for Python 3.12 ([#905](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/905)) ([7501d17](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/7501d17ee05d41c1e009e4ca44ad7f8edaf18001))


### Dependencies

* Update dependency aiohttp to v3.9.3 ([#993](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/993)) ([168b1f4](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/168b1f43b2d0e4b376d8858aa32bc54e26d3e069))
* Update dependency cryptography to v42.0.2 ([#994](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/994)) ([6b762df](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/6b762df593ffbdc81a7ae98386230af9dc570147))
* Update dependency google-auth to v2.27.0 ([#980](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/980)) ([def011a](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/def011a0f7eee9d6288b441de5df416f429d227f))

## [1.6.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.5.0...v1.6.0) (2024-01-17)


### Features

* add support for domain-scoped projects ([#937](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/937)) ([3d1f36e](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/3d1f36e176d1689380d71fc56f111dbb8de34dcb))


### Dependencies

* Update dependency google-auth to v2.26.2 ([#964](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/964)) ([43d7ad6](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/43d7ad6d7b57454256b933580d51113cc22a2206))
* update dependency pg8000 to v1.30.4 ([#962](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/962)) ([8012c8f](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/8012c8f7d32cd59f851638d7167067f2804125f6))

## [1.5.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.4.3...v1.5.0) (2023-12-12)


### Features

* introduce compatibility with native namespace packages ([#906](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/906)) ([083da11](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/083da1193a838be9f16653f2d4efb4ad8bcfa73a))


### Dependencies

* Update dependency aiohttp to v3.9.1 ([#916](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/916)) ([b6f9485](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/b6f9485d644b6ff3203ebed175ec8a3754bf319b))
* Update dependency cryptography to v41.0.7 ([#917](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/917)) ([43e22e1](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/43e22e1e03c5066c328729920b5f8a8bb6480d07))
* Update dependency google-auth to v2.25.2 ([#929](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/929)) ([24439a9](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/24439a991df189ebe252415f369ff4ce93a42d58))

## [1.4.3](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.4.2...v1.4.3) (2023-11-15)


### Bug Fixes

* use IAM login creds in expiration logic ([#898](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/898)) ([7f8a3a4](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/7f8a3a46ce754de7ffcf8adb58a075cb43c987f4))
* Use utcnow() in refresh calculation ([#890](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/890)) ([469ed04](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/469ed044c45947f8153133a10753eaf078b133dd))


### Dependencies

* Update dependency asyncpg to v0.29.0 ([#887](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/887)) ([9c566ea](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/9c566eaa3ed08874c6653d0ce35f92c3ab99888c))
* Update dependency cryptography to v41.0.5 ([#874](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/874)) ([9f9dd0d](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/9f9dd0dc5ac43fa9402ccb7477b8972a74fa3703))
* Update dependency pg8000 to v1.30.3 ([#882](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/882)) ([13e9d31](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/13e9d3132290989a788157f1d91b83103ccb3764))

## [1.4.2](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.4.1...v1.4.2) (2023-10-09)


### Dependencies

* Update actions/checkout action to v3.6.0 ([#829](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/829)) ([f6c1fea](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/f6c1fea75527f28c4b150720b7367001767a9f6f))
* Update actions/checkout action to v4 ([#837](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/837)) ([0f570a6](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/0f570a66e2416cacb987b62a84b1f9547ae71e7a))
* Update actions/checkout action to v4.1.0 ([#855](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/855)) ([0566b15](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/0566b1507638f909ef3081287c8531479787c3e1))
* Update actions/setup-python action to v4.7.1 ([#858](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/858)) ([1085306](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/108530617916fa1ec8462cc6c6fcceb77fc8c73f))
* Update actions/upload-artifact action to v3.1.3 ([#838](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/838)) ([3238c96](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/3238c96735fed1b9f124c885923f40cd1208300e))
* Update dependencies for github ([#863](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/863)) ([cad15e2](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/cad15e2f5afe29c8248d61f6bf18e81ae43d1395))
* Update dependency aiohttp to v3.8.6 ([#864](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/864)) ([0d4cf17](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/0d4cf175dfd8b2ec4716c048283fb713f20d211a))
* Update dependency black to v23.9.1 ([#840](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/840)) ([89e90fd](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/89e90fdc8879e60c22e734cac338d5e5a857dbb6))
* Update dependency cryptography to v41.0.4 ([#851](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/851)) ([c700e9b](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/c700e9b984e6660c3058d707808158e0225fe506))
* Update dependency pg8000 to v1.30.2 ([#848](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/848)) ([62079f7](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/62079f74cc742ec9882db518a58ae7a1f65822d0))
* Update dependency pytest to v7.4.2 ([#835](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/835)) ([3d05557](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/3d05557e66e8552f50f0e9199c3c96fd130b8e0d))
* Update dependency SQLAlchemy to v2.0.21 ([#849](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/849)) ([f5e9c2f](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/f5e9c2f6ba39a4fed68874b0eb97490676534a9c))
* Update dependency types-mock to v5.1.0.2 ([#836](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/836)) ([9a57a41](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/9a57a41a76c4c7d2fcf94bfbbb54e5575802dc57))
* Update github/codeql-action action to v2.21.5 ([#832](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/832)) ([6c7c322](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/6c7c3229190f46d5e30e48ffa17043029b234124))
* Update github/codeql-action action to v2.21.6 ([#841](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/841)) ([71b9347](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/71b9347e265398ae2c3a0db4c1a7595ac199b9bf))
* Update github/codeql-action action to v2.21.7 ([#847](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/847)) ([53a19ad](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/53a19adc5e73a9d0d7ce949e21cb794d67507345))
* Update github/codeql-action action to v2.21.8 ([#850](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/850)) ([2bd4f3a](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/2bd4f3ae98168f3d194195807e7d9863fc426bc6))
* Update github/codeql-action action to v2.21.9 ([#857](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/857)) ([28f07ae](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/28f07ae5c3125a576933dd44ab08a1afbcf71e92))

## [1.4.1](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.4.0...v1.4.1) (2023-08-18)


### Bug Fixes

* re-use existing connections on force refresh ([#828](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/828)) ([f98c1b6](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/f98c1b6e29a2328a1911fda10ac5ce463ec70197))

## [1.4.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.3.0...v1.4.0) (2023-08-08)


### Features

* configure pg8000 connection with SSLSocket ([#789](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/789)) ([a6433b9](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/a6433b98323f91378cdb285f9c732dd45a7376a3))


### Dependencies

* Update dependency aiohttp to v3.8.5 ([#801](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/801)) ([7ed23d0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/7ed23d00fabeb6cda498c64bb994fe7e6a0f4a2e))
* Update dependency cryptography to v41.0.3 [SECURITY] ([#810](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/810)) ([d11b3a5](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/d11b3a58090b923c27539bae20051f957f34fcde))
* Update dependency pg8000 to v1.30.1 ([#808](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/808)) ([c4cd9bc](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/c4cd9bc5bb64bb170eba7d30c0f303e8b839beef))
* Update dependency python-tds to v1.13.0 ([#818](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/818)) ([65cccf3](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/65cccf361057cff1f4b676474b7e1798f66d9408))

## [1.3.0](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/compare/v1.2.4...v1.3.0) (2023-07-11)


### Features

* add support for PSC connections ([#766](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/766)) ([c238fe3](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/c238fe34e7e18a82c53112c56c141fdf38649523))
* remove support for Python 3.7 ([#761](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/761)) ([5b8a172](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/commit/5b8a172e23e322ef6b425740cab4bed0a308c171))


### Documentation

* update getconn in README samples ([#773](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector/issues/773)) ([179c06e](https://github.com/GoogleCloudPlatform/cloud-sql-python-conne

[... Content truncated due to length ...]

</details>


## YouTube Video Transcripts

_No YouTube video transcripts found._


## Additional Sources Scraped

<details>
<summary>https://www.postgresql.org/docs/current/datatype-json.html</summary>



</details>

<details>
<summary>https://www.sqlalchemy.org/</summary>



</details>

<details>
<summary>https://alembic.sqlalchemy.org/</summary>

Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

</details>

<details>
<summary>https://cloud.google.com/sql/docs/postgres</summary>

The provided markdown content is documentation for Google Cloud SQL for PostgreSQL. While Cloud SQL is a topic covered in the `article_guidelines`, the `markdown_content` is an external reference page, not the core lesson content that the guidelines describe. The task is to keep "only the core textual content (and code content if there are code sections) that is pertinent to the article guidelines provided below." Since the provided markdown is not the lesson itself but rather a general documentation page, it is entirely irrelevant to the specific narrative flow, sections, and content points outlined in the `article_guidelines` for Lesson 33.

Therefore, the cleaned markdown content is empty.

</details>

<details>
<summary>https://cloud.google.com/run/docs/configuring/services/containers</summary>

The provided markdown content is a detailed guide on configuring containers for Google Cloud Run services. While the article guidelines mention Cloud Run and its ephemeral nature as a justification for database migration, the specific content of this markdown (configuring container ports, entrypoints, arguments, and start order) is not the core textual content pertinent to the lesson's objective, which is about database and file handling.

The article guidelines indicate that the lesson will *mention* ephemeral containers in Cloud Run as a *reason* for needing a database, potentially citing Cloud Run documentation. However, the provided content is an extensive operational guide rather than a discussion of the underlying ephemeral storage problem.

Therefore, the entire content of the provided markdown is considered irrelevant to the core lesson's narrative and specific section requirements, as it goes far beyond a simple citation or brief explanation of ephemeral storage.

</details>

<details>
<summary>https://www.sqlite.org/whentouse.html</summary>

SQLite is not directly comparable to client/server SQL database engines such as MySQL, Oracle, PostgreSQL, or SQL Server since SQLite is trying to solve a different problem.

Client/server SQL database engines strive to implement a shared repository of enterprise data. They emphasize scalability, concurrency, centralization, and control.
SQLite strives to provide local data storage for individual applications and devices. SQLite emphasizes economy, efficiency, reliability, independence, and simplicity.

SQLite does not compete with client/server databases.
SQLite competes with `fopen()`.

# 1. Situations Where SQLite Works Well

-   **Embedded devices and the internet of things**
    Because an SQLite database requires no administration, it works well in devices that must operate without expert human support. SQLite is a good fit for use in cellphones, set-top boxes, televisions, game consoles, cameras, watches, kitchen appliances, thermostats, automobiles, machine tools, airplanes, remote sensors, drones, medical devices, and robots: the "internet of things".

    Client/server database engines are designed to live inside a lovingly-attended datacenter at the core of the network. SQLite works there too, but SQLite also thrives at the edge of the network, fending for itself while providing fast and reliable data services to applications that would otherwise have dodgy connectivity.

-   **Application file format**

    SQLite is often used as the on-disk file format for desktop applications such as version control systems, financial analysis tools, media cataloging and editing suites, CAD packages, record keeping programs, and so forth. The traditional File/Open operation calls sqlite3\_open() to attach to the database file. Updates happen automatically as application content is revised so the File/Save menu option becomes superfluous. The File/Save\_As menu option can be implemented using the [backup API](https://www.sqlite.org/backup.html).

    There are many benefits to this approach, including improved performance, reduced cost and complexity, and improved reliability. See technical notes ["aff\_short.html"](https://www.sqlite.org/aff_short.html) and ["appfileformat.html"](https://www.sqlite.org/appfileformat.html) and ["fasterthanfs.html"](https://www.sqlite.org/fasterthanfs.html) for more information. This use case is closely related to the [data transfer format](https://www.sqlite.org/whentouse.html#wireproto) and [data container](https://www.sqlite.org/whentouse.html#container) use cases below.

-   **Websites**

    SQLite works great as the database engine for most low to medium traffic websites (which is to say, most websites). The amount of web traffic that SQLite can handle depends on how heavily the website uses its database. Generally speaking, any site that gets fewer than 100K hits/day should work fine with SQLite. The 100K hits/day figure is a conservative estimate, not a hard upper bound. SQLite has been demonstrated to work with 10 times that amount of traffic.

    The SQLite website ( [https://sqlite.org/](https://sqlite.org/)) uses SQLite itself, of course, and as of this writing (2015) it handles about 400K to 500K HTTP requests per day, about 15-20% of which are dynamic pages touching the database. Dynamic content uses [about 200 SQL statements per webpage](https://www.sqlite.org/np1queryprob.html). This setup runs on a single VM that shares a physical server with 23 others and yet still keeps the load average below 0.1 most of the time.

    See also: [Hacker News discussion from 2022-12-13](https://news.ycombinator.com/item?id=33975635).

-   **Data analysis**

    People who understand SQL can employ the [sqlite3 command-line shell](https://www.sqlite.org/cli.html) (or various third-party SQLite access programs) to analyze large datasets. Raw data can be imported from CSV files, then that data can be sliced and diced to generate a myriad of summary reports. More complex analysis can be done using simple scripts written in Tcl or Python (both of which come with SQLite built-in) or in R or other languages using readily available adaptors. Possible uses include website log analysis, sports statistics analysis, compilation of programming metrics, and analysis of experimental results. Many bioinformatics researchers use SQLite in this way.

    The same thing can be done with an enterprise client/server database, of course. The advantage of SQLite is that it is easier to install and use and the resulting database is a single file that can be written to a USB memory stick or emailed to a colleague.

-   **Cache for enterprise data**

    Many applications use SQLite as a cache of relevant content from an enterprise RDBMS. This reduces latency, since most queries now occur against the local cache and avoid a network round-trip. It also reduces the load on the network and on the central database server. And in many cases, it means that the client-side application can continue operating during network outages.

-   **Server-side database**

    Systems designers report success using SQLite as a data store on server applications running in the datacenter, or in other words, using SQLite as the underlying storage engine for an application-specific database server.

    With this pattern, the overall system is still client/server: clients send requests to the server and get back replies over the network. But instead of sending generic SQL and getting back raw table content, the client requests and server responses are high-level and application-specific. The server translates requests into multiple SQL queries, gathers the results, does post-processing, filtering, and analysis, then constructs a high-level reply containing only the essential information.

    Developers report that SQLite is often faster than a client/server SQL database engine in this scenario. Database requests are serialized by the server, so concurrency is not an issue. Concurrency is also improved by "database sharding": using separate database files for different subdomains. For example, the server might have a separate SQLite database for each user, so that the server can handle hundreds or thousands of simultaneous connections, but each SQLite database is only used by one connection.

-   **Data transfer format**

    Because an SQLite database is a single compact file in a [well-defined cross-platform format](https://www.sqlite.org/fileformat2.html), it is often used as a container for transferring content from one system to another. The sender gathers content into an SQLite database file, transfers that one file to the receiver, then the receiver uses SQL to extract the content as needed.

    An SQLite database facilitates data transfer between systems even when the endpoints have different word sizes and/or byte orders. The data can be a complex mix of large binary blobs, text, and small numeric or boolean values. The data format can be easily extended by adding new tables and/or columns, without breaking legacy receivers. The SQL query language means that receivers are not required to parse the entire transfer all at once, but can instead query the received content as needed. The data format is "transparent" in the sense that it is easily decoded for human viewing using a variety of universally available, open-source tools, from multiple vendors.

-   **File archive and/or data container**

    The [SQLite Archive](https://www.sqlite.org/sqlar.html) idea shows how SQLite can be used as a substitute for ZIP archives or Tarballs. An archive of files stored in SQLite is only very slightly larger, and in some cases actually smaller, than the equivalent ZIP archive. And an SQLite archive features incremental and atomic updating and the ability to store much richer metadata.

    [Fossil](https://www.fossil-scm.org/) version 2.5 and later offers [SQLite Archive files](https://www.sqlite.org/sqlar.html) as a download format, in addition to traditional tarball and ZIP archive. The [sqlite3.exe command-line shell](https://www.sqlite.org/cli.html) version 3.22.0 and later will create, list, or unpack an SQL archive using the [.archive command](https://www.sqlite.org/cli.html#sqlar).

    SQLite is a good solution for any situation that requires bundling diverse content into a self-contained and self-describing package for shipment across a network. Content is encoded in a [well-defined, cross-platform, and stable file format](https://www.sqlite.org/fileformat2.html). The encoding is efficient, and receivers can extract small subsets of the content without having to read and parse the entire file.

    SQL archives are useful as the distribution format for software or content updates that are broadcast to many clients. Variations on this idea are used, for example, to transmit TV programming guides to set-top boxes and to send over-the-air updates to vehicle navigation systems.

-   **Replacement for _ad hoc_ disk files**

    Many programs use [fopen()](http://man.he.net/man3/fopen), [fread()](http://man.he.net/man3/fread), and [fwrite()](http://man.he.net/man3/fwrite) to create and manage files of data in home-grown formats. SQLite works particularly well as a replacement for these _ad hoc_ data files. Contrary to intuition, SQLite can be [faster than the filesystem](https://www.sqlite.org/fasterthanfs.html) for reading and writing content to disk.

-   **Internal or temporary databases**

    For programs that have a lot of data that must be sifted and sorted in diverse ways, it is often easier and quicker to load the data into an in-memory SQLite database and use queries with joins and ORDER BY clauses to extract the data in the form and order needed rather than to try to code the same operations manually. Using an SQL database internally in this way also gives the program greater flexibility since new columns and indices can be added without having to recode every query.

-   **Stand-in for an enterprise database during demos or testing**

    Client applications typically use a generic database interface that allows connections to various SQL database engines. It makes good sense to include SQLite in the mix of supported databases and to statically link the SQLite engine in with the client. That way the client program can be used standalone with an SQLite data file for testing or for demonstrations.

-   **Education and Training**

    Because it is simple to setup and use (installation is trivial: just copy the **sqlite3** or **sqlite3.exe** executable to the target machine and run it) SQLite makes a good database engine for use in teaching SQL. Students can easily create as many databases as they like and can email databases to the instructor for comments or grading. For more advanced students who are interested in studying how an RDBMS is implemented, the modular and well-commented and documented SQLite code can serve as a good basis.

-   **Experimental SQL language extensions**

    The simple, modular design of SQLite makes it a good platform for prototyping new, experimental database language features or ideas.

# 2. Situations Where A Client/Server RDBMS May Work Better

-   **Client/Server Applications**

    If there are many client programs sending SQL to the same database over a network, then use a client/server database engine instead of SQLite. SQLite will work over a network filesystem, but because of the latency associated with most network filesystems, performance will not be great. Also, file locking logic is buggy in many network filesystem implementations (on both Unix and Windows). If file locking does not work correctly, two or more clients might try to modify the same part of the same database at the same time, resulting in corruption. Because this problem results from bugs in the underlying filesystem implementation, there is nothing SQLite can do to prevent it.

    A good rule of thumb is to avoid using SQLite in situations where the same database will be accessed directly (without an intervening application server) and simultaneously from many computers over a network.

-   **High-volume Websites**

    SQLite will normally work fine as the database backend to a website. But if the website is write-intensive or is so busy that it requires multiple servers, then consider using an enterprise-class client/server database engine instead of SQLite.

-   **Very large datasets**

    An SQLite database is limited in size to 281 terabytes (2^48 bytes, 256 tibibytes). And even if it could handle larger databases, SQLite stores the entire database in a single disk file and many filesystems limit the maximum size of files to something less than this. So if you are contemplating databases of this magnitude, you would do well to consider using a client/server database engine that spreads its content across multiple disk files, and perhaps across multiple volumes.

-   **High Concurrency**

    SQLite supports an unlimited number of simultaneous readers, but it will only allow one writer at any instant in time. For many situations, this is not a problem. Writers queue up. Each application does its database work quickly and moves on, and no lock lasts for more than a few dozen milliseconds. But there are some applications that require more concurrency, and those applications may need to seek a different solution.

# 3. Checklist For Choosing The Right Database Engine

1.  **Is the data separated from the application by a network?**
    **→ choose client/server**

    Relational database engines act as bandwidth-reducing data filters. So it is best to keep the database engine and the data on the same physical device so that the high-bandwidth engine-to-disk link does not have to traverse the network, only the lower-bandwidth application-to-engine link.

    But SQLite is built into the application. So if the data is on a separate device from the application, it is required that the higher bandwidth engine-to-disk link be across the network. This works, but it is suboptimal. Hence, it is usually better to select a client/server database engine when the data is on a separate device from the application.

    _Nota Bene:_
    In this rule, "application" means the code that issues SQL statements. If the "application" is an [application server](https://www.sqlite.org/whentouse.html#serversidedb) and if the content resides on the same physical machine as the application server, then SQLite might still be appropriate even though the end user is another network hop away.

2.  **Many concurrent writers? → choose client/server**

    If many threads and/or processes need to write to the database at the same instant (and they cannot queue up and take turns) then it is best to select a database engine that supports that capability, which always means a client/server database engine.

    SQLite only supports one writer at a time per database file. But in most cases, a write transaction only takes milliseconds and so multiple writers can simply take turns. SQLite will handle more write concurrency than many people suspect. Nevertheless, client/server database systems, because they have a long-running server process at hand to coordinate access, can usually handle far more write concurrency than SQLite ever will.

3.  **Big data? → choose client/server**

    If your data will grow to a size that you are uncomfortable or unable to fit into a single disk file, then you should select a solution other than SQLite. SQLite supports databases up to 281 terabytes in size, assuming you can find a disk drive and filesystem that will support 281-terabyte files. Even so, when the size of the content looks like it might creep into the terabyte range, it would be good to consider a centralized client/server database.

4.  **Otherwise → choose SQLite!**

    For device-local storage with low writer concurrency and less than a terabyte of content, SQLite is almost always a better solution. SQLite is fast and reliable and it requires no configuration or maintenance. It keeps things simple. SQLite "just works".

</details>

<details>
<summary>https://docs.docker.com/compose/how-tos/networking/</summary>

```markdown
# Networking in Compose

By default Compose sets up a single
network for your app. Each
container for a service joins the default network and is both reachable by
other containers on that network, and discoverable by the service's name.

> Note
>
> Your app's network is given a name based on the "project name",
> which is based on the name of the directory it lives in. You can override the
> project name with either the
> `--project-name` flag
> or the `COMPOSE_PROJECT_NAME` environment variable.

For example, suppose your app is in a directory called `myapp`, and your `compose.yaml` looks like this:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres:18
    ports:
      - "8001:5432"
```

When you run `docker compose up`, the following happens:

1. A network called `myapp_default` is created.
2. A container is created using `web`'s configuration. It joins the network
`myapp_default` under the name `web`.
3. A container is created using `db`'s configuration. It joins the network
`myapp_default` under the name `db`.

Each container can now look up the service name `web` or `db` and
get back the appropriate container's IP address. For example, `web`'s
application code could connect to the URL `postgres://db:5432` and start
using the Postgres database.

It is important to note the distinction between `HOST_PORT` and `CONTAINER_PORT`.
In the above example, for `db`, the `HOST_PORT` is `8001` and the container port is
`5432` (postgres default). Networked service-to-service
communication uses the `CONTAINER_PORT`. When `HOST_PORT` is defined,
the service is accessible outside the swarm as well.

Within the `web` container, your connection string to `db` would look like
`postgres://db:5432`, and from the host machine, the connection string would
look like `postgres://{DOCKER_IP}:8001` for example `postgres://localhost:8001` if your container is running locally.

## Update containers on the network

If you make a configuration change to a service and run `docker compose up` to update it, the old container is removed and the new one joins the network under a different IP address but the same name. Running containers can look up that name and connect to the new address, but the old address stops working.

If any containers have connections open to the old container, they are closed. It is a container's responsibility to detect this condition, look up the name again and reconnect.

> Tip
>
> Reference containers by name, not IP, whenever possible. Otherwise you’ll need to constantly update the IP address you use.

## Link containers

Links allow you to define extra aliases by which a service is reachable from another service. They are not required to enable services to communicate. By default, any service can reach any other service at that service's name. In the following example, `db` is reachable from `web` at the hostnames `db` and `database`:

```yaml
services:
  web:
    build: .
    links:
      - "db:database"
  db:
    image: postgres:18
```

See the
links reference for more information.

## Multi-host networking

When deploying a Compose application on a Docker Engine with
Swarm mode enabled,
you can make use of the built-in `overlay` driver to enable multi-host communication.

Overlay networks are always created as `attachable`. You can optionally set the
`attachable` property to `false`.

Consult the
Swarm mode section to see how to set up
a Swarm cluster, and the
overlay network driver documentation
to learn about multi-host overlay networks.

## Specify custom networks

Instead of just using the default app network, you can specify your own networks with the top-level `networks` key. This lets you create more complex topologies and specify
custom network drivers and options. You can also use it to connect services to externally-created networks which aren't managed by Compose.

Each service can specify what networks to connect to with the service-level `networks` key, which is a list of names referencing entries under the top-level `networks` key.

The following example shows a Compose file which defines two custom networks. The `proxy` service is isolated from the `db` service, because they do not share a network in common. Only `app` can talk to both.

```yaml
services:
  proxy:
    build: ./proxy
    networks:
      - frontend
  app:
    build: ./app
    networks:
      - frontend
      - backend
  db:
    image: postgres:18
    networks:
      - backend

networks:
  frontend:
    # Specify driver options
    driver: bridge
    driver_opts:
      com.docker.network.bridge.host_binding_ipv4: "127.0.0.1"
  backend:
    # Use a custom driver
    driver: custom-driver
```

Networks can be configured with static IP addresses by setting the
ipv4\_address and/or ipv6\_address for each attached network.

Networks can also be given a
custom name:

```yaml
services:
  # ...
networks:
  frontend:
    name: custom_frontend
    driver: custom-driver-1
```

## Configure the default network

Instead of, or as well as, specifying your own networks, you can also change the settings of the app-wide default network by defining an entry under `networks` named `default`:

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres:18

networks:
  default:
    # Use a custom driver
    driver: custom-driver-1
```

## Use an existing network

If you've manually created a bridge network outside of Compose using the `docker network create` command, you can connect your Compose services to it by marking the network as `external`.

If you want your containers to join a pre-existing network, use the
`external` option

```yaml
services:
  # ...
networks:
  network1:
    name: my-pre-existing-network
    external: true
```

Instead of attempting to create a network called `[projectname]_default`, Compose looks for a network called `my-pre-existing-network` and connects your app's containers to it.

## Further reference information

For full details of the network configuration options available, see the following references:

- Top-level `networks` element
- Service-level `networks` attribute
```

</details>

<details>
<summary>https://docs.docker.com/engine/storage/volumes/</summary>



</details>

<details>
<summary>https://docs.docker.com/reference/compose-file/services/#healthcheck</summary>

The provided markdown content is a general reference document on defining services in Docker Compose, including detailed explanations of numerous attributes. While Docker Compose is mentioned in the article guidelines for setting up local development with PostgreSQL, the content here does not pertain to the specific `docker-compose.yml` setup or the core textual content outlined for the lesson on "Database and File Handling Guidelines."

The `article_guidelines` specify that the content for each section should be drawn from `source.md` (e.g., "Source reference: Use the opening paragraphs and introductory content from `source.md` (lines 1-6)"). The provided `markdown_content` does not appear to be this `source.md` and instead is a broad reference.

Therefore, the entire provided markdown content is considered irrelevant to the specific article guidelines.

</details>

<details>
<summary>https://magicstack.github.io/asyncpg/current/</summary>

**asyncpg** is a database interface library designed specifically for PostgreSQL and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL server binary protocol for use with Python’s `asyncio` framework.

**asyncpg** requires Python 3.9 or later and is supported for PostgreSQL versions 9.5 to 18.

</details>

<details>
<summary>https://modelcontextprotocol.io/specification</summary>



</details>

<details>
<summary>https://cloud.google.com/sql/docs/postgres/connect-run</summary>

```markdown
# Connect from Cloud Run

This page contains information and examples for connecting to a
Cloud SQL instance from a service running in Cloud Run.

**For step-by-step instructions on running a Cloud Run sample web**
**application connected to Cloud SQL,** see the
[quickstart for connecting
from Cloud Run](https://docs.cloud.google.com/sql/docs/postgres/connect-instance-cloud-run).

Cloud SQL is a fully-managed database service that helps you set up,
maintain, manage, and administer your relational databases in the cloud.

[Cloud Run](https://docs.cloud.com/run/docs/overview/what-is-cloud-run) is
a managed compute platform that lets you run containers directly on top of
Google Cloud infrastructure.

## Set up a Cloud SQL instance

1. Enable the Cloud SQL Admin API in the Google Cloud project that you are connecting from, if you
    haven't already done so:

**Roles required to enable APIs**

To enable APIs, you need the Service Usage Admin IAM
role (`roles/serviceusage.serviceUsageAdmin`), which
contains the `serviceusage.services.enable` permission. [Learn how to grant
roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

[Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin&redirect=https://console.cloud.google.com)

2. [Create a Cloud SQL
    for PostgreSQL instance](https://docs.cloud.google.com/sql/docs/postgres/create-instance). We recommend that you choose a Cloud SQL [instance location](https://docs.cloud.google.com/sql/docs/postgres/locations) in the same region as your Cloud Run service for better latency, to avoid some networking costs, and to reduce
    cross region failure risks.

By default, Cloud SQL assigns a public IP address to a new
instance.

You also have the option to assign a private IP address. For more
information about the connectivity options for both, see the
[Connecting Overview](https://docs.cloud.google.com/sql/docs/postgres/connect-overview)
page.

3. When you create the instance, you can choose the [server certificate (CA) hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies) for the instance and then configure the hierarchy
    as the `serverCaMode` for the instance. You must select the
    per-instance CA option (`GOOGLE_MANAGED_INTERNAL_CA`) as the server CA mode
    for instances that you want to connect to from
    web applications.

## Configure Cloud Run

The steps to configure Cloud Run depend on the type of IP address that
you assigned to your Cloud SQL instance. If you route all egress traffic
through Direct VPC egress or a Serverless VPC Access connector, use a
private IP address.
[Compare the two network egress methods](https://docs.cloud.google.com/run/docs/configuring/vpc-connect-comparison).

Public IP (default)

- Make sure that the instance has a public IP address. You can
verify this on the **Overview** page for your instance in the
[Google Cloud console](https://console.cloud.google.com/sql).
If you need to add one, see the
[Configuring public IP page](https://docs.cloud.google.com/sql/docs/postgres/configure-ip)
for instructions.
- Get the INSTANCE\_CONNECTION\_NAME for your instance. You can find
this value on the **Overview** page for your instance in the
[Google Cloud console](https://console.cloud.google.com/sql) or by running the
following
`gcloud sql instances describe`
command:

```
gcloud sql instances describe INSTANCE_NAME

```

Replace INSTANCE\_NAME with the name of your Cloud SQL
instance.
- Get the CLOUD\_RUN\_SERVICE\_ACCOUNT\_NAME for your Cloud Run
service. You can find this value on the **IAM** page of the
project that's hosting the Cloud Run service in the
[Google Cloud console](https://console.cloud.google.com/iam-admin/serviceaccounts) or by
running the following
`gcloud run services describe`
command in the project that's hosting the Cloud Run service:

```
gcloud run services describe CLOUD_RUN_SERVICE_NAME
  --region CLOUD_RUN_SERVICE_REGION --format="value(spec.template.spec.serviceAccountName)"

```

Replace the following variables:

- CLOUD\_RUN\_SERVICE\_NAME: the name of your Cloud Run service
- CLOUD\_RUN\_SERVICE\_REGION: the region of your Cloud Run service
- [Configure the service account](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) for your Cloud Run service. To
connect to Cloud SQL, make sure that the service account has the
`Cloud SQL Client` [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles#cloud-sql-roles).
- If you're adding a Cloud SQL connection to a new service, you need
to have your service
[containerized](https://docs.cloud.google.com/discover/what-are-containerized-applications)
and uploaded to the Container Registry or Artifact Registry. If you don't
already have a connection, then see these instructions about
[building and deploying](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
a container image.

- If you're connecting to
instances that are configured with the shared certificate authority (CA)
(`GOOGLE_MANAGED_CAS_CA`) option or the customer-managed CA
(`CUSTOMER_MANAGED_CAS_CA`) option as the
[server CA mode](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#ca-hierarchies),
then select the second generation execution environment when you
[select the
execution environment for the service](https://docs.cloud.google.com/run/docs/about-execution-environments#choose).
Both server CA mode options require you to connect to the instance
with the Cloud SQL Auth Proxy v2.

If your service runs in a first generation execution environment, then
you can connect only to Cloud SQL instances that are configured with
the per-instance certificate authority (CA) option
(`GOOGLE_MANAGED_INTERNAL_CA`) as the server CA mode. The first
generation execution environment of Cloud Run embeds the Cloud SQL Auth Proxy
v1. For more information about connection requirements to Cloud SQL
for the Cloud SQL Auth Proxy,
see [Requirements for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#requirements).

Like any configuration change, setting a new configuration
for the Cloud SQL connection leads to the creation of a new
Cloud Run revision. Subsequent revisions will also automatically get
this Cloud SQL connection unless you make explicit updates to change it.

Console

1. [Go to Cloud Run](https://console.cloud.google.com/run/services)

2. Start configuring the service. To add Cloud SQL
    connections to an existing service, do the following:
1. From the **Services** list, click the service name you want.
2. Click **Edit & deploy new revision**.
3. Enable connecting to a Cloud SQL instance:

1. Click **Container(s)** and then **Settings**.
2. Scroll to **Cloud SQL connections**.
3. Click **Add connection**.
4. Click **Enable the Cloud SQL Admin** button if you haven't
       enabled the Cloud SQL Admin API yet.

https://docs.cloud.google.com/static/run/docs/images/cloudsql-connection.png
- If you're adding a connection to a Cloud SQL
      instance in your project, then select the Cloud SQL
      instance you want from the menu.

- If you're using a Cloud SQL instance from another
      project, then select **custom connection string** in
      the menu and enter the full instance connection name in the
      format PROJECT-ID:REGION:INSTANCE-ID.

- To delete a connection, hold your cursor to the
      right of the connection to display the delete **Delete** icon, and click it.
4. Click **Create** or **Deploy**.

Command line

Before using any of the following commands, make the following replacements:

- IMAGE with the image you're deploying
- SERVICE\_NAME with the name of your Cloud Run service
- INSTANCE\_CONNECTION\_NAME with the instance connection name of
your Cloud SQL instance, or a comma delimited list of
connection names.

If you're deploying a new container, use the following command:

```
gcloud run deploy \
    --image=IMAGE \
    --add-cloudsql-instances=INSTANCE_CONNECTION_NAME
```

If you're updating an existing service, use the following command:

```
gcloud run services update SERVICE_NAME \
    --add-cloudsql-instances=INSTANCE_CONNECTION_NAME
```

Terraform

The following code creates a base Cloud Run container, with a connected Cloud SQL instance.

```
resource "google_cloud_run_v2_service" "default" {
  name     = "cloudrun-service"
  location = "us-central1"

  deletion_protection = false # set to "true" in production

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello:latest" # Image to deploy

      volume_mounts {
        name       = "cloudsql"
        mount_path = "/cloudsql"
      }
    }
    volumes {
      name = "cloudsql"
      cloud_sql_instance {
        instances = [google_sql_database_instance.default.connection_name]
      }
    }
  }
  client     = "terraform"
  depends_on = [google_project_service.secretmanager_api, google_project_service.cloudrun_api, google_project_service.sqladmin_api]
}
```

1. Apply the changes by entering `terraform apply`.

2. Verify the changes by checking the [Cloud Run](https://docs.cloud.google.com/run) service, clicking the **Revisions** tab, and then the **Connections** tab.

Private IP

If the authorizing service account belongs to a different project than the
one containing the Cloud SQL instance, do the following:

- In both projects, enable the Cloud SQL Admin API.
- For the service account in the project that contains the Cloud SQL instance, add the [IAM permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions#serverless-roles-permissions).

Direct VPC egress and connectors use private IP addresses to handle
communication to your VPC network.

To connect directly with private IP addresses using one of these egress methods,
do the following:

1. Make sure that the Cloud SQL instance created previously has a
    private IP address. To add an internal IP address, see
    [Configure private IP](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip).
2. [Configure your egress method](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc)
    to connect to the same VPC network as your Cloud SQL
    instance.
    Note the following conditions:

- Direct VPC egress and Serverless VPC Access both support
      communication to VPC networks connected using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn)
      and [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering).
- Direct VPC egress and Serverless VPC Access don't support
      [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).
- Unless you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#shared-vpc), a connector must share the same project and
      region as the resource that uses it, although the connector can send traffic
      to resources in different regions.

4. Connect using your instance's private IP address and port `5432`.

## Connect to Cloud SQL

After you configure Cloud Run, you can connect to your
Cloud SQL instance.

Public IP (default)

For public IP paths, Cloud Run can be set up to use the
[Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) for encryption
in two ways:

- Through [Unix sockets](https://docs.cloud.google.com/sql/docs/postgres/connect-run#connect-unix-socket)
- By using a [Cloud SQL connector](https://docs.cloud.google.com/sql/docs/postgres/connect-run#connect-connectors)

**Connect with Unix sockets**

Once correctly configured, you can connect your service to your Cloud SQL
instance's Unix domain socket accessed on the environment's filesystem
at the following path:
`/cloudsql/INSTANCE_CONNECTION_NAME`.

The INSTANCE\_CONNECTION\_NAME uses the format
`project:region:instance-id`. You can find it
on the **Overview** page for your instance in the
[Google Cloud console](https://console.cloud.google.com/sql) or by running the
following command:

`gcloud sql instances describe [INSTANCE_NAME]`

These connections are automatically encrypted without any additional
configuration.

The code samples shown below are extracts from more complete examples on
the
GitHub site. Click `View on GitHub` to see more.

Python

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/postgres/sqlalchemy/README.md).

```
import os

import sqlalchemy

def connect_unix_socket() -> sqlalchemy.engine.base.Engine:
    """Initializes a Unix socket connection pool for a Cloud SQL instance of Postgres."""
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.
    db_user = os.environ["DB_USER"]  # e.g. 'my-database-user'
    db_pass = os.environ["DB_PASS"]  # e.g. 'my-database-password'
    db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    unix_socket_path = os.environ[\
        "INSTANCE_UNIX_SOCKET"\
    ]  # e.g. '/cloudsql/project:region:instance'

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # postgresql+pg8000://<db_user>:<db_pass>@/<db_name>
        #                         ?unix_sock=<INSTANCE_UNIX_SOCKET>/.s.PGSQL.5432
        # Note: Some drivers require the `unix_sock` query parameter to use a different key.
        # For example, 'psycopg2' uses the path set to `host` in order to connect successfully.
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=db_user,
            password=db_pass,
            database=db_name,
            query={"unix_sock": f"{unix_socket_path}/.s.PGSQL.5432"},
        ),
        # ...
    )
    return pool
```

Java

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/postgres/servlet/README.md).

```
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import javax.sql.DataSource;

public class ConnectorConnectionPoolFactory extends ConnectionPoolFactory {

  // Note: Saving credentials in environment variables is convenient, but not
  // secure - consider a more secure solution such as
  // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
  // keep secrets safe.
  private static final String INSTANCE_CONNECTION_NAME =
      System.getenv("INSTANCE_CONNECTION_NAME");
  private static final String INSTANCE_UNIX_SOCKET = System.getenv("INSTANCE_UNIX_SOCKET");
  private static final String DB_USER = System.getenv("DB_USER");
  private static final String DB_PASS = System.getenv("DB_PASS");
  private static final String DB_NAME = System.getenv("DB_NAME");

  public static DataSource createConnectionPool() {
    // The configuration object specifies behaviors for the connection pool.
    HikariConfig config = new HikariConfig();

    // The following URL is equivalent to setting the config options below:
    // jdbc:postgresql:///<DB_NAME>?cloudSqlInstance=<INSTANCE_CONNECTION_NAME>&
    // socketFactory=com.google.cloud.sql.postgres.SocketFactory&user=<DB_USER>&password=<DB_PASS>
    // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
    // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url

    // Configure which instance and what database user to connect with.
    config.setJdbcUrl(String.format("jdbc:postgresql:///%s", DB_NAME));
    config.setUsername(DB_USER); // e.g. "root", _postgres"
    config.setPassword(DB_PASS); // e.g. "my-password"

    config.addDataSourceProperty("socketFactory", "com.google.cloud.sql.postgres.SocketFactory");
    config.addDataSourceProperty("cloudSqlInstance", INSTANCE_CONNECTION_NAME);

    // Unix sockets are not natively supported in Java, so it is necessary to use the Cloud SQL
    // Java Connector to connect. When setting INSTANCE_UNIX_SOCKET, the connector will
    // call an external package that will enable Unix socket connections.
    // Note: For Java users, the Cloud SQL Java Connector can provide authenticated connections
    // which is usually preferable to using the Cloud SQL Proxy with Unix sockets.
    // See https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory for details.
    if (INSTANCE_UNIX_SOCKET != null) {
      config.addDataSourceProperty("unixSocketPath", INSTANCE_UNIX_SOCKET);
    }

    // cloudSqlRefreshStrategy set to "lazy" is used to perform a
    // refresh when needed, rather than on a scheduled interval.
    // This is recommended for serverless environments to
    // avoid background refreshes from throttling CPU.
    config.addDataSourceProperty("cloudSqlRefreshStrategy", "lazy");

    // ... Specify additional connection properties here.
    // ...

    // Initialize the connection pool using the configuration object.
    return new HikariDataSource(config);
  }
}
```

Node.js

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/cloud-sql/postgres/knex/README.md).

```
const Knex = require('knex');

// createUnixSocketPool initializes a Unix socket connection pool for
// a Cloud SQL instance of Postgres.
const createUnixSocketPool = async config => {
  // Note: Saving credentials in environment variables is convenient, but not
  // secure - consider a more secure solution such as
  // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
  // keep secrets safe.
  return Knex({
    client: 'pg',
    connection: {
      user: process.env.DB_USER, // e.g. 'my-user'
      password: process.env.DB_PASS, // e.g. 'my-user-password'
      database: process.env.DB_NAME, // e.g. 'my-database'
      host: process.env.INSTANCE_UNIX_SOCKET, // e.g. '/cloudsql/project:region:instance'
    },
    // ... Specify additional properties here.
    ...config,
  });
};
```

C#

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/master/cloud-sql/postgres/README.md).

```
using Npgsql;
using System;

namespace CloudSql
{
    public class PostgreSqlUnix
    {
        public static NpgsqlConnectionStringBuilder NewPostgreSqlUnixSocketConnectionString()
        {
            // Equivalent connection string:
            // "Server=<INSTANCE_UNIX_SOCKET>;Uid=<DB_USER>;Pwd=<DB_PASS>;Database=<DB_NAME>"
            var connectionString = new NpgsqlConnectionStringBuilder()
            {
                // The Cloud SQL proxy provides encryption between the proxy and instance.
                SslMode = SslMode.Disable,

                // Note: Saving credentials in environment variables is convenient, but not
                // secure - consider a more secure solution such as
                // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                // keep secrets safe.
                Host = Environment.GetEnvironmentVariable("INSTANCE_UNIX_SOCKET"), // e.g. '/cloudsql/project:region:instance'
                Username = Environment.GetEnvironmentVariable("DB_USER"), // e.g. 'my-db-user
                Password = Environment.GetEnvironmentVariable("DB_PASS"), // e.g. 'my-db-password'
                Database = Environment.GetEnvironmentVariable("DB_NAME"), // e.g. 'my-database'
            };
            connectionString.Pooling = true;
            // Specify additional properties here.
            return connectionString;
        }
    }
}
```

Go

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/postgres/database-sql/README.md).

```
package cloudsql

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	// Note: If connecting using the App Engine Flex Go runtime, use
	// "github.com/jackc/pgx/stdlib" instead, since v5 requires
	// Go modules which are not supported by App Engine Flex.
	_ "github.com/jackc/pgx/v5/stdlib"
)

// connectUnixSocket initializes a Unix socket connection pool for
// a Cloud SQL instance of Postgres.
func connectUnixSocket() (*sql.DB, error) {
	mustGetenv := func(k string) string {
		v := os.Getenv(k)
		if v == "" {
			log.Fatalf("Fatal Error in connect_unix.go: %s environment variable not set.\n", k)
		}
		return v
	}
	// Note: Saving credentials in environment variables is convenient, but not
	// secure - consider a more secure solution such as
	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
	// keep secrets safe.
	var (
		dbUser         = mustGetenv("DB_USER")              // e.g. 'my-db-user'
		dbPwd          = mustGetenv("DB_PASS")              // e.g. 'my-db-password'
		unixSocketPath = mustGetenv("INSTANCE_UNIX_SOCKET") // e.g. '/cloudsql/project:region:instance'
		dbName         = mustGetenv("DB_NAME")              // e.g. 'my-database'
	)

	dbURI := fmt.Sprintf("user=%s password=%s database=%s host=%s",
		dbUser, dbPwd, dbName, unixSocketPath)

	// dbPool is the pool of database connections.
	dbPool, err := sql.Open("pgx", dbURI)
	if err != nil {
		return nil, fmt.Errorf("sql.Open: %w", err)
	}

	// ...

	return dbPool, nil
}
```

Ruby

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/cloud-sql/postgres/activerecord/README.md).

```
unix: &unix
  adapter: postgresql
  # Configure additional properties here.
  # Note: Saving credentials in environment variables is convenient, but not
  # secure - consider a more secure solution such as
  # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
  # keep secrets safe.
  username: <%= ENV["DB_USER"] %>  # e.g. "my-database-user"
  password: <%= ENV["DB_PASS"] %> # e.g. "my-database-password"
  database: <%= ENV.fetch("DB_NAME") { "vote_development" } %>
  # Specify the Unix socket path as host
  host: "<%= ENV["INSTANCE_UNIX_SOCKET"] %>"
```

PHP

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/cloud_sql/postgres/pdo/README.md).

```
namespace Google\Cloud\Samples\CloudSQL\Postgres;

use PDO;
use PDOException;
use RuntimeException;
use TypeError;

class DatabaseUnix
{
    public static function initUnixDatabaseConnection(): PDO
    {
        try {
            // Note: Saving credentials in environment variables is convenient, but not
            // secure - consider a more secure solution such as
            // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
            // keep secrets safe.
            $username = getenv('DB_USER'); // e.g. 'your_db_user'
            $password = getenv('DB_PASS'); // e.g. 'your_db_password'
            $dbName = getenv('DB_NAME'); // e.g. 'your_db_name'
            $instanceUnixSocket = getenv('INSTANCE_UNIX_SOCKET'); // e.g. '/cloudsql/project:region:instance'

            // Connect using UNIX sockets
            $dsn = sprintf(
                'pgsql:dbname=%s;host=%s',
                $dbName,
                $instanceUnixSocket
            );

            // Connect to the database.
            $conn = new PDO(
                $dsn,
                $username,
                $password,
                # ...
            );
        } catch (TypeError $e) {
            throw new RuntimeException(
                sprintf(
                    'Invalid or missing configuration! Make sure you have set ' .
                        '$username, $password, $dbName, ' .
                        'and $instanceUnixSocket (for UNIX socket mode). ' .
                        'The PHP error was %s',
                    $e->getMessage()
                ),
                (int) $e->getCode(),
                $e
            );
        } catch (PDOException $e) {
            throw new RuntimeException(
                sprintf(
                    'Could not connect to the Cloud SQL Database. Check that ' .
                        'your username and password are correct, that the Cloud SQL ' .
                        'proxy is running, and that the database exists and is ready ' .
                        'for use. For more assistance, refer to %s. The PDO error was %s',
                    'https://cloud.google.com/sql/docs/postgres/connect-external-app',
                    $e->getMessage()
                ),
                (int) $e->getCode(),
                $e
            );
        }

        return $conn;
    }
}
```

**Connect with Cloud SQL connectors**

The [Cloud SQL connectors](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors)
are language specific libraries that provide encryption and IAM-based authorization
when connecting to a Cloud SQL instance.

Python

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/postgres/sqlalchemy/README.md).

```
import os

from google.cloud.sql.connector import Connector, IPTypes
import pg8000

import sqlalchemy

def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    """
    Initializes a connection pool for a Cloud SQL instance of Postgres.

    Uses the Cloud SQL Python Connector package.
    """
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.

    instance_connection_name = os.environ[\
        "INSTANCE_CONNECTION_NAME"\
    ]  # e.g. 'project:region:instance'
    db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
    db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
    db_name = os.environ["DB_NAME"]  # e.g. 'my-database'

    ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC

    # initialize Cloud SQL Python Connector object
    connector = Connector(refresh_strategy="LAZY")

    def getconn() -> pg8000.dbapi.Connection:
        conn: pg8000.dbapi.Connection = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
            ip_type=ip_type,
        )
        return conn

    # The Cloud SQL Python Connector can be used with SQLAlchemy
    # using the 'creator' argument to 'create_engine'
    pool = sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
        # ...
    )
    return pool
```

Java

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/postgres/servlet/README.md).

Note:

- CLOUD\_SQL\_CONNECTION\_NAME should be represented as
<MY-PROJECT>:<INSTANCE-REGION>:<INSTANCE-NAME>
- See the JDBC socket factory version requirements for the pom.xml
file [here](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc-mysql.md).

```
import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import javax.sql.DataSource;

public class ConnectorConnectionPoolFactory extends ConnectionPoolFactory {

  // Note: Saving credentials in environment variables is convenient, but not
  // secure - consider a more secure solution such as
  // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
  // keep secrets safe.
  private static final String INSTANCE_CONNECTION_NAME =
      System.getenv("INSTANCE_CONNECTION_NAME");
  private static final String INSTANCE_UNIX_SOCKET = System.getenv("INSTANCE_UNIX_SOCKET");
  private static final String DB_USER = System.getenv("DB_USER");
  private static final String DB_PASS = System.getenv("DB_PASS");
  private static final String DB_NAME = System.getenv("DB_NAME");

  public static DataSource createConnectionPool() {
    // The configuration object specifies behaviors for the connection pool.
    HikariConfig config = new HikariConfig();

    // The following URL is equivalent to setting the config options below:
    // jdbc:postgresql:///<DB_NAME>?cloudSqlInstance=<INSTANCE_CONNECTION_NAME>&
    // socketFactory=com.google.cloud.sql.postgres.SocketFactory&user=<DB_USER>&password=<DB_PASS>
    // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
    // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url

    // Configure which instance and what database user to connect with.
    config.setJdbcUrl(String.format("jdbc:postgresql:///%s", DB_NAME));
    config.setUsername(DB_USER); // e.g. "root", _postgres"
    config.setPassword(DB_PASS); // e.g. "my-password"

    config.addDataSourceProperty("socketFactory", "com.google.cloud.sql.postgres.SocketFactory");
    config.addDataSourceProperty("cloudSqlInstance", INSTANCE_CONNECTION_NAME);

    // The ipTypes argument can be used to specify a comma delimited list of preferred IP types
    // for connecting to a Cloud SQL instance. The argument ipTypes=PRIVATE will force the
    // SocketFactory to connect with an instance's associated private IP.
    config.addDataSourceProperty("ipTypes", "PUBLIC,PRIVATE");

    // cloudSqlRefreshStrategy set to "lazy" is used to perform a
    // refresh when needed, rather than on a scheduled interval.
    // This is recommended for serverless environments to
    // avoid background refreshes from throttling CPU.
    config.addDataSourceProperty("cloudSqlRefreshStrategy", "lazy");

    // ... Specify additional connection properties here.
    // ...

    // Initialize the connection pool using the configuration object.
    return new HikariDataSource(config);
  }
}
```

Go

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/postgres/database-sql/README.md).

```
package cloudsql

import (
	"context"
	"database/sql"
	"fmt"
	"log"
	"net"
	"os"

	"cloud.google.com/go/cloudsqlconn"
	"github.com/jackc/pgx/v5"
	"github.com/jackc/pgx/v5/stdlib"
)

func connectWithConnector() (*sql.DB, error) {
	mustGetenv := func(k string) string {
		v := os.Getenv(k)
		if v == "" {
			log.Fatalf("Fatal Error in connect_connector.go: %s environment variable not set.\n", k)
		}
		return v
	}
	// Note: Saving credentials in environment variables is convenient, but not
	// secure - consider a more secure solution such as
	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
	// keep passwords and other secrets safe.
	var (
		dbUser                 = mustGetenv("DB_USER")                  // e.g. 'my-db-user'
		dbPwd                  = mustGetenv("DB_PASS")                  // e.g. 'my-db-password'
		dbName                 = mustGetenv("DB_NAME")                  // e.g. 'my-database'
		instanceConnectionName = mustGetenv("INSTANCE_CONNECTION_NAME") // e.g. 'project:region:instance'
		usePrivate             = os.Getenv("PRIVATE_IP")
	)

	dsn := fmt.Sprintf("user=%s password=%s database=%s", dbUser, dbPwd, dbName)
	config, err := pgx.ParseConfig(dsn)
	if err != nil {
		return nil, err
	}
	var opts []cloudsqlconn.Option
	if usePrivate != "" {
		opts = append(opts, cloudsqlconn.WithDefaultDialOptions(cloudsqlconn.WithPrivateIP()))
	}
	// WithLazyRefresh() Option is used to perform refresh
	// when needed, rather than on a scheduled interval.
	// This is recommended for serverless environments to
	// avoid background refreshes from throttling CPU.
	opts = append(opts, cloudsqlconn.WithLazyRefresh())
	d, err := cloudsqlconn.NewDialer(context.Background(), opts...)
	if err != nil {
		return nil, err
	}
	// Use the Cloud SQL connector to handle connecting to the instance.
	// This approach does *NOT* require the Cloud SQL proxy.
	config.DialFunc = func(ctx context.Context, network, instance string) (net.Conn, error) {
		return d.Dial(ctx, instanceConnectionName)
	}
	dbURI := stdlib.RegisterConnConfig(config)
	dbPool, err := sql.Open("pgx", dbURI)
	if err != nil {
		return nil, fmt.Errorf("sql.Open: %w", err)
	}
	return dbPool, nil
}
```

Node.js

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/main/cloud-sql/postgres/knex/README.md).

```
const Knex = require('knex');
const {Connector} = require('@google-cloud/cloud-sql-connector');

// In case the PRIVATE_IP environment variable is defined then we set
// the ipType=PRIVATE for the new connector instance, otherwise defaults
// to public ip type.
const getIpType = () =>
  process.env.PRIVATE_IP === '1' || process.env.PRIVATE_IP === 'true'
    ? 'PRIVATE'
    : 'PUBLIC';

// connectWithConnector initializes connection pool for a Cloud SQL instance
// of Postgres using the Cloud SQL Node.js Connector.
const connectWithConnector = async config => {
  // Note: Saving credentials in environment variables is convenient, but not
  // secure - consider a more secure solution such as
  // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
  // keep secrets safe.
  const connector = new Connector();
  const clientOpts = await connector.getOptions({
    instanceConnectionName: process.env.INSTANCE_CONNECTION_NAME,
    ipType: getIpType(),
  });
  const dbConfig = {
    client: 'pg',
    connection: {
      ...clientOpts,
      user: process.env.DB_USER, // e.g. 'my-user'
      password: process.env.DB_PASS, // e.g. 'my-user-password'
      database: process.env.DB_NAME, // e.g. 'my-database'
    },
    // ... Specify additional properties here.
    ...config,
  };
  // Establish a connection to the database.
  return Knex(dbConfig);
};
```

### Use Secret Manager

Google recommends that you use [Secret Manager](https://docs.cloud.google.com/secret-manager) to store
sensitive information such as SQL credentials. You can [pass secrets as
environment variables or mount as a volume](https://docs.cloud.google.com/run/docs/configuring/secrets) with Cloud Run.

After [creating a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create) in
Secret Manager, update an existing service, with the following command:

Command line

```
gcloud run services update SERVICE_NAME \
  --add-cloudsql-instances=INSTANCE_CONNECTION_NAME
  --update-env-vars=INSTANCE_CONNECTION_NAME=INSTANCE_CONNECTION_NAME_SECRET \
  --update-secrets=DB_USER=DB_USER_SECRET:latest \
  --update-secrets=DB_PASS=DB_PASS_SECRET:latest \
  --update-secrets=DB_NAME=DB_NAME_SECRET:latest
```

Terraform

The following creates secret resources to securely hold the database user, password, and name values using `google_secret_manager_secret` and `google_secret_manager_secret_version`. Note that you must update the project compute service account to have access to each secret.

```

# Create dbuser secret
resource "google_secret_manager_secret" "dbuser" {
  secret_id = "dbusersecret"
  replication {
    auto {}
  }
  depends_on = [google_project_service.secretmanager_api]
}

# Attaches secret data for dbuser secret
resource "google_secret_manager_secret_version" "dbuser_data" {
  secret      = google_secret_manager_secret.dbuser.id
  secret_data = "secret-data" # Stores secret as a plain txt in state
}

# Update service account for dbuser secret
resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbuser" {
  secret_id = google_secret_manager_secret.dbuser.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
}
```

```

# Create dbpass secret
resource "google_secret_manager_secret" "dbpass" {
  secret_id = "dbpasssecret"
  replication {
    auto {}
  }
  depends_on = [google_project_service.secretmanager_api]
}

# Attaches secret data for dbpass secret
resource "google_secret_manager_secret_version" "dbpass_data" {
  secret      = google_secret_manager_secret.dbpass.id
  secret_data = "secret-data" # Stores secret as a plain txt in state
}

# Update service account for dbpass secret
resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbpass" {
  secret_id = google_secret_manager_secret.dbpass.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
}
```

```

# Create dbname secret
resource "google_secret_manager_secret" "dbname" {
  secret_id = "dbnamesecret"
  replication {
    auto {}
  }
  depends_on = [google_project_service.secretmanager_api]
}

# Attaches secret data for dbname secret
resource "google_secret_manager_secret_version" "dbname_data" {
  secret      = google_secret_manager_secret.dbname.id
  secret_data = "secret-data" # Stores secret as a plain txt in state
}

# Update service account for dbname secret
resource "google_secret_manager_secret_iam_member" "secretaccess_compute_dbname" {
  secret_id = google_secret_manager_secret.dbname.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${data.google_project.project.number}-compute@developer.gserviceaccount.com" # Project's compute service account
}
```

Update the main Cloud Run resource to include the new secrets.

```
resource "google_cloud_run_v2_service" "default" {
  name     = "cloudrun-service"
  location = "us-central1"

  deletion_protection = false # set to "true" in production

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello:latest" # Image to deploy

      # Sets a environment variable for instance connection name
      env {
        name  = "INSTANCE_CONNECTION_NAME"
        value = google_sql_database_instance.default.connection_name
      }
      # Sets a secret environment variable for database user secret
      env {
        name = "DB_USER"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.dbuser.secret_id # secret name
            version = "latest"                                      # secret version number or 'latest'
          }
        }
      }
      # Sets a secret environment variable for database password secret
      env {
        name = "DB_PASS"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.dbpass.secret_id # secret name
            version = "latest"                                      # secret version number or 'latest'
          }
        }
      }
      # Sets a secret environment variable for database name secret
      env {
        name = "DB_NAME"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.dbname.secret_id # secret name
            version = "latest"                                      # secret version number or 'latest'
          }
        }
      }

      volume_mounts {
        name       = "cloudsql"
        mount_path = "/cloudsql"
      }
    }
    volumes {
      name = "cloudsql"
      cloud_sql_instance {
        instances = [google_sql_database_instance.default.connection_name]
      }
    }
  }
  client     = "terraform"
  depends_on = [google_project_service.secretmanager_api, google_project_service.cloudrun_api, google_project_service.sqladmin_api]
}
```

Apply the changes by entering `terraform apply`.

The example command uses the secret version, latest; however, Google recommends
[pinning the secret](https://docs.cloud.google.com/secret-manager/docs/best-practices#administration) to a specific version, SECRET\_NAME:v1.

Private IP

For private IP paths, your application connects directly to your
instance through a VPC network.
This method uses TCP to connect directly to the Cloud SQL
instance without using the Cloud SQL Auth Proxy.

### Connect with TCP

Connect using the private IP address of your Cloud SQL instance as the host and port `5432`.

Python

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/postgres/sqlalchemy/README.md).

```
import os
import ssl

import sqlalchemy

def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
    """Initializes a TCP connection pool for a Cloud SQL instance of Postgres."""
    # Note: Saving credentials in environment variables is convenient, but not
    # secure - consider a more secure solution such as
    # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
    # keep secrets safe.
    db_host = os.environ[\
        "INSTANCE_HOST"\
    ]  # e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
    db_user = os.environ["DB_USER"]  # e.g. 'my-db-user'
    db_pass = os.environ["DB_PASS"]  # e.g. 'my-db-password'
    db_name = os.environ["DB_NAME"]  # e.g. 'my-database'
    db_port = os.environ["DB_PORT"]  # e.g. 5432

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name,
        ),
        # ...
    )
    return pool
```

Java

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/java-docs-samples/blob/master/cloud-sql/postgres/servlet/README.md).

Note:

- CLOUD\_SQL\_CONNECTION\_NAME should be represented as
<MY-PROJECT>:<INSTANCE-REGION>:<INSTANCE-NAME>
- Using the argument ipTypes=PRIVATE will force the SocketFactory
to connect with an instance's associated private IP
- See the [JDBC socket factory version requirements for the pom.xml
file](https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory/blob/main/docs/jdbc.md).

```

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import javax.sql.DataSource;

public class TcpConnectionPoolFactory extends ConnectionPoolFactory {

  // Note: Saving credentials in environment variables is convenient, but not
  // secure - consider a more secure solution such as
  // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
  // keep secrets safe.
  private static final String DB_USER = System.getenv("DB_USER");
  private static final String DB_PASS = System.getenv("DB_PASS");
  private static final String DB_NAME = System.getenv("DB_NAME");

  private static final String INSTANCE_HOST = System.getenv("INSTANCE_HOST");
  private static final String DB_PORT = System.getenv("DB_PORT");

  public static DataSource createConnectionPool() {
    // The configuration object specifies behaviors for the connection pool.
    HikariConfig config = new HikariConfig();

    // The following URL is equivalent to setting the config options below:
    // jdbc:postgresql://<INSTANCE_HOST>:<DB_PORT>/<DB_NAME>?user=<DB_USER>&password=<DB_PASS>
    // See the link below for more info on building a JDBC URL for the Cloud SQL JDBC Socket Factory
    // https://github.com/GoogleCloudPlatform/cloud-sql-jdbc-socket-factory#creating-the-jdbc-url

    // Configure which instance and what database user to connect with.
    config.setJdbcUrl(String.format("jdbc:postgresql://%s:%s/%s", INSTANCE_HOST, DB_PORT, DB_NAME));
    config.setUsername(DB_USER); // e.g. "root", "postgres"
    config.setPassword(DB_PASS); // e.g. "my-password"

    // ... Specify additional connection properties here.
    // ...

    // Initialize the connection pool using the configuration object.
    return new HikariDataSource(config);
  }
}
```

Node.js

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/cloud-sql/postgres/knex/README.md).

```
const Knex = require('knex');
const fs = require('fs');

// createTcpPool initializes a TCP connection pool for a Cloud SQL
// instance of Postgres.
const createTcpPool = async config => {
  // Note: Saving credentials in environment variables is convenient, but not
  // secure - consider a more secure solution such as
  // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
  // keep secrets safe.
  const dbConfig = {
    client: 'pg',
    connection: {
      host: process.env.INSTANCE_HOST, // e.g. '127.0.0.1'
      port: process.env.DB_PORT, // e.g. '5432'
      user: process.env.DB_USER, // e.g. 'my-user'
      password: process.env.DB_PASS, // e.g. 'my-user-password'
      database: process.env.DB_NAME, // e.g. 'my-database'
    },
    // ... Specify additional properties here.
    ...config,
  };
  // Establish a connection to the database.
  return Knex(dbConfig);
};
```

Go

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/golang-samples/tree/master/cloudsql/postgres/database-sql/README.md).

```
package cloudsql

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	// Note: If connecting using the App Engine Flex Go runtime, use
	// "github.com/jackc/pgx/stdlib" instead, since v5 requires
	// Go modules which are not supported by App Engine Flex.
	_ "github.com/jackc/pgx/v5/stdlib"
)

// connectTCPSocket initializes a TCP connection pool for a Cloud SQL
// instance of Postgres.
func connectTCPSocket() (*sql.DB, error) {
	mustGetenv := func(k string) string {
		v := os.Getenv(k)
		if v == "" {
			log.Fatalf("Fatal Error in connect_tcp.go: %s environment variable not set.", k)
		}
		return v
	}
	// Note: Saving credentials in environment variables is convenient, but not
	// secure - consider a more secure solution such as
	// Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
	// keep secrets safe.
	var (
		dbUser    = mustGetenv("DB_USER")       // e.g. 'my-db-user'
		dbPwd     = mustGetenv("DB_PASS")       // e.g. 'my-db-password'
		dbTCPHost = mustGetenv("INSTANCE_HOST") // e.g. '127.0.0.1' ('172.17.0.1' if deployed to GAE Flex)
		dbPort    = mustGetenv("DB_PORT")       // e.g. '5432'
		dbName    = mustGetenv("DB_NAME")       // e.g. 'my-database'
	)

	dbURI := fmt.Sprintf("host=%s user=%s password=%s port=%s database=%s",
		dbTCPHost, dbUser, dbPwd, dbPort, dbName)

	// dbPool is the pool of database connections.
	dbPool, err := sql.Open("pgx", dbURI)
	if err != nil {
		return nil, fmt.Errorf("sql.Open: %w", err)
	}

	// ...

	return dbPool, nil
}
```

C#

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/master/cloud-sql/mysql/README.md).

```
using Npgsql;
using System;

namespace CloudSql
{
    public class PostgreSqlTcp
    {
        public static NpgsqlConnectionStringBuilder NewPostgreSqlTCPConnectionString()
        {
            // Equivalent connection string:
            // "Uid=<DB_USER>;Pwd=<DB_PASS>;Host=<INSTANCE_HOST>;Database=<DB_NAME>;"
            var connectionString = new NpgsqlConnectionStringBuilder()
            {
                // Note: Saving credentials in environment variables is convenient, but not
                // secure - consider a more secure solution such as
                // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
                // keep secrets safe.
                Host = Environment.GetEnvironmentVariable("INSTANCE_HOST"),     // e.g. '127.0.0.1'
                // Set Host to 'cloudsql' when deploying to App Engine Flexible environment
                Username = Environment.GetEnvironmentVariable("DB_USER"), // e.g. 'my-db-user'
                Password = Environment.GetEnvironmentVariable("DB_PASS"), // e.g. 'my-db-password'
                Database = Environment.GetEnvironmentVariable("DB_NAME"), // e.g. 'my-database'

                // The Cloud SQL proxy provides encryption between the proxy and instance.
                SslMode = SslMode.Disable,
            };
            connectionString.Pooling = true;
            // Specify additional properties here.
            return connectionString;
        }
    }
}
```

Ruby

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/ruby-docs-samples/tree/master/cloud-sql/postgres/activerecord/README.md).

```
tcp: &tcp
  adapter: postgresql
  # Configure additional properties here.
  # Note: Saving credentials in environment variables is convenient, but not
  # secure - consider a more secure solution such as
  # Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
  # keep secrets safe.
  username: <%= ENV["DB_USER"] %>  # e.g. "my-database-user"
  password: <%= ENV["DB_PASS"] %> # e.g. "my-database-password"
  database: <%= ENV.fetch("DB_NAME") { "vote_development" } %>
  host: <%= ENV.fetch("INSTANCE_HOST") { "127.0.0.1" }%> # '172.17.0.1' if deployed to GAE Flex
  port: <%= ENV.fetch("DB_PORT") { 5432 }%>
```

PHP

To see this snippet in the context of a web application, view
[the README on GitHub](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/main/cloud_sql/postgres/pdo/README.md).

```
namespace Google\Cloud\Samples\CloudSQL\Postgres;

use PDO;
use PDOException;
use RuntimeException;
use TypeError;

class DatabaseTcp
{
    public static function initTcpDatabaseConnection(): PDO
    {
        try {
            // Note: Saving credentials in environment variables is convenient, but not
            // secure - consider a more secure solution such as
            // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
            // keep secrets safe.
            $username = getenv('DB_USER'); // e.g. 'your_db_user'
            $password = getenv('DB_PASS'); // e.g. 'your_db_password'
            $dbName = getenv('DB_NAME'); // e.g. 'your_db_name'
            $instanceHost = getenv('INSTANCE_HOST'); // e.g. '127.0.0.1' ('172.17.0.1' for GAE Flex)

            // Connect using TCP
            $dsn = sprintf('pgsql:dbname=%s;host=%s', $dbName, $instanceHost);

            // Connect to the database
            $conn = new PDO(
                $dsn,
                $username,
                $password,
                # ...
            );
        } catch (TypeError $e) {
            throw new RuntimeException(
                sprintf(
                    'Invalid or missing configuration! Make sure you have set ' .
                        '$username, $password, $dbName, and $instanceHost (for TCP mode). ' .
                        'The PHP error was %s',
                    $e->getMessage()
                ),
                $e->getCode(),
                $e
            );
        } catch (PDOException $e) {
            throw new RuntimeException(
                sprintf(
                    'Could not connect to the Cloud SQL Database. Check that ' .
                        'your username and password are correct, that the Cloud SQL ' .
                        'proxy is running, and that the database exists and is ready ' .
                        'for use. For more assistance, refer to %s. The PDO error was %s',
                    'https://cloud.google.com/sql/docs/postgres/connect-external-app',
                    $e->getMessage()
                ),
                $e->getCode(),
                $e
            );
        }

        return $conn;
    }
}
```

## Best practices and other information

You can use the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) when testing
your application locally. See the
[quickstart for using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-auth-proxy)
for detailed instructions.

You can also test using the
[Cloud SQL Proxy via a docker container](https://docs.cloud.google.com/sql/docs/postgres/connect-docker).

### Connection Pools

Connections to underlying databases may be dropped, either by the database
server itself, or by the platform infrastructure. We recommend using a client
library that supports connection pools that
automatically reconnect broken client connections.

You can use Managed Connection Pooling with your Cloud SQL
instances, which lets you scale your workloads by optimizing resource
utilization and connection latency for your Cloud SQL instances using
pooling. For detailed information about Managed Connection Pooling, see
[Managed Connection Pooling overview](https://docs.cloud.google.com/sql/docs/postgres/managed-connection-pooling).

For more detailed examples on how to use connection pools, see the
[Managing database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections) page.

### Connection Limits

Both the MySQL and PostgreSQL editions of Cloud SQL impose a maximum limit on
concurrent connections, and these limits may vary depending on the database
engine chosen (see the
[Cloud SQL Quotas and Limits](https://docs.cloud.google.com/sql/docs/quotas#fixed-limits) page).

Cloud Run container instances are limited to 100 connections to a
Cloud SQL database.
Each instance of a Cloud Run service or job can have
100 connections to the database, and as this service or job scales, the total number of
connections per deployment can grow.

You can limit the maximum number of connections used per instance by using a
connection pool. For more detailed examples on how to limit the number of
connections, see the
[Managing database connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections#count) page.

### API Quota Limits

Cloud Run provides a mechanism that connects using the Cloud SQL Auth Proxy, which uses the
Cloud SQL Admin API.
[API quota limits](https://console.cloud.google.com/iam-admin/quotas?service=sqladmin.googleapis.com) apply to the Cloud SQL Auth Proxy. The Cloud SQL Admin API quota
used is approximately two times the number of Cloud SQL instances
configured by the number of Cloud Run instances of a particular
service deployed at any one time.
You can [cap or increase the number
of Cloud Run instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) to modify the expected API quota
consumed.

## What's next

- Learn more about [Cloud Run](https://docs.cloud.google.com/run/docs).
- Learn more about [building and deploying](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy) container images.

- See a [complete example in Python for using Cloud Run with PostgreSQL](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/cloud-sql/postgres/sqlalchemy).
```

</details>

<details>
<summary>https://cloud.google.com/sql/docs/postgres/iam-authentication</summary>

Google Cloud offers Identity and Access Management (IAM), which lets you give
access to specific Google Cloud resources and prevent unwanted
access to other resources. This page describes how Cloud SQL is integrated with
IAM
and how you can use IAM for managing access to Cloud SQL
resources and for database authentication.
For a detailed description of Google Cloud IAM, see
[IAM documentation](https://docs.cloud.google.com/iam/docs).

Cloud SQL provides a set of [predefined roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles)
designed to help you control access to your Cloud SQL resources. You can
also create your own [custom roles](https://docs.cloud.google.com/sql/docs/postgres/iam-roles#custom-roles),
if the predefined roles don't provide the sets of permissions you need.

## IAM authentication concepts

When using IAM authentication, permission to access a resource
(a Cloud SQL instance) isn't granted _directly_ to the end user. Instead,
permissions are grouped into _roles_, and roles are granted to _principals_. For
more information, see the
[IAM overview](https://docs.cloud.google.com/iam/docs/overview).

Administrators who have users log in through IAM database authentication can use
IAM authentication to centrally manage access control to their instances
using IAM policies.

IAM policies involve the following entities:

- **Principals**. In Cloud SQL, you can use several
types of principals: a _user account_, a _service account_
(for applications), or a _group_.
For more information, see
[Concepts related to identity](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity).
- **Roles**. A role is a collection of permissions. You can grant roles to
principals to provide them with the privileges required to accomplish
specific tasks.
For example, with IAM database authentication, a principal requires
the `cloudsql.instances.login` permission to log in to an instance, which is
included in the **Cloud SQL Instance User** role.
To get the permission, you bind the user, service account,
or group to the predefined Cloud SQL role or a custom role that
includes the permission. For more information about IAM roles,
see [Roles](https://docs.cloud.google.com/iam/docs/overview#roles).
- **Resource**. The resources that principals access are Cloud SQL
instances. By default, IAM policy bindings are applied at the
project-level, such that principals receive role permissions for all
Cloud SQL instances in the project.

## IAM database authentication

Database authentication is the process of verifying the identity of a user who is
attempting to access databases. In Cloud SQL, you can use the following
types of database authentication for database users:

- The database's [built-in authentication](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication)
uses a username and password to authenticate a database user.
- IAM database authentication uses IAM to authenticate a user by using an access
token.

## Automatic versus manual IAM database authentication

Cloud SQL for PostgreSQL has two options for IAM database authentication: automatic and manual.

### Automatic IAM database authentication

_Automatic IAM database authentication_ lets you hand off requesting and managing access tokens
to
an intermediary [Cloud SQL connector](https://docs.cloud.google.com/sql/docs/postgres/connect-overview),
such as the Cloud SQL Auth Proxy or one of the Cloud SQL Language Connectors. With automatic
IAM database authentication, users need to pass only the
IAM database username in a connection request from the client.
The connector submits the access token information for the password attribute on
behalf of the client.

Automatic IAM database authentication requires the use of a Cloud SQL connector and
is supported by the
[Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy), the [Go connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#go), the
[Java connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#java), and the
[Python connector](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors#python).

For the most secure and reliable experience, we recommend you use automatic
IAM database authentication. IAM database authentication uses OAuth 2.0 access tokens, which are short-lived and
valid for only one hour. Cloud SQL connectors are able to request and refresh
these tokens, ensuring that long-lived processes or applications that rely on
connection pooling can have stable connections. Automatic IAM database authentication is strongly
recommended over manual authentication.

For more information, see [Log in with automatic IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins#log-in-with-automatic).

### Manual IAM database authentication

_Manual IAM database authentication_ requires the IAM principal to explicitly pass
the access token for the password attribute in the client connection request.
Principals must first log in to Google Cloud and explicitly request the access
token from IAM.

Using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), you can explicitly request an
[OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) token with the
Cloud SQL Admin API scope that is used to log in to the database. When you log in as a
database user with IAM database authentication, you use your email address as the username and
the access token as the password. You can use this method with either a direct
connection to the database or with a Cloud SQL connector.

Logging in with IAM database authentication can only be performed over an SSL
connection.

For more information, see
[Logging in with manual IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins#logging-in-as-a-user).

### Context-aware access and IAM database authentication

If you're using [context-aware access](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto)
in your IAM configuration, then you can't use a
Cloud SQL connector such as the Cloud SQL Auth Proxy or one of the
Cloud SQL Language Connectors with IAM database authentication. Attempts to login either manually or
automatically with IAM authentication will fail.
Connect directly to the instance instead.

## User and service account administration

To provide users and service accounts access to databases on an instance using
IAM database authentication, you need to add them to the instance or add
them to a group that has access to the instance. For more information,
see [Add a user or service account that uses IAM](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user).

If you use the Google Cloud console to add users or service accounts, Cloud SQL
asks you to add the "Cloud SQL User" role to the user. This role is required
for users to log in to the instance.

If you add users using `gcloud` or the API, you need to grant login privileges
manually. Use the PostgreSQL [GRANT](https://www.postgresql.org/docs/current/static/sql-grant.html) command
to [grant database privileges](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#grant-db-privileges).

## Instance configuration for Cloud SQL IAM database authentication

You can enable IAM database authentication on an instance using the `cloudsql.iam_authentication`
flag. Once you enable this flag, the instance enables logins from accounts that
are configured for IAM database authentication.

This flag is required for IAM group authentication and IAM database authentication.

Setting the flag does not prevent existing, non-IAM users from
using their usernames and passwords to log in. However, if you disable this flag
on the instance, any user that you previously added using IAM database authentication loses
access to the instance. For more information, see
[Configuring instances for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances).

### Cloud SQL IAM database authentication for different instance scenarios

|     |     |
| --- | --- |
| **Read replicas** | IAM database authentication is not enabled in a read replica automatically, even when it<br> is enabled on the primary instance. After you create a read replica, you<br> need to add IAM database authentication. For more information, see<br> [Configure read replica logins for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica#configure_iam_replicas). |
| **Restored instances** | If an instance was previously backed up and later restored to the same or<br> a different instance in the same project, the current user login<br> authorizations apply. If you restore a backup to a new instance in another<br> project, you need to set up the user authorizations for the new instance. For<br> more information, see<br> [Add a user or service account that uses IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user). |

## About IAM Conditions

IAM Conditions lets you grant
roles based on a variety of attributes. For example, you can allow
access only at certain dates and times or grant access only to
Cloud SQL resources with certain names.

For more information about IAM Conditions, see
the [Overview of IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview)
page. You can also learn more about
[Using IAM Conditions](https://docs.cloud.google.com/sql/docs/postgres/iam-conditions)
with Cloud SQL, including examples.

## Work with Cloud Audit Logs

To keep records of data access, including logins, you can use audit logs.
[Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit#data-access) is turned off, by default. You
need to turn on [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) for
login tracking. Using audit logging for this purpose incurs costs for data
logging. For more information, see [Audit Logs](https://docs.cloud.google.com/sql/docs/postgres/audit-logging#audited_operations),
[Configuring Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)
and [Pricing for logging data](https://docs.cloud.google.com/logging#pricing).

## Restrictions

1. The login for an IAM database authentication user account must be all lowercase. For example,
     `example-user@example.com`. `Example-User@example.com`
     is not allowed.
2. For security, logins using IAM database authentication are only available on an SSL
     connection. Unencrypted connections are rejected.
3. There is a per-minute login quota for each instance, which includes both
     successful and unsuccessful logins. When the quota is exceeded, logins are
     temporarily unavailable. We recommend that you avoid frequent logins and
     restrict logins using [authorized networks](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks).

     The quota for authorization of logins is 12,000 per minute, per instance.

## What's next

  - Learn how to [configure instances for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances).
  - Learn how to [add a user or service account that uses IAM database authentication to your database](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user).
  - Learn how to [log in to a Cloud SQL database with IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins).
  - Learn how to [view login information in audit logs](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#viewing-login-audit-logs).
  - Learn about [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

</details>

## Local Files

<details>
<summary>source.md</summary>

In Lesson 32, we took the first major steps toward production readiness by implementing OAuth 2.0 authentication with Descope and containerizing our research agent with Docker. We identified four key changes required to transform our local prototype into a cloud-native application: (1) stateless data storage, (2) user authentication, (3) file upload/download handling, and (4) containerization. With authentication and Docker complete, this lesson tackles the remaining pieces: replacing the local filesystem with a PostgreSQL database and implementing workarounds for file transfers that the MCP specification does not yet support.

The transition from file-based to database-backed storage is more than a technical upgrade; it is a fundamental shift in how our agent manages state. In `research_agent_part_2`, every piece of data lived in a `.nova/` folder on the local filesystem. This approach worked for single-user development but fails catastrophically in production where multiple users share the same server and container instances can be replaced at any moment. By moving all state to a PostgreSQL database, we achieve three critical goals: data persists beyond container lifetimes, each user's data is isolated from others, and we gain powerful query capabilities for features like rate limiting and analytics.

This lesson also introduces a bonus feature enabled by our database: rate limiting for MCP tools. Since each tool call can trigger expensive LLM API requests, we need a way to track and limit usage per user. The database makes this straightforward by recording every tool invocation and checking usage counts before allowing new calls.

## Choosing a Database

The first major decision when moving from file-based to database-backed storage is choosing the right database technology. Before committing to a specific solution, it is worth considering the alternatives and understanding why PostgreSQL emerged as the best choice for our use case.

### Why We Need a Database

Serverless platforms like Cloud Run impose constraints that make local file storage impractical:

*   **Ephemeral Containers:** Container instances can be created, destroyed, or replaced at any time. Any data written to the local filesystem is lost when this happens [[1]](https://cloud.google.com/run/docs/configuring/services/containers).
*   **Multi-User Isolation:** Multiple users will access our agent simultaneously. Without a database, their data would intermingle in the same files, causing overwrites and corruption.
*   **Query Capabilities:** Features like rate limiting require counting records efficiently. A database provides indexing and query optimization that file-based storage cannot match.

### Why PostgreSQL

After evaluating SQLite (unsuitable for multi-container deployments [[2]](https://www.sqlite.org/whentouse.html)), MySQL/MariaDB (limited JSON support), MongoDB (less appropriate for relational data [[4]](https://www.mongodb.com/docs/manual/core/data-modeling-introduction/)), and Firebase/Firestore (vendor lock-in and limited query capabilities [[5]](https://firebase.google.com/docs/firestore)), PostgreSQL emerged as the ideal choice. It provides ACID transactions for data integrity [[7]](https://www.postgresql.org/docs/current/tutorial-transactions.html), native JSON/JSONB columns for storing structured data like extracted URLs [[3]](https://www.postgresql.org/docs/current/datatype-json.html), high-performance async support through `asyncpg` [[8]](https://magicstack.github.io/asyncpg/current/), seamless Cloud SQL integration [[9]](https://cloud.google.com/sql/docs/postgres), and a rich Python ecosystem with SQLAlchemy and Alembic [[10]](https://www.sqlalchemy.org/), [[11]](https://alembic.sqlalchemy.org/) [[6]](https://www.postgresql.org/about/).

## Database Schema Design

With PostgreSQL selected, let's design a schema that captures all the data our research agent needs to persist. The schema must replace every file that `research_agent_part_2` stored in the `.nova/` folder while also supporting multi-user access through user ID associations.

### The Article Model

The `Article` model is the central entity in our schema, replacing the research folder and its `.nova/` subdirectory. Every piece of data that was previously a file now becomes a column on this table.

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
        Enum(ArticleStatus, ...),
        default=ArticleStatus.CREATED,
        nullable=False,
        comment="Current status of the research workflow",
    )

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

*   **UUID Primary Key:** Using UUIDs instead of auto-incrementing integers allows us to generate IDs client-side and prevents information leakage about how many articles exist.
*   **User ID Index:** The `user_id` column is indexed for fast lookups when querying a user's articles.
*   **JSON Column:** The `extracted_urls` field uses PostgreSQL's native JSON type to store structured data that would otherwise require multiple tables.
*   **Status Enum:** A PostgreSQL enum tracks the workflow state, enabling queries like "show me all failed articles."

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

## Refactoring Tools: From Files to Database

Now that we understand the schema, let's see how the MCP tools were refactored to use the database instead of the filesystem. Every tool follows the same transformation pattern: what was once a file path parameter becomes a UUID, file reads become database queries, and file writes become database updates.

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

This same pattern applies to all other tools in the research workflow. The business logic (URL extraction, web scraping, LLM calls) remains unchanged; only the storage layer is different.

## Local Development with Docker Compose

With our tools refactored for database access, we need a way to run PostgreSQL during development. Docker Compose provides an elegant solution by defining our multi-container application in a single YAML file. With one command, we can spin up both the PostgreSQL database and our MCP server.

### The Two-Service Architecture

Our `docker-compose.yml` defines two services that work together:

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

volumes:
  postgres_data:
    driver: local
```

### Key Configuration Elements

Several aspects of this configuration deserve explanation:

*   **Docker Network Hostname:** The `DATABASE_URL` uses `postgres` as the hostname, which Docker's internal networking resolves to the PostgreSQL container's IP address. This works because both containers share the same Docker network [[12]](https://docs.docker.com/compose/how-tos/networking/).

*   **Named Volume:** The `postgres_data` volume persists database files outside the container. When you run `docker compose down`, the data survives. Only `docker compose down -v` removes the volume [[13]](https://docs.docker.com/engine/storage/volumes/).

*   **Health Check:** The `pg_isready` command verifies PostgreSQL is accepting connections. The MCP server's `depends_on: condition: service_healthy` ensures it waits for a healthy database before starting [[14]](https://docs.docker.com/reference/compose-file/services/#healthcheck).

*   **Source Mount:** Mounting `./src:/app/src:ro` allows code changes during development without rebuilding the container, while `:ro` (read-only) prevents the container from modifying host files.

To start the development environment:

```bash
# Build and start both services
docker compose up -d

# View logs
docker compose logs -f mcp-server

# Stop services (preserves data)
docker compose down

# Stop and remove all data
docker compose down -v
```

## Cloud SQL for Production

Docker Compose works perfectly for local development, but production requires a managed database service. Google Cloud SQL provides fully managed PostgreSQL instances that integrate seamlessly with Cloud Run, offering automatic backups, high availability, and IAM-based authentication.

### What is Cloud SQL

Cloud SQL is Google Cloud's fully managed relational database service supporting PostgreSQL, MySQL, and SQL Server [[9]](https://cloud.google.com/sql/docs/postgres). For production deployments, it offers several advantages over self-managed databases:

*   **Automatic Backups:** Daily backups with point-in-time recovery, configurable retention periods.
*   **High Availability:** Optional regional instances with automatic failover.
*   **Security Patches:** Google applies security updates without downtime.
*   **Private Connectivity:** Cloud Run can connect to Cloud SQL over private IP, never exposing the database to the public internet [[15]](https://cloud.google.com/sql/docs/postgres/connect-run).
*   **IAM Authentication:** Instead of managing passwords, Cloud Run authenticates using its service account [[16]](https://cloud.google.com/sql/docs/postgres/iam-authentication).

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

The `is_cloud_sql` property provides a simple check: if `CLOUD_SQL_INSTANCE` is set, we are running in production; otherwise, we use the local `DATABASE_URL`.

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

The Cloud SQL Python Connector provides several benefits over direct connection strings [[17]](https://github.com/GoogleCloudPlatform/cloud-sql-python-connector):

*   **IAM Authentication:** Connects using the Cloud Run service account's identity.
*   **Automatic Certificate Handling:** Manages SSL certificates transparently.
*   **Connection Pooling:** Efficiently manages database connections.
*   **Lazy Refresh:** The `refresh_strategy="lazy"` option is optimized for Cloud Run, where CPU may be throttled between requests.

## Database Migrations with Alembic

Whether running locally or in the cloud, we need a way to evolve our database schema over time. Adding a new column, creating a new table, or modifying an index requires careful coordination between code changes and database changes. Alembic provides database migrations for SQLAlchemy, acting as version control for your database schema.

### What is Alembic

Alembic is a database migration tool created by the author of SQLAlchemy [[11]](https://alembic.sqlalchemy.org/). It addresses a fundamental challenge: your SQLAlchemy models define what the schema *should* be, but the database might have an older schema. Alembic bridges this gap by:

*   **Version Control:** Each migration has a unique revision ID, creating a linear history of schema changes.
*   **Upgrade/Downgrade:** Migrations define both `upgrade()` (apply changes) and `downgrade()` (rollback) functions.
*   **Autogeneration:** Alembic can compare your models to the database and generate migration scripts automatically.
*   **Environment Support:** The same migrations run in development, staging, and production.

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
        sa.Column("guideline_text", sa.Text(), nullable=False),
        sa.Column("status", postgresql.ENUM(..., name="article_status", create_type=False),
                  nullable=False, server_default="created"),
        sa.Column("extracted_urls", postgresql.JSON(), nullable=True),
        sa.Column("perplexity_results", sa.Text(), nullable=True),
        # ... more columns
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()")),
    )

def downgrade() -> None:
    """Drop the articles table."""
    op.drop_table("articles")
    op.execute("DROP TYPE IF EXISTS article_status")
```

Key patterns in this migration:

*   **Idempotent Enum Creation:** The `DO $$ BEGIN ... EXCEPTION` block handles the case where the enum already exists, making the migration safe to re-run.
*   **Server Defaults:** Using `server_default=sa.text("now()")` ensures timestamps are set by the database, not Python.
*   **Comments:** Column comments document the schema for future developers.

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

The composite index on `(user_id, year_month)` is crucial for rate limiting performance. When checking a user's monthly usage, the database can quickly locate all matching records without scanning the entire table.

### Running Migrations

In development, run migrations manually:

```bash
# Apply all pending migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# View current revision
alembic current

# View migration history
alembic history
```

In production, the Docker entrypoint script runs migrations automatically on container startup:

```bash
# research_agent_part_3/docker-entrypoint.sh

#!/bin/bash
set -e

echo "Running database migrations..."
alembic upgrade head

echo "Starting MCP server..."
exec uvicorn src.server:mcp --host 0.0.0.0 --port 8000
```

This ensures the database schema is always up-to-date before the application starts accepting requests.

## Rate Limiting for MCP Tools

With the database infrastructure in place, we can now implement features that require persistent storage. Rate limiting is a perfect example: it needs to track usage across requests and even container restarts. Without a database, we would have no way to know how many tool calls a user has made this month.

### Why Rate Limiting Matters

MCP tools are not free to operate. Each tool call can trigger expensive API requests:

*   **LLM Calls:** Perplexity research, source selection, and query generation all invoke paid LLM APIs.
*   **Web Scraping:** Firecrawl charges per page scraped.
*   **YouTube Transcription:** Processing videos consumes compute resources.

Without rate limiting, a single user (or a malfunctioning agent loop) could exhaust your API budget in minutes. Rate limiting also enables future business models: in the current implementation, all users share the same monthly limit, but the system could be extended to support premium users with higher limits or unlimited access.

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

The `year_month` column is a deliberate denormalization. We could extract the month from `created_at`, but storing it explicitly enables a simple, indexed query: `SELECT COUNT(*) WHERE user_id = ? AND year_month = ?`.

### The @rate_limited Decorator

The rate limiting logic is encapsulated in a decorator that wraps MCP tools:

```python
# research_agent_part_3/src/utils/rate_limit_utils.py

class RateLimitExceededError(Exception):
    """Raised when a user exceeds their monthly tool call limit."""

    def __init__(self, user_id: str, current_usage: int, limit: int):
        self.user_id = user_id
        self.current_usage = current_usage
        self.limit = limit
        # Calculate next month reset date
        now = datetime.now(UTC)
        if now.month == 12:
            self.resets_at = datetime(now.year + 1, 1, 1, tzinfo=UTC)
        else:
            self.resets_at = datetime(now.year, now.month + 1, 1, tzinfo=UTC)

        super().__init__(
            f"Monthly tool usage limit exceeded. You have used {current_usage}/{limit} "
            f"tool calls this month. Your quota resets on {self.resets_at.strftime('%B %d, %Y')}."
        )


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

The decorator:

1.  Extracts the `user_id` from the OAuth access token (authentication required).
2.  Queries the database for the current month's usage count.
3.  Raises `RateLimitExceededError` if the limit is reached, including the reset date.
4.  Records the new tool call if within limits.
5.  Executes the original tool function.

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

The decorator order matters: `@mcp.tool()` registers the function as an MCP tool, `@opik.track()` adds observability, and `@rate_limited` enforces usage limits.

## File Upload: Working Around MCP Limitations

Rate limiting solves the usage tracking problem, but there's another challenge the MCP specification doesn't address: file uploads and downloads. The MCP protocol defines tools, resources, and prompts, but it has no mechanism for transferring files over HTTP transport. Let's see how we worked around this limitation.

### The MCP Protocol Gap

When running locally with `stdio` transport, file handling is straightforward: the agent can read files from the user's filesystem. But HTTP transport is different:

*   The MCP client (Cursor) and MCP server may be on different machines.
*   There's no MCP message type for "upload this file" or "download this file."
*   Users need to upload article guidelines before research can begin.

The MCP specification is actively evolving and may address file handling in future versions [[18]](https://modelcontextprotocol.io/specification). For now, we implement a workaround using custom HTTP endpoints.

### Our Solution: Custom HTTP Endpoints

FastMCP allows adding custom HTTP routes alongside MCP endpoints using the `@mcp.custom_route()` decorator. These routes are regular HTTP endpoints that exist outside the MCP protocol.

### The Upload Flow

The upload flow involves coordination between the user, the AI agent, and the MCP server:

```mermaid
sequenceDiagram
    participant User
    participant Agent as "AI Agent (Cursor)"
    participant MCP as "MCP Server"
    participant DB as "Database"

    User->>Agent: "I want to research a new article"
    Agent->>Agent: Retrieve user_id from auth token
    Agent->>User: "Please upload your guideline at: {URL}?user_id=xxx"
    User->>MCP: Opens URL in browser
    MCP->>User: Returns HTML upload form
    User->>MCP: Uploads .md file via form
    MCP->>DB: Creates Article record
    DB->>MCP: Returns article UUID
    MCP->>User: Displays UUID on success page
    User->>Agent: "My article ID is abc-123-..."
    Agent->>MCP: Calls tools with article_guideline_id=abc-123
```

Image 2: Sequence diagram showing the article guideline upload flow. The agent provides a URL with the user's ID, the user uploads their file in a browser, and receives a UUID to provide back to the agent.

### Implementation Details

The upload UI is implemented in `upload_ui.py`:

```python
# research_agent_part_3/src/ui/upload_ui.py

UPLOAD_PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Upload Article Guideline - Nova Research</title>
    <!-- Styled form with drag-and-drop support -->
</head>
<body>
    <div class="container">
        <h1>Upload Article Guideline</h1>
        <form id="uploadForm">
            <div class="file-input-wrapper">
                <input type="file" id="fileInput" accept=".md" required>
                <div class="file-text">Click or drag to upload your markdown file</div>
            </div>
            <button type="submit">Upload Article Guideline</button>
        </form>
        <div class="result" id="result">
            <!-- Shows UUID on success -->
        </div>
    </div>
    <script>
        // JavaScript handles form submission and displays result
        const userId = new URLSearchParams(window.location.search).get('user_id');
        
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData();
            formData.append('file', fileInput.files[0]);
            
            const response = await fetch(
                `/upload_article_guideline?user_id=${encodeURIComponent(userId)}`,
                { method: 'POST', body: formData }
            );
            const data = await response.json();
            // Display article_id to user
        });
    </script>
</body>
</html>
"""


async def post_upload_guideline(request: Request) -> JSONResponse:
    """Handle article guideline file upload."""
    
    # Get user_id from query params
    user_id = request.query_params.get("user_id")
    if not user_id:
        return JSONResponse(status_code=400, content={"error": "Missing user_id"})

    # Parse multipart form data
    form = await request.form()
    file = form.get("file")
    content = await file.read()
    if isinstance(content, bytes):
        content = content.decode("utf-8")

    # Generate article ID and save to database
    article_id = uuid.uuid4()
    session_factory = await get_async_session_factory()
    async with session_factory() as session:
        article = Article(
            id=article_id,
            user_id=user_id,
            guideline_text=content,
            status=ArticleStatus.CREATED,
        )
        session.add(article)
        await session.commit()

    return JSONResponse(
        status_code=201,
        content={"article_id": str(article_id), "message": "Upload successful"},
    )
```

The routes are registered in `ui.py`:

```python
# research_agent_part_3/src/routers/ui.py

def register_ui_routes(mcp: FastMCP) -> None:
    """Register UI routes with the FastMCP server."""

    @mcp.custom_route("/upload_article_guideline", methods=["GET"])
    async def upload_page(request: Request) -> HTMLResponse:
        """Serve the article guideline upload page."""
        return await get_upload_page(request)

    @mcp.custom_route("/upload_article_guideline", methods=["POST"])
    async def upload_guideline(request: Request) -> JSONResponse:
        """Handle article guideline file upload."""
        return await post_upload_guideline(request)
```

## File Download: Delivering Research Results

The upload flow gets data into the system. At the end of the research workflow, we need the reverse: a way for users to download the final research document. The same custom route approach applies.

### The Download Flow

```mermaid
sequenceDiagram
    participant User
    participant Agent as "AI Agent (Cursor)"
    participant MCP as "MCP Server"
    participant DB as "Database"

    Agent->>MCP: Calls create_research_file(article_id)
    MCP->>DB: Queries all research data
    DB->>MCP: Returns scraped content, transcripts, etc.
    MCP->>MCP: Compiles markdown document
    MCP->>DB: Saves to Article.research column
    MCP->>Agent: Returns {download_url: "{URL}?article_guideline_id=xxx"}
    Agent->>User: "Download your research at: {URL}"
    User->>MCP: Opens URL in browser
    MCP->>DB: Queries Article.research
    DB->>MCP: Returns markdown content
    MCP->>User: Returns file with Content-Disposition: attachment
    User->>User: Browser downloads research.md
```

Image 3: Sequence diagram showing the research file download flow. The tool compiles research data, saves it to the database, and returns a download URL that the user opens in their browser.

### Implementation

The download route is simpler than upload since it only needs to serve existing content:

```python
# research_agent_part_3/src/routers/downloads.py

def register_download_routes(mcp: FastMCP) -> None:
    """Register download routes with the FastMCP server."""

    @mcp.custom_route("/download_research", methods=["GET"])
    async def download_research(request: Request) -> Response:
        """Download the research.md file for a given article."""
        
        article_guideline_id = request.query_params.get("article_guideline_id")
        if not article_guideline_id:
            return JSONResponse(status_code=400, content={"error": "Missing article_guideline_id"})

        # Validate UUID format
        try:
            article_uuid = uuid.UUID(article_guideline_id)
        except ValueError:
            return JSONResponse(status_code=400, content={"error": "Invalid UUID format"})

        # Query database for article
        session_factory = await get_async_session_factory()
        async with session_factory() as session:
            article = await session.get(Article, article_uuid)

            if not article:
                return JSONResponse(status_code=404, content={"error": "Article not found"})

            if not article.research:
                return JSONResponse(
                    status_code=404,
                    content={"error": "No research content. Run create_research_file first."},
                )

            # Return as downloadable file
            return Response(
                content=article.research,
                media_type="text/markdown; charset=utf-8",
                headers={"Content-Disposition": 'attachment; filename="research.md"'},
            )
```

The `create_research_file_tool` generates the download URL:

```python
# research_agent_part_3/src/tools/create_research_file_tool.py

def get_download_url(article_guideline_id: str) -> str:
    """Get the download URL for the research file."""
    if settings.server_base_url:
        base_url = settings.server_base_url.rstrip("/")
    else:
        base_url = f"http://{settings.server_host}:{settings.server_port}"
    return f"{base_url}/download_research?article_guideline_id={article_guideline_id}"


async def create_research_file_tool(article_guideline_id: str) -> Dict[str, Any]:
    """Generate comprehensive research markdown and provide download link."""
    
    # ... compile research from database ...
    
    # Save to database
    article.research = final_markdown
    await session.commit()

    # Return download URL
    download_url = get_download_url(article_guideline_id)
    return {
        "status": "success",
        "download_url": download_url,
        "message": f"Research complete. Download at: {download_url}",
    }
```

## Analytics and Monitoring

All this usage data, including tool calls, articles created, and research completed, lives in our database. This opens up powerful analytics possibilities that were impossible with file-based storage.

### What the Database Captures

Our schema provides rich data for analysis:

*   **Tool Usage:** Every tool call is recorded in `tool_call_usage` with user, tool name, and timestamp.
*   **Article Lifecycle:** The `articles` table tracks status transitions from `created` through `completed` or `failed`.
*   **Research Artifacts:** All intermediate data (scraped URLs, transcripts, etc.) is preserved for debugging.

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

-- Average tools per research session
SELECT 
    a.id as article_id,
    COUNT(t.id) as tool_calls
FROM articles a
LEFT JOIN tool_call_usage t ON a.user_id = t.user_id
GROUP BY a.id;

-- Users approaching rate limit
SELECT user_id, COUNT(*) as calls
FROM tool_call_usage
WHERE year_month = to_char(now(), 'YYYY-MM')
GROUP BY user_id
HAVING COUNT(*) > 80
ORDER BY calls DESC;
```

### Preview: Querying Cloud SQL

Once deployed, you can run these queries directly in Google Cloud Console's Cloud SQL Studio, or connect via the `gcloud` CLI:

```bash
# Connect to Cloud SQL instance
gcloud sql connect nova-db --user=nova --database=nova_research
```

We will cover Cloud SQL querying in detail in Lesson 34 after deploying the application.

## Conclusion

This lesson addressed the core infrastructure challenges of preparing an AI agent for production deployment. We transformed our research agent from a file-based prototype into a database-backed, rate-limited, cloud-ready application.

### Summary of Changes

*   **Database Integration:** Replaced the ephemeral `.nova/` folder with persistent PostgreSQL storage, ensuring data survives container restarts and can be queried efficiently.

*   **Schema Design:** Created an article-centric data model with supporting tables for research artifacts, each linked to users through authentication.

*   **Tool Refactoring:** Updated all MCP tools to read from and write to database columns instead of filesystem paths, maintaining the same business logic while changing only the storage layer.

*   **Environment Flexibility:** Designed the application to use Docker Compose with local PostgreSQL for development and Cloud SQL for production, switching based on environment variables.

*   **Schema Evolution:** Implemented Alembic migrations to version-control database changes, with automatic migration on container startup.

*   **Rate Limiting:** Added usage tracking and monthly limits to protect API budgets and enable tiered pricing models.

*   **File Handling:** Worked around MCP's lack of file transfer support by implementing custom HTTP endpoints for upload and download.

### What's Next in Lesson 34

With our agent fully prepared for production, the next lesson covers the actual deployment:

*   **Google Cloud Run Deployment:** Pushing our container to Artifact Registry and deploying to Cloud Run.
*   **Cloud SQL Setup:** Creating and configuring the production database instance.
*   **Continuous Deployment:** Setting up GitHub Actions to automatically deploy on push to main.
*   **Monitoring and Logging:** Using Cloud Logging and Cloud Monitoring to observe our agent in production.

## References

1. Google. (n.d.). *Container runtime contract*. Google Cloud. https://cloud.google.com/run/docs/configuring/services/containers
2. SQLite. (n.d.). *Appropriate Uses For SQLite*. https://www.sqlite.org/whentouse.html
3. PostgreSQL. (n.d.). *JSON Types*. https://www.postgresql.org/docs/current/datatype-json.html
4. MongoDB. (n.d.). *Data Modeling Introduction*. https://www.mongodb.com/docs/manual/core/data-modeling-introduction/
5. Firebase. (n.d.). *Cloud Firestore*. https://firebase.google.com/docs/firestore
6. PostgreSQL. (n.d.). *About PostgreSQL*. https://www.postgresql.org/about/
7. PostgreSQL. (n.d.). *Transactions*. https://www.postgresql.org/docs/current/tutorial-transactions.html
8. MagicStack. (n.d.). *asyncpg Documentation*. https://magicstack.github.io/asyncpg/current/
9. Google. (n.d.). *Cloud SQL for PostgreSQL documentation*. Google Cloud. https://cloud.google.com/sql/docs/postgres
10. SQLAlchemy. (n.d.). *SQLAlchemy Documentation*. https://www.sqlalchemy.org/
11. Alembic. (n.d.). *Alembic Documentation*. https://alembic.sqlalchemy.org/
12. Docker. (n.d.). *Networking in Compose*. https://docs.docker.com/compose/how-tos/networking/
13. Docker. (n.d.). *Use volumes*. https://docs.docker.com/engine/storage/volumes/
14. Docker. (n.d.). *Compose file reference: healthcheck*. https://docs.docker.com/reference/compose-file/services/#healthcheck
15. Google. (n.d.). *Connect from Cloud Run*. Google Cloud. https://cloud.google.com/sql/docs/postgres/connect-run
16. Google. (n.d.). *IAM database authentication*. Google Cloud. https://cloud.google.com/sql/docs/postgres/iam-authentication
17. Google. (n.d.). *Cloud SQL Python Connector*. GitHub. https://github.com/GoogleCloudPlatform/cloud-sql-python-connector
18. Model Context Protocol. (n.d.). *MCP Specification*. https://modelcontextprotocol.io/specification

</details>