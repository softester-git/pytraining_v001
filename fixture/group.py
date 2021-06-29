class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def init_create_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.init_create_group()
        self.fill_group_form(group)
        self.submit_form()
        self.return_to_groups_page()

    def submit_form(self):
        wd = self.app.wd
        #wd.find_element_by_name("submit").click()
        wd.find_element_by_xpath("//input[@name='submit']").click()

    def submit_edit_form(self):
        wd = self.app.wd
        #wd.find_element_by_name("submit").click()
        wd.find_element_by_xpath("//input[@name='update']").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        self.submit_edit_form()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.group_name)
        self.change_field_value("group_header", group.group_header)
        self.change_field_value("group_footer", group.group_footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)