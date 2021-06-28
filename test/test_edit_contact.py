from model.contact import Contact


def test_delete_first_group(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.contact.edit_first_contact(Contact(fname="FirstN", lname="LastN", addr="Addr", email="test@test.te"))
    app.session.logout()
