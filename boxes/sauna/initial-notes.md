# sauna - 10.10.10.175
## Initial notes, SMB Needs to be authenticated before we can do anything
- List of possible users found on the about page and listed under possible users

## LDAP - we can unauthenticated search to find data about the domain EGOTISTICAL-BANK.LOCAL
```
ldapsearch -h EGOTISTICAL-BANK.LOCAL -p 389 -x -b "dc=EGOTISTICAL-BANK,dc=local"
```
- Gives a lot of information, but the most crucial thing is that it gives us a user
```

# Hugo Smith, EGOTISTICAL-BANK.LOCAL
dn: CN=Hugo Smith,DC=EGOTISTICAL-BANK,DC=LOCAL

```

### To get his specific record
```
ldapsearch -h EGOTISTICAL-BANK.LOCAL -p 3268 -x -b cn='Hugo Smith',dc=EGOTISTICAL-BANK,dc=local

```
