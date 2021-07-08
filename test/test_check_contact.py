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
