from urllib.parse import urlparse
from decimal import Decimal
from datetime import date
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
    PARAMETER_FOUR = 3
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
                break
        return None if len(params) is 0 else params

    def check_second_level_param_count(self, params, count):
        if len(params) == count:
            return True
        else:
            self.view.display_item('incorrect parameter count, expected ' + str(count) + '.....')
            return False

    def check_data_type(self, str_value):
        currency_value = self.check_data_currency(str_value)
        if currency_value is not None:
            return currency_value
        int_value = self.check_data_int(str_value)
        if int_value is not None:
            return int_value
        date_value = self.check_data_date(str_value)
        if date_value is not None:
            return date_value
        return str_value

    def check_data_int(self, str_value):
        pattern = re.compile('^[0-9]+$')
        int_value = None
        if pattern.match(str_value):
            int_value = int(str_value)
        return int_value

    def check_data_currency(self, str_value):
        pattern = re.compile('\$[1-9]?[0-9]+\.[0-9][0-9]$')
        currency_value = None
        if pattern.match(str_value):
            str_value = str_value.strip('$')
            currency_value = Decimal(str_value)
        return currency_value

    def check_data_date(self, str_value):
        pattern = re.compile('[.,/#!$%\^&*;:{}=\-_`~()a-zA-Z]+')
        date_value = None
        str_values = str_value.split(' ')
        month_number = months.get(str_values[self.PARAMETER_ONE])
        if month_number is not None:
            month = month_number
            try:
                day = int(pattern.sub('', str_values[self.PARAMETER_TWO]))
                year = int(str_values[self.PARAMETER_THREE])
                date_value = date(year, month, day)
            except TypeError:
                self.view.display_item('Error parsing date.....')
        return date_value

    def check_url(self, url):
        valid_url = False
        match = urlparse(url)
        if match[self.URL_SCHEME] == self.URL_SCHEME_HTTP or match[self.URL_SCHEME] == self.URL_SCHEME_HTTPS:
            valid_url = True
        return valid_url

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
          'September': 9, 'October': 10, 'November': 11, 'December': 12}



