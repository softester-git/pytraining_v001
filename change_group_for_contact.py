from fixture.db import DbFixture
from model.group import Group


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")


group_id = "594"
contact_id = "538"


cursor = db.connection.cursor()
check = cursor.execute("select id from address_in_groups where id="+contact_id+" and group_id="+group_id)
row = cursor.fetchall()
if len(row) == 0:
    cursor.execute("insert into address_in_groups (id, group_id, created) values ("+contact_id+", "+group_id+", now())")
else:
    cursor.execute("delete from address_in_groups where id="+contact_id+" and group_id="+group_id)
