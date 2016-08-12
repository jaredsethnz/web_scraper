from webscraper.model.optionfilter import OptionFilter
from webscraper.view.consoleview import ConsoleView


class WebData(OptionFilter):

    def __init__(self):
        super(OptionFilter).__init__()
        self.view = ConsoleView()

    def handle_command(self, args):
        return self.command(args, web_data_options)

    def clear_data(self, *args):
        self.view.display_item('clearing saved data.....')

    def display_data(self, *args):
        self.view.display_item('displaying current data.....')

    def load_saved_data(self, *args):
        self.view.display_item('loading saved data.....')

    def save_data(self, *args):
        self.view.display_item('saving data to disk.....')

    def get_data(self, name=None):
        self.view.display_item('getting data named {0}...'.format(name))
        return None

# possible web data options and parameter count
web_data_options = {'c': ['clear_data', 2], 'd': ['display_data', 2],
                    'l': ['load_saved_data', 2], 's': ['save_data', 2]}
