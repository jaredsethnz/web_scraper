from webscraper.model.optionfilter import OptionFilter
from webscraper.view.consoleview import ConsoleView


class GraphCreator(OptionFilter):

    def __init__(self, web_data):
        super(OptionFilter).__init__()
        self.web_data = web_data
        self.data = None
        self.graph_type = None
        self.view = ConsoleView()

    def handle_command(self, args):
        return self.command(args, graph_creator_options)

    def graph_type(self, *args):
        self.view.display_item('setting graph type.....')

    def graph_data(self, *args):
        self.data = self.web_data.get_data(args[self.COMMAND_OPTION])

# possible graph creator options and parameter count
graph_creator_options = {'t': ['graph_type', 2], 'd': ['graph_data', 2]}
