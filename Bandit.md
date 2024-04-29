# Level 15
Connect to the ssl server by using openssl cmd

openssl s_client -connect localhost:30001 is the prompt

After connecting submit the previous key.

password = `JQttfApK4SeyHwDlI9SXGR50qclOAil1`

## LEVEL -16
Here we have range of port numbers. To check for which of them the server is listining.

cmd = netstat -tuln | grep ':' | awk -F ' ' '{print $4}' | awk -F ':' '{print $NF}' | awk '$1 >= 31000 && $1 <= 32000' | sort -n |uniq

in output we will see two port numbers are will speack to the ssl.

when we enter the correct one.

in output we will get a key.
