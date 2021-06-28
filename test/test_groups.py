# -*- coding: utf-8 -*-
from model.group import Group
import time

def test_create_group(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.group.create(Group(group_name="group_name_1", group_header="group_header_1", group_footer="group_footer_1"))
    app.session.logout()
    time.sleep(3)

def test_create_empty_group(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.group.create(Group(group_name="", group_header="", group_footer=""))
    app.session.logout()
