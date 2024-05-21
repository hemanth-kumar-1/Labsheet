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

## LEVEL -17
we should connect with the key we got in the previous level.

after connecting we see two files in it.

we use diff command to note the diff between the files.

cmd = diff passwords.new passwords.old

password = `hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg`

## LEVEL -18
we will automatically lodded out, when we connect to the server 

so no chance to stay in it 

so we will combine the cat command when we use ssh command itself.

password = `awhqfNnAbc1naukrpqDYcF95h7HoMTrC`

## Level -19
After connecting to the server we will see a 32 bit executable file.

we will see that it is a level20 user file, and it is setuid file, so we can acess the files as level20 user.

cmd = `./bandit20-do  cat /etc/bandit_pass/bandit20`

password = `VxCazJaVykI6W36BkBU0mJTCM8rR95XT`

## Level -20
connect to the server with two different terminals.

on one terminal connect using nc command with ur desired port number(nc -nlvp 8888)

on the other terminal run the excutable file using the same port number(./suconnect 8888)

on the first terminal send the password of the previous level.

if it was correct the password for the next level will be displayed.

password = `NvEJF7oVjkddltPSrdKEFOllh9V1IBcq`

## Level -21
After connecting to the server we should move to the directory specified in the question

we will there see list of files being there when u open a file named cronjob_bandit22

we will see a executable file of cronjob_bandit22.sh and its path

open the file using the path and then we should open another file which is stored in tmp directory.

password = `WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff`

## Level -22
Same as above until u open cronjob_bandit23 file.

Then we see that we need to create md5sum of the text "I am user username", here username is bandit23.

then we should use that md5sum value to open the file in the tmp directory.

password = `QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G`
