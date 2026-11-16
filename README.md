# AI Personal Learning Assistant

A Python capstone prototype exploring a structured learning workflow with planner, researcher, summariser and quiz-generator components. The repository includes PDF ingestion, sentence-transformer embeddings, optional FAISS search, session storage, optional Google Cloud Storage-backed memory and a Vertex AI Agent Engine deployment configuration.

## Current implementation status

This repository is a prototype, not a production-ready or fully LLM-driven tutor. The implementation should be described accurately:

- **Planner:** rule-based workflow selection based on the requested mode.
- **Researcher:** can ingest PDF text, split it into chunks, create sentence-transformer embeddings and retrieve relevant chunks. FAISS is used when installed; a NumPy similarity fallback is available.
- **Summariser:** currently returns an extractive slice of retrieved text; it does not call an LLM.
- **Quiz generator:** currently uses question templates and placeholder answer choices; it is not a validated knowledge-assessment system.
- **Answer action:** currently returns a placeholder response rather than a generated LLM answer.
- **Session and memory:** session data is stored under /tmp; the MemoryBank can use Google Cloud Storage when configured and otherwise falls back to local files.
- **Cloud deployment:** an Agent Engine configuration and deployment script are included. Validate the configuration and runtime behaviour in your own Google Cloud project before claiming a live production deployment.

## Project structure

~~~text
ai-learning-assistant/
├── demo/
│   └── DEMO_INSTRUCTIONS.md
├── sample_agent/
│   ├── agent_engine_app.py
│   ├── deploy.sh
│   ├── .agent_engine_config.json
│   ├── .env.example
│   ├── requirements.txt
│   ├── run_demo.py
│   ├── memory/
│   ├── tools/
│   └── utils/
├── README.md
└── .gitignore
~~~

## Local setup

Use Python 3.10 or later.

~~~bash
git clone https://github.com/AkashVH5500/ai-learning-assistant.git
cd ai-learning-assistant

python -m venv .venv
~~~

Activate the environment:

- macOS / Linux: source .venv/bin/activate
- Windows PowerShell: .venv\Scripts\Activate.ps1

Install the project dependencies:

~~~bash
python -m pip install --upgrade pip
pip install -r sample_agent/requirements.txt
~~~

## Run the PDF retrieval demo

The demo can run without Google Cloud credentials. To test PDF ingestion, pass a local PDF path:

~~~bash
python -m sample_agent.run_demo path/to/document.pdf
~~~

Without a PDF argument, the researcher starts with an empty in-memory document collection and reports that no documents are available.

## Optional Google Cloud configuration

Copy the example file and replace the placeholders with your own project settings:

~~~bash
cp sample_agent/.env.example sample_agent/.env
~~~

For a Bash shell, load these variables before running deployment commands:

~~~bash
set -a
source sample_agent/.env
set +a
~~~

Authenticate using the Google Cloud CLI or another supported Application Default Credentials flow. Then run the deployment script from the repository root:

~~~bash
bash sample_agent/deploy.sh
~~~

The script expects PROJECT_ID and GOOGLE_CLOUD_LOCATION. The configured bucket is used by the optional GCS-backed MemoryBank. Do not commit .env or service-account credentials.

## Dependencies

The dependency list is maintained in sample_agent/requirements.txt and includes Google ADK deployment tooling, Vertex AI / Google Cloud Storage libraries, sentence-transformers, PDFMiner, NumPy, Pandas, scikit-learn, tqdm and FAISS CPU.

## Limitations and next steps

1. Replace the placeholder answer path with a real model-backed generation step and source-grounded response handling.
2. Replace extractive summarisation and template quiz generation with evaluated implementations.
3. Add automated tests for planner modes, PDF ingestion, retrieval, memory persistence and failure cases.
4. Add a small, redistributable sample document and clear retrieval-quality evaluation.
5. Verify Agent Engine deployment and document an actual, reproducible deployment result.

## Author

Akash V Hiremath — [GitHub](https://github.com/AkashVH5500)
