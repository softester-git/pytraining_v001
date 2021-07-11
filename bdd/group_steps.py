from pytest_bdd import given, when, then
from model.group import Group
import random
from time import sleep

@given("a group list")
def group_list(db):
    return db.get_group_list()

@given("a group with <name>, <header> and <footer>")
def new_group_list(name, header, footer):
    return Group(group_name=name, group_header=header, group_footer=footer)

@when("I add the group to the list")
def add_new_group(app, new_group_list):
    app.group.create(new_group_list)

@then("the new group list is equal to the old list with the added group")
def verify_group_added(db, app, group_list, new_group_list):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group_list)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

@given("a non-empty group list")
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="GroupName", group_header="GroupHeader", group_footer="GroupFooter"))
    return db.get_group_list()

@given("a random group from the list")
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when("I delete the group from the list")
def delete_group(app, random_group):
    app.group.delete_group_by_id(str(random_group.group_id))

@then("the new group list equal to the old list without the deleted group")
def verify_group_deleted(app, db, non_empty_group_list, random_group, check_ui):
    new_groups = db.get_group_list()
    assert len(non_empty_group_list) - 1 == len(new_groups)
    assert list(filter(lambda s: s.group_id != random_group.group_id, non_empty_group_list)) == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)