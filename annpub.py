import datetime
import time
import subprocess
import rss
import makejson

now = datetime.datetime.now()
date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

host = '10.0.0.187'
port = '22'
username = 'web'
target = "sftp -o IdentityFile=~/.ssh/id_rsa -P " + port + " " + username + "@" + host

def turngmt():
    global a
    global expiretime
    if time.localtime().tm_isdst == 0:
        a = int(expiretime[:2]) + int(time.timezone / 60 / 60)

    else:
        a = int(expiretime[:2]) + int(time.altzone / 60 / 60)

def addday():
    global expire
    global gmtexp
    if expiretime == '':
        gmtexp = "never"
    else:
        turngmt()
        if a >= 24:
            expire += 1
            gmtexp = a - 24
        else:
            gmtexp = a
            if gmtexp < 10:
                gmtexp = '0' + str(gmtexp)
            else:
                gmtexp = str(gmtexp)

            gmtexp += ':' + expiretime[2:4] + ':00Z'

def pubapp(topic, exp, pri, exptime):
    global expire
    global expiretime
    expire = exp
    expiretime = exptime


    sftp = subprocess.Popen(target, shell=False, stdin=subprocess.PIPE)
    sftp.stdin.write(bytes("cd /var/www/html/api/announcement/ \n", "UTF-8"))
    sftp.stdin.write(bytes("get announcement.xml announcement.xml \n", "UTF-8"))
    sftp.stdin.write(bytes("get announcement.json announcement.json \n", "UTF-8"))
    sftp.stdin.write(bytes("exit \n", "UTF-8"))
    sftp.stdin.close()

    addday()

    priority = str(pri)
    rss.rsscreate(date, topic)
    makejson.create(date, topic, expire, priority, gmtexp)


    sftp = subprocess.Popen(target, shell=False, stdin=subprocess.PIPE)
    sftp.stdin.write(bytes("cd /var/www/html/api/announcement/ \n", "UTF-8"))
    sftp.stdin.write(bytes("put announcement.xml announcement.xml \n", "UTF-8"))
    sftp.stdin.write(bytes("put announcement.json announcement.json \n", "UTF-8"))
    sftp.stdin.write(bytes("exit \n", "UTF-8"))
    sftp.stdin.close()
