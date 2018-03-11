import tkinter
global root
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
root=tkinter.Tk()
root.title("HANGMAN GAME")
root.geometry('400x400+400+400')
frame = tkinter.Frame(root,padx=20, pady=20)
TOKEN = 'B7D85MZqK_AAAAAAAAAAMVg8i2moGGPTreICy2AfMhMjl440AH06YnoJI5HnngwB'

LOCALFILE = 'transfer.txt'
BACKUPPATH = '/file.txt' # Keep the forward slash before destination filename


# Uploads contents of LOCALFILE to Dropbox
def backup():
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


# Adding few functions to check file details
def checkFileDetails():
    print("Checking file details")

    for entry in dbx.files_list_folder('').entries:
        print("File list is : ")
        print(entry.name)


# Run this script independently
def buttonpressed():    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    global dbx
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

    try:
        checkFileDetails()
    except Error as err:
        sys.exit("Error while checking file details")

    print("Creating backup...")
    # Create a backup of the current settings file
    backup()

    print("Done!")









labelDesc = tkinter.Label(frame, text="**Enter the word for second player to guess along with a relevent hint**",fg="red")
labelDesc.pack(side = tkinter.BOTTOM)
label = tkinter.Label(frame, text = "PLAYER 1", font=("bold"))
label.pack(side = tkinter.BOTTOM)
frame.pack()
frame = tkinter.Frame(root,padx = 20, pady=20)
E1 = tkinter.Entry(frame, bd =5, width = 40)
L1 = tkinter.Label(frame, text="Enter the word : ")
L1.pack( side = tkinter.LEFT)

E1.pack(side = tkinter.RIGHT)
frame.pack()
frame = tkinter.Frame(root)
E2 = tkinter.Entry(frame, bd =5, width=40)
L2 = tkinter.Label(frame, text="Enter a hint : ")
L2.pack( side = tkinter.LEFT)

E2.pack(side = tkinter.RIGHT)
frame.pack()
#b1 = button()

#print E1.get()    

s = ""
def nex():
    global s
    s=E1.get()
    s =s.upper()
    f1=open("transfer.txt","w")
    #print s
    f1.write(s+'\n')
    s=E2.get()
    s=s.upper()
    f1.write(s)
    f1.close()
    buttonpressed()
    la = tkinter.Label(root,text = "word has been given to PLAYER 2");
    la.pack()
   
'''
def pas():
    return s
'''
frame = tkinter.Frame(root)
b=tkinter.Button(frame,text="Submit",bg="green",fg="black",command=nex)
b.pack(side="bottom",padx=10)
frame.pack()
root.mainloop()
