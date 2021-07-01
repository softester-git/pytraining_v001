# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(group_name="new_group", group_header="new_group_header", group_footer="new_group_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)