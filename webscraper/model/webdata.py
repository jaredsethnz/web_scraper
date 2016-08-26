import re

from bs4 import BeautifulSoup
from orderedset import OrderedSet

from webscraper.model.optionfilter import OptionFilter
from webscraper.model.webobject import WebObject
from webscraper.view.consoleview import ConsoleView


class WebData(OptionFilter):
    TAG_TYPE = 0
    CLASS_ID = 1
    CLASS_ID_NAME = 2
    CONSOLIDATE_DATA_PARAM_COUNT = 2
    CONSOLIDATE_ERROR_MSG = 'Error consolidating data, please try again...'

    def __init__(self, web_request, web_object_factory, data_handler):
        super(OptionFilter).__init__()
        self.web_request = web_request
        self.web_object_factory = web_object_factory
        self.data_handler = data_handler
        self.filtered_data = []
        self.filtered_data_keywords = []
        self.filtered_recursive_data = []
        self.filtered_recursive_data_keywords = []
        self.web_data_objects = []
        self.view = ConsoleView()

    def handle_command(self, args):
        return self.command(args, web_data_options)

    def get_data(self):
        return self.web_data_objects

    def clear_filtered_data(self, *args):
        self.view.display_item('clearing filtered data.....')
        del self.filtered_data[:]
        del self.filtered_data_keywords[:]
        del self.filtered_recursive_data[:]
        del self.filtered_recursive_data_keywords[:]
        del self.web_data_objects[:]

    def print_data(self, *args):
        attr = self.method_options(args[self.COMMAND_OPTION],
                                   web_data_print_options)
        if attr is not None:
            if not isinstance(attr, list):
                self.view.display_item(args[self.COMMAND_OPTION] + ': '
                                       + str(attr))
            else:
                self.view.display_items(attr)

    def print_web_data_object(self, *args):
        self.view.display_item('displaying web data objects.....')
        self.view.display_item('---------------------------------'
                               '-----------------------------------')
        for wo in self.web_data_objects:
            wo.func_display_data(wo, self.view)
            self.view.display_item('-----------------------------'
                                   '-----------------------------------')

    def display_saves(self, *args):
        self.data_handler.display_save_list()

    def load_saved_data(self, *args):
        self.view.display_item('loading saved data.....')
        loaded_objs = self.data_handler.load_objects(args[self.PARAMETER_ONE])
        self.web_data_objects = loaded_objs

    def save_data(self, *args):
        self.view.display_item('saving data to disk.....')
        self.data_handler.save_objects(self.web_data_objects,
                                       args[self.PARAMETER_ONE])

    def remove_data(self, *args):
        self.data_handler.remove_objects(args[self.PARAMETER_ONE])

    def get_request_data(self, *args):
        try:
            data_options = self.check_second_level_args(args)
            [self.COMMAND_OPTION]
            data = self.web_request.get_request_data()
            req_data = BeautifulSoup(data, 'html.parser') \
                .findAll(data_options[self.TAG_TYPE],
                         attrs={data_options[self.CLASS_ID]: data_options
                         [self.CLASS_ID_NAME]})
            for data in req_data:
                self.filtered_data.append(data)
                self.view.display_item('filtering data.....')
        except TypeError:
            self.view.display_item(self.COMMAND_ERROR_MSG)
            return

    def get_recursive_request_data(self, *args):
        try:
            data_options = self.check_second_level_args(args)
            [self.COMMAND_OPTION]
            for data in self.web_request.get_recursive_request_data():
                self.view.display_item('filtering recursive data.....')
                rec_data = BeautifulSoup(data, 'html.parser') \
                    .find(data_options[self.TAG_TYPE],
                          attrs={data_options[self.CLASS_ID]: data_options
                          [self.CLASS_ID_NAME]})
                self.filtered_recursive_data.append(rec_data)
        except TypeError:
            self.view.display_item(self.COMMAND_ERROR_MSG)
            return

    def filter_urls(self, *args):
        try:
            data_options = self.check_second_level_args(args)
            [self.COMMAND_OPTION]
            self.view.display_item('filtering urls.....')
            for data in self.filtered_data:
                tag_depth = self.check_data_int(data_options[self.CLASS_ID])
                if tag_depth is not None:
                    url = data.find_all(data_options[self.TAG_TYPE])
                    self.web_request.add_recursive_url(url[tag_depth]['href'])
                else:
                    url = data.find(data_options[self.TAG_TYPE],
                                    attrs={data_options[self.CLASS_ID]:
                                    data_options[self.CLASS_ID_NAME]})
                    self.web_request.add_recursive_url(url['href'])
        except (TypeError, KeyError, IndexError):
            self.view.display_item(self.COMMAND_ERROR_MSG)
            return

    def set_data_keywords(self, *args):
        kw_pairs = self.check_second_level_args(args)
        if kw_pairs is not None:
            for kw_pair in kw_pairs:
                keywords = [kw_pair[0], kw_pair[1], kw_pair[2]]
                self.view.display_item('adding tag, class pair: '
                                       + str(keywords))
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
        if params is not None and self.check_second_level_param_count\
                    (params, self.CONSOLIDATE_DATA_PARAM_COUNT):
            func_one = self.method_options(params[self.PARAMETER_ONE]
                                           [self.PARAMETER_ONE],
                                           web_data_consolidate_options)
            func_two = self.method_options(params[self.PARAMETER_TWO]
                                           [self.PARAMETER_ONE], web_data_consolidate_options)
            try:
                attr_one = func_one(self.filtered_data, self.filtered_data_keywords,
                                    params[self.PARAMETER_ONE][self.PARAMETER_TWO],
                                    params[self.PARAMETER_ONE][self.PARAMETER_THREE])
                attr_two = func_two(self.filtered_recursive_data, self.filtered_recursive_data_keywords,
                                    params[self.PARAMETER_TWO][self.PARAMETER_TWO],
                                    params[self.PARAMETER_TWO][self.PARAMETER_THREE])
                self.create_web_data_object(attr_one, attr_two)
            except TypeError:
                self.view.display_item(self.CONSOLIDATE_ERROR_MSG)

    def filter_by_children(self, *args):
        obj_attrs = []
        data = args[0]
        for d in data:
            names = OrderedSet()
            attrs = {}
            try:
                for dc in d.find_all('div'):
                    name = dc.find('span')
                    value = dc.find('div')
                    if value and name is not None:
                        if name.text not in names:
                            names.add(name.text)
                            attrs[name.text] = value.text
                obj_attrs.append(attrs)
            except AttributeError:
                self.view.display_item('Error filtering data from children.....')
        web_objs = self.sanitise_attributes(obj_attrs)
        return web_objs

    def filter_by_keywords(self, *args):
        data = args[self.PARAMETER_ONE]
        data_kw = args[self.PARAMETER_TWO]
        obj_attr = []
        for d in data:
            try:
                attrs = {}
                for kw_pair in data_kw:
                    tag_depth = self.check_data_int(kw_pair[self.PARAMETER_TWO])
                    if tag_depth is not None:
                        value = d.find_all(kw_pair[self.PARAMETER_ONE])
                        value = value[tag_depth].string
                        value = self.check_data_type(value) if value else 'unknown'
                        attrs[kw_pair[self.PARAMETER_THREE]] = value
                    else:
                        value = d.find(kw_pair[self.PARAMETER_ONE],
                                       {kw_pair[self.PARAMETER_TWO]: kw_pair[self.PARAMETER_THREE]}).string
                        value = self.check_data_type(value) if value else 'unknown'
                        attrs[kw_pair[self.PARAMETER_THREE]] = value
                obj_attr.append(attrs)
            except (TypeError, KeyError, IndexError):
                self.view.display_item(self.CONSOLIDATE_ERROR_MSG)
        return obj_attr

    def sanitise_attributes(self, obj_attrs):
        sanitised_obj_attrs = []
        for dict in obj_attrs:
            attrs = {}
            for key, value in dict.items():
                value = value.replace(key, '')
                key = key.replace(value, '')
                sanitized_key = key.replace('\n', '').replace(' ', '').lower()
                sanitized_value = re.sub('[ ]+', ' ', value.replace('\n', '')).strip()
                sanitized_value = self.check_data_type(sanitized_value)
                attrs[sanitized_key] = sanitized_value
            sanitised_obj_attrs.append(attrs)
        return sanitised_obj_attrs

    def create_web_data_object(self, attr_one, attr_two, obj_name='product'):
        if len(attr_two) > 0:
            for attr_one, attr_two in zip(attr_one, attr_two):
                self.view.display_item('creating object.....')
                attr_one.update(attr_two)
                new_obj = self.web_object_factory.build_object(obj_name, attr_one)
                self.web_data_objects.append(new_obj)
        else:
            for attr_one in attr_one:
                self.view.display_item('creating object.....')
                new_obj = self.web_object_factory.build_object(obj_name, attr_one)
                self.web_data_objects.append(new_obj)


# possible web data options and parameter count
web_data_options = {'wo': ['print_web_data_object', 1], 'p': ['print_data', 2],
                    'l': ['load_saved_data', 2], 's': ['save_data', 2],
                    'g': ['get_request_data', 2], 'gr': ['get_recursive_request_data', 2],
                    'cf': ['clear_filtered_data', 1], 'fu': ['filter_urls', 2],
                    'dk': ['set_data_keywords', 2], 'rdk': ['set_recursive_data_keywords', 2],
                    'cd': ['consolidate_data', 2], 'ds': ['display_saves', 1],
                    'rs': ['remove_data', 2]}

web_data_print_options = {'fdata': 'filtered_data', 'rdata': 'filtered_recursive_data',
                          'fdkeywords': 'filtered_data_keywords', 'rfdkeywords': 'filtered_recursive_data_keywords'}

web_data_consolidate_options = {'kw': 'filter_by_keywords', 'child': 'filter_by_children'}
