from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class ProcessOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(ProcessOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        data = context['ti'].xcom_pull(key='scraped_data', task_ids='scrape_website')
        processed_data = [(item[0].upper(), item[1]) for item in data]
        context['ti'].xcom_push(key='processed_data', value=processed_data)
