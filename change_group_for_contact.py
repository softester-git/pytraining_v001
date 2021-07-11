from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact
import random


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_change(db):
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    random_contact = random.choice(contacts)
    random_group = random.choice(groups)
    if db.check_relation(group=random_group, contact=random_contact):
        db.del_relation(random_group, random_contact)
    else:
        db.add_relation(random_group, random_contact)


db.connection.close()