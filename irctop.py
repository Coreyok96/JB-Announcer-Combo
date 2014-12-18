import subprocess


host = '10.0.0.187'
port = '22'
username = 'irc'
target = "sftp -o IdentityFile=~/.ssh/id_rsa -P " + port + " " + username + "@" + host


def pubirc(topic):
    filew = open('announcement.txt', 'w')
    filew.write(topic)
    filew.close()

    sftp = subprocess.Popen(target, shell=False, stdin=subprocess.PIPE)
    sftp.stdin.write(bytes("cd announcement \n", "UTF-8"))
    sftp.stdin.write(bytes("put announcement.txt announcement.txt \n", "UTF-8"))
    sftp.stdin.write(bytes("exit \n", "UTF-8"))
    sftp.stdin.close()
