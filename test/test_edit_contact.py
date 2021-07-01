from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    app.contact.edit_first_contact(Contact(fname="NewFirstName", lname="NewLastName", email3="newemail3@test.test", byear="2000"))
