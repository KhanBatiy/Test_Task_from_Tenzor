import pytest
from pages.sbis_contacts_page import SbisContactsPage


@pytest.mark.usefixtures("browser")
def test_change_region(browser):
    """
    Тест для проверки смены региона на странице контактов sbis.ru.
    """
    # Шаг 1: Переход на сайт sbis.ru в раздел "Контакты"
    sbis_contacts_page = SbisContactsPage(browser)
    sbis_contacts_page.open("https://sbis.ru/contacts")

    # Шаг 2: Проверка, что определился регион и есть список партнеров
    current_region = sbis_contacts_page.get_current_region()
    assert current_region, "Регион не определился"
    partners_list = sbis_contacts_page.get_partners_list()
    assert len(partners_list) > 0, "Список партнеров пуст"

    # Шаг 3: Изменение региона на Камчатский край
    sbis_contacts_page.change_region(sbis_contacts_page.KAMCHATKA_REGION)

    # Шаг 4: Проверка, что подставился выбранный регион, список партнеров изменился, URL и title содержат информацию о выбранном регионе
    new_region = sbis_contacts_page.get_current_region()
    assert new_region == "Камчатский край", f"Новый регион: {new_region}"

    new_partners_list = sbis_contacts_page.get_partners_list()
    assert len(new_partners_list) > 0, "Список партнеров пуст после смены региона"
    assert partners_list != new_partners_list, "Список партнеров не изменился"

    current_url = sbis_contacts_page.get_current_url()
    assert "41-kamchatskij-kraj" in current_url, "URL не содержит информацию о Камчатском крае"

    current_title = sbis_contacts_page.get_title()
    assert "Камчатский край" in current_title, "Заголовок страницы не содержит информацию о Камчатском крае"
