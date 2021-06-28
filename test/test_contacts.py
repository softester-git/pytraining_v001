# -*- coding: utf-8 -*-
from model.contact import Contact
from time import sleep

def test_create_contact(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.contact.create(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    app.session.logout()
    sleep(3)


def test_create_empty_contact(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.contact.create(Contact(fname="", lname="", addr="", email=""))
    app.session.logout()
    sleep(3)
