# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.group.edit_first_group(Group(group_name="new_group"))
    app.session.logout()
