import allure
from method.change_user_methods import ChangeUser
from conftest import create_user_and_get_token

@allure.feature('Класс тестирования изменения данных пользователя.')
class TestChangeUser:

    @allure.title('Меняем данные пользователя с авторизацией. Ожидаем ответ = 200, True')
    def test_change_user_with_auth(self, create_user_and_get_token):
        user = ChangeUser.change_user_with_auth()
        assert user.status_code == 200

    @allure.title('Меняем данные пользователя без авторизации. Ожидаем ответ = 401, You should be authorised')
    def test_change_user_no_auth(self):
        user = ChangeUser.change_user_no_auth()
        assert user.status_code == 401 and user.json()['message'] == 'You should be authorised'