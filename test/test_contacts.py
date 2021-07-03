# -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test", phone2="002", home="003", work="004", mobile="005")
    app.contact.create(contact)
#    assert len(old_contacts) + 1 == app.contact.count()
    sleep(1)
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_create_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test")
    app.contact.create(contact)
#    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
