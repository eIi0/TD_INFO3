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
