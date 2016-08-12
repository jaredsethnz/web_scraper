import requests
from urllib.parse import urlparse
from webscraper.model.messagehandler import MessageHandler
from webscraper.model.optionfilter import OptionFilter
from webscraper.view.consoleview import ConsoleView


class WebRequest(OptionFilter, MessageHandler):

    # https://www.mightyape.co.nz/Games/PS4/Best-Sellers
    PRINT_DATA_MSG = 'No data to display.....'
    URL_NOT_VALID_MSG = 'please enter a valid url.....'

    def __init__(self):
        super(OptionFilter).__init__()
        self.url = 'https://www.mightyape.co.nz/Games/PS4/Best-Sellers'
        self.url_padding = ''
        self.recursive_urls = []
        self.requests = requests
        self.request_data = None
        self.recursive_request_data = []
        self.recursive_request_data_count = 0
        self.view = ConsoleView()

    def handle_command(self, args):
        return self.command(args, web_request_options)

    def print_data(self, *args):
        attr = self.method_options(args[self.COMMAND_OPTION], web_request_print_options)
        if isinstance(attr, str):
            self.view.display_item(args[self.COMMAND_OPTION] + ': ' + str(attr))
        else:
            self.view.display_items(attr)

    def set_url(self, *args):
        match = urlparse(args[self.COMMAND_OPTION])
        if match[self.URL_SCHEME] == self.URL_SCHEME_HTTP or match[self.URL_SCHEME] == self.URL_SCHEME_HTTPS:
            self.url = args[self.COMMAND_OPTION]
            self.view.display_item('setting url.....')
        else:
            self.view.display_item(self.URL_NOT_VALID_MSG)

    def set_url_padding(self, *args):
        match = urlparse(args[self.COMMAND_OPTION])
        if match[self.URL_SCHEME] == self.URL_SCHEME_HTTP or match[self.URL_SCHEME] == self.URL_SCHEME_HTTPS:
            self.url_padding = args[self.COMMAND_OPTION]
            self.view.display_item('setting url padding.....')
        else:
            self.view.display_item(self.URL_NOT_VALID_MSG)

    def add_recursive_url(self, *args):
        if self.check_url((self.url_padding + args[self.COMMAND_OPTION])):
            self.recursive_urls.append(self.url_padding + args[self.COMMAND_OPTION])
            self.view.display_item('adding url.....')
        else:
            self.view.display_item(self.URL_NOT_VALID_MSG)

    def fetch_html(self, *args):
        if MessageHandler.check_none_condition(self, self.url, 'url not set.....'):
            self.view.display_item('fetching html from ' + self.url + '.....')
            self.request_data = self.requests.get(self.url).text

    def recursive_fetch(self, *args):
        if len(self.recursive_urls) > 0:
            self.view.display_item('fetching recursive html.....')
            for url in self.recursive_urls:
                self.view.display_item('fetching html from ' + url + '.....')
                result = self.requests.get(url).text
                self.recursive_request_data.append(result)
                self.recursive_request_data_count += 1
        else:
            self.view.display_item('no recursive urls set.....')

    def get_request_data(self):
        return self.request_data

    def get_recursive_request_data(self):
        return self.recursive_request_data

# possible we request options and parameter count
web_request_options = {'p': ['print_data', 2], 'u': ['set_url', 2],
                       'f': ['fetch_html', 1], 'up': ['set_url_padding', 2],
                       'ur': ['add_recursive_url', 2], 'rf': ['recursive_fetch', 1]}

web_request_print_options = {'url': 'url', 'urlpadd': 'url_padding',
                             'recurls': 'recursive_urls', 'reqdata': 'request_data',
                             'recdata': 'recursive_request_data', 'recdatacount': 'recursive_request_data_count'}
