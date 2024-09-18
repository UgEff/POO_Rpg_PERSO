# initialisation du joueur
joueur = Joeur(
    nom="Hero",
    age=25,
    point_de_vie=100,
    force=5,
    defense=2,
    inventaire=[],
    est_vivant=True,
    niveau=1,
    experience=0,
    experience_next_niveau=10
)

# initialisation des ennemis de base
Gobelin = Ennemi(
    nom="Gobelin",
    age=20,
    point_de_vie=50,
    force=20,
    defense=5,
    inventaire=[],
    est_vivant=True,
    niveau=1,
    point_de_vie_max=50,
    type_ennemi="gobelin",
    experience_to_give=10,
    #donne un loot
    loot=[Baton,potion_de_soin]
)

Squelette = Ennemi(
    nom="Squelette",
    age=30,
    point_de_vie=30,
    force=10,
    defense=2,
    inventaire=[],
    est_vivant=True,
    niveau=1,
    point_de_vie_max=30,
    type_ennemi="squelette",
    experience_to_give=5,
    loot=[epee]
)

# initialisation ennemie boss
Dragon = Ennemi(
    nom="Dragon",
    age=1000,
    point_de_vie=200,
    force=50,
    defense=20,
    inventaire=[],
    est_vivant=True,
    niveau=1,
    point_de_vie_max=200,
    type_ennemi="dragon",
    experience_to_give=100,
    loot=[Armure_de_fer]
)

Orc=Ennemi(
    nom="Orc",
    age=40,
    point_de_vie=70,
    force=30,
    defense=10,
    inventaire=[],
    est_vivant=True,
    niveau=1,
    point_de_vie_max=70,
    type_ennemi="orc",
    experience_to_give=20,
    loot=[Epee,piece_d_or]
)