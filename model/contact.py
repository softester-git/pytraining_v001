from sys import maxsize

class Contact:
    def __init__(self, id=None, fname=None, mname=None, lname=None, nname=None, photo=None, title=None, company=None, addr=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None, bmonth=None, bday=None, amonth=None, aday=None, byear=None, ayear=None, address2=None, phone2=None, notes=None, all_phones=None, all_emails=None):
        self.id = id
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
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return("%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.fname, self.mname, self.lname, self.nname, self.photo, self.title, self.company, self.addr, self.home, self.work, self.mobile, self.email, self.email2, self.email3, self.homepage, self.bmonth, self.bday, self.amonth, self.aday, self.byear, self.ayear, self.address2, self.phone2, self.notes))

    def __eq__(self, other):
        return((self.id is None or other.id is None or self.id == other.id) and
               self.fname == other.fname and
               self.lname == other.lname and
               self.addr == other.addr)
               #self.mname == other.mname and
               #self.nname == other.nname and
               #self.photo == other.photo and
               #self.title == other.title and
               #self.company == other.company and
               #self.home == other.home and
               #self.mobile == other.mobile and
               #self.work == other.work and
               #self.fax == other.fax and
               #self.email == other.email and
               #self.email2 == other.email2 and
               #self.email3 == other.email3 and
               #self.homepage == other.homepage and
               #self.bmonth == other.bmonth and
               #self.bday == other.bday and
               #self.amonth == other.amonth and
               #self.aday == other.aday and
               #self.byear == other.byear and
               #self.ayear == other.ayear and
               #self.address2 == other.address2 and
               #self.phone2 == other.phone2 and
               #self.notes == other.notes)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
