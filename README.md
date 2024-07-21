pip i -r requirement

airflow db migrate

airflow users create \
    --username Admin \
    --firstname Admin \
    --lastname Admin \
    --role Admin \
    --email Admin@yopmail.com \
    --password Admin

airflow users create \
    --username Viewer \
    --firstname Viewer \
    --lastname Viewer \
    --role Viewer \
    --email Viewer@yopmail.com \
    --password Viewer