# Local Note Search Script

Status: draft
Parent: [[Idea Hub]]
Related:
Created: 14-04-2026

## Summary

Create a reusable local script that agents can call to retrieve candidate related notes without reading the entire vault. The first version should traverse the existing note graph and return note names. Shared metadata such as tags can also be used as a retrieval signal.

## Details

The script is intended to reduce the overhead of broad vault reads when an agent needs to situate a note within the surrounding note space.

Initial use case:
- call the script for a new note to find nearby candidate notes that may be relevant for linking

Secondary use case:
- rerun the script after substantial note changes when metadata or surrounding relationships may need review

V1 boundaries:
- local script
- reusable by agents
- graph traversal is the primary retrieval mechanism
- shared metadata such as tags may contribute candidate notes
- returns candidate note names only
- does not decide which links should actually be added
- does not modify notes automatically

Deferred work:
- BM25-based retrieval
- semantic / embedding-based retrieval
- richer ranking or explanation layers

The script should support the documentation-centered workflow by reducing unnecessary vault-wide reading while still giving agents enough nearby context to make linking decisions.

## Open Questions

- Should the V1 input be note path, note title, or both?
- Should graph traversal stop at direct neighbors or allow bounded multi-hop expansion?
- Should shared metadata be an expansion source, a scoring signal, or both?
- Will note names alone be enough for downstream agent use, or will paths be needed soon after V1?
