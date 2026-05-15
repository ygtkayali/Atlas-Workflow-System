#!/usr/bin/env bash
# Fires on: SessionStart, resume, clear, compact
# Purpose: inject workflow state + scoped context

set -euo pipefail

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
STATE_FILE="$PROJECT_ROOT/.claude/workflow-state.json"

output=""

if [[ -f "$STATE_FILE" ]]; then
  PHASE=$(jq -r '.phase // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  SKILL=$(jq -r '.active_skill // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  GATE=$(jq -r '.gate_status // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  STATE_SET_AT=$(jq -r '.state_set_at // ""' "$STATE_FILE" 2>/dev/null || echo "")

  output+="## Active Workflow State"$'\n'

  # Staleness check: non-default state that survived a session boundary is dangerous
  # (gate_status: approved + active_skill: project-implementer = write guard bypassed)
  if [[ "$PHASE" != "none" || "$SKILL" != "none" || "$GATE" != "none" ]]; then
    NOW=$(date +%s)
    if [[ -n "$STATE_SET_AT" ]]; then
      MTIME=$(date -d "$STATE_SET_AT" +%s 2>/dev/null || echo "0")
      AGE_LABEL="$STATE_SET_AT"
    else
      MTIME=$(stat -c %Y "$STATE_FILE" 2>/dev/null || echo "0")
      AGE_LABEL="unknown (file mtime used)"
    fi
    AGE_H=$(( (NOW - MTIME) / 3600 ))

    if [[ "$AGE_H" -ge 4 ]]; then
      output+="WARNING: Non-default workflow state is ${AGE_H}h old — likely stale from a previous session."$'\n'
      output+="If stale, reset before acting: jq -n '{\"phase\":\"none\",\"active_skill\":\"none\",\"gate_status\":\"none\",\"approved_scope\":[],\"verification_required\":false,\"verification_done\":false,\"state_set_at\":null}' > \"${STATE_FILE}\""$'\n'
    fi
    output+="- State age: ${AGE_LABEL} (${AGE_H}h ago)"$'\n'
  fi

  output+="- Phase: ${PHASE}"$'\n'
  output+="- Active skill: ${SKILL}"$'\n'
  output+="- Gate status: ${GATE}"$'\n'$'\n'
fi

output+="## Git Context"$'\n'
output+="- Branch: $(git branch --show-current 2>/dev/null || echo 'unknown')"$'\n'
DIRTY=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
output+="- Uncommitted changes: ${DIRTY} files"$'\n'$'\n'

INFLIGHT_DIR="$PROJECT_ROOT/docs/In-flight"
if [[ -d "$INFLIGHT_DIR" ]]; then
  output+="## Active In-Flight Artifacts"$'\n'
  while IFS= read -r line; do
    output+="$line"$'\n'
  done < <(find "$INFLIGHT_DIR" -maxdepth 2 -name '*.md' -printf '- %P\n' 2>/dev/null | head -20)
  output+=$'\n'
fi

output+="## Entry Points"$'\n'
output+="- Project structure: context-map.md"$'\n'
output+="- Active work: docs/In-flight/"$'\n'
output+="- Routing: AGENTS.md"$'\n'
output+="- Config: atlas.yaml"$'\n'

echo "{\"additionalContext\": $(echo "$output" | jq -Rsa .)}"
