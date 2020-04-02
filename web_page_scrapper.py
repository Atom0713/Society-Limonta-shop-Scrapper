# access names and subsections of the products, save those to db, and their urls, send it to scrap_items_meta to get each items metadata

import lxml as lxml
import pandas as pd
from urllib import urlopen
from bs4 import BeautifulSoup



class Scrapper:

    def __init__(self, url):
        self.url = url
        Scrapper.get_html(self)

    def get_html(self):
        #get html of the page
        html = urlopen(self.url)
        #create BeautifulSoup object
        soup = BeautifulSoup(html, 'lxml')
        type(soup)
        #shop name
        title = soup.title.string
        print(title)

        # TODO create List to hold all products wit hthe list of their sub products
        # get to the shop menu
        div_tags = soup.find_all("div", {"class": "MegaMenu__Item MegaMenu__Item--fit"})
        for div_tag in div_tags:
            # get each products name
            a_tag = div_tag.find("a", {"class":"MegaMenu__Title"})
            # get each products sub list of products
            items_list = div_tag.find("ul", {"class": "Linklist"})
            print ("Room: " + a_tag.text)

            # TODO create dictionary to save all items of the product dict = {a_tag.text: []}
            for li_tag in items_list:
                # get name of each sub product
                print("accessory: " + li_tag.text)
                print (li_tag.find("a").get("href") + "\n")
                # TODO save name of the product with its sub product names to the dictionary dict = {a_tag: [li_tag.text]}

                # TODO get url of each sub product and call scrap_items_meta to get information about all items in a sub product





        # TODO save name of the product and its sub product names to DB




