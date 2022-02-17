import pytest
from pages.LoginPage import LoginPage

class Test1:

    def test_click_login_button(self, open_browser):
        login_page = open_browser
        login_page.click_login_button()
        assert login_page.is_login_url(), 'Página requerida não encontrada!'
        assert login_page.has_error_msg(), 'Mensagem de erro não encontrada!'

