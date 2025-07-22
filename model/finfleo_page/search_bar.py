from selene import browser, have


class Search_bar:
    def search_in_bar(self):
        browser.open('https://finleo.ru')
        browser.all('input[type=text]')[0].send_keys('БелАЗ').press_enter()
        browser.element('[class="search-bar__results--empty"]').should(have.exact_text('Ничего не найдено'))