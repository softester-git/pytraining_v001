from time import sleep
import re

from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def __repr__(self):
        return("%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.app.id, self.app.fname, self.app.mname, self.app.lname, self.app.nname, self.app.photo, self.app.title, self.app.company, self.app.addr, self.app.home, self.app.work, self.app.mobile, self.app.email, self.app.email2, self.app.email3, self.app.homepage, self.app.bmonth, self.app.bday, self.app.amonth, self.app.aday, self.app.byear, self.app.ayear, self.app.address2, self.app.phone2, self.app.notes))

    contact_cache = None

    def submit_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='submit']").click()

    def update_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='update']").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php") and not len(wd.find_elements_by_name("submit")) > 0:
            wd.find_element_by_link_text("add new").click()

    def return_to_home(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        sleep(5)
        self.open_contact_page()
        #sleep(5)
        self.fill_contact_form(contact)
        self.submit_form()
        self.return_to_home()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        # return to home page
        self.return_to_home()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        # return to home page
        self.return_to_home()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.return_to_home()
        # open edit form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        self.update_form()
        self.return_to_home()
        self.contact_cache = None

    def edit_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.return_to_home()
        # open edit form
        wd.find_element_by_xpath("//a[@href='edit.php?id="+str(id)+"']").click()
        self.fill_contact_form(contact)
        self.update_form()
        self.return_to_home()
        self.contact_cache = None

    def open_edit_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home()
        sleep(1)
        wd.find_element_by_xpath("//a[@href='edit.php?id=" + str(id) + "']").click()

    def open_view_contact_by_id(self, id):
        wd = self.app.wd
        self.return_to_home()
        sleep(1)
        wd.find_element_by_xpath("//a[@href='view.php?id=" + str(id) + "']").click()

    def fill_contact_form(self, contact):
        self.app.change_field_value("firstname", contact.fname)
        self.app.change_field_value("middlename", contact.mname)
        self.app.change_field_value("lastname", contact.lname)
        self.app.change_field_value("nickname", contact.nname)
        self.app.change_select_fields("photo", contact.photo)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.addr)
        self.app.change_field_value("home", contact.home)
        self.app.change_field_value("mobile", contact.mobile)
        self.app.change_field_value("work", contact.work)
        self.app.change_field_value("fax", contact.fax)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
        self.app.change_field_value("homepage", contact.homepage)
        self.app.change_select_fields("bday", contact.bday)
        self.app.change_select_fields("bmonth", contact.bmonth)
        self.app.change_field_value("byear", contact.byear)
        self.app.change_select_fields("aday", contact.aday)
        self.app.change_select_fields("amonth", contact.amonth)
        self.app.change_field_value("ayear", contact.byear)
        self.app.change_field_value("address2", contact.address2)
        self.app.change_field_value("phone2", contact.phone2)
        self.app.change_field_value("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home()
            wd.find_elements_by_name("entry")
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                contact_id_value = cells[0].find_element_by_tag_name("input").get_attribute("value")
                last_name_value = cells[1].text
                first_name_value = cells[2].text
                address_value = cells[3].text
                all_emails_value = cells[4].text
                all_phones_value = cells[5].text
                self.contact_cache.append(Contact(fname=first_name_value if first_name_value != "" else None,
                                                  lname=last_name_value if last_name_value != "" else None,
                                                  addr=address_value if address_value != "" else None,
                                                  id=contact_id_value if contact_id_value != "" else None,
                                                  all_phones=all_phones_value,
                                                  all_emails=all_emails_value
                                                  ))
        return self.contact_cache

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='" + str(id) + "']").click()

    def get_contact_from_edit_page(self, id):
        wd = self.app.wd
        self.open_edit_contact_by_id(id)
        firstname_value = wd.find_element_by_name("firstname").get_attribute("value")
        lastname_value = wd.find_element_by_name("lastname").get_attribute("value")
        address_value = wd.find_element_by_name("address").get_attribute("value")
        id_value = wd.find_element_by_name("id").get_attribute("value")
        email_value = wd.find_element_by_name("email").get_attribute("value")
        email2_value = wd.find_element_by_name("email2").get_attribute("value")
        email3_value = wd.find_element_by_name("email3").get_attribute("value")
        homephone_value = wd.find_element_by_name("home").get_attribute("value")
        workphone_value = wd.find_element_by_name("work").get_attribute("value")
        mobilephone_value = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone_value = wd.find_element_by_name("phone2").get_attribute("value")
        return(Contact(fname=firstname_value if firstname_value != "" else None,
                       lname=lastname_value if lastname_value != "" else None,
                       id=id_value if id_value != "" else None,
                       addr=address_value if address_value != "" else None,
                       home=homephone_value if homephone_value != "" else None,
                       work=workphone_value if workphone_value != "" else None,
                       mobile=mobilephone_value if mobilephone_value != "" else None,
                       phone2=secondaryphone_value if secondaryphone_value != "" else None
                       ))

    def get_contact_from_view_page(self, id):
        wd = self.app.wd
        self.open_view_contact_by_id(id)
        text = wd.find_element_by_id("content").text
        try:
            home = re.search("H: (.*)", text).group(1)
        except:
            home = None
        try:
            work = re.search("W: (.*)", text).group(1)
        except:
            work = None
        try:
            mobile = re.search("M: (.*)", text).group(1)
        except:
            mobile = None
        try:
            phone2 = re.search("P: (.*)", text).group(1)
        except:
            phone2 = None
        return(Contact(home=home, work=work, mobile=mobile, phone2=phone2))

    def del_relation(self, group, contact):
        # How to delete group from contact by ui?
        pass

    def add_relation(self, group, contact):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_id(str(contact.id))
        wd.find_element_by_name("to_group").send_keys(str(group.group_id))
        wd.find_element_by_name("add").click()
        self.return_to_home()
