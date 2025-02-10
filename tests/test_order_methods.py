import allure
from method import OrderMethods

@allure.feature('Класс тестирования создания заказов.')
class TestOrders:

    @allure.title('Создаем заказ авторизированным пользователем с ингредиентами. Ожидаем ответ = 200, True')
    def test_create_order_with_auth_and_ingredients(self):
        new_order = OrderMethods.create_order_with_auth()
        assert new_order.status_code == 200 and new_order.json()['success'] == True

    @allure.title('Создаем заказ авторизированным пользователем без ингредиентов. Ожидаем ответ = 400, Ingredient ids must be provided')
    def test_create_order_no_ingredients(self):
        new_order = OrderMethods.create_order_no_ingredients()
        assert new_order.status_code == 400 and new_order.json()['message'] == 'Ingredient ids must be provided'

    @allure.title('Создаем заказ авторизированным пользователем с неверным хешем ингредиентов. Ожидаем ответ = 500')
    def test_create_order_wrong_ingredients(self):
        new_order = OrderMethods.create_order_wrong_ingredients()
        assert new_order.status_code == 500

    @allure.title('Создаем заказ не авторизированным пользователем с ингредиентами. Ожидаем ответ = 200, True')
    def test_create_order_no_auth(self):
        new_order = OrderMethods.create_order_no_auth()
        assert new_order.status_code == 200 and new_order.json()['success'] == True