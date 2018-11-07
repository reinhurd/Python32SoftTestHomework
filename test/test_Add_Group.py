# -*- coding: utf-8 -*-
import pytest
from model.group import Group

'''
Всегда запуск этого теста первым (если запускается весь пакет тестов из tests) 
для обхода бага с логаутом в Firefox
'''


@pytest.mark.run(order=1)
def test_add_group(app):
    app.session.login(username="admin", password="secret", first_time_open_homepage=True)
    app.group.create(Group(name="gfdgd", header="sdfgsdgdd", footer="sdfgsdg"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

