import pytest
import time
import requests
from data import gen_payload, BASE_URL, LOGIN_URL, CREATE_USER_URL, GET_USER_URL


@pytest.fixture()
def create_user_and_get_token(timeout=10):
    start_time = time.time()
    try:
        payload = gen_payload()

        create_response = requests.post(f'{BASE_URL}{CREATE_USER_URL}', data=payload)
        create_response.raise_for_status()

        auth_payload = {key: value for key, value in payload.items() if key != 'name'}


        while True:
            login_response = requests.post(f'{BASE_URL}{LOGIN_URL}', data=auth_payload)
            if login_response.ok:
                response_data = login_response.json()
                if 'accessToken' in response_data:
                    token = response_data['accessToken']
                    yield token
                    break
            if time.time() - start_time > timeout:
                raise TimeoutError("Не удалось получить токен за отведенное время.")
            time.sleep(1)

    finally:

        if 'token' in locals():
            requests.delete(f'{BASE_URL}{GET_USER_URL}', headers={'Authorization': token})