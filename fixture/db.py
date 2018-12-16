import pymysql
from model.group import Group
from model.userinfo import UserInfo


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_userinfo_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(UserInfo(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_userinfo_tel_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, fax from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, fax) = row
                list.append(UserInfo(id=str(id), firstname=firstname, lastname=lastname, homephone=home, mobilephone=mobile, workphone=work, fax=fax))
        finally:
            cursor.close()
        return list

    def get_userinfo_mail_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id, firstname, lastname, email, email2, email3) = row
                list.append(UserInfo(id=str(id), firstname=firstname, lastname=lastname, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
