from tkinter import *
from irctop import *
from annpub import *
from calendar import monthrange
import datetime

now = datetime.datetime.now()
days = monthrange(now.year, now.month)

def settop():
    if irc.get() == 1:
        pubirc(entry1.get())
    if apps.get() == 1:
        pubapp(entry1.get(), expire)
    root.quit()

def day():
    global expire
    exp.configure(text='1 day')
    expire = 1

def week():
    global expire
    exp.configure(text='1 week')
    expire = 7

def fortnight():
    global expire
    exp.configure(text='1 fortnight')
    expire = 14

def month():
    global expire
    exp.configure(text='1 month')
    expire = days[1]

def never():
    global expire
    exp.configure(text='Never')
    expire = 'never'


root = Tk()

root.title("JB Announcer")

irc = IntVar()
apps = IntVar()

label1 = Label(root, text="Announcement:")
entry1 = Entry(root, width=80)

label1.grid(row=0, sticky=E, padx=(15, 8))

entry1.grid(row=0, column=1, padx=(0, 15))

c = Checkbutton(root, text="Set as IRC topic.", variable=irc)
c.grid(columnspan=2)

exp = Menubutton(root, text='Apps expire in... ∇', relief=RAISED, font=('', 8), pady=2, padx=2, bd=3)
exp.grid(column=1, sticky=E, row=1, padx=(0, 100), pady=(5, 0))
exp.menu = Menu(exp, tearoff=0)
exp["menu"] = exp.menu

dayVar = IntVar()
weekVar = IntVar()
monthVar = IntVar()
foreverVar = IntVar()

exp.menu.add_command(label="1 day", command=day)
exp.menu.add_command(label="1 week", command=week)
exp.menu.add_command(label="1 fortnight", command=fortnight)
exp.menu.add_command(label="1 month", command=month)
exp.menu.add_command(label="Never", command=never)


d = Checkbutton(root, text="Post to JB apps.", variable=apps)
d.grid(columnspan=2, row=2)

Post = Button(text="Go!", command=settop)
Post.grid(row=5, columnspan=2)

root.mainloop()
