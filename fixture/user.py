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

    def select_user_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[contains(@href, "edit.php?id=%s")]' % id).click()

    def select_user_by_index_for_mod(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def mod_first_user(self, userinfo):
        self.mod_user_by_index(0, userinfo)
        self.users_cache = None

    def mod_user_by_index(self, index, userinfo):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_user_by_index_for_mod(index)
        self.enter_text(userinfo)
        wd.find_element_by_name("update").click()
        self.users_cache = None

    def mod_user_by_id(self, id, userinfo):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_user_by_id(id)
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

    def del_user_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_user_by_id(id)
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
        ##Iterate instance attr:value to fullfill data of new contact
        for params, value in userinfo.__dict__.items():
            if value is not None \
                    and params != "all_phones_from_homepage" and params != "all_emails" and params != "id":
                wd.find_element_by_name(params).click()
                wd.find_element_by_name(params).clear()
                wd.find_element_by_name(params).send_keys(value)

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
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.users_cache.append(UserInfo(firstname=firstname, lastname=lastname,
                                                 all_phones_from_homepage=all_phones, all_emails=all_emails, id=id))
        return list(self.users_cache)

    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_user_by_index_for_mod(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return UserInfo(firstname=firstname, lastname=lastname, homephone=home, mobilephone=mobile, workphone=work,
                        phone2=phone2, email=email, email2=email2, email3=email3, id=id)
