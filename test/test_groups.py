# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    old_groups_count = app.group.count()
    app.group.create(group)
    assert old_groups_count + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
