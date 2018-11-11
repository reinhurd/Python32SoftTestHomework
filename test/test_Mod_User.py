from model.userinfo import UserInfo


def test_mod_user(app):
    if app.user.count() == 0:
        app.user.create(UserInfo(firstname="Test", middlename="", lastname=""))
    app.user.mod_first_user(UserInfo(firstname="EDITED44", middlename="EDITED44", lastname="EDITED44"))


