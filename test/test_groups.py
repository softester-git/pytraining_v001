# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.fill_group_form(Group(group_name="group_name_1", group_header="group_header_1", group_footer="group_footer_1"))
    app.session.logout()


def test_create_empty_group(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.fill_group_form(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()
