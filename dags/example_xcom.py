from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def push_data(**kwargs):
    data = "This is a test"
    # Push data to XCom
    kwargs['ti'].xcom_push(key='my_key', value=data)

def pull_data(**kwargs):
    # Pull data from XCom
    pulled_data = kwargs['ti'].xcom_pull(key='my_key', task_ids='push_task')
    print(f"Pulled data: {pulled_data}")

with DAG(dag_id='example_xcom', start_date=datetime(2023, 8, 11), schedule_interval=None) as dag:
    push_task = PythonOperator(
        task_id='push_task',
        python_callable=push_data,
        provide_context=True
    )

    pull_task = PythonOperator(
        task_id='pull_task',
        python_callable=pull_data,
        provide_context=True
    )

    push_task >> pull_task
