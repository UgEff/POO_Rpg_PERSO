from classes.joueur import Joueur
from classes.lieu import Lieu
from classes.inventaire import Inventaire
from classes.objet import Objet
from classes.objet import potion_de_soin , piece_d_or , Baton , Couteau , Epee , Protection_tissue, Armure_de_cuir ,Armure_de_fer 
from classes.ennemi import gobelin , squelette , orc , dragon

nom_du_hero=input("quel est ton nom aventurier: ")
age_du_hero=input(f"quelle est ton age {nom_du_hero} : ")
try:
    age_hero=int(age_du_hero)
except ValueError:
    print("Entre un nombre")
    age_hero=int(input("Ton age : "))


# Instance Hero
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
                choix_action_objet=input("entrer votre choix : ") #action sur objet
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
                


        elif choix_lieu == "2":  # Forêt
            foret.decrire()  # Décrit la forêt
            print(f"Que voulez-vous faire {hero.nom} ?")
            print("1. Voir les ennemis\n2. Fouiller\n3. Partir")
            choix_action_lieu = input("Entrez votre choix : ")

            # Action dans la forêt
            if choix_action_lieu == "1":  # Voir les ennemis
                ennemis_present = foret.list_ennemis()  # Liste des ennemis présents
                if not ennemis_present:
                    print("Il n'y a pas d'ennemis ici.")
                else:
                    print("Que voulez-vous faire ?")
                    print("1. Attaquer un ennemi\n2. Partir")
                    choix_combat = input("Entrez votre choix : ")

                    if choix_combat == "1":  # Combattre un ennemi
                        print("Quel ennemi voulez-vous attaquer ?")
                        for index, ennemi in enumerate(ennemis_present):
                            print(f"{index + 1}. {ennemi.nom} (Niveau {ennemi.niveau})")

                        choix_ennemi = input("Entrez le numéro de l'ennemi à attaquer : ")
                        try:
                            ennemi_a_combattre = ennemis_present[int(choix_ennemi) - 1]
                            # Lancer le combat
                            combat = Combat(hero, ennemi_a_combattre)
                            combat.tour_par_tour()
                        except (ValueError, IndexError):
                            print("Choix invalide, vous ne pouvez pas combattre cet ennemi.")
                    else:
                        print("Vous avez choisi de partir.")

            elif choix_action_lieu == "2":  # Fouiller
                foret.list_objet()  # Liste les objets disponibles
                print(f"Que voulez-vous faire {hero.nom} ?")
                print("1. Prendre un objet\n2. Ne rien faire")
                choix_objet = input("Entrez votre choix : ")

                if choix_objet == "1":
                    foret.list_objet()
                    choix_objet_a_prendre = input("Quel objet prendre ? (numéro) : ")
                    try:
                        objet_a_prendre = foret.objet.pop(int(choix_objet_a_prendre) - 1)
                        hero.inventaire.ajouter_objet(objet_a_prendre)
                        print(f"Vous avez pris {objet_a_prendre.nom} !")
                    except (ValueError, IndexError):
                        print("Choix invalide, il n'y a pas d'objet à prendre.")

            elif choix_action_lieu == "3":  # Partir
                print("Vous quittez la forêt.")



        elif choix_lieu == "3":
            caverne.decrire()

        else:
            print("cette direction n'existe pas")

        

    elif choix == "2": # afficher l'Inventaire
        hero.inventaire.afficher_sac()
        
    elif choix == "3":
        print("Vous venez de quiter l'aventure")
        break


    else:
        print("Vous venez de quitter l'aventure")
