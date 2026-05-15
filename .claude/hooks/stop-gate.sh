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
# Allow stop when: review is fully complete, or Claude has explicitly handed a proposal
# to the user (awaiting_approval). Block when any named subphase is still in progress —
# that means the skill abandoned work mid-subphase without surfacing a proposal.
if [[ "$PHASE" == "review-sync" ]]; then
  SUBPHASE=$(jq -r '.review_subphase // "none"' "$STATE_FILE" 2>/dev/null || echo "none")
  if [[ "$SUBPHASE" != "complete" && "$SUBPHASE" != "awaiting_approval" ]]; then
    echo "BLOCKED: Review-sync subphase '${SUBPHASE}' is still in progress." >&2
    echo "Before stopping, either set review_subphase: \"awaiting_approval\" (proposal shown, waiting for user)" >&2
    echo "or set review_subphase: \"complete\" (full review done)." >&2
    exit 2
  fi
fi

exit 0
