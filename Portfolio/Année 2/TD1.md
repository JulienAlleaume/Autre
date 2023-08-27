Exercice 1 :

a) echo "pouet" > text.txt | at 09:56 AM
b) echo "pouet" > text.txt | at 09:56 PM
c) echo "pouet" > test.txt | at 05:27 AM 2048-01-21
d) echo "pouet" > test.txt | at now + 20 minutes
e) echo "pouet" > test.txt | at now + 3 days
f) echo "pouet" > test.txt | at now + 3 days 
g) echo "pouet" > test.txt | at -m now + 3 days

2: at -l 

3: at -r *nom*

4: Stocker dans /var/spool/cron/atjob/

5: Dans JOBS les task sont stocker :  

GNOME_TERMINAL_SERVICE=:1.126; export GNOME_TERMINAL_SERVICE                   │
│SHLVL=1; export SHLVL                                                         │
│QT_IM_MODULE=ibus; export QT_IM_MODULE                                        │
│PT8HOME=/opt/pt; export PT8HOME                                               │
│XDG_RUNTIME_DIR=/run/user/1000; export XDG_RUNTIME_DIR                        │
│XDG_DATA_DIRS=/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/d│
│esktop; export XDG_DATA_DIRS                                                  │
│PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/│
│usr/local/games:/snap/bin:/snap/bin; export PATH                              │
│GDMSESSION=ubuntu; export GDMSESSION                                          │
│ZELLIJ=0; export ZELLIJ                                                       │
│DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus; export DBUS_SESSION_BUS│
│_ADDRESS                                                                      │
│cd /home/julien || {                                                          │
│         echo 'Execution directory inaccessible' >&2                          │
│         exit 1                                                               │
│}                                                

CRON SYSTEM:

a) /etc/crontab
b) Il doivent être placé dans /etc/cron.daily ; .weekly ; . monthly
c) Julien utilisateur connecter executant la commande
d) Par rapport au dossier c'est minuit si non préciser.
e) run-parts permet d'executer tout les script dans un dossier.

CRON USER :

a) "Editor"
b) "export EDITOR=vim"
c) "var/spool/cron/crontabs"
e) "5  3    * * *  ..."
f) "3  * * * *..."
g) "8-17  *  *  *  *..."
h) "15 13 * 1-7 1 ..."



