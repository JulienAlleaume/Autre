# Shéma réseau ![TEST](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/a69f4433fb316a3753858b0f86dc739f1d495f73/Image/Sh%C3%A9ma_r%C3%A9seau.drawio.svg)

Ce schéma réseau a été réalisé grâce à draw.io. Malheureusement je n'ai pas réussi à utiliser Mermaid, il y a trop de complications, différentes versions et de plus VScode et Github n'ont pas la même présentation pour Mermaid en fonction des plugins installés.   

Ce réseau a été réaliser en salle de réseau grâce à un switch, un routeur et deux ordinateurs sous Windows et une machine virtuel linux.   

Pour linux j'ai utilisé une VirtualBox Kali-Linux. Grâce au logiciel Oracle VM VirtualBox, et une image disque, j'ai créé une machine virtuelle. Toute les commandes et captures d'écran ont été testé et faite sur la VM.   

* Mise en place du réseau :   
  *-* Je recrée le branchement du schéma.   
  *-* Je configure ensuite les ip sur le menu du routeur, pour y accéder j'ai tapé dans un navigateur 192.168.88.1. Il est aussi possible d'utiliser RouterOS.   
  *-* Une fois connecter dans l'onglets "configuration rapide" j'ai récupéré l'adresse ip du port 1 "internet", qui est 10.202.0.196 et l'adresse de mon réseau local qui est 192.168.88.0.   
  *-* Ensuite j'ai récupéré l'ip d'un collègue qui est dans la même salle et qui avait son propre réseau local en 192.168.80.0 et son port 1 "internet" en 10.202.0.191 .   
  *-* Nous avons ensuite crée la route entre nos réseaux dans le menu 'IP'-> 'Routes'. ![RouteurRoute](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/Router2.png)   
  On renseigne l'adresses de destination et la gateway du réseau distant.   
  
  *-* J'essaie ensuite de ping l'ordinateur de mon collègue dans son réseau.  ![RouteurRoute](https://github.com/IUT-Beziers/sae12-JulienAlleaume/blob/f6cf29d53a6b98f2b3c3768a32b72ee210d84bd4/Image/Ping1.PNG)   
  Tout fonctionne bien dans les deux sens. Les réseau communique entre eux.
