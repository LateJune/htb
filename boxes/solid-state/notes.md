# 10.10.10.51 - solid state
## port 80
### /README.txt
- possible user: aj
	* aj@lkn.io
	* @ajlkn

## port 4555 - JAMES Remote admin
- version 2.3.2
- There is a exploit that is for apache james remote admin
- Default credentails in the exploit are as follows
	* user: root
	* pass: root

- These default creds also get us inside of the service
### Exploring commands - listusers
```
listusers
Existing accounts 5
user: james
user: thomas
user: john
user: mindy
user: mailadmin

```
## port 110 pop3 
- I changed all the default passwords in JAMES remote admin to root
- mindy's password is: P@55W0rd1!2@
```
Dear Mindy,


	 Here are your ssh credentials to access the system. Remember to reset your password after your first login. 
	 Your access is restricted at the moment, feel free to ask your supervisor to add any commands you need to your path. 

	 username: mindy
	 pass: P@55W0rd1!2@

	 Respectfully,
	 James

```

### User.txt
mindy@solidstate:~$ cat user.txt 
914d0a4ebc177889b5b89a23f556fd75

#### We are trying to break out of the retricted shell by using the code execution exploit
- Then priv esc through other means
- Looking through the directory where James was installed there is a tmp.py file
- found by execuing `ps -aux | grep james`
	* shows up in the /opt dir
- tmp.py is a root owned writable and executable by the world
- reverse shell for the win
### was running in a cron job set the reverse shell, save it and wait

# whoami
root
# cat root.txt
b4c9723a28899b1c45db281d99cc87c9


