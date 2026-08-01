import datetime
import shelve
import hashlib
import secrets 
from datetime import datetime


# This is where all of the user profile stuff goes
def Log(msg):
    today = datetime.now().strftime("%m/%d/%y")
    print(f"{today} {msg}")

def ErrorLog(msg):
    today = datetime.now().strftime("%m/%d/%y")
    print(f"{today}\033[91m   Error!: {msg}\033[0m")   # red text
    Log(msg)



def load_user(username):
        with shelve.open("Py_Storage") as db:
            return db[username]

def save_user(user_obj):
        with shelve.open("Py_Storage") as db:
            db[user_obj.username] = user_obj
def is_OK_username(username):       # Fix this in issue #5 !
    if username.strip() == "":
        Log("Invalid username: empty string")
        return False
    if username.strip() == "admin":
        Log("Invalid username: 'admin' is reserved")
        return False
    with shelve.open("Py_Storage") as db:
        return username not in db
    


def hash(text, salt): 
    iterations = 50000
    dk = hashlib.pbkdf2_hmac(
            "sha256",              # underlying hash
            text.lower().encode(),
            salt.encode(), # password
            iterations             # stretching
        )
    return dk.hex()

class User:
    def __init__(self, username, password):
        self.username = username
        self.nickname = username.capitalize()
        self.salt = secrets.token_hex(16)
        self.password = self.encrypt_pass(password)
        self.note_count = 0
        self.notes = {}

    def add_note(self, title, content):
        self.note_count += 1
        noteid = f"Note{self.note_count}"
        self.notes[noteid] = {"name": title, "content": content}
        return noteid
    def encrypt_pass(self, text): 
        iterations = 50000
        dk = hashlib.pbkdf2_hmac(
            "sha256",              # underlying hash
            text.lower().encode(), # password
            self.salt.encode(),         # salt
            iterations             # stretching
        )
        return dk.hex()
    def delete_acount(self):
        username = self.username.lower()

        with shelve.open("Py_Storage") as db:
            if username in db:
                del db[username]
                return True
            else:
                return False