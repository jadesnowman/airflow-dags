from airflow.plugins_manager import AirflowPlugin
from hooks.api_hook import APIHook
from operators.scrape_operator import ScrapeOperator
from operators.process_operator import ProcessOperator
from sensors.data_ready_sensor import DataReadySensor

class MyCustomPlugin(AirflowPlugin):
    name = "my_custom_plugin"
    hooks = [APIHook]
    operators = [ScrapeOperator, ProcessOperator]
    sensors = [DataReadySensor]
