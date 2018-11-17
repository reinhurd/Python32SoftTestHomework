from model.group import Group


def test_mod_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    old_groups = app.group.get_group_list()
    group = Group(name="EDITED44", header="EDITED444", footer="EDITED44")
    group.id = old_groups[0].id
    app.group.mod_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
