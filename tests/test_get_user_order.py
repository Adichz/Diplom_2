import allure
from method import OrderMethods

@allure.feature('Класс тестирования получения заказа.')
class TestGetUserOrder:

    @allure.title('Получаем заказ авторизированного пользователя. Ожидаем ответ = 200, заказ в сообщении')
    def test_get_order_with_auth(self):
        new_order = OrderMethods.get_order_with_auth()
        assert new_order.status_code == 200 and  "orders" in new_order.text

    @allure.title('Получаем заказ  не авторизированного пользователя. Ожидаем ответ = 401, You should be authorised')
    def test_get_order_no_auth(self):
        new_order = OrderMethods.get_order_no_auth()
        assert new_order.status_code == 401 and new_order.json()['message'] == "You should be authorised"