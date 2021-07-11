# -*- coding: utf-8 -*-
from time import sleep
from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if len(old_contacts) == 0:
        app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
        old_contacts_count = 1
    else
        old_contacts_count = len(old_contacts)
    id = random.choice(list(map(lambda x: x.id, old_contacts)))
    app.contact.edit_contact_by_id(Contact(fname="new_FirstName", lname="new_LastName", addr="new_Address"), id)
    sleep(1)
    assert old_contacts_count == app.contact.count()
    new_contacts = db.get_contact_list()
    listed_map = list(map(lambda s: Contact(id=id, fname="new_FirstName", lname="new_LastName", addr="new_Address") if s.id == str(id) else s, old_contacts))
    assert sorted(listed_map, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
