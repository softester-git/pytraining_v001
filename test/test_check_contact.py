import re
from random import choice

def test_contact_home_page_eq_edit_page(app, db):
    contacts = db.get_contact_list()
    index = choice(list(map(lambda x: x.id, contacts)))
    contact_from_home_page = list(filter(lambda x: x.id == index, contacts))[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page == contact_from_edit_page

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda y: y != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [str(contact.home), str(contact.work), str(contact.mobile), str(contact.phone2)]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda y: y != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [str(contact.email), str(contact.email2), str(contact.email3)]))))
