from model.group import Group


def test_del_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test", header="", footer=""))
    app.group.del_first_group()
    app.open_home_page()
