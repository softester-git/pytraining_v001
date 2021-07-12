# -*- coding: utf-8 -*-
from model.group import Group
import pytest


def test_create_group(app, db, check_ui, json_groups):
    group = json_groups
    with pytest.allure.steps("Given a group list"):
        old_groups = db.get_group_list()
    with pytest.allure.steps("When I add the group to the list"):
        app.group.create(group)
    with pytest.allure.steps("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
