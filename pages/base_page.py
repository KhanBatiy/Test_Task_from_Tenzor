from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Базовый класс для всех страниц. Содержит общие методы для работы с веб-элементами.
class BasePage:
    def __init__(self, driver: WebDriver):
        # Инициализация базовой страницы.
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Ожидание до 10 секунд

    def open(self, url):
        # Открывает указанный URL в браузере.
        self.driver.get(url)

    def find_element(self, locator):
        # Ожидает появления элемента на странице и возвращает его.
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        # Ожидает появления всех элементов на странице и возвращает их.
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        # Находит элемент и кликает по нему.
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        # Прокручивает страницу до указанного элемента.
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text(self, locator):
        # Возвращает текст элемента.
        return self.find_element(locator).text

    def get_current_url(self):
        # Возвращает текущий URL страницы.
        return self.driver.current_url

    def get_title(self):
        # Возвращает заголовок страницы.
        return self.driver.title
