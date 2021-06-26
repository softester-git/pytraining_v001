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
    app.login(user_name="admin",user_pass="secret")
    # Использование модели Contact
    app.fill_form(Contact(contact_title="title1", contact_company="company1", contact_address="address1"))
    app.logout()


def test_create_empty_contact(app):
    app.login(user_name="admin",user_pass="secret")
    # Использование модели Contact
    app.fill_form(Contact(contact_title="", contact_company="", contact_address=""))
    app.logout()
