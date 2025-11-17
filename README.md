# AI Personal Learning Assistant (Advanced Capstone)

This repository contains an advanced multi-agent AI Personal Learning Assistant built for the Kaggle + Google ADK capstone.

Highlights:
- Sequential + Loop agents (Planner -> Researcher -> Summarizer -> QuizGenerator)
- Custom tools: search_notes, summarize, quiz_generator
- Sessions (InMemorySessionService) and Long-term Memory (MemoryBank using GCS)
- Context engineering utilities (compaction)
- Observability/logging
- ADK + Vertex AI Agent Engine deployment configuration (agent_engine_config.json)

See `sample_agent/` for the ADK-ready agent app and `demo/` for runnable demo scripts and instructions.
