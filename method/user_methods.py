import requests
import allure

from data import BASE_URL, CREATE_USER_URL, gen_payload

@allure.title('Методы создания Пользоваателя.')
class UserMethods:

    @staticmethod
    @allure.step('Создаем уникального пользователя')
    def create_user(payload):
        response = requests.post(f'{BASE_URL}{CREATE_USER_URL}', data=payload)
        return response

    @staticmethod
    @allure.step('Создаем пользователя без почты')
    def create_user_no_email():
        payload = gen_payload()
        response = requests.post(f'{BASE_URL}{CREATE_USER_URL}', data={'password': payload.get('password'), 'name': payload.get('name')})
        return response

    @staticmethod
    @allure.step('Создаем пользователя без пароля')
    def create_user_no_pwd():
        payload = gen_payload()
        response = requests.post(f'{BASE_URL}{CREATE_USER_URL}', data={'email': payload.get('email'), 'name': payload.get('name')})
        return response

    @staticmethod
    @allure.step('Создаем пользователя без имени')
    def create_user_no_name():
        payload = gen_payload()
        response = requests.post(f'{BASE_URL}{CREATE_USER_URL}', data={'email': payload.get('email'), 'password': payload.get('password')})
        return response


    @staticmethod
    @allure.step('Создаем пользователя 2 раза')
    def create_user_two_times():
        payload = gen_payload()
        requests.post(f'{BASE_URL}{CREATE_USER_URL}', data=payload)
        return requests.post(f'{BASE_URL}{CREATE_USER_URL}', data=payload)
