from model.userinfo import UserInfo


def test_del_user(app):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", lastname=""))
    old_users = app.user.get_users_list()
    app.user.del_first_user()
    new_users = app.user.get_users_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[0:1] = []
    assert old_users == new_users


