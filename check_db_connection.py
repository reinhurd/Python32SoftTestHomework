from fixture.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_userinfo_not_in_group(Group(id='42'))
    for s in l:
        print(s)
    print(len(l))
finally:
    pass #db.destroy()