
def automate_webscraper():
    from webscraper.cli.command import Command
    input = Command()

    # Set url
    input.onecmd('request u--https://www.mightyape.co.nz'
                 '/dvds-blu-ray/best-sellers')

    # Set recursive url padding (This is needed because when we filter the
    # product page urls they aren't full paths)
    input.onecmd('request up--https://www.mightyape.co.nz')

    # Fetch url data
    input.onecmd('request f')

    # Filter the data we want from the request data
    input.onecmd('data g--div:class:product')

    # Filter all the urls for the products (best selling blu-ray & DVDs) so we
    # can get the extra data on those pages
    input.onecmd('data fu--a:class:title')

    # Recursive fetch all the data from the filtered urls
    input.onecmd('request rf')

    # Filter all the data we want from the recursive url fetch
    input.onecmd('data gr--div:class:productDetails')

    # Add keywords by which we can filter the main data (This can also be done
    # for recursive but not for MightyApe)
    input.onecmd('data dk--a:class:title|div:class:format|span:class:price')

    # Consolidate all this data into objects -- kw specifies to filter the
    # primary fetch by keywords, the second specifies to filter the recursive
    # data by children ignoring keywords Ignore the trailing zeros for now,
    # they are needed but not used in this iteration
    input.onecmd('data cd--kw:0:0|child:0:0')

    # Display all the created objects
    input.onecmd('data wo')

    # Save the objects
    input.onecmd('data s--dvd_bluray_bestsellers.pickle')

    # Display saves
    input.onecmd('data ds')

    # Load the save
    input.onecmd('data l--dvd_bluray_bestsellers.pickle')

    # Set graph data -- for the second argument, you pass the name
    # of an attribute stored in the created objects eg. genre
    # Note not all objects contain all attributes, but the program will
    # automatically handle this
    input.onecmd('graph d--countryofproduction')

    # Display the graph -- the second argument here is the title for the graph
    input.onecmd('graph g--CountryProduction')

    # Set graph data to format
    input.onecmd('graph d--format')

    # Display the graph -- the second argument here is the title for the graph
    input.onecmd('graph g--FormatSales')

    # Set graph data to genre
    input.onecmd('graph d--genre')

    # Display the graph -- the second argument here is the title for the graph
    input.onecmd('graph g--GenreSales')

if __name__ == "__main__":
    automate_webscraper()
