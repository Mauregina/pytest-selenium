import pytest
from pages.LoginPage import LoginPage

class Test1:
    @pytest.fixture()
    def open_browser(self):
        self.login_page = LoginPage()
        yield #o que vem depois do yield é executado apenas no final do teste
        self.login_page.close()

    def test_click_login_button(self, open_browser):
        self.login_page.click_login_button()
        assert self.login_page.is_login_url(), 'Página requerida não encontrada!'
        assert self.login_page.has_error_msg(), 'Mensagem de erro não encontrada!'

