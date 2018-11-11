from model.group import Group


def test_mod_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    app.group.mod_first_group(Group(name="EDITED44", header="EDITED444", footer="EDITED44"))

