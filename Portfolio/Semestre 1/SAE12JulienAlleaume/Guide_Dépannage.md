# Guide Dépannage

Voici un guide pour dépanner votre ordinateur s’il n'a pas accès à internet. Tout au long de ce dépannage il y aura des exemples des commandes utilisé et souvent une image pour montrer précisément l'endroit à prêter attention. Le guide commencera par des actions qui suive le modèle tcp/ip. D'abords les couches matérielles avec les câbles, la carte réseaux, adresses IP, ect... Puis enfin les couches hautes, comme les points d'accès aux services réseaux, ect... Le dépannage comprend les OS <ins> Linux et Windows</ins>. 

## Linux:   

Il se peut que certaine commande ne fonctionne pas sur Linux car il faut peut-être les installer. Si cela arrive il suffit d'écrire dans un terminal root (Pour accéder au mode root exécuter la commande <ins>"su root"</ins> puis le mot de passe), apt-get install "nom de l'application". Par exemple : "<ins> apt-get install man-db manpages-posix </ins>". Cette commande installe le package 'man' qui permet d'avoir de l'aide sur les commandes. Exemple :" man ip "   (Voir les images ci-dessous)

![LinuxMan1](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/22d4b5c3861a24e3bd82d220d1a725fb9d3fca0c/Image/LinuxMan1.PNG)    

Le résultat de la commande sera :   

![LinuxMan2](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/LinuxMan2.PNG)
---
Pour les commandes Linux un <ins>terminal en mode root </ins>est recommandé.

1.  Première choses à effectuer :   

    * Regarder que les appareils soient bien allumé, ordinateur, box internet, serveurs(DHCP,DNS,ect...), ect...
    * Vérifier que le pc est branché à internet :   
    *-* Regarder que l'ordinateur à un câble Ethernet de branché. Vérifier que le câble est bien branché des deux coté.  
    *-* Sinon vérifier que le câble n'est pas cassé cela peut être visible s’il y a des marques de torsion.   
    *-* Tester de changer le câble Ethernet avec un intact ou neuf.

##

2. Vérifier que la carte réseau est allumé :

   * Pour ce faire taper la commande <span style="color:red">"ip link show"</span>, il faut trouver dans la liste qui s'affiche la carte réseau à vérifier (voir image ci-dessous)![LinuxCarte1](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/LinuxCarte.PNG)   
   * Une fois trouvé regarder si la carte est " up ", cela signifie qu'elle est allumée.
   * S’il y a marqué " down " il faut allumer la carte réseau. Donc il faut exécuter la commande :  
   <span style="color:red">ip link set up dev "nom carte réseau"</span>. Par exemple : " ip link set up dev eth0 ".  

##

3. On vérifie son adressages IP:  

    * Grâce à la commande <span style="color:red">"ifconfig"</span> on vérifie si notre carte réseau à une adresse ip affecté. Par exemple : (Voir photo ci-dessous)![LinuxIfconfig1](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/LinuxIfconfig1.png)   
    Ici on peut voir que ma carte réseau a l'adresse 192.168.1.2 avec le masque réseau 255.255.255.0 .
    * Avant d'activer le service DHCP il faut vérifier s’il n'y a pas déjà le service d'allumer. Pour ce faire exécuter la commande <span style="color:red">"ps aux | grep dhclient"</span> (voir photo ci-dessous)![LinuxPsAux1](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/LinuxPsAux1.png)Dans le cadre rouge les trois services dhclient qui tourne. Il est possible de les éteindre les services, il suffit de faire <span style="color:red">kill 'ID du processus'</span> l'ID processus est le premier chiffre de la ligne par exemple : " kill 50479 " , cette commande éteint le processus dhclient nommé 50479 (Ici le premier de la liste).
    * Pour activer le DHCP exécuter la commande :  
    <span style="color:red">"dhclient"</span>.   
    * Sinon il est possible d'adresser une adresse IP avec la commande :   
   <span style="color:red">ip addr add "adresse ip"/"masque de sous réseaux" dev "nom carte réseau"</span> (Exemple : ip addr add 192.168.1.2/24 dev eno1).![LinuxIP1](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/LinuxIP1.PNG)  

