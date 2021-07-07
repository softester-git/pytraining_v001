from model.group import Group
import random

def test_delete_some_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    old_groups = db.get_group_list()
    old_groups_count = app.group.count()
    index = random.choice(list(map(lambda x: x.group_id, old_groups)))
    app.group.delete_group_by_index(index)
    new_groups = db.get_group_list()
    assert old_groups_count - 1 == app.group.count()
    assert list(filter(lambda s: s.group_id != index, old_groups)) == new_groups
