import requests

from data import BASE_URL, GET_USER_URL, gen_payload
from method.login_methods import LoginMethods


class ChangeUser:

    @staticmethod
    def change_user_with_auth():
        payload = gen_payload()
        log = LoginMethods.login_user()
        token = log.json()["accessToken"]
        user = requests.patch(f'{BASE_URL}{GET_USER_URL}', data=payload, headers={'Authorization': f"{token}"})
        return user

    @staticmethod
    def change_user_no_auth():
        payload = gen_payload()
        LoginMethods.login_user()
        user = requests.patch(f'{BASE_URL}{GET_USER_URL}', data=payload)
        return user
