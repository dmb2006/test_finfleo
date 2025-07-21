import allure
from allure_commons.types import Severity
from model.finfleo_page.main_page_submit import Submit_page


@allure.tag('Web')
@allure.link('https://finleo.ru', name='finfleo')
@allure.story('EXEP-1201')
@allure.severity(Severity.NORMAL)
@allure.feature('Заказ обратного звонка')
@allure.title('Заполнение формы')
def test_submit_application():
    with allure.step('Открытие страницы для отправки формы на обратный звонок'):
        submit_page = Submit_page()

    with allure.step('Заполнение формы тестовыми данными'):
        submit_page.fill_submit_form()

    with allure.step('Проверка, что формы отправлена и отображается message'):
        submit_page.should_fill_submit_form()
