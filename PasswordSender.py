import requests

class PasswordSender:
    address = ""
    username = ""

    def __init__(self, address, username):
        """
        :param address: Адресс, куда присываются запросы на авторизацию
        :param username: Аккаунт, к которому подбирается пароль
        """
        self.address = address
        self.username = username
        pass

    def send_password(self, password):
        """
        :param password: Пароль для отправки
        :return: Если код ответа 200 (т.е. происзошел вход) присылается True. Иначе, False
        """
        # Формирование ПОСТ запроса. В пост-завпросе хранятся логин и пароль
        response = requests.post(self.address, data={'username': self.username, 'password': password})
        if response.status_code < 300 :
            return True
        else:
            return False
