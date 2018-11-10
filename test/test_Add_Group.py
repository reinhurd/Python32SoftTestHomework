# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="gfd77d", header="sdf77gdd", footer="sdf77dg"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

