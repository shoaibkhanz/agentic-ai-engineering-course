# Lesson 17 Guideline

## Global Context of the Lesson

### What We Are Planning to Share

Lesson 17 continues Part 2B by **building the ingestion layer** of our MCP‑based research agent and **executing Steps 1–2** of the server‑hosted workflow. You will:

- Implement a **sources‑extractor** MCP tool that scans an `article_guideline.md` and writes a compact JSON registry used by the rest of the workflow.
    - **Schema keys (normalized)**: `github_urls`, `youtube_videos_urls`, `other_urls`, `local_file_paths`.
- Add a **parallel web scraping** MCP tool that uses **Firecrawl** to return **markdown**, followed by a **brief LLM clean pass** aligned to the guideline so only pertinent content remains.
- Process **local files** (with **Jupyter→Markdown** conversion suited for LLMs), **ingest GitHub repos** (via `gitingest`), and **transcribe YouTube videos** (via Gemini; include a fallback if direct YT URL handling is restricted).
- **Run the agent with the server‑hosted MCP prompt** for **Steps 1–2**, inspect `.nova/` artifacts, and practice **non‑critical vs. critical failure** handling with explicit triggers for each tool.

> Refer back, don’t re‑teach:
> 
> - For **MCP concepts, transports, server/client layout** → **Lesson 16** (sections *MCP in Short*, *How the MCP Server Is Organized*, *The MCP Client*).
> - For **system design levers (cost/latency/context)** → **Lesson 14** (sections *Inference‑Time Scaling*, *Context Strategy*).
> - For **why we split research vs writing** → **Lesson 12**, and **framework trade‑offs** → **Lesson 13**.

### Why We Think It’s Valuable

A research agent lives or dies by the **quality, structure, and cost** of its inputs. Persisting big payloads to files, returning **short tool summaries**, and delegating messy capture to a **specialized scraper** lowers token spend and improves reliability (see **L14** for the cost levers we’re applying here). MCP lets us expose these tools once and drive them from any client; **server‑hosted prompts** make the workflow universally discoverable (see **L16**).

### Expected Length of the Lesson

**3,200–3,600 words** (without the titles and references), where we assume that 200–250 words ≈ 1 minute of reading time.

### Theory / Practice Ratio

**25% theory – 75% hands‑on**

---

## Anchoring the Lesson in the Course

### Details About the Course

This piece sits in **Part 2B: Building our MCP Research Agent**. Keep the point of view consistent (we/us for instructors; you/your for the student). **Don’t re‑teach prior lessons;** when needed, insert explicit references:

- “See **Lesson 16**: MCP server/client, transports, capability discovery.”
- “See **Lesson 14**: cost levers (file‑first outputs, small tool returns).”
- “See **Lesson 12–13**: the agent/workflow split and framework trade‑offs.”

### Lesson Scope

This is **Lesson 17 (Part 2B)** on **Data Ingestion for the MCP Research Agent**—you implement the ingestion tools and run **Steps 1–2** of the server‑hosted workflow to populate `.nova/` artifacts **without** starting the research rounds.

### Point of View

We write as a team (“we/our/us”) addressing a single reader (“you/your”). Avoid singular first‑person and never use “we” to refer to the student.

### Who Is the Intended Audience

Aspiring AI engineers learning how to **equip an MCP agent with production‑minded ingestion tools** that balance **reliability** and **token efficiency**.

### Concepts Introduced in Previous Lessons

- **Part 1:** Workflows vs. agents; context engineering; structured outputs; tool calling; planning/reasoning (ReAct); RAG; memory; multimodal.
- **Part 2A:** **L12** (capstone scope & agent split), **L13** (framework trade‑offs), **L14** (system design levers & cost budgets).
- **Part 2B:** **L16** (MCP primer; FastMCP client/server; server‑hosted prompt; discovery; thin orchestration over heavy tools).

> In this lesson, refer back to these, don’t re‑explain them.
> 

### Concepts That Will Be Introduced in Future Lessons

- **L18–L19:** Research rounds (generate next queries; run Perplexity), curation/selection, deep scrapes, and `research.md`.
- **L20–L23:** LangGraph writing workflow (stages, reflection, HITL).
- **Part 3:** Evaluation, observability, optimization, deployment.

### Anchoring the Reader in the Educational Journey

Assume **MCP primitives** and **ReAct** are known. If you mention Perplexity loop or curation, keep it high‑level and say: “covered in **L18–L19**.” For details on MCP mechanics, say: “See **L16**.”

---

## Narrative Flow of the Lesson

