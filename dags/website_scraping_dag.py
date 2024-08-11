from airflow import DAG
from datetime import datetime
from operators.scrape_operator import ScrapeOperator
from sensors.data_ready_sensor import DataReadySensor

default_args = {
    'owner': 'user',
    'start_date': datetime(2024, 8, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'website_scraping_dag',
    default_args=default_args,
    description='A DAG to scrape, process, and store Y Combinator news data',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    scrape_website = ScrapeOperator(
        task_id='scrape_website',
        url='https://news.ycombinator.com',
    )

    scrape_website