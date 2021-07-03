from model.group import Group
from random import randrange
from time import sleep

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    sleep(1)
    new_groups = app.group.get_group_list()
#    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
#    assert old_groups == new_groups

