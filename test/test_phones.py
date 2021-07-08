import re
from random import choice


def test_phones_on_home_page(app, db):
    contacts = db.get_contact_list()
    index = choice(list(map(lambda x: x.id, contacts)))
    contact_from_home_page = list(filter(lambda x: x.id == index, contacts))[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_home_page.home == contact_from_edit_page.home
    assert contact_from_home_page.work == contact_from_edit_page.work
    assert contact_from_home_page.mobile == contact_from_edit_page.mobile
    assert contact_from_home_page.phone2 == contact_from_edit_page.phone2

def test_phones_on_contact_view_page(app, db):
    contacts = db.get_contact_list()
    index = choice(list(map(lambda x: x.id, contacts)))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda y: y != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [str(contact.home), str(contact.work), str(contact.mobile), str(contact.phone2)]))))
