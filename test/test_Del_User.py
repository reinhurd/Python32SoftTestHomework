from model.userinfo import UserInfo


def test_del_user(app):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", middlename="", lastname=""))
    app.user.del_first_user()



