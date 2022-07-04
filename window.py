"""
Window app
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from downloader import download_mp3


def main():
    '''
    Docstring about main()
    '''

    window = tk.Tk()
    xpad = 10

    url_var = tk.StringVar()
    which_ext = tk.IntVar()

    extensions = (
        ('MP3 files', '.mp3'),
        ('MP4 files', '.mp4'),
        ('WAV files', '.wav'),
    )

    def get_path():
        global PATH

        ext = extensions[int(which_ext.get())]
        PATH = filedialog.asksaveasfilename(filetypes=[ext])

        if PATH is not None:
            messagebox.showinfo(title='Information', message='Path chosen succesfully')
            but_download.config(state=tk.ACTIVE)

        if not PATH.endswith(ext[1]):
            PATH += ext[1]


    # Widgets here
    lab_url = tk.Label(window, text='Enter video url')
    ent_url = tk.Entry(window, textvariable=url_var, width=50)


    lab_ext = tk.Label(window, text='Choose export extension:')

    rad_mp3 = tk.Radiobutton(window, text='.mp3', value=0, variable=which_ext)
    rad_mp4 = tk.Radiobutton(window, text='.mp4', value=1, variable=which_ext)
    rad_wav = tk.Radiobutton(window, text='.wav', value=2, variable=which_ext)


    but_path = tk.Button(window, text='Choose path to save file...', command=get_path)

    but_download = tk.Button(
        window, text='Download file',
        state=tk.DISABLED,
        command=lambda: download_mp3(url_var.get(), PATH)
        )


    # Allocate widgets

    # Url input label and entry
    lab_url.place(x=10, y=20)
    ent_url.place(x=110, y=20)

    # Choose ext text
    lab_ext.place(x=xpad, y=50)

    # Extensions radio buttons
    rad_mp3.place(x=xpad, y=80)
    rad_mp4.place(x=xpad, y=110)
    rad_wav.place(x=xpad, y=140)

    # File dialog
    but_path.place(x=xpad, y=180)

    # Download button
    but_download.place(x=xpad, y=220)



    # Window configs
    window.iconbitmap('static/youtube.ico')
    window.title('Youtube video / music downloader')
    window.geometry('420x300+10+20')
    window.minsize(420, 300)
    window.maxsize(420, 300)

    window.mainloop()

if __name__ == '__main__':
    main()