##

4. Si cela ne marche toujours pas il faut vérifier en essayant de ping un autre ordinateur sur le réseau :

   * Ping avec la commande : <span style="color:red"> ping "ip de la machine visé" </span> (Exemple: ping 192.168.1.2) La machine visée est censé répondre au ping.
   * Sinon tenter de ping la passerelle réseau ou le serveur google(IP serveur test de ping google 8.8.8.8).

##

5. Pour aller plus loin on vérifie la table de routage pour s'assurer de son bon réglage ou fonctionnement : 

    * Premièrement regarder si il y a deja une passerelle avec la commande <span style="color:red"> route -n </span> . (image ci-dessous)![LinuxRoute1](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/LinuxRoute1.png)    
    Dans l'exemple il y a bien une route vers la passerelle. S’il n'y a rien, il faut faire la route manuellement vers la passerelle du réseau. Pour ce faire taper la commande <span style="color:red"> route add default gw " ip passerelle " </span> Exemple : " route add default gw 10.0.2.2 ".
    * Une autre commande permet de vérifier les routes par défaut pour s'assurer que l'ordinateur communique bien avec le réseau, <span style="color:red"> ip route show  </span>. S’il n'y a pas de route il faut en rajouter une grâce à la commande :
    <span style="color:red">ip route add default "adresse ip"/"masque sous réseau" dev "nom carte réseau"</span>


---------
## Windows:

Pour utiliser les commandes Windows je recommande d'utiliser le <ins>PowerShell en mode Administrateur.</ins> Comparé à Linux il n’y a pas besoins d'installer de logiciel, ou autre utilitaire. Le PowerShell de Windows est déjà complet.

1.  Test de base à effectuer :
    * Regarder que les appareils soient bien allumé, ordinateur, box internet, serveurs (DHCP,DNS,ect...), ect...
    * Vérifier que le pc est branché à internet :
    *-* Regarder que l'ordinateur à un câble Ethernet de branché. Vérifier que le câble est bien branché des deux coté.
    *-* Sinon vérifier que le câble n'est pas cassé cela peut être visible s’il y a des marques de torsion.
    *-* Tester de changer le câble Ethernet avec un intact ou neuf.

##

2. On s'assure de la connectivité réseau :   

    * Grace à <span style="color:red">"netstat "</span>.   (Voir image ce-dessous)![WinNetstat](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/WinNetstat.PNG)

  
    * S'il y a écrit "ESTABLISHED" cela signifie que vous avez accés à internet. Sinon voila a quoi ressemble un non-accès à internet: (voir image ci-dessous)
   
    ![WinNetstat2](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/WinNetstat2.PNG)   
    
    Il y a écrit " SYN_SENT", "FIN_WAIT_1", "TIME_WAIT", cela signifie que la connexion n'as pas pu se faire, donc que votre ordinateur n'as pas accès internet.

##

3. Vérifier que la carte réseau est allumé :

   * Pour savoir le nom de sa carte réseau et si elle est allumé on utilise la commande <span style="color:red">"netadapter"</span>, il faut trouver dans la liste qui s'affiche la carte réseau à configurer. Par exemple je cherche à configurer la carte wi-fi : (Voir image ci-dessous) ![WinNetAdapter](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/WinNetAdapter.PNG)    Encadré en rouge le nom de la carte réseau, qu'il faudra utilisé pour l'étape suivante et encadré en jaune le status "up", "disconnected" ou "disabled". (Souvent pour Windows la carte réseau filaire s'appelle "Ethernet").
   * Pour allumer la carte réseau on exécute la commande :  
   <span style="color:red">Enable-netadapter -name "Nom carte réseau"</span>.   
   Exemple je vais éteindre et rallumer ma carte réseau "Ethernet":   
   *-* Je met la commande : ' Disable-NetAdapter -name Ethernet ' et regarde ensuite le resultat avec ' NetAdapter ' (Voir image ci-dessous) ![WinNetAdapterDis](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/WinNetAdapterDis.PNG)     
    En exécutant la commande il demande confirmation répondre o (oui) ou n (non). On voit bien que ma carte réseau est désactivé.   
    *-* Je souhaite maintenant l'allumer : ' enable-NetAdapter -name Ethernet ' . (Voir image ci-dessous)![WinNetAdapterEna](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/WinNetAdapterEna.PNG)   Ma carte réseau est maintenant activé. Dans mon cas il y a écrit "Disconnected" car je ne suis pas branché en ethernet mais en Wi-Fi.

