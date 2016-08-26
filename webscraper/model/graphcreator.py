import decimal

from webscraper.model.optionfilter import OptionFilter
from webscraper.view.consoleview import ConsoleView
from datetime import date
import matplotlib.pyplot as plt


class GraphCreator(OptionFilter):

    def __init__(self, web_data):
        super(OptionFilter).__init__()
        self.web_data = web_data
        self.data = {}
        self.graph_type = None
        self.view = ConsoleView()

    def handle_command(self, args):
        return self.command(args, graph_creator_options)

    def display_graph(self, *args):

        labels = []
        sizes = []
        colors = []
        explode = []
        color_count = len(graph_colors) - 1
        count = 0
        largest_value = 0
        for key, value in self.data.items():
            largest_value = value if value >= largest_value else largest_value
            color = graph_colors[count]
            labels.append(key)
            sizes.append(value)
            colors.append(color)
            explode.append(0.0)
            count = (count + 1) if count < color_count else 0
        if len(self.data) > 0:
            explode_index = sizes.index(largest_value)
            explode[explode_index] = 0.1

            plt.title(args[self.PARAMETER_ONE])
            plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=90)
            plt.axis('equal')
            self.view.display_item('displaying graph.....')
            plt.show()

    def graph_data(self, *args):
        self.data.clear()
        web_data = self.web_data.get_data()
        attr_name = args[self.PARAMETER_ONE]
        self.view.display_item('gathering data.....')
        for wd in web_data:
            try:
                wd_attr = getattr(wd, attr_name)
                if type(wd_attr) is decimal.Decimal:
                    self.currency_data(wd_attr)
                elif type(wd_attr) is date:
                    self.date_data(wd_attr)
                else:
                    self.str_data(wd_attr)
            except (AttributeError, UnboundLocalError):
                self.view.\
                    display_item('Error, WebObject contains no attribute ' +
                                 attr_name + '.....')

    def currency_data(self, value):
        self.view.display_item('currency')

    def date_data(self, value):
        pass

    def str_data(self, value):
        if self.data.get(value) is None:
            self.data[value] = 1
        else:
            self.data[value] = self.data.get(value) + 1

    def display_graph_data(self, *args):
        for key, value in self.data.items():
            print(key + ': ' + str(value))

# possible graph creator options and parameter count
graph_creator_options = {'g': ['display_graph', 2], 'd': ['graph_data', 2],
                         'gd': ['display_graph_data', 1]}

data_type_funcs = {'str': 'str_data', 'decimal.Decimal': 'currency_data'}

graph_colors = ['red', 'yellow', 'greenyellow', 'deepskyblue', 'royalblue',
                'mediumpurple', 'deeppink', 'aqua', 'lime', 'dodgerblue']
