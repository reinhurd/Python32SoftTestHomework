# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.userinfo import UserInfo


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.newuser.create(UserInfo(firstname="fdsafsadf3", middlename="fdgdsgffd4", lastname="adgkasdfl5"))
    app.session.logout()



