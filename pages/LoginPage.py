from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    URL = 'https://www.saucedemo.com/'
    URL_inventory = 'https://www.saucedemo.com/inventory.html'
    id_login_btn = 'login-button'
    id_username = 'user-name'
    key_username = 'standard_user'
    id_password = 'password'
    key_password = 'secret_sauce'
    class_error_msg = 'error-message-container'
    class_title = 'title'
    txt_error_msg = 'Epic sadface: Username is required'
    txt_title = 'PRODUCTS'


    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.open_url_login()

    def open_url_login(self):
        self.driver.get(self.URL)

    def close(self):
        self.driver.quit()

    def click_login_button(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def efetuar_login(self):
        self.driver.find_element(By.ID, self.id_username).send_keys(self.key_username)
        self.driver.find_element(By.ID, self.id_password).send_keys(self.key_password)
        self.click_login_button()

    def is_login_url(self):
        return self.driver.current_url == self.URL

    def is_inventory_url(self):
        return self.driver.current_url == self.URL_inventory

    def has_error_msg(self):
        error_msg = self.driver.find_element(By.CLASS_NAME, self.class_error_msg).text
        return error_msg == self.txt_error_msg

    def has_title_product(self):
        title_products = self.driver.find_element(By.CLASS_NAME, self.class_title).text
        return title_products.upper() == self.txt_title