from urllib import urlopen
from bs4 import BeautifulSoup
# get url of the page containing product items, scrap items metadata and save to DB
class ScrapMetadata:

    def __init__(self):
        pass
        
    def scrap_items(self, url):
        #get html of the page
        html = urlopen(url)
        #create BeautifulSoup object
        soup = BeautifulSoup(html, 'lxml')

        items_list = []

        # TODO access items metadata using soup.

        item = {"name": "pluto", "price": 250, "width": 200}
        items_list.append(item)
        items_list.append(item)

        return items_list

