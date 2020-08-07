from pytube import YouTube
from tkinter import *
import time

def download():
    link = url.get('1.0', 'end-1c')

    if link == '':
        pass
    else:
        yt = YouTube(link)
        stream = yt.streams.first()
        stream.download()

if __name__ == "__main__":
    root = Tk()
    root.title('YouTube Downloader')
    root.maxsize(700, 250)
    root.minsize(700, 250)

    url = Text(root, width = 60, height = 2)
    url.place(x=90, y=180)

    button = Button(root, text = 'Download', command = download)
    button.place(x=330, y=220)

    root.mainloop()