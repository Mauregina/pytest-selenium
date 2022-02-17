from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.PageObject import PageObject

class ProductPage(PageObject):
    URL_inventory = 'https://www.saucedemo.com/inventory.html'
    class_title_page = 'title'
    class_menu = 'react-burger-menu-btn'
    class_inventory_ctn = 'inventory_container'
    txt_title = 'PRODUCTS'

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver=driver)

    def is_product_page(self):
        is_products_url = self.driver.current_url == self.URL_inventory
        title_products = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        is_title_products = title_products.upper() == self.txt_title
        try:
            has_menu = True
            self.driver.find_element(By.ID, self.class_menu)
        except NoSuchElementException:
            has_menu = False

        try:
            has_inventory_container = True
            self.driver.find_element(By.ID, self.class_inventory_ctn)
        except NoSuchElementException:
            has_inventory_container = False

        return is_products_url and is_title_products and has_menu and has_inventory_container
