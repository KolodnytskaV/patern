import random
from E_tour_de_jeu import *


def init_dominos(taille,nom_fichier):
    """La fonction init_dominos prend en argument une taille de royaume et un fichier
    contenant les dominos. Elle mélange la liste globale des dominos et en prend autant que
    nécessaire pour la partie sur un royaume de cette taille avec 2 joueurs.
    Par exemple, pour taille = 5, on prend seulement 24 dominos sur les 48 présents dans le fichier."""
    dominos = extraire_dominos(nom_fichier) #Extraction des dominos depuis le fichier
    nb_dominos = (taille ** 2 - 1) 
    return dominos[:nb_dominos] #Retourne la sélection de dominos nécessaires
    pass

'''print(len(init_dominos(5,"dominos.csv")))'''

def couronnes_zone(royaume,posL,posC,cases_visitees,nb_couronnes):
    """La fonction couronnes_zone est une fonction récursive. Elle prend en argument
    un royaume partiellement rempli, les coordonnées d'une case, un ensemble de cases visitees
    avec le nombre de couronnes présentes sur ces cases visitees. Toutes les cases visitees ont
    la même couleur que la case de coordonnées (posL,posC) et appartiennent à la même zone.
    La fonction renvoie le nombre de couronnes de toute la zone (celle qui contient la case
    (posL,posC), les cases visitees et certainement d'autres cases).
    Si (posL,posC) est déjà présente dans les cases visitees, on renverra nb_couronnes."""
    if (posL, posC) in cases_visitees or royaume[posL][posC]=='CH':
        return nb_couronnes
    cases_visitees.append((posL, posC))
    terrain, couronnes = royaume[posL][posC]
    
    nb_couronnes += int(couronnes)
    
    #Déplacements possibles : droite, gauche, bas, haut
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dL, dC in directions:
        nL, nC = posL + dL, posC + dC
        if 0 <= nL < len(royaume) and 0 <= nC < len(royaume) and (nL, nC) not in cases_visitees and royaume[nL][nC] is not None:
            voisin_terrain, _ = royaume[nL][nC]
            if voisin_terrain == terrain:
                nb_couronnes = couronnes_zone(royaume, nL, nC, cases_visitees, nb_couronnes)
    return nb_couronnes
    pass

'''royaume = creer_royaume(5)
cases_libres = init_cases_libres(5)
ajoutDomino(royaume,cases_libres,(3,'F0','F0'),0,0,'left')
ajoutDomino(royaume,cases_libres,(4,'F0','F0'),0,2,'top')
ajoutDomino(royaume,cases_libres,(24,'F1','Y0'),1,0,'left')
ajoutDomino(royaume,cases_libres,(25,'F1','Y0'),2,0,'top')
ajoutDomino(royaume,cases_libres,(26,'F1','Y0'),0,3,'left')
ajoutDomino(royaume,cases_libres,(5,'F0','F0'),1,3,'top')
ajoutDomino(royaume,cases_libres,(27,'F1','Y0'),3,1,'bottom')
afficher_royaume(royaume)
cases_visitees = []
print(couronnes_zone(royaume, 0, 0, cases_visitees, 0))
print(cases_visitees)
cases_visitees = [(1, 0), (0, 1), (0, 0), (2, 0), (0, 2), (1, 2)]
print(couronnes_zone(royaume, 0, 3, cases_visitees, 2))
print(couronnes_zone(royaume, 1, 1, [], 0))
print(couronnes_zone(royaume, 3, 1, [(3,1)], 1))'''

def score_zone(royaume,posL,posC):
    """La fonction score_zone prend en argument un royaume et une de ses cases.
    Elle renvoie un tuple contenant le score obtenu avec la zone contenant la case (posL,posC),
    ainsi que la liste des cases de cette zone.
    Si la case est vide (royaume[posL][posC] vaut None), on renverra comme score 0 et comme
    cases de la zone, la seule case (posL,posC)."""
    if royaume[posL][posC] is None:
        return 0, [(posL, posC)]
    cases_visitees = []
    nb_couronnes = couronnes_zone(royaume, posL, posC, cases_visitees, 0)
    return nb_couronnes * len(cases_visitees), cases_visitees
    pass

#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#ajoutDomino(royaume,cases_libres,(3,'F0','F0'),0,0,'left')
#ajoutDomino(royaume,cases_libres,(4,'F0','F0'),0,2,'top')
#ajoutDomino(royaume,cases_libres,(24,'F1','Y0'),1,0,'left')
#ajoutDomino(royaume,cases_libres,(25,'F1','Y0'),2,0,'top')
#ajoutDomino(royaume,cases_libres,(26,'F1','Y0'),0,3,'left')
#ajoutDomino(royaume,cases_libres,(5,'F0','F0'),1,3,'top')
#ajoutDomino(royaume,cases_libres,(27,'F1','Y0'),3,1,'bottom')
#afficher_royaume(royaume)
#print(score_zone(royaume,0,0))
#print(score_zone(royaume,3,1))
#print(score_zone(royaume,4,4))

