#!/bin/bash

file=$1

while IFS= read -r line; do

	echo "[+] Current Entry: $line\n"
	url="https://$line"
	echo "[+] Url to capture $url"
	command="firefox -screenshot $line.png $url --ignore"
	
	$command
	echo $command	
	printf "\n"

	


done < $file


echo "[-] Finished"
