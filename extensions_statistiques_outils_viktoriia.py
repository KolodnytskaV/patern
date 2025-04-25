def get_zones_infos(royaume): 
    taille = len(royaume)
    #on fait une matrice de booleens pour savoir si la case a été visitée ou non
    visite = [[False] * taille for _ in range(taille)]

    zones = []

    #on fait une fonction dfs pour explorer le royaume
    def dfs(i, j, couleur):
        stack = [(i, j)] # pile pour la DFS
        cases = [] # liste des cases de la zone
        couronnes = 0 # nombre de couronnes dans la zone

        while stack: 
            x, y = stack.pop()
            #verifier si la case est dans le royaume
            if not (0 <= x < taille and 0 <= y < taille):
                continue
            #verifier si la case a deja été visitée
            if visite[x][y]:
                continue

            case = royaume[x][y]

            #verifier si la case est vide ou si elle n'est pas de la bonne couleur ou si elle est le chateau
            if not case or case == "CH" or case[0] != couleur:
                continue

            #on marque la case comme visitée
            visite[x][y] = True
            cases.append((x,y))

            #on ajoute le nombre de couronnes de la case
            couronnes += int(case[1])

            #on ajoute les cases voisines à la pile : haut, bas, gauche, droite
            stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

        #on retourne les infos de la zone actuelle
        return {"taille": len(cases), "couronnes": couronnes, "cases": cases}

    #parcours de toutes les cases du royaume 
    for i in range(taille):
        for j in range(taille):
            case = royaume[i][j]
            #si la case n'est pas vide et n'est pas le chateau et n'a pas été visitée
            if case and case != "CH" and not visite[i][j]:
                zones.append(dfs(i, j, case[0]))
    #on retourne la liste coplète des zones trouvées
    return zones
