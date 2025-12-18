import random
import time
import requests
from tenacity import retry, stop_after_attempt, wait_exponential_jitter

@retry(stop=stop_after_attempt(5), wait=wait_exponential_jitter(initial=2, max=30))
def polite_get(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"}
    r = requests.get(url, headers=headers, timeout=30)

    # Handle common throttling signals
    if r.status_code in (429, 503):
        raise RuntimeError(f"Throttled: {r.status_code}")

    r.raise_for_status()

    # Small random delay to reduce burstiness
    time.sleep(random.uniform(1.0, 3.0))
    return r.text

if __name__ == "__main__":
    print(polite_get("https://example.com")[:200])
