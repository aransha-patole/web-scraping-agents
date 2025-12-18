import requests

def debug_http(url: str):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0)"}
    r = requests.get(url, headers=headers, timeout=30, allow_redirects=True)

    print("URL:", r.url)
    print("Status:", r.status_code)
    print("Server:", r.headers.get("server"))
    print("Content-Type:", r.headers.get("content-type"))
    print("Set-Cookie:", r.headers.get("set-cookie"))
    print("Snippet:", r.text[:200])

if __name__ == "__main__":
    debug_http("https://example.com")
