# -*- coding: utf-8 -*-
import pytest
from application import Application
from userinfo import UserInfo


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.create_new_user(UserInfo(firstname="fdsafsadf3", middlename="fdgdsgffd4", lastname="adgkasdfl5"))
    app.logout()



