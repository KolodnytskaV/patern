from  F_jeu_complet_extensions import jeu_complet, total_score
from A_gestion_royaume import afficher_royaume
from extensions_statistiques_outils_viktoriia import get_zones_infos 

#fonction pour afficher les statistiques d'un royaume
def afficher_statistiques(royaume, joueur): 
    #on récupère les zones du royaume
    zones = get_zones_infos(royaume)
    #calcul du nombre de zones
    nb_zones = len(zones)
    #estimation du nombre de dominos(chaque domino = 2 cases)
    total_dominos = sum(len(zone["cases"]) // 2 for zone in zones)
    #score total du joueur
    total_score_joueur = sum(zone["taille"] * zone["couronnes"] for zone in zones)
    #score de la zone la plus rentable
    score_max_zone = max(zone["taille"] * zone["couronnes"] for zone in zones)  if zones else 0
    #total de couronnes dans le royaume
    couronnes_totales = sum(zone["couronnes"] for zone in zones)
    #moyenne de couronnes par domino
    couronnes_par_domino = couronnes_totales / total_dominos if total_dominos > 0 else 0

    print("Statistiques pour jooueur :", joueur)
    print("Nombre de zones : ", nb_zones)
    print("Dominos posés estimés : ", total_dominos)
    print("Score final : ", total_score_joueur)
    print("Moyenne couronnes/domino : ", couronnes_par_domino)
    print("Zone la plus rentable : ", score_max_zone) 

def main(): 
    print("Lancement d'une partie complète pour générer les statistiques")

    royaumes, _, _, _, _, joueurs, _ = jeu_complet(affichage=False)

    #pour chaque joueur afficher le royaume et les statistiques
    for i in range(2):
        joueur = joueurs[i]
        royaume = royaumes[i]
        print("-" * 50)
        afficher_royaume(royaume, joueur)
        afficher_statistiques(royaume, joueur)

if __name__ == "__main__":
    main()