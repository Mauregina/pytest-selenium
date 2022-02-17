from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.PageObject import PageObject

class LoginPage(PageObject):
    URL = 'https://www.saucedemo.com/'
    id_login_btn = 'login-button'
    id_username = 'user-name'
    key_username = 'standard_user'
    id_password = 'password'
    key_password = 'secret_sauce'
    class_error_msg = 'error-message-container'
    txt_error_msg = 'Epic sadface: Username is required'


    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.open_url_login()

    def open_url_login(self):
        self.driver.get(self.URL)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def efetuar_login(self):
        self.driver.find_element(By.ID, self.id_username).send_keys(self.key_username)
        self.driver.find_element(By.ID, self.id_password).send_keys(self.key_password)
        self.click_login_button()

    def is_login_url(self):
        return self.driver.current_url == self.URL

    def has_error_msg(self):
        error_msg = self.driver.find_element(By.CLASS_NAME, self.class_error_msg).text
        return error_msg == self.txt_error_msg
