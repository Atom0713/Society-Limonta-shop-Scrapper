import sys
from errno import errorcode
import mysql.connector as mysql_con
from mysql.connector.errors import Error

db_name = "limonta_online_shop_db"

tables_names = ("rooms", "room_accessories", "items")

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'HackMeNoMySQL13',
    'database': '{}'.format(db_name),
    'raise_on_warnings': True
}


class DBManagement:

    # TODO establish DB connection. Create checks for non existing tables. Create function to populate DB

    def __init__(self, shop_list):
        self.shop_list = shop_list
        self.db_con = None
        
        self.db_connection()
        self.tables_exist()



        #self.save_data()

        self.db_con.close()

    def db_connection(self):
        try:
            self.db_con = mysql_con.connect(**config)
            return True
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                sys.exit()
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                self.create_database()
            else:
                print (err)

    def create_database(self):
        try:
            cursor = self.db_con.cursor()
            cursor.execute("CREATE DATABASE {}".format(db_name))
        except Error as err:
            print ("Something went wrong: {}".format(err))
            sys.exit()



    def tables_exist(self):
        for table in tables_names:
            try:
                cursor = self.db_con.cursor()
                cursor.execute("DROP TABLE {}".format(table))
            except Error as err:
                if err.errno == errorcode.ER_BAD_TABLE_ERROR:
                    print("Creating table spam")
                    self.create_table()
                else:
                    raise


    def create_table(self):
        pass

    def save_data(self):
        # for y in self.shop_list:
        #     for x in y:
        #         print ("\nRoom: " + x)
        #         for z in y[x]:
        #             for a in z:
        #                 print ("accessory: " + a)
        #                 for b in z[a]:
        #                     for c in b:
        #                         value = b[c]
        #                         print ("items meta: " + c + "->" + str(value))
        #                     print ("\n")
        pass








