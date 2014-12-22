from tkinter import *
from irctop import *
from annpub import *
from calendar import monthrange
import datetime

now = datetime.datetime.now()
days = monthrange(now.year, now.month)

def finddays():
    global expire
    today = datetime.date(now.year, now.month, now.day)
    expdate = datetime.date(yyyy, mm, dd)
    delta = expdate - today
    expire = delta.days

def settop():
    global expire
    global entryexp
    try:
        expire
    except NameError:
        global yyyy
        global mm
        global dd
        expire = entryexp.get()
        yyyy = int(expire[6:10])
        mm = int(expire[0:2])
        dd = int(expire[3:5])
        time = expire[11:15]
        finddays()
    try:
        time
    except NameError:
        time = 0000
    try:
        priority
    except NameError:
        priority = 50
    if irc.get() == 1:
        pubirc(entry1.get())
    if apps.get() == 1:
        pubapp(entry1.get(), expire, priority, time)
    root.quit()

def pricommand():
    pri.menu.add_command(label="100", command=hundred)
    pri.menu.add_command(label="75", command=seventy5)
    pri.menu.add_command(label="50", command=fifty)
    pri.menu.add_command(label="25", command=twenty5)
    pri.menu.add_command(label="0", command=zero)

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

def options():
    global entryexp
    global pri
    global priority
    exp.destroy()
    pri.destroy()
    labelexp = Label(root, text="Enter date and time.")
    labelexp.grid(column=1, row=1, sticky=E, padx=(0, 52))
    entryexp = Entry(root)
    entryexp.grid(column=1, row=2, sticky=E, padx=(0, 40))

    try:
        priority
    except NameError:
        priority = 'Priority... ∇'

    pri = Menubutton(root, text=priority, relief=RAISED, font=('', 8), pady=2, padx=2, bd=3)
    pri.grid(column=1, sticky=E, row=3, padx=(0, 100), pady=(5, 5))
    pri.menu = Menu(pri, tearoff=0)
    pri["menu"] = pri.menu

    pricommand()

def hundred():
    global priority
    pri.configure(text='100')
    priority = 100

def seventy5():
    global priority
    pri.configure(text='75')
    priority = 75

def fifty():
    global priority
    pri.configure(text='50')
    priority = 50

def twenty5():
    global priority
    pri.configure(text='25')
    priority = 25

def zero():
    global priority
    pri.configure(text='0')
    priority = 0


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

exp.menu.add_command(label="1 day", command=day)
exp.menu.add_command(label="1 week", command=week)
exp.menu.add_command(label="1 fortnight", command=fortnight)
exp.menu.add_command(label="1 month", command=month)
exp.menu.add_command(label="Never", command=never)
exp.menu.add_separator()
exp.menu.add_command(label="More options...", command=options)

pri = Menubutton(root, text='Priority... ∇', relief=RAISED, font=('', 8), pady=2, padx=2, bd=3)
pri.grid(column=1, sticky=E, row=2, padx=(0, 100), pady=(5, 5))
pri.menu = Menu(pri, tearoff=0)
pri["menu"] = pri.menu

pricommand()

d = Checkbutton(root, text="Post to JB apps.", variable=apps)
d.grid(columnspan=2, row=2)

Post = Button(text="Go!", command=settop)
Post.grid(row=3, columnspan=2)

root.mainloop()
