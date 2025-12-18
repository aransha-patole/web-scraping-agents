import requests
from bs4 import BeautifulSoup

def scrape_static(url: str) -> list[str]:
    headers = {"User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"}
    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")
    # Example selector - change per target site
    return [x.get_text(strip=True) for x in soup.select("h1, h2")][:20]

if __name__ == "__main__":
    print(scrape_static("https://example.com"))
