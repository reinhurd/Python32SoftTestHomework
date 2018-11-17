# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="gfd77d", header="sdf77gdd", footer="sdf77dg"))
    new_group = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_group)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_group = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_group)

