import sys
from errno import errorcode
import mysql.connector as mysql_con
from mysql.connector.errors import Error

db_name = "limonta_online_shop_db"

tables_names = ("rooms", "room_accessories", "items")

# db and user information
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

        print (self.db_connection())



        # if self.db_connection() == errorcode.ER_BAD_DB_ERROR:
        #     print ("yes")
        #     self.create_database()
        #     self.create_tables()
        # elif not self.tables_exist():
        #     self.create_tables()
        #     # self.save_data()
        # else:
        #     pass
        #     # TODO create update_tables function that will empty existng tables and populate them with newly extracted data.

        self.db_con.close()

    def db_connection(self):
        try:
            self.db_con = mysql_con.connect(**config)
        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                sys.exit()
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                return err.errno
            else:
                print (err)

    def create_database(self):
        try:
            cursor = self.db_con.cursor()
            cursor.execute("CREATE DATABASE {}".format(db_name))
        except Error as err:
            print ("Something went wrong: {}".format(err))
            sys.exit()


#############################################################################################
    def tables_exist(self):
        # TODO check mysql documentation. Find the best way you think suits this procedure.
        for table in tables_names:
            try:
                cursor = self.db_con.cursor()
                cursor.execute("DROP TABLE {}".format(table))
            except Error as err:
                if err.errno == errorcode.ER_BAD_TABLE_ERROR:
                    print("Creating table {}".format(table))
                else:
                    raise
#############################################################################################

    def create_tables(self):
        for table in tables_names:
            try:
                cursor = self.db_con.cursor()
                cursor.execute("{}".format(self.get_table_structure(table)))
            except Error as err:
                print()


    def get_table_structure(self, argument):
        # TODO adjust tables intialization sql script.

        tables_structures = {}
        tables_structures ["rooms"]  = (
                        "CREATE TABLE `rooms` ("
                        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
                        "  `birth_date` date NOT NULL,"
                        "  `first_name` varchar(14) NOT NULL,"
                        "  `last_name` varchar(16) NOT NULL,"
                        "  `gender` enum('M','F') NOT NULL,"
                        "  `hire_date` date NOT NULL,"
                        "  PRIMARY KEY (`emp_no`)")

        tables_structures["rooms_accessories"]  =  (
                        "CREATE TABLE `rooms_accessories` ("
                        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
                        "  `birth_date` date NOT NULL,"
                        "  `first_name` varchar(14) NOT NULL,"
                        "  `last_name` varchar(16) NOT NULL,"
                        "  `gender` enum('M','F') NOT NULL,"
                        "  `hire_date` date NOT NULL,"
                        "  PRIMARY KEY (`emp_no`)")

        tables_structures["items"]  =  (
                        "CREATE TABLE `items` ("
                        "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
                        "  `birth_date` date NOT NULL,"
                        "  `first_name` varchar(14) NOT NULL,"
                        "  `last_name` varchar(16) NOT NULL,"
                        "  `gender` enum('M','F') NOT NULL,"
                        "  `hire_date` date NOT NULL,"
                        "  PRIMARY KEY (`emp_no`)")

        return tables_structures.get(argument)





###########################################################################
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
###########################################################################







