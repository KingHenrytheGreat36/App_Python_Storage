# This is where all functions go 
from User import *

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