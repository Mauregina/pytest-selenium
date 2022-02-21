class Test1:

    def test_click_login_button(self, login_page_open):
        login_page_open.click_login_btn()
        assert login_page_open.is_login_url(), 'Página deLogin não encontrada!'
        assert login_page_open.has_login_error_msg(), 'Mensagem de erro incorreta!'

