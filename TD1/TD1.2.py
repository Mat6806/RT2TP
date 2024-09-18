def Superior(a:int,b:int) -> int :
    #fonction qui compare deux nombre et ressort le nombre supérieurs des deux
    if a > b:
        return a
    else: 
        return b
        
resultat = Superior(3.4,3.2)
print("Le plus gros nombre est", resultat)


def SuperiorSeuil(a:int):
    b =int(input("veuillez inserer un seuil")) #selection de la variable par l'utilisateur
    if a>b:         #comparaison avec un if 
        print(f"{a} est supérieur au seuil {b}") 
    else:
        print(f"{a} est inférieur au seuil {b}")

SuperiorSeuil(43)

def SuperiorListe():
    a = [2,4,1,23,6,14] #initialisation de la liste
    resultat = a[0] #création de la variable qui va stocker le resultat
    for i in range(1,len(a)): #création de la boucle de comparaison
        if a[i] >resultat:    #element de comparaison qui défille à chaque valeurs de la boucle
            resultat = a[i] #ajout de la variable qui est supérieur aux autres dans le résultat
    print(resultat)     #affichage sur résultat

SuperiorListe()

def SuperiorListeSeuil():
    a = [2,4,1,23,6,14] #initialisation de la liste
    resultat = a[0] #création de la variable qui va stocker le resultat
    b = int(input("selectionner un seuil"))
    for i in range(1,len(a)): #création de la boucle de comparaison
        if a[i] >b:    #element de comparaison qui défille à chaque valeurs de la boucle
            resultat = a[i] #ajout de la variable qui est supérieur aux autres dans le résultat
    else:
        resultat = b
    print(resultat)     #affichage sur résultat

SuperiorListeSeuil()