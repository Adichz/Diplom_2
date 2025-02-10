import allure
from method import ChangeUser

@allure.feature('Класс тестирования изменения данных пользователя.')
class TestChangeUser:

    @allure.title('Меняем данные пользователя с авторизацией. Ожидаем ответ = 200, True')
    def test_change_user_with_auth(self):
        user = ChangeUser.change_user_with_auth()
        assert user.status_code == 200 and user.json()['success'] == True

    @allure.title('Меняем данные пользователя без авторизации. Ожидаем ответ = 401, You should be authorised')
    def test_change_user_no_auth(self):
        user = ChangeUser.change_user_no_auth()
        assert user.status_code == 401 and user.json()['message'] == 'You should be authorised'