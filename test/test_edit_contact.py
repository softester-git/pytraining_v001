# -*- coding: utf-8 -*-
from time import sleep
from model.contact import Contact
import random


def test_edit_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="NewFirstName", lname="NewLastName", addr="NewAddress"))
    old_contacts = db.get_contact_list()
    old_contacts_count = app.contact.count()
    index = random.choice(list(map(lambda x: x.id, old_contacts)))
    app.contact.edit_contact_by_index(Contact(fname="new_FirstName", lname="new_LastName", addr="new_Address"), index)
    sleep(1)
    assert old_contacts_count == app.contact.count()