- **The problem we’re solving (Ingestion Debt):**
    
    Real research agents fail not for lack of “reasoning,” but because inputs are **noisy, redundant, and expensive** to pass to models. We need a **file‑first, tool‑light** ingestion layer that converts heterogeneous sources into **LLM‑ready markdown** and returns **short, structured tool summaries**.
    
- **What goes wrong without this design (Five anti‑patterns):**
    - Dumping entire pages into prompts (explodes token costs; see **L14**).
    - Browser‑grade scrapers (HTML noise, dynamic sites break).
    - Returning full content from tools (bloats context; hard to retry).
    - Inconsistent file naming/paths (collisions; hard to audit).
- **Our approach (MCP + file‑first artifacts):**
    - **MCP server‑hosted prompt** (discoverable recipe; see **L16**).
    - Specialized tools: **extract → process local → scrape & clean → GitHub ingest → YT transcribe**.
    - Each tool **persists artifacts** and returns a **compact `{status, counts, output_path, message}`**.
- **Walkthrough of Steps 1–2 (hands‑on):**
    - Run the server‑hosted prompt for **Steps 1–2** only.
    - Inspect `.nova/` folders; confirm counts match actual files.
    - Observe **concurrency**, **timeouts**, **retries**, and **cache**.
- **Advanced considerations you apply today (not just theory):**
    - **Clean‑pass constraints**: “remove irrelevancies, **don’t summarize**,” keep content traceable to source.
    - **Front‑matter metadata** in saved markdown (URL, captured‑at, tool version) for auditability.
    - **Critical vs non‑critical** failure policy for each tool, with concrete triggers.
- **Worked example (multi‑source guideline):**
    
    A guideline cites a GitHub repo, 2 web pages, 1 notebook, and a YouTube talk. Show the extractor’s JSON, the four tool results, and the finalized `.nova/` tree; call out a failure (e.g., one page blocked) and how the critical policy responds.
    
- **Zoom out (how this unlocks L18–L19):**
    
    Clean, deduped, on‑disk artifacts reduce **context cost** and enable reliable **Perplexity rounds** and **deep scrapes** later. See **L18–L19** for the research loop.
    

---

## Lesson Outline

1. **From MCP Setup to Ingestion: the Plan**
2. **Workflow & Endpoints: where the ingestion tools live**
3. **Tool to extract URLs & local references from the guideline**
4. **Tool to organize local files for LLMs (incl. Jupyter→Markdown)**
5. **Tool to scrape & clean web pages in parallel**
6. **Tool to ingest content from GitHub**
7. **Tool to transcribe and structure YouTube videos**
8. **Run Steps 1–2 end‑to‑end: inspect `.nova/`, handle failures, and wrap‑up**

---

## Section 1 — From MCP Setup to Ingestion: the Plan

- **Assume L16 is done**: you have a running MCP server and client; you know **in‑memory** and **stdio** transports, and how to list tools/resources/prompts. If you need the refresher, **see L16**.
- **Why ingestion first**: We’re cementing a **file‑first contract** that future steps read selectively (see **L14** for cost heuristics).
- **Notebook mapping**: Point to **Notebook Section 1 (Setup)** for API keys (Gemini, Firecrawl, optional GitHub) and **Section 2** for the Step 1–2 excerpt of the server‑hosted prompt.
- **Return policy**: Tools return **short dicts** and **write heavy content to files** for token efficiency.

---

## Section 2 — Workflow & Endpoints: where the ingestion tools live

- **Open the repo** to locate the server‑hosted prompt and tool routers.
- In `mcp_server/src/routers/tools.py`, verify registration for **five ingestion endpoints** used in Steps **1–2**:
    
    `extract_guidelines_urls`, `process_local_files`, `scrape_and_clean_other_urls`, `process_github_urls`, `transcribe_youtube_urls`.
    
- The **server‑hosted prompt** (`mcp_server/src/prompts/research_instructions_prompt.py`) enumerates **Steps 1–6** and the **critical‑stop policy**.
- **Short returns only**: `{status, counts, output_path, message}`—not full content.

> Reference cue: For MCP primitives and discovery, see L16.
> 

---

## Section 3 — Tool to extract URLs & local references from the guideline

