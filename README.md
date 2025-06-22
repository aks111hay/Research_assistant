# 🧠 Research Paper Summarization API

This is a modular FastAPI-based multi-agent backend system that allows users to:
- Upload academic PDFs
- Classify them by topic
- Generate human-like summaries
- Synthesize across papers
- Convert summaries into podcast audio
- Search academic databases like arXiv

---

## 📦 Features

| Feature               | Description                              |
|----------------------|------------------------------------------|
| PDF Upload           | Accept academic paper files              |
| Text Extraction      | Extract text from PDF or URL             |
| Topic Classification | Jina embeddings-based similarity check   |
| Summarization        | Uses HuggingFace DistilBART              |
| Audio Podcast        | Converts summary to .mp3 using gTTS      |
| Paper Search         | Pulls research papers from arXiv API     |
| Synthesis            | Summarizes multiple papers at once       |

---

## 🚀 Setup Instructions

```bash
# Step 1: Clone and install
pip install -r requierments.txt

# Step 2: Run the API
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI

---

## 📁 Folder Structure

```
.
├── main.py                  # FastAPI app
├── requirements.txt         # Dependencies
├── agents/                  # Agent modules
│   ├── processing_agent.py
│   ├── topic_classifier.py
│   ├── summarizer_agent.py
│   ├── podcast_agent.py
│   ├── search_agent.py
│   └── synthesis_agent.py
├── uploads/                 # Uploaded PDFs
├── audio/                   # Podcast output
```

---

## 🧠 Multi-Agent Overview

| Agent              | Role                                  |
|-------------------|----------------------------------------|
| `processing_agent`| Extract text from PDF or URL           |
| `topic_classifier`| Use Jina AI embeddings for classification |
| `summarizer_agent`| Generate summaries using DistilBART    |
| `podcast_agent`   | Convert text to audio                  |
| `search_agent`    | Search papers using arXiv API          |
| `synthesis_agent` | Combine and summarize multiple papers  |

---

## 📡 API Endpoints

### `/upload/` → Upload a PDF
### `/classify/` → Classify uploaded paper into topic
```json
{
  "filename": "example.pdf",
  "topics": ["NLP", "Quantum Computing"]
}
```

### `/summarize/` → Summarize a single paper
### `/audio/` → Generate audio from summary
### `/search/` → Search arXiv for papers
### `/process/url/` → Get text from online URL
### `/synthesize/` → Summarize multiple papers together

---

