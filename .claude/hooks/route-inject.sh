#!/usr/bin/env bash
# Fires on: UserPromptSubmit (every user message)
# Purpose: re-inject routing table + active skill into fresh context on every turn

set -euo pipefail

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
STATE_FILE="$PROJECT_ROOT/.claude/workflow-state.json"

output=""

if [[ -f "$STATE_FILE" ]]; then
  SKILL=$(jq -r '.active_skill // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  PHASE=$(jq -r '.phase // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  GATE=$(jq -r '.gate_status // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  TASK=$(jq -r '.active_task // "none"' "$STATE_FILE" 2>/dev/null || echo "none")

  if [[ "$SKILL" != "none" ]]; then
    output+="ACTIVE SKILL: ${SKILL} | Phase: ${PHASE} | Gate: ${GATE}"$'\n'
    output+="Active task: ${TASK}"$'\n'
    output+="Do not switch skills without explicit handoff or user direction."$'\n'$'\n'
  fi
fi

output+="SKILL ROUTER:"$'\n'
output+="- Ambiguous/early-stage/solution-led → dw-clarify-intent"$'\n'
output+="- Note CRUD/metadata/governance → dw-note-manager"$'\n'
output+="- Implementation planning → project-planner"$'\n'
output+="- Approved packet or clear coding → project-implementer"$'\n'
output+="- Verification before closeout → implementation-verifier"$'\n'
output+="- Review/sync/maintenance → project-review-sync"$'\n'
output+="- Note retrieval (any phase) → note-search"$'\n'$'\n'

output+="ROUTING CONSTRAINTS:"$'\n'
output+="- Directive phrasing alone does not skip dw-clarify-intent."$'\n'
output+="- dw-clarify-intent output must be explicit handoff, not implicit continuation."$'\n'
output+="- Durable note mutations route through dw-note-manager only."$'\n'
output+="- Choose smallest valid skill sequence. Stop at first unresolved gate."$'\n'
output+="- If confidence is insufficient to choose skill safely, route to dw-clarify-intent."$'\n'
output+="- Note discovery (type lookup, exemplar finding, existence check, concept search) → note-search, not ls/grep on docs/."$'\n'
output+="- ls and grep on docs/ are only acceptable for exact-string matches, filename checks, or implementation code — not note discovery."$'\n'

echo "{\"additionalContext\": $(echo "$output" | jq -Rsa .)}"
