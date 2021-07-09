import re
from fixture.orm import ORMFixture


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_contact_home_page_eq_edit_page(app):
    contacts = db.get_contact_list()
    contacts_home = app.contact.get_contact_list()
    index = list(map(lambda x: x.id, contacts))
    contact_from_home_page = []
    contact_from_edit_page = []
    for i in index:
        contact_from_home_page.append(list(filter(lambda x: x.id == i, contacts_home))[0])
        contact_from_edit_page.append(app.contact.get_contact_from_edit_page(i))
    assert contact_from_home_page == contact_from_edit_page
    assert contact_from_home_page == contacts
    assert contact_from_edit_page == contacts

def clear(s):
    return re.sub("[() -]", "", s)
