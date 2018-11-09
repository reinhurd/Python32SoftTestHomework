def test_del_group(app):
    app.group.del_first_group()
    app.open_home_page()
