from airflow.hooks.base import BaseHook
import requests

class APIHook(BaseHook):
    def __init__(self, api_conn_id):
        super().__init__()
        self.conn_id = api_conn_id
        self.base_url = self.get_connection(api_conn_id).host

    def get_data(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        return response.json()
