# -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    old_contacts_count = app.contact.count()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.edit_contact_by_index(Contact(fname="NewFirstName", lname="NewLastName", email3="newemail3@test.test", byear="2000"), index)
    sleep(1)
    assert old_contacts_count == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) != sorted(new_contacts, key=Contact.id_or_max)
