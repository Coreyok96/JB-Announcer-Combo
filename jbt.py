from tkinter import *
from irctop import *
from annpub import *
from calendar import monthrange
import datetime

now = datetime.datetime.now()
date = str(now.month) + "/" + str(now.day) + "/" + str(now.year)
days = monthrange(now.year, now.month)

def finddate():
    global expire
    if addays == "never":
        expire = "never"
    else:
        currentdate = datetime.date(year=int(date[6:10]), month=int(date[:2]), day=int(date[3:5]))
        enddate = currentdate + datetime.timedelta(days=addays)
        expire = str(enddate.year) + '-' + str(enddate.month) + '-' + str(enddate.day)

def settop():
    global expire
    global entryexp
    try:
        if expire == "never":
            time = ''
    except NameError:
        rawexpire = entryexp.get()
        yy = int(rawexpire[6:10])
        mm = int(rawexpire[:2])
        dd = int(rawexpire[3:5])
        expire = datetime.date(year=yy, month=mm, day=dd)
        time = rawexpire[11:]
    try:
        time
    except NameError:
        time = '0000'
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
    global addays
    exp.configure(text='1 day')
    addays = 1
    finddate()

def week():
    global addays
    exp.configure(text='1 week')
    addays = 7
    finddate()

def fortnight():
    global addays
    exp.configure(text='1 fortnight')
    addays = 14
    finddate()

def month():
    global addays
    exp.configure(text='1 month')
    addays = days[1]
    finddate()

def never():
    global addays
    exp.configure(text='Never')
    addays = 'never'
    finddate()

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
