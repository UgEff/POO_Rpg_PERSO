from .perso import Personnage
from .objet import *


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


# Création d'un ennemi Gobelin
gobelin = Ennemi(
    nom="Gobelin",
    age=25,
    point_de_vie=50,
    force=30,
    defense=5,
    inventaire=[],  # Pas d'inventaire pour cet ennemi
    est_vivant=True,
    niveau=1,
    point_de_vie_max=50,
    type_ennemi="gobelin",  # Type d'ennemi valide
    experience_to_give=20,  # Expérience donnée quand tué
    loot=[Baton]  # Pas de loot à donner à ce stade
)
# Creation d'ennemi squelette
squelette = Ennemi(
    nom="Squelette",
    age=120,
    point_de_vie=20,
    force=10,
    defense=5,
    inventaire=[], 
    est_vivant=True,
    niveau=3,
    point_de_vie_max=50,
    type_ennemi="squelette",  # Type d'ennemi valide
    experience_to_give=30,  # Expérience donnée quand tué
    loot=[Couteau]
)  

orc = Ennemi(
    nom="Orc",
    age=30,
    point_de_vie=80,
    force=15,
    defense=8,
    inventaire=[],  # Le loot de l'orc
    est_vivant=True,
    niveau=2,
    point_de_vie_max=80,
    type_ennemi="orc",
    experience_to_give=20,
    loot=[piece_d_or]
)

loup = Ennemi(
    nom="Loup",
    age=5,
    point_de_vie=40,
    force=12,
    defense=5,
    inventaire=[],  # Pas de loot pour ce loup
    est_vivant=True,
    niveau=1,
    point_de_vie_max=40,
    type_ennemi="loup",
    experience_to_give=15,
    loot=[]  # Pas de loot
)

goule = Ennemi(
    nom="Goule",
    age=50,
    point_de_vie=60,
    force=10,
    defense=6,
    inventaire=[],  # Loot pour la goule
    est_vivant=True,
    niveau=2,
    point_de_vie_max=60,
    type_ennemi="goule",
    experience_to_give=25,
    loot=[potion_de_soin]
)

troll = Ennemi(
    nom="Troll",
    age=40,
    point_de_vie=120,
    force=20,
    defense=12,
    inventaire=[],  # Loot du troll
    est_vivant=True,
    niveau=3,
    point_de_vie_max=120,
    type_ennemi="troll",
    experience_to_give=30,
    loot=[Armure_de_cuir, Epee]
)

dragon = Ennemi(
    nom="Dragon",
    age=500,
    point_de_vie=300,
    force=50,
    defense=20,
    inventaire=[],  # Loot du dragon
    est_vivant=True,
    niveau=10,
    point_de_vie_max=300,
    type_ennemi="dragon",
    experience_to_give=100,
    loot=[Armure_de_fer, Epee,Couteau,potion_de_soin]
)