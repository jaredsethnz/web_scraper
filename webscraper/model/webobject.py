from webscraper.view.consoleview import ConsoleView


class WebObject(object):

    def display_data(self):
        self.view.display_item(type(self))
        for a in dir(self):
            if not a.startswith('__') and not a.startswith('view'):
                attr = getattr(self, a)
                self.view.display_item(a + ' = ' + str(attr))


class WebObjectFactory(object):

    data_object = None

    def __init__(self):
        pass

    def build_object(self, *args):
        args[1]['view'] = ConsoleView()
        self.data_object = type(args[0], (WebObject,), args[1])
        return self.data_object

