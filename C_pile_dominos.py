import random

def extraire_dominos(nom_fichier):
    """La fonction extraire_dominos prend en argument un nom de fichier
    et renvoie la liste mélangée des dominos donnée par ce fichier"""
    dominos = []
    with open(nom_fichier) as file:            
        for ligne in file:
            ligne = ligne.strip()
            elements = ligne.split(';')
            if len(elements) == 3: #vérification que la ligne contient bien 3 éléments
                numeros, valeur1, valeur2 = elements
                numeros = numeros.split('-')
                if len(numeros) == 2: 
                    debut, fin = map(int, numeros)
                    for num in range(debut, fin + 1):
                        dominos.append((num, valeur1, valeur2))
                else:  #quand il n'y a qu'un seul numéro
                    dominos.append((int(numeros[0]), valeur1, valeur2))
            
    random.shuffle(dominos) #Mélange des dominos
    return dominos

#Lecture et mélange des dominos depuis un fichier
l = extraire_dominos("dominos.csv")
print(l)
print(len(l))


#Trie une liste de tuples selon le premier élément en utilisant le tri par séléction
def tri_selection(liste):
    for i in range(len(liste)):
        min_index = i
        for j in range(i + 1, len(liste)):
            if liste[j][0] < liste[min_index][0]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i] #échange des éléments
    return liste


#Extrait les 4 premiers dominos d'une liste, sansmodifier la liste originale! Trie ensuite ces dominos et les renvoie
def extraire_premier_bloc(liste_dominos):
    bloc = liste_dominos[:4] # Extraction des 4 premiers dominos
    return tri_selection(bloc)


#liste_test = [(6, 'F0', 'F0'), (1, 'Y0', 'Y0'), (3, 'F0', 'F0'), (2, 'Y0', 'Y0'), (4, 'F0', 'F0'), (5, 'F0', 'F0'), (7, 'B0', 'B0')]
#first = extraire_premier_bloc(liste_test)
#print(first)
#print(len(liste_test))

def piocher_bloc(liste_dominos):
    """La fonction piocher_bloc prend en argument une liste de dominos.
    Elle renvoie le premier bloc de 4 dominos trié en ordre croissant par indice
    Elle modifie la liste passée en argument en supprimant ce premier bloc du début de la liste"""
    bloc = liste_dominos[:4] # Extraction des 4 premiers dominos
    del liste_dominos[:4]  # Suppression de ces dominos de la liste original
    return tri_selection(bloc)


def remplir_choix(liste_dominos, dico_choix):
    """La fonction remplir_choix prend en argument la liste de dominos restants à être posés
    ainsi que le dictionnaire de choix, dont les clés sont les entiers entre 1 et 4.
    La fonction ne renvoie rien. Elle réalise la pioche des 4 prochains dominos dans la liste
    puis les assigne dans l'ordre croissant aux indices allant de 1 à 4 dans dico_choix.
    La valeur dico_choix[i] pour tout i entre 1 et 4 est une liste contenant le domino correspondant
    suivi d'un élément None, sensé représenter le joueur qui a posé son pion sur le domino.
    Cette valeur None sera modifiée lorsqu'un joueur posera son pion sur le domino.
    Attention : si liste_dominos est vide, on vide dico_choix."""
    
    if not liste_dominos:
        dico_choix.clear()# On vide le dictionnaire si plus de dominos
        return
    
    # Vérifier qu'il y a au moins 4 dominos disponibles, sinon prendre ce qui reste
    bloc = liste_dominos[:4] if len(liste_dominos) >= 4 else liste_dominos[:]
    del liste_dominos[:len(bloc)]
    bloc_trie = tri_selection(bloc)
    # Remplissage du dictionnaire avec les dominos
    for i in range(1, len(bloc_trie) + 1):
        dico_choix[i] = [bloc_trie[i-1], None]


#liste_test = [(6, 'F0', 'F0'), (1, 'Y0', 'Y0'), (3, 'F0', 'F0'), (2, 'Y0', 'Y0'), (4, 'F0', 'F0'), (5, 'F0', 'F0'), (7, 'B0', 'B0')]
#dico_choix = {}
#remplir_choix(liste_test, dico_choix)
#print(dico_choix)
#print(liste_test)
#remplir_choix([], dico_choix)
#print(len(dico_choix))

#Donnée aux étudiants
def afficher_choix_ou_depot(dico):
    """La fonction afficher_choix_ou_depot prend en argument un dictionnaire (qui sera
    soit un dictionnaire de dépot ou un dictionnaire de choix). Elle ne renvoie rien.
    Elle affiche le dictionnaire de manière élégante."""
    if not dico:
        print("Dictionnaire vide.")
        return
    for i in range(1,5):
        print(i, "- Domino", dico[i][0], "Joueur", dico[i][1])

