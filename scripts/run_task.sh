#!/usr/bin/env bash
set -euo pipefail

TASK=${1?"task id required"}

# 1) render prompts from plan.yaml and task_template.txt
# 2) call agent (external orchestrator) with rendered prompts
# 3) on success, run scripts/verify.sh and update progress.json

