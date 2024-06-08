# utils/http_request.py
import requests
import json

class HttpRequest:
    def __init__(self, base_url):
        self.base_url = base_url

    def http_request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        # 确保 headers 是字典类型
        if 'headers' in kwargs and isinstance(kwargs['headers'], str):
            kwargs['headers'] = json.loads(kwargs['headers'])
        response = requests.request(method, url, **kwargs)
        return response