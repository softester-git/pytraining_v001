# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [
    Contact(fname=fname, lname=lname, addr=addr)
    for fname in ["", random_string("first_name", 10)]
    for lname in ["", random_string("last_name", 10)]
    for addr in ["", random_string("address", 10)]
]

@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    old_contacts_count = app.contact.count()
    app.contact.create(contact)
    assert old_contacts_count + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
