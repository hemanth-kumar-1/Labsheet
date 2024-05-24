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

## Level -23
same we should move to cron directory and open cronjob_bandit24 file.

when we open executable file(.sh extension) inside cronjob_bandit24, we will see that we want to write our script.

first we should create a directory in tmp directory and then we should create a file in it, give permissions to all members for the created file.

now move to the directory shown in the executable file.

Then create a file and use nano editor to write the code in it.

code = etc/bandit_pass/bandit24 > tmp/"created directory"/"created file"  --> this code will redirected the password to the file.

We can check our password in that file after few seconds.

password = `VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar`

## Level -24
for this level we should write our own shell script code to submit all the possible numbers with the previous password.

the code(we will write this code in tmp directory):

`#!/bin/bash

count=0000

passwd="VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar"

while [ "$count" -le 10000 ]
do
    echo "$passwd $count"
    count=$((count + 1))
done | nc localhost 30002 > test  #it is the file where the password goes`

then - cat test | grep password.

password = 'p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d'

## Level -25 & 26

In this level we will find a sshkey of next level.

we see that the bash file of next level is not a regular bash and something else(given in the website).

so to see the bash file of the level we prompt `cat /etc/passwd | grep bandit26`.

we will see a diff bash that is bin/passwd/showtext.

when we open the file showtext will see a executable file. 

in that file we see a command more. we should know about more command for solving next level.

when we login to the bandit26 using the key we got, we will be logged out automatically.

here where more works, we will now shrink the size of terminal, then try to login.

Here more command waits for our input, so type 'v' to enter the edit mode.

Now in the editor we can type :set shell=/bin/bash and hit enter after that type :!cat /etc/bandit_pass/bandit26 to get bandit26 password. 

if we type `:!ls` to see files here we will notice a executable file 'bandit27-do'.

now if we write `:!./bandit27-do cat /etc/bandit_pass/bandit27`, we will get the password for bandit27 the next level.

password of bandit25 = `c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1`

password of badnit26 = `YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS`

## Level -27
we should copy a file from a github repositry.

we should create a tmp directory for our work space because we can't make editing in home directory.

After creating the directory we can clone the directory using git clone command.

`git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo`

Here we specify the port number using ':'.

It will store the copied file in repo directory and we can read the password from it.

password = `AVanL161y9rsbcJIsFHuw35rjaOM19nR`.

## Level -28
Same as above we clone the git repository .

`ssh://bandit28-git@localhost:2220/home/bandit28-git/repo`

When we move to repo directory we can see a file named `README.md`.

When we open it we see the password is like `xxxxxxx`.

some body had changed the repo so to see what are the changes made and when are they we can use `git log` command.

we can use `git show "provide the hash code"`

password = `tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S`

## Level -29
Same after connecting we clone the git repository using `git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo`

After that in repo directory we see README.md file in it we see the password will be like "<no passwords in production".

when we run git log for changes we will see only the username is changed.

Then i checked the branches with git branch -av.

we will see a list, when we check remotes/origin/dev using `git checkout remotes/origin/dev`.

we will see the password is updated in readme file.

password = `xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS`

## Level -30
Same after cloning the github repo, and when we see the information its just some ascii text.

when we check for the tags it had, we will find the tag secret.

when we check for it by git show secret. The password will display.

password = `OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt`
