from model.data.users import Submit_user
from selene import browser, have, be, command


class Submit_page:
    def __init__(self):
        self.cookies_popup = browser.element('/html/body/div[1]/button[1]')

    def fill_submit_form(self):
        browser.open('https://finleo.ru')
        self.cookies_popup.click()

        browser.element('[name="name"]').send_keys(Submit_user.name)
        browser.element('[name="phone"]').send_keys(Submit_user.phone)
        browser.element('[type="submit"]').perform(command.js.click)
        return

    def should_fill_submit_form(self):
        browser.element('[class="form-favorable-offer__form--title"]').should(have.text('Оставить заявку'))
        browser.element('[role="status"]').should(have.text('Заявка принята'))
        return