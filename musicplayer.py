import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *

root=Tk()
root.minsize(300,300)
root["bg"]='#20bdb5'

listofsongs=[]
realnames=[]

v=StringVar()
songlabel=Label(root,textvariable=v,width=50)

index=0

def nextsong(event):
    global index
    index +=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def  prevsong(event):
    global index
    index -=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopmusic(event):
    pygame.mixer.music.stop()
    v.set('')

def pausemusic(event):
    if pausebutton["text"] == "Pause":
        pausebutton["text"] = "Resume"
        #pausebutton["bg"] = "red"
        pygame.mixer.music.pause()
    else:
        pausebutton["text"] = "Pause"
        #pausebutton["bg"] = "green"
        pygame.mixer.music.unpause()


def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname


def directorychooser():
    directory=askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir=os.path.realpath(files)
            audio=ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

directorychooser()

label=Label(root,text='Music player',font=('Arial', 20))
label['bg']='#20bdb5'
label.pack()

listbox=Listbox(root, width=50, height=20)
listbox.pack()

realnames.reverse()

for item in realnames:
    listbox.insert(0,item)

realnames.reverse()

songlabel.pack()

previousbutton=Button(root,text='<')
previousbutton.pack(side=LEFT,padx=25, pady=10)

pausebutton=Button(root,text='Pause')
pausebutton.pack(side=LEFT,padx=25, pady=5)




stopbutton=Button(root,text='Stop Music')
stopbutton.pack(side=LEFT,padx=25, pady=5)

nextbutton=Button(root,text='>')
nextbutton.pack(side=LEFT,padx=25, pady=10)


nextbutton.bind('<Button-1>',nextsong)
previousbutton.bind('<Button-1>',prevsong)
stopbutton.bind('<Button-1>',stopmusic)
pausebutton.bind('<Button-1>',pausemusic)




root.mainloop()