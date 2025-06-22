# import os
# import requests

# OPENROUTER_API_KEY = '' # or paste directly

# def summarize(text: str) -> str:
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "model": "deepseek/deepseek-r1-0528",
#         "messages": [
#             {"role": "system", "content": "You are an academic summarization assistant. Summarize long research papers in detail."},
#             {"role": "user", "content": f"Summarize the following research paper:\n\n{text}"}
#         ]
#     }

#     response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

#     if response.status_code == 200:
#         return response.json()['choices'][0]['message']['content']
#     else:
#         raise Exception(f"DeepSeek failed: {response.status_code} - {response.text}")

from transformers import pipeline

summarizer = pipeline("summarization",model="facebook/bart-large-cnn")
def summarize(text, max_len=12000):
    if len(text) > 1000:
        text = text[:1000]  # trim long input
    summary = summarizer(text, max_length=max_len, min_length=30, do_sample=False)
    return summary[0]['summary_text']