from pytube import YouTube
from time import time

if __name__ == "__main__":
    url = input('Url please \n')

    yt = YouTube(url)

    stream = yt.streams.first()

    stream.download('video/')