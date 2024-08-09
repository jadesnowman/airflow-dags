from playwright.sync_api import sync_playwright
import re, csv
from url_parse import url_to_slug

def save_data_to_csv(data, filename):
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['image_alt', 'image_url'])
        for item in data:
            writer.writerow([item['image_alt'], item['image_url']])

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
    
    # Wait for the games list to load
    page.wait_for_selector('ul.css-cnqlhg')


    # Extracting both image URLs from the image-set property
    games = page.query_selector_all('ul.css-cnqlhg li')

    extracted_data = []
    for game in games:
        image_element = game.query_selector('img')
        image_url = image_element.get_attribute('data-image') if image_element else "No image found"
        image_alt = image_element.get_attribute('alt') if image_element else "No image found"

        extracted_data.append({
            'image_alt': image_alt,
            'image_url': image_url,
        })

    browser.close()

    return extracted_data

with sync_playwright() as playwright:
    chrome_executable_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    url = 'https://store.epicgames.com/en-US/collection/top-new-releases'
    data = run(playwright, url, chrome_executable_path)
    save_data_to_csv(data, url_to_slug(url, 'csv'))

