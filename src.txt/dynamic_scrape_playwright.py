from playwright.sync_api import sync_playwright

def scrape_dynamic(url: str, selector: str) -> list[str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)

        # Wait until the JS-injected content appears
        page.wait_for_selector(selector, timeout=30_000)

        items = page.locator(selector).all_text_contents()
        browser.close()
        return [x.strip() for x in items if x.strip()]

if __name__ == "__main__":
    print(scrape_dynamic("https://example.com", "h1"))
