from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com/'

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get(URL)
driver.find_element(By.ID, 'login-button').click()

assert driver.current_url == URL, 'Página requerida não encontrada!'

error_msg = driver.find_element(By.CLASS_NAME, 'error-message-container').text

assert error_msg == 'Epic sadface: Username is required', 'Mensagem de erro não encontrada!'

# driver.quit()