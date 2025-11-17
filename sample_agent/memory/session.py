# InMemorySessionService - stores short-term session state in /tmp for demo
import os, json
class InMemorySessionService:
    def __init__(self):
        self._dir = '/tmp/pla_sessions'
        os.makedirs(self._dir, exist_ok=True)
    def _path(self, user_id): return os.path.join(self._dir, f"{user_id}.json")
    def load(self, user_id):
        p = self._path(user_id)
        if not os.path.exists(p): return {}
        with open(p,'r') as f: return json.load(f)
    def save(self, user_id, data):
        p = self._path(user_id)
        with open(p,'w') as f: json.dump(data, f)
    def append_conversation(self, user_id, user_msg, assistant_msg):
        s = self.load(user_id) or {}
        conv = s.get('conversations', [])
        conv.append({'user': user_msg, 'assistant': assistant_msg})
        s['conversations'] = conv[-50:]
        self.save(user_id, s)
