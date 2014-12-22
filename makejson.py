import os


def format(date, exp, pri, announcement):
    filew = open('announcement.json', 'a')
    filew.write('       {\n')
    filew.write('           "date": "' + date + '",\n')
    filew.write('           "expires": "' + exp + '",\n')
    filew.write('           "priority": "' + pri + '",\n')
    filew.write('           "announcement": "' + announcement + '"\n')
    filew.write('       }\n')
    filew.write('   ]\n')
    filew.write('}\n')

def create(day, topic, exp, pri, exptime):
    expiry = str(exp) + ' ' + exptime

    if os.path.isfile('announcement.json'):
        text = open('announcement.json', 'r')
        lines = text.readlines()
        text.close()
        keep = ''
        for line in lines[0:-2]:
            keep += line
        filew = open('announcement.json', 'w')
        filew.write(keep[0:-1] + ',\n')
        filew.close()
        format(day, expiry, pri, topic)
    else:
        filew = open('announcement.json', 'w')
        filew.write('{\n')
        filew.write('   "announcement": [\n')
        filew.close()
        format(day, expiry, pri, topic)