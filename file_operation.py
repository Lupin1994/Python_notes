import Note

def write_file(array):
    file = open("Notes_list.txt", 'w', encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close()
    
def read_file():
    try:
        array = []
        file = open("Notes_list.txt", 'r', encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(id = split_n[0],header=split_n[1],body = split_n[2],time = split_n[3])
            array.append(note)
    except Exception:
        print("Заметки пусты")
    finally:
        return array
