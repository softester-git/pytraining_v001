from model.contact import Contact
from time import sleep

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(fname="NewFirstName", lname="NewLastName", email3="newemail3@test.test", byear="2000"))
    sleep(1)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
