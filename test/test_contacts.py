# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    app.session.logout()


def test_create_empty_contact(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.contact.create(Contact(fname="", lname="", addr="", email=""))
    app.session.logout()
