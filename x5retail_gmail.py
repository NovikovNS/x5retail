import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@allure.feature('Функциональное тестирование Gmail')
@allure.story('Проверка отправления письма')
def test_send_successful(driver):
    wait = WebDriverWait(driver, 5)

    with allure.step('нажать кнопку "Написать"'):
        driver.find_element_by_xpath("//div[text()='Написать']").click()
        #driver.find_element_by_css_selector('#\:3o > div > div').click()

    with allure.step('нажать на поле для ввода почты пользователя'):
        driver.find_element_by_name("to").send_keys('xretailtest718@gmail.com')

    with allure.step('нажать на поле для ввода темы письма'):
        driver.find_element_by_name("subjectbox").send_keys('Тест')

    # нажать на поле для ввода текста письма
    #driver.find_element_by_css_selector('[aria-label="Тело письма"]').send_keys('Тест')
    #driver.find_element_by_css_selector('#\:9y').send_keys('Тест')

    with allure.step('нажать кнопку отправить'):
        driver.find_element_by_xpath("//div[text()='Отправить']").click()
    #wait.until(EC.presence_of_element_located((By.ID, "link_undo")))

    with allure.step('получить сообщение, что письмо отправлено'):
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Письмо отправлено.')]")))


    # ошибка неопознанный отправитель, заполненный текст
    # \:dc # селектор для окна этой ошибки

    # ошибка пустой отправитель, пустой текст
    # \:dd # селектор для окна этой ошибки

    # любой заполенный отправитель, пустой текст. Появляется всплывающее окно в браузере. Как обойти это?
    # поискать ответ у Баранцева

    #time.sleep(5)



