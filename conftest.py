import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    """
    Фикстура для инициализации и закрытия браузера.
    :yield: Экземпляр WebDriver.
    """
    driver = webdriver.Chrome()  # Инициализация ChromeDriver
    yield driver
    driver.quit()  # Закрытие браузера после завершения теста
