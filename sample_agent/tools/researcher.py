# researcher.py - searches ingested docs using embeddings + vector store
import os, numpy as np, logging
from sentence_transformers import SentenceTransformer
try:
    import faiss
    HAS_FAISS = True
except Exception:
    HAS_FAISS = False
from pdfminer.high_level import extract_text

logger = logging.getLogger('researcher')
EMBED_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'

class ResearcherAgent:
    def __init__(self, memory_bank=None):
        self.model = SentenceTransformer(EMBED_MODEL)
        self.docs = []  # each: {'id','text','meta'}
        self.embeddings = None
        self.index = None
        self.memory_bank = memory_bank

    def ingest_pdf(self, file_path, doc_id=None):
        text = extract_text(file_path)
        chunks = self._chunk_text(text)
        for i,ch in enumerate(chunks):
            self.docs.append({'id': f"{doc_id or file_path}_{i}", 'text': ch, 'meta': {'source': file_path}})
        self._build_index()

    def _chunk_text(self, text, chunk_size=800):
        words = text.split()
        chunks = [ ' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size) ]
        return chunks

    def _build_index(self):
        if not self.docs: return
        texts = [d['text'] for d in self.docs]
        embs = self.model.encode(texts, convert_to_numpy=True)
        self.embeddings = embs
        if HAS_FAISS:
            dim = embs.shape[1]
            self.index = faiss.IndexFlatL2(dim)
            self.index.add(embs)
        else:
            self.index = None

    def search(self, query, top_k=5):
        if not self.docs: return []
        q_emb = self.model.encode([query], convert_to_numpy=True)
        if self.index is not None:
            D,I = self.index.search(q_emb, top_k)
            idxs = I[0].tolist()
        else:
            sims = (self.embeddings @ q_emb[0])
            idxs = list(np.argsort(-sims)[:top_k])
        return [ self.docs[i] for i in idxs ]
