#!/bin/sh
printf "\n====Running Scraper====\n"
./"Tor Browser"/Browser/firefox.exe & 
python scraper.py $1 $2 #$1 and $2 are the first two arguments passed to the bash script
kill 0