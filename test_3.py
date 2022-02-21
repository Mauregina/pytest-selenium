import pytest
from pages.LoginPage import LoginPage
from pages.MenuPage import MenuPage
from pages.ProductPage import ProductPage

class Test3:

    @pytest.fixture()
    def setup(self):
        self.login_page = LoginPage(browser='chrome')
        self.login_page.execute_login()
        self.product_page = ProductPage(self.login_page.driver)
        assert self.product_page.is_product_page(), "Página de Produtos não encontrada!"
        yield
        self.login_page.close()

    def test_execute_logout(self, setup):
        menu_page = MenuPage(self.product_page.driver)
        menu_page.execute_logout()

        assert self.login_page.is_login_url(), 'Página de login não encontrada!'




