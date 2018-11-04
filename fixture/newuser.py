class NewUserHelper:

    def __init__(self, app):
        self.app = app

    def open_add_user_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, userinfo):
        wd = self.app.wd
        self.open_add_user_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(userinfo.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(userinfo.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(userinfo.lastname)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
