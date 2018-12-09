from model.group import Group
from model.userinfo import UserInfo


def test_group_list_compare_ui_and_db(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test", header="Test", footer="Test"))
    ui_group = app.group.get_group_list()
    db_groups = db.get_group_list()
    assert sorted(ui_group, key=Group.id_or_max) == sorted(db_groups, key=Group.id_or_max)


def test_contacts_list_compare_ui_and_db(app, db):
    if len(db.get_userinfo_list()) == 0:
        app.user.create(UserInfo(firstname="Test", lastname="TEST"))
    db_users = db.get_userinfo_list()
    ui_users = app.user.get_users_list()
    assert sorted(ui_users, key=UserInfo.id_or_max) == sorted(db_users, key=Group.id_or_max)
