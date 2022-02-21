from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.PageObject import PageObject

class LoginPage(PageObject):
    URL_LOGIN = 'https://www.saucedemo.com/'
    id_login_btn = 'login-button'
    id_username = 'user-name'
    key_username = 'standard_user'
    id_password = 'password'
    key_password = 'secret_sauce'
    class_error_msg = 'error-message-container'
    txt_error_msg = 'Epic sadface: Username is required'


    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.open_login_URL()

    def open_login_URL(self):
        self.driver.get(self.URL_LOGIN)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def is_login_url(self):
        return self.driver.current_url == self.URL_LOGIN

    def has_login_error_msg(self):
        error_msg = self.driver.find_element(By.CLASS_NAME, self.class_error_msg).text
        return error_msg == self.txt_error_msg

    def execute_login(self):
        self.driver.find_element(By.ID, self.id_username).send_keys(self.key_username)
        self.driver.find_element(By.ID, self.id_password).send_keys(self.key_password)
        self.click_login_btn()
