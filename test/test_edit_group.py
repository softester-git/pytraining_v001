# -*- coding: utf-8 -*-
from model.group import Group
from time import sleep
from random import randrange

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    old_groups_count = app.group.count()
    index = randrange(len(old_groups))
    app.group.edit_group_by_index(Group(group_name="new_group", group_header="new_group_header", group_footer="new_group_footer"), index)
    sleep(1)
    new_groups_count = app.group.count()
    assert old_groups_count == new_groups_count

