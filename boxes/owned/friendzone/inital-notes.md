# Friendzone - domain friendzone.red - 10.10.10.123
## AT http://10.10.10.123/
- info@friendzoneportal.red


## At https://friendzone.red/js/js - Text is displayed
```
Testing some functions !

I'am trying not to break things !
QVdGNGdEOHVPYzE1ODExNzE3MTlVOWp3amNrZjN6
```
- Looks like b64, decoded is below. Possible password
```
AWF4gD8uOc1581171719U9jwjckf3z
```

## smbmap -H 10.10.10.123 output
```
jonathan@kali:~/htb/boxes/friendzone$ smbmap -H 10.10.10.123
[+] Finding open SMB ports....
[+] Guest SMB session established on 10.10.10.123...
[+] IP: 10.10.10.123:445        Name: friendzone.red                                    
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        Files                                                   NO ACCESS       FriendZone Samba Server Files /etc/Files
        .                                                  
        dr--r--r--                0 Wed Jan 16 15:10:51 2019    .
        dr--r--r--                0 Wed Jan 23 16:51:02 2019    ..
        fr--r--r--               57 Tue Oct  9 19:52:42 2018    creds.txt
        general                                                 READ ONLY       FriendZone Samba Server Files
        Development                                             READ, WRITE     FriendZone Samba Server Files
        IPC$                                                    NO ACCESS       IPC Service (FriendZone server (Samba, Ubuntu))
jonathan@kali:~/htb/boxes/friendzone$ 

```
### connect on smbclient and download creds.txt
```
smbclient //10.10.10.123/general
Enter WORKGROUP\jonathan's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Jan 16 15:10:51 2019
  ..                                  D        0  Wed Jan 23 16:51:02 2019
  creds.txt                           N       57  Tue Oct  9 19:52:42 2018

                9221460 blocks of size 1024. 6459144 blocks available
smb: \> get creds.txt
getting file \creds.txt of size 57 as creds.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> exit

```

## Preformed a zone transfer and recieved a list of urls found in the hosts directory
### many rabbit holes but administrator1.friendzone.red gives a real login
- Username: admin
- Password: WORKWORKHhallelujah@#

## After loggin in tells us to go to dashboard.php 
### Webpage is running php time php script from the upload.php page
- replacing the php script in the query string runs other scrips found in the page
- uploading payloads may also work??
	* php reverse shell after we download the php script and see how its runs 
	* lfi
