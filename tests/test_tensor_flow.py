import pytest
from pages.sbis_contacts_page import SbisContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage


# Тест для проверки функциональности баннера Тензор на sbis.ru.
@pytest.mark.usefixtures("browser")
def test_tensor_banner(browser):
    # Шаг 1: Переход на сайт sbis.ru в раздел "Контакты"
    sbis_contacts_page = SbisContactsPage(browser)
    sbis_contacts_page.open("https://sbis.ru/contacts")

    # Шаг 2: Клик по баннеру Тензор
    sbis_contacts_page.click_tensor_banner()

    # Переключение на новую вкладку (страница tensor.ru)
    browser.switch_to.window(browser.window_handles[1])

    # Шаг 3: Проверка наличия блока "Сила в людях"
    tensor_main_page = TensorMainPage(browser)
    assert tensor_main_page.is_power_in_people_block_present(), "Блок 'Сила в людях' не найден"

    # Шаг 4: Переход на страницу "О нас"
    tensor_main_page.go_to_about_page()

    # Шаг 5: Проверка раздела "Работаем" и размеров изображений
    tensor_about_page = TensorAboutPage(browser)
    assert tensor_about_page.is_working_section_present(), "Раздел 'Работаем' не найден"
    assert tensor_about_page.check_images_dimensions(), "Фотографии имеют разные размеры"
