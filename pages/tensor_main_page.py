from pages.base_page import BasePage


# Класс для работы с главной страницей tensor.ru.
class TensorMainPage(BasePage):
    # Локатор блока "Сила в людях"
    POWER_IN_PEOPLE_BLOCK = ("xpath", '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    # Локатор ссылки "Подробнее" в блоке "Сила в людях"
    DETAILS_LINK = ("xpath", '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')

    def is_power_in_people_block_present(self):
        # Проверяет, отображается ли блок "Сила в людях".
        return self.find_element(self.POWER_IN_PEOPLE_BLOCK).is_displayed()

    def go_to_about_page(self):
        # Прокручивает страницу до ссылки "Подробнее" и кликает по ней.
        self.scroll_to_element(self.DETAILS_LINK)
        self.click_element(self.DETAILS_LINK)
