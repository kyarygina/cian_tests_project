import allure
from allure_commons.types import Severity
from pages.web.main_page import MainPage

@allure.epic("Web UI Tests")
@allure.feature("Навигационные вкладки в хедере страницы")
@allure.story("Проверка навигационных вкладок в хедере главной страницы")
class TestHeaderTabs:

    main_page = MainPage()

    @allure.tag("web")
    @allure.severity(Severity.NORMAL)
    @allure.label("owner", "kyarygina")
    def test_header_navigation_tabs(self):
        expected_tabs = [
            "Аренда",
            "Продажа",
            "Новостройки",
            "Дома и участки",
            "Коммерческая",
            "Ипотека",
            "Сервисы"
        ]

        with allure.step("Проверить навигационные вкладки в хедере главной страницы"):
            self.main_page.should_header_navigation_tabs_have_text(*expected_tabs)

    @allure.tag("web")
    @allure.severity(Severity.NORMAL)
    @allure.label("owner", "kyarygina")
    def test_header_link_tabs(self):
        expected_tabs = [
            "Мой дом",
            "Сделка",
            "Приложение Циан"
        ]

        with allure.step("Проверить вкладки со ссылками в хедере главной страницы"):
            self.main_page.should_header_link_tabs_have_text(*expected_tabs)