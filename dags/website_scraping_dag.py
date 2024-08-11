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

    data_ready = DataReadySensor(
        task_id='check_data_ready',
        task_id_to_check='scrape_website',
        timeout=5,  # wait for 5 seconds max
        poke_interval=1,  # check every seconds
    )

    scrape_website >> data_ready