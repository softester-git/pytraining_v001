# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.login(user="admin",passw="secret")
    app.fill_form(Contact(contact_title="title1", contact_company="company1", contact_address="address1"))
    app.logout()


def test_create_empty_contact(app):
    app.login(user="admin",passw="secret")
    app.fill_form(Contact(contact_title="", contact_company="", contact_address=""))
    app.logout()
