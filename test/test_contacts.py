# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_create_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(fname="", lname="", addr="", email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
