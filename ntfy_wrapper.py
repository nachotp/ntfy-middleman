import requests
from requests.auth import HTTPBasicAuth

class NtfyPublisher:
    def __init__(self, domain, topic, username, password) -> None:
        self.domain=domain
        self.topic=topic
        self.username=username
        self.password=password
    
    def post(self, message, title : str=None, priority=None, tags : list=None):
        headers = {}
        
        if title:
            headers["Title"] = title
        if priority:
            headers["Priority"] = priority
        if tags:
            headers["Tags"] = ",".join(tags)


        requests.post(
            f"{self.domain}/{self.topic}",
            auth= None if not self.username else HTTPBasicAuth(self.username, self.password),
            data=message,
            headers=headers
        )
