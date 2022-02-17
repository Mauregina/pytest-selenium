import pytest
from pages.LoginPage import LoginPage

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