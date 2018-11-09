from model.group import Group


def test_mod_group(app):
    app.group.mod_first_group(Group(name="EDITED", header="EDITED", footer="EDITED"))

