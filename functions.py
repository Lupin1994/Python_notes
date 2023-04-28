import file_operation
import Note
import view

number = 2 # Минимальное количество символов

def add():
    note = view.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array)
    print('Заметка создана успешно')

def show(text):
    logic = True
    array = file_operation.read_file()
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
    if logic == True:
        print("Заметок нет")
        
def del_show(text): 
    id = input('Введите id заметки: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = view.create_note(number)
                Note.Note.set_header(notes,note.get_header())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена')
    if logic == True:
        print('Такой заметки нет')
    file_operation.write_file(array)