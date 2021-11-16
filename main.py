import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pydub import AudioSegment
import sys
sys.path.append('path/to/ffmpeg')

root = tk.Tk()

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 6)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 2)

fileTypes = [
    "wav",
    "flac",
    "ogg",
    "mp3",
]

for x in range(4):
    root.rowconfigure(x, weight = 1)

def submit():
    print(filename+' Submitted!')
    print("Type: "+defDrop.get())
    
    sound = AudioSegment.from_file(path)
    fileKeys = filename.rsplit(".", 1)
    fileNoExt = fileKeys[0]
    newFileName = "/Users/ethan/Downloads/Output/"+fileNoExt+"."+defDrop.get()
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

    fileKeys = path.rsplit("/", 1)
    filename = fileKeys[1]
    fileEntry.delete(0, 'end')
    fileEntry.insert(0, filename)

    fileKeys = path.rsplit(".", 1)
    fileExt = fileKeys[1]
    extLabel.config(text = '.'+fileExt)


root.title('Audio Converter')
root.geometry('600x300+50+50')      #widthxheight+-x+-y
root.resizable(False,False)         #widthResize, heightResize
root.attributes('-alpha', 1.0)    #0.0 is transparent, 1.0 is opaque

fileEntry = ttk.Entry(root, width = 30)

extLabel = ttk.Label(root, width = 6)

defDrop = tk.StringVar()
defDrop.set("wav")
extDrop = tk.OptionMenu(root, defDrop, *fileTypes)

convEntry = ttk.Entry(root, width = 6)

fileButton = ttk.Button(root, text = 'Browse Files', command = browseFiles, width = 10)

submitButton = ttk.Button(root, text = 'submit', command = submit, width = 10)

fileEntryLabel = tk.Label(root, text = 'filename:', bg = 'white')
fileEntryLabel.grid(column = 0, row = 0, sticky = 'e')
fileExtLabel = tk.Label(root, text = 'from:', bg = 'white')
fileExtLabel.grid(column = 2, row = 0, sticky = 'e')
convExtLabel = tk.Label(root, text = 'to:', bg = 'white')
convExtLabel.grid(column = 2, row = 2, sticky = 'ne')

fileEntry.grid(column = 1, row = 0, sticky = 'w')
extLabel.grid(column = 3, row = 0, sticky = 'w')
fileButton.grid(column = 1, row = 1, sticky = 'nw')
extDrop.grid(column = 3, row = 2, sticky = 'nw')
submitButton.grid(column = 1, row = 2, sticky = '')


root.mainloop()