- The workflow starts by **scanning the guidelines** and writing a compact JSON registry.
- **Tool goal:** Scan `article_guideline.md`, extract **GitHub** / **YouTube** / **other HTTP(S)** URLs and **local file references**, then write `.nova/guidelines_filenames.json`. Return a **summary** (counts + output path).
- *Show section 3 of the notebook:* walk through the implementation of `extract_guidelines_urls_tool.py`:
    1. Regex URL extraction + domain categorization.
    2. Local paths are limited to `.py`, `.ipynb`, `.md` (ignore anything that looks like a URL).
    3. JSON schema keys: `github_urls`, `youtube_videos_urls`, `other_urls`, **`local_file_paths`**.
    4. Return **short result**: `status`, counts, `output_path`, `message`.
- **Run it** (show the minimal call + printed dict from the notebook). This tool **seeds all of Step 2** and exemplifies **file‑first + short output** design.
- **Why this matters**: This tool **seeds Step 2** and enforces a **stable on‑disk contract**.

---

## Section 4 — Tool to organize local files for LLMs (incl. Jupyter→Markdown)

- With references extracted, **copy/convert local files** into a layout the model can actually read.
- **Tool goal:** Copy referenced local files into `.nova/local_files_from_research/`, **flattening paths** in filenames. Convert **notebooks to markdown** with code + markdown cells and **truncated outputs** to keep size manageable.
- *Show section 4 of the notebook:* explain `process_local_files_tool.py`:
    - Load `guidelines_filenames.json` .
    - Create a destination folder.
    - For `.ipynb`, use the notebook converter to produce **LLM‑friendly markdown** (keep code + outputs, truncate very long outputs).
    - Build and return `{status: "success" | "warning", files_processed, files_total, processed_files, warnings, errors, output_directory, message}`.
- **Edge behavior**: If 0 local files, return `status="success"` with 0 counts (**non‑critical**). The agent should continue to the other Step‑2 sub‑steps.
- **Why markdown**: predictable structure, selective reads, lower token waste (**see L14**).

---

## Section 5 — Tool to scrape & clean web pages in parallel

