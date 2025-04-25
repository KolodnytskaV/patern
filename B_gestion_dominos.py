from A_gestion_royaume import *


#Détermine la position de la deuxième partie du domino en fonction de la direction
def partie_droite_domino(posL,posC,direction): 
    directions = {"top": (1, 0), "bottom": (-1, 0), "left": (0, 1), "right": (0, -1)}
    return (posL + directions[direction][0], posC + directions[direction][1]) if direction in directions else None

#print(partie_droite_domino(12,-3,'left'))
#print(partie_droite_domino(5,5,'bottom'))


#Vérifie si un espace est libre pour placer un domino
def espaceLibre(royaume,posL,posC,direction):
    if direction not in ("left", "right", "top", "bottom"):
        return False
    rows = len(royaume)
    cols = len(royaume[0])
    posL2, posC2 = partie_droite_domino(posL, posC, direction) 
    #Pour voir si la position initiale est dans les limites
    if not (0 <= posL < rows and 0 <= posC < cols and 0 <= posL2 < rows and 0 <= posC2 < cols):
        return False
    return royaume[posL][posC] is None and royaume[posL2][posC2] is None

#royaume = creer_royaume(5)
#royaume[0][0] = 'Y0'
#royaume[0][1] = 'F0'
#royaume[1][0] = 'M2'
#royaume[1][1] = 'B1'
#afficher_royaume(royaume)
#print(espaceLibre(royaume,0,0,"left"))
#print(espaceLibre(royaume,0,1,"left"))
#print(espaceLibre(royaume,5,1,"bottom"))
#print(espaceLibre(royaume,1,4,"left"))
#print(espaceLibre(royaume,4,2,"top"))
#print(espaceLibre(royaume,2,3,"right"))
#print(espaceLibre(royaume,2,3,"xyz"))
#print(espaceLibre(royaume,2,3,"left"))
#print(espaceLibre(royaume,0,2,"left"))
#print(espaceLibre(royaume,4,4,"right"))
#print(espaceLibre(royaume,4,4,"bottom"))


#Ajoute un domino au royaume si l'espace est libre
def ajoutDomino(royaume,cases_libres,domino,posL,posC,direction):
    
    # Vérifier si l'espace est libre pour placer le domino
    if espaceLibre(royaume, posL, posC, direction):
        # Déterminer les coordonnées de la case droite du domino
        posL2, posC2 = partie_droite_domino(posL, posC, direction)
        
        # Placer le domino dans le royaume
        royaume[posL][posC] = domino[1]
        royaume[posL2][posC2] = domino[2]
        
        cases_libres.remove((posL, posC))
        cases_libres.remove((posL2, posC2))

    else:
        print(f"Le domino {domino} ne peut pas être ajouté à l'emplacement {(posL, posC)} dans la direction {direction}")

#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#domino1 = (31,'B1','Y0')
#domino2 = (32,'B1','F0')
#domino3 = (25,'F1','Y0')
#ajoutDomino(royaume,cases_libres,domino1,2,3,'left')
#ajoutDomino(royaume,cases_libres,domino2,1,4,'left')
#ajoutDomino(royaume,cases_libres,domino1,3,3,'bottom')
#ajoutDomino(royaume,cases_libres,domino3,1,2,'bottom')
#ajoutDomino(royaume,cases_libres,domino3,0,0,'right')
#ajoutDomino(royaume,cases_libres,domino3,2,1,'xyz')
#print(espaceLibre(royaume,2,1,'left'))
#print(espaceLibre(royaume,2,1,'right'))
#afficher_royaume(royaume)
#print(len(cases_libres))


#Trouve les cases voisines d'ine position donnée
def voisinages(royaume,posL,posC, libres = False):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    voisins = [(posL + dL, posC + dC) for dL, dC in directions if 0 <= posL + dL  < len(royaume) and 0 <= posC + dC < len(royaume)]
    
    
    return [v for v in voisins if not libres or royaume[v[0]][v[1]] is None]



#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#domino1 = (31,'B1','Y0')
#ajoutDomino(royaume,cases_libres,domino1,2,3,'left')
#afficher_royaume(royaume)
#print(voisinages(royaume,2,1))
#print(voisinages(royaume,0,1))
#print(voisinages(royaume,1,3))
#print(voisinages(royaume,1,3,True))


#Vérifie si un domino peut être placé selon les règles du jeu
def domino_valide(royaume,domino,posL,posC,direction):
    if not espaceLibre(royaume, posL, posC, direction):
        return False
    posL2, posC2 = partie_droite_domino(posL, posC, direction)
    couleur1, couleur2 = domino[1][0], domino[2][0]
    voisins_1 = voisinages(royaume, posL, posC)
    voisins_2 = voisinages(royaume, posL2, posC2)

    for voisinL, voisinC in voisins_1:
        if royaume[voisinL][voisinC] =='CH':
            return True
        elif royaume[voisinL][voisinC] is not None and royaume[voisinL][voisinC][0] == couleur1:
            return True
        
    for voisinL, voisinC in voisins_2:
        if royaume[voisinL][voisinC] =='CH':
            return True
        elif royaume[voisinL][voisinC] is not None and royaume[voisinL][voisinC][0] == couleur2:
            return True

    return False
    


#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#domino1 = (31,'B1','Y0')
#domino2 = (32,'B1','F0')
#domino3 = (25,'F1','Y0')
#domino4 = (1,'Y0','Y0')
#ajoutDomino(royaume,cases_libres,domino1,2,3,'left')
#ajoutDomino(royaume,cases_libres,domino3,1,2,'bottom')
#afficher_royaume(royaume)
#print(domino_valide(royaume,domino4,2,1,'right'))
#print(domino_valide(royaume,domino4,0,0,'left'))
#print(domino_valide(royaume,domino4,0,0,'right'))
#print(domino_valide(royaume,domino2,0,0,'left'))
#print(domino_valide(royaume,domino3,0,1,'right'))


#Vérifie si un domino peut être placé quelque part dans le royaume
def domino_possible(royaume,cases_libres,domino):
    for posL, posC in cases_libres:
        for direction in ["left", "right", "top", "bottom"]:
            if domino_valide(royaume, domino, posL, posC, direction):
                return True
    return False

#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#domino = (3,'F0','F0')
#domino1 = (1,'Y0','Y0')
#domino2 = (13,'Y0','F0')
#ajoutDomino(royaume,cases_libres,domino,2,3,'left')
#ajoutDomino(royaume,cases_libres,domino,1,2,'bottom')
#ajoutDomino(royaume,cases_libres,domino,3,2,'top')
#ajoutDomino(royaume,cases_libres,domino,2,1,'right')
#print(domino_possible(royaume,cases_libres,domino1))
#print(domino_possible(royaume,cases_libres,domino2))
#afficher_royaume(royaume)
