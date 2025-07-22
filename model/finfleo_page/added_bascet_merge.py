import allure
from selene import browser, have, be
from model.data.users import Basket_user


class Basket_merge:
    def __init__(self):
        self.main_url = browser.open('https://finleo.ru/')
        self.go_to_shops = browser.element('a[href="https://marketplace.finleo.ru/store"]')
        self.click_powerbank = browser.element('a[href="https://marketplace.finleo.ru/tproduct/800240342-494631817652-power-bank-prizvanie"]')
        self.added_power_bank_in_basket = browser.element('#rec809397496 .js-store-prod-popup-buy-btn-txt')
        self.current_address = browser.element('[id="input_1726812687876"]')

    def added_merge_in_basket(self, user: Basket_user):
        with allure.step('Открытие страницы https://finleo.ru/'):
            self.main_url
        with allure.step('Переход по ссылке на marketplace'):
            self.go_to_shops.should(be.clickable).click()
        with allure.step('Выбор powerbank'):
            self.click_powerbank.click()
        with allure.step('Добавление powerbank в корзину'):
            self.added_power_bank_in_basket.click()
        with allure.step('Заполнение имени'):
            browser.element('[id="input_1496239431201"]').send_keys(user.name)
        with allure.step('Заполнение телефона'):
            browser.element('[type="tel"]').send_keys(user.phone)
        with allure.step('Заполнение email'):
            browser.element('[type="email"]').send_keys(user.email)
        with allure.step('Заполнение адреса'):
            self.current_address.send_keys(user.address)
        with allure.step('Отправка заполненной формы'):
            browser.element('[type="submit"]').click()


    def shoult_fill_form(self, user: Basket_user):
        with allure.step('Проверка, что заказа принят'):
            browser.element('[id="form797298622"]').should(have.text('Спасибо! Данные успешно отправлены.'))