from sys import maxsize


class Contact:
    def __init__(self, fname=None, mname=None, lname=None, nname=None, photo=None, title=None, company=None, addr=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None, bmonth=None, bday=None, amonth=None, aday=None, byear=None, ayear=None, address2=None, phone2=None, notes=None, id=None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nname = nname
        self.photo = photo
        self.title = title
        self.company = company
        self.addr = addr
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bmonth = bmonth
        self.bday = bday
        self.amonth = amonth
        self.aday = aday
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return("%s:%s:%s" % (self.id, self.fname, self.lname))

    def __eq__(self, other):
        return(self.id is None or other.id is None or self.id == other.id and self.fname == other.fname and self.lname == other.lname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
