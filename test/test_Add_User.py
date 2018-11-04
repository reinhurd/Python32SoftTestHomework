# -*- coding: utf-8 -*-
from model.userinfo import UserInfo


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.newuser.create(UserInfo(firstname="fdsafsadf3", middlename="fdgdsgffd4", lastname="adgkasdfl5"))
    app.session.logout()



