import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    # запуск gmail и авторизация
    driver.get("https://www.google.com/gmail/")
    driver.find_element_by_id("identifierId").send_keys("xretailtest718@gmail.com")
    driver.find_element_by_css_selector('#identifierNext div button').click()
    driver.implicitly_wait(5)
    driver.find_element_by_css_selector('#password [type="password"]').send_keys('Parolqwerty1234')
    driver.find_element_by_css_selector('#passwordNext div button').click()
    request.addfinalizer(driver.quit)
    return driver
