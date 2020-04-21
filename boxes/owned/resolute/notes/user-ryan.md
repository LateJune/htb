# *Evil-WinRM* PS C:\> net user ryan
User name                    ryan
Full Name                    Ryan Bertrand
Comment                      
User's comment               
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            1/28/2020 4:14:02 PM
Password expires             Never
Password changeable          1/29/2020 4:14:02 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      
Global Group memberships     *Domain Users         *Contractors          
The command completed successfully

# *Evil-WinRM* PS C:\> net localgroup DnsAdmins
Alias name     DnsAdmins
Comment        DNS Administrators Group

Members

-------------------------------------------------------------------------------
Contractors
The command completed successfully.

# *Evil-WinRM* PS C:\> net group contractors
Group name     Contractors
Comment        Contractors

Members

-------------------------------------------------------------------------------
ryan                     
The command completed successfully.

