# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class CreateGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_create_group(self):
        self.login(user_name="admin", user_pass="secret")
        self.fill_group_form(Group(group_name="group_name_001", group_header="group_header_001", group_footer="group_footer_001"))
        self.logout()


    def test_create_empty_group(self):
        self.login(user_name="admin", user_pass="secret")
        self.fill_group_form(Group(group_name="", group_header="", group_footer=""))
        self.logout()


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()
        #wd.find_element_by_xpath("//div[@id='content']/form/span").click()


    def submit_form(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()


    def fill_group_form(self, group):
        wd = self.wd
        self.open_groups_page()
        self.init_create_group()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.group_header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.group_footer)
        self.submit_form()
        self.return_to_groups_page()


    def init_create_group(self):
        wd = self.wd
        wd.find_element_by_name("new").click()


    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()


    def login(self, user_name, user_pass):
        wd = self.wd
        self.open_main_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user_pass)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def tearDown(self):
        wd = self.wd
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
