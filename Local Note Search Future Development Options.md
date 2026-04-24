# Local Note Search Future Development Options

Status: [[status-pending]]
Parent: [[Idea Hub]]
Related: [[Local Note Search Script]]
Created: 18-04-2026

---

## Summary

Preserve future development options for the local note search tool without expanding the initial version beyond its current scope.

## Future Directions

- use semantic or content-related tags when the vault has mature tagging
- distinguish operational tags from semantic tags before any tag-based retrieval is enabled
- add a strict mode alongside expanded mode after initial evaluation
- add BM25-based retrieval for text-heavy vaults
- add semantic / embedding-based retrieval for broader context matching
- add richer ranking explanations for debugging and trust

## Vault-Type Considerations

A knowledge base may benefit more from semantic tags and hybrid retrieval.

A technical project vault may rely more on explicit links, bounded graph traversal, and conservative expansion.

Future retrieval behavior may need to depend on vault maturity rather than one fixed rule.

## Questions To Revisit

- How should a vault declare which tags are semantic enough to use for retrieval?
- When should tag-based expansion be enabled instead of remaining off?
- What evaluation method should compare retrieval quality across different vault types?
- When does result explanation become necessary for agent debugging and review?
