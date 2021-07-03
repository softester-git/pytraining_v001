# -*- coding: utf-8 -*-
from model.group import Group
from time import sleep

def test_create_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="group_name_1", group_header="group_header_1", group_footer="group_footer_1")
    app.group.create(group)
#    assert len(old_groups) + 1 == app.group.count()
    sleep(1)
    new_groups = app.group.get_group_list()
    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_create_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(group_name="", group_header="", group_footer="")
    app.group.create(group)
#    assert len(old_groups) + 1 == app.group.count()
    sleep(1)
    new_groups = app.group.get_group_list()
    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
