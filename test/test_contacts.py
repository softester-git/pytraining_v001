# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.session.login(user_name="admin", user_pass="secret")
    # Использование модели Contact
    app.fill_contact_form(Contact(fname="FirstName", lname="LastName", addr="Address", email="test@test.test"))
    app.session.logout()


#def test_create_empty_contact(app):
#    app.session.login(user_name="admin", user_pass="secret")
    # Использование модели Contact
#    app.fill_contact_form(Contact(fname="", lname="", addr="", email=""))
#    app.session.logout()
