from urllib.parse import urlparse
import re


class OptionFilter(object):

    COMMAND_OPTION = 0
    COMMAND_PARAM = 1
    COMMAND_PARAM_2 = 2
    COMMAND_PARAM_3 = 3
    COMMAND_COUNT = 1
    COMMAND_COUNT_1 = 1
    COMMAND_COUNT_2 = 2
    COMMAND_COUNT_3 = 3
    PARAMETER_ONE = 0
    PARAMETER_TWO = 1
    PARAMETER_THREE = 2
    COMMAND_PARAM_DELIMITER = '--'
    COMMAND_SECOND_LEVEL_DELIMITER = '|'
    COMMAND_SECOND_LEVEL_DELIMITER_TWO = ':'
    COMMAND_ERROR_MSG = 'command error, run help command for command details.....'
    URL_SCHEME = 0
    URL_SCHEME_HTTP = 'http'
    URL_SCHEME_HTTPS = 'https'

    def command(self, args, options):
        commands = self.check_args(args, options)
        if commands is not None:
            for command in commands:
                command[self.COMMAND_OPTION](*command[1:])
        else:
            return self.COMMAND_ERROR_MSG

    def method_options(self, attr, options):
        option = options.get(attr)
        if option is not None:
            return getattr(self, option)
        else:
            return None

    def check_args(self, args, options):
        commands = []
        valid_commands = True
        for arg in args:
            command = []
            arg_param = arg.split(self.COMMAND_PARAM_DELIMITER)
            param = options.get(arg_param[self.COMMAND_OPTION])
            if param is not None and len(arg_param) == param[self.COMMAND_COUNT]:
                method = getattr(self, param[self.COMMAND_OPTION])
                command.append(method)
                value1 = arg_param[self.COMMAND_PARAM] if param[self.COMMAND_COUNT] > self.COMMAND_COUNT_1 else None
                value2 = arg_param[self.COMMAND_PARAM_2] if param[self.COMMAND_COUNT] > self.COMMAND_COUNT_2 else None
                value3 = arg_param[self.COMMAND_PARAM_3] if param[self.COMMAND_COUNT] > self.COMMAND_COUNT_3 else None
                command.append(value1)
                command.append(value2)
                command.append(value3)
            else:
                valid_commands = False
            commands.append(command)
        return None if not valid_commands or len(args) == 0 else commands

    def check_second_level_args(self, args):
        params = []
        pattern = re.compile('[A-Za-z0-9]+:[A-Za-z0-9]+:[A-Za-z0-9]+$')
        args = args[self.COMMAND_OPTION].split(self.COMMAND_SECOND_LEVEL_DELIMITER)
        for arg in args:
            if pattern.match(arg):
                param = arg.split(self.COMMAND_SECOND_LEVEL_DELIMITER_TWO)
                params.append([param[self.PARAMETER_ONE], param[self.PARAMETER_TWO], param[self.PARAMETER_THREE]])
            else:
                self.view.display_item(self.COMMAND_ERROR_MSG)
                return None
        return None if len(params) is 0 else params

    def check_second_level_param_count(self, params, count):
        if len(params) == count:
            return True
        else:
            self.view.display_item('incorrect parameter count, expected ' + str(count) + '.....')
            return False

    def check_url(self, url):
        valid_url = False
        match = urlparse(url)
        if match[self.URL_SCHEME] == self.URL_SCHEME_HTTP or match[self.URL_SCHEME] == self.URL_SCHEME_HTTPS:
            valid_url = True
        return valid_url
