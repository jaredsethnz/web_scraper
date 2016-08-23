from webscraper.model.webrequest import WebRequest
from unittest import TestCase


class WebRequestTest(WebRequest, TestCase):

    ERROR_MSG = 'Error Message:  '
    START_TEST = 'StartingTest'
    STOP_TEST = 'StoppingTest'

    def __init__(self):
        super().__init__()
        self.test = TestCase()

    def clear_request_data(self):
        self.url = ''
        self.url_padding = ''
        del self.recursive_urls[:]
        self.request_data = None
        self.requests_status_code = None
        del self.recursive_request_data[:]
        self.recursive_request_data_count = 0

    def print_test_title(self, text, number):
        self.view.display_item('----------------' + text + '::' + number + '----------------')

    # All WebRequest unit tests below

    def set_url_test_one(self):
        self.print_test_title(self.START_TEST, '1.1')
        url = 'http://www.google.com'
        self.set_url(url)
        self.test.assertEqual(self.url, url, self.ERROR_MSG + 'url no equal to set value')

    def set_url_test_two(self):
        self.print_test_title(self.START_TEST, '1.2')
        url = 'google.com'
        self.set_url(url)
        self.test.assertNotEqual(self.url, url, self.ERROR_MSG + 'url equal to set value')

    def set_url_padding_test_one(self):
        self.print_test_title(self.START_TEST, '2.1')
        url_padding = 'http://www.google.com'
        self.set_url_padding(url_padding)
        self.test.assertEqual(self.url_padding, url_padding, self.ERROR_MSG + 'url padding not equal to set value')

    def set_url_padding_test_two(self):
        self.print_test_title(self.START_TEST, '2.2')
        url_padding = 'google.com'
        self.set_url_padding(url_padding)
        self.test.assertNotEqual(self.url_padding, url_padding, self.ERROR_MSG + 'url padding equal to padding value')

    def add_recursive_url_test_one(self):
        self.print_test_title(self.START_TEST, '3.1')
        self.clear_request_data()
        rec_url = 'http://www.google.com'
        self.add_recursive_url(rec_url)
        self.test.assertEqual(self.recursive_urls[0], rec_url, self.ERROR_MSG + 'recursive url not in list')

    def add_recursive_url_test_two(self):
        self.print_test_title(self.START_TEST, '3.2')
        self.clear_request_data()
        rec_url = 'test'
        zero_urls = 0
        self.add_recursive_url(rec_url)
        self.test.assertEqual(len(self.recursive_urls), zero_urls, self.ERROR_MSG + 'recursive url in list')

    def fetch_html_test_one(self):
        self.print_test_title(self.START_TEST, '4.1')
        self.clear_request_data()
        url = 'http://www.google.com'
        response_okay = 200
        self.set_url(url)
        self.fetch_html()
        self.test.assertEqual(self.requests_status_code, response_okay,
                              self.ERROR_MSG + 'response code ' + str(self.requests_status_code))

    def fetch_html_test_two(self):
        self.print_test_title(self.START_TEST, '4.2')
        self.clear_request_data()
        url = 'http://www.thisisafakeurlsoyeah.com'
        response_okay = 200
        self.set_url(url)
        self.fetch_html()
        self.test.assertNotEqual(self.requests_status_code, response_okay,
                                 self.ERROR_MSG + 'response code ' + str(self.requests_status_code))

    def recursive_fetch_test_one(self):
        self.print_test_title(self.START_TEST, '5.1')
        self.clear_request_data()
        url = 'http://www.google.com'
        response_okay = 200
        self.add_recursive_url(url)
        self.add_recursive_url(url)
        self.recursive_fetch()
        self.test.assertEqual(self.requests_status_code, response_okay,
                              self.ERROR_MSG + 'response code ' + str(self.requests_status_code))

    def recursive_fetch_test_two(self):
        self.print_test_title(self.START_TEST, '5.2')
        self.clear_request_data()
        url = 'http://www.thisisafakeurlsoyeah.com'
        response_okay = 200
        self.add_recursive_url(url)
        self.add_recursive_url(url)
        self.recursive_fetch()
        self.test.assertNotEqual(self.requests_status_code, response_okay,
                                 self.ERROR_MSG + 'response code ' + str(self.requests_status_code))


web_request_test = WebRequestTest()

# Test setting request url
web_request_test.set_url_test_one()
web_request_test.set_url_test_two()

# Test setting request url padding
web_request_test.set_url_padding_test_one()
web_request_test.set_url_padding_test_two()

# Test adding recursive urls
web_request_test.add_recursive_url_test_one()
web_request_test.add_recursive_url_test_two()

# Test request data fetching
web_request_test.fetch_html_test_one()
web_request_test.fetch_html_test_two()

# Test recursive data fetching
web_request_test.recursive_fetch_test_one()
web_request_test.recursive_fetch_test_two()
