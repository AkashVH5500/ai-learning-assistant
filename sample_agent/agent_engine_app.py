# ADK entrypoint for Agent Engine (sample_agent/agent_engine_app.py)
import os, json, logging
from typing import Dict, Any

# local tools & memory
from sample_agent.tools.planner import PlannerAgent
from sample_agent.tools.researcher import ResearcherAgent
from sample_agent.tools.summarizer import SummarizerAgent
from sample_agent.tools.quiz_generator import QuizAgent
from sample_agent.memory.session import InMemorySessionService
from sample_agent.memory.memory_bank import MemoryBank
from sample_agent.utils.context_engineering import compact_context

# Setup logging (observability)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('agent_engine_app')

PROJECT_ID = os.environ.get('PROJECT_ID')
BUCKET = os.environ.get('BUCKET_NAME')

# instantiate agents/tools/services once per runtime
session_service = InMemorySessionService()
memory_bank = MemoryBank(bucket=BUCKET, project=PROJECT_ID)

planner = PlannerAgent()
researcher = ResearcherAgent(memory_bank=memory_bank)
summarizer = SummarizerAgent()
quiz_agent = QuizAgent(memory_bank=memory_bank)

def handle(request: Dict[str, Any]) -> Dict[str, Any]:
    """Main ADK handle entrypoint expected by ADK/Agent Engine.
    Request format:
      {"user_id": "...", "prompt": "...", "mode": "ask|quiz|summarize", ...}
    """
    user_id = request.get('user_id', 'anon')
    prompt = request.get('prompt', '')
    mode = request.get('mode', 'ask')

    logger.info('Handling request user=%s mode=%s', user_id, mode)

    # load session state
    session = session_service.load(user_id)

    # Planner decides the flow (sequential agents)
    plan = planner.plan(prompt, mode=mode, session=session)
    logger.info('Planner produced plan: %s', plan)

    result = None
    # Sequential execution of plan steps
    for step in plan:
        if step['action'] == 'research':
            docs = researcher.search(step.get('query', prompt), top_k=5)
            logger.info('Researcher returned %d docs', len(docs))
            session_service.append_conversation(user_id, f"Research: {step.get('query')}", f"Found {len(docs)} docs")
            # compact context for downstream
            compacted = compact_context(docs, max_tokens=1500)
            session['last_context'] = compacted
        elif step['action'] == 'summarize':
            ctx = session.get('last_context', [])
            summary = summarizer.summarize(ctx, level=step.get('level','medium'))
            session_service.append_conversation(user_id, f"Summarize: {step.get('query')}", summary.get('text'))
            result = {'type':'summary', 'payload': summary}
        elif step['action'] == 'quiz':
            quiz = quiz_agent.generate_quiz(step.get('query', prompt), n=step.get('n',5))
            session_service.save(user_id, {'last_quiz': quiz})
            result = {'type':'quiz', 'payload': quiz}
        elif step['action'] == 'answer':
            # default LLM-backed answer: use researcher docs + memory to compose answer
            ctx = session.get('last_context', [])
            # here you'd call ADK/vertex LLM with contexts; we include a placeholder response
            answer_text = f"(LLM answer stub) Based on {len(ctx)} context chunks, answer to: {prompt[:200]}"
            session_service.append_conversation(user_id, prompt, answer_text)
            result = {'type':'answer', 'payload': {'text': answer_text, 'sources':[d.get('meta') for d in ctx]}}
        # loop agent behavior: if result doesn't meet quality, planner may include retries (handled by planner)
    # persist session
    session_service.save(user_id, session)
    logger.info('Finished handling for user=%s', user_id)
    return result or {'text': 'No action taken'}
