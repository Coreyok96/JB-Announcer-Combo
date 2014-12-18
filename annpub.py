import os
import subprocess
import datetime


now = datetime.datetime.now()
date = str(now.day) + "/" + str(now.month) + "/" + str(now.year)

host = '10.0.0.187'
port = '22'
username = 'web'
target = "sftp -o IdentityFile=~/.ssh/id_rsa -P " + port + " " + username + "@" + host

def layout():
        filew = open('announcement.xml', 'w')
        filew.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        filew.write('<rss version="2.0">\n')
        filew.write('<channel>\n')
        filew.write('   <title>Jupiter Broadcasting Announcements</title>\n')
        filew.write('   <description>RSS feed for Jupiter Broadcasting announcements</description>\n')
        filew.write('   <link>http://www.jupiterbroadcasting.com</link>\n')
        filew.close()

def newitem():
        filew = open('announcement.xml', 'a')
        filew.write('   <item>\n')
        filew.write('       <title>Announcement: ' + date + '</title>\n')
        filew.write('       <description>' + announcement + '</description>\n')
        filew.write('   </item>\n')
        filew.close()

def pubapp(topic):
    global announcement
    announcement = topic
    sftp = subprocess.Popen(target, shell=False, stdin=subprocess.PIPE)
    sftp.stdin.write(bytes("cd /var/www/html/api/announcement/ \n", "UTF-8"))
    sftp.stdin.write(bytes("get announcement.xml announcement.xml \n", "UTF-8"))
    sftp.stdin.write(bytes("exit \n", "UTF-8"))
    sftp.stdin.close()

    if os.path.isfile('announcement.xml'):
        text = open('announcement.xml', 'r')
        lines = text.readlines()
        keep = ''
        for line in lines:
            if line == '<?xml version="1.0" encoding="UTF-8"?>\n' or line == '<rss version="2.0">\n' or line == '<channel>\n' or line == '   <title>Jupiter Broadcasting Announcements</title>\n' or line == '   <description>RSS feed for Jupiter Broadcasting announcements</description>\n' or line == '   <link>http://www.jupiterbroadcasting.com</link>\n':
                pass
            else:
                keep = keep + line
        layout()
        newitem()
        filew = open('announcement.xml', 'a')
        filew.write(keep)
        filew.close()

    else:
        layout()
        newitem()
        filew = open('announcement.xml', 'a')
        filew.write('</channel>\n')
        filew.write('</rss>')
        filew.close()

    sftp = subprocess.Popen(target, shell=False, stdin=subprocess.PIPE)
    sftp.stdin.write(bytes("cd /var/www/html/api/announcement/ \n", "UTF-8"))
    sftp.stdin.write(bytes("put announcement.xml announcement.xml \n", "UTF-8"))
    sftp.stdin.write(bytes("exit \n", "UTF-8"))
    sftp.stdin.close()