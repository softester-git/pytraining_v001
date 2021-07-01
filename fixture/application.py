from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.select import Select
import os

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        #self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def change_field_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_fields(self, field_name, text):
        wd = self.wd
        if text is not None:
            if not field_name == "photo":
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            else:
                wd.find_element_by_name(field_name).send_keys(os.path.abspath(text))

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
