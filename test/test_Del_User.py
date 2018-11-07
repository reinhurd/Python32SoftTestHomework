def test_del_user(app):
    app.session.login(username="admin", password="secret", first_time_open_homepage=True)
    app.user.del_first_user()
    app.session.logout()

