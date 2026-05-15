#!/usr/bin/env bash
# Fires on: PreToolUse for Edit, Write, MultiEdit
# Purpose: gate durable note mutations and implementation writes

set -euo pipefail

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.filePath // ""')

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
STATE_FILE="$PROJECT_ROOT/.claude/workflow-state.json"

# Strip PROJECT_ROOT prefix so all pattern checks work on relative paths
# (Edit/Write tools pass absolute paths; all guards below use ^-anchored relative patterns)
REL_PATH="${FILE_PATH#${PROJECT_ROOT}/}"

# Durable note mutation gate
# Block writes to docs/ unless active skill is dw-note-manager
# Exception: docs/In-flight/ is always writable
if echo "$REL_PATH" | grep -qE '^docs/' && ! echo "$REL_PATH" | grep -qE '^docs/In-flight/'; then
  ACTIVE_SKILL="none"
  if [[ -f "$STATE_FILE" ]]; then
    ACTIVE_SKILL=$(jq -r '.active_skill // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  fi

  if [[ "$ACTIVE_SKILL" != "dw-note-manager" ]]; then
    echo "BLOCKED: Write to durable note path (${FILE_PATH}) outside dw-note-manager." >&2
    echo "Durable note mutations must route through dw-note-manager skill." >&2
    echo "Update .claude/workflow-state.json or route through the correct skill." >&2
    exit 2
  fi
fi

# Implementation approval gate
if echo "$REL_PATH" | grep -qE '\.(ts|tsx|js|jsx|py|go|rs|java|rb|css|scss|html|sql)$'; then
  GATE="none"
  SKILL="none"
  SCOPE=""

  if [[ -f "$STATE_FILE" ]]; then
    GATE=$(jq -r '.gate_status // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
    SKILL=$(jq -r '.active_skill // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
    SCOPE=$(jq -r '.approved_scope // [] | join(",")' "$STATE_FILE" 2>/dev/null || echo "")
  fi

  if [[ "$GATE" == "approved" && "$SKILL" == "project-implementer" ]]; then
    if [[ -n "$SCOPE" ]]; then
      IN_SCOPE=false
      IFS=',' read -ra SCOPE_PATHS <<< "$SCOPE"
      for sp in "${SCOPE_PATHS[@]}"; do
        if echo "$REL_PATH" | grep -q "^${sp}"; then
          IN_SCOPE=true
          break
        fi
      done
      if [[ "$IN_SCOPE" == "false" ]]; then
        echo "BLOCKED: File ${FILE_PATH} is outside approved scope (${SCOPE})." >&2
        echo "Only files within the approved scope can be modified." >&2
        exit 2
      fi
    fi
    exit 0
  fi

  if [[ ! -f "$STATE_FILE" ]]; then
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","additionalContext":"No workflow state file found. If this is an implementation task, create .claude/workflow-state.json with gate_status: approved before proceeding."}}'
    exit 0
  fi

  if [[ "$GATE" != "approved" ]]; then
    echo "BLOCKED: Implementation gate not approved (current: ${GATE})." >&2
    echo "Run through project-planner and get approval before coding." >&2
    exit 2
  fi
fi

exit 0
