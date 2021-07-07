from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        group_name = None if group.group_name is None else group.group_name.strip()
        return Group(group_id=group.group_id, group_name=group_name)
    db_list = list(map(clean, db.get_group_list()))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)