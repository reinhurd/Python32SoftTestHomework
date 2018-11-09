from model.userinfo import UserInfo


def test_mod_user(app):
    app.user.mod_first_user(UserInfo(firstname="EDITED", middlename="EDITED", lastname="EDITED"))


