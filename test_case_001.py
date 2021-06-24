# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class CreateGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_create_group(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.init_create_group(wd)
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group_name_001")
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("group_header_001")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("group_footer_001")
        # submit form
        wd.find_element_by_name("submit").click()
        # return to groups page
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_xpath("//div[@id='content']/form/span").click()
        # logout
        wd.find_element_by_link_text("Logout").click()

    def init_create_group(self, wd):
        wd.find_element_by_name("new").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
