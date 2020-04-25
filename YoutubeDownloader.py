from pytube import YouTube
import os
from tkinter import filedialog
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()
label1 = tk.Label(root, text='Youtube Downloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)
label2 = tk.Label(root, text='URL:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)
entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def downloadYouTube():
    videourl = entry1.get()
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    download_root = tk.Tk()
    download_root.withdraw()
    download_root.filename = filedialog.askdirectory(title = "Selecione a pasta para salvar os videos")
    path = download_root.filename
    yt.download(path)
button1 = tk.Button(text='DOWNLOAD!', command=downloadYouTube, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
root.mainloop()