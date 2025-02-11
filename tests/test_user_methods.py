import allure


from data import gen_payload
from method.user_methods import UserMethods

@allure.feature('Класс тестирования создания пользователя.')
class TestUser:

    @allure.title('Создаем пользователя с корректными данными. Ожидаем ответ = 200, True')
    def test_create_user(self):
        payload = gen_payload()
        new_user = UserMethods.create_user(payload)
        assert new_user.status_code == 200 and new_user.json()['success'] == True

    @allure.title('Создаем существующего пользователя. Ожидаем ответ = 403, User already exists')
    def test_create_user_two_times(self):
        new_user = UserMethods.create_user_two_times()
        assert new_user.status_code == 403 and new_user.json()['message'] == "User already exists"

    @allure.title('Создаем пользователя без почты. Ожидаем ответ = 403, Email, password and name are required fields')
    def test_create_user_no_email(self):
        new_user = UserMethods.create_user_no_email()
        assert new_user.status_code == 403 and new_user.json()['message'] == "Email, password and name are required fields"

    @allure.title('Создаем пользователя без пароля. Ожидаем ответ = 403, Email, password and name are required fields')
    def test_create_user_no_pwd(self):
        new_user = UserMethods.create_user_no_pwd()
        assert new_user.status_code == 403 and new_user.json()['message'] == "Email, password and name are required fields"

    @allure.title('Создаем пользователя без имени. Ожидаем ответ = 403, Email, password and name are required fields')
    def test_create_user_no_name(self):
        new_user = UserMethods.create_user_no_name()
        assert new_user.status_code == 403 and new_user.json()['message'] == "Email, password and name are required fields"
