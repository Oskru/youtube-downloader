import os
from tkinter import messagebox
from pytube import YouTube
from email.mime import audio
from moviepy.editor import *   # TODO: Implement conversion from mp4 downloaded file


def download_mp3(url, path):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()

        dir_path = os.path.dirname(path)
        video.download(output_path=dir_path, filename=os.path.basename(path))

        messagebox.showinfo(
            title='Information',
            message=f'{os.path.basename(path)} has been downloaded succesfully!'
            )

    except Exception as e:
        messagebox.showerror(title='Error', message=f'An unexpected error has occured.\r\nDetails: {e}')