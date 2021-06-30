# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    app.group.edit_first_group(Group(group_name="new_group"))
