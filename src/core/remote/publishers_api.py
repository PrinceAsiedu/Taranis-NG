import requests


class PublishersApi:

    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key
        self.headers = {'Authorization': 'Bearer ' + self.api_key}

    def get_publishers_info(self):
        response = requests.get(self.api_url + "/api/publishers", headers=self.headers)
        return response.json(), response.status_code

    def publish(self, data):
        response = requests.post(self.api_url + "/api/publishers", json=data, headers=self.headers)
        return response.json(), response.status_code
