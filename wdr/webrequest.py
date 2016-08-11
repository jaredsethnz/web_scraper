import requests
import bs4


class WebRequest(object):

    def __init__(self):
        self.url = None
        self.requests = requests
        self.request_data = None

    def set_url(self, url):
        self.url = url

    def get_url(self, args):
        return self.url

    def get_data(self, args):
        return self.request_data

    def fetch_request_data(self, args):
        r = self.requests.get(self.url)
        self.request_data = r.text


request_options = {'p': 'print', 'u': 'url', 'f': 'fetch', 'r': 'recursive'}