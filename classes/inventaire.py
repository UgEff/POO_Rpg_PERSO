from .perso import Personnage
from .objet import Objet

class Inventaire():
    def __init__(self,objet=None):
        self.objet = objet
        self.sac = []

    def ajouter_objet(self,objet):
        self.sac.append(objet)
        return self.sac

    def retirer_objet(self,objet):
        if objet in self.sac:
            self.sac.remove(objet)
        return self.sac

    def afficher_sac(self):
        if len(self.sac) == 0:
            print("Votre sac est vide")
        else:
            print("Objet dans votre sac:")
            for objet in self.sac:
                print(f"{objet.nom}: {objet.description}")

