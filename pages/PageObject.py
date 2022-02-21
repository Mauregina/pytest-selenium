from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class PageObject:

    def __init__(self, browser=None, driver=None):
        #chamado por ProductPage
        if driver:
            self.driver = driver
            self.driver.implicitly_wait(3)
        # chamado por LoginPage
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
                self.driver.implicitly_wait(3)
            else:
                raise Exception(f'Browser não suportado!')

    def close(self):
        self.driver.quit()
