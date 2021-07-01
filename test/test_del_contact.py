from model.contact import Contact


def test_delete_first_contact(app):
    #if app.contact.count() == 0:
    #    app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    old_contacts = app.contact.get_contact_list()
    print(old_contacts)
    #app.contact.delete_first_contact()
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) - 1 == len(new_contacts)

