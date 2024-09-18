from perso import Personnage

class Objet:
    def __init__(self,nom,description,effet):
        self.nom = nom
        self.description = description
        self.effet = effet

    def utiliser(Personnage):
        print(f"{Personnage.nom} utilise {self.nom} avec l'effet {self.effet}")
        


class Arme(Objet):
    def __init0__(self,nom,description,effet,dommage):
        super().__init__(nom,description,effet)
        self.dommage = dommage

    def equiper(self,personnage):
        personnage.force += self.dommage
        print(f'Arme {nom} est équipée par {personnage.nom}')
        return personnage.force

class Armure(Objet):
    def __init__(self,nom,description,effet,defense):
        super().__init__(nom,description,effet)
        print(f'Armure {nom} est équipée par {personnage.nom}')
        self.defense = defense

    def equiper(self,personnage):
        personnage.defense += self.defense
        return personnage.defense


class Potion(Objet):
    def __init__(self,nom,description,effet,soin):
        super().__init__(nom,description,effet)
        self.soin = soin

        def utiliser(self,personnage):
            personnage.point_de_vie += self.soin
            print(f'{personnage.nom} a utilisé {self.nom} et a été soigné de {self.soin} points de vie')
            return personnage.point_de_vie


#Instancer du loot
piece_d_or=Objet(
    nom="Piece d'or",
    description="Monnaie",
    effet="argent",
    )

potion_de_soin=Objet(
    nom="Potion de soin",
    description="Restaure 30 point de vie",
    effet="soin",
    ) 

Baton=Arme(
    nom="Baton",
    description="Arme de base",
    effet="attaque",
    dommage=5
    )

Couteau=Arme(
    nom="Couteau",
    description="Arme de base",
    effet="attaque",
    dommage=10
    )

Epee=Arme(
    nom="Epee",
    description="Arme de base",
    effet="attaque",
    dommage=15
    )

Protection_tissue=Armure(
    nom="Protection tissue",
    description="Armure de base",
    effet="defense",
    defense=2
    )

Armure_de_cuir=Armure(
    nom="Armure de cuir",
    description="Armure de base",
    effet="defense",
    defense=5
    )

Armure_de_fer=Armure(
    nom="Armure de fer",
    description="Armure de base",
    effet="defense",
    defense=10
    )