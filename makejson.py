import os

def format(exp):
    filew = open('announcement.json', 'a')
    filew.write('       {\n')
    filew.write('           "date": "' + date + '",\n')
    filew.write('           "expires": "' + str(exp) + '",\n')
    filew.write('           "announcement": "' + announcement + '"\n')
    filew.write('       }\n')
    filew.write('   ]\n')
    filew.write('}\n')

def create(day, topic, exp):
    global date
    date = day
    global announcement
    announcement = topic
    if os.path.isfile('announcement.json'):
        text = open('announcement.json', 'r')
        lines = text.readlines()
        text.close()
        keep = ''
        for line in lines[0:-2]:
            keep = keep + line
        filew = open('announcement.json', 'w')
        filew.write(keep[0:-1] + ',\n')
        filew.close()
        format(exp)
    else:
        filew = open('announcement.json', 'w')
        filew.write('{\n')
        filew.write('   "announcement": [\n')
        filew.close()
        format(exp)