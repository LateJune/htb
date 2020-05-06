# Bashed - 10.10.10.68
## Port 80

First get to a blog page with a posting describing the authors project, Phpbash!

This is a web shell that executes commands in the browser via php to the host machine. As they stated it helps a lot with pentesting

Start off with a directory scan using gobuster and run nikto to see if there are any vulnerabilities

```
gobuster dir -u http://10.10.10.68/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.html,.txt -o gobuster-meduim.txt
```
```
nikto -host http://10.10.10.68/ -output nikto.txt
```

nikto revealed some hidden directories, but nothing truly substaintial. 

## /dev

while gobuster was busy revealing other hidden directories, its important to note that the author linked his project github page! 

reading up on it, there are two versions a phpbash.php and a phpbash.min.php which is a more compact version.

I first looked under /uploads and appended /phpbash.php but recieved a 404. Same with /phpbash.min.php

Next I looked under /php and was able to see the website directory but only a sendMail.php file was there. I could look into the code later for an exploit, but continuing enumeration

Next I saw the /dev directory and in front of me were the phpbash files

the webshell works excelently, I ran some preliminary commands to see how everything worked

## reverse shell

I grabbed the pentest monkey php reverse shell, changed the ip address to my own and used the port 1985 to listen on 

Tried to wget in the current directory /dev that I was in, but I was denied permissions

I moved to the uploads directory and was able to wget my reverse php shell

Listened on port 1985 with nc

Browsed to http://10.10.10.68/uploads/php-reverse-shell.php

And got my unprivlaged shell

## Enumeration - www-data

Start off with upgrading the shell

```
python -c 'import pty; pty.spawn("/bin/bash")'
```

```
ctrl + z 

stty raw -echo

fg 
```
1) background the rev shell

2) tell current stty to echo input characters

3) foreground the old shell

### Upload an enumeration script

## user script manager we can just become them and gain there privlages

```
sudo -u scriptmanager bash
```
sudo -l gives us an idea that we can do this as www-data 

## Road to root

In the default / directory, issing the command ls -la we notice an unfamiliar file called scripts that is owned by the scriptmanager

inside of it are two files test.py and test.txt

test.py is scriptmanager owned and test.txt is root owned so this is the way to win

there must be a crontab running in the background executing this file as root

I Placed a reverse shell inside test.py that was found on pen test monkey for python

made sure it was using the correct ip, set up a listener and waiting for my shell to arrive

user.txt: 2c281f318555dbc1b856957c7147bfc1

root.txt: cc4f0afe3a1026d402ba10329674a8e2 
