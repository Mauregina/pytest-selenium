import pytest
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage


def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help="Browser to run the tests")

@pytest.fixture()
def open_browser(browser):
    login_page = LoginPage(browser=browser)
    yield login_page
    login_page.close()

@pytest.fixture()
def browser(request):
    selected_browser = request.config.getoption('browser').lower()

    if selected_browser not in ['chrome']:
        raise Exception(f'Browser não suportado: {selected_browser}')

    yield selected_browser

@pytest.fixture()
def efetuar_login(open_browser):
    login_page = open_browser
    login_page.efetuar_login()
    product_page = ProductPage(login_page.driver)
    assert product_page.is_product_page(), 'Página de Produtos encontrada!'
    yield login_page