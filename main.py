from web_page_scrapper import Scrapper
from db_controller import DBManagement as Db


class Main:

    def __init__(self):
        shopping_list = Scrapper("https://uk.societylimonta.com")

        # TODO perform db management operations in DBManagement class
        if Db().tables_exist():
            Db().save_data()
        else:
            Db().create_tables()
            Db().save_data()






Main()