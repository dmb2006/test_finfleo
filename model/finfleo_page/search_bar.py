import allure
from selene import browser, have


class Search_bar:
    def search_in_bar(self):
        with allure.step('Открытие страницы'):
            browser.open('https://finleo.ru')
        with allure.step(f'Ввод в поисковую строку {'БелАЗ'}'):
            browser.all('input[type=text]')[0].send_keys('БелАЗ').press_enter()
        with allure.step('Проверка, что по данному запросу ничего не найдено'):
            browser.element('[class="search-bar__results--empty"]').should(have.exact_text('Ничего не найдено'))