from B_gestion_dominos import *
from C_pile_dominos import *
from D_gestion_joueurs import *
import random

# Vide le dictionnaire de depôt et y transfère le contenu du dictionnaire de choix
def vide_et_transfere_depot(dico_depot,dico_choix):
    """La fonction vide_et_transfere_depot prend en argument les dictionnaires de depot et de choix.
    Elle ne renvoie rien. Elle commence par vider le dictionnaire de dépot.
    Ensuite, elle ajoute le contenu du dictionnaire de choix dans le dictionnaire de dépot."""
    dico_depot.clear()
    for key, value in dico_choix.items():
        dico_depot[key] = value[:]
    



#dico_depot = {1: [(10,'G0','G0'),"A"], 2: [(19,'Y1','F0'),"B"], 3: [(24,'F1','Y0'),"B"], 4:[(48,'Y0','M3'),"A"]}
#dico_choix = {1: [(1,'Y0','Y0'),None], 2: [(3,'F0','F0'),None], 3: [(4,'F0','F0'),None], 4:[(13,'Y0','F0'),None]}
#vide_et_transfere_depot(dico_depot,dico_choix)
#print(dico_depot)
#print(dico_choix)

def choix_pion(dico_choix,joueur,dico_configurations):
    """La fonction choix_pion prend en argument le dictionnaire de choix, un nom de joueur
    et le dictionnaire des configurations.
    Elle renvoie le domino disponible choisi par le joueur sur la pile de choix.
    Si le joueur est en configuration manuel, on lui demande de choisir un domino de dico_choix.
    Tant que son choix est invalide, on lui redemande.
    Si le joueur est en configuration random, on choisit au hasard un des dominos disponibles
    de dico_choix. Dans les deux cas, on ne modifie pas dico_choix, on renvoie juste l'entier choisi."""
    if dico_configurations.get(joueur) == 'm':
        while True:
            try:
                choix = int(input(f"{joueur}, choisissez un domino parmi {list(dico_choix.keys())}: "))
                if choix in dico_choix and dico_choix[choix][1] is None:
                    return choix
                print("Impossible !", end=" ")
            except ValueError:
                print("Entrée invalide.")
    else:
        choix = random.choice([key for key, value in dico_choix.items() if value[1] is None])
        print(f"{joueur} a choisi aléatoirement de poser son pion sur le domino {choix}")
        return choix

    pass

#dico_choix = {1: [(1,'Y0','Y0'),"Alex"], 2: [(3,'F0','F0'),None], 3: [(4,'F0','F0'),"Nadia"], 4:[(13,'Y0','F0'),None]}
#dico_configurations = {"Alex" : "m", "Nadia" : "r"}
#choix_pion(dico_choix,"Alex",dico_configurations)
#print(choix_pion(dico_choix,"Nadia",dico_configurations))

def pose_et_choix(royaume,cases_libres,dico_depot,dico_choix,dico_configurations,indice_depot):
    """La fonction pose_et_choix consiste à implémenter une action de jeu, c'est-à-dire
    la pose d'un domino suivie de la pose d'un pion sur la pile de choix.
    Elle prend en argument un royaume, ses cases libres,
    les dictionnaires de depot/choix/configurations, ainsi qu'un entier indice_depot
    correspondant à l'indice du domino dans la pile de depot que l'on va placer.
    Les fonctions pose_domino et choix_pion codées précedemment sont à utiliser.
    La fonction commence par afficher le royaume avant la pose du domino, puis implémente
    la pose du domino, affiche la pile de choix, demande au joueur de choisir où
    poser son pion sur la pile de choix (si elle est non vide),
    et enfin inscrit le nom du joueur sur cette pile."""
    joueur = dico_depot[indice_depot][1]
    domino = dico_depot[indice_depot][0]
    print(f"Royaume de {joueur} avant la pose du domino:")
    afficher_royaume(royaume, joueur)
    
    pose_domino(royaume, cases_libres, domino, dico_configurations, joueur)
    if dico_choix:
        afficher_choix_ou_depot(dico_choix)
        choix = choix_pion(dico_choix, joueur, dico_configurations)
        if choix in dico_choix:
            dico_choix[choix][1] = joueur
    pass

#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#ajoutDomino(royaume,cases_libres,(10,'G0','G0'),2,3,'left')
#ajoutDomino(royaume,cases_libres,(19,'Y1','F0'),3,2,'left')
#dico_depot = {1: [(10,'G0','G0'),"A"], 2: [(19,'Y1','F0'),"B"], 3: [(24,'F1','Y0'),"B"], 4:[(48,'Y0','M3'),"A"]}
#dico_choix = {1: [(1,'Y0','Y0'),None], 2: [(3,'F0','F0'),"A"], 3: [(4,'F0','F0'),"B"], 4:[(13,'Y0','F0'),None]}
#indice_depot = 3 #les deux premiers dominos de la file de dépot ont déjà été déposés
#dico_configurations = {"A":'m',"B":'r'}
#pose_et_choix(royaume,cases_libres,dico_depot,dico_choix,dico_configurations,indice_depot)
#print("Depot :")
#afficher_choix_ou_depot(dico_depot)
#print("Choix :")
#afficher_choix_ou_depot(dico_choix)

