class Personnage():
    # Constructeur
    def __init__(self,nom,age,point_de_vie,force,defense,inventaire,est_vivant):
        self.nom = nom
        self.age = age
        self.point_de_vie = point_de_vie
        self.force = force
        self.defense = defense
        self.inventaire = inventaire
        self.est_vivant = est_vivant

        # methode
        def attaque(self,ennemi):
            ennemi.point_de_vie -= self.force - ennemi.defense
            return ennemi.point_de_vie
        
        def encaisser_degat(self,degat):
            self.point_de_vie -= degat
            return self.point_de_vie

        def est_vivant(self):
            if self.point_de_vie > 0:
                return True
            else:
                return False

                