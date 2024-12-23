import requests
import json

CHAINLINK_NODE_URL = "https://chainlink-node.example.com"

class OracleAdapter:
    def __init__(self, feed_url):
        self.feed_url = feed_url

    def get_data(self):
        response = requests.get(self.feed_url)
        if response.status_code == 200:
            data = response.json()
            return data
        return None

    def push_to_chainlink(self, data):
        # In a real scenario, send to Chainlink node job
        payload = {"data": data}
        requests.post(CHAINLINK_NODE_URL, json=payload)
