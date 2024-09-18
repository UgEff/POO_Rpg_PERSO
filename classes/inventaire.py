from perso import Personnage
from objet import Objet

class Inventaire():
    def __init__(self,objet):
        self.objet = objet
        self.sac = []

    def ajouter_objet(self,objet):
        self.sac.append(objet)
        return self.sac

    def retirer_objet(self,objet):
        self.sac.remove(objet)
        return self.sac

    def afficher_sac(self):
        if len(self.sac) == 0:
            print("Votre sac est vide")
        else:
            for objet in self.sac:
                print(object.nom)

