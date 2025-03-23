from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


# Класс для работы со страницей контактов на sbis.ru.
class SbisContactsPage(BasePage):
    # Локаторы
    TENSOR_BANNER = ("xpath", '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')
    REGION_SELECTOR = ("xpath", '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    PARTNERS_LIST = ("xpath", '//*[@id="contacts_list"]//div[contains(@class, "controls-ListView__itemV")]')
    KAMCHATKA_REGION = ("xpath", '//span[@title="Камчатский край"]')

    def get_current_region(self):
        # Возвращает текущий регион.
        return self.get_text(self.REGION_SELECTOR)

    def get_partners_list(self):
        # Возвращает список партнеров.
        return self.find_elements(self.PARTNERS_LIST)

    def change_region(self, region_locator):
        # Изменяет регион на указанный.
        self.click_element(self.REGION_SELECTOR)  # Открываем список регионов
        self.click_element(region_locator)  # Выбираем указанный регион
        # Ожидание обновления региона
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.REGION_SELECTOR, "Камчатский край")
        )

    def click_tensor_banner(self):
        # Кликает по баннеру Тензор.
        self.click_element(self.TENSOR_BANNER)
