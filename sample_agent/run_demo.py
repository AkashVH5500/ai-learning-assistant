# run_demo.py - quick local demo script: ingest a PDF (if provided) and run a sample flow
import os, sys
from sample_agent.tools.researcher import ResearcherAgent
from sample_agent.tools.summarizer import SummarizerAgent
from sample_agent.tools.quiz_generator import QuizAgent

r = ResearcherAgent()
s = SummarizerAgent()
q = QuizAgent()

# optional: pass a PDF path as first arg to ingest
if len(sys.argv) > 1:
    pdf = sys.argv[1]
    print('Ingesting', pdf)
    r.ingest_pdf(pdf, doc_id='manual_demo')
    print('Ingested. Running search...')
docs = r.search('gradient descent', top_k=3)
print('Found', len(docs), 'docs. First snippet:\n', docs[0]['text'][:400] if docs else 'no docs')
summary = s.summarize(docs, level='beginner') if docs else {'text':'no docs'}
print('\nSummary (truncated):\n', summary['text'][:500])
quiz = q.generate_quiz('gradient descent', n=3)
print('\nSample quiz:', quiz)
