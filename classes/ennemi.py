from perso import Personnage


class Ennemi(Personnage):
    # constructeur
    def __init__(self,nom,age,point_de_vie,force,defense,inventaire,est_vivant,niveau,point_de_vie_max,type_ennemi,experience_to_give,loot):
        super().__init__(nom,age,point_de_vie,force,defense,inventaire,est_vivant)
        # type d'ennemi possible
        type_ennemie = ["gobelin","squelette","orc","loup","goule","troll","dragon"]
        if type_ennemi not in type_ennemie:
            raise ValueError(f"Le type d'ennemi doit être dans {type_ennemie}")

        self.type_ennemi = type_ennemi
        self.point_de_vie_max = point_de_vie_max
        self.experience_to_give = experience_to_give
        self.loot = loot if loot is not None else [] # si le loot est vide on met une liste vide
        self.niveau = max(1,niveau) # on met le niveau de l'ennemi à 1 si il est inférieur à 1

    # methode
    def comportement_IA(self,point_de_vie,inventaire,est_vivant):
        action = "attaque"
        # si possede un objet de type arme il va attaquer avec
        if "arme" in self.inventaire:
            action = "attaque"
        # Si l'ennemi possède une arme dans son inventaire, il attaque
        if "arme" in self.inventaire:
            action = "attaque"

        # Si les points de vie sont entre 80% et 100%, il attaque ou se défend à 70% d'attaque et 30% de défense
        if self.point_de_vie >= self.point_de_vie_max * 0.8:
            action = np.random.choice(["attaque", "defense"], p=[0.7, 0.3])

        # Si les points de vie sont entre 30% et 80%, il attaque à 30% et se défend à 70%
        elif self.point_de_vie < self.point_de_vie_max * 0.8 and self.point_de_vie >= self.point_de_vie_max * 0.3:
            action = np.random.choice(["attaque", "defense"], p=[0.3, 0.7])

        # Si les points de vie sont entre 20% et 30%, il attaque peu et se défend beaucoup
        elif self.point_de_vie < self.point_de_vie_max * 0.3 and self.point_de_vie > self.point_de_vie_max * 0.2:
            action = np.random.choice(["attaque", "defense"], p=[0.2, 0.8])

        # Si les points de vie sont inférieurs à 20%, il peut tenter de fuir
        elif self.point_de_vie <= self.point_de_vie_max * 0.2:
            action = np.random.choice(["attaque", "defense", "fuite"], p=[0.1, 0.7, 0.2])

        return action
    
    def attaque(self,cible):
        print(f"{self.nom} attaque {cible.nom}")
