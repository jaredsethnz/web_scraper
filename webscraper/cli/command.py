from cmd import Cmd
from webscraper.model.graphcreator import GraphCreator
from webscraper.model.webdata import WebData
from webscraper.model.webrequest import *
from webscraper.view.consoleview import *


class Command(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.view = ConsoleView()
        self.web_request = WebRequest()
        self.web_data = WebData(self.web_request)
        self.graph_creator = GraphCreator(self.web_data)

    def do_request(self, args):
        """
        request n (new) http:// (url)
        request f (fetch)
        request p (print data)
        """
        result = self.web_request.handle_command(self.split_args(args))
        if result is not None:
            self.default(result)

    def do_data(self, args):
        """
        -- Use the data command to clear saved data, displayed current data or reloads saved data
        --OPTIONS--
        data c -- clears saved data
        data d -- displays current data
        data r -- reloads data saved to disk
        """
        result = self.web_data.handle_command(self.split_args(args))
        if result is not None:
            self.default(result)

    def do_graph(self, args):
        """
        -- Use the graph command to display data in a graphical format
        --OPTIONS--
        graph t 'graph type' d 'data set name' -- displays a graph type with the specified data set
        """
        result = self.graph_creator.handle_command(self.split_args(args))
        if result is not None:
            self.default(result)

    def split_args(self, args):
        if args is None:
            return None
        else:
            return args.split()
