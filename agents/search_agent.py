import requests
from bs4 import BeautifulSoup

def search_arxiv(query="machine learning", max_results=5):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    response = requests.get(url)
    entries = []
    if response.ok:
        soup = BeautifulSoup(response.content, 'xml')
        for entry in soup.find_all('entry'):
            entries.append({
                "title": entry.title.text.strip(),
                "url": entry.id.text,
                "summary": entry.summary.text.strip(),
                "published": entry.published.text
            })
    return entries
