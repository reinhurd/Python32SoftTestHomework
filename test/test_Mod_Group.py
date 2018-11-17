from model.group import Group


def test_mod_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    app.group.mod_first_group(Group(name="EDITED44", header="EDITED444", footer="EDITED44"))
    new_group = app.group.get_group_list()
    assert len(old_groups) == len(new_group)
