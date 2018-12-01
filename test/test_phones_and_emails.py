import re

def test_phones_and_emails_on_homepage(app):
    user_from_homepage = app.user.get_users_list()[0]
    user_from_editpage = app.user.get_user_info_from_edit_page(0)
    assert user_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(user_from_editpage)
    assert user_from_homepage.all_emails == merge_email_like_on_homepage(user_from_editpage)


def clear(s):
    pattern = r'[() -]'
    return re.sub(pattern, "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     filter(lambda x: x is not None,
                            [contact.email, contact.email2, contact.email3])))
