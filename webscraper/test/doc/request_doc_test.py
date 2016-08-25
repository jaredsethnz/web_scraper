

"""
>>> from webscraper.cli.command import Command
>>> cmd = Command()

>>> cmd.onecmd('request u--https://www.mightyape.co.nz/games/best-sellers')
setting url.....

>>> cmd.onecmd('request f')
fetching html from https://www.mightyape.co.nz/games/best-sellers.....

>>> cmd.onecmd('request up--http://www.mightyape.co.nz')
setting url padding.....

>>> cmd.onecmd('data g--div:class:product') # doctest: +ELLIPSIS
filtering data.....

>>> cmd.onecmd('data fu--a:class:title') # doctest: +ELLIPSIS
filtering urls.....
adding url.....

>>> cmd.onecmd('request rf') # doctest: +ELLIPSIS
fetching recursive html.....

>>> cmd.onecmd('data gr--div:class:productDetails') # doctest: +ELLIPSIS
filtering recursive data.....

>>> cmd.onecmd('data dk--a:class:title|span:class:price|div:class:format') # doctest: +ELLIPSIS
adding tag, class pair: ['a', 'class', 'title']
adding tag, class pair: ['span', 'class', 'price']
adding tag, class pair: ['div', 'class', 'format']

>>> cmd.onecmd('data cd--kw:0:0|child:0:0') # doctest: +ELLIPSIS
creating object.....

>>> cmd.onecmd('data s--best_selling_gaming.pickle')


>>> cmd.onecmd('graph d--format')
gathering data.....

>>> cmd.onecmd('graph g--format')
displaying graph.....

"""


def test():
    import doctest
    return doctest.testmod(verbose=True)

if __name__ == "__main__":
    test()
