from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.PageObject import PageObject

class MenuPage(PageObject):
    id_menu = 'react-burger-menu-btn'
    id_logout = 'logout_sidebar_link'
    class_menu_list = 'bm-item-list'

    def __init__(self, driver):
        super(MenuPage, self).__init__(driver=driver)

    def open_menu(self):
        self.driver.find_element(By.ID, self.id_menu).click()

    def is_menu_open(self):
        try:
            self.driver.find_element(By.CLASS_NAME, self.class_menu_list).click()
            return True
        except NoSuchElementException:
            return False

    def click_logout_item(self):
        self.driver.find_element(By.ID, self.id_logout).click()

    def efetuar_logout(self):
        self.open_menu()

        if self.is_menu_open():
            self.click_logout_item()
        else:
            raise Exception('Menu não foi aberto!')
