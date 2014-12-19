import os


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


def rsscreate(day, topic):
    global date
    date = day
    global announcement
    announcement = topic
    if os.path.isfile('announcement.xml'):
        text = open('announcement.xml', 'r')
        lines = text.readlines()
        text.close()
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
