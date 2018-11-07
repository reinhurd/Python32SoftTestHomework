def test_del_group(app):
    app.session.login(username="admin", password="secret", first_time_open_homepage=True)
    app.group.del_first_group()
    app.session.logout()
