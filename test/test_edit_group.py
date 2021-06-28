# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.session.login(user_name="admin", user_pass="secret")
    app.group.edit_first_group(Group(group_name="group_name_2", group_header="group_header_2", group_footer="group_footer_2"))
    app.session.logout()
