import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com/'

class Test1:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get(URL)
        yield #o que vem depois do yield é executado apenas no final do teste
        self.driver.quit()

    def test_click_login_button(self, setup):
        self.driver.find_element(By.ID, 'login-button').click()
        assert self.driver.current_url == URL, 'Página requerida não encontrada!'
        error_msg = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert error_msg == 'Epic sadface: Username is required', 'Mensagem de erro não encontrada!'

