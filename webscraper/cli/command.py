from cmd import Cmd

from webscraper.model.graphcreator import GraphCreator
from webscraper.model.webdata import WebData
from webscraper.model.webobject import DataHandler
from webscraper.model.webobject import WebObjectFactory
from webscraper.model.webrequest import *
from webscraper.view.consoleview import *


class Command(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.view = ConsoleView()
        self.web_request = WebRequest()
        self.web_object_factory = WebObjectFactory()
        self.data_handler = DataHandler()
        self.web_data = WebData(self.web_request, self.web_object_factory,
                                self.data_handler)
        self.graph_creator = GraphCreator(self.web_data)

    def do_request(self, args):
        """

        ----------------------------------------------------------------------

        -- request --
        -- Use the request command to handle fetching of website data

        ----------------------------------------------------------------------

        -- OPTIONS --
        u  -- sets primary url for fetch request
              example: request u--'url_here'
        f  -- fetches data from primary url
              example: request f
        up -- sets url padding (if required)
              example: request up--'url_padding'
        ur -- add recursive url (usually done from data)
              example: request ur--'url'
        rf -- fetches data from all recursive urls
              example: request rf
        p  -- prints data related to requests
              example: request p--'p_option'

            -- p OPTIONS --
            url           -- prints primary url
                          example: request p--url
            urlpadd       -- prints recursive url padding
                          example: request p--urlpadd
            recurls       -- prints recursive urls
                          example: request p--recurls
            reqdata       -- prints primary request data
                          example: request p--reqdata
            recdata       -- prints recursive request data
                          example: request p--recdata
            recdatacount  -- prints recursive data count
                          example: request p--recdatacount

        ----------------------------------------------------------------------

        """
        result = self.web_request.handle_command(self.split_args(args))
        if result is not None:
            self.default(result)

    def do_data(self, args):
        """

        ----------------------------------------------------------------------

        -- data --
        -- Use the data command to filter and manipulate website data

        ----------------------------------------------------------------------

        -- OPTIONS --
        l   -- load saved web objects
               example: data l--'file_name'
        s   -- save filtered web objects
               example: data s--'file_name'
        g   -- get request data by tag, class/id, name
               example: data g--'tag':'class/id':'name'
        gr  -- get recursive request data by tag, class/id, name
               example: data gr--'tag':'class/id':'name'
        cf  -- clear all currently filtered data
               example: data cf
        fu  -- filter urls from request data adding
               example: data fu--'tag':'class/id':'name'
               them to recursive urls
        dk  -- set keywords to filter filtered data
               example: data dk--'tag':'class/id':'name'
        rdk -- set keywords to filter recursive filtered data
               example: data rdk--'tag':'class/id':'name'
        cd  -- consolidate all filtered data
               example: data cd--'cd_option':'cd_option'

            -- cd OPTIONS --
            kw    -- filters data by keywords
                     example: data cd--kw:0:0|kw:0:0
            child -- filters data by children
                     example: data cd--kw:0:0|child:0:0

        wo  -- display all created web objects
               example: data wo
        p  -- prints data related to filtered data
              example: data p--'p_option'

            -- p OPTIONS --
            fdata       -- prints filtered data
                           example: data p--fdata
            rdata       -- prints filtered recursive data
                           example: data p--rdata
            fdkeywords  -- prints filtered data keywords
                           example: data p--fdkeywords
            rfdkeywords -- prints recursive filtered data keywords
                           example: data p--rfdkeywords

        ----------------------------------------------------------------------

        """
        result = self.web_data.handle_command(self.split_args(args))
        if result is not None:
            self.default(result)

    def do_graph(self, args):
        """

        ----------------------------------------------------------------------

        -- graph --
        -- Use the graph command to display filtered data in a graphical format

        ----------------------------------------------------------------------

        -- OPTIONS --
        g  -- displays graph -- takes one parameter 'graph_title'
              example: graph g--'graph_title_here'
        d  -- sets graph data -- takes one parameter
              example: graph d--'attribute_name_here'
        gd -- displays currently set graph data -- takes no parameters
              example: graph gd

        ----------------------------------------------------------------------

        """
        result = self.graph_creator.handle_command(self.split_args(args))
        if result is not None:
            self.default(result)

    def split_args(self, args):
        if args is None:
            return None
        else:
            return args.split()
