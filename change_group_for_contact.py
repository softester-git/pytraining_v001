from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact
import random
#from time import sleep

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_change(db, app):
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    random_contact = random.choice(contacts)
    random_group = random.choice(groups)
    if db.check_relation(group=random_group, contact=random_contact):
        db.del_relation(group=random_group, contact=random_contact)
        #app.contact.del_relation(group=random_group, contact=random_contact)
        check = db.check_relation(group=random_group, contact=random_contact)
        assert check is False
    else:
        print(random_group)
        app.contact.add_relation(group=random_group, contact=random_contact)
        check = db.check_relation(group=random_group, contact=random_contact)
        assert check is True


db.connection.close()