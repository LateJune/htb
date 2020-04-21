# Port 80
Having a tough time brute forcing the web directory - maybe dropping packets or cause im FREE not VIP

## Found main website directory being hosted under http://10.10.10.171/music/
### another noteworthy page http://10.10.10.171/music/contact.html

### Cicked around and found http://10.10.0.171/ona/
- OpenNetAdmin Version v18.1.1 --> out of date 
	* 18.1.1 - Command Injection Exploit (Metasploit)
- Was unable to find the metasploit module so just used the .sh file
	* needed to change the file format to unix using the vi command `:set fileformat=unix`
		- Getting strange error --> opennetadmin-exploit.sh: Bourne-Again shell script, ASCII text executable, with CRLF line terminators

## Script for the shell
### ./opennetadmin-exploit.sh http://10.10.10.171/ona/
```
http://10.10.10.171/ona/winc/
http://10.10.10.171/ona/modules/
https://github.com/opennetadmin/ona/wiki/plugins
```
