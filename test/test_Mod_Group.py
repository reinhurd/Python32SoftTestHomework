from model.group import Group
from random import randrange


def test_mod_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="EDITED44", header="EDITED444", footer="EDITED44")
    group.id = old_groups[index].id
    app.group.mod_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
