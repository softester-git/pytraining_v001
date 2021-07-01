# -*- coding: utf-8 -*-
from model.group import Group
from sys import maxsize


def test_create_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="group_name_1", group_header="group_header_1", group_footer="group_footer_1")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    def id_or_max(gr):
        if gr.group_id:
            return int(gr.group_id)
        else:
            return maxsize
    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)



def test_create_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(group_name="", group_header="", group_footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
