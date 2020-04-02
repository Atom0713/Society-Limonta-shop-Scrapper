import lxml as lxml
import pandas as pd
from urllib import urlopen
from bs4 import BeautifulSoup
# get url of the page containing product items, scrap items metadata and save to DB
class ScrapMetadata:

    def __init__(self, url):
        self.url = url
        
    def scrap_items(self):
        #get html of the page
        html = urlopen(self.url)
        #create BeautifulSoup object
        soup = BeautifulSoup(html, 'lxml')
        