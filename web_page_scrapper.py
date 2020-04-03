# access names and subsections of the products, save those to db, and their urls, send it to scrap_items_meta to get each items metadata
from urllib import urlopen
from bs4 import BeautifulSoup
from scrap_metadata import ScrapMetadata as Sm

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

        shopping_list = []
        # get to the shop menu
        div_tags = soup.find_all("div", {"class": "MegaMenu__Item MegaMenu__Item--fit"})
        for div_tag in div_tags:
            # get each products name
            room_link = div_tag.find("a", {"class":"MegaMenu__Title"})
            room_name = room_link.text.strip()
            # get each products sub list of products
            items_list = div_tag.find("ul", {"class": "Linklist"})

            room_products_list = []
            for li_tag in items_list:
                # get name of each sub product
                room_product_name = li_tag.text.strip()

                link = self.url + li_tag.find("a").get("href").strip()

                # returns a list of products, where each item in the list is a dictionary,
                # that contains a single product metadata.
                items_list = Sm().scrap_items(link)
                # associate a list of items with a product name
                if room_product_name != "View all":
                    room_product_items_dict = {room_product_name: items_list}
                    #add a product that contains a list of items to the list of products
                    room_products_list.append(room_product_items_dict)
            # add
            rooms_dict = {room_name: room_products_list}
            shopping_list.append(rooms_dict)

        for y in shopping_list:
            for x in y:
                print ("\nRoom: " + x)
                for z in y[x]:
                    for a in z:
                        print ("accessory: " + a)
                        for b in z[a]:
                            for c in b:
                                value = b[c]
                                print ("items meta: " + c + "->" + str(value))
                            print "\n"

        return shopping_list



        # TODO save name of the product and its sub product names to DB




