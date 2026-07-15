import shelve
import hashlib
import secrets 

# This is where all of the user profile stuff goes

def load_user(username):
        with shelve.open("Storage") as db:
            return db[username]

def save_user(user_obj):
        with shelve.open("Storage") as db:
            db[user_obj.username] = user_obj

def Hash(text): 
    salt = "kalsdjfa;jsdlkfjsldjfa;l"
    iterations = 50000
    dk = hashlib.pbkdf2_hmac(
            "sha256",              # underlying hash
            text.lower().encode(), # password
            salt.encode(),         # salt
            iterations             # stretching
        )
    return dk.hex()

class User:
    def __init__(self, username, password):
        self.username = username
        self.salt = secrets.token_hex(16)
        self.password = self.PassEncrypt(password)
        self.note_count = 0
        self.notes = {}

    def add_note(self, title, content):
        self.note_count += 1
        nid = f"Note{self.note_count}"
        self.notes[nid] = {"name": title, "content": content}
        return nid
    def list_note_names(self):
        return [note["name"] for note in self.notes.values()]
    def isNote(self, notename):
         return any(data["name"] == notename for data in self.notes.values())
    def PassEncrypt(self, text): 
        iterations = 50000
        dk = hashlib.pbkdf2_hmac(
            "sha256",              # underlying hash
            text.lower().encode(), # password
            self.salt.encode(),         # salt
            iterations             # stretching
        )
        return dk.hex()