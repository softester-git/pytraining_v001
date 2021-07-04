from model.group import Group
from random import randrange
from time import sleep

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    old_groups_count = app.group.count()
    old_groups = app.group.get_group_list()
    index = randrange(old_groups_count)
    app.group.delete_group_by_index(index)
    sleep(1)
    assert old_groups_count - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) is not sorted(new_groups, key=Group.id_or_max)

