# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    old_contacts_count = app.contact.count()
    app.contact.create(contact)
    assert old_contacts_count + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
