import Note


def action_number():
    action_number = int(input(" 1-вывод всех заметок \n 2-Создать заметку \n 3-удалить заметку \n 4-редактировать заметку \n 5-выход \n Введите номер действия: "))
    return action_number



def create_note(number):
    header = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return Note.Note(header=header, body=body)

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text

def goodbuy():
    print("До свидания!Хорошего Вам дня.")