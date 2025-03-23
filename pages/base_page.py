from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для всех страниц.
    Содержит общие методы для работы с веб-элементами.
    """
    def __init__(self, driver: WebDriver):
        """
        Инициализация базовой страницы.
        :param driver: Экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Ожидание до 10 секунд

    def open(self, url):
        """
        Открывает указанный URL в браузере.
        :param url: URL для открытия.
        """
        self.driver.get(url)

    def find_element(self, locator):
        """
        Ожидает появления элемента на странице и возвращает его.
        :param locator: Локатор элемента (кортеж из стратегии и значения).
        :return: Найденный элемент.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """
        Ожидает появления всех элементов на странице и возвращает их.
        :param locator: Локатор элементов.
        :return: Список найденных элементов.
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        """
        Находит элемент и кликает по нему.
        :param locator: Локатор элемента.
        """
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        """
        Прокручивает страницу до указанного элемента.
        :param locator: Локатор элемента.
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text(self, locator):
        """
        Возвращает текст элемента.
        :param locator: Локатор элемента.
        :return: Текст элемента.
        """
        return self.find_element(locator).text

    def get_current_url(self):
        """
        Возвращает текущий URL страницы.
        :return: Текущий URL.
        """
        return self.driver.current_url

    def get_title(self):
        """
        Возвращает заголовок страницы.
        :return: Заголовок страницы.
        """
        return self.driver.title
