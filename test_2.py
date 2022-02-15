import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com/'

class Test2:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.get(URL)
        yield #o que vem depois do yield é executado apenas no final do teste
        self.driver.quit()

    def test_efetuar_login(self, setup):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()

        assert self.driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Página requerida encontrada!'
        title_products = self.driver.find_element(By.CLASS_NAME, 'title').text

        assert title_products == 'PRODUCTS', 'Título da página de produtos encontrado!'

