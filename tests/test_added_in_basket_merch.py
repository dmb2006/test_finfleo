import allure
from allure_commons.types import Severity

from model.data.users import Basket_user
from model.finfleo_page.added_bascet_merge import Basket_merge


@allure.tag('Web')
@allure.link('https://marketplace.finleo.ru/store', name='finfleo/marketplace')
@allure.story('EXEP-1202')
@allure.severity(Severity.CRITICAL)
@allure.feature('Заказать Мерч')
@allure.title('Добавление Мерча в корзину')
def test_added_merge_in_basket():
    basket_merge = Basket_merge()

    basket_user = Basket_user(
        name='Jeny',
        phone='89117894512',
        email='jeny@yandex.ru',
        address='Moscow Moscovskay street 12'
    )

    basket_merge.added_merge_in_basket(basket_user)

    basket_merge.shoult_fill_form(basket_user)
