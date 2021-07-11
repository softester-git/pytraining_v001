from pytest_bdd import given, when, then
from model.contact import Contact
import random
from time import sleep

@given("a contact list")
def contact_list(db):
    return db.get_contact_list()

@given("a contact with <fname> and <lname>")
def new_contact_list(fname, lname):
    return Contact(fname=fname, lname=lname)

@when("I add the contact to the list")
def add_new_contact(app, new_contact_list):
    app.contact.create(new_contact_list)

@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(db, app, contact_list, new_contact_list):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact_list)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

@given("a non-empty contact list")
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="FirstName", lname="LastName"))
    return db.get_contact_list()

@given("a random contact from the list")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(str(random_contact.id))

@when("I edit the contact from the list")
def edit_contact(app, random_contact):
    app.contact.edit_contact_by_id(contact=random_contact, id=str(random_contact.id))

@then("Then the new contact list count equal to the old list count")
def verify_contact_edited(app, db, non_empty_contact_list, random_contact, check_ui):
    new_contacts = db.get_contact_list()
    assert len(non_empty_contact_list) - 1 == len(new_contacts)


@then("the new contact list equal to the old list without the deleted contact")
def verify_contact_deleted(app, db, non_empty_contact_list, random_contact, check_ui):
    new_contacts = db.get_contact_list()
    assert len(non_empty_contact_list) - 1 == len(new_contacts)
    assert list(filter(lambda s: s.contact_id != random_contact.id, non_empty_contact_list)) == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)