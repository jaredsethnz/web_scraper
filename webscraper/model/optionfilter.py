
class OptionFilter(object):

    COMMAND_OPTION = 0
    COMMAND_PARAM = 1
    COMMAND_COUNT = 1
    COMMAND_PARAM_DELIMITER = '-'
    COMMAND_ERROR_MSG = 'command error, run help command for command details.....'

    def command(self, args, options):
        commands = self.check_args(args, options)
        if commands is not None:
            for command in commands:
                command[self.COMMAND_OPTION](command[self.COMMAND_PARAM])
        else:
            return self.COMMAND_ERROR_MSG

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
                value = arg_param[self.COMMAND_PARAM] if param[self.COMMAND_COUNT] > 1 else None
                command.append(value)
            else:
                valid_commands = False
            commands.append(command)
        return None if not valid_commands or len(args) == 0 else commands

