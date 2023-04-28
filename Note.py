import time
import uuid

class Note:
    def __init__(self, id = str(uuid.uuid1())[0:3], header = "Text", body = "Text" , time = time.strftime("Time %H:%M:%S Data %d.%m.%Y\n")):
        self.id = id
        self.header = header
        self.body = body
        self.time = time

    def get_id(note):
        return note.id
    
    def get_header(note):
        return note.header
    
    def get_body(note):
        return note.body
    
    def get_time(note):
        return note.time
    
    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]
        
    def set_header(note,header):
        note.header = header
        
    def set_body(note,body):
        note.body = body
        
    def set_date(note):
        note.date = time.strftime("Time %H:%M:%S Data %d.%m.%Y\n")
        
    def to_string(note):
        return note.id + ';' + note.header + ';' + note.body + ';' + note.time

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.header + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.time       
    
    
        
