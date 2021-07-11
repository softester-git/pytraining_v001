# -*- coding: utf-8 -*-
from time import sleep
from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="NewFirstName", lname="NewLastName", addr="NewAddress"))
    old_contacts = db.get_contact_list()
    old_contacts_count = app.contact.count()
    id = random.choice(list(map(lambda x: x.id, old_contacts)))
    app.contact.edit_contact_by_id(Contact(fname="new_FirstName", lname="new_LastName", addr="new_Address"), id)
    sleep(1)
    assert old_contacts_count == app.contact.count()
    new_contacts = db.get_contact_list()
    listed_map = list(map(lambda s: Contact(id=id, fname="new_FirstName", lname="new_LastName", addr="new_Address") if s.id == str(id) else s, old_contacts))
    assert sorted(listed_map, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
