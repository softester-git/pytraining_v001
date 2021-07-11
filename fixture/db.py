#import pymysql.cursors
import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
#        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        cursor = self.connection.cursor()
        try:
            list = []
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                id = row[0] if row[0] != "" else None
                name = row[1] if row[1] != "" else None
                header = row[2] if row[2] != "" else None
                footer = row[3] if row[3] != "" else None
                list.append(Group(group_id=str(id), group_name=name, group_header=header, group_footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        cursor = self.connection.cursor()
        try:
            list = []
            cursor.execute("select id, firstname, lastname, address, home, work, mobile, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                id = row[0] if row[0] != "" else None
                firstname = row[1] if row[1] != "" else None
                lastname = row[2] if row[2] != "" else None
                address = row[3] if row[3] != "" else None
                home = row[4] if row[4] != "" else None
                work = row[5] if row[5] != "" else None
                mobile = row[6] if row[6] != "" else None
                phone2 = row[7] if row[7] != "" else None
                all_phones = str(home) + "\n" + str(work) + "\n" + str(mobile) + "\n" + str(phone2)
                list.append(Contact(id=str(id), fname=firstname if firstname != "" else None, lname=lastname if lastname != "" else None, addr=address if address != "" else None, all_phones=all_phones))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
