from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    userinfos = db.get_userinfo_list()
    for userinfo in userinfos:
        print(userinfo)
    print(len(userinfos))
finally:
    db.destroy()
