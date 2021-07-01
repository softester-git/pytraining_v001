# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_name="group_name_1", group_header="group_header_1", group_footer="group_footer_1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_create_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_name="", group_header="", group_footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
