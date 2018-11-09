# -*- coding: utf-8 -*-
from model.userinfo import UserInfo


def test_add_user(app):
    app.user.create(UserInfo(firstname="fdsafsadf3", middlename="fdgdsgffd4", lastname="adgkasdfl5"))




