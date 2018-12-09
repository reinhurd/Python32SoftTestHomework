# -*- coding: utf-8 -*-
from model.userinfo import UserInfo


def test_add_user(app, db, json_userinfos, check_ui):
    user = json_userinfos
    old_users = db.get_userinfo_list()
    app.user.create(user)
    new_users = db.get_userinfo_list()
    old_users.append(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(old_users, key=UserInfo.id_or_max) == sorted(new_users, key=UserInfo.id_or_max)





