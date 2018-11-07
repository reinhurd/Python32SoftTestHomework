from model.userinfo import UserInfo


def test_mod_user(app):
    app.session.login(username="admin", password="secret", first_time_open_homepage=True)
    app.user.mod_first_user(UserInfo(firstname="EDITED", middlename="EDITED", lastname="EDITED"))
    app.session.logout()

