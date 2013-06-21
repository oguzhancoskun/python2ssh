'''
Created on 21 Haz 2013

@author: onuragtas
'''
import paramiko

nbytes = 4096
hostname = '10.1.1.50'
port = 22
username = 'root'
password = 'test-935'
#command = 'ls'

client = paramiko.Transport((hostname, port))
client.connect(username=username, password=password)
 
stdout_data = []
stderr_data = []
session = client.open_channel(kind='session')
while True:
    session = client.open_channel(kind='session')
    command = raw_input("Komut:")
    session.exec_command(command)
    while True:
        if session.recv_ready():
            for element in stdout_data:
                stdout_data.remove(element);
            stdout_data.append(session.recv(nbytes))
        if session.recv_stderr_ready():
            stderr_data.append(session.recv_stderr(nbytes))
        if session.exit_status_ready():
            break

    #print 'exit status: ', session.recv_exit_status()
    print ''.join(stdout_data)
    #print ''.join(stderr_data)

session.close()
client.close()