#import pymysql.cursors
import mysql.connector
from model.group import Group


class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
#        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def get_group_list(self):
        cursor = self.connection.cursor()
        try:
            list = []
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                id = row[0] if row[0] != "" else None
                name = row[1] if row[1] != "" else None
                header = row[2] if row[2] != "" else None
                footer = row[3] if row[3] != "" else None
                list.append(Group(group_id=str(id), group_name=name, group_header=header, group_footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
