from model.contact import Contact
import os


def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(fname="NewFirstName", lname="NewLastName", photo=os.path.abspath('test/facebook.png'), email3="newemail3@test.test", byear="2000"))
