from classes.joueur import Joueur
from classes.lieu import Lieu
from classes.inventaire import Inventaire
from classes.objet import Objet

nom_du_hero=input("quel est ton nom aventurier: ")
age_du_hero=input(f"quelle est ton age {nom_du_hero} : ")
try:
    age_hero=int(age_du_hero)
except ValueError:
    print("Entre un nombre")
    age_hero=int(input("Ton age : "))

hero=Joueur(
    nom=nom_du_hero,
    age=age_hero,
    point_de_vie=100,
    force=10,
    defense=5,
    inventaire=[],
    est_vivant=True,
    niveau=1,
    experience=0,
    experience_next_niveau=30,
)

# TEST INIT perso *****
print(f"Bienvenue, {hero.nom}, âgé de {hero.age} ans. Tu commences avec {hero.point_de_vie} points de vie.")

while hero.est_vivant:
    # menu action
    print(f"que voulais vous faire {hero.nom} ?")
    print("1. Explorer\n 2. Inventaire\n 3. Quitter le jeux")
    choix = input("entrer votre choix: ")

    # Si le hero choisi de se deplacer dans un lieu
    if choix == "1":
        print("vers quel direction veux tu aller ?:")
        print("1. Village\n2. Foret \n3. Caverne")
        choix_lieu = input("Choisis un lieu à explorer : ")

    
        if choix_lieu == "1": # Village
            village.decrire()
            # Que fair dans ce lieux
            print(f"que voulais vous faire {hero.nom} ?")
            print("1. Voir les ennemies \n 2. Fouiller \n 3. Partir")
            choix_action_lieu=input("entrer votre choix : ")
            
            if choix_action_lieu=="1":
                village.list_ennemis() # voir si il y a des ennemies
            elif choix_action_lieu=="2":
                village.list_objet() # voir si il y a des objets
                print(f"que voulais vous faire {hero.nom} ?")
                print("1. Prendre objet \n 2. Rien ")
                choix_action_objet=input("entrer votre choix : ")
                if choix_action_objet=="1":
                    village.list_objet()
                    choix_objet=input("Quelle objet prendre : 1")
                    if choix_objet=="1":
                        object_a_prendre = village.objet.pop(0)
                        hero.inventaire.ajouter_objet(object_a_prendre)
                        print ("objet prix !")
                    else:
                        print("il n'y a pas d'objet dans ce lieu")
            else:
                print("Tu quittes le villages")
                


        elif choix_lieu == "2": # Foret 
            foret.decrire()


        elif choix_lieu == "3":
            caverne.decrire()

        else:
            print("cette direction n'existe pas")

        

    elif choix == "2":
        hero.inventaire.afficher_sac()


    else:
        break
    print("Vous venez de quitter l'aventure")
