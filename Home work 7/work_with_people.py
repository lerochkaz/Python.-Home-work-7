def informatio_request():
    working_mode = int(
        input('Выберите режим работы, где 0-экспорт, а 1-импорт: '))
    return working_mode


def import_text():
    return input('Введите фамилию: ')


def getUserInput():
    return input('Введите ФИО тел заметки через пробел: ')
