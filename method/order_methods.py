import requests
import allure

from data import BASE_URL, ORDERS_URL, LOGOUT_URL
from method.login_methods import LoginMethods


class OrderMethods:

    @staticmethod
    @allure.step('Создаем заказ с авторизацией')
    def create_order_with_auth():
        LoginMethods.login_user()
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', data=ingredients)
        return response


    @staticmethod
    @allure.step('Создаем заказ без авторизации')
    def create_order_no_auth():
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        log = LoginMethods.login_user()
        token = log.json()["refreshToken"]
        requests.post(f'{BASE_URL}{LOGOUT_URL}', data={"token": f"{token}"})
        return requests.post(f'{BASE_URL}{ORDERS_URL}', data=ingredients)


    @staticmethod
    @allure.step('Создаем заказ без ингредиентов')
    def create_order_no_ingredients():
        LoginMethods.login_user()
        ingredients = {"ingredients": [""]}
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', data=ingredients)
        return response

    @staticmethod
    @allure.step('Создаем заказ с неправильным хешем')
    def create_order_wrong_ingredients():
        LoginMethods.login_user()
        ingredients = {"ingredients": ["1111111111111111"]}
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', data=ingredients)
        return response

    @staticmethod
    @allure.step('Получаем заказ без авторизации')
    def get_order_no_auth():
        log = LoginMethods.login_user()
        token = log.json()["refreshToken"]
        requests.post(f'{BASE_URL}{LOGOUT_URL}', data={"token": f"{token}"})
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response

    @staticmethod
    @allure.step('Получаем заказ c авторизацией')
    def get_order_with_auth():
        log = LoginMethods.login_user()
        token = log.json()["accessToken"]
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        requests.post(f'{BASE_URL}{ORDERS_URL}', data=ingredients)
        response = requests.get(f'{BASE_URL}{ORDERS_URL}', headers={"Authorization": f"{token}"})
        return response
