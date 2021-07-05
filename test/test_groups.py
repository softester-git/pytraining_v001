# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(group_name=group_name if group_name!="" else None, group_header=group_header if group_header!="" else None, group_footer=group_footer if group_footer!="" else None)
    for group_name in ["", random_string("name", 10)]
    for group_header in ["", random_string("header", 20)]
    for group_footer in ["", random_string("footer", 20)]
]

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_create_group(app, group):
    old_groups = app.group.get_group_list()
    old_groups_count = app.group.count()
    app.group.create(group)
    assert old_groups_count + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
