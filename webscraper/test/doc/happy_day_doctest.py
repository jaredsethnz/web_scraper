"""
>>> from webscraper.cli.command import Command
>>> cmd_test_1 = Command()

# ----------Test Happy Day Scenario----------

>>> cmd_test_1.onecmd('request u--https://www.mightyape.co.nz/games/best-sellers')
setting url.....

>>> cmd_test_1.onecmd('request f')
fetching html from https://www.mightyape.co.nz/games/best-sellers.....

>>> cmd_test_1.onecmd('request up--http://www.mightyape.co.nz')
setting url padding.....

>>> cmd_test_1.onecmd('data g--div:class:product')  # doctest: +ELLIPSIS
filtering data.....

>>> cmd_test_1.onecmd('data fu--a:class:title')  # doctest: +ELLIPSIS
filtering urls.....
adding url.....

>>> cmd_test_1.onecmd('request rf')  # doctest: +ELLIPSIS
fetching recursive html.....

>>> cmd_test_1.onecmd('data gr--div:class:productDetails')  # doctest: +ELLIPSIS
filtering recursive data.....

>>> cmd_test_1.onecmd('data dk--a:class:title|span:class:price|div:class:format')  # doctest: +ELLIPSIS
adding tag, class pair: ['a', 'class', 'title']
adding tag, class pair: ['span', 'class', 'price']
adding tag, class pair: ['div', 'class', 'format']

>>> cmd_test_1.onecmd('data cd--kw:0:0|child:0:0')  # doctest: +ELLIPSIS
creating object.....

>>> cmd_test_1.onecmd('data s--best_selling_gaming.pickle')
saving data to disk.....

>>> cmd_test_1.onecmd('data ds')
displaying file save locations.....
-----------------------------------------------------------------
<BLANKLINE>
/Users/Seth/GitHub/web_scraper/webscraper/test/doc/best_selling_gaming.pickle
<BLANKLINE>
-----------------------------------------------------------------
<BLANKLINE>

>>> cmd_test_1.onecmd('data cf')
clearing filtered data.....

>>> cmd_test_1.onecmd('data wo')
displaying web data objects.....
----------------------------------------------------------------

>>> cmd_test_1.onecmd('data l--best_selling_gaming.pickle')
loading saved data.....

>>> cmd_test_1.onecmd('graph d--format')
gathering data.....

>>> cmd_test_1.onecmd('graph g--format')
displaying graph.....
"""


def test_happy_day():
    import doctest
    return doctest.testmod(verbose=True)


if __name__ == "__main__":
    test_happy_day()
