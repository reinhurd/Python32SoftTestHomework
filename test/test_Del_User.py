def test_del_user(app):
    app.session.login(username="admin", password="secret")
    app.user.del_first_user()
    app.open_home_page()
    app.session.logout()

