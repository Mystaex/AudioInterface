import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pydub import AudioSegment

root = tk.Tk()

#Types of files that can be converted
fileTypes = [
    "wav",
    "flac",
    "ogg",
    "mp3",
]

#         #
#Functions#
#         #

#Configures the grid columns and rows
def gridConfig():
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 6)
    root.columnconfigure(2, weight = 1)
    root.columnconfigure(3, weight = 2)
    for x in range(4):
        root.rowconfigure(x, weight = 1)

#Functionality for the submit button
def submit():
    if len(newFileEntry.get()) == 0 or len(fileEntry.get()) == 0:
        print('At least 1 value is left blank. Please fill them all in.')
        return
    print(filename+' Submitted!')
    print("Type: "+defDrop.get())
    
    sound = AudioSegment.from_file("/Users/ethan/Downloads/Output/"+fileEntry.get()+"."+defDrop.get())
    newFileName = "/Users/ethan/Downloads/Output/"+newFileEntry.get()+"."+defDrop.get()
    sound.export(newFileName, format = defDrop.get(), bitrate = "128k")
    print(filename+' Converted')


#Function to open file explorer. Opens in Downloads folder. Sets global filename to chosen file.
#Only allow music file types: mp3, wav, flac
#Changes entry box to fit filename
def browseFiles():
    global filename
    global path
    path = filedialog.askopenfilename(initialdir = "/Users/ethan/Downloads/",
                                          title = "Select a File",
                                          filetypes = (("Music files",
                                                        ".mp3 .wav .flac"),
                                                       ("all files",
                                                        "*.*")))

    fileKeysOne = path.rsplit("/", 1)
    fileKeysTwo = fileKeysOne[1].rsplit(".", 1)
    filename = fileKeysTwo[0]
    fileEntry.delete(0, 'end')
    fileEntry.insert(0, filename)

    if len(newFileEntry.get()) == 0:
        newFileEntry.insert(0, filename)

    fileExt = fileKeysTwo[1]
    extLabel.config(text = '.'+fileExt)

#Lays out items in the grid
def defineGUI():
    gridConfig()
    fileEntryLabel.grid(column = 0, row = 0, sticky = 'se')
    fileExtLabel.grid(column = 2, row = 0, sticky = 'se')
    convExtLabel.grid(column = 2, row = 2, sticky = 'e')
    newFileLabel.grid(column = 0, row = 2, sticky = 'e')

    fileEntry.grid(column = 1, row = 0, sticky = 'sw')
    extLabel.grid(column = 3, row = 0, sticky = 'sw')
    fileButton.grid(column = 1, row = 1, sticky = 'nw')
    extDrop.grid(column = 3, row = 2, sticky = 'w')
    newFileEntry.grid(column = 1, row = 2, sticky = 'w')
    submitButton.grid(column = 1, row = 3, sticky = '')



#          #
#   MAIN   #
#          #

#Define GUI frame attributes
root.title('Audio Converter')
root.geometry('600x300+50+50')      #widthxheight+-x+-y
root.resizable(False,False)         #widthResize, heightResize
root.attributes('-alpha', 1.0)    #0.0 is transparent, 1.0 is opaque

#Define buttons and labels
fileEntry = ttk.Entry(root, width = 30)
extLabel = ttk.Label(root, width = 6)
fileButton = ttk.Button(root, text = 'Browse Files', command = browseFiles, width = 10)
submitButton = ttk.Button(root, text = 'submit', command = submit, width = 10)
newFileEntry = ttk.Entry(root, width = 30)

convExtLabel = tk.Label(root, text = 'to:', bg = 'white')
fileExtLabel = tk.Label(root, text = 'from:', bg = 'white')
fileEntryLabel = tk.Label(root, text = 'filename:', bg = 'white')
newFileLabel = tk.Label(root, text = 'new filename:', bg = 'white')

#Define dropdown menu
defDrop = tk.StringVar()
defDrop.set("wav")
extDrop = tk.OptionMenu(root, defDrop, *fileTypes)

defineGUI()

#Needed for GUI work
#End of main program
root.mainloop()