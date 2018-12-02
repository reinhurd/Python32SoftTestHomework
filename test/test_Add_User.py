# -*- coding: utf-8 -*-
from model.userinfo import UserInfo


def test_add_user(app, json_userinfos):
    user = json_userinfos
    old_users = app.user.get_users_list()
    app.user.create(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=UserInfo.id_or_max) == sorted(new_users, key=UserInfo.id_or_max)





