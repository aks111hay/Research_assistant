from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from agents.processing_agent import extract_text_from_pdf, extract_text_from_url
from agents.topic_classifier import classify_paper
from agents.summarizer_agent import summarize  # now uses DeepSeek under the hood
from agents.podcast_agent import generate_audio
from agents.search_agent import search_arxiv
from agents.synthesis_agent import synthesize
import os

app = FastAPI()

# CORS (allow frontend to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
AUDIO_DIR = "audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

class ClassificationRequest(BaseModel):
    filename: str
    topics: List[str]

@app.post("/upload/")
async def upload_paper(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return {"message": "File uploaded", "filename": file.filename}

@app.post("/classify/")
def classify(data: ClassificationRequest):
    path = os.path.join(UPLOAD_DIR, data.filename)
    text = extract_text_from_pdf(path)
    topic = classify_paper(text, data.topics)
    return {"topic": topic}

@app.post("/summarize/")
def summarize_text(filename: str):
    path = os.path.join(UPLOAD_DIR, filename)
    text = extract_text_from_pdf(path)
    if len(text) > 1000:
        text = text[:1000]

    try:
        summary = summarize(text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/audio/")
def generate_audio_summary(filename: str):
    path = os.path.join(UPLOAD_DIR, filename)
    text = extract_text_from_pdf(path)
    summary = summarize(text)
    audio_path = os.path.join(AUDIO_DIR, f"{filename}.mp3")
    generate_audio(summary, audio_path)
    return {"message": "Audio generated", "audio_file": audio_path}

@app.get("/search/")
def search(query: str = "machine learning", max_results: int = 5):
    return search_arxiv(query, max_results)

@app.post("/process/url/")
def process_url(url: str):
    text = extract_text_from_url(url)
    return {"text": text[:500]}

from pydantic import BaseModel
from typing import List

class SynthesisRequest(BaseModel):
    summaries: List[str]

@app.post("/synthesize/")
def synthesize_route(request: SynthesisRequest):
    result = synthesize(request.summaries)
    return {"synthesis": result}


@app.get("/")
def root():
    return {"status": "OK", "message": "Backend is running"}

if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
