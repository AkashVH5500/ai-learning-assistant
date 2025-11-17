# Demo instructions (local & deployed)

## Local
1. Create virtual env and install deps:
   python3 -m venv venv && source venv/bin/activate
   pip install -r sample_agent/requirements.txt
2. Set GOOGLE_APPLICATION_CREDENTIALS if using GCS integration.
3. Run a quick ingestion + search test:
   python -c "from sample_agent.tools.researcher import ResearcherAgent; r=ResearcherAgent(); r.ingest_pdf('path/to/lecture.pdf','lec1'); print(r.search('gradient descent',top_k=2)[0]['text'][:300])"

## Deployed (Agent Engine)
1. Deploy using deploy.sh (ensure env vars PROJECT_ID and deployed_region are exported)
2. After deploy, ADK prints an engine name. Use the agent engine client to call it (example code below).
3. Example call (Python, adapt to your ADK/vertexai version):
   from vertexai import agent_engines
   client = agent_engines.AgentEnginesClient()
   engine_name = 'projects/PROJECT_NUM/locations/europe-west4/reasoningEngines/ENGINE_ID'
   agent_engine = client.get(name=engine_name)
   resp = agent_engine.run({'user_id':'akash','prompt':'Explain overfitting like I am 12','mode':'ask'})
   print(resp)
