# Debut
#    Fonction bubulle (tableau)
#    déclarer tri -> False
#    Tant que tri == False
#       tri -> True
#       Pour loop de 0 à taille de tableau-1
#           Si tableau position loop > tableau position loop+1
#               déclarer v = tableau position loop
#               tableau position loop = tableau position loop+1
#               tableau position loop+1 = v
#               tri -> False
#           Fin de Si
#       Fin de Pour
#       Afficher tableau
#    Fin de Fonction
# Fin

def triselectif1(tab):
    etape = 0
    changement = 0
    tri = False
    while(tri == False):
        tri = True
        for loop in range(len(tab)-1):
            if tab[loop] > tab[loop+1]:
                tab[loop], tab[loop+1] = tab[loop+1],tab[loop]
                tri = False
                changement += 1
            etape += 1
    print(tab)
    print("comparaison", etape)
    print("changement", changement)
