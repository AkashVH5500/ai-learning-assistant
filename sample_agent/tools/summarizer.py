# summarizer.py - simple summarizer that stitches context; in production call an LLM
def chunk_texts_to_summary(contexts, max_chars=2000):
    combined = '\n\n'.join([c['text'] for c in contexts])
    # Very simple extractive-style summary (first N characters)
    return combined[:max_chars]

class SummarizerAgent:
    def __init__(self): pass

    def summarize(self, contexts, level='medium'):
        text = chunk_texts_to_summary(contexts)
        # create basic "sources" list
        sources = list({c.get('meta',{}).get('source') for c in contexts if c.get('meta')})
        return {'text': text, 'sources': sources}
