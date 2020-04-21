# Initial Foothold - www-data

```
www-data@bitlab:/bin$ dpkg -l | grep sql
dpkg -l | grep sql
ii  libaprutil1-dbd-sqlite3:amd64         1.6.1-2                           amd64        Apache Portable Runtime Utility Library - SQLite3 Driver
ii  libsqlite3-0:amd64                    3.22.0-1ubuntu0.1                 amd64        SQLite 3 shared library
ii  php-pgsql                             1:7.2+60ubuntu1                   all          PostgreSQL module for PHP [default]
ii  php7.2-pgsql                          7.2.19-0ubuntu0.18.04.1           amd64        PostgreSQL module for PHP

```

```
www-data@bitlab:/bin$ uname -a
uname -a
Linux bitlab 4.15.0-29-generic #31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
```


