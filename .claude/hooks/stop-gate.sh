#!/usr/bin/env bash
# Fires on: Stop (when Claude ends its turn)
# Purpose: block completion if verification wasn't done, block auto-chaining of gated phases

set -euo pipefail

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
STATE_FILE="$PROJECT_ROOT/.claude/workflow-state.json"

if [[ ! -f "$STATE_FILE" ]]; then
  exit 0
fi

PHASE=$(jq -r '.phase // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
VERIFICATION_REQUIRED=$(jq -r '.verification_required // false' "$STATE_FILE" 2>/dev/null || echo "false")
VERIFICATION_DONE=$(jq -r '.verification_done // false' "$STATE_FILE" 2>/dev/null || echo "false")

# Verification gate
if [[ "$PHASE" == "implementation" && "$VERIFICATION_REQUIRED" == "true" && "$VERIFICATION_DONE" != "true" ]]; then
  echo "BLOCKED: Implementation phase requires verification before completion." >&2
  echo "Run tests, lint, typecheck, or build checks, then set verification_done: true in workflow-state.json." >&2
  exit 2
fi

# Phase transition gate for review-sync
if [[ "$PHASE" == "review-sync" ]]; then
  SUBPHASE=$(jq -r '.review_subphase // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  if [[ "$SUBPHASE" != "complete" ]]; then
    echo "BLOCKED: Review-sync phases are gated." >&2
    echo "Current subphase: ${SUBPHASE}. Each subphase must be proposed and approved separately." >&2
    exit 2
  fi
fi

exit 0
