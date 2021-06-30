class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='submit']").click()

    def update_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='update']").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0:
            wd.find_element_by_link_text("add new").click()

    def return_to_home(self):
        wd = self.app.wd
        if not wd.current_url.endswith("addressbook/"):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        self.open_contact_page()
        self.fill_contact_form(contact)
        self.submit_form()
        self.return_to_home()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to_alert().accept()
        # return to groups page
        self.return_to_home()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.return_to_home()
        # open edit form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        self.update_form()
        self.return_to_home()

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
        return len(wd.find_elements_by_xpath("//input[@value='Delete']"))
