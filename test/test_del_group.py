from model.group import Group
from random import randrange
from time import sleep

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    old_groups_count = app.group.count()
    index = randrange(old_groups_count)
    app.group.delete_group_by_index(index)
    sleep(1)
    assert old_groups_count - 1 == app.group.count()

