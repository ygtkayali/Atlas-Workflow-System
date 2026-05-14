#!/usr/bin/env bash
# Fires on: PreToolUse for Bash
# Purpose: block destructive git ops, prevent broad scanning, enforce git-add hygiene

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

# Destructive git commands
if echo "$COMMAND" | grep -qE 'git\s+(push\s+.*--force|reset\s+--hard|rebase|commit\s+.*--amend|checkout\s+--\s+\.|clean\s+-fd)'; then
  echo "BLOCKED: Destructive git command detected." >&2
  echo "These require explicit human approval. Ask the user first." >&2
  exit 2
fi

# Blanket git add
if echo "$COMMAND" | grep -qE 'git\s+add\s+(-A|--all|\.\s*$)'; then
  echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Blanket git add detected. Workflow requires staging only task-related files. Confirm this is intentional."}}'
  exit 0
fi

# Inject git status before any commit
if echo "$COMMAND" | grep -qE 'git\s+commit'; then
  # If chained with git add, run the add portion first to get accurate staged state
  if echo "$COMMAND" | grep -qE 'git\s+add'; then
    ADD_CMD=$(echo "$COMMAND" | sed 's/ &&.*$//')
    eval "$ADD_CMD" 2>/dev/null || true
    GIT_STATUS=$(git status --porcelain 2>/dev/null | head -20)
    STAGED=$(git diff --cached --stat 2>/dev/null)
    git reset HEAD 2>/dev/null || true
  else
    GIT_STATUS=$(git status --porcelain 2>/dev/null | head -20)
    STAGED=$(git diff --cached --stat 2>/dev/null)
  fi
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"additionalContext\":\"Git status before commit:\n${GIT_STATUS}\n\nStaged changes:\n${STAGED}\"}}"
  exit 0
fi

exit 0
