from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

#functions
def selectpath():
    #allows user to select download path in computer
    path = filedialog.askdirectory()
    pathlabel.config(text=path)
def downloadfile():
#get user path
    getlink = linkfield.get()
#get selected path
    userpath = pathlabel.cget("text")
    screen.title("Downloading...")
#download video
    mp4video = YouTube(getlink).streams.get_highest_resolution().download()
    vidclip = VideoFileClip(mp4video)
    vidclip.close()
#move to selected location
    shutil.move(mp4video, userpath)
    screen.title("Download Completed ")

    



screen = Tk()
title = screen.title("Youtube video Downloader")
canvas = Canvas(screen, width= 600,height=500)
canvas.pack()

#ImageLogo
logoimg = PhotoImage(file="C://Users/Asus/Desktop/Python practice/Youtube Video Downloader/Youtubelogo.png")
canvas.create_image(300,120,image= logoimg)

#LinkField
linkfield = Entry(screen, width= 50)
linklabel = Label(screen, text = "Enter  Download link :",font={"Courier",15})

#Select file saving path 
pathlabel = Label(screen,text="Select path for download",font={"Courier",15})
selectbtn = Button(screen, text="Select",font={"Courier",15}, command=selectpath)
#Add to window
canvas.create_window(300,350,window=pathlabel)
canvas.create_window(300,400,window=selectbtn)

#Add widgets window
canvas.create_window(300, 250, window=linklabel)
canvas.create_window(300, 300, window=linkfield)

#Download buttons
downloadbtn = Button(screen,text="Download File",font={"Courier",15},command=downloadfile)
#add to canvas
canvas.create_window(300,450,window=downloadbtn)



screen.mainloop()



