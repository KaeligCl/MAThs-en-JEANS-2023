''' Cette fonction prend une liste en entrée et retourne une nouvelle liste, 
dans laquelle chaque élément de la liste initiale a été décrémenté de 1, 
sauf le dernier élément qui a été incrémenté de 1. '''


def suivant(liste):
    nv_liste = []
    nv_val = 0
    for val in liste:
        if val != 1:
            nv_liste.append(val-1)
        nv_val += 1
    nv_liste.append(nv_val)
    return nv_liste


''' Cette fonction prend une liste en entrée, calcule la longueur de la plus longue 
suite de nombres obtenue en appliquant la fonction suivant() répétitivement à cette liste, 
et retourne la longueur et la liste complète de toutes les suites obtenues. '''


def suite(liste):
    longueur = 0
    liste_suite = [liste]
    nv_liste = suivant(liste)
    while nv_liste not in liste_suite:
        liste_suite.append(nv_liste)
        nv_liste = suivant(nv_liste)
    longueur = len(liste_suite) - liste_suite.index(nv_liste)
    return longueur, liste_suite


'''Cette fonction construit une liste de toutes les combinaisons possibles 
de nombres dont la somme est égale au nombre donné en entrée.'''


def construire(nb):
    dico_poss[nb] = []
    construire_rec(nb, nb, [])


'''Cette fonction est appelée par la fonction construire() pour 
construire récursivement la liste de toutes les combinaisons possibles 
de nombres dont la somme est égale au nombre donné en entrée. '''


def construire_rec(nb, n, liste):
    if n == 0:
        dico_poss[nb].append(liste)
    else:
        for i in range(1, n+1):
            construire_rec(nb, n-i, liste+[i])


'''Cette fonction prend une liste de nombres en entrée et calcule la plus longue suite de 
nombres que l'on peut obtenir en appliquant la fonction suivant() répétitivement à cette liste. 
Elle stocke la longueur et la suite complète dans un dictionnaire pour chaque liste donnée.'''


def suites(liste):
    for dep in liste:
        tu_dep = tuple(dep)
        dico_suites[tu_dep] = suite(dep)


'''Cette fonction effectue le traitement principal pour le nombre de boîtes donné en entrée.
Elle construit d'abord toutes les combinaisons possibles de nombres dont la somme est égale 
au nombre de boîtes donné en entrée, puis calcule la plus longue suite de nombres pour chacune de ces combinaisons.
Elle détermine ensuite la plus longue suite trouvée et la liste de toutes les suites ayant cette longueur.
Elle affiche enfin ces résultats.'''


def demo():
    global high_longueur
    best_suite = []  # stocke les suites de nombres avec la plus grande longueur
    orgenised_suite = []  # stocke les suites de nombres avec la plus grande longueur, triées
    # initialise le nombre
    nb_choisi = int(y)
    # créé toute les configuration possible pour le nombre de boite donné
    construire(nb_choisi)
    suites(dico_poss[nb_choisi])
    # vérifie quelle est la plus longue suite et la stock dans high_longueur
    for depart, (longueur, suite) in dico_suites.items():
        if len(suite)-longueur > high_longueur:
            high_longueur = len(suite)-longueur
            best_suite = [tuple(suite[0])]
    # stock les autres suite qui font la même longueur que la plus longue
    for depart, (longueur, suite) in dico_suites.items():
        if len(suite)-longueur == high_longueur:
            best_suite.append(tuple(suite[0]))
            temporary_memory = suite[0]
            temporary_memory.sort()
            orgenised_suite.append(tuple(temporary_memory))

    # supprime les doublons et trie la liste best_suite
    best_suite = list(set(best_suite))
    best_suite.sort()
    # supprime les doublons et trie la liste orgenised_suite
    orgenised_suite = list(set(orgenised_suite))
    orgenised_suite.sort()

    # début de la séquence d'affichage dans le terminal
    print("_"*50)

    print("nombre de boite =", list(depart))
    print("max longueur =", high_longueur)

    print()

    # print la liste que si elle est assez petite pour ne pas déranger le lecteur de pleins de liste
    if len(best_suite) < 25:
        print("liste avec max longueur :", best_suite)
    else:
        print("liste avec max longueur : Trop long")
    print("nombre de liste avec max longueur :", len(best_suite))
    print()

    # print la liste que si elle est assez petite pour ne pas déranger le lecteur de pleins de liste
    if len(orgenised_suite) < 25:
        print("liste avec max longueur (organiser):", orgenised_suite)
    else:
        print("liste avec max longueur (organiser): Trop long")
    print("nombre de liste avec max longueur (organiser):", len(orgenised_suite))
    print()

    print("-"*50)
    print()


# initialise les variable et dictionnaire
dico_poss = {}
dico_suites = {}
high_longueur = 0

y = 0
x = int(input("\nChoisir un nombre de cartons entre 1 et 20 (0 pour avoir les 6 premier nombre demi-pyramidaux): "))
if x == 0:
    while x <= 5:
        x += 1
        y += x
        high_longueur = 0
        dico_poss = {}
        dico_suites = {}
        demo()
else:
    y = x
    demo()
