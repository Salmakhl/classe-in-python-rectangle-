class rectangle():
    #def __init__(self):
      #  self.longueur = 18 
       # self.largeur = 11

    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur


    #def __init__(self,rectangle1):
     #   self.longueur = rectangle1.longueur
      #  self.largeur = rectangle1.largeur


    def perimetre(self):
        return (self.longueur+ self.largeur)*2
    


    def air(self):
        return (self.largeur*self.longueur)
    

    def IScarre(self):
        if self.longueur==self.largeur :
            print("est un carré.")


    def affichageR(self):
        print("la longueur :{} ,la largeur: {}".format(self.longueur,self.largeur))
        print(f"le perimetre est{self.air}")
        print(f"l'aire est {self.perimetre}")
        print(f"le rectangle {self.IScarre}")
        





