#Composition
class enseignement():
    """ cette classe définie i=ub enseignement """
    def __init__ (self, intitule:str, cm:float, td:float,tp:float) -> None:
        self.sujet:str = intitule
        self.cm:float = cm
        self.td:float = td
        self.tp:float = tp
        
    def calculHeureqtd(self)->float:
        return (self.cm * 1.5 + self.td + self.tp * 0.67)
    
class etudiant():
    """cette classe definit les etudiant"""
    def __init__ (self, prenom:str,nom:str,annee:str)-> None:
        self.prenom:str = prenom 
        self.nom:str = nom
        self.annee:str = annee
        """Compositon de l'objet avec enseignement"""
        self.enseignement = enseignement #= Enseignement("ProgAvancé", 2,2,11)#compositon
    
    #on va appeler cette méthode sur l'instance étudiant
    def totalHeureqtd(self) -> float:
        """calcul du total d'heures"""
        return self.enseignement.calculHeureqtd()

#creation instance de la classe Etudiant qui en interne génenre l'instance de l classe enseignement
ens = enseignement('progavancé',2,2,11)
etud = etudiant('Jean-marc','Pouchoulon','première')

#appel de la méthode totalHeuresqt sur l'instance etud qui appelle la methode sur l'instance ens
print(round(etud.totalHeureqtd(),1))
        