from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk

import tkinter.messagebox as mb
import tkinter as tk
import datetime
import time
import random

app = Tk()
app.title("Windows 10 Update Center")
app.geometry("500x550")
app.resizable(False, False)
app.iconbitmap("icon.ico")

iconwindows10 = PhotoImage(master=app, file="icon-png.png")
output_iconwindows10 = Label(app, image=iconwindows10, bg="#FFFFFF")
output_iconwindows10.image = iconwindows10
output_iconwindows10.place(relx=0.05, rely=0.05)

Label(app, text="Windows 10", font=("Segoe UI", 25), fg="#01A6F0", bg="#FFFFFF").place(relx=0.16, rely=0.05)
Label(app, text="Update Center", font=("Segoe UI", 13), fg="#01A6F0", bg="#FFFFFF").place(relx=0.26, rely=0.13)

Label(app, text="Description:", font=("Segoe UI", 10, "bold"), bg="#FFFFFF").place(relx=0.04, rely=0.20)

description = ScrolledText(app, wrap=WORD, undo=True, width=62, height=15, font=("Segoe UI", 10))
description.pack(expand=True)
description.place(relx=0.05, rely=0.25)

current_month = datetime.date.today().month
current_year = datetime.date.today().year

description.configure(state='normal')
description.insert('end', f'Critical {current_month}/{current_year} -- KB5390699\n\n• Highlights\nUpdate to improve your PC security against malwares, ransomwares and PUP.\n\n• Improvements and fixes\nThe security update includes quality improvements.\n\n  - Security updates to Microsoft Edge and Internet Explorer.\n  - Small bug fixes.\n\nIf you installed earlier updates, only the new fixes contained in this package will be downloaded and installed on your device.')
description.configure(state='disabled')

# def update_progress_label():
#     # return f"{pb['value']}%"

def progress():
    randnum = random.randint(1, 5)
    start_button.place(relx=1, rely=1)
    value_label.place(relx=0.40, rely=0.85)
    if pb['value'] < 100:
        pb['value'] += randnum
        # value_label['text'] = update_progress_label()
        randtime = random.randint(1000, 3000)
        pb.after(800, progress)
    else:
        value_label.place(relx=1, rely=1)
        start_button.place(relx=0.40, rely=0.85)
        mb.showerror(message='Windows 10 can\'t finish the update, please don\'t shutdown or restart your computer and retry later.', title="Windows 10 Update Center")
        pb['value'] = 0


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()


# progressbar
pb = ttk.Progressbar(
    app,
    orient='horizontal',
    mode='determinate',
    length=280,
    maximum=100
)
# place the progressbar
pb.place(relx=0.20, rely=0.80)

# label
value_label = Label(app, text="Downloading...", font=("Segoe UI", 10), bg="#FFFFFF")
value_label.place(relx=1, rely=1)

# start button
start_button = Button(
    app,
    text='Download',
    command=progress,
    font=("Segoe UI", 10),
    bg="#FFFFFF"
)
start_button.place(relx=0.40, rely=0.85)

app.config(bg="#FFFFFF")
app.mainloop()
