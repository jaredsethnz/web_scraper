from webscraper.model.optionfilter import OptionFilter
from webscraper.view.consoleview import ConsoleView
from bs4 import BeautifulSoup


class WebData(OptionFilter):

    TAG_TYPE = 0
    CLASS_NAME = 1

    def __init__(self, web_request):
        super(OptionFilter).__init__()
        self.web_request = web_request
        self.filtered_data = None
        self.filtered_recursive_data = []
        self.view = ConsoleView()
        self.args = None

    def handle_command(self, args):
        return self.command(args, web_data_options)

    def clear_data(self, *args):
        self.view.display_item('clearing data.....')

    def clear_filtered_data(self, *args):
        self.view.display_item('clearing filtered data.....')
        self.filtered_data = None

    def print_data(self, *args):
        attr = self.method_options(args[self.COMMAND_OPTION], web_data_print_options)
        if not isinstance(attr, list):
            self.view.display_item(args[self.COMMAND_OPTION] + ': ' + str(attr))
        else:
            self.view.display_items(attr)

    def load_saved_data(self, *args):
        self.view.display_item('loading saved data.....')

    def save_data(self, *args):
        self.view.display_item('saving data to disk.....')

    def get_request_data(self, *args):
        data = self.web_request.get_request_data()
        data = BeautifulSoup(data, 'html.parser').find(args[self.TAG_TYPE], attrs={'class': args[self.CLASS_NAME]})
        self.filtered_data = data
        self.view.display_item(data)

    def get_recursive_request_data(self, *args):
        for data in self.web_request.get_recursive_request_data():
            self.view.display_item('filtering recursive data.....')
            rec_data = BeautifulSoup(data, 'html.parser').find(args[self.TAG_TYPE], attrs={'class': args[self.CLASS_NAME]})
            self.filtered_recursive_data.append(rec_data)

    def filter_urls(self, *args):
        self.view.display_item('filtering urls.....')
        urls = self.filtered_data.findAll(args[self.TAG_TYPE], attrs={'class': args[self.CLASS_NAME]})
        for url in urls:
            self.web_request.add_recursive_url(url['href'])

# possible web data options and parameter count
web_data_options = {'c': ['clear_data', 2], 'p': ['print_data', 2],
                    'l': ['load_saved_data', 2], 's': ['save_data', 2],
                    'g': ['get_request_data', 3], 'gr': ['get_recursive_request_data', 3],
                    'cf': ['clear_filtered_data', 1], 'fu': ['filter_urls', 3]}

web_data_print_options = {'fdata': 'filtered_data', 'rdata': 'filtered_recursive_data'}
