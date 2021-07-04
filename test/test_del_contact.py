from model.contact import Contact
from time import sleep
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    old_contacts_count = app.contact.count()
    old_contacts = app.contact.get_contact_list()
    index = randrange(old_contacts_count)
    app.contact.delete_contact_by_index(index)
    sleep(1)
    assert old_contacts_count - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) is not sorted(new_contacts, key=Contact.id_or_max)
