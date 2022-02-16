import pytest
from pages.LoginPage import LoginPage

URL = 'https://www.saucedemo.com/'

class Test2:
    @pytest.fixture()
    def open_browser(self):
        self.login_page = LoginPage()
        yield #o que vem depois do yield é executado apenas no final do teste
        self.login_page.close()

    def test_efetuar_login(self, open_browser):
        self.login_page.efetuar_login()
        assert self.login_page.is_inventory_url(), 'Página requerida encontrada!'
        assert self.login_page.has_title_product(), 'Título da página de produtos encontrado!'

