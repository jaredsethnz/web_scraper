class ConsoleView(object):
    """
    Console view handles all output to console.
    """

    def display_item(self, item):
        print(item)

    def display_items(self, items):
        print(
            '-----------------------------------'
            '------------------------------\n')
        for item in items:
            print(item)
            print(
                '\n--------------------------------'
                '---------------------------------\n')
