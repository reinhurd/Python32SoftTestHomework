from sys import maxsize

class UserInfo:
    """
    Fullfill user info on create-new-users page.
    """
    def __init__(self, firstname=None, lastname=None, homephone=None, mobilephone=None, workphone=None, fax=None,
                 phone2=None, email=None, email2=None, email3=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.home = homephone
        self.mobile = mobilephone
        self.work = workphone
        self.fax = fax
        self.phone2 = phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and ((self.firstname == other.firstname) and (self.lastname == other.lastname))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
