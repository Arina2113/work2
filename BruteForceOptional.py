class BruteForceOptional:
    currentPassword = [0]
    characters = []
    length = 0


    def __get_string_password(self):
        """
        Метод для конвертирования набора чисел в буквенный пароль.
        Пример:
        currentPassword = [3, 4, 1, 1],
        characters = [p, y, t, h, o, n],
        result = "hoyy".
        """
        # Создаём переменную
        result = ""
        # Проходим по urrentPassword
        for i in range(len(self.currentPassword)):
            # Заменяем цифры на буквы в соответствии с позицией в characters
            result += self.characters[self.currentPassword[i]]
        return result

    def __increase_password(self, index):
        """
        :param index - индекс, где происходит увлеичение разряда

        Увеличение происходит путем добавления единицы к последнему значению.
        Если значение больше, чем длина characters, значение приравнивается к нулю и
        происходит добавление к следующиему разряду.

        Сам метод рекрсивный: увеличиваем на 1 разряд, передающийся как индекс.
        Если увеличить нельзя: обнуляем и увеличиваем следующий.

        Возвращает False, если не удалось увеличить, True, сли получилось.

        Пример:
        currentPassword = [1, 3, 5, 5],
        characters = [p, y, t, h, o, n],
        currentPassword (после увеличения) = [1, 4, 0, 0].
        """

        # Промерка, если значение уже нужно обнулить
        if self.currentPassword[index] == len(self.characters) - 1:
            # Если индекс нельзя изменить
            if index == 0:
                return False
            else:
                # Увеличиваем следующий индекс, а значение этого обнуляем
                self.currentPassword[index] = 0
                return self.__increase_password(index - 1)
        # Если значение недостаточно большое для обнуления
        else:
            #  Увеличиваем значение по индексу
            self.currentPassword[index] = self.currentPassword[index] + 1
            return True

    def get_password(self):
        """Получаем следующий пароль."""
        # Формируем текстовый пароль
        result = self.__get_string_password()
        # Проверяем, можно ли увеличить (в логике происходит увеличение пароля)
        if not self.__increase_password(len(self.currentPassword) - 1):
            # Если нельзя, возвращаем пустой результат
            result = ""
        return result

    def __init__(self, characters, length):
        """
        :param characters: Переменная для сохранения результата подбора пароля.
        Содержит в себе цифры, обозначающие индексы в characters.
        Длина length.
        :param length: Длина пароля.

        characters - Список символов, из которых осуществляется составление пароля.
        Остаются только уникальные символы.
        """
        # Оставляем только уникальзые символы
        self.characters = list(set(list(characters)))
        # Получаем список нужной длины
        self.currentPassword = [0] * length
        # Сохраняем длину
        self.length = length
        pass
