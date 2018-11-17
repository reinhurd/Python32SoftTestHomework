from model.userinfo import UserInfo


def test_mod_user(app):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", lastname="TEST"))
    old_users = app.user.get_users_list()
    user_mod = UserInfo(firstname="EDITED44", lastname="EDITED44")
    app.user.mod_first_user(user_mod)
    new_users = app.user.get_users_list()
    assert len(old_users) == len(new_users)
    old_users[0] = user_mod
    assert sorted(old_users, key=UserInfo.id_or_max) == sorted(new_users, key=UserInfo.id_or_max)
