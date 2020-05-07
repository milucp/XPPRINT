XPPRINT
=======

pretty-print of html


GETTING STARTED
---------------

    $ pip install xpprint
    $ curl -s http://www.pythonscraping.com/pages/page3.html | xpprint
    -html
    | -head
    | | -style
    | -body
    | | -div#wrapper
    | | | -img
    | | | -h1
    | | | -div#content
    | | | -table#giftList
    | | | | -tr
    | | | | | -th
    | | | | | -th
    | | | | | -th
    | | | | | -th
    | | | | -tr.gift#gift1
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | | -img
    | | | | -tr.gift#gift2
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | | -img
    | | | | -tr.gift#gift3
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | | -img
    | | | | -tr.gift#gift4
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | | -img
    | | | | -tr.gift#gift5
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | -td
    | | | | | | -img
    -div#footer


USAGE
-----

    $ xpprint -h
    usage: xpprint [-h] [--filter [FILTER]] [--parser PARSER] [--source] [html]
    
    html tree view pprint
    
    positional arguments:
      html               stdin or .html filename
    
    optional arguments:
      -h, --help         show this help message and exit
      --filter [FILTER]  filtered tag names (default: ['p', 'br', 'span'])
      --parser PARSER    HTML parser name (default: html.parser)
      --source           add "sourceline, pos" of corresponding start-tags


IMPORTANT LINKS
---------------

- The Tree Command for Linux Homepage -
  http://mama.indstate.edu/users/ice/tree/

- Collecting More Data from the Modern Web | Web Scraping with Python -
  http://www.pythonscraping.com/
