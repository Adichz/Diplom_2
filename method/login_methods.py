import requests
import allure

from data import gen_payload, BASE_URL, LOGIN_URL
from method.user_methods import UserMethods

@allure.title('Методы Логина Пользователя.')
class LoginMethods:

    @staticmethod
    @allure.step('Логинимся пользователем')
    def login_user():
        payload = gen_payload()
        UserMethods.create_user(payload)
        return requests.post(f'{BASE_URL}{LOGIN_URL}', data={'email': payload.get('email'), 'password': payload.get('password')})


    @staticmethod
    @allure.step('Логинимся пользователем без почты')
    def login_user_no_email():
        payload = gen_payload()
        UserMethods.create_user(payload)
        return requests.post(f'{BASE_URL}{LOGIN_URL}', data={'password': payload.get('password')})

    @staticmethod
    @allure.step('Логинимся пользователем c неверным паролем')
    def login_user_wrong_pwd():
        payload = gen_payload()
        UserMethods.create_user(payload)
        return requests.post(f'{BASE_URL}{LOGIN_URL}', data={'email': payload.get('email'), 'password': payload.get('parrol')})