##

4. On vérifie son adressages IP:  

    * Grâce à la commande vu avant <span style="color:red">"ipconfig /all"</span> on vérifie si notre carte réseau à une adresse ip affecté. Si le réseau dispose d'un DHCP il faut exécuter c'est deux commandes :   
    *-* La première commande vas enlever toute les adresse ip attribué sur toute les carte réseau : <span style="color:red">"ipconfig /release "</span>.   
    *-* La deuxième commande permet de demander une adresse ip si les réseau dispose d'un service DHCP (service qui permet d'attribuer une adresse ip automatiquement):
    <span style="color:red">"ipconfig /renew"</span>   
    * Sinon il est possible d'adresser une adresse IP manuellement avec les commandes :   
    *-* Pour entrer dans le programme qui permet la gestion de tout l'aspect réseau de l'ordinateur :
    <span style="color:red">netsh</span> .   
    *-* Ensuite taper la commande <span style="color:red">interface ip</span> , elle active la configuration de l'ipv4 . 
    *-* Pour suivre la commande <span style="color:red">show adresses</span> , elle affiche toute les interfaces réseaux de l'ordinateur et les ip associé.
    
    ![NetshShow](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/NetshShow1.PNG)   
    *-* Pour finir on affecte une adresse ip <span style="color:red"> set address "Nom de l'interface(Encadré en rouge sur l'image ci-dessus)" statique xxx.xxx.xxx.xxx             yyy.yyy.yyy.yyy zzz.zzz.zzz.zzz</span> . Dans la commande, *xxx.xxx.xxx.xxx* représente l'adresse IP que vous souhaitez attribuer à votre ordinateur. Les *yyy.yyy.yyy.yyy*     représente le masque IP. Enfin les *zzz.zzz.zzz.zzz* sont l'adresse de la passerelle du réseau. Pour exemple: ' netsh interface ip set address "Wi-fi" static 192.168.25.3       255.255.255.0 192.168.25.1 ' .

##

5. On vérifie la table de routage pour s’assurée :  

    * Il faut regarder les routes par défaut pour s'assurer que l'ordinateur communique bien avec le réseau. Pour vérifier il faut faire la commande<span style="color:red"> route print  </span>. S’il n'y a pas de route vers la passerelle il faut en rajouter une grâce à la commande :
    <span style="color:red">route ADD "ip du réseau de destination" MASK "Masque du sous réseau de  destination"  "ip de la passerelle" Metric 3 IF  'interface réseau"  </span>. Exemple route ADD 157.0.0.0 MASK 255.0.0.0  157.55.80.1 METRIC 3 IF 2   
    * Pour avoir le numéro de l'interface réseau il faut exécuter la commande : <span style="color:red"> netsh interface ip show interface </span>, il suffit ensuite de prendre le numéro de la carte réseau souhaité.(voir image ci-dessous) ![NetshInterface](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/NetshInterface1.PNG)   
  
##

6. Si cela ne marche toujours pas il faut essayer ces étapes afin de peut-être déceler le problème :
   * Premièrement on test de Ping un autre Ordinateur sur le réseau ou alors Google(8.8.8.8) avec la commande : <span style="color:red"> ping "ip de la machine visé" </span> (Exemple: ping 192.168.1.2)Ping utilise le protocole ICMP. La machine visée est censée répondre au ping.    


-----



  

