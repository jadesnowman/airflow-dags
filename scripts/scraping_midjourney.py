from playwright.sync_api import sync_playwright
import re, csv
from url_parse import url_to_slug

def save_data_to_csv(data, filename):
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['1x, 2x'])
        for item in data:
            writer.writerow([item[0], item[1]])

def run(playwright, url, chrome_executable_path=None):

    # Launch Chrome with Playwright
    browser = playwright.chromium.launch(
        headless=False,  # Set to True to run in headless mode
        executable_path=chrome_executable_path
    )

    page = browser.new_page()
    
    page.goto(url, wait_until='networkidle')

    # Scroll to the bottom to load more content if needed
    page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    
    # Wait for a while to ensure content is loaded
    page.wait_for_timeout(5000)

    # Extracting both image URLs from the image-set property
    elements = page.query_selector_all('div.absolute div a')
    
    image_urls = []
    for element in elements:
        # Get the background image URL from the style attribute
        style = element.get_attribute('style')
        if style:
            # Extract URLs from image-set property
            matches = re.findall(r'url\(["\'](.*?)["\']\)', style)
            if matches:
                # The image-set property might contain multiple URLs (1x, 2x)
                sizes = []
                for index, image_url in enumerate(matches):
                    sizes.append(image_url)

                image_urls.append(sizes)

    browser.close()

    return image_urls

with sync_playwright() as playwright:
    chrome_executable_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    url = 'https://www.midjourney.com/showcase'
    data = run(playwright, url, chrome_executable_path)
    save_data_to_csv(data, url_to_slug(url, 'csv'))
