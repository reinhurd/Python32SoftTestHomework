# -*- coding: utf-8 -*-
from model.userinfo import UserInfo


def test_add_user(app):
    old_users = app.user.get_users_list()
    user = UserInfo(firstname="fds7773", lastname="adgkasdfl5", homephone=777, mobilephone=768, workphone=543789,
                    fax=888, phone2=654796, email="ghfdj@aa.ru", email2="fsdafsa@bb.ru", email3="42143@ru.ru")
    app.user.create(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=UserInfo.id_or_max) == sorted(new_users, key=UserInfo.id_or_max)





