import random as rd

class Quete():
    # Classe qui permet de créer des quêtes
    # constructeur
    def __init__(self,description,objectif,recompense,progression):
        self.description = description
        self.objectif = objectif
        self.recompense = recompense
        self.progression = progression

    # methode
    def afficher_info(self):
        print(f"Description: {self.description}") 
        print(f"Objectif: {self.objectif}")
        print(f"Récompense: {self.recompense}")
        print(f"Progression: {self.progression}")
        return

    def maj_progression(self,quantité):
        if self.progression + quantité >= self.objectif:
            self.progression = self.objectif
            print("Quête terminée")
        else:
            self.progression += quantité
            print(f"Progression: {self.progression}/{self.objectif}")



q1 = Quete("tuer 5 gobelins",5,"100 pièces",0)
q2 = Quete("tuer 10 squelette",10,"200 pièces",0)
q3 = Quete("tuer 15 orc",15,"300 pièces",0)
q4 = Quete("tuer 1 dragon",20,"400 pièces",0)

lst_q=[q1,q2,q3,q4]
rd_quest = rd.choice(lst_q)
rd_quest.afficher_info()
