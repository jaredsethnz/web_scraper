from webscraper.view.consoleview import ConsoleView
import shelve


class WebObject(object):

    def __init__(self):
        pass

    def display_data(self):
        print(type(self))
        for a in dir(self):
            attr = getattr(self, a)
            print(a + ' = ' + str(attr))


class WebObjectFactory(object):

    def __init__(self):
        pass

    def build_object(self, *args):
        data_object = type(args[0], (WebObject,), args[1])
        return data_object


class DataHandler(object):

    def __init__(self):
        pass

    def save_objects(self, web_objs, key):
        data = shelve.open('web_data_objects.db')
        try:
            data[key] = web_objs
            print('data saved.....')
        finally:
            data.close()


    def load_objects(self, path):
        pass


