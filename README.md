echo $AIRFLOW_HOME

pip i -r requirement

airflow db migrate

airflow users create \
    --username groot \
    --firstname groot \
    --lastname groot \
    --role Admin \
    --email groot@yopmail.com \
    --password groot

airflow users create \
    --username rocket \
    --firstname rocket \
    --lastname rocket \
    --role Viewer \
    --email rocket@yopmail.com \
    --password rocket

airflow webserver --port 9999

airflow scheduler

airflow celery worker

airflow celery stop

airflow celery flower

airflow dags list