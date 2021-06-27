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
    app.login(user_name="admin", user_pass="secret")
    # Использование модели Contact
    app.fill_form(Contact(fname="Firstname", lname="Lastname", addr="address1", email="test@test.test"))
    app.logout()


def test_create_empty_contact(app):
    app.login(user_name="admin", user_pass="secret")
    # Использование модели Contact
    app.fill_form(Contact(fname="", lname="", addr="", email=""))
    app.logout()
