import tkinter as tk
from pytube import YouTube

#Display window
dock = tk.Tk()
dock.geometry('500x300')
dock.resizable(0,0)
dock.title("YouTube Video Downloader by @yxzdi")
tk.Label(dock, text="YouTube Video Downloader", font="arial 20 bold").pack()

#Enter the URL
link = tk.StringVar()

tk.Label(dock, text="Paste Link Here: ", font="arial 15 bold").place(x=160, y=60)
link_error = tk.Entry(dock, width =70, textvariable = link).place(x =32, y=90)

#Function to download the video
def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    tk.Label(dock, text = "Succesfully Downloaded", font ="arial 15").place(x =180, y=200)

#Download Button
tk.Button(dock, text ="DOWNLOAD", font ="Verdana 15 bold", bg="orange", padx=2, command =Downloader).place(x=180, y=150)

dock.mainloop()
