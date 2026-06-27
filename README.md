# 🤖 AI Personal Learning Assistant

An advanced **multi-agent AI Learning Assistant** developed as the **Google ADK + Kaggle AI Agents Capstone Project**. The system leverages multiple AI agents working collaboratively to help users learn topics efficiently by generating study plans, researching content, summarizing information, and creating quizzes.

---

## 📖 Overview

The AI Personal Learning Assistant uses a **multi-agent architecture**, where each specialized agent performs a dedicated task in the learning workflow. The project demonstrates context engineering, memory management, agent orchestration, and deployment using **Google Agent Development Kit (ADK)** and **Vertex AI Agent Engine**.

---

## 🚀 Features

* 🤖 Multi-Agent AI Architecture
* 📚 Personalized Learning Assistance
* 📝 Automatic Study Plan Generation
* 🔍 Intelligent Research Agent
* 📄 AI-powered Summarization
* ❓ Quiz Generation
* 🧠 Long-term Memory Support
* 💬 Session Management
* 📊 Context Engineering & Compression
* ☁️ Vertex AI Agent Engine Deployment
* 📈 Logging and Observability

---

## 🏗️ Multi-Agent Workflow

```text
User Query
     │
     ▼
 Planner Agent
     │
     ▼
 Research Agent
     │
     ▼
 Summarizer Agent
     │
     ▼
 Quiz Generator Agent
     │
     ▼
 Final Learning Response
```

Each agent focuses on a single responsibility, making the system modular, scalable, and easier to extend.

---

## 🛠️ Technologies Used

* Python
* Google Agent Development Kit (ADK)
* Vertex AI
* Google Cloud Platform (GCP)
* Vertex AI Agent Engine
* Google Cloud Storage (GCS)
* Generative AI
* Multi-Agent Systems
* Context Engineering
* Logging & Observability

---

## 📂 Project Structure

```text
ai-learning-assistant/
│
├── demo/                        # Demo scripts
├── sample_agent/                # ADK-ready agent implementation
├── README.md
├── advanced_ai_learning_assistant.zip
```

---

## ⚙️ Core Components

### 🧠 Planner Agent

Creates a structured learning roadmap based on the user's topic.

### 🔍 Research Agent

Collects relevant educational information using available knowledge sources.

### 📄 Summarizer Agent

Condenses researched content into concise and easy-to-understand notes.

### ❓ Quiz Generator Agent

Creates quizzes to reinforce learning and assess understanding.

---

## 💾 Memory System

The project includes:

* Session Management using `InMemorySessionService`
* Long-term Memory using `MemoryBank`
* Google Cloud Storage (GCS) integration
* Context Compression for efficient conversations

---

## ▶️ Getting Started

### Clone the Repository

```bash
git clone https://github.com/AkashVH5500/ai-learning-assistant.git

cd ai-learning-assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Demo

```bash
python demo/main.py
```

or execute the sample agent according to the ADK setup instructions.

---

## 📈 Future Enhancements

* Voice-based Learning Assistant
* PDF & Document Learning
* Multi-language Support
* Personalized Learning Analytics
* Web Search Integration
* Learning Progress Dashboard
* Mobile Application
* Cloud Deployment

---

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Multi-Agent AI Systems
* Agent Orchestration
* Large Language Models (LLMs)
* Prompt Engineering
* Context Engineering
* Memory Management
* Google ADK
* Vertex AI Deployment
* Cloud-based AI Applications

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## 📄 License

This project is developed for educational and research purposes.

---

## 👨‍💻 Author

**Akash V Hiremath**

Computer Science Engineering Student | AI & Full Stack Developer

GitHub: https://github.com/AkashVH5500

---
