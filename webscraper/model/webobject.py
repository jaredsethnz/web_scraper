import sys
from webscraper.view.consoleview import ConsoleView
import pickle
from os.path import abspath
from os import remove


class WebObject(object):

    def __init__(self):
        pass

    def func_display_data(self, view):
        for a in dir(self):
            if not a.startswith('__') and not a.startswith('func'):
                attr = getattr(self, a)
                view.display_item(a + ' = ' + str(attr))


class WebObjectFactory(object):

    def build_object(self, *args):
        data_object = type(args[0], (WebObject,), args[1])
        return data_object


class DataHandler(object):

    def __init__(self):
        self.web_object_factory = WebObjectFactory()
        self.view = ConsoleView()
        self.save_list = self.init_save_list()

    def init_save_list(self):
        s_list = []
        try:
            with open('savelist.pickle', 'rb') as input_file:
                s_list = pickle.load(input_file)
        except (EOFError, FileNotFoundError):
            self.view.display_item('No save list found, creating new save list.....')
            with open('savelist.pickle', 'wb') as output_file:
                pickle.dump(s_list, output_file)
        return s_list

    def save_save_list(self):
        try:
            with open('savelist.pickle', 'wb') as output_file:
                pickle.dump(self.save_list, output_file)
        except (EOFError, FileNotFoundError):
            self.view.display_item('Error saving save list.....')

    def display_save_list(self):
        self.view.display_item('displaying file save locations.....')
        self.view.display_items(self.save_list)

    def add_save_list(self, save_location):
        save_location = abspath(save_location)
        if save_location not in self.save_list:
            self.save_list.append(save_location)
            self.save_save_list()

    def remove_save_list(self, save_location):
        save_location = abspath(save_location)
        self.save_list.remove(save_location)
        self.save_save_list()

    def save_objects(self, web_objs, path):
        try:
            sys.setrecursionlimit(1000000)
            objs = []
            for obj in web_objs:
                dict = obj.__dict__.copy()
                for key in obj.__dict__:
                    if key.startswith('__') and key.endswith('__'):
                        del dict[key]
                objs.append(dict)
            output_file = open(path, 'wb')
            pickle.dump(objs, output_file)
            self.add_save_list(path)
        except FileNotFoundError:
            self.view.display_item('Error saving file.....')

    def remove_objects(self, path):
        try:
            self.view.display_item('removing file ' + path + '.....')
            remove(path)
            self.remove_save_list(path)
        except FileNotFoundError:
            self.view.display_item('File ' + path + ' not found.....')

    def load_objects(self, path):
        loaded_objs = []
        try:
            with open(path, 'rb') as input_file:
                web_objs = pickle.load(input_file)
            for obj in web_objs:
                loaded_objs.append(self.web_object_factory.build_object('product', obj))
        except FileNotFoundError:
            self.view.display_item('File ' + path + ' not found.....')
        return loaded_objs


