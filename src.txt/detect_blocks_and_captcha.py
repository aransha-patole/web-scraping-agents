import re
import requests

CAPTCHA_HINTS = [
    r"captcha",
    r"are you human",
    r"verify you are a human",
    r"challenge-form",
    r"cloudflare",
]

def looks_like_captcha(html: str) -> bool:
    s = html.lower()
    return any(re.search(p, s) for p in CAPTCHA_HINTS)

def fetch_or_stop(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"}
    r = requests.get(url, headers=headers, timeout=30)

    if r.status_code in (403, 429):
        return {"ok": False, "reason": f"Blocked or rate-limited: {r.status_code}"}

    if looks_like_captcha(r.text):
        return {"ok": False, "reason": "CAPTCHA detected (stop & use permitted access route)"}

    return {"ok": True, "html_snippet": r.text[:200]}

if __name__ == "__main__":
    print(fetch_or_stop("https://example.com"))
