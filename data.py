import random
import string

BASE_URL = 'https://stellarburgers.nomoreparties.site/api/'
ORDERS_URL = 'orders'
INGR_URL = 'ingredients'
CREATE_USER_URL = 'auth/register'
LOGIN_URL = 'auth/login'
LOGOUT_URL = 'auth/logout'
GET_ORDER_URL = 'orders/all'
GET_USER_URL = 'auth/user'
ERROR_MSG = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>Error</title>\n</head>\n<body>\n<pre>Internal Server Error</pre>\n</body>\n</html>\n'



def gen_payload():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = generate_random_string(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": f'{email}@yandex.ru',
        "password": password,
        "name": name
    }
    return payload
