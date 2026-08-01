import shelve
import uuid

def load_note(noteid):
        with shelve.open("Notes") as db:
            return db[noteid]

def save_note(note_obj):
        with shelve.open("Notes") as db:
            db[note_obj.id] = note_obj
class Note:
    def __init__(self, name, content, owner):
        self.name = name
        self.id = str(uuid.uuid4())
        self.content = content
        self.owner = owner