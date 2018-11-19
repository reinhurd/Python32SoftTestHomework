from model.userinfo import UserInfo
from random import randrange


def test_mod_user_by_index(app):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", lastname="TEST"))
    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    user_mod = UserInfo(firstname="EDITED4466", lastname="EDITED4466")
    user_mod.id = old_users[index].id
    app.user.mod_user_by_index(index, user_mod)
    new_users = app.user.get_users_list()
    assert len(old_users) == len(new_users)
    old_users[index] = user_mod
    assert sorted(old_users, key=UserInfo.id_or_max) == sorted(new_users, key=UserInfo.id_or_max)
