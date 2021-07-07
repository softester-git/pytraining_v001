from model.group import Group
from random import randrange

def test_delete_some_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(group_name="Test"))
    old_groups = db.get_group_list()
    old_groups_count = app.group.count()
    index = randrange(old_groups_count)
    deleted_group_id = old_groups[index].group_id
    app.group.delete_group_by_index(index)
    new_groups = db.get_group_list()
    assert old_groups_count - 1 == app.group.count()
    eq_old_groups = []

    for gr in old_groups:
        if gr.group_id != deleted_group_id:
            eq_old_groups.append(Group(group_id=gr.group_id, group_name=gr.group_name))
    assert eq_old_groups == new_groups
