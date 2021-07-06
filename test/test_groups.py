# -*- coding: utf-8 -*-
from model.group import Group
from time import sleep
import pytest
from data.add_group import test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_create_group(app, group):
    old_groups = app.group.get_group_list()
    old_groups_count = app.group.count()
    app.group.create(group)
    #app.wd.find_element_by_name("new")
    assert old_groups_count + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
