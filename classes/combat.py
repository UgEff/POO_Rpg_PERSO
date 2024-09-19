
from joueur import Joueur
from ennemi import Ennemi


class Combat():
    def __init__(self,joueur,ennemi):
        self.joueur = joueur
        self.ennemi = ennemi

    def calcule_degat(self,attaquant,defenseur):
        degat=attaquant.force-defenseur.defense
        degat = max(degat, 0)  # Les dégâts ne peuvent pas être inférieurs à zéro
        defenseur.point_de_vie -= degat
        print(f"{attaquant.nom} inflige {degat} points de dégâts à {defenseur.nom}")
    
    def tour_par_tour(self):
        while True:
            choix=self.afficher_menu_action()
            # attaque du joueur
            if choix == "1":
                self.calcule_degat(self.joueur, self.ennemi)
                if self.ennemi.point_de_vie <=0:
                    print("Vous avez gagné")
                    self.joueur.gagner_experience(self.ennemi.experience_to_give)
                    # loot
                    if self.ennemi.loot is not None:
                        print("l'ennemie à laissé tomber des objets")
                    for loot in self.ennemi.loot:
                        print(f'{objet.nom} a été ajouté à votre inventaire')
                        self.joueur.inventaire.append(loot)
                    print(f"les objets ont été ajouté à votre inventaire")
                    break
                
                # attaque de l'ennemi
                self.ennemi.attaque(self.joueur)
                self.calcule_degat(self.ennemi, self.joueur)
                if self.joueur.point_de_vie <=0:
                    print("Vous avez perdu")
                    break

            elif choix == "2":
                self.joueur.utiliser_objet()
                continue

            elif choix == "3":
                print("Vous avez fui")
                break
            
        
    def afficher_menu_action(self):
        choix=""
        while choix != "1" and choix != "2" and choix != "3":
            print("1. Attaquer")
            print("2. Utiliser un objet")
            print("3. Fuir")
            choix = input("Que voulez-vous faire ?")
            if choix != "1" and choix != "2" and choix != "3":
                print("Veuillez choisir une action valide")
        return choix


# Exemple de création d'un joueur et d'un ennemi
# Création d'une instance de la classe Joueur
"""
joueur = Joueur(
    nom="Héros",               # Nom du joueur
    age=30,                    # Âge du joueur (exemple)
    point_de_vie=100,          # Points de vie initiaux
    force=15,                  # Force du joueur
    defense=1,                # Défense du joueur
    inventaire=[],             # Inventaire vide pour commencer
    est_vivant=True,           # Le joueur est en vie
    niveau=1,                  # Niveau initial
    experience=0,              # Expérience initiale
    experience_next_niveau=100 # Expérience nécessaire pour monter de niveau
)
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
    loot=[]  # Pas de loot à donner à ce stade
)
# Création d'une instance de la classe Combat
#combat = Combat(joueur, ennemi)
# Lancer le combat
#combat.tour_par_tour()
"""