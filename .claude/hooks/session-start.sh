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
  TASK=$(jq -r '.active_task // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  GATE=$(jq -r '.gate_status // "none"' "$STATE_FILE" 2>/dev/null || echo "none")

  output+="## Active Workflow State"$'\n'
  output+="- Phase: ${PHASE}"$'\n'
  output+="- Active skill: ${SKILL}"$'\n'
  output+="- Active task: ${TASK}"$'\n'
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
