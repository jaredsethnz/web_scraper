import requests
from webscraper.model.optionfilter import OptionFilter
from webscraper.view.consoleview import ConsoleView


class WebRequest(OptionFilter):

    def __init__(self):
        super(OptionFilter).__init__()
        self.url = None
        self.requests = requests
        self.request_data = None
        self.view = ConsoleView()

    def handle_command(self, args):
        return self.command(args, web_request_options)

    def print_data(self, *args):
        self.view.display_item('printing data......')

    def set_url(self, *args):
        self.view.display_item('setting url.....')

    def fetch_html(self, *args):
        self.view.display_item('fetching html.....')

    def recursive_fetch(self, *args):
        self.view.display_item('setting fetch to recursive.....')

# possible we request options and parameter count
web_request_options = {'p': ['print_data', 2], 'u': ['set_url', 2],
                       'f': ['fetch_html', 1], 'r': ['recursive_fetch', 1]}
