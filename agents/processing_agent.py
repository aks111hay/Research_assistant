import fitz  # PyMuPDF
import requests
from bs4 import BeautifulSoup

import tempfile


def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_url(url):
    # Download the PDF
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to download PDF: {response.status_code}")

    # Save it to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(response.content)
        tmp_path = tmp_file.name

    # Extract text using PyMuPDF
    text = ""
    with fitz.open(tmp_path) as doc:
        for page in doc:
            text += page.get_text()

    return text
