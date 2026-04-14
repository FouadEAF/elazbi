import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://localhost:8080')
        
        # Scroll to #resume-section
        element = await page.query_selector('#resume-section')
        if element:
            await element.scroll_into_view_if_needed()
            await page.screenshot(path='resume_screenshot.png', full_page=False)
            print("Screenshot saved to resume_screenshot.png")
        else:
            print("Could not find resume section.")
        await browser.close()

asyncio.run(run())