- Local artifacts are set—now **tame the web** with robust scrapes and a focused LLM clean pass.
- **Tool goal:** From `other_urls`, **scrape** each page, save **markdown** files under `.nova/urls_from_guidelines/`, and return a summary (total, successes, failures, output dir). Then run a **brief LLM clean pass** to remove nav/ads/footers and keep content **relevant to the guideline**.
- *Show section 5 of the notebook:* cover `scrape_and_clean_other_urls_tool.py`:
    - **Two‑stage pipeline.**
        1. **Firecrawl**: robust capture that returns **markdown**; handles dynamic content; supports caching and timeouts. Show the code from section 5 of the notebook.
        2. **LLM clean** (`clean_markdown(...)`): prompt instructs “**remove only irrelevant sections**; do **not** summarize; keep guideline‑pertinent content.” Show the code from section 5 of the notebook.
    - **Concurrency.** Asynchronous scraping with a **`concurrency_limit`** arg (recommend 4 for stability under vendor load).
    - **Retries + timeouts.** Show `scrape_url(...)` with retries, per‑request timeout, and Firecrawl `maxAge` to leverage cache where acceptable. ([Firecrawl](https://docs.firecrawl.dev/features/scrape?utm_source=chatgpt.com))
    - **Outputs.** `status`, `urls_processed` vs `urls_failed`, `successful_urls_count`, `failed_urls_count`, `output_directory`, `message`.
- Why a vendor scraper? Building and maintaining a modern scraper (JS rendering, anti‑bot handling, diverse HTML) is costly and brittle; Firecrawl specializes in LLM‑ready markdown and scale.

---

## Section 6 — Tool to ingest content from GitHub

- General pages are covered—**code repos** need a purpose‑built ingest
- **Tool goal:** Turn GitHub URLs into **prompt‑friendly digests** (repo overview + selected file contents) saved under `.nova/urls_from_guidelines_code/`.
- *Show section 6 from the notebook:* explain the `process_github_urls_tool.py` flow:
    - Use **`gitingest`** to fetch repository structure and content optimized for LLMs. It supports **public** and **private repos** (with a token that is used once and discarded). ([gitingest.com](https://gitingest.com/?utm_source=chatgpt.com))
    - Return `{status, urls_processed, urls_total, files_saved, output_directory, message}` and show a sample result.
- Why a repo‑specific tool? Repos require different heuristics (trees, code, notebooks); gitingest standardizes this into a digest.

---

## Section 7 — Tool to transcribe and structure YouTube videos

- Text and code are in—**videos** add fresh, high‑signal context.
- **Tool goal:** Given `youtube_videos_urls`, produce **timestamped markdown transcripts** saved under `.nova/urls_from_guidelines_youtube_videos/`. Expect **minutes‑scale latency** for longer videos; use **controlled concurrency**.
- *Show section 7 from the notebook:* walk `transcribe_youtube_videos_tool.py` and the helper `transcribe_youtube(...)`:
    - **Gemini video understanding:** you can **pass YouTube URLs directly** in a `generateContent` request; transcription is a documented capability.
    - Provide the prompt text, timestamp interval, retries/timeouts, and output writing.
    - Return `{status, videos_processed, videos_total, output_directory, message}`.
- Note for production. Keep concurrency conservative to respect API quotas; show the knob in the code comments. (Vertex AI docs also describe video understanding usage.)

---

## Section 8 — Run Steps 1–2 end‑to‑end: inspect `.nova/`, handle failures, and wrap‑up

- With all tools wired, **drive the workflow**, explore artifacts, and practice **non‑critical vs. critical** outcomes.
- **Drive the workflow with the server‑hosted prompt:** show section 8 from the notebook: start the in‑memory client, then type:
    - `/prompt/full_research_instructions_prompt` → agent explains the numbered steps and asks for `research_directory`.
    - Provide the path and say: “**Run only Steps 1–2 and stop**.”
    - Watch tool calls: `extract_guidelines_urls` → local/files/scrape/github/youtube, skipping `process_local_files` if the count is 0.
- **Why prompts on the server?** Any MCP client can discover and run the same recipe.
- **Explore the artifacts (from section 9 of the notebook)**

```
research_directory/
├── article_guideline.md
├── .nova/
│   ├── guidelines_filenames.json
│   ├── local_files_from_research/
│   ├── urls_from_guidelines/
│   ├── urls_from_guidelines_code/
│   └── urls_from_guidelines_youtube_videos/

```

**Critical vs. Non‑critical policy (concrete triggers for Steps 1–2):**

- **extract_guidelines_urls**
    - **Critical**: `article_guideline.md` missing or unreadable → stop and ask for a valid path.
    - **Non‑critical**: any category count is 0 (pipeline continues).
- **process_local_files**
    - **Critical**: destination write failures across all files (e.g., permission issues).
    - **Non‑critical**: 0 files to process; individual file errors (record in `warnings`/`errors`).
- **scrape_and_clean_other_urls**
    - If `other_urls > 0` **and** `urls_processed == 0` → **Critical stop**.
    - If `other_urls == 0` → **Non‑critical** (skip).
- **process_github_urls**
    - If `github_urls > 0` **and** `urls_processed == 0` → **Critical stop**.
    - If `github_urls == 0` → **Non‑critical** (skip).
- **transcribe_youtube_urls**
    - If `youtube_videos_urls > 0` **and** `videos_processed == 0` → **Critical stop**.
    - If `youtube_videos_urls == 0` → **Non‑critical** (skip).
- **Token efficiency:** keep heavy text out of the LLM’s context; the agent sees **short summaries + file paths**, and reads only what it needs later.
- **Auditability:** artifacts persist; easy to diff and debug.

---

## Article Code

Links to code used in this lesson (always prioritize this notebook):

1. **Notebook — L17 Data Ingestion**
    "/Users/omar/Documents/ai_repos/agentic-ai-engineering-course/lessons/17_data_ingestion/notebook.ipynb"

---

## Sources

0. Local files to use during research and writing:
    - [NOVA_SYSTEM_DESIGN]("/Users/omar/Documents/ai_repos/agentic-ai-engineering-course/lessons/14_agent_system_design/nova_system_design_notes.md")
1. **MCP — Tools** (server‑exposed actions & schemas). ([Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/tools))
2. **MCP — Prompts** (server‑hosted, discoverable workflow recipes). ([Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/prompts))
3. **MCP — Resources** (read‑only data exposed by servers). ([Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/resources))
4. **Firecrawl — Product & API** (scrape to markdown; dynamic sites; caching; timeouts). ([Firecrawl - The Web Data API for AI](https://www.firecrawl.dev/))
5. **Gemini API — Video understanding** (pass YouTube URLs; transcription). ([Google AI for Developers](https://ai.google.dev/gemini-api/docs/video-understanding))
6. **gitingest** — site + GitHub (LLM‑ready repo digests; private repo token notes). ([gitingest.com](https://gitingest.com/))
7. **Vertex AI — Video understanding** (Gemini video in Vertex). ([Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding))
8. **MCP explainer (alt framing & analogy)** — helpful context; optional. ([OpenAI GitHub](https://openai.github.io/openai-agents-python/mcp/))
9. **Background news on MCP** (industry adoption context). ([The Verge](https://www.theverge.com/2024/11/25/24305774/anthropic-model-context-protocol-data-sources))