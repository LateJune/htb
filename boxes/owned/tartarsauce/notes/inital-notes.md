# 10.10.10.88 - tartarsauce
## nmap reveals port 80 as open port - robots.txt reveals hidden pages
### http://10.10.10.88/webservices/monstra-3.0.4/

- login page found on that same website linked below
### Username and password so simple
- admin:admin 

### Poking around
- possible user: Awilum
	- Monstra 

### Monstra 3.0.4
- Search sploit reveals there is a authenticated RCE
### Unable to upload a file - Rabbit hole

## http://10.10.10.88/webservices/wp/
### Wordpress directory
- used burp to change reponse headers
	- page was being redirected and giving a fake 404
	- Redirected to http:/10...
	- we need http://10...
- Burp proxy to change reponse headers and body in the options
	- Match on http:/10 --> http://10

## There is a vulnerable plugin as found on wpscan --> need to update and get it to work...
### Gwolle plugin has an rfi that can be found in my www directory
- Able to have the webserver touch our net cat and it is appending wp-load.php to the file I am requesting

