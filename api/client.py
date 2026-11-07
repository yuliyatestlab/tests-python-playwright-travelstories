import requests
from bs4 import BeautifulSoup

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, **kwargs):
        kwargs.setdefault("allow_redirects", False)
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path, **kwargs):
        kwargs.setdefault("allow_redirects", False)
        return self.session.post(f"{self.base_url}{path}", **kwargs)

    def csrf_token(self, path):
        soup = BeautifulSoup(self.get(path).text, "html.parser")
        return soup.find("input", {"name": "csrf_token"})["value"]

    def login(self, email, password):
        token = self.csrf_token("/login")
        return self.post("/login", data={
            "email": email,
            "password": password,
            "csrf_token": token,
        })
