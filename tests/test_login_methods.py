import allure

from method.login_methods import LoginMethods

@allure.feature('Класс тестирования Входа.')
class TestLogin:

    @allure.title('Логинимся с верными данными. Ожидаем ответ = 200, заказ в сообщении')
    def test_login_user(self):
        login_user = LoginMethods.login_user()
        assert login_user.status_code == 200 and login_user.json()['success'] == True

    @allure.title('Логинимся без логина. Ожидаем ответ = 401, email or password are incorrect')
    def test_login_no_email(self):
        login_user = LoginMethods.login_user_no_email()
        assert login_user.status_code == 401 and login_user.json()['message'] == 'email or password are incorrect'

    @allure.title('Логинимся с неверным паролем. Ожидаем ответ = 401, email or password are incorrect')
    def test_login_wrong_pwd(self):
        login_user = LoginMethods.login_user_wrong_pwd()
        assert login_user.status_code == 401 and login_user.json()['message'] == 'email or password are incorrect'
