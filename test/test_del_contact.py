def test_delete_first_contact(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.contact.delete_first_contact()
    app.session.logout()
