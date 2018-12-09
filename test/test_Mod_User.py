from model.userinfo import UserInfo
import random


def test_mod_user_by_id(app, db, check_ui):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", lastname="TEST"))
    old_users = db.get_userinfo_list()
    user = random.choice(old_users)
    user_mod = UserInfo(firstname="EDITED4466", lastname="EDITED4466")
    app.user.mod_user_by_id(user.id, user_mod)
    new_users = db.get_userinfo_list()
    #assert len(old_users) == len(new_users)
    pos = old_users.index(user)
    old_users[pos] = user_mod
    assert old_users == new_users
    if check_ui:
        assert sorted(old_users, key=UserInfo.id_or_max) == sorted(new_users, key=UserInfo.id_or_max)
