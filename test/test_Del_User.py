from model.userinfo import UserInfo
import random


def test_del_user_by_id(app, db, check_ui):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", lastname=""))
    old_users = db.get_userinfo_list()
    user = random.choice(old_users)
    app.user.del_user_by_id(user.id)
    new_users = db.get_userinfo_list()
    assert len(old_users) - 1 == len(new_users)
    old_users.remove(user)
    assert old_users == new_users
    if check_ui:
        assert sorted(old_users, key=UserInfo.id_or_max) == sorted(new_users, key=UserInfo.id_or_max)


