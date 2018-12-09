from model.group import Group
import random


def test_mod_group_by_id(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edit_group = Group(name="EDITED44", header="EDITED444", footer="EDITED44")
    app.group.mod_group_by_id(group.id, edit_group)
    new_groups = db.get_group_list()
    #assert len(old_groups) == len(new_groups)
    pos = old_groups.index(group)
    old_groups[pos] = edit_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
