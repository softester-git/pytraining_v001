# -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address"))
    old_contacts_count = app.contact.count()
    index = randrange(old_contacts_count)
    app.contact.edit_contact_by_index(Contact(fname="new_FirstName", lname="new_LastName", addr="new_Address"), index)
    sleep(1)
    assert old_contacts_count == app.contact.count()
