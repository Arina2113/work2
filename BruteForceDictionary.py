class BruteForceDictionary:
    """
    Падбор пароля из списка предложенных в файле
    """

    # Имя файла
    filename = 'dictionary.txt'
    # Стрим для чтения
    file = open(filename)
    # Текущий пароль
    currentPassword = file.readline()

    def get_password(self):
        """
        :return: Текущий пароль. Если файл закончится, будет выдавать пустую строчку
        """
        result = self.currentPassword
        # Изменение текущего пароля
        self.currentPassword = self.file.readline()
        # даляем пробелы
        return result.rstrip()

    def __init__(self):
        pass
