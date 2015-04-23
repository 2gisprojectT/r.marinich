from base_component import BaseComponent

class Dashboard(BaseComponent):
    tags = {
        'login': 'login',
        'password': 'password',

        'button': 'input.form_b',

        'mainClass': 'prof',
        'insideClass': 'user_menu_link',
    }

    def input(self, login, password):
        self.driver.find_element_by_name(self.tags['login']).click()
        self.driver.find_element_by_name(self.tags['login']).send_keys(login)
        self.driver.find_element_by_name(self.tags['password']).send_keys(password)
        self.driver.find_element_by_css_selector(self.tags['button']).click()

    def getHtmlPage(self):
        return self.driver.find_element_by_tag_name("body").text

    def getDashboardLink(self):
        return self.driver.find_element_by_class_name(self.tags['mainClass']).find_element_by_class_name(self.tags['insideClass']).get_attribute('href')