# This is where all functions go 
from User import *

print("Wrong File.")
# 5, New Note
def NewNote(username):
    notewriting = f"You will now create a semi-secure storage cell that's called a Note. Each note is independent and tied to your account ({username}) with us.\nYour name can be anything you want. It is used to read the note later.\nPress enter to cancel note creation at any time.\nWhat would you like the note to be called? "
    name = input(notewriting)
    print()
    content = input(f"Your note ({name}) will be saved shortly. What would you like the contents of the note to be? (this can be changed)\n\n>")
    if name == "" or content == "":
        pass
    user_obj = load_user(username) 
    notecount = user_obj.add_note(name, content)
    save_user(user_obj)
    if len(content) < 15:
        whatsinit = f", \"{content}\""
    else: 
        whatsinit = f" something that has {len(content)} characters"

    print(f"Perfect. {name} has been saved for account {username}. It says{whatsinit}. (For debuging purposes, it is acualy note {notecount})")

# 6 Edit Note
def EditNote(username):
    notename1 = input(f"You requested to edit a note.\nEnter the name of the note you would like to edit, enter anything to see note names, or press enter to exit.\n")
    if notename1 == "":
        pass
    user_obj = load_user(username)    
    if user_obj.isNote(notename1):
        print("y")   # FINISH EDIT NOTE
    else:
        print("That is not a note name.")
        ListNote(username)
        notename2 = input("Whitch note would you like to edit? (if cancel, press enter)\n")
        if user_obj.isNote(notename2):
            print("y") # FINISH EDIT NOTE
        else:
            print("Sorry, that is not a note. Try again (press 6) or create a note by pressing 5.")
        


# 7 List Note
def ListNote(username):
    print("These are all of the notes that you have")
    user_obj = load_user(username)
    names = user_obj.list_note_names()
    st = ""
    for name in names:
        st = st + f"    {name}"
        
    print(st.strip())