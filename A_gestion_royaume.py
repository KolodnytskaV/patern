#Une fois que vous avez testé une fonction et voulez passer à la prochaine,
#pensez à recommenter le bloc de tests pour qu'il ne s'exécute plus après.
#En général, un Ctrl + / fait l'affaire pour commenter un bloc de code en Python

#crée un royaume sous forme de matrice (taille x taille). 
# La case centrale contient 'CH' représentant le château.
#La taille doit être un entier impair et positif.

def creer_royaume(taille = 7):
    if taille < 0 or taille % 2 == 0:
        return ValueError("Impossible de créer un royaume : 'taille' est pair ou négatif")
    royaume = [[None for _ in range(taille)] for _ in range(taille)]
    centre = taille//2
    royaume[centre][centre] = 'CH'
    return royaume
        

#royaume = creer_royaume(5)
#print(royaume)
#royaume[0][0] = 'Y1'
#print(royaume)
#print(creer_royaume())

#Initialise un tuple contenant deux royaumes indépendants de taille spécifiée
def init_tuple_royaumes(taille = 7):
    royaume1 = creer_royaume(taille)
    royaume2 = creer_royaume(taille)
    return royaume1, royaume2

#tup = init_tuple_royaumes(5)
#tup[0][0][0] = "Y0"
#print(tup[0])
#print(tup[1])

#Donné aux étudiants
#La fonction afficheCoordonnees prend en argument un royaume et affiche les coordonnées de chaque point du royaume. 
#Cette fonction ne sera jamais utilisée, elle est là pour vous aider à comprendre comment sont fixées les coordonnées
def afficherCoordonnees(royaume):
    n = len(royaume)
    for i in range(n):
        for j in range(n):
            print("|"+str((i,j)), end ="")
        print("|")

#royaume = creer_royaume(5)
#afficherCoordonnees(royaume)


#Retourne la liste des coordonées des cases libres d'un royaume de taille donnée
#La case centrale contenant le château est exclue
def init_cases_libres(taille):
    centre = taille//2
    return [(i,j) for i in range(taille) for j in range(taille) if (i, j) != (centre, centre)]
    
#print(init_cases_libres(3))


#Retourne un tuple contenant deux listes indépendantes des cases libres
def init_tuple_libres(taille):
    cases_libres = init_cases_libres(taille)
    return cases_libres[:], cases_libres[:]
    

#tup = init_tuple_libres(5)

#tup[0].remove((0,0))
#print(len(tup[0]))
#print(len(tup[1]))


#Affiche le royaume sous forme de grille avec indication du joueur
#Les cases vides sont représentées par la valeur de 'vide' par défaut deux espaces) 
def afficher_royaume(royaume, joueur = "A",vide = "  "):
    if not  royaume:
        return
    taille = len(royaume)
    bordure = "-" * (4 * taille + 1)

    print(bordure)
    print("Joueur", joueur)
    for i in range(taille):
        print(f'{i} ', end='')
        for j in range(taille):
            case = royaume[i][j] if royaume[i][j] else vide
            print(f'|{case}', end='')
        print('|')
    
    print(bordure)
    print(' ' + ' '.join(map(str, range(taille))))

#royaume = creer_royaume(5)
#royaume[1][0] = 'Y0'
#royaume[2][3] = 'B1'
#afficher_royaume(royaume)