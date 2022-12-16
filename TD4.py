import random


class Matrice2D():
    def __init__(self, nbLignes, nbColonnes):
        self.nbLignes = nbLignes
        self.nbColonnes = nbColonnes
        self.Matrice = [] 

        for i in range(self.nbLignes):
            nvligne = []
            for j in range(self.nbColonnes):
                nvligne.append(0)
            self.Matrice.append(nvligne)

    def affiche(self):
        for lig in self.Matrice:
            for val in lig:
                print(f"{val:.2f} ", end='')
            print("")
    
    def randomInit(self, etendue):
        random.seed()

        for i in range(self.nbLignes):
            for j in range(self.nbColonnes):
                    self.Matrice[i][j] = random.uniform(0.0,etendue)



class MatriceRotation(Matrice2D):
    def __init__(self, axe,angle=0):
        self.axe=axe
        self.angle=angle

        # if



    def affiche(self):
        Matrice2D.affiche(self)

    # def multiplieMatrice(self,MatriceRotationA, axe):
        

if __name__ == "__main__":
    m = Matrice2D(2,3)
    m.affiche()
    m.randomInit(100)
    m.affiche()