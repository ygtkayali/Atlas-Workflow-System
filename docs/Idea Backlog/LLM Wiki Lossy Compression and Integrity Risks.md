# LLM Wiki Lossy Compression and Integrity Risks

Status: [[Tags/status-draft]]
Type: [[idea-note]]
Related: [[Local Note Search Script]]
Created: 06-05-2026
Priority: [[docs/Tags/priority-high|priority-high]] 

---

## Idea

An LLM-generated wiki can be useful as a small, curated research aid, but it is not a neutral or lossless replacement for the original source material.

The core risk is that the wiki is derived knowledge. Raw documents are rewritten into pages, summaries, timelines, entity notes, and indexes. That transformation can drop caveats, dates, minority views, exact wording, edge cases, and source context.

Once users query the generated wiki instead of the original sources, summary errors and missing context can become part of the working knowledge base.

## Integrity Risks

- Derived pages may flatten source nuance into confident but incomplete claims.
- New source material can affect many existing pages at once, including entity pages, concept pages, timelines, summaries, and indexes.
- Update work becomes graph maintenance: changed claims, conflicts, duplicates, provenance, stale pages, and old page behavior all need to be managed explicitly.
- "Ask the LLM to maintain it" is not enough unless the system has validators, source hashes, span-level citations, regression tests, and human review.
- The wiki does not remove retrieval. At larger scale it still needs search, ranking, indexing, reranking, chunking, and access control.
- A markdown wiki at that point becomes another indexed corpus, not a replacement for RAG.

## Production Concerns

Any serious version of this system would need explicit handling for:

- permissions
- multi-user edits
- audit logs
- rollback
- deletion
- sensitive data
- source versioning
- concurrency
- compliance
- cost
- latency
- update frequency

These are not secondary polish details. They are common failure points for knowledge-base systems.

## Reasonable Claim

The narrower and more defensible claim is:

LLM-generated wiki workflows can be useful for small-to-medium, slow-moving, human-curated research folders.

They are much less convincing for large, fast-changing, high-stakes, multi-user, or enterprise knowledge bases unless the system is engineered around provenance, validation, review, retrieval, and operational controls.

## Questions

- What kinds of source material are safe to summarize into durable wiki-style notes?
- When should generated pages be treated as indexes or navigation aids rather than knowledge sources?
- What metadata is required to preserve source provenance, update state, and confidence?
- How should future workflow tooling prevent derived summaries from replacing source-grounded retrieval?
- What validators or review checks would be necessary before generated wiki content can influence implementation or planning?

## Use As Reference

Use this note as a cautionary reference when evaluating future development around:

- source-material processing
- generated wiki pages
- knowledge graph maintenance
- note promotion workflows
- retrieval versus summarization boundaries
- system integrity checks
- human review gates
