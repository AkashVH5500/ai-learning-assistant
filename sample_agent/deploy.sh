#!/usr/bin/env bash
set -euo pipefail

: "\${PROJECT_ID:?Set PROJECT_ID to your Google Cloud project ID}"
: "\${GOOGLE_CLOUD_LOCATION:?Set GOOGLE_CLOUD_LOCATION to your Agent Engine region}"

adk deploy agent_engine \
  --project="\${PROJECT_ID}" \
  --region="\${GOOGLE_CLOUD_LOCATION}" \
  sample_agent \
  --agent_engine_config_file=sample_agent/.agent_engine_config.json
