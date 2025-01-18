import requests
from bs4 import BeautifulSoup
import csv

def scrape_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titleline = soup.find_all('span', class_='titleline')

        extracted_data = []
        for tr in titleline:
            row = tr.find_all('a')
            if row:
                extracted_data.append({
                    'title': row[0].text,
                    'link': row[0].get('href')
                })

        return extracted_data

    else:
        print(f"Failed to retrieve content, status code: {response.status_code}")
        return []

def save_data_to_csv(data, filename):
    with open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link'])
        for item in data:
            writer.writerow([item['title'], item['link']])

url = 'https://news.ycombinator.com/'  # Example site
data = scrape_data(url)
save_data_to_csv(data, 'testing.csv')