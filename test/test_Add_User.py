# -*- coding: utf-8 -*-
from model.userinfo import UserInfo
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    UserInfo(
        firstname=random_string("firstname", 15),
        lastname=random_string("lastname", 15),
        homephone=random_string("homephone", 15),
        mobilephone=random_string("mobilephone", 15),
        workphone=random_string("workphone", 15),
        fax=random_string("fax", 15),
        phone2=random_string("phone2", 15),
        email=random_string("email", 15),
        email2=random_string("email2", 15),
        email3=random_string("email3", 15),
    )
    for i in range(3)
]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_users = app.user.get_users_list()
    app.user.create(user)
    new_users = app.user.get_users_list()
    assert len(old_users) + 1 == len(new_users)
    old_users.append(user)
    assert sorted(old_users, key=UserInfo.id_or_max) == sorted(new_users, key=UserInfo.id_or_max)