def total_score(royaume):
    """La fonction total_score prend en argument un royaume. Elle n'a aucun effet de bord.
    Elle renvoie le score obtenu avec tout le royaume."""
    cases_comptabilisees = set()
    score_total = 0
    for i in range(len(royaume)):
        for j in range(len(royaume[i])):
            if (i, j) not in cases_comptabilisees and royaume[i][j] is not None:
                score, cases = score_zone(royaume, i, j)
                cases_comptabilisees.update(cases)
                score_total += score
    return score_total
    pass

#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#ajoutDomino(royaume,cases_libres,(3,'F0','F0'),0,0,'left')
#ajoutDomino(royaume,cases_libres,(4,'F0','F0'),0,2,'top')
#ajoutDomino(royaume,cases_libres,(24,'F1','Y0'),1,0,'left')
#ajoutDomino(royaume,cases_libres,(25,'F1','Y0'),2,0,'top')
#ajoutDomino(royaume,cases_libres,(26,'F1','Y0'),0,3,'left')
#ajoutDomino(royaume,cases_libres,(5,'F0','F0'),1,3,'top')
#ajoutDomino(royaume,cases_libres,(27,'F1','Y0'),3,1,'bottom')
#afficher_royaume(royaume)
#print(total_score(royaume))
#ajoutDomino(royaume,cases_libres,(19,'Y1','F0'),4,0,'left')
#ajoutDomino(royaume,cases_libres,(46,'S0','M2'),3,2,'top')
#ajoutDomino(royaume,cases_libres,(47,'S0','M2'),3,3,'top')
#ajoutDomino(royaume,cases_libres,(48,'Y0','M3'),3,4,'top')
#ajoutDomino(royaume,cases_libres,(23,'Y1','M0'),1,4,'top')
#afficher_royaume(royaume)
#print(total_score(royaume))

def jeu_complet(taille=7, nom_fichier = "dominos.csv", perso = False, affichage = True):
    """La fonction jeu_complet est la fonction principale du projet. Elle prend en argument
    la taille du royaume, le nom du fichier contenant les dominos (par défaut "dominos.csv"),
    un argument optionnel booléen perso (par défaut False) qui indique si les noms de joueurs
    sont personnalisés, en référence à la méthode init_tuple_joueurs.
    La fonction implémente une partie de KingDomino.
    Elle initialise d'abord toutes les structures de données (tuples, listes, dictionnaires).
    Elle implémente le premier tour où les deux joueurs choisissent leurs 2 premiers dominos.
    Ensuite, elle implémente les tours de jeu, jusqu'à ce que la liste des dominos (attention,
    le dernier tour, où les deux joueurs ne font que poser des dominos et où la pile de choix
    est vide,ne doit pas être oublié !).
    Elle termine en indiquant quel joueur est le vainqueur de la partie, avec les deux scores
    correspondants."""

    joueurs = ("A", "B") if not perso else init_tuple_joueurs()
    royaumes = init_tuple_royaumes(taille)
    cases_libres = init_tuple_libres(taille)
    dominos = init_dominos(taille, nom_fichier)
    dico_configurations = init_configurations(joueurs)
    
    if affichage:
        print(f"KINGDOMINO : joueur {joueurs[0]} vs joueur {joueurs[1]}\n")
    
    dico_depot, dico_choix = premier_tour(dominos, joueurs, dico_configurations)
    
    #Boucle principale du jeu
    while dico_choix:
        tour_de_jeu(royaumes, cases_libres, dominos, dico_depot, dico_choix, joueurs, dico_configurations)
    
    #Calcul des scores et affichage du gagnant
    score_A = total_score(royaumes[0])
    score_B = total_score(royaumes[1])
    gagnant = joueurs[0] if score_A > score_B else joueurs[1]
    
    if affichage:
        print("\n-----------------------------")
        print(f"Score final : {joueurs[0]} : {score_A} | {joueurs[1]} : {score_B}")
        print(f"Le gagnant est {gagnant} !")
        print("-----------------------------")
    
    return royaumes, cases_libres, dominos, dico_depot, dico_choix, joueurs, dico_configurations

def main():
    taille = 3
    jeu_complet(taille, nom_fichier="dominos.csv", perso=False, affichage=True)

main()