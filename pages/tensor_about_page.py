from pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TensorAboutPage(BasePage):
    """
    Класс для работы со страницей "О нас" на tensor.ru.
    """
    # Локатор раздела "Работаем"
    WORKING_SECTION = ("xpath", '//*[@id="container"]/div[1]/div/div[4]/div[1]/h2')
    # Локатор всех изображений в разделе "Работаем"
    WORKING_IMAGES = ("xpath", '//*[@id="container"]/div[1]/div/div[4]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)  # Вызов конструктора родительского класса

    def is_working_section_present(self):
        """
        Проверяет, отображается ли раздел "Работаем".
        :return: True, если раздел отображается, иначе False.
        """
        return self.find_element(self.WORKING_SECTION).is_displayed()

    def check_images_dimensions(self):
        """
        Проверяет, что все изображения в разделе "Работаем" имеют одинаковые размеры.
        :return: True, если все изображения имеют одинаковые размеры, иначе False.
        """
        # Ожидание загрузки изображений
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.WORKING_IMAGES)
        )

        images = self.driver.find_elements(*self.WORKING_IMAGES)
        sizes = set()  # Используем множество для хранения уникальных размеров
        for image in images:
            size = (image.size['width'], image.size['height'])
            print(f"Image size: {size}")  # Вывод размеров в консоль
            sizes.add(size)
        return len(sizes) == 1  # Если все размеры одинаковы, множество будет содержать только один элемент
