from webscraper.view.consoleview import ConsoleView


class WebObject(object):

    def display_data(self):
        print(type(self))
        for a in dir(self):
            if not a.startswith('__') and not a.startswith('view'):
                attr = getattr(self, a)
                print(a + ' = ' + str(attr))


class WebObjectFactory(object):

    data_object = None

    def __init__(self):
        pass

    def build_object(self, *args):
        self.data_object = type(args[0], (WebObject,), args[1])
        print('TESTING')
        return self.data_object

