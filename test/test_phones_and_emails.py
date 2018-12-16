import re
from model.userinfo import UserInfo


def test_phones_on_homepage(app, db):
    users_from_homepage = app.user.get_users_list()
    users_from_db = db.get_userinfo_tel_list()
    assert sorted(users_from_homepage, key=UserInfo.id_or_max) == sorted(users_from_db, key=UserInfo.id_or_max)


def test_mail_on_homepage(app, db):
    users_from_homepage = app.user.get_users_list()
    users_from_db = db.get_userinfo_mail_list()
    assert sorted(users_from_homepage, key=UserInfo.id_or_max) == sorted(users_from_db, key=UserInfo.id_or_max)


"""
def clear(s):
    return s
    #pattern = r'[() -]'
    #return re.sub(pattern, "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     filter(lambda x: x is not None,
                            [contact.email, contact.email2, contact.email3])))
"""