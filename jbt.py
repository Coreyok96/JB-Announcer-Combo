from tkinter import *
from irctop import *
from annpub import *


def settop():
    if irc.get() == 1:
        pubirc(entry1.get())
    if apps.get() == 1:
        pubapp(entry1.get())
    root.quit()

root = Tk()

root.title("JB Announcer")

irc = IntVar()
apps = IntVar()

label1 = Label(root, text="Announcement:")
entry1 = Entry(root, width=80)

label1.grid(row=0, sticky=E, padx=20)

entry1.grid(row=0, column=1, padx=20)

c = Checkbutton(root, text="Set as IRC topic.", variable=irc)
c.grid(columnspan=2)

d = Checkbutton(root, text="Post to JB apps.", variable=apps)
d.grid(columnspan=2)

Post = Button(text="Go!", command=settop)
Post.grid(row=5, columnspan=2)

root.mainloop()
