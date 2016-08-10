from cmd import Cmd
import wdr.webrequest


class Command(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.web_request = None

    def do_args(self, args):
        """
        Displays the passed arguments
        :param args:
        :return:
        """
        print(args)

    def do_new_request(self, args):
        """
        Prepares new request
        :return:
        """
        self.web_request = wdr.webrequest.WebRequest(args)

    # Request related functions follow
    def do_print_request_url(self, args):
        if self.web_request is not None:
            print(self.web_request.get_url())

    def do_request_url_data(self, args):
        if self.web_request is not None:
            self.web_request.fetch_request_data()
        else:
            print('Error: no web request created...')

    def do_print_request_data(self, args):
        if self.web_request is not None:
            print(self.web_request.get_data())
        else:
            print('Error: no web request created...')
