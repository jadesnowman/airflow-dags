from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import requests
from bs4 import BeautifulSoup
import json
import os
import uuid
from datetime import datetime

class ScrapeOperator(BaseOperator):
    @apply_defaults
    def __init__(self, url, *args, **kwargs):
        super(ScrapeOperator, self).__init__(*args, **kwargs)
        self.url = url

    def execute(self, context):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = self.parse_data(soup)
        self.save_data(context, data)

    def parse_data(self, soup):
        items = soup.find_all('span', class_='titleline')

        extracted_data = []
        for tr in items:
            row = tr.find_all('a')
            if row:
                extracted_data.append({
                    'title': row[0].text,
                    'link': row[0].get('href')
                })

        return extracted_data
    
    def save_data(self, context, data):
        # Access $AIRFLOW_HOME
        airflow_home = os.environ.get('AIRFLOW_HOME', '/usr/local/airflow')

        # Get the current date in YYYYMMDD format
        current_date = datetime.now().strftime("%Y%m%d")

        # Generate a random file name with the date and a .txt extension
        random_file_name = f"{current_date}_{uuid.uuid4()}.json"

        # Define full file path
        file_path = os.path.join(airflow_home, 'data', random_file_name)
            
        json_data = json.dumps(data)
        
        with open(file_path, 'w') as f:
            f.write(json_data)

        context['ti'].xcom_push(key='scraped_data', value=file_path)