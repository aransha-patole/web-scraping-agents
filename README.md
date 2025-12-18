# web-scraping-agents
Web Scraping + Web Agents Workflow (HTTP • DOM • JS • Anti-bot).

This repository illustrates the process of downloading web data that cannot be easily accessed in ways that are covered by APIs, and records the fundamentals required to accomplish it safely and responsibly.

Scraping: When APIs are not enough.
There exist a large amount of valuable datasets available publicly on the web, yet lacking completeness/accessibility through formal APIs:
- Job advertisements and job specifications through the company career pages.
- E-commerce e-mail text, delivery ETA drift, price history, e-commerce pages.
- Blog entries / security/news releases and unstructured news.
- Portal research abstracts/metadata/metadata/data

## Core Topics Covered
- HTTP protocols: methods/headers/cookies/sessions/status codes (200/403/429)
- DOM parsing and selectors (CSS/XPath).
- JavaScript rendering: why the headless browsers are successful when there is a request failure.
- Anti-bot systems CAPTCHA, IP blocking, rate limiting, fingerprinting.
- Ethical scraping: politeness, robots.txt knowledge, caching, backoff.

## Code Demos
- src/static scrape requests.py Requests + BeautifulSoup (static HTML)
- `src/dynamic/src/dynamic-scrape-playwright.py`: Playwright scraping (JS-rendered)
- `src/http_debugger.py: Oversight headers/ status codes, rate limits.
- `src/politeness rate-limit.py: backoff + jitter + crawl-delay demeanor.
- detect block pages / CAPTCHAs: src/detect-blocks-and-captcha.py detect-blocks-and-captcha: detect block pages / CAPTCHAs and fail-safely.

## Startup & Agent Lens
The modern web agents do not just scrape sites but navigate websites as human beings.
Some examples are the web-agent framing of Yutori and OpenAI/Anthropic approaches:
- Yutori: AI agents that do daily digital tasks and/or discuss agents with one another on the advantages of leader versus follower on the DOM vs. GUI interface:contentReference[oaicite:0]{index=0}
- OpenAI Operator / Computer-Using Agent / Deep Research: browser + tool-using agents: browser + tool-using agents: contentReference[oaicite:1] index=1.
- interaction and framing of the safety of desktop/browser interaction and anthropic computer use-:contentReference[oaicite:2]{index=2}

## Legal/Ethical Note
This is a learning repo and can be used legitimately as an engineer (public pages will be allowed and ToS must be adhered to).
CAPTCHA is viewed as a red light: we recognize it and drive out instead of driving over it.
