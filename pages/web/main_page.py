import allure
from selene import browser
from selene.support.conditions import have


class MainPage:

    def __init__(self):

        # Элементы на вкладке "Купить"
        self.buy_realty_type_dropdown = browser.element('button[title="Квартиру в новостройке и вторичке"]')
        self.buy_realty_house_checkbox = browser.all('span').element_by(have.text('Дом, дача'))
        self.buy_realty_price_dropdown = browser.all('button').element_by(have.text('Цена'))
        self.buy_realty_price_from_input = browser.element('input[placeholder="от"]')
        self.buy_realty_price_to_input = browser.element('input[placeholder="до"]')
        self.buy_realty_location_input = browser.element('input[placeholder="Город, адрес, метро, район, ж/д или шоссе"]')
        self.buy_realty_location = browser.element('[title="Сочи, Краснодарский край"]')
        self.buy_realty_type_filled_filter = browser.element('button[title="Дом, дачу"]')
        self.buy_realty_price_filled_filter = browser.element('button[title = "7 000 000 - 9 000 000 ₽"]')
        self.buy_realty_location_filled_filter = browser.element('#geo-suggest-input')

        # Элементы на вкладке "Снять"
        self.rent_realty_tab = browser.all('a').element_by(have.text('Снять'))
        self.rent_realty_price_dropdown = browser.all('button').element_by(have.text('Цена'))
        self.rent_realty_price_from_input = browser.element('input[placeholder="от"]')
        self.rent_realty_price_to_input = browser.element('input[placeholder="до"]')
        self.rent_realty_location_input = browser.element('input[placeholder="Город, адрес, метро, район, ж/д, шоссе или ЖК"]')
        self.rent_realty_location = browser.element('span[title="Краснодар"]')
        self.rent_realty_type_filled_filter = browser.element('button[title="Квартиру"]')
        self.rent_realty_size_filled_filter = browser.element('button[title="1, 2 комн."]')
        self.rent_realty_price_filled_filter = browser.element('button[title="20 000 - 30 000 ₽"]')
        self.rent_realty_location_filled_filter = browser.element('#geo-suggest-input')

        # Элементы на вкладке "Посуточно"
        self.daily_rent_realty_tab = browser.all('a').element_by(have.text('Посуточно'))
        self.daily_rent_location_input = browser.element('input[placeholder="Куда вы хотите поехать?"]')
        self.daily_rent_realty_location = browser.element('span[title="Калининград"]')
        self.daily_rent_realty_location_filled_filter = browser.element('#geo-suggest-input')
        self.daily_rent_realty_type_filled_filter = browser.element('button[title="Квартиру"]')

        # Элементы на вкладке "Ипотека"
        self.mortgage_realty_tab = browser.all('ul[data-name="FiltersTabs"] a').element_by(have.text('Ипотека'))
        self.mortgage_realty_type_dropdown = browser.all('button').element_by(have.text('Квартира во вторичке'))
        self.mortgage_realty_newbuilding_checkbox = browser.all('button').element_by(have.text('Квартира в новостройке'))
        self.mortgage_realty_price = browser.element('input[placeholder="Стоимость недвижимости"]')
        self.mortgage_realty_down_payment = browser.element('input[placeholder="Первоначальный взнос"]')
        self.mortgage_realty_term = browser.all('button').element_by(have.text('Срок'))
        self.mortgage_realty_term_from_list = browser.all('button').element_by(have.text('20 лет'))
        self.mortgage_realty_location_input = browser.element('input[placeholder="Город"]')
        self.mortgage_realty_location = browser.all('span').element_by(have.text('Саратов'))
        self.mortgage_realty_right_button = browser.element('[data-mark="FiltersMortgageRightButton"]')
        self.mortgage_realty_type_filled_filter = browser.all('button').element_by(have.text('Квартира в новостройке'))
        self.mortgage_realty_price_filled_filter = browser.element('input[placeholder="Стоимость недвижимости"]')
        self.mortgage_realty_down_payment_filled_filter = browser.element('input[placeholder="Первоначальный взнос"]')
        self.mortgage_realty_term_filled_filter = browser.all('button').element_by(have.text('20 лет'))

        # Элементы на вкладке "Подбор риелтора"
        self.realtor_realty_tab = browser.all('a').element_by(have.text('Подбор риелтора'))
        self.realtor_question_tab = browser.element('div[data-name="CPDModalContainer"] span')

    # Методы для вкладки "Купить"

    @allure.step("Нажать на дропдаун с выбором типа недвижимости")
    def click_buy_realty_type_dropdown(self):
        self.buy_realty_type_dropdown.click()
        return self

    @allure.step("Выбрать чек-бокс 'Дом,дача'")
    def click_house_checkbox(self):
        self.buy_realty_house_checkbox.click()
        return self

    @allure.step("Нажать на дропдаун с выбором цены")
    def click_buy_realty_price_dropdown(self):
        self.buy_realty_price_dropdown.click()
        return self

    @allure.step("Заполнить поле с ценой 'от'")
    def fill_buy_realty_price_from_input(self, value):
        self.buy_realty_price_from_input.set_value(value)
        return self

    @allure.step("Заполнить поле с ценой 'до'")
    def fill_buy_realty_price_to_input(self, value):
        self.buy_realty_price_to_input.set_value(value)
        return self

    @allure.step("Заполнить поле с локацией")
    def fill_buy_realty_location_input(self, value):
        self.buy_realty_location_input.set_value(value)
        return self

    @allure.step("Нажать на локацию из выпадающего списка")
    def click_buy_realty_location(self):
        self.buy_realty_location.click()
        return self

    @allure.step("Проверить наличие текста в заполненных фильтрах на вкладке 'Купить'")
    def should_buy_realty_filters_have_text(self, realty_type, realty_price, realty_location):
        self.buy_realty_type_filled_filter.should(have.text(realty_type))
        self.buy_realty_price_filled_filter.should(have.text(realty_price))
        self.buy_realty_location_filled_filter.should(have.value(realty_location))
        return self

    # Методы для вкладки "Снять"

    @allure.step("Нажать на вкладку 'Снять'")
    def click_rent_realty_tab(self):
        self.rent_realty_tab.click()
        return self

    @allure.step("Нажать на дропдаун с выбором цены")
    def click_rent_realty_price_dropdown(self):
        self.rent_realty_price_dropdown.click()
        return self

    @allure.step("Заполнить поле с ценой 'от'")
    def fill_rent_realty_price_from_input(self, value):
        self.rent_realty_price_from_input.set_value(value)
        return self

    @allure.step("Заполнить поле с ценой 'до'")
    def fill_rent_realty_price_to_input(self, value):
        self.rent_realty_price_to_input.set_value(value)
        return self

    @allure.step("Заполнить поле с локацией")
    def fill_rent_realty_location_input(self, value):
        self.rent_realty_location_input.set_value(value)
        return self

    @allure.step("Нажать на локацию из выпадающего списка")
    def click_rent_realty_location(self):
        self.rent_realty_location.click()
        return self

    @allure.step("Проверить наличие текста в заполненных фильтрах на вкладке 'Снять'")
    def should_rent_realty_filters_have_text(self, realty_type, realty_size, realty_price, realty_location):
        self.rent_realty_type_filled_filter.should(have.text(realty_type))
        self.rent_realty_size_filled_filter.should(have.text(realty_size))
        self.rent_realty_price_filled_filter.should(have.text(realty_price))
        self.rent_realty_location_filled_filter.should(have.value(realty_location))
        return self

    # Методы для вкладки "Посуточно"

    @allure.step("Нажать на вкладку 'Посуточно'")
    def click_daily_rent_realty_tab(self):
        self.daily_rent_realty_tab.click()
        return self

    @allure.step("Заполнить поле с локацией")
    def fill_daily_rent_location_input(self, value):
        self.daily_rent_location_input.set_value(value)
        return self

    @allure.step("Нажать на локацию из выпадающего списка")
    def click_daily_rent_realty_location(self):
        self.daily_rent_realty_location.click()
        return self

    @allure.step("Проверить наличие текста в заполненных фильтрах на вкладке 'Посуточно'")
    def should_daily_rent_realty_filters_have_text(self, realty_location):
        self.daily_rent_realty_location_filled_filter.should(have.value(realty_location))
        return self

    # Методы для вкладки "Ипотека"

    @allure.step("Нажать на вкладку 'Ипотека'")
    def click_mortgage_realty_tab(self):
        self.mortgage_realty_tab.click()
        return self

    @allure.step("Нажать на дропдаун с выбором типа недвижимости")
    def click_mortgage_realty_type_dropdown(self):
        self.mortgage_realty_type_dropdown.click()
        return self

    @allure.step("Выбрать чек-бокс 'Квартира в новостройке'")
    def click_mortgage_realty_newbuilding_checkbox(self):
        self.mortgage_realty_newbuilding_checkbox.click()
        return self

    @allure.step("Указать стоимость недвижимости")
    def fill_mortgage_realty_price(self, value):
        self.mortgage_realty_price.set_value(value)
        return self

    @allure.step("Указать сумму первоначального взноса")
    def fill_mortgage_realty_down_payment(self, value):
        self.mortgage_realty_down_payment.set_value(value)
        return self

    @allure.step("Нажать на дропдаун с выбором срока ипотеки")
    def click_mortgage_realty_term(self):
        self.mortgage_realty_term.click()
        return self

    @allure.step("Выбрать срок ипотеки")
    def click_mortgage_realty_term_from_list(self):
        self.mortgage_realty_term_from_list.click()
        return self

    @allure.step("Проверить наличие текста в заполненных фильтрах на вкладке 'Ипотека'")
    def should_mortgage_realty_filters_have_text(self, realty_type, realty_price, realty_down_payment, realty_term):
        self.mortgage_realty_type_filled_filter.should(have.text(realty_type))
        self.mortgage_realty_price_filled_filter.should(have.value(realty_price))
        self.mortgage_realty_down_payment_filled_filter.should(have.value(realty_down_payment))
        self.mortgage_realty_term_filled_filter.should(have.text(realty_term))
        return self

    # Методы для вкладки "Подбор риелтора"

    @allure.step("Нажать на вкладку 'Подбор риелтора'")
    def click_realtor_realty_tab(self):
        self.realtor_realty_tab.click()
        return self

    @allure.step("Проверить наличие текста в заголовке")
    def should_header_have_text(self,value):
        self.realtor_question_tab.should(have.text(value))
        return self