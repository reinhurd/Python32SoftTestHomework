from pony.orm import *
from datetime import datetime
from model.group import Group
from model.userinfo import UserInfo
#from pymysql.converters import decoders # working incorrect

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        userinfos = Set(lambda: ORMFixture.ORMUserInfo, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMUserInfo(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='userinfos', lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)


    def convert_group_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_userinfo_to_model(self, userinfos):
        def convert(userinfo):
            return UserInfo(id=str(userinfo.id), firstname=userinfo.firstname, lastname=userinfo.lastname)
        return list(map(convert, userinfos))

    @db_session
    def get_group_list(self):
        return self.convert_group_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_userinfo_list(self):
        return self.convert_userinfo_to_model(select(c for c in ORMFixture.ORMUserInfo if c.deprecated is None))

    @db_session
    def get_userinfo_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_userinfo_to_model(orm_group.userinfos)

    @db_session
    def get_userinfo_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_userinfo_to_model(
            select(c for c in ORMFixture.ORMUserInfo if c.deprecated is None and orm_group not in c.groups))

