from webscraper.model.optionfilter import OptionFilter
from webscraper.view.consoleview import ConsoleView
from bs4 import BeautifulSoup


class WebData(OptionFilter):

    TAG_TYPE = 0
    CLASS_NAME = 1

    def __init__(self, web_request, web_object_factory):
        super(OptionFilter).__init__()
        self.web_request = web_request
        self.web_object_factory = web_object_factory
        self.filtered_data = []
        self.filtered_data_keywords = []
        self.filtered_recursive_data = []
        self.filtered_recursive_data_keywords = []
        self.web_data_objects = []
        self.view = ConsoleView()

    def handle_command(self, args):
        return self.command(args, web_data_options)

    def clear_data(self, *args):
        self.view.display_item('clearing data.....')

    def clear_filtered_data(self, *args):
        self.view.display_item('clearing filtered data.....')
        self.filtered_data = []
        self.filtered_data_keywords = []
        self.filtered_recursive_data = []
        self.filtered_recursive_data_keywords = []
        self.web_data_objects = []

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
        self.view.display_item(len(self.filtered_data))
        self.view.display_item(len(self.filtered_recursive_data))

    def get_request_data(self, *args):
        data = self.web_request.get_request_data()
        req_data = BeautifulSoup(data, 'html.parser')\
            .findAll(args[self.TAG_TYPE], attrs={'class': args[self.CLASS_NAME]})
        for data in req_data:
            self.filtered_data.append(data)
            self.view.display_item('filtering data.....')

    def get_recursive_request_data(self, *args):
        for data in self.web_request.get_recursive_request_data():
            self.view.display_item('filtering recursive data.....')
            rec_data = BeautifulSoup(data, 'html.parser')\
                .find(args[self.TAG_TYPE], attrs={'class': args[self.CLASS_NAME]})
            self.filtered_recursive_data.append(rec_data)

    def filter_urls(self, *args):
        self.view.display_item('filtering urls.....')
        for data in self.filtered_data:
            url = data.find(args[self.TAG_TYPE], attrs={'class': args[self.CLASS_NAME]})
            self.web_request.add_recursive_url(url['href'])

    def set_data_keywords(self, *args):
        kw_pairs = args[self.COMMAND_OPTION].split('|')
        for kw_pair in kw_pairs:
            kw = kw_pair.split(':')
            keywords = [kw[0], kw[1]]
            self.view.display_item('adding tag, class pair: ' + str(keywords))
            self.filtered_data_keywords.append(keywords)

    def set_recursive_data_keywords(self, *args):
        rkw_pairs = args[self.COMMAND_OPTION].split('|')
        for rkw_pair in rkw_pairs:
            rkw = rkw_pair.split(':')
            rkeywords = [rkw[0], rkw[1]]
            self.view.display_item('adding tag, class pair: ' + str(rkeywords))
            self.filtered_recursive_data_keywords.append(rkeywords)

    def consolidate_data(self, *args):
        object_name = args[self.COMMAND_OPTION]
        attr_dic = {}
        index = 0
        for data in self.filtered_data:
            for kw in self.filtered_data_keywords:
                data_value = data.find(kw[self.TAG_TYPE], attrs={'class': kw[self.CLASS_NAME]}).get_text("|", strip=True)
                attr_dic[kw[self.CLASS_NAME]] = data_value
            for kw in self.filtered_recursive_data_keywords:
                data_value = self.filtered_recursive_data[index].find(kw[self.TAG_TYPE],
                                                                      attrs={'class': kw[self.CLASS_NAME]}).get_text("|", strip=True)
                attr_dic[kw[self.CLASS_NAME]] = data_value
            index += 1
            new_object = self.web_object_factory.build_object(object_name, attr_dic)
            new_object.display_data(new_object)
            self.web_data_objects.append(new_object)

# possible web data options and parameter count
web_data_options = {'c': ['clear_data', 2], 'p': ['print_data', 2],
                    'l': ['load_saved_data', 2], 's': ['save_data', 2],
                    'g': ['get_request_data', 3], 'gr': ['get_recursive_request_data', 3],
                    'cf': ['clear_filtered_data', 1], 'fu': ['filter_urls', 3],
                    'dk': ['set_data_keywords', 2], 'rdk': ['set_recursive_data_keywords', 2],
                    'cd': ['consolidate_data', 2]}

web_data_print_options = {'fdata': 'filtered_data', 'rdata': 'filtered_recursive_data',
                          'fdkeywords': 'filtered_data_keywords', 'rfdkeywords': 'filtered_recursive_data_keywords',
                          'wo': 'web_data_objects'}
