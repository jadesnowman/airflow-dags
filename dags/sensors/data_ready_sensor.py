from airflow.sensors.base import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

class DataReadySensor(BaseSensorOperator):
    @apply_defaults
    def __init__(self, task_id_to_check, *args, **kwargs):
        super(DataReadySensor, self).__init__(*args, **kwargs)
        self.task_id_to_check = task_id_to_check

    def poke(self, context):
        try:
            data = context['ti'].xcom_pull(task_ids=self.task_id_to_check)
            self.log.info(f"Extracted items from the HTML")
            self.log.info(data)
            return data is not None
        except Exception as e:
            self.log.info(f"Error: {e}")
            return False