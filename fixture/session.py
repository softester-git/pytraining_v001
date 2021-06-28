from time import sleep


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, user_pass):
        wd = self.app.wd
        self.app.open_main_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user_pass)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        sleep(2)
        wd.find_element_by_link_text("Logout").click()
        sleep(2)