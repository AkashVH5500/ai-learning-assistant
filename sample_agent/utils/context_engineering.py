# context_engineering.py - simple context compaction utilities
def compact_context(docs, max_tokens=1000):
    # very simple compaction: keep top docs until approx token/char limit
    kept = []
    total = 0
    for d in docs:
        l = len(d.get('text',''))
        if total + l > max_tokens and kept:
            break
        kept.append(d)
        total += l
    return kept
