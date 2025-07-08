### Candidate Web-Search Queries

1. What are structured outputs in the context of large language models, and why are they considered essential for building reliable, type-safe AI agents?
Reason: Provides theoretical and industry perspectives (academic papers, engineering blogs, API docs) to support Section 1’s argument that agents need structured outputs for reliability, validation, and downstream processing.

2. What prompt-engineering techniques and example templates successfully force models like GPT-4 or Claude to emit strict JSON (or other schema-bound) responses?
Reason: Supplies concrete, authoritative best-practice sources to cite in Section 2 when explaining how to coerce raw LLMs into JSON through prompt design.

3. How is Python’s Pydantic library used to parse, validate, and type-check data returned by LLMs, and why is it favored over plain dictionaries?
Reason: Backs Section 3 with documentation, tutorials, and case studies illustrating Pydantic’s role as the “bridge” between LLM outputs and Python code.

4. What are the comparative advantages and token-cost implications of JSON versus YAML versus XML when serializing LLM outputs?
Reason: Offers data or expert analysis to strengthen Section 2’s side note on choosing lighter formats (YAML/XML) to reduce token usage while maintaining structure.

5. In what ways does the Google Gemini API enable structured output (e.g., JSON mode, function calling) and how can it be integrated with Pydantic in Python?
Reason: Provides official docs or blog posts necessary for Section 4’s walkthrough on leveraging Gemini’s built-in structured output capabilities with Pydantic.

