# MemoryBank - long-term memory backed by GCS (if configured). Falls back to local files.
import os, json
try:
    from google.cloud import storage
    HAS_GCS = True
except Exception:
    HAS_GCS = False

class MemoryBank:
    def __init__(self, bucket=None, project=None):
        self.bucket = bucket or os.environ.get('BUCKET_NAME')
        self.project = project or os.environ.get('PROJECT_ID')
        self._local = '/tmp/pla_memory'
        os.makedirs(self._local, exist_ok=True)
        if HAS_GCS and self.bucket:
            self.client = storage.Client(project=self.project)
            self.bucket_obj = self.client.bucket(self.bucket)
        else:
            self.client = None

    def _key(self, user_id): return f'pla_memory/{user_id}.json'
    def load(self, user_id):
        if self.client and self.bucket_obj:
            blob = self.bucket_obj.blob(self._key(user_id))
            if not blob.exists(): return {}
            return json.loads(blob.download_as_text())
        p = os.path.join(self._local, f"{user_id}.json")
        if not os.path.exists(p): return {}
        with open(p,'r') as f: return json.load(f)
    def save(self, user_id, data):
        if self.client and self.bucket_obj:
            blob = self.bucket_obj.blob(self._key(user_id))
            blob.upload_from_string(json.dumps(data))
            return
        p = os.path.join(self._local, f"{user_id}.json")
        with open(p,'w') as f: json.dump(data, f)
