from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.PageObject import PageObject

class ProductPage(PageObject):
    URL_inventory = 'https://www.saucedemo.com/inventory.html'
    class_title_page = 'title'
    id_menu = 'react-burger-menu-btn'
    id_inventory_ctn = 'inventory_container'
    id_logout = 'logout_sidebar_link'
    txt_title = 'PRODUCTS'
    class_product_item = 'inventory_item'
    class_btn_add_to_cart = 'btn_inventory'
    txt_remove_btn = 'REMOVE'
    class_product_item_name = 'inventory_item_name'

    def __init__(self, driver):
        super(ProductPage, self).__init__(driver=driver)

    def is_product_page(self):
        is_products_url = self.driver.current_url == self.URL_inventory
        title_products = self.driver.find_element(By.CLASS_NAME, self.class_title_page).text
        is_title_products = title_products.upper() == self.txt_title
        try:
            has_menu = True
            self.driver.find_element(By.ID, self.id_menu)
        except NoSuchElementException:
            has_menu = False

        try:
            has_inventory_container = True
            self.driver.find_element(By.ID, self.id_inventory_ctn)
        except NoSuchElementException:
            has_inventory_container = False

        return is_products_url and is_title_products and has_menu and has_inventory_container

    def click_menu_button(self):
        self.driver.find_element(By.ID, self.id_menu).click()

    def click_logout_button(self):
        self.driver.find_element(By.ID, self.id_logout).click()

    def efetuar_logout(self):
        self.click_menu_button()
        self.click_logout_button()

    def add_product_to_cart(self, product_number):
        product_list_elements = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        add_to_cart_element = product_list_elements[product_number-1].find_element(By.class_btn_add_to_cart)
        add_to_cart_element.click()
        btn_text = product_list_elements[product_number-1].find_element(By.class_btn_add_to_cart).text

        if btn_text.upper() != btn_text:
            raise Exception("Botão não mudou para ''REMOVE'")

        return product_list_elements[product_number-1].find_element(By.CLASS_NAME, self.class_product_item_name).text
