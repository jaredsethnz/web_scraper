"""
>>> from webscraper.cli.command import Command
>>> cmd_test_2 = Command()

# ----------Test command or data input errors...----------

>>> cmd_test_2.onecmd('request f')
fetching html from .....
data fetch error.....

>>> cmd_test_2.onecmd('request rf')
no recursive urls set.....

>>> cmd_test_2.onecmd('request u--mightyape.co.nz')
please enter a valid url.....

>>> cmd_test_2.onecmd('request up--mightyape.co.nz')
please enter a valid url.....

>>> cmd_test_2.onecmd('request ur--mightyape.co.nz')
please enter a valid url.....

>>> cmd_test_2.onecmd('data g--div:class:product')
command error, run help command for command details.....

>>> cmd_test_2.onecmd('data gr--div:class:productDetails')

>>> cmd_test_2.onecmd('data cd--kw:0:0|child:0:0')

>>> cmd_test_2.onecmd('data wo')
displaying web data objects.....
----------------------------------------------------------------

>>> cmd_test_2.onecmd('graph d--format')
gathering data.....

>>> cmd_test_2.onecmd('request')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('request p--blah')

>>> cmd_test_2.onecmd('request u')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('request up')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('request f--')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('request rf--test')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('request u')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('data')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('data p--hmmmmm')

>>> cmd_test_2.onecmd('data l--')
loading saved data.....
File  not found.....

>>> cmd_test_2.onecmd('data s')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('data g--nothing')
command error, run help command for command details.....
command error, run help command for command details.....

>>> cmd_test_2.onecmd('data gr--norecursive')
command error, run help command for command details.....
command error, run help command for command details.....

>>> cmd_test_2.onecmd('data cf--extra')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('data fu--a:blah')
command error, run help command for command details.....
command error, run help command for command details.....

>>> cmd_test_2.onecmd('data dk--a:blah|div:class:test')
command error, run help command for command details.....

>>> cmd_test_2.onecmd('data rdk--a:blah:place|div:test')
command error, run help command for command details.....

>>> cmd_test_2.onecmd('data cd--hmm:place|div:test')
command error, run help command for command details.....

>>> cmd_test_2.onecmd('data ds--files')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('graph')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('graph d')
*** Unknown syntax: command error, run help command for command details.....

>>> cmd_test_2.onecmd('graph g')
*** Unknown syntax: command error, run help command for command details.....

"""


def test_command_error():
    import doctest
    return doctest.testmod(verbose=True)


if __name__ == "__main__":
    test_command_error()
