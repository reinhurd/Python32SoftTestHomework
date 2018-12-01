import re

def test_phones_on_homepage(app):
    user_from_homepage = app.user.get_users_list()[0]
    user_from_editpage = app.user.get_user_info_from_edit_page(0)
    assert clear(user_from_homepage.home) == clear(user_from_editpage.home)
    assert clear(user_from_homepage.work) == clear(user_from_editpage.work)
    assert clear(user_from_homepage.mobile) == clear(user_from_editpage.mobile)
    assert clear(user_from_homepage.phone2) == clear(user_from_editpage.phone2)


def clear(s):
    ##Clear all non-Digits
    pattern = r'\D'
    return re.sub(pattern, "", s)
