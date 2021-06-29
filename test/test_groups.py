# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    app.group.create(Group(group_name="group_name_1", group_header="group_header_1", group_footer="group_footer_1"))


def test_create_empty_group(app):
    app.group.create(Group(group_name="", group_header="", group_footer=""))
