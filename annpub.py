import datetime
import subprocess
import rss
import makejson

now = datetime.datetime.now()
date = str(now.day) + "/" + str(now.month) + "/" + str(now.year)

host = '10.0.0.187'
port = '22'
username = 'web'
target = "sftp -o IdentityFile=~/.ssh/id_rsa -P " + port + " " + username + "@" + host



def pubapp(topic):
    sftp = subprocess.Popen(target, shell=False, stdin=subprocess.PIPE)
    sftp.stdin.write(bytes("cd /var/www/html/api/announcement/ \n", "UTF-8"))
    sftp.stdin.write(bytes("get announcement.xml announcement.xml \n", "UTF-8"))
    sftp.stdin.write(bytes("get announcement.json announcement.json \n", "UTF-8"))
    sftp.stdin.write(bytes("exit \n", "UTF-8"))
    sftp.stdin.close()

    rss.rsscreate(date, topic)
    makejson.create(date, topic)


    sftp = subprocess.Popen(target, shell=False, stdin=subprocess.PIPE)
    sftp.stdin.write(bytes("cd /var/www/html/api/announcement/ \n", "UTF-8"))
    sftp.stdin.write(bytes("put announcement.xml announcement.xml \n", "UTF-8"))
    sftp.stdin.write(bytes("put announcement.json announcement.json \n", "UTF-8"))
    sftp.stdin.write(bytes("exit \n", "UTF-8"))
    sftp.stdin.close()