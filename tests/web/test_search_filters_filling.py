import allure
from allure_commons.types import Severity
from pages.web.main_page import MainPage

main_page = MainPage()

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.suite("Фильтры поиска на главной странице")
@allure.title("Проверка фильтров на вкладке 'Купить'")
@allure.link("https://www.cian.ru", name="Testing")
def test_buy_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Купить'"):
        (
            main_page
            .click_buy_realty_type_dropdown()
            .click_house_checkbox()
            .click_buy_realty_price_dropdown()
            .fill_buy_realty_price_from_input('7000000')
            .fill_buy_realty_price_to_input('9000000')
            .fill_buy_realty_location_input('Сочи')
            .click_buy_realty_location()
        )

    with allure.step("Проверить, что фильтры заполнены корректно"):
        main_page.should_buy_realty_filters_have_text('Дом, дачу', '7 - 9 млн', 'Краснодарский край, Сочи')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.suite("Фильтры поиска на главной странице")
@allure.title("Проверка фильтров на вкладке 'Снять'")
@allure.link("https://www.cian.ru", name="Testing")
def test_rent_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Снять'"):
        (
            main_page
            .click_rent_realty_tab()
            .click_rent_realty_price_dropdown()
            .fill_rent_realty_price_from_input('20000')
            .fill_rent_realty_price_to_input('30000')
            .fill_rent_realty_location_input('Краснодар')
            .click_rent_realty_location()
        )
    with allure.step("Проверить, что фильтры заполнены корректно"):
        main_page.should_rent_realty_filters_have_text('Квартиру', '1, 2 комн.', '20 - 30 тыс', 'Краснодар')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.suite("Фильтры поиска на главной странице")
@allure.title("Проверка фильтров на вкладке 'Посуточно'")
@allure.link("https://www.cian.ru", name="Testing")
def test_daily_rent_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Посуточно'"):
        (
            main_page
            .click_daily_rent_realty_tab()
            .fill_daily_rent_location_input('Калининград')
            .click_daily_rent_realty_location()
        )
    with allure.step("Проверить, что фильтры заполнены корректно"):
        main_page.should_daily_rent_realty_filters_have_text('Калининград')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.suite("Фильтры поиска на главной странице")
@allure.title("Проверка фильтров на вкладке 'Ипотека'")
@allure.link("https://www.cian.ru", name="Testing")
def test_mortgage_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Ипотека'"):
        (
            main_page
            .click_mortgage_realty_tab()
            .click_mortgage_realty_type_dropdown()
            .click_mortgage_realty_newbuilding_checkbox()
            .fill_mortgage_realty_price('9000000')
            .fill_mortgage_realty_down_payment('3000000')
            .click_mortgage_realty_term()
            .click_mortgage_realty_term_from_list()
        )
    with allure.step("Проверить, что фильтры заполнены корректно"):
        main_page.should_mortgage_realty_filters_have_text('Квартира в новостройке', '9 000 000', '3 000 000', '20 лет')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.suite("Фильтры поиска на главной странице")
@allure.title("Проверка диалогового окна на вкладке 'Подбор риелтора'")
@allure.link("https://www.cian.ru", name="Testing")
def test_realtor_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Подбор риелтора'"):
        (
            main_page
            .click_realtor_realty_tab()
        )
    with allure.step("Проверить, что открыто окно с заголовком 'С чем нужна помощь риелтора?'"):
        main_page.should_header_have_text('С чем нужна помощь риелтора?')