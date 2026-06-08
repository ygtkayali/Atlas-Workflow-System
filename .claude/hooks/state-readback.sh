#!/usr/bin/env bash
# Fires on: PostToolUse for Edit, Write, MultiEdit
# Purpose: after a write to workflow-state.json, read it back and surface the
#          active state as additionalContext so Claude sees what was persisted.

set -euo pipefail

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.filePath // ""')

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
STATE_FILE="$PROJECT_ROOT/.claude/workflow-state.json"

REL_PATH="${FILE_PATH#${PROJECT_ROOT}/}"

if [[ "$REL_PATH" != ".claude/workflow-state.json" ]]; then
  exit 0
fi

if [[ ! -f "$STATE_FILE" ]]; then
  echo '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"workflow-state.json was written but the file cannot be read back — verify the path is correct."}}'
  exit 0
fi

ACTIVE_SKILL=$(jq -r '.active_skill // "none"' "$STATE_FILE" 2>/dev/null || echo "PARSE_ERROR")
PHASE=$(jq -r '.phase // "none"' "$STATE_FILE" 2>/dev/null || echo "PARSE_ERROR")
GATE=$(jq -r '.gate_status // "none"' "$STATE_FILE" 2>/dev/null || echo "PARSE_ERROR")
SCOPE=$(jq -r '.approved_scope // [] | join(", ")' "$STATE_FILE" 2>/dev/null || echo "PARSE_ERROR")
VER_REQ=$(jq -r '.verification_required // false' "$STATE_FILE" 2>/dev/null || echo "PARSE_ERROR")
VER_DONE=$(jq -r '.verification_done // false' "$STATE_FILE" 2>/dev/null || echo "PARSE_ERROR")
SET_AT=$(jq -r '.state_set_at // "null"' "$STATE_FILE" 2>/dev/null || echo "PARSE_ERROR")

NEXT_ACTION=""
if [[ "$ACTIVE_SKILL" != "none" && "$ACTIVE_SKILL" != "PARSE_ERROR" ]]; then
  NEXT_ACTION=" REQUIRED: active_skill is '${ACTIVE_SKILL}' — invoke the Skill tool with skill='${ACTIVE_SKILL}' before writing any files."
fi

TIMESTAMP_WARN=""
if [[ "$ACTIVE_SKILL" != "none" && "$SET_AT" == "null" ]]; then
  TIMESTAMP_WARN=" WARNING: state_set_at is null — add an ISO-8601 UTC timestamp so session-start.sh can detect stale state."
fi

MSG="workflow-state.json readback — active_skill: ${ACTIVE_SKILL} | phase: ${PHASE} | gate_status: ${GATE} | approved_scope: [${SCOPE}] | verification_required: ${VER_REQ} | verification_done: ${VER_DONE} | state_set_at: ${SET_AT}.${NEXT_ACTION}${TIMESTAMP_WARN}"

echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PostToolUse\",\"additionalContext\":$(echo "$MSG" | jq -Rs .)}}"
