#!/usr/bin/env bash
set -e
if [ -z "$PROJECT_ID" ]; then echo "Please set PROJECT_ID"; exit 1; fi
if [ -z "$deployed_region" ]; then echo "Please set deployed_region"; exit 1; fi
adk deploy agent_engine --project=$PROJECT_ID --region=$deployed_region sample_agent --agent_engine_config_file=sample_agent/.agent_engine_config.json
