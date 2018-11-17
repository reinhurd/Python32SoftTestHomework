from model.userinfo import UserInfo
from random import randrange


def test_del_user_by_index(app):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", lastname=""))
    old_users = app.user.get_users_list()
    index = randrange(len(old_users))
    app.user.del_user_by_index(index)
    new_users = app.user.get_users_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[index:index+1] = []
    assert old_users == new_users


