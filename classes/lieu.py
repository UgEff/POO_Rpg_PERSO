import random as rd
from .objet import * #import tout les objets
from .ennemi import *

class Lieu():
    def __init__(self, nom, description, ennemi=None, objet=None):
        self.nom = nom
        self.description = description
        self.ennemi = ennemi if ennemi is not None else []  
        self.objet = objet if objet is not None else []  

    def decrire(self):
        print(f"Vous entrez dans {self.nom}. {self.description}")

    # afficher les ennemis dans le lieu
    def list_ennemis(self):
        if not self.ennemi:
            print("Il n'y a pas d'ennemis ici.")
        else:
            print(f'Vous voyez {len(self.ennemi)} ennemis ici:')
            for ennemi in self.ennemi:
                print(f" {ennemi.nom} (niveau {ennemi.niveau})")

    def list_objet(self):
        if not self.objet:
            print("il n'y a aucun objet ici")
        else:
            print(" vous voyer des objets dnas la piece")
            for obj in self.objet:
                print(f"{objet.nom}: {objet.description}")

    def ennemi_apparition(self):
        ennemi_present=[]
        for ennemi , taux_apparition in self.ennemi:
            if rd.random() < taux_apparition:
                ennemi_present.append(ennemi)
        return ennemi_present


# Creation d'instance de lieu
village = Lieu(
    nom="Village principal",
    description="Le village où le personnage est né et a grandi",
    ennemi=[], 
    objet=[potion_de_soin] 
)


foret = Lieu(
    nom="Forêt au bord du village",
    description="Un endroit sombre rempli de créatures.",
    ennemi=[(gobelin, 0.5), (squelette, 0.3), (orc, 0.1), (dragon, 0.1)],
    objet=[] 
)


caverne = Lieu(
    nom="Caverne sombre",
    description="Une caverne remplie de dangers inconnus.",
    ennemi=[(squelette, 0.4), (gobelin, 0.2)],
    objet=[Epee]
)



"""
# Zone de test *****
village.decrire()
"""