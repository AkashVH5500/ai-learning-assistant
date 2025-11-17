# planner.py - creates a simple sequential plan based on prompt and mode
class PlannerAgent:
    def __init__(self): pass

    def plan(self, prompt: str, mode: str='ask', session: dict=None):
        """Return a list of steps. Each step is a dict with 'action' and params."""
        steps = []
        if mode == 'quiz':
            steps.append({'action':'research', 'query': prompt})
            steps.append({'action':'quiz', 'query': prompt, 'n':5})
        elif mode == 'summarize':
            steps.append({'action':'research', 'query': prompt})
            steps.append({'action':'summarize', 'query': prompt, 'level':'medium'})
        else: # default ask
            steps.append({'action':'research', 'query': prompt})
            steps.append({'action':'answer', 'query': prompt})
        return steps
