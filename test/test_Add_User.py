# -*- coding: utf-8 -*-
from model.userinfo import UserInfo


def test_add_user(app):
    app.user.create(UserInfo(firstname="fds7773", middlename="fdgds7774", lastname="adgkasdfl5"))




