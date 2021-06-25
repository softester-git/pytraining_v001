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
    app.login(user_name="admin", user_pass="secret")
    app.fill_group_form(Group(group_name="group_name_001", group_header="group_header_001", group_footer="group_footer_001"))
    app.logout()


def test_create_empty_group(app):
    app.login(user_name="admin", user_pass="secret")
    app.fill_group_form(Group(group_name="", group_header="", group_footer=""))
    app.logout()
