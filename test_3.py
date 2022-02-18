import pytest
from pages.LoginPage import LoginPage
from pages.MenuPage import MenuPage
from pages.ProductPage import ProductPage

class Test3:

    def test_efetuar_logout(self, efetuar_login):
        login_page = efetuar_login
        menu_page = MenuPage(login_page.driver)
        menu_page.efetuar_logout()

        assert login_page.is_login_page(), 'Página de login esta sendo exibida!'




