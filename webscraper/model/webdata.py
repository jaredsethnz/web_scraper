from webscraper.model.optionfilter import OptionFilter
from webscraper.view.consoleview import ConsoleView
from bs4 import BeautifulSoup


class WebData(OptionFilter):

    TAG_TYPE = 0
    CLASS_ID = 1
    CLASS_ID_NAME = 2
    CONSOLIDATE_DATA_PARAM_COUNT = 2

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
        del self.filtered_data[:]
        del self.filtered_data_keywords[:]
        del self.filtered_recursive_data[:]
        del self.filtered_recursive_data_keywords[:]
        del self.web_data_objects[:]

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
        data = self.check_second_level_args(args)
        self.view.display_item(data)

    def get_request_data(self, *args):
        try:
            data_options = self.check_second_level_args(args)[self.COMMAND_OPTION]
            data = self.web_request.get_request_data()
            req_data = BeautifulSoup(data, 'html.parser')\
                .findAll(data_options[self.TAG_TYPE],
                         attrs={data_options[self.CLASS_ID]: data_options[self.CLASS_ID_NAME]})
            for data in req_data:
                self.filtered_data.append(data)
                self.view.display_item('filtering data.....')
        except TypeError:
            self.view.display_item(self.COMMAND_ERROR_MSG)
            return

    def get_recursive_request_data(self, *args):
        try:
            data_options = self.check_second_level_args(args)[self.COMMAND_OPTION]
            for data in self.web_request.get_recursive_request_data():
                self.view.display_item('filtering recursive data.....')
                rec_data = BeautifulSoup(data, 'html.parser')\
                    .find(data_options[self.TAG_TYPE],
                          attrs={data_options[self.CLASS_ID]: args[data_options.CLASS_ID_NAME]})
                self.filtered_recursive_data.append(rec_data)
        except TypeError:
            self.view.display_item(self.COMMAND_ERROR_MSG)
            return

    def filter_urls(self, *args):
        self.view.display_item('filtering urls.....')
        for data in self.filtered_data:
            url = data.find(args[self.TAG_TYPE], attrs={args[self.CLASS_ID]: args[self.CLASS_ID_NAME]})
            self.web_request.add_recursive_url(url['href'])

    def set_data_keywords(self, *args):
        kw_pairs = self.check_second_level_args(args)
        if kw_pairs is not None:
            for kw_pair in kw_pairs:
                keywords = [kw_pair[0], kw_pair[1], kw_pair[2]]
                self.view.display_item('adding tag, class pair: ' + str(keywords))
                self.filtered_data_keywords.append(keywords)

    def set_recursive_data_keywords(self, *args):
        kw_pairs = self.check_second_level_args(args)
        if kw_pairs is not None:
            for kw_pair in kw_pairs:
                r_keywords = [kw_pair[0], kw_pair[1], kw_pair[2]]
                self.view.display_item('adding tag, class pair: ' + str(r_keywords))
                self.filtered_recursive_data_keywords.append(r_keywords)

    def consolidate_data(self, *args):
        params = self.check_second_level_args(args)
        if self.check_second_level_param_count(params, self.CONSOLIDATE_DATA_PARAM_COUNT):
            attr_one = params[self.PARAMETER_ONE][self.PARAMETER_ONE]
            att_two = params[self.PARAMETER_TWO][self.PARAMETER_ONE]
            self.view.display_item(attr_one + ' --- ' + att_two)

    def filter_by_children(self, *args):
        print(args)

    def filter_by_keywords(self, *args):
        obj_attr = {}
        for fdata in self.filtered_data:
            for kw_pair in self.filtered_data_keywords:
                try:
                    value = fdata.find(kw_pair[self.PARAMETER_ONE],
                                       {kw_pair[self.PARAMETER_TWO]: kw_pair[self.PARAMETER_THREE]}).string
                    self.view.display_item(value)
                except AttributeError:
                    self.view.display_item('Error consolidating data, please try again...')


# possible web data options and parameter count
web_data_options = {'c': ['clear_data', 2], 'p': ['print_data', 2],
                    'l': ['load_saved_data', 2], 's': ['save_data', 2],
                    'g': ['get_request_data', 2], 'gr': ['get_recursive_request_data', 2],
                    'cf': ['clear_filtered_data', 1], 'fu': ['filter_urls', 4],
                    'dk': ['set_data_keywords', 2], 'rdk': ['set_recursive_data_keywords', 2],
                    'cd': ['consolidate_data', 2]}

web_data_print_options = {'fdata': 'filtered_data', 'rdata': 'filtered_recursive_data',
                          'fdkeywords': 'filtered_data_keywords', 'rfdkeywords': 'filtered_recursive_data_keywords',
                          'wo': 'web_data_objects'}

web_data_consolidate_options = {'kw': 'filter_by_keywords', 'child': 'filter_by_children'}
