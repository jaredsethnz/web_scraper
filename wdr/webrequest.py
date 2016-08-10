import requests
# import bn4


class WebRequest(object):

    def __init__(self, url):
        self.url = url
        self.requests = requests
        self.request_data = None

    def get_url(self):
        return self.url

    def get_data(self):
        return self.request_data

    def fetch_request_data(self):
        r = self.requests.get(self.url)
        self.request_data = r.text
