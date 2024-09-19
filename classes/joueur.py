
from .perso import Personnage
import numpy as np

class Joueur(Personnage):
    def __init__(self, nom, age, point_de_vie, force, defense, inventaire, est_vivant, niveau, experience, experience_next_niveau):
        super().__init__(nom, age, point_de_vie, force, defense, inventaire, est_vivant)
        self.niveau = niveau
        self.experience = experience
        self.experience_next_niveau = experience_next_niveau

    # methode
    #apres un ennemie tuer le joueur recupere l'experience de l'ennemie
    def gagner_experience(self,montant_experience):
        self.experience = self.experience + montant_experience
        # condition de montéé de niveau du joueur
        if self.experience >= self.experience_next_niveau:
            self.level_up()
            print("Vous avez gagner un niveau")
        else: 
            diff_xp = self.experience_next_niveau-self.experience
            print(f"il vous reste {diff_xp} avant le niveau suivant")

        

    # une fois l'experience atteint un certain xp le joueur monte de niveau ainsi que ses attributs
    def level_up(self):
        while (self.experience >= self.experience_next_niveau):
            self.niveau +=1
            self.experience -= self.experience_next_niveau
            self.experience_next_niveau = self.experience_next_niveau + (self.experience_next_niveau * 0.2)
            self.point_de_vie += 5
            self.force += 2
            self.defense += 2
            print(f"Vous avez atteint le niveau {self.niveau}")
        return 
        
    def utiliser_objet(self):
        if not self.inventaire:
            print("Votre inventaire est vide")
        else:
            print(f"liste ojet {self.afficher_sac()}")
            choix = input("Quel objet voulez-vous utiliser ? (entrer position de l'objet)")
            objet=self.inventaire[int(choix)]
            objet.utiliser(self)
            if objet.effet=="soin":
                self.point_de_vie += objet.valeur
                print(f"Vous avez récupéré {objet.valeur} points de vie")
                print(f"Vous avez maintenant {self.point_de_vie} points de vie")
            elif objet.effet=="attaque":
                self.force += objet.valeur
                print(f"Vous avez augmenté votre force de {objet.valeur}")
                print(f"Votre force est maintenant de {self.force}")
            elif objet.effet=="defense":
                self.defense += objet.valeur
                print(f"Vous avez augmenté votre défense de {objet.valeur}")
                print(f"Votre défense est maintenant de {self.defense}")
            self.inventaire.remove(objet)
    
        