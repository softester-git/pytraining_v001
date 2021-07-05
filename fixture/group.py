from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def __repr__(self):
        return("%s:%s:%s:%s" % (self.app.group_name, self.app.group_header, self.app.group_footer, self.app.group_id))

    def return_to_groups_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/group.php") and not len(wd.find_elements_by_name("new")) > 0:
            wd.find_element_by_link_text("groups").click()

    def init_create_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/group.php") or (wd.current_url.endswith("/group.php") and not len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        self.init_create_group()
        self.fill_group_form(group)
        self.submit_form()
        self.return_to_groups_page()
        self.group_cache = None

    def submit_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='submit']").click()

    def submit_edit_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='update']").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open edit form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        self.submit_edit_form()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_index(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open edit form
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        self.submit_edit_form()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        self.app.change_field_value("group_name", group.group_name)
        self.app.change_field_value("group_header", group.group_header)
        self.app.change_field_value("group_footer", group.group_footer)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = list(element.text.split("\n"))[0]
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text if text!="" else None, group_id=id if id!="" else None))
        return list(self.group_cache)
