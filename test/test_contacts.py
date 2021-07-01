# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_create_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(fname="", lname="", addr="", email=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
