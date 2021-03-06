#!/usr/bin/env python
# Python Network Programming Cookbook, Second Edition -- Chapter - 5
# This program is optimized for Python 2.7.12 and Python 3.5.2.
# It may run on any other version with/without modifications.
#this code show us how many email that we have in our inbox
#this code need google account app password to log in to our email account

import argparse
import getpass
import poplib

GOOGLE_POP3_SERVER = 'pop.googlemail.com'

def download_email(username): 
    mailbox = poplib.POP3_SSL(GOOGLE_POP3_SERVER, '995') 
    mailbox.user(username)
    password = getpass.getpass(prompt='Enter your Google password: ') 
    mailbox.pass_(password) 
    num_messages = len(mailbox.list()[1])
    print ('Total emails: {}'.format(num_messages))
    mailbox.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Email Download Example')
    parser.add_argument('--username', action="store", dest="username", default=getpass.getuser())
    given_args = parser.parse_args() 
    username = given_args.username
    download_email(username)

