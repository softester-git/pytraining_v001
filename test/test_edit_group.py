# -*- coding: utf-8 -*-
from time import sleep
from model.group import Group
import random


def test_edit_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    old_groups = db.get_group_list()
    old_groups_count = app.group.count()
    index = random.choice(list(map(lambda x: x.group_id, old_groups)))
    app.group.edit_group_by_index(Group(group_name="new_group", group_header="new_group_header", group_footer="new_group_footer"), index)
    sleep(1)
    assert old_groups_count == app.group.count()
