from airflow.hooks.postgres_hook import PostgresHook

def store_data_in_db(data, table_name):
    hook = PostgresHook(postgres_conn_id='my_postgres')
    hook.insert_rows(table_name, data)