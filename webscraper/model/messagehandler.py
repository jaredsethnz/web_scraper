

class MessageHandler(object):

    def check_none_condition(self, value, message):
        result = False
        if value is not None:
            result = True
        else:
            self.view.display_item(message)
        return result
