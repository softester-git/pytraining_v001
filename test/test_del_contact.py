from model.contact import Contact
import random
from time import sleep


def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    old_contacts = db.get_contact_list()
    old_contacts_count = app.contact.count()
    index = random.choice(list(map(lambda x: x.id, old_contacts)))
    app.contact.delete_contact_by_index(index)
    sleep(1)
    assert old_contacts_count - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    assert list(filter(lambda s: s.id != index, old_contacts)) == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