# Exécute un tour de jeu, incluant la pose de dominos et le choix des pions
def tour_de_jeu(tuple_royaumes,tuple_libres,liste_dominos,dico_depot,dico_choix,tuple_joueurs,dico_configurations):
    """La fonction tour_de_jeu prend en argument les différentes structures de données du jeu.
    Elle ne renvoie rien et modifie ces structures de données. Grâce aux fonctions codées
    précedemment, elle modélise un tour de jeu, c'est-à-dire la pose de 4 dominos (2 pour
    chaque joueur) dans l'ordre dans lequel les pions sont posées sur la pile de dépot. Aussi,
    elle implémente les choix des joueurs sur la pile de choix. On termine par transferer
    le contenu de la pile de choix dans la pile de depot. Le remplissage de la pile de choix
    avec des nouveaux dominos se fait lui au début du tour."""
    remplir_choix(liste_dominos, dico_choix)
    
    for indice_depot in sorted(dico_depot.keys()):
        joueur = dico_depot[indice_depot][1]
        if joueur == tuple_joueurs[0]:
            pose_et_choix(tuple_royaumes[0], tuple_libres[0], dico_depot, dico_choix, dico_configurations, indice_depot) 
        else:
            pose_et_choix(tuple_royaumes[1], tuple_libres[1], dico_depot, dico_choix, dico_configurations, indice_depot)
        
    vide_et_transfere_depot(dico_depot, dico_choix)
    

    pass

#tuple_royaumes = init_tuple_royaumes(5)
#tuple_joueurs = init_tuple_joueurs()
#tuple_libres = init_tuple_libres(5)
#liste_dominos = extraire_dominos("dominos.csv")
#dico_depot = {1: [(10,'G0','G0'),"A"], 2: [(19,'Y1','F0'),"B"], 3: [(24,'F1','Y0'),"B"], 4:[(48,'Y0','M3'),"A"]}
#dico_choix = {1: [(1,'Y0','Y0'),None], 2: [(3,'F0','F0'),None], 3: [(4,'F0','F0'),None], 4:[(13,'Y0','F0'),None]}
#dico_configurations = {"A":'m',"B":'r'}
#tour_de_jeu(tuple_royaumes,tuple_libres,liste_dominos,dico_depot,dico_choix,tuple_joueurs,dico_configurations)
#afficher_royaume(tuple_royaumes[0],"A")
#afficher_royaume(tuple_royaumes[1],"B")
#print("Depot :", dico_depot)
#print("Choix :", dico_choix)


#Gère le premier tour en déterminant l'ordre des joueurs et leurs premiers choix
def premier_tour(liste_dominos,tuple_joueurs,dico_configurations):
    """La fonction premier_tour prend en argument la liste des dominos restants à être
    traités, le tuple des joueurs et le dictionnaire des configurations. Elle renvoie
    le dictionnaire de dépot et le dictionnaire de choix obtenus à l'issue du tour préliminaire.
    Concrètement, la fonction choisit aléatoirement un joueur qui commence (disons "A").
    Le joueur A pose son pion sur un domino de son choix (le mode de choix est déterminé par
    le dictionnaire des configurations : manuel ou random). Ensuite, le joueur B choisit 2 dominos
    sur la pile de choix et enfin le joueur A sélectionne le domino restant. La fonction termine en
    transferant le contenu de la pile de choix dans la pile de depot, en préparation du
    prochain tour."""
    dico_depot = {}
    dico_choix = {}
    remplir_choix(liste_dominos, dico_choix)
    afficher_choix_ou_depot(dico_choix)
    joueur_A = random.choice(tuple_joueurs)
    joueur_B = tuple_joueurs[1] if tuple_joueurs[0] == joueur_A else tuple_joueurs[0]
    print(f"\nTirage au sort : le joueur {joueur_A} commence !\n")
    choix_A = choix_pion(dico_choix, joueur_A, dico_configurations)
    dico_choix[choix_A][1] = joueur_A
    for _ in range(2):
        choix_B = choix_pion(dico_choix, joueur_B, dico_configurations)
        dico_choix[choix_B][1] = joueur_B
    choix_A = choix_pion(dico_choix, joueur_A, dico_configurations)
    dico_choix[choix_A][1] = joueur_A
    vide_et_transfere_depot(dico_depot, dico_choix)
    return dico_depot, dico_choix
    pass

#liste_dominos = extraire_dominos("dominos.csv")
#tuple_joueurs = ("Yves-Jean","Alexandre")
#dico_configurations = {"Yves-Jean":"m","Alexandre":"r"}
#dico_depot, dico_choix = premier_tour(liste_dominos,tuple_joueurs,dico_configurations)
#print(dico_depot)
#print(dico_choix)
