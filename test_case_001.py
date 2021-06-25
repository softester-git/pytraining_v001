# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.login("admin")
    app.fill_group_form(Group(group_name="group_name_1", group_header="group_header_1", group_footer="group_footer_1"))
    app.logout()


def test_create_empty_group(app):
    app.login("admin")
    app.fill_group_form(Group(group_name="", group_header="", group_footer=""))
    app.logout()
