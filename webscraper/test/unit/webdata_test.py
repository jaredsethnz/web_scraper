from webscraper.model.webdata import WebData
from webscraper.model.webobject import WebObjectFactory, DataHandler
from webscraper.model.webrequest import WebRequest
from unittest import TestCase


class WebDataTest(WebData, TestCase):

    def __init__(self):
        super(WebRequest(), WebObjectFactory(), DataHandler()).__init__()
        self.test = TestCase()

    def print_test_title(self, text, number):
        self.view.display_item('----------------' + text + '::'
                               + number + '----------------')

    # All WebRequest unit tests below
    def save_data_test_one(self):
        pass

    def save_data_test_two(self):
        pass

    def load_saved_data_test_one(self):
        pass

    def load_saved_data_test_two(self):
        pass

    def remove_data_test_one(self):
        pass

    def remove_data_test_two(self):
        pass

    def get_request_data_test_one(self):
        pass

    def get_request_data_test_two(self):
        pass

    def get_recursive_request_data_one(self):
        pass

    def get_recursive_request_data_two(self):
        pass

    def filter_urls_test_one(self):
        pass

    def filter_urls_test_two(self):
        pass

    def set_data_keywords_test_one(self):
        pass

    def set_data_keywords_test_two(self):
        pass

    def set_recursive_data_keywords_test_one(self):
        pass

    def set_recursive_data_keywords_test_two(self):
        pass

    def consolidate_data_test_one(self):
        pass

    def consolidate_data_test_two(self):
        pass

    def create_web_data_object_test_one(self):
        pass

    def create_web_data_object_test_two(self):
        pass


web_data_test = WebDataTest()

# Test setting request url
