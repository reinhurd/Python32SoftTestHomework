from model.userinfo import UserInfo


class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_add_user_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()

    def create(self, userinfo):
        wd = self.app.wd
        self.open_add_user_page()
        self.enter_text(userinfo)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.users_cache = None

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def mod_first_user(self, userinfo):
        self.mod_user_by_index(0, userinfo)
        self.users_cache = None

    def mod_user_by_index(self, index, userinfo):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_user_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.enter_text(userinfo)
        wd.find_element_by_name("update").click()
        self.users_cache = None

    def del_user_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_user_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.implicitly_wait(1)
        wd.find_element_by_xpath("//a[contains(text(),'home')]").click()
        self.users_cache = None

    def del_first_user(self):
        self.del_user_by_index(0)
        self.users_cache = None

    def enter_text(self, userinfo):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(userinfo.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(userinfo.lastname)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    users_cache = None

    def get_users_list(self):
        if self.users_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.users_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.users_cache.append(UserInfo(firstname=firstname, lastname=lastname, id=id))
        return list(self.users_cache)



