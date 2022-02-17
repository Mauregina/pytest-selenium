import pytest
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage

class Test2:

    def test_efetuar_login(self, open_browser):
        login_page = open_browser
        login_page.efetuar_login()
        product_page = ProductPage(login_page.driver)
        assert product_page.is_product_page(), 'Página de produtos não encontrada!'

