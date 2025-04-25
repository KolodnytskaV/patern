from B_gestion_dominos import *
import random


#Donnée aux étudiants
def init_tuple_joueurs(perso = False):
    """La fonction init_tuple_joueurs prend un argument optionnel perso (fixé par défaut à False)
    Si perso est activé à True, la fonction demande à l'utilisateur de saisir deux noms
    de joueurs et les renvoie sous forme de tuples. Sinon, elle renvoie A,B."""
    nom_A = "A"
    nom_B = "B"
    if perso:
        nom_A = input("Nom du premier joueur : ")
        nom_B = input("Nom du second joueur : ")
    return nom_A,nom_B

#Initialisation des configurations de jeu pour chaque joueur
#Demande à chaque joueur le mode de jeu
def init_configurations(tuple_joueurs):
    dico_configurations = {}

    for joueur in tuple_joueurs:
        choix = ""
        while choix not in ['m', 'r']:
            choix = input(f"Mode de jeu pour  {joueur} ('m' pour manuel, 'r' pour random) : ").lower()
            if choix in ['m', 'r']:
                dico_configurations[joueur] = choix
            else: 
                print("Saisie incorrecte!")
    return dico_configurations  
    pass

print(init_configurations(("Alex","Bob")))


#Joueur place le domino manuellement
#Demande de saisir les coordonées et la direction pour poser un domino
def pose_domino_manuel(royaume,cases_libres,domino,joueur="A"):
    while True: 
        try: 
            posL = int(input("Entrez la ligne: "))
            posC = int(input("Entrez la colonne :"))
            direction = input("Entrez la direction (left, right, top, bottom) : ").lower()

            if espaceLibre(royaume, posL, posC, direction):
                ajoutDomino(royaume, cases_libres, domino, posL, posC, direction)
                print(f"Le domino {domino} a été ajouté avec succès.")
                afficher_royaume(royaume, joueur)
                return
            else: 
                print("Emplacement ou direction invalide, réessayez.")
        except ValueError:
            print("Entrée invalide! Veuillez entrer des nombres pour les coordonées")

    
    pass

#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#domino1 = (31,'B1','Y0')
#domino2 = (32,'B1','F0')
#domino3 = (25,'F1','Y0')
#ajoutDomino(royaume,cases_libres,domino1,2,3,'left')
#ajoutDomino(royaume,cases_libres,domino2,1,2,'bottom')
#ajoutDomino(royaume,cases_libres,domino3,0,1,'right')
#afficher_royaume(royaume,"Alice")
#pose_domino_manuel(royaume,cases_libres,domino1,"Alice")


#Pose un domino en manière random
#Choisi une case et une direction random pour poser un domino
def pose_domino_random(royaume,cases_libres,domino,joueur,TENTATIVES = 10000):
    print(f"{joueur}, placez le domino {domino} en mode random")
    directions = ['left', 'right', 'top', 'bottom']
    for _ in range(TENTATIVES):
        posL, posC = random.choice(cases_libres)
        direction = random.choice(directions)
        if espaceLibre(royaume, posL, posC, direction):
            ajoutDomino(royaume, cases_libres, domino, posL, posC, direction)
            print(joueur, " : le domino ", domino, " a bien été ajouté.")
            return
    print(f"Échec : Après {TENTATIVES} tentatives, le domino {domino} n'a pas pu être placé.")
    pass

#royaume = creer_royaume(5)
#cases_libres = init_cases_libres(5)
#domino = (3,'F0','F0')
#domino1 = (1,'Y0','Y0')
#domino2 = (13,'Y0','F0')
#ajoutDomino(royaume,cases_libres,domino,2,3,'left')
#ajoutDomino(royaume,cases_libres,domino,1,2,'bottom')
#ajoutDomino(royaume,cases_libres,domino,3,2,'top')
#ajoutDomino(royaume,cases_libres,domino,2,1,'right')
#afficher_royaume(royaume,"Bob")
#pose_domino_random(royaume,cases_libres,domino1,"Bob")
#pose_domino_random(royaume,cases_libres,domino2,"Bob")

#Donnée aux étudiants
def pose_domino(royaume,cases_libres,domino,dico_configurations,joueur):
    """La fonction pose_domino effectue la pose d'un domino, en fonction du dictionnaire
    des configurations. Elle fait simplement appel aux fonctions pose_domino_manuel
    et pose_domino_random déjà codées ci-dessus."""
    if domino_possible(royaume,cases_libres,domino):
        if dico_configurations[joueur] == 'm':
            pose_domino_manuel(royaume,cases_libres,domino,joueur)
        else:
            pose_domino_random(royaume,cases_libres,domino,joueur)
    else:
        print(f"Le domino {domino} ne peut pas être placé dans le royaume de {joueur}.")